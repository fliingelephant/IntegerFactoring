"""Structural audit of the fresh F04 reconstruction artifacts."""

import argparse
import csv
import hashlib
import json
from pathlib import Path


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", type=Path)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    summary = json.loads((run_dir / "summary.json").read_text())

    assert summary["status_label"] == "self-audited"
    assert summary["finite_claim_result"] == "confirmed"
    assert summary["total_local_coefficients_exhausted"] == 17_375_452
    assert summary["total_local_zero_count"] == 0

    family_audits = {}
    for key, filename in [
        ("local_mod_p", "local_coefficients_mod_p.jsonl"),
        ("local_mod_q", "local_coefficients_mod_q.jsonl"),
    ]:
        family = summary[key]
        path = run_dir / filename
        rows = [json.loads(line) for line in path.read_text().splitlines()]
        assert [row["a"] for row in rows] == list(range(1, 2943))
        assert all(row["coefficient_count"] == 2953 for row in rows)
        assert all(row["zero_count"] == 0 for row in rows)
        assert all(row["product_mod_prime"] != 0 for row in rows)
        assert all(row["minimum_least_residue"] > 0 for row in rows)
        assert sha256(path) == family["row_file_sha256"]
        zero_path = run_dir / ("local_zeros_mod_p.jsonl" if key == "local_mod_p" else "local_zeros_mod_q.jsonl")
        assert zero_path.stat().st_size == 0
        family_audits[key] = {
            "rows": len(rows),
            "coefficient_count": sum(row["coefficient_count"] for row in rows),
            "row_file_sha256": sha256(path),
            "all_row_products_nonzero": True,
            "zero_file_empty": True,
        }

    order_path = run_dir / "orders_2_through_2953.csv"
    with order_path.open(newline="") as handle:
        order_rows = list(csv.DictReader(handle))
    assert [int(row["candidate_r"]) for row in order_rows] == list(range(2, 2954))
    passers = [int(row["candidate_r"]) for row in order_rows if row["order_exceeds_log2N_squared"] == "1"]
    assert passers == [2953]
    assert sha256(order_path) == summary["minimal_r_exhaustion"]["sha256"]

    result = {
        "status": "artifact_audit_passed",
        "run_dir": str(run_dir),
        "families": family_audits,
        "order_rows": len(order_rows),
        "order_passers": passers,
        "order_file_sha256": sha256(order_path),
        "summary_sha256": sha256(run_dir / "summary.json"),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
