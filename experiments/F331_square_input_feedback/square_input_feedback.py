#!/usr/bin/env python3
"""F331: charged public feedback among square inputs to the F326 path."""

import argparse
from collections import Counter
import hashlib
import inspect
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
HERE = Path(__file__).resolve().parent
F326_DIR = ROOT / "experiments" / "F326_direct_gauss_pairing"
F328_DIR = ROOT / "experiments" / "F328_capped_rabin_paths"
F326_SOURCE = F326_DIR / "direct_gauss_pairing.py"
F328_SOURCE = F328_DIR / "capped_rabin_paths.py"
MODULI_SOURCE = F328_DIR / "moduli.json"
F326_SOURCE_SHA256 = "7829cc45822021c64c42842a2c938b15c52df85e30ae694efcdd4171c5012f73"
F328_SOURCE_SHA256 = "2388f049fcd69d9cd7fd95dbaeb5b0871d14a9865c44b248258545beb272d86b"
MODULI_SHA256 = "acf09b285c57c39cfcb93d3cd77addce909498e224955fd0ec9d2e4d86ee0428"
SEED = 33120260907
ROUNDS = 16
PROBE_CAP = 8
MAX_PROPOSALS = 4
TRIALS_PER_MODULUS = 32
TARGET_BITS = (20, 28, 36, 44)
POLICIES = ("path", "uniform", "last")
INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024

sys.path.insert(0, str(F326_DIR))
sys.path.insert(0, str(F328_DIR))
from direct_gauss_pairing import GaussPairing, auxiliary, jacobi
from capped_rabin_paths import arithmetic_walk, operation_counts


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


def derived_seed(*parts):
    raw = ":".join(str(part) for part in (SEED, *parts)).encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:16], "big")


def sample_bounded(bound, generator, costs, prefix):
    assert bound >= 1
    if bound == 1:
        costs[prefix + "_draws"] += 1
        return 0
    width = (bound - 1).bit_length()
    while True:
        costs[prefix + "_draws"] += 1
        costs[prefix + "_fair_bits"] += width
        value = generator.getrandbits(width)
        if value < bound:
            return value
        costs[prefix + "_rejections"] += 1


def sample_nonzero(n, generator, costs, prefix):
    return sample_bounded(n - 1, generator, costs, prefix) + 1


def add_pairing_costs(costs, pairing_counts):
    raw = dict(pairing_counts)
    for key in (
        "F_calls",
        "floor_sum_calls",
        "floor_sum_euclidean_iterations",
        "rank_calls",
        "select_calls",
        "select_binary_iterations",
    ):
        costs[key] += raw.get(key, 0)
    costs["solver_gcd_calls"] += raw.get("F_gcd_calls", 0)
    costs["solver_gcd_calls"] += raw.get("decode_gcd_calls", 0)
    costs["modular_inversion_calls"] += raw.get("setup_modular_inversions", 0)
    costs["modular_inversion_calls"] += raw.get("F_modular_inversions", 0)
    costs["modular_inversion_calls"] += raw.get("decode_modular_inversions", 0)


def retain_unit_coordinate(value, branch, pool, seen, last):
    if value == 0 or abs(value) == 1 or branch == "fixed_nonunit":
        return last
    absolute = abs(value)
    if absolute not in seen:
        seen.add(absolute)
        pool.append(absolute)
    return absolute


def path_probe(n, a, cap):
    started = time.perf_counter()
    pairing = GaussPairing(n, a)
    current_rank = pairing.L
    pool = []
    seen = set()
    last_unit = None
    trace = []
    endpoint = None
    path_modular_multiplications = 0
    for step in range(1, cap + 1):
        coordinate = pairing.select(current_rank)
        image, branch = pairing.F(coordinate)
        if branch == "scaled_inverse":
            path_modular_multiplications += 2
        elif branch == "negate":
            path_modular_multiplications += 1
        last_unit = retain_unit_coordinate(
            coordinate, branch, pool, seen, last_unit
        )
        last_unit = retain_unit_coordinate(image, branch, pool, seen, last_unit)
        row = {
            "step": step,
            "current_rank": current_rank,
            "current_coordinate": coordinate,
            "F_image": image,
            "F_branch": branch,
        }
        if image == coordinate:
            decoded = pairing.decode(coordinate, branch)
            if "factor" in decoded:
                divisor = decoded["factor"]
                assert 1 < divisor < n and n % divisor == 0
                endpoint_type = "factor"
            else:
                root = decoded["root"]
                assert root * root % n == a
                path_modular_multiplications += 1
                endpoint_type = "root"
            endpoint = {
                "step": step,
                "rank": current_rank,
                "coordinate": coordinate,
                "branch": branch,
                "endpoint_type": endpoint_type,
                "output": decoded,
                "verified_exactly": True,
            }
            row.update({"terminal": True, "endpoint": endpoint})
            trace.append(row)
            break
        image_rank = pairing.rank(image)
        next_rank = auxiliary(
            image_rank, pairing.L, pairing.d, "rank_reflection"
        )
        row.update(
            {
                "terminal": False,
                "F_image_rank": image_rank,
                "next_rank": next_rank,
            }
        )
        trace.append(row)
        current_rank = next_rank
    return {
        "solver_interface": ["n", "a", "cap"],
        "n": n,
        "a": a,
        "method": "rank_reflection",
        "cap": cap,
        "h": pairing.h,
        "L": pairing.L,
        "d": pairing.d,
        "status": "completed" if endpoint else "censored_at_cap",
        "endpoint": endpoint,
        "F_calls": pairing.counters["F_calls"],
        "pairing_operation_counts": operation_counts(pairing.counters),
        "path_modular_multiplications": path_modular_multiplications,
        "distinct_absolute_visited_units": pool,
        "last_nontrivial_visited_unit": last_unit,
        "visited_scope": (
            "Computed current coordinates and their computed F images; "
            "opposite signs share one absolute multiplier."
        ),
        "trace": trace,
        "walltime_seconds": time.perf_counter() - started,
    }


def pull_back_root(n, a0, public_multiplier, current_root, costs):
    inverse_multiplier = pow(public_multiplier, -1, n)
    costs["modular_inversion_calls"] += 1
    root0 = current_root * inverse_multiplier % n
    costs["modular_multiplication_calls"] += 2
    assert root0 * root0 % n == a0
    return root0


def nearest_square(value, costs):
    costs["integer_square_root_calls"] += 1
    lower = math.isqrt(value)
    upper = lower + 1
    lower_square = lower * lower
    upper_square = upper * upper
    costs["integer_square_multiplications"] += 2
    if value - lower_square <= upper_square - value:
        return lower, lower_square, value - lower_square
    return upper, upper_square, upper_square - value


def choose_path_multipliers(pool, generator, costs):
    available = list(pool)
    selected = []
    while available and len(selected) < MAX_PROPOSALS:
        position = sample_bounded(
            len(available), generator, costs, "policy_random"
        )
        selected.append(available.pop(position))
    return selected


def controller(n, a0, policy, policy_seed):
    """Public controller: its signature and state contain no hidden root."""
    assert policy in POLICIES
    started = time.perf_counter()
    generator = random.Random(policy_seed)
    a = a0
    cumulative_multiplier = 1
    costs = Counter()
    history = []
    for round_index in range(ROUNDS):
        costs["rounds"] += 1
        assert a == a0 * cumulative_multiplier * cumulative_multiplier % n
        costs["invariant_validation_multiplications"] += 2
        current_root, current_square, current_gap = nearest_square(a, costs)
        round_record = {
            "round": round_index,
            "a": a,
            "cumulative_multiplier": cumulative_multiplier,
            "ordinary_square_test": {
                "nearest_root": current_root,
                "nearest_square": current_square,
                "gap": current_gap,
                "is_exact": current_gap == 0,
            },
        }
        if current_gap == 0:
            root0 = pull_back_root(
                n, a0, cumulative_multiplier, current_root, costs
            )
            round_record["outcome"] = {
                "type": "ordinary_square_root",
                "root_of_a0": root0,
            }
            history.append(round_record)
            return {
                "status": "root",
                "factor": None,
                "root_of_a0": root0,
                "history": history,
                "costs": dict(costs),
                "walltime_seconds": time.perf_counter() - started,
            }

        costs["path_probes"] += 1
        probe = path_probe(n, a, PROBE_CAP)
        add_pairing_costs(costs, probe["pairing_operation_counts"]["raw_pairing_counters"])
        costs["modular_multiplication_calls"] += probe[
            "path_modular_multiplications"
        ]
        round_record["path_probe"] = probe
        if probe["endpoint"] is not None:
            endpoint = probe["endpoint"]
            if endpoint["endpoint_type"] == "factor":
                factor = endpoint["output"]["factor"]
                round_record["outcome"] = {
                    "type": "direct_path_factor",
                    "factor": factor,
                }
                history.append(round_record)
                return {
                    "status": "factor",
                    "factor": factor,
                    "root_of_a0": None,
                    "history": history,
                    "costs": dict(costs),
                    "walltime_seconds": time.perf_counter() - started,
                }
            root0 = pull_back_root(
                n,
                a0,
                cumulative_multiplier,
                endpoint["output"]["root"],
                costs,
            )
            round_record["outcome"] = {
                "type": "path_root",
                "root_of_a0": root0,
            }
            history.append(round_record)
            return {
                "status": "root",
                "factor": None,
                "root_of_a0": root0,
                "history": history,
                "costs": dict(costs),
                "walltime_seconds": time.perf_counter() - started,
            }

        if policy == "path":
            multipliers = choose_path_multipliers(
                probe["distinct_absolute_visited_units"], generator, costs
            )
        elif policy == "last":
            multipliers = (
                [probe["last_nontrivial_visited_unit"]]
                if probe["last_nontrivial_visited_unit"] is not None
                else []
            )
        else:
            multipliers = []
            for _ in range(MAX_PROPOSALS):
                candidate = sample_nonzero(
                    n, generator, costs, "policy_random"
                )
                costs["multiplier_generation_gcd_calls"] += 1
                divisor = math.gcd(candidate, n)
                if divisor != 1:
                    assert 1 < divisor < n and n % divisor == 0
                    round_record.setdefault("proposals", []).append(
                        {
                            "order": len(multipliers),
                            "candidate": candidate,
                            "generation_gcd": divisor,
                            "outcome": "multiplier_generation_factor",
                        }
                    )
                    round_record["outcome"] = {
                        "type": "multiplier_generation_factor",
                        "factor": divisor,
                    }
                    history.append(round_record)
                    return {
                        "status": "factor",
                        "factor": divisor,
                        "root_of_a0": None,
                        "history": history,
                        "costs": dict(costs),
                        "walltime_seconds": time.perf_counter() - started,
                    }
                multipliers.append(candidate)

        if not multipliers:
            round_record["proposals"] = []
            round_record["outcome"] = {"type": "empty_multiplier_pool"}
            history.append(round_record)
            return {
                "status": "empty_pool_failure",
                "factor": None,
                "root_of_a0": None,
                "history": history,
                "costs": dict(costs),
                "walltime_seconds": time.perf_counter() - started,
            }

        proposals = []
        for order, multiplier in enumerate(multipliers):
            assert 1 <= multiplier < n and math.gcd(multiplier, n) == 1
            costs["proposals"] += 1
            costs["modular_multiplication_calls"] += 2
            proposed_a = a * multiplier * multiplier % n
            nearest_root, nearest_value, score = nearest_square(proposed_a, costs)
            difference = proposed_a - nearest_value
            costs["proposal_gcd_calls"] += 1
            divisor = math.gcd(difference, n)
            proposal = {
                "order": order,
                "multiplier": multiplier,
                "proposed_a": proposed_a,
                "nearest_root": nearest_root,
                "nearest_square": nearest_value,
                "score": score,
                "signed_difference": difference,
                "difference_gcd": divisor,
            }
            proposals.append(proposal)
            if 1 < divisor < n:
                assert n % divisor == 0
                proposal["outcome"] = "proposal_screen_factor"
                round_record["proposals"] = proposals
                round_record["outcome"] = {
                    "type": "proposal_screen_factor",
                    "factor": divisor,
                }
                history.append(round_record)
                return {
                    "status": "factor",
                    "factor": divisor,
                    "root_of_a0": None,
                    "history": history,
                    "costs": dict(costs),
                    "walltime_seconds": time.perf_counter() - started,
                }
            if difference == 0:
                assert divisor == n
                costs["modular_multiplication_calls"] += 1
                proposed_multiplier = cumulative_multiplier * multiplier % n
                root0 = pull_back_root(
                    n, a0, proposed_multiplier, nearest_root, costs
                )
                proposal["outcome"] = "proposal_ordinary_square_root"
                proposal["proposed_cumulative_multiplier"] = proposed_multiplier
                round_record["proposals"] = proposals
                round_record["outcome"] = {
                    "type": "proposal_ordinary_square_root",
                    "root_of_a0": root0,
                }
                history.append(round_record)
                return {
                    "status": "root",
                    "factor": None,
                    "root_of_a0": root0,
                    "history": history,
                    "costs": dict(costs),
                    "walltime_seconds": time.perf_counter() - started,
                }
            assert divisor == 1
            proposal["outcome"] = "unit_gap"

        selected = min(proposals, key=lambda item: (item["score"], item["order"]))
        costs["modular_multiplication_calls"] += 1
        cumulative_multiplier = (
            cumulative_multiplier * selected["multiplier"] % n
        )
        a = selected["proposed_a"]
        selected["selected"] = True
        round_record["proposals"] = proposals
        round_record["selected_order"] = selected["order"]
        round_record["next_a"] = a
        round_record["next_cumulative_multiplier"] = cumulative_multiplier
        history.append(round_record)

    return {
        "status": "round_cap_censor",
        "factor": None,
        "root_of_a0": None,
        "history": history,
        "costs": dict(costs),
        "walltime_seconds": time.perf_counter() - started,
    }


def initial_draw(n, modulus_id, trial_index):
    seed = derived_seed("hidden", modulus_id, trial_index)
    generator = random.Random(seed)
    costs = Counter()
    hidden_root = sample_nonzero(n, generator, costs, "hidden_random")
    costs["generation_gcd_calls"] += 1
    divisor = math.gcd(hidden_root, n)
    if divisor == 1:
        costs["modular_multiplication_calls"] += 1
        a0 = hidden_root * hidden_root % n
        assert jacobi(a0, n) == 1
        factor = None
    else:
        assert 1 < divisor < n and n % divisor == 0
        a0 = None
        factor = divisor
    return {
        "hidden_seed": seed,
        "hidden_root": hidden_root,
        "a0": a0,
        "generation_factor": factor,
        "costs": dict(costs),
    }


def run_attempt(modulus, trial_index, policy):
    started = time.perf_counter()
    n = modulus["n"]
    initial = initial_draw(n, modulus["modulus_id"], trial_index)
    policy_seed = derived_seed("policy", policy, modulus["modulus_id"], trial_index)
    if initial["generation_factor"] is not None:
        accepted_factor = initial["generation_factor"]
        status = "factor_from_initial_generation"
        controller_result = None
        total_costs = Counter(initial["costs"])
    else:
        controller_result = controller(n, initial["a0"], policy, policy_seed)
        total_costs = Counter(initial["costs"])
        total_costs.update(controller_result["costs"])
        accepted_factor = controller_result["factor"]
        if controller_result["status"] == "root":
            total_costs["outer_root_decode_gcd_calls"] += 1
            divisor = math.gcd(
                controller_result["root_of_a0"] - initial["hidden_root"], n
            )
            if 1 < divisor < n:
                accepted_factor = divisor
                status = "factor_from_pulled_back_root"
            else:
                assert divisor in (1, n)
                status = "pulled_back_root_decode_failure"
        elif controller_result["status"] == "factor":
            status = "factor_from_controller"
        else:
            status = controller_result["status"]
    if accepted_factor is not None:
        assert 1 < accepted_factor < n and n % accepted_factor == 0
        assert any(
            accepted_factor % prime == 0
            for prime in (modulus["p_offline"], modulus["q_offline"])
        )
    total_costs["total_gcd_calls"] = sum(
        total_costs.get(key, 0)
        for key in (
            "generation_gcd_calls",
            "solver_gcd_calls",
            "multiplier_generation_gcd_calls",
            "proposal_gcd_calls",
            "outer_root_decode_gcd_calls",
        )
    )
    return {
        "modulus_id": modulus["modulus_id"],
        "target_bits": modulus["target_bits"],
        "n": n,
        "p_offline": modulus["p_offline"],
        "q_offline": modulus["q_offline"],
        "trial_index": trial_index,
        "policy": policy,
        "policy_seed": policy_seed,
        "initial": initial,
        "controller": controller_result,
        "status": status,
        "factor_success": accepted_factor is not None,
        "accepted_factor": accepted_factor,
        "total_costs": dict(total_costs),
        "walltime_seconds": time.perf_counter() - started,
    }


def tiny_checks():
    started = time.perf_counter()
    counts = Counter()
    assert list(inspect.signature(controller).parameters) == [
        "n",
        "a0",
        "policy",
        "policy_seed",
    ]
    counts["controller_interface_checks"] += 1
    for n in (15, 21, 35, 45):
        for hidden_root in range(1, n):
            if math.gcd(hidden_root, n) != 1:
                continue
            a0 = hidden_root * hidden_root % n
            for cumulative_multiplier in range(1, n):
                if math.gcd(cumulative_multiplier, n) != 1:
                    continue
                a = a0 * cumulative_multiplier * cumulative_multiplier % n
                for sign in (1, -1):
                    current_root = sign * hidden_root * cumulative_multiplier % n
                    costs = Counter()
                    root0 = pull_back_root(
                        n, a0, cumulative_multiplier, current_root, costs
                    )
                    assert root0 == sign * hidden_root % n
                    assert current_root * current_root % n == a
                    counts["root_pullback_checks"] += 1
    for n, hidden_root in ((15, 2), (21, 4), (35, 2), (45, 2)):
        a = hidden_root * hidden_root % n
        ours = path_probe(n, a, PROBE_CAP)
        reference = arithmetic_walk(n, a, "rank_reflection", PROBE_CAP)
        assert ours["n"] == reference["n"]
        assert ours["a"] == reference["a"]
        assert ours["L"] == reference["L"] and ours["d"] == reference["d"]
        assert ours["status"] == reference["status"]
        assert ours["endpoint"] == reference["endpoint"]
        assert (
            ours["pairing_operation_counts"]
            == reference["final_operation_counts"]
        )
        counts["path_probe_agreement_checks"] += 1
    return {
        "scope": (
            "Public controller signature, exhaustive root pullback on four "
            "tiny moduli, and exact eight-call probe agreement on four cases."
        ),
        "counts": dict(counts),
        "walltime_seconds": time.perf_counter() - started,
    }


def load_moduli():
    data = json.loads(MODULI_SOURCE.read_text())
    assert data["status"] == "passed"
    selected = {
        row["modulus_id"]: row
        for row in data["moduli"]
        if row["target_bits"] in TARGET_BITS
    }
    assert len(selected) == 2 * len(TARGET_BITS)
    for row in selected.values():
        assert row["p_offline"] * row["q_offline"] == row["n"]
    return selected


def summarize(attempts):
    summary = {}
    for policy in POLICIES:
        rows = [row for row in attempts if row["policy"] == policy]
        successes = [row for row in rows if row["factor_success"]]
        operation_totals = Counter()
        for row in rows:
            operation_totals.update(row["total_costs"])
        summary[policy] = {
            "attempts": len(rows),
            "factor_successes": len(successes),
            "status_counts": dict(Counter(row["status"] for row in rows)),
            "operation_totals": dict(operation_totals),
            "walltime_seconds": sum(row["walltime_seconds"] for row in rows),
            "cost_per_observed_factor": (
                {
                    key: value / len(successes)
                    for key, value in operation_totals.items()
                }
                if successes
                else None
            ),
        }
    return summary


def run_rows(modulus, trial_start, trial_end):
    attempts = []
    for trial_index in range(trial_start, trial_end + 1):
        shared = None
        for policy in POLICIES:
            attempt = run_attempt(modulus, trial_index, policy)
            initial_signature = (
                attempt["initial"]["hidden_seed"],
                attempt["initial"]["hidden_root"],
                attempt["initial"]["a0"],
                attempt["initial"]["generation_factor"],
            )
            if shared is None:
                shared = initial_signature
            else:
                assert initial_signature == shared
            attempts.append(attempt)
            print(
                json.dumps(
                    {
                        "event": "attempt_complete",
                        "modulus_id": modulus["modulus_id"],
                        "trial_index": trial_index,
                        "policy": policy,
                        "status": attempt["status"],
                        "factor_success": attempt["factor_success"],
                        "F_calls": attempt["total_costs"].get("F_calls", 0),
                        "rounds": attempt["total_costs"].get("rounds", 0),
                        "proposals": attempt["total_costs"].get("proposals", 0),
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
            if peak_rss_bytes() > MEMORY_LIMIT_BYTES:
                raise MemoryError("peak RSS exceeded 512 MiB")
    return attempts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("check", "pilot", "batch"), required=True)
    parser.add_argument("--modulus-id")
    parser.add_argument("--trial-start", type=int, default=0)
    parser.add_argument("--trial-end", type=int, default=31)
    parser.add_argument("--output", required=True)
    parser.add_argument("--status", required=True)
    arguments = parser.parse_args()
    started = time.perf_counter()

    def timeout_handler(_signal_number, _frame):
        raise TimeoutError("internal 28-second alarm fired")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(INTERNAL_TIMEOUT_SECONDS)
    source_hash = sha256(Path(__file__))
    input_hashes = {
        "DESIGN.md": sha256(HERE / "DESIGN.md"),
        "F326_direct_gauss_pairing.py": sha256(F326_SOURCE),
        "F328_capped_rabin_paths.py": sha256(F328_SOURCE),
        "F328_moduli.json": sha256(MODULI_SOURCE),
    }
    running = {
        "status": "running",
        "experiment": "F331_square_input_feedback",
        "family": "route:F31",
        "mode": arguments.mode,
        "source_sha256": source_hash,
        "input_hashes": input_hashes,
    }
    write_json(arguments.status, running)
    try:
        assert input_hashes["F326_direct_gauss_pairing.py"] == F326_SOURCE_SHA256
        assert input_hashes["F328_capped_rabin_paths.py"] == F328_SOURCE_SHA256
        assert input_hashes["F328_moduli.json"] == MODULI_SHA256
        moduli = load_moduli()
        checks = tiny_checks() if arguments.mode in ("check", "pilot") else None
        if arguments.mode == "check":
            attempts = []
            modulus_scope = None
            trial_scope = None
        elif arguments.mode == "pilot":
            modulus = moduli["b20_i0"]
            attempts = run_rows(modulus, 0, 1)
            modulus_scope = modulus["modulus_id"]
            trial_scope = [0, 1]
        else:
            assert arguments.modulus_id in moduli
            assert 0 <= arguments.trial_start <= arguments.trial_end
            assert arguments.trial_end < TRIALS_PER_MODULUS
            modulus = moduli[arguments.modulus_id]
            attempts = run_rows(
                modulus, arguments.trial_start, arguments.trial_end
            )
            modulus_scope = modulus["modulus_id"]
            trial_scope = [arguments.trial_start, arguments.trial_end]
        payload = {
            **running,
            "status": "passed",
            "seed": SEED,
            "controller_parameters": {
                "rounds": ROUNDS,
                "path_probe_cap": PROBE_CAP,
                "maximum_proposals": MAX_PROPOSALS,
                "policies": POLICIES,
            },
            "modulus_scope": modulus_scope,
            "trial_scope_inclusive": trial_scope,
            "tiny_checks": checks,
            "summary": summarize(attempts),
            "attempts": attempts,
            "scope": (
                "Finite paired policy comparison. Offline factors validate "
                "only. The controller interface excludes the hidden root, and "
                "all pulled-back roots are decoded only by the outer driver."
            ),
            "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
            "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
            "memory_limit_bytes": MEMORY_LIMIT_BYTES,
            "walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        if payload["peak_rss_bytes"] > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 512 MiB")
        write_json(arguments.output, payload)
        status = {
            key: payload[key]
            for key in (
                "status",
                "experiment",
                "family",
                "mode",
                "source_sha256",
                "input_hashes",
                "modulus_scope",
                "trial_scope_inclusive",
                "internal_timeout_seconds",
                "hard_timeout_seconds",
                "memory_limit_bytes",
                "walltime_seconds",
                "peak_rss_bytes",
            )
        }
        status["output"] = arguments.output
        write_json(arguments.status, status)
        print(json.dumps({"event": "passed", **status}, sort_keys=True), flush=True)
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
        print(json.dumps({"event": "failed", **failure}, sort_keys=True), flush=True)
        raise
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    main()
