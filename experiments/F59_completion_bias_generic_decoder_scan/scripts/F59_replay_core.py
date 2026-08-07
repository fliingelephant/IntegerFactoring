import math


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
            return records
        divisor = math.gcd(state, modulus)
        if divisor != 1:
            add_direct_event(direct_events, divisor, modulus)
            return records
        item = relation(modulus, state)
        records.append(item)
        state = item[2]

    if state != 1:
        add_direct_event(direct_events, math.gcd(state, modulus), modulus)
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
    final_events = {}
    final_records = walk_prefix(15, 7, 1, final_events)
    assert final_records == [(7, 13, 6)]
    assert final_events == {"3": 1}
    return {
        "synthetic_6_10_15_kernel": kernel,
        "N15_singleton_factor": result["first_useful_certificate"],
        "N15_final_endpoint_event": final_events,
    }
