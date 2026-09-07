#!/usr/bin/env python3
"""F339: exact finite search for public nonuniform coupled rank jumps."""

import argparse
from collections import Counter
from fractions import Fraction
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
EXPERIMENT_DIR = ROOT / "experiments" / "F339_coupled_rank_sources"
F337_DIR = ROOT / "experiments" / "F337_random_rank_gaps"
F337_SOURCE = F337_DIR / "random_rank_gaps.py"
RETURN_MAP = EXPERIMENT_DIR / "RETURN_MAP_JUMPS.md"
DESIGN = EXPERIMENT_DIR / "COUPLING_SEARCH.md"
IDENTITY_CHECK = EXPERIMENT_DIR / "check_output.json"

F337_SOURCE_SHA256 = (
    "187e35a09f704ce29bdce7c42820a23551801cb835a80fc32575f4732e4e08e1"
)
RETURN_MAP_SHA256 = (
    "cbe3426744bb0d263a4439afdcd0847d7f1fe6992a18217914b2f857c970b8a8"
)
DESIGN_SHA256 = "50f50d5c75e68388d0ce62ebcc8371d2525c5270165b10f559c5105a67e1a0f5"
IDENTITY_CHECK_SHA256 = (
    "66107520aa0305b227bfe2bf8a1520eb84200a93f3234e3747a6bcfd42b92fee"
)
F337_OUTPUT_SHA256 = {
    209: "0041fbac4fa65c00656256869eb2078757aa72f0514f6ba4e2d9c0a2e8e79bf3",
    1333: "4bd39bef4c29dccb42f16c5fc49619d7e21cc14926a8f4b1e96ad1bafa231722",
    10807: "080d11ce2ab306e065c7eb07a0d7f01b838187b15c1818f2ad8618109fd36756",
}

SEED = 33920260907
ROUTE = "route:F31"
RULE_NAMES = (
    "q_one",
    "q_half",
    "q_alpha",
    "q_beta",
    "q_gap_difference",
    "q_N_mod_L",
)
SMALL_D_LIMIT = 4096
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 256 * 1024 * 1024
RUN_PROGRESS = {}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


if sha256(F337_SOURCE) != F337_SOURCE_SHA256:
    raise RuntimeError("frozen F337 source hash changed")
sys.path.insert(0, str(F337_DIR))
import random_rank_gaps as f337  # noqa: E402

f334 = f337.f334


def peak_rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def write_json(path, value):
    target = Path(path)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(target)


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


def fraction_from_record(record):
    return Fraction(record["numerator"], record["denominator"])


def stable_json_sha256(value):
    data = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def validate_dependencies():
    expected = {
        F337_SOURCE: F337_SOURCE_SHA256,
        RETURN_MAP: RETURN_MAP_SHA256,
        DESIGN: DESIGN_SHA256,
        IDENTITY_CHECK: IDENTITY_CHECK_SHA256,
    }
    for path, expected_hash in expected.items():
        if sha256(path) != expected_hash:
            raise ArithmeticError(f"frozen dependency changed: {path}")
    for modulus, expected_hash in F337_OUTPUT_SHA256.items():
        path = F337_DIR / f"full_N{modulus}_output.json"
        if sha256(path) != expected_hash:
            raise ArithmeticError(f"frozen F337 output changed: {path}")
    if json.loads(IDENTITY_CHECK.read_text()).get("status") != "passed":
        raise ArithmeticError("independent return-map identity check is not passed")


def label_factor(factor, offline_factors):
    return [prime for prime in offline_factors if factor % prime == 0]


def checked_gcd(value, modulus, counts, category):
    divisor = f334.charged_gcd(value, modulus, counts, category)
    factor = divisor if 1 < divisor < modulus else None
    if factor is not None:
        if modulus % factor:
            raise ArithmeticError("gcd output is not a divisor")
        counts["factor_verification_divisions"] += 1
    return divisor, factor


class FloorSumCounter:
    floor_sum = f334.GaussPairing.floor_sum

    def __init__(self):
        self.counters = Counter()


def rank_formula(k, modulus_l, u, inverse_u, m):
    counts = Counter()
    counts["rank_evaluation_calls"] += 1
    counts["rank_modular_multiplications"] += 1
    phase = inverse_u * k % modulus_l
    oracle = FloorSumCounter()
    deleted = oracle.floor_sum(phase, modulus_l, u, modulus_l - m) - oracle.floor_sum(
        phase, modulus_l, u, 0
    )
    add_counts(counts, oracle.counters)
    rank = phase - deleted
    if not 0 <= rank < m:
        raise ArithmeticError("rank formula returned an invalid rank")
    return rank, counts


def exact_bounded_draw_cost(bound):
    width = (bound - 1).bit_length()
    trials = Fraction(1 << width, bound)
    return {
        "bounded_draw_calls": Fraction(1, 1),
        "random_bit_trials": trials,
        "random_range_rejections": trials - 1,
        "random_fair_bits": width * trials,
    }


def expected_count_record(deterministic, conditional_total, denominator, draw_bound):
    values = {}
    for key, value in deterministic.items():
        if not key.startswith("maximum_"):
            values[key] = Fraction(value, 1)
    for key, value in conditional_total.items():
        if not key.startswith("maximum_"):
            values[key] = values.get(key, Fraction(0, 1)) + Fraction(
                value, denominator
            )
    if draw_bound is not None:
        for key, value in exact_bounded_draw_cost(draw_bound).items():
            values[key] = values.get(key, Fraction(0, 1)) + value
    return {key: fraction_record(value) for key, value in sorted(values.items())}


def cost_per_success(expected_counts, success_probability):
    if success_probability == 0:
        return None
    return {
        key: fraction_record(fraction_from_record(value) / success_probability)
        for key, value in expected_counts.items()
        if fraction_from_record(value)
    }


def direct_gcd_control(values, modulus, offline_factors, category):
    grouped = {}
    for label, value in values:
        canonical = abs(value)
        grouped.setdefault(canonical, []).append(label)
    counts = Counter()
    rows = []
    for canonical in sorted(grouped):
        divisor, factor = checked_gcd(canonical, modulus, counts, category)
        row = {
            "argument": canonical,
            "source_labels": sorted(grouped[canonical]),
            "gcd": divisor,
            "factor": factor,
        }
        if factor is not None:
            row["offline_factor_labels"] = label_factor(factor, offline_factors)
        rows.append(row)
    return {
        "raw_arguments": len(values),
        "deduplicated_arguments": len(rows),
        "rows": rows,
        "factor_rows": [row for row in rows if row["factor"] is not None],
        "operation_counts": dict(sorted(counts.items())),
    }


def menu_control(q, d, m, modulus, offline_factors):
    if d > SMALL_D_LIMIT:
        return {
            "status": "not_enumerated_above_limit",
            "d": d,
            "limit": SMALL_D_LIMIT,
            "raw_arguments": 2 * (d + 1),
        }
    values = []
    for deleted in range(d + 1):
        values.append((f"q-h:{deleted}", q - deleted))
        values.append((f"q-h-m:{deleted}", q - deleted - m))
    output = direct_gcd_control(values, modulus, offline_factors, "menu")
    output.update({"status": "enumerated", "d": d, "limit": SMALL_D_LIMIT})
    digest = hashlib.sha256()
    for row in output["rows"]:
        digest.update(f"{row['argument']},{row['gcd']};".encode())
    output["argument_gcd_sha256"] = digest.hexdigest()
    output.pop("rows")
    return output


def source_generation_record(parameter, source_artifact, offline_factors):
    factors = parameter["generation_factors"]
    for factor in factors:
        if not (1 < factor < source_artifact["modulus"] and source_artifact["modulus"] % factor == 0):
            raise ArithmeticError("retained source generation factor is invalid")
    return {
        "attempt_id": parameter["attempt_id"],
        "policy": parameter["policy"],
        "policy_kind": parameter["policy_kind"],
        "gamma": parameter["gamma"],
        "status": parameter["status"],
        "a": parameter["a"],
        "parameters": parameter["parameters"],
        "source_seeds": parameter["source_seeds"],
        "source_ranges": parameter["source_ranges"],
        "generation_factors": factors,
        "offline_factor_labels": {
            str(factor): label_factor(factor, offline_factors) for factor in factors
        },
        "generation_operation_counts": parameter["generation_operation_counts"],
        "generation_walltime_seconds": parameter["generation_walltime_seconds"],
        "frozen_parameter_sha256": stable_json_sha256(parameter),
        "frozen_source_artifact": source_artifact,
        "cells": [],
        "anomalies": [],
    }


def analyze_rule(
    rule_name,
    q,
    duplicate_of,
    modulus,
    offline_factors,
    t,
    m,
    u,
    v,
    alpha,
    beta,
    modulus_l,
    d,
    inverse_u,
    ranks,
    rank_costs,
    generation_counts,
    setup_counts,
):
    c = q * u % modulus_l
    direct_values = [
        ("t", t),
        ("m", m),
        ("L", modulus_l),
        ("u", u),
        ("v", v),
        ("alpha", alpha),
        ("beta", beta),
        ("q", q),
        ("q-m", q - m),
        ("c", c),
        ("L-c", modulus_l - c),
    ]
    direct_control = direct_gcd_control(
        direct_values, modulus, offline_factors, "direct_control"
    )
    deterministic = Counter()
    add_counts(deterministic, generation_counts)
    add_counts(deterministic, setup_counts)
    deterministic["jump_modular_multiplications"] += 1
    deterministic["jump_endpoint_tests"] += 1

    if q == 0:
        expected_counts = expected_count_record(deterministic, Counter(), 1, None)
        return {
            "rule": rule_name,
            "q": q,
            "duplicate_of": duplicate_of,
            "proposal_status": "zero_failed_proposal",
            "c": c,
            "accepted_starts": 0,
            "rejected_starts": m,
            "acceptance_probability": fraction_record(0),
            "factor_starts": 0,
            "unconditional_factor_probability": fraction_record(0),
            "factor_histogram": {},
            "first_factor_witnesses": [],
            "rank_difference_sha256": None,
            "expected_algorithm_operation_counts": expected_counts,
            "operation_cost_per_success": None,
            "direct_control": direct_control,
            "small_d_menu": {
                "status": "not_applicable_zero_proposal",
                "d": d,
                "limit": SMALL_D_LIMIT,
            },
            "basic_direct_control_factor": bool(direct_control["factor_rows"]),
            "menu_dominates_coupled": None,
        }

    predicted_accepted = max(0, m - c) + max(0, m - (modulus_l - c))
    conditional_total = Counter()
    accepted = 0
    factor_starts = 0
    factor_histogram = Counter()
    first_witnesses = []
    digest = hashlib.sha256()
    deleted_by_phase = [int((phase * u) % modulus_l >= m) for phase in range(modulus_l)]
    doubled_prefix = [0]
    for value in deleted_by_phase + deleted_by_phase:
        doubled_prefix.append(doubled_prefix[-1] + value)

    for k in range(m):
        k_prime = (k + c) % modulus_l
        if k_prime >= m:
            continue
        accepted += 1
        phase = inverse_u * k % modulus_l
        deleted = doubled_prefix[phase + q] - doubled_prefix[phase]
        forward = q - deleted
        if not 1 <= forward < m:
            raise ArithmeticError(
                f"invalid retained displacement rule={rule_name} k={k} q={q}"
            )
        rank_difference = ranks[k_prime] - ranks[k]
        expected_difference = forward - (m if ranks[k_prime] < ranks[k] else 0)
        if rank_difference != expected_difference:
            raise ArithmeticError(
                f"rank displacement mismatch rule={rule_name} k={k} q={q}"
            )
        deleted_without_wrap = q - rank_difference
        deleted_with_wrap = q - m - rank_difference
        if not (
            0 <= deleted_without_wrap <= d or 0 <= deleted_with_wrap <= d
        ):
            raise ArithmeticError("rank difference escaped the fixed-q menu")
        add_counts(conditional_total, rank_costs[k])
        add_counts(conditional_total, rank_costs[k_prime])
        gcd_counts = Counter()
        divisor, factor = checked_gcd(
            rank_difference, modulus, gcd_counts, "coupled_difference"
        )
        add_counts(conditional_total, gcd_counts)
        digest.update(f"{k},{k_prime},{rank_difference},{divisor};".encode())
        if factor is not None:
            factor_starts += 1
            factor_histogram[factor] += 1
            if len(first_witnesses) < 8:
                first_witnesses.append(
                    {
                        "k": k,
                        "k_prime": k_prime,
                        "rank": ranks[k],
                        "rank_prime": ranks[k_prime],
                        "rank_difference": rank_difference,
                        "deleted_visits": deleted,
                        "factor": factor,
                        "offline_factor_labels": label_factor(factor, offline_factors),
                    }
                )

    if accepted != predicted_accepted:
        raise ArithmeticError(
            f"endpoint count mismatch rule={rule_name} observed={accepted} predicted={predicted_accepted}"
        )
    menu = menu_control(q, d, m, modulus, offline_factors)
    if menu["status"] == "enumerated" and factor_starts and not menu["factor_rows"]:
        raise ArithmeticError("enumerated fixed-q menu failed to dominate a coupled factor")

    probability = Fraction(factor_starts, m)
    expected_counts = expected_count_record(
        deterministic, conditional_total, m, m
    )
    return {
        "rule": rule_name,
        "q": q,
        "duplicate_of": duplicate_of,
        "proposal_status": "evaluated",
        "c": c,
        "accepted_starts": accepted,
        "rejected_starts": m - accepted,
        "predicted_accepted_starts": predicted_accepted,
        "acceptance_probability": fraction_record(Fraction(accepted, m)),
        "factor_starts": factor_starts,
        "unconditional_factor_probability": fraction_record(probability),
        "factor_histogram": {
            str(factor): count for factor, count in sorted(factor_histogram.items())
        },
        "first_factor_witnesses": first_witnesses,
        "rank_difference_sha256": digest.hexdigest(),
        "expected_algorithm_operation_counts": expected_counts,
        "operation_cost_per_success": cost_per_success(expected_counts, probability),
        "direct_control": direct_control,
        "small_d_menu": menu,
        "basic_direct_control_factor": bool(direct_control["factor_rows"]),
        "menu_dominates_coupled": (
            True if menu["status"] == "enumerated" else None
        ),
    }


def analyze_cell(parameter, source_cell, modulus, offline_factors):
    multiplier = parameter["a"]
    t = source_cell["t"]
    m = t + 1
    extrema = source_cell["extrema"]
    u = extrema["u"]
    v = extrema["v"]
    alpha = extrema["alpha"]
    beta = extrema["beta"]
    modulus_l = u + v
    d = modulus_l - m
    if extrema["m"] != m or extrema["u_plus_v"] != modulus_l:
        raise ArithmeticError("F337 extremum metadata is inconsistent")
    if not (0 <= d < min(u, v)):
        raise ArithmeticError("deleted interval has invalid size")
    if math.gcd(u, v) != 1 or alpha * v + beta * u != modulus:
        raise ArithmeticError("return-map setup identities failed")

    residues = [multiplier * k % modulus for k in range(m)]
    if len(set(residues)) != m:
        raise ArithmeticError("orbit prefix contains duplicate residues")
    sorted_points = sorted(residues)
    rank_by_residue = {value: rank for rank, value in enumerate(sorted_points)}
    offline_ranks = [rank_by_residue[value] for value in residues]

    setup_counts = Counter(source_cell["setup_operation_counts"])
    inverse_u = f334.charged_mod_inverse(
        u, modulus_l, setup_counts, "return_map_setup"
    )
    ranks = []
    rank_costs = []
    rank_digest = hashlib.sha256()
    for k in range(m):
        rank, counts = rank_formula(k, modulus_l, u, inverse_u, m)
        if rank != offline_ranks[k]:
            raise ArithmeticError(f"return-map rank mismatch k={k}")
        ranks.append(rank)
        rank_costs.append(counts)
        rank_digest.update(f"{k},{rank};".encode())

    q_values = {
        "q_one": 1 % modulus_l,
        "q_half": (modulus_l // 2) % modulus_l,
        "q_alpha": alpha % modulus_l,
        "q_beta": beta % modulus_l,
        "q_gap_difference": (beta - alpha) % modulus_l,
        "q_N_mod_L": modulus % modulus_l,
    }
    if q_values["q_gap_difference"] != modulus * inverse_u % modulus_l:
        raise ArithmeticError("gap-difference jump identity failed")
    seen = {}
    rules = []
    for rule_name in RULE_NAMES:
        q = q_values[rule_name]
        duplicate_of = seen.get(q)
        if duplicate_of is None:
            seen[q] = rule_name
        rules.append(
            analyze_rule(
                rule_name,
                q,
                duplicate_of,
                modulus,
                offline_factors,
                t,
                m,
                u,
                v,
                alpha,
                beta,
                modulus_l,
                d,
                inverse_u,
                ranks,
                rank_costs,
                parameter["generation_operation_counts"],
                setup_counts,
            )
        )

    uniform_rank_delta = fraction_from_record(
        source_cell["laws"]["uniform_rank"]["delta"]
    )
    uniform_q_factor = uniform_rank_delta * Fraction(m, modulus_l - 1)
    return {
        "t": t,
        "t_scale": source_cell["t_scale"],
        "m": m,
        "u": u,
        "v": v,
        "L": modulus_l,
        "d": d,
        "alpha": alpha,
        "beta": beta,
        "rank_map_sha256": rank_digest.hexdigest(),
        "setup_operation_counts": dict(sorted(setup_counts.items())),
        "uniform_nonzero_q_control": {
            "acceptance_probability": fraction_record(
                Fraction(m - 1, modulus_l - 1)
            ),
            "unconditional_factor_probability": fraction_record(uniform_q_factor),
            "uniform_rank_delta": fraction_record(uniform_rank_delta),
            "runtime_rank_queries": 0,
            "runtime_gcd_calls_after_rank_draw": 1,
        },
        "direct_uniform_rank_gcd_mass": source_cell["laws"]["uniform_rank"][
            "direct_count_factor_mass"
        ],
        "rules": rules,
        "anomalies": [],
    }


def run_modulus(modulus, pilot):
    path = F337_DIR / f"full_N{modulus}_output.json"
    data = json.loads(path.read_text())
    if data["status"] != "passed" or len(data["cases"]) != 1:
        raise ArithmeticError("F337 source artifact is not a passing single case")
    case = data["cases"][0]
    if case["modulus"] != modulus:
        raise ArithmeticError("F337 modulus mismatch")
    offline_factors = case["offline_factor_labels"]
    source_artifact = {
        "path": str(path),
        "sha256": F337_OUTPUT_SHA256[modulus],
        "modulus": modulus,
    }
    parameters = []
    anomalies = []
    source_parameters = case["parameters"]
    if pilot:
        source_parameters = [
            parameter
            for parameter in source_parameters
            if int(parameter["attempt_id"].split(":")[1]) < 2
        ]
    RUN_PROGRESS.update(
        {
            "modulus": modulus,
            "pilot": pilot,
            "source_parameters": len(source_parameters),
            "completed_parameters": 0,
            "completed_cells": 0,
        }
    )
    stop = False
    for source_parameter in source_parameters:
        parameter = source_generation_record(
            source_parameter, source_artifact, offline_factors
        )
        if parameter["status"] == "unit":
            for source_cell in source_parameter["cells"]:
                try:
                    cell = analyze_cell(
                        parameter, source_cell, modulus, offline_factors
                    )
                except ArithmeticError as exception:
                    anomaly = {
                        "attempt_id": parameter["attempt_id"],
                        "policy": parameter["policy"],
                        "a": parameter["a"],
                        "t": source_cell["t"],
                        "message": str(exception),
                    }
                    parameter["anomalies"].append(anomaly)
                    anomalies.append(anomaly)
                    stop = True
                    break
                parameter["cells"].append(cell)
                RUN_PROGRESS["completed_cells"] += 1
        parameters.append(parameter)
        RUN_PROGRESS["completed_parameters"] += 1
        RUN_PROGRESS["last_attempt_id"] = parameter["attempt_id"]
        if stop:
            break
        if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 256 MiB")

    return {
        "modulus": modulus,
        "actual_bits": modulus.bit_length(),
        "offline_factor_labels": offline_factors,
        "source_parameter_records": len(parameters),
        "source_generation_factor_records": sum(
            parameter["status"] == "generation_factor" for parameter in parameters
        ),
        "unit_parameter_records": sum(
            parameter["status"] == "unit" for parameter in parameters
        ),
        "diagnostic_cells": sum(len(parameter["cells"]) for parameter in parameters),
        "rule_views": sum(
            len(cell["rules"])
            for parameter in parameters
            for cell in parameter["cells"]
        ),
        "parameters": parameters,
        "anomalies": anomalies,
        "source_artifact": source_artifact,
    }


def summarize_cases(cases):
    summaries = []
    for case in cases:
        by_rule = {}
        by_policy_rule = {}
        all_cells = [
            cell for parameter in case["parameters"] for cell in parameter["cells"]
        ]
        for rule_name in RULE_NAMES:
            rows = [
                rule
                for cell in all_cells
                for rule in cell["rules"]
                if rule["rule"] == rule_name
            ]
            mean_acceptance = sum(
                fraction_from_record(row["acceptance_probability"]) for row in rows
            ) / len(rows)
            mean_factor = sum(
                fraction_from_record(row["unconditional_factor_probability"])
                for row in rows
            ) / len(rows)
            by_rule[rule_name] = {
                "cells": len(rows),
                "zero_proposals": sum(row["q"] == 0 for row in rows),
                "duplicate_rule_views": sum(row["duplicate_of"] is not None for row in rows),
                "positive_factor_cells": sum(row["factor_starts"] > 0 for row in rows),
                "positive_without_basic_direct_control": sum(
                    row["factor_starts"] > 0 and not row["basic_direct_control_factor"]
                    for row in rows
                ),
                "basic_direct_control_factor_cells": sum(
                    row["basic_direct_control_factor"] for row in rows
                ),
                "mean_unconditional_acceptance": fraction_record(mean_acceptance),
                "mean_unconditional_factor_probability": fraction_record(mean_factor),
                "enumerated_menu_gcd_calls": sum(
                    row["small_d_menu"].get("operation_counts", {}).get("gcd_calls", 0)
                    for row in rows
                ),
                "menu_factor_cells": sum(
                    bool(row["small_d_menu"].get("factor_rows", [])) for row in rows
                ),
            }
        for parameter in case["parameters"]:
            for cell in parameter["cells"]:
                for rule in cell["rules"]:
                    key = (parameter["policy"], rule["rule"])
                    record = by_policy_rule.setdefault(
                        key,
                        {
                            "cells": 0,
                            "acceptance_sum": Fraction(0, 1),
                            "factor_sum": Fraction(0, 1),
                            "positive_factor_cells": 0,
                            "positive_without_basic_direct_control": 0,
                        },
                    )
                    record["cells"] += 1
                    record["acceptance_sum"] += fraction_from_record(
                        rule["acceptance_probability"]
                    )
                    record["factor_sum"] += fraction_from_record(
                        rule["unconditional_factor_probability"]
                    )
                    record["positive_factor_cells"] += rule["factor_starts"] > 0
                    record["positive_without_basic_direct_control"] += (
                        rule["factor_starts"] > 0
                        and not rule["basic_direct_control_factor"]
                    )
        policy_rows = []
        for (policy, rule_name), record in sorted(by_policy_rule.items()):
            policy_rows.append(
                {
                    "policy": policy,
                    "rule": rule_name,
                    "cells": record["cells"],
                    "positive_factor_cells": record["positive_factor_cells"],
                    "positive_without_basic_direct_control": record[
                        "positive_without_basic_direct_control"
                    ],
                    "mean_unconditional_acceptance": fraction_record(
                        record["acceptance_sum"] / record["cells"]
                    ),
                    "mean_unconditional_factor_probability": fraction_record(
                        record["factor_sum"] / record["cells"]
                    ),
                }
            )
        uniform_q_mean = sum(
            fraction_from_record(
                cell["uniform_nonzero_q_control"]["unconditional_factor_probability"]
            )
            for cell in all_cells
        ) / len(all_cells)
        summaries.append(
            {
                "modulus": case["modulus"],
                "actual_bits": case["actual_bits"],
                "source_parameter_records": case["source_parameter_records"],
                "source_generation_factor_records": case[
                    "source_generation_factor_records"
                ],
                "unit_parameter_records": case["unit_parameter_records"],
                "diagnostic_cells": case["diagnostic_cells"],
                "rule_views": case["rule_views"],
                "uniform_nonzero_q_mean_factor_probability": fraction_record(
                    uniform_q_mean
                ),
                "rules": by_rule,
                "policy_rule_rows": policy_rows,
                "anomalies": len(case["anomalies"]),
            }
        )
    return summaries


def strongest_without_basic_control(cases, limit=24):
    rows = []
    for case in cases:
        for parameter in case["parameters"]:
            for cell in parameter["cells"]:
                for rule in cell["rules"]:
                    probability = fraction_from_record(
                        rule["unconditional_factor_probability"]
                    )
                    if probability == 0 or rule["basic_direct_control_factor"]:
                        continue
                    rows.append(
                        {
                            "modulus": case["modulus"],
                            "attempt_id": parameter["attempt_id"],
                            "policy": parameter["policy"],
                            "a": parameter["a"],
                            "source_parameters": parameter["parameters"],
                            "t": cell["t"],
                            "t_scale": cell["t_scale"],
                            "L": cell["L"],
                            "d": cell["d"],
                            "alpha": cell["alpha"],
                            "beta": cell["beta"],
                            "rule": rule["rule"],
                            "q": rule["q"],
                            "duplicate_of": rule["duplicate_of"],
                            "acceptance_probability": rule["acceptance_probability"],
                            "unconditional_factor_probability": rule[
                                "unconditional_factor_probability"
                            ],
                            "uniform_nonzero_q_factor_probability": cell[
                                "uniform_nonzero_q_control"
                            ]["unconditional_factor_probability"],
                            "direct_uniform_rank_gcd_mass": cell[
                                "direct_uniform_rank_gcd_mass"
                            ],
                            "factor_histogram": rule["factor_histogram"],
                            "menu_status": rule["small_d_menu"]["status"],
                            "menu_deduplicated_arguments": rule[
                                "small_d_menu"
                            ].get("deduplicated_arguments"),
                            "menu_factor_rows": rule["small_d_menu"].get(
                                "factor_rows", []
                            ),
                            "expected_algorithm_operation_counts": rule[
                                "expected_algorithm_operation_counts"
                            ],
                        }
                    )
    rows.sort(
        key=lambda row: (
            fraction_from_record(row["unconditional_factor_probability"]),
            -row["modulus"],
            row["attempt_id"],
            row["rule"],
        ),
        reverse=True,
    )
    return rows[:limit]


def run_aggregate():
    cases = []
    artifacts = []
    for modulus in F337_OUTPUT_SHA256:
        path = EXPERIMENT_DIR / f"search_N{modulus}_output.json"
        data = json.loads(path.read_text())
        if data["status"] != "passed" or len(data["cases"]) != 1:
            raise ArithmeticError(f"non-passing search artifact: {path}")
        cases.extend(data["cases"])
        artifacts.append(
            {
                "path": str(path),
                "sha256": sha256(path),
                "walltime_seconds": data["walltime_seconds"],
                "peak_rss_bytes": data["peak_rss_bytes"],
            }
        )
    return {
        "status": "passed",
        "experiment": "F339_coupled_rank_sources",
        "route": ROUTE,
        "mode": "aggregate",
        "scope": (
            "Exact finite evaluation of six fixed public jump rules on every "
            "retained F337 unit cell. Endpoint failures and all F337 generation "
            "records remain in the denominator; offline factors only label gcds."
        ),
        "summary": summarize_cases(cases),
        "strongest_positive_without_basic_direct_control": (
            strongest_without_basic_control(cases)
        ),
        "input_artifacts": artifacts,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("pilot", "search", "aggregate"), required=True)
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
        "experiment": "F339_coupled_rank_sources",
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
            cases = [run_modulus(209, True)]
            payload = {
                "status": "passed" if not cases[0]["anomalies"] else "anomaly",
                "experiment": "F339_coupled_rank_sources",
                "route": ROUTE,
                "mode": "pilot",
                "scope": "N=209, source indices 0 and 1 from every F337 law.",
                "cases": cases,
                "summary": summarize_cases(cases),
                "strongest_positive_without_basic_direct_control": (
                    strongest_without_basic_control(cases)
                ),
            }
        elif arguments.mode == "search":
            if arguments.modulus not in F337_OUTPUT_SHA256:
                raise ValueError("search mode requires a prescribed modulus")
            cases = [run_modulus(arguments.modulus, False)]
            payload = {
                "status": "passed" if not cases[0]["anomalies"] else "anomaly",
                "experiment": "F339_coupled_rank_sources",
                "route": ROUTE,
                "mode": "search",
                "scope": "All frozen F337 source records and unit cells for one modulus.",
                "cases": cases,
                "summary": summarize_cases(cases),
                "strongest_positive_without_basic_direct_control": (
                    strongest_without_basic_control(cases)
                ),
            }
        else:
            payload = run_aggregate()
        if payload["status"] == "anomaly":
            payload["first_anomaly"] = next(
                anomaly for case in payload["cases"] for anomaly in case["anomalies"]
            )
        signal.alarm(0)
        payload.update(
            {
                "seed": SEED,
                "source_sha256": sha256(Path(__file__)),
                "dependency_sha256": {
                    "COUPLING_SEARCH": DESIGN_SHA256,
                    "RETURN_MAP_JUMPS": RETURN_MAP_SHA256,
                    "return_map_identity_check": IDENTITY_CHECK_SHA256,
                    "F337_source": F337_SOURCE_SHA256,
                    "F337_outputs": {
                        str(key): value for key, value in F337_OUTPUT_SHA256.items()
                    },
                },
                "small_d_menu_limit": SMALL_D_LIMIT,
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
                "small_d_menu_limit",
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
