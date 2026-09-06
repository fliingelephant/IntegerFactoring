#!/usr/bin/env python3

from math import gcd, isqrt
from pathlib import Path


PREREG_SHA = "0ae27d2388282828ca10150d13abe5213a81d718f1a7d28d9eb899579dd5f412"
CORRIGENDUM_SHA = "ddea9130f780d44acf7234628fbb6cd646227359c6a3b6eafa92420ae608b2cd"
MENU_MASK = {
    "K": 1,
    "R": 2,
    "C": 4,
    "KR": 3,
    "KC": 5,
    "RC": 6,
    "KRC": 7,
}
ROWS = (
    (
        "F236_combined_word_worst",
        4190987,
        4243619,
        None,
        "published F236 combined-word minimum residual 2095493",
    ),
    (
        "F236_cubic_carry_worst",
        3565721,
        6646697,
        None,
        "published F236 best cubic-cap carry magnitude 14",
    ),
    (
        "F237_power_word_obstruction",
        15187245471009208343,
        26569391171797958567,
        (
            ((7593622735504604171, 1),),
            ((37, 1), (359045826645918359, 1)),
        ),
        "published F237 power-word minimum residual >2^58",
    ),
)


def factor(n: int) -> tuple[tuple[int, int], ...]:
    factors = []
    exponent = 0
    while n % 2 == 0:
        n //= 2
        exponent += 1
    if exponent:
        factors.append((2, exponent))
    divisor = 3
    while divisor <= isqrt(n):
        exponent = 0
        while n % divisor == 0:
            n //= divisor
            exponent += 1
        if exponent:
            factors.append((divisor, exponent))
        divisor += 2
    if n > 1:
        factors.append((n, 1))
    return tuple(factors)


def factor_text(factors: tuple[tuple[int, int], ...]) -> str:
    if not factors:
        return "1"
    return "*".join(
        str(prime) if exponent == 1 else f"{prime}^{exponent}"
        for prime, exponent in factors
    )


def word_bounds(n: int, factors: list[int]) -> tuple[int, int]:
    lower = 1 + n * sum(value.bit_length() - 1 for value in factors)
    upper = n * sum(value.bit_length() for value in factors)
    return lower, upper


def scan_row(
    name: str,
    p: int,
    q: int,
    certified: tuple[tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]] | None,
    comparison: str,
) -> str:
    N = p * q
    n = N.bit_length()
    d = gcd(p - 1, q - 1)
    residual = ((p - 1) // d, (q - 1) // d)
    if N >> n != 0:
        raise AssertionError("literal endpoint is not zero")

    quotient = [0] * (n + 1)
    remainder = [0] * (n + 1)
    centered = [0] * (n + 1)
    for j in range(1, n + 1):
        quotient[j] = N >> j
        remainder[j] = N - (quotient[j] << j)
        rounded = (N + (1 << (j - 1))) >> j
        centered[j] = N - (rounded << j)
        if not (-(1 << (j - 1)) <= centered[j] < (1 << (j - 1))):
            raise AssertionError("centered range")
        piecewise = (
            remainder[j] - (1 << j)
            if remainder[j] >= (1 << (j - 1))
            else remainder[j]
        )
        if centered[j] != piecewise:
            raise AssertionError("centered convention")
    if not (
        quotient[n] == 0
        and quotient[n - 1] == 1
        and remainder[1] == 1
        and remainder[n] == N
        and centered[1] == -1
        and centered[n] == N - (1 << n)
    ):
        raise AssertionError("endpoint check")

    if certified is None:
        factorizations = (factor(residual[0]), factor(residual[1]))
    else:
        factorizations = certified
        for value, factors in zip(residual, factorizations, strict=True):
            product = 1
            for prime, exponent in factors:
                product *= prime**exponent
            if product != value:
                raise AssertionError("certified factorization product")

    side_results = []
    hit_lines = []
    for side, (s, factors, other) in enumerate(
        zip(residual, factorizations, (q, p), strict=True)
    ):
        remaining = {menu: 1 for menu in MENU_MASK}
        for prime, exponent in factors:
            hits_k = []
            hits_r = []
            hits_c = []
            for j in range(1, n + 1):
                if j < n:
                    direct = quotient[j] % prime == 0
                    interval = N % (prime << j) < (1 << j)
                    local = other % prime == remainder[j] % prime
                    if direct != interval or direct != local:
                        raise AssertionError("quotient incidence")
                    if direct:
                        hits_k.append(j)
                if remainder[j] % prime == 0:
                    hits_r.append(j)
                if centered[j] % prime == 0:
                    hits_c.append(j)
            mask = bool(hits_k) | (bool(hits_r) << 1) | (bool(hits_c) << 2)
            for menu, menu_mask in MENU_MASK.items():
                if not (mask & menu_mask):
                    remaining[menu] *= prime**exponent
            hit_lines.append(
                f"  side={'p' if side == 0 else 'q'} ell={prime} "
                f"K={hits_k} R={hits_r} C={hits_c}"
            )

        products = {"K": 1 % s, "R": 1 % s, "C": 1 % s}
        for j in range(1, n + 1):
            if j < n:
                products["K"] = products["K"] * quotient[j] % s
            products["R"] = products["R"] * remainder[j] % s
            products["C"] = products["C"] * abs(centered[j]) % s
        powered = {key: pow(value, n, s) for key, value in products.items()}
        for menu, mask in MENU_MASK.items():
            word = 1 % s
            for bit, key in ((1, "K"), (2, "R"), (4, "C")):
                if mask & bit:
                    word = word * powered[key] % s
            if s // gcd(s, word) != remaining[menu]:
                raise AssertionError("word residual cross-check")
        side_results.append(remaining)

    factor_lists = {
        "K": quotient[1:n],
        "R": remainder[1 : n + 1],
        "C": [abs(value) for value in centered[1 : n + 1]],
    }
    bounds = {key: word_bounds(n, values) for key, values in factor_lists.items()}
    for menu, mask in MENU_MASK.items():
        if len(menu) == 1:
            continue
        values = []
        for bit, key in ((1, "K"), (2, "R"), (4, "C")):
            if mask & bit:
                values.extend(factor_lists[key])
        bounds[menu] = word_bounds(n, values)

    lines = [
        f"ROW {name}",
        f"p={p} q={q} N={N} n={n} d={d}",
        f"literal_K_n={quotient[n]} literal_word=0 valid_F238_word=no",
        f"sp={residual[0]} ({factor_text(factorizations[0])})",
        f"sq={residual[1]} ({factor_text(factorizations[1])})",
        f"comparison={comparison}",
    ]
    lines.extend(hit_lines)
    for menu in MENU_MASK:
        rp = side_results[0][menu]
        rq = side_results[1][menu]
        lower, upper = bounds[menu]
        lines.append(
            f"  menu={menu} rp={rp} rq={rq} min={min(rp, rq)} "
            f"bitlen_bounds=[{lower},{upper}]"
        )
    return "\n".join(lines)


def main() -> None:
    blocks = [
        f"PREREG_SHA256 {PREREG_SHA}",
        f"PREREG_CORRIGENDUM_SHA256 {CORRIGENDUM_SHA}",
    ]
    for row in ROWS:
        blocks.append(scan_row(*row))
    output = "\n\n".join(blocks) + "\n"
    path = Path(__file__).with_name("named.out")
    path.write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
