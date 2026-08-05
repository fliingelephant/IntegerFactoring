#!/usr/bin/env python3
"""Exact parameter and primality checks for F04 reconstruction."""

import argparse
import json
import math
from pathlib import Path


def trial_division_prime(n: int) -> tuple[bool, int]:
    if n < 2:
        return False, 0
    if n in (2, 3):
        return True, math.isqrt(n)
    if n % 2 == 0 or n % 3 == 0:
        return False, math.isqrt(n)
    limit = math.isqrt(n)
    d = 5
    while d <= limit:
        if n % d == 0 or (d + 2 <= limit and n % (d + 2) == 0):
            return False, limit
        d += 6
    return True, limit


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    params = json.loads(Path(args.input).read_text())
    n = int(params["N"])
    p = int(params["p"])
    q = int(params["q"])
    r = int(params["r"])
    p_prime, p_limit = trial_division_prime(p)
    q_prime, q_limit = trial_division_prime(q)
    r_prime, r_limit = trial_division_prime(r)
    result = {
        "family_id": params["family_id"],
        "product_matches": p * q == n,
        "p_prime_by_complete_trial_division": p_prime,
        "p_trial_limit": p_limit,
        "q_prime_by_complete_trial_division": q_prime,
        "q_trial_limit": q_limit,
        "r_prime_by_complete_trial_division": r_prime,
        "r_trial_limit": r_limit,
        "shift_count": int(params["shift_last"]) - int(params["shift_first"]) + 1,
        "statuses_per_field": r
        * (int(params["shift_last"]) - int(params["shift_first"]) + 1),
        "statuses_total": 2
        * r
        * (int(params["shift_last"]) - int(params["shift_first"]) + 1),
        "residues": {"p_mod_r": p % r, "q_mod_r": q % r, "N_mod_r": n % r},
        "exact_relation_q_equals_2p_minus_23": q == 2 * p - 23,
    }
    if not all((result["product_matches"], p_prime, q_prime, r_prime)):
        raise SystemExit("parameter or primality check failed")
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()

