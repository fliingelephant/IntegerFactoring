from math import gcd, isqrt


def primes_upto(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


odd_primes = [r for r in primes_upto(500) if r >= 5]
for p in odd_primes:
    for q in [r for r in odd_primes if r > p]:
        N = p * q
        roots = {}
        for x in range(1, N):
            roots.setdefault(x * x % N, []).append(x)
        for d in range(2, N):
            if isqrt(d) ** 2 == d or gcd(d, N) != 1:
                continue
            ds = roots.get(d, [])
            for i, a in enumerate(ds):
                for b in ds[i + 1 :]:
                    if a >= b or a + b >= N or a * a <= d or b * b <= d:
                        continue
                    for u in range(2, (N - 1) // d + 1):
                        c1 = u * d
                        if gcd(u * a, N) != 1:
                            continue
                        w1 = pow(c1, -1, N)
                        if any(1 < gcd(z, N) < N for z in (c1 - w1, c1 + w1)):
                            continue
                        for v in range(2, (N - 1) // d + 1):
                            if u == v:
                                continue
                            c2 = v * d
                            if c1 == c2 or gcd(v * b, N) != 1:
                                continue
                            w2 = pow(c2, -1, N)
                            if any(1 < gcd(z, N) < N for z in (c2 - w2, c2 + w2)):
                                continue

                            U1 = u * a * a
                            U2 = v * b * b
                            if U1 % N != c1 or U2 % N != c2:
                                continue
                            A1, B1 = c1 * w1, U1 * w1
                            A2, B2 = c2 * w2, U2 * w2
                            values = [A1, B1, A2, B2]
                            if len(set(values)) != 4:
                                continue
                            product = A1 * B1 * A2 * B2
                            root = isqrt(product)
                            if root * root != product:
                                continue
                            rho = root % N
                            gminus = gcd(rho - 1, N)
                            gplus = gcd(rho + 1, N)
                            if not (1 < gminus < N and 1 < gplus < N):
                                continue
                            cross_minus = gcd(b - a, N)
                            cross_plus = gcd(a + b, N)
                            if not (1 < cross_minus < N and 1 < cross_plus < N):
                                continue
                            print({
                                "N": N, "p": p, "q": q, "d": d,
                                "a": a, "b": b, "u": u, "v": v,
                                "c1": c1, "w1": w1, "U1": U1,
                                "canonical1": A1, "lifted1": B1,
                                "c2": c2, "w2": w2, "U2": U2,
                                "canonical2": A2, "lifted2": B2,
                                "product": product, "root": root,
                                "normalized_root": rho,
                                "root_gcds": [gminus, gplus],
                                "cross_gcds": [cross_minus, cross_plus],
                                "direct_gcds": [
                                    gcd(c1 - w1, N), gcd(c1 + w1, N),
                                    gcd(c2 - w2, N), gcd(c2 + w2, N),
                                ],
                            })
                            raise SystemExit(0)

raise SystemExit("no certificate in frozen range")
