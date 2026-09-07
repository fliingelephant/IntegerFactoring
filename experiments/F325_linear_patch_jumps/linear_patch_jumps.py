#!/usr/bin/env python3
"""F325: exact first-exit jumps for the modified D-layer parity graph."""

import argparse
from collections import Counter
import hashlib
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

import gurobipy as gp


ROOT = Path(__file__).resolve().parents[2]
F322_DIR = ROOT / "experiments" / "F322_ppa_collision_structure"
F324_DIR = ROOT / "experiments" / "F324_reflection_pairings"
sys.path.insert(0, str(F322_DIR))
sys.path.insert(0, str(F324_DIR))
from parity_paths import Pairing
from reflection_pairings import ReflectionMatching, jacobi, sample_unit_character


SEED = 32520260907
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024
METHODS = ("original_R_micro", "modified_R_micro", "modified_R_macro")
DATASETS = {
    "pilot": (209, 1333),
    "scale": (10807, 66013),
}
F324_OUTPUTS = (
    F324_DIR / "pilot_output.json",
    F324_DIR / "scale_output.json",
)


def peak_rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_sha256():
    return sha256(Path(__file__))


def write_json(path, value):
    target = Path(path)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(target)


def split_node(pairing, node):
    layer, offset = divmod(node, pairing.n)
    return layer, offset - pairing.h


def make_node(pairing, layer, x):
    return layer * pairing.n + x + pairing.h


def is_d_state(pairing, node):
    layer, x = split_node(pairing, node)
    if layer != 1 or x == 0:
        return False
    ax = pairing.rep(pairing.a * x)
    bx = pairing.rep(pairing.bi * x)
    return not (
        (x > 0 and ax > 0 and bx > 0)
        or (x < 0 and ax < 0 and bx < 0)
    )


def modified_r(pairing, node):
    if is_d_state(pairing, node):
        layer, x = split_node(pairing, node)
        return make_node(pairing, layer, -x), "D:negate_modified"
    return pairing.r(node)


def validate_endpoint(pairing, node, result):
    if "factor" in result:
        factor = result["factor"]
        assert 1 < factor < pairing.n and pairing.n % factor == 0
        return "factor"
    root = result["root"]
    assert root * root % pairing.n == result["radicand"] % pairing.n
    return "root"


def walk_micro(n, a, b, cap, modified):
    pairing = Pairing(n, a, b)
    matching = ReflectionMatching(pairing, (1, 1, 1))
    current = matching.start()
    states_before_r = []
    trace = []
    branch_counts = Counter()
    port_counts = Counter()
    removed_d_nonunit_states = 0
    seen = set()
    result = None
    endpoint_type = None
    endpoint_node = None
    censor_reason = None

    for step in range(1, cap + 1):
        if current in seen:
            censor_reason = "repeated_state"
            break
        seen.add(current)
        states_before_r.append(current)
        layer, x = split_node(pairing, current)
        d_state = is_d_state(pairing, current)
        if modified and d_state and math.gcd(x, n) > 1:
            removed_d_nonunit_states += 1
        r_node, branch = (
            modified_r(pairing, current) if modified else pairing.r(current)
        )
        branch_counts[branch] += 1
        if r_node == current:
            result = pairing.decode(current)
            endpoint_type = validate_endpoint(pairing, current, result)
            endpoint_node = current
            if len(trace) < 80:
                trace.append(
                    {
                        "step": step,
                        "node": current,
                        "layer": layer,
                        "x": x,
                        "d_state": d_state,
                        "branch": branch,
                        "terminal": True,
                    }
                )
            break
        next_node, port = matching.apply(r_node)
        port_counts[port] += 1
        if len(trace) < 80:
            next_layer, next_x = split_node(pairing, next_node)
            trace.append(
                {
                    "step": step,
                    "node": current,
                    "layer": layer,
                    "x": x,
                    "d_state": d_state,
                    "branch": branch,
                    "r_node": r_node,
                    "s_port": port,
                    "next_node": next_node,
                    "next_layer": next_layer,
                    "next_x": next_x,
                }
            )
        current = next_node
    else:
        censor_reason = "step_cap"

    return {
        "method": "modified_R_micro" if modified else "original_R_micro",
        "status": "completed" if result is not None else "censored",
        "censor_reason": censor_reason,
        "cap": cap,
        "r_calls": len(states_before_r),
        "equivalent_r_calls": len(states_before_r),
        "matching_calls": sum(port_counts.values()),
        "result": result,
        "endpoint_type": endpoint_type,
        "endpoint_node": endpoint_node,
        "states_before_r_validation": states_before_r,
        "state_after_cap_validation": current,
        "removed_d_nonunit_states": removed_d_nonunit_states,
        "branch_counts": dict(branch_counts),
        "port_counts": dict(port_counts),
        "trace_prefix": trace,
    }


def brute_first_exit(pairing, x):
    started = time.perf_counter()
    scanned = 0
    if x > 0:
        values = range(x + 1, pairing.h)
        fallback = pairing.h
        positive = True
    else:
        values = range(x + 1, 0)
        fallback = 0
        positive = False
    for z in values:
        scanned += 1
        az = pairing.rep(pairing.a * z)
        bz = pairing.rep(pairing.bi * z)
        if (positive and az > 0 and bz > 0) or (
            not positive and az < 0 and bz < 0
        ):
            return z, scanned, time.perf_counter() - started
    return fallback, scanned, time.perf_counter() - started


def gurobi_first_exit(pairing, x, environment):
    validation_target, scanned, validation_seconds = brute_first_exit(pairing, x)
    if pairing.a == pairing.n - 1:
        direct = pairing.h if x > 0 else 0
        assert direct == validation_target
        return {
            "status": "special_a_minus1",
            "target": direct,
            "solver_called": False,
            "solver_seconds": 0.0,
            "validation_target": validation_target,
            "validation_scanned": scanned,
            "validation_seconds": validation_seconds,
            "exact_candidate_verified": True,
        }

    lower_z = x + 1
    upper_z = pairing.h - 1 if x > 0 else -1
    fallback = pairing.h if x > 0 else 0
    if lower_z > upper_z:
        assert fallback == validation_target
        return {
            "status": "empty_interval",
            "target": fallback,
            "solver_called": False,
            "solver_seconds": 0.0,
            "validation_target": validation_target,
            "validation_scanned": scanned,
            "validation_seconds": validation_seconds,
            "exact_candidate_verified": True,
        }

    lower_value = 1 if x > 0 else pairing.h + 1
    upper_value = pairing.h if x > 0 else pairing.n - 1
    started = time.perf_counter()
    model = gp.Model(env=environment)
    model.Params.OutputFlag = 0
    model.Params.Threads = 1
    model.Params.TimeLimit = 1.0
    model.Params.MIPGap = 0.0
    model.Params.MIPGapAbs = 0.0
    model.Params.IntFeasTol = 1e-9
    model.Params.FeasibilityTol = 1e-9
    z = model.addVar(lb=lower_z, ub=upper_z, vtype=gp.GRB.INTEGER, name="z")
    ka = model.addVar(
        lb=-pairing.n, ub=pairing.n, vtype=gp.GRB.INTEGER, name="k_a"
    )
    kb = model.addVar(
        lb=-pairing.n, ub=pairing.n, vtype=gp.GRB.INTEGER, name="k_b"
    )
    model.addConstr(pairing.a * z - pairing.n * ka >= lower_value)
    model.addConstr(pairing.a * z - pairing.n * ka <= upper_value)
    model.addConstr(pairing.bi * z - pairing.n * kb >= lower_value)
    model.addConstr(pairing.bi * z - pairing.n * kb <= upper_value)
    model.setObjective(z, gp.GRB.MINIMIZE)
    model.optimize()
    solver_seconds = time.perf_counter() - started
    status_code = model.Status
    result = {
        "solver_called": True,
        "solver_status_code": status_code,
        "solver_seconds": solver_seconds,
        "validation_target": validation_target,
        "validation_scanned": scanned,
        "validation_seconds": validation_seconds,
    }

    if status_code == gp.GRB.OPTIMAL and model.SolCount:
        candidate = int(round(z.X))
        candidate_ka = int(round(ka.X))
        candidate_kb = int(round(kb.X))
        exact_a = pairing.a * candidate - pairing.n * candidate_ka
        exact_b = pairing.bi * candidate - pairing.n * candidate_kb
        exact_valid = (
            lower_z <= candidate <= upper_z
            and lower_value <= exact_a <= upper_value
            and lower_value <= exact_b <= upper_value
            and candidate == validation_target
        )
        result.update(
            {
                "status": "optimal" if exact_valid else "invalid_candidate",
                "target": candidate if exact_valid else None,
                "candidate": candidate,
                "candidate_k_a": candidate_ka,
                "candidate_k_b": candidate_kb,
                "candidate_a_residue": exact_a,
                "candidate_b_residue": exact_b,
                "exact_candidate_verified": exact_valid,
            }
        )
    elif status_code == gp.GRB.INFEASIBLE:
        exact_valid = validation_target == fallback
        result.update(
            {
                "status": "infeasible" if exact_valid else "false_infeasible",
                "target": fallback if exact_valid else None,
                "exact_candidate_verified": exact_valid,
            }
        )
    else:
        result.update(
            {
                "status": "solver_unresolved",
                "target": None,
                "exact_candidate_verified": False,
            }
        )
    model.dispose()
    return result


def reference_state(micro, index):
    states = micro["states_before_r_validation"]
    if index < len(states):
        return states[index]
    if (
        index == micro["cap"]
        and micro["status"] == "censored"
        and micro["censor_reason"] == "step_cap"
    ):
        return micro["state_after_cap_validation"]
    return None


def walk_macro(n, a, b, cap, environment, modified_micro):
    pairing = Pairing(n, a, b)
    matching = ReflectionMatching(pairing, (1, 1, 1))
    current = matching.start()
    equivalent_steps = 0
    actual_r_calls = 0
    matching_calls = 0
    macro_actions = 0
    skipped_d_steps = 0
    removed_d_nonunit_states = 0
    branch_counts = Counter()
    port_counts = Counter()
    solver_status_counts = Counter()
    solver_calls = 0
    solver_seconds = 0.0
    validation_seconds = 0.0
    validation_scanned = 0
    first_exit_records = []
    trace = []
    result = None
    endpoint_type = None
    endpoint_node = None
    censor_reason = None

    while equivalent_steps < cap:
        expected_current = reference_state(modified_micro, equivalent_steps)
        assert expected_current == current, (
            "macro/reference state mismatch",
            n,
            a,
            b,
            equivalent_steps,
            current,
            expected_current,
        )
        layer, x = split_node(pairing, current)
        if is_d_state(pairing, current) and x != pairing.h:
            first_exit = gurobi_first_exit(pairing, x, environment)
            solver_status_counts[first_exit["status"]] += 1
            solver_calls += int(first_exit["solver_called"])
            solver_seconds += first_exit["solver_seconds"]
            validation_seconds += first_exit["validation_seconds"]
            validation_scanned += first_exit["validation_scanned"]
            if len(first_exit_records) < 80:
                first_exit_records.append({"from_x": x, **first_exit})
            if not first_exit["exact_candidate_verified"]:
                censor_reason = "first_exit_" + first_exit["status"]
                break
            target = first_exit["target"]
            jump = target - x
            assert jump > 0
            remaining = cap - equivalent_steps
            if jump > remaining:
                equivalent_steps = cap
                current = reference_state(modified_micro, cap)
                censor_reason = "equivalent_step_cap"
                break
            reference_states = modified_micro["states_before_r_validation"][
                equivalent_steps : equivalent_steps + jump
            ]
            for state in reference_states:
                _, state_x = split_node(pairing, state)
                if is_d_state(pairing, state) and math.gcd(state_x, n) > 1:
                    removed_d_nonunit_states += 1
            equivalent_steps += jump
            skipped_d_steps += jump
            macro_actions += 1
            current = make_node(pairing, 1, target)
            assert reference_state(modified_micro, equivalent_steps) == current
            if len(trace) < 80:
                trace.append(
                    {
                        "kind": "macro",
                        "from_x": x,
                        "to_x": target,
                        "jump": jump,
                        "equivalent_steps": equivalent_steps,
                        "solver_status": first_exit["status"],
                    }
                )
            continue

        d_state = is_d_state(pairing, current)
        if d_state and math.gcd(x, n) > 1:
            removed_d_nonunit_states += 1
        r_node, branch = modified_r(pairing, current)
        actual_r_calls += 1
        equivalent_steps += 1
        branch_counts[branch] += 1
        if r_node == current:
            result = pairing.decode(current)
            endpoint_type = validate_endpoint(pairing, current, result)
            endpoint_node = current
            if len(trace) < 80:
                trace.append(
                    {
                        "kind": "micro",
                        "x": x,
                        "d_state": d_state,
                        "branch": branch,
                        "terminal": True,
                        "equivalent_steps": equivalent_steps,
                    }
                )
            break
        next_node, port = matching.apply(r_node)
        matching_calls += 1
        port_counts[port] += 1
        if len(trace) < 80:
            _, next_x = split_node(pairing, next_node)
            trace.append(
                {
                    "kind": "micro",
                    "x": x,
                    "d_state": d_state,
                    "branch": branch,
                    "s_port": port,
                    "next_x": next_x,
                    "equivalent_steps": equivalent_steps,
                }
            )
        current = next_node
    else:
        censor_reason = "equivalent_step_cap"

    status = "completed" if result is not None else "censored"
    matches_reference = None
    if not (censor_reason or "").startswith("first_exit_"):
        matches_reference = (
            status == modified_micro["status"]
            and result == modified_micro["result"]
            and endpoint_node == modified_micro["endpoint_node"]
            and equivalent_steps == modified_micro["equivalent_r_calls"]
        )
        assert matches_reference

    return {
        "method": "modified_R_macro",
        "status": status,
        "censor_reason": censor_reason,
        "cap": cap,
        "r_calls_actual": actual_r_calls,
        "matching_calls_actual": matching_calls,
        "macro_actions": macro_actions,
        "skipped_d_steps": skipped_d_steps,
        "equivalent_r_calls": equivalent_steps,
        "removed_d_nonunit_states": removed_d_nonunit_states,
        "result": result,
        "endpoint_type": endpoint_type,
        "endpoint_node": endpoint_node,
        "matches_modified_micro": matches_reference,
        "branch_counts_actual": dict(branch_counts),
        "port_counts_actual": dict(port_counts),
        "solver_calls": solver_calls,
        "solver_status_counts": dict(solver_status_counts),
        "solver_seconds": solver_seconds,
        "validation_seconds": validation_seconds,
        "validation_scanned": validation_scanned,
        "first_exit_records_prefix": first_exit_records,
        "trace_prefix": trace,
    }


def small_modified_checks(limit=31):
    started = time.perf_counter()
    checks = Counter()
    for n in range(3, limit + 1, 2):
        units = [value for value in range(1, n) if math.gcd(value, n) == 1]
        for a in units:
            for b in units:
                pairing = Pairing(n, a, b)
                original = [pairing.r(z)[0] for z in range(3 * n)]
                modified = [modified_r(pairing, z)[0] for z in range(3 * n)]
                assert all(modified[modified[z]] == z for z in range(3 * n))
                checks["pairings"] += 1
                checks["states"] += 3 * n
                for z in range(3 * n):
                    if is_d_state(pairing, z):
                        _, x = split_node(pairing, z)
                        if math.gcd(x, n) > 1:
                            assert original[z] == z
                            assert modified[z] != z
                            checks["removed_d_nonunit_fixed_points"] += 1
                    if modified[z] == z:
                        result = pairing.decode(z)
                        validate_endpoint(pairing, z, result)
                        checks["fixed_endpoints"] += 1
    return {
        "limit": limit,
        "checks": dict(checks),
        "elapsed_seconds": time.perf_counter() - started,
    }


def load_public_queries(dataset):
    wanted = set(DATASETS[dataset])
    by_n = {}
    source_hashes = {}
    for path in F324_OUTPUTS:
        source_hashes[path.name] = sha256(path)
        data = json.loads(path.read_text())
        for row in data["generation"]:
            if row["n"] in wanted:
                by_n.setdefault(row["n"], []).append(row)
    queries = []
    for n in DATASETS[dataset]:
        rows = sorted(by_n[n], key=lambda row: row["query_index"])
        assert len(rows) == 8
        queries.extend(
            {
                **row,
                "query_kind": "reused_F324_public_pair",
            }
            for row in rows
        )
        if jacobi(-1, n) == 1:
            template = rows[0]
            generator = random.Random(int.from_bytes(
                hashlib.sha256(f"{SEED}:{dataset}:{n}:a_minus1".encode()).digest()[:8],
                "big",
            ))
            b, b_cost = sample_unit_character(n, -1, generator)
            for factor in b_cost["proper_factor_hits"]:
                assert 1 < factor < n and n % factor == 0
            queries.append(
                {
                    "n": n,
                    "p_offline": template["p_offline"],
                    "q_offline": template["q_offline"],
                    "query_index": 8,
                    "query_kind": "conditional_public_a_minus1",
                    "a": n - 1,
                    "b": b,
                    "a_qr_mod_p_offline": pow(
                        n - 1, (template["p_offline"] - 1) // 2, template["p_offline"]
                    )
                    == 1,
                    "a_qr_mod_q_offline": pow(
                        n - 1, (template["q_offline"] - 1) // 2, template["q_offline"]
                    )
                    == 1,
                    "a_square_mod_n_offline": (
                        pow(
                            n - 1,
                            (template["p_offline"] - 1) // 2,
                            template["p_offline"],
                        )
                        == 1
                        and pow(
                            n - 1,
                            (template["q_offline"] - 1) // 2,
                            template["q_offline"],
                        )
                        == 1
                    ),
                    "a_generation": {
                        "public_fixed_value": n - 1,
                        "jacobi_calls": 1,
                        "jacobi_value": 1,
                    },
                    "b_generation": b_cost,
                    "generation_factor_hits": b_cost["proper_factor_hits"],
                }
            )
    return queries, source_hashes


def summarize(query_results):
    summary = {}
    for method in METHODS:
        rows = [query[method] for query in query_results]
        completed = [row for row in rows if row["status"] == "completed"]
        entry = {
            "runs": len(rows),
            "completed": len(completed),
            "censored": len(rows) - len(completed),
            "factor_endpoints": sum(
                row["endpoint_type"] == "factor" for row in completed
            ),
            "root_endpoints": sum(
                row["endpoint_type"] == "root" for row in completed
            ),
            "censor_reasons": dict(
                Counter(row["censor_reason"] for row in rows if row["censor_reason"])
            ),
        }
        if method == "modified_R_macro":
            entry.update(
                {
                    "mean_equivalent_r_calls": statistics.fmean(
                        row["equivalent_r_calls"] for row in rows
                    ),
                    "mean_actual_r_calls": statistics.fmean(
                        row["r_calls_actual"] for row in rows
                    ),
                    "mean_macro_actions": statistics.fmean(
                        row["macro_actions"] for row in rows
                    ),
                    "total_skipped_d_steps": sum(
                        row["skipped_d_steps"] for row in rows
                    ),
                    "total_removed_d_nonunit_states": sum(
                        row["removed_d_nonunit_states"] for row in rows
                    ),
                    "total_solver_calls": sum(row["solver_calls"] for row in rows),
                    "solver_status_counts": dict(
                        sum(
                            (
                                Counter(row["solver_status_counts"])
                                for row in rows
                            ),
                            Counter(),
                        )
                    ),
                    "solver_seconds": sum(row["solver_seconds"] for row in rows),
                    "validation_seconds": sum(
                        row["validation_seconds"] for row in rows
                    ),
                    "validation_scanned": sum(
                        row["validation_scanned"] for row in rows
                    ),
                    "all_match_modified_micro": all(
                        row["matches_modified_micro"] is True for row in rows
                    ),
                }
            )
        else:
            entry.update(
                {
                    "mean_r_calls": statistics.fmean(row["r_calls"] for row in rows),
                    "max_r_calls": max(row["r_calls"] for row in rows),
                    "total_removed_d_nonunit_states": sum(
                        row["removed_d_nonunit_states"] for row in rows
                    ),
                }
            )
        summary[method] = entry
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", choices=sorted(DATASETS), required=True)
    parser.add_argument("--small-checks", action="store_true")
    parser.add_argument("--output", required=True)
    parser.add_argument("--status", required=True)
    arguments = parser.parse_args()
    started = time.perf_counter()

    def timeout_handler(_signal_number, _frame):
        raise TimeoutError("internal 28-second alarm fired")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(INTERNAL_TIMEOUT_SECONDS)
    write_json(
        arguments.status,
        {
            "status": "running",
            "dataset": arguments.dataset,
            "seed": SEED,
            "source_sha256": source_sha256(),
            "pairing_source_sha256": sha256(F322_DIR / "parity_paths.py"),
        },
    )
    environment = None
    try:
        environment = gp.Env(empty=True)
        environment.setParam("OutputFlag", 0)
        environment.setParam("Threads", 1)
        environment.start()
        small_checks = small_modified_checks() if arguments.small_checks else None
        public_queries, f324_hashes = load_public_queries(arguments.dataset)
        results = []
        for query in public_queries:
            n, a, b = query["n"], query["a"], query["b"]
            assert math.gcd(a, n) == math.gcd(b, n) == 1
            assert jacobi(a, n) == 1 and jacobi(b, n) == -1
            cap = min(3 * n, 8192)
            original = walk_micro(n, a, b, cap, modified=False)
            modified = walk_micro(n, a, b, cap, modified=True)
            macro = walk_macro(n, a, b, cap, environment, modified)
            original.pop("states_before_r_validation")
            original.pop("state_after_cap_validation")
            modified.pop("states_before_r_validation")
            modified.pop("state_after_cap_validation")
            result = {
                "query": query,
                "cap": cap,
                "original_R_micro": original,
                "modified_R_micro": modified,
                "modified_R_macro": macro,
                "original_vs_modified_same_endpoint": (
                    original["status"] == modified["status"]
                    and original["result"] == modified["result"]
                    and original["endpoint_node"] == modified["endpoint_node"]
                ),
            }
            results.append(result)
            print(
                json.dumps(
                    {
                        "event": "query_complete",
                        "dataset": arguments.dataset,
                        "n": n,
                        "query_kind": query["query_kind"],
                        "query_index": query["query_index"],
                        "steps": {
                            "original": original["equivalent_r_calls"],
                            "modified": modified["equivalent_r_calls"],
                            "macro_actual": macro["r_calls_actual"],
                            "macro_equivalent": macro["equivalent_r_calls"],
                        },
                        "statuses": {
                            "original": original["status"],
                            "modified": modified["status"],
                            "macro": macro["status"],
                        },
                    }
                ),
                flush=True,
            )
            if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
                raise MemoryError("peak RSS exceeded 512 MiB")

        payload = {
            "status": "passed",
            "experiment": "F325_linear_patch_jumps",
            "family": "route:F29",
            "dataset": arguments.dataset,
            "seed": SEED,
            "methods": METHODS,
            "source_sha256": source_sha256(),
            "pairing_source_sha256": sha256(F322_DIR / "parity_paths.py"),
            "f324_output_hashes": f324_hashes,
            "public_scope": (
                "The eight base parameter pairs per modulus are the exact public "
                "F324 pairs. Offline factors only retain prior labels and verify "
                "outputs. Conditional a=-1 controls use the public Jacobi condition."
            ),
            "graph_scope": (
                "Macro and modified micro paths use the modified graph in which "
                "D-layer nonunits are paired. Removed original fixed points are "
                "counted only as removed states, never as skipped successes."
            ),
            "solver_scope": (
                "Gurobi 13.0.2 uses one thread and a one-second per-call limit. "
                "Every optimum or infeasible result is checked by exact arithmetic "
                "and a brute linear scan. The scan is validation, not algorithm work."
            ),
            "cap_rule": "min(3*N,8192) equivalent r calls",
            "small_modified_checks": small_checks,
            "summary": summarize(results),
            "queries": results,
            "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
            "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
            "memory_limit_bytes": MEMORY_LIMIT_BYTES,
            "total_walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, payload)
        status = {
            key: payload[key]
            for key in (
                "status",
                "experiment",
                "dataset",
                "seed",
                "source_sha256",
                "pairing_source_sha256",
                "internal_timeout_seconds",
                "hard_timeout_seconds",
                "memory_limit_bytes",
                "total_walltime_seconds",
                "peak_rss_bytes",
            )
        }
        status["output"] = arguments.output
        write_json(arguments.status, status)
        print(json.dumps({"event": "passed", **status}), flush=True)
    except BaseException as exception:
        failure = {
            "status": "failed",
            "experiment": "F325_linear_patch_jumps",
            "dataset": arguments.dataset,
            "seed": SEED,
            "source_sha256": source_sha256(),
            "exception_type": type(exception).__name__,
            "exception": str(exception),
            "traceback": traceback.format_exc(),
            "total_walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, failure)
        write_json(arguments.status, failure)
        print(json.dumps({"event": "failed", **failure}), flush=True)
        raise
    finally:
        if environment is not None:
            environment.dispose()
        signal.alarm(0)


if __name__ == "__main__":
    main()
