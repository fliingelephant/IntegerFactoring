#!/usr/bin/env python3
"""Run full C2T on the first diverse 1M direct-null input using Sage factor."""

from __future__ import annotations

import json
from pathlib import Path

from sage.all import Integer, factor

import search_factor_assisted as search


P = 1000003
Q = 1199999
BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "SINGLE_1M_SAGE_OUTPUT.json"


def sage_factor(value: int) -> dict[int, int]:
    return {int(prime): int(exponent) for prime, exponent in factor(Integer(value))}


def main() -> int:
    search.factor_u64 = sage_factor
    modulus = P * Q
    result = {
        "experiment": "F98_multiseed_presentation_closure_kill",
        "role": "full factor-assisted Sage replay of first diverse-1M direct null",
        "p": P,
        "q": Q,
        "N": modulus,
        "stable": search.stable(P, Q),
        "least_factor_exceeds_n_squared": P > modulus.bit_length() ** 2,
        "selector_receives": ["N"],
        "result": search.run_overpowered_c2t(modulus),
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["result"]["status"], result["result"].get("factor_method"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
