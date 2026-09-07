#!/usr/bin/env python3
"""F334: exact gcd-screened count descent and public dyadic-menu controls."""

import argparse
from collections import Counter
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
EXPERIMENT_DIR = ROOT / "experiments" / "F334_count_descent"
F326_DIR = ROOT / "experiments" / "F326_direct_gauss_pairing"
F326_SOURCE = F326_DIR / "direct_gauss_pairing.py"
F326_SOURCE_SHA256 = "7829cc45822021c64c42842a2c938b15c52df85e30ae694efcdd4171c5012f73"
F328_INPUT = ROOT / "experiments" / "F328_capped_rabin_paths" / "moduli.json"
F328_INPUT_SHA256 = "acf09b285c57c39cfcb93d3cd77addce909498e224955fd0ec9d2e4d86ee0428"
F330_DESIGN = (
    ROOT / "experiments" / "F330_short_path_conditions" / "Q_DESCENT_DESIGN.md"
)
F330_DESIGN_SHA256 = "5453c6e1c4f43985158a2fd3db60d8c9acfd61e0fbedc72684de39fe1ed5858a"
F330_CF_NOTE = (
    ROOT / "experiments" / "F330_short_path_conditions" / "DISCREPANCY_NOTE.md"
)
F330_CF_NOTE_SHA256 = "ef1c19be8d814807b3132a508db0e39ac0fa9a2f0361b7e0d74ca99e72abdd50"

sys.path.insert(0, str(F326_DIR))
from direct_gauss_pairing import GaussPairing, jacobi as f326_jacobi  # noqa: E402


SEED = 33420260907
ROUTE = "route:F31"
CUTOFFS = (8, 32, 128)
ACCEPTED_PARAMETERS = 256
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024
METHODS = (
    "fixed_multiplier",
    "fresh_multiplier",
    "inverse_start_fixed_multiplier",
)
COST_KEYS = (
    "Q_calls",
    "K_calls",
    "floor_sum_calls",
    "floor_sum_euclidean_iterations",
    "gcd_calls",
    "gcd_euclidean_divisions",
    "jacobi_calls",
    "jacobi_outer_iterations",
    "jacobi_halvings",
    "jacobi_mod_reductions",
    "bounded_draw_calls",
    "random_bit_trials",
    "random_range_rejections",
    "random_fair_bits",
    "modular_inversion_calls",
    "modular_inverse_euclidean_divisions",
    "factor_verification_divisions",
)
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


def write_deterministic_gzip_jsonl(path, rows):
    target = Path(path)
    temporary = target.with_suffix(target.suffix + ".tmp")
    with temporary.open("wb") as raw:
        with gzip.GzipFile(
            filename="", mode="wb", fileobj=raw, compresslevel=9, mtime=0
        ) as compressed:
            with io.TextIOWrapper(compressed, encoding="utf-8") as text_output:
                for row in rows:
                    text_output.write(
                        json.dumps(row, sort_keys=True, separators=(",", ":"))
                        + "\n"
                    )
    temporary.replace(target)


def derived_seed(*parts):
    raw = ":".join(str(part) for part in (SEED, *parts)).encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:16], "big")


def add_counts(target, source):
    for key, value in source.items():
        if key.startswith("maximum_"):
            target[key] = max(target[key], value)
        else:
            target[key] += value


def counter_delta(after, before):
    return {
        key: after.get(key, 0) - before.get(key, 0)
        for key in sorted(set(after) | set(before))
        if after.get(key, 0) != before.get(key, 0)
    }


def fraction_record(numerator, denominator):
    return {
        "numerator": numerator,
        "denominator": denominator,
        "decimal": numerator / denominator if denominator else None,
    }


def charged_gcd(value, modulus, counters, category):
    counters["gcd_calls"] += 1
    counters[f"{category}_gcd_calls"] += 1
    counters["maximum_gcd_operand_bits"] = max(
        counters["maximum_gcd_operand_bits"],
        abs(value).bit_length(),
        modulus.bit_length(),
    )
    left, right = abs(value), modulus
    divisions = 0
    while right:
        left, right = right, left % right
        divisions += 1
    counters["gcd_euclidean_divisions"] += divisions
    counters[f"{category}_gcd_euclidean_divisions"] += divisions
    return left


def charged_mod_inverse(value, modulus, counters, category):
    counters["modular_inversion_calls"] += 1
    counters[f"{category}_modular_inversion_calls"] += 1
    old_r, current_r = modulus, value % modulus
    old_s, current_s = 0, 1
    divisions = 0
    while current_r:
        quotient = old_r // current_r
        old_r, current_r = current_r, old_r - quotient * current_r
        old_s, current_s = current_s, old_s - quotient * current_s
        divisions += 1
    if old_r != 1:
        raise ArithmeticError("modular inverse requested for a nonunit")
    counters["modular_inverse_euclidean_divisions"] += divisions
    counters[f"{category}_modular_inverse_euclidean_divisions"] += divisions
    return old_s % modulus


def charged_jacobi(value, modulus, counters, validate):
    counters["jacobi_calls"] += 1
    original_value = value
    original_modulus = modulus
    value %= modulus
    counters["jacobi_mod_reductions"] += 1
    result = 1
    while value:
        counters["jacobi_outer_iterations"] += 1
        while value % 2 == 0:
            value //= 2
            counters["jacobi_halvings"] += 1
            if modulus % 8 in (3, 5):
                result = -result
        value, modulus = modulus, value
        counters["jacobi_swaps"] += 1
        if value % 4 == modulus % 4 == 3:
            result = -result
        value %= modulus
        counters["jacobi_mod_reductions"] += 1
    result = result if modulus == 1 else 0
    if validate and result != f326_jacobi(original_value, original_modulus):
        raise ArithmeticError("charged Jacobi disagrees with frozen F326")
    return result


def bounded_sample(generator, bound, counters):
    if bound < 1:
        raise ValueError("positive sampling bound required")
    width = (bound - 1).bit_length()
    counters["bounded_draw_calls"] += 1
    while True:
        counters["random_bit_trials"] += 1
        counters["random_fair_bits"] += width
        value = generator.getrandbits(width)
        if value < bound:
            return value
        counters["random_range_rejections"] += 1


def sample_parameter_event(modulus, generator, category, validate):
    started = time.perf_counter()
    counts = Counter()
    rejected_jacobi = 0
    while True:
        candidate = bounded_sample(generator, modulus - 1, counts) + 1
        divisor = charged_gcd(candidate, modulus, counts, category)
        if divisor > 1:
            if not (1 < divisor < modulus and modulus % divisor == 0):
                raise ArithmeticError("parameter generation produced an invalid factor")
            counts["factor_verification_divisions"] += 1
            return {
                "status": "factor",
                "candidate": candidate,
                "factor": divisor,
                "rejected_jacobi_draws": rejected_jacobi,
                "operation_counts": dict(sorted(counts.items())),
                "walltime_seconds": time.perf_counter() - started,
            }
        symbol = charged_jacobi(candidate, modulus, counts, validate)
        if symbol == 1:
            return {
                "status": "accepted",
                "a": candidate,
                "rejected_jacobi_draws": rejected_jacobi,
                "operation_counts": dict(sorted(counts.items())),
                "walltime_seconds": time.perf_counter() - started,
            }
        if symbol != -1:
            raise ArithmeticError("unit parameter had a nonunit Jacobi value")
        rejected_jacobi += 1
        counts["jacobi_negative_rejections"] += 1


def generate_initial_parameter(modulus, modulus_id, accepted_index, validate):
    stream_seed = derived_seed("initial_parameter", modulus_id, accepted_index)
    generator = random.Random(stream_seed)
    factor_events = []
    event_index = 0
    while True:
        event = sample_parameter_event(
            modulus, generator, "initial_generation", validate
        )
        event["event_index"] = event_index
        event_index += 1
        if event["status"] == "factor":
            factor_events.append(event)
            continue
        return {
            "stream_seed": stream_seed,
            "factor_events": factor_events,
            "accepted_event": event,
            "a": event["a"],
        }


class CountOracle:
    """Use the frozen F326 Q, K, and floor_sum method objects without graph setup."""

    floor_sum = GaussPairing.floor_sum
    K = GaussPairing.K
    Q = GaussPairing.Q

    def __init__(self, modulus, multiplier):
        self.n = modulus
        self.a = multiplier % modulus
        self.h = (modulus - 1) // 2
        self.counters = Counter()


def continued_fraction_sum(multiplier, modulus, counters):
    counters["continued_fraction_calls"] += 1
    left, right = modulus, multiplier
    quotient_sum = 0
    last_quotient = None
    divisions = 0
    while right:
        quotient, remainder = divmod(left, right)
        quotient_sum += quotient
        last_quotient = quotient
        left, right = right, remainder
        divisions += 1
    if left != 1 or last_quotient is None or last_quotient < 2:
        raise ArithmeticError("noncanonical continued fraction for a unit")
    counters["continued_fraction_euclidean_divisions"] += divisions
    counters["continued_fraction_quotient_sum"] += quotient_sum
    return quotient_sum


def signed_rep(value, modulus):
    half = (modulus - 1) // 2
    return (value + half) % modulus - half


def validate_small_count(multiplier, modulus, t, q, counters):
    half = (modulus - 1) // 2
    brute = 0
    for y in range(1, t + 1):
        counters["brute_Q_membership_tests"] += 1
        residue = multiplier * y % modulus
        brute += 1 <= residue <= half
    if brute != q:
        raise ArithmeticError("frozen floor sum disagrees with brute Q")

    inverse = pow(multiplier, -1, modulus)
    counters["reciprocity_validation_modular_inversions"] += 1
    remainder = signed_rep(multiplier * t, modulus)

    def count_interval(lower, upper):
        total = 0
        if lower > upper:
            return total
        for value in range(lower, upper + 1):
            counters["reciprocity_membership_tests"] += 1
            preimage = inverse * value % modulus
            total += 1 <= preimage <= t - 1
        return total

    if remainder > 0:
        right_side = (
            t
            + 1
            + count_interval(1, remainder - 1)
            - count_interval(half + 1, half + remainder)
        )
    else:
        size = -remainder
        right_side = (
            t
            - 1
            + count_interval(half + 1 - size, half)
            - count_interval(modulus - size + 1, modulus - 1)
        )
    if 2 * q != right_side:
        raise ArithmeticError("signed-remainder count identity failed")


def make_factor_output(modulus, source, value, divisor, stage, counts):
    if not (1 < divisor < modulus and modulus % divisor == 0):
        raise ArithmeticError("descent returned an invalid factor")
    counts["factor_verification_divisions"] += 1
    return {
        "factor": divisor,
        "screen_source": source,
        "screen_value": value,
        "stage": stage,
    }


def run_descent(
    modulus,
    initial_a,
    method,
    fresh_seed,
    validate_small,
):
    started = time.perf_counter()
    operation_counts = Counter()
    validation_counts = Counter()
    trace = []
    cf_cache = {}
    half = (modulus - 1) // 2

    if method == "inverse_start_fixed_multiplier":
        inverse = charged_mod_inverse(
            initial_a, modulus, operation_counts, "inverse_start"
        )
        t = min(inverse, modulus - inverse)
    else:
        t = half
    initial_t = t

    fixed_oracle = (
        CountOracle(modulus, initial_a)
        if method != "fresh_multiplier"
        else None
    )
    fresh_generator = (
        random.Random(fresh_seed) if method == "fresh_multiplier" else None
    )
    current_a = initial_a
    maximum_abs_defect = None
    continued_stages = 0

    def finish(status, stopping_reason, output):
        return {
            "method": method,
            "status": status,
            "stopping_reason": stopping_reason,
            "initial_a": initial_a,
            "initial_t": initial_t,
            "fresh_stream_seed": fresh_seed,
            "output": output,
            "stages_with_count": sum("q" in row for row in trace),
            "continued_stages": continued_stages,
            "maximum_abs_defect": maximum_abs_defect,
            "distinct_cf_sums": [
                {"a": a, "S": value} for a, value in sorted(cf_cache.items())
            ],
            "operation_counts": dict(sorted(operation_counts.items())),
            "validation_counts": dict(sorted(validation_counts.items())),
            "walltime_seconds": time.perf_counter() - started,
            "trace": trace,
        }

    if t <= 1:
        return finish("stopping_failure", "t_at_most_one", None)

    stage = 0
    while True:
        parameter_event = None
        if method == "fresh_multiplier" and stage > 0:
            parameter_event = sample_parameter_event(
                modulus, fresh_generator, "fresh_generation", validate_small
            )
            add_counts(operation_counts, parameter_event["operation_counts"])
            if parameter_event["status"] == "factor":
                output = {
                    "factor": parameter_event["factor"],
                    "screen_source": "fresh_parameter_generation",
                    "screen_value": parameter_event["candidate"],
                    "stage": stage,
                }
                trace.append(
                    {
                        "stage": stage,
                        "t": t,
                        "parameter_generation": parameter_event,
                        "termination": "fresh_parameter_generation_factor",
                    }
                )
                return finish("success", "fresh_parameter_generation_factor", output)
            current_a = parameter_event["a"]

        gcd_t = charged_gcd(t, modulus, operation_counts, "screen_t")
        if gcd_t > 1:
            output = make_factor_output(
                modulus, "t", t, gcd_t, stage, operation_counts
            )
            trace.append(
                {
                    "stage": stage,
                    "t": t,
                    "a": current_a,
                    "parameter_generation": parameter_event,
                    "gcd_t": gcd_t,
                    "termination": "factor_at_t",
                }
            )
            return finish("success", "factor_at_t", output)

        if current_a not in cf_cache:
            cf_cache[current_a] = continued_fraction_sum(
                current_a, modulus, validation_counts
            )
        cf_sum = cf_cache[current_a]

        oracle = (
            CountOracle(modulus, current_a)
            if method == "fresh_multiplier"
            else fixed_oracle
        )
        before = dict(oracle.counters)
        q = oracle.Q(t)
        query_counts = counter_delta(oracle.counters, before)
        add_counts(operation_counts, query_counts)
        other = t - q
        defect = 2 * q - t
        remainder = signed_rep(current_a * t, modulus)
        if remainder == 0:
            raise ArithmeticError("unit multiplier produced zero signed remainder")
        if abs(defect) > abs(remainder):
            raise ArithmeticError("small-remainder defect bound failed")
        if abs(defect) > 10 * cf_sum:
            raise ArithmeticError("continued-fraction defect bound failed")
        if validate_small:
            validate_small_count(
                current_a, modulus, t, q, validation_counts
            )
        maximum_abs_defect = (
            abs(defect)
            if maximum_abs_defect is None
            else max(maximum_abs_defect, abs(defect))
        )

        if method == "inverse_start_fixed_multiplier" and stage == 0:
            if remainder not in (-1, 1):
                raise ArithmeticError("inverse start did not have remainder +/-1")
            expected = (t + 1) // 2 if remainder == 1 else t // 2
            if q != expected:
                raise ArithmeticError("inverse-start first count identity failed")

        child_hits = []
        gcd_q = None
        gcd_other = None
        if q:
            gcd_q = charged_gcd(q, modulus, operation_counts, "screen_q")
            if gcd_q > 1:
                child_hits.append(
                    make_factor_output(
                        modulus, "q", q, gcd_q, stage, operation_counts
                    )
                )
        if other:
            gcd_other = charged_gcd(
                other, modulus, operation_counts, "screen_complement"
            )
            if gcd_other > 1:
                child_hits.append(
                    make_factor_output(
                        modulus,
                        "t_minus_q",
                        other,
                        gcd_other,
                        stage,
                        operation_counts,
                    )
                )

        next_t = min(q, other)
        if next_t != (t - abs(defect)) // 2:
            raise ArithmeticError("defect child identity failed")
        if q and other and next_t > t // 2:
            raise ArithmeticError("continuing stage did not halve t")

        row = {
            "stage": stage,
            "t": t,
            "a": current_a,
            "parameter_generation": parameter_event,
            "gcd_t": gcd_t,
            "q": q,
            "t_minus_q": other,
            "gcd_q": gcd_q,
            "gcd_t_minus_q": gcd_other,
            "defect": defect,
            "signed_remainder": remainder,
            "cf_sum": cf_sum,
            "floor_sum_operation_counts": query_counts,
            "next_t": next_t,
        }

        if child_hits:
            output = {
                "factors": sorted({hit["factor"] for hit in child_hits}),
                "screen_hits": child_hits,
                "stage": stage,
            }
            if method == "inverse_start_fixed_multiplier" and stage == 0:
                for hit in child_hits:
                    relations = []
                    divisor = hit["factor"]
                    validation_counts["inverse_start_relation_modulo_tests"] += 2
                    if (initial_a - 1) % divisor == 0:
                        relations.append("divides_a_minus_1")
                    if (initial_a + 1) % divisor == 0:
                        relations.append("divides_a_plus_1")
                    hit["inverse_start_first_count_relations"] = relations
                output["output_type"] = "inverse_start_first_count_gcd_reproduction"
            else:
                output["output_type"] = "count_descent_gcd"
            row["termination"] = "factor_at_child_count"
            trace.append(row)
            return finish("success", "factor_at_child_count", output)

        if q == 0 or other == 0:
            row["termination"] = "empty_side"
            trace.append(row)
            return finish("stopping_failure", "empty_side", None)

        continued_stages += 1
        if next_t > t // 2:
            raise ArithmeticError("halving invariant failed")
        row["termination"] = None
        trace.append(row)
        t = next_t
        stage += 1
        if stage > initial_t.bit_length():
            raise ArithmeticError("count descent exceeded logarithmic stage bound")
        if t <= 1:
            return finish("stopping_failure", "t_at_most_one", None)


def dyadic_candidates(initial_t, cutoff, global_half):
    if cutoff <= 0:
        raise ValueError("dyadic cutoff must be positive")
    candidates = set()
    raw_integer_count = 0
    stage_count = max(0, initial_t.bit_length() - 1)
    for stage in range(stage_count):
        denominator = 1 << (stage + 1)
        lower_numerator = initial_t - cutoff * denominator
        lower = -((-lower_numerator) // denominator)
        upper = (initial_t + (cutoff // 2) * denominator) // denominator
        lower = max(1, lower)
        upper = min(global_half, upper)
        if lower <= upper:
            raw_integer_count += upper - lower + 1
            candidates.update(range(lower, upper + 1))
    return sorted(candidates), raw_integer_count, stage_count


def run_menu(modulus, initial_t, cutoff, menu_kind):
    started = time.perf_counter()
    candidates, raw_integer_count, stage_count = dyadic_candidates(
        initial_t, cutoff, (modulus - 1) // 2
    )
    counts = Counter()
    hits = []
    digest = hashlib.sha256()
    for candidate in candidates:
        digest.update(str(candidate).encode())
        digest.update(b",")
        divisor = charged_gcd(candidate, modulus, counts, "menu")
        if 1 < divisor < modulus:
            if modulus % divisor:
                raise ArithmeticError("menu gcd did not divide modulus")
            counts["factor_verification_divisions"] += 1
            hits.append({"candidate": candidate, "factor": divisor})
    return {
        "menu_kind": menu_kind,
        "initial_t": initial_t,
        "cutoff": cutoff,
        "window_stage_count": stage_count,
        "raw_window_integer_count": raw_integer_count,
        "deduplicated_candidate_count": len(candidates),
        "deduplicated_retests_removed": raw_integer_count - len(candidates),
        "candidate_sha256": digest.hexdigest(),
        "factor_hits": hits,
        "success": bool(hits),
        "operation_counts": dict(sorted(counts.items())),
        "walltime_seconds": time.perf_counter() - started,
    }, set(candidates)


def attach_menu_comparison(result, menu_records, candidate_sets):
    comparisons = {}
    for cutoff in CUTOFFS:
        record = menu_records[str(cutoff)]
        candidates = candidate_sets[cutoff]
        stayed = (
            result["maximum_abs_defect"] is not None
            and result["maximum_abs_defect"] <= cutoff
        )
        if stayed:
            for row in result["trace"]:
                if "q" not in row:
                    continue
                for value in (row["q"], row["t_minus_q"]):
                    if value and value not in candidates:
                        raise ArithmeticError(
                            "bounded-defect child was absent from its public menu"
                        )
        output_factors = set()
        output_values = []
        output = result["output"]
        if output:
            if "factor" in output:
                output_factors.add(output["factor"])
                output_values.append(output["screen_value"])
            else:
                output_factors.update(output["factors"])
                output_values.extend(
                    hit["screen_value"] for hit in output["screen_hits"]
                )
        menu_factors = {hit["factor"] for hit in record["factor_hits"]}
        comparisons[str(cutoff)] = {
            "observed_trajectory_stayed_within_cutoff": stayed,
            "larger_defect_observed": (
                result["maximum_abs_defect"] is not None
                and result["maximum_abs_defect"] > cutoff
            ),
            "menu_success": record["success"],
            "observed_output_factor_found_by_menu": bool(
                output_factors & menu_factors
            ),
            "observed_output_screen_value_in_menu": any(
                value in candidates for value in output_values
            ),
        }
    result["menu_comparison"] = comparisons


def factor_small_integer(value):
    factors = []
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            factors.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append(remaining)
    return factors


def label_factor_outputs(result, offline_factors):
    output = result["output"]
    if not output:
        return
    factors = [output["factor"]] if "factor" in output else output["factors"]
    output["offline_factor_labels"] = {
        str(factor): [
            prime for prime in offline_factors if factor % prime == 0
        ]
        for factor in factors
    }


def label_menu_outputs(menu_record, offline_factors):
    for hit in menu_record["factor_hits"]:
        hit["offline_factor_labels"] = [
            prime for prime in offline_factors if hit["factor"] % prime == 0
        ]


def cost_per_success(counts, successes):
    if not successes:
        return None
    return {
        key: counts.get(key, 0) / successes
        for key in COST_KEYS
        if counts.get(key, 0)
    }


def summarize_case(records, fixed_menus, sampled_initial_generation):
    summary = {
        "accepted_initial_parameter_denominator": len(records),
        "methods": {},
        "fixed_start_menus": {},
        "inverse_start_menus": {},
    }
    initial_factor_events = [
        event
        for record in records
        for event in record.get("initial_generation_factor_events", [])
    ]
    summary["initial_generation_factor_events"] = len(initial_factor_events)
    summary["generation_inclusive_denominator"] = (
        len(records) + len(initial_factor_events)
        if sampled_initial_generation
        else None
    )
    initial_factor_counts = Counter()
    accepted_generation_counts = Counter()
    for record in records:
        for event in record.get("initial_generation_factor_events", []):
            add_counts(initial_factor_counts, event["operation_counts"])
        accepted = record.get("accepted_initial_generation_event")
        if accepted:
            add_counts(accepted_generation_counts, accepted["operation_counts"])

    for method in METHODS:
        results = [record["methods"][method] for record in records]
        successes = sum(result["status"] == "success" for result in results)
        failures = Counter(
            result["stopping_reason"]
            for result in results
            if result["status"] == "stopping_failure"
        )
        output_types = Counter()
        operation_counts = Counter()
        validation_counts = Counter()
        defects = []
        cf_sums = []
        stages = []
        for result in results:
            add_counts(operation_counts, result["operation_counts"])
            add_counts(validation_counts, result["validation_counts"])
            if result["maximum_abs_defect"] is not None:
                defects.append(result["maximum_abs_defect"])
            cf_sums.extend(row["S"] for row in result["distinct_cf_sums"])
            stages.append(result["stages_with_count"])
            if result["output"]:
                output_types[
                    result["output"].get(
                        "output_type", result["stopping_reason"]
                    )
                ] += 1
        conditional_counts = Counter(operation_counts)
        if sampled_initial_generation:
            add_counts(conditional_counts, accepted_generation_counts)
        inclusive_counts = Counter(conditional_counts)
        if sampled_initial_generation:
            add_counts(inclusive_counts, initial_factor_counts)
        inclusive_successes = (
            successes + len(initial_factor_events)
            if sampled_initial_generation
            else None
        )
        summary["methods"][method] = {
            "conditional_successes": successes,
            "conditional_success_rate": fraction_record(successes, len(results)),
            "stopping_failures": dict(sorted(failures.items())),
            "time_censors": 0,
            "output_types": dict(sorted(output_types.items())),
            "generation_inclusive_successes": inclusive_successes,
            "generation_inclusive_success_rate": (
                fraction_record(
                    inclusive_successes,
                    len(records) + len(initial_factor_events),
                )
                if sampled_initial_generation
                else None
            ),
            "trajectory_operation_counts": dict(sorted(operation_counts.items())),
            "conditional_operation_counts": dict(
                sorted(conditional_counts.items())
            ),
            "generation_inclusive_operation_counts": (
                dict(sorted(inclusive_counts.items()))
                if sampled_initial_generation
                else None
            ),
            "conditional_cost_per_success": cost_per_success(
                conditional_counts, successes
            ),
            "generation_inclusive_cost_per_success": (
                cost_per_success(inclusive_counts, inclusive_successes)
                if sampled_initial_generation
                else None
            ),
            "validation_counts": dict(sorted(validation_counts.items())),
            "actual_maximum_abs_defect": max(defects) if defects else None,
            "cf_sum_observations": len(cf_sums),
            "actual_maximum_cf_sum": max(cf_sums) if cf_sums else None,
            "actual_mean_cf_sum": statistics.fmean(cf_sums) if cf_sums else None,
            "maximum_count_stages": max(stages) if stages else 0,
            "mean_count_stages": statistics.fmean(stages) if stages else 0.0,
        }

    for cutoff in CUTOFFS:
        key = str(cutoff)
        record = fixed_menus[key]
        fixed_results = [
            item["methods"]["fixed_multiplier"] for item in records
        ]
        summary["fixed_start_menus"][key] = {
            "menu_kind": record["menu_kind"],
            "initial_t": record["initial_t"],
            "cutoff": record["cutoff"],
            "window_stage_count": record["window_stage_count"],
            "raw_window_integer_count": record["raw_window_integer_count"],
            "deduplicated_candidate_count": record[
                "deduplicated_candidate_count"
            ],
            "deduplicated_retests_removed": record[
                "deduplicated_retests_removed"
            ],
            "candidate_sha256": record["candidate_sha256"],
            "factor_hits": record["factor_hits"],
            "success": record["success"],
            "operation_counts": record["operation_counts"],
            "walltime_seconds": record["walltime_seconds"],
            "trajectory_denominator": len(fixed_results),
            "fixed_trajectories_within_cutoff": sum(
                result["menu_comparison"][key][
                    "observed_trajectory_stayed_within_cutoff"
                ]
                for result in fixed_results
            ),
            "fixed_trajectories_with_larger_defect": sum(
                result["menu_comparison"][key]["larger_defect_observed"]
                for result in fixed_results
            ),
            "fixed_successes_whose_factor_was_in_menu": sum(
                result["menu_comparison"][key][
                    "observed_output_factor_found_by_menu"
                ]
                for result in fixed_results
            ),
        }

        inverse_menus = [
            item["inverse_start_menus"][key] for item in records
        ]
        inverse_results = [
            item["methods"]["inverse_start_fixed_multiplier"] for item in records
        ]
        menu_counts = Counter()
        for menu in inverse_menus:
            add_counts(menu_counts, menu["operation_counts"])
        menu_successes = sum(menu["success"] for menu in inverse_menus)
        summary["inverse_start_menus"][key] = {
            "menu_kind": "parameter_dependent_inverse_start",
            "cutoff": cutoff,
            "denominator": len(inverse_menus),
            "successes": menu_successes,
            "success_rate": fraction_record(menu_successes, len(inverse_menus)),
            "operation_counts": dict(sorted(menu_counts.items())),
            "cost_per_success": cost_per_success(menu_counts, menu_successes),
            "trajectories_within_cutoff": sum(
                result["menu_comparison"][key][
                    "observed_trajectory_stayed_within_cutoff"
                ]
                for result in inverse_results
            ),
            "trajectories_with_larger_defect": sum(
                result["menu_comparison"][key]["larger_defect_observed"]
                for result in inverse_results
            ),
            "successes_whose_factor_was_in_menu": sum(
                result["menu_comparison"][key][
                    "observed_output_factor_found_by_menu"
                ]
                for result in inverse_results
            ),
            "candidate_count_min": min(
                menu["deduplicated_candidate_count"] for menu in inverse_menus
            )
            if inverse_menus
            else 0,
            "candidate_count_max": max(
                menu["deduplicated_candidate_count"] for menu in inverse_menus
            )
            if inverse_menus
            else 0,
            "candidate_count_mean": statistics.fmean(
                menu["deduplicated_candidate_count"] for menu in inverse_menus
            )
            if inverse_menus
            else 0.0,
        }
    return summary


def externalize_attempt_records(payload, trace_path):
    if payload["mode"] == "scale":
        cases = [payload["case"]]
    else:
        cases = payload["cases"]
    trace_rows = [
        {
            "record_type": "header",
            "experiment": "F334_count_descent",
            "route": ROUTE,
            "mode": payload["mode"],
            "scope": (
                "Each later row is one complete accepted-initial-parameter "
                "record. Generation-factor events are separate earlier "
                "terminal attempts inside that record."
            ),
        }
    ]
    total_records = 0
    for case in cases:
        if "modulus" in case:
            case_id = case["modulus"]["modulus_id"]
        else:
            case_id = f"small_{case['n']}"
        records = case.pop("records")
        summaries = []
        for record in records:
            trace_rows.append(
                {
                    "record_type": "accepted_parameter",
                    "case_id": case_id,
                    "record": record,
                }
            )
            summaries.append(
                {
                    "accepted_index": record["accepted_index"],
                    "a": record["a"],
                    "initial_parameter_source": record[
                        "initial_parameter_source"
                    ],
                    "initial_generation_factor_count": len(
                        record["initial_generation_factor_events"]
                    ),
                    "initial_generation_factors": [
                        event["factor"]
                        for event in record["initial_generation_factor_events"]
                    ],
                    "methods": {
                        method: {
                            key: record["methods"][method][key]
                            for key in (
                                "status",
                                "stopping_reason",
                                "output",
                                "initial_t",
                                "stages_with_count",
                                "continued_stages",
                                "maximum_abs_defect",
                                "distinct_cf_sums",
                                "menu_comparison",
                            )
                        }
                        for method in METHODS
                    },
                    "inverse_start_menus": {
                        key: {
                            field: menu[field]
                            for field in (
                                "initial_t",
                                "cutoff",
                                "deduplicated_candidate_count",
                                "candidate_sha256",
                                "factor_hits",
                                "success",
                            )
                        }
                        for key, menu in record["inverse_start_menus"].items()
                    },
                }
            )
        case["attempt_summaries"] = summaries
        total_records += len(records)
    write_deterministic_gzip_jsonl(trace_path, trace_rows)
    return {
        "path": str(trace_path),
        "sha256": sha256(trace_path),
        "compressed_bytes": Path(trace_path).stat().st_size,
        "format": "deterministic gzip JSON Lines; mtime=0; compact sorted JSON",
        "accepted_parameter_records": total_records,
    }


def build_parameter_record(
    modulus,
    modulus_id,
    accepted_index,
    initial_a,
    offline_factors,
    initial_generation,
    fixed_menus,
    fixed_candidate_sets,
    validate_small,
):
    fresh_seed = derived_seed("fresh_inner", modulus_id, accepted_index)
    methods = {
        "fixed_multiplier": run_descent(
            modulus,
            initial_a,
            "fixed_multiplier",
            None,
            validate_small,
        ),
        "fresh_multiplier": run_descent(
            modulus,
            initial_a,
            "fresh_multiplier",
            fresh_seed,
            validate_small,
        ),
        "inverse_start_fixed_multiplier": run_descent(
            modulus,
            initial_a,
            "inverse_start_fixed_multiplier",
            None,
            validate_small,
        ),
    }
    for result in methods.values():
        label_factor_outputs(result, offline_factors)
    attach_menu_comparison(
        methods["fixed_multiplier"], fixed_menus, fixed_candidate_sets
    )
    attach_menu_comparison(
        methods["fresh_multiplier"], fixed_menus, fixed_candidate_sets
    )

    inverse_menus = {}
    inverse_candidate_sets = {}
    for cutoff in CUTOFFS:
        inverse_setup_counts = Counter()
        inverse = charged_mod_inverse(
            initial_a,
            modulus,
            inverse_setup_counts,
            "inverse_start_menu",
        )
        inverse_t = min(inverse, modulus - inverse)
        menu, candidates = run_menu(
            modulus,
            inverse_t,
            cutoff,
            "parameter_dependent_inverse_start",
        )
        merged_menu_counts = Counter(inverse_setup_counts)
        add_counts(merged_menu_counts, menu["operation_counts"])
        menu["operation_counts"] = dict(sorted(merged_menu_counts.items()))
        label_menu_outputs(menu, offline_factors)
        inverse_menus[str(cutoff)] = menu
        inverse_candidate_sets[cutoff] = candidates
    attach_menu_comparison(
        methods["inverse_start_fixed_multiplier"],
        inverse_menus,
        inverse_candidate_sets,
    )

    record = {
        "accepted_index": accepted_index,
        "a": initial_a,
        "fresh_stream_seed": fresh_seed,
        "methods": methods,
        "inverse_start_menus": inverse_menus,
    }
    if initial_generation is None:
        record["initial_parameter_source"] = "exhaustive_enumeration"
        record["initial_generation_factor_events"] = []
        record["accepted_initial_generation_event"] = None
    else:
        record["initial_parameter_source"] = "uniform_rejection_sampling"
        record["initial_stream_seed"] = initial_generation["stream_seed"]
        record["initial_generation_factor_events"] = initial_generation[
            "factor_events"
        ]
        record["accepted_initial_generation_event"] = initial_generation[
            "accepted_event"
        ]
    return record


def load_f328_moduli():
    if sha256(F328_INPUT) != F328_INPUT_SHA256:
        raise ArithmeticError("F328 modulus input hash changed")
    data = json.loads(F328_INPUT.read_text())
    rows = []
    for row in data["moduli"]:
        if row["p_offline"] * row["q_offline"] != row["n"]:
            raise ArithmeticError("F328 offline factor labels do not multiply to N")
        rows.append(row)
    return rows


def prepare_fixed_menus(modulus, offline_factors):
    initial_t = (modulus - 1) // 2
    records = {}
    candidate_sets = {}
    for cutoff in CUTOFFS:
        menu, candidates = run_menu(
            modulus, initial_t, cutoff, "parameter_independent_fixed_start"
        )
        label_menu_outputs(menu, offline_factors)
        records[str(cutoff)] = menu
        candidate_sets[cutoff] = candidates
    return records, candidate_sets


def run_sampled_case(modulus_row, start, stop, mode):
    modulus = modulus_row["n"]
    modulus_id = modulus_row["modulus_id"]
    offline_factors = [modulus_row["p_offline"], modulus_row["q_offline"]]
    fixed_menus, fixed_candidate_sets = prepare_fixed_menus(
        modulus, offline_factors
    )
    records = []
    RUN_PROGRESS.update(
        {
            "mode": mode,
            "modulus_id": modulus_id,
            "requested_range": [start, stop],
            "completed_accepted_parameters": 0,
        }
    )
    for accepted_index in range(start, stop):
        generation = generate_initial_parameter(
            modulus, modulus_id, accepted_index, False
        )
        record = build_parameter_record(
            modulus,
            modulus_id,
            accepted_index,
            generation["a"],
            offline_factors,
            generation,
            fixed_menus,
            fixed_candidate_sets,
            False,
        )
        records.append(record)
        RUN_PROGRESS["completed_accepted_parameters"] = len(records)
        RUN_PROGRESS["last_accepted_index"] = accepted_index
        current_rss = peak_rss_bytes()
        if current_rss > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 512 MiB")

    return {
        "modulus": modulus_row,
        "accepted_index_range": [start, stop],
        "accepted_initial_parameters": len(records),
        "initial_parameter_sampling": (
            "Each accepted index has an independent seeded fair-bit rejection "
            "stream. Jacobi-negative units are charged retries. A nonunit draw "
            "ends a separate generation-factor attempt. Sampling then continues "
            "only to obtain the requested conditional Jacobi-positive parameter."
        ),
        "fixed_start_menus": fixed_menus,
        "records": records,
        "summary": summarize_case(records, fixed_menus, True),
    }


def run_pilot():
    rows = {row["modulus_id"]: row for row in load_f328_moduli()}
    pilot_rows = [
        {
            "modulus_id": "pilot_209",
            "n": 209,
            "p_offline": 11,
            "q_offline": 19,
            "actual_bits": 8,
            "target_bits": 8,
        },
        rows["b92_i0"],
    ]
    accepted_counts = {"pilot_209": 8, "b92_i0": 4}
    cases = []
    for row in pilot_rows:
        cases.append(
            run_sampled_case(
                row, 0, accepted_counts[row["modulus_id"]], "pilot"
            )
        )
    return {
        "status": "passed",
        "experiment": "F334_count_descent",
        "route": ROUTE,
        "mode": "pilot",
        "cases": cases,
        "randomness_scope": (
            "All pilot initial and fresh streams are reproducible finite samples."
        ),
    }


def run_small_exact():
    cases = []
    RUN_PROGRESS.update(
        {
            "mode": "small_exact",
            "completed_moduli": 0,
            "completed_initial_parameters": 0,
        }
    )
    for modulus in range(3, 102, 2):
        offline_factors = factor_small_integer(modulus)
        if len(offline_factors) == 1 and offline_factors[0] == modulus:
            continue
        positive_units = [
            a
            for a in range(1, modulus)
            if math.gcd(a, modulus) == 1 and f326_jacobi(a, modulus) == 1
        ]
        fixed_menus, fixed_candidate_sets = prepare_fixed_menus(
            modulus, offline_factors
        )
        records = []
        for accepted_index, initial_a in enumerate(positive_units):
            records.append(
                build_parameter_record(
                    modulus,
                    f"small_{modulus}",
                    accepted_index,
                    initial_a,
                    offline_factors,
                    None,
                    fixed_menus,
                    fixed_candidate_sets,
                    True,
                )
            )
            RUN_PROGRESS["completed_initial_parameters"] += 1
        cases.append(
            {
                "n": modulus,
                "offline_prime_factor_labels": offline_factors,
                "jacobi_positive_units": len(positive_units),
                "fixed_start_menus": fixed_menus,
                "records": records,
                "summary": summarize_case(records, fixed_menus, False),
            }
        )
        RUN_PROGRESS["completed_moduli"] = len(cases)
        RUN_PROGRESS["last_completed_modulus"] = modulus
        if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 512 MiB")
    return {
        "status": "passed",
        "experiment": "F334_count_descent",
        "route": ROUTE,
        "mode": "small_exact",
        "scope": (
            "Every odd composite N<=101 and every Jacobi-positive unit a. "
            "Fixed and inverse-start rows are exact conditional enumerations. "
            "Fresh-mode inner streams use one reproducible independent stream "
            "per initial a and are non-exhaustive randomness."
        ),
        "cases": cases,
    }


def merge_summary_counts(target, source):
    for key, value in source.items():
        if isinstance(value, int):
            target[key] += value


def run_aggregate():
    scale_paths = sorted(EXPERIMENT_DIR.glob("scale_b*_output.json"))
    payloads = []
    seen = set()
    for path in scale_paths:
        data = json.loads(path.read_text())
        if data.get("status") != "passed" or data.get("mode") != "scale":
            continue
        case = data["case"]
        key = (
            case["modulus"]["modulus_id"],
            tuple(case["accepted_index_range"]),
        )
        if key in seen:
            raise ArithmeticError("duplicate scale batch")
        seen.add(key)
        payloads.append((path, data))

    by_modulus = {}
    for path, data in payloads:
        case = data["case"]
        modulus_id = case["modulus"]["modulus_id"]
        if case["accepted_index_range"] != [0, ACCEPTED_PARAMETERS]:
            raise ArithmeticError("aggregate expects one complete batch per modulus")
        if modulus_id in by_modulus:
            raise ArithmeticError("duplicate complete modulus")
        by_modulus[modulus_id] = {
            "source_file": path.name,
            "source_sha256": sha256(path),
            "modulus": case["modulus"],
            "summary": case["summary"],
        }
    expected_ids = {
        row["modulus_id"] for row in load_f328_moduli()
    }
    if set(by_modulus) != expected_ids:
        raise ArithmeticError("aggregate does not contain all twelve F328 moduli")

    overall = {}
    for method in METHODS:
        conditional_denominator = 0
        conditional_successes = 0
        inclusive_denominator = 0
        inclusive_successes = 0
        conditional_counts = Counter()
        inclusive_counts = Counter()
        stopping_failures = Counter()
        for entry in by_modulus.values():
            summary = entry["summary"]
            method_summary = summary["methods"][method]
            conditional_denominator += summary[
                "accepted_initial_parameter_denominator"
            ]
            conditional_successes += method_summary["conditional_successes"]
            inclusive_denominator += summary["generation_inclusive_denominator"]
            inclusive_successes += method_summary[
                "generation_inclusive_successes"
            ]
            add_counts(
                conditional_counts,
                method_summary["conditional_operation_counts"],
            )
            add_counts(
                inclusive_counts,
                method_summary["generation_inclusive_operation_counts"],
            )
            add_counts(stopping_failures, method_summary["stopping_failures"])
        overall[method] = {
            "conditional_successes": conditional_successes,
            "conditional_success_rate": fraction_record(
                conditional_successes, conditional_denominator
            ),
            "generation_inclusive_successes": inclusive_successes,
            "generation_inclusive_success_rate": fraction_record(
                inclusive_successes, inclusive_denominator
            ),
            "stopping_failures": dict(sorted(stopping_failures.items())),
            "conditional_operation_counts": dict(
                sorted(conditional_counts.items())
            ),
            "generation_inclusive_operation_counts": dict(
                sorted(inclusive_counts.items())
            ),
            "conditional_cost_per_success": cost_per_success(
                conditional_counts, conditional_successes
            ),
            "generation_inclusive_cost_per_success": cost_per_success(
                inclusive_counts, inclusive_successes
            ),
            "time_censors": 0,
        }
    small_path = EXPERIMENT_DIR / "small_output.json"
    pilot_path = EXPERIMENT_DIR / "pilot_output.json"
    return {
        "status": "passed",
        "experiment": "F334_count_descent",
        "route": ROUTE,
        "mode": "aggregate",
        "scale_moduli": [
            by_modulus[key] for key in sorted(by_modulus)
        ],
        "overall_scale_summary": overall,
        "small_output": {
            "path": small_path.name,
            "sha256": sha256(small_path),
        },
        "pilot_output": {
            "path": pilot_path.name,
            "sha256": sha256(pilot_path),
        },
        "scope": (
            "Finite conditional J-law samples and a separate "
            "generation-inclusive view. Zero observed successes have no "
            "unbounded interpretation."
        ),
    }


def validate_dependencies():
    expected = {
        F326_SOURCE: F326_SOURCE_SHA256,
        F328_INPUT: F328_INPUT_SHA256,
        F330_DESIGN: F330_DESIGN_SHA256,
        F330_CF_NOTE: F330_CF_NOTE_SHA256,
    }
    for path, expected_hash in expected.items():
        if sha256(path) != expected_hash:
            raise ArithmeticError(f"frozen dependency changed: {path}")
    if CountOracle.floor_sum is not GaussPairing.floor_sum:
        raise ArithmeticError("CountOracle is not using frozen F326 floor_sum")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode", choices=("pilot", "small", "scale", "aggregate"), required=True
    )
    parser.add_argument("--modulus-id")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int, default=ACCEPTED_PARAMETERS)
    parser.add_argument("--output", required=True)
    parser.add_argument("--status", required=True)
    parser.add_argument("--traces")
    arguments = parser.parse_args()
    started = time.perf_counter()
    validate_dependencies()

    def timeout_handler(_signal_number, _frame):
        raise TimeoutError("internal 28-second alarm fired")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(INTERNAL_TIMEOUT_SECONDS)
    running = {
        "status": "running",
        "experiment": "F334_count_descent",
        "route": ROUTE,
        "mode": arguments.mode,
        "seed": SEED,
        "source_sha256": sha256(Path(__file__)),
        "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
        "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
        "memory_limit_bytes": MEMORY_LIMIT_BYTES,
    }
    write_json(arguments.status, running)
    try:
        if arguments.mode == "pilot":
            payload = run_pilot()
        elif arguments.mode == "small":
            payload = run_small_exact()
        elif arguments.mode == "aggregate":
            payload = run_aggregate()
        else:
            if not arguments.modulus_id:
                raise ValueError("--modulus-id is required for scale mode")
            if not (0 <= arguments.start < arguments.stop <= ACCEPTED_PARAMETERS):
                raise ValueError("invalid accepted-index range")
            rows = {
                row["modulus_id"]: row for row in load_f328_moduli()
            }
            if arguments.modulus_id not in rows:
                raise ValueError("unknown F328 modulus id")
            payload = {
                "status": "passed",
                "experiment": "F334_count_descent",
                "route": ROUTE,
                "mode": "scale",
                "case": run_sampled_case(
                    rows[arguments.modulus_id],
                    arguments.start,
                    arguments.stop,
                    "scale",
                ),
                "randomness_scope": (
                    "Initial parameters and fresh-mode inner parameters use "
                    "independent reproducible finite streams. This is not "
                    "exhaustive randomness."
                ),
            }
        if arguments.mode != "aggregate":
            if not arguments.traces:
                raise ValueError("--traces is required outside aggregate mode")
            payload["trace_artifact"] = externalize_attempt_records(
                payload, arguments.traces
            )
        signal.alarm(0)
        payload.update(
            {
                "seed": SEED,
                "source_sha256": sha256(Path(__file__)),
                "dependency_sha256": {
                    "F326_direct_gauss_pairing": F326_SOURCE_SHA256,
                    "F328_moduli": F328_INPUT_SHA256,
                    "F330_Q_descent_design": F330_DESIGN_SHA256,
                    "F330_discrepancy_note": F330_CF_NOTE_SHA256,
                },
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
        if "trace_artifact" in payload:
            status["trace_artifact"] = payload["trace_artifact"]
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
