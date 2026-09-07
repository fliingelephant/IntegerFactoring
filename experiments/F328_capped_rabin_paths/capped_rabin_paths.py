#!/usr/bin/env python3
"""F328: charged capped Rabin attempts on the F326 arithmetic path."""

import argparse
from collections import Counter
import hashlib
import inspect
import json
import math
from pathlib import Path
import platform
import random
import resource
import signal
import sys
import time
import traceback


ROOT = Path(__file__).resolve().parents[2]
F326_DIR = ROOT / "experiments" / "F326_direct_gauss_pairing"
F326_SOURCE = F326_DIR / "direct_gauss_pairing.py"
F326_SOURCE_SHA256 = "7829cc45822021c64c42842a2c938b15c52df85e30ae694efcdd4171c5012f73"
sys.path.insert(0, str(F326_DIR))
from direct_gauss_pairing import (  # noqa: E402
    AUXILIARY_MATCHINGS,
    GaussPairing,
    auxiliary,
    brute_domain,
    jacobi,
    walk as frozen_f326_walk,
)


SEED = 32820260907
CAPS = (32, 128, 512, 2048)
TRIALS_PER_MODULUS = 16
INTERNAL_TIMEOUT_SECONDS = 25
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024
COST_KEYS = (
    "F_calls",
    "floor_sum_calls",
    "floor_sum_euclidean_iterations",
    "solver_gcd_calls",
    "generation_gcd_calls",
    "root_decode_gcd_calls",
    "total_gcd_calls",
    "modular_inversion_calls",
    "hidden_sampling_fair_bits",
    "matching_fair_bits",
    "total_fair_bits",
    "walltime_seconds",
)


def peak_rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    target = Path(path)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(target)


def derived_seed(*parts):
    raw = ":".join(str(part) for part in (SEED, *parts)).encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:16], "big")


def operation_counts(counter):
    raw = dict(counter)
    return {
        "F_calls": raw.get("F_calls", 0),
        "floor_sum_calls": raw.get("floor_sum_calls", 0),
        "floor_sum_euclidean_iterations": raw.get(
            "floor_sum_euclidean_iterations", 0
        ),
        "solver_gcd_calls": raw.get("F_gcd_calls", 0)
        + raw.get("decode_gcd_calls", 0),
        "modular_inversion_calls": raw.get("setup_modular_inversions", 0)
        + raw.get("F_modular_inversions", 0)
        + raw.get("decode_modular_inversions", 0),
        "rank_calls": raw.get("rank_calls", 0),
        "select_calls": raw.get("select_calls", 0),
        "select_binary_iterations": raw.get("select_binary_iterations", 0),
        "raw_pairing_counters": raw,
    }


def arithmetic_walk(n, a, method, cap):
    """Run one bounded path using no state other than public input and current rank."""
    assert n > 1 and n % 2 == 1
    assert 1 <= a < n and jacobi(a, n) == 1
    assert method in AUXILIARY_MATCHINGS and cap >= 1
    started = time.perf_counter()
    pairing = GaussPairing(n, a)
    assert pairing.d % 2 == 1
    setup_counts = dict(pairing.counters)
    current = pairing.L
    checkpoints = tuple(checkpoint for checkpoint in CAPS if checkpoint <= cap)
    snapshots = {}
    endpoint = None

    for step in range(1, cap + 1):
        coordinate = pairing.select(current)
        image, branch = pairing.F(coordinate)
        if image == coordinate:
            decoded = pairing.decode(coordinate, branch)
            if "factor" in decoded:
                divisor = decoded["factor"]
                if not (1 < divisor < n and n % divisor == 0):
                    raise ArithmeticError("F326 returned an invalid divisor")
                endpoint_type = "factor"
            else:
                root = decoded["root"]
                if root * root % n != a:
                    raise ArithmeticError("F326 returned an invalid square root")
                endpoint_type = "root"
            endpoint = {
                "step": step,
                "rank": current,
                "coordinate": coordinate,
                "branch": branch,
                "endpoint_type": endpoint_type,
                "output": decoded,
                "verified_exactly": True,
            }
        else:
            image_rank = pairing.rank(image)
            current = auxiliary(image_rank, pairing.L, pairing.d, method)

        if step in checkpoints:
            snapshots[step] = {
                "operation_counts": operation_counts(pairing.counters),
                "walltime_seconds": time.perf_counter() - started,
                "current_rank_after_step": None if endpoint else current,
            }
        if endpoint is not None:
            break

    elapsed = time.perf_counter() - started
    final_counts = operation_counts(pairing.counters)
    prefixes = {}
    for checkpoint in checkpoints:
        if endpoint is not None and endpoint["step"] <= checkpoint:
            prefixes[str(checkpoint)] = {
                "status": "completed",
                "charged_F_calls": endpoint["step"],
                "endpoint_type": endpoint["endpoint_type"],
                "endpoint_step": endpoint["step"],
                "operation_counts": final_counts,
                "walltime_seconds": elapsed,
                "current_rank_after_step": None,
            }
        else:
            snapshot = snapshots[checkpoint]
            prefixes[str(checkpoint)] = {
                "status": "censored_at_cap",
                "charged_F_calls": checkpoint,
                "endpoint_type": None,
                "endpoint_step": None,
                **snapshot,
            }

    return {
        "solver_interface": ["n", "a", "method", "cap"],
        "n": n,
        "a": a,
        "method": method,
        "cap": cap,
        "h": pairing.h,
        "L": pairing.L,
        "d": pairing.d,
        "status": "completed" if endpoint is not None else "censored_at_cap",
        "endpoint": endpoint,
        "F_calls": final_counts["F_calls"],
        "setup_operation_counts": setup_counts,
        "final_operation_counts": final_counts,
        "prefixes": prefixes,
        "walltime_seconds": elapsed,
        "state_scope": (
            "The transition retains one current rank. Four fixed-size prefix "
            "snapshots are measurement output, not path-search state."
        ),
    }


def sample_nonzero_residue(n, generator):
    bound = n - 1
    width = bound.bit_length()
    draws = 0
    while True:
        draws += 1
        value = generator.getrandbits(width)
        if value < bound:
            return value + 1, {
                "bit_width": width,
                "draws": draws,
                "rejections": draws - 1,
                "fair_bits": draws * width,
            }


def run_trial(n, modulus_id, target_bits, trial_index, max_cap):
    trial_started = time.perf_counter()
    hidden_seed = derived_seed("hidden", modulus_id, trial_index)
    coin_seed = derived_seed("matching", modulus_id, trial_index)
    hidden_generator = random.Random(hidden_seed)
    hidden_root, sampling = sample_nonzero_residue(n, hidden_generator)
    generation_divisor = math.gcd(hidden_root, n)
    after_generation = time.perf_counter()
    common = {
        "modulus_id": modulus_id,
        "target_bits": target_bits,
        "n": n,
        "trial_index": trial_index,
        "hidden_seed": hidden_seed,
        "matching_seed": coin_seed,
        "hidden_root": hidden_root,
        "hidden_sampling": sampling,
        "generation_gcd_calls": 1,
        "max_cap": max_cap,
    }

    if generation_divisor != 1:
        if not (1 < generation_divisor < n and n % generation_divisor == 0):
            raise ArithmeticError("generation gcd was not a proper divisor")
        elapsed = time.perf_counter() - trial_started
        outcomes = {}
        for cap in CAPS:
            if cap > max_cap:
                continue
            costs = {
                "F_calls": 0,
                "floor_sum_calls": 0,
                "floor_sum_euclidean_iterations": 0,
                "solver_gcd_calls": 0,
                "generation_gcd_calls": 1,
                "root_decode_gcd_calls": 0,
                "total_gcd_calls": 1,
                "modular_inversion_calls": 0,
                "hidden_sampling_fair_bits": sampling["fair_bits"],
                "matching_fair_bits": 0,
                "total_fair_bits": sampling["fair_bits"],
                "walltime_seconds": elapsed,
            }
            outcomes[str(cap)] = {
                "status": "factor_from_generation_gcd",
                "factor_success": True,
                "generation_factor": True,
                "direct_factor": False,
                "valid_root": False,
                "root_factor": False,
                "root_decoding_failure": False,
                "censored": False,
                "costs": costs,
            }
        return {
            **common,
            "a": None,
            "method": None,
            "matching_fair_bits": 0,
            "generation_factor": generation_divisor,
            "solver": None,
            "root_postprocessing": None,
            "final_status": "factor_from_generation_gcd",
            "accepted_factor": generation_divisor,
            "outcomes_by_cap": outcomes,
            "walltime_seconds": elapsed,
        }

    coin_generator = random.Random(coin_seed)
    coin = coin_generator.getrandbits(1)
    method = AUXILIARY_MATCHINGS[coin]
    a = hidden_root * hidden_root % n
    if jacobi(a, n) != 1:
        raise ArithmeticError("a hidden unit square failed its public checks")
    before_solver = time.perf_counter()
    pre_solver_walltime = before_solver - trial_started
    solver = arithmetic_walk(n, a, method, max_cap)
    endpoint = solver["endpoint"]
    accepted_factor = None
    root_postprocessing = None
    root_decode_walltime = 0.0
    if endpoint is None:
        final_status = "censored_at_max_cap"
    elif endpoint["endpoint_type"] == "factor":
        accepted_factor = endpoint["output"]["factor"]
        if not (1 < accepted_factor < n and n % accepted_factor == 0):
            raise ArithmeticError("outer validation rejected the direct divisor")
        final_status = "direct_factor"
    else:
        returned_root = endpoint["output"]["root"]
        if returned_root * returned_root % n != a:
            raise ArithmeticError("outer validation rejected the square root")
        decode_started = time.perf_counter()
        difference_gcd = math.gcd(returned_root - hidden_root, n)
        root_decode_walltime = time.perf_counter() - decode_started
        if 1 < difference_gcd < n:
            accepted_factor = difference_gcd
            final_status = "factor_from_valid_root"
        else:
            final_status = "valid_root_decoding_failure"
        root_postprocessing = {
            "returned_root": returned_root,
            "verified_square": True,
            "difference_gcd": difference_gcd,
            "gcd_calls": 1,
            "produced_proper_factor": accepted_factor is not None,
        }

    outcomes = {}
    for cap in CAPS:
        if cap > max_cap:
            continue
        prefix = solver["prefixes"][str(cap)]
        completed = prefix["status"] == "completed"
        valid_root = completed and prefix["endpoint_type"] == "root"
        direct_factor = completed and prefix["endpoint_type"] == "factor"
        root_factor = valid_root and accepted_factor is not None
        root_failure = valid_root and accepted_factor is None
        solver_counts = prefix["operation_counts"]
        root_gcd_calls = 1 if valid_root else 0
        costs = {
            "F_calls": solver_counts["F_calls"],
            "floor_sum_calls": solver_counts["floor_sum_calls"],
            "floor_sum_euclidean_iterations": solver_counts[
                "floor_sum_euclidean_iterations"
            ],
            "solver_gcd_calls": solver_counts["solver_gcd_calls"],
            "generation_gcd_calls": 1,
            "root_decode_gcd_calls": root_gcd_calls,
            "total_gcd_calls": 1
            + solver_counts["solver_gcd_calls"]
            + root_gcd_calls,
            "modular_inversion_calls": solver_counts["modular_inversion_calls"],
            "hidden_sampling_fair_bits": sampling["fair_bits"],
            "matching_fair_bits": 1,
            "total_fair_bits": sampling["fair_bits"] + 1,
            "walltime_seconds": pre_solver_walltime
            + prefix["walltime_seconds"]
            + (root_decode_walltime if valid_root else 0.0),
        }
        if not completed:
            status = "censored_at_cap"
        elif direct_factor:
            status = "direct_factor"
        elif root_factor:
            status = "factor_from_valid_root"
        else:
            status = "valid_root_decoding_failure"
        outcomes[str(cap)] = {
            "status": status,
            "factor_success": direct_factor or root_factor,
            "generation_factor": False,
            "direct_factor": direct_factor,
            "valid_root": valid_root,
            "root_factor": root_factor,
            "root_decoding_failure": root_failure,
            "censored": not completed,
            "endpoint_step": prefix["endpoint_step"],
            "unfinished_current_rank": prefix["current_rank_after_step"],
            "costs": costs,
        }

    return {
        **common,
        "a": a,
        "method": method,
        "matching_coin": coin,
        "matching_fair_bits": 1,
        "generation_factor": None,
        "pre_solver_walltime_seconds": pre_solver_walltime,
        "solver": solver,
        "root_postprocessing": root_postprocessing,
        "final_status": final_status,
        "accepted_factor": accepted_factor,
        "outcomes_by_cap": outcomes,
        "walltime_seconds": time.perf_counter() - trial_started,
    }


def summarize_trials(trials, caps):
    summaries = {}
    for cap in caps:
        outcomes = [trial["outcomes_by_cap"][str(cap)] for trial in trials]
        totals = {
            key: sum(outcome["costs"][key] for outcome in outcomes)
            for key in COST_KEYS
        }
        factors = sum(outcome["factor_success"] for outcome in outcomes)
        summary = {
            "attempts": len(outcomes),
            "solver_attempts": sum(trial["solver"] is not None for trial in trials),
            "generation_factor_successes": sum(
                outcome["generation_factor"] for outcome in outcomes
            ),
            "verified_direct_factor_outputs": sum(
                outcome["direct_factor"] for outcome in outcomes
            ),
            "verified_valid_root_outputs": sum(
                outcome["valid_root"] for outcome in outcomes
            ),
            "root_factor_successes": sum(
                outcome["root_factor"] for outcome in outcomes
            ),
            "root_decoding_failures": sum(
                outcome["root_decoding_failure"] for outcome in outcomes
            ),
            "censored_solver_attempts": sum(outcome["censored"] for outcome in outcomes),
            "total_factor_successes": factors,
            "matching_counts": dict(
                Counter(trial["method"] for trial in trials if trial["method"])
            ),
            "charged_cost_totals": totals,
        }
        if factors:
            summary["empirical_charged_cost_per_factor"] = {
                key: value / factors for key, value in totals.items()
            }
        summaries[str(cap)] = summary
    return summaries


def small_agreement_checks():
    assert sha256(F326_SOURCE) == F326_SOURCE_SHA256
    assert tuple(inspect.signature(arithmetic_walk).parameters) == (
        "n",
        "a",
        "method",
        "cap",
    )
    cases = ((15, 4), (21, 4), (35, 9), (77, 4))
    rows = []
    for n, a in cases:
        assert math.gcd(a, n) == 1 and jacobi(a, n) == 1
        domain, _ = brute_domain(n, a)
        for method in AUXILIARY_MATCHINGS:
            reference = frozen_f326_walk(n, a, method, n, domain)
            candidate = arithmetic_walk(n, a, method, n)
            assert reference["status"] == candidate["status"] == "completed"
            assert reference["F_calls"] == candidate["F_calls"]
            assert reference["fixed_coordinate"] == candidate["endpoint"]["coordinate"]
            assert reference["endpoint_type"] == candidate["endpoint"]["endpoint_type"]
            assert reference["output"] == candidate["endpoint"]["output"]
            rows.append(
                {
                    "n": n,
                    "a": a,
                    "method": method,
                    "F_calls": candidate["F_calls"],
                    "endpoint_type": candidate["endpoint"]["endpoint_type"],
                }
            )
    return {
        "status": "passed",
        "cases": len(rows),
        "scope": (
            "Four tiny composite inputs and both auxiliary methods agree exactly "
            "with the frozen F326 validated walk in stopping step, coordinate, "
            "endpoint type, and decoded output."
        ),
        "rows": rows,
    }


def load_moduli(path):
    payload = json.loads(Path(path).read_text())
    assert payload["status"] == "passed"
    seen_ids = set()
    for row in payload["moduli"]:
        assert row["modulus_id"] not in seen_ids
        seen_ids.add(row["modulus_id"])
        assert row["p_offline"] * row["q_offline"] == row["n"]
        assert row["p_offline"] != row["q_offline"]
        assert row["n"].bit_length() == row["actual_bits"] == row["target_bits"]
    return payload


def run_job(arguments, source_hash, log):
    input_payload = load_moduli(arguments.input)
    matches = [
        row for row in input_payload["moduli"] if row["modulus_id"] == arguments.modulus_id
    ]
    if len(matches) != 1:
        raise ValueError("modulus id does not identify exactly one input row")
    modulus = matches[0]
    if arguments.trial_start < 0 or arguments.trials < 1:
        raise ValueError("invalid trial range")
    if arguments.trial_start + arguments.trials > TRIALS_PER_MODULUS:
        raise ValueError("trial range exceeds the planned 16 trials")
    if arguments.max_cap not in CAPS:
        raise ValueError("max cap must be one of the retained caps")

    trials = []
    started = time.perf_counter()
    base = {
        "experiment": "F328_capped_rabin_paths",
        "mode": "run",
        "run_label": arguments.run_label,
        "seed": SEED,
        "modulus": modulus,
        "trial_start": arguments.trial_start,
        "requested_trials": arguments.trials,
        "max_cap": arguments.max_cap,
        "caps": [cap for cap in CAPS if cap <= arguments.max_cap],
        "source_sha256": source_hash,
        "f326_source_sha256": sha256(F326_SOURCE),
        "input_sha256": sha256(arguments.input),
        "solver_isolation": (
            "arithmetic_walk receives only N, a, method, and cap. Hidden r remains "
            "in this outer driver. Offline p,q are retained labels only."
        ),
        "sampling_contract": (
            "The ideal sampler draws ceil(log2(N-1)) fair bits and rejects values "
            "outside 0..N-2, then adds one. A separate fair bit selects the "
            "matching after a unit draw. This finite run replaces the fair bits "
            "with independently seeded Python Random.getrandbits streams."
        ),
        "python_version": platform.python_version(),
        "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
        "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
        "memory_limit_bytes": MEMORY_LIMIT_BYTES,
    }
    for trial_index in range(
        arguments.trial_start, arguments.trial_start + arguments.trials
    ):
        trial = run_trial(
            modulus["n"],
            modulus["modulus_id"],
            modulus["target_bits"],
            trial_index,
            arguments.max_cap,
        )
        trial["offline_labels"] = {
            "p_offline": modulus["p_offline"],
            "q_offline": modulus["q_offline"],
            "usage": "retained label; not supplied to arithmetic_walk",
        }
        trials.append(trial)
        partial = {
            **base,
            "status": "running",
            "completed_trials": len(trials),
            "trials": trials,
            "summary_by_cap": summarize_trials(trials, base["caps"]),
            "walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, partial)
        log(
            "trial_complete",
            modulus_id=modulus["modulus_id"],
            trial_index=trial_index,
            final_status=trial["final_status"],
            F_calls=trial["solver"]["F_calls"] if trial["solver"] else 0,
            walltime_seconds=trial["walltime_seconds"],
            peak_rss_bytes=peak_rss_bytes(),
        )
        if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 512 MiB")

    return {
        **base,
        "status": "passed",
        "completed_trials": len(trials),
        "trials": trials,
        "summary_by_cap": summarize_trials(trials, base["caps"]),
        "walltime_seconds": time.perf_counter() - started,
        "peak_rss_bytes": peak_rss_bytes(),
    }


def aggregate_jobs(arguments, source_hash):
    input_payload = load_moduli(arguments.input)
    input_hash = sha256(arguments.input)
    trials = []
    job_hashes = {}
    for job_path_text in arguments.job:
        job_path = Path(job_path_text)
        job = json.loads(job_path.read_text())
        assert job["status"] == "passed"
        assert job["input_sha256"] == input_hash
        assert job["source_sha256"] == source_hash
        job_hashes[job_path.name] = sha256(job_path)
        trials.extend(job["trials"])

    keys = [(trial["modulus_id"], trial["trial_index"]) for trial in trials]
    if len(keys) != len(set(keys)):
        raise ValueError("duplicate modulus/trial rows in aggregate inputs")
    trials.sort(key=lambda row: (row["target_bits"], row["modulus_id"], row["trial_index"]))
    coverage = {}
    by_modulus = {}
    by_scale = {}
    for modulus in input_payload["moduli"]:
        rows = [trial for trial in trials if trial["modulus_id"] == modulus["modulus_id"]]
        present = sorted(trial["trial_index"] for trial in rows)
        coverage[modulus["modulus_id"]] = {
            "present_trial_indices": present,
            "missing_trial_indices": [
                index for index in range(TRIALS_PER_MODULUS) if index not in present
            ],
        }
        by_modulus[modulus["modulus_id"]] = summarize_trials(rows, CAPS) if rows else {}
    for target_bits in sorted({row["target_bits"] for row in trials}):
        rows = [trial for trial in trials if trial["target_bits"] == target_bits]
        by_scale[str(target_bits)] = summarize_trials(rows, CAPS)

    return {
        "status": "passed",
        "experiment": "F328_capped_rabin_paths",
        "mode": "aggregate",
        "seed": SEED,
        "caps": CAPS,
        "planned_trials_per_modulus": TRIALS_PER_MODULUS,
        "modulus_count": len(input_payload["moduli"]),
        "trial_count": len(trials),
        "all_requested_trials_present": all(
            not value["missing_trial_indices"] for value in coverage.values()
        ),
        "coverage": coverage,
        "summary_by_cap": summarize_trials(trials, CAPS),
        "summary_by_scale_and_cap": by_scale,
        "summary_by_modulus_and_cap": by_modulus,
        "trials": trials,
        "input_sha256": input_hash,
        "job_sha256": job_hashes,
        "source_sha256": source_hash,
        "f326_source_sha256": sha256(F326_SOURCE),
        "cost_scope": (
            "Every cap charges every attempted prefix, including censored prefixes. "
            "Setup arithmetic is included. Generation gcd and exact-rejection bits "
            "are included for every outer attempt; root decoding gcd is included only "
            "after a verified root. Cost-per-factor fields exist only when that group "
            "has at least one verified factor success."
        ),
        "inference_scope": (
            "These are seeded finite measurements. Zero observed successes are not "
            "a probability bound, and no complexity theorem is inferred."
        ),
        "walltime_seconds": sum(
            trial["walltime_seconds"] for trial in trials
        ),
        "peak_rss_bytes": peak_rss_bytes(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("check", "run", "aggregate"), required=True)
    parser.add_argument("--input")
    parser.add_argument("--modulus-id")
    parser.add_argument("--trial-start", type=int, default=0)
    parser.add_argument("--trials", type=int, default=1)
    parser.add_argument("--max-cap", type=int, default=2048)
    parser.add_argument("--run-label", default="unspecified")
    parser.add_argument("--job", action="append", default=[])
    parser.add_argument("--output", required=True)
    parser.add_argument("--status", required=True)
    parser.add_argument("--log", required=True)
    arguments = parser.parse_args()
    started = time.perf_counter()
    source_hash = sha256(Path(__file__))
    if sha256(F326_SOURCE) != F326_SOURCE_SHA256:
        raise RuntimeError("the imported F326 source does not match its frozen hash")

    log_path = Path(arguments.log)
    log_path.write_text("")

    def log(event, **values):
        with log_path.open("a") as stream:
            stream.write(json.dumps({"event": event, **values}, sort_keys=True) + "\n")

    def timeout_handler(_signal_number, _frame):
        raise TimeoutError("internal 25-second alarm fired")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(INTERNAL_TIMEOUT_SECONDS)
    running = {
        "status": "running",
        "experiment": "F328_capped_rabin_paths",
        "mode": arguments.mode,
        "source_sha256": source_hash,
        "seed": SEED,
    }
    write_json(arguments.status, running)
    log("start", **running)
    try:
        if arguments.mode == "check":
            payload = {
                "status": "passed",
                "experiment": "F328_capped_rabin_paths",
                "mode": "check",
                "agreement": small_agreement_checks(),
                "source_sha256": source_hash,
                "f326_source_sha256": sha256(F326_SOURCE),
            }
        elif arguments.mode == "run":
            if not arguments.input or not arguments.modulus_id:
                parser.error("run mode requires --input and --modulus-id")
            payload = run_job(arguments, source_hash, log)
        else:
            if not arguments.input or not arguments.job:
                parser.error("aggregate mode requires --input and at least one --job")
            payload = aggregate_jobs(arguments, source_hash)
        payload["internal_timeout_seconds"] = INTERNAL_TIMEOUT_SECONDS
        payload["hard_timeout_seconds"] = HARD_TIMEOUT_SECONDS
        payload["memory_limit_bytes"] = MEMORY_LIMIT_BYTES
        payload["process_walltime_seconds"] = time.perf_counter() - started
        payload["peak_rss_bytes"] = peak_rss_bytes()
        if payload["peak_rss_bytes"] > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 512 MiB")
        write_json(arguments.output, payload)
        status = {
            key: payload[key]
            for key in (
                "status",
                "experiment",
                "mode",
                "source_sha256",
                "internal_timeout_seconds",
                "hard_timeout_seconds",
                "memory_limit_bytes",
                "process_walltime_seconds",
                "peak_rss_bytes",
            )
        }
        status["output"] = arguments.output
        write_json(arguments.status, status)
        log("passed", **status)
    except BaseException as exception:
        partial = {}
        if Path(arguments.output).exists():
            try:
                partial = json.loads(Path(arguments.output).read_text())
            except (OSError, json.JSONDecodeError):
                partial = {}
        failure = {
            **running,
            "status": "failed",
            "exception_type": type(exception).__name__,
            "exception": str(exception),
            "traceback": traceback.format_exc(),
            "partial_completed_trials": partial.get("trials", []),
            "next_trial_index": arguments.trial_start
            + len(partial.get("trials", [])),
            "process_walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, failure)
        write_json(arguments.status, failure)
        log("failed", **failure)
        raise
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    main()
