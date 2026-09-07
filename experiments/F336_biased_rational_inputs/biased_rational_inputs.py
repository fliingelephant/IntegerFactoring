#!/usr/bin/env python3
"""F336: exact finite trials of biased rational inputs for count descent."""

import argparse
from collections import Counter
from fractions import Fraction
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
EXPERIMENT_DIR = ROOT / "experiments" / "F336_biased_rational_inputs"
F334_DIR = ROOT / "experiments" / "F334_count_descent"
F334_SOURCE = F334_DIR / "count_descent.py"
F328_INPUT = ROOT / "experiments" / "F328_capped_rabin_paths" / "moduli.json"
DESIGN = EXPERIMENT_DIR / "DESIGN.md"
MENU_BOUND = EXPERIMENT_DIR / "MENU_BOUND.md"

F334_SOURCE_SHA256 = (
    "cb93f160d57b2a3285551cbd268e732917e3062a90eb8ca62df843f581be1e24"
)
F328_INPUT_SHA256 = (
    "acf09b285c57c39cfcb93d3cd77addce909498e224955fd0ec9d2e4d86ee0428"
)
DESIGN_SHA256 = "fb07018513f000b1b70e697e4d51bcb4aa38e06f1d93a5642ad2c54dabc44e0c"
MENU_BOUND_SHA256 = (
    "d03683007e950dd689a3f47955b1805c8ceca589ac3c95c09917236286fe6cb7"
)

SEED = 33620260907
ROUTE = "route:F31"
DIRECT_INVERSE_SCALES = ((1, 8), (1, 4), (3, 8), (1, 2), (3, 4))
RATIO_SCALES = ((1, 8), (1, 4), (3, 8))
TRIALS_PER_PROFILE = 128
INVERSE_FORMULA_LIMIT = 1 << 16
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024
RUN_PROGRESS = {}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


if sha256(F334_SOURCE) != F334_SOURCE_SHA256:
    raise RuntimeError("frozen F334 source hash changed")
sys.path.insert(0, str(F334_DIR))
import count_descent as f334  # noqa: E402


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


def derived_seed(*parts):
    raw = ":".join(str(part) for part in (SEED, *parts)).encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:16], "big")


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
        F328_INPUT: F328_INPUT_SHA256,
        DESIGN: DESIGN_SHA256,
        MENU_BOUND: MENU_BOUND_SHA256,
    }
    for path, expected_hash in expected.items():
        if sha256(path) != expected_hash:
            raise ArithmeticError(f"frozen dependency changed: {path}")
    if f334.CountOracle.floor_sum is not f334.GaussPairing.floor_sum:
        raise ArithmeticError("F334 CountOracle is not using frozen F326 floor_sum")


def load_moduli():
    data = json.loads(F328_INPUT.read_text())
    rows = []
    for row in data["moduli"]:
        if row["p_offline"] * row["q_offline"] != row["n"]:
            raise ArithmeticError("offline factor labels do not multiply to N")
        rows.append(row)
    return rows


def scale_record(bit_length, numerator, denominator):
    exponent = max(2, bit_length * numerator // denominator)
    return {
        "numerator": numerator,
        "denominator": denominator,
        "exponent": exponent,
        "label": f"{numerator}_{denominator}",
    }


def sample_odd_value(modulus, scale, generator, counts):
    lower = 1 << (scale["exponent"] - 1)
    upper = min((1 << scale["exponent"]) - 1, modulus - 1)
    first = lower if lower & 1 else lower + 1
    last = upper if upper & 1 else upper - 1
    number = (last - first) // 2 + 1
    index = f334.bounded_sample(generator, number, counts)
    value = first + 2 * index
    if not (lower <= value <= upper and value & 1):
        raise ArithmeticError("odd-range sampler returned an invalid value")
    return value, {
        "lower": lower,
        "upper": upper,
        "first_odd": first,
        "last_odd": last,
        "odd_value_count": number,
    }


def sample_uniform_nonzero(modulus, generator, counts):
    return f334.bounded_sample(generator, modulus - 1, counts) + 1


def canonical_cf_stats(multiplier, modulus):
    left, right = modulus, multiplier
    digits = []
    while right:
        quotient, remainder = divmod(left, right)
        digits.append(quotient)
        left, right = right, remainder
    if left != 1 or not digits or digits[-1] < 2:
        raise ArithmeticError("noncanonical continued fraction for a unit")
    return {
        "digit_sum": sum(digits),
        "largest_digit": max(digits),
        "digit_count": len(digits),
        "euclidean_divisions": len(digits),
    }


def label_factor(factor, offline_factors):
    return [prime for prime in offline_factors if factor % prime == 0]


def verified_generation_factor(
    row_id,
    policy,
    policy_kind,
    gamma,
    trial_index,
    modulus_row,
    generation,
):
    modulus = modulus_row["n"]
    factors = generation["factors"]
    for factor in factors:
        if not (1 < factor < modulus and modulus % factor == 0):
            raise ArithmeticError("generation factor is not a proper divisor")
    output = {
        "factors": factors,
        "offline_factor_labels": {
            str(factor): label_factor(
                factor, [modulus_row["p_offline"], modulus_row["q_offline"]]
            )
            for factor in factors
        },
    }
    row = {
        "row_id": row_id,
        "modulus_id": modulus_row["modulus_id"],
        "modulus": modulus,
        "actual_bits": modulus_row["actual_bits"],
        "trial_index": trial_index,
        "policy": policy,
        "policy_kind": policy_kind,
        "gamma": gamma,
        "status": "success",
        "output_type": "generation_factor",
        "stopping_reason": generation["stopping_reason"],
        "stopping_stage": None,
        "parameters": generation["parameters"],
        "source_seeds": generation["source_seeds"],
        "source_range": generation.get("source_range"),
        "a": None,
        "jacobi_sign": None,
        "continued_fraction": None,
        "defects": [],
        "maximum_abs_defect": None,
        "stages_with_count": 0,
        "continued_stages": 0,
        "verified_output": output,
        "algorithm_operation_counts": generation["operation_counts"],
        "diagnostic_operation_counts": {},
        "standalone_walltime_seconds": generation["walltime_seconds"],
        "diagnostics": {},
        "anomalies": [],
    }
    witness = {
        "row_id": row_id,
        "output_type": "generation_factor",
        "generation": generation,
        "full_descent_trace": None,
    }
    return row, witness


def inverse_periodic_first_count(modulus, denominator, multiplier, t):
    if denominator > INVERSE_FORMULA_LIMIT:
        return None
    c = (denominator * multiplier - 1) // modulus
    if denominator * multiplier != 1 + c * modulus:
        raise ArithmeticError("inverse coefficient identity failed")
    residue_count = t % denominator
    threshold = (denominator - 1) // 2
    tail = sum(
        (c * value) % denominator <= threshold
        for value in range(1, residue_count + 1)
    )
    return ((denominator + 1) // 2) * (t // denominator) + tail


def ratio_model_diagnostics(result, numerator, denominator, modulus):
    maximum = Fraction(0, 1)
    violations = []
    checked = 0
    bound = 4 * (numerator + denominator)
    for trace_row in result["trace"]:
        if "q" not in trace_row:
            continue
        t = trace_row["t"]
        if denominator % 2 == 0:
            predicted = Fraction(t, 2)
        else:
            remainder = (numerator * t) % modulus
            triangular_numerator = min(remainder, modulus - remainder)
            predicted = Fraction(t, 2) + Fraction(
                triangular_numerator, 2 * denominator * numerator
            )
        error = abs(Fraction(trace_row["q"], 1) - predicted)
        maximum = max(maximum, error)
        checked += 1
        if error > bound:
            violations.append(
                {
                    "stage": trace_row["stage"],
                    "t": t,
                    "q": trace_row["q"],
                    "predicted": fraction_record(
                        predicted.numerator, predicted.denominator
                    ),
                    "error": fraction_record(error.numerator, error.denominator),
                    "bound": bound,
                }
            )
    return {
        "checked_stages": checked,
        "bound": bound,
        "maximum_error": fraction_record(maximum.numerator, maximum.denominator),
        "violations": violations,
    }


def accepted_attempt(
    row_id,
    policy,
    policy_kind,
    gamma,
    trial_index,
    modulus_row,
    multiplier,
    generation,
    transform_counts,
    transform_walltime,
    rational_numerator,
    rational_denominator,
    keep_full_trace,
):
    modulus = modulus_row["n"]
    if math.gcd(multiplier, modulus) != 1:
        raise ArithmeticError("accepted multiplier is not a unit")
    if multiplier * rational_denominator % modulus != rational_numerator % modulus:
        raise ArithmeticError("a*b=r relation failed")

    diagnostic_counts = Counter()
    jacobi_sign = f334.charged_jacobi(
        multiplier, modulus, diagnostic_counts, False
    )
    if jacobi_sign not in (-1, 1):
        raise ArithmeticError("unit has zero Jacobi symbol")
    cf = canonical_cf_stats(multiplier, modulus)
    diagnostic_counts["reported_cf_calls"] += 1
    diagnostic_counts["reported_cf_euclidean_divisions"] += cf[
        "euclidean_divisions"
    ]

    result = f334.run_descent(
        modulus,
        multiplier,
        "fixed_multiplier",
        derived_seed("unused_fresh", row_id),
        False,
    )
    if result["distinct_cf_sums"] != [
        {"a": multiplier, "S": cf["digit_sum"]}
    ]:
        raise ArithmeticError("reported CF sum disagrees with frozen F334")
    add_counts(diagnostic_counts, result["validation_counts"])

    algorithm_counts = Counter()
    add_counts(algorithm_counts, generation["operation_counts"])
    add_counts(algorithm_counts, transform_counts)
    add_counts(algorithm_counts, result["operation_counts"])

    trace_rows = [row for row in result["trace"] if "q" in row]
    defects = [row["defect"] for row in trace_rows]
    if result["maximum_abs_defect"] != (
        max(map(abs, defects)) if defects else None
    ):
        raise ArithmeticError("maximum defect does not match retained defects")

    anomalies = []
    diagnostics = {}
    if policy_kind == "inverse":
        expected = inverse_periodic_first_count(
            modulus, rational_denominator, multiplier, (modulus - 1) // 2
        )
        if expected is not None:
            observed = trace_rows[0]["q"]
            diagnostics["inverse_periodic_first_count"] = {
                "denominator_limit": INVERSE_FORMULA_LIMIT,
                "expected": expected,
                "observed": observed,
                "match": observed == expected,
            }
            if observed != expected:
                anomalies.append(
                    {
                        "kind": "inverse_periodic_first_count_violation",
                        "expected": expected,
                        "observed": observed,
                    }
                )
        else:
            diagnostics["inverse_periodic_first_count"] = {
                "denominator_limit": INVERSE_FORMULA_LIMIT,
                "status": "not_evaluated_above_limit",
            }
    if policy_kind == "ratio":
        ratio_diagnostics = ratio_model_diagnostics(
            result, rational_numerator, rational_denominator, modulus
        )
        diagnostics["triangular_wave"] = ratio_diagnostics
        anomalies.extend(
            {
                "kind": "triangular_wave_error_bound_violation",
                **violation,
            }
            for violation in ratio_diagnostics["violations"]
        )

    verified_output = result["output"]
    if verified_output:
        factors = (
            [verified_output["factor"]]
            if "factor" in verified_output
            else verified_output["factors"]
        )
        for factor in factors:
            if not (1 < factor < modulus and modulus % factor == 0):
                raise ArithmeticError("count descent returned an invalid factor")
        verified_output["offline_factor_labels"] = {
            str(factor): label_factor(
                factor, [modulus_row["p_offline"], modulus_row["q_offline"]]
            )
            for factor in factors
        }

    stopping_stage = (
        result["trace"][-1]["stage"] if result["trace"] else None
    )
    row = {
        "row_id": row_id,
        "modulus_id": modulus_row["modulus_id"],
        "modulus": modulus,
        "actual_bits": modulus_row["actual_bits"],
        "trial_index": trial_index,
        "policy": policy,
        "policy_kind": policy_kind,
        "gamma": gamma,
        "status": result["status"],
        "output_type": "count_factor" if verified_output else "stopping_failure",
        "stopping_reason": result["stopping_reason"],
        "stopping_stage": stopping_stage,
        "parameters": generation["parameters"],
        "source_seeds": generation["source_seeds"],
        "source_range": generation.get("source_range"),
        "a": multiplier,
        "jacobi_sign": jacobi_sign,
        "continued_fraction": cf,
        "defects": defects,
        "maximum_abs_defect": result["maximum_abs_defect"],
        "stages_with_count": result["stages_with_count"],
        "continued_stages": result["continued_stages"],
        "verified_output": verified_output,
        "algorithm_operation_counts": dict(sorted(algorithm_counts.items())),
        "diagnostic_operation_counts": dict(sorted(diagnostic_counts.items())),
        "standalone_walltime_seconds": (
            generation["walltime_seconds"]
            + transform_walltime
            + result["walltime_seconds"]
        ),
        "diagnostics": diagnostics,
        "anomalies": anomalies,
    }
    witness = None
    if keep_full_trace or verified_output or anomalies:
        witness = {
            "row_id": row_id,
            "output_type": row["output_type"],
            "generation": generation,
            "transform_operation_counts": dict(sorted(transform_counts.items())),
            "full_descent_trace": result["trace"],
            "diagnostics": diagnostics,
            "anomalies": anomalies,
        }
    return row, witness


def paired_direct_inverse(modulus_row, trial_index, scale, keep_full_trace):
    modulus = modulus_row["n"]
    modulus_id = modulus_row["modulus_id"]
    stream_seed = derived_seed(
        "paired_direct_inverse", modulus_id, trial_index, scale["label"]
    )
    generator = random.Random(stream_seed)
    started = time.perf_counter()
    counts = Counter()
    denominator, source_range = sample_odd_value(
        modulus, scale, generator, counts
    )
    divisor = f334.charged_gcd(
        denominator, modulus, counts, "source_generation"
    )
    elapsed = time.perf_counter() - started
    common_parameters = {
        "paired_draw": denominator,
        "raw_numerator": None,
        "raw_denominator": denominator,
    }
    source_seeds = {"paired_draw": stream_seed}
    gamma = {key: scale[key] for key in ("numerator", "denominator", "exponent")}
    rows = []
    witnesses = []

    if divisor > 1:
        counts["factor_verification_divisions"] += 1
        generation = {
            "factors": [divisor],
            "stopping_reason": "paired_denominator_generation_factor",
            "parameters": common_parameters,
            "source_seeds": source_seeds,
            "source_range": source_range,
            "operation_counts": dict(sorted(counts.items())),
            "walltime_seconds": elapsed,
        }
        for policy_kind in ("direct", "inverse"):
            policy = f"{policy_kind}_{scale['label']}"
            row_id = f"{modulus_id}:{trial_index}:{policy}"
            row, witness = verified_generation_factor(
                row_id,
                policy,
                policy_kind,
                gamma,
                trial_index,
                modulus_row,
                generation,
            )
            rows.append(row)
            witnesses.append(witness)
        return rows, witnesses

    direct_generation = {
        "parameters": {
            **common_parameters,
            "reduced_numerator": denominator,
            "reduced_denominator": 1,
        },
        "source_seeds": source_seeds,
        "source_range": source_range,
        "operation_counts": dict(sorted(counts.items())),
        "walltime_seconds": elapsed,
    }
    direct_policy = f"direct_{scale['label']}"
    row, witness = accepted_attempt(
        f"{modulus_id}:{trial_index}:{direct_policy}",
        direct_policy,
        "direct",
        gamma,
        trial_index,
        modulus_row,
        denominator,
        direct_generation,
        Counter(),
        0.0,
        denominator,
        1,
        keep_full_trace,
    )
    rows.append(row)
    if witness:
        witnesses.append(witness)

    inverse_counts = Counter()
    inverse_started = time.perf_counter()
    multiplier = f334.charged_mod_inverse(
        denominator, modulus, inverse_counts, "source_transform"
    )
    inverse_elapsed = time.perf_counter() - inverse_started
    inverse_generation = {
        "parameters": {
            **common_parameters,
            "reduced_numerator": 1,
            "reduced_denominator": denominator,
        },
        "source_seeds": source_seeds,
        "source_range": source_range,
        "operation_counts": dict(sorted(counts.items())),
        "walltime_seconds": elapsed,
    }
    inverse_policy = f"inverse_{scale['label']}"
    row, witness = accepted_attempt(
        f"{modulus_id}:{trial_index}:{inverse_policy}",
        inverse_policy,
        "inverse",
        gamma,
        trial_index,
        modulus_row,
        multiplier,
        inverse_generation,
        inverse_counts,
        inverse_elapsed,
        1,
        denominator,
        keep_full_trace,
    )
    rows.append(row)
    if witness:
        witnesses.append(witness)
    return rows, witnesses


def ratio_attempt(modulus_row, trial_index, scale, keep_full_trace):
    modulus = modulus_row["n"]
    modulus_id = modulus_row["modulus_id"]
    numerator_seed = derived_seed("ratio_numerator", modulus_id, trial_index, scale["label"])
    denominator_seed = derived_seed(
        "ratio_denominator", modulus_id, trial_index, scale["label"]
    )
    numerator_generator = random.Random(numerator_seed)
    denominator_generator = random.Random(denominator_seed)
    counts = Counter()
    started = time.perf_counter()
    numerator, numerator_range = sample_odd_value(
        modulus, scale, numerator_generator, counts
    )
    denominator, denominator_range = sample_odd_value(
        modulus, scale, denominator_generator, counts
    )
    numerator_divisor = f334.charged_gcd(
        numerator, modulus, counts, "numerator_generation"
    )
    denominator_divisor = None
    if numerator_divisor == 1:
        denominator_divisor = f334.charged_gcd(
            denominator, modulus, counts, "denominator_generation"
        )
    factors = sorted(
        {
            divisor
            for divisor in (numerator_divisor, denominator_divisor)
            if divisor is not None and divisor > 1
        }
    )
    common_parameters = {
        "raw_numerator": numerator,
        "raw_denominator": denominator,
        "reduced_numerator": None,
        "reduced_denominator": None,
    }
    source_seeds = {
        "numerator": numerator_seed,
        "denominator": denominator_seed,
    }
    source_range = {
        "numerator": numerator_range,
        "denominator": denominator_range,
    }
    policy = f"ratio_{scale['label']}"
    gamma = {key: scale[key] for key in ("numerator", "denominator", "exponent")}
    row_id = f"{modulus_id}:{trial_index}:{policy}"
    if factors:
        counts["factor_verification_divisions"] += len(factors)
        generation = {
            "factors": factors,
            "stopping_reason": "ratio_component_generation_factor",
            "parameters": common_parameters,
            "source_seeds": source_seeds,
            "source_range": source_range,
            "operation_counts": dict(sorted(counts.items())),
            "walltime_seconds": time.perf_counter() - started,
        }
        return verified_generation_factor(
            row_id,
            policy,
            "ratio",
            gamma,
            trial_index,
            modulus_row,
            generation,
        )

    common = f334.charged_gcd(
        numerator, denominator, counts, "rational_reduction"
    )
    reduced_numerator = numerator // common
    reduced_denominator = denominator // common
    transform_counts = Counter()
    transform_started = time.perf_counter()
    inverse = f334.charged_mod_inverse(
        reduced_denominator, modulus, transform_counts, "source_transform"
    )
    multiplier = reduced_numerator * inverse % modulus
    transform_elapsed = time.perf_counter() - transform_started
    generation = {
        "parameters": {
            **common_parameters,
            "ordinary_common_gcd": common,
            "reduced_numerator": reduced_numerator,
            "reduced_denominator": reduced_denominator,
        },
        "source_seeds": source_seeds,
        "source_range": source_range,
        "operation_counts": dict(sorted(counts.items())),
        "walltime_seconds": time.perf_counter() - started - transform_elapsed,
    }
    return accepted_attempt(
        row_id,
        policy,
        "ratio",
        gamma,
        trial_index,
        modulus_row,
        multiplier,
        generation,
        transform_counts,
        transform_elapsed,
        reduced_numerator,
        reduced_denominator,
        keep_full_trace,
    )


def uniform_attempt(modulus_row, trial_index, keep_full_trace):
    modulus = modulus_row["n"]
    modulus_id = modulus_row["modulus_id"]
    stream_seed = derived_seed("uniform", modulus_id, trial_index)
    generator = random.Random(stream_seed)
    counts = Counter()
    started = time.perf_counter()
    multiplier = sample_uniform_nonzero(modulus, generator, counts)
    divisor = f334.charged_gcd(
        multiplier, modulus, counts, "source_generation"
    )
    elapsed = time.perf_counter() - started
    parameters = {
        "raw_numerator": multiplier,
        "raw_denominator": 1,
        "reduced_numerator": multiplier if divisor == 1 else None,
        "reduced_denominator": 1 if divisor == 1 else None,
    }
    generation = {
        "parameters": parameters,
        "source_seeds": {"uniform_nonzero": stream_seed},
        "source_range": {"lower": 1, "upper": modulus - 1, "value_count": modulus - 1},
        "operation_counts": dict(sorted(counts.items())),
        "walltime_seconds": elapsed,
    }
    row_id = f"{modulus_id}:{trial_index}:uniform"
    if divisor > 1:
        counts["factor_verification_divisions"] += 1
        generation["operation_counts"] = dict(sorted(counts.items()))
        generation["factors"] = [divisor]
        generation["stopping_reason"] = "uniform_generation_factor"
        return verified_generation_factor(
            row_id,
            "uniform",
            "uniform",
            None,
            trial_index,
            modulus_row,
            generation,
        )
    return accepted_attempt(
        row_id,
        "uniform",
        "uniform",
        None,
        trial_index,
        modulus_row,
        multiplier,
        generation,
        Counter(),
        0.0,
        multiplier,
        1,
        keep_full_trace,
    )


def run_trial(modulus_row, trial_index, keep_full_trace):
    rows = []
    witnesses = []
    for numerator, denominator in DIRECT_INVERSE_SCALES:
        scale = scale_record(modulus_row["n"].bit_length(), numerator, denominator)
        new_rows, new_witnesses = paired_direct_inverse(
            modulus_row, trial_index, scale, keep_full_trace
        )
        rows.extend(new_rows)
        witnesses.extend(new_witnesses)
    for numerator, denominator in RATIO_SCALES:
        scale = scale_record(modulus_row["n"].bit_length(), numerator, denominator)
        row, witness = ratio_attempt(
            modulus_row, trial_index, scale, keep_full_trace
        )
        rows.append(row)
        if witness:
            witnesses.append(witness)
    row, witness = uniform_attempt(modulus_row, trial_index, keep_full_trace)
    rows.append(row)
    if witness:
        witnesses.append(witness)
    if len(rows) != 14:
        raise ArithmeticError("trial did not produce fourteen policy rows")
    return rows, witnesses


def brute_fixed_descent(modulus, multiplier):
    half = (modulus - 1) // 2
    t = half
    trace = []
    if t <= 1:
        return {"stopping_reason": "t_at_most_one", "factors": [], "trace": trace}
    stage = 0
    while True:
        divisor_t = math.gcd(t, modulus)
        if divisor_t > 1:
            trace.append({"stage": stage, "t": t, "termination": "factor_at_t"})
            return {
                "stopping_reason": "factor_at_t",
                "factors": [divisor_t],
                "trace": trace,
            }
        q = sum(
            1 <= multiplier * y % modulus <= half for y in range(1, t + 1)
        )
        other = t - q
        factors = sorted(
            {
                divisor
                for value in (q, other)
                if value
                for divisor in (math.gcd(value, modulus),)
                if divisor > 1
            }
        )
        termination = "factor_at_child_count" if factors else None
        if not factors and (q == 0 or other == 0):
            termination = "empty_side"
        trace.append(
            {
                "stage": stage,
                "t": t,
                "q": q,
                "t_minus_q": other,
                "defect": 2 * q - t,
                "termination": termination,
            }
        )
        if factors:
            return {
                "stopping_reason": "factor_at_child_count",
                "factors": factors,
                "trace": trace,
            }
        if q == 0 or other == 0:
            return {"stopping_reason": "empty_side", "factors": [], "trace": trace}
        t = min(q, other)
        stage += 1
        if t <= 1:
            return {"stopping_reason": "t_at_most_one", "factors": [], "trace": trace}


def run_tiny():
    oracle_checks = 0
    descent_checks = 0
    for modulus in range(9, 52, 2):
        if all(modulus % divisor for divisor in range(3, math.isqrt(modulus) + 1, 2)):
            continue
        half = (modulus - 1) // 2
        for multiplier in range(1, modulus):
            if math.gcd(multiplier, modulus) != 1:
                continue
            oracle = f334.CountOracle(modulus, multiplier)
            for t in range(half + 1):
                q = oracle.Q(t)
                brute_q = sum(
                    1 <= multiplier * y % modulus <= half
                    for y in range(1, t + 1)
                )
                if q != brute_q:
                    raise ArithmeticError("tiny CountOracle mismatch")
                oracle_checks += 1
            frozen = f334.run_descent(
                modulus, multiplier, "fixed_multiplier", 0, True
            )
            brute = brute_fixed_descent(modulus, multiplier)
            if frozen["stopping_reason"] != brute["stopping_reason"]:
                raise ArithmeticError("tiny descent stopping-reason mismatch")
            frozen_factors = []
            if frozen["output"]:
                frozen_factors = (
                    [frozen["output"]["factor"]]
                    if "factor" in frozen["output"]
                    else frozen["output"]["factors"]
                )
            if frozen_factors != brute["factors"]:
                raise ArithmeticError("tiny descent factor mismatch")
            frozen_counts = [
                (row["t"], row["q"], row["t_minus_q"], row["defect"])
                for row in frozen["trace"]
                if "q" in row
            ]
            brute_counts = [
                (row["t"], row["q"], row["t_minus_q"], row["defect"])
                for row in brute["trace"]
                if "q" in row
            ]
            if frozen_counts != brute_counts:
                raise ArithmeticError("tiny descent count trace mismatch")
            descent_checks += 1

    sample_checks = 0
    relation_checks = 0
    rows = {row["modulus_id"]: row for row in load_moduli()}
    modulus_row = rows["b20_i0"]
    for trial_index in range(8):
        trial_rows, _ = run_trial(modulus_row, trial_index, False)
        for row in trial_rows:
            sample_checks += 1
            if row["a"] is None:
                continue
            parameters = row["parameters"]
            if row["a"] * parameters["reduced_denominator"] % row["modulus"] != parameters["reduced_numerator"] % row["modulus"]:
                raise ArithmeticError("tiny sampled rational relation mismatch")
            relation_checks += 1
    forced_cases = []
    for candidate in (3, 7):
        counts = Counter()
        divisor = f334.charged_gcd(candidate, 15, counts, "forced_generation")
        forced_cases.append(
            {
                "modulus": 15,
                "candidate": candidate,
                "gcd": divisor,
                "kind": "generation_factor" if divisor > 1 else "unit",
            }
        )
    if forced_cases != [
        {"modulus": 15, "candidate": 3, "gcd": 3, "kind": "generation_factor"},
        {"modulus": 15, "candidate": 7, "gcd": 1, "kind": "unit"},
    ]:
        raise ArithmeticError("forced generation cases failed")

    return {
        "status": "passed",
        "experiment": "F336_biased_rational_inputs",
        "route": ROUTE,
        "mode": "tiny",
        "scope": "Exact finite protocol and oracle checks; no probability claim.",
        "oracle_membership_checks": oracle_checks,
        "complete_unit_descent_checks": descent_checks,
        "sampled_policy_rows_checked": sample_checks,
        "accepted_rational_relations_checked": relation_checks,
        "forced_generation_cases": forced_cases,
    }


def summarize_rows(rows):
    if not rows:
        raise ValueError("cannot summarize empty row list")
    policy = rows[0]["policy"]
    if any(row["policy"] != policy for row in rows):
        raise ArithmeticError("mixed policies in summary")
    algorithm_totals = Counter()
    diagnostic_totals = Counter()
    for row in rows:
        add_counts(algorithm_totals, row["algorithm_operation_counts"])
        add_counts(diagnostic_totals, row["diagnostic_operation_counts"])
    output_types = Counter(row["output_type"] for row in rows)
    stopping_reasons = Counter(row["stopping_reason"] for row in rows)
    unit_rows = [row for row in rows if row["a"] is not None]
    cf_rows = [row["continued_fraction"] for row in unit_rows]
    defect_values = [
        abs(defect) for row in unit_rows for defect in row["defects"]
    ]
    successes = output_types["generation_factor"] + output_types["count_factor"]
    operation_cost = {
        key: fraction_record(value, successes)
        for key, value in sorted(algorithm_totals.items())
        if successes and value
    }
    walltime_total = sum(row["standalone_walltime_seconds"] for row in rows)
    distinct_parameters = len({row["a"] for row in unit_rows})
    return {
        "policy": policy,
        "attempts": len(rows),
        "accepted_unit_parameters": len(unit_rows),
        "distinct_accepted_parameters": distinct_parameters,
        "repeated_accepted_parameters": len(unit_rows) - distinct_parameters,
        "output_type_counts": dict(sorted(output_types.items())),
        "stopping_reason_counts": dict(sorted(stopping_reasons.items())),
        "generation_factor_successes": output_types["generation_factor"],
        "count_factor_successes": output_types["count_factor"],
        "total_successes": successes,
        "jacobi_sign_counts": dict(
            sorted(Counter(str(row["jacobi_sign"]) for row in unit_rows).items())
        ),
        "continued_fraction": {
            "observations": len(cf_rows),
            "digit_sum_total": sum(row["digit_sum"] for row in cf_rows),
            "digit_sum_median": statistics.median(
                row["digit_sum"] for row in cf_rows
            ) if cf_rows else None,
            "largest_observed_digit": max(
                (row["largest_digit"] for row in cf_rows), default=None
            ),
        },
        "defects": {
            "observations": len(defect_values),
            "maximum_absolute": max(defect_values, default=None),
            "mean_absolute": fraction_record(
                sum(defect_values), len(defect_values)
            ),
        },
        "algorithm_operation_totals": dict(sorted(algorithm_totals.items())),
        "diagnostic_operation_totals": dict(sorted(diagnostic_totals.items())),
        "standalone_walltime_total_seconds": walltime_total,
        "cost_per_observed_success": {
            "algorithm_operations": operation_cost if successes else None,
            "standalone_walltime_seconds": fraction_record(
                int(round(walltime_total * 10**12)), successes * 10**12
            ) if successes else None,
        },
        "maximum_stopping_stage": max(
            (row["stopping_stage"] for row in rows if row["stopping_stage"] is not None),
            default=None,
        ),
        "rows_with_anomalies": sum(bool(row["anomalies"]) for row in rows),
    }


def attach_uniform_ratios(policy_summaries):
    uniform = policy_summaries["uniform"]
    uniform_successes = uniform["total_successes"]
    uniform_totals = uniform["algorithm_operation_totals"]
    uniform_walltime = uniform["standalone_walltime_total_seconds"]
    metrics = (
        "gcd_calls",
        "gcd_euclidean_divisions",
        "floor_sum_calls",
        "floor_sum_euclidean_iterations",
        "random_fair_bits",
        "modular_inversion_calls",
        "modular_inverse_euclidean_divisions",
    )
    for summary in policy_summaries.values():
        successes = summary["total_successes"]
        ratios = {}
        for metric in metrics:
            numerator_total = summary["algorithm_operation_totals"].get(metric, 0)
            denominator_total = uniform_totals.get(metric, 0)
            if successes and uniform_successes and numerator_total and denominator_total:
                ratios[metric] = fraction_record(
                    numerator_total * uniform_successes,
                    successes * denominator_total,
                )
            else:
                ratios[metric] = None
        if successes and uniform_successes and uniform_walltime > 0:
            ratios["standalone_walltime"] = fraction_record(
                int(round(summary["standalone_walltime_total_seconds"] * 10**12))
                * uniform_successes,
                successes * int(round(uniform_walltime * 10**12)),
            )
        else:
            ratios["standalone_walltime"] = None
        summary["cost_per_success_ratio_to_uniform"] = ratios


def run_case(modulus_row, start, stop, keep_full_trace):
    rows = []
    witnesses = []
    anomalies = []
    RUN_PROGRESS.update(
        {
            "modulus_id": modulus_row["modulus_id"],
            "requested_trial_range": [start, stop],
            "completed_trials": 0,
            "completed_rows": 0,
        }
    )
    for trial_index in range(start, stop):
        trial_rows, trial_witnesses = run_trial(
            modulus_row, trial_index, keep_full_trace
        )
        rows.extend(trial_rows)
        witnesses.extend(trial_witnesses)
        anomalies.extend(
            {"row_id": row["row_id"], **anomaly}
            for row in trial_rows
            for anomaly in row["anomalies"]
        )
        RUN_PROGRESS["completed_trials"] += 1
        RUN_PROGRESS["completed_rows"] = len(rows)
        RUN_PROGRESS["last_trial_index"] = trial_index
        if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 512 MiB")
    by_policy = {}
    for row in rows:
        by_policy.setdefault(row["policy"], []).append(row)
    summaries = {
        policy: summarize_rows(policy_rows)
        for policy, policy_rows in sorted(by_policy.items())
    }
    if "uniform" in summaries:
        attach_uniform_ratios(summaries)
    return {
        "modulus": modulus_row,
        "trial_range": [start, stop],
        "trials": stop - start,
        "policy_rows": len(rows),
        "policy_summaries": summaries,
        "anomalies": anomalies,
    }, rows, witnesses


def artifact_record(path, rows):
    write_deterministic_gzip_jsonl(path, rows)
    return {
        "path": str(path),
        "sha256": sha256(path),
        "compressed_bytes": Path(path).stat().st_size,
        "rows": len(rows),
    }


def run_aggregate():
    modulus_rows = {row["modulus_id"]: row for row in load_moduli()}
    jobs = []
    all_rows = {modulus_id: [] for modulus_id in modulus_rows}
    coverage = {modulus_id: Counter() for modulus_id in modulus_rows}
    for path in sorted(EXPERIMENT_DIR.glob("scale_b*_output.json")):
        data = json.loads(path.read_text())
        if data.get("status") not in ("passed", "passed_with_anomalies"):
            raise ArithmeticError(f"non-passing scale output: {path}")
        case = data["case"]
        modulus_id = case["modulus"]["modulus_id"]
        if modulus_id not in modulus_rows:
            raise ArithmeticError("aggregate found unknown modulus")
        rows_path = Path(data["row_artifact"]["path"])
        if sha256(rows_path) != data["row_artifact"]["sha256"]:
            raise ArithmeticError("row artifact hash mismatch")
        rows = read_gzip_jsonl(rows_path)
        if len(rows) != data["row_artifact"]["rows"]:
            raise ArithmeticError("row artifact count mismatch")
        all_rows[modulus_id].extend(rows)
        for trial_index in range(*case["trial_range"]):
            coverage[modulus_id][trial_index] += 1
        jobs.append(
            {
                "output": str(path),
                "output_sha256": sha256(path),
                "row_artifact": data["row_artifact"],
                "witness_artifact": data["witness_artifact"],
                "trial_range": case["trial_range"],
                "walltime_seconds": data["walltime_seconds"],
                "peak_rss_bytes": data["peak_rss_bytes"],
            }
        )

    cases = []
    for modulus_id, modulus_row in modulus_rows.items():
        if coverage[modulus_id] != Counter({i: 1 for i in range(TRIALS_PER_PROFILE)}):
            raise ArithmeticError(f"incomplete or duplicate trial coverage: {modulus_id}")
        rows = all_rows[modulus_id]
        if len(rows) != 14 * TRIALS_PER_PROFILE:
            raise ArithmeticError("wrong aggregate policy-row count")
        by_policy = {}
        for row in rows:
            by_policy.setdefault(row["policy"], []).append(row)
        summaries = {
            policy: summarize_rows(policy_rows)
            for policy, policy_rows in sorted(by_policy.items())
        }
        if set(map(len, by_policy.values())) != {TRIALS_PER_PROFILE}:
            raise ArithmeticError("wrong aggregate per-policy denominator")
        attach_uniform_ratios(summaries)
        cases.append(
            {
                "modulus": modulus_row,
                "policy_summaries": summaries,
                "total_policy_rows": len(rows),
                "rows_with_anomalies": sum(bool(row["anomalies"]) for row in rows),
            }
        )
    return {
        "status": "passed_with_anomalies"
        if any(case["rows_with_anomalies"] for case in cases)
        else "passed",
        "experiment": "F336_biased_rational_inputs",
        "route": ROUTE,
        "mode": "aggregate",
        "scope": (
            "Exactly 128 reproducible finite trials for each of fourteen source "
            "profiles and each retained modulus. Offline factors label verified "
            "outputs only. No finite trend is an asymptotic success claim."
        ),
        "cases": cases,
        "jobs": jobs,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode", choices=("tiny", "pilot", "scale", "aggregate"), required=True
    )
    parser.add_argument("--modulus-id")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int, default=TRIALS_PER_PROFILE)
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
        "experiment": "F336_biased_rational_inputs",
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
        if arguments.mode == "tiny":
            payload = run_tiny()
        elif arguments.mode == "aggregate":
            payload = run_aggregate()
        else:
            if not arguments.rows or not arguments.witnesses:
                raise ValueError("row and witness artifacts are required")
            moduli = {row["modulus_id"]: row for row in load_moduli()}
            if arguments.mode == "pilot":
                selected = [moduli["b20_i0"], moduli["b20_i1"]]
                start, stop = 0, 2
                keep_full_trace = True
            else:
                if arguments.modulus_id not in moduli:
                    raise ValueError("unknown or missing modulus id")
                if not (0 <= arguments.start < arguments.stop <= TRIALS_PER_PROFILE):
                    raise ValueError("invalid trial range")
                selected = [moduli[arguments.modulus_id]]
                start, stop = arguments.start, arguments.stop
                keep_full_trace = False
            cases = []
            all_rows = []
            all_witnesses = []
            for modulus_row in selected:
                case, rows, witnesses = run_case(
                    modulus_row, start, stop, keep_full_trace
                )
                cases.append(case)
                all_rows.extend(rows)
                all_witnesses.extend(witnesses)
            payload = {
                "status": "passed_with_anomalies"
                if any(case["anomalies"] for case in cases)
                else "passed",
                "experiment": "F336_biased_rational_inputs",
                "route": ROUTE,
                "mode": arguments.mode,
                "case": cases[0] if arguments.mode == "scale" else None,
                "cases": cases if arguments.mode == "pilot" else None,
                "randomness_scope": (
                    "Independent reproducible fair-bit rejection streams. "
                    "Direct/inverse policy pairs share their denominator draw; "
                    "each standalone cost includes that generation work."
                ),
                "row_artifact": artifact_record(arguments.rows, all_rows),
                "witness_artifact": artifact_record(
                    arguments.witnesses, all_witnesses
                ),
            }
            if arguments.mode == "scale":
                payload.pop("cases")
            else:
                payload.pop("case")
        signal.alarm(0)
        payload.update(
            {
                "seed": SEED,
                "source_sha256": sha256(Path(__file__)),
                "dependency_sha256": {
                    "F334_count_descent": F334_SOURCE_SHA256,
                    "F328_moduli": F328_INPUT_SHA256,
                    "DESIGN": DESIGN_SHA256,
                    "MENU_BOUND": MENU_BOUND_SHA256,
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
        if "row_artifact" in payload:
            status["row_artifact"] = payload["row_artifact"]
            status["witness_artifact"] = payload["witness_artifact"]
        write_json(arguments.status, status)
        print(json.dumps({"event": payload["status"], **status}), flush=True)
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
