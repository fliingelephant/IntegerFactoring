#!/usr/bin/env python3
"""Search small AKS polynomial stages for CRT-localizing coefficients.

This is discovery code for family F04.  It deliberately factors the small test
inputs, so it is not an implementation of a factoring algorithm.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def distinct_prime_factors(n: int) -> list[int]:
    factors: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        factors.append(n)
    return factors


def is_prime_power(n: int) -> bool:
    return len(distinct_prime_factors(n)) == 1


def euler_phi(n: int) -> int:
    result = n
    for p in distinct_prime_factors(n):
        result -= result // p
    return result


def multiplicative_order(a: int, modulus: int) -> int:
    if math.gcd(a, modulus) != 1:
        return 0
    x = 1
    for order in range(1, euler_phi(modulus) + 1):
        x = x * a % modulus
        if x == 1:
            return order
    raise AssertionError("order did not divide phi")


def aks_r(n: int, max_r: int) -> tuple[int, int]:
    threshold = math.log2(n) ** 2
    for r in range(2, max_r + 1):
        order = multiplicative_order(n % r, r)
        if order > threshold:
            return r, order
    raise RuntimeError(f"no AKS r <= {max_r} for N={n}")


def cyclic_mul(left: list[int], right: list[int], modulus: int) -> list[int]:
    r = len(left)
    result = [0] * r
    for i, x in enumerate(left):
        if x:
            for j, y in enumerate(right):
                if y:
                    result[(i + j) % r] = (
                        result[(i + j) % r] + x * y
                    ) % modulus
    return result


def cyclic_binomial_error(n: int, r: int, a: int, modulus: int) -> list[int]:
    result = [0] * r
    result[0] = 1
    base = [0] * r
    base[0] = a % modulus
    base[1 % r] = (base[1 % r] + 1) % modulus
    exponent = n
    while exponent:
        if exponent & 1:
            result = cyclic_mul(result, base, modulus)
        exponent >>= 1
        if exponent:
            base = cyclic_mul(base, base, modulus)
    result[n % r] = (result[n % r] - 1) % modulus
    result[0] = (result[0] - a) % modulus
    return result


def analyze(n: int, max_r: int, shift_limit: int | None = None) -> dict[str, object]:
    primes = distinct_prime_factors(n)
    r, order = aks_r(n, max_r)
    shift_bound = math.floor(math.sqrt(euler_phi(r)) * math.log2(n))
    shifts: list[dict[str, object]] = []
    any_separator = False
    any_pass_fail = False
    tested_shift_bound = min(shift_bound, shift_limit or shift_bound)
    for a in range(1, tested_shift_bound + 1):
        coeffs = cyclic_binomial_error(n, r, a, n)
        gcds = sorted({math.gcd(c, n) for c in coeffs})
        separators = [g for g in gcds if 1 < g < n]
        local_zero = {
            str(p): all(c % p == 0 for c in coeffs) for p in primes
        }
        pass_fail = len(set(local_zero.values())) > 1
        any_separator |= bool(separators)
        any_pass_fail |= pass_fail
        shifts.append(
            {
                "a": a,
                "gcds": gcds,
                "separators": separators,
                "local_zero": local_zero,
                "nonzero_supports": sorted(
                    {
                        tuple(p for p in primes if c % p != 0)
                        for c in coeffs
                        if c % n != 0
                    }
                ),
            }
        )
    return {
        "N": n,
        "prime_factors": primes,
        "r": r,
        "order": order,
        "log2_squared": math.log2(n) ** 2,
        "phi_r": euler_phi(r),
        "shift_bound": shift_bound,
        "tested_shift_bound": tested_shift_bound,
        "aks_trial_gcd_would_stop": min(primes) <= r,
        "any_separator": any_separator,
        "any_pass_fail": any_pass_fail,
        "shifts": shifts,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=6)
    parser.add_argument("--stop", type=int, default=200)
    parser.add_argument("--max-r", type=int, default=1000)
    parser.add_argument("--numbers", type=int, nargs="*")
    parser.add_argument("--shift-limit", type=int)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    records = []
    candidates = args.numbers or range(args.start, args.stop + 1)
    for n in candidates:
        if len(distinct_prime_factors(n)) >= 2 and not is_prime_power(n):
            record = analyze(n, args.max_r, args.shift_limit)
            records.append(record)
            print(
                f"N={n} r={record['r']} A={record['shift_bound']} "
                f"separator={record['any_separator']} "
                f"pass_fail={record['any_pass_fail']} "
                f"pre_gcd={record['aks_trial_gcd_would_stop']}"
            )
    args.output.write_text(json.dumps(records, indent=2) + "\n")


if __name__ == "__main__":
    main()
