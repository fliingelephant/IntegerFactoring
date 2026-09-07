#!/usr/bin/env python3
"""F329: bounded random-center and lazy-matching arithmetic paths."""

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import random
import resource
import signal
import sys
import time
import traceback


ROOT = Path(__file__).resolve().parents[2]
F326_DIR = ROOT / "experiments" / "F326_direct_gauss_pairing"
F326_SOURCE = F326_DIR / "direct_gauss_pairing.py"
F326_SOURCE_SHA256 = "7829cc45822021c64c42842a2c938b15c52df85e30ae694efcdd4171c5012f73"
F328_INPUT = ROOT / "experiments" / "F328_capped_rabin_paths" / "moduli.json"
F328_INPUT_SHA256 = "acf09b285c57c39cfcb93d3cd77addce909498e224955fd0ec9d2e4d86ee0428"
sys.path.insert(0, str(F326_DIR))
from direct_gauss_pairing import GaussPairing, brute_domain, jacobi  # noqa: E402


SEED = 32920260907
METHODS = ("rank_L_reflection", "uniform_center_reflection", "lazy_uniform_matching")
SCREENS = ("baseline", "static_edge")
PILOT_CAPS = (4, 16, 64, 256)
SCALE_CAPS = (16, 64, 256, 1024)
ALL_CAPS = tuple(sorted(set(PILOT_CAPS + SCALE_CAPS)))
SQUARES_PER_MODULUS = 16
RANDOM_REPLICATES = 4
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024
PILOT_MODULI = (
    {"modulus_id": "pilot_209", "n": 209, "p_offline": 11, "q_offline": 19},
    {"modulus_id": "pilot_1333", "n": 1333, "p_offline": 31, "q_offline": 43},
    {"modulus_id": "pilot_10807", "n": 10807, "p_offline": 101, "q_offline": 107},
)
COST_KEYS = (
    "F_calls",
    "floor_sum_calls",
    "floor_sum_euclidean_iterations",
    "pairing_gcd_calls",
    "static_screen_gcd_calls",
    "root_decode_gcd_calls",
    "generation_gcd_calls",
    "total_gcd_calls",
    "modular_inversion_calls",
    "matching_bounded_draw_calls",
    "matching_bit_trials",
    "matching_rejections",
    "matching_fair_bits",
    "generation_fair_bits",
    "total_fair_bits",
    "charged_walltime_seconds",
)


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
    return int.from_bytes(hashlib.sha256(raw).digest()[:16], "big")


def fraction_record(value):
    value = Fraction(value)
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": str(value),
    }


def bounded_sample(generator, bound, counters):
    """Uniformly sample [0,bound) by fair-bit rejection from a power of two."""
    assert bound >= 1
    width = (bound - 1).bit_length()
    counters["bounded_draw_calls"] += 1
    while True:
        counters["bit_trials"] += 1
        counters["fair_bits"] += width
        value = generator.getrandbits(width)
        if value < bound:
            return value
        counters["rejections"] += 1


class SparsePool:
    """Sparse forward/inverse Fisher-Yates pool with identity defaults."""

    def __init__(self, size, generator, random_counters):
        self.size = size
        self.generator = generator
        self.random_counters = random_counters
        self.forward = {}
        self.inverse = {}
        self.counters = Counter()
        self.max_map_entries = 0

    def _forward(self, position):
        self.counters["map_gets"] += 1
        return self.forward.get(position, position)

    def _inverse(self, label):
        self.counters["map_gets"] += 1
        return self.inverse.get(label, label)

    def _set_forward(self, position, label):
        self.counters["map_sets"] += 1
        if position == label:
            self.forward.pop(position, None)
        else:
            self.forward[position] = label

    def _set_inverse(self, label, position):
        self.counters["map_sets"] += 1
        if label == position:
            self.inverse.pop(label, None)
        else:
            self.inverse[label] = position

    def _update_peak(self):
        self.max_map_entries = max(
            self.max_map_entries, len(self.forward) + len(self.inverse)
        )

    def remove(self, label):
        position = self._inverse(label)
        assert position < self.size and self._forward(position) == label
        last_position = self.size - 1
        last_label = self._forward(last_position)
        self._set_forward(position, last_label)
        self._set_forward(last_position, label)
        self._set_inverse(last_label, position)
        self._set_inverse(label, last_position)
        self.size -= 1
        self.counters["removals"] += 1
        self._update_peak()

    def pop_uniform(self):
        assert self.size >= 1
        position = bounded_sample(self.generator, self.size, self.random_counters)
        label = self._forward(position)
        self.remove(label)
        self.counters["uniform_pops"] += 1
        return label

    def snapshot(self):
        return {
            "active_size": self.size,
            "forward_entries": len(self.forward),
            "inverse_entries": len(self.inverse),
            "map_entries": len(self.forward) + len(self.inverse),
            "maximum_map_entries": self.max_map_entries,
            "operation_counts": dict(self.counters),
        }


def pairing_counts(counter):
    raw = dict(counter)
    return {
        "F_calls": raw.get("F_calls", 0),
        "floor_sum_calls": raw.get("floor_sum_calls", 0),
        "floor_sum_euclidean_iterations": raw.get(
            "floor_sum_euclidean_iterations", 0
        ),
        "pairing_gcd_calls": raw.get("F_gcd_calls", 0)
        + raw.get("decode_gcd_calls", 0),
        "modular_inversion_calls": raw.get("setup_modular_inversions", 0)
        + raw.get("F_modular_inversions", 0)
        + raw.get("decode_modular_inversions", 0),
        "rank_calls": raw.get("rank_calls", 0),
        "select_calls": raw.get("select_calls", 0),
        "select_binary_iterations": raw.get("select_binary_iterations", 0),
        "raw_pairing_counters": raw,
    }


def state_snapshot(
    pairing,
    random_counters,
    pool,
    base_seconds,
    static_screen_gcd_calls=0,
    static_screen_seconds=0.0,
    current_rank=None,
):
    return {
        "pairing_counts": pairing_counts(pairing.counters),
        "matching_random_counts": dict(random_counters),
        "pool": pool.snapshot() if pool else None,
        "base_walltime_seconds": base_seconds,
        "static_screen_gcd_calls": static_screen_gcd_calls,
        "static_screen_walltime_seconds": static_screen_seconds,
        "current_rank_after_step": current_rank,
    }


def static_edge_screen(n, x, y, screen_counters):
    """Evaluate the six distinct symmetric gcd arguments for the whole F edge."""
    arguments = (
        ("x_minus_one", x - 1),
        ("x_plus_one", x + 1),
        ("y_minus_one", y - 1),
        ("y_plus_one", y + 1),
        ("edge_difference", x - y),
        ("edge_sum", x + y),
    )
    hits = []
    for name, value in arguments:
        divisor = math.gcd(value, n)
        screen_counters["gcd_calls"] += 1
        if 1 < divisor < n:
            hits.append({"test": name, "divisor": divisor})
    unique_divisors = sorted({hit["divisor"] for hit in hits})
    return {"hits": hits, "proper_divisors": unique_divisors}


def arithmetic_trajectory(n, a, method, cap, matching_seed):
    """Run one public trajectory and derive paired baseline/static-screen views."""
    assert n > 1 and n % 2 == 1
    assert 1 <= a < n and jacobi(a, n) == 1
    assert method in METHODS and cap >= 1
    started = time.perf_counter()
    base_started = time.perf_counter()
    pairing = GaussPairing(n, a)
    base_seconds = time.perf_counter() - base_started
    assert pairing.d % 2 == 1
    random_counters = Counter()
    screen_counters = Counter()
    screen_seconds = 0.0
    generator = random.Random(matching_seed)
    pool = None
    center = None

    base_started = time.perf_counter()
    if method == "rank_L_reflection":
        center = pairing.L
        current = center
    elif method == "uniform_center_reflection":
        center = bounded_sample(generator, pairing.d, random_counters)
        current = center
    else:
        pool = SparsePool(pairing.d, generator, random_counters)
        current = pool.pop_uniform()
    start_rank = current
    base_seconds += time.perf_counter() - base_started

    checkpoints = tuple(checkpoint for checkpoint in ALL_CAPS if checkpoint <= cap)
    baseline_snapshots = {}
    static_snapshots = {}
    baseline_endpoint = None
    static_endpoint = None

    for step in range(1, cap + 1):
        base_started = time.perf_counter()
        coordinate = pairing.select(current)
        image, branch = pairing.F(coordinate)
        base_seconds += time.perf_counter() - base_started

        screen_result = None
        if static_endpoint is None:
            screen_started = time.perf_counter()
            screen_result = static_edge_screen(n, coordinate, image, screen_counters)
            screen_seconds += time.perf_counter() - screen_started

        if image == coordinate:
            base_started = time.perf_counter()
            decoded = pairing.decode(coordinate, branch)
            base_seconds += time.perf_counter() - base_started
            if "factor" in decoded:
                divisor = decoded["factor"]
                if not (1 < divisor < n and n % divisor == 0):
                    raise ArithmeticError("fixed decoder returned an invalid factor")
                endpoint_type = "factor"
            else:
                root = decoded["root"]
                if root * root % n != a:
                    raise ArithmeticError("fixed decoder returned an invalid root")
                endpoint_type = "root"
            endpoint_core = {
                "step": step,
                "rank": current,
                "coordinate": coordinate,
                "first_hit_type": "fixed_" + branch,
                "endpoint_type": endpoint_type,
                "decoder_output": decoded,
                "verified_exactly": True,
            }
            baseline_endpoint = {
                **endpoint_core,
                "screen_factors": [],
                "state": state_snapshot(
                    pairing,
                    random_counters,
                    pool,
                    base_seconds,
                    current_rank=None,
                ),
            }
            if static_endpoint is None:
                static_endpoint = {
                    **endpoint_core,
                    "screen_factors": screen_result["proper_divisors"],
                    "screen_hits": screen_result["hits"],
                    "state": state_snapshot(
                        pairing,
                        random_counters,
                        pool,
                        base_seconds,
                        screen_counters["gcd_calls"],
                        screen_seconds,
                        current_rank=None,
                    ),
                }
        else:
            if static_endpoint is None and screen_result["proper_divisors"]:
                static_endpoint = {
                    "step": step,
                    "rank": current,
                    "coordinate": coordinate,
                    "image_coordinate": image,
                    "first_hit_type": "screened_nonfixed_edge",
                    "endpoint_type": "factor",
                    "decoder_output": {
                        "factor": screen_result["proper_divisors"][0],
                        "kind": "static_edge_screen",
                    },
                    "screen_factors": screen_result["proper_divisors"],
                    "screen_hits": screen_result["hits"],
                    "verified_exactly": True,
                    "state": state_snapshot(
                        pairing,
                        random_counters,
                        pool,
                        base_seconds,
                        screen_counters["gcd_calls"],
                        screen_seconds,
                        current_rank=None,
                    ),
                }

            # A standalone T-call censor stops before exposing the next
            # auxiliary edge. Snapshot every requested prefix at that boundary.
            if step in checkpoints:
                baseline_snapshots[step] = state_snapshot(
                    pairing,
                    random_counters,
                    pool,
                    base_seconds,
                    current_rank=current,
                )
                if static_endpoint is None:
                    static_snapshots[step] = state_snapshot(
                        pairing,
                        random_counters,
                        pool,
                        base_seconds,
                        screen_counters["gcd_calls"],
                        screen_seconds,
                        current_rank=current,
                    )

            if step < cap:
                base_started = time.perf_counter()
                image_rank = pairing.rank(image)
                if method in ("rank_L_reflection", "uniform_center_reflection"):
                    current = (2 * center - image_rank) % pairing.d
                else:
                    pool.remove(image_rank)
                    current = pool.pop_uniform()
                base_seconds += time.perf_counter() - base_started
        if baseline_endpoint is not None:
            break

    endpoints = {"baseline": baseline_endpoint, "static_edge": static_endpoint}
    snapshot_sets = {"baseline": baseline_snapshots, "static_edge": static_snapshots}
    views = {screen: {} for screen in SCREENS}
    for screen in SCREENS:
        endpoint = endpoints[screen]
        for checkpoint in checkpoints:
            if endpoint is not None and endpoint["step"] <= checkpoint:
                state = endpoint["state"]
                public_endpoint = {
                    key: value for key, value in endpoint.items() if key != "state"
                }
                views[screen][str(checkpoint)] = {
                    "status": "completed",
                    "endpoint": public_endpoint,
                    "state": state,
                }
            else:
                views[screen][str(checkpoint)] = {
                    "status": "censored_at_cap",
                    "endpoint": None,
                    "state": snapshot_sets[screen][checkpoint],
                }

    return {
        "solver_interface": ["n", "a", "method", "cap", "matching_seed"],
        "n": n,
        "a": a,
        "method": method,
        "cap": cap,
        "matching_seed": matching_seed,
        "center": center,
        "start_rank": start_rank,
        "h": pairing.h,
        "L": pairing.L,
        "d": pairing.d,
        "views": views,
        "baseline_terminal_step": baseline_endpoint["step"] if baseline_endpoint else None,
        "static_terminal_step": static_endpoint["step"] if static_endpoint else None,
        "maximum_pool_map_entries": pool.max_map_entries if pool else 0,
        "process_walltime_seconds": time.perf_counter() - started,
        "implementation_scope": (
            "One current rank is retained. Prefix snapshots are fixed-size output. "
            "The lazy pool uses sparse forward/inverse Python dictionaries and "
            "samples active positions directly without depletion rejection."
        ),
    }


def postprocess_view(view, hidden_root, n, generation_draw, root_cache):
    state = view["state"]
    counts = state["pairing_counts"]
    random_counts = state["matching_random_counts"]
    endpoint = view["endpoint"]
    root_decode = None
    root_decode_seconds = 0.0
    root_decode_gcd_calls = 0
    valid_root = False
    root_factor = False
    root_decoding_failure = False
    direct_factor = False
    screen_factor = False

    if endpoint is not None:
        screen_factor = bool(endpoint.get("screen_factors"))
        if endpoint["endpoint_type"] == "root":
            valid_root = True
            root = endpoint["decoder_output"]["root"]
            if root * root % n != endpoint["decoder_output"]["radicand"]:
                raise ArithmeticError("outer validation rejected a root")
            cache_key = (n, hidden_root, root)
            if cache_key not in root_cache:
                decode_started = time.perf_counter()
                divisor = math.gcd(root - hidden_root, n)
                root_cache[cache_key] = {
                    "divisor": divisor,
                    "walltime_seconds": time.perf_counter() - decode_started,
                }
            divisor = root_cache[cache_key]["divisor"]
            root_decode_seconds = root_cache[cache_key]["walltime_seconds"]
            root_decode_gcd_calls = 1
            root_factor = 1 < divisor < n
            root_decoding_failure = not root_factor
            root_decode = {
                "hidden_root_used_only_outside_solver": True,
                "difference_gcd": divisor,
                "proper_factor": divisor if root_factor else None,
                "success": root_factor,
            }
        else:
            divisor = endpoint["decoder_output"]["factor"]
            if not (1 < divisor < n and n % divisor == 0):
                raise ArithmeticError("outer validation rejected a factor")
            direct_factor = endpoint["first_hit_type"].startswith("fixed_")
            screen_factor = screen_factor or endpoint["first_hit_type"] == (
                "screened_nonfixed_edge"
            )

    factor_success = direct_factor or screen_factor or root_factor
    matching_bits = random_counts.get("fair_bits", 0)
    generation_bits = generation_draw["sampling"]["fair_bits"]
    costs = {
        "F_calls": counts["F_calls"],
        "floor_sum_calls": counts["floor_sum_calls"],
        "floor_sum_euclidean_iterations": counts[
            "floor_sum_euclidean_iterations"
        ],
        "pairing_gcd_calls": counts["pairing_gcd_calls"],
        "static_screen_gcd_calls": state["static_screen_gcd_calls"],
        "root_decode_gcd_calls": root_decode_gcd_calls,
        "generation_gcd_calls": 1,
        "total_gcd_calls": counts["pairing_gcd_calls"]
        + state["static_screen_gcd_calls"]
        + root_decode_gcd_calls
        + 1,
        "modular_inversion_calls": counts["modular_inversion_calls"],
        "matching_bounded_draw_calls": random_counts.get("bounded_draw_calls", 0),
        "matching_bit_trials": random_counts.get("bit_trials", 0),
        "matching_rejections": random_counts.get("rejections", 0),
        "matching_fair_bits": matching_bits,
        "generation_fair_bits": generation_bits,
        "total_fair_bits": matching_bits + generation_bits,
        "charged_walltime_seconds": state["base_walltime_seconds"]
        + state["static_screen_walltime_seconds"]
        + generation_draw["walltime_seconds"]
        + root_decode_seconds,
    }
    return {
        **view,
        "factor_success": factor_success,
        "direct_factor": direct_factor,
        "screen_factor": screen_factor,
        "valid_root": valid_root,
        "root_factor": root_factor,
        "root_decoding_failure": root_decoding_failure,
        "root_postprocessing": root_decode,
        "costs": costs,
    }


def generate_square_queries(dataset, modulus_id, n, count=SQUARES_PER_MODULUS):
    hidden_seed = derived_seed("hidden_roots", dataset, modulus_id)
    generator = random.Random(hidden_seed)
    random_counters = Counter()
    queries = []
    generation_factors = []
    draw_index = 0
    while len(queries) < count:
        before = dict(random_counters)
        draw_started = time.perf_counter()
        candidate = bounded_sample(generator, n - 1, random_counters) + 1
        divisor = math.gcd(candidate, n)
        elapsed = time.perf_counter() - draw_started
        sampling = {
            key: random_counters.get(key, 0) - before.get(key, 0)
            for key in ("bounded_draw_calls", "bit_trials", "rejections", "fair_bits")
        }
        draw = {
            "draw_index": draw_index,
            "candidate": candidate,
            "sampling": sampling,
            "gcd_calls": 1,
            "walltime_seconds": elapsed,
        }
        draw_index += 1
        if divisor != 1:
            if not (1 < divisor < n and n % divisor == 0):
                raise ArithmeticError("outer generation gcd was not a proper factor")
            generation_factors.append(
                {
                    **draw,
                    "factor": divisor,
                    "before_square_index": len(queries),
                }
            )
            continue
        a = candidate * candidate % n
        if jacobi(a, n) != 1:
            raise ArithmeticError("accepted unit square failed its Jacobi check")
        queries.append(
            {
                "query_index": len(queries),
                "hidden_root": candidate,
                "a": a,
                "generation_draw": draw,
                "preceding_generation_factor_indices": [
                    event["draw_index"]
                    for event in generation_factors
                    if event["before_square_index"] == len(queries)
                ],
            }
        )
    return {
        "hidden_seed": hidden_seed,
        "queries": queries,
        "generation_factors": generation_factors,
        "total_outer_draws": draw_index,
        "random_counts": dict(random_counters),
        "scope": (
            "Sampling continues after retaining an immediate generation factor "
            "only to obtain the fixed requested number of conditional unit-square "
            "inputs. Generation-factor draws remain separate outer successes."
        ),
    }


def screen_absorbing_diagnostics(n, a, factors):
    domain, enumeration_seconds = brute_domain(n, a)
    pairing = GaussPairing(n, a)
    assert pairing.d == len(domain)
    fixed = set()
    screened = set()
    branch_counts = Counter()
    seen_edges = set()
    for rank, coordinate in enumerate(domain):
        image, branch = pairing.F(coordinate)
        image_rank = pairing.rank(image)
        if image == coordinate:
            fixed.add(rank)
            branch_counts[branch] += 1
            continue
        edge = tuple(sorted((rank, image_rank)))
        if edge in seen_edges:
            continue
        seen_edges.add(edge)
        result = static_edge_screen(n, coordinate, image, Counter())
        if result["proper_divisors"]:
            screened.update(edge)
    q = len(fixed)
    b = len(fixed | screened)
    distinct_prime_count = len(set(factors))
    q_unit = branch_counts["first_inverse"] + branch_counts["scaled_inverse"]
    assert q_unit == 2**distinct_prime_count - 1
    assert q % 2 == b % 2 == 1
    return {
        "status": "exact",
        "d": pairing.d,
        "q": q,
        "b": b,
        "fixed_branch_counts": {
            key: branch_counts[key]
            for key in ("fixed_nonunit", "first_inverse", "scaled_inverse")
        },
        "q_unit": q_unit,
        "expected_q_unit": 2**distinct_prime_count - 1,
        "screened_nonfixed_ranks": len(screened),
        "domain_enumeration_seconds": enumeration_seconds,
        "scope": "Offline full-domain diagnostic; not supplied to any solver.",
    }


def survival_fraction(d, absorbing_size, cap):
    survival = Fraction(1)
    for failure_index in range(cap):
        numerator = d - absorbing_size - 2 * failure_index
        denominator = d - 2 * failure_index
        if numerator <= 0:
            return Fraction(0)
        survival *= Fraction(numerator, denominator)
    return survival


def matching_recipes(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for offset in range(1, len(values)):
        partner = values[offset]
        remaining = values[1:offset] + values[offset + 1 :]
        for rest in matching_recipes(remaining):
            yield ((first, partner),) + rest


def generic_matching_controls():
    scenarios = []
    total_paths = 0
    for d in (1, 3, 5, 7, 9):
        for q in range(1, d + 1, 2):
            involution = list(range(d))
            for left in range(q, d, 2):
                involution[left] = left + 1
                involution[left + 1] = left
            nonfixed_pairs = [(left, left + 1) for left in range(q, d, 2)]
            for screened_pair_count in range(len(nonfixed_pairs) + 1):
                absorbing = set(range(q))
                for edge in nonfixed_pairs[:screened_pair_count]:
                    absorbing.update(edge)
                b = len(absorbing)
                hitting_times = []
                terminal_counts = Counter()
                matchings_per_start = None
                for start in range(d):
                    recipes = tuple(matching_recipes(v for v in range(d) if v != start))
                    if matchings_per_start is None:
                        matchings_per_start = len(recipes)
                    assert len(recipes) == matchings_per_start
                    for recipe in recipes:
                        auxiliary = {start: start}
                        for left, right in recipe:
                            auxiliary[left] = right
                            auxiliary[right] = left
                        current = start
                        calls = 0
                        while True:
                            calls += 1
                            if current in absorbing:
                                hitting_times.append(calls)
                                terminal_counts[current] += 1
                                break
                            current = auxiliary[involution[current]]
                            assert calls <= d
                total = len(hitting_times)
                total_paths += total
                cap_rows = []
                for cap in range(1, (d - b) // 2 + 2):
                    observed_survival = Fraction(
                        sum(hitting_time > cap for hitting_time in hitting_times), total
                    )
                    observed_mean = Fraction(
                        sum(min(hitting_time, cap) for hitting_time in hitting_times), total
                    )
                    expected_survival = survival_fraction(d, b, cap)
                    expected_mean = sum(
                        (survival_fraction(d, b, k) for k in range(cap)), Fraction(0)
                    )
                    completed = total - sum(
                        hitting_time > cap for hitting_time in hitting_times
                    )
                    cap_rows.append(
                        {
                            "cap": cap,
                            "observed_survival": fraction_record(observed_survival),
                            "P247_survival": fraction_record(expected_survival),
                            "observed_mean_calls": fraction_record(observed_mean),
                            "P247_mean_calls": fraction_record(expected_mean),
                            "survival_equal": observed_survival == expected_survival,
                            "mean_equal": observed_mean == expected_mean,
                        }
                    )

                # Re-enumerate only endpoint/cap pairs to preserve exact path order.
                capped_endpoint_counts = {
                    cap: Counter() for cap in range(1, (d - b) // 2 + 2)
                }
                path_index = 0
                for start in range(d):
                    for recipe in matching_recipes(v for v in range(d) if v != start):
                        auxiliary = {start: start}
                        for left, right in recipe:
                            auxiliary[left] = right
                            auxiliary[right] = left
                        current = start
                        calls = 0
                        while True:
                            calls += 1
                            if current in absorbing:
                                for cap in capped_endpoint_counts:
                                    if calls <= cap:
                                        capped_endpoint_counts[cap][current] += 1
                                break
                            current = auxiliary[involution[current]]
                        path_index += 1
                assert path_index == total
                for row in cap_rows:
                    counts = capped_endpoint_counts[row["cap"]]
                    completed = sum(counts.values())
                    row["endpoint_counts"] = {str(key): counts[key] for key in sorted(counts)}
                    row["endpoint_uniform"] = all(
                        Fraction(counts[vertex], completed) == Fraction(1, b)
                        for vertex in absorbing
                    )
                    assert row["survival_equal"] and row["mean_equal"]
                    assert row["endpoint_uniform"]
                assert all(
                    count == total // b for count in terminal_counts.values()
                ) and set(terminal_counts) == absorbing
                scenarios.append(
                    {
                        "d": d,
                        "q": q,
                        "absorbing_size": b,
                        "screened_nonfixed_pairs": screened_pair_count,
                        "matchings_per_singleton_start": matchings_per_start,
                        "enumerated_paths": total,
                        "uncapped_terminal_counts": {
                            str(key): terminal_counts[key] for key in sorted(terminal_counts)
                        },
                        "caps": cap_rows,
                    }
                )
    return {
        "status": "passed",
        "scenarios": len(scenarios),
        "enumerated_paths": total_paths,
        "scope": (
            "Every odd d<=9, every odd fixed count q, every absorbing size "
            "b=q+2g, every singleton start, and every perfect matching of the "
            "remaining ranks. All comparisons use Fraction arithmetic."
        ),
        "rows": scenarios,
    }


def sparse_pool_controls():
    deletion_orders = 0
    invariant_checks = 0
    for size in range(1, 8):
        for order in itertools.permutations(range(size)):
            pool = SparsePool(size, random.Random(0), Counter())
            active = set(range(size))
            for label in order:
                pool.remove(label)
                active.remove(label)
                labels = {pool._forward(position) for position in range(pool.size)}
                assert labels == active
                assert all(pool._inverse(value) < pool.size for value in active)
                invariant_checks += 1
            deletion_orders += 1
    uniform_pop_runs = 0
    for size in range(1, 32):
        for seed in range(8):
            pool = SparsePool(size, random.Random(seed), Counter())
            popped = [pool.pop_uniform() for _ in range(size)]
            assert sorted(popped) == list(range(size))
            uniform_pop_runs += 1
    return {
        "status": "passed",
        "exhaustive_deletion_orders_through_size_7": deletion_orders,
        "active_set_invariant_checks": invariant_checks,
        "complete_uniform_pop_runs": uniform_pop_runs,
        "scope": (
            "All deletion orders through pool size seven, plus eight seeded full "
            "uniform-pop runs at every size through 31."
        ),
    }


def reflection_path_for_control(n, a, center, cap):
    pairing = GaussPairing(n, a)
    current = center
    baseline_endpoint = None
    static_endpoint = None
    for step in range(1, cap + 1):
        coordinate = pairing.select(current)
        image, branch = pairing.F(coordinate)
        screen = static_edge_screen(n, coordinate, image, Counter())
        if image == coordinate:
            decoded = pairing.decode(coordinate, branch)
            core = {
                "step": step,
                "rank": current,
                "first_hit_type": "fixed_" + branch,
                "endpoint_type": "factor" if "factor" in decoded else "root",
                "decoder_output": decoded,
            }
            baseline_endpoint = {**core, "screen_factors": []}
            if static_endpoint is None:
                static_endpoint = {
                    **core,
                    "screen_factors": screen["proper_divisors"],
                }
            break
        if static_endpoint is None and screen["proper_divisors"]:
            static_endpoint = {
                "step": step,
                "rank": current,
                "first_hit_type": "screened_nonfixed_edge",
                "endpoint_type": "factor",
                "decoder_output": {
                    "factor": screen["proper_divisors"][0],
                    "kind": "static_edge_screen",
                },
                "screen_factors": screen["proper_divisors"],
            }
        image_rank = pairing.rank(image)
        current = (2 * center - image_rank) % pairing.d
    assert baseline_endpoint is not None
    assert static_endpoint is not None
    return {"baseline": baseline_endpoint, "static_edge": static_endpoint}


def arithmetic_reflection_controls():
    rows = []
    for n, factors in ((15, (3, 5)), (21, (3, 7)), (35, (5, 7))):
        squares = sorted({r * r % n for r in range(1, n) if math.gcd(r, n) == 1})
        for a in squares:
            roots = [r for r in range(1, n) if math.gcd(r, n) == 1 and r * r % n == a]
            diagnostics = screen_absorbing_diagnostics(n, a, factors)
            d = diagnostics["d"]
            paths = [reflection_path_for_control(n, a, center, d) for center in range(d)]
            screens = {}
            for screen_name, absorbing_size in (
                ("baseline", diagnostics["q"]),
                ("static_edge", diagnostics["b"]),
            ):
                cap_rows = []
                for cap in range(1, min(d, 64) + 1):
                    endpoints = [path[screen_name] for path in paths]
                    completed = [endpoint for endpoint in endpoints if endpoint["step"] <= cap]
                    survival = Fraction(d - len(completed), d)
                    mean_calls = Fraction(
                        sum(min(endpoint["step"], cap) for endpoint in endpoints), d
                    )
                    benchmark_survival = survival_fraction(d, absorbing_size, cap)
                    benchmark_mean = sum(
                        (
                            survival_fraction(d, absorbing_size, k)
                            for k in range(cap)
                        ),
                        Fraction(0),
                    )
                    first_hits = Counter(endpoint["first_hit_type"] for endpoint in completed)
                    endpoint_counts = Counter(endpoint["rank"] for endpoint in completed)
                    factor_outputs = sum(
                        endpoint["endpoint_type"] == "factor" for endpoint in completed
                    )
                    screen_factor_centers = sum(
                        bool(endpoint["screen_factors"]) for endpoint in completed
                    )
                    valid_roots = [
                        endpoint
                        for endpoint in completed
                        if endpoint["endpoint_type"] == "root"
                    ]
                    root_factor_pairs = 0
                    root_failure_pairs = 0
                    for endpoint in valid_roots:
                        root = endpoint["decoder_output"]["root"]
                        for hidden_root in roots:
                            divisor = math.gcd(root - hidden_root, n)
                            if 1 < divisor < n:
                                root_factor_pairs += 1
                            else:
                                root_failure_pairs += 1
                    cap_rows.append(
                        {
                            "cap": cap,
                            "completed_centers": len(completed),
                            "surviving_centers": d - len(completed),
                            "reflection_survival": fraction_record(survival),
                            "P247_survival": fraction_record(benchmark_survival),
                            "survival_difference": fraction_record(
                                survival - benchmark_survival
                            ),
                            "reflection_mean_calls": fraction_record(mean_calls),
                            "P247_mean_calls": fraction_record(benchmark_mean),
                            "mean_difference": fraction_record(mean_calls - benchmark_mean),
                            "first_hit_types": dict(first_hits),
                            "endpoint_rank_counts": {
                                str(key): endpoint_counts[key]
                                for key in sorted(endpoint_counts)
                            },
                            "factor_outputs": factor_outputs,
                            "screen_factor_centers": screen_factor_centers,
                            "valid_root_outputs": len(valid_roots),
                            "outer_root_factor_pairs": root_factor_pairs,
                            "outer_root_decoding_failure_pairs": root_failure_pairs,
                            "root_fibre_size": len(roots),
                        }
                    )
                screens[screen_name] = {
                    "absorbing_size": absorbing_size,
                    "caps": cap_rows,
                }
            rows.append(
                {
                    "n": n,
                    "offline_factors": factors,
                    "a": a,
                    "roots": roots,
                    "diagnostics": diagnostics,
                    "centers_enumerated": d,
                    "rank_L_center": GaussPairing(n, a).L,
                    "screens": screens,
                }
            )
    return {
        "status": "passed",
        "instances": len(rows),
        "scope": (
            "Every distinct unit square for N=15,21,35; every reflection center; "
            "all caps through min(d,64); and the complete hidden-root fibre used "
            "only for offline outer-decoding counts."
        ),
        "rows": rows,
    }


def generic_reflection_control():
    rows = []
    for d in (3, 5, 7, 11, 13):
        hitting_times = {}
        for center in range(d):
            current = center
            calls = 0
            while True:
                calls += 1
                image = (-current) % d
                if image == current:
                    hitting_times[center] = calls
                    break
                current = (2 * center - image) % d
                assert calls <= d
        assert hitting_times[0] == 1
        assert all(
            hitting_times[center] == (d + 1) // 2 for center in range(1, d)
        )
        rows.append({"prime_d": d, "hitting_times": hitting_times})
    return {
        "status": "passed",
        "scope": (
            "Generic F(i)=-i mod d for five odd primes. This is not an F326 "
            "arithmetic counterexample."
        ),
        "rows": rows,
    }


def summarize_trajectories(trajectories, caps):
    result = {}
    for method in METHODS:
        method_rows = [row for row in trajectories if row["method"] == method]
        result[method] = {}
        for screen in SCREENS:
            result[method][screen] = {}
            for cap in caps:
                views = [row["views"][screen][str(cap)] for row in method_rows]
                totals = {
                    key: sum(view["costs"][key] for view in views) for key in COST_KEYS
                }
                factors = sum(view["factor_success"] for view in views)
                summary = {
                    "attempts": len(views),
                    "factor_successes": factors,
                    "censors": sum(view["status"] != "completed" for view in views),
                    "direct_factor_outputs": sum(view["direct_factor"] for view in views),
                    "screen_factor_outputs": sum(view["screen_factor"] for view in views),
                    "valid_root_outputs": sum(view["valid_root"] for view in views),
                    "root_factor_successes": sum(view["root_factor"] for view in views),
                    "root_decoding_failures": sum(
                        view["root_decoding_failure"] for view in views
                    ),
                    "first_hit_types": dict(
                        Counter(
                            view["endpoint"]["first_hit_type"]
                            for view in views
                            if view["endpoint"] is not None
                        )
                    ),
                    "charged_cost_totals": totals,
                    "maximum_pool_map_entries": max(
                        (
                            view["state"]["pool"]["maximum_map_entries"]
                            if view["state"]["pool"]
                            else 0
                        )
                        for view in views
                    )
                    if views
                    else 0,
                }
                if factors:
                    summary["empirical_charged_cost_per_factor"] = {
                        key: value / factors for key, value in totals.items()
                    }
                result[method][screen][str(cap)] = summary
    return result


def load_moduli(dataset):
    if dataset == "pilot":
        rows = []
        for source in PILOT_MODULI:
            row = {**source, "target_bits": source["n"].bit_length()}
            assert row["p_offline"] * row["q_offline"] == row["n"]
            rows.append(row)
        return rows, None
    if sha256(F328_INPUT) != F328_INPUT_SHA256:
        raise RuntimeError("the retained F328 modulus input hash changed")
    payload = json.loads(F328_INPUT.read_text())
    rows = [row for row in payload["moduli"] if row["target_bits"] in (20, 28, 36)]
    assert len(rows) == 6
    return rows, F328_INPUT_SHA256


def run_job(arguments, source_hash, log):
    rows, scale_input_hash = load_moduli(arguments.dataset)
    matches = [row for row in rows if row["modulus_id"] == arguments.modulus_id]
    if len(matches) != 1:
        raise ValueError("modulus id does not select one dataset row")
    modulus = matches[0]
    caps = PILOT_CAPS if arguments.dataset == "pilot" else SCALE_CAPS
    if arguments.max_cap != caps[-1]:
        raise ValueError("max cap does not match the dataset protocol")
    if arguments.query_start < 0 or arguments.queries < 1:
        raise ValueError("invalid query range")
    if arguments.query_start + arguments.queries > SQUARES_PER_MODULUS:
        raise ValueError("query range exceeds 16 accepted squares")
    if arguments.replicates != RANDOM_REPLICATES:
        raise ValueError("the retained protocol uses four random replicates")

    generated = generate_square_queries(
        arguments.dataset, modulus["modulus_id"], modulus["n"]
    )
    selected_queries = generated["queries"][
        arguments.query_start : arguments.query_start + arguments.queries
    ]
    selected_query_indices = {query["query_index"] for query in selected_queries}
    selected_generation_factors = [
        {
            **event,
            "dataset": arguments.dataset,
            "modulus_id": modulus["modulus_id"],
            "n": modulus["n"],
        }
        for event in generated["generation_factors"]
        if event["before_square_index"] in selected_query_indices
    ]
    trajectories = []
    query_rows = []
    started = time.perf_counter()
    base = {
        "experiment": "F329_random_center_paths",
        "route": "route:F31",
        "mode": "run",
        "dataset": arguments.dataset,
        "run_label": arguments.run_label,
        "seed": SEED,
        "modulus": modulus,
        "query_start": arguments.query_start,
        "requested_queries": arguments.queries,
        "replicates_per_random_method": arguments.replicates,
        "caps": caps,
        "max_cap": arguments.max_cap,
        "source_sha256": source_hash,
        "f326_source_sha256": sha256(F326_SOURCE),
        "f328_input_sha256": scale_input_hash,
        "hidden_generation": {
            "seed": generated["hidden_seed"],
            "total_outer_draws_for_all_16_squares": generated["total_outer_draws"],
            "scope": generated["scope"],
        },
        "selected_generation_factors": selected_generation_factors,
        "solver_isolation": (
            "The inner trajectory receives N, a, method, cap, and an independently "
            "derived matching seed. Hidden roots and offline factors remain in the "
            "outer driver."
        ),
        "randomness_scope": (
            "Ideal bounded draws use fair-bit rejection from the next power of two. "
            "The finite run uses independently derived Python Random.getrandbits "
            "streams and records every bit trial and rejection."
        ),
        "screen_scope": (
            "The paired static screen evaluates six distinct gcd arguments invariant "
            "under exchanging the endpoints: endpoint +/-1 for both endpoints, edge "
            "difference, and edge sum. Its charged state freezes at first absorption."
        ),
        "python_version": platform.python_version(),
        "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
        "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
        "memory_limit_bytes": MEMORY_LIMIT_BYTES,
    }

    for query in selected_queries:
        query_trajectories = []
        for method in METHODS:
            replicate_count = 1 if method == "rank_L_reflection" else arguments.replicates
            for replicate_index in range(replicate_count):
                matching_seed = derived_seed(
                    "matching",
                    arguments.dataset,
                    modulus["modulus_id"],
                    query["query_index"],
                    method,
                    replicate_index,
                )
                trajectory = arithmetic_trajectory(
                    modulus["n"],
                    query["a"],
                    method,
                    arguments.max_cap,
                    matching_seed,
                )
                processed_views = {screen: {} for screen in SCREENS}
                root_cache = {}
                for screen in SCREENS:
                    for cap in caps:
                        processed_views[screen][str(cap)] = postprocess_view(
                            trajectory["views"][screen][str(cap)],
                            query["hidden_root"],
                            modulus["n"],
                            query["generation_draw"],
                            root_cache,
                        )
                retained = {
                    **{
                        key: value
                        for key, value in trajectory.items()
                        if key != "views"
                    },
                    "query_index": query["query_index"],
                    "replicate_index": replicate_index,
                    "views": processed_views,
                }
                trajectories.append(retained)
                query_trajectories.append(retained)

        if arguments.diagnostics:
            if modulus["n"] > 1333:
                raise ValueError("full-domain diagnostics are restricted to N<=1333")
            diagnostics = screen_absorbing_diagnostics(
                modulus["n"],
                query["a"],
                (modulus["p_offline"], modulus["q_offline"]),
            )
        else:
            diagnostics = {
                "status": "unknown",
                "q": "unknown",
                "b": "unknown",
                "scope": "Not enumerated for this job.",
            }
        query_rows.append(
            {
                **query,
                "dataset": arguments.dataset,
                "modulus_id": modulus["modulus_id"],
                "n": modulus["n"],
                "hidden_root_scope": "outer validation only; never supplied to solver",
                "offline_diagnostics": diagnostics,
                "trajectory_count": len(query_trajectories),
            }
        )
        partial = {
            **base,
            "status": "running",
            "completed_queries": len(query_rows),
            "queries": query_rows,
            "trajectories": trajectories,
            "summary": summarize_trajectories(trajectories, caps),
            "walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, partial)
        log(
            "query_complete",
            modulus_id=modulus["modulus_id"],
            query_index=query["query_index"],
            trajectories=len(query_trajectories),
            walltime_seconds=time.perf_counter() - started,
            peak_rss_bytes=peak_rss_bytes(),
        )
        if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 512 MiB")

    return {
        **base,
        "status": "passed",
        "completed_queries": len(query_rows),
        "queries": query_rows,
        "trajectories": trajectories,
        "summary": summarize_trajectories(trajectories, caps),
        "walltime_seconds": time.perf_counter() - started,
        "peak_rss_bytes": peak_rss_bytes(),
    }


def aggregate_jobs(arguments, source_hash):
    caps = PILOT_CAPS if arguments.dataset == "pilot" else SCALE_CAPS
    moduli, scale_input_hash = load_moduli(arguments.dataset)
    jobs = []
    job_hashes = {}
    queries = []
    trajectories = []
    generation_factors = []
    for path_text in arguments.job:
        path = Path(path_text)
        payload = json.loads(path.read_text())
        assert payload["status"] == "passed"
        assert payload["dataset"] == arguments.dataset
        assert payload["source_sha256"] == source_hash
        jobs.append(payload)
        job_hashes[path.name] = sha256(path)
        queries.extend(payload["queries"])
        trajectories.extend(payload["trajectories"])
        generation_factors.extend(payload["selected_generation_factors"])

    query_keys = [(row["n"], row["query_index"]) for row in queries]
    if len(query_keys) != len(set(query_keys)):
        raise ValueError("duplicate square-query keys")
    trajectory_keys = [
        (row["n"], row["query_index"], row["method"], row["replicate_index"])
        for row in trajectories
    ]
    if len(trajectory_keys) != len(set(trajectory_keys)):
        raise ValueError("duplicate trajectory keys")
    generation_keys = [
        (event["n"], event["draw_index"]) for event in generation_factors
    ]
    if len(generation_keys) != len(set(generation_keys)):
        raise ValueError("duplicate generation-factor events")
    trajectories.sort(
        key=lambda row: (row["n"], row["query_index"], row["method"], row["replicate_index"])
    )

    by_modulus = {}
    coverage = {}
    for modulus in moduli:
        rows = [row for row in trajectories if row["n"] == modulus["n"]]
        present = sorted({row["query_index"] for row in rows})
        coverage[modulus["modulus_id"]] = {
            "present_query_indices": present,
            "missing_query_indices": [
                index for index in range(SQUARES_PER_MODULUS) if index not in present
            ],
        }
        if present and len(rows) != len(present) * (1 + 2 * RANDOM_REPLICATES):
            raise ValueError("unexpected trajectory count for a covered modulus")
        by_modulus[modulus["modulus_id"]] = {
            "n": modulus["n"],
            "target_bits": modulus["target_bits"],
            "summary": summarize_trajectories(rows, caps),
            "generation_factor_events": sum(
                event.get("modulus_id") == modulus["modulus_id"]
                for event in generation_factors
            ),
        }
        modulus_queries = [query for query in queries if query["n"] == modulus["n"]]
        if modulus_queries and all(
            query["offline_diagnostics"]["status"] == "exact"
            for query in modulus_queries
        ):
            benchmark = {}
            observed_summary = by_modulus[modulus["modulus_id"]]["summary"]
            for screen, size_key in (("baseline", "q"), ("static_edge", "b")):
                benchmark[screen] = {}
                for cap in caps:
                    expected_censors = Fraction(0)
                    expected_F_calls = Fraction(0)
                    for query in modulus_queries:
                        diagnostic = query["offline_diagnostics"]
                        expected_censors += RANDOM_REPLICATES * survival_fraction(
                            diagnostic["d"], diagnostic[size_key], cap
                        )
                        expected_F_calls += RANDOM_REPLICATES * sum(
                            (
                                survival_fraction(
                                    diagnostic["d"], diagnostic[size_key], k
                                )
                                for k in range(cap)
                            ),
                            Fraction(0),
                        )
                    methods = {}
                    for method in (
                        "uniform_center_reflection",
                        "lazy_uniform_matching",
                    ):
                        summary = observed_summary[method][screen][str(cap)]
                        methods[method] = {
                            "observed_censors": summary["censors"],
                            "observed_completed": summary["attempts"]
                            - summary["censors"],
                            "observed_F_calls": summary["charged_cost_totals"][
                                "F_calls"
                            ],
                            "censors_minus_P247_expectation": fraction_record(
                                Fraction(summary["censors"]) - expected_censors
                            ),
                            "F_calls_minus_P247_expectation": fraction_record(
                                Fraction(
                                    summary["charged_cost_totals"]["F_calls"]
                                )
                                - expected_F_calls
                            ),
                        }
                    benchmark[screen][str(cap)] = {
                        "attempts": RANDOM_REPLICATES * len(modulus_queries),
                        "P247_expected_censors": fraction_record(expected_censors),
                        "P247_expected_completed": fraction_record(
                            RANDOM_REPLICATES * len(modulus_queries)
                            - expected_censors
                        ),
                        "P247_expected_F_calls": fraction_record(expected_F_calls),
                        "observed_methods": methods,
                    }
            by_modulus[modulus["modulus_id"]]["P247_benchmark"] = benchmark
        else:
            by_modulus[modulus["modulus_id"]]["P247_benchmark"] = {
                "status": "unknown",
                "reason": "q and b were not enumerated for every retained square input",
            }

    diagnostics = {}
    for job in jobs:
        for query in job["queries"]:
            key = f'{job["modulus"]["modulus_id"]}:{query["query_index"]}'
            diagnostics[key] = query["offline_diagnostics"]

    return {
        "status": "passed",
        "experiment": "F329_random_center_paths",
        "route": "route:F31",
        "mode": "aggregate",
        "dataset": arguments.dataset,
        "seed": SEED,
        "caps": caps,
        "square_inputs_per_modulus": SQUARES_PER_MODULUS,
        "random_replicates_per_square": RANDOM_REPLICATES,
        "modulus_count": len(moduli),
        "query_count": len(queries),
        "trajectory_count": len(trajectories),
        "all_requested_queries_present": all(
            not row["missing_query_indices"] for row in coverage.values()
        ),
        "coverage": coverage,
        "by_modulus": by_modulus,
        "offline_diagnostics": diagnostics,
        "generation_factors": generation_factors,
        "trajectories": trajectories,
        "job_sha256": job_hashes,
        "job_process_walltime_seconds": sum(
            job["process_walltime_seconds"] for job in jobs
        ),
        "source_sha256": source_hash,
        "f326_source_sha256": sha256(F326_SOURCE),
        "f328_input_sha256": scale_input_hash,
        "inference_scope": (
            "All success and cost ratios are finite per-N measurements. Input sizes "
            "are not pooled into an inferred asymptotic rate. Unknown q/b labels "
            "remain unknown. Every censor remains in the charged numerator."
        ),
        "peak_rss_bytes": peak_rss_bytes(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("exact", "run", "aggregate"), required=True)
    parser.add_argument("--dataset", choices=("pilot", "scale"))
    parser.add_argument("--modulus-id")
    parser.add_argument("--query-start", type=int, default=0)
    parser.add_argument("--queries", type=int, default=1)
    parser.add_argument("--replicates", type=int, default=RANDOM_REPLICATES)
    parser.add_argument("--max-cap", type=int)
    parser.add_argument("--diagnostics", action="store_true")
    parser.add_argument("--run-label", default="unspecified")
    parser.add_argument("--job", action="append", default=[])
    parser.add_argument("--output", required=True)
    parser.add_argument("--status", required=True)
    parser.add_argument("--log", required=True)
    arguments = parser.parse_args()
    started = time.perf_counter()
    source_hash = sha256(Path(__file__))
    if sha256(F326_SOURCE) != F326_SOURCE_SHA256:
        raise RuntimeError("the imported F326 source does not match its frozen hash")

    log_path = Path(arguments.log)
    log_path.write_text("")

    def log(event, **values):
        with log_path.open("a") as stream:
            stream.write(json.dumps({"event": event, **values}, sort_keys=True) + "\n")

    def timeout_handler(_signal_number, _frame):
        raise TimeoutError("internal 28-second alarm fired")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(INTERNAL_TIMEOUT_SECONDS)
    running = {
        "status": "running",
        "experiment": "F329_random_center_paths",
        "mode": arguments.mode,
        "dataset": arguments.dataset,
        "seed": SEED,
        "source_sha256": source_hash,
    }
    write_json(arguments.status, running)
    log("start", **running)
    try:
        if arguments.mode == "exact":
            payload = {
                "status": "passed",
                "experiment": "F329_random_center_paths",
                "mode": "exact",
                "generic_matching": generic_matching_controls(),
                "sparse_pool": sparse_pool_controls(),
                "arithmetic_reflections": arithmetic_reflection_controls(),
                "generic_reflection": generic_reflection_control(),
                "source_sha256": source_hash,
                "f326_source_sha256": sha256(F326_SOURCE),
            }
        elif arguments.mode == "run":
            if not arguments.dataset or not arguments.modulus_id or not arguments.max_cap:
                parser.error("run mode needs dataset, modulus id, and max cap")
            payload = run_job(arguments, source_hash, log)
        else:
            if not arguments.dataset or not arguments.job:
                parser.error("aggregate mode needs a dataset and job files")
            payload = aggregate_jobs(arguments, source_hash)
        payload["internal_timeout_seconds"] = INTERNAL_TIMEOUT_SECONDS
        payload["hard_timeout_seconds"] = HARD_TIMEOUT_SECONDS
        payload["memory_limit_bytes"] = MEMORY_LIMIT_BYTES
        payload["process_walltime_seconds"] = time.perf_counter() - started
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
                "source_sha256",
                "internal_timeout_seconds",
                "hard_timeout_seconds",
                "memory_limit_bytes",
                "process_walltime_seconds",
                "peak_rss_bytes",
            )
        }
        status["dataset"] = arguments.dataset
        status["output"] = arguments.output
        write_json(arguments.status, status)
        log("passed", **status)
    except BaseException as exception:
        partial = {}
        if Path(arguments.output).exists():
            try:
                partial = json.loads(Path(arguments.output).read_text())
            except (OSError, json.JSONDecodeError):
                partial = {}
        failure = {
            **running,
            "status": "failed",
            "exception_type": type(exception).__name__,
            "exception": str(exception),
            "traceback": traceback.format_exc(),
            "partial_queries": partial.get("queries", []),
            "partial_trajectories": partial.get("trajectories", []),
            "process_walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, failure)
        write_json(arguments.status, failure)
        log("failed", **failure)
        raise
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    main()
