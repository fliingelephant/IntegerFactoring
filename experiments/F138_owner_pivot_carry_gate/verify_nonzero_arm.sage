from pathlib import Path
import json


p = Integer(1320008795989904748182462774062723291576584579927832140369037)
q = Integer(1483391727238122164760277073344336797129797980984686650045533)
N = Integer(1958090127852978830975606630525183532915462684425760907751271701246799901589218459681729024239617354885430788103473361721)
r = Integer(1631741773210815692479672192104319610762885570354800756459393084372333251324348716401440853533014462404525656752894468101)

n = Integer(ceil(log(N + 1, 2)))
L = Integer(ceil(log(n + 1, 2)))
E = Integer(2) ** (L * L)

q0 = Integer(2)
ell = Integer(3)
A = Integer(2)
w0 = inverse_mod(q0, N)
H = w0 + N * A
c = ell * q0
z = H // ell
P = c * z

checks = {
    "p_is_prime": bool(p.is_prime(proof=True)),
    "q_is_prime": bool(q.is_prime(proof=True)),
    "r_is_prime": bool(r.is_prime(proof=True)),
    "N_equals_p_times_q": bool(N == p * q),
    "balanced_distinct_factors": bool(p < q < 2 * p),
    "N_is_one_mod_6": bool(N % 6 == 1),
    "r_formula": bool(6 * r == 5 * N + 1),
    "n_equals_400": bool(n == 400),
    "L_equals_9": bool(L == 9),
    "E_equals_2_power_81": bool(E == Integer(2) ** 81),
    "seed_square_bound_below_p": bool((E + 1) ** 2 + 1 < p),
    "base_inverse_formula": bool(w0 == (N + 1) // 2),
    "anchor_is_eligible": bool(ell.is_prime() and ell <= E and gcd(ell, N * q0) == 1),
    "digit_is_nonzero": bool(A > 0),
    "digit_is_maximum": bool(A == ell - 1),
    "digit_congruence": bool((w0 + N * A) % ell == 0),
    "H_equals_3r": bool(H == 3 * r),
    "left_endpoint_is_6": bool(c == 6),
    "right_endpoint_is_r": bool(z == r),
    "endpoints_are_canonical": bool(1 <= c < N and 1 <= z < N),
    "right_is_inverse": bool(inverse_mod(c, N) == z),
    "exact_value_formula": bool(P == 6 * r == 1 + 5 * N),
    "r_valuation_is_one": bool(P.valuation(r) == 1),
    "minus_screen_is_one": bool(gcd(c - z, N) == 1),
    "plus_screen_is_one": bool(gcd(c + z, N) == 1),
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
        "E_plus_1_squared_plus_1": str((E + 1) ** 2 + 1),
        "base_q": int(q0),
        "anchor_ell": int(ell),
        "digit_A": int(A),
        "base_inverse_w": str(w0),
        "fresh_H": str(H),
        "left_c": int(c),
        "right_z": str(z),
        "exact_value": str(P),
        "carry": int(5),
    },
}

output_path = Path("experiments/F138_owner_pivot_carry_gate/OUTPUT_NONZERO_ARM.json")
output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
print(output["status"])
