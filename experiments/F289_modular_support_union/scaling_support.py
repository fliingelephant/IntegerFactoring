"""F289 scaling pilot for affine-node support at M comparable to N.

The one-patch oracle is imported from F288/PATCH_SUPPORT.py. One process uses
a 30-second hard alarm, a 26-second global soft budget, and bounded exact
queries. Budget exhaustion is recorded as a result state.
"""

import heapq
import json
import math
import resource
import signal
import sys
import time
import traceback
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "F288_integer_hyperbola_support"))

import PATCH_SUPPORT as patch_oracle
from branch_support import full_enumeration_baseline, public_incumbent, result_record


ALARM_SECONDS = 30
GLOBAL_SOFT_SECONDS = 26
QUERY_SOFT_SECONDS = 2.5
MAX_NODE_QUERIES = 100_000
MEMORY_CAP_BYTES = 128 * (1 << 20)
FACTOR_EXPONENTS = (8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60)
NORMALS = ((1, 1), (2, 1), (5, 4), (4, 3), (3, 2), (7, 4))
OUTPUT_PATH = HERE / "scaling_output.json"
LOG_PATH = HERE / "scaling_run.log"


def alarm_handler(_signum, _frame):
    raise TimeoutError(f"F289 scaling pilot exceeded {ALARM_SECONDS} seconds")


def is_prime_64(value):
    if value < 2:
        return False
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % prime == 0:
            return value == prime

    odd_part = value - 1
    shifts = 0
    while odd_part & 1 == 0:
        shifts += 1
        odd_part >>= 1
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % value == 0:
            continue
        witness = pow(base, odd_part, value)
        if witness in (1, value - 1):
            continue
        for _ in range(shifts - 1):
            witness = witness * witness % value
            if witness == value - 1:
                break
        else:
            return False
    return True


def next_prime_64(candidate):
    candidate = max(2, candidate)
    if candidate == 2:
        return candidate
    candidate |= 1
    while not is_prime_64(candidate):
        candidate += 2
    return candidate


def labelled_balanced_semiprime(exponent):
    scale = 1 << exponent
    p_label = next_prime_64(9 * scale // 8 + 2 * exponent + 1)
    q_label = next_prime_64(7 * scale // 4 + 3 * exponent + 1)
    assert p_label != q_label and p_label & 1 and q_label & 1
    assert p_label < 1 << 64 and q_label < 1 << 64
    return scale, p_label, q_label


def public_outcome(value, n):
    if value[1] > n:
        return "nonfactor"
    assert value[1] == n
    if value[2] == 1 or value[3] == 1:
        return "trivial_factor"
    return "proper_factor"


def audit_factor_label(value, n, p_label, q_label):
    outcome = public_outcome(value, n)
    if outcome == "proper_factor":
        assert {value[2], value[3]} == {p_label, q_label}
    return outcome


def fast_branch_support(n, modulus, a, b, query_deadline):
    k = modulus.bit_length() - 1
    assert modulus == 1 << k and n & 1
    h = max(1, k // 2)
    started = time.monotonic()
    initial, incumbent_x_trials, center = public_incumbent(n, modulus, a, b)
    incumbent = initial

    for name in patch_oracle.counts:
        patch_oracle.counts[name] = 0

    queried = [0] * (h + 1)
    expanded = [0] * (h + 1)
    pruned = [0] * (h + 1)
    accepted = [0] * (h + 1)
    primitives = [
        {"support_calls": 0, "seek_calls": 0, "next_calls": 0, "raycasts": 0}
        for _ in range(h + 1)
    ]
    heap = []
    peak_queue = 0
    early_factor = None
    approximate = None

    def milestone(value, depth, source):
        return {
            "source": source,
            "depth": depth,
            "value": result_record(value),
            "outcome": public_outcome(value, n),
            "queried_nodes": sum(queried),
            "expanded_nodes": sum(expanded),
            "elapsed_seconds": time.monotonic() - started,
            "primitive_calls": dict(patch_oracle.counts),
        }

    if public_outcome(initial, n) == "proper_factor":
        early_factor = milestone(initial, 0, "initial_incumbent")

    def evaluate(r, u0):
        nonlocal early_factor, peak_queue
        before = dict(patch_oracle.counts)
        point = patch_oracle.support(
            n, *patch_oracle.patch(n, k, r, u0), a, b
        )
        assert point is not None
        bound = (
            a * point[0] + b * point[1],
            point[0] * point[1],
            point[0],
            point[1],
        )
        queried[r] += 1
        for name in primitives[r]:
            primitives[r][name] += patch_oracle.counts[name] - before[name]

        if early_factor is None and public_outcome(bound, n) == "proper_factor":
            early_factor = milestone(bound, r, "node_oracle")

        if bound >= incumbent:
            pruned[r] += 1
            return
        heapq.heappush(heap, (bound, r, u0))
        peak_queue = max(peak_queue, len(heap))

    def record_approximation():
        nonlocal approximate
        if approximate is not None:
            return
        minimum_live_node_objective = None if not heap else heap[0][0][0]
        global_lower_objective = min(
            incumbent[0],
            incumbent[0]
            if minimum_live_node_objective is None
            else minimum_live_node_objective,
        )
        if 100 * incumbent[0] <= 101 * global_lower_objective:
            approximate = {
                "value": result_record(incumbent),
                "outcome": public_outcome(incumbent, n),
                "minimum_live_node_objective": minimum_live_node_objective,
                "global_lower_objective": global_lower_objective,
                "inequality": [
                    100 * incumbent[0],
                    101 * global_lower_objective,
                ],
                "queried_nodes": sum(queried),
                "expanded_nodes": sum(expanded),
                "elapsed_seconds": time.monotonic() - started,
                "primitive_calls": dict(patch_oracle.counts),
            }

    evaluate(1, 1)
    record_approximation()
    status = "exact"
    budget_reason = None

    while heap:
        bound, r, u0 = heap[0]
        if bound >= incumbent:
            heapq.heappop(heap)
            pruned[r] += 1
            record_approximation()
            continue
        if (bound[1] - n) % modulus == 0:
            heapq.heappop(heap)
            accepted[r] += 1
            incumbent = bound
            record_approximation()
            continue

        # Both budget gates precede the pop. On exit, this unsplit parent
        # remains in the heap and covers its entire unresolved subtree.
        if sum(queried) + 2 > MAX_NODE_QUERIES:
            status = "budget_exhausted"
            budget_reason = "node_limit"
            break
        if time.monotonic() >= query_deadline:
            status = "budget_exhausted"
            budget_reason = "query_time"
            break

        heapq.heappop(heap)
        assert r < h
        expanded[r] += 1
        s = 1 << r
        # Once expansion begins, query both children before the next gate.
        evaluate(r + 1, u0)
        evaluate(r + 1, u0 + s)
        record_approximation()

    if not heap:
        status = "exact"
        budget_reason = None
        record_approximation()

    assert sum(queried) == sum(expanded) + sum(pruned) + sum(accepted) + len(heap)
    assert sum(queried) == patch_oracle.counts["support_calls"]
    assert incumbent[1] >= n and (incumbent[1] - n) % modulus == 0
    if status == "exact":
        assert not heap
    else:
        assert heap

    depth_counts = [
        {
            "depth": depth,
            "queried": queried[depth],
            "expanded": expanded[depth],
            "pruned": pruned[depth],
            "accepted": accepted[depth],
            **primitives[depth],
        }
        for depth in range(1, h + 1)
        if queried[depth]
    ]
    minimum_live_node_objective = None if not heap else heap[0][0][0]
    global_lower_objective = min(
        incumbent[0],
        incumbent[0]
        if minimum_live_node_objective is None
        else minimum_live_node_objective,
    )
    return {
        "status": status,
        "budget_reason": budget_reason,
        "initial": result_record(initial),
        "current_incumbent": result_record(incumbent),
        "exact_result": result_record(incumbent) if status == "exact" else None,
        "current_outcome": public_outcome(incumbent, n),
        "incumbent_x_trials": incumbent_x_trials,
        "continuous_center_floor": center,
        "h": h,
        "leaf_nodes": 1 << (h - 1),
        "queried_nodes": sum(queried),
        "expanded_nodes": sum(expanded),
        "pruned_nodes": sum(pruned),
        "accepted_nodes": sum(accepted),
        "live_nodes": len(heap),
        "minimum_live_node_objective": minimum_live_node_objective,
        "global_lower_objective": global_lower_objective,
        "unresolved_subtree_frontier_complete": True,
        "peak_queue": peak_queue,
        "primitive_calls": dict(patch_oracle.counts),
        "early_factor_detection": early_factor,
        "relative_1_01_certificate": approximate,
        "counts_by_depth": depth_counts,
        "runtime_seconds": time.monotonic() - started,
    }


def query_audit(query, n, p_label, q_label):
    current = query["current_incumbent"]
    current_value = (
        current["objective"],
        current["product"],
        current["point"][0],
        current["point"][1],
    )
    assert audit_factor_label(current_value, n, p_label, q_label) == query[
        "current_outcome"
    ]
    for key in ("early_factor_detection", "relative_1_01_certificate"):
        event = query[key]
        if event is None:
            continue
        value = event["value"]
        tuple_value = (
            value["objective"],
            value["product"],
            value["point"][0],
            value["point"][1],
        )
        assert audit_factor_label(tuple_value, n, p_label, q_label) == event[
            "outcome"
        ]


def aggregate(scales):
    queries = [query for scale in scales for query in scale["queries"]]
    exact = [query for query in queries if query["status"] == "exact"]
    exhausted = [
        query for query in queries if query["status"] == "budget_exhausted"
    ]
    return {
        "inputs": len(scales),
        "queries": len(queries),
        "exact_queries": len(exact),
        "budget_exhausted_queries": len(exhausted),
        "budget_reasons": {
            reason: sum(query["budget_reason"] == reason for query in exhausted)
            for reason in ("query_time", "node_limit")
        },
        "exact_outcomes": {
            outcome: sum(query["current_outcome"] == outcome for query in exact)
            for outcome in ("proper_factor", "trivial_factor", "nonfactor")
        },
        "queries_with_early_factor_detection": sum(
            query["early_factor_detection"] is not None for query in queries
        ),
        "early_factor_detected_before_final_node_count": sum(
            query["early_factor_detection"] is not None
            and query["early_factor_detection"]["queried_nodes"]
            < query["queried_nodes"]
            for query in queries
        ),
        "budget_exhausted_with_early_factor": sum(
            query["status"] == "budget_exhausted"
            and query["early_factor_detection"] is not None
            for query in queries
        ),
        "queries_with_relative_1_01_certificate": sum(
            query["relative_1_01_certificate"] is not None for query in queries
        ),
        "relative_1_01_certified_before_final_node_count": sum(
            query["relative_1_01_certificate"] is not None
            and query["relative_1_01_certificate"]["queried_nodes"]
            < query["queried_nodes"]
            for query in queries
        ),
        "relative_1_01_proper_factor_certificates": sum(
            query["relative_1_01_certificate"] is not None
            and query["relative_1_01_certificate"]["outcome"] == "proper_factor"
            for query in queries
        ),
        "inputs_with_early_factor_detection": sum(
            scale["summary"]["any_early_factor_detection"] for scale in scales
        ),
        "inputs_with_relative_1_01_factor": sum(
            scale["summary"]["any_relative_1_01_factor"] for scale in scales
        ),
        "inputs_with_exact_factor_result": sum(
            scale["summary"]["any_exact_factor_result"] for scale in scales
        ),
        "queried_nodes": sum(query["queried_nodes"] for query in queries),
        "expanded_nodes": sum(query["expanded_nodes"] for query in queries),
        "pruned_nodes": sum(query["pruned_nodes"] for query in queries),
        "accepted_nodes": sum(query["accepted_nodes"] for query in queries),
        "maximum_queried_nodes": max(query["queried_nodes"] for query in queries),
        "maximum_peak_queue": max(query["peak_queue"] for query in queries),
        "primitive_calls": {
            name: sum(query["primitive_calls"][name] for query in queries)
            for name in patch_oracle.counts
        },
        "runtime_seconds": sum(query["runtime_seconds"] for query in queries),
    }


def main():
    started = time.monotonic()
    global_deadline = started + GLOBAL_SOFT_SECONDS
    logs = [
        "F289 M=Theta(N) affine-node scaling pilot",
        f"source_alarm_seconds={ALARM_SECONDS}",
        f"global_soft_seconds={GLOBAL_SOFT_SECONDS}",
        f"query_soft_seconds={QUERY_SOFT_SECONDS}",
        f"max_node_queries={MAX_NODE_QUERIES}",
        "processes=1",
        "estimated_peak_memory_mb<128",
        "factor_labels_used_for=case_construction_and_post_hoc_audit_only",
        "patch_oracle=F288/PATCH_SUPPORT.py",
    ]
    scales = []
    stop_reason = None

    for exponent in FACTOR_EXPONENTS:
        if time.monotonic() >= global_deadline:
            stop_reason = "global_time_budget"
            break
        max_rss_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        max_rss_bytes = (
            max_rss_raw if sys.platform == "darwin" else max_rss_raw * 1024
        )
        if max_rss_bytes >= MEMORY_CAP_BYTES:
            stop_reason = "memory_cap"
            break

        scale_started = time.monotonic()
        scale, p_label, q_label = labelled_balanced_semiprime(exponent)
        n = p_label * q_label
        modulus_limit = n // 8
        k = modulus_limit.bit_length() - 1
        modulus = 1 << k
        assert modulus <= n // 8 < 2 * modulus
        query_rows = []

        for a, b in NORMALS:
            if time.monotonic() >= global_deadline:
                stop_reason = "global_time_budget"
                break
            query_deadline = min(
                global_deadline, time.monotonic() + QUERY_SOFT_SECONDS
            )
            query = fast_branch_support(
                n, modulus, a, b, query_deadline
            )
            query["normal"] = [a, b]
            query_audit(query, n, p_label, q_label)
            query_rows.append(query)

        if not query_rows:
            break

        baseline = None
        baseline_runtime = None
        baseline_scanned = None
        if exponent == FACTOR_EXPONENTS[0] and len(query_rows) == len(NORMALS):
            baseline_started = time.monotonic()
            baseline_values, p0, k_bound, baseline_scanned = (
                full_enumeration_baseline(n, modulus)
            )
            baseline_runtime = time.monotonic() - baseline_started
            baseline = {
                "P0": p0,
                "K": k_bound,
                "scanned_x_values": baseline_scanned,
                "runtime_seconds": baseline_runtime,
            }
            for query in query_rows:
                normal = tuple(query["normal"])
                assert query["status"] == "exact"
                assert query["exact_result"] == result_record(
                    baseline_values[normal]
                )

        scale_summary = {
            "queries_run": len(query_rows),
            "exact_queries": sum(
                query["status"] == "exact" for query in query_rows
            ),
            "budget_exhausted_queries": sum(
                query["status"] == "budget_exhausted" for query in query_rows
            ),
            "any_early_factor_detection": any(
                query["early_factor_detection"] is not None
                for query in query_rows
            ),
            "any_relative_1_01_factor": any(
                query["relative_1_01_certificate"] is not None
                and query["relative_1_01_certificate"]["outcome"]
                == "proper_factor"
                for query in query_rows
            ),
            "any_exact_factor_result": any(
                query["status"] == "exact"
                and query["current_outcome"] == "proper_factor"
                for query in query_rows
            ),
            "queried_nodes": sum(
                query["queried_nodes"] for query in query_rows
            ),
            "maximum_queried_nodes": max(
                query["queried_nodes"] for query in query_rows
            ),
            "maximum_peak_queue": max(
                query["peak_queue"] for query in query_rows
            ),
        }
        if scale_summary["exact_queries"] == len(NORMALS):
            assert scale_summary["any_relative_1_01_factor"]
            assert scale_summary["any_exact_factor_result"]

        scales.append(
            {
                "label": f"factor_scale=2^{exponent}",
                "B": scale,
                "N": n,
                "N_bits": n.bit_length(),
                "p_label": p_label,
                "q_label": q_label,
                "factor_ratio": [q_label, p_label],
                "M": modulus,
                "k": k,
                "M_over_N_bounds": ["1/16", "1/8"],
                "h": max(1, k // 2),
                "leaf_nodes": 1 << (max(1, k // 2) - 1),
                "summary": scale_summary,
                "small_exact_baseline": baseline,
                "queries": query_rows,
            }
        )
        logs.append(
            f"factor_scale=2^{exponent} N_bits={n.bit_length()} k={k} "
            f"queries={len(query_rows)} exact={scale_summary['exact_queries']} "
            f"budget_exhausted={scale_summary['budget_exhausted_queries']} "
            f"nodes={scale_summary['queried_nodes']} "
            f"elapsed_seconds={time.monotonic() - scale_started:.6f}"
        )
        if stop_reason is not None:
            break

    totals = aggregate(scales)
    query_refs = [
        (scale, query) for scale in scales for query in scale["queries"]
    ]
    exact_refs = [
        entry for entry in query_refs if entry[1]["status"] == "exact"
    ]
    exhausted_refs = [
        entry for entry in query_refs if entry[1]["status"] == "budget_exhausted"
    ]
    early_refs = [
        entry
        for entry in query_refs
        if entry[1]["early_factor_detection"] is not None
    ]
    representatives = []
    if scales and scales[0]["small_exact_baseline"] is not None:
        representatives.append(
            {
                "kind": "small_exact_baseline",
                "label": scales[0]["label"],
                "N": scales[0]["N"],
                "M": scales[0]["M"],
                "comparisons": len(scales[0]["queries"]),
                **scales[0]["small_exact_baseline"],
            }
        )
    if early_refs:
        scale, query = max(early_refs, key=lambda entry: entry[0]["N_bits"])
        representatives.append(
            {
                "kind": "largest_input_early_factor",
                "label": scale["label"],
                "N": scale["N"],
                "N_bits": scale["N_bits"],
                "M": scale["M"],
                "normal": query["normal"],
                "event": query["early_factor_detection"],
                "exact_status": query["status"],
                "exact_queried_nodes": query["queried_nodes"],
            }
        )
    if exact_refs:
        scale, query = max(exact_refs, key=lambda entry: entry[0]["N_bits"])
        representatives.append(
            {
                "kind": "largest_exact_query",
                "label": scale["label"],
                "N": scale["N"],
                "N_bits": scale["N_bits"],
                "M": scale["M"],
                "normal": query["normal"],
                "result": query["exact_result"],
                "outcome": query["current_outcome"],
                "queried_nodes": query["queried_nodes"],
                "peak_queue": query["peak_queue"],
                "runtime_seconds": query["runtime_seconds"],
            }
        )
    if exhausted_refs:
        scale, query = exhausted_refs[0]
        representatives.append(
            {
                "kind": "first_budget_exhausted_query",
                "label": scale["label"],
                "N": scale["N"],
                "N_bits": scale["N_bits"],
                "M": scale["M"],
                "normal": query["normal"],
                "budget_reason": query["budget_reason"],
                "current_incumbent": query["current_incumbent"],
                "minimum_live_node_objective": query[
                    "minimum_live_node_objective"
                ],
                "global_lower_objective": query["global_lower_objective"],
                "relative_1_01_certificate": query[
                    "relative_1_01_certificate"
                ],
                "queried_nodes": query["queried_nodes"],
                "live_nodes": query["live_nodes"],
                "peak_queue": query["peak_queue"],
                "runtime_seconds": query["runtime_seconds"],
            }
        )

    elapsed = time.monotonic() - started
    max_rss_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    max_rss_bytes = (
        max_rss_raw if sys.platform == "darwin" else max_rss_raw * 1024
    )
    payload = {
        "experiment": "F289_affine_patch_scaling",
        "status": "finite_scaling_pilot",
        "decision_inputs": ["N", "M", "a", "b"],
        "factor_label_scope": "case construction and post-hoc audit only",
        "modulus_rule": "largest power of two at most N/8",
        "normals": [list(normal) for normal in NORMALS],
        "relative_accuracy_test": (
            "100*incumbent <= 101*min(incumbent,"
            "minimum_live_node_objective)"
        ),
        "resource_plan": {
            "processes": 1,
            "source_alarm_seconds": ALARM_SECONDS,
            "global_soft_seconds": GLOBAL_SOFT_SECONDS,
            "query_soft_seconds": QUERY_SOFT_SECONDS,
            "max_node_queries": MAX_NODE_QUERIES,
            "memory_cap_bytes": MEMORY_CAP_BYTES,
            "factor_exponents": list(FACTOR_EXPONENTS),
        },
        "runtime": {
            "elapsed_seconds": elapsed,
            "max_rss_bytes": max_rss_bytes,
            "stop_reason": stop_reason or "input_schedule_completed",
        },
        "aggregate": totals,
        "representative_certificates": representatives,
        "scales": scales,
    }
    logs.append(f"total_elapsed_seconds={elapsed:.6f}")
    logs.append(f"max_rss_bytes={max_rss_bytes}")
    logs.append(f"stop_reason={payload['runtime']['stop_reason']}")
    logs.append(f"inputs={totals['inputs']}")
    logs.append(f"queries={totals['queries']}")
    logs.append(f"exact_queries={totals['exact_queries']}")
    logs.append(
        f"budget_exhausted_queries={totals['budget_exhausted_queries']}"
    )
    logs.append(f"queried_nodes={totals['queried_nodes']}")
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
                    "inputs": output["aggregate"]["inputs"],
                    "queries": output["aggregate"]["queries"],
                    "exact_queries": output["aggregate"]["exact_queries"],
                    "budget_exhausted_queries": output["aggregate"][
                        "budget_exhausted_queries"
                    ],
                    "elapsed_seconds": output["runtime"]["elapsed_seconds"],
                    "max_rss_bytes": output["runtime"]["max_rss_bytes"],
                    "stop_reason": output["runtime"]["stop_reason"],
                },
                indent=2,
            )
        )
    except BaseException:
        signal.alarm(0)
        LOG_PATH.write_text(traceback.format_exc(), encoding="utf-8")
        raise
