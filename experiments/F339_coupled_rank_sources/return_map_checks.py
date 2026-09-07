#!/usr/bin/env python3
"""Finite checks for the F339 return-map and engineered-source identities."""

import argparse
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
EXPERIMENT_DIR = ROOT / "experiments" / "F339_coupled_rank_sources"
DESIGN = EXPERIMENT_DIR / "RETURN_MAP_JUMPS.md"
DESIGN_SHA256 = "cbe3426744bb0d263a4439afdcd0847d7f1fe6992a18217914b2f857c970b8a8"
ROUTE = "route:F31"
INTERNAL_TIMEOUT_SECONDS = 8
HARD_TIMEOUT_SECONDS = 10
MEMORY_LIMIT_BYTES = 64 * 1024 * 1024
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


def require(condition, kind, **context):
    if condition:
        return
    anomaly = {"kind": kind, **context}
    if "first_anomaly" not in RUN_PROGRESS:
        RUN_PROGRESS["first_anomaly"] = anomaly
    raise ArithmeticError(json.dumps(anomaly, sort_keys=True))


def floor_sum(count, modulus, slope, offset, counters):
    counters["floor_sum_calls"] += 1
    answer = 0
    while True:
        counters["floor_sum_euclidean_iterations"] += 1
        if slope >= modulus:
            answer += (count - 1) * count * (slope // modulus) // 2
            slope %= modulus
        if offset >= modulus:
            answer += count * (offset // modulus)
            offset %= modulus
        top = slope * count + offset
        if top < modulus:
            return answer
        count = top // modulus
        offset = top % modulus
        modulus, slope = slope, modulus


def direct_orbit(modulus, multiplier, t):
    points = sorted(
        (multiplier * index % modulus, index)
        for index in range(t + 1)
    )
    require(
        len({residue for residue, _ in points}) == t + 1,
        "orbit_residues_not_distinct",
        N=modulus,
        a=multiplier,
        t=t,
    )
    order = [index for _, index in points]
    rank = {index: position for position, index in enumerate(order)}
    successor = {
        order[position]: order[(position + 1) % len(order)]
        for position in range(len(order))
    }
    return points, order, rank, successor


def check_generic_case(modulus, multiplier, t, totals):
    points, _, direct_rank, direct_successor = direct_orbit(
        modulus, multiplier, t
    )
    m = t + 1
    alpha, u = points[1]
    maximum_residue, v = points[-1]
    beta = modulus - maximum_residue
    L = u + v
    d = L - m

    require(
        max(u, v) < m <= L,
        "extremum_index_bounds",
        N=modulus,
        a=multiplier,
        t=t,
        u=u,
        v=v,
        m=m,
        L=L,
    )
    require(
        d < min(u, v),
        "deleted_interval_too_long",
        N=modulus,
        a=multiplier,
        t=t,
        d=d,
        u=u,
        v=v,
    )
    require(
        math.gcd(u, v) == 1,
        "return_indices_not_coprime",
        N=modulus,
        a=multiplier,
        t=t,
        u=u,
        v=v,
    )
    require(
        alpha * v + beta * u == modulus,
        "positive_gap_equation",
        N=modulus,
        a=multiplier,
        t=t,
        alpha=alpha,
        beta=beta,
        u=u,
        v=v,
    )
    require(
        math.gcd(u, L) == 1,
        "rotation_step_not_unit",
        N=modulus,
        a=multiplier,
        t=t,
        u=u,
        L=L,
    )

    residues = {index: residue for residue, index in points}
    for index in range(m):
        cursor = (index + u) % L
        return_steps = 1
        deleted_landings = 0
        while cursor >= m:
            deleted_landings += 1
            cursor = (cursor + u) % L
            return_steps += 1
        require(
            deleted_landings <= 1 and return_steps <= 2,
            "multiple_deleted_landings",
            N=modulus,
            a=multiplier,
            t=t,
            index=index,
        )
        require(
            cursor == direct_successor[index],
            "first_return_not_successor",
            N=modulus,
            a=multiplier,
            t=t,
            index=index,
            expected=direct_successor[index],
            observed=cursor,
        )
        exact_change = cursor - index
        if exact_change == u:
            successor_kind = "plus_u"
            expected_gap = alpha
        elif exact_change == -v:
            successor_kind = "minus_v"
            expected_gap = beta
        elif exact_change == u - v:
            successor_kind = "u_minus_v"
            expected_gap = alpha + beta
        else:
            require(
                False,
                "unknown_successor_change",
                N=modulus,
                a=multiplier,
                t=t,
                index=index,
                successor=cursor,
                change=exact_change,
            )
        actual_gap = (residues[cursor] - residues[index]) % modulus
        require(
            actual_gap == expected_gap,
            "successor_gap_mismatch",
            N=modulus,
            a=multiplier,
            t=t,
            index=index,
            successor_kind=successor_kind,
            actual_gap=actual_gap,
            expected_gap=expected_gap,
        )
        totals["successor_" + successor_kind] += 1
        totals["successor_checks"] += 1
        totals["first_return_steps"] += return_steps

    inverse_u = pow(u, -1, L)
    deleted_prefix = [0]
    for step in range(L):
        deleted_prefix.append(
            deleted_prefix[-1] + int((u * step) % L >= m)
        )
    require(
        deleted_prefix[-1] == d,
        "deleted_prefix_total",
        N=modulus,
        a=multiplier,
        t=t,
        observed=deleted_prefix[-1],
        expected=d,
    )

    for index in range(m):
        rotation_time = inverse_u * index % L
        direct_deleted = deleted_prefix[rotation_time]
        floor_deleted = floor_sum(
            rotation_time, L, u, L - m, totals
        ) - floor_sum(rotation_time, L, u, 0, totals)
        require(
            floor_deleted == direct_deleted,
            "rank_deleted_floor_sum",
            N=modulus,
            a=multiplier,
            t=t,
            index=index,
            rotation_time=rotation_time,
            direct=direct_deleted,
            floor_sum=floor_deleted,
        )
        formula_rank = rotation_time - direct_deleted
        require(
            formula_rank == direct_rank[index],
            "rank_formula",
            N=modulus,
            a=multiplier,
            t=t,
            index=index,
            formula=formula_rank,
            direct=direct_rank[index],
        )
        totals["rank_checks"] += 1

    rank_pair_counts = Counter()
    accepted_total = 0
    rejected_total = 0
    endpoint_formula_total = 0
    for q in range(1, L):
        c = q * u % L
        accepted = [
            index
            for index in range(m)
            if (index + c) % L < m
        ]
        expected_K = max(0, m - c) + max(0, m - (L - c))
        require(
            len(accepted) == expected_K,
            "endpoint_count_K",
            N=modulus,
            a=multiplier,
            t=t,
            q=q,
            c=c,
            direct=len(accepted),
            formula=expected_K,
        )
        endpoint_formula_total += expected_K
        accepted_total += len(accepted)
        rejected_total += m - len(accepted)
        totals["q_values_checked"] += 1
        for index in accepted:
            endpoint = (index + c) % L
            require(
                endpoint != index,
                "coupled_endpoints_equal",
                N=modulus,
                a=multiplier,
                t=t,
                q=q,
                index=index,
            )
            direct_deleted = sum(
                (index + step * u) % L >= m
                for step in range(q)
            )
            floor_deleted = floor_sum(
                q, L, u, index + L - m, totals
            ) - floor_sum(q, L, u, index, totals)
            require(
                floor_deleted == direct_deleted,
                "arc_deleted_floor_sum",
                N=modulus,
                a=multiplier,
                t=t,
                q=q,
                index=index,
                direct=direct_deleted,
                floor_sum=floor_deleted,
            )
            require(
                0 <= direct_deleted <= d,
                "deleted_visit_bounds",
                N=modulus,
                a=multiplier,
                t=t,
                q=q,
                index=index,
                h=direct_deleted,
                d=d,
            )
            displacement = q - direct_deleted
            require(
                1 <= displacement < m,
                "retained_displacement_bounds",
                N=modulus,
                a=multiplier,
                t=t,
                q=q,
                index=index,
                D=displacement,
            )
            epsilon = int(direct_rank[endpoint] < direct_rank[index])
            rank_difference = direct_rank[endpoint] - direct_rank[index]
            require(
                rank_difference == displacement - epsilon * m,
                "rank_difference_formula",
                N=modulus,
                a=multiplier,
                t=t,
                q=q,
                index=index,
                endpoint=endpoint,
                difference=rank_difference,
                formula=displacement - epsilon * m,
            )
            menu = {
                value
                for deleted in range(d + 1)
                for value in (q - deleted, q - deleted - m)
            }
            require(
                rank_difference in menu,
                "menu_containment",
                N=modulus,
                a=multiplier,
                t=t,
                q=q,
                index=index,
                difference=rank_difference,
            )
            rank_pair_counts[
                (direct_rank[index], direct_rank[endpoint])
            ] += 1
            totals["accepted_pairs_checked"] += 1
            totals["direct_deleted_terms"] += q
            totals["menu_membership_checks"] += 1

    require(
        accepted_total == endpoint_formula_total == m * (m - 1),
        "uniform_q_acceptance_total",
        N=modulus,
        a=multiplier,
        t=t,
        accepted=accepted_total,
        expected=m * (m - 1),
    )
    require(
        rejected_total == m * d,
        "uniform_q_rejection_total",
        N=modulus,
        a=multiplier,
        t=t,
        rejected=rejected_total,
        expected=m * d,
    )
    expected_pairs = {
        (left, right)
        for left in range(m)
        for right in range(m)
        if left != right
    }
    require(
        set(rank_pair_counts) == expected_pairs
        and set(rank_pair_counts.values()) == {1},
        "uniform_distinct_rank_law",
        N=modulus,
        a=multiplier,
        t=t,
        observed_pairs=len(rank_pair_counts),
        expected_pairs=len(expected_pairs),
    )
    totals["uniform_rank_law_checks"] += 1
    totals["accepted_pairs_formula_total"] += accepted_total
    totals["rejected_pairs_formula_total"] += rejected_total
    totals["generic_cases"] += 1
    totals["maximum_L"] = max(totals["maximum_L"], L)
    totals["maximum_d"] = max(totals["maximum_d"], d)


def check_generic(limit):
    totals = Counter()
    by_modulus = {}
    for modulus in range(3, limit + 1, 2):
        before_cases = totals["generic_cases"]
        before_pairs = totals["accepted_pairs_checked"]
        units = 0
        for multiplier in range(1, modulus):
            if math.gcd(multiplier, modulus) != 1:
                continue
            units += 1
            for t in range(1, modulus):
                RUN_PROGRESS.update(
                    {
                        "phase": "generic",
                        "N": modulus,
                        "a": multiplier,
                        "t": t,
                    }
                )
                check_generic_case(modulus, multiplier, t, totals)
        by_modulus[str(modulus)] = {
            "units": units,
            "cases": totals["generic_cases"] - before_cases,
            "accepted_pairs": totals["accepted_pairs_checked"] - before_pairs,
        }
        totals["moduli"] += 1
        totals["unit_parameters"] += units
        if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
            raise MemoryError("generic check exceeded 64 MiB")
    return {
        "limit": limit,
        "scope": "Every odd N in range, every unit a, and every 1<=t<N.",
        "totals": dict(sorted(totals.items())),
        "by_modulus": by_modulus,
        "first_anomaly": RUN_PROGRESS.get("first_anomaly"),
    }


def engineered_rank(index, M):
    if index == 0:
        return 0
    if index == M + 1:
        return M + 1
    return M + 1 - index


def check_engineered(limit):
    totals = Counter()
    first_exit_examples = []
    second_exit_examples = []
    accepted_examples = []
    by_modulus = {}
    for modulus in range(9, limit + 1, 2):
        RUN_PROGRESS.update({"phase": "engineered", "N": modulus})
        M = math.isqrt(modulus)
        divisor_M = math.gcd(M, modulus)
        totals["screen_M_gcd_calls"] += 1
        if 1 < divisor_M < modulus:
            totals["first_generation_gcd_exits"] += 1
            if len(first_exit_examples) < 8:
                first_exit_examples.append(
                    {"N": modulus, "M": M, "factor": divisor_M}
                )
            by_modulus[str(modulus)] = {
                "status": "factor_at_M",
                "factor": divisor_M,
            }
            continue
        require(
            divisor_M == 1,
            "engineered_M_gcd_not_unit_or_proper",
            N=modulus,
            M=M,
            gcd=divisor_M,
        )

        alpha = modulus % M
        beta = modulus // M - alpha
        u = M
        v = M + 1
        m = M + 2
        L = 2 * M + 1
        d = M - 1
        multiplier = modulus - alpha - beta
        require(
            1 <= alpha < M and beta >= 1,
            "engineered_gap_positivity",
            N=modulus,
            M=M,
            alpha=alpha,
            beta=beta,
        )
        require(
            alpha * v + beta * u == modulus,
            "engineered_gap_equation",
            N=modulus,
            alpha=alpha,
            beta=beta,
            u=u,
            v=v,
        )
        require(
            math.gcd(u, v) == 1 and L == u + v and d == L - m,
            "engineered_return_parameters",
            N=modulus,
            u=u,
            v=v,
            L=L,
            m=m,
            d=d,
        )
        divisor_a = math.gcd(multiplier, modulus)
        totals["screen_a_gcd_calls"] += 1
        if 1 < divisor_a < modulus:
            totals["second_generation_gcd_exits"] += 1
            if len(second_exit_examples) < 8:
                second_exit_examples.append(
                    {
                        "N": modulus,
                        "M": M,
                        "a": multiplier,
                        "factor": divisor_a,
                    }
                )
            by_modulus[str(modulus)] = {
                "status": "factor_at_a",
                "factor": divisor_a,
            }
            continue
        require(
            divisor_a == 1,
            "engineered_a_gcd_not_unit_or_proper",
            N=modulus,
            a=multiplier,
            gcd=divisor_a,
        )
        require(
            multiplier * M % modulus == alpha
            and multiplier * (M + 1) % modulus == modulus - beta,
            "engineered_residue_increments",
            N=modulus,
            M=M,
            a=multiplier,
            alpha=alpha,
            beta=beta,
        )

        t = M + 1
        points, order, direct_rank, _ = direct_orbit(
            modulus, multiplier, t
        )
        require(
            points[1] == (alpha, M)
            and points[-1] == (modulus - beta, M + 1),
            "engineered_extrema",
            N=modulus,
            a=multiplier,
            observed_min=points[1],
            observed_max=points[-1],
        )
        expected_order = [0, M, *range(M - 1, 0, -1), M + 1]
        require(
            order == expected_order,
            "engineered_sorted_order",
            N=modulus,
            observed=order,
            expected=expected_order,
        )
        for index in range(m):
            require(
                direct_rank[index] == engineered_rank(index, M),
                "engineered_rank_formula",
                N=modulus,
                index=index,
                observed=direct_rank[index],
                expected=engineered_rank(index, M),
            )
            totals["engineered_rank_checks"] += 1

        accepted_pairs = 0
        rejected_pairs = 0
        maximum_control_size = 0
        for q in range(1, L):
            c = q * M % L
            require(
                c != 0,
                "engineered_zero_translation",
                N=modulus,
                q=q,
                c=c,
            )
            exception_starts = set()
            for exceptional in (0, M + 1):
                for index in (exceptional, (exceptional - c) % L):
                    endpoint = (index + c) % L
                    if index < m and endpoint < m:
                        exception_starts.add(index)
            require(
                len(exception_starts) <= 4,
                "too_many_engineered_exception_pairs",
                N=modulus,
                q=q,
                count=len(exception_starts),
            )
            control = {-c, L - c}
            for index in exception_starts:
                endpoint = (index + c) % L
                control.add(
                    engineered_rank(endpoint, M)
                    - engineered_rank(index, M)
                )
            require(
                len(control) <= 6,
                "engineered_control_too_large",
                N=modulus,
                q=q,
                size=len(control),
            )
            maximum_control_size = max(maximum_control_size, len(control))
            control_factors = {
                value: math.gcd(value, modulus)
                for value in control
            }
            totals["engineered_control_gcd_calls"] += len(control)
            for index in range(m):
                endpoint = (index + c) % L
                if endpoint >= m:
                    rejected_pairs += 1
                    continue
                accepted_pairs += 1
                difference = direct_rank[endpoint] - direct_rank[index]
                require(
                    difference in control,
                    "engineered_six_value_containment",
                    N=modulus,
                    q=q,
                    index=index,
                    endpoint=endpoint,
                    difference=difference,
                    control=sorted(control),
                )
                if index not in exception_starts:
                    require(
                        difference in (-c, L - c),
                        "engineered_affine_nonexception",
                        N=modulus,
                        q=q,
                        index=index,
                        endpoint=endpoint,
                        difference=difference,
                        c=c,
                    )
                direct_factor = math.gcd(difference, modulus)
                require(
                    control_factors[difference] == direct_factor,
                    "engineered_control_gcd_mismatch",
                    N=modulus,
                    q=q,
                    index=index,
                    difference=difference,
                )
                totals["engineered_accepted_pair_checks"] += 1
                totals["engineered_direct_gcd_checks"] += 1

        require(
            accepted_pairs == m * (m - 1),
            "engineered_uniform_acceptance_total",
            N=modulus,
            accepted=accepted_pairs,
            expected=m * (m - 1),
        )
        require(
            rejected_pairs == m * d,
            "engineered_uniform_rejection_total",
            N=modulus,
            rejected=rejected_pairs,
            expected=m * d,
        )
        totals["accepted_unit_sources"] += 1
        totals["engineered_q_values_checked"] += L - 1
        totals["maximum_six_value_control_size"] = max(
            totals["maximum_six_value_control_size"],
            maximum_control_size,
        )
        if len(accepted_examples) < 8:
            accepted_examples.append(
                {
                    "N": modulus,
                    "M": M,
                    "a": multiplier,
                    "alpha": alpha,
                    "beta": beta,
                    "L": L,
                    "d": d,
                    "maximum_control_size": maximum_control_size,
                }
            )
        by_modulus[str(modulus)] = {
            "status": "accepted_unit_source",
            "M": M,
            "a": multiplier,
            "alpha": alpha,
            "beta": beta,
            "accepted_pairs": accepted_pairs,
            "maximum_control_size": maximum_control_size,
        }
        if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
            raise MemoryError("engineered check exceeded 64 MiB")

    require(
        totals["first_generation_gcd_exits"] > 0,
        "missing_first_generation_gcd_exit",
        limit=limit,
    )
    require(
        totals["second_generation_gcd_exits"] > 0,
        "missing_second_generation_gcd_exit",
        limit=limit,
    )
    require(
        totals["accepted_unit_sources"] > 0,
        "missing_engineered_unit_source",
        limit=limit,
    )
    totals["odd_moduli"] = (limit - 7) // 2
    return {
        "limit": limit,
        "scope": (
            "Every odd 9<=N<=limit, with both ordered generation gcd screens; "
            "every q and accepted k on each unit source."
        ),
        "totals": dict(sorted(totals.items())),
        "first_generation_exit_examples": first_exit_examples,
        "second_generation_exit_examples": second_exit_examples,
        "accepted_source_examples": accepted_examples,
        "by_modulus": by_modulus,
        "first_anomaly": RUN_PROGRESS.get("first_anomaly"),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("pilot", "full"), required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--status", required=True)
    arguments = parser.parse_args()
    if sha256(DESIGN) != DESIGN_SHA256:
        raise ArithmeticError("frozen RETURN_MAP_JUMPS design hash changed")

    generic_limit = 11 if arguments.mode == "pilot" else 31
    engineered_limit = 51 if arguments.mode == "pilot" else 511
    started = time.perf_counter()

    def timeout_handler(_signal_number, _frame):
        raise TimeoutError("internal 8-second alarm fired")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(INTERNAL_TIMEOUT_SECONDS)
    running = {
        "status": "running",
        "experiment": "F339_coupled_rank_sources",
        "route": ROUTE,
        "mode": arguments.mode,
        "source_sha256": sha256(Path(__file__)),
        "design_sha256": DESIGN_SHA256,
        "generic_limit": generic_limit,
        "engineered_limit": engineered_limit,
    }
    write_json(arguments.status, running)
    try:
        generic = check_generic(generic_limit)
        engineered = check_engineered(engineered_limit)
        signal.alarm(0)
        payload = {
            **running,
            "status": "passed",
            "generic": generic,
            "engineered": engineered,
            "independent_oracle": (
                "Sorted direct residues, direct successor maps, direct arc "
                "counts, and incremental deleted prefixes. Euclidean floor "
                "sums are checked against those independently built values."
            ),
            "first_anomaly": RUN_PROGRESS.get("first_anomaly"),
            "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
            "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
            "memory_limit_bytes": MEMORY_LIMIT_BYTES,
            "walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        if payload["peak_rss_bytes"] > MEMORY_LIMIT_BYTES:
            raise MemoryError("check exceeded 64 MiB")
        write_json(arguments.output, payload)
        status = {
            key: payload[key]
            for key in (
                "status",
                "experiment",
                "route",
                "mode",
                "source_sha256",
                "design_sha256",
                "generic_limit",
                "engineered_limit",
                "internal_timeout_seconds",
                "hard_timeout_seconds",
                "memory_limit_bytes",
                "walltime_seconds",
                "peak_rss_bytes",
                "first_anomaly",
            )
        }
        status["output"] = arguments.output
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
