#!/usr/bin/env python3
import math
import time


START = time.monotonic()


def primes_upto(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


SMALL_PRIMES = primes_upto(1_000_000)


def parity_class(value):
    odd = set()
    remaining = value
    for prime in SMALL_PRIMES:
        if prime * prime > remaining:
            break
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent ^= 1
        if exponent:
            odd.add(prime)
    if remaining > 1:
        odd.add(remaining)
    return odd


def subset_product(records, mask):
    product = 1
    supplied = 1
    ids = []
    for i, row in enumerate(records):
        if mask >> i & 1:
            product *= row["A"]
            supplied = supplied * row["x"] % row["N"]
            ids.append(row["j"])
    return product, supplied, ids


def first_dependency(records):
    prime_bits = {}
    next_bit = 0
    pivots = {}
    for index, row in enumerate(records):
        vector = 0
        for prime in parity_class(row["A"]):
            if prime not in prime_bits:
                prime_bits[prime] = next_bit
                next_bit += 1
            vector ^= 1 << prime_bits[prime]
        combination = 1 << index
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = (vector, combination)
                break
            old_vector, old_combination = pivots[pivot]
            vector ^= old_vector
            combination ^= old_combination
        if not vector:
            return combination
    return None


def main():
    primes = primes_upto(1000)
    tested = 0
    generated = 0
    retained = 0
    screens = 0
    for p in primes:
        if p < 3 or p > 500:
            continue
        for q in primes:
            if not p < q < 2 * p:
                continue
            if time.monotonic() - START > 60:
                print({"status": "timeout", "tested": tested, "generated": generated, "retained": retained})
                return
            N = p * q
            n = N.bit_length()
            S, T = 1, 0
            seen = {}
            records = []
            direct = []
            for j in range(4 * n + 1):
                assert S * S - 2 * T * T == 1
                y = T % N
                x = S % N
                A = 1 + 2 * y * y
                generated += 1
                if j:
                    g = math.gcd(x, N)
                    if 1 < g < N:
                        direct.append((j, "root", g))
                        screens += 1
                    else:
                        R = math.isqrt(A)
                        if R * R == A:
                            for sign, value in (("minus", R - x), ("plus", R + x)):
                                h = math.gcd(value % N, N)
                                if 1 < h < N:
                                    direct.append((j, "square_" + sign, h))
                                    screens += 1
                        elif y in seen:
                            old = seen[y]
                            for sign, value in (("minus", x - old), ("plus", x + old)):
                                h = math.gcd(value % N, N)
                                if 1 < h < N:
                                    direct.append((j, "duplicate_" + sign, h))
                                    screens += 1
                        else:
                            seen[y] = x
                            records.append({"N": N, "j": j, "y": y, "x": x, "A": A})
                            retained += 1
                S, T = 3 * S + 4 * T, 2 * S + 3 * T
            tested += 1
            mask = first_dependency(records)
            if mask is not None:
                product, supplied, ids = subset_product(records, mask)
                root = math.isqrt(product)
                assert root * root == product
                assert root * root % N == supplied * supplied % N
                minus = math.gcd((root - supplied) % N, N)
                plus = math.gcd((root + supplied) % N, N)
                rows = [records[i] for i in range(len(records)) if mask >> i & 1]
                print({
                    "status": "witness",
                    "p": p,
                    "q": q,
                    "N": N,
                    "n": n,
                    "support_j": ids,
                    "rows": rows,
                    "root": root,
                    "supplied": supplied,
                    "gcd_minus": minus,
                    "gcd_plus": plus,
                    "earlier_screens": direct,
                    "tested": tested,
                    "generated": generated,
                    "retained": retained,
                    "wall_seconds": time.monotonic() - START,
                })
                return
    print({"status": "null", "tested": tested, "generated": generated, "retained": retained, "screens": screens, "wall_seconds": time.monotonic() - START})


if __name__ == "__main__":
    main()
