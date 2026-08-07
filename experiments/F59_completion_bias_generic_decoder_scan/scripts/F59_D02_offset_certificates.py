import json
import math
from pathlib import Path


RUN = "F59-D02"
FAMILY = "F26"
TARGET_FACTOR_BITS = (10, 14, 18, 22)
RATIOS = ((21, 20), (4, 3), (7, 4))
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


def walk_prefix(modulus, start_offset, step_cap, direct_events):
    records = []
    state = modulus - start_offset
    for step_index in range(step_cap):
        if state == 1:
            break
        divisor = math.gcd(state, modulus)
        if divisor != 1:
            if proper_divisor(divisor, modulus):
                key = str(divisor)
                direct_events[key] = direct_events.get(key, 0) + 1
            return records
        inverse = pow(state, -1, modulus)
        quotient = (state * inverse - 1) // modulus
        assert state * inverse == modulus * quotient + 1
        assert 0 <= quotient < state
        records.append(
            {
                "start_offset": start_offset,
                "step_index": step_index,
                "u": state,
                "v": inverse,
                "k": quotient,
            }
        )
        state = quotient

    if state != 1:
        divisor = math.gcd(state, modulus)
        if proper_divisor(divisor, modulus):
            key = str(divisor)
            direct_events[key] = direct_events.get(key, 0) + 1
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
    for free_column in range(column_count):
        if free_column in pivot_columns:
            continue
        vector = 1 << free_column
        for pivot in sorted(pivots):
            if (pivots[pivot] & vector).bit_count() & 1:
                vector ^= 1 << pivot
        assert all(not ((row & vector).bit_count() & 1) for row in pivots.values())
        kernel.append(vector)
    return len(pivots), kernel


def decode_with_certificates(modulus, raw_records):
    unique = []
    quotient_to_index = {}
    duplicate_count = 0
    zero_count = 0
    for record in raw_records:
        quotient = record["k"]
        if quotient == 0:
            zero_count += 1
            continue
        known_index = quotient_to_index.get(quotient)
        if known_index is not None:
            duplicate_count += 1
            unique[known_index]["duplicate_provenance"].append(
                [record["start_offset"], record["step_index"]]
            )
            continue
        retained = dict(record)
        retained["A"] = modulus * quotient + 1
        retained["duplicate_provenance"] = []
        assert retained["A"] == retained["u"] * retained["v"]
        quotient_to_index[quotient] = len(unique)
        unique.append(retained)

    initial_entries = []
    for index, record in enumerate(unique):
        mask = 1 << index
        initial_entries.append((record["u"], mask))
        initial_entries.append((record["v"], mask))
    blocks, refinements, gcd_tests = parity_coprime_basis(initial_entries)
    rows = []
    for value, mask in blocks:
        root = math.isqrt(value)
        if root * root != value:
            rows.append(mask)
    rank, kernel = binary_kernel_basis(rows, len(unique))
    assert rank + len(kernel) == len(unique)

    certificates = []
    for vector in kernel:
        selected_indices = []
        product = 1
        odd_endpoint_labels = set()
        remaining = vector
        while remaining:
            low_bit = remaining & -remaining
            index = low_bit.bit_length() - 1
            selected_indices.append(index)
            record = unique[index]
            product *= record["A"]
            for endpoint in (record["u"], record["v"]):
                if endpoint in odd_endpoint_labels:
                    odd_endpoint_labels.remove(endpoint)
                else:
                    odd_endpoint_labels.add(endpoint)
            remaining ^= low_bit
        root = math.isqrt(product)
        assert root * root == product
        residue = root % modulus
        if residue == 1:
            root_type = "global_plus"
            divisors = None
        elif residue == modulus - 1:
            root_type = "global_minus"
            divisors = None
        else:
            minus_divisor = math.gcd(root - 1, modulus)
            plus_divisor = math.gcd(root + 1, modulus)
            assert proper_divisor(minus_divisor, modulus)
            assert proper_divisor(plus_divisor, modulus)
            root_type = "non_global"
            divisors = [minus_divisor, plus_divisor]
        certificates.append(
            {
                "selected_columns": selected_indices,
                "support_size": len(selected_indices),
                "selected_relations": [unique[index] for index in selected_indices],
                "root_mod_N": residue,
                "root_type": root_type,
                "gcd_divisors": divisors,
                "formal_endpoint_even": not odd_endpoint_labels,
                "odd_endpoint_labels": sorted(odd_endpoint_labels),
                "contains_N_minus_1_loop": any(
                    unique[index]["u"] == modulus - 1
                    and unique[index]["v"] == modulus - 1
                    for index in selected_indices
                ),
            }
        )

    global_square_columns = []
    for index, record in enumerate(unique):
        root = math.isqrt(record["A"])
        if root * root == record["A"] and root % modulus in (1, modulus - 1):
            global_square_columns.append(index)

    return {
        "raw_relation_count": len(raw_records),
        "zero_relation_count": zero_count,
        "duplicate_quotient_count": duplicate_count,
        "unique_relation_count": len(unique),
        "global_square_singleton_columns": global_square_columns,
        "squareclass_rank": rank,
        "kernel_dimension": len(kernel),
        "formal_endpoint_basis_relations": sum(
            certificate["formal_endpoint_even"] for certificate in certificates
        ),
        "arithmetic_only_basis_relations": sum(
            not certificate["formal_endpoint_even"] for certificate in certificates
        ),
        "global_plus_basis_roots": sum(
            certificate["root_type"] == "global_plus" for certificate in certificates
        ),
        "global_minus_basis_roots": sum(
            certificate["root_type"] == "global_minus" for certificate in certificates
        ),
        "non_global_basis_roots": sum(
            certificate["root_type"] == "non_global" for certificate in certificates
        ),
        "gcd_refinements": refinements,
        "gcd_pair_tests": gcd_tests,
        "certificates": certificates,
    }


def global_square_relation(modulus, record):
    relation_value = modulus * record["k"] + 1
    root = math.isqrt(relation_value)
    return root * root == relation_value and root % modulus in (1, modulus - 1)


def self_check():
    arithmetic = decode_with_certificates(
        15,
        [{"start_offset": 0, "step_index": 0, "u": 2, "v": 8, "k": 1}],
    )
    assert arithmetic["kernel_dimension"] == 1
    assert arithmetic["certificates"][0]["root_type"] == "non_global"
    assert not arithmetic["certificates"][0]["formal_endpoint_even"]
    formal = decode_with_certificates(
        15,
        [{"start_offset": 1, "step_index": 0, "u": 14, "v": 14, "k": 13}],
    )
    assert formal["kernel_dimension"] == 1
    assert formal["certificates"][0]["root_type"] == "global_minus"
    assert formal["certificates"][0]["formal_endpoint_even"]
    return {
        "N15_arithmetic_relation": arithmetic["certificates"][0],
        "N15_global_loop": formal["certificates"][0],
    }


self_checks = self_check()
records = []
for target_bits in TARGET_FACTOR_BITS:
    prime_p = next_prime(1 << target_bits)
    for ratio_numerator, ratio_denominator in RATIOS:
        lower_q = (ratio_numerator * prime_p + ratio_denominator - 1) // ratio_denominator
        prime_q = next_prime(max(prime_p + 2, lower_q))
        modulus = prime_p * prime_q
        input_bits = modulus.bit_length()
        direct_events = {}
        full_raw = []
        for offset in range(1, input_bits + 1):
            full_raw.extend(walk_prefix(modulus, offset, input_bits, direct_events))

        no_global_singletons_raw = [
            record for record in full_raw if not global_square_relation(modulus, record)
        ]
        no_first_offset_raw = [record for record in full_raw if record["start_offset"] != 1]
        full = decode_with_certificates(modulus, full_raw)
        no_global_singletons = decode_with_certificates(modulus, no_global_singletons_raw)
        no_first_offset = decode_with_certificates(modulus, no_first_offset_raw)

        records.append(
            {
                "target_factor_bits": target_bits,
                "ratio": [ratio_numerator, ratio_denominator],
                "p": prime_p,
                "q": prime_q,
                "N": modulus,
                "input_bits": input_bits,
                "direct_gcd_events": {
                    "event_count": sum(direct_events.values()),
                    "divisor_counts": dict(sorted(direct_events.items(), key=lambda item: int(item[0]))),
                },
                "full_offset_batch": full,
                "without_global_square_singletons": no_global_singletons,
                "without_first_offset_path": no_first_offset,
            }
        )
        print(
            json.dumps(
                {
                    "N": modulus,
                    "bits": input_bits,
                    "full_kernel": full["kernel_dimension"],
                    "full_formal": full["formal_endpoint_basis_relations"],
                    "full_arithmetic_only": full["arithmetic_only_basis_relations"],
                    "without_global_singletons_kernel": no_global_singletons["kernel_dimension"],
                    "without_first_offset_kernel": no_first_offset["kernel_dimension"],
                    "non_global_roots": full["non_global_basis_roots"],
                },
                sort_keys=True,
            ),
            flush=True,
        )

payload = {
    "run": RUN,
    "family": FAMILY,
    "disposition": "finite deterministic certificate replay only; no asymptotic inference",
    "target_factor_bits": TARGET_FACTOR_BITS,
    "ratios": RATIOS,
    "source": "deterministic offsets c=1,...,n with n-step prefixes",
    "variants": [
        "full offset batch",
        "remove every global-square singleton relation",
        "remove the complete c=1 trajectory",
    ],
    "self_checks": self_checks,
    "records": records,
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT.open("w", encoding="utf-8") as handle:
    json.dump(payload, handle, indent=2, sort_keys=True)
    handle.write("\n")

print(json.dumps({"output": str(OUTPUT), "input_count": len(records)}, sort_keys=True))
