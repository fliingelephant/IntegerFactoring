import hashlib
import json
import math
from pathlib import Path


RUN = "F59-A02"
BASE = Path(__file__).resolve().parent.parent
INPUT = BASE / "output" / "F59-D02.json"
OUTPUT = BASE / "output" / f"{RUN}.json"
EXPECTED_HASHES = {
    "scripts/F59_D02_offset_certificates.py": "05341e985a0e5c72911d8d118f2f33dda72241e468a190bd3355f481f348cf13",
    "run_F59_D02.sh": "c4db954bd60311adc2aebd9fcbca3acaec73a2e46e5b8cc8066c0aadcac780e5",
    "logs/F59-D02.log": "50b3db5e8fe8123f334fd395d8c4f3fb05a839d41e8d9b7a644e198bc5cae018",
    "output/F59-D02.json": "23c1272fdaebfd932fb727b75d73e47f46b34a0d468b761c39956b9075073b6e",
}


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def is_prime(value):
    if value < 2:
        return False
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % prime == 0:
            return value == prime
    odd_part = value - 1
    power_of_two = 0
    while odd_part % 2 == 0:
        odd_part //= 2
        power_of_two += 1
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % value == 0:
            continue
        residue = pow(base, odd_part, value)
        if residue in (1, value - 1):
            continue
        for _ in range(power_of_two - 1):
            residue = residue * residue % value
            if residue == value - 1:
                break
        else:
            return False
    return True


def regenerate(modulus, input_bits):
    direct_events = {}
    records = []
    for start_offset in range(1, input_bits + 1):
        state = modulus - start_offset
        for step_index in range(input_bits):
            if state == 1:
                break
            divisor = math.gcd(state, modulus)
            if divisor != 1:
                if 1 < divisor < modulus:
                    key = str(divisor)
                    direct_events[key] = direct_events.get(key, 0) + 1
                break
            inverse = pow(state, -1, modulus)
            quotient = (state * inverse - 1) // modulus
            records.append(
                {
                    "start_offset": start_offset,
                    "step_index": step_index,
                    "u": state,
                    "v": inverse,
                    "k": quotient,
                }
            )
            state = quotient
        else:
            if state != 1:
                divisor = math.gcd(state, modulus)
                if 1 < divisor < modulus:
                    key = str(divisor)
                    direct_events[key] = direct_events.get(key, 0) + 1
    return records, direct_events


def is_global_square(modulus, record):
    relation_value = modulus * record["k"] + 1
    root = math.isqrt(relation_value)
    return root * root == relation_value and root % modulus in (1, modulus - 1)


def deduplicate(modulus, raw_records):
    unique = []
    quotient_to_index = {}
    zero_count = 0
    duplicate_count = 0
    for record in raw_records:
        quotient = record["k"]
        if quotient == 0:
            zero_count += 1
            continue
        known = quotient_to_index.get(quotient)
        if known is not None:
            duplicate_count += 1
            unique[known]["duplicate_provenance"].append(
                [record["start_offset"], record["step_index"]]
            )
            continue
        retained = dict(record)
        retained["A"] = modulus * quotient + 1
        retained["duplicate_provenance"] = []
        quotient_to_index[quotient] = len(unique)
        unique.append(retained)
    return unique, zero_count, duplicate_count


def verify_variant(modulus, raw_records, variant):
    unique, zero_count, duplicate_count = deduplicate(modulus, raw_records)
    assert variant["raw_relation_count"] == len(raw_records)
    assert variant["zero_relation_count"] == zero_count
    assert variant["duplicate_quotient_count"] == duplicate_count
    assert variant["unique_relation_count"] == len(unique)
    assert variant["squareclass_rank"] + variant["kernel_dimension"] == len(unique)
    assert len(variant["certificates"]) == variant["kernel_dimension"]
    assert (
        variant["formal_endpoint_basis_relations"]
        + variant["arithmetic_only_basis_relations"]
        == variant["kernel_dimension"]
    )
    assert (
        variant["global_plus_basis_roots"]
        + variant["global_minus_basis_roots"]
        + variant["non_global_basis_roots"]
        == variant["kernel_dimension"]
    )
    expected_global_columns = []
    for index, record in enumerate(unique):
        root = math.isqrt(record["A"])
        if root * root == record["A"] and root % modulus in (1, modulus - 1):
            expected_global_columns.append(index)
    assert variant["global_square_singleton_columns"] == expected_global_columns

    certificate_summaries = []
    for certificate in variant["certificates"]:
        selected = certificate["selected_columns"]
        assert selected == sorted(set(selected))
        assert certificate["support_size"] == len(selected)
        assert len(certificate["selected_relations"]) == len(selected)
        product = 1
        odd_endpoints = set()
        for index, stored_relation in zip(selected, certificate["selected_relations"]):
            assert stored_relation == unique[index]
            assert stored_relation["u"] * stored_relation["v"] == stored_relation["A"]
            assert stored_relation["A"] == modulus * stored_relation["k"] + 1
            product *= stored_relation["A"]
            for endpoint in (stored_relation["u"], stored_relation["v"]):
                if endpoint in odd_endpoints:
                    odd_endpoints.remove(endpoint)
                else:
                    odd_endpoints.add(endpoint)
        root = math.isqrt(product)
        assert root * root == product
        residue = root % modulus
        assert certificate["root_mod_N"] == residue
        if residue == 1:
            expected_type = "global_plus"
        elif residue == modulus - 1:
            expected_type = "global_minus"
        else:
            expected_type = "non_global"
        assert certificate["root_type"] == expected_type
        assert certificate["formal_endpoint_even"] == (not odd_endpoints)
        assert certificate["odd_endpoint_labels"] == sorted(odd_endpoints)
        assert certificate["contains_N_minus_1_loop"] == any(
            unique[index]["u"] == modulus - 1 and unique[index]["v"] == modulus - 1
            for index in selected
        )
        if expected_type == "non_global":
            divisors = [math.gcd(root - 1, modulus), math.gcd(root + 1, modulus)]
            assert certificate["gcd_divisors"] == divisors
            assert all(1 < divisor < modulus for divisor in divisors)
        else:
            assert certificate["gcd_divisors"] is None
        certificate_summaries.append(
            {
                "root_type": expected_type,
                "formal_endpoint_even": not odd_endpoints,
                "support_size": len(selected),
                "selected_quotients": [unique[index]["k"] for index in selected],
            }
        )
    return certificate_summaries


actual_hashes = {relative: sha256(BASE / relative) for relative in EXPECTED_HASHES}
assert actual_hashes == EXPECTED_HASHES
with INPUT.open("r", encoding="utf-8") as handle:
    payload = json.load(handle)

assert payload["run"] == "F59-D02"
assert payload["family"] == "F26"
assert payload["target_factor_bits"] == [10, 14, 18, 22]
assert payload["ratios"] == [[21, 20], [4, 3], [7, 4]]
assert len(payload["records"]) == 12

totals = {
    "full_kernel_dimension": 0,
    "full_formal_relations": 0,
    "full_arithmetic_only_relations": 0,
    "full_non_global_roots": 0,
    "without_global_singletons_kernel_dimension": 0,
    "without_first_offset_kernel_dimension": 0,
    "direct_gcd_events": 0,
}
arithmetic_certificates = []

for record in payload["records"]:
    modulus = record["N"]
    prime_p = record["p"]
    prime_q = record["q"]
    input_bits = record["input_bits"]
    assert is_prime(prime_p)
    assert is_prime(prime_q)
    assert modulus == prime_p * prime_q
    assert input_bits == modulus.bit_length()
    raw, direct_events = regenerate(modulus, input_bits)
    assert record["direct_gcd_events"]["event_count"] == sum(direct_events.values())
    assert record["direct_gcd_events"]["divisor_counts"] == direct_events
    assert all(int(divisor) in (prime_p, prime_q) for divisor in direct_events)

    without_global = [item for item in raw if not is_global_square(modulus, item)]
    without_first = [item for item in raw if item["start_offset"] != 1]
    full_summaries = verify_variant(modulus, raw, record["full_offset_batch"])
    verify_variant(modulus, without_global, record["without_global_square_singletons"])
    verify_variant(modulus, without_first, record["without_first_offset_path"])

    full = record["full_offset_batch"]
    totals["full_kernel_dimension"] += full["kernel_dimension"]
    totals["full_formal_relations"] += full["formal_endpoint_basis_relations"]
    totals["full_arithmetic_only_relations"] += full["arithmetic_only_basis_relations"]
    totals["full_non_global_roots"] += full["non_global_basis_roots"]
    totals["without_global_singletons_kernel_dimension"] += record[
        "without_global_square_singletons"
    ]["kernel_dimension"]
    totals["without_first_offset_kernel_dimension"] += record[
        "without_first_offset_path"
    ]["kernel_dimension"]
    totals["direct_gcd_events"] += record["direct_gcd_events"]["event_count"]
    for summary in full_summaries:
        if not summary["formal_endpoint_even"]:
            arithmetic_certificates.append(
                {
                    "N": modulus,
                    "input_bits": input_bits,
                    **summary,
                }
            )

audit = {
    "run": RUN,
    "audited_run": "F59-D02",
    "verdict": "pass",
    "disposition": "artifact and certificate audit; finite evidence only",
    "verified_hashes": actual_hashes,
    "totals": totals,
    "arithmetic_only_certificates": arithmetic_certificates,
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT.open("w", encoding="utf-8") as handle:
    json.dump(audit, handle, indent=2, sort_keys=True)
    handle.write("\n")

print(json.dumps({"output": str(OUTPUT), "totals": totals}, sort_keys=True))
