from pathlib import Path
import json


p = Integer(1440575060366591719164812115423434185454445360021359262957569)
q = Integer(1531570574064344929935978281536186047620048484429603222323201)
N = Integer(2206342372188439231071704119788681118383639175630092611385003672288203658512531224766164082517129137765776226834467258369)
r = Integer(2206342372188439231071703663527772386250305539544495574654345939408069421197500116321867676177152627713145274674754869377)

n = Integer(ceil(log(N + 1, 2)))
L = Integer(ceil(log(n + 1, 2)))
E = Integer(2) ** (L * L)

a = E
c = 2 * E
A = E - 1
w = inverse_mod(2, N)
H = w + A * N
P = c * r

checks = {
    "p_is_prime": bool(p.is_prime(proof=True)),
    "q_is_prime": bool(q.is_prime(proof=True)),
    "r_is_prime": bool(r.is_prime(proof=True)),
    "N_equals_p_times_q": bool(N == p * q),
    "balanced_distinct_factors": bool(p < q < 2 * p),
    "n_equals_400": bool(n == 400),
    "L_equals_9": bool(L == 9),
    "E_equals_2_power_81": bool(E == Integer(2) ** 81),
    "N_is_one_mod_c": bool(N % c == 1),
    "r_formula": bool(c * r == 1 + (c - 1) * N),
    "factor_bound_above_c_square": bool(c ** 2 + 1 < p),
    "base_inverse_formula": bool(w == (N + 1) // 2),
    "anchor_is_maximum": bool(a == E),
    "anchor_is_unit": bool(gcd(a, N) == 1),
    "digit_is_maximum": bool(A == a - 1),
    "fresh_H_formula": bool(H == a * r),
    "left_endpoint_formula": bool(c == 2 * a),
    "selected_residue_beyond_seed_bank": bool(c > E + 1),
    "endpoints_are_canonical": bool(1 <= c < N and 1 <= r < N),
    "right_is_inverse": bool(inverse_mod(c, N) == r),
    "exact_value_formula": bool(P == 1 + (c - 1) * N),
    "r_valuation_is_one": bool(P.valuation(r) == 1),
    "minus_screen_is_one": bool(gcd(c - r, N) == 1),
    "plus_screen_is_one": bool(gcd(c + r, N) == 1),
    "r_above_half_universe_cutoff": bool(r > (N - 1) / 2),
    "only_one_positive_r_multiple_below_N": bool(r < N and 2 * r > N - 1),
}

output = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "certificate": {
        "p": str(p),
        "q": str(q),
        "N": str(N),
        "r": str(r),
        "n": int(n),
        "L": int(L),
        "E": str(E),
        "anchor_a": str(a),
        "digit_A": str(A),
        "left_c": str(c),
        "base_inverse_w": str(w),
        "fresh_H": str(H),
        "exact_value": str(P),
        "carry": str(c - 1),
        "c_squared_plus_1": str(c ** 2 + 1),
    },
}

output_path = Path("experiments/F138_owner_pivot_carry_gate/OUTPUT_QPOLY_MAX_DIGIT.json")
output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
print(output["status"])
