from pathlib import Path
import json


p = Integer(1045051789228925522286798994428155162483171043575427210769649)
q = Integer(1554444160139607735219235490867513970584901047572020145318529)
N = Integer(1624474650810351494674724672626447596101101292465081710399215356070170241230595297993492854704406556802940436598350526321)
r = Integer(812237325405175747337362336313223798050550646232540855199607678035085120615297648996746427352203278401470218299175263161)

n = Integer(ceil(log(N + 1, 2)))
L = Integer(ceil(log(n + 1, 2)))
E = Integer(2) ** (L * L)

large_checks = {
    "p_is_prime": bool(p.is_prime(proof=True)),
    "q_is_prime": bool(q.is_prime(proof=True)),
    "r_is_prime": bool(r.is_prime(proof=True)),
    "N_equals_p_times_q": bool(N == p * q),
    "N_equals_2r_minus_1": bool(N == 2 * r - 1),
    "balanced_distinct_factors": bool(p < q < 2 * p),
    "n_equals_400": bool(n == 400),
    "L_equals_9": bool(L == 9),
    "E_equals_2_power_81": bool(E == Integer(2) ** 81),
    "seed_square_bound_below_p": bool((E + 1) ** 2 + 1 < p),
    "p_is_below_q": bool(p < q),
    "r_above_half_universe_cutoff": bool(r > (N - 1) / 2),
    "r_below_N": bool(r < N),
    "two_times_r_is_N_plus_1": bool(2 * r == N + 1),
    "two_inverse_is_r": bool(inverse_mod(2, N) == r),
    "seed_two_value_is_N_plus_1": bool(2 * inverse_mod(2, N) == N + 1),
    "r_valuation_is_one": bool((N + 1).valuation(r) == 1),
    "only_one_positive_r_multiple_below_N": bool(r < N and 2 * r > N - 1),
}

N_small = Integer(161)
small_records = [(10, 145, 9), (26, 31, 5), (32, 156, 31), (87, 124, 67)]
small_values = []
small_parities = []
small_checks = {}

for c_raw, w_raw, k_raw in small_records:
    c = Integer(c_raw)
    w = Integer(w_raw)
    k = Integer(k_raw)
    value = c * w
    factors = factor(value)
    parity = sorted(Integer(prime) for prime, exponent in factors if exponent % 2 == 1)
    small_values.append(Integer(value))
    small_parities.append(parity)
    key = str(c)
    small_checks[f"inverse_{key}"] = bool(inverse_mod(c, N_small) == w)
    small_checks[f"carry_{key}"] = bool(value == 1 + k * N_small)
    small_checks[f"minus_screen_{key}"] = bool(gcd(c - w, N_small) == 1)
    small_checks[f"plus_screen_{key}"] = bool(gcd(c + w, N_small) == 1)

small_rows = sorted(set().union(*(set(parity) for parity in small_parities)))
small_matrix = matrix(
    GF(2),
    [[Integer(row in parity) for parity in small_parities] for row in small_rows],
)
small_degrees = [sum(Integer(entry) for entry in matrix_row) for matrix_row in small_matrix.rows()]

small_checks["values_are_distinct"] = bool(len(set(small_values)) == 4)
small_checks["no_degree_one_row"] = bool(min(small_degrees) >= 2)
small_checks["rank_is_four"] = bool(small_matrix.rank() == 4)
small_checks["kernel_is_zero"] = bool(small_matrix.right_kernel().dimension() == 0)

checks = large_checks | small_checks
output = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "large_certificate": {
        "p": str(p),
        "q": str(q),
        "N": str(N),
        "r": str(r),
        "n": int(n),
        "L": int(L),
        "E": str(E),
        "E_plus_1_squared_plus_1": str((E + 1) ** 2 + 1),
    },
    "small_certificate": {
        "N": int(N_small),
        "values": [int(value) for value in small_values],
        "parity_rows": [int(row) for row in small_rows],
        "column_parities": [[int(row) for row in parity] for parity in small_parities],
        "row_degrees": [int(degree) for degree in small_degrees],
        "rank": int(small_matrix.rank()),
        "nullity": int(small_matrix.right_kernel().dimension()),
    },
}

output_path = Path("experiments/F138_owner_pivot_carry_gate/OUTPUT.json")
output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
print(output["status"])
