import hashlib
import json
from pathlib import Path


RUN = "F59-A03"
BASE = Path(__file__).resolve().parent.parent
ORIGINAL = BASE / "output" / "F59-D01.json"
REPLAY = BASE / "output" / "F59-D01-R2.json"
OUTPUT = BASE / "output" / f"{RUN}.json"
EXPECTED_HASHES = {
    "scripts/F59_D01_scan.py": "b68a07945899395649a5373f6d321009bb42cf072dfad9342392d2c8fd7c8c0a",
    "run_F59_D01.sh": "df5deb3b562c43e87530d6c55ef1543c7f526465f6d1b550f0f3b4199b481504",
    "logs/F59-D01.log": "122d6f779b5089457cf7be43c7dcef98840808052967c5e1846380cc9da3db4c",
    "output/F59-D01.json": "4ea14ef32aa2eed5d829115a12e151d8d6f38f8fa7146f67f46f18bf59120c8f",
    "scripts/F59_replay_core.py": "7b2b1a1d1b0bc46ccaaec6a178f4ff96aa7ecc26e4eb2a441521128ef14fbec9",
    "scripts/F59_D01_replay.py": "a95a28233e05593c00be40a56b957fc1f41cceab3ea7dcf076996eb6ccc1347c",
    "run_F59_D01_replay.sh": "a54cb42fa1286f8b6d66fb83db8192a8deb9fa36a80984cf7c919af2947b27cd",
    "logs/F59-D01-R2.log": "dc684686e111283c9ee727514b03d333e874cbac02d83a1e9bb3b21866e37bdb",
    "output/F59-D01-R2.json": "d6a56efdeb8cdebe5253fc0b26c65b6580deef7acc89e4a40cf227cc0311fe79",
}


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def without(mapping, excluded):
    return {key: value for key, value in mapping.items() if key not in excluded}


def compare_direct(old, new, require_equal):
    assert old["event_count"] == sum(old["divisor_counts"].values())
    assert new["event_count"] == sum(new["divisor_counts"].values())
    if require_equal:
        assert new == old
    else:
        assert new["event_count"] >= old["event_count"]
        for divisor in set(old["divisor_counts"]) | set(new["divisor_counts"]):
            assert new["divisor_counts"].get(divisor, 0) >= old["divisor_counts"].get(
                divisor, 0
            )
    return new["event_count"] - old["event_count"]


actual_hashes = {relative: sha256(BASE / relative) for relative in EXPECTED_HASHES}
assert actual_hashes == EXPECTED_HASHES
with ORIGINAL.open("r", encoding="utf-8") as handle:
    original = json.load(handle)
with REPLAY.open("r", encoding="utf-8") as handle:
    replay = json.load(handle)

assert original["run"] == "F59-D01"
assert replay["run"] == "F59-D01-R2"
assert replay["replays"] == "F59-D01"
assert replay["repairs"] == [
    "gcd-check the endpoint produced by the final capped transition",
    "runner preserves timeout and Python exit status",
]
assert replay["self_checks"]["N15_final_endpoint_event"] == {"3": 1}
for key, value in original["self_checks"].items():
    assert replay["self_checks"][key] == value
for key in (
    "family",
    "master_seed",
    "target_factor_bits",
    "ratios",
    "trials_per_random_source",
    "batch_rule",
    "decoder",
):
    assert replay[key] == original[key]
assert len(original["records"]) == len(replay["records"]) == 12

totals = {
    "input_count": 12,
    "child_seed_count": 0,
    "iid_direct_event_increase": 0,
    "tail_direct_event_increase": 0,
    "offset_direct_event_increase": 0,
    "changed_non_direct_fields": 0,
}
per_input_direct_increases = []
old_seeds = []
new_seeds = []

for old_record, new_record in zip(original["records"], replay["records"]):
    excluded_sources = {
        "iid_single_step",
        "random_tail_prefixes",
        "deterministic_offset_tail_prefixes",
    }
    assert without(new_record, excluded_sources) == without(old_record, excluded_sources)

    old_iid = old_record["iid_single_step"]
    new_iid = new_record["iid_single_step"]
    assert new_iid["summary"] == old_iid["summary"]
    assert len(old_iid["trials"]) == len(new_iid["trials"]) == 8
    iid_increase = 0
    for old_batch, new_batch in zip(old_iid["trials"], new_iid["trials"]):
        old_seeds.append(old_batch["stream_seed"])
        new_seeds.append(new_batch["stream_seed"])
        assert without(new_batch, {"direct_gcd_events"}) == without(
            old_batch, {"direct_gcd_events"}
        )
        iid_increase += compare_direct(
            old_batch["direct_gcd_events"], new_batch["direct_gcd_events"], True
        )

    old_tails = old_record["random_tail_prefixes"]
    new_tails = new_record["random_tail_prefixes"]
    assert without(new_tails["summary"], {"total_direct_gcd_events"}) == without(
        old_tails["summary"], {"total_direct_gcd_events"}
    )
    assert len(old_tails["trials"]) == len(new_tails["trials"]) == 8
    tail_increase = 0
    for old_batch, new_batch in zip(old_tails["trials"], new_tails["trials"]):
        old_seeds.append(old_batch["stream_seed"])
        new_seeds.append(new_batch["stream_seed"])
        assert without(new_batch, {"direct_gcd_events"}) == without(
            old_batch, {"direct_gcd_events"}
        )
        tail_increase += compare_direct(
            old_batch["direct_gcd_events"], new_batch["direct_gcd_events"], False
        )
    assert (
        new_tails["summary"]["total_direct_gcd_events"]
        - old_tails["summary"]["total_direct_gcd_events"]
        == tail_increase
    )

    old_offset = old_record["deterministic_offset_tail_prefixes"]
    new_offset = new_record["deterministic_offset_tail_prefixes"]
    assert without(new_offset, {"direct_gcd_events"}) == without(
        old_offset, {"direct_gcd_events"}
    )
    offset_increase = compare_direct(
        old_offset["direct_gcd_events"], new_offset["direct_gcd_events"], False
    )

    totals["iid_direct_event_increase"] += iid_increase
    totals["tail_direct_event_increase"] += tail_increase
    totals["offset_direct_event_increase"] += offset_increase
    per_input_direct_increases.append(
        {
            "N": old_record["N"],
            "iid": iid_increase,
            "random_tail": tail_increase,
            "deterministic_offset": offset_increase,
        }
    )

assert old_seeds == new_seeds
assert len(old_seeds) == 192
totals["child_seed_count"] = len(old_seeds)

audit = {
    "run": RUN,
    "audited_runs": ["F59-D01", "F59-D01-R2"],
    "verdict": "pass",
    "disposition": "same-seed replay comparison; finite evidence only",
    "verified_hashes": actual_hashes,
    "totals": totals,
    "per_input_direct_increases": per_input_direct_increases,
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT.open("w", encoding="utf-8") as handle:
    json.dump(audit, handle, indent=2, sort_keys=True)
    handle.write("\n")

print(json.dumps({"output": str(OUTPUT), "totals": totals}, sort_keys=True))
