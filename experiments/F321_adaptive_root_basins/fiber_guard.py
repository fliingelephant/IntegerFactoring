#!/usr/bin/env python3
"""Bounded public selected-fiber guard and matched base comparison."""

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

from composite_pilot import adaptive_trial, is_prime, next_prime, peak_rss_bytes


SEED = 32120260910
TRIALS_PER_CASE = 16
GUARD_COUNTS = (2, 8)
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


def evaluate_h(seed, roots, n):
    value = seed
    for root in roots:
        value = value * (value - root) % n
    return value, len(roots)


def guarded_trial(n, budget, guard_count, seed):
    generator = random.Random(seed)
    roots = []
    h_evaluations = 0
    modular_multiplications = 0
    gcd_calls = 0
    unit_parameters_proposed = 0
    accepted_parameters = 0
    rejected_global_equalities = 0
    guard_unit_differences = 0
    guard_factor_hits = 0
    full_gcd_proposals = 0
    incomplete_guards = 0

    while h_evaluations < budget:
        proposal_seed = generator.randrange(n)
        parameter, cost = evaluate_h(proposal_seed, roots, n)
        h_evaluations += 1
        modular_multiplications += cost
        divisor = math.gcd(parameter, n)
        gcd_calls += 1
        if 1 < divisor < n:
            return {
                "status": "factor",
                "factor": divisor,
                "factor_source": "proposal",
                "probe": h_evaluations,
                "h_evaluations": h_evaluations,
                "parameters_final": len(roots),
                "unit_parameters_proposed": unit_parameters_proposed,
                "accepted_parameters": accepted_parameters,
                "rejected_global_equalities": rejected_global_equalities,
                "guard_unit_differences": guard_unit_differences,
                "guard_factor_hits": guard_factor_hits,
                "full_gcd_proposals": full_gcd_proposals,
                "incomplete_guards": incomplete_guards,
                "modular_multiplications": modular_multiplications,
                "gcd_calls": gcd_calls,
                "random_draws": h_evaluations,
            }
        if divisor == n:
            full_gcd_proposals += 1
            continue

        unit_parameters_proposed += 1
        accepted = True
        for _ in range(guard_count):
            if h_evaluations >= budget:
                incomplete_guards += 1
                accepted = False
                break
            guard_seed = generator.randrange(n)
            guard_value, cost = evaluate_h(guard_seed, roots, n)
            h_evaluations += 1
            modular_multiplications += cost
            difference_divisor = math.gcd(guard_value - parameter, n)
            gcd_calls += 1
            if 1 < difference_divisor < n:
                guard_factor_hits += 1
                return {
                    "status": "factor",
                    "factor": difference_divisor,
                    "factor_source": "guard_difference",
                    "probe": h_evaluations,
                    "h_evaluations": h_evaluations,
                    "parameters_final": len(roots),
                    "unit_parameters_proposed": unit_parameters_proposed,
                    "accepted_parameters": accepted_parameters,
                    "rejected_global_equalities": rejected_global_equalities,
                    "guard_unit_differences": guard_unit_differences,
                    "guard_factor_hits": guard_factor_hits,
                    "full_gcd_proposals": full_gcd_proposals,
                    "incomplete_guards": incomplete_guards,
                    "modular_multiplications": modular_multiplications,
                    "gcd_calls": gcd_calls,
                    "random_draws": h_evaluations,
                }
            if difference_divisor == n:
                rejected_global_equalities += 1
                accepted = False
                break
            guard_unit_differences += 1
        if accepted:
            roots.append(parameter)
            accepted_parameters += 1

    return {
        "status": "censored",
        "reason": (
            "budget_exhausted_mid_guard"
            if incomplete_guards
            else "budget_exhausted"
        ),
        "factor": None,
        "factor_source": None,
        "probe": None,
        "h_evaluations": h_evaluations,
        "parameters_final": len(roots),
        "unit_parameters_proposed": unit_parameters_proposed,
        "accepted_parameters": accepted_parameters,
        "rejected_global_equalities": rejected_global_equalities,
        "guard_unit_differences": guard_unit_differences,
        "guard_factor_hits": guard_factor_hits,
        "full_gcd_proposals": full_gcd_proposals,
        "incomplete_guards": incomplete_guards,
        "modular_multiplications": modular_multiplications,
        "gcd_calls": gcd_calls,
        "random_draws": h_evaluations,
    }


def base_trial(n, budget, seed):
    row = adaptive_trial(n, budget, seed)
    return {
        **row,
        "factor_source": "proposal" if row["status"] == "factor" else None,
        "h_evaluations": row["probes"],
        "unit_parameters_proposed": row["parameters_final"],
        "accepted_parameters": row["parameters_final"],
        "rejected_global_equalities": 0,
        "guard_unit_differences": 0,
        "guard_factor_hits": 0,
        "full_gcd_proposals": row["full_gcd_probes"],
        "incomplete_guards": 0,
    }


def summarize(trials):
    successes = [row for row in trials if row["status"] == "factor"]
    proposed = sum(row["unit_parameters_proposed"] for row in trials)
    accepted = sum(row["accepted_parameters"] for row in trials)
    return {
        "trial_count": len(trials),
        "success_count": len(successes),
        "success_fraction": [len(successes), len(trials)],
        "censor_reasons": dict(
            Counter(row.get("reason") for row in trials if row["status"] != "factor")
        ),
        "factor_sources": dict(Counter(row["factor_source"] for row in successes)),
        "total_h_evaluations": sum(row["h_evaluations"] for row in trials),
        "total_modular_multiplications": sum(
            row["modular_multiplications"] for row in trials
        ),
        "total_gcd_calls": sum(row["gcd_calls"] for row in trials),
        "total_unit_parameters_proposed": proposed,
        "total_accepted_parameters": accepted,
        "accepted_parameter_fraction": [accepted, proposed] if proposed else [0, 0],
        "total_rejected_global_equalities": sum(
            row["rejected_global_equalities"] for row in trials
        ),
        "total_guard_unit_differences": sum(
            row["guard_unit_differences"] for row in trials
        ),
        "mean_h_evaluations_all_trials": statistics.fmean(
            row["h_evaluations"] for row in trials
        ),
        "mean_modular_multiplications_all_trials": statistics.fmean(
            row["modular_multiplications"] for row in trials
        ),
        "mean_gcd_calls_all_trials": statistics.fmean(
            row["gcd_calls"] for row in trials
        ),
        "median_h_evaluation_on_success": (
            statistics.median(row["probe"] for row in successes) if successes else None
        ),
    }


def build_cases():
    cases = []
    for exponent in (12, 16, 20, 24):
        p = next_prime(1 << exponent)
        q = next_prime((8 * p + 4) // 5)
        assert is_prime(p) and is_prime(q) and p != q
        n = p * q
        cases.append(
            {
                "kind": "balanced_approximately_1.6",
                "source_exponent": exponent,
                "p": p,
                "q": q,
                "N": n,
                "bitlength": n.bit_length(),
                "budget": min(4096, n.bit_length() ** 2),
            }
        )
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
            "guard_counts": GUARD_COUNTS,
            "source_sha256": source_sha256(),
            "original_source_sha256": dependency_sha256(),
        },
    )
    try:
        output_cases = []
        for case_index, case in enumerate(build_cases()):
            methods = {"base_adaptive": base_trial}
            for guard_count in GUARD_COUNTS:
                methods[f"fiber_guard_K{guard_count}"] = (
                    lambda n, budget, seed, k=guard_count: guarded_trial(
                        n, budget, k, seed
                    )
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
                        "N": case["N"],
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
            "stage": "selected-fiber guards",
            "family": "route:F29",
            "seed": SEED,
            "trials_per_case": TRIALS_PER_CASE,
            "guard_counts": GUARD_COUNTS,
            "source_sha256": source_sha256(),
            "original_source_sha256": dependency_sha256(),
            "public_scope": (
                "Every parameter, guard seed, and decision uses only N, public "
                "budgets, current public outputs, gcds, and independent random bits."
            ),
            "budget_rule": (
                "Every proposal or guard evaluation of H counts once against "
                "min(4096, bitlength(N)^2)."
            ),
            "censoring": (
                "All finite failures and guards interrupted by the public budget "
                "remain present. No unbounded probability theorem is inferred."
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
                "guard_counts",
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
            "stage": "selected-fiber guards",
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
