import json
import math
import random
import time
from pathlib import Path


RUN = "F59-D01"
FAMILY = "F26"
TARGET_FACTOR_BITS = (10, 14, 18, 22)
RATIOS = ((21, 20), (4, 3), (7, 4))
TRIALS = 8
MASTER_SEED = 0xF59D01
OUTPUT = Path(__file__).resolve().parent.parent / "output" / f"{RUN}.json"


def is_prime(value):
    if value < 2:
        return False
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % prime == 0:
            return value == prime
    odd_part = value - 1
    power_of_two = 0
    while odd_part % 2 == 0:
        odd_part //= 2
        power_of_two += 1
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % value == 0:
            continue
        residue = pow(base, odd_part, value)
        if residue in (1, value - 1):
            continue
        for _ in range(power_of_two - 1):
            residue = residue * residue % value
            if residue == value - 1:
                break
        else:
            return False
    return True


def next_prime(lower_bound):
    candidate = max(2, lower_bound)
    if candidate == 2:
        return 2
    candidate |= 1
    while not is_prime(candidate):
        candidate += 2
    return candidate


def proper_divisor(divisor, modulus):
    return 1 < divisor < modulus


def add_direct_event(events, divisor, modulus):
    if proper_divisor(divisor, modulus):
        key = str(divisor)
        events[key] = events.get(key, 0) + 1


def sample_unit(rng, modulus, direct_events):
    while True:
        candidate = rng.randrange(1, modulus)
        divisor = math.gcd(candidate, modulus)
        if divisor == 1:
            return candidate
        add_direct_event(direct_events, divisor, modulus)


def relation(modulus, unit):
    inverse = pow(unit, -1, modulus)
    quotient = (unit * inverse - 1) // modulus
    assert 0 <= quotient < unit
    assert unit * inverse == modulus * quotient + 1
    return unit, inverse, quotient


def walk_prefix(modulus, start, step_cap, direct_events):
    records = []
    state = start
    for _ in range(step_cap):
        if state == 1:
            break
        divisor = math.gcd(state, modulus)
        if divisor != 1:
            add_direct_event(direct_events, divisor, modulus)
            break
        item = relation(modulus, state)
        records.append(item)
        state = item[2]
    return records


def parity_coprime_basis(initial_entries):
    stable = []
    work = [(value, mask) for value, mask in initial_entries if value > 1 and mask]
    refinements = 0
    gcd_tests = 0

    while work:
        value, mask = work.pop()
        for index, (basis_value, basis_mask) in enumerate(stable):
            gcd_tests += 1
            divisor = math.gcd(value, basis_value)
            if divisor == 1:
                continue

            stable.pop(index)
            refinements += 1
            for new_value, new_mask in (
                (divisor, mask ^ basis_mask),
                (value // divisor, mask),
                (basis_value // divisor, basis_mask),
            ):
                if new_value > 1 and new_mask:
                    work.append((new_value, new_mask))
            break
        else:
            stable.append((value, mask))

    return stable, refinements, gcd_tests


def binary_kernel_basis(row_masks, column_count):
    pivots = {}
    for original in row_masks:
        row = original
        while row:
            pivot = row.bit_length() - 1
            known = pivots.get(pivot)
            if known is None:
                pivots[pivot] = row
                break
            row ^= known

    kernel = []
    pivot_columns = set(pivots)
    ordered_pivots = sorted(pivots)
    for free_column in range(column_count):
        if free_column in pivot_columns:
            continue
        vector = 1 << free_column
        for pivot in ordered_pivots:
            if (pivots[pivot] & vector).bit_count() & 1:
                vector ^= 1 << pivot
        assert all(not ((row & vector).bit_count() & 1) for row in pivots.values())
        kernel.append(vector)

    return len(pivots), kernel


def decode_relations(modulus, raw_relations):
    unique = []
    seen_quotients = set()
    duplicate_count = 0
    zero_count = 0
    for unit, inverse, quotient in raw_relations:
        assert unit * inverse == modulus * quotient + 1
        if quotient == 0:
            zero_count += 1
            continue
        if quotient in seen_quotients:
            duplicate_count += 1
            continue
        seen_quotients.add(quotient)
        unique.append((unit, inverse, quotient))

    initial_entries = []
    relation_values = []
    quotient_values = []
    for index, (unit, inverse, quotient) in enumerate(unique):
        mask = 1 << index
        initial_entries.append((unit, mask))
        initial_entries.append((inverse, mask))
        relation_value = modulus * quotient + 1
        assert relation_value == unit * inverse
        assert relation_value % modulus == 1
        relation_values.append(relation_value)
        quotient_values.append(quotient)

    coprime_blocks, refinements, gcd_tests = parity_coprime_basis(initial_entries)
    row_masks = []
    square_block_count = 0
    for value, mask in coprime_blocks:
        root = math.isqrt(value)
        if root * root == value:
            square_block_count += 1
        else:
            row_masks.append(mask)

    rank, kernel = binary_kernel_basis(row_masks, len(unique))
    assert rank + len(kernel) == len(unique)

    global_plus = 0
    global_minus = 0
    useful = 0
    first_certificate = None
    for vector in kernel:
        selected = []
        product = 1
        remaining = vector
        while remaining:
            low_bit = remaining & -remaining
            index = low_bit.bit_length() - 1
            selected.append(index)
            product *= relation_values[index]
            remaining ^= low_bit
        root = math.isqrt(product)
        assert root * root == product
        root_residue = root % modulus
        if root_residue == 1:
            global_plus += 1
            continue
        if root_residue == modulus - 1:
            global_minus += 1
            continue

        minus_divisor = math.gcd(root - 1, modulus)
        plus_divisor = math.gcd(root + 1, modulus)
        assert proper_divisor(minus_divisor, modulus)
        assert proper_divisor(plus_divisor, modulus)
        useful += 1
        if first_certificate is None:
            first_certificate = {
                "selected_columns": selected,
                "selected_quotients": [quotient_values[index] for index in selected],
                "root_mod_N": root_residue,
                "gcd_root_minus_one": minus_divisor,
                "gcd_root_plus_one": plus_divisor,
            }

    sorted_quotients = sorted(quotient_values)
    minimum_gap = None
    span = None
    if len(sorted_quotients) >= 2:
        minimum_gap = min(
            right - left for left, right in zip(sorted_quotients, sorted_quotients[1:])
        )
        span = sorted_quotients[-1] - sorted_quotients[0]

    return {
        "raw_relation_count": len(raw_relations),
        "zero_relation_count": zero_count,
        "duplicate_quotient_count": duplicate_count,
        "unique_relation_count": len(unique),
        "minimum_quotient_gap": minimum_gap,
        "quotient_span": span,
        "coprime_block_count": len(coprime_blocks),
        "square_block_count": square_block_count,
        "nonsquare_row_count": len(row_masks),
        "squareclass_rank": rank,
        "kernel_dimension": len(kernel),
        "global_plus_basis_roots": global_plus,
        "global_minus_basis_roots": global_minus,
        "useful_basis_roots": useful,
        "factor_found_by_batch_decoder": useful > 0,
        "gcd_refinements": refinements,
        "gcd_pair_tests": gcd_tests,
        "maximum_block_bits": max((value.bit_length() for value, _ in coprime_blocks), default=0),
        "first_useful_certificate": first_certificate,
    }


def direct_event_summary(events):
    return {
        "event_count": sum(events.values()),
        "divisor_counts": dict(sorted(events.items(), key=lambda item: int(item[0]))),
    }


def summarize_trials(trials):
    return {
        "trial_count": len(trials),
        "trials_with_nonzero_kernel": sum(row["kernel_dimension"] > 0 for row in trials),
        "trials_with_useful_basis_root": sum(row["factor_found_by_batch_decoder"] for row in trials),
        "total_kernel_dimension": sum(row["kernel_dimension"] for row in trials),
        "total_useful_basis_roots": sum(row["useful_basis_roots"] for row in trials),
        "total_direct_gcd_events": sum(row["direct_gcd_events"]["event_count"] for row in trials),
        "minimum_unique_relation_count": min(row["unique_relation_count"] for row in trials),
        "maximum_unique_relation_count": max(row["unique_relation_count"] for row in trials),
        "minimum_rank_deficit": min(row["kernel_dimension"] for row in trials),
        "maximum_rank_deficit": max(row["kernel_dimension"] for row in trials),
    }


def self_check():
    synthetic_entries = (
        (2, 0b001),
        (3, 0b001),
        (2, 0b010),
        (5, 0b010),
        (3, 0b100),
        (5, 0b100),
    )
    blocks, _, _ = parity_coprime_basis(synthetic_entries)
    rows = [mask for value, mask in blocks if math.isqrt(value) ** 2 != value]
    rank, kernel = binary_kernel_basis(rows, 3)
    assert rank == 2
    assert kernel == [0b111]
    result = decode_relations(15, [(2, 8, 1)])
    assert result["kernel_dimension"] == 1
    assert result["useful_basis_roots"] == 1
    assert result["first_useful_certificate"]["gcd_root_minus_one"] == 3
    return {
        "synthetic_6_10_15_kernel": kernel,
        "N15_singleton_factor": result["first_useful_certificate"],
    }


started = time.monotonic()
self_checks = self_check()
master = random.Random(MASTER_SEED)
input_records = []

for target_bits in TARGET_FACTOR_BITS:
    prime_p = next_prime(1 << target_bits)
    for ratio_numerator, ratio_denominator in RATIOS:
        lower_q = (ratio_numerator * prime_p + ratio_denominator - 1) // ratio_denominator
        prime_q = next_prime(max(prime_p + 2, lower_q))
        modulus = prime_p * prime_q
        input_bits = modulus.bit_length()
        batch_size = input_bits * input_bits

        iid_trials = []
        tail_trials = []
        for trial_index in range(TRIALS):
            iid_seed = master.getrandbits(64)
            iid_rng = random.Random(iid_seed)
            iid_direct = {}
            iid_relations = [
                relation(modulus, sample_unit(iid_rng, modulus, iid_direct))
                for _ in range(batch_size)
            ]
            iid_result = decode_relations(modulus, iid_relations)
            iid_result.update(
                {
                    "trial": trial_index,
                    "stream_seed": iid_seed,
                    "direct_gcd_events": direct_event_summary(iid_direct),
                }
            )
            iid_trials.append(iid_result)

            tail_seed = master.getrandbits(64)
            tail_rng = random.Random(tail_seed)
            tail_direct = {}
            tail_relations = []
            for _ in range(input_bits):
                start = sample_unit(tail_rng, modulus, tail_direct)
                tail_relations.extend(walk_prefix(modulus, start, input_bits, tail_direct))
            tail_result = decode_relations(modulus, tail_relations)
            tail_result.update(
                {
                    "trial": trial_index,
                    "stream_seed": tail_seed,
                    "start_count": input_bits,
                    "step_cap_per_start": input_bits,
                    "direct_gcd_events": direct_event_summary(tail_direct),
                }
            )
            tail_trials.append(tail_result)

        offset_direct = {}
        offset_relations = []
        for offset in range(1, input_bits + 1):
            offset_relations.extend(
                walk_prefix(modulus, modulus - offset, input_bits, offset_direct)
            )
        offset_result = decode_relations(modulus, offset_relations)
        offset_result.update(
            {
                "start_count": input_bits,
                "step_cap_per_start": input_bits,
                "direct_gcd_events": direct_event_summary(offset_direct),
            }
        )

        record = {
            "target_factor_bits": target_bits,
            "ratio_numerator": ratio_numerator,
            "ratio_denominator": ratio_denominator,
            "p": prime_p,
            "q": prime_q,
            "q_over_p": prime_q / prime_p,
            "N": modulus,
            "input_bits": input_bits,
            "declared_batch_size_n_squared": batch_size,
            "iid_single_step": {
                "summary": summarize_trials(iid_trials),
                "trials": iid_trials,
            },
            "random_tail_prefixes": {
                "summary": summarize_trials(tail_trials),
                "trials": tail_trials,
            },
            "deterministic_offset_tail_prefixes": offset_result,
        }
        input_records.append(record)
        print(
            json.dumps(
                {
                    "N": modulus,
                    "bits": input_bits,
                    "ratio": [ratio_numerator, ratio_denominator],
                    "iid_nonzero_kernel_trials": record["iid_single_step"]["summary"]["trials_with_nonzero_kernel"],
                    "iid_useful_trials": record["iid_single_step"]["summary"]["trials_with_useful_basis_root"],
                    "tail_nonzero_kernel_trials": record["random_tail_prefixes"]["summary"]["trials_with_nonzero_kernel"],
                    "tail_useful_trials": record["random_tail_prefixes"]["summary"]["trials_with_useful_basis_root"],
                    "offset_kernel_dimension": offset_result["kernel_dimension"],
                    "offset_useful": offset_result["factor_found_by_batch_decoder"],
                },
                sort_keys=True,
            ),
            flush=True,
        )

elapsed = time.monotonic() - started
payload = {
    "run": RUN,
    "family": FAMILY,
    "disposition": "finite seeded discovery and kill evidence only; no asymptotic inference",
    "master_seed": MASTER_SEED,
    "target_factor_bits": TARGET_FACTOR_BITS,
    "ratios": RATIOS,
    "trials_per_random_source": TRIALS,
    "batch_rule": "n^2 single-step relations, or n starts times at most n descent steps",
    "decoder": "factor-free parity gcd refinement followed by exact kernel-basis roots",
    "self_checks": self_checks,
    "elapsed_seconds": elapsed,
    "records": input_records,
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT.open("w", encoding="utf-8") as handle:
    json.dump(payload, handle, indent=2, sort_keys=True)
    handle.write("\n")

print(json.dumps({"output": str(OUTPUT), "elapsed_seconds": elapsed}, sort_keys=True))
