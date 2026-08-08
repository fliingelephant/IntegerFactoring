#!/usr/bin/env python3
"""Replay full factor-assisted C2T on one declared semiprime."""

from __future__ import annotations

import json
from pathlib import Path

from search_factor_assisted import run_overpowered_c2t, stable


P = 10267
Q = 19727
OUTPUT = Path(__file__).resolve().parent / "SINGLE_202537109_OUTPUT.json"


def main() -> int:
    modulus = P * Q
    result = {
        "experiment": "F98_multiseed_presentation_closure_kill",
        "role": "full factor-assisted single-input replay",
        "p": P,
        "q": Q,
        "N": modulus,
        "stable": stable(P, Q),
        "selector_receives": ["N"],
        "result": run_overpowered_c2t(modulus),
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"status={result['result']['status']}")
    print(f"output={OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
