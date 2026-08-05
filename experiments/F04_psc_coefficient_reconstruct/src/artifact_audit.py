#!/usr/bin/env python3
"""Independent parser and consistency audit of the completed F04 artifacts."""

import argparse
import csv
import hashlib
import json
import struct
from pathlib import Path

N = 20000000499999937
P = 100000007
Q = 199999991
R = 2953
FIRST = 1
LAST = 2942
COUNT = LAST - FIRST + 1
HEADER = struct.Struct("<8sIIIIQQQQ")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_sha_manifest(path: Path) -> dict[str, str]:
    entries = {}
    for line in path.read_text().splitlines():
        digest, name = line.split(maxsplit=1)
        entries[name.lstrip("* ")] = digest
    return entries


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    root = Path(args.root).resolve()
    binary = root / "outputs/global_vectors.bin"
    expected_size = HEADER.size + COUNT * (4 + 8 * R)
    if binary.stat().st_size != expected_size:
        raise SystemExit(f"binary size mismatch: {binary.stat().st_size} != {expected_size}")

    nonunits = 0
    top_failures = 0
    coefficients = 0
    with binary.open("rb") as stream:
        header = HEADER.unpack(stream.read(HEADER.size))
        expected_header = (b"F04GLOB1", 1, R, FIRST, LAST, N, P, Q, COUNT * R)
        if header != expected_header:
            raise SystemExit(f"header mismatch: {header!r}")
        unpack_coefficients = struct.Struct(f"<{R}Q")
        for expected_shift in range(FIRST, LAST + 1):
            shift = struct.unpack("<I", stream.read(4))[0]
            if shift != expected_shift:
                raise SystemExit(f"shift mismatch: {shift} != {expected_shift}")
            vector = unpack_coefficients.unpack(stream.read(8 * R))
            if any(value >= N for value in vector):
                raise SystemExit(f"noncanonical coefficient at shift {shift}")
            nonunits += sum(value % P == 0 or value % Q == 0 for value in vector)
            top_failures += vector[-1] == 0
            coefficients += len(vector)
        if stream.read(1):
            raise SystemExit("trailing data")

    generator = json.loads((root / "outputs/generator_summary.json").read_text())
    verifier = json.loads((root / "outputs/verifier_summary.json").read_text())
    theorem = json.loads((root / "outputs/theorem_exhaustive.json").read_text())
    spot = json.loads((root / "outputs/spot_audit.json").read_text())
    if generator["status"] != "pass" or generator["coefficient_count"] != COUNT * R:
        raise SystemExit("generator summary mismatch")
    if verifier["status"] != "pass" or verifier["total_nonzero_D_statuses"] != 2 * COUNT * R:
        raise SystemExit("verifier summary mismatch")
    if theorem["status"] != "pass" or spot["status"] != "pass":
        raise SystemExit("theorem/spot audit did not pass")

    rows = 0
    with (root / "outputs/per_shift.csv").open(newline="") as stream:
        for row in csv.DictReader(stream):
            rows += 1
            if row["nonunits"] != "0" or row["global_top_nonzero"] != "1" or \
                    row["p_top_nonzero"] != "1" or row["q_top_nonzero"] != "1" or \
                    row["p_chain"] != "pass" or row["q_chain"] != "pass":
                raise SystemExit(f"bad per-shift row: {row}")
    if rows != COUNT:
        raise SystemExit(f"per-shift row count mismatch: {rows}")

    manifest_path = root / "manifests/run_001.outputs.sha256"
    manifest = parse_sha_manifest(manifest_path)
    relative_binary = "outputs/global_vectors.bin"
    if manifest.get(relative_binary) != sha256(binary):
        raise SystemExit("global binary digest mismatch")

    if nonunits or top_failures or coefficients != COUNT * R:
        raise SystemExit("independent coefficient scan failed")
    result = {
        "status": "pass",
        "binary_size_bytes": expected_size,
        "binary_sha256": sha256(binary),
        "coefficients_independently_parsed": coefficients,
        "nonunit_coefficients": nonunits,
        "global_top_failures": top_failures,
        "per_shift_rows_checked": rows,
        "nonzero_D_statuses_reconciled": 2 * COUNT * R,
    }
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()

