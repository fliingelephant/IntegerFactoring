import csv
import hashlib
import math
import pathlib
import sys


root = pathlib.Path(sys.argv[1])
expected_hashes = {
    "run_F228_D01.cpp": "c3ebba44df3ba098e383fa84239c81503040fcf17e8dbed42927d5e601941256",
    "run_F228_D02.cpp": "0a1b68b31e2029fafdcf6ec7ff6bc05666c0c4485e7e5ce4ea6129ec094aa606",
    "run_F228_D03.cpp": "af923ebe14525856c360e1f62c9a390bd4ede95031b68d5680f6feafad0288d5",
    "D01_OUTPUT.tsv": "1702c92fd32dddb33a9f309e660a50ce0066c819f6d6e8837cfe134ddfdcee33",
    "D02_OUTPUT.tsv": "314ab2df46ba6b56c0a429266e050182725b4a28aa33b0b3d6b4b29ab1cd9392",
    "D03_OUTPUT.tsv": "a6de38c9e5a448d6dd5c1548989bd23e39787dd0054997f1e30e771901a5abc9",
}
for name, expected in expected_hashes.items():
    observed = hashlib.sha256((root / name).read_bytes()).hexdigest()
    assert observed == expected, (name, observed, expected)


def rows(name):
    with (root / name).open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def ceil_fourth_root(n):
    lo, hi = 0, 1
    while hi**4 < n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**4 < n:
            lo = mid
        else:
            hi = mid
    return hi


d01 = rows("D01_OUTPUT.tsv")
assert len(d01) == 512
d01_success = [int(row["success_num"]) for row in d01]
assert (min(d01_success), max(d01_success), sum(d01_success)) == (17, 72, 22962)

d02 = rows("D02_OUTPUT.tsv")
d03 = rows("D03_OUTPUT.tsv")
assert len(d02) == len(d03) == 96
d03_by_key = {(row["k"], row["row"]): row for row in d03}
for row in d02:
    match = d03_by_key[(row["k"], row["row"])]
    assert row["p"] == match["p"] and row["q"] == match["q"]
    assert int(row["success_num"]) == int(match["cap20_num"])

expected = {
    22: (2754, 524, 0, 29),
    26: (1514, 92, 0, 31),
    30: (788, 15, 0, 34),
}
for k, summary in expected.items():
    block = [row for row in d03 if int(row["k"]) == k]
    assert len(block) == 32
    observed = (
        sum(int(row["oracle_num"]) for row in block),
        sum(int(row["cap20_num"]) for row in block),
        sum(int(row["oracle_num"]) == 0 for row in block),
        max(int(row["max_omega"]) for row in block),
    )
    assert observed == summary, (k, observed, summary)
    assert all(row["oracle_num"] == row["cap40_num"] for row in block)

for row in d03:
    p, q, n_value = int(row["p"]), int(row["q"]), int(row["N"])
    assert p * q == n_value and p < q < 2 * p
    assert is_prime(p) and is_prime(q)
    assert is_prime((p - 1) // 2) and is_prime((q - 1) // 2)
    assert math.gcd(p - 1, q - 1) == 2
    assert int(row["n"]) == n_value.bit_length()
    assert int(row["J"]) == ceil_fourth_root(n_value)

    factors = [] if row["best_primes"] == "-" else [int(x) for x in row["best_primes"].split(",")]
    assert math.prod(factors) == int(row["best_product"])
    u, exponent = int(row["best_u"]), int(row["best_i"])
    b = 1 << (n_value.bit_length() // 2)
    quotient = u * n_value // b
    for ell in factors:
        assert is_prime(ell) and n_value % ell != 0
        assert any((quotient + c) % ell == 0 for c in range(-4, 5))
        assert p % ell == pow(n_value, exponent, ell)

print("PASS hashes=6 d01_rows=512 d02_rows=96 d03_rows=96")
print("PASS d02_cap20_matches_d03_rowwise")
print("PASS d03_safe_prime_and_selected_support_certificates=96")
