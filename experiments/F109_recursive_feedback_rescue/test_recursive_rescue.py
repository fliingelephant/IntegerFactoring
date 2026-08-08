#!/usr/bin/env python3
"""Compare full C2T recursion with its final small-pair trajectory."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parents[2]
SOURCE_PATH = ROOT / "experiments/F98_multiseed_presentation_closure_kill/search_factor_assisted.py"
EXPECTED_SOURCE_SHA256 = "cbf50afc19a387ee58dffa9b0cca9a4ac2e732265c1b841cb535907cce364479"
CASES = [
    (41011, 79043, (2, 13)),
    (80107, 159899, (3, 5)),
    (80363, 159631, (2, 7)),
    (80687, 159319, (2, 7)),
    (80779, 159199, (2, 13)),
    (80803, 159179, (2, 5)),
    (320107, 639839, (2, 13)),
]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha256_file(SOURCE_PATH) == EXPECTED_SOURCE_SHA256
SPEC = importlib.util.spec_from_file_location("f109_pinned_f98", SOURCE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot import pinned F98 factor-assisted source")
F98 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(F98)


def run_pair_menu(modulus: int, u: int, v: int) -> dict[str, object]:
    n = modulus.bit_length()
    bound = n * n
    for trial in range(2, bound + 1):
        divisor = math.gcd(trial, modulus)
        assert not 1 < divisor < modulus

    decoder = F98.PrimeDecoder(modulus)
    seen: set[int] = set()
    cache: dict[int, dict[int, int]] = {1: {}}
    retained = 0
    attempted = 0
    repeated = 0

    def factors(value: int):
        result = cache.get(value)
        if result is None:
            result = F98.factor_u64(value)
            cache[value] = result
        return result

    def retain(c: int, provenance: dict[str, object]):
        nonlocal retained, attempted, repeated
        attempted += 1
        if c in seen:
            repeated += 1
            return None
        seen.add(c)
        w = pow(c, -1, modulus)
        for sign, difference in (("minus", c - w), ("plus", c + w)):
            divisor = math.gcd(difference, modulus)
            if 1 < divisor < modulus:
                return {
                    "channel": f"direct_{sign}",
                    "factor": divisor,
                    "c": c,
                    "w": w,
                    "provenance": provenance,
                }
        relation_factors = dict(factors(c))
        for prime, exponent in factors(w).items():
            relation_factors[prime] = relation_factors.get(prime, 0) + exponent
        decoder.add(relation_factors)
        retained += 1
        if decoder.factor is not None:
            return {
                "channel": decoder.factor_method,
                "factor": decoder.factor,
                "dependency_support": decoder.factor_dependency_size,
                "provenance": provenance,
            }
        return None

    for seed in range(2, n + 1):
        result = retain(seed, {"kind": "initial_seed", "seed": seed})
        assert result is None

    for exponent in range(bound + 1):
        for orientation, candidate in (
            ("u_power_times_v", pow(u, exponent, modulus) * v % modulus),
            ("u_times_v_power", u * pow(v, exponent, modulus) % modulus),
        ):
            result = retain(
                candidate,
                {
                    "kind": "fixed_pair_trajectory",
                    "u": u,
                    "v": v,
                    "exponent": exponent,
                    "orientation": orientation,
                },
            )
            if result is not None:
                return {
                    "status": "factor",
                    "n": n,
                    "bound": bound,
                    "pair": [u, v],
                    "attempted": attempted,
                    "repeated": repeated,
                    "retained": retained,
                    "dependencies": decoder.dependencies,
                    "global_dependencies": decoder.global_dependencies,
                    "result": result,
                }
    return {
        "status": "null",
        "n": n,
        "bound": bound,
        "pair": [u, v],
        "attempted": attempted,
        "repeated": repeated,
        "retained": retained,
        "dependencies": decoder.dependencies,
        "global_dependencies": decoder.global_dependencies,
    }


def compact_recursive(result: dict[str, object]):
    active_pairs = result.get("active_pairs", [])
    return {
        "status": result["status"],
        "factor": result.get("factor"),
        "factor_method": result.get("factor_method"),
        "factor_dependency_size": result.get("factor_dependency_size"),
        "round": result.get("round"),
        "relations": result.get("relations"),
        "dependencies": result.get("dependencies"),
        "causal_pair": active_pairs[-1] if active_pairs else None,
        "round_summaries": [
            {
                "round": row["round"],
                "active": row["active"],
                "new_relations": row["new_relations"],
                "new_dependencies": row["new_dependencies"],
            }
            for row in result.get("rounds", [])
        ],
    }


def main() -> None:
    started = time.monotonic()
    output = []
    for p, q, expected_pair in CASES:
        modulus = p * q
        case_started = time.monotonic()
        recursive = compact_recursive(F98.run_overpowered_c2t(modulus))
        causal_pair = tuple(recursive["causal_pair"] or ())
        assert recursive["status"] == "feedback_factor"
        assert recursive["factor"] in (p, q)
        assert causal_pair == expected_pair
        isolated = run_pair_menu(modulus, *expected_pair)
        if isolated["status"] == "factor":
            assert isolated["result"]["factor"] in (p, q)
        output.append(
            {
                "p": p,
                "q": q,
                "N": modulus,
                "trial_hard": min(p, q) > modulus.bit_length() ** 2,
                "stable": F98.stable(p, q),
                "recursive": recursive,
                "isolated_final_pair": isolated,
                "causal_pair_members_are_initial_seeds": all(
                    2 <= value <= modulus.bit_length() for value in expected_pair
                ),
                "elapsed_seconds": time.monotonic() - case_started,
            }
        )
    result = {
        "status": "PASS",
        "role": "factor-assisted bounded comparison; N-only replay required for promotion",
        "pinned_source": {
            "path": str(SOURCE_PATH.relative_to(ROOT)),
            "sha256": sha256_file(SOURCE_PATH),
        },
        "cases": output,
        "all_recursive_runs_factor": all(
            case["recursive"]["status"] == "feedback_factor" for case in output
        ),
        "all_isolated_final_pairs_factor": all(
            case["isolated_final_pair"]["status"] == "factor" for case in output
        ),
        "all_causal_pair_members_are_initial_seeds": all(
            case["causal_pair_members_are_initial_seeds"] for case in output
        ),
        "elapsed_seconds": time.monotonic() - started,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
