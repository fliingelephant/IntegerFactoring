#!/usr/bin/env python3
"""F326: exact ranked Gauss-domain pairing and finite path experiments."""

import argparse
from bisect import bisect_left
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


ROOT = Path(__file__).resolve().parents[2]
F324_DIR = ROOT / "experiments" / "F324_reflection_pairings"
F324_OUTPUTS = (
    F324_DIR / "pilot_output.json",
    F324_DIR / "scale_output.json",
)
SEED = 32620260907
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024
PUBLIC_DATASETS = {
    "pilot": (209, 1333),
    "scale": (10807, 66013, 256027),
}
AUXILIARY_MATCHINGS = ("delete_adjacent", "rank_reflection")
RABIN_TRIALS = 32


def peak_rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    target = Path(path)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(target)


def derived_seed(*parts):
    raw = ":".join(str(part) for part in (SEED, *parts)).encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:8], "big")


def jacobi(a, n):
    """Binary Jacobi algorithm used by the public parameter interface."""
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


def jacobi_by_factorization(a, n):
    """Independent small-test oracle; trial factors are validation only."""
    remaining = n
    prime = 2
    result = 1
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            residue = pow(a % prime, (prime - 1) // 2, prime)
            legendre = -1 if residue == prime - 1 else residue
            result *= legendre**exponent
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        residue = pow(a % remaining, (remaining - 1) // 2, remaining)
        result *= -1 if residue == remaining - 1 else residue
    return result


class GaussPairing:
    """Uniform rank/select and arithmetic involution on the F326 domain."""

    def __init__(self, n, a):
        self.n = n
        self.a = a % n
        self.h = (n - 1) // 2
        self.counters = Counter()
        self.a_inverse = pow(self.a, -1, n)
        self.counters["setup_modular_inversions"] += 1
        self.L = self.Q(self.h)
        self.d = self.L + self.h + 1

    def rep(self, value):
        return (value + self.h) % self.n - self.h

    def floor_sum(self, count, modulus, slope, offset):
        """sum_{0<=j<count} floor((slope*j+offset)/modulus)."""
        self.counters["floor_sum_calls"] += 1
        answer = 0
        while True:
            self.counters["floor_sum_euclidean_iterations"] += 1
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

    def K(self, t):
        self.counters["K_calls"] += 1
        return self.floor_sum(t, self.n, self.a, self.a + self.h) - self.floor_sum(
            t, self.n, self.a, self.a
        )

    def Q(self, t):
        self.counters["Q_calls"] += 1
        return t - self.K(t)

    def in_domain(self, x):
        return 0 <= x <= self.h or (
            -self.h <= x < 0 and self.rep(self.a * x) < 0
        )

    def rank(self, x):
        self.counters["rank_calls"] += 1
        if x >= 0:
            return self.L + x
        return self.L - self.Q(-x)

    def select(self, index):
        self.counters["select_calls"] += 1
        if index >= self.L:
            return index - self.L
        target = self.L - index
        low, high = 1, self.h
        while low < high:
            self.counters["select_binary_iterations"] += 1
            middle = (low + high) // 2
            if self.Q(middle) >= target:
                high = middle
            else:
                low = middle + 1
        return -low

    def F(self, x):
        self.counters["F_calls"] += 1
        if x == 0:
            return 1, "swap_0_1"
        if x == 1:
            return 0, "swap_0_1"
        self.counters["F_gcd_calls"] += 1
        if math.gcd(x, self.n) > 1:
            return x, "fixed_nonunit"
        self.counters["F_modular_inversions"] += 1
        inverse = self.rep(pow(x, -1, self.n))
        if x > 0 and inverse > 0:
            return inverse, "first_inverse"
        if self.rep(self.a * x) < 0 and inverse < 0:
            return self.rep(self.a_inverse * inverse), "scaled_inverse"
        return -x, "negate"

    def decode(self, x, branch):
        self.counters["decode_calls"] += 1
        if branch == "fixed_nonunit":
            self.counters["decode_gcd_calls"] += 1
            divisor = math.gcd(x, self.n)
            assert 1 < divisor < self.n and self.n % divisor == 0
            return {"factor": divisor, "kind": "nonunit"}
        if branch == "first_inverse":
            self.counters["decode_gcd_calls"] += 1
            divisor = math.gcd(x - 1, self.n)
            assert 1 < divisor < self.n and self.n % divisor == 0
            return {"factor": divisor, "kind": "nontrivial_root_of_one"}
        assert branch == "scaled_inverse"
        self.counters["decode_modular_inversions"] += 1
        root = self.rep(pow(x, -1, self.n))
        assert root * root % self.n == self.a
        return {"root": root, "radicand": self.a, "kind": "square_root_of_a"}


def auxiliary(index, L, d, method):
    if method == "delete_adjacent":
        if index == L:
            return L
        compressed = index if index < L else index - 1
        partner = compressed ^ 1
        return partner if partner < L else partner + 1
    assert method == "rank_reflection"
    return (2 * L - index) % d


def brute_domain(n, a):
    started = time.perf_counter()
    h = (n - 1) // 2
    rep = lambda value: (value + h) % n - h
    values = [x for x in range(-h, 0) if rep(a * x) < 0]
    values.extend(range(h + 1))
    return values, time.perf_counter() - started


def validate_output(n, a, output, factors=None):
    if "factor" in output:
        divisor = output["factor"]
        assert 1 < divisor < n and n % divisor == 0
        if factors is not None:
            assert any(divisor % prime == 0 for prime in factors)
        return "factor"
    root = output["root"]
    assert root * root % n == a % n
    return "root"


def counter_delta(after, before):
    return {
        key: after.get(key, 0) - before.get(key, 0)
        for key in sorted(set(after) | set(before))
        if after.get(key, 0) != before.get(key, 0)
    }


def walk(n, a, method, cap, validation_domain, factors=None):
    pairing = GaussPairing(n, a)
    assert pairing.d == len(validation_domain)
    setup_counts = dict(pairing.counters)
    started = time.perf_counter()
    current = pairing.L
    seen = set()
    trace = []
    output = None
    endpoint_type = None
    fixed_coordinate = None
    censor_reason = None
    validation_rank_select_checks = 0

    for step in range(1, cap + 1):
        if current in seen:
            censor_reason = "repeated_rank"
            break
        seen.add(current)
        coordinate = pairing.select(current)
        assert validation_domain[current] == coordinate
        validation_rank_select_checks += 1
        image, branch = pairing.F(coordinate)
        assert pairing.in_domain(image)
        if image == coordinate:
            output = pairing.decode(coordinate, branch)
            endpoint_type = validate_output(n, a, output, factors)
            fixed_coordinate = coordinate
            if len(trace) < 80:
                trace.append(
                    {
                        "step": step,
                        "rank": current,
                        "coordinate": coordinate,
                        "F_branch": branch,
                        "terminal": True,
                    }
                )
            break
        image_rank = pairing.rank(image)
        position = bisect_left(validation_domain, image)
        assert position < len(validation_domain)
        assert validation_domain[position] == image and position == image_rank
        validation_rank_select_checks += 1
        next_rank = auxiliary(image_rank, pairing.L, pairing.d, method)
        if len(trace) < 80:
            trace.append(
                {
                    "step": step,
                    "rank": current,
                    "coordinate": coordinate,
                    "F_image": image,
                    "F_image_rank": image_rank,
                    "F_branch": branch,
                    "next_rank": next_rank,
                }
            )
        current = next_rank
    else:
        censor_reason = "step_cap"

    return {
        "method": method,
        "status": "completed" if output is not None else "censored",
        "censor_reason": censor_reason,
        "n": n,
        "a": a,
        "h": pairing.h,
        "K_h": pairing.h - pairing.L,
        "L": pairing.L,
        "d": pairing.d,
        "cap": cap,
        "F_calls": pairing.counters["F_calls"],
        "output": output,
        "endpoint_type": endpoint_type,
        "fixed_coordinate": fixed_coordinate,
        "setup_operation_counts": setup_counts,
        "path_operation_counts": counter_delta(pairing.counters, setup_counts),
        "validation_rank_select_checks": validation_rank_select_checks,
        "algorithm_walltime_seconds": time.perf_counter() - started,
        "trace_prefix": trace,
    }


def small_exact_checks(limit=101, a_limit=16):
    started = time.perf_counter()
    counts = Counter()
    path_steps = Counter()
    max_path = {method: None for method in AUXILIARY_MATCHINGS}
    for n in range(3, limit + 1, 2):
        for a in range(1, min(a_limit, n - 1) + 1):
            if math.gcd(a, n) != 1:
                continue
            h = (n - 1) // 2
            explicit_K = sum(
                ((a * y) % n) > h for y in range(1, h + 1)
            )
            independent_symbol = jacobi_by_factorization(a, n)
            assert jacobi(a, n) == independent_symbol
            assert (-1 if explicit_K % 2 else 1) == independent_symbol
            counts["all_residue_gauss_parity_checks"] += 1
            if independent_symbol != 1:
                continue

            domain, _ = brute_domain(n, a)
            pairing = GaussPairing(n, a)
            assert pairing.K(h) == explicit_K
            assert pairing.L == len(domain) - h - 1
            assert pairing.d == len(domain) and pairing.d % 2 == 1
            counts["positive_jacobi_instances"] += 1
            counts["domain_coordinates"] += len(domain)

            fixed = []
            for rank, coordinate in enumerate(domain):
                assert pairing.in_domain(coordinate)
                assert pairing.rank(coordinate) == rank
                assert pairing.select(rank) == coordinate
                image, branch = pairing.F(coordinate)
                assert pairing.in_domain(image)
                back, _ = pairing.F(image)
                assert back == coordinate
                counts["rank_select_checks"] += 1
                counts["F_squared_checks"] += 1
                if image == coordinate:
                    output = pairing.decode(coordinate, branch)
                    validate_output(n, a, output)
                    fixed.append(coordinate)
                    counts["fixed_decoder_" + output["kind"]] += 1

            for method in AUXILIARY_MATCHINGS:
                fixed_aux = []
                for index in range(pairing.d):
                    partner = auxiliary(index, pairing.L, pairing.d, method)
                    assert auxiliary(partner, pairing.L, pairing.d, method) == index
                    if partner == index:
                        fixed_aux.append(index)
                    counts["auxiliary_squared_checks"] += 1
                assert fixed_aux == [pairing.L]
                result = walk(n, a, method, pairing.d, domain)
                assert result["status"] == "completed"
                assert result["fixed_coordinate"] in fixed
                counts["completed_full_paths"] += 1
                path_steps[method] += result["F_calls"]
                if max_path[method] is None or result["F_calls"] > max_path[method][0]:
                    max_path[method] = (result["F_calls"], n, a)

    return {
        "scope": (
            "All odd N through 101 and all unit a<=16. Gauss parity uses an "
            "independent trial-factor Jacobi oracle. Full domain, rank/select, "
            "F, decoder, auxiliary, and path checks use every Jacobi-positive case."
        ),
        "limit": limit,
        "a_limit": a_limit,
        "counts": dict(counts),
        "path_F_calls": dict(path_steps),
        "max_path": {
            method: {
                "F_calls": value[0],
                "n": value[1],
                "a": value[2],
            }
            for method, value in max_path.items()
        },
        "walltime_seconds": time.perf_counter() - started,
    }


def load_f324():
    generation = {}
    references = {}
    factors = {}
    hashes = {}
    for path in F324_OUTPUTS:
        hashes[path.name] = sha256(path)
        data = json.loads(path.read_text())
        assert data["status"] == "passed"
        for row in data["generation"]:
            key = (row["n"], row["query_index"])
            generation[key] = row
            factors[row["n"]] = (row["p_offline"], row["q_offline"])
        for row in data["rows"]:
            if row["method"] in ("adjacent", "negation"):
                key = (row["n"], row["query_index"], row["method"])
                references[key] = {
                    name: row[name]
                    for name in (
                        "n",
                        "a",
                        "b",
                        "query_index",
                        "method",
                        "status",
                        "censor_reason",
                        "cap",
                        "steps",
                        "result",
                        "endpoint_type",
                    )
                }
    return generation, references, factors, hashes


def public_run(dataset, include_small_checks):
    started = time.perf_counter()
    generation, references, factors, hashes = load_f324()
    results = []
    brute_seconds = 0.0
    for n in PUBLIC_DATASETS[dataset]:
        for query_index in range(8):
            query = generation[(n, query_index)]
            a, b = query["a"], query["b"]
            assert math.gcd(a, n) == 1 and jacobi(a, n) == 1
            domain, validation_seconds = brute_domain(n, a)
            brute_seconds += validation_seconds
            pairing = GaussPairing(n, a)
            cap = min(pairing.d, 8192)
            paths = {
                method: walk(n, a, method, cap, domain, factors[n])
                for method in AUXILIARY_MATCHINGS
            }
            refs = {}
            for method in ("adjacent", "negation"):
                reference = references[(n, query_index, method)]
                assert reference["a"] == a and reference["b"] == b
                refs[method] = reference
            results.append(
                {
                    "query": query,
                    "ranked_domain": {
                        "h": pairing.h,
                        "K_h": pairing.h - pairing.L,
                        "L": pairing.L,
                        "d": pairing.d,
                        "cap": cap,
                    },
                    "validation_brute_domain_seconds": validation_seconds,
                    "paths": paths,
                    "F322_reference_from_F324": refs,
                }
            )
            print(
                json.dumps(
                    {
                        "event": "public_query_complete",
                        "dataset": dataset,
                        "n": n,
                        "query_index": query_index,
                        "a": a,
                        "direct": {
                            method: {
                                "status": paths[method]["status"],
                                "F_calls": paths[method]["F_calls"],
                                "endpoint": paths[method]["endpoint_type"],
                            }
                            for method in AUXILIARY_MATCHINGS
                        },
                    }
                ),
                flush=True,
            )
            if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
                raise MemoryError("peak RSS exceeded 512 MiB")

    summary = {}
    for method in AUXILIARY_MATCHINGS:
        rows = [result["paths"][method] for result in results]
        completed = [row for row in rows if row["status"] == "completed"]
        summary[method] = {
            "runs": len(rows),
            "completed": len(completed),
            "censored": len(rows) - len(completed),
            "censor_reasons": dict(
                Counter(row["censor_reason"] for row in rows if row["censor_reason"])
            ),
            "factor_endpoints": sum(row["endpoint_type"] == "factor" for row in completed),
            "root_endpoints": sum(row["endpoint_type"] == "root" for row in completed),
            "total_F_calls": sum(row["F_calls"] for row in rows),
            "mean_F_calls": statistics.fmean(row["F_calls"] for row in rows),
            "max_F_calls": max(row["F_calls"] for row in rows),
            "total_floor_sum_calls": sum(
                row["setup_operation_counts"].get("floor_sum_calls", 0)
                + row["path_operation_counts"].get("floor_sum_calls", 0)
                for row in rows
            ),
            "total_select_binary_iterations": sum(
                row["path_operation_counts"].get("select_binary_iterations", 0)
                for row in rows
            ),
            "algorithm_walltime_seconds": sum(
                row["algorithm_walltime_seconds"] for row in rows
            ),
        }
    for method in ("adjacent", "negation"):
        rows = [result["F322_reference_from_F324"][method] for result in results]
        summary["F322_" + method] = {
            "runs": len(rows),
            "completed": sum(row["status"] == "completed" for row in rows),
            "censored": sum(row["status"] != "completed" for row in rows),
            "total_r_calls": sum(row["steps"] for row in rows),
            "factor_endpoints": sum(row["endpoint_type"] == "factor" for row in rows),
            "root_endpoints": sum(row["endpoint_type"] == "root" for row in rows),
        }

    return {
        "status": "passed",
        "experiment": "F326_direct_gauss_pairing",
        "mode": "public",
        "dataset": dataset,
        "seed": SEED,
        "public_moduli": PUBLIC_DATASETS[dataset],
        "queries_per_modulus": 8,
        "auxiliary_matchings": AUXILIARY_MATCHINGS,
        "cap_rule": "min(d,8192) F calls",
        "parameter_scope": (
            "Exact F324 public pairs are reused. Only N and Jacobi-positive a "
            "enter the direct Gauss pairing. b appears solely in the retained "
            "F322 reference. Offline p,q label and verify outputs only."
        ),
        "validation_scope": (
            "Explicit domain construction and lookup validate rank/select calls. "
            "Their time is separate and is not charged as algorithm work."
        ),
        "small_exact_checks": small_exact_checks() if include_small_checks else None,
        "summary": summary,
        "validation_brute_domain_seconds": brute_seconds,
        "results": results,
        "f324_output_hashes": hashes,
        "source_sha256": sha256(Path(__file__)),
        "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
        "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
        "memory_limit_bytes": MEMORY_LIMIT_BYTES,
        "walltime_seconds": time.perf_counter() - started,
        "peak_rss_bytes": peak_rss_bytes(),
    }


def rabin_run(dataset):
    started = time.perf_counter()
    _, _, factors, hashes = load_f324()
    trials = []
    brute_seconds = 0.0
    for n in PUBLIC_DATASETS[dataset]:
        for trial_index in range(RABIN_TRIALS):
            hidden_seed = derived_seed("rabin", dataset, n, trial_index, "hidden")
            coin_seed = derived_seed("rabin", dataset, n, trial_index, "solver_coins")
            hidden_generator = random.Random(hidden_seed)
            coin_generator = random.Random(coin_seed)
            draws = 0
            generation_factor = None
            hidden_root = None
            while hidden_root is None and generation_factor is None:
                candidate = hidden_generator.randrange(1, n)
                draws += 1
                divisor = math.gcd(candidate, n)
                if divisor == 1:
                    hidden_root = candidate
                else:
                    assert divisor < n
                    generation_factor = divisor

            method = AUXILIARY_MATCHINGS[coin_generator.randrange(2)]
            if generation_factor is not None:
                assert 1 < generation_factor < n and n % generation_factor == 0
                record = {
                    "n": n,
                    "trial_index": trial_index,
                    "hidden_seed": hidden_seed,
                    "solver_coin_seed": coin_seed,
                    "hidden_draws": draws,
                    "hidden_root": None,
                    "auxiliary_matching": method,
                    "a": None,
                    "path": None,
                    "status": "factor_from_hidden_root_generation",
                    "accepted_factor": generation_factor,
                    "root_postprocessing": None,
                    "offline_factors": factors[n],
                }
            else:
                a = hidden_root * hidden_root % n
                assert math.gcd(a, n) == 1 and jacobi(a, n) == 1
                domain, validation_seconds = brute_domain(n, a)
                brute_seconds += validation_seconds
                pairing = GaussPairing(n, a)
                cap = min(pairing.d, 8192)
                path = walk(n, a, method, cap, domain, factors[n])
                accepted_factor = None
                root_postprocessing = None
                status = "path_censored"
                if path["status"] == "completed" and path["endpoint_type"] == "factor":
                    accepted_factor = path["output"]["factor"]
                    status = "direct_factor"
                elif path["status"] == "completed":
                    returned_root = path["output"]["root"]
                    assert returned_root * returned_root % n == a
                    minus_gcd = math.gcd(returned_root - hidden_root, n)
                    plus_gcd = math.gcd(returned_root + hidden_root, n)
                    candidates = [
                        divisor
                        for divisor in (minus_gcd, plus_gcd)
                        if 1 < divisor < n
                    ]
                    if candidates:
                        accepted_factor = candidates[0]
                        status = "factor_from_root_difference"
                    else:
                        status = "root_without_factor"
                    root_postprocessing = {
                        "returned_root": returned_root,
                        "minus_gcd": minus_gcd,
                        "plus_gcd": plus_gcd,
                        "produced_factor": bool(candidates),
                    }
                if accepted_factor is not None:
                    assert 1 < accepted_factor < n and n % accepted_factor == 0
                record = {
                    "n": n,
                    "trial_index": trial_index,
                    "hidden_seed": hidden_seed,
                    "solver_coin_seed": coin_seed,
                    "hidden_draws": draws,
                    "hidden_root": hidden_root,
                    "auxiliary_matching": method,
                    "a": a,
                    "path": path,
                    "status": status,
                    "accepted_factor": accepted_factor,
                    "root_postprocessing": root_postprocessing,
                    "offline_factors": factors[n],
                    "validation_brute_domain_seconds": validation_seconds,
                }
            trials.append(record)
            print(
                json.dumps(
                    {
                        "event": "rabin_trial_complete",
                        "dataset": dataset,
                        "n": n,
                        "trial_index": trial_index,
                        "method": method,
                        "status": record["status"],
                        "F_calls": record["path"]["F_calls"] if record["path"] else 0,
                    }
                ),
                flush=True,
            )
            if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
                raise MemoryError("peak RSS exceeded 512 MiB")

    by_n = {}
    for n in PUBLIC_DATASETS[dataset]:
        rows = [row for row in trials if row["n"] == n]
        solver_rows = [row for row in rows if row["path"] is not None]
        by_n[str(n)] = {
            "trials": len(rows),
            "generation_factor_successes": sum(
                row["status"] == "factor_from_hidden_root_generation" for row in rows
            ),
            "solver_calls": len(solver_rows),
            "completed_solver_paths": sum(
                row["path"]["status"] == "completed" for row in solver_rows
            ),
            "censored_solver_paths": sum(
                row["path"]["status"] != "completed" for row in solver_rows
            ),
            "direct_factor_successes": sum(row["status"] == "direct_factor" for row in rows),
            "root_difference_successes": sum(
                row["status"] == "factor_from_root_difference" for row in rows
            ),
            "root_without_factor": sum(
                row["status"] == "root_without_factor" for row in rows
            ),
            "total_factor_successes": sum(row["accepted_factor"] is not None for row in rows),
            "total_F_calls": sum(row["path"]["F_calls"] for row in solver_rows),
            "matching_coin_counts": dict(
                Counter(row["auxiliary_matching"] for row in rows)
            ),
        }

    return {
        "status": "passed",
        "experiment": "F326_direct_gauss_pairing",
        "mode": "rabin",
        "dataset": dataset,
        "seed": SEED,
        "public_moduli": PUBLIC_DATASETS[dataset],
        "trials_per_modulus": RABIN_TRIALS,
        "cap_rule": "min(d,8192) F calls",
        "independence_scope": (
            "The hidden root and the auxiliary-matching coin use independent "
            "derived seeds. The path solver receives only N, a, its independent "
            "matching choice, and the public cap. The hidden root is used only "
            "after a verified square root returns."
        ),
        "generation_scope": (
            "The hidden candidate is uniform on 1 through N-1. A proper gcd "
            "found before obtaining a unit is an immediate Las Vegas factor."
        ),
        "validation_scope": (
            "Offline factors only verify outputs. Explicit domains validate "
            "rank/select and are excluded from algorithm operation counts."
        ),
        "summary_by_n": by_n,
        "trials": trials,
        "validation_brute_domain_seconds": brute_seconds,
        "f324_output_hashes": hashes,
        "source_sha256": sha256(Path(__file__)),
        "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
        "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
        "memory_limit_bytes": MEMORY_LIMIT_BYTES,
        "walltime_seconds": time.perf_counter() - started,
        "peak_rss_bytes": peak_rss_bytes(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("public", "rabin"), required=True)
    parser.add_argument("--dataset", choices=tuple(PUBLIC_DATASETS), required=True)
    parser.add_argument("--small-checks", action="store_true")
    parser.add_argument("--output", required=True)
    parser.add_argument("--status", required=True)
    arguments = parser.parse_args()
    started = time.perf_counter()

    def timeout_handler(_signal_number, _frame):
        raise TimeoutError("internal 28-second alarm fired")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(INTERNAL_TIMEOUT_SECONDS)
    running = {
        "status": "running",
        "experiment": "F326_direct_gauss_pairing",
        "mode": arguments.mode,
        "dataset": arguments.dataset,
        "seed": SEED,
        "source_sha256": sha256(Path(__file__)),
    }
    write_json(arguments.status, running)
    try:
        if arguments.mode == "public":
            payload = public_run(arguments.dataset, arguments.small_checks)
        else:
            assert not arguments.small_checks
            payload = rabin_run(arguments.dataset)
        payload["walltime_seconds"] = time.perf_counter() - started
        payload["peak_rss_bytes"] = peak_rss_bytes()
        if payload["peak_rss_bytes"] > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 512 MiB")
        write_json(arguments.output, payload)
        status = {
            key: payload[key]
            for key in (
                "status",
                "experiment",
                "mode",
                "dataset",
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
        write_json(arguments.status, status)
        print(json.dumps({"event": "passed", **status}), flush=True)
    except BaseException as exception:
        failure = {
            **running,
            "status": "failed",
            "exception_type": type(exception).__name__,
            "exception": str(exception),
            "traceback": traceback.format_exc(),
            "walltime_seconds": time.perf_counter() - started,
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
