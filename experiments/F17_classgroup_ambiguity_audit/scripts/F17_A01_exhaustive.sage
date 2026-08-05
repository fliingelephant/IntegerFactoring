from itertools import product
from json import dump
from math import gcd, lcm
from pathlib import Path
from sys import argv

from sage.all import is_prime


FAMILY = "F17"
RUN = "F17_A01"


def reduced_forms(D):
    """Enumerate canonical primitive positive reduced forms of D."""
    forms = []
    # Reducedness implies 3*a^2 <= |D|.
    a_max = int((abs(D) // 3) ** 0.5) + 2
    while 3 * a_max * a_max > abs(D):
        a_max -= 1
    while 3 * (a_max + 1) * (a_max + 1) <= abs(D):
        a_max += 1
    for a in range(1, a_max + 1):
        for b in range(-a, a + 1):
            numerator = b * b - D
            if numerator % (4 * a):
                continue
            c = numerator // (4 * a)
            if a > c:
                continue
            if b < 0 and (abs(b) == a or a == c):
                continue
            if gcd(gcd(a, abs(b)), c) != 1:
                continue
            forms.append((a, b, c))
    return sorted(forms)


def expected_ambiguous(p, q):
    N = p * q
    if N % 4 == 3:
        expected = [(1, 1, (N + 1) // 4)]
        if q > 3 * p:
            expected.append((p, p, (p + q) // 4))
        else:
            expected.append(((p + q) // 4, (q - p) // 2, (p + q) // 4))
        return -N, sorted(expected)

    expected = [(1, 0, N), (2, 2, (N + 1) // 2), (p, 0, q)]
    if q > 3 * p:
        expected.append((2 * p, 2 * p, (p + q) // 2))
    else:
        expected.append(((p + q) // 2, q - p, (p + q) // 2))
    return -4 * N, sorted(expected)


def extracted_pair(D, form):
    a, b, c = form
    N = abs(D) if D % 2 else abs(D) // 4
    if b == 0:
        pair = (a, c)
    elif b == a:
        if D % 2:
            pair = (a, 4 * c - a)
        else:
            pair = (a // 2, (4 * c - a) // 2)
    elif a == c:
        if D % 2:
            pair = (2 * a - b, 2 * a + b)
        else:
            pair = (a - b // 2, a + b // 2)
    else:
        raise AssertionError("not ambiguous")
    assert pair[0] * pair[1] == N
    return tuple(sorted(pair))


def stirling2(n, k):
    table = [[0] * (k + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            table[i][j] = table[i - 1][j - 1] + j * table[i - 1][j]
    return table[n][k]


def formula_failure_count(H, m):
    total = 0
    for k in range(0, min(m, H) + 1):
        # binomial(H,k) * 2^k * k! * S(m,k)
        numerator = 1
        for j in range(k):
            numerator *= H - j
        total += numerator * (2**k) * stirling2(m, k)
    return total


def brute_failure_count(H, m):
    # A coarse state is (square fiber, T0-coset bit). Failure means each
    # occupied fiber sees at most one bit.
    count = 0
    for sequence in product(range(2 * H), repeat=m):
        seen = {}
        failed = True
        for state in sequence:
            fiber, bit = divmod(state, 2)
            if fiber in seen and seen[fiber] != bit:
                failed = False
                break
            seen[fiber] = bit
        count += int(failed)
    return count


def element_tuples(invariants):
    return product(*(range(modulus) for modulus in invariants))


def scalar_multiple(element, exponent, invariants):
    return tuple((exponent * x) % modulus for x, modulus in zip(element, invariants))


def image_of_power(invariants, exponent):
    return {
        scalar_multiple(element, exponent, invariants)
        for element in element_tuples(invariants)
    }


def run():
    primes = [p for p in range(3, 160) if is_prime(p)]
    checked = 0
    branch_counts = {"odd_discriminant": 0, "even_discriminant": 0}
    examples = []
    for i, p in enumerate(primes):
        for q in primes[i + 1 :]:
            N = p * q
            D, expected = expected_ambiguous(p, q)
            forms = reduced_forms(D)
            ambiguous = sorted(
                form for form in forms if form[1] == 0 or form[1] == form[0] or form[0] == form[2]
            )
            assert ambiguous == expected, (p, q, D, ambiguous, expected)
            assert len(ambiguous) == (2 if D % 2 else 4)
            useful = []
            decoys = []
            for form in ambiguous:
                pair = extracted_pair(D, form)
                if pair == (1, N):
                    decoys.append(form)
                else:
                    assert pair == (p, q), (p, q, form, pair)
                    useful.append(form)
            assert len(useful) == len(ambiguous) // 2
            assert len(decoys) == len(ambiguous) // 2
            if D % 2:
                branch_counts["odd_discriminant"] += 1
            else:
                branch_counts["even_discriminant"] += 1
                assert (2, 2, (N + 1) // 2) in decoys
            if (p, q) in [(3, 5), (3, 7), (3, 11), (5, 13)]:
                examples.append(
                    {
                        "p": p,
                        "q": q,
                        "D": D,
                        "class_number_by_reduced_forms": len(forms),
                        "ambiguous": ambiguous,
                        "useful": useful,
                        "decoys": decoys,
                    }
                )
            checked += 1

    stirling_checks = []
    for H in range(1, 4):
        for m in range(0, 7):
            brute = brute_failure_count(H, m)
            formula = formula_failure_count(H, m)
            assert brute == formula, (H, m, brute, formula)
            stirling_checks.append({"H": H, "m": m, "failure_count": brute})

    power_checks = []
    # The odd cyclic factor exercises the distinction between order and
    # exponent while keeping the state spaces small.
    for invariants in [(2, 3), (4, 3), (8, 3), (2, 2, 3), (4, 2, 3), (4, 4, 3), (8, 2, 3), (8, 4, 3), (8, 8, 3)]:
        h = 1
        lam = 1
        t = 1
        for modulus in invariants:
            h *= modulus
            lam = lcm(lam, modulus)
            t *= gcd(2, modulus)
        exponent_image = image_of_power(invariants, lam // 2)
        h_image = image_of_power(invariants, h // 2)
        assert all(scalar_multiple(x, 2, invariants) == tuple(0 for _ in invariants) for x in exponent_image)
        if t == 2:
            assert len(exponent_image) == 2
            assert len(h_image) == 2
        elif t == 4:
            two_parts = sorted([modulus for modulus in invariants if modulus % 2 == 0], reverse=True)
            expected_w = 4 if two_parts[0] == two_parts[1] else 2
            assert len(exponent_image) == expected_w
            assert h_image == {tuple(0 for _ in invariants)}
        else:
            raise AssertionError((invariants, t))
        power_checks.append(
            {
                "invariants": invariants,
                "h": h,
                "lambda": lam,
                "t": t,
                "lambda_over_2_image_size": len(exponent_image),
                "h_over_2_image_size": len(h_image),
            }
        )

    result = {
        "family": FAMILY,
        "run": RUN,
        "scope": {
            "distinct_odd_prime_bound_exclusive": 160,
            "semiprimes_checked": checked,
            "branch_counts": branch_counts,
            "stirling_H": [1, 2, 3],
            "stirling_m": [0, 1, 2, 3, 4, 5, 6],
        },
        "examples": examples,
        "stirling_checks": stirling_checks,
        "power_checks": power_checks,
        "status": "pass",
        "limitations": "Finite checks only; the unbounded claims require the symbolic audit proof.",
    }
    output = Path(argv[1])
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w") as handle:
        dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(f"{RUN}: PASS ({checked} semiprimes; {len(stirling_checks)} Stirling checks; {len(power_checks)} power checks)")


run()
