#!/usr/bin/env python3
"""Exact verifier for the GCT carry-obstruction certificate.

Uses only Python's standard library: integer arithmetic, modular inversion,
gcd, exact square root, and deterministic Miller--Rabin for 64-bit integers.
"""

from itertools import combinations
from math import gcd, isqrt


def is_prime_64(n: int) -> bool:
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    # Deterministic for all n < 2^64.
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def canonical_data(N: int, c: int) -> tuple[int, int, int, int]:
    assert 1 <= c < N and gcd(c, N) == 1
    w = pow(c, -1, N)
    kappa = (c * w - 1) // N
    assert c * w == 1 + kappa * N
    return c, w, kappa, c * w


def det_bareiss(matrix: list[list[int]]) -> int:
    """Fraction-free exact determinant."""
    a = [row[:] for row in matrix]
    n = len(a)
    assert all(len(row) == n for row in a)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot_value - a[i][k] * a[k][j]
                assert numerator % prev == 0
                a[i][j] = numerator // prev
        prev = pivot_value
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[n - 1][n - 1]


def rank_mod_prime(matrix: list[list[int]], p: int) -> int:
    a = [[x % p for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][col] != 0), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(x * inv) % p for x in a[rank]]
        for i in range(rows):
            if i != rank and a[i][col] != 0:
                factor = a[i][col]
                a[i] = [
                    (a[i][j] - factor * a[rank][j]) % p
                    for j in range(cols)
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def gcd_free_blocks(values: list[int]) -> list[int]:
    """Refine values into pairwise-coprime blocks using gcd and exact division."""
    blocks = sorted(set(x for x in values if x > 1))
    while True:
        split = None
        for i, a in enumerate(blocks):
            for j in range(i + 1, len(blocks)):
                b = blocks[j]
                g = gcd(a, b)
                if g != 1:
                    split = (i, j, g)
                    break
            if split is not None:
                break
        if split is None:
            break
        i, j, g = split
        a, b = blocks[i], blocks[j]
        new_blocks = [x for t, x in enumerate(blocks) if t not in (i, j)]
        for x in (g, a // g, b // g):
            if x > 1 and x not in new_blocks:
                new_blocks.append(x)
        blocks = sorted(new_blocks)

    for i, a in enumerate(blocks):
        for b in blocks[i + 1 :]:
            assert gcd(a, b) == 1
    for value in values:
        remainder = value
        for block in blocks:
            while remainder % block == 0:
                remainder //= block
        assert remainder == 1
    return blocks


def parity_row_masks(values: list[int], blocks: list[int]) -> list[int]:
    rows: list[int] = []
    for block in blocks:
        # Exact-square blocks contribute no parity row.
        if isqrt(block) ** 2 == block:
            continue
        mask = 0
        for i, value in enumerate(values):
            x = value
            exponent = 0
            while x % block == 0:
                x //= block
                exponent += 1
            if exponent & 1:
                mask |= 1 << i
        if mask:
            rows.append(mask)
    return rows


def gf2_rank(row_masks: list[int], column_count: int) -> int:
    rows = [row for row in row_masks if row]
    rank = 0
    for col in range(column_count):
        pivot = next(
            (i for i in range(rank, len(rows)) if (rows[i] >> col) & 1),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(len(rows)):
            if i != rank and ((rows[i] >> col) & 1):
                rows[i] ^= rows[rank]
        rank += 1
        if rank == column_count:
            break
    return rank


def main() -> None:
    p = 1_847
    q = 2_621
    N = 4_840_987
    assert N == p * q
    assert is_prime_64(p) and is_prime_64(q)

    n = N.bit_length()
    trial_bound = n * n
    assert n == 23
    assert min(p, q) > trial_bound

    # Public static source: a = 2,...,4n and j = 1,...,4.
    B = 4 * n
    exact_values: dict[int, tuple[int, int, int, int, int]] = {}
    source_positions = 0
    for a in range(2, B + 1):
        assert gcd(a, N) == 1
        for j in range(1, 5):
            c = pow(a, j, N)
            c, w, kappa, exact = canonical_data(N, c)
            source_positions += 1
            assert gcd(c - w, N) == 1
            assert gcd(c + w, N) == 1
            exact_values.setdefault(exact, (a, j, c, w, kappa))

    relations = list(exact_values)
    assert source_positions == 364
    assert len(relations) == 240

    # Complete factor-free square decoder for the static source.
    blocks = gcd_free_blocks(relations)
    assert len(blocks) == 267
    assert not any(isqrt(b) ** 2 == b for b in blocks)
    rows = parity_row_masks(relations, blocks)
    parity_rank = gf2_rank(rows, len(relations))
    assert parity_rank == len(relations) == 240
    kernel_dimension = len(relations) - parity_rank
    assert kernel_dimension == 0

    # Four-step torus/carry obstruction at the publicly scanned seed a=68.
    a = 68
    trajectory = [canonical_data(N, pow(a, j, N)) for j in range(1, 5)]
    expected = [
        (68, 71_191, 1, 4_840_988),
        (4_624, 4_486_079, 4_285, 20_743_629_296),
        (314_432, 3_696_712, 240_109, 1_162_364_547_584),
        (2_017_428, 2_047_711, 853_361, 4_131_109_507_308),
    ]
    assert trajectory == expected

    c1, w1, k1, _ = trajectory[0]
    _, _, k2, _ = trajectory[1]
    _, _, k3, _ = trajectory[2]
    _, _, k4, _ = trajectory[3]
    s = 1 + a + w1
    omega = k4 - k1 + s * (k2 - k3)
    assert s == 71_260
    assert omega == -16_803_964_880
    assert gcd(abs(omega), N) == q

    lift_matrix = [[1, c, w, kappa] for c, w, kappa, _ in trajectory]
    determinant = det_bareiss(lift_matrix)
    assert determinant == 937_401_734_708_188_800
    assert gcd(abs(determinant), N) == q
    assert rank_mod_prime(lift_matrix, p) == 4
    assert rank_mod_prime(lift_matrix, q) == 3

    # Explicit right-null vector modulo q; it is not null modulo p.
    null_vector = (1_590, 1_257, 283, 1)
    assert all(
        sum(row[j] * null_vector[j] for j in range(4)) % q == 0
        for row in lift_matrix
    )
    assert any(
        sum(row[j] * null_vector[j] for j in range(4)) % p != 0
        for row in lift_matrix
    )

    # The base has maximal local order in both hidden fields.
    for prime, prime_divisors in ((p, (2, 13, 71)), (q, (2, 5, 131))):
        assert pow(a, prime - 1, prime) == 1
        for ell in prime_divisors:
            assert pow(a, (prime - 1) // ell, prime) != 1

    # The certificate is not a disguised short order/sign or pairwise collision.
    for t in range(1, 9):
        assert gcd(pow(a, t, N) - 1, N) == 1
        assert gcd(pow(a, t, N) + 1, N) == 1
    residues = [entry[0] for entry in trajectory]
    for x, y in combinations(residues, 2):
        for value in (x - y, x + y, x * y - 1, x * y + 1):
            assert gcd(abs(value), N) == 1

    # Compatibility with the previously proved cyclotomic absorbing family:
    # all carries are equal, so the obstruction vanishes at every CRT factor.
    cyclotomic_N = 2**41 - 1
    cyclotomic_trajectory = [
        canonical_data(cyclotomic_N, pow(2, j, cyclotomic_N))
        for j in range(1, 5)
    ]
    assert [entry[2] for entry in cyclotomic_trajectory] == [1, 1, 1, 1]
    cyclotomic_s = 1 + 2 + cyclotomic_trajectory[0][1]
    cyclotomic_omega = (
        cyclotomic_trajectory[3][2]
        - cyclotomic_trajectory[0][2]
        + cyclotomic_s
        * (cyclotomic_trajectory[1][2] - cyclotomic_trajectory[2][2])
    )
    assert cyclotomic_omega == 0

    print(
        "PASS: GCT carry obstruction",
        {
            "N": N,
            "factors": (p, q),
            "bits": n,
            "trial_bound": trial_bound,
            "static_positions": source_positions,
            "distinct_exact_values": len(relations),
            "gcd_free_blocks": len(blocks),
            "parity_rank": parity_rank,
            "kernel_dimension": kernel_dimension,
            "seed": a,
            "omega": omega,
            "determinant": determinant,
            "rank_mod_p": rank_mod_prime(lift_matrix, p),
            "rank_mod_q": rank_mod_prime(lift_matrix, q),
            "factor": gcd(abs(omega), N),
        },
    )


if __name__ == "__main__":
    main()
