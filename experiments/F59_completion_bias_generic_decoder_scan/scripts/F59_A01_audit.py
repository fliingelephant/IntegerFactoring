import hashlib
import json
from pathlib import Path


RUN = "F59-A01"
BASE = Path(__file__).resolve().parent.parent
INPUT = BASE / "output" / "F59-D01.json"
OUTPUT = BASE / "output" / f"{RUN}.json"
EXPECTED_HASHES = {
    "scripts/F59_D01_scan.py": "b68a07945899395649a5373f6d321009bb42cf072dfad9342392d2c8fd7c8c0a",
    "run_F59_D01.sh": "df5deb3b562c43e87530d6c55ef1543c7f526465f6d1b550f0f3b4199b481504",
    "logs/F59-D01.log": "122d6f779b5089457cf7be43c7dcef98840808052967c5e1846380cc9da3db4c",
    "output/F59-D01.json": "4ea14ef32aa2eed5d829115a12e151d8d6f38f8fa7146f67f46f18bf59120c8f",
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


def verify_batch(batch, prime_p, prime_q, raw_cap):
    assert batch["raw_relation_count"] <= raw_cap
    assert (
        batch["zero_relation_count"]
        + batch["duplicate_quotient_count"]
        + batch["unique_relation_count"]
        == batch["raw_relation_count"]
    )
    assert batch["squareclass_rank"] + batch["kernel_dimension"] == batch["unique_relation_count"]
    assert (
        batch["global_plus_basis_roots"]
        + batch["global_minus_basis_roots"]
        + batch["useful_basis_roots"]
        == batch["kernel_dimension"]
    )
    assert batch["factor_found_by_batch_decoder"] == (batch["useful_basis_roots"] > 0)
    assert (batch["first_useful_certificate"] is not None) == (batch["useful_basis_roots"] > 0)
    if batch["unique_relation_count"] >= 2:
        assert batch["minimum_quotient_gap"] >= 1
        assert batch["quotient_span"] >= batch["minimum_quotient_gap"]
    else:
        assert batch["minimum_quotient_gap"] is None
        assert batch["quotient_span"] is None

    direct = batch["direct_gcd_events"]
    assert direct["event_count"] == sum(direct["divisor_counts"].values())
    assert all(int(divisor) in (prime_p, prime_q) for divisor in direct["divisor_counts"])
    if batch["first_useful_certificate"] is not None:
        certificate = batch["first_useful_certificate"]
        assert certificate["gcd_root_minus_one"] in (prime_p, prime_q)
        assert certificate["gcd_root_plus_one"] in (prime_p, prime_q)
        assert certificate["gcd_root_minus_one"] != certificate["gcd_root_plus_one"]


def recompute_summary(trials):
    return {
        "trial_count": len(trials),
        "trials_with_nonzero_kernel": sum(row["kernel_dimension"] > 0 for row in trials),
        "trials_with_useful_basis_root": sum(row["factor_found_by_batch_decoder"] for row in trials),
        "total_kernel_dimension": sum(row["kernel_dimension"] for row in trials),
        "total_useful_basis_roots": sum(row["useful_basis_roots"] for row in trials),
        "total_direct_gcd_events": sum(row["direct_gcd_events"]["event_count"] for row in trials),
        "minimum_unique_relation_count": min(row["unique_relation_count"] for row in trials),
        "maximum_unique_relation_count": max(row["unique_relation_count"] for row in trials),
        "minimum_rank_deficit": min(row["kernel_dimension"] for row in trials),
        "maximum_rank_deficit": max(row["kernel_dimension"] for row in trials),
    }


actual_hashes = {relative: sha256(BASE / relative) for relative in EXPECTED_HASHES}
assert actual_hashes == EXPECTED_HASHES

with INPUT.open("r", encoding="utf-8") as handle:
    payload = json.load(handle)

assert payload["run"] == "F59-D01"
assert payload["family"] == "F26"
assert payload["master_seed"] == 0xF59D01
assert payload["target_factor_bits"] == [10, 14, 18, 22]
assert payload["ratios"] == [[21, 20], [4, 3], [7, 4]]
assert payload["trials_per_random_source"] == 8
assert len(payload["records"]) == 12
assert payload["self_checks"]["synthetic_6_10_15_kernel"] == [7]
assert payload["self_checks"]["N15_singleton_factor"]["gcd_root_minus_one"] == 3

totals = {
    "iid_batches": 0,
    "iid_nonzero_kernel_batches": 0,
    "iid_useful_batches": 0,
    "iid_total_kernel_dimension": 0,
    "iid_direct_gcd_events": 0,
    "random_tail_batches": 0,
    "random_tail_nonzero_kernel_batches": 0,
    "random_tail_useful_batches": 0,
    "random_tail_total_kernel_dimension": 0,
    "random_tail_direct_gcd_events": 0,
    "offset_batches": 0,
    "offset_nonzero_kernel_batches": 0,
    "offset_useful_batches": 0,
    "offset_total_kernel_dimension": 0,
    "offset_global_plus_roots": 0,
    "offset_global_minus_roots": 0,
    "offset_direct_gcd_events": 0,
}
offset_dimensions = []
per_input = []

for record in payload["records"]:
    prime_p = record["p"]
    prime_q = record["q"]
    modulus = record["N"]
    input_bits = record["input_bits"]
    raw_cap = input_bits * input_bits
    assert is_prime(prime_p)
    assert is_prime(prime_q)
    assert prime_p < prime_q
    assert modulus == prime_p * prime_q
    assert input_bits == modulus.bit_length()
    assert record["declared_batch_size_n_squared"] == raw_cap

    iid = record["iid_single_step"]
    tails = record["random_tail_prefixes"]
    assert iid["summary"] == recompute_summary(iid["trials"])
    assert tails["summary"] == recompute_summary(tails["trials"])
    assert len(iid["trials"]) == 8
    assert len(tails["trials"]) == 8
    for trial_index, batch in enumerate(iid["trials"]):
        assert batch["trial"] == trial_index
        assert batch["raw_relation_count"] == raw_cap
        verify_batch(batch, prime_p, prime_q, raw_cap)
    for trial_index, batch in enumerate(tails["trials"]):
        assert batch["trial"] == trial_index
        assert batch["start_count"] == input_bits
        assert batch["step_cap_per_start"] == input_bits
        verify_batch(batch, prime_p, prime_q, raw_cap)

    offset = record["deterministic_offset_tail_prefixes"]
    assert offset["start_count"] == input_bits
    assert offset["step_cap_per_start"] == input_bits
    verify_batch(offset, prime_p, prime_q, raw_cap)

    totals["iid_batches"] += 8
    totals["iid_nonzero_kernel_batches"] += iid["summary"]["trials_with_nonzero_kernel"]
    totals["iid_useful_batches"] += iid["summary"]["trials_with_useful_basis_root"]
    totals["iid_total_kernel_dimension"] += iid["summary"]["total_kernel_dimension"]
    totals["iid_direct_gcd_events"] += iid["summary"]["total_direct_gcd_events"]
    totals["random_tail_batches"] += 8
    totals["random_tail_nonzero_kernel_batches"] += tails["summary"]["trials_with_nonzero_kernel"]
    totals["random_tail_useful_batches"] += tails["summary"]["trials_with_useful_basis_root"]
    totals["random_tail_total_kernel_dimension"] += tails["summary"]["total_kernel_dimension"]
    totals["random_tail_direct_gcd_events"] += tails["summary"]["total_direct_gcd_events"]
    totals["offset_batches"] += 1
    totals["offset_nonzero_kernel_batches"] += int(offset["kernel_dimension"] > 0)
    totals["offset_useful_batches"] += int(offset["factor_found_by_batch_decoder"])
    totals["offset_total_kernel_dimension"] += offset["kernel_dimension"]
    totals["offset_global_plus_roots"] += offset["global_plus_basis_roots"]
    totals["offset_global_minus_roots"] += offset["global_minus_basis_roots"]
    totals["offset_direct_gcd_events"] += offset["direct_gcd_events"]["event_count"]
    offset_dimensions.append(offset["kernel_dimension"])
    per_input.append(
        {
            "N": modulus,
            "input_bits": input_bits,
            "ratio": [record["ratio_numerator"], record["ratio_denominator"]],
            "iid_nonzero_kernel_trials": iid["summary"]["trials_with_nonzero_kernel"],
            "tail_nonzero_kernel_trials": tails["summary"]["trials_with_nonzero_kernel"],
            "offset_kernel_dimension": offset["kernel_dimension"],
            "offset_global_plus_roots": offset["global_plus_basis_roots"],
            "offset_global_minus_roots": offset["global_minus_basis_roots"],
            "offset_useful_roots": offset["useful_basis_roots"],
        }
    )

audit = {
    "run": RUN,
    "audited_run": "F59-D01",
    "verdict": "pass",
    "disposition": "artifact and internal-consistency audit; finite evidence only",
    "verified_hashes": actual_hashes,
    "totals": totals,
    "offset_kernel_dimensions": offset_dimensions,
    "per_input": per_input,
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT.open("w", encoding="utf-8") as handle:
    json.dump(audit, handle, indent=2, sort_keys=True)
    handle.write("\n")

print(json.dumps({"output": str(OUTPUT), "totals": totals}, sort_keys=True))
