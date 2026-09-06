from math import gcd


N = 341
components = (11, 31)
g, M, B = 340, 2, 2
relations = ((337, 85, 84), (325, 277, 264))
d1, d2 = 337, 277

assert gcd(M, N) == 1
assert pow(g, M, N) == 1
assert gcd(pow(g, M // 2, N) - 1, N) == 1

for c, w, carry in relations:
    assert 1 <= c < N and 1 <= w < N
    assert c * w == 1 + carry * N
    assert gcd(c, N) == gcd(w, N) == 1
    assert gcd(c - w, N) == 1
    assert gcd(c + w, N) == 1

assert gcd(d1, d2) == 1
assert gcd(d1, N) == gcd(d2, N) == 1

direct_screens = {}
for d in (d1, d2):
    direct_screens[str(d)] = {
        "d-1": gcd(d - 1, N),
        "d+1": gcd(d + 1, N),
        "d^2-1": gcd(pow(d, 2, N) - 1, N),
        "d^2+1": gcd(pow(d, 2, N) + 1, N),
    }
    assert set(direct_screens[str(d)].values()) == {1}

bounded_scans = {
    str(d): [gcd(pow(d, e * M, N) - 1, N) for e in range(1, B + 1)]
    for d in (d1, d2)
}
assert bounded_scans == {"337": [1, 1], "277": [1, 1]}


def relative_order(d, modulus):
    e = 1
    while pow(d, e, modulus) not in (1, modulus - 1):
        e += 1
    return e


local_orders = {
    str(d): [relative_order(d, modulus) for modulus in components]
    for d in (d1, d2)
}
assert local_orders == {"337": [5, 5], "277": [5, 5]}
assert d2 * d1 * d1 % N == g

old_words = (1, d1, d1 * d1 % N)
old_fingerprints = {pow(word, M, N) for word in old_words}
shifted_fingerprints = {pow(d2 * word % N, M, N) for word in old_words}
assert old_fingerprints == {1, 16, 256}
assert shifted_fingerprints == {1, 4, 64}
assert old_fingerprints & shifted_fingerprints == {1}

print("ALL CHECKS PASSED")
print("bounded scans:", bounded_scans)
print("local relative orders:", local_orders)
print("direct screens:", direct_screens)
print("old fingerprints:", sorted(old_fingerprints))
print("shifted fingerprints:", sorted(shifted_fingerprints))
print("intersection:", sorted(old_fingerprints & shifted_fingerprints))
