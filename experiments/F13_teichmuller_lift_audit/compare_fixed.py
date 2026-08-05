#!/usr/bin/env python3
"""Byte-addressed comparison of independent A02 probes to author R01."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--author", required=True)
    parser.add_argument("--audit", required=True)
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()

    author_path = Path(arguments.author)
    audit_path = Path(arguments.audit)
    author = json.loads(author_path.read_text())
    audit = json.loads(audit_path.read_text())
    comparisons = []
    for author_record, audit_record in zip(author["instances"], audit["records"], strict=True):
        fixed = author_record["fixed_small_probes"]
        fields = {
            "bases": fixed["bases_tested"] == audit_record["bases"],
            "pairs": fixed["additive_pairs_tested"] == audit_record["pairs"],
            "rounded_exponent": fixed["ceil_2_sqrt_N"] == audit_record["ceil_2_sqrt_N"],
            "true_sum": fixed["true_p_plus_q"] == audit_record["p_plus_q"],
            "additive_first_20": fixed["additive_two_stage_factor_hits"]
            == audit_record["additive_hits"][:20],
            "iterated_first_20": fixed["iterated_difference_factor_hits"]
            == audit_record["iterated_hits"][:20],
            "high_digit_first_20": fixed["high_digit_factor_hits"]
            == audit_record["high_digit_hits"][:20],
            "rounded_first_20": fixed["rounded_exponent_identity_factor_hits"]
            == audit_record["rounded_hits"][:20],
        }
        assert all(fields.values())
        comparisons.append({"N": audit_record["N"], "fields": fields})

    source = Path(__file__).resolve()
    result = {
        "approach_family": "F13_teichmuller_lift_audit",
        "status": "PASS",
        "comparisons": comparisons,
        "author_json": str(author_path.resolve()),
        "author_json_sha256": sha256(author_path),
        "audit_json": str(audit_path.resolve()),
        "audit_json_sha256": sha256(audit_path),
        "source": str(source),
        "source_sha256": sha256(source),
    }
    Path(arguments.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
