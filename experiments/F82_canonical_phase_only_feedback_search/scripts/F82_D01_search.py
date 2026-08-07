#!/usr/bin/env python3

import json
import math
from pathlib import Path


PRIME_LIMIT = 149
BASE_LIMIT = 64


def primes_through(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for value in range(2, math.isqrt(limit) + 1):
        if sieve[value]:
            for multiple in range(value * value, limit + 1, value):
                sieve[multiple] = False
    return [value for value, keep in enumerate(sieve) if keep]


def multiplicative_order(value, prime):
    residue = value % prime
    current = 1
    for order in range(1, prime):
        current = current * residue % prime
        if current == 1:
            return order
    raise AssertionError("unit order not found")


def proper_factor(value, modulus):
    divisor = math.gcd(value, modulus)
    return divisor if 1 < divisor < modulus else None


def pairwise_coprime(values):
    return all(
        math.gcd(values[left], values[right]) == 1
        for left in range(len(values))
        for right in range(left + 1, len(values))
    )


def main():
    primes = [prime for prime in primes_through(PRIME_LIMIT) if prime >= 5]
    moduli = sorted(
        (p * q, p, q)
        for index, p in enumerate(primes)
        for q in primes[index + 1 :]
    )
    counts = {
        "moduli": 0,
        "bases": 0,
        "equal_order_bases": 0,
        "old_states": 0,
        "feedback_pairs": 0,
        "proper_refinements": 0,
        "new_equal_order_blocks": 0,
    }
    witness = None

    for modulus, p, q in moduli:
        counts["moduli"] += 1
        for base in range(2, min(BASE_LIMIT, modulus - 1) + 1):
            if math.gcd(base, modulus) != 1:
                continue
            counts["bases"] += 1
            order_p = multiplicative_order(base, p)
            order_q = multiplicative_order(base, q)
            if order_p != order_q or order_p < 3:
                continue
            counts["equal_order_bases"] += 1
            order = order_p
            powers = [pow(base, exponent, modulus) for exponent in range(order)]
            assert len(set(powers)) == order

            for old_exponent in range(2, order):
                old_endpoint = powers[old_exponent]
                old_inverse = powers[(-old_exponent) % order]
                base_inverse = powers[-1]
                old_endpoints = [base, base_inverse, old_endpoint, old_inverse]
                if min(old_endpoints) <= 1 or len(set(old_endpoints)) != 4:
                    continue
                if not pairwise_coprime(old_endpoints):
                    continue
                counts["old_states"] += 1

                for feedback_exponent in range(1, order):
                    selected = powers[feedback_exponent]
                    inverse = powers[(-feedback_exponent) % order]
                    if (
                        selected <= 1
                        or inverse <= 1
                        or selected in old_endpoints
                        or inverse in old_endpoints
                        or selected == inverse
                    ):
                        continue
                    if (
                        proper_factor(selected - 1, modulus)
                        or proper_factor(selected + 1, modulus)
                        or proper_factor(inverse - 1, modulus)
                        or proper_factor(inverse + 1, modulus)
                        or proper_factor(selected - inverse, modulus)
                    ):
                        continue
                    counts["feedback_pairs"] += 1

                    appended = [selected, inverse]
                    for old_index, old_value in enumerate(old_endpoints):
                        for new_index, new_value in enumerate(appended):
                            block = math.gcd(old_value, new_value)
                            if not (1 < block < old_value and block < new_value):
                                continue
                            counts["proper_refinements"] += 1
                            if math.gcd(block, modulus) != 1:
                                continue

                            other_values = [
                                value
                                for index, value in enumerate(old_endpoints)
                                if index != old_index
                            ]
                            other_values.append(appended[1 - new_index])
                            if any(math.gcd(block, value) != 1 for value in other_values):
                                continue

                            block_order_p = multiplicative_order(block, p)
                            block_order_q = multiplicative_order(block, q)
                            if block_order_p != block_order_q:
                                continue
                            if block in powers:
                                continue
                            counts["new_equal_order_blocks"] += 1

                            block_order = block_order_p
                            mixed = None
                            for block_exponent in range(1, block_order):
                                block_power = pow(block, block_exponent, modulus)
                                for old_power_exponent in range(order):
                                    residue = (
                                        block_power * powers[old_power_exponent]
                                    ) % modulus
                                    factor = proper_factor(residue - 1, modulus)
                                    if factor is not None:
                                        mixed = {
                                            "block_exponent": block_exponent,
                                            "old_power_exponent": old_power_exponent,
                                            "residue": residue,
                                            "factor": factor,
                                            "sign": 1,
                                        }
                                        break
                                    factor = proper_factor(residue + 1, modulus)
                                    if factor is not None:
                                        mixed = {
                                            "block_exponent": block_exponent,
                                            "old_power_exponent": old_power_exponent,
                                            "residue": residue,
                                            "factor": factor,
                                            "sign": -1,
                                        }
                                        break
                                if mixed is not None:
                                    break
                            if mixed is None:
                                continue

                            witness = {
                                "N": modulus,
                                "p": p,
                                "q": q,
                                "base": base,
                                "old_local_order": order,
                                "old_exponent": old_exponent,
                                "old_endpoints": old_endpoints,
                                "old_relation_quotients": [
                                    (base * base_inverse - 1) // modulus,
                                    (old_endpoint * old_inverse - 1) // modulus,
                                ],
                                "feedback_exponent": feedback_exponent,
                                "selected": selected,
                                "canonical_inverse": inverse,
                                "feedback_quotient": (
                                    selected * inverse - 1
                                )
                                // modulus,
                                "split_old_endpoint_index": old_index,
                                "split_new_endpoint": (
                                    "selected" if new_index == 0 else "canonical_inverse"
                                ),
                                "new_block": block,
                                "new_block_local_order": block_order,
                                "new_block_in_old_subgroup": False,
                                "mixed_certificate": mixed,
                            }
                            break
                        if witness is not None:
                            break
                    if witness is not None:
                        break
                if witness is not None:
                    break
            if witness is not None:
                break
        if witness is not None:
            break

    payload = {
        "run": "F82-D01",
        "prime_limit": PRIME_LIMIT,
        "base_limit": BASE_LIMIT,
        "enumeration_order": "increasing N, then base, old exponent, feedback exponent",
        "counts_before_stop": counts,
        "witness": witness,
    }
    output_path = Path(__file__).resolve().parents[1] / "output" / "F82-D01.json"
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
