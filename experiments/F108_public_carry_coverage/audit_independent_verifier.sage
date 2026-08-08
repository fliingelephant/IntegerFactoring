#!/usr/bin/env sage
"""Hostile, independent audit of F108.

This file does not import or execute the F108 candidate source.  Sage
factorization is used only as a hidden-truth oracle after the public gcd
construction has been computed independently.
"""

import ast
import hashlib
import json
import operator
import random
import time
from math import gcd, isqrt, prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PUBLIC_PATH = ROOT / "experiments/F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json"
CANDIDATE_SOURCE = HERE / "analyze_public_carry_coverage.py"
CANDIDATE_OUTPUT = HERE / "OUTPUT.json"

EXPECTED_HASHES = {
    PUBLIC_PATH: "ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab",
    CANDIDATE_SOURCE: "0be579050066d9bc79e4bf5192a606989958fef2531420fb83984de925e1e8de",
    CANDIDATE_OUTPUT: "2427d36129ecac0de8e735d972f641dbdb2c22d885c28d1502ba0ff9411340c5",
}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rank_of_masks(masks, width):
    rows = [[(int(mask) >> column) & 1 for column in range(width)] for mask in masks]
    if not rows:
        return 0
    return int(Matrix(GF(2), rows).rank())


def matrix_of_masks(masks, width):
    return Matrix(
        GF(2),
        [[(int(mask) >> column) & 1 for column in range(width)] for mask in masks],
    )


def lifo_refinement(entries):
    """Reconstruct the pinned P66 transition without importing it."""
    pending = [(int(value), int(mask)) for value, mask in entries if value > 1 and mask]
    settled = []
    refinements = 0
    gcd_tests = 0
    while pending:
        value, mask = pending.pop()
        collision = None
        for position in range(len(settled)):
            old_value, old_mask = settled[position]
            gcd_tests += 1
            divisor = gcd(value, old_value)
            if divisor > 1:
                collision = (position, old_value, old_mask, divisor)
                break
        if collision is None:
            settled.append((value, mask))
            continue
        position, old_value, old_mask, divisor = collision
        del settled[position]
        refinements += 1
        pieces = (
            (divisor, operator.xor(mask, old_mask)),
            (value // divisor, mask),
            (old_value // divisor, old_mask),
        )
        pending.extend((part, part_mask) for part, part_mask in pieces if part > 1 and part_mask)

    for left in range(len(settled)):
        for right in range(left):
            require(gcd(settled[left][0], settled[right][0]) == 1, "terminal blocks overlap")
    return settled, refinements, gcd_tests


def saturation_rows(blocks, exposure_integers):
    exposure_product = prod(exposure_integers)
    rows = []
    supported_blocks = 0
    gcd_calls = 0
    for value, mask in blocks:
        remaining = value
        supported = 1
        while True:
            divisor = gcd(remaining, exposure_product)
            gcd_calls += 1
            if divisor == 1:
                break
            supported *= divisor
            remaining //= divisor
        require(supported * remaining == value, "saturation lost a factor")
        if supported > 1:
            supported_blocks += 1
        root = isqrt(supported)
        if root * root != supported:
            rows.append(mask)
    return rows, {
        "supported_terminal_blocks": supported_blocks,
        "nonsquare_supported_blocks": len(rows),
        "distinct_exposed_row_masks": len(set(rows)),
        "saturation_gcds": gcd_calls,
        "rank": rank_of_masks(rows, WIDTH),
        "exposure_product_bits": exposure_product.bit_length(),
    }


def states_for_key(modulus, bound, key):
    _, u_value, v_value, orientation = key
    if orientation == "u_power_times_v":
        multiplier, fixed = u_value, v_value
    else:
        multiplier, fixed = v_value, u_value
    states = []
    power = 1
    for _ in range(bound + 1):
        c_value = power * fixed % modulus
        w_value = int(inverse_mod(c_value, modulus))
        states.append((c_value, w_value, c_value * w_value))
        power = power * multiplier % modulus
    return multiplier, states


def exposure_scan(modulus, bound, keys, selected_values):
    raw_exposures = []
    local_exposures = []
    raw_pairs = []
    raw_counts = {
        "oriented_trajectories": len(keys),
        "transitions": len(keys) * bound,
        "c_zero_transitions": 0,
        "w_zero_transitions": 0,
        "two_zero_transitions_excluded": 0,
        "no_zero_transitions": 0,
    }
    local_zero_pairs = 0
    for key in keys:
        multiplier, states = states_for_key(modulus, bound, key)
        for exponent in range(bound):
            c_value, w_value, product_value = states[exponent]
            next_c, next_w, next_product = states[exponent + 1]
            c_numerator = multiplier * c_value - next_c
            w_numerator = multiplier * next_w - w_value
            require(c_numerator % modulus == 0, "nonintegral first carry")
            require(w_numerator % modulus == 0, "nonintegral second carry")
            first = c_numerator // modulus
            second = w_numerator // modulus
            require(0 <= first < multiplier, "first carry out of range")
            require(0 <= second < multiplier, "second carry out of range")
            if first == 0 and second == 0:
                raw_counts["two_zero_transitions_excluded"] += 1
                require(product_value == next_product, "two-zero step is not an exact duplicate")
                continue
            if first == 0 or second == 0:
                require(product_value != next_product, "one-zero step is an exact duplicate")
                raw_pairs.append((product_value, next_product))
            if first == 0:
                raw_exposures.append(c_value)
                raw_counts["c_zero_transitions"] += 1
            if second == 0:
                raw_exposures.append(next_w)
                raw_counts["w_zero_transitions"] += 1
            if first != 0 and second != 0:
                raw_counts["no_zero_transitions"] += 1

            if product_value in selected_values and next_product in selected_values:
                if first == 0 or second == 0:
                    local_zero_pairs += 1
                if first == 0:
                    local_exposures.append(c_value)
                if second == 0:
                    local_exposures.append(next_w)

    raw_counts["exposure_integers"] = len(raw_exposures)
    require(
        raw_counts["c_zero_transitions"]
        + raw_counts["w_zero_transitions"]
        + raw_counts["two_zero_transitions_excluded"]
        + raw_counts["no_zero_transitions"]
        == raw_counts["transitions"],
        "carry-state partition is incomplete",
    )
    return raw_exposures, raw_counts, raw_pairs, local_exposures, local_zero_pairs


def hidden_coverage(prime_rows, exposure_integers, width):
    exposed_primes = [
        prime
        for prime, mask in prime_rows.items()
        if mask and any(value % prime == 0 for value in exposure_integers)
    ]
    masks = [prime_rows[prime] for prime in exposed_primes]
    return {
        "prime_rows": len(exposed_primes),
        "distinct_masks": len(set(masks)),
        "rank": rank_of_masks(masks, width),
        "mask_set": set(masks),
    }


started = time.monotonic()
for path, expected in EXPECTED_HASHES.items():
    require(file_hash(path) == expected, f"pinned hash changed: {path}")

# Static factor-free audit.  Parsing is allowed; the candidate module is never
# imported or executed.
candidate_text = CANDIDATE_SOURCE.read_text()
candidate_tree = ast.parse(candidate_text)
forbidden_calls = []
for node in ast.walk(candidate_tree):
    if not isinstance(node, ast.Call):
        continue
    if isinstance(node.func, ast.Name):
        call_name = node.func.id
    elif isinstance(node.func, ast.Attribute):
        call_name = node.func.attr
    else:
        call_name = ""
    if call_name in {"factor", "factorint", "is_prime", "is_prime_power", "prime_factors"}:
        forbidden_calls.append(call_name)
require(not forbidden_calls, f"candidate calls forbidden factor operation: {forbidden_calls}")

public = json.loads(PUBLIC_PATH.read_text())
claimed = json.loads(CANDIDATE_OUTPUT.read_text())
MODULUS = int(public["N"])
BOUND = int(public["B"])
records = public["decoder"]["first_useful_certificate"]["witness_records"]
WIDTH = len(records)
require((MODULUS, BOUND, WIDTH) == (202_537_109, 784, 166), "fixed input changed")
require(len({int(record["P"]) for record in records}) == WIDTH, "circuit values are not distinct")

entries = []
prime_rows = {}
factor_cache = {}
for column, record in enumerate(records):
    c_value = int(record["c"])
    w_value = int(record["w"])
    product_value = int(record["P"])
    require(c_value * w_value == product_value, "invalid exact relation")
    require(product_value % MODULUS == 1, "invalid modular relation")
    mask = 1 << column
    entries.extend(((c_value, mask), (w_value, mask)))
    for endpoint in (c_value, w_value):
        if endpoint not in factor_cache:
            factor_cache[endpoint] = [(int(p), int(e)) for p, e in factor(ZZ(endpoint))]
        for prime, exponent in factor_cache[endpoint]:
            if exponent % 2:
                prime_rows[prime] = operator.xor(prime_rows.get(prime, 0), mask)

blocks, refinement_count, refinement_gcd_tests = lifo_refinement(entries)
full_rows = [
    mask for value, mask in blocks if isqrt(value) * isqrt(value) != value
]
full_matrix = matrix_of_masks(full_rows, WIDTH)
nonzero_prime_rows = {prime: mask for prime, mask in prime_rows.items() if mask}
hidden_full_matrix = matrix_of_masks(list(nonzero_prime_rows.values()), WIDTH)
require(set(full_rows) == set(nonzero_prime_rows.values()), "public full row masks differ from hidden truth")
require(full_matrix.rank() == hidden_full_matrix.rank() == 165, "full rank is not 165")
require(full_matrix.right_kernel() == hidden_full_matrix.right_kernel(), "public and hidden kernels differ")
require(full_matrix.right_nullity() == 1, "fixed circuit nullity is not one")

# Verify the terminal-block prime-row formula against factored hidden truth.
for prime, hidden_mask in prime_rows.items():
    containing = [(value, mask) for value, mask in blocks if value % prime == 0]
    if not containing:
        require(hidden_mask == 0, f"nonzero prime row {prime} vanished")
        continue
    require(len(containing) == 1, f"prime {prime} occurs in two terminal blocks")
    value, mask = containing[0]
    terminal_mask = mask if int(valuation(ZZ(value), prime)) % 2 else 0
    require(terminal_mask == hidden_mask, f"terminal formula failed at prime {prime}")

represented_keys = sorted(
    {
        (
            int(record["provenance"]["active_relation_index_zero_based"]),
            int(record["provenance"]["u"]),
            int(record["provenance"]["v"]),
            str(record["provenance"]["orientation"]),
        )
        for record in records
        if record["provenance"]["kind"] == "feedback_trajectory"
    }
)
all_keys = []
for active_index, pair in enumerate(public["active_pairs"]):
    u_value, v_value = map(int, pair)
    all_keys.append((active_index, u_value, v_value, "u_power_times_v"))
    all_keys.append((active_index, u_value, v_value, "u_times_v_power"))
require((len(represented_keys), len(all_keys)) == (8, 54), "trajectory-key counts changed")

selected_values = {int(record["P"]) for record in records}
(
    represented_exposures,
    represented_counts,
    represented_pairs,
    represented_local_exposures,
    represented_local_pairs,
) = exposure_scan(MODULUS, BOUND, represented_keys, selected_values)
(
    all_exposures,
    all_counts,
    all_pairs,
    all_local_exposures,
    all_local_pairs,
) = exposure_scan(MODULUS, BOUND, all_keys, selected_values)

represented_public_rows, represented_public = saturation_rows(blocks, represented_exposures)
all_public_rows, all_public = saturation_rows(blocks, all_exposures)
represented_hidden = hidden_coverage(nonzero_prime_rows, represented_exposures, WIDTH)
all_hidden = hidden_coverage(nonzero_prime_rows, all_exposures, WIDTH)
require(set(represented_public_rows) == represented_hidden["mask_set"], "represented theorem equality failed")
require(set(all_public_rows) == all_hidden["mask_set"], "all-trajectory theorem equality failed")
require(set(represented_public_rows).issubset(set(full_rows)), "represented rows exceed full space")
require(set(all_public_rows).issubset(set(full_rows)), "all-trajectory rows exceed full space")

represented_matrix = matrix_of_masks(represented_public_rows, WIDTH)
all_matrix = matrix_of_masks(all_public_rows, WIDTH)
require(represented_matrix.rank() == all_matrix.rank() == full_matrix.rank(), "exposed rank is not full")
require(represented_matrix.right_kernel() == full_matrix.right_kernel(), "represented kernel differs")
require(all_matrix.right_kernel() == full_matrix.right_kernel(), "all-trajectory kernel differs")

# The raw exposures are outside the selected circuit in general.  They do,
# however, connect distinct exact values in the complete generated round-one
# value set.  Report both scopes instead of conflating them.
generated_values = set()
for seed in range(2, int(public["n"]) + 1):
    inverse = int(inverse_mod(seed, MODULUS))
    generated_values.add(seed * inverse)
for key in all_keys:
    _, states = states_for_key(MODULUS, BOUND, key)
    generated_values.update(product_value for _, _, product_value in states)
require(len(generated_values - {1}) == int(public["decoder"]["unique_relation_count"]), "full value set mismatch")
require(
    all(left != right and left in generated_values and right in generated_values for left, right in all_pairs),
    "a raw exposure is not between two retained full-batch values",
)
require(
    all(left != right and left in generated_values and right in generated_values for left, right in represented_pairs),
    "a represented raw exposure is not between two retained full-batch values",
)

represented_local_rows, represented_local_public = saturation_rows(blocks, represented_local_exposures)
all_local_rows, all_local_public = saturation_rows(blocks, all_local_exposures)
represented_local_hidden = hidden_coverage(nonzero_prime_rows, represented_local_exposures, WIDTH)
all_local_hidden = hidden_coverage(nonzero_prime_rows, all_local_exposures, WIDTH)
require(set(represented_local_rows) == represented_local_hidden["mask_set"], "local represented theorem failed")
require(set(all_local_rows) == all_local_hidden["mask_set"], "local all theorem failed")

# Root and unique dependency are checked independently from the claimed gcds.
exact_product = prod(int(record["P"]) for record in records)
exact_root = isqrt(exact_product)
require(exact_root * exact_root == exact_product, "certificate product is not a square")
root_modulus = exact_root % MODULUS
root_gcds = [gcd(root_modulus - 1, MODULUS), gcd(root_modulus + 1, MODULUS)]
require((root_modulus, sorted(root_gcds)) == (132_013_085, [10_267, 19_727]), "root check changed")

# Exhaustively attack gcd saturation on small integers.
saturation_cases = 0
for value in range(2, 160):
    for exposure in range(1, 160):
        remaining = value
        supported = 1
        divisions = 0
        while True:
            divisor = gcd(remaining, exposure)
            if divisor == 1:
                break
            supported *= divisor
            remaining //= divisor
            divisions += 1
        expected_supported = prod(
            int(prime) ** int(exponent)
            for prime, exponent in factor(ZZ(value))
            if exposure % int(prime) == 0
        )
        require(supported == expected_supported, f"small saturation counterexample: {value},{exposure}")
        require(divisions <= value.bit_length() - 1, "saturation division bound failed")
        saturation_cases += 1

# Attack the terminal theorem on random pairwise-coprime blocks.
rng = random.Random(int(108))
available_primes = [int(prime) for prime in prime_range(2, 400)]
random_terminal_cases = 0
for _ in range(512):
    rng.shuffle(available_primes)
    width = rng.randrange(1, 10)
    block_count = rng.randrange(1, 10)
    cursor = 0
    synthetic_blocks = []
    prime_data = []
    for _block in range(block_count):
        mask = rng.randrange(1, 1 << width)
        factor_count = rng.randrange(1, 5)
        block_value = 1
        for prime in available_primes[cursor : cursor + factor_count]:
            exponent = rng.randrange(1, 8)
            block_value *= prime**exponent
            prime_data.append((prime, exponent, mask))
        cursor += factor_count
        synthetic_blocks.append((block_value, mask))
    exposed_primes = {
        prime for prime, _, _ in prime_data if rng.randrange(2) == 1
    }
    synthetic_exposure = prod(exposed_primes) if exposed_primes else 1
    public_masks, _ = saturation_rows(synthetic_blocks, [synthetic_exposure])
    hidden_masks = {
        mask
        for prime, exponent, mask in prime_data
        if prime in exposed_primes and exponent % 2
    }
    require(set(public_masks) == hidden_masks, "random terminal theorem counterexample")
    random_terminal_cases += 1

# Instantiate the F99 private-row boundary at a fresh T and verify both carry
# coordinates.  The second carry is exactly one, which is needed for the
# rank-at-most-one conclusion.
T = 6
Ks = [2**exponent - 1 for exponent in range(1, T + 1)]
private_primes = []
for exponent in range(1, T + 1):
    lower = 2 ** (T + exponent)
    prime = int(next_prime(lower))
    require(lower < prime < 2 * lower, "Bertrand interval failed")
    private_primes.append(prime)
M = 2**T * prod(prime**2 for prime in private_primes)
targets = [1] + [
    int((prime - 1) * inverse_mod(K, prime**2) % (prime**2))
    for K, prime in zip(Ks, private_primes)
]
a_class = int(CRT_list(targets, [2**T] + [prime**2 for prime in private_primes]))
require(gcd(a_class, M) == 1 and gcd(M, 7) == 1, "CRT class is not reduced")
left_class = next(1 + lift * M for lift in range(1, 7) if gcd(1 + lift * M, 7 * M) == 1)
right_class = next(a_class + lift * M for lift in range(1, 7) if gcd(a_class + lift * M, 7 * M) == 1)
progression_modulus = 7 * M
left_prime = next(
    left_class + step * progression_modulus
    for step in range(100_000)
    if is_prime(left_class + step * progression_modulus)
)
right_prime = next(
    right_class + step * progression_modulus
    for step in range(100_000)
    if is_prime(right_class + step * progression_modulus)
)
require(left_prime != right_prime, "private-row semiprime factors coincide")
private_N = int(left_prime * right_prime)
require(private_N % M == a_class, "private-row modulus missed CRT class")
private_products = [1 + K * private_N for K in Ks]
private_identity_rows = []
for index, (exponent, private_prime) in enumerate(zip(range(1, T + 1), private_primes)):
    c_value = 2**exponent
    w_value = private_products[index] // c_value
    require(0 < w_value < private_N, "private inverse is not canonical")
    require((c_value * w_value) % private_N == 1, "private inverse identity failed")
    require(int(valuation(ZZ(private_products[index]), private_prime)) == 1, "private valuation is not one")
    row = [1 if value % private_prime == 0 else 0 for value in private_products]
    require(sum(row) == 1 and row[index] == 1, "private row is not private")
    private_identity_rows.append(row)
require(Matrix(GF(2), private_identity_rows).rank() == T, "private matrix lost full rank")
private_exposures = []
carry_pairs = []
for exponent in range(1, T):
    c_value = 2**exponent
    next_c = 2 ** (exponent + 1)
    w_value = private_products[exponent - 1] // c_value
    next_w = private_products[exponent] // next_c
    first = (2 * c_value - next_c) // private_N
    second = (2 * next_w - w_value) // private_N
    carry_pairs.append([first, second])
    require((first, second) == (0, 1), "F99 carry boundary changed")
    private_exposures.append(c_value)
require(set(int(prime) for value in private_exposures for prime, _ in factor(ZZ(value))) == {2}, "F99 exposure has an odd prime")
two_row = [int(valuation(ZZ(value), 2)) % 2 for value in private_products]
f99_exposed_rank = int(Matrix(GF(2), [two_row]).rank())
require(f99_exposed_rank <= 1 < T, "F99 exposure unexpectedly spans")

# Compare exact fixed counts only after all independent computations exist.
expected_represented_counts = {
    key: claimed["represented_trajectory_coverage"][key]
    for key in (
        "oriented_trajectories",
        "transitions",
        "exposure_integers",
        "c_zero_transitions",
        "w_zero_transitions",
        "two_zero_transitions_excluded",
        "no_zero_transitions",
    )
}
expected_all_counts = {
    key: claimed["all_round_one_coverage"][key]
    for key in expected_represented_counts
}
require(represented_counts == expected_represented_counts, "represented carry counts differ")
require(all_counts == expected_all_counts, "all-trajectory carry counts differ")
for computed, section in (
    (represented_public, claimed["represented_trajectory_coverage"]),
    (all_public, claimed["all_round_one_coverage"]),
):
    for key in (
        "supported_terminal_blocks",
        "nonsquare_supported_blocks",
        "distinct_exposed_row_masks",
        "saturation_gcds",
        "rank",
        "exposure_product_bits",
    ):
        require(computed[key] == section[key], f"claimed coverage count differs: {key}")
require(
    {
        "terminal_blocks": len(blocks),
        "square_terminal_blocks": sum(isqrt(value) * isqrt(value) == value for value, _ in blocks),
        "nonsquare_row_masks": len(full_rows),
        "distinct_nonsquare_row_masks": len(set(full_rows)),
        "rank": int(full_matrix.rank()),
        "nullity": int(full_matrix.right_nullity()),
        "refinements": refinement_count,
        "gcd_tests": refinement_gcd_tests,
    }
    == claimed["public_refinement"],
    "claimed public-refinement counts differ",
)

result = {
    "status": "PASS",
    "candidate_source_executed_or_imported": False,
    "pins": {str(path.relative_to(ROOT)): digest for path, digest in EXPECTED_HASHES.items()},
    "general_theorem_attacks": {
        "exhaustive_saturation_cases": saturation_cases,
        "random_pairwise_coprime_terminal_cases": random_terminal_cases,
        "counterexamples": 0,
    },
    "factor_free_static_audit": {
        "forbidden_factor_calls": forbidden_calls,
        "candidate_imports": sorted(
            {
                alias.name
                for node in candidate_tree.body
                if isinstance(node, (ast.Import, ast.ImportFrom))
                for alias in node.names
            }
        ),
    },
    "fixed_circuit": {
        "N": MODULUS,
        "columns": WIDTH,
        "hidden_nonzero_prime_rows": len(nonzero_prime_rows),
        "hidden_distinct_masks": len(set(nonzero_prime_rows.values())),
        "public_terminal_blocks": len(blocks),
        "public_distinct_full_masks": len(set(full_rows)),
        "full_rank": int(full_matrix.rank()),
        "full_nullity": int(full_matrix.right_nullity()),
        "root_mod_N": root_modulus,
        "root_gcds": root_gcds,
    },
    "represented_raw_scope": {
        **represented_counts,
        **represented_public,
        "hidden_exposed_prime_rows": represented_hidden["prime_rows"],
        "hidden_distinct_masks": represented_hidden["distinct_masks"],
        "same_kernel_as_full": represented_matrix.right_kernel() == full_matrix.right_kernel(),
    },
    "all_round_one_raw_scope": {
        **all_counts,
        **all_public,
        "hidden_exposed_prime_rows": all_hidden["prime_rows"],
        "hidden_distinct_masks": all_hidden["distinct_masks"],
        "same_kernel_as_full": all_matrix.right_kernel() == full_matrix.right_kernel(),
    },
    "scope_boundary": {
        "full_generated_nonunit_values": len(generated_values - {1}),
        "raw_exposure_pairs_are_distinct_retained_full_batch_values": True,
        "represented_circuit_local_zero_carry_pairs": represented_local_pairs,
        "represented_circuit_local_exposure_integers": len(represented_local_exposures),
        "represented_circuit_local_distinct_masks": len(set(represented_local_rows)),
        "represented_circuit_local_rank": rank_of_masks(represented_local_rows, WIDTH),
        "all_trajectories_circuit_local_zero_carry_pairs": all_local_pairs,
        "all_trajectories_circuit_local_exposure_integers": len(all_local_exposures),
        "all_trajectories_circuit_local_distinct_masks": len(set(all_local_rows)),
        "all_trajectories_circuit_local_rank": rank_of_masks(all_local_rows, WIDTH),
    },
    "f99_boundary": {
        "T": T,
        "N_bits": private_N.bit_length(),
        "full_rank": T,
        "carry_pairs": carry_pairs,
        "exposed_prime_set": [2],
        "exposed_rank": f99_exposed_rank,
    },
    "elapsed_seconds": time.monotonic() - started,
}
print(json.dumps(result, indent=2, sort_keys=True, default=int))
