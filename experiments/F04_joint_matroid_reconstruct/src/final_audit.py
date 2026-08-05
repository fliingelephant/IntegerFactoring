#!/usr/bin/env python3
"""Cross-check independent computations and inventory all retained provenance."""

import hashlib
import json
import math
import os
from pathlib import Path


root = Path(__file__).resolve().parents[1]
run_dir = Path(os.environ["F04_RECONSTRUCT_RUN_DIR"])


def load(relative):
    return json.loads((root / relative).read_text(encoding="utf-8"))


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def crt_pair(x, p, y, q):
    return (x + p * ((y - x) * pow(p, -1, q) % q)) % (p * q)


def trial_division_prime(n):
    if n % 2 == 0:
        return n == 2
    for divisor in range(3, math.isqrt(n) + 1, 2):
        if n % divisor == 0:
            return False
    return True


p14_global = load("runs/004_generate_P14_global/global_matrix.json")
p11_global = load("runs/005_generate_P11_global/global_matrix.json")
p14_local = load("runs/006_analyze_P14_local/local_analysis.json")
p14_audit = load("runs/017_independent_audit_P14/p14_independent_audit.json")
p11_local = load("runs/010_analyze_P11_flint/local_analysis_flint.json")
p11_direct = load("runs/016_direct_audit_P11/direct_audit.json")
p11_all_rows = load("runs/022_audit_all_P11_global_rows/all_global_rows_audit.json")
tail_scan = load("runs/014_scan_tail_minors_examples/tail_minor_scan.json")
exchange_blocks = load("runs/019_extract_exchange_block/exchange_blocks.json")

p14_matrix = root / "runs/004_generate_P14_global/global_matrix_u64le.bin"
p11_matrix = root / "runs/005_generate_P11_global/global_matrix_u64le.bin"
assert sha256(p14_matrix) == p14_global["sha256"] == p14_audit["global_matrix_sha256"]
assert sha256(p11_matrix) == p11_global["sha256"]
assert p11_all_rows == {
    "schema": 1,
    "N": 20000000499999937,
    "r": 2953,
    "A": 2942,
    "entries_compared": 8687726,
    "mismatches": 0,
    "all_match": True,
    "elapsed_seconds": p11_all_rows["elapsed_seconds"],
    "factor_inputs": [],
}
assert p14_audit["formula_matches_every_entry"] == {"271": True, "293": True}
assert p14_audit["local"] == {
    "271": {"base_determinant": 0, "base_rank": 23, "full_rank": 23},
    "293": {"base_determinant": 30, "base_rank": 266, "full_rank": 266},
}
assert p14_local["base_determinant_crt"] == crt_pair(0, 271, 30, 293) == 71815
assert p14_local["base_determinant_gcd_N"] == math.gcd(71815, 79403) == 271

assert p11_local["base_determinants"] == {
    "100000007": 56136614,
    "199999991": 132391112,
}
assert p11_direct["direct_base_determinants"] == p11_local["base_determinants"]
assert p11_direct["direct_exchanged_determinants"] == {
    "100000007": 15564403,
    "199999991": 0,
}
assert all(item["matches"] for item in p11_direct["sampled_global_rows"])

p, q = 100000007, 199999991
assert p * q == 20000000499999937
assert p11_local["base_determinant_crt"] == (
    crt_pair(56136614, p, 132391112, q)
) == 16315256998204520
assert math.gcd(p11_local["base_determinant_crt"], p * q) == 1
assert p11_local["exchanged_determinant_crt"] == (
    crt_pair(15564403, p, 0, q)
) == 2473353088699106
assert math.gcd(p11_local["exchanged_determinant_crt"], p * q) == q

for prime in (p, q):
    item = exchange_blocks[str(prime)]
    block = item["block"]
    determinant = (
        block[0][0] * block[1][1] - block[0][1] * block[1][0]
    ) % prime
    assert determinant == item["determinant"]
assert exchange_blocks[str(p)]["determinant"] == 67899852
assert exchange_blocks[str(q)]["determinant"] == 0
assert 3122 % 2 == 0
assert 56136614 * 67899852 % p == 15564403

assert tail_scan["one_tail"] == {
    "total": 2942 * 11,
    "p_basis": 2942 * 11,
    "q_basis": 2942 * 11,
    "both_basis": 2942 * 11,
    "p_only": 0,
    "q_only": 0,
    "neither": 0,
}
two_total = math.comb(2942, 2) * math.comb(11, 2)
assert tail_scan["two_tail"]["total"] == two_total == 237941605
assert tail_scan["two_tail"] == {
    "total": two_total,
    "p_basis": two_total,
    "q_basis": two_total - 2,
    "both_basis": two_total - 2,
    "p_only": 2,
    "q_only": 0,
    "neither": 0,
}
assert tail_scan["p_only_two_tail_examples"] == [
    {"removed": [423, 2336], "tail_offsets": [2, 6]},
    {"removed": [1618, 1874], "tail_offsets": [3, 10]},
]

prime_checks = {
    str(value): trial_division_prime(value)
    for value in (271, 293, p, q)
}
assert all(prime_checks.values())

run_statuses = {}
for path in sorted((root / "runs").glob("*/manifest.json")):
    manifest = json.loads(path.read_text(encoding="utf-8"))
    run_statuses[path.parent.name] = {
        "return_code": manifest["return_code"],
        "timed_out": manifest.get("timed_out", False),
        "interrupted": manifest.get("interrupted", False),
        "manifest_sha256": sha256(path),
    }
assert run_statuses["001_benchmark_global_row"]["return_code"] == 1
assert run_statuses["002_benchmark_global_row"]["return_code"] == 1
assert run_statuses["007_analyze_P11_local"]["interrupted"]
for name, status in run_statuses.items():
    if name not in {
        "001_benchmark_global_row",
        "002_benchmark_global_row",
        "007_analyze_P11_local",
    }:
        assert status["return_code"] == 0

audit = {
    "schema": 1,
    "status": "all assertions passed",
    "prime_checks_by_trial_division": prime_checks,
    "global_matrix_sha256": {
        "P14": p14_global["sha256"],
        "P11": p11_global["sha256"],
    },
    "P14": {
        "local_ranks": [23, 266],
        "base_determinants": [0, 30],
        "base_crt": 71815,
        "base_gcd_N": 271,
    },
    "P11": {
        "base_determinants": [56136614, 132391112],
        "base_crt": 16315256998204520,
        "base_gcd_N": 1,
        "exchanged_determinants": [15564403, 0],
        "exchanged_crt": 2473353088699106,
        "exchanged_gcd_N": 199999991,
        "one_tail_candidates": 32362,
        "two_tail_candidates": 237941605,
        "two_tail_p_only": 2,
        "independently_recomputed_global_entries": 8687726,
    },
    "retained_run_statuses": run_statuses,
}
(run_dir / "final_audit.json").write_text(
    json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)

inventory = {}
for directory in ("src", "artifacts"):
    for path in sorted((root / directory).glob("*")):
        if path.is_file():
            inventory[str(path.relative_to(root))] = {
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
report_path = root / "REPORT.md"
inventory["REPORT.md"] = {
    "bytes": report_path.stat().st_size,
    "sha256": sha256(report_path),
}
for relative in (
    "runs/004_generate_P14_global/global_matrix.json",
    "runs/004_generate_P14_global/global_matrix_u64le.bin",
    "runs/005_generate_P11_global/global_matrix.json",
    "runs/005_generate_P11_global/global_matrix_u64le.bin",
    "runs/006_analyze_P14_local/local_analysis.json",
    "runs/010_analyze_P11_flint/local_analysis_flint.json",
    "runs/014_scan_tail_minors_examples/tail_minor_scan.json",
    "runs/016_direct_audit_P11/direct_audit.json",
    "runs/017_independent_audit_P14/p14_independent_audit.json",
    "runs/019_extract_exchange_block/exchange_blocks.json",
    "runs/022_audit_all_P11_global_rows/all_global_rows_audit.json",
    "runs/024_capture_toolchain/stdout.log",
):
    path = root / relative
    inventory[relative] = {"bytes": path.stat().st_size, "sha256": sha256(path)}
(run_dir / "provenance_inventory.json").write_text(
    json.dumps(inventory, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(audit, sort_keys=True))
