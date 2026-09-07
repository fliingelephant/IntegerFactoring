#!/usr/bin/env python3
"""F324: public reflection matchings composed with F322's Pairing involution."""

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


F322_DIR = Path(__file__).resolve().parents[1] / "F322_ppa_collision_structure"
sys.path.insert(0, str(F322_DIR))
from parity_paths import Pairing


SEED = 32420260907
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024
QUERIES_PER_N = 8
METHODS = (
    "common_C_1",
    "common_C_minus1",
    "common_C_2",
    "layer_C_1_1_b",
    "layer_C_1_ainv_b",
    "common_C_uniform",
    "adjacent",
    "negation",
)
DATASETS = {
    "pilot": ((209, 11, 19), (1333, 31, 43), (10807, 101, 107)),
    "scale": ((66013, 251, 263), (256027, 503, 509)),
}


def peak_rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def source_sha256():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def dependency_sha256():
    return hashlib.sha256((F322_DIR / "parity_paths.py").read_bytes()).hexdigest()


def write_json(path, value):
    target = Path(path)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(target)


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def derived_seed(dataset, n_index, query_index, purpose):
    raw = f"{SEED}:{dataset}:{n_index}:{query_index}:{purpose}".encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:8], "big")


def sample_unit_character(n, target, generator):
    draws = 0
    gcd_calls = 0
    jacobi_calls = 0
    proper_factors = []
    full_gcds = 0
    while True:
        value = generator.randrange(n)
        draws += 1
        divisor = math.gcd(value, n)
        gcd_calls += 1
        if 1 < divisor < n:
            proper_factors.append(divisor)
            continue
        if divisor == n:
            full_gcds += 1
            continue
        symbol = jacobi(value, n)
        jacobi_calls += 1
        if symbol == target:
            return value, {
                "draws": draws,
                "gcd_calls": gcd_calls,
                "jacobi_calls": jacobi_calls,
                "proper_factor_hits": proper_factors,
                "full_gcds": full_gcds,
            }


class ReflectionMatching:
    def __init__(self, pairing, constants):
        self.pairing = pairing
        self.n = pairing.n
        self.constants = tuple(value % self.n for value in constants)
        inverse_two = pow(2, -1, self.n)
        self.fixed_coordinates = tuple(
            pairing.rep(value * inverse_two % self.n) for value in self.constants
        )

    def node(self, layer, coordinate):
        return layer * self.n + coordinate + self.pairing.h

    def split(self, node):
        layer, offset = divmod(node, self.n)
        return layer, offset - self.pairing.h

    def start(self):
        return self.node(2, self.fixed_coordinates[2])

    def apply(self, node):
        layer, coordinate = self.split(node)
        if layer == 0 and coordinate == self.fixed_coordinates[0]:
            return self.node(1, self.fixed_coordinates[1]), "cross_01"
        if layer == 1 and coordinate == self.fixed_coordinates[1]:
            return self.node(0, self.fixed_coordinates[0]), "cross_10"
        if layer == 2 and coordinate == self.fixed_coordinates[2]:
            return node, "fixed_2"
        reflected = self.pairing.rep(self.constants[layer] - coordinate)
        return self.node(layer, reflected), "standard"


class AdjacentMatching:
    def __init__(self, pairing):
        self.pairing = pairing
        self.n = pairing.n

    def start(self):
        return 0

    def split(self, node):
        layer, offset = divmod(node, self.n)
        return layer, offset - self.pairing.h

    def apply(self, node):
        if node == 0:
            return node, "fixed_adjacent"
        return (node + 1 if node % 2 else node - 1), "adjacent"


def matrix_multiply(left, right):
    return (
        left[0] * right[0] + left[1] * right[2],
        left[0] * right[1] + left[1] * right[3],
        left[2] * right[0] + left[3] * right[2],
        left[2] * right[1] + left[3] * right[3],
    )


def compress_runs(sequence):
    histogram = Counter()
    current = None
    length = 0
    run_count = 0
    for item in sequence:
        if item is None:
            if length:
                histogram[length] += 1
                run_count += 1
            current = None
            length = 0
            continue
        if item == current:
            length += 1
        else:
            if length:
                histogram[length] += 1
                run_count += 1
            current = item
            length = 1
    if length:
        histogram[length] += 1
        run_count += 1
    return (
        {str(k): v for k, v in sorted(histogram.items())},
        max(histogram, default=0),
        run_count,
    )


def method_constants(method, n, a, b, generator):
    if method == "common_C_1":
        return (1, 1, 1), {}
    if method == "common_C_minus1":
        return (-1, -1, -1), {}
    if method == "common_C_2":
        return (2, 2, 2), {}
    if method == "layer_C_1_1_b":
        return (1, 1, b), {}
    if method == "layer_C_1_ainv_b":
        return (1, pow(a, -1, n), b), {}
    if method == "common_C_uniform":
        value = generator.randrange(n)
        return (value, value, value), {"random_C": value, "random_draws": 1}
    if method == "negation":
        return (0, 0, 0), {}
    if method == "adjacent":
        return None, {}
    raise ValueError(method)


def validate_endpoint(pairing, node, result):
    if "factor" in result:
        factor = result["factor"]
        assert 1 < factor < pairing.n and pairing.n % factor == 0
        return "factor"
    root = result["root"]
    radicand = result["radicand"]
    assert root * root % pairing.n == radicand % pairing.n
    return "root"


def walk(n, a, b, method, constants, cap):
    pairing = Pairing(n, a, b)
    matching = AdjacentMatching(pairing) if method == "adjacent" else ReflectionMatching(pairing, constants)
    current = matching.start()
    trace = []
    branch_counts = Counter()
    port_counts = Counter()
    exception_counts = Counter()
    matrix_counts = Counter()
    matrix_sequence = []
    prediction_checks = 0
    seen = set()
    result = None
    endpoint_type = None
    censor_reason = None

    inverse_a = pow(a, -1, n)
    inverse_constants = {
        "1": 1 % n,
        "ainv": inverse_a,
        "b": b % n,
        "b2": b * b % n,
        "b_over_a": b * inverse_a % n,
    }

    for step in range(1, cap + 1):
        if current in seen:
            censor_reason = "repeated_state"
            break
        seen.add(current)
        source_layer, source_x = matching.split(current)
        r_node, branch = pairing.r(current)
        branch_counts[branch] += 1
        r_layer, r_x = matching.split(r_node)
        if r_node == current:
            result = pairing.decode(current)
            endpoint_type = validate_endpoint(pairing, current, result)
            exception_counts["terminal"] += 1
            if len(trace) < 80:
                trace.append(
                    {
                        "step": step,
                        "node": current,
                        "layer": source_layer,
                        "x": source_x,
                        "r_node": r_node,
                        "r_layer": r_layer,
                        "r_x": r_x,
                        "branch": branch,
                        "terminal": True,
                    }
                )
            break

        next_node, port = matching.apply(r_node)
        port_counts[port] += 1
        next_layer, next_x = matching.split(next_node)
        matrix_key = None
        predicted_x = None

        if method == "adjacent":
            exception_counts["adjacent_matching"] += 1
            matrix_sequence.append(None)
        elif port != "standard":
            exception_counts["auxiliary_port"] += 1
            matrix_sequence.append(None)
        elif source_x == 0 or r_x == 0:
            exception_counts["zero_coordinate"] += 1
            matrix_sequence.append(None)
        elif "swap01" in branch:
            exception_counts["zero_swap"] += 1
            matrix_sequence.append(None)
        elif branch == "nonunit":
            exception_counts["nonunit"] += 1
            matrix_sequence.append(None)
        else:
            destination_c = constants[r_layer] % n
            if r_x == pairing.rep(-source_x):
                predicted_x = pairing.rep(source_x + destination_c)
                matrix = (1, destination_c, 0, 1)
                matrix_key = f"add:C={destination_c}"
            else:
                assert math.gcd(source_x, n) == 1
                actual_c = r_x * source_x % n
                labels = sorted(
                    name for name, value in inverse_constants.items() if value == actual_c
                )
                assert labels, (n, a, b, method, source_x, r_x, actual_c, branch)
                predicted_x = pairing.rep(
                    destination_c - actual_c * pow(source_x, -1, n)
                )
                matrix = (destination_c, (-actual_c) % n, 1, 0)
                matrix_key = (
                    f"inverse:C={destination_c}:c={actual_c}:"
                    + ",".join(labels)
                )
            assert predicted_x == next_x
            prediction_checks += 1
            matrix_counts[matrix_key] += 1
            matrix_sequence.append(matrix_key)

        if len(trace) < 80:
            trace.append(
                {
                    "step": step,
                    "node": current,
                    "layer": source_layer,
                    "x": source_x,
                    "r_node": r_node,
                    "r_layer": r_layer,
                    "r_x": r_x,
                    "branch": branch,
                    "s_port": port,
                    "next_node": next_node,
                    "next_layer": next_layer,
                    "next_x": next_x,
                    "matrix_key": matrix_key,
                    "predicted_x": predicted_x,
                }
            )
        current = next_node
    else:
        censor_reason = "step_cap"

    run_histogram, max_run, run_count = compress_runs(matrix_sequence)
    cube = matrix_multiply(matrix_multiply((1, -1, 1, 0), (1, -1, 1, 0)), (1, -1, 1, 0))
    unipotent_square = matrix_multiply((1, -1, 1, -1), (1, -1, 1, -1))
    assert cube == (-1, 0, 0, -1)
    assert unipotent_square == (0, 0, 0, 0)

    return {
        "method": method,
        "constants_mod_n": ([value % n for value in constants] if constants is not None else None),
        "fixed_coordinates": (
            list(matching.fixed_coordinates)
            if isinstance(matching, ReflectionMatching)
            else None
        ),
        "start_node": matching.start(),
        "cap": cap,
        "steps": len(seen),
        "status": "completed" if result is not None else "censored",
        "censor_reason": censor_reason,
        "result": result,
        "endpoint_type": endpoint_type,
        "branch_counts": dict(branch_counts),
        "port_counts": dict(port_counts),
        "exception_counts": dict(exception_counts),
        "generic_prediction_checks": prediction_checks,
        "generic_matrix_counts": dict(matrix_counts),
        "generic_matrix_run_histogram": run_histogram,
        "generic_matrix_run_count": run_count,
        "max_generic_same_matrix_run": max_run,
        "algebra_checks": {
            "C1_c1_matrix_cube": list(cube),
            "C1_c1_expected_minus_identity": True,
            "C2_c1_M_minus_I_square": list(unipotent_square),
            "C2_c1_unipotent_check": True,
        },
        "trace_prefix": trace,
    }


def small_full_checks(limit=31):
    checks = Counter()
    started = time.perf_counter()
    for n in range(3, limit + 1, 2):
        inverse_two = pow(2, -1, n)
        for c0 in range(n):
            for c1 in range(n):
                for c2 in range(n):
                    h = n // 2

                    def rep(value):
                        return (value + h) % n - h

                    fixed = [rep(c * inverse_two % n) for c in (c0, c1, c2)]

                    def node(layer, x):
                        return layer * n + x + h

                    def s(z):
                        layer, offset = divmod(z, n)
                        x = offset - h
                        if layer == 0 and x == fixed[0]:
                            return node(1, fixed[1])
                        if layer == 1 and x == fixed[1]:
                            return node(0, fixed[0])
                        if layer == 2 and x == fixed[2]:
                            return z
                        return node(layer, rep((c0, c1, c2)[layer] - x))

                    values = [s(z) for z in range(3 * n)]
                    assert all(values[values[z]] == z for z in range(3 * n))
                    assert sum(values[z] == z for z in range(3 * n)) == 1
                    if c0 == c1 == c2 == 0:
                        for z in range(3 * n):
                            layer, offset = divmod(z, n)
                            x = offset - h
                            expected = (
                                layer * n - x + h
                                if x
                                else ((1 - layer) * n + h if layer < 2 else z)
                            )
                            assert values[z] == expected
                            checks["negation_match_states"] += 1
                    checks["reflection_matchings"] += 1
                    checks["reflection_states"] += 3 * n

        units = [value for value in range(1, n) if math.gcd(value, n) == 1]
        for a in units:
            for b in units:
                pairing = Pairing(n, a, b)
                rr = [pairing.r(z)[0] for z in range(3 * n)]
                assert all(rr[rr[z]] == z for z in range(3 * n))
                checks["pairings"] += 1
                checks["pairing_states"] += 3 * n
                for z in range(3 * n):
                    if rr[z] == z:
                        result = pairing.decode(z)
                        validate_endpoint(pairing, z, result)
                        checks["endpoints"] += 1
    return {
        "limit": limit,
        "checks": dict(checks),
        "elapsed_seconds": time.perf_counter() - started,
    }


def summarize(rows):
    by_method = {}
    for method in METHODS:
        subset = [row for row in rows if row["method"] == method]
        completed = [row for row in subset if row["status"] == "completed"]
        factors = [row for row in completed if row["endpoint_type"] == "factor"]
        roots = [row for row in completed if row["endpoint_type"] == "root"]
        port_counts = Counter()
        matrix_counts = Counter()
        run_histogram = Counter()
        for row in subset:
            port_counts.update(row["port_counts"])
            matrix_counts.update(row["generic_matrix_counts"])
            run_histogram.update(
                {int(length): count for length, count in row["generic_matrix_run_histogram"].items()}
            )
        by_method[method] = {
            "runs": len(subset),
            "completed": len(completed),
            "censored": len(subset) - len(completed),
            "factor_endpoints": len(factors),
            "root_endpoints": len(roots),
            "censor_reasons": dict(
                Counter(row["censor_reason"] for row in subset if row["censor_reason"])
            ),
            "mean_steps_all_runs": statistics.fmean(row["steps"] for row in subset),
            "median_steps_all_runs": statistics.median(row["steps"] for row in subset),
            "max_steps": max(row["steps"] for row in subset),
            "port_counts": dict(port_counts),
            "generic_prediction_checks": sum(
                row["generic_prediction_checks"] for row in subset
            ),
            "generic_matrix_counts": dict(matrix_counts),
            "generic_matrix_run_histogram": {
                str(key): value for key, value in sorted(run_histogram.items())
            },
            "max_generic_same_matrix_run": max(run_histogram, default=0),
        }
    return by_method


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
            "pairing_source_sha256": dependency_sha256(),
        },
    )
    try:
        full_checks = small_full_checks() if arguments.small_checks else None
        rows = []
        generation = []
        for n_index, (n, p, q) in enumerate(DATASETS[arguments.dataset]):
            assert p * q == n
            for query_index in range(QUERIES_PER_N):
                generator = random.Random(
                    derived_seed(arguments.dataset, n_index, query_index, "parameters")
                )
                a, a_cost = sample_unit_character(n, 1, generator)
                b, b_cost = sample_unit_character(n, -1, generator)
                assert math.gcd(a, n) == math.gcd(b, n) == 1
                assert jacobi(a, n) == 1 and jacobi(b, n) == -1
                qr_p = pow(a, (p - 1) // 2, p) == 1
                qr_q = pow(a, (q - 1) // 2, q) == 1
                query_record = {
                    "n": n,
                    "p_offline": p,
                    "q_offline": q,
                    "query_index": query_index,
                    "a": a,
                    "b": b,
                    "a_qr_mod_p_offline": qr_p,
                    "a_qr_mod_q_offline": qr_q,
                    "a_square_mod_n_offline": qr_p and qr_q,
                    "a_generation": a_cost,
                    "b_generation": b_cost,
                    "generation_factor_hits": (
                        a_cost["proper_factor_hits"] + b_cost["proper_factor_hits"]
                    ),
                }
                for factor in query_record["generation_factor_hits"]:
                    assert 1 < factor < n and n % factor == 0
                generation.append(query_record)
                cap = min(3 * n, 8192)
                for method in METHODS:
                    method_generator = random.Random(
                        derived_seed(
                            arguments.dataset,
                            n_index,
                            query_index,
                            "method:" + method,
                        )
                    )
                    constants, method_randomness = method_constants(
                        method, n, a, b, method_generator
                    )
                    row = walk(n, a, b, method, constants, cap)
                    row.update(
                        {
                            "n": n,
                            "p_offline": p,
                            "q_offline": q,
                            "query_index": query_index,
                            "a": a,
                            "b": b,
                            "a_square_mod_n_offline": qr_p and qr_q,
                            "method_randomness": method_randomness,
                        }
                    )
                    rows.append(row)
            print(
                json.dumps(
                    {
                        "event": "modulus_complete",
                        "dataset": arguments.dataset,
                        "n": n,
                        "runs": QUERIES_PER_N * len(METHODS),
                    }
                ),
                flush=True,
            )
            if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
                raise MemoryError("peak RSS exceeded 512 MiB")

        payload = {
            "status": "passed",
            "experiment": "F324_reflection_pairings",
            "family": "route:F29",
            "dataset": arguments.dataset,
            "seed": SEED,
            "queries_per_n": QUERIES_PER_N,
            "methods": METHODS,
            "source_sha256": source_sha256(),
            "pairing_source_sha256": dependency_sha256(),
            "public_parameter_scope": (
                "a and b use only exact uniform residues, gcd, and Jacobi signs. "
                "Generation factor hits are recorded and ignored only to finish "
                "the offline comparison pair. No factor selects a, b, C, or a path."
            ),
            "offline_factor_scope": (
                "p and q construct datasets, verify factors, and classify whether "
                "Jacobi-positive a is a square. They select no public action."
            ),
            "cap_rule": "min(3*N,8192) r calls",
            "small_full_checks": full_checks,
            "generation": generation,
            "summary": summarize(rows),
            "rows": rows,
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
                "queries_per_n",
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
            "experiment": "F324_reflection_pairings",
            "dataset": arguments.dataset,
            "seed": SEED,
            "source_sha256": source_sha256(),
            "pairing_source_sha256": dependency_sha256(),
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
        signal.alarm(0)


if __name__ == "__main__":
    main()
