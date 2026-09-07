#!/usr/bin/env python3
"""Pollard-rho control under the adaptive trial's worst-case work budget."""

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import random
import signal
import statistics
import time
import traceback

from composite_pilot import peak_rss_bytes
from composite_scale import build_cases


SEED = 32120260911
TRIALS_PER_CASE = 32
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024
SCALE_OUTPUT = Path(__file__).with_name("scale_output.json")


def source_sha256():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def file_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    target = Path(path)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(target)


def derived_seed(case_index, trial_index):
    raw = f"{SEED}:{case_index}:{trial_index}:rho_work_matched".encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:8], "big")


def rho_trial(n, multiplication_budget, seed):
    generator = random.Random(seed)
    modular_multiplications = 0
    gcd_calls = 0
    random_draws = 0
    polynomial_attempts = 0
    cycle_collisions = 0
    x = None
    y = None
    constant = None
    while modular_multiplications + 3 <= multiplication_budget:
        if x is None:
            x = generator.randrange(2, n - 1)
            y = x
            constant = generator.randrange(1, n)
            random_draws += 2
            polynomial_attempts += 1
        x = (x * x + constant) % n
        y = (y * y + constant) % n
        y = (y * y + constant) % n
        modular_multiplications += 3
        divisor = math.gcd(abs(x - y), n)
        gcd_calls += 1
        if 1 < divisor < n:
            return {
                "status": "factor",
                "factor": divisor,
                "modular_multiplications": modular_multiplications,
                "gcd_calls": gcd_calls,
                "random_draws": random_draws,
                "polynomial_attempts": polynomial_attempts,
                "cycle_collisions": cycle_collisions,
                "unused_multiplication_budget": (
                    multiplication_budget - modular_multiplications
                ),
            }
        if divisor == n:
            cycle_collisions += 1
            x = None
            y = None
            constant = None
    return {
        "status": "censored",
        "reason": "multiplication_budget_exhausted",
        "factor": None,
        "modular_multiplications": modular_multiplications,
        "gcd_calls": gcd_calls,
        "random_draws": random_draws,
        "polynomial_attempts": polynomial_attempts,
        "cycle_collisions": cycle_collisions,
        "unused_multiplication_budget": multiplication_budget - modular_multiplications,
    }


def summarize(trials):
    successes = [row for row in trials if row["status"] == "factor"]
    return {
        "trial_count": len(trials),
        "success_count": len(successes),
        "success_fraction": [len(successes), len(trials)],
        "censor_reasons": dict(
            Counter(row.get("reason") for row in trials if row["status"] != "factor")
        ),
        "factor_counts": {
            str(key): value
            for key, value in sorted(Counter(row["factor"] for row in successes).items())
        },
        "total_modular_multiplications": sum(
            row["modular_multiplications"] for row in trials
        ),
        "total_gcd_calls": sum(row["gcd_calls"] for row in trials),
        "total_cycle_collisions": sum(row["cycle_collisions"] for row in trials),
        "total_polynomial_attempts": sum(
            row["polynomial_attempts"] for row in trials
        ),
        "mean_modular_multiplications_all_trials": statistics.fmean(
            row["modular_multiplications"] for row in trials
        ),
        "median_modular_multiplications_on_success": (
            statistics.median(row["modular_multiplications"] for row in successes)
            if successes
            else None
        ),
        "mean_gcd_calls_all_trials": statistics.fmean(
            row["gcd_calls"] for row in trials
        ),
        "median_gcd_calls_on_success": (
            statistics.median(row["gcd_calls"] for row in successes)
            if successes
            else None
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--status", required=True)
    arguments = parser.parse_args()
    started = time.perf_counter()

    def timeout_handler(_signal_number, _frame):
        raise TimeoutError("internal 28-second alarm fired")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(INTERNAL_TIMEOUT_SECONDS)
    write_json(
        arguments.status,
        {
            "status": "running",
            "seed": SEED,
            "trials_per_case": TRIALS_PER_CASE,
            "source_sha256": source_sha256(),
            "scale_output_sha256": file_sha256(SCALE_OUTPUT),
        },
    )
    try:
        recorded_scale = json.loads(SCALE_OUTPUT.read_text())
        cases = build_cases()
        assert [
            (row["N"], row["budget"]) for row in cases
        ] == [
            (row["N"], row["budget"]) for row in recorded_scale["cases"]
        ]
        output_cases = []
        for case_index, case in enumerate(cases):
            multiplication_budget = case["budget"] * (case["budget"] - 1) // 2
            trials = []
            for trial_index in range(TRIALS_PER_CASE):
                trial_seed = derived_seed(case_index, trial_index)
                row = rho_trial(case["N"], multiplication_budget, trial_seed)
                row["trial_index"] = trial_index
                row["seed"] = trial_seed
                if row["factor"] is not None:
                    assert 1 < row["factor"] < case["N"]
                    assert case["N"] % row["factor"] == 0
                trials.append(row)
            output_cases.append(
                {
                    **case,
                    "multiplication_budget": multiplication_budget,
                    "rho_work_matched": {
                        "summary": summarize(trials),
                        "trials": trials,
                    },
                    "recorded_adaptive_summary": recorded_scale["cases"][case_index][
                        "methods"
                    ]["adaptive_roots"]["summary"],
                }
            )
            if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
                raise MemoryError("peak RSS exceeded 512 MiB")
            print(
                json.dumps(
                    {
                        "event": "case_complete",
                        "case_index": case_index,
                        "N": case["N"],
                        "multiplication_budget": multiplication_budget,
                        "successes": sum(row["status"] == "factor" for row in trials),
                    }
                ),
                flush=True,
            )
        payload = {
            "status": "passed",
            "experiment": "F321_adaptive_root_basins",
            "stage": "work-matched Pollard-rho control",
            "family": "route:F29",
            "seed": SEED,
            "trials_per_case": TRIALS_PER_CASE,
            "source_sha256": source_sha256(),
            "scale_output_sha256": file_sha256(SCALE_OUTPUT),
            "work_rule": (
                "For public B=min(4096,bitlength(N)^2), rho receives "
                "W=B*(B-1)//2 modular multiplications. Each Floyd iteration "
                "uses three. A gcd=N restarts x and c within the same W."
            ),
            "censoring": (
                "Every finite failure remains. Comparisons are empirical work "
                "counts, not expected-cost or asymptotic claims."
            ),
            "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
            "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
            "memory_limit_bytes": MEMORY_LIMIT_BYTES,
            "cases": output_cases,
            "total_walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, payload)
        status = {
            key: payload[key]
            for key in (
                "status",
                "experiment",
                "stage",
                "seed",
                "trials_per_case",
                "source_sha256",
                "scale_output_sha256",
                "internal_timeout_seconds",
                "hard_timeout_seconds",
                "memory_limit_bytes",
                "total_walltime_seconds",
                "peak_rss_bytes",
            )
        }
        status["output"] = arguments.output
        write_json(arguments.status, status)
        print(json.dumps({"event": "passed", **status}), flush=True)
    except BaseException as exception:
        failure = {
            "status": "failed",
            "experiment": "F321_adaptive_root_basins",
            "stage": "work-matched Pollard-rho control",
            "seed": SEED,
            "source_sha256": source_sha256(),
            "scale_output_sha256": file_sha256(SCALE_OUTPUT),
            "exception_type": type(exception).__name__,
            "exception": str(exception),
            "traceback": traceback.format_exc(),
            "total_walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, failure)
        write_json(arguments.status, failure)
        print(json.dumps({"event": "failed", **failure}), flush=True)
        raise
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    main()
