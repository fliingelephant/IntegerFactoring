#!/usr/bin/env python3
"""Independent exact verifier for RECONSTRUCTION_STATEMENT.md.

This program uses only Python integer arithmetic and the Euclidean algorithm.
Primality is certified recursively with Lucas's primality criterion.
"""

from __future__ import annotations

import hashlib
import math
import pathlib
import sys


HERE = pathlib.Path(__file__).resolve().parent
STATEMENT = HERE / "RECONSTRUCTION_STATEMENT.md"
SOURCE = pathlib.Path(__file__).resolve()

# Complete factorizations of n - 1.  The leaves terminate at the prime 2.
LUCAS_FACTORS: dict[int, dict[int, int]] = {
    3: {2: 1},
    5: {2: 2},
    7: {2: 1, 3: 1},
    11: {2: 1, 5: 1},
    17: {2: 4},
    29: {2: 2, 7: 1},
    1871: {2: 1, 5: 1, 11: 1, 17: 1},
    34511: {2: 1, 5: 1, 7: 1, 17: 1, 29: 1},
}


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def factor_product(factors: dict[int, int]) -> int:
    product = 1
    for prime, exponent in factors.items():
        product *= prime**exponent
    return product


def lucas_witness(n: int, prime_divisors: tuple[int, ...]) -> int:
    for a in range(2, n):
        if pow(a, n - 1, n) == 1 and all(
            math.gcd(pow(a, (n - 1) // q, n) - 1, n) == 1
            for q in prime_divisors
        ):
            return a
    raise AssertionError(f"no Lucas witness found for {n}")


def emit_lucas_certificate(n: int, proved: set[int]) -> None:
    if n in proved:
        return
    if n == 2:
        print("LUCAS n=2 base_prime=true")
        proved.add(n)
        return

    factors = LUCAS_FACTORS[n]
    assert factor_product(factors) == n - 1
    for q in sorted(factors):
        emit_lucas_certificate(q, proved)

    divisors = tuple(sorted(factors))
    witness = lucas_witness(n, divisors)
    fermat = pow(witness, n - 1, n)
    residues = {q: pow(witness, (n - 1) // q, n) for q in divisors}
    gcd_checks = {
        q: math.gcd(residues[q] - 1, n)
        for q in divisors
    }
    assert fermat == 1
    assert all(value == 1 for value in gcd_checks.values())
    factor_text = "*".join(
        str(q) if exponent == 1 else f"{q}^{exponent}"
        for q, exponent in sorted(factors.items())
    )
    gcd_text = ",".join(
        f"q={q}:res={residues[q]}:gcd={gcd_checks[q]}" for q in divisors
    )
    print(
        f"LUCAS n={n} n-1={factor_text} witness={witness} "
        f"pow={fermat} checks=[{gcd_text}]"
    )
    proved.add(n)


def multiplicative_order(a: int, modulus: int, bound: int) -> int:
    value = 1
    for exponent in range(1, bound + 1):
        value = value * a % modulus
        if value == 1:
            return exponent
    raise AssertionError("order exceeds supplied bound")


def main() -> None:
    print("RECONSTRUCT verifier: Python exact integers; no primality library", file=sys.stderr)
    print("runner=/opt/homebrew/bin/timeout --verbose 20s /opt/homebrew/bin/python3", file=sys.stderr)
    print(f"statement_sha256={sha256(STATEMENT)}", file=sys.stderr)
    print(f"source_sha256={sha256(SOURCE)}", file=sys.stderr)

    p = 1871
    q = 34511
    N = (3**17 - 1) // 2
    assert N == 64_570_081 == p * q
    print(f"IDENTITY N={N} 3^17={3**17} factors={p}*{q}")

    proved: set[int] = set()
    emit_lucas_certificate(p, proved)
    emit_lucas_certificate(q, proved)

    n = N.bit_length()
    trial_bound = n * n
    assert n == 26 and trial_bound == 676
    assert p > trial_bound and q > trial_bound
    print(
        f"SIZE bitlength={n} square={trial_bound} "
        f"2^25={2**25} N={N} 2^26={2**26} "
        f"factors_above_bound={p > trial_bound and q > trial_bound}"
    )

    g = math.gcd(p - 1, q - 1)
    A = (p - 1) // g
    B = (q - 1) // g
    coprime = math.gcd(A * B, N - 1)
    assert (g, A, B, coprime) == (170, 11, 203, 1)
    print(f"DECOMPOSITION g={g} A={A} B={B} AB={A * B} gcd(AB,N-1)={coprime}")

    orders = {
        p: multiplicative_order(3, p, 17),
        q: multiplicative_order(3, q, 17),
        N: multiplicative_order(3, N, 17),
    }
    assert all(order == 17 for order in orders.values())
    print("ORDERS " + " ".join(f"ord_3_mod_{modulus}={order}" for modulus, order in orders.items()))

    residues = [pow(3, exponent, N) for exponent in range(677)]
    assert len(set(residues)) == 17
    assert residues[:17] == [3**exponent for exponent in range(17)]
    assert all(residues[exponent] == residues[exponent % 17] for exponent in range(677))
    print(f"ORBIT exponents=0..676 distinct_residues={len(set(residues))}")

    relation_rows: list[str] = []
    for r in range(1, 17):
        c = 3**r
        w = 3 ** (17 - r)
        minus = math.gcd(c - w, N)
        plus = math.gcd(c + w, N)
        assert c < N and w < N
        assert c * w == 3**17 == 1 + 2 * N
        assert (c * w) % N == 1
        assert minus == plus == 1
        relation_rows.append(f"r={r}:c={c}:w={w}:gcd-={minus}:gcd+={plus}")
    print(f"RELATION common_value={3**17}=1+2N rows=[{' ; '.join(relation_rows)}]")
    print("VERDICT PASS")
    print("RECONSTRUCT verifier completed successfully", file=sys.stderr)


if __name__ == "__main__":
    main()
