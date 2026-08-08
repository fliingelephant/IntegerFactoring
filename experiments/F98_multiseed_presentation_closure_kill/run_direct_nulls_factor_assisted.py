#!/usr/bin/env python3
"""Run full C2T on every direct-null input from the named 10K screen."""

from __future__ import annotations

import json
from pathlib import Path

from search_factor_assisted import run_overpowered_c2t, stable


CASES = [
    (10267, 19727),
    (11071, 18899),
    (12919, 16931),
    (13487, 16319),
    (14207, 15619),
]
BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "DIRECT_NULLS_10K_FULL_OUTPUT.json"


def main() -> int:
    results = []
    for p, q in CASES:
        modulus = p * q
        results.append(
            {
                "p": p,
                "q": q,
                "N": modulus,
                "stable": stable(p, q),
                "selector_receives": ["N"],
                "result": run_overpowered_c2t(modulus),
            }
        )
    output = {
        "experiment": "F98_multiseed_presentation_closure_kill",
        "role": "full factor-assisted replay of all diverse-10K direct nulls",
        "cases": results,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    for record in results:
        result = record["result"]
        print(record["N"], result["status"], result.get("factor_method"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
