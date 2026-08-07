import json
import math
import platform
import time
from pathlib import Path


RUN = "F65-D01"
FAMILY = "F26/F62"
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


def collect_offset_relations(modulus):
    bit_length = modulus.bit_length()
    records = []
    direct_events = []
    for offset in range(1, bit_length + 1):
        state = modulus - offset
        for step in range(bit_length):
            if state == 1:
                break
            divisor = math.gcd(state, modulus)
            if 1 < divisor < modulus:
                direct_events.append(
                    {"offset": offset, "step": step, "state": state, "divisor": divisor}
                )
                break
            inverse = pow(state, -1, modulus)
            quotient = (state * inverse - 1) // modulus
            assert state * inverse == 1 + quotient * modulus
            assert 0 <= quotient < state
            records.append(
                {
                    "offset": offset,
                    "step": step,
                    "u": state,
                    "v": inverse,
                    "k": quotient,
                }
            )
            state = quotient
        else:
            divisor = math.gcd(state, modulus)
            if 1 < divisor < modulus:
                direct_events.append(
                    {
                        "offset": offset,
                        "step": bit_length,
                        "state": state,
                        "divisor": divisor,
                    }
                )
    return records, direct_events


def gcd_free_blocks(values):
    blocks = sorted(set(value for value in values if value > 1))
    while True:
        split = None
        for left_index in range(len(blocks)):
            for right_index in range(left_index + 1, len(blocks)):
                divisor = math.gcd(blocks[left_index], blocks[right_index])
                if divisor != 1:
                    split = (left_index, right_index, divisor)
                    break
            if split is not None:
                break
        if split is None:
            break
        left_index, right_index, divisor = split
        left = blocks[left_index]
        right = blocks[right_index]
        retained = [
            value
            for index, value in enumerate(blocks)
            if index not in (left_index, right_index)
        ]
        retained.extend((divisor, left // divisor, right // divisor))
        blocks = sorted(set(value for value in retained if value > 1))

    for left_index in range(len(blocks)):
        for right_index in range(left_index + 1, len(blocks)):
            assert math.gcd(blocks[left_index], blocks[right_index]) == 1
    return blocks


def exponent_budgets(values, blocks):
    budgets = [0] * len(blocks)
    for value in values:
        remainder = value
        for index, block in enumerate(blocks):
            while remainder % block == 0:
                budgets[index] += 1
                remainder //= block
        assert remainder == 1
    return budgets


def screens(residue, modulus):
    minus = math.gcd(residue - 1, modulus)
    plus = math.gcd(residue + 1, modulus)
    proper = sorted(set(value for value in (minus, plus) if 1 < value < modulus))
    return proper


def scan_variant(modulus, candidates):
    seen = set()
    candidate_count = 0
    screen_hits = 0
    self_inverse_count = 0
    first_hit = None
    for residue, certificate in candidates:
        if residue in seen:
            continue
        seen.add(residue)
        candidate_count += 1
        divisors = screens(residue, modulus)
        if residue * residue % modulus == 1 and residue not in (1, modulus - 1):
            self_inverse_count += 1
        if divisors:
            screen_hits += 1
            if first_hit is None:
                first_hit = {
                    "residue": residue,
                    "divisors": divisors,
                    "certificate": certificate,
                    "self_inverse": residue * residue % modulus == 1,
                }
    return {
        "candidate_count": candidate_count,
        "first_hit": first_hit,
        "screen_hit_count": screen_hits,
        "self_inverse_count": self_inverse_count,
        "unique_residue_count": len(seen),
    }


def analyze_variant(modulus, records, retain_duplicates):
    if retain_duplicates:
        retained = [record for record in records if record["k"] != 0]
    else:
        first_by_quotient = {}
        for record in records:
            if record["k"] != 0 and record["k"] not in first_by_quotient:
                first_by_quotient[record["k"]] = record
        retained = list(first_by_quotient.values())

    endpoints = []
    for record in retained:
        endpoints.extend((record["u"], record["v"]))
    blocks = gcd_free_blocks(endpoints)
    budgets = exponent_budgets(endpoints, blocks)
    assert all(math.gcd(block, modulus) == 1 for block in blocks)

    def block_candidates():
        for index, block in enumerate(blocks):
            yield block, {"kind": "block", "block": block, "index": index}

    def legal_pair_candidates():
        for left_index, left in enumerate(blocks):
            if budgets[left_index] >= 2 and left * left < modulus:
                yield left * left, {
                    "kind": "legal_square",
                    "blocks": [left, left],
                    "indices": [left_index, left_index],
                }
            for right_index in range(left_index + 1, len(blocks)):
                right = blocks[right_index]
                product = left * right
                if product < modulus:
                    yield product, {
                        "kind": "legal_pair",
                        "blocks": [left, right],
                        "indices": [left_index, right_index],
                    }

    def single_power_candidates():
        for index, block in enumerate(blocks):
            value = 1
            for exponent in range(1, budgets[index] + 1):
                value *= block
                if value >= modulus:
                    break
                yield value, {
                    "kind": "legal_power",
                    "block": block,
                    "index": index,
                    "exponent": exponent,
                }

    def signed_pair_candidates():
        powers = []
        for index, block in enumerate(blocks):
            powers.append((index, block, pow(block, -1, modulus)))
        for index, positive, inverse in powers:
            yield positive, {"kind": "signed_single", "index": index, "sign": 1}
            yield inverse, {"kind": "signed_single", "index": index, "sign": -1}
        for left_position in range(len(powers)):
            left_index, left_positive, left_inverse = powers[left_position]
            for right_position in range(left_position + 1, len(powers)):
                right_index, right_positive, right_inverse = powers[right_position]
                for left_sign, left_value in ((1, left_positive), (-1, left_inverse)):
                    for right_sign, right_value in ((1, right_positive), (-1, right_inverse)):
                        yield left_value * right_value % modulus, {
                            "kind": "signed_pair",
                            "indices": [left_index, right_index],
                            "signs": [left_sign, right_sign],
                            "blocks": [blocks[left_index], blocks[right_index]],
                        }

    return {
        "block_count": len(blocks),
        "blocks": blocks,
        "exponent_budgets": budgets,
        "relation_count": len(retained),
        "block_screens": scan_variant(modulus, block_candidates()),
        "legal_pair_screens": scan_variant(modulus, legal_pair_candidates()),
        "single_power_screens": scan_variant(modulus, single_power_candidates()),
        "signed_pair_screens": scan_variant(modulus, signed_pair_candidates()),
    }


def main():
    started = time.monotonic()
    records = []
    for target_bits in TARGET_FACTOR_BITS:
        p = next_prime(1 << target_bits)
        for numerator, denominator in RATIOS:
            lower_bound = max(p + 2, (numerator * p + denominator - 1) // denominator)
            q = next_prime(lower_bound)
            modulus = p * q
            raw, direct_events = collect_offset_relations(modulus)
            print(
                f"input N={modulus} bits={modulus.bit_length()} raw={len(raw)} "
                f"direct={len(direct_events)}",
                flush=True,
            )
            variants = {}
            for name, retain_duplicates in (("unique", False), ("raw", True)):
                variant_started = time.monotonic()
                variants[name] = analyze_variant(modulus, raw, retain_duplicates)
                print(
                    f"variant={name} blocks={variants[name]['block_count']} "
                    f"elapsed={time.monotonic() - variant_started:.6f}",
                    flush=True,
                )
            records.append(
                {
                    "N": modulus,
                    "direct_events": direct_events,
                    "input_bits": modulus.bit_length(),
                    "p": p,
                    "q": q,
                    "ratio": [numerator, denominator],
                    "raw_relation_count": len(raw),
                    "target_factor_bits": target_bits,
                    "variants": variants,
                }
            )

    output = {
        "disposition": (
            "Finite discovery and certificate evidence only. Hits do not prove an "
            "all-input law; misses do not refute wider support, larger exponents, "
            "different transcripts, or later feedback rounds."
        ),
        "elapsed_seconds": time.monotonic() - started,
        "family": FAMILY,
        "platform": platform.platform(),
        "python": platform.python_version(),
        "records": records,
        "run": RUN,
        "source": "deterministic offset prefixes with n starts and n-step cap",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("x", encoding="utf-8") as handle:
        json.dump(output, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(f"wrote={OUTPUT} elapsed={output['elapsed_seconds']:.6f}", flush=True)


if __name__ == "__main__":
    main()

