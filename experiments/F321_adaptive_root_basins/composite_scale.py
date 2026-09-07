#!/usr/bin/env python3
"""Larger public composite trials for F321; original pilot files stay fixed."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import signal
import statistics
import time
import traceback

from composite_pilot import (
    adaptive_trial,
    is_prime,
    next_prime,
    peak_rss_bytes,
    pollard_rho_trial,
    uniform_gcd_trial,
)


SEED = 32120260909
TRIALS_PER_CASE = 32
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024
ORIGINAL_SOURCE = Path(__file__).with_name("composite_pilot.py")


def source_sha256():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def dependency_sha256():
    return hashlib.sha256(ORIGINAL_SOURCE.read_bytes()).hexdigest()


def write_json(path, value):
    target = Path(path)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(target)


def derived_seed(case_index, trial_index, method):
    raw = f"{SEED}:{case_index}:{trial_index}:{method}".encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:8], "big")


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
        "mean_modular_multiplications_all_trials": statistics.fmean(
            row["modular_multiplications"] for row in trials
        ),
        "mean_gcd_calls_all_trials": statistics.fmean(
            row["gcd_calls"] for row in trials
        ),
        "median_probe_on_success": (
            statistics.median(row["probe"] for row in successes) if successes else None
        ),
        "mean_probe_on_success": (
            statistics.fmean(row["probe"] for row in successes) if successes else None
        ),
    }


def build_cases():
    cases = []
    for exponent in (18, 20, 22, 24, 26, 28):
        p = next_prime(1 << exponent)
        q = next_prime((8 * p + 4) // 5)
        cases.append(
            {
                "kind": "balanced_approximately_1.6",
                "source_exponents": [exponent, None],
                "p": p,
                "q": q,
            }
        )
    for small_exponent, large_exponent in ((18, 28), (20, 32)):
        p = next_prime(1 << small_exponent)
        q = next_prime(1 << large_exponent)
        cases.append(
            {
                "kind": "unbalanced",
                "source_exponents": [small_exponent, large_exponent],
                "p": p,
                "q": q,
            }
        )
    for row in cases:
        assert is_prime(row["p"]) and is_prime(row["q"]) and row["p"] != row["q"]
        row["N"] = row["p"] * row["q"]
        row["bitlength"] = row["N"].bit_length()
        row["budget"] = min(4096, row["bitlength"] ** 2)
    return cases


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
            "original_source_sha256": dependency_sha256(),
        },
    )
    try:
        methods = {
            "adaptive_roots": adaptive_trial,
            "uniform_gcd": uniform_gcd_trial,
            "pollard_rho": pollard_rho_trial,
        }
        output_cases = []
        for case_index, case in enumerate(build_cases()):
            print(
                json.dumps(
                    {
                        "event": "case_start",
                        "case_index": case_index,
                        "N": case["N"],
                        "budget": case["budget"],
                    }
                ),
                flush=True,
            )
            results = {}
            for method_name, method in methods.items():
                trials = []
                for trial_index in range(TRIALS_PER_CASE):
                    trial_seed = derived_seed(case_index, trial_index, method_name)
                    row = method(case["N"], case["budget"], trial_seed)
                    row["trial_index"] = trial_index
                    row["seed"] = trial_seed
                    if row["factor"] is not None:
                        assert 1 < row["factor"] < case["N"]
                        assert case["N"] % row["factor"] == 0
                    trials.append(row)
                results[method_name] = {
                    "summary": summarize(trials),
                    "trials": trials,
                }
            output_cases.append({**case, "methods": results})
            if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
                raise MemoryError("peak RSS exceeded 512 MiB")
            print(
                json.dumps(
                    {
                        "event": "case_complete",
                        "case_index": case_index,
                        "successes": {
                            name: value["summary"]["success_count"]
                            for name, value in results.items()
                        },
                    }
                ),
                flush=True,
            )
        payload = {
            "status": "passed",
            "experiment": "F321_adaptive_root_basins",
            "stage": "larger public composite trials",
            "family": "route:F29",
            "seed": SEED,
            "trials_per_case": TRIALS_PER_CASE,
            "source_sha256": source_sha256(),
            "original_source_sha256": dependency_sha256(),
            "public_scope": (
                "Each method receives only N, its bitlength-derived public budget, "
                "and independent random bits. Factors only construct and label cases."
            ),
            "censoring": (
                "Every finite failure remains present. No scaling fit or unbounded "
                "success law is inferred."
            ),
            "budget_rule": "min(4096, bitlength(N)^2) H evaluations or gcd stages",
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
                "original_source_sha256",
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
            "stage": "larger public composite trials",
            "seed": SEED,
            "source_sha256": source_sha256(),
            "original_source_sha256": dependency_sha256(),
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
