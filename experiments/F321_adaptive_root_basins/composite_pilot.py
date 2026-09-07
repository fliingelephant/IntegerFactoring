#!/usr/bin/env python3
"""Public adaptive-root discovery pilot and two randomized controls."""

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import random
import resource
import signal
import statistics
import sys
import time
import traceback


SEED = 32120260907
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024
TRIALS_PER_CASE = 16


def peak_rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def source_sha256():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def write_json(path, value):
    target = Path(path)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(target)


def is_prime(n):
    if n < 2:
        return False
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % prime == 0:
            return n == prime
    d = n - 1
    shift = 0
    while d % 2 == 0:
        shift += 1
        d //= 2
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % n == 0:
            continue
        x = pow(base, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(shift - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def next_prime(start):
    candidate = max(2, start)
    if candidate == 2:
        return 2
    candidate |= 1
    while not is_prime(candidate):
        candidate += 2
    return candidate


def derived_seed(case_index, trial_index, method):
    raw = f"{SEED}:{case_index}:{trial_index}:{method}".encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:8], "big")


def adaptive_trial(n, budget, seed):
    generator = random.Random(seed)
    parameters = []
    modular_multiplications = 0
    gcd_calls = 0
    probes = 0
    full_gcd_probes = 0
    for probe in range(1, budget + 1):
        x = generator.randrange(n)
        y = x
        for root in parameters:
            y = y * (y - root) % n
            modular_multiplications += 1
        divisor = math.gcd(y, n)
        gcd_calls += 1
        probes = probe
        if 1 < divisor < n:
            return {
                "status": "factor",
                "factor": divisor,
                "probe": probe,
                "probes": probes,
                "parameters_final": len(parameters),
                "full_gcd_probes": full_gcd_probes,
                "modular_multiplications": modular_multiplications,
                "gcd_calls": gcd_calls,
                "random_draws": probes,
            }
        if divisor == 1:
            parameters.append(y)
        else:
            full_gcd_probes += 1
    return {
        "status": "censored",
        "reason": "budget_exhausted",
        "factor": None,
        "probe": None,
        "probes": probes,
        "parameters_final": len(parameters),
        "full_gcd_probes": full_gcd_probes,
        "modular_multiplications": modular_multiplications,
        "gcd_calls": gcd_calls,
        "random_draws": probes,
    }


def uniform_gcd_trial(n, budget, seed):
    generator = random.Random(seed)
    for probe in range(1, budget + 1):
        x = generator.randrange(n)
        divisor = math.gcd(x, n)
        if 1 < divisor < n:
            return {
                "status": "factor",
                "factor": divisor,
                "probe": probe,
                "probes": probe,
                "modular_multiplications": 0,
                "gcd_calls": probe,
                "random_draws": probe,
            }
    return {
        "status": "censored",
        "reason": "budget_exhausted",
        "factor": None,
        "probe": None,
        "probes": budget,
        "modular_multiplications": 0,
        "gcd_calls": budget,
        "random_draws": budget,
    }


def pollard_rho_trial(n, budget, seed):
    generator = random.Random(seed)
    x = generator.randrange(2, n - 1)
    y = x
    constant = generator.randrange(1, n)
    modular_multiplications = 0
    for step in range(1, budget + 1):
        x = (x * x + constant) % n
        y = (y * y + constant) % n
        y = (y * y + constant) % n
        modular_multiplications += 3
        divisor = math.gcd(abs(x - y), n)
        if 1 < divisor < n:
            return {
                "status": "factor",
                "factor": divisor,
                "probe": step,
                "probes": step,
                "constant": constant,
                "modular_multiplications": modular_multiplications,
                "gcd_calls": step,
                "random_draws": 2,
            }
        if divisor == n:
            return {
                "status": "censored",
                "reason": "cycle_collision",
                "factor": None,
                "probe": None,
                "probes": step,
                "constant": constant,
                "modular_multiplications": modular_multiplications,
                "gcd_calls": step,
                "random_draws": 2,
            }
    return {
        "status": "censored",
        "reason": "budget_exhausted",
        "factor": None,
        "probe": None,
        "probes": budget,
        "constant": constant,
        "modular_multiplications": modular_multiplications,
        "gcd_calls": budget,
        "random_draws": 2,
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
    for exponent in (8, 10, 12, 14, 16):
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
    for small_exponent, large_exponent in ((8, 16), (10, 18), (12, 20)):
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
        row["budget"] = min(512, row["bitlength"] ** 2)
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
            "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
            "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
            "memory_limit_bytes": MEMORY_LIMIT_BYTES,
        },
    )
    try:
        output_cases = []
        methods = {
            "adaptive_roots": adaptive_trial,
            "uniform_gcd": uniform_gcd_trial,
            "pollard_rho": pollard_rho_trial,
        }
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
            method_results = {}
            for method_name, method in methods.items():
                trials = []
                for trial_index in range(TRIALS_PER_CASE):
                    seed = derived_seed(case_index, trial_index, method_name)
                    row = method(case["N"], case["budget"], seed)
                    row["trial_index"] = trial_index
                    row["seed"] = seed
                    if row["factor"] is not None:
                        assert 1 < row["factor"] < case["N"]
                        assert case["N"] % row["factor"] == 0
                    trials.append(row)
                method_results[method_name] = {
                    "summary": summarize(trials),
                    "trials": trials,
                }
            output_cases.append({**case, "methods": method_results})
            if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
                raise MemoryError("peak RSS exceeded 512 MiB")
            print(
                json.dumps(
                    {
                        "event": "case_complete",
                        "case_index": case_index,
                        "successes": {
                            name: data["summary"]["success_count"]
                            for name, data in method_results.items()
                        },
                    }
                ),
                flush=True,
            )
        payload = {
            "status": "passed",
            "experiment": "F321_adaptive_root_basins",
            "family": "route:F29",
            "seed": SEED,
            "trials_per_case": TRIALS_PER_CASE,
            "public_scope": (
                "Each tested algorithm receives only N, its public bitlength budget, "
                "and independent random bits. Factors only construct and label cases."
            ),
            "censoring": (
                "Every unsuccessful finite trial remains in the output. No empirical "
                "success fraction is interpreted as an unbounded probability theorem."
            ),
            "source_sha256": source_sha256(),
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
                "seed",
                "trials_per_case",
                "source_sha256",
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
            "seed": SEED,
            "source_sha256": source_sha256(),
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
