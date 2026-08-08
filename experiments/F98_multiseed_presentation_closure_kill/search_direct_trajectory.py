#!/usr/bin/env python3
"""Fast diverse-band screen for direct C2T endpoint-difference factors."""

from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

from search_factor_assisted import factor_u64, primes_through, public_basis, stable


def direct_round_one(modulus: int) -> dict[str, object]:
    n = modulus.bit_length()
    bound = n * n
    for t in range(2, bound + 1):
        divisor = math.gcd(t, modulus)
        if 1 < divisor < modulus:
            return {"status": "trial_factor", "factor": divisor}

    records = []
    seen = set()
    for seed in range(2, n + 1):
        inverse = pow(seed, -1, modulus)
        c_factors = factor_u64(seed)
        w_factors = factor_u64(inverse)
        relation_factors = dict(c_factors)
        for p, exponent in w_factors.items():
            relation_factors[p] = relation_factors.get(p, 0) + exponent
        records.append(
            {
                "c": seed,
                "w": inverse,
                "P": seed * inverse,
                "c_factors": c_factors,
                "w_factors": w_factors,
                "relation_factors": relation_factors,
            }
        )
        seen.add(seed)
        for sign, difference in (("minus", seed - inverse), ("plus", seed + inverse)):
            divisor = math.gcd(difference, modulus)
            if 1 < divisor < modulus:
                return {
                    "status": "initial_direct_factor",
                    "factor": divisor,
                    "sign": sign,
                    "c": seed,
                    "w": inverse,
                }

    blocks, supports = public_basis(records)
    active = []
    for relation_index, record in enumerate(records):
        if any(exponent & 1 for exponent in record["relation_factors"].values()):
            support = supports[relation_index]
            if len(support) == 1:
                pair = (support[0], 1)
            else:
                pair = tuple(support[:2])
            active.append((relation_index, pair))
            if len(active) == n:
                break

    residues_examined = 0
    for relation_index, (u, v) in active:
        for exponent in range(bound + 1):
            candidates = (
                ("u_power_times_v", pow(u, exponent, modulus) * v % modulus),
                ("u_times_v_power", u * pow(v, exponent, modulus) % modulus),
            )
            for orientation, c in candidates:
                if c in seen:
                    continue
                seen.add(c)
                residues_examined += 1
                inverse = pow(c, -1, modulus)
                for sign, difference in (("minus", c - inverse), ("plus", c + inverse)):
                    divisor = math.gcd(difference, modulus)
                    if 1 < divisor < modulus:
                        return {
                            "status": "feedback_direct_factor",
                            "factor": divisor,
                            "sign": sign,
                            "c": c,
                            "w": inverse,
                            "active_relation_index_zero_based": relation_index,
                            "u": u,
                            "v": v,
                            "exponent": exponent,
                            "orientation": orientation,
                            "residues_examined": residues_examined,
                            "public_basis_size": len(blocks),
                        }
    return {
        "status": "round_one_direct_null",
        "residues_examined": residues_examined,
        "active_relations": len(active),
        "public_basis_size": len(blocks),
        "n": n,
        "B": bound,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-min", type=int, required=True)
    parser.add_argument("--prime-max", type=int, required=True)
    parser.add_argument("--pair-cap", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    started = time.monotonic()
    primes = [
        p
        for p in primes_through(args.prime_max)
        if args.prime_min <= p <= args.prime_max
    ]
    trace = []
    pairs_tested = 0
    stable_tested = 0
    for i, p in enumerate(primes):
        q_index = len(primes) - 1 - i
        if q_index <= i or pairs_tested >= args.pair_cap:
            break
        q = primes[q_index]
        pairs_tested += 1
        if not stable(p, q):
            continue
        stable_tested += 1
        result = direct_round_one(p * q)
        trace.append({"p": p, "q": q, "N": p * q, "result": result})
        output = {
            "experiment": "F98_multiseed_presentation_closure_kill",
            "role": "round-one direct-hit diverse-band screen",
            "bounds": vars(args) | {"output": str(args.output)},
            "pairs_tested": pairs_tested,
            "stable_pairs_tested": stable_tested,
            "trace": trace,
            "elapsed_seconds": time.monotonic() - started,
        }
        temporary = args.output.with_suffix(args.output.suffix + ".tmp")
        temporary.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
        temporary.replace(args.output)
    print(f"pairs_tested={pairs_tested}")
    print(f"stable_pairs_tested={stable_tested}")
    print(f"elapsed_seconds={time.monotonic() - started:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
