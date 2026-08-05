#!/usr/bin/env python3
"""Independent structural and arithmetic audit for F04 full-column scan."""

import argparse
import csv
import hashlib
import json
import math
import struct
from pathlib import Path

N = 20000000499999937
P = 100000007
Q = 199999991
A = 2942
R = 2953
EXTRA = 11
GLOBAL_HEADER = struct.Struct("<8sIIIIIQQQQ")
C_HEADER = struct.Struct("<8sIIIQ")


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_c(path: Path, prime: int) -> list[tuple[int, ...]]:
    with path.open("rb") as stream:
        header = C_HEADER.unpack(stream.read(C_HEADER.size))
        if header != (b"F04CMAT1", 1, A, EXTRA, prime):
            raise SystemExit(f"bad C header in {path}: {header!r}")
        row = struct.Struct(f"<{EXTRA}Q")
        matrix = [row.unpack(stream.read(row.size)) for _ in range(A)]
        if stream.read(1):
            raise SystemExit(f"trailing bytes in {path}")
    if any(value >= prime for values in matrix for value in values):
        raise SystemExit(f"noncanonical C entry in {path}")
    return matrix


def crt(xp: int, xq: int) -> int:
    return xp + P * (((xq - xp) * pow(P, -1, Q)) % Q)


def sign_for(removed: list[int]) -> int:
    exponent = sum(i + 1 for i in removed)
    exponent += sum(range(A - len(removed) + 1, A + 1))
    return -1 if exponent % 2 else 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    root = Path(args.root).resolve()
    summary = json.loads((root / "outputs/summary.json").read_text())
    if summary["status"] != "pass" or not summary["global_rows_formed_directly_modulo_N"]:
        raise SystemExit("bad summary status")
    if summary["entry_statuses"] != A * EXTRA:
        raise SystemExit("entry count mismatch")
    expected_minors = math.comb(A, 2) * math.comb(EXTRA, 2)
    if summary["two_by_two_statuses"] != expected_minors:
        raise SystemExit("minor count mismatch")
    if summary["delta_p"] == 0 or summary["delta_q"] == 0:
        raise SystemExit("base determinant unexpectedly zero")
    if summary["delta_global"] != crt(summary["delta_p"], summary["delta_q"]):
        raise SystemExit("base determinant CRT mismatch")
    if math.gcd(summary["delta_global"], N) != 1:
        raise SystemExit("base determinant is not a global unit")

    global_path = root / "outputs/global_matrix.bin"
    expected_global_size = GLOBAL_HEADER.size + A * (4 + 8 * R)
    if global_path.stat().st_size != expected_global_size:
        raise SystemExit("global file size mismatch")
    canonical_entries = 0
    with global_path.open("rb") as stream:
        header = GLOBAL_HEADER.unpack(stream.read(GLOBAL_HEADER.size))
        expected_header = (b"F04FCM01", 1, A, R, 1, A, N, P, Q, A * R)
        if header != expected_header:
            raise SystemExit(f"global header mismatch: {header!r}")
        row = struct.Struct(f"<{R}Q")
        for shift in range(1, A + 1):
            if struct.unpack("<I", stream.read(4))[0] != shift:
                raise SystemExit("global shift order mismatch")
            values = row.unpack(stream.read(row.size))
            if any(value >= N for value in values):
                raise SystemExit(f"noncanonical global row {shift}")
            canonical_entries += R
        if stream.read(1):
            raise SystemExit("trailing global bytes")

    cp = load_c(root / "outputs/C_p.bin", P)
    cq = load_c(root / "outputs/C_q.bin", Q)
    entry_union = []
    zero_p = zero_q = mismatch = 0
    for i in range(A):
        for j in range(EXTRA):
            vp, vq = cp[i][j], cq[i][j]
            zero_p += vp == 0
            zero_q += vq == 0
            mismatch += (vp == 0) != (vq == 0)
            if vp == 0 or vq == 0:
                entry_union.append((i, j, vp, vq, int(vp == 0), int(vq == 0)))
    with (root / "outputs/entry_zeros.csv").open(newline="") as stream:
        rows = [tuple(map(int, (r["base_row"], r["extra_column"], r["p_value"],
                                    r["q_value"], r["p_zero"], r["q_zero"])))
                for r in csv.DictReader(stream)]
    if rows != entry_union or (zero_p, zero_q, mismatch) != (
        summary["entry_zero_p"], summary["entry_zero_q"], summary["entry_zero_mismatches"]
    ):
        raise SystemExit("entry zero-pattern mismatch")

    minor_rows = []
    with (root / "outputs/two_by_two_zeros.csv").open(newline="") as stream:
        for row in csv.DictReader(stream):
            values = tuple(int(row[name]) for name in (
                "base_row_1", "base_row_2", "extra_column_1", "extra_column_2",
                "p_value", "q_value", "p_zero", "q_zero"))
            i1, i2, j1, j2, vp, vq, zp, zq = values
            actual_p = (cp[i1][j1] * cp[i2][j2] - cp[i1][j2] * cp[i2][j1]) % P
            actual_q = (cq[i1][j1] * cq[i2][j2] - cq[i1][j2] * cq[i2][j1]) % Q
            if (vp, vq, zp, zq) != (actual_p, actual_q, int(actual_p == 0), int(actual_q == 0)):
                raise SystemExit(f"bad retained minor record {values}")
            minor_rows.append(values)
    if minor_rows != sorted(minor_rows, key=lambda x: x[:4]):
        raise SystemExit("minor records are not in canonical order")
    if sum(row[6] for row in minor_rows) != summary["two_by_two_zero_p"] or \
            sum(row[7] for row in minor_rows) != summary["two_by_two_zero_q"] or \
            sum(row[6] != row[7] for row in minor_rows) != summary["two_by_two_zero_mismatches"]:
        raise SystemExit("retained minor zero counts disagree with summary")

    if summary["certificate_present"]:
        order = summary["certificate_order"]
        removed = [summary["certificate_i1"]]
        if order == 2:
            removed.append(summary["certificate_i2"])
        sign = sign_for(removed)
        if sign != summary["certificate_sign"]:
            raise SystemExit("certificate sign mismatch")
        fp = sign * summary["delta_p"] * summary["certificate_quotient_p"] % P
        fq = sign * summary["delta_q"] * summary["certificate_quotient_q"] % Q
        if fp != summary["certificate_formula_p"] or fq != summary["certificate_formula_q"]:
            raise SystemExit("certificate quotient formula mismatch")
        if fp != summary["certificate_direct_p"] or fq != summary["certificate_direct_q"]:
            raise SystemExit("direct determinant and quotient formula disagree")
        global_value = crt(fp, fq)
        if global_value != summary["certificate_global_value"] or \
                math.gcd(global_value, N) != summary["certificate_gcd_N"] or \
                summary["certificate_gcd_N"] not in (P, Q):
            raise SystemExit("global exchange certificate mismatch")

    manifest = {}
    for line in (root / "manifests/run_001.primary_outputs.sha256").read_text().splitlines():
        value, name = line.split(maxsplit=1)
        manifest[name.strip()] = value
    for relative in ("outputs/global_matrix.bin", "outputs/C_p.bin", "outputs/C_q.bin",
                     "outputs/entry_zeros.csv", "outputs/two_by_two_zeros.csv", "outputs/summary.json"):
        if manifest.get(relative) != digest(root / relative):
            raise SystemExit(f"hash mismatch for {relative}")

    result = {
        "status": "pass",
        "canonical_global_entries_parsed": canonical_entries,
        "entry_statuses_recomputed": A * EXTRA,
        "retained_zero_2x2_records_recomputed": len(minor_rows),
        "two_by_two_family_size_reconciled": expected_minors,
        "certificate_recomputed": bool(summary["certificate_present"]),
        "global_matrix_sha256": digest(global_path),
        "C_p_sha256": digest(root / "outputs/C_p.bin"),
        "C_q_sha256": digest(root / "outputs/C_q.bin"),
    }
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()

