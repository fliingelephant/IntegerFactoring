from math import gcd, lcm


# For each certified odd prime r:
#   (complete factorization of r-1, Lucas witness).
# Every prime factor in a record occurs earlier in this dictionary.
CERTS = {
    3: ([(2, 1)], 2),
    5: ([(2, 2)], 2),
    7: ([(2, 1), (3, 1)], 3),
    11: ([(2, 1), (5, 1)], 2),
    13: ([(2, 2), (3, 1)], 2),
    17: ([(2, 4)], 3),
    29: ([(2, 2), (7, 1)], 2),
    31: ([(2, 1), (3, 1), (5, 1)], 3),
    37: ([(2, 2), (3, 2)], 2),
    89: ([(2, 3), (11, 1)], 3),
    103: ([(2, 1), (3, 1), (17, 1)], 5),
    113: ([(2, 4), (7, 1)], 3),
    131: ([(2, 1), (5, 1), (13, 1)], 2),
    137: ([(2, 3), (17, 1)], 3),
    179: ([(2, 1), (89, 1)], 2),
    227: ([(2, 1), (113, 1)], 2),
    233: ([(2, 3), (29, 1)], 3),
    239: ([(2, 1), (7, 1), (17, 1)], 7),
    673: ([(2, 5), (3, 1), (7, 1)], 5),
    1097: ([(2, 3), (137, 1)], 3),
    12907: ([(2, 1), (3, 3), (239, 1)], 2),
    182353: ([(2, 4), (3, 1), (29, 1), (131, 1)], 7),
    6014663: ([(2, 1), (233, 1), (12907, 1)], 5),
    7294121: ([(2, 3), (5, 1), (182353, 1)], 6),
    31470827: ([(2, 1), (103, 1), (227, 1), (673, 1)], 2),
    29847543133: ([(2, 2), (3, 1), (11, 1), (31, 1), (7294121, 1)], 2),
    494376480176081: ([(2, 4), (5, 1), (179, 1), (1097, 1), (31470827, 1)], 3),
    359045826645918359: ([(2, 1), (6014663, 1), (29847543133, 1)], 19),
    759362273550460417: ([(2, 9), (3, 1), (494376480176081, 1)], 11),
    7593622735504604171: ([(2, 1), (5, 1), (759362273550460417, 1)], 2),
    15187245471009208343: ([(2, 1), (7593622735504604171, 1)], 5),
    26569391171797958567: ([(2, 1), (37, 1), (359045826645918359, 1)], 5),
}


certified = {2}
for prime, (factorization, witness) in CERTS.items():
    assert all(base in certified for base, _ in factorization)
    product = 1
    for base, exponent in factorization:
        product *= base**exponent
    assert product == prime - 1
    assert pow(witness, prime - 1, prime) == 1
    assert all(pow(witness, (prime - 1) // base, prime) != 1
               for base, _ in factorization)
    certified.add(prime)


p = 15187245471009208343
q = 26569391171797958567
N = 403515865741360589240927487586184724481
n = 129
B = 2**64
H = 21874638913457614155
s_p = 7593622735504604171
large_q = 359045826645918359
s_q = 37 * large_q

assert p in certified and q in certified
assert p * q == N
assert p < q < 2 * p
assert 2**128 < N + 1 < 2**129
assert n == 129 and B == 2 ** (n // 2)
assert N - 1 == B * H
assert (p - 1) // 2 == s_p and (q - 1) // 2 == s_q
assert (p - 1) % 4 == 2 and (q - 1) % 4 == 2
assert gcd(s_p, s_q) == 1
assert s_p in certified and 37 in certified and large_q in certified


def verify_order(modulus, order, factorization):
    product = 1
    for prime, exponent in factorization:
        assert prime in certified
        product *= prime**exponent
    assert product == order
    assert pow(N, order, modulus) == 1
    assert all(pow(N, order // prime, modulus) != 1
               for prime, _ in factorization)


order_p = 3796811367752302085
order_37 = 36
order_large_q = 179522913322959179
order_q = 6462824879626530444

verify_order(s_p, order_p, [(5, 1), (759362273550460417, 1)])
verify_order(37, order_37, [(2, 2), (3, 2)])
verify_order(large_q, order_large_q, [(6014663, 1), (29847543133, 1)])
assert order_q == lcm(order_37, order_large_q)
verify_order(
    s_q,
    order_q,
    [(2, 2), (3, 2), (6014663, 1), (29847543133, 1)],
)

assert min(order_p, order_q) > 2**61
assert 2**57 < min(order_p, order_large_q)
assert min(s_p, large_q) > 2**58

print("PASS F237")
print("N_bits", n)
print("B", B)
print("meta_orders", order_p, order_q)
print("power_word_K_max", 2**57)
print("residual_lower_bound", large_q)

