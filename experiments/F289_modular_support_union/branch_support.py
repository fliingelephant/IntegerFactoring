"""F289 exact branch-and-bound support over the modular union.

One Python process; 30-second source alarm; estimated peak memory below 128 MB.
The branch search runs before the full-enumeration baseline. Prime factors
construct and audit labelled semiprimes only.
"""

import heapq
import json
import math
import resource
import signal
import sys
import time
import traceback
from fractions import Fraction
from pathlib import Path

from support_union import labelled_semiprime, least_feasible_y


ALARM_SECONDS = 30
INITIAL_EXPONENTS = (8, 10, 12)
EXTENDED_EXPONENTS = (14, 16)
NORMALS = ((1, 1), (9, 8), (5, 4), (4, 3), (3, 2), (7, 4), (2, 1))
MIN_K = 4
OUTPUT_PATH = Path(__file__).with_name("branch_output.json")
LOG_PATH = Path(__file__).with_name("branch_run.log")


def alarm_handler(_signum, _frame):
    raise TimeoutError(f"F289 branch pilot exceeded {ALARM_SECONDS} seconds")


def result_record(value):
    return {
        "objective": value[0],
        "product": value[1],
        "point": [value[2], value[3]],
    }


def public_incumbent(n, modulus, a, b):
    center = math.isqrt((b * n) // a)
    tested = []
    seen = set()
    radius = 0
    while len(tested) < 64:
        for x in (center - radius, center + radius):
            if x >= 1 and x & 1 and x not in seen:
                seen.add(x)
                tested.append(x)
                if len(tested) == 64:
                    break
        radius += 1

    best = None
    for x in tested:
        y = least_feasible_y(n, x, modulus)
        candidate = (a * x + b * y, x * y, x, y)
        if best is None or candidate < best:
            best = candidate

    for x, y in ((1, n), (n, 1)):
        candidate = (a * x + b * y, n, x, y)
        if candidate < best:
            best = candidate

    assert best is not None
    assert best[2] > 0 and best[3] > 0
    assert best[1] >= n and (best[1] - n) % modulus == 0
    return best, len(tested), center


def node_support(n, k, r, u0, a, b, objective_cap):
    """Return the exact coarse-node lexicographic support below the cap."""
    s = 1 << r
    node_modulus = 1 << min(k, 2 * r + 1)
    inverse0 = pow(u0, -1, node_modulus)
    v0 = n * inverse0 % node_modulus
    delta = n * (
        pow(u0 + s, -1, node_modulus) - inverse0
    ) % node_modulus

    discriminant = objective_cap * objective_cap - 4 * a * b * n
    assert discriminant >= 0
    root = math.isqrt(discriminant)
    denominator = 2 * a
    lower = max(1, (objective_cap - root + denominator - 1) // denominator)
    upper = (objective_cap + root) // denominator

    quadratic_lower = a * lower * lower - objective_cap * lower + b * n
    quadratic_upper = a * upper * upper - objective_cap * upper + b * n
    assert lower <= upper
    assert quadratic_lower <= 0 and quadratic_upper <= 0
    if lower > 1:
        assert a * (lower - 1) * (lower - 1) - objective_cap * (lower - 1) + b * n > 0
    assert a * (upper + 1) * (upper + 1) - objective_cap * (upper + 1) + b * n > 0

    first_x = u0 + s * ((lower - u0 + s - 1) // s)
    best = None
    scanned = 0
    for x in range(first_x, upper + 1, s):
        scanned += 1
        j = (x - u0) // s
        residue = (v0 + delta * j) % node_modulus
        y_lower = (n + x - 1) // x
        y = y_lower + (residue - y_lower) % node_modulus
        assert x > 0 and y > 0 and x * y >= n
        assert (x * y - n) % node_modulus == 0
        candidate = (a * x + b * y, x * y, x, y)
        if candidate[0] <= objective_cap and (best is None or candidate < best):
            best = candidate
    return best, scanned


def branch_support(n, modulus, a, b):
    k = modulus.bit_length() - 1
    assert modulus == 1 << k and k >= MIN_K and n & 1
    h = max(1, k // 2)
    initial, incumbent_x_trials, center = public_incumbent(n, modulus, a, b)
    incumbent = initial

    queried = [0] * (h + 1)
    expanded = [0] * (h + 1)
    pruned = [0] * (h + 1)
    accepted = [0] * (h + 1)
    scanned = [0] * (h + 1)
    heap = []
    peak_queue = 0

    def evaluate(r, u0):
        nonlocal peak_queue
        queried[r] += 1
        bound, count = node_support(n, k, r, u0, a, b, incumbent[0])
        scanned[r] += count
        if bound is None or bound >= incumbent:
            pruned[r] += 1
            return
        heapq.heappush(heap, (bound, r, u0))
        peak_queue = max(peak_queue, len(heap))

    evaluate(1, 1)
    while heap:
        bound, r, u0 = heapq.heappop(heap)
        if bound >= incumbent:
            pruned[r] += 1
            continue
        if (bound[1] - n) % modulus == 0:
            accepted[r] += 1
            incumbent = bound
            continue

        assert r < h
        expanded[r] += 1
        s = 1 << r
        evaluate(r + 1, u0)
        evaluate(r + 1, u0 + s)

    assert sum(queried) == sum(expanded) + sum(pruned) + sum(accepted)
    assert incumbent[2] > 0 and incumbent[3] > 0
    assert incumbent[1] >= n and (incumbent[1] - n) % modulus == 0
    depth_counts = [
        {
            "depth": r,
            "queried": queried[r],
            "expanded": expanded[r],
            "pruned": pruned[r],
            "accepted": accepted[r],
            "scanned_x_values": scanned[r],
        }
        for r in range(1, h + 1)
    ]
    root_outcome = (
        "expanded"
        if expanded[1]
        else "accepted"
        if accepted[1]
        else "pruned"
    )
    return {
        "initial": initial,
        "result": incumbent,
        "incumbent_x_trials": incumbent_x_trials,
        "continuous_center_floor": center,
        "h": h,
        "leaf_nodes": 1 << (h - 1),
        "queried_nodes": sum(queried),
        "expanded_nodes": sum(expanded),
        "pruned_nodes": sum(pruned),
        "accepted_nodes": sum(accepted),
        "peak_queue": peak_queue,
        "scanned_x_values": sum(scanned),
        "root_outcome": root_outcome,
        "counts_by_depth": depth_counts,
    }


def full_enumeration_baseline(n, modulus):
    """Stream the existing finite support capture for all fixed normals."""
    root = math.isqrt(n)
    if root * root < n:
        root += 1
    x0 = root if root & 1 else root + 1
    y0 = least_feasible_y(n, x0, modulus)
    k_bound = max(x0, y0)

    best = {normal: None for normal in NORMALS}
    scanned = 0
    for x in range(1, k_bound + 1, 2):
        scanned += 1
        y = least_feasible_y(n, x, modulus)
        points = ((x, y),) if x == y else ((x, y), (y, x))
        for point_x, point_y in points:
            product = point_x * point_y
            assert product >= n and (product - n) % modulus == 0
            for a, b in NORMALS:
                candidate = (
                    a * point_x + b * point_y,
                    product,
                    point_x,
                    point_y,
                )
                if best[(a, b)] is None or candidate < best[(a, b)]:
                    best[(a, b)] = candidate

    assert all(value is not None for value in best.values())
    return best, [x0, y0], k_bound, scanned


def post_hoc_outcome(result, n, p_label, q_label):
    x, y = result[2], result[3]
    if result[1] > n:
        return "nonfactor"
    assert result[1] == n
    if x == 1 or y == 1:
        return "trivial_factor"
    assert {x, y} == {p_label, q_label}
    return "proper_factor"


def aggregate_rows(scale_rows):
    queries = [
        query
        for scale in scale_rows
        for batch in scale["batches"]
        for query in batch["queries"]
    ]
    batches = [batch for scale in scale_rows for batch in scale["batches"]]
    depth_rows = [
        row for query in queries for row in query["counts_by_depth"]
    ]
    maximum_depth = max(row["depth"] for row in depth_rows)
    counts_by_depth = [
        {
            "depth": depth,
            "queried": sum(
                row["queried"] for row in depth_rows if row["depth"] == depth
            ),
            "expanded": sum(
                row["expanded"] for row in depth_rows if row["depth"] == depth
            ),
            "pruned": sum(
                row["pruned"] for row in depth_rows if row["depth"] == depth
            ),
            "accepted": sum(
                row["accepted"] for row in depth_rows if row["depth"] == depth
            ),
            "scanned_x_values": sum(
                row["scanned_x_values"]
                for row in depth_rows
                if row["depth"] == depth
            ),
        }
        for depth in range(1, maximum_depth + 1)
    ]
    queried_nodes = sum(query["queried_nodes"] for query in queries)
    full_leaf_node_count = sum(query["leaf_nodes"] for query in queries)
    branch_scanned = sum(query["scanned_x_values"] for query in queries)
    baseline_logical_scanned = sum(
        batch["scanned_x_values"] * len(batch["queries"]) for batch in batches
    )
    node_gcd = math.gcd(queried_nodes, full_leaf_node_count)
    scan_gcd = math.gcd(branch_scanned, baseline_logical_scanned)
    outcomes = {
        name: sum(query["outcome"] == name for query in queries)
        for name in ("proper_factor", "trivial_factor", "nonfactor")
    }
    return {
        "scales": len(scale_rows),
        "batches": len(batches),
        "queries": len(queries),
        "all_results_match_baseline": all(query["matches_baseline"] for query in queries),
        "outcomes": outcomes,
        "initial_incumbent_optimal": sum(
            query["initial_incumbent_optimal"] for query in queries
        ),
        "root_outcomes": {
            name: sum(query["root_outcome"] == name for query in queries)
            for name in ("accepted", "expanded", "pruned")
        },
        "queried_nodes": queried_nodes,
        "expanded_nodes": sum(query["expanded_nodes"] for query in queries),
        "pruned_nodes": sum(query["pruned_nodes"] for query in queries),
        "accepted_nodes": sum(query["accepted_nodes"] for query in queries),
        "full_leaf_node_count": full_leaf_node_count,
        "queried_to_full_leaf_ratio": [
            queried_nodes // node_gcd,
            full_leaf_node_count // node_gcd,
        ],
        "peak_queue": max(query["peak_queue"] for query in queries),
        "branch_scanned_x_values": branch_scanned,
        "baseline_logical_scanned_x_values": baseline_logical_scanned,
        "branch_to_logical_baseline_scan_ratio": [
            branch_scanned // scan_gcd,
            baseline_logical_scanned // scan_gcd,
        ],
        "baseline_actual_shared_scanned_x_values": sum(
            batch["scanned_x_values"] for batch in batches
        ),
        "branch_runtime_seconds": sum(
            query["runtime_seconds"] for query in queries
        ),
        "baseline_shared_runtime_seconds": sum(
            batch["runtime_seconds"] for batch in batches
        ),
        "counts_by_depth": counts_by_depth,
    }


def compact_certificate(scale, batch, query):
    return {
        "label": scale["label"],
        "B": scale["B"],
        "N": scale["N"],
        "p_label": scale["p_label"],
        "q_label": scale["q_label"],
        "M": batch["M"],
        "k": batch["k"],
        "normal": query["normal"],
        "initial": query["initial"],
        "result": query["result"],
        "outcome": query["outcome"],
        "h": query["h"],
        "leaf_nodes": query["leaf_nodes"],
        "queried_nodes": query["queried_nodes"],
        "expanded_nodes": query["expanded_nodes"],
        "pruned_nodes": query["pruned_nodes"],
        "accepted_nodes": query["accepted_nodes"],
        "peak_queue": query["peak_queue"],
        "branch_scanned_x_values": query["scanned_x_values"],
        "baseline_scanned_x_values": batch["scanned_x_values"],
        "root_outcome": query["root_outcome"],
    }


def main():
    started = time.monotonic()
    logs = [
        "F289 exact affine-node branch-and-bound support pilot",
        f"source_alarm_seconds={ALARM_SECONDS}",
        "processes=1",
        "estimated_peak_memory_mb<128",
        "branch_runs_before_baseline=true",
        "factor_labels_used_for=case_construction_and_post_hoc_audit_only",
        "node_order=(objective,product,x,y)",
    ]
    scales = []

    def run_scale(exponent, phase):
        scale_started = time.monotonic()
        scale, p_label, q_label = labelled_semiprime(exponent)
        n = p_label * q_label
        modulus_limit = 16 * math.isqrt(n)
        maximum_k = modulus_limit.bit_length() - 1
        scale_record = {
            "label": f"B=2^{exponent}",
            "B": scale,
            "N": n,
            "N_bits": n.bit_length(),
            "p_label": p_label,
            "q_label": q_label,
            "modulus_limit": modulus_limit,
            "maximum_k": maximum_k,
            "batches": [],
        }

        for k in range(MIN_K, maximum_k + 1):
            modulus = 1 << k
            branch_rows = []
            for a, b in NORMALS:
                query_started = time.monotonic()
                branch = branch_support(n, modulus, a, b)
                branch["runtime_seconds"] = time.monotonic() - query_started
                branch_rows.append(((a, b), branch))

            baseline_started = time.monotonic()
            baseline, p0, k_bound, baseline_scanned = full_enumeration_baseline(
                n, modulus
            )
            baseline_runtime = time.monotonic() - baseline_started

            query_records = []
            for normal, branch in branch_rows:
                exact = baseline[normal]
                assert branch["result"] == exact
                outcome = post_hoc_outcome(
                    branch["result"], n, p_label, q_label
                )
                query_records.append(
                    {
                        "normal": list(normal),
                        "initial": result_record(branch["initial"]),
                        "result": result_record(branch["result"]),
                        "baseline_result": result_record(exact),
                        "outcome": outcome,
                        "matches_baseline": True,
                        "initial_incumbent_optimal": branch["initial"]
                        == branch["result"],
                        "incumbent_x_trials": branch["incumbent_x_trials"],
                        "continuous_center_floor": branch[
                            "continuous_center_floor"
                        ],
                        "h": branch["h"],
                        "leaf_nodes": branch["leaf_nodes"],
                        "queried_nodes": branch["queried_nodes"],
                        "expanded_nodes": branch["expanded_nodes"],
                        "pruned_nodes": branch["pruned_nodes"],
                        "accepted_nodes": branch["accepted_nodes"],
                        "peak_queue": branch["peak_queue"],
                        "scanned_x_values": branch["scanned_x_values"],
                        "root_outcome": branch["root_outcome"],
                        "runtime_seconds": branch["runtime_seconds"],
                        "counts_by_depth": branch["counts_by_depth"],
                    }
                )

            scale_record["batches"].append(
                {
                    "M": modulus,
                    "k": k,
                    "P0": p0,
                    "K": k_bound,
                    "scanned_x_values": baseline_scanned,
                    "runtime_seconds": baseline_runtime,
                    "queries": query_records,
                }
            )

        scales.append(scale_record)
        elapsed = time.monotonic() - scale_started
        logs.append(
            f"phase={phase} B=2^{exponent} maximum_k={maximum_k} "
            f"batches={len(scale_record['batches'])} "
            f"queries={len(scale_record['batches']) * len(NORMALS)} "
            f"elapsed_seconds={elapsed:.6f}"
        )

    run_scale(INITIAL_EXPONENTS[0], "small_pilot")
    pilot_elapsed = time.monotonic() - started
    logs.append(f"small_pilot_elapsed_seconds={pilot_elapsed:.6f}")

    if pilot_elapsed < 5:
        for exponent in INITIAL_EXPONENTS[1:]:
            run_scale(exponent, "initial")

    initial_elapsed = time.monotonic() - started
    logs.append(f"initial_elapsed_seconds={initial_elapsed:.6f}")
    extended = []
    max_rss_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    max_rss_bytes = max_rss_raw if sys.platform == "darwin" else max_rss_raw * 1024
    if (
        len(scales) == len(INITIAL_EXPONENTS)
        and initial_elapsed < 12
        and max_rss_bytes < 128 * (1 << 20)
    ):
        run_scale(EXTENDED_EXPONENTS[0], "extended")
        extended.append(EXTENDED_EXPONENTS[0])

    elapsed_before_last = time.monotonic() - started
    max_rss_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    max_rss_bytes = max_rss_raw if sys.platform == "darwin" else max_rss_raw * 1024
    if (
        extended
        and elapsed_before_last < 20
        and max_rss_bytes < 128 * (1 << 20)
    ):
        run_scale(EXTENDED_EXPONENTS[1], "extended")
        extended.append(EXTENDED_EXPONENTS[1])

    aggregate = aggregate_rows(scales)
    query_refs = [
        (scale, batch, query)
        for scale in scales
        for batch in scale["batches"]
        for query in batch["queries"]
    ]
    root_accept = next(
        (entry for entry in query_refs if entry[2]["root_outcome"] == "accepted"),
        None,
    )
    best_node_reduction = min(
        query_refs,
        key=lambda entry: Fraction(
            entry[2]["queried_nodes"], entry[2]["leaf_nodes"]
        ),
    )
    largest_scan_ratio = max(
        query_refs,
        key=lambda entry: Fraction(
            entry[2]["scanned_x_values"], entry[1]["scanned_x_values"]
        ),
    )
    maximum_modulus = max(entry[1]["M"] for entry in query_refs)
    largest_modulus_middle_normal = next(
        entry
        for entry in query_refs
        if entry[1]["M"] == maximum_modulus and entry[2]["normal"] == [3, 2]
    )
    chosen = [
        entry
        for entry in (
            root_accept,
            best_node_reduction,
            largest_scan_ratio,
            largest_modulus_middle_normal,
        )
        if entry is not None
    ]
    representatives = []
    seen = set()
    for scale, batch, query in chosen:
        key = (scale["N"], batch["M"], tuple(query["normal"]))
        if key not in seen:
            seen.add(key)
            representatives.append(compact_certificate(scale, batch, query))

    elapsed = time.monotonic() - started
    max_rss_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    max_rss_bytes = max_rss_raw if sys.platform == "darwin" else max_rss_raw * 1024
    payload = {
        "experiment": "F289_affine_node_branch_support",
        "status": "exact_finite_query_count_pilot",
        "decision_inputs": ["N", "M", "a", "b"],
        "factor_label_scope": "case construction and post-hoc audit only",
        "normal_order": "(objective, product, x, y)",
        "normals": [list(normal) for normal in NORMALS],
        "resource_plan": {
            "processes": 1,
            "source_alarm_seconds": ALARM_SECONDS,
            "estimated_peak_memory_mb": "<128",
            "initial_exponents": list(INITIAL_EXPONENTS),
            "conditional_extended_exponents": list(EXTENDED_EXPONENTS),
            "maximum_modulus_rule": "largest power of two at most 16*isqrt(N)",
        },
        "runtime": {
            "elapsed_seconds": elapsed,
            "max_rss_bytes": max_rss_bytes,
            "extended_exponents_completed": extended,
        },
        "aggregate": aggregate,
        "aggregates_by_scale": [
            {"label": scale["label"], **aggregate_rows([scale])}
            for scale in scales
        ],
        "representative_certificates": representatives,
        "scales": scales,
    }
    logs.append(f"total_elapsed_seconds={elapsed:.6f}")
    logs.append(f"max_rss_bytes={max_rss_bytes}")
    logs.append(f"scales={len(scales)}")
    logs.append(f"batches={aggregate['batches']}")
    logs.append(f"queries={aggregate['queries']}")
    logs.append(f"queried_nodes={aggregate['queried_nodes']}")
    logs.append(f"branch_scanned_x_values={aggregate['branch_scanned_x_values']}")
    logs.append(
        "baseline_logical_scanned_x_values="
        f"{aggregate['baseline_logical_scanned_x_values']}"
    )
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
                    "scales": output["aggregate"]["scales"],
                    "queries": output["aggregate"]["queries"],
                    "all_results_match_baseline": output["aggregate"][
                        "all_results_match_baseline"
                    ],
                    "elapsed_seconds": output["runtime"]["elapsed_seconds"],
                    "max_rss_bytes": output["runtime"]["max_rss_bytes"],
                },
                indent=2,
            )
        )
    except BaseException:
        signal.alarm(0)
        LOG_PATH.write_text(traceback.format_exc(), encoding="utf-8")
        raise
