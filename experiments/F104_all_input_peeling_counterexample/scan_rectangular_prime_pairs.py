#!/usr/bin/env python3
"""Scan deterministic stable prime pairs from two disjoint factor bands."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time


HERE = Path(__file__).resolve().parent
FAST_SOURCE = HERE / "scan_prime_core_candidates.py"
EXPECTED_FAST_SHA256 = "2b38a3920524a434988ab4fa105d5770a2ef755e5d519c4248b0d2d6bebda79f"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha256(FAST_SOURCE) == EXPECTED_FAST_SHA256
SPEC = importlib.util.spec_from_file_location("f104_fast_rectangular", FAST_SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot import fast F104 source")
FAST = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(FAST)
BASE = FAST.BASE


def write_output(path: Path, payload: dict[str, object]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-min", type=int, required=True)
    parser.add_argument("--p-max", type=int, required=True)
    parser.add_argument("--q-min", type=int, required=True)
    parser.add_argument("--q-max", type=int, required=True)
    parser.add_argument("--pair-cap", type=int, required=True)
    parser.add_argument("--partners-per-p", type=int, default=1)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert args.p_max < args.q_min

    all_primes = BASE.primes_through(args.q_max)
    p_values = [prime for prime in all_primes if args.p_min <= prime <= args.p_max]
    q_values = [prime for prime in all_primes if args.q_min <= prime <= args.q_max]
    started = time.monotonic()
    pairs_tested = 0
    stable_tested = 0
    completed = 0
    trace: list[dict[str, object]] = []
    counterexample = None
    payload: dict[str, object] = {
        "status": "running",
        "role": "factor-assisted rectangular-band scan; factor-free P66 acceptance required",
        "source_sha256": sha256(Path(__file__).resolve()),
        "fast_source_sha256": sha256(FAST_SOURCE),
        "bounds": {
            "p_min": args.p_min,
            "p_max": args.p_max,
            "q_min": args.q_min,
            "q_max": args.q_max,
            "pair_cap": args.pair_cap,
            "partners_per_p": args.partners_per_p,
            "enumeration": "p ascending; disjoint q values consumed from the descending q tail",
        },
    }

    for p_index, p in enumerate(p_values):
        for offset in range(args.partners_per_p):
            q_index = len(q_values) - 1 - p_index * args.partners_per_p - offset
            if q_index < 0 or pairs_tested >= args.pair_cap:
                break
            q = q_values[q_index]
            N = p * q
            n = N.bit_length()
            bound = n * n
            if p <= bound:
                continue
            pairs_tested += 1
            certificate = BASE.stable_certificate(p, q)
            if not certificate["stable"]:
                continue
            stable_tested += 1
            result = FAST.normalize_result(BASE.run_one_round(N))
            entry = {
                "pair_ordinal": pairs_tested,
                "stable_ordinal": stable_tested,
                "p": p,
                "q": q,
                "factor_ratio_q_over_p": q / p,
                "N": N,
                "n": n,
                "B": bound,
                "trial_hard": p > bound and q > bound,
                "stable_certificate": certificate,
                "result": result,
            }
            trace.append(entry)
            if result["status"] == "round_complete":
                completed += 1
                if not result["matrix"]["core_rank_deficient"]:
                    second = FAST.normalize_result(BASE.run_one_round(N))
                    assert second["status"] == "round_complete"
                    assert second["matrix"] == result["matrix"]
                    entry["deterministic_second_prime_replay_match"] = True
                    counterexample = entry
                    break
            payload.update(
                {
                    "pairs_tested": pairs_tested,
                    "stable_pairs_tested": stable_tested,
                    "completed_rounds": completed,
                    "trace": trace,
                    "counterexample": counterexample,
                    "elapsed_seconds": time.monotonic() - started,
                }
            )
            write_output(args.output, payload)
            print(
                f"stable={stable_tested} N={N} status={result['status']} completed={completed}",
                file=sys.stderr,
                flush=True,
            )
        if counterexample is not None or pairs_tested >= args.pair_cap:
            break

    payload.update(
        {
            "status": "counterexample_candidate" if counterexample is not None else "cap_complete",
            "pairs_tested": pairs_tested,
            "stable_pairs_tested": stable_tested,
            "completed_rounds": completed,
            "trace": trace,
            "counterexample": counterexample,
            "elapsed_seconds": time.monotonic() - started,
        }
    )
    write_output(args.output, payload)
    print(f"status={payload['status']}")
    print(f"elapsed_seconds={payload['elapsed_seconds']:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
