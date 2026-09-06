import json
from math import isqrt, prod


def is_prime(value):
    return value >= 2 and all(value % divisor for divisor in range(2, isqrt(value) + 1))


u = 32987
v = 32993
N = u * v
f = 66

assert is_prime(u)
assert is_prime(v)
assert N == 1088340091

euclidean_primes = [
    divisor + 1
    for divisor in range(1, f + 1)
    if f % divisor == 0 and is_prime(divisor + 1)
]
assert euclidean_primes == [2, 3, 7, 23, 67]

rows = []
accepted = []
for auxiliary_prime in euclidean_primes:
    base = N % auxiliary_prime
    orbit = []
    residue = 1
    while residue not in orbit:
        orbit.append(residue)
        residue = residue * base % auxiliary_prime

    u_residue = u % auxiliary_prime
    v_residue = v % auxiliary_prime
    both_in_orbit = u_residue in orbit and v_residue in orbit
    if both_in_orbit:
        accepted.append(auxiliary_prime)
    rows.append(
        {
            "q": auxiliary_prime,
            "N_mod_q": base,
            "u_mod_q": u_residue,
            "v_mod_q": v_residue,
            "orbit": orbit,
            "both_hidden_residues_in_orbit": both_in_orbit,
        }
    )

assert accepted == [2]
assert prod(euclidean_primes) == 64722
assert isqrt(N) == 32989
assert prod(euclidean_primes) > isqrt(N)

print(
    json.dumps(
        {
            "status": "PASS",
            "workflow": "post-hoc exact reconstruction; not preregistered",
            "u": u,
            "v": v,
            "N": N,
            "f": f,
            "sqrt_floor_N": isqrt(N),
            "euclidean_primes": euclidean_primes,
            "euclidean_prime_product": prod(euclidean_primes),
            "accepted_auxiliary_primes": accepted,
            "rows": rows,
        },
        indent=2,
        sort_keys=True,
    )
)

