#!/usr/bin/env python3
"""F338: fair count branches on every frozen F336 source attempt."""

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
import gzip
import hashlib
import io
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


ROOT = Path(__file__).resolve().parents[2]
EXPERIMENT_DIR = ROOT / "experiments" / "F338_fair_count_branches"
F334_DIR = ROOT / "experiments" / "F334_count_descent"
F334_SOURCE = F334_DIR / "count_descent.py"
F336_DIR = ROOT / "experiments" / "F336_biased_rational_inputs"
F336_SOURCE = F336_DIR / "biased_rational_inputs.py"
F336_AGGREGATE = F336_DIR / "aggregate_output.json"
FAIR_BRANCH = F336_DIR / "FAIR_BRANCH.md"
FAIR_CHECKER = F336_DIR / "fair_branch_checks.py"
FAIR_DP_OUTPUT = F336_DIR / "fair_branch_scale.json"
F328_INPUT = ROOT / "experiments" / "F328_capped_rabin_paths" / "moduli.json"
DESIGN = EXPERIMENT_DIR / "DESIGN.md"

F334_SOURCE_SHA256 = (
    "cb93f160d57b2a3285551cbd268e732917e3062a90eb8ca62df843f581be1e24"
)
F336_SOURCE_SHA256 = (
    "b660db8da032e3f514dfdfc5a4183defb5392b22d4cf8bcfa4ab9eaec57c5256"
)
F336_AGGREGATE_SHA256 = (
    "afca015f15169be06a080b1e000d02409251d73d8c5df59cbd0b269ac18b3801"
)
FAIR_BRANCH_SHA256 = (
    "ce8c57e5c3dbbb8cedcfa6ad6b1001cffde5ec305d6bec29d63295ca5f58f507"
)
FAIR_CHECKER_SHA256 = (
    "46ad21c1911c516ad760fa61262895499b6ebb0ca9c97943585c619be4dfcd4e"
)
F328_INPUT_SHA256 = (
    "acf09b285c57c39cfcb93d3cd77addce909498e224955fd0ec9d2e4d86ee0428"
)
DESIGN_SHA256 = "d5879d6b995e85ce8d95d702b848f6c3c2dda13dc7aa24cd888c39fad66e4acb"

sys.path.insert(0, str(F334_DIR))
import count_descent as f334  # noqa: E402
sys.path.insert(0, str(F336_DIR))
import fair_branch_checks as fair_checks  # noqa: E402


SEED = 33820260907
ROUTE = "route:F31"
TRIALS_PER_PROFILE = 128
PROFILES_PER_TRIAL = 14
EXPECTED_SOURCE_ROWS = 12 * TRIALS_PER_PROFILE * PROFILES_PER_TRIAL
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024
RUN_PROGRESS = {}


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


def write_gzip_jsonl(path, rows):
    target = Path(path)
    temporary = target.with_suffix(target.suffix + ".tmp")
    with temporary.open("wb") as raw:
        with gzip.GzipFile(
            filename="", mode="wb", fileobj=raw, compresslevel=9, mtime=0
        ) as compressed:
            with io.TextIOWrapper(compressed, encoding="utf-8") as output:
                for row in rows:
                    output.write(
                        json.dumps(row, sort_keys=True, separators=(",", ":"))
                        + "\n"
                    )
    temporary.replace(target)


def read_gzip_jsonl(path):
    with gzip.open(path, "rt", encoding="utf-8") as source:
        return [json.loads(line) for line in source]


def derived_seed(row_id):
    raw = f"{SEED}:fair_branch:{row_id}".encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:16], "big")


def row_digest(row):
    encoded = json.dumps(row, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def add_counts(target, source):
    for key, value in source.items():
        if key.startswith("maximum_"):
            target[key] = max(target[key], value)
        else:
            target[key] += value


def fraction_record(numerator, denominator):
    if not denominator:
        return None
    value = Fraction(numerator, denominator)
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "decimal": float(value),
    }


def validate_dependencies():
    expected = {
        F334_SOURCE: F334_SOURCE_SHA256,
        F336_SOURCE: F336_SOURCE_SHA256,
        F336_AGGREGATE: F336_AGGREGATE_SHA256,
        FAIR_BRANCH: FAIR_BRANCH_SHA256,
        FAIR_CHECKER: FAIR_CHECKER_SHA256,
        F328_INPUT: F328_INPUT_SHA256,
        DESIGN: DESIGN_SHA256,
    }
    for source_file, expected_hash in expected.items():
        if sha256(source_file) != expected_hash:
            raise ArithmeticError(f"frozen dependency changed: {source_file}")
    if f334.CountOracle.floor_sum is not f334.GaussPairing.floor_sum:
        raise ArithmeticError("CountOracle is not using the frozen floor sum")


def load_moduli():
    data = json.loads(F328_INPUT.read_text())
    result = {}
    for row in data["moduli"]:
        if row["p_offline"] * row["q_offline"] != row["n"]:
            raise ArithmeticError("offline labels do not multiply to N")
        result[row["modulus_id"]] = row
    if len(result) != 12:
        raise ArithmeticError("expected twelve F328 moduli")
    return result


def source_catalog():
    aggregate = json.loads(F336_AGGREGATE.read_text())
    if aggregate["status"] != "passed":
        raise ArithmeticError("F336 aggregate is not passed")
    if aggregate["source_sha256"] != F336_SOURCE_SHA256:
        raise ArithmeticError("F336 aggregate has the wrong source hash")
    catalog = {}
    for job in aggregate["jobs"]:
        output_path = Path(job["output"])
        if sha256(output_path) != job["output_sha256"]:
            raise ArithmeticError("F336 job output hash changed")
        output = json.loads(output_path.read_text())
        if output["status"] != "passed":
            raise ArithmeticError("F336 source job is not passed")
        case = output["case"]
        modulus_id = case["modulus"]["modulus_id"]
        trial_range = tuple(case["trial_range"])
        artifact = output["row_artifact"]
        artifact_path = ROOT / artifact["path"]
        if sha256(artifact_path) != artifact["sha256"]:
            raise ArithmeticError("F336 row artifact hash changed")
        if artifact != job["row_artifact"]:
            raise ArithmeticError("F336 aggregate row reference changed")
        key = (modulus_id, *trial_range)
        if key in catalog:
            raise ArithmeticError("duplicate F336 source batch")
        catalog[key] = {
            "output_path": str(output_path),
            "output_sha256": job["output_sha256"],
            "row_artifact": artifact,
            "modulus": case["modulus"],
        }
    if len(catalog) != 24:
        raise ArithmeticError("expected 24 F336 source batches")
    return catalog


def load_source_rows(modulus_id, start, stop):
    catalog = source_catalog()
    matches = [
        source
        for (candidate_id, source_start, source_stop), source in catalog.items()
        if candidate_id == modulus_id
        and source_start <= start < stop <= source_stop
    ]
    if len(matches) != 1:
        raise ValueError("requested range is not inside one frozen F336 batch")
    source = matches[0]
    rows = [
        row
        for row in read_gzip_jsonl(ROOT / source["row_artifact"]["path"])
        if start <= row["trial_index"] < stop
    ]
    if len(rows) != PROFILES_PER_TRIAL * (stop - start):
        raise ArithmeticError("wrong F336 source row count")
    row_ids = [row["row_id"] for row in rows]
    if len(row_ids) != len(set(row_ids)):
        raise ArithmeticError("duplicate frozen row id")
    for row in rows:
        if row["modulus_id"] != modulus_id:
            raise ArithmeticError("source row has wrong modulus")
        if not start <= row["trial_index"] < stop:
            raise ArithmeticError("source row has wrong trial index")
    rows.sort(key=lambda row: (row["trial_index"], row["policy"]))
    return source, rows


def normalized_output(output):
    if isinstance(output, dict):
        return {
            key: normalized_output(value)
            for key, value in output.items()
            if key != "offline_factor_labels"
        }
    if isinstance(output, list):
        return [normalized_output(value) for value in output]
    return output


def output_factors(output):
    if not output:
        return []
    if "factor" in output:
        return [output["factor"]]
    return list(output["factors"])


def replay_minimum(source_row):
    if source_row["a"] is None:
        if source_row["output_type"] != "generation_factor":
            raise ArithmeticError("null multiplier was not a generation factor")
        return None
    modulus = source_row["modulus"]
    multiplier = source_row["a"]
    result = f334.run_descent(
        modulus,
        multiplier,
        "fixed_multiplier",
        f334.derived_seed("F338_min_replay", source_row["row_id"]),
        False,
    )
    if result["status"] != source_row["status"]:
        raise ArithmeticError("minimum replay status mismatch")
    if result["stopping_reason"] != source_row["stopping_reason"]:
        raise ArithmeticError("minimum replay stop mismatch")
    stopping_stage = result["trace"][-1]["stage"] if result["trace"] else None
    if stopping_stage != source_row["stopping_stage"]:
        raise ArithmeticError("minimum replay stage mismatch")
    defects = [row["defect"] for row in result["trace"] if "q" in row]
    if defects != source_row["defects"]:
        raise ArithmeticError("minimum replay defects mismatch")
    if result["stages_with_count"] != source_row["stages_with_count"]:
        raise ArithmeticError("minimum replay query count mismatch")
    if result["continued_stages"] != source_row["continued_stages"]:
        raise ArithmeticError("minimum replay continuation mismatch")
    if normalized_output(result["output"]) != normalized_output(
        source_row["verified_output"]
    ):
        raise ArithmeticError("minimum replay output mismatch")
    expected_type = "count_factor" if result["output"] else "stopping_failure"
    if expected_type != source_row["output_type"]:
        raise ArithmeticError("minimum replay output type mismatch")
    return result


def recover_source_transform_counts(source_row, minimum_result):
    original = source_row["algorithm_operation_counts"]
    minimum = minimum_result["operation_counts"] if minimum_result else {}
    additive = {}
    maximum_fields = {}
    for key in sorted(set(original) | set(minimum)):
        original_value = original.get(key, 0)
        minimum_value = minimum.get(key, 0)
        if key.startswith("maximum_"):
            maximum_fields[key] = {
                "original_combined": original_value,
                "minimum_descent": minimum_value,
                "source_transform_not_subtracted": True,
            }
            continue
        difference = original_value - minimum_value
        if difference < 0:
            raise ArithmeticError(f"negative recovered source counter: {key}")
        if difference:
            additive[key] = difference
    return additive, maximum_fields


def make_output(modulus, stage, hits):
    factors = sorted({hit["factor"] for hit in hits})
    for factor in factors:
        if not (1 < factor < modulus and modulus % factor == 0):
            raise ArithmeticError("fair branch produced an invalid factor")
    return {
        "factors": factors,
        "screen_hits": hits,
        "stage": stage,
        "output_type": "count_descent_gcd",
    }


def run_fair_descent(modulus, multiplier, branch_seed):
    if math.gcd(multiplier, modulus) != 1:
        raise ArithmeticError("fair descent multiplier is not a unit")
    started = time.perf_counter()
    oracle = f334.CountOracle(modulus, multiplier)
    generator = random.Random(branch_seed)
    counts = Counter()
    trace = []
    defects = []
    bit_digest = hashlib.sha256()
    t = (modulus - 1) // 2
    stage = 0

    def finish(status, reason, output):
        return {
            "status": status,
            "stopping_reason": reason,
            "output": output,
            "stopping_stage": trace[-1]["stage"] if trace else None,
            "stages_with_count": sum("q" in row for row in trace),
            "continued_stages": sum("branch_bit" in row for row in trace),
            "branch_seed": branch_seed,
            "branch_bits_sha256": bit_digest.hexdigest(),
            "defects": defects,
            "maximum_abs_defect": max(map(abs, defects)) if defects else None,
            "operation_counts": dict(sorted(counts.items())),
            "processing_walltime_seconds": time.perf_counter() - started,
            "trace": trace,
        }

    if t <= 1:
        return finish("stopping_failure", "t_at_most_one", None)

    while True:
        gcd_t = f334.charged_gcd(t, modulus, counts, "screen_t")
        if gcd_t > 1:
            counts["factor_verification_divisions"] += 1
            output = {
                "factor": gcd_t,
                "screen_source": "t",
                "screen_value": t,
                "stage": stage,
            }
            trace.append(
                {
                    "stage": stage,
                    "t": t,
                    "gcd_t": gcd_t,
                    "termination": "factor_at_t",
                }
            )
            return finish("success", "factor_at_t", output)

        before = dict(oracle.counters)
        q = oracle.Q(t)
        query_counts = f334.counter_delta(oracle.counters, before)
        add_counts(counts, query_counts)
        other = t - q
        defect = 2 * q - t
        defects.append(defect)
        hits = []
        gcd_q = None
        gcd_other = None
        if q:
            gcd_q = f334.charged_gcd(q, modulus, counts, "screen_q")
            if gcd_q > 1:
                counts["factor_verification_divisions"] += 1
                hits.append(
                    {
                        "factor": gcd_q,
                        "screen_source": "q",
                        "screen_value": q,
                        "stage": stage,
                    }
                )
        if other:
            gcd_other = f334.charged_gcd(
                other, modulus, counts, "screen_complement"
            )
            if gcd_other > 1:
                counts["factor_verification_divisions"] += 1
                hits.append(
                    {
                        "factor": gcd_other,
                        "screen_source": "t_minus_q",
                        "screen_value": other,
                        "stage": stage,
                    }
                )

        row = {
            "stage": stage,
            "t": t,
            "gcd_t": gcd_t,
            "q": q,
            "t_minus_q": other,
            "gcd_q": gcd_q,
            "gcd_t_minus_q": gcd_other,
            "defect": defect,
            "floor_sum_operation_counts": query_counts,
        }
        if hits:
            row["termination"] = "factor_at_child_count"
            trace.append(row)
            return finish(
                "success",
                "factor_at_child_count",
                make_output(modulus, stage, hits),
            )
        if q == 0 or other == 0:
            row["termination"] = "empty_side"
            trace.append(row)
            return finish("stopping_failure", "empty_side", None)

        branch_bit = generator.getrandbits(1)
        counts["branch_bit_draws"] += 1
        counts["branch_fair_bits"] += 1
        counts["random_bit_trials"] += 1
        counts["random_fair_bits"] += 1
        bit_digest.update(bytes((branch_bit,)))
        next_t = q if branch_bit == 0 else other
        if not 1 <= next_t < t:
            raise ArithmeticError("fair branch did not strictly decrease t")
        row["branch_bit"] = branch_bit
        row["selected_child"] = "q" if branch_bit == 0 else "t_minus_q"
        row["next_t"] = next_t
        if next_t <= 1:
            row["termination"] = "t_at_most_one"
            trace.append(row)
            return finish("stopping_failure", "t_at_most_one", None)
        row["termination"] = None
        trace.append(row)
        t = next_t
        stage += 1


def label_output(output, offline_factors):
    if not output:
        return
    output["offline_factor_labels"] = {
        str(factor): [prime for prime in offline_factors if factor % prime == 0]
        for factor in output_factors(output)
    }


def combine_fair_counts(
    source_counts,
    source_maximum_fields,
    fair_counts,
):
    combined = Counter()
    add_counts(combined, source_counts)
    add_counts(combined, fair_counts)
    for key, values in source_maximum_fields.items():
        combined[key] = max(
            values["original_combined"],
            fair_counts.get(key, 0),
        )
    return dict(sorted(combined.items()))


def transform_source_row(source_row, source_reference, offline_factors):
    started = time.perf_counter()
    digest = row_digest(source_row)
    branch_seed = derived_seed(source_row["row_id"])
    minimum = replay_minimum(source_row)
    source_counts, source_maximum = recover_source_transform_counts(
        source_row, minimum
    )
    if source_row["a"] is None:
        fair_result = {
            "status": "success",
            "stopping_reason": source_row["stopping_reason"],
            "output": source_row["verified_output"],
            "stopping_stage": None,
            "stages_with_count": 0,
            "continued_stages": 0,
            "branch_seed": branch_seed,
            "branch_bits_sha256": hashlib.sha256().hexdigest(),
            "defects": [],
            "maximum_abs_defect": None,
            "operation_counts": {},
            "processing_walltime_seconds": 0.0,
            "trace": [],
        }
        fair_output_type = "generation_factor"
    else:
        fair_result = run_fair_descent(
            source_row["modulus"], source_row["a"], branch_seed
        )
        label_output(fair_result["output"], offline_factors)
        fair_output_type = (
            "count_factor" if fair_result["output"] else "stopping_failure"
        )

    combined_counts = combine_fair_counts(
        source_counts,
        source_maximum,
        fair_result["operation_counts"],
    )
    result = {
        "row_id": source_row["row_id"],
        "source_row_sha256": digest,
        "source_row_artifact": source_reference["row_artifact"],
        "modulus_id": source_row["modulus_id"],
        "modulus": source_row["modulus"],
        "actual_bits": source_row["actual_bits"],
        "trial_index": source_row["trial_index"],
        "policy": source_row["policy"],
        "policy_kind": source_row["policy_kind"],
        "gamma": source_row["gamma"],
        "parameters": source_row["parameters"],
        "source_seeds": source_row["source_seeds"],
        "source_range": source_row["source_range"],
        "a": source_row["a"],
        "jacobi_sign": source_row["jacobi_sign"],
        "continued_fraction": source_row["continued_fraction"],
        "source_minimum": {
            "status": source_row["status"],
            "output_type": source_row["output_type"],
            "stopping_reason": source_row["stopping_reason"],
            "stopping_stage": source_row["stopping_stage"],
            "stages_with_count": source_row["stages_with_count"],
            "continued_stages": source_row["continued_stages"],
            "verified_output": source_row["verified_output"],
            "algorithm_operation_counts": source_row[
                "algorithm_operation_counts"
            ],
            "standalone_walltime_seconds_undecomposed": source_row[
                "standalone_walltime_seconds"
            ],
        },
        "minimum_descent_operation_counts": (
            minimum["operation_counts"] if minimum else {}
        ),
        "source_transform_operation_counts": dict(sorted(source_counts.items())),
        "source_transform_maximum_fields": source_maximum,
        "fair": {
            "status": fair_result["status"],
            "output_type": fair_output_type,
            "stopping_reason": fair_result["stopping_reason"],
            "first_hit_stage": (
                fair_result["stopping_stage"]
                if fair_result["output"] is not None
                else None
            ),
            "stopping_stage": fair_result["stopping_stage"],
            "stages_with_count": fair_result["stages_with_count"],
            "continued_stages": fair_result["continued_stages"],
            "branch_seed": branch_seed,
            "branch_bit_draws": fair_result["operation_counts"].get(
                "branch_bit_draws", 0
            ),
            "branch_bits_sha256": fair_result["branch_bits_sha256"],
            "defects": fair_result["defects"],
            "maximum_abs_defect": fair_result["maximum_abs_defect"],
            "verified_output": fair_result["output"],
            "descent_operation_counts": fair_result["operation_counts"],
            "algorithm_operation_counts": combined_counts,
        },
        "source_diagnostic_operation_counts": source_row[
            "diagnostic_operation_counts"
        ],
        "minimum_replay_match": True,
        "counter_recovery": (
            "Additive counters equal frozen standalone minus replayed minimum "
            "descent. Maximum fields are retained separately and never subtracted."
        ),
        "walltime_scope": (
            "The frozen minimum-policy wall time is undecomposed. F338 does not "
            "subtract it or claim a source-generation wall time."
        ),
        "f338_processing_walltime_seconds": (
            time.perf_counter() - started
        ),
        "anomalies": [],
    }
    witness = {
        "row_id": source_row["row_id"],
        "source_row_sha256": digest,
        "source_row": source_row,
        "minimum_replay_trace": minimum["trace"] if minimum else None,
        "fair_branch_seed": branch_seed,
        "fair_trace": fair_result["trace"],
        "counter_recovery": {
            "source_transform_operation_counts": dict(
                sorted(source_counts.items())
            ),
            "source_transform_maximum_fields": source_maximum,
            "minimum_descent_operation_counts": (
                minimum["operation_counts"] if minimum else {}
            ),
            "fair_descent_operation_counts": fair_result["operation_counts"],
            "fair_total_operation_counts": combined_counts,
        },
    }
    return result, witness


def cost_per_success(counts, successes):
    if not successes:
        return None
    return {
        key: fraction_record(value, successes)
        for key, value in sorted(counts.items())
        if value and not key.startswith("maximum_")
    }


def summarize_rows(rows):
    if not rows:
        raise ValueError("cannot summarize no rows")
    minimum_totals = Counter()
    fair_totals = Counter()
    source_totals = Counter()
    minimum_descent_totals = Counter()
    fair_descent_totals = Counter()
    minimum_types = Counter()
    fair_types = Counter()
    fair_stops = Counter()
    fair_success_stages = []
    for row in rows:
        add_counts(
            minimum_totals,
            row["source_minimum"]["algorithm_operation_counts"],
        )
        add_counts(fair_totals, row["fair"]["algorithm_operation_counts"])
        add_counts(source_totals, row["source_transform_operation_counts"])
        add_counts(
            minimum_descent_totals,
            row["minimum_descent_operation_counts"],
        )
        add_counts(
            fair_descent_totals,
            row["fair"]["descent_operation_counts"],
        )
        minimum_types[row["source_minimum"]["output_type"]] += 1
        fair_types[row["fair"]["output_type"]] += 1
        fair_stops[row["fair"]["stopping_reason"]] += 1
        if row["fair"]["first_hit_stage"] is not None:
            fair_success_stages.append(row["fair"]["first_hit_stage"])
    minimum_successes = (
        minimum_types["generation_factor"] + minimum_types["count_factor"]
    )
    fair_successes = fair_types["generation_factor"] + fair_types["count_factor"]
    comparison = {}
    for metric in (
        "Q_calls",
        "floor_sum_calls",
        "floor_sum_euclidean_iterations",
        "gcd_calls",
        "gcd_euclidean_divisions",
        "random_fair_bits",
        "branch_fair_bits",
        "modular_inversion_calls",
        "modular_inverse_euclidean_divisions",
    ):
        minimum_value = minimum_totals.get(metric, 0)
        fair_value = fair_totals.get(metric, 0)
        comparison[metric] = {
            "minimum_cost_per_success": fraction_record(
                minimum_value, minimum_successes
            ),
            "fair_cost_per_success": fraction_record(
                fair_value, fair_successes
            ),
            "fair_to_minimum_ratio": (
                fraction_record(
                    fair_value * minimum_successes,
                    minimum_value * fair_successes,
                )
                if minimum_successes
                and fair_successes
                and minimum_value
                and fair_value
                else None
            ),
        }
    return {
        "attempts": len(rows),
        "policy": rows[0]["policy"],
        "minimum": {
            "generation_factor_successes": minimum_types["generation_factor"],
            "count_factor_successes": minimum_types["count_factor"],
            "total_successes": minimum_successes,
            "output_type_counts": dict(sorted(minimum_types.items())),
            "algorithm_operation_totals": dict(sorted(minimum_totals.items())),
            "cost_per_observed_success": cost_per_success(
                minimum_totals, minimum_successes
            ),
        },
        "fair": {
            "generation_factor_successes": fair_types["generation_factor"],
            "count_factor_successes": fair_types["count_factor"],
            "total_successes": fair_successes,
            "output_type_counts": dict(sorted(fair_types.items())),
            "stopping_reason_counts": dict(sorted(fair_stops.items())),
            "algorithm_operation_totals": dict(sorted(fair_totals.items())),
            "cost_per_observed_success": cost_per_success(
                fair_totals, fair_successes
            ),
            "branch_bit_draws": fair_descent_totals.get(
                "branch_bit_draws", 0
            ),
            "first_hit_stage_minimum": (
                min(fair_success_stages) if fair_success_stages else None
            ),
            "first_hit_stage_maximum": (
                max(fair_success_stages) if fair_success_stages else None
            ),
            "first_hit_stage_mean": (
                statistics.fmean(fair_success_stages)
                if fair_success_stages
                else None
            ),
        },
        "source_transform_operation_totals": dict(sorted(source_totals.items())),
        "minimum_descent_operation_totals": dict(
            sorted(minimum_descent_totals.items())
        ),
        "fair_descent_operation_totals": dict(
            sorted(fair_descent_totals.items())
        ),
        "charged_cost_comparison": comparison,
        "rows_with_anomalies": sum(bool(row["anomalies"]) for row in rows),
    }


def summarize_case(rows, modulus_row, start, stop):
    by_policy = defaultdict(list)
    for row in rows:
        by_policy[row["policy"]].append(row)
    if len(by_policy) != PROFILES_PER_TRIAL:
        raise ArithmeticError("wrong number of F336 source profiles")
    expected = stop - start
    if set(map(len, by_policy.values())) != {expected}:
        raise ArithmeticError("wrong per-profile batch denominator")
    return {
        "modulus": modulus_row,
        "trial_range": [start, stop],
        "trials": expected,
        "policy_rows": len(rows),
        "policy_summaries": {
            policy: summarize_rows(policy_rows)
            for policy, policy_rows in sorted(by_policy.items())
        },
        "generation_factor_rows": sum(
            row["fair"]["output_type"] == "generation_factor" for row in rows
        ),
        "rows_with_anomalies": sum(bool(row["anomalies"]) for row in rows),
    }


def exact_small_tree(modulus, multiplier):
    oracle = f334.CountOracle(modulus, multiplier)
    state_rows = {}

    @lru_cache(None)
    def visit(t):
        if t <= 1:
            return {
                "success": Fraction(0),
                "queries": Fraction(0),
                "Q_calls": Fraction(0),
                "gcd_calls": Fraction(0),
                "branch_bits": Fraction(0),
                "maximum_queries": 0,
            }
        gcd_t = math.gcd(t, modulus)
        local_queries = 1
        local_q_calls = 0
        local_gcd_calls = 1
        if 1 < gcd_t < modulus:
            state_rows[t] = {
                "t": t,
                "gcd_t": gcd_t,
                "termination": "factor_at_t",
            }
            return {
                "success": Fraction(1),
                "queries": Fraction(local_queries),
                "Q_calls": Fraction(local_q_calls),
                "gcd_calls": Fraction(local_gcd_calls),
                "branch_bits": Fraction(0),
                "maximum_queries": 1,
            }
        q = oracle.Q(t)
        brute = sum(
            1 <= multiplier * y % modulus <= oracle.h
            for y in range(1, t + 1)
        )
        if q != brute:
            raise ArithmeticError("small tree CountOracle mismatch")
        other = t - q
        local_q_calls = 1
        gcd_q = math.gcd(q, modulus) if q else None
        gcd_other = math.gcd(other, modulus) if other else None
        local_gcd_calls += int(bool(q)) + int(bool(other))
        hit = (
            gcd_q is not None and 1 < gcd_q < modulus
        ) or (
            gcd_other is not None and 1 < gcd_other < modulus
        )
        state_rows[t] = {
            "t": t,
            "gcd_t": gcd_t,
            "q": q,
            "t_minus_q": other,
            "gcd_q": gcd_q,
            "gcd_t_minus_q": gcd_other,
            "termination": (
                "factor_at_child_count"
                if hit
                else "empty_side"
                if not q or not other
                else None
            ),
        }
        local = {
            "queries": Fraction(local_queries),
            "Q_calls": Fraction(local_q_calls),
            "gcd_calls": Fraction(local_gcd_calls),
        }
        if hit or not q or not other:
            return {
                "success": Fraction(int(hit)),
                **local,
                "branch_bits": Fraction(0),
                "maximum_queries": 1,
            }
        left = visit(q)
        right = visit(other)
        return {
            "success": (left["success"] + right["success"]) / 2,
            "queries": local["queries"]
            + (left["queries"] + right["queries"]) / 2,
            "Q_calls": local["Q_calls"]
            + (left["Q_calls"] + right["Q_calls"]) / 2,
            "gcd_calls": local["gcd_calls"]
            + (left["gcd_calls"] + right["gcd_calls"]) / 2,
            "branch_bits": Fraction(1)
            + (left["branch_bits"] + right["branch_bits"]) / 2,
            "maximum_queries": 1
            + max(left["maximum_queries"], right["maximum_queries"]),
        }

    leaves = []

    def expand(t, bits, probability, trace):
        if t <= 1:
            leaves.append(
                {
                    "branch_bits": bits,
                    "probability": str(probability),
                    "status": "stopping_failure",
                    "stopping_reason": "t_at_most_one",
                    "trace": trace,
                }
            )
            return
        row = state_rows[t]
        if row["termination"]:
            leaves.append(
                {
                    "branch_bits": bits,
                    "probability": str(probability),
                    "status": (
                        "success"
                        if row["termination"].startswith("factor")
                        else "stopping_failure"
                    ),
                    "stopping_reason": row["termination"],
                    "trace": [*trace, row],
                }
            )
            return
        for bit, child in ((0, row["q"]), (1, row["t_minus_q"])):
            branch_row = {
                **row,
                "branch_bit": bit,
                "selected_child": "q" if bit == 0 else "t_minus_q",
                "next_t": child,
            }
            expand(child, bits + str(bit), probability / 2, [*trace, branch_row])

    initial = (modulus - 1) // 2
    result = visit(initial)
    expand(initial, "", Fraction(1), [])
    return result, leaves, len(state_rows)


def run_small_controls():
    retained = json.loads(FAIR_DP_OUTPUT.read_text())
    frozen_examples = {
        (row["N"], row["a"]): row
        for row in retained["witnesses"]
        if (row["N"], row["a"]) in ((25, 8), (35, 4))
    }
    results = []
    for modulus, multiplier in ((25, 8), (35, 4)):
        exact, leaves, states = exact_small_tree(modulus, multiplier)
        active_fair, active_minimum, maximum, _, _ = fair_checks.compare(
            modulus, multiplier
        )
        coordinates = (
            "success",
            "queries",
            "Q_calls",
            "gcd_calls",
            "branch_bits",
        )
        for index, key in enumerate(coordinates):
            if exact[key] != active_fair[index]:
                raise ArithmeticError("active DP and F338 small tree disagree")
        witness = frozen_examples[(modulus, multiplier)]
        if exact["success"] != Fraction(witness["fair_success"]):
            raise ArithmeticError("small witness success changed")
        if exact["queries"] != Fraction(witness["fair_expected_queries"]):
            raise ArithmeticError("small witness query expectation changed")
        minimum = f334.run_descent(
            modulus,
            multiplier,
            "fixed_multiplier",
            0,
            False,
        )
        if minimum["status"] != "stopping_failure" or active_minimum[0]:
            raise ArithmeticError("small minimum branch was not the frozen failure")
        results.append(
            {
                "N": modulus,
                "a": multiplier,
                "fair_expectation": {
                    key: str(exact[key]) for key in coordinates
                },
                "maximum_path_queries": exact["maximum_queries"],
                "memoized_states": states,
                "terminal_paths": leaves,
                "minimum_result": {
                    "status": minimum["status"],
                    "stopping_reason": minimum["stopping_reason"],
                    "trace": minimum["trace"],
                },
                "active_DP_maximum_path_queries": maximum,
            }
        )
    return results


def select_witnesses(transformed, witness_by_row, keep_all):
    if keep_all:
        return [witness_by_row[row["row_id"]] for row in transformed]
    retained = []
    seen_outputs = set()
    for row in transformed:
        factors = tuple(output_factors(row["fair"]["verified_output"]))
        output_key = (
            row["modulus_id"],
            row["policy"],
            row["fair"]["output_type"],
            factors,
        )
        keep = False
        if row["fair"]["verified_output"] and output_key not in seen_outputs:
            seen_outputs.add(output_key)
            keep = True
        if row["anomalies"]:
            keep = True
        if keep:
            retained.append(witness_by_row[row["row_id"]])
    return retained


def artifact_record(path, rows):
    write_gzip_jsonl(path, rows)
    return {
        "path": str(path),
        "sha256": sha256(path),
        "rows": len(rows),
        "compressed_bytes": Path(path).stat().st_size,
    }


def transform_batch(modulus_id, start, stop, keep_all_traces):
    moduli = load_moduli()
    source_reference, source_rows = load_source_rows(modulus_id, start, stop)
    transformed = []
    witness_by_row = {}
    RUN_PROGRESS.update(
        {
            "modulus_id": modulus_id,
            "trial_range": [start, stop],
            "source_rows": len(source_rows),
            "completed_rows": 0,
        }
    )
    for source_row in source_rows:
        row, witness = transform_source_row(
            source_row,
            source_reference,
            [
                moduli[modulus_id]["p_offline"],
                moduli[modulus_id]["q_offline"],
            ],
        )
        transformed.append(row)
        witness_by_row[row["row_id"]] = witness
        RUN_PROGRESS["completed_rows"] = len(transformed)
        if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 512 MiB")
    witnesses = select_witnesses(
        transformed, witness_by_row, keep_all_traces
    )
    return (
        summarize_case(transformed, moduli[modulus_id], start, stop),
        transformed,
        witnesses,
        source_reference,
    )


def run_aggregate():
    moduli = load_moduli()
    output_paths = sorted(EXPERIMENT_DIR.glob("scale_b*_output.json"))
    if len(output_paths) != 24:
        raise ArithmeticError("aggregate requires 24 F338 scale jobs")
    jobs_by_modulus = defaultdict(list)
    job_records = []
    for output_path in output_paths:
        payload = json.loads(output_path.read_text())
        if payload["status"] != "passed" or payload["mode"] != "scale":
            raise ArithmeticError("F338 scale job is not passed")
        if payload["source_sha256"] != sha256(Path(__file__)):
            raise ArithmeticError("F338 scale job source hash mismatch")
        case = payload["case"]
        modulus_id = case["modulus"]["modulus_id"]
        row_artifact = payload["row_artifact"]
        row_path = Path(row_artifact["path"])
        if sha256(row_path) != row_artifact["sha256"]:
            raise ArithmeticError("F338 compact row hash mismatch")
        jobs_by_modulus[modulus_id].append((case["trial_range"], row_path))
        job_records.append(
            {
                "output": str(output_path),
                "output_sha256": sha256(output_path),
                "modulus_id": modulus_id,
                "trial_range": case["trial_range"],
                "row_artifact": row_artifact,
                "witness_artifact": payload["witness_artifact"],
                "walltime_seconds": payload["walltime_seconds"],
                "peak_rss_bytes": payload["peak_rss_bytes"],
            }
        )

    cases = []
    all_generation_rows = []
    for modulus_id in sorted(moduli):
        jobs = sorted(jobs_by_modulus[modulus_id])
        if [item[0] for item in jobs] != [[0, 64], [64, 128]]:
            raise ArithmeticError("F338 modulus coverage is incomplete")
        rows = []
        for _, row_path in jobs:
            rows.extend(read_gzip_jsonl(row_path))
        if len(rows) != PROFILES_PER_TRIAL * TRIALS_PER_PROFILE:
            raise ArithmeticError("wrong aggregate F338 row count")
        row_ids = [row["row_id"] for row in rows]
        if len(row_ids) != len(set(row_ids)):
            raise ArithmeticError("duplicate aggregate F338 row")
        cases.append(
            summarize_case(rows, moduli[modulus_id], 0, TRIALS_PER_PROFILE)
        )
        all_generation_rows.extend(
            row for row in rows
            if row["fair"]["output_type"] == "generation_factor"
        )

    shared_events = {
        (
            row["modulus_id"],
            row["trial_index"],
            json.dumps(row["source_seeds"], sort_keys=True),
            tuple(output_factors(row["fair"]["verified_output"])),
        )
        for row in all_generation_rows
    }
    total_rows = sum(case["policy_rows"] for case in cases)
    if total_rows != EXPECTED_SOURCE_ROWS:
        raise ArithmeticError("aggregate did not retain all F336 rows")
    return {
        "status": "passed",
        "experiment": "F338_fair_count_branches",
        "route": ROUTE,
        "mode": "aggregate",
        "source_attempt_law": (
            "All frozen F336 rows; direct/inverse paired generation rows remain "
            "standalone costs and are not independent discoveries."
        ),
        "total_policy_rows": total_rows,
        "generation_factor_rows": len(all_generation_rows),
        "distinct_shared_generation_events": len(shared_events),
        "cases": cases,
        "jobs": sorted(
            job_records,
            key=lambda row: (row["modulus_id"], row["trial_range"]),
        ),
        "scope": (
            "Finite per-input/profile comparison. Every failure is charged. "
            "Zero-success costs are null. No asymptotic inference."
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode", choices=("pilot", "scale", "aggregate"), required=True
    )
    parser.add_argument("--modulus-id")
    parser.add_argument("--start", type=int)
    parser.add_argument("--stop", type=int)
    parser.add_argument("--output", required=True)
    parser.add_argument("--status", required=True)
    parser.add_argument("--rows")
    parser.add_argument("--witnesses")
    arguments = parser.parse_args()
    started = time.perf_counter()
    validate_dependencies()

    def timeout_handler(_signal_number, _frame):
        raise TimeoutError("internal 28-second alarm fired")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(INTERNAL_TIMEOUT_SECONDS)
    running = {
        "status": "running",
        "experiment": "F338_fair_count_branches",
        "route": ROUTE,
        "mode": arguments.mode,
        "seed": SEED,
        "source_sha256": sha256(Path(__file__)),
    }
    write_json(arguments.status, running)
    try:
        if arguments.mode == "aggregate":
            payload = run_aggregate()
        else:
            if not arguments.rows or not arguments.witnesses:
                raise ValueError("row and witness artifacts are required")
            if arguments.mode == "pilot":
                small_controls = run_small_controls()
                cases = []
                all_rows = []
                all_witnesses = []
                source_references = []
                for modulus_id in ("b20_i0", "b20_i1"):
                    case, rows, witnesses, source_reference = transform_batch(
                        modulus_id, 0, 2, True
                    )
                    cases.append(case)
                    all_rows.extend(rows)
                    all_witnesses.extend(witnesses)
                    source_references.append(source_reference)
                payload = {
                    "status": "passed",
                    "experiment": "F338_fair_count_branches",
                    "route": ROUTE,
                    "mode": "pilot",
                    "small_controls": small_controls,
                    "cases": cases,
                    "source_references": source_references,
                    "row_artifact": artifact_record(arguments.rows, all_rows),
                    "witness_artifact": artifact_record(
                        arguments.witnesses, all_witnesses
                    ),
                }
            else:
                if not arguments.modulus_id:
                    raise ValueError("--modulus-id is required for scale")
                if (arguments.start, arguments.stop) not in (
                    (0, 64),
                    (64, 128),
                ):
                    raise ValueError("scale range must be one frozen 64-index batch")
                case, rows, witnesses, source_reference = transform_batch(
                    arguments.modulus_id,
                    arguments.start,
                    arguments.stop,
                    False,
                )
                payload = {
                    "status": "passed",
                    "experiment": "F338_fair_count_branches",
                    "route": ROUTE,
                    "mode": "scale",
                    "case": case,
                    "source_reference": source_reference,
                    "row_artifact": artifact_record(arguments.rows, rows),
                    "witness_artifact": artifact_record(
                        arguments.witnesses, witnesses
                    ),
                }
        signal.alarm(0)
        payload.update(
            {
                "seed": SEED,
                "source_sha256": sha256(Path(__file__)),
                "dependency_sha256": {
                    "F334_count_descent": F334_SOURCE_SHA256,
                    "F336_biased_rational_inputs": F336_SOURCE_SHA256,
                    "F336_aggregate": F336_AGGREGATE_SHA256,
                    "active_FAIR_BRANCH": FAIR_BRANCH_SHA256,
                    "active_fair_branch_checker": FAIR_CHECKER_SHA256,
                    "F328_moduli": F328_INPUT_SHA256,
                    "design": DESIGN_SHA256,
                },
                "counter_scope": (
                    "Source and transform operation counters are recovered by "
                    "verified additive subtraction. Maximum fields are separate. "
                    "Wall-clock values are never subtracted."
                ),
                "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
                "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
                "memory_limit_bytes": MEMORY_LIMIT_BYTES,
                "walltime_seconds": time.perf_counter() - started,
                "peak_rss_bytes": peak_rss_bytes(),
            }
        )
        if payload["peak_rss_bytes"] > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 512 MiB")
        write_json(arguments.output, payload)
        status = {
            key: payload[key]
            for key in (
                "status",
                "experiment",
                "route",
                "mode",
                "seed",
                "source_sha256",
                "internal_timeout_seconds",
                "hard_timeout_seconds",
                "memory_limit_bytes",
                "walltime_seconds",
                "peak_rss_bytes",
            )
        }
        status["output"] = arguments.output
        if "row_artifact" in payload:
            status["row_artifact"] = payload["row_artifact"]
            status["witness_artifact"] = payload["witness_artifact"]
        write_json(arguments.status, status)
        print(json.dumps({"event": "passed", **status}), flush=True)
    except TimeoutError as exception:
        signal.alarm(0)
        censored = {
            **running,
            "status": "censored",
            "censor_reason": "internal_timeout",
            "exception": str(exception),
            "progress": RUN_PROGRESS,
            "walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, censored)
        write_json(arguments.status, censored)
        print(json.dumps({"event": "censored", **censored}), flush=True)
    except BaseException as exception:
        signal.alarm(0)
        failed = {
            **running,
            "status": "failed",
            "exception_type": type(exception).__name__,
            "exception": str(exception),
            "traceback": traceback.format_exc(),
            "progress": RUN_PROGRESS,
            "walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, failed)
        write_json(arguments.status, failed)
        print(json.dumps({"event": "failed", **failed}), flush=True)
        raise


if __name__ == "__main__":
    main()
