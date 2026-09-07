from math import comb


def moments(n, a, b, m):
    if n == 0:
        return 0, 0, 0
    x1 = n * (n - 1) // 2
    x2 = n * (n - 1) * (2 * n - 1) // 6
    q, a0 = divmod(a, m)
    s, b0 = divmod(b, m)
    if q or s:
        f0, g0, k0 = moments(n, a0, b0, m)
        return (
            q * x1 + s * n + f0,
            q * q * x2 + s * s * n + g0 + 2 * q * s * x1 + 2 * q * k0 + 2 * s * f0,
            q * x2 + s * x1 + k0,
        )
    if a == 0:
        return 0, 0, 0
    h = (a * (n - 1) + b) // m
    if h == 0:
        return 0, 0, 0
    fp, gp, kp = moments(h, m, m + a - 1 - b, a)
    return (
        n * h - fp,
        n * h * h - 2 * (kp + fp) + fp,
        h * x1 - (gp - fp) // 2,
    )


def direct_moments(n, a, b, m):
    ys = [(a * x + b) // m for x in range(n)]
    return sum(ys), sum(y * y for y in ys), sum(x * y for x, y in enumerate(ys))


def choose2(q):
    return q * (q - 1) // 2


def choose3(q):
    return q * (q - 1) * (q - 2) // 6


cases = 0
for k in range(3, 10):
    r = 1 << k
    phi = r // 2
    odd = list(range(1, r, 2))
    p = 1
    modulus = 8 * r
    for u in odd:
        p = p * u % modulus

    q1 = [(u * pow(u, -1, r) - 1) // r for u in odd]
    assert sum(q1) % 4 == 2
    assert sum(choose2(q) for q in q1) % 4 == 2

    for nu in odd:
        m1 = moments(r, nu, 0, r)
        m2 = moments(phi, nu, 0, phi)
        assert m1 == direct_moments(r, nu, 0, r)
        assert m2 == direct_moments(phi, nu, 0, phi)
        j_moment = (m1[1] + m1[2] - m2[1] - 2 * m2[2]) % 8

        t = 0
        j_direct = 0
        for w in odd:
            uw = pow(w, -1, r)
            f = nu * w // r
            qw = (w * uw - 1) // r
            t += uw * qw * f
            j_direct += f * f + w * f
        assert j_moment == j_direct % 8
        assert j_moment % 2 == 0
        b = (2 + nu * (nu - 1) + j_moment // 2 - nu * (t % 4)) % 4

        qnu = []
        for u in odd:
            v = nu * pow(u, -1, r) % r
            qnu.append((u * v - nu) // r)
        assert b == sum(choose2(q) for q in qnu) % 4

        for ell in [*range(8), (1 << 20) + 3, 10**30 + 5]:
            n_value = nu + r * ell
            qn = [q - ell for q in qnu]
            h_direct = sum(qn) % 8
            bn_direct = sum(choose2(q) for q in qn) % 4
            an_direct = sum(choose3(q) for q in qn) % 2
            c_direct = sum(q % 2 == 0 for q in qn) % 8

            d = (p * p - pow(n_value, phi, modulus)) % modulus
            assert d % r == 0
            multiplier = pow(pow(n_value, phi - 1, 8), -1, 8)
            h_formula = (d // r) * multiplier % 8
            assert h_formula == h_direct
            assert bn_direct == (b - ell * h_formula) % 4
            assert an_direct == (n_value % 8 == 1)
            c_formula = (
                phi
                - h_formula
                + 2 * (b - ell * h_formula)
                - 4 * (n_value % 8 == 1)
            ) % 8
            assert c_formula == c_direct
            cases += 1

print(f"PASS: k=3..9, {cases} full-input cases; moment recursion and all congruences agree")
