#!/usr/bin/env python3

from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parent

EXPECTED = {
    "PREREG.md": "6836c71d66d1032f802c2fc079afcebaacd450cc9ba5e27716d24b7caecd8e65",
    "PREREG_CARRY.md": "5088802fadf141525f191fa6dfe2a30d109df9db99869fb10b05f012bd36211c",
    "PREREG_CARRY_ORDER.md": "8253288b7ec033e79842646124da2c4ca58cdaec230153c50db2f77dad9138b1",
    "PREREG_CARRY_RESIDUAL_TRADEOFF.md": "cc080636879d5c26b3a6a49262d33bf71453bcb6455181a474cf557f7caaaa21",
    "PREREG_FIRST_HIT_DENSITY.md": "9c907834a147a834268e1722fe002e8e7d17f8933f7d1f40a8b32ce3488cb049",
    "PREREG_FIXED_CENTER_SCALING.md": "7b84e93fe7babf3c3a9251427cbd7d1a1e030ccad48cdf65ca787471b4dd9353",
    "PREREG_GCD_COLLISION.md": "4f98c9584933c158bce9a533ef7c47b498d76c900c73fd41db88a422ed0a4404",
    "PREREG_MULTIPLIER_CARRY.md": "120ef3fbc2176f6bfde394ceb28183eb3543a0b6734a9cc5032e87d8851c635c",
    "PREREG_MULTIPLIER_SCALING.md": "fc80449e52d4a3f3b17e0b061df5c5a7ebf3024e1f7a23836d41c02733db7958",
    "PREREG_RANDOM_HIT.md": "513d5a5a30d3d70b6f9346beca3a5d973a7a5afaece8ca17a6ecf0b13deb33f7",
    "scan.cpp": "511449ee931a3efa85320934a1a49435c88ff50e2179f6cfd812a880df30fc2c",
    "carry_scan.cpp": "89d21982e8e0d7771ee639025e62a3a63ff4404e1dc855feff5179e417406bcd",
    "carry_order_scan.cpp": "8332a8367ed1ceb0f873928867262c8ce997fbc85790d60b2ac4d3be7135e3bb",
    "tradeoff_scan.cpp": "1a6736db769d80b0c782a6c4720954d3cffd752ffe205dcbe487c5a9e18db12d",
    "multiplier_carry_scan.cpp": "d81176c2c139b7c40ba52d65319cf9ade1d7431e601b231ec8d5391b814bf375",
    "multiplier_scaling_scan.cpp": "9ef5db28596555d2857b2b6a75e8579fcbd382325e7d6369d04c07eec4f1cbc1",
    "fixed_center_scaling_scan.cpp": "1e62c8196d47dbcb4ecf7e1cc5d326f4e8a1a66c3cd2094cdb17c9ff43261c97",
    "first_hit_scan.cpp": "a075d2e61ef6dcfba628c304f9775eefc23db9250fac8f22f2e9c9af2c3850de",
    "gcd_collision_scan.cpp": "86c4f9492792d042e9941a3672cb288ae052cc8ae04b2feccc4b7980383cc09d",
    "random_hit_scan.cpp": "592b1517e08c947aaa3714d5a87637028706568b3e628c7f870b40c23f7e13f8",
    "output/word_scan.out": "38603fdc32a5a9f20cd396fbfa7ac41f2569d43a6760d7b34d996d30362ae1b7",
    "output/carry.out": "8d5b6f11a2f25a007b278178856167caee7b71e453da19e228bd9a9bf6530672",
    "output/carry_order.out": "d5722b8bc472179143cea98093e9aafa49b345927a4991acf2f8b8c361ea29d5",
    "output/multiplier_carry.out": "8b076693c997208424c41a39091a8f5b97eea7df55a797de023d27fd66140f77",
    "output/tradeoff.out": "92a68135e0bd10b5dde320715228a7b798b2cc7fbcda6c03f8a2e9f2d87c67ef",
    "output/multiplier_scaling.out": "63268e6260bf178b0a6426660a182e90eeb83e0b376a15ec7c65a537fad5fd1b",
    "output/fixed_center_scaling.out": "389964b6367d3bd1ea5538175497a7e52d911cdff3a85109b4827a3a7a490ba3",
    "output/first_hit.out": "6b72f5b762b797404b87a745f9aa46d881ff62fd737cd6d0ad46312deefb9348",
    "output/gcd_collision.out": "672b2119b1e41fae19b89432e846893474e8d6ed06f4f78e7fa1782bc95cdfe5",
    "output/random_hit.out": "f3a19a1557c4c1a6fea930bf57d77e66f8b79bbb50fd82741f2bcd87e84a977e",
}


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def is_prime(n):
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


def prime_factors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out.append(n)
    return out


def order(a, p):
    assert is_prime(p) and gcd(a, p) == 1
    o = p - 1
    for ell in prime_factors(o):
        while o % ell == 0 and pow(a, o // ell, p) == 1:
            o //= ell
    return o


for name, expected in EXPECTED.items():
    actual = digest(ROOT / name)
    assert actual == expected, (name, expected, actual)

word = (ROOT / "output/word_scan.out").read_text()
assert "TOTAL 34463" in word
assert "residual_combined=2095493" in word
assert "p=4190987 q=4243619 N=17784952061953" in word

carry_order = (ROOT / "output/carry_order.out").read_text()
assert "TOTAL 34463 MAX_MIN_ORDER 2095492 MAX_MIN_RESIDUAL 2095493" in carry_order

scaling = (ROOT / "output/multiplier_scaling.out").read_text()
assert "CAP n^1 MAX 27483" in scaling
assert "CAP n^2 MAX 414" in scaling
assert "CAP n^3 MAX 14" in scaling
assert "3565721 6646697 N=23700267073537 n=45" in scaling
assert "14@5218" in scaling

fixed = (ROOT / "output/fixed_center_scaling.out").read_text()
assert fixed.count("MAX 1322450") >= 3

random_hit = (ROOT / "output/random_hit.out").read_text()
assert "hits=15/91125 fraction=0.000164609" in random_hit

carry = (ROOT / "output/carry.out").read_text()
assert "45:522514/19" in carry

tradeoff = (ROOT / "output/tradeoff.out").read_text()
assert "MAX 522514 MAX_e1_D1 522514 MAX_SAFE 467736" in tradeoff

# Independently verify the named public-word and carry-order witness.
p, q = 4190987, 4243619
N = p * q
n = N.bit_length()
B = 1 << (n // 2)
H = (N - 1) // B
sp, sq = (p - 1) // 2, (q - 1) // 2
assert (N, n, B, H, sp, sq) == (
    17784952061953,
    45,
    4194304,
    4240263,
    2095493,
    2121809,
)
assert all(is_prime(z) for z in (p, q, sp, sq))
assert order(N % sp, sp) == 2095492
assert order(N % sq, sq) == 2121808
assert order(39, sp) == 2095492
assert order(39, sq) == 2121808

for modulus in (sp, sq):
    w = 1
    for k in range(1, n + 1):
        w = w * (pow(N, k, modulus) - 1) % modulus
        w = w * (pow(H, k, modulus) - 1) % modulus
    for u in range(1, n + 1):
        for shift in range(-n, n + 1):
            child = u * H + shift
            if child > 0:
                w = w * pow(child, n, modulus) % modulus
    for k in range(2, n + 1):
        w = w * k % modulus
    assert w != 0

# Check the exact theorem, including a dyadic half-tie.
for p, q, u in ((11, 19, 8), (43, 67, 3), (4190987, 4243619, 1000)):
    N = p * q
    B = 1 << (N.bit_length() // 2)
    H = (N - 1) // B
    kp = (u * p + B // 2) // B
    kq = (u * q + B // 2) // B
    x = u * p - kp * B
    y = u * q - kq * B
    assert -B // 2 <= x < B // 2
    assert -B // 2 <= y < B // 2
    assert (x * y - u * u) % B == 0
    c = (x * y - u * u) // B
    numerator = u * u * H + kp * kq * B - c
    assert numerator % u == 0
    T = numerator // u
    assert T == kp * q + kq * p
    delta = T * T - 4 * kp * kq * N
    root = isqrt(delta)
    assert root * root == delta
    candidates = []
    for sign in (-1, 1):
        top = T + sign * root
        if top % (2 * kq) == 0:
            candidates.append(top // (2 * kq))
    assert any(1 < z < N and N % z == 0 for z in candidates)

print("PASS F236")

