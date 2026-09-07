#!/usr/bin/env python3
"""Conditional finite-field image-population diagnostic for adaptive roots."""

import argparse
import hashlib
import json
from pathlib import Path
import random
import resource
import signal
import sys
import time
import traceback

import numpy as np


SEED = 32120260908
PRIMES = (257, 1031, 4099, 16411, 65521)
SEEDS_PER_PRIME = 4
MAX_ACCEPTED_UPDATES = 256
SELECTED_STAGES = frozenset((0, 1, 2, 3, 4, 8, 16, 32, 64, 128, 256))
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024


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
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def derived_seed(prime, replicate):
    raw = f"{SEED}:{prime}:{replicate}".encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:8], "big")


def state_statistics(images, prime):
    counts = np.bincount(images, minlength=prime)
    z0 = int(counts[0])
    square_sum = int(np.dot(counts, counts))
    nonzero_support = int(np.count_nonzero(counts[1:]))
    drift_numerator = int(np.dot(counts[1:], counts[1:]))
    return counts, z0, square_sum, nonzero_support, drift_numerator


def run_replicate(prime, replicate):
    seed = derived_seed(prime, replicate)
    generator = random.Random(seed)
    images = np.arange(prime, dtype=np.int64)
    started = time.perf_counter()
    selected = []
    failures = []
    counts, z0, square_sum, support, drift_numerator = state_statistics(images, prime)
    selected.append(
        {
            "stage": 0,
            "z0": z0,
            "multiplicity_square_sum": square_sum,
            "nonzero_support_size": support,
            "expected_drift_numerator": drift_numerator,
            "expected_drift_denominator": prime * (prime - z0),
            "elapsed_seconds": time.perf_counter() - started,
        }
    )
    updates_completed = 0
    stop_reason = "update_cap"
    for stage in range(1, MAX_ACCEPTED_UPDATES + 1):
        nonzero_seed_indices = np.flatnonzero(images)
        if len(nonzero_seed_indices) == 0:
            stop_reason = "whole_field_zero"
            break
        selected_seed_index = int(
            nonzero_seed_indices[generator.randrange(len(nonzero_seed_indices))]
        )
        root = int(images[selected_seed_index])
        root_multiplicity = int(counts[root])
        expected_denominator = prime * (prime - z0)
        images = images * (images - root) % prime
        next_counts, next_z0, next_square_sum, next_support, next_drift = (
            state_statistics(images, prime)
        )
        if next_z0 != z0 + root_multiplicity:
            failures.append(
                {
                    "stage": stage,
                    "z0_before": z0,
                    "root": root,
                    "root_multiplicity": root_multiplicity,
                    "z0_after": next_z0,
                }
            )
            raise AssertionError("z0 drift identity failed")
        updates_completed = stage
        if stage in SELECTED_STAGES or next_z0 == prime:
            selected.append(
                {
                    "stage": stage,
                    "selected_seed_index": selected_seed_index,
                    "selected_root": root,
                    "selected_root_multiplicity": root_multiplicity,
                    "z0_before": z0,
                    "z0": next_z0,
                    "observed_z0_increment": next_z0 - z0,
                    "multiplicity_square_sum": next_square_sum,
                    "nonzero_support_size": next_support,
                    "expected_drift_numerator_before": drift_numerator,
                    "expected_drift_denominator_before": expected_denominator,
                    "elapsed_seconds": time.perf_counter() - started,
                }
            )
        counts = next_counts
        z0 = next_z0
        square_sum = next_square_sum
        support = next_support
        drift_numerator = next_drift
        if z0 == prime:
            stop_reason = "whole_field_zero"
            break
        if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 512 MiB")
    return {
        "prime": prime,
        "replicate": replicate,
        "seed": seed,
        "updates_completed": updates_completed,
        "stop_reason": stop_reason,
        "final_z0": z0,
        "final_nonzero_support_size": support,
        "final_multiplicity_square_sum": square_sum,
        "selected_stages": selected,
        "failures": failures,
        "elapsed_seconds": time.perf_counter() - started,
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
            "primes": PRIMES,
            "seeds_per_prime": SEEDS_PER_PRIME,
            "max_accepted_updates": MAX_ACCEPTED_UPDATES,
            "source_sha256": source_sha256(),
        },
    )
    try:
        for prime in PRIMES:
            assert is_prime(prime)
        rows = []
        for prime in PRIMES:
            print(json.dumps({"event": "prime_start", "prime": prime}), flush=True)
            prime_rows = [run_replicate(prime, replicate) for replicate in range(SEEDS_PER_PRIME)]
            rows.extend(prime_rows)
            print(
                json.dumps(
                    {
                        "event": "prime_complete",
                        "prime": prime,
                        "updates": [row["updates_completed"] for row in prime_rows],
                        "final_z0": [row["final_z0"] for row in prime_rows],
                    }
                ),
                flush=True,
            )
        payload = {
            "status": "passed",
            "experiment": "F321_adaptive_root_basins",
            "diagnostic": "conditional finite-field image-population process",
            "family": "route:F29",
            "seed": SEED,
            "primes": PRIMES,
            "primes_verified_offline": True,
            "seeds_per_prime": SEEDS_PER_PRIME,
            "max_accepted_updates": MAX_ACCEPTED_UPDATES,
            "scope_warning": (
                "This process samples a uniform seed conditioned on its current image "
                "being nonzero. It is not the law of surviving public composite runs "
                "without an additional survival-weighting proof."
            ),
            "drift_identity": (
                "Given counts c[a], expected increase of z0/p is "
                "sum_(a!=0)c[a]^2 / (p*(p-z0))."
            ),
            "source_sha256": source_sha256(),
            "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
            "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
            "memory_limit_bytes": MEMORY_LIMIT_BYTES,
            "rows": rows,
            "total_walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, payload)
        status = {
            key: payload[key]
            for key in (
                "status",
                "experiment",
                "diagnostic",
                "seed",
                "primes",
                "seeds_per_prime",
                "max_accepted_updates",
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
            "diagnostic": "conditional finite-field image-population process",
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
