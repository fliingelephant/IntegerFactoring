from sage.all import *
import json

proof.all(True)

N = Integer(989)
B = Integer(5)
p = Integer(23)
q_factor = Integer(43)

old_pairs = [(Integer(2), Integer(495)), (Integer(16), Integer(680))]
packed_q = Integer(187)
packed_w = Integer(238)
anchor_pairs = [
    (Integer(1), Integer(0), Integer(187), Integer(238)),
    (Integer(2), Integer(0), Integer(374), Integer(119)),
    (Integer(3), Integer(1), Integer(561), Integer(409)),
    (Integer(4), Integer(2), Integer(748), Integer(554)),
    (Integer(5), Integer(3), Integer(935), Integer(641)),
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

def native(value):
    if isinstance(value, Integer):
        return int(value)
    if isinstance(value, dict):
        return {str(key): native(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [native(item) for item in value]
    return value

old_records = [pair_record(c, w) for c, w in old_pairs]
packed_record = pair_record(packed_q, packed_w)

anchor_records = []
for ell, digit, c, z in anchor_pairs:
    record = pair_record(c, z)
    record.update(
        {
            "anchor": int(ell),
            "eligible": bool(1 <= ell <= B and gcd(ell, N * packed_q) == 1),
            "digit": int(digit),
            "digit_congruence": bool((packed_w + N * digit) % ell == 0),
            "digit_range": bool(0 <= digit < ell),
            "endpoint_division": bool(z == (packed_w + N * digit) // ell),
            "left_endpoint": bool(c == ell * packed_q),
        }
    )
    anchor_records.append(record)

old_values = [c * w for c, w in old_pairs]
distinct_anchor_values = []
for record in anchor_records:
    value = Integer(record["value"])
    if value not in distinct_anchor_values:
        distinct_anchor_values.append(value)
retained_values = old_values + distinct_anchor_values

supports = [set(parity_support(value)) for value in retained_values]
rows = sorted(set().union(*supports))
matrix_rows = [[int(row in support) for support in supports] for row in rows]
M = matrix(GF(2), matrix_rows)
degrees = {str(row): sum(row in support for support in supports) for row in rows}

column_names = ["old_2", "old_16", "V0", "V1", "V2", "V3"]
peeling_witness = [(7, 2), (3, 3), (277, 4), (641, 5), (11, 0), (17, 1)]
active = set(range(6))
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

old_supports = supports[:2]
nonzero_supports = supports[3:]

checks = {
    "prime_factorization_of_N": bool(p.is_prime(proof=True) and q_factor.is_prime(proof=True) and N == p * q_factor),
    "packed_size": bool(B * packed_q < N),
    "packed_inverse": bool(inverse_mod(packed_q, N) == packed_w and packed_q * packed_w == 1 + 45 * N),
    "packed_sign_screens_null": bool(packed_record["minus_gcd"] == 1 and packed_record["plus_gcd"] == 1),
    "all_pairs_canonical": bool(all(record["in_range"] and record["unit_endpoints"] and record["inverse"] for record in old_records + anchor_records)),
    "all_anchor_sign_screens_null": bool(all(record["minus_gcd"] == 1 and record["plus_gcd"] == 1 for record in anchor_records)),
    "complete_integer_anchor_bank": bool([record["anchor"] for record in anchor_records] == list(range(1, int(B) + 1)) and all(record["eligible"] for record in anchor_records)),
    "old_carries": bool([record["carry"] for record in old_records] == [1, 11]),
    "anchor_digits": bool([record["digit"] for record in anchor_records] == [0, 0, 1, 2, 3] and all(record["digit_congruence"] and record["digit_range"] for record in anchor_records)),
    "anchor_carries": bool([record["carry"] for record in anchor_records] == [45, 45, 232, 419, 606]),
    "anchor_construction": bool(all(record["endpoint_division"] and record["left_endpoint"] for record in anchor_records)),
    "zero_digit_duplicate": bool(anchor_records[0]["value"] == anchor_records[1]["value"] == 44506),
    "selected_dedup_values": bool(
        [int(value) for value in distinct_anchor_values] == [44506, 229449, 414392, 599335]
        and len(set(retained_values)) == 6
    ),
    "exact_factorizations": bool(
        old_records[0]["factorization"] == {"2": 1, "3": 2, "5": 1, "11": 1}
        and old_records[1]["factorization"] == {"2": 7, "5": 1, "17": 1}
        and anchor_records[0]["factorization"] == {"2": 1, "7": 1, "11": 1, "17": 2}
        and anchor_records[2]["factorization"] == {"3": 1, "11": 1, "17": 1, "409": 1}
        and anchor_records[3]["factorization"] == {"2": 3, "11": 1, "17": 1, "277": 1}
        and anchor_records[4]["factorization"] == {"5": 1, "11": 1, "17": 1, "641": 1}
    ),
    "selected_old_degree_one_rows": bool(
        11 in old_supports[0] and 11 not in old_supports[1]
        and 17 in old_supports[1] and 17 not in old_supports[0]
    ),
    "simultaneous_nonzero_preservation": bool(all(11 in support and 17 in support for support in nonzero_supports)),
    "expected_rows": bool(rows == [2, 3, 5, 7, 11, 17, 277, 409, 641]),
    "rank_six": bool(M.rank() == 6),
    "nullity_zero": bool(6 - M.rank() == 0),
    "peels_completely": bool(all(item["valid"] for item in peeling_checks) and not active),
}

output = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "N": int(N),
    "factorization_N": [int(p), int(q_factor)],
    "B": int(B),
    "packed_record": packed_record,
    "old_records": old_records,
    "anchor_records": anchor_records,
    "retained_values": [int(value) for value in retained_values],
    "rows": rows,
    "matrix_rows": matrix_rows,
    "degrees": degrees,
    "rank": int(M.rank()),
    "nullity": int(6 - M.rank()),
    "peeling_witness": peeling_checks,
    "checks": checks,
}

print(json.dumps(native(output), sort_keys=True, indent=2))
