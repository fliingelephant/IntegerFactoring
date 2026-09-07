#!/usr/bin/env python3
"""Dyadic Vandermonde-band products: exact reference and fast constructor."""

from functools import lru_cache
import json
import math
from pathlib import Path
import random
import resource
import signal
import time

BASE = Path(__file__).resolve().parent


@lru_cache(None)
def elementary(s, degree):
    length = 1 << s
    power = []
    for j in range(degree + 1):
        power.append((length ** (j + 1) - sum(
            math.comb(j + 1, r) * power[r] for r in range(j)
        )) // (j + 1))
    values = [1]
    for j in range(1, degree + 1):
        numerator = sum((-1) ** (r - 1) * values[j - r] * power[r]
                        for r in range(1, j + 1))
        assert numerator % j == 0
        values.append(numerator // j)
    return tuple(values)


def fast_bands(s, A, B, C, n, c, d, precision):
    length = 1 << s
    modulus = 1 << precision
    valuation = (C & -C).bit_length() - 1
    degree = min(length, (precision - 1) // valuation)
    coeffs = elementary(s, degree)
    base = B + C * c
    ratio = C * pow(base, -1, modulus) % modulus
    correction = 0
    for coefficient in reversed(coeffs):
        correction = (correction * ratio + coefficient) % modulus
    product = pow(base, length, modulus) * correction % modulus
    determinant = A * B + C * n
    sign_exponent = n + c + d + (-determinant - 1) // 2 + C // 2
    sign = -1 if sign_exponent & 1 else 1
    first = (sign * product * pow(-determinant, -length // 2, modulus)) % modulus
    result = [first]
    for _ in range(1, s):
        result.append(result[-1] ** 2 % modulus)
    return result, {"coefficient_degree": degree,
                    "canonical_points_enumerated": 0, "pairs_enumerated": 0}


def direct_bands(s, A, B, C, n, c, d, precision):
    length = 1 << s
    modulus = 1 << precision
    xs = [c + i for i in range(length)]
    denominators = [B + C * x for x in xs]
    ys = [(n - A * x) * pow(D, -1, length) % length
          for x, D in zip(xs, denominators)]
    ys = [y + length * (y < d) for y in ys]
    result = [1] * s
    orientation = [1] * s
    determinant = A * B + C * n
    pairs = 0
    for i in range(length):
        for j in range(i + 1, length):
            difference = j - i
            valuation = (difference & -difference).bit_length() - 1
            dy = ys[j] - ys[i]
            assert (abs(dy) & -abs(dy)).bit_length() - 1 == valuation
            band = s - valuation - 1
            factor = (
                (dy >> valuation) * denominators[i] * denominators[j]
                * pow(-determinant * (difference >> valuation), -1, modulus)
            ) % modulus
            result[band] = result[band] * factor % modulus
            if dy < 0:
                orientation[band] *= -1
            pairs += 1
    assert orientation[1:] == [1] * (s - 1)
    return result, pairs, orientation[0]


def run():
    started = time.monotonic()
    rng = random.Random(30920260907)
    band_checks = 0
    direct_pairs = 0
    rows = []
    for s in range(2, 8):
        length = 1 << s
        precision = 3 * s + 5
        for _ in range(12):
            A = 2 * rng.randrange(-7, 8) + 1
            B = 2 * rng.randrange(-7, 8) + 1
            C = 2 * rng.randrange(1, 8)
            n = rng.randrange(-4 * length, 12 * length)
            c, d = rng.randrange(length + 1), rng.randrange(length + 1)
            expected, pairs, sign = direct_bands(s, A, B, C, n, c, d, precision)
            actual, counts = fast_bands(s, A, B, C, n, c, d, precision)
            assert actual == expected, (s, A, B, C, n, c, d)
            direct_pairs += pairs
            band_checks += s
            rows.append({"s": s, "A": A, "B": B, "C": C, "n": n,
                         "c": c, "d": d, "precision": precision,
                         "sign": sign, "bands": actual, "constructor": counts})

    # Actual N=289, original M=32; quotient graph has L=16.
    s, A, B, C, n, precision = 4, 1, 1, 2, 144, 24
    modulus = 1 << precision
    graph = [(x, (n - x) * pow(1 + 2 * x, -1, 16) % 16)
             for x in range(16)]
    contrasts = []
    for a, b, c, d in ((8, 9, 8, 9), (1, 2, 1, 2), (0, 16, 0, 16)):
        corners = [fast_bands(s, A, B, C, n, x, y, precision)[0]
                   for x, y in ((b, d), (a, c), (a, d), (b, c))]
        contrast = [corners[0][r] * corners[1][r]
                    * pow(corners[2][r] * corners[3][r], -1, modulus) % modulus
                    for r in range(s)]
        count = sum(a <= x < b and c <= y < d for x, y in graph)
        assert contrast == [1] * s
        contrasts.append({"rectangle": [a, b, c, d], "exact_count": count,
                          "multiplicative_contrasts": contrast})
    assert [x["exact_count"] for x in contrasts] == [1, 0, 16]

    original_k = 65
    original_modulus = 1 << original_k
    original_N = 9 * original_modulus + 1
    s = original_k - 1
    length = 1 << s
    assert 1 << ((original_N // 8).bit_length() - 1) == original_modulus
    large_started = time.monotonic()
    values, counts = fast_bands(
        s, 1, 1, 2, (original_N - 1) // 2,
        length // 3, length // 5, 128,
    )
    large = {"original_N": original_N, "original_M": original_modulus,
             "L": length, "s": s, "c": length // 3, "d": length // 5,
             "precision": 128, "bands": values, "constructor": counts,
             "elapsed_seconds": time.monotonic() - large_started,
             "verification": "Computed from the formula; no independent large pair enumeration."}
    return {"status": "passed", "band_checks": band_checks,
            "direct_reference_pairs": direct_pairs, "rows": rows,
            "selected_window_witnesses": contrasts, "large_case": large,
            "elapsed_seconds": time.monotonic() - started,
            "peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "timeout_seconds": 30,
            "scope": "Complete pair products only; no shifted B or rectangle evaluator."}


if __name__ == "__main__":
    signal.alarm(30)
    result = run()
    text = json.dumps(result, indent=2) + "\n"
    with (BASE / "output.json").open("x") as out:
        out.write(text)
    print(text, end="")
