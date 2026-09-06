"""F289 exact support descent over a union of modular inverse-graph cosets.

One Python process; 60-second source alarm; estimated peak memory below 128 MB.
Prime factors construct and audit labelled semiprimes only. The public hull,
support queries, successors, and basins depend only on N and M.
"""

import json
import math
import resource
import signal
import sys
import time
import traceback
from fractions import Fraction
from pathlib import Path


ALARM_SECONDS = 60
INITIAL_EXPONENTS = (8, 10, 12)
EXTENDED_EXPONENTS = (14, 16)
MODULI = (1, 2, 4, 8, 16, 64, 256)
CONTROL_MODULI = (1, 2, 4, 8)
MOVE_MODULI = (16, 64, 256)
NORMAL_LOW = Fraction(1)
NORMAL_HIGH = Fraction(2)
OUTPUT_PATH = Path(__file__).with_name("output.json")
LOG_PATH = Path(__file__).with_name("run.log")


def alarm_handler(_signum, _frame):
    raise TimeoutError(f"F289 exceeded its {ALARM_SECONDS}-second source alarm")


def next_prime(candidate):
    candidate = max(2, candidate)
    if candidate == 2:
        return candidate
    candidate |= 1
    while True:
        limit = math.isqrt(candidate)
        divisor = 3
        while divisor <= limit and candidate % divisor:
            divisor += 2
        if divisor > limit:
            return candidate
        candidate += 2


def least_feasible_y(n, x, modulus):
    lower = (n + x - 1) // x
    if modulus == 1:
        return lower
    residue = (n * pow(x, -1, modulus)) % modulus
    return lower + (residue - lower) % modulus


def rational_pair(value):
    return [value.numerator, value.denominator]


def support_query(hull, a, b):
    """Return the selected endpoint and every endpoint of the optimal face."""
    lo = 0
    hi = len(hull) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        left = hull[mid]
        right = hull[mid + 1]
        delta = a * (right[0] - left[0]) + b * (right[1] - left[1])
        if delta < 0:
            lo = mid + 1
        else:
            hi = mid

    if lo:
        left = hull[lo - 1]
        right = hull[lo]
        assert a * (right[0] - left[0]) + b * (right[1] - left[1]) < 0

    face = [lo]
    if lo + 1 < len(hull):
        left = hull[lo]
        right = hull[lo + 1]
        delta = a * (right[0] - left[0]) + b * (right[1] - left[1])
        assert delta >= 0
        if delta == 0:
            face.append(lo + 1)

    selected = min(
        face,
        key=lambda index: (
            hull[index][0] * hull[index][1],
            hull[index][0],
            hull[index][1],
        ),
    )
    objective = a * hull[selected][0] + b * hull[selected][1]
    assert all(a * hull[index][0] + b * hull[index][1] == objective for index in face)
    return selected, tuple(face)


def analyze(n, modulus):
    """Analyze one public pair (N, M), without receiving its factor labels."""
    assert n > 0
    assert modulus > 0 and modulus & (modulus - 1) == 0
    if modulus > 1:
        assert n & 1

    root = math.isqrt(n)
    if root * root < n:
        root += 1
    x0 = root if root & 1 else root + 1
    y0 = least_feasible_y(n, x0, modulus)
    k_bound = max(x0, y0)
    assert x0 * y0 >= n and (x0 * y0 - n) % modulus == 0

    points_by_x = {}
    x_step = 1 if modulus == 1 else 2
    x_start = 1
    for x in range(x_start, k_bound + 1, x_step):
        y = least_feasible_y(n, x, modulus)
        assert x * y >= n and (x * y - n) % modulus == 0
        for point_x, point_y in ((x, y), (y, x)):
            previous = points_by_x.get(point_x)
            if previous is None or point_y < previous:
                points_by_x[point_x] = point_y

    frontier = []
    best_y = None
    for x, y in sorted(points_by_x.items()):
        if best_y is None or y < best_y:
            frontier.append((x, y))
            best_y = y

    hull = []
    for point in frontier:
        while len(hull) >= 2:
            left = hull[-2]
            middle = hull[-1]
            cross = (
                (middle[0] - left[0]) * (point[1] - left[1])
                - (middle[1] - left[1]) * (point[0] - left[0])
            )
            if cross > 0:
                break
            hull.pop()
        hull.append(point)

    assert hull
    assert all(
        hull[index][0] < hull[index + 1][0]
        and hull[index][1] > hull[index + 1][1]
        for index in range(len(hull) - 1)
    )
    assert all(
        (hull[index][0] - hull[index - 1][0])
        * (hull[index + 1][1] - hull[index - 1][1])
        - (hull[index][1] - hull[index - 1][1])
        * (hull[index + 1][0] - hull[index - 1][0])
        > 0
        for index in range(1, len(hull) - 1)
    )

    products = [x * y for x, y in hull]
    successors = []
    optimal_faces = []
    for index, (x, y) in enumerate(hull):
        successor, face = support_query(hull, y, x)
        successor_product = products[successor]
        assert successor_product <= products[index]
        assert (successor_product == products[index]) == (successor == index)
        successors.append(successor)
        optimal_faces.append(face)

    if modulus in CONTROL_MODULI:
        assert all(successor == index for index, successor in enumerate(successors))

    sinks = [-1] * len(hull)
    steps = [-1] * len(hull)
    for index, successor in enumerate(successors):
        if successor == index:
            sinks[index] = index
            steps[index] = 0

    for start in range(len(hull)):
        if sinks[start] >= 0:
            continue
        path = []
        index = start
        while sinks[index] < 0:
            path.append(index)
            successor = successors[index]
            assert products[successor] < products[index]
            index = successor
            assert len(path) <= len(hull)
        sink = sinks[index]
        distance = steps[index]
        for index in reversed(path):
            distance += 1
            sinks[index] = sink
            steps[index] = distance

    cone_lengths = []
    for index, (x, y) in enumerate(hull):
        lower = (
            Fraction(y - hull[index + 1][1], hull[index + 1][0] - x)
            if index + 1 < len(hull)
            else Fraction(0)
        )
        upper = (
            Fraction(hull[index - 1][1] - y, x - hull[index - 1][0])
            if index
            else None
        )
        clipped_low = max(lower, NORMAL_LOW)
        clipped_high = min(upper, NORMAL_HIGH) if upper is not None else NORMAL_HIGH
        cone_lengths.append(max(Fraction(0), clipped_high - clipped_low))
    assert sum(cone_lengths, Fraction(0)) == NORMAL_HIGH - NORMAL_LOW

    fixed_indices = [
        index for index, successor in enumerate(successors) if successor == index
    ]
    proper_factor_sinks = [
        index
        for index in fixed_indices
        if products[index] == n and hull[index][0] > 1 and hull[index][1] > 1
    ]
    trivial_factor_sinks = [
        index
        for index in fixed_indices
        if products[index] == n
        and (hull[index][0] == 1 or hull[index][1] == 1)
    ]
    false_sinks = [index for index in fixed_indices if products[index] > n]
    assert (
        len(proper_factor_sinks) + len(trivial_factor_sinks) + len(false_sinks)
        == len(fixed_indices)
    )

    basin_by_sink = {index: Fraction(0) for index in fixed_indices}
    for index, width in enumerate(cone_lengths):
        basin_by_sink[sinks[index]] += width

    proper_mass = sum(
        (basin_by_sink[index] for index in proper_factor_sinks), Fraction(0)
    )
    trivial_mass = sum(
        (basin_by_sink[index] for index in trivial_factor_sinks), Fraction(0)
    )
    false_mass = sum(
        (basin_by_sink[index] for index in false_sinks), Fraction(0)
    )
    assert proper_mass + trivial_mass + false_mass == NORMAL_HIGH - NORMAL_LOW

    move_indices = [
        index for index, successor in enumerate(successors) if successor != index
    ]
    direct_proper_mass = sum(
        (cone_lengths[index] for index in proper_factor_sinks), Fraction(0)
    )
    direct_trivial_mass = sum(
        (cone_lengths[index] for index in trivial_factor_sinks), Fraction(0)
    )
    direct_false_fixed_mass = sum(
        (cone_lengths[index] for index in false_sinks), Fraction(0)
    )
    direct_moving_mass = sum(
        (cone_lengths[index] for index in move_indices), Fraction(0)
    )
    assert (
        direct_proper_mass
        + direct_trivial_mass
        + direct_false_fixed_mass
        + direct_moving_mass
        == NORMAL_HIGH - NORMAL_LOW
    )
    assert proper_mass >= direct_proper_mass
    weighted_move_indices = [
        index
        for index in move_indices
        if hull[index][0] <= hull[index][1] <= 2 * hull[index][0]
    ]
    representative = None
    if move_indices:
        representative_pool = weighted_move_indices or move_indices
        source_index = max(
            representative_pool,
            key=lambda index: (
                products[index] - products[successors[index]],
                -products[index],
                -index,
            ),
        )
        target_index = successors[source_index]
        source = hull[source_index]
        target = hull[target_index]
        a, b = source[1], source[0]
        reflection = (2 * source[0] - target[0], 2 * source[1] - target[1])
        assert reflection[0] > 0 and reflection[1] > 0
        assert reflection[0] * reflection[1] >= n
        assert (reflection[0] * reflection[1] - n) % modulus != 0
        representative = {
            "source_index": source_index,
            "source": list(source),
            "source_product": products[source_index],
            "normal": [a, b],
            "self_objective": 2 * products[source_index],
            "target_index": target_index,
            "target": list(target),
            "target_product": products[target_index],
            "target_objective": a * target[0] + b * target[1],
            "optimal_face": [list(hull[index]) for index in optimal_faces[source_index]],
            "reflection": list(reflection),
            "reflection_product": reflection[0] * reflection[1],
            "reflection_residue": reflection[0] * reflection[1] % modulus,
            "required_residue": n % modulus,
        }

    smallest_false_defect = (
        min(products[index] - n for index in false_sinks) if false_sinks else None
    )
    return {
        "N": n,
        "N_bits": n.bit_length(),
        "M": modulus,
        "P0": [x0, y0],
        "K": k_bound,
        "eligible_x": (k_bound + (0 if modulus == 1 else 1)) // x_step,
        "candidate_columns": len(points_by_x),
        "pareto_points": len(frontier),
        "hull_vertices": len(hull),
        "moves": len(move_indices),
        "moves_with_self_normal_in_interval": len(weighted_move_indices),
        "support_ties": sum(len(face) == 2 for face in optimal_faces),
        "fixed_points": len(fixed_indices),
        "maximum_steps": max(steps),
        "proper_factor_sinks": len(proper_factor_sinks),
        "trivial_factor_sinks": len(trivial_factor_sinks),
        "false_sinks": len(false_sinks),
        "smallest_false_sink_defect": smallest_false_defect,
        "factor_sink_points": [
            list(hull[index])
            for index in proper_factor_sinks + trivial_factor_sinks
        ],
        "direct_cone_lengths": {
            "proper_factor": rational_pair(direct_proper_mass),
            "trivial_factor": rational_pair(direct_trivial_mass),
            "false_fixed": rational_pair(direct_false_fixed_mass),
            "moving": rational_pair(direct_moving_mass),
        },
        "basin_lengths": {
            "proper_factor": rational_pair(proper_mass),
            "trivial_factor": rational_pair(trivial_mass),
            "false_sink": rational_pair(false_mass),
        },
        "proper_factor_basin_gain": rational_pair(proper_mass - direct_proper_mass),
        "all_vertices_self_fixed": not move_indices,
        "representative_move": representative,
    }


def labelled_semiprime(exponent):
    """Construct a deterministic, visibly unbalanced semiprime near B^2."""
    scale = 1 << exponent
    p = next_prime(9 * scale // 8 + 2 * exponent + 1)
    q = next_prime(7 * scale // 4 + 3 * exponent + 1)
    assert p != q and p & 1 and q & 1
    return scale, p, q


def main():
    started = time.monotonic()
    logs = [
        "F289 exact modular-support-union pilot",
        f"source_alarm_seconds={ALARM_SECONDS}",
        "processes=1",
        "estimated_peak_memory_mb<128",
        "estimated_runtime_seconds<60",
        "factor_labels_used_for=case_construction_and_post_hoc_audit_only",
        "normal_slope_interval=[1,2]",
    ]
    cases = []
    representative_by_modulus = {}

    def run_scale(exponent, phase):
        scale_started = time.monotonic()
        scale, p_label, q_label = labelled_semiprime(exponent)
        n = p_label * q_label
        for modulus in MODULI:
            result = analyze(n, modulus)
            result["label"] = f"B=2^{exponent}"
            result["B"] = scale
            result["p_label"] = p_label
            result["q_label"] = q_label

            expected_factor_points = {
                (1, n),
                (p_label, q_label),
                (q_label, p_label),
                (n, 1),
            }
            actual_factor_points = {
                tuple(point) for point in result["factor_sink_points"]
            }
            assert actual_factor_points == expected_factor_points
            assert result["proper_factor_sinks"] == 2
            assert result["trivial_factor_sinks"] == 2
            result["factor_audit"] = "passed"

            if result["representative_move"] is not None:
                representative_by_modulus.setdefault(
                    modulus,
                    {
                        "label": result["label"],
                        "B": scale,
                        "N": n,
                        "p_label": p_label,
                        "q_label": q_label,
                        "M": modulus,
                        "P0": result["P0"],
                        "K": result["K"],
                        **result["representative_move"],
                    },
                )
            result.pop("representative_move")
            cases.append(result)
        logs.append(
            f"phase={phase} B=2^{exponent} "
            f"elapsed_seconds={time.monotonic() - scale_started:.6f}"
        )

    run_scale(INITIAL_EXPONENTS[0], "small_pilot")
    pilot_elapsed = time.monotonic() - started
    logs.append(f"small_pilot_elapsed_seconds={pilot_elapsed:.6f}")
    assert pilot_elapsed < 10

    for exponent in INITIAL_EXPONENTS[1:]:
        run_scale(exponent, "initial")
    initial_elapsed = time.monotonic() - started
    logs.append(f"initial_elapsed_seconds={initial_elapsed:.6f}")

    extended = []
    if initial_elapsed < 20:
        for exponent in EXTENDED_EXPONENTS:
            run_scale(exponent, "extended")
            extended.append(exponent)

    for modulus in MOVE_MODULI:
        assert modulus in representative_by_modulus

    aggregates = []
    for modulus in MODULI:
        selected = [case for case in cases if case["M"] == modulus]
        proper_mass = sum(
            (
                Fraction(*case["basin_lengths"]["proper_factor"])
                for case in selected
            ),
            Fraction(0),
        )
        trivial_mass = sum(
            (
                Fraction(*case["basin_lengths"]["trivial_factor"])
                for case in selected
            ),
            Fraction(0),
        )
        false_mass = sum(
            (
                Fraction(*case["basin_lengths"]["false_sink"])
                for case in selected
            ),
            Fraction(0),
        )
        direct_proper_mass = sum(
            (
                Fraction(*case["direct_cone_lengths"]["proper_factor"])
                for case in selected
            ),
            Fraction(0),
        )
        case_count = len(selected)
        aggregate = {
            "M": modulus,
            "cases": case_count,
            "hull_vertices": sum(case["hull_vertices"] for case in selected),
            "moves": sum(case["moves"] for case in selected),
            "moves_with_self_normal_in_interval": sum(
                case["moves_with_self_normal_in_interval"] for case in selected
            ),
            "move_cases": sum(case["moves"] > 0 for case in selected),
            "fixed_points": sum(case["fixed_points"] for case in selected),
            "proper_factor_sinks": sum(
                case["proper_factor_sinks"] for case in selected
            ),
            "trivial_factor_sinks": sum(
                case["trivial_factor_sinks"] for case in selected
            ),
            "false_sinks": sum(case["false_sinks"] for case in selected),
            "maximum_steps": max(case["maximum_steps"] for case in selected),
            "mean_basin_lengths": {
                "proper_factor": rational_pair(proper_mass / case_count),
                "trivial_factor": rational_pair(trivial_mass / case_count),
                "false_sink": rational_pair(false_mass / case_count),
            },
            "mean_direct_proper_factor_length": rational_pair(
                direct_proper_mass / case_count
            ),
            "mean_proper_factor_basin_gain": rational_pair(
                (proper_mass - direct_proper_mass) / case_count
            ),
            "all_vertices_self_fixed": all(
                case["all_vertices_self_fixed"] for case in selected
            ),
        }
        if modulus in CONTROL_MODULI:
            assert aggregate["all_vertices_self_fixed"]
            assert aggregate["moves"] == 0
        else:
            assert aggregate["moves"] > 0
        aggregates.append(aggregate)

    elapsed = time.monotonic() - started
    max_rss_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    max_rss_bytes = max_rss_raw if sys.platform == "darwin" else max_rss_raw * 1024
    payload = {
        "experiment": "F289_modular_support_union",
        "status": "exact_finite_pilot",
        "decision_inputs": ["N", "M"],
        "factor_label_scope": "case construction and post-hoc audit only",
        "support": "positive integer pairs with xy>=N and xy congruent to N modulo M",
        "normal_slope_interval": [1, 2],
        "tie_policy": "retain both optimal face endpoints; select smaller product",
        "arithmetic": "exact integers and fractions",
        "resource_plan": {
            "processes": 1,
            "source_alarm_seconds": ALARM_SECONDS,
            "estimated_peak_memory_mb": "<128",
            "initial_exponents": list(INITIAL_EXPONENTS),
            "conditional_extended_exponents": list(EXTENDED_EXPONENTS),
            "moduli": list(MODULI),
        },
        "runtime": {
            "elapsed_seconds": elapsed,
            "max_rss_bytes": max_rss_bytes,
            "extended_exponents_completed": extended,
        },
        "aggregates_by_modulus": aggregates,
        "representative_move_certificates": [
            representative_by_modulus[modulus] for modulus in MOVE_MODULI
        ],
        "cases": cases,
    }
    logs.append(f"total_elapsed_seconds={elapsed:.6f}")
    logs.append(f"max_rss_bytes={max_rss_bytes}")
    logs.append(f"cases={len(cases)}")
    logs.append("status=success")
    return payload, logs


if __name__ == "__main__":
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(ALARM_SECONDS)
    try:
        output, run_logs = main()
        OUTPUT_PATH.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
        LOG_PATH.write_text("\n".join(run_logs) + "\n", encoding="utf-8")
        signal.alarm(0)
        print(
            json.dumps(
                {
                    "status": "success",
                    "cases": len(output["cases"]),
                    "elapsed_seconds": output["runtime"]["elapsed_seconds"],
                    "max_rss_bytes": output["runtime"]["max_rss_bytes"],
                    "aggregate_moves": {
                        row["M"]: row["moves"]
                        for row in output["aggregates_by_modulus"]
                    },
                },
                indent=2,
            )
        )
    except BaseException:
        signal.alarm(0)
        LOG_PATH.write_text(traceback.format_exc(), encoding="utf-8")
        raise
