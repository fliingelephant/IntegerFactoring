from sage.all import *
import json

proof.all(True)

N = Integer(667)
B = Integer(5)
p = Integer(23)
q_factor = Integer(29)

old_pairs = [(Integer(7), Integer(286)), (Integer(19), Integer(316))]
packed_q = Integer(133)
packed_w = Integer(331)
anchor_pairs = [
    (Integer(2), Integer(1), Integer(266), Integer(499)),
    (Integer(3), Integer(2), Integer(399), Integer(555)),
    (Integer(5), Integer(2), Integer(665), Integer(333)),
]

def factor_dict(x):
    return {str(prime): int(exponent) for prime, exponent in factor(x)}

def parity_support(x):
    return [int(prime) for prime, exponent in factor(x) if exponent % 2 == 1]

def pair_record(c, w):
    value = c * w
    return {
        "c": int(c),
        "w": int(w),
        "in_range": bool(1 <= c < N and 1 <= w < N),
        "unit_endpoints": bool(gcd(c, N) == 1 and gcd(w, N) == 1),
        "inverse": bool((c * w) % N == 1 and inverse_mod(c, N) == w),
        "minus_gcd": int(gcd(c - w, N)),
        "plus_gcd": int(gcd(c + w, N)),
        "value": int(value),
        "carry": int((value - 1) // N),
        "factorization": factor_dict(value),
        "parity_support": parity_support(value),
    }

old_records = [pair_record(c, w) for c, w in old_pairs]
anchor_records = []
for ell, digit, c, z in anchor_pairs:
    record = pair_record(c, z)
    record.update(
        {
            "anchor": int(ell),
            "digit": int(digit),
            "digit_congruence": bool((packed_w + N * digit) % ell == 0),
            "endpoint_division": bool(z == (packed_w + N * digit) // ell),
            "left_endpoint": bool(c == ell * packed_q),
        }
    )
    anchor_records.append(record)

retained_values = [
    old_pairs[0][0] * old_pairs[0][1],
    old_pairs[1][0] * old_pairs[1][1],
    anchor_pairs[0][2] * anchor_pairs[0][3],
    anchor_pairs[1][2] * anchor_pairs[1][3],
]
supports = [set(parity_support(value)) for value in retained_values]
rows = sorted(set().union(*supports))
matrix_rows = [[int(row in support) for support in supports] for row in rows]
M = matrix(GF(2), matrix_rows)
degrees = {str(row): sum(row in support for support in supports) for row in rows}

column_names = ["old_7", "old_19", "digit_1", "digit_2"]
peeling_witness = [(11, 0), (79, 1), (499, 2), (5, 3)]
active = set(range(4))
peeling_checks = []
for row, column in peeling_witness:
    incident = sorted(index for index in active if row in supports[index])
    valid = incident == [column]
    peeling_checks.append(
        {
            "row": int(row),
            "column": column_names[column],
            "active_incident_columns": [column_names[index] for index in incident],
            "valid": bool(valid),
        }
    )
    if valid:
        active.remove(column)

checks = {
    "prime_factorization_of_N": bool(p.is_prime(proof=True) and q_factor.is_prime(proof=True) and N == p * q_factor),
    "packed_size": bool(B * packed_q < N),
    "packed_inverse": bool(inverse_mod(packed_q, N) == packed_w and packed_q * packed_w == 1 + 66 * N),
    "all_pairs_canonical": bool(all(record["in_range"] and record["unit_endpoints"] and record["inverse"] for record in old_records + anchor_records)),
    "all_sign_screens_null": bool(all(record["minus_gcd"] == 1 and record["plus_gcd"] == 1 for record in old_records + anchor_records)),
    "old_carries": bool([record["carry"] for record in old_records] == [3, 9]),
    "anchor_digits": bool([record["digit"] for record in anchor_records] == [1, 2, 2] and all(record["digit_congruence"] for record in anchor_records)),
    "anchor_carries": bool([record["carry"] for record in anchor_records] == [199, 332, 332]),
    "anchor_construction": bool(all(record["endpoint_division"] and record["left_endpoint"] for record in anchor_records)),
    "digit_two_duplicate": bool(anchor_records[1]["value"] == anchor_records[2]["value"] == 221445),
    "distinct_new_values": bool(anchor_records[0]["value"] == 132734 and anchor_records[0]["value"] != anchor_records[1]["value"] and all(anchor_records[0]["value"] != record["value"] and anchor_records[1]["value"] != record["value"] for record in old_records)),
    "exact_factorizations": bool(
        old_records[0]["factorization"] == {"2": 1, "7": 1, "11": 1, "13": 1}
        and old_records[1]["factorization"] == {"2": 2, "19": 1, "79": 1}
        and anchor_records[0]["factorization"] == {"2": 1, "7": 1, "19": 1, "499": 1}
        and anchor_records[1]["factorization"] == {"3": 2, "5": 1, "7": 1, "19": 1, "37": 1}
    ),
    "old_global_private_rows": bool(7 in supports[0] and 7 not in supports[1] and 19 in supports[1] and 19 not in supports[0]),
    "simultaneous_preservation": bool(all(7 in support and 19 in support for support in supports[2:])),
    "expected_rows": bool(rows == [2, 5, 7, 11, 13, 19, 37, 79, 499]),
    "rank_four": bool(M.rank() == 4),
    "nullity_zero": bool(4 - M.rank() == 0),
    "peels_completely": bool(all(item["valid"] for item in peeling_checks) and not active),
}

output = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "N": int(N),
    "factorization_N": [int(p), int(q_factor)],
    "B": int(B),
    "packed_q": int(packed_q),
    "packed_w": int(packed_w),
    "packed_carry": int(66),
    "old_records": old_records,
    "anchor_records": anchor_records,
    "retained_values": [int(value) for value in retained_values],
    "rows": rows,
    "matrix_rows": matrix_rows,
    "degrees": degrees,
    "rank": int(M.rank()),
    "nullity": int(4 - M.rank()),
    "peeling_witness": peeling_checks,
    "checks": checks,
}

print(json.dumps(output, sort_keys=True, indent=2))
