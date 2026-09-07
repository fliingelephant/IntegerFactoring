#!/usr/bin/env python3
"""F330: exact small-remainder identities and frozen F326 path traces."""

import argparse
from bisect import bisect_left, bisect_right, insort
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time
import traceback


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
F326_DIR = ROOT / "experiments" / "F326_direct_gauss_pairing"
F326_SOURCE = F326_DIR / "direct_gauss_pairing.py"
F328_AGGREGATE = ROOT / "experiments" / "F328_capped_rabin_paths" / "aggregate_output.json"
F326_SOURCE_SHA256 = "7829cc45822021c64c42842a2c938b15c52df85e30ae694efcdd4171c5012f73"
F328_AGGREGATE_SHA256 = "840dd677cdb49e617f87824a9d5f414869dd36e50c95e2bf01c5a80dfdb9b7b7"
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 256 * 1024 * 1024
FROZEN_PATHS = (
    {
        "n": 209407403,
        "a": 71556651,
        "method": "rank_reflection",
        "cap": 32,
        "expected_endpoint_call": 7,
    },
    {
        "n": 209407403,
        "a": 6998896,
        "method": "delete_adjacent",
        "cap": 32,
        "expected_endpoint_call": 31,
    },
    {
        "n": 170611297,
        "a": 49354795,
        "method": "rank_reflection",
        "cap": 32,
        "expected_endpoint_call": 25,
    },
)

sys.path.insert(0, str(F326_DIR))
from direct_gauss_pairing import GaussPairing, auxiliary


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def peak_rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def write_json(path, value):
    target = Path(path)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(target)


def difference(after, before):
    return {
        key: after.get(key, 0) - before.get(key, 0)
        for key in sorted(set(after) | set(before))
        if after.get(key, 0) != before.get(key, 0)
    }


def check_reciprocity(limit=101):
    started = time.perf_counter()
    counts = Counter()
    maximum = None
    selected_examples = []
    for n in range(3, limit + 1, 2):
        h = (n - 1) // 2
        for a in range(1, n):
            if math.gcd(a, n) != 1:
                continue
            inverse_a = pow(a, -1, n)
            q_prefix = [0]
            for y in range(1, h + 1):
                residue = a * y % n
                q_prefix.append(q_prefix[-1] + int(1 <= residue <= h))
            inverse_images = []
            for t in range(1, h + 1):
                if t > 1:
                    insort(inverse_images, a * (t - 1) % n)

                def interval_count(lower, upper):
                    if lower > upper:
                        return 0
                    return bisect_right(inverse_images, upper) - bisect_left(
                        inverse_images, lower
                    )

                q_direct = q_prefix[t]
                centered_remainder = (a * t + h) % n - h
                assert centered_remainder != 0
                if centered_remainder > 0:
                    right = (
                        t
                        + 1
                        + interval_count(1, centered_remainder - 1)
                        - interval_count(h + 1, h + centered_remainder)
                    )
                    sign = "positive"
                    counts["positive_remainder_cases"] += 1
                else:
                    s = -centered_remainder
                    right = (
                        t
                        - 1
                        + interval_count(h + 1 - s, h)
                        - interval_count(n - s + 1, n - 1)
                    )
                    sign = "negative"
                    counts["negative_remainder_cases"] += 1
                left = 2 * q_direct
                assert left == right, (
                    n,
                    a,
                    inverse_a,
                    t,
                    centered_remainder,
                    left,
                    right,
                )
                discrepancy = left - t
                assert abs(discrepancy) <= abs(centered_remainder)
                if maximum is None or abs(discrepancy) > maximum["absolute_discrepancy"]:
                    maximum = {
                        "n": n,
                        "a": a,
                        "inverse_a": inverse_a,
                        "t": t,
                        "centered_remainder": centered_remainder,
                        "Q_t": q_direct,
                        "discrepancy": discrepancy,
                        "absolute_discrepancy": abs(discrepancy),
                    }
                if centered_remainder == 1:
                    assert q_direct == (t + 1) // 2
                    counts["remainder_plus_one_cases"] += 1
                    if len(selected_examples) < 10:
                        selected_examples.append(
                            {
                                "kind": "remainder_plus_one",
                                "n": n,
                                "a": a,
                                "t": t,
                                "Q_t": q_direct,
                            }
                        )
                elif centered_remainder == -1:
                    assert q_direct == t // 2
                    counts["remainder_minus_one_cases"] += 1
                    if len(selected_examples) < 10:
                        selected_examples.append(
                            {
                                "kind": "remainder_minus_one",
                                "n": n,
                                "a": a,
                                "t": t,
                                "Q_t": q_direct,
                            }
                        )
                counts["identity_checks"] += 1
                counts["interval_queries"] += 2
                counts["discrepancy_bound_checks"] += 1
            counts["unit_parameters"] += 1
            counts["inverse_image_updates"] += max(0, h - 1)
    return {
        "scope": (
            "Every odd N from 3 through 101, every unit a, and every "
            "1<=t<=(N-1)/2. Q is an independently accumulated direct residue "
            "count; interval counts use sorted inverse images."
        ),
        "limit": limit,
        "counts": dict(counts),
        "maximum_discrepancy": maximum,
        "selected_unit_remainder_examples": selected_examples,
        "walltime_seconds": time.perf_counter() - started,
    }


def reflection_rule(pairing, observer, image, next_coordinate):
    if image < 0:
        y = -image
        q_y = observer.Q(y)
        error = 2 * q_y - y
        predicted = (y + error) // 2
        assert predicted == q_y == next_coordinate
        return {
            "case": "negative_image",
            "y": y,
            "Q_y": q_y,
            "error": error,
            "formula": "next=Q(y)=(y+error)/2",
            "predicted_next_coordinate": predicted,
        }
    if image == 0:
        assert next_coordinate == 0
        return {
            "case": "zero_image",
            "formula": "next=0",
            "predicted_next_coordinate": 0,
        }
    if image <= pairing.L:
        selected = observer.select(pairing.L - image)
        y = -selected
        assert y > 0 and observer.Q(y) == image
        error = 2 * image - y
        predicted = -2 * image + error
        assert predicted == selected == next_coordinate
        return {
            "case": "positive_image_at_most_L",
            "z": image,
            "y": y,
            "Q_y": image,
            "error": error,
            "formula": "next=-y=-2*z+error",
            "predicted_next_coordinate": predicted,
        }
    predicted = pairing.d - image
    assert predicted == next_coordinate
    return {
        "case": "positive_image_above_L",
        "z": image,
        "formula": "next=d-z",
        "predicted_next_coordinate": predicted,
    }


def trace_path(specification):
    n = specification["n"]
    a = specification["a"]
    method = specification["method"]
    cap = specification["cap"]
    pairing = GaussPairing(n, a)
    observer = GaussPairing(n, a)
    setup_counts = dict(pairing.counters)
    current_rank = pairing.L
    trace = []
    output = None
    endpoint_call = None
    for step in range(1, cap + 1):
        before = dict(pairing.counters)
        coordinate = pairing.select(current_rank)
        coordinate_inverse = None
        if coordinate != 0 and math.gcd(coordinate, n) == 1:
            coordinate_inverse = pairing.rep(pow(coordinate, -1, n))
        image, branch = pairing.F(coordinate)
        row = {
            "step": step,
            "current_rank": current_rank,
            "current_coordinate": coordinate,
            "current_coordinate_inverse": coordinate_inverse,
            "F_image": image,
            "F_branch": branch,
        }
        if image == coordinate:
            output = pairing.decode(coordinate, branch)
            if "factor" in output:
                divisor = output["factor"]
                assert 1 < divisor < n and n % divisor == 0
                endpoint_type = "factor"
            else:
                root = output["root"]
                assert root * root % n == a
                endpoint_type = "root"
            endpoint_call = step
            row.update(
                {
                    "terminal": True,
                    "endpoint_type": endpoint_type,
                    "output": output,
                    "operation_delta": difference(pairing.counters, before),
                    "operation_counts_cumulative": dict(pairing.counters),
                }
            )
            trace.append(row)
            break

        image_rank = pairing.rank(image)
        next_rank = auxiliary(image_rank, pairing.L, pairing.d, method)
        next_coordinate = observer.select(next_rank)
        assert pairing.in_domain(next_coordinate)
        row.update(
            {
                "terminal": False,
                "F_image_rank": image_rank,
                "next_rank": next_rank,
                "next_coordinate": next_coordinate,
            }
        )
        if method == "rank_reflection":
            row["auxiliary_affine_rule"] = reflection_rule(
                pairing, observer, image, next_coordinate
            )
        elif image_rank == pairing.L:
            assert next_rank == pairing.L
            row["auxiliary_rule"] = {
                "case": "fixed_deleted_rank",
                "image_rank": image_rank,
            }
        else:
            compressed = image_rank if image_rank < pairing.L else image_rank - 1
            partner = compressed ^ 1
            row["auxiliary_rule"] = {
                "case": "delete_rank_L_then_xor_one",
                "compressed_image_rank": compressed,
                "compressed_partner": partner,
            }
        row["operation_delta"] = difference(pairing.counters, before)
        row["operation_counts_cumulative"] = dict(pairing.counters)
        trace.append(row)
        current_rank = next_rank
    assert endpoint_call == specification["expected_endpoint_call"]
    return {
        **specification,
        "h": pairing.h,
        "L": pairing.L,
        "d": pairing.d,
        "status": "completed",
        "endpoint_call": endpoint_call,
        "output": output,
        "setup_operation_counts": setup_counts,
        "path_operation_counts": difference(pairing.counters, setup_counts),
        "observer_validation_operation_counts": dict(observer.counters),
        "trace": trace,
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
    source_hash = sha256(Path(__file__))
    input_hashes = {
        "DESIGN.md": sha256(HERE / "DESIGN.md"),
        "F326_direct_gauss_pairing.py": sha256(F326_SOURCE),
        "F328_aggregate_output.json": sha256(F328_AGGREGATE),
    }
    running = {
        "status": "running",
        "experiment": "F330_short_path_conditions",
        "family": "route:F31",
        "source_sha256": source_hash,
        "input_hashes": input_hashes,
    }
    write_json(arguments.status, running)
    try:
        assert input_hashes["F326_direct_gauss_pairing.py"] == F326_SOURCE_SHA256
        assert input_hashes["F328_aggregate_output.json"] == F328_AGGREGATE_SHA256
        reciprocity = check_reciprocity()
        paths = [trace_path(specification) for specification in FROZEN_PATHS]
        payload = {
            **running,
            "status": "passed",
            "reciprocity": reciprocity,
            "frozen_paths": paths,
            "scope": (
                "Exact finite identity checks and deterministic reproduction "
                "of three already selected F328 paths. No frequency, sampling, "
                "or asymptotic path-length claim."
            ),
            "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
            "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
            "memory_limit_bytes": MEMORY_LIMIT_BYTES,
            "walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        if payload["peak_rss_bytes"] > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 256 MiB")
        write_json(arguments.output, payload)
        status = {
            key: payload[key]
            for key in (
                "status",
                "experiment",
                "family",
                "source_sha256",
                "input_hashes",
                "internal_timeout_seconds",
                "hard_timeout_seconds",
                "memory_limit_bytes",
                "walltime_seconds",
                "peak_rss_bytes",
            )
        }
        status["output"] = arguments.output
        write_json(arguments.status, status)
        print(
            json.dumps(
                {
                    "event": "passed",
                    **status,
                    "reciprocity_counts": reciprocity["counts"],
                    "paths": [
                        {
                            "n": path["n"],
                            "a": path["a"],
                            "method": path["method"],
                            "endpoint_call": path["endpoint_call"],
                            "output": path["output"],
                        }
                        for path in paths
                    ],
                },
                sort_keys=True,
            ),
            flush=True,
        )
    except BaseException as exception:
        failure = {
            **running,
            "status": "failed",
            "exception_type": type(exception).__name__,
            "exception": str(exception),
            "traceback": traceback.format_exc(),
            "walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, failure)
        write_json(arguments.status, failure)
        print(json.dumps({"event": "failed", **failure}, sort_keys=True), flush=True)
        raise
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    main()
