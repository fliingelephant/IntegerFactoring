#!/usr/bin/env python3
"""Scan stable pairs p=g*A+1, q=g*B+1 for fixed coprime odd A,B."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time


HERE = Path(__file__).resolve().parent
FAST_SOURCE = HERE / "scan_prime_core_candidates.py"
EXPECTED_FAST_SHA256 = "2b38a3920524a434988ab4fa105d5770a2ef755e5d519c4248b0d2d6bebda79f"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha256(FAST_SOURCE) == EXPECTED_FAST_SHA256
SPEC = importlib.util.spec_from_file_location("f104_fast_structured", FAST_SOURCE)
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
    parser.add_argument("--g-min", type=int, required=True)
    parser.add_argument("--g-max", type=int, required=True)
    parser.add_argument("--pair-cap", type=int, required=True)
    parser.add_argument("--shapes", default="1:3,1:5,1:7,3:5,3:7,5:7")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    shapes = []
    for encoded in args.shapes.split(","):
        A, B = map(int, encoded.split(":"))
        assert 0 < A < B and A % 2 == B % 2 == 1 and math.gcd(A, B) == 1
        shapes.append((A, B))

    started = time.monotonic()
    prime_pairs = 0
    completed = 0
    trace: list[dict[str, object]] = []
    counterexample = None
    payload: dict[str, object] = {
        "status": "running",
        "role": "factor-assisted structured-stability scan; factor-free acceptance required",
        "source_sha256": sha256(Path(__file__).resolve()),
        "fast_source_sha256": sha256(FAST_SOURCE),
        "bounds": {
            "g_min": args.g_min,
            "g_max": args.g_max,
            "pair_cap": args.pair_cap,
            "shapes": [list(shape) for shape in shapes],
            "enumeration": "even g ascending, then shapes in displayed order",
        },
        "stability_identity": "for coprime A,B and gcd(g,A*B)=1, gcd(A*B,(g*A+1)*(g*B+1)-1)=1",
    }

    first_g = args.g_min + (args.g_min & 1)
    for g in range(first_g, args.g_max + 1, 2):
        for A, B in shapes:
            if math.gcd(g, A * B) != 1:
                continue
            p = g * A + 1
            q = g * B + 1
            if not FAST.is_prime_u64(p) or not FAST.is_prime_u64(q):
                continue
            N = p * q
            n = N.bit_length()
            bound = n * n
            if p <= bound:
                continue
            certificate = BASE.stable_certificate(p, q)
            assert certificate["stable"]
            prime_pairs += 1
            result = FAST.normalize_result(BASE.run_one_round(N))
            entry = {
                "ordinal": prime_pairs,
                "g": g,
                "A": A,
                "B_shape": B,
                "p": p,
                "q": q,
                "N": N,
                "n": n,
                "trial_bound": bound,
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
                    "prime_pairs_tested": prime_pairs,
                    "completed_rounds": completed,
                    "trace": trace,
                    "counterexample": counterexample,
                    "elapsed_seconds": time.monotonic() - started,
                }
            )
            write_output(args.output, payload)
            print(
                f"pair={prime_pairs} g={g} shape={A}:{B} N={N} status={result['status']} completed={completed}",
                file=sys.stderr,
                flush=True,
            )
            if prime_pairs >= args.pair_cap:
                break
        if counterexample is not None or prime_pairs >= args.pair_cap:
            break

    payload.update(
        {
            "status": "counterexample_candidate" if counterexample is not None else "cap_complete",
            "prime_pairs_tested": prime_pairs,
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
