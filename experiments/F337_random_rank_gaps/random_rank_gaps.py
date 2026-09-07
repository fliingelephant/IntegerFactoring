#!/usr/bin/env python3
"""F337: exact finite useful-energy diagnostics for random rank gaps."""

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import random
import resource
import signal
import sys
import time
import traceback


ROOT = Path(__file__).resolve().parents[2]
EXPERIMENT_DIR = ROOT / "experiments" / "F337_random_rank_gaps"
F336_DIR = ROOT / "experiments" / "F336_biased_rational_inputs"
F336_SOURCE = F336_DIR / "biased_rational_inputs.py"
RANDOMIZED_WINDOWS = F336_DIR / "RANDOMIZED_WINDOWS.md"
INVERSE_GAP_TRANSFER = EXPERIMENT_DIR / "INVERSE_GAP_TRANSFER.md"
F334_SOURCE = ROOT / "experiments" / "F334_count_descent" / "count_descent.py"

F336_SOURCE_SHA256 = (
    "b660db8da032e3f514dfdfc5a4183defb5392b22d4cf8bcfa4ab9eaec57c5256"
)
RANDOMIZED_WINDOWS_SHA256 = (
    "421936d7e539483cfcb1dbf22302d166cd35e42d5c7bddb89921bcec1acfdb84"
)
INVERSE_GAP_TRANSFER_SHA256 = (
    "8254a944670559369014e2e984d69f61345e281fb0849f80a5c1a2becf12a51d"
)
F334_SOURCE_SHA256 = (
    "cb93f160d57b2a3285551cbd268e732917e3062a90eb8ca62df843f581be1e24"
)

SEED = 33720260907
ROUTE = "route:F31"
INPUTS = {
    209: (11, 19),
    1333: (31, 43),
    10807: (101, 107),
}
DIRECT_INVERSE_SCALES = ((1, 4), (1, 2))
RATIO_SCALES = ((1, 4), (3, 8))
ATTEMPTS_PER_LAW = 8
PILOT_ATTEMPTS_PER_LAW = 2
BATCH_SIZES = (2, 8, 32)
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 256 * 1024 * 1024
RUN_PROGRESS = {}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


if sha256(F336_SOURCE) != F336_SOURCE_SHA256:
    raise RuntimeError("frozen F336 sampler source hash changed")
sys.path.insert(0, str(F336_DIR))
import biased_rational_inputs as f336  # noqa: E402

f334 = f336.f334


def peak_rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def write_json(path, value):
    target = Path(path)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
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


def fraction_record(value):
    value = Fraction(value)
    return {
        "exact": str(value),
        "numerator": value.numerator,
        "denominator": value.denominator,
        "decimal": float(value),
    }


def ratio_record(numerator, denominator):
    if denominator == 0:
        return None
    return fraction_record(Fraction(numerator, denominator))


def validate_dependencies():
    expected = {
        F336_SOURCE: F336_SOURCE_SHA256,
        RANDOMIZED_WINDOWS: RANDOMIZED_WINDOWS_SHA256,
        INVERSE_GAP_TRANSFER: INVERSE_GAP_TRANSFER_SHA256,
        F334_SOURCE: F334_SOURCE_SHA256,
    }
    for path, expected_hash in expected.items():
        if sha256(path) != expected_hash:
            raise ArithmeticError(f"frozen dependency changed: {path}")
    if f334.CountOracle.floor_sum is not f334.GaussPairing.floor_sum:
        raise ArithmeticError("F334 CountOracle lost its frozen floor-sum method")


def checked_gcd(value, modulus, counts, category):
    divisor = f334.charged_gcd(value, modulus, counts, category)
    factor = divisor if 1 < divisor < modulus else None
    if factor is not None:
        if modulus % factor:
            raise ArithmeticError("gcd output is not a divisor")
        counts["factor_verification_divisions"] += 1
    return divisor, factor


def rank_count(oracle, t, threshold, counters):
    counters["rank_query_calls"] += 1
    before = dict(oracle.counters)
    value = t + oracle.floor_sum(t, oracle.n, oracle.a, oracle.a) - oracle.floor_sum(
        t, oracle.n, oracle.a, oracle.a + oracle.n - 1 - threshold
    )
    add_counts(counters, counter_delta(oracle.counters, before))
    if not 0 <= value <= t:
        raise ArithmeticError("rank query returned an invalid count")
    return value


def least_threshold_for_rank(oracle, t, target, counters):
    low, high = 0, oracle.n - 1
    while low < high:
        counters["rank_binary_search_iterations"] += 1
        middle = (low + high) // 2
        if rank_count(oracle, t, middle, counters) >= target:
            high = middle
        else:
            low = middle + 1
    if rank_count(oracle, t, low, counters) < target:
        raise ArithmeticError("rank binary search missed its target")
    if low and rank_count(oracle, t, low - 1, counters) >= target:
        raise ArithmeticError("rank binary search was not minimal")
    return low


def source_range(modulus, scale):
    lower = 1 << (scale["exponent"] - 1)
    upper = min((1 << scale["exponent"]) - 1, modulus - 1)
    first = lower if lower & 1 else lower + 1
    last = upper if upper & 1 else upper - 1
    return {
        "lower": lower,
        "upper": upper,
        "first_odd": first,
        "last_odd": last,
        "odd_value_count": (last - first) // 2 + 1,
    }


def factor_generation_record(
    attempt_id,
    policy,
    policy_kind,
    gamma,
    modulus,
    factors,
    parameters,
    seeds,
    ranges,
    counts,
    walltime,
):
    offline_factors = INPUTS[modulus]
    for factor in factors:
        if not (1 < factor < modulus and modulus % factor == 0):
            raise ArithmeticError("invalid generation factor")
    return {
        "attempt_id": attempt_id,
        "policy": policy,
        "policy_kind": policy_kind,
        "gamma": gamma,
        "status": "generation_factor",
        "a": None,
        "parameters": parameters,
        "source_seeds": seeds,
        "source_ranges": ranges,
        "generation_factors": factors,
        "offline_factor_labels": {
            str(factor): [prime for prime in offline_factors if factor % prime == 0]
            for factor in factors
        },
        "generation_operation_counts": dict(sorted(counts.items())),
        "generation_walltime_seconds": walltime,
        "cells": [],
        "anomalies": [],
    }


def unit_generation_record(
    attempt_id,
    policy,
    policy_kind,
    gamma,
    multiplier,
    parameters,
    seeds,
    ranges,
    counts,
    walltime,
):
    return {
        "attempt_id": attempt_id,
        "policy": policy,
        "policy_kind": policy_kind,
        "gamma": gamma,
        "status": "unit",
        "a": multiplier,
        "parameters": parameters,
        "source_seeds": seeds,
        "source_ranges": ranges,
        "generation_factors": [],
        "offline_factor_labels": {},
        "generation_operation_counts": dict(sorted(counts.items())),
        "generation_walltime_seconds": walltime,
        "cells": [],
        "anomalies": [],
    }


def paired_direct_inverse(modulus, attempt_index, scale):
    stream_seed = derived_seed(
        "paired_direct_inverse", modulus, attempt_index, scale["label"]
    )
    generator = random.Random(stream_seed)
    counts = Counter()
    started = time.perf_counter()
    denominator, ranges = f336.sample_odd_value(modulus, scale, generator, counts)
    divisor, factor = checked_gcd(
        denominator, modulus, counts, "source_generation"
    )
    common_parameters = {
        "paired_draw": denominator,
        "raw_numerator": None,
        "raw_denominator": denominator,
    }
    seeds = {"paired_draw": stream_seed}
    gamma = {key: scale[key] for key in ("numerator", "denominator", "exponent")}
    records = []
    if factor is not None:
        elapsed = time.perf_counter() - started
        for policy_kind in ("direct", "inverse"):
            policy = f"{policy_kind}_{scale['label']}"
            records.append(
                factor_generation_record(
                    f"N{modulus}:{attempt_index}:{policy}",
                    policy,
                    policy_kind,
                    gamma,
                    modulus,
                    [factor],
                    common_parameters,
                    seeds,
                    ranges,
                    counts,
                    elapsed,
                )
            )
        return records
    if divisor != 1:
        raise ArithmeticError("source gcd was neither unit nor proper factor")

    generation_elapsed = time.perf_counter() - started
    direct_policy = f"direct_{scale['label']}"
    records.append(
        unit_generation_record(
            f"N{modulus}:{attempt_index}:{direct_policy}",
            direct_policy,
            "direct",
            gamma,
            denominator,
            {
                **common_parameters,
                "reduced_numerator": denominator,
                "reduced_denominator": 1,
            },
            seeds,
            ranges,
            counts,
            generation_elapsed,
        )
    )

    inverse_counts = Counter(counts)
    inverse_started = time.perf_counter()
    multiplier = f334.charged_mod_inverse(
        denominator, modulus, inverse_counts, "source_transform"
    )
    inverse_elapsed = time.perf_counter() - inverse_started
    inverse_policy = f"inverse_{scale['label']}"
    records.append(
        unit_generation_record(
            f"N{modulus}:{attempt_index}:{inverse_policy}",
            inverse_policy,
            "inverse",
            gamma,
            multiplier,
            {
                **common_parameters,
                "reduced_numerator": 1,
                "reduced_denominator": denominator,
            },
            seeds,
            ranges,
            inverse_counts,
            generation_elapsed + inverse_elapsed,
        )
    )
    return records


def ratio_generation(modulus, attempt_index, scale):
    numerator_seed = derived_seed(
        "ratio_numerator", modulus, attempt_index, scale["label"]
    )
    denominator_seed = derived_seed(
        "ratio_denominator", modulus, attempt_index, scale["label"]
    )
    numerator_generator = random.Random(numerator_seed)
    denominator_generator = random.Random(denominator_seed)
    counts = Counter()
    started = time.perf_counter()
    numerator, numerator_range = f336.sample_odd_value(
        modulus, scale, numerator_generator, counts
    )
    denominator, denominator_range = f336.sample_odd_value(
        modulus, scale, denominator_generator, counts
    )
    _, numerator_factor = checked_gcd(
        numerator, modulus, counts, "numerator_generation"
    )
    denominator_factor = None
    if numerator_factor is None:
        _, denominator_factor = checked_gcd(
            denominator, modulus, counts, "denominator_generation"
        )
    factors = sorted(
        factor
        for factor in (numerator_factor, denominator_factor)
        if factor is not None
    )
    parameters = {
        "raw_numerator": numerator,
        "raw_denominator": denominator,
        "reduced_numerator": None,
        "reduced_denominator": None,
    }
    seeds = {"numerator": numerator_seed, "denominator": denominator_seed}
    ranges = {"numerator": numerator_range, "denominator": denominator_range}
    policy = f"ratio_{scale['label']}"
    gamma = {key: scale[key] for key in ("numerator", "denominator", "exponent")}
    attempt_id = f"N{modulus}:{attempt_index}:{policy}"
    if factors:
        return factor_generation_record(
            attempt_id,
            policy,
            "ratio",
            gamma,
            modulus,
            factors,
            parameters,
            seeds,
            ranges,
            counts,
            time.perf_counter() - started,
        )

    common = f334.charged_gcd(
        numerator, denominator, counts, "rational_reduction"
    )
    reduced_numerator = numerator // common
    reduced_denominator = denominator // common
    multiplier = f334.charged_mod_inverse(
        reduced_denominator, modulus, counts, "source_transform"
    )
    multiplier = reduced_numerator * multiplier % modulus
    if multiplier * reduced_denominator % modulus != reduced_numerator % modulus:
        raise ArithmeticError("ratio source relation failed")
    return unit_generation_record(
        attempt_id,
        policy,
        "ratio",
        gamma,
        multiplier,
        {
            **parameters,
            "ordinary_common_gcd": common,
            "reduced_numerator": reduced_numerator,
            "reduced_denominator": reduced_denominator,
        },
        seeds,
        ranges,
        counts,
        time.perf_counter() - started,
    )


def uniform_generation(modulus, attempt_index):
    stream_seed = derived_seed("uniform", modulus, attempt_index)
    generator = random.Random(stream_seed)
    counts = Counter()
    started = time.perf_counter()
    multiplier = f336.sample_uniform_nonzero(modulus, generator, counts)
    _, factor = checked_gcd(multiplier, modulus, counts, "source_generation")
    parameters = {
        "raw_numerator": multiplier,
        "raw_denominator": 1,
        "reduced_numerator": multiplier if factor is None else None,
        "reduced_denominator": 1 if factor is None else None,
    }
    ranges = {"lower": 1, "upper": modulus - 1, "value_count": modulus - 1}
    attempt_id = f"N{modulus}:{attempt_index}:uniform"
    if factor is not None:
        return factor_generation_record(
            attempt_id,
            "uniform",
            "uniform",
            None,
            modulus,
            [factor],
            parameters,
            {"uniform_nonzero": stream_seed},
            ranges,
            counts,
            time.perf_counter() - started,
        )
    return unit_generation_record(
        attempt_id,
        "uniform",
        "uniform",
        None,
        multiplier,
        parameters,
        {"uniform_nonzero": stream_seed},
        ranges,
        counts,
        time.perf_counter() - started,
    )


def generate_parameters(modulus, attempts_per_law):
    records = []
    bit_length = modulus.bit_length()
    for attempt_index in range(attempts_per_law):
        for numerator, denominator in DIRECT_INVERSE_SCALES:
            scale = f336.scale_record(bit_length, numerator, denominator)
            records.extend(
                paired_direct_inverse(modulus, attempt_index, scale)
            )
        for numerator, denominator in RATIO_SCALES:
            scale = f336.scale_record(bit_length, numerator, denominator)
            records.append(ratio_generation(modulus, attempt_index, scale))
        records.append(uniform_generation(modulus, attempt_index))
    if len(records) != 7 * attempts_per_law:
        raise ArithmeticError("parameter generator produced the wrong law count")
    return records


def weights_record(numerators, denominator, modulus, p, q, validate_quadratic):
    if len(numerators) >= modulus:
        raise ArithmeticError("rank support must be smaller than N")
    if sum(numerators) != denominator:
        raise ArithmeticError("weights do not sum to one")
    size = len(numerators)
    same_numerator = sum(value * value for value in numerators)
    grouped_p = [0] * p
    grouped_q = [0] * q
    for index, value in enumerate(numerators):
        grouped_p[index % p] += value
        grouped_q[index % q] += value
    kappa_p_numerator = sum(value * value for value in grouped_p)
    kappa_q_numerator = sum(value * value for value in grouped_q)
    delta_numerator = kappa_p_numerator + kappa_q_numerator - 2 * same_numerator
    if delta_numerator < 0:
        raise ArithmeticError("useful energy became negative")

    direct_numerator = sum(
        value
        for index, value in enumerate(numerators)
        if 1 < math.gcd(index, modulus) < modulus
    )
    d_numerators = [
        grouped_p[index % p] + grouped_q[index % q] - 2 * value
        for index, value in enumerate(numerators)
    ]
    if any(value < 0 for value in d_numerators):
        raise ArithmeticError("conditional useful mass became negative")
    if sum(
        weight * conditional
        for weight, conditional in zip(numerators, d_numerators)
    ) != delta_numerator:
        raise ArithmeticError("grouped delta identity failed")
    eta_numerator = sum(
        weight * conditional * conditional
        for weight, conditional in zip(numerators, d_numerators)
    )

    if validate_quadratic:
        brute_delta_numerator = 0
        for left, left_weight in enumerate(numerators):
            for right, right_weight in enumerate(numerators):
                divisor = math.gcd(left - right, modulus)
                if 1 < divisor < modulus:
                    brute_delta_numerator += left_weight * right_weight
        if brute_delta_numerator != delta_numerator:
            raise ArithmeticError("quadratic useful-energy identity failed")

    delta = Fraction(delta_numerator, denominator * denominator)
    eta = Fraction(eta_numerator, denominator**3)
    batch = {}
    for batch_size in BATCH_SIZES:
        first = math.comb(batch_size, 2) * delta
        second = (
            math.comb(batch_size, 2) * delta
            + 6 * math.comb(batch_size, 3) * eta
            + 6 * math.comb(batch_size, 4) * delta * delta
        )
        lower = first * first / second if second else Fraction(0, 1)
        batch[str(batch_size)] = {
            "E_T": fraction_record(first),
            "E_T_squared": fraction_record(second),
            "second_moment_success_lower_bound": fraction_record(lower),
        }
    return {
        "support_size": size,
        "weight_denominator": denominator,
        "kappa_p": fraction_record(Fraction(kappa_p_numerator, denominator**2)),
        "kappa_q": fraction_record(Fraction(kappa_q_numerator, denominator**2)),
        "kappa_same": fraction_record(Fraction(same_numerator, denominator**2)),
        "direct_count_factor_mass": fraction_record(
            Fraction(direct_numerator, denominator)
        ),
        "delta": fraction_record(delta),
        "eta": fraction_record(eta),
        "batch_bounds": batch,
        "quadratic_validation": "passed" if validate_quadratic else "not_run",
    }


def useful_class_pair_energy(left_ranks, right_ranks, modulus, p, q):
    left_p = Counter(index % p for index in left_ranks)
    right_p = Counter(index % p for index in right_ranks)
    left_q = Counter(index % q for index in left_ranks)
    right_q = Counter(index % q for index in right_ranks)
    same = len(set(left_ranks) & set(right_ranks))
    numerator = (
        sum(value * right_p.get(residue, 0) for residue, value in left_p.items())
        + sum(value * right_q.get(residue, 0) for residue, value in left_q.items())
        - 2 * same
    )
    return fraction_record(Fraction(numerator, len(left_ranks) * len(right_ranks)))


def ratios_to_uniform(law, uniform):
    result = {}
    for key in (
        "kappa_p",
        "kappa_q",
        "kappa_same",
        "direct_count_factor_mass",
        "delta",
        "eta",
    ):
        numerator = Fraction(law[key]["numerator"], law[key]["denominator"])
        denominator = Fraction(
            uniform[key]["numerator"], uniform[key]["denominator"]
        )
        result[key] = fraction_record(numerator / denominator) if denominator else None
    result["batch_bounds"] = {}
    for batch_size in map(str, BATCH_SIZES):
        numerator_record = law["batch_bounds"][batch_size][
            "second_moment_success_lower_bound"
        ]
        denominator_record = uniform["batch_bounds"][batch_size][
            "second_moment_success_lower_bound"
        ]
        numerator = Fraction(
            numerator_record["numerator"], numerator_record["denominator"]
        )
        denominator = Fraction(
            denominator_record["numerator"], denominator_record["denominator"]
        )
        result["batch_bounds"][batch_size] = (
            fraction_record(numerator / denominator) if denominator else None
        )
    return result


def rank_set_hash(ranks):
    digest = hashlib.sha256()
    for rank in ranks:
        digest.update(str(rank).encode())
        digest.update(b",")
    return digest.hexdigest()


def inverse_gap_transfer_diagnostic(modulus, parameter, t, points, rank_by_residue):
    if parameter["policy_kind"] != "inverse":
        return {"status": "not_an_inverse_source"}
    denominator = parameter["parameters"]["reduced_denominator"]
    size = t + 1
    if denominator > size:
        return {
            "status": "not_evaluated_b_greater_than_m",
            "b": denominator,
            "m": size,
        }
    quotient, remainder = divmod(size, denominator)
    sigmas = [(-modulus * index) % denominator for index in range(denominator)]
    starts = [
        (modulus * index + sigmas[index]) // denominator
        for index in range(denominator)
    ]
    lengths = [
        quotient + int(sigma < remainder)
        for sigma in sigmas
    ]
    expected_points = [
        start + offset
        for start, length in zip(starts, lengths)
        for offset in range(length)
    ]
    if expected_points != points:
        raise ArithmeticError(
            f"inverse cluster expansion mismatch N={modulus} a={parameter['a']} "
            f"b={denominator} t={t}"
        )
    cumulative = 0
    boundary_ranks = []
    for index, sigma in enumerate(sigmas):
        cumulative += sigma < remainder
        rank = quotient * (index + 1) + cumulative - 1
        if rank != rank_by_residue[starts[index] + lengths[index] - 1]:
            raise ArithmeticError(
                f"inverse boundary-rank mismatch N={modulus} "
                f"a={parameter['a']} b={denominator} t={t} j={index}"
            )
        boundary_ranks.append(rank)

    half_pair_check = None
    if t == (modulus - 1) // 2:
        residual_digest = hashlib.sha256()
        proper_pairs = []
        minimum_abs_residual = None
        maximum_abs_residual = 0
        pair_checks = 0
        cumulative_flags = []
        running = 0
        for sigma in sigmas:
            running += sigma < remainder
            cumulative_flags.append(running)
        for left in range(denominator):
            for right in range(left + 1, denominator):
                difference = right - left
                excess = cumulative_flags[right] - cumulative_flags[left]
                residual = (
                    (1 - 2 * remainder) * difference
                    + 2 * denominator * excess
                )
                rank_difference = boundary_ranks[right] - boundary_ranks[left]
                if 2 * denominator * rank_difference != modulus * difference + residual:
                    raise ArithmeticError(
                        f"inverse half residual identity mismatch N={modulus} "
                        f"a={parameter['a']} b={denominator} k={left} l={right}"
                    )
                left_gcd = math.gcd(rank_difference, modulus)
                right_gcd = math.gcd(residual, modulus)
                if left_gcd != right_gcd:
                    raise ArithmeticError(
                        f"inverse half gcd transfer mismatch N={modulus} "
                        f"a={parameter['a']} b={denominator} k={left} l={right}"
                    )
                if residual == 0 or abs(residual) >= 2 * denominator * denominator:
                    raise ArithmeticError(
                        f"inverse half residual bound mismatch N={modulus} "
                        f"a={parameter['a']} b={denominator} k={left} l={right} "
                        f"E={residual}"
                    )
                minimum_abs_residual = (
                    abs(residual)
                    if minimum_abs_residual is None
                    else min(minimum_abs_residual, abs(residual))
                )
                maximum_abs_residual = max(maximum_abs_residual, abs(residual))
                residual_digest.update(
                    f"{left},{right},{residual},{left_gcd};".encode()
                )
                if 1 < left_gcd < modulus:
                    proper_pairs.append(
                        {
                            "k": left,
                            "l": right,
                            "rank_difference": rank_difference,
                            "residual": residual,
                            "factor": left_gcd,
                        }
                    )
                pair_checks += 1
        least_prime = min(INPUTS[modulus])
        exclusion_applies = least_prime > 2 * denominator * denominator
        if exclusion_applies and proper_pairs:
            raise ArithmeticError(
                f"inverse guarded boundary exclusion failed N={modulus} "
                f"a={parameter['a']} b={denominator}"
            )
        half_pair_check = {
            "pair_checks": pair_checks,
            "minimum_absolute_residual": minimum_abs_residual,
            "maximum_absolute_residual": maximum_abs_residual,
            "strict_bound": 2 * denominator * denominator,
            "residual_gcd_sha256": residual_digest.hexdigest(),
            "proper_gcd_pairs": proper_pairs,
            "least_prime_offline_label": least_prime,
            "least_prime_exclusion_applies": exclusion_applies,
            "status": "passed",
        }
    return {
        "status": "passed",
        "b": denominator,
        "m": size,
        "L": quotient,
        "r": remainder,
        "sigma": sigmas,
        "cluster_starts": starts,
        "cluster_lengths": lengths,
        "boundary_ranks": boundary_ranks,
        "cluster_points": len(expected_points),
        "half_orbit_pair_check": half_pair_check,
    }


def analyze_cell(modulus, p, q, parameter, t):
    multiplier = parameter["a"]
    half = (modulus - 1) // 2
    if not (1 <= t < modulus and math.gcd(multiplier, modulus) == 1):
        raise ArithmeticError("invalid rank-gap cell input")

    control_counts = Counter()
    gcd_t, factor_t = checked_gcd(t, modulus, control_counts, "screen_t")
    gcd_t_plus_one, factor_t_plus_one = checked_gcd(
        t + 1, modulus, control_counts, "control_t_plus_one"
    )

    residues_by_orbit = [multiplier * index % modulus for index in range(t + 1)]
    if len(set(residues_by_orbit)) != t + 1:
        raise ArithmeticError("orbit prefix contains a duplicate")
    points = sorted(residues_by_orbit)
    if points[0] != 0 or len(points) != t + 1:
        raise ArithmeticError("sorted orbit has the wrong support")
    rank_by_residue = {value: index for index, value in enumerate(points)}
    gaps = [
        (points[(index + 1) % len(points)] - points[index]) % modulus
        for index in range(len(points))
    ]
    if any(gap <= 0 for gap in gaps) or sum(gaps) != modulus:
        raise ArithmeticError("cyclic gaps are not a positive partition of N")

    setup_oracle = f334.CountOracle(modulus, multiplier)
    setup_counts = Counter()
    alpha = least_threshold_for_rank(setup_oracle, t, 1, setup_counts)
    maximum_residue = least_threshold_for_rank(setup_oracle, t, t, setup_counts)
    beta = modulus - maximum_residue
    inverse = f334.charged_mod_inverse(
        multiplier, modulus, setup_counts, "gap_setup"
    )
    u = alpha * inverse % modulus
    v = maximum_residue * inverse % modulus
    size = t + 1
    if alpha != points[1] or maximum_residue != points[-1]:
        raise ArithmeticError("rank-query extremum disagrees with sorted orbit")
    if not (1 <= u <= t and 1 <= v <= t and u + v >= size):
        raise ArithmeticError("three-gap extremal indices failed their guards")

    class_specs = [
        ("plus_u", range(0, size - u), u, alpha),
        ("wrap_minus_v", range(v, size), -v, beta),
        ("middle_u_minus_v", range(size - u, v), u - v, alpha + beta),
    ]
    classes = []
    successor_checks = 0
    class_validation_counts = Counter()
    class_oracle = f334.CountOracle(modulus, multiplier)
    all_class_ranks = []
    for name, index_range, move, length in class_specs:
        indices = list(index_range)
        if not indices:
            continue
        ranks = []
        for orbit_index in indices:
            expected_successor = orbit_index + move
            if not 0 <= expected_successor < size:
                raise ArithmeticError("successor index left the orbit prefix")
            residue = residues_by_orbit[orbit_index]
            successor_residue = residues_by_orbit[expected_successor]
            actual_gap = (successor_residue - residue) % modulus
            if actual_gap != length:
                raise ArithmeticError("three-class successor gap mismatch")
            rank = rank_count(class_oracle, t, residue, class_validation_counts)
            if rank != rank_by_residue[residue]:
                raise ArithmeticError("class rank query disagrees with sorted rank")
            ranks.append(rank)
            successor_checks += 1
        if len(set(ranks)) != len(indices):
            raise ArithmeticError("class rank image contains duplicates")
        all_class_ranks.extend(ranks)
        classes.append(
            {
                "name": name,
                "orbit_index_lower": indices[0],
                "orbit_index_upper": indices[-1],
                "size": len(indices),
                "successor_move": move,
                "gap_length": length,
                "rank_set_minimum": min(ranks),
                "rank_set_maximum": max(ranks),
                "rank_set_sha256": rank_set_hash(sorted(ranks)),
                "ranks_internal": ranks,
            }
        )
    if sorted(all_class_ranks) != list(range(size)):
        raise ArithmeticError("class rank images do not partition all ranks")
    if successor_checks != size:
        raise ArithmeticError("successor table did not cover every orbit index")

    closed_same_numerator = sum(
        item[1].stop - item[1].start
        for item in class_specs
        if item[1].stop > item[1].start
    )
    if closed_same_numerator != size:
        raise ArithmeticError("class sizes do not sum to t+1")
    closed_same_numerator = (
        (size - u) * alpha * alpha
        + (size - v) * beta * beta
        + (u + v - size) * (alpha + beta) * (alpha + beta)
    )
    if closed_same_numerator != sum(gap * gap for gap in gaps):
        raise ArithmeticError("closed kappa_same formula failed")

    inverse_transfer = inverse_gap_transfer_diagnostic(
        modulus, parameter, t, points, rank_by_residue
    )

    threshold_seed = derived_seed(
        "threshold_validation", parameter["attempt_id"], t
    )
    threshold_generator = random.Random(threshold_seed)
    threshold_counts = Counter()
    thresholds = [0, modulus - 1]
    thresholds.extend(
        f334.bounded_sample(threshold_generator, modulus, threshold_counts)
        for _ in range(16)
    )
    threshold_oracle = f334.CountOracle(modulus, multiplier)
    threshold_rows = []
    for threshold in thresholds:
        value = rank_count(threshold_oracle, t, threshold, threshold_counts)
        expected = sum(point <= threshold for point in points) - 1
        if value != expected:
            raise ArithmeticError("rank threshold formula disagrees with sorted array")
        threshold_rows.append({"U": threshold, "rank": value})

    mu_numerators = gaps
    uniform_numerators = [1] * size
    class_lcm = math.lcm(*(item["size"] for item in classes))
    nu_denominator = len(classes) * class_lcm
    nu_numerators = [0] * size
    for item in classes:
        weight = class_lcm // item["size"]
        for rank in item["ranks_internal"]:
            if nu_numerators[rank]:
                raise ArithmeticError("nu class images overlap")
            nu_numerators[rank] = weight
    if any(value == 0 for value in nu_numerators):
        raise ArithmeticError("nu omitted a rank")

    validate_quadratic = modulus == 209
    laws = {
        "mu": weights_record(
            mu_numerators, modulus, modulus, p, q, validate_quadratic
        ),
        "nu": weights_record(
            nu_numerators, nu_denominator, modulus, p, q, validate_quadratic
        ),
        "uniform_rank": weights_record(
            uniform_numerators, size, modulus, p, q, validate_quadratic
        ),
    }
    if laws["mu"]["kappa_same"]["numerator"] * (
        modulus * modulus // laws["mu"]["kappa_same"]["denominator"]
    ) != closed_same_numerator:
        # The reduced fraction makes a direct cross-product clearer below.
        observed = Fraction(
            laws["mu"]["kappa_same"]["numerator"],
            laws["mu"]["kappa_same"]["denominator"],
        )
        if observed != Fraction(closed_same_numerator, modulus * modulus):
            raise ArithmeticError("mu duplicate energy disagrees with closed formula")

    for name, law in laws.items():
        law["ratios_to_uniform_rank"] = ratios_to_uniform(
            law, laws["uniform_rank"]
        )
        if name == "mu":
            law["runtime_contract"] = {
                "setup_rank_queries": 0,
                "rank_queries_per_sample": 1,
                "threshold_draws_per_sample": 1,
            }
        elif name == "uniform_rank":
            law["runtime_contract"] = {
                "setup_rank_queries": 0,
                "rank_queries_per_sample": 1,
                "orbit_index_draws_per_sample": 1,
            }
        else:
            law["runtime_contract"] = {
                "setup_operation_counts": dict(sorted(setup_counts.items())),
                "rank_queries_per_sample": 1,
                "class_draws_per_sample": 1,
                "orbit_index_draws_per_sample": 1,
            }

    class_pair_energies = {}
    for left in classes:
        class_pair_energies[left["name"]] = {}
        for right in classes:
            class_pair_energies[left["name"]][right["name"]] = (
                useful_class_pair_energy(
                    left["ranks_internal"],
                    right["ranks_internal"],
                    modulus,
                    p,
                    q,
                )
            )

    public_classes = []
    for item in classes:
        public_classes.append(
            {key: value for key, value in item.items() if key != "ranks_internal"}
        )
    return {
        "t": t,
        "t_scale": (
            "sqrt"
            if t == math.isqrt(modulus)
            else "eighth"
            if t == (modulus - 1) // 8
            else "half"
        ),
        "controls": {
            "gcd_t": gcd_t,
            "factor_at_t": factor_t,
            "gcd_t_plus_one": gcd_t_plus_one,
            "factor_at_t_plus_one": factor_t_plus_one,
            "operation_counts": dict(sorted(control_counts.items())),
        },
        "rank_support_size": size,
        "endpoint_ranks": {
            "rank_zero": {"rank": 0, "gap": gaps[0]},
            "rank_t": {"rank": t, "gap": gaps[t]},
            "kept_as_distinct_integer_ranks": True,
        },
        "extrema": {
            "alpha": alpha,
            "u": u,
            "beta": beta,
            "v": v,
            "u_plus_v": u + v,
            "m": size,
        },
        "classes": public_classes,
        "class_pair_useful_energies": class_pair_energies,
        "closed_kappa_same": fraction_record(
            Fraction(closed_same_numerator, modulus * modulus)
        ),
        "laws": laws,
        "setup_operation_counts": dict(sorted(setup_counts.items())),
        "offline_class_validation": {
            "successor_checks": successor_checks,
            "full_image_rank_queries": class_validation_counts[
                "rank_query_calls"
            ],
            "operation_counts": dict(sorted(class_validation_counts.items())),
            "status": "passed",
        },
        "threshold_validation": {
            "seed": threshold_seed,
            "thresholds": threshold_rows,
            "operation_counts": dict(sorted(threshold_counts.items())),
            "status": "passed",
        },
        "inverse_gap_transfer": inverse_transfer,
        "quadratic_validation": (
            "direct_O(t^2)_passed" if validate_quadratic else "grouped_sums_only"
        ),
        "anomalies": [],
    }


def run_modulus(modulus, attempts_per_law, mode):
    p, q = INPUTS[modulus]
    if p * q != modulus or p == q:
        raise ArithmeticError("offline labels are not distinct factors")
    t_values = sorted(
        {
            max(1, min(modulus - 1, math.isqrt(modulus))),
            max(1, min(modulus - 1, (modulus - 1) // 8)),
            max(1, min(modulus - 1, (modulus - 1) // 2)),
        }
    )
    if len(t_values) != 3:
        raise ArithmeticError("prescribed t scales were not distinct")
    parameters = generate_parameters(modulus, attempts_per_law)
    anomalies = []
    RUN_PROGRESS.update(
        {
            "mode": mode,
            "modulus": modulus,
            "parameter_records": len(parameters),
            "completed_parameter_records": 0,
            "completed_cells": 0,
        }
    )
    stop_after_anomaly = False
    for parameter in parameters:
        if parameter["status"] == "unit":
            for t in t_values:
                try:
                    cell = analyze_cell(modulus, p, q, parameter, t)
                except ArithmeticError as exception:
                    anomaly = {
                        "kind": "author_identity_or_protocol_violation",
                        "attempt_id": parameter["attempt_id"],
                        "policy": parameter["policy"],
                        "a": parameter["a"],
                        "t": t,
                        "message": str(exception),
                    }
                    parameter["anomalies"].append(anomaly)
                    anomalies.append(anomaly)
                    stop_after_anomaly = True
                    break
                parameter["cells"].append(cell)
                anomalies.extend(
                    {"attempt_id": parameter["attempt_id"], "t": t, **item}
                    for item in cell["anomalies"]
                )
                RUN_PROGRESS["completed_cells"] += 1
        RUN_PROGRESS["completed_parameter_records"] += 1
        RUN_PROGRESS["last_attempt_id"] = parameter["attempt_id"]
        if stop_after_anomaly:
            break
        if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 256 MiB")

    policies = sorted({parameter["policy"] for parameter in parameters})
    summaries = {}
    for policy in policies:
        rows = [parameter for parameter in parameters if parameter["policy"] == policy]
        if len(rows) != attempts_per_law:
            raise ArithmeticError("wrong per-law attempt count")
        unit_rows = [row for row in rows if row["status"] == "unit"]
        summaries[policy] = {
            "attempts": len(rows),
            "unit_parameters": len(unit_rows),
            "generation_factor_attempts": len(rows) - len(unit_rows),
            "distinct_unit_parameters": len({row["a"] for row in unit_rows}),
            "diagnostic_cells": sum(len(row["cells"]) for row in rows),
            "factor_at_t_controls": sum(
                cell["controls"]["factor_at_t"] is not None
                for row in unit_rows
                for cell in row["cells"]
            ),
            "factor_at_t_plus_one_controls": sum(
                cell["controls"]["factor_at_t_plus_one"] is not None
                for row in unit_rows
                for cell in row["cells"]
            ),
        }
    return {
        "modulus": modulus,
        "actual_bits": modulus.bit_length(),
        "offline_factor_labels": [p, q],
        "attempts_per_law": attempts_per_law,
        "t_values": t_values,
        "parameters": parameters,
        "policy_summaries": summaries,
        "anomalies": anomalies,
    }


def summarize_result(data):
    summaries = []
    for case in data["cases"]:
        energy = {
            law: {"positive_delta_cells": 0, "delta_sum": Fraction(0, 1)}
            for law in ("mu", "nu", "uniform_rank")
        }
        cells = 0
        for parameter in case["parameters"]:
            for cell in parameter["cells"]:
                cells += 1
                for law in energy:
                    delta = Fraction(
                        cell["laws"][law]["delta"]["numerator"],
                        cell["laws"][law]["delta"]["denominator"],
                    )
                    energy[law]["delta_sum"] += delta
                    energy[law]["positive_delta_cells"] += delta > 0
        summaries.append(
            {
                "modulus": case["modulus"],
                "actual_bits": case["actual_bits"],
                "parameter_attempts": len(case["parameters"]),
                "unit_parameters": sum(
                    row["status"] == "unit" for row in case["parameters"]
                ),
                "generation_factor_attempts": sum(
                    row["status"] == "generation_factor"
                    for row in case["parameters"]
                ),
                "diagnostic_cells": cells,
                "factor_at_t_controls": sum(
                    summary["factor_at_t_controls"]
                    for summary in case["policy_summaries"].values()
                ),
                "factor_at_t_plus_one_controls": sum(
                    summary["factor_at_t_plus_one_controls"]
                    for summary in case["policy_summaries"].values()
                ),
                "energy": {
                    law: {
                        "positive_delta_cells": record["positive_delta_cells"],
                        "mean_delta": fraction_record(
                            record["delta_sum"] / cells if cells else 0
                        ),
                    }
                    for law, record in energy.items()
                },
                "anomalies": len(case["anomalies"]),
            }
        )
    return summaries


def run_aggregate():
    paths = [EXPERIMENT_DIR / f"full_N{modulus}_output.json" for modulus in INPUTS]
    references = []
    summaries = []
    for path in paths:
        data = json.loads(path.read_text())
        if data["status"] != "passed":
            raise ArithmeticError(f"non-passing full result: {path}")
        summaries.extend(data["summary"])
        references.append(
            {
                "path": str(path),
                "sha256": sha256(path),
                "walltime_seconds": data["walltime_seconds"],
                "peak_rss_bytes": data["peak_rss_bytes"],
            }
        )
    return {
        "status": "passed",
        "experiment": "F337_random_rank_gaps",
        "route": ROUTE,
        "mode": "aggregate",
        "scope": (
            "Exact finite diagnostics for three inputs, seven source laws, "
            "eight parameter attempts per law, and three thresholds. Offline "
            "factor labels are used only in energy diagnostics and validation."
        ),
        "summary": summaries,
        "input_artifacts": references,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("pilot", "full", "aggregate"), required=True)
    parser.add_argument("--modulus", type=int)
    parser.add_argument("--output", required=True)
    parser.add_argument("--status", required=True)
    arguments = parser.parse_args()
    started = time.perf_counter()
    validate_dependencies()

    def timeout_handler(_signal_number, _frame):
        raise TimeoutError("internal 28-second alarm fired")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(INTERNAL_TIMEOUT_SECONDS)
    running = {
        "status": "running",
        "experiment": "F337_random_rank_gaps",
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
            cases = [run_modulus(209, PILOT_ATTEMPTS_PER_LAW, "pilot")]
            payload = {
                "status": "passed" if not cases[0]["anomalies"] else "anomaly",
                "experiment": "F337_random_rank_gaps",
                "route": ROUTE,
                "mode": "pilot",
                "cases": cases,
                "scope": "N=209 pilot with two attempts per each of seven laws.",
            }
        elif arguments.mode == "full":
            if arguments.modulus not in INPUTS:
                raise ValueError("full mode requires a prescribed modulus")
            cases = [run_modulus(arguments.modulus, ATTEMPTS_PER_LAW, "full")]
            payload = {
                "status": "passed" if not cases[0]["anomalies"] else "anomaly",
                "experiment": "F337_random_rank_gaps",
                "route": ROUTE,
                "mode": "full",
                "cases": cases,
                "scope": (
                    "Eight attempts per each of seven source laws; three public "
                    "t scales per unit parameter."
                ),
            }
        else:
            payload = run_aggregate()
        if payload["status"] == "anomaly":
            payload["first_anomaly"] = next(
                anomaly
                for case in payload["cases"]
                for anomaly in case["anomalies"]
            )
        if arguments.mode != "aggregate":
            payload["summary"] = summarize_result(payload)
        signal.alarm(0)
        payload.update(
            {
                "seed": SEED,
                "source_sha256": sha256(Path(__file__)),
                "dependency_sha256": {
                    "RANDOMIZED_WINDOWS": RANDOMIZED_WINDOWS_SHA256,
                    "INVERSE_GAP_TRANSFER": INVERSE_GAP_TRANSFER_SHA256,
                    "F336_sampler": F336_SOURCE_SHA256,
                    "F334_floor_sum": F334_SOURCE_SHA256,
                },
                "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
                "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
                "memory_limit_bytes": MEMORY_LIMIT_BYTES,
                "walltime_seconds": time.perf_counter() - started,
                "peak_rss_bytes": peak_rss_bytes(),
            }
        )
        if payload["peak_rss_bytes"] > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 256 MiB")
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
        if "first_anomaly" in payload:
            status["first_anomaly"] = payload["first_anomaly"]
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
