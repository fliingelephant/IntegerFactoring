#!/usr/bin/env python3
"""Aggregate and audit the eight retained F331 scale batches."""

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import resource
import signal
import sys
import time
import traceback


HERE = Path(__file__).resolve().parent
MODULUS_IDS = (
    "b20_i0",
    "b20_i1",
    "b28_i0",
    "b28_i1",
    "b36_i0",
    "b36_i1",
    "b44_i0",
    "b44_i1",
)
POLICIES = ("path", "uniform", "last")
TRIALS = 32
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024
COST_KEYS = (
    "F_calls",
    "floor_sum_calls",
    "floor_sum_euclidean_iterations",
    "rank_calls",
    "select_calls",
    "select_binary_iterations",
    "total_gcd_calls",
    "modular_inversion_calls",
    "modular_multiplication_calls",
    "integer_square_root_calls",
    "proposals",
)


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


def outcome_type(attempt):
    if attempt["controller"] is None:
        return "initial_generation_factor"
    final = attempt["controller"]["history"][-1]
    controller_type = final.get("outcome", {}).get("type")
    if attempt["status"] == "factor_from_pulled_back_root":
        return controller_type + "_outer_factor"
    if attempt["status"] == "pulled_back_root_decode_failure":
        return controller_type + "_outer_failure"
    return controller_type or attempt["status"]


def public_keys(value):
    keys = set()
    if isinstance(value, dict):
        for key, item in value.items():
            keys.add(key)
            keys.update(public_keys(item))
    elif isinstance(value, list):
        for item in value:
            keys.update(public_keys(item))
    return keys


def summarize(rows):
    totals = Counter()
    successes = [row for row in rows if row["factor_success"]]
    for row in rows:
        totals.update(row["total_costs"])
        totals["charged_walltime_microseconds"] += round(
            row["walltime_seconds"] * 1_000_000
        )
        totals["total_fair_bits"] += row["total_costs"].get(
            "hidden_random_fair_bits", 0
        ) + row["total_costs"].get("policy_random_fair_bits", 0)
    return {
        "attempts": len(rows),
        "factor_successes": len(successes),
        "hit_rate": len(successes) / len(rows),
        "status_counts": dict(Counter(row["status"] for row in rows)),
        "output_type_counts": dict(Counter(row["output_type"] for row in rows)),
        "cost_totals": dict(totals),
        "selected_cost_per_observed_factor": (
            {
                key: (
                    totals["charged_walltime_microseconds"]
                    / 1_000_000
                    / len(successes)
                    if key == "charged_walltime_seconds"
                    else totals[key] / len(successes)
                )
                for key in (*COST_KEYS, "total_fair_bits", "charged_walltime_seconds")
            }
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
    source_hash = sha256(Path(__file__))
    running = {
        "status": "running",
        "experiment": "F331_square_input_feedback",
        "mode": "aggregate",
        "family": "route:F31",
        "source_sha256": source_hash,
    }
    write_json(arguments.status, running)
    try:
        compact = []
        batch_hashes = {}
        expected_source = None
        expected_inputs = None
        paired_patterns = Counter()
        for modulus_id in MODULUS_IDS:
            path = HERE / f"batch_{modulus_id}_output.json"
            batch_hashes[path.name] = sha256(path)
            data = json.loads(path.read_text())
            assert data["status"] == "passed" and data["mode"] == "batch"
            assert data["modulus_scope"] == modulus_id
            assert data["trial_scope_inclusive"] == [0, TRIALS - 1]
            if expected_source is None:
                expected_source = data["source_sha256"]
                expected_inputs = data["input_hashes"]
            else:
                assert data["source_sha256"] == expected_source
                assert data["input_hashes"] == expected_inputs
            assert len(data["attempts"]) == TRIALS * len(POLICIES)
            seen = set()
            by_trial = defaultdict(dict)
            initial_by_trial = {}
            for attempt in data["attempts"]:
                key = (attempt["trial_index"], attempt["policy"])
                assert key not in seen
                seen.add(key)
                assert attempt["modulus_id"] == modulus_id
                assert 0 <= attempt["trial_index"] < TRIALS
                assert attempt["policy"] in POLICIES
                n = attempt["n"]
                assert attempt["p_offline"] * attempt["q_offline"] == n
                initial = attempt["initial"]
                initial_signature = (
                    initial["hidden_seed"],
                    initial["hidden_root"],
                    initial["a0"],
                    initial["generation_factor"],
                )
                if attempt["trial_index"] in initial_by_trial:
                    assert (
                        initial_by_trial[attempt["trial_index"]]
                        == initial_signature
                    )
                else:
                    initial_by_trial[attempt["trial_index"]] = initial_signature
                if initial["generation_factor"] is None:
                    assert initial["a0"] == initial["hidden_root"] ** 2 % n
                else:
                    divisor = initial["generation_factor"]
                    assert 1 < divisor < n and n % divisor == 0
                controller = attempt["controller"]
                if controller is not None:
                    assert "hidden_root" not in public_keys(controller)
                    a0 = initial["a0"]
                    for round_row in controller["history"]:
                        a = round_row["a"]
                        cumulative = round_row["cumulative_multiplier"]
                        assert a == a0 * cumulative * cumulative % n
                        if "next_a" in round_row:
                            next_cumulative = round_row[
                                "next_cumulative_multiplier"
                            ]
                            assert (
                                round_row["next_a"]
                                == a0 * next_cumulative * next_cumulative % n
                            )
                    if controller["root_of_a0"] is not None:
                        root = controller["root_of_a0"]
                        assert root * root % n == a0
                factor = attempt["accepted_factor"]
                if factor is not None:
                    assert 1 < factor < n and n % factor == 0
                    assert attempt["factor_success"]
                else:
                    assert not attempt["factor_success"]
                compact_row = {
                    "modulus_id": modulus_id,
                    "target_bits": attempt["target_bits"],
                    "n": n,
                    "trial_index": attempt["trial_index"],
                    "policy": attempt["policy"],
                    "status": attempt["status"],
                    "output_type": outcome_type(attempt),
                    "factor_success": attempt["factor_success"],
                    "accepted_factor": factor,
                    "rounds": attempt["total_costs"].get("rounds", 0),
                    "F_calls": attempt["total_costs"].get("F_calls", 0),
                    "proposals": attempt["total_costs"].get("proposals", 0),
                    "total_costs": attempt["total_costs"],
                    "walltime_seconds": attempt["walltime_seconds"],
                }
                compact.append(compact_row)
                by_trial[attempt["trial_index"]][attempt["policy"]] = compact_row
            assert len(seen) == TRIALS * len(POLICIES)
            assert len(initial_by_trial) == TRIALS
            for trial_index in range(TRIALS):
                policies = by_trial[trial_index]
                assert set(policies) == set(POLICIES)
                pattern = tuple(
                    int(policies[policy]["factor_success"]) for policy in POLICIES
                )
                paired_patterns[(modulus_id, pattern)] += 1
            del data
            if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
                raise MemoryError("peak RSS exceeded 512 MiB")

        assert len(compact) == len(MODULUS_IDS) * TRIALS * len(POLICIES)
        by_policy = {
            policy: summarize([row for row in compact if row["policy"] == policy])
            for policy in POLICIES
        }
        by_modulus_policy = {}
        for modulus_id in MODULUS_IDS:
            by_modulus_policy[modulus_id] = {
                policy: summarize(
                    [
                        row
                        for row in compact
                        if row["modulus_id"] == modulus_id
                        and row["policy"] == policy
                    ]
                )
                for policy in POLICIES
            }
        by_bits_policy = {}
        for target_bits in (20, 28, 36, 44):
            by_bits_policy[str(target_bits)] = {
                policy: summarize(
                    [
                        row
                        for row in compact
                        if row["target_bits"] == target_bits
                        and row["policy"] == policy
                    ]
                )
                for policy in POLICIES
            }
        payload = {
            **running,
            "status": "passed",
            "source_experiment_sha256": expected_source,
            "source_input_hashes": expected_inputs,
            "batch_hashes": batch_hashes,
            "coverage": {
                "moduli": len(MODULUS_IDS),
                "trials_per_modulus_policy": TRIALS,
                "policies": POLICIES,
                "attempts": len(compact),
            },
            "summary_by_policy": by_policy,
            "summary_by_modulus_and_policy": by_modulus_policy,
            "summary_by_bits_and_policy": by_bits_policy,
            "paired_success_patterns_by_modulus": [
                {
                    "modulus_id": modulus_id,
                    "pattern_path_uniform_last": list(pattern),
                    "count": count,
                }
                for (modulus_id, pattern), count in sorted(paired_patterns.items())
            ],
            "compact_attempts": compact,
            "scope": (
                "Exact audit and finite aggregation of all retained batches. "
                "Ratios with no observed success remain null. No pooled or "
                "per-scale value is an asymptotic estimate."
            ),
            "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
            "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
            "memory_limit_bytes": MEMORY_LIMIT_BYTES,
            "walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        if payload["peak_rss_bytes"] > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 512 MiB")
        write_json(arguments.output, payload)
        status = {
            key: payload[key]
            for key in (
                "status",
                "experiment",
                "mode",
                "family",
                "source_sha256",
                "coverage",
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
                    "summary_by_policy": by_policy,
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
