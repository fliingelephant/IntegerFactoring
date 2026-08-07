import hashlib
import json
import math
from pathlib import Path


RUN = "F65-A01"
BASE = Path(__file__).resolve().parent.parent
INPUT = BASE / "output" / "F65-D01.json"
OUTPUT = BASE / "output" / f"{RUN}.json"
EXPECTED_HASHES = {
    "source": "c7810ba32ce5d359530bf865252ee4446d4b95c29047e6e43ecbe03581c385ba",
    "runner": "82d204d8d2c69b43011aa020a843feefdec081d02cfd3e2ab141c0dcbf58bd15",
    "log": "5cf9dcb382afa5ca186ccd45103467d47d1585aedb72c9b4a6ba890c5b5c058c",
    "output": "0d41c802e316689ea0617820535616dec55d5f331155ffbb55dcdb5599f71309",
}
PATHS = {
    "source": BASE / "scripts" / "F65_D01_scan.py",
    "runner": BASE / "run_F65_D01.sh",
    "log": BASE / "logs" / "F65-D01.log",
    "output": INPUT,
}
MENUS = (
    "block_screens",
    "legal_pair_screens",
    "single_power_screens",
    "signed_pair_screens",
)


def digest(path):
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1 << 20):
            hasher.update(chunk)
    return hasher.hexdigest()


def screens(residue, modulus):
    return sorted(
        set(
            divisor
            for divisor in (
                math.gcd(residue - 1, modulus),
                math.gcd(residue + 1, modulus),
            )
            if 1 < divisor < modulus
        )
    )


def validate_hit(hit, blocks, budgets, modulus):
    residue = hit["residue"]
    certificate = hit["certificate"]
    kind = certificate["kind"]
    assert 1 <= residue < modulus
    assert hit["divisors"] == screens(residue, modulus)
    assert hit["divisors"]
    assert hit["self_inverse"] == (residue * residue % modulus == 1)

    if kind == "block":
        index = certificate["index"]
        assert certificate["block"] == blocks[index]
        expected = blocks[index]
    elif kind == "legal_square":
        left_index, right_index = certificate["indices"]
        assert left_index == right_index
        assert budgets[left_index] >= 2
        assert certificate["blocks"] == [blocks[left_index], blocks[right_index]]
        expected = blocks[left_index] ** 2
        assert expected < modulus
    elif kind == "legal_pair":
        left_index, right_index = certificate["indices"]
        assert left_index < right_index
        assert certificate["blocks"] == [blocks[left_index], blocks[right_index]]
        expected = blocks[left_index] * blocks[right_index]
        assert expected < modulus
    elif kind == "legal_power":
        index = certificate["index"]
        exponent = certificate["exponent"]
        assert certificate["block"] == blocks[index]
        assert 1 <= exponent <= budgets[index]
        expected = blocks[index] ** exponent
        assert expected < modulus
    elif kind == "signed_single":
        index = certificate["index"]
        sign = certificate["sign"]
        assert sign in (-1, 1)
        expected = blocks[index] if sign == 1 else pow(blocks[index], -1, modulus)
    elif kind == "signed_pair":
        left_index, right_index = certificate["indices"]
        left_sign, right_sign = certificate["signs"]
        assert left_index < right_index
        assert left_sign in (-1, 1) and right_sign in (-1, 1)
        assert certificate["blocks"] == [blocks[left_index], blocks[right_index]]
        left = blocks[left_index] if left_sign == 1 else pow(blocks[left_index], -1, modulus)
        right = blocks[right_index] if right_sign == 1 else pow(blocks[right_index], -1, modulus)
        expected = left * right % modulus
    else:
        raise AssertionError(f"unknown certificate kind {kind}")

    assert residue == expected


def main():
    actual_hashes = {name: digest(path) for name, path in PATHS.items()}
    assert actual_hashes == EXPECTED_HASHES
    with INPUT.open(encoding="utf-8") as handle:
        data = json.load(handle)
    assert data["run"] == "F65-D01"
    assert len(data["records"]) == 12

    totals = {
        variant: {
            menu: {
                "candidate_count": 0,
                "inputs_with_hit": 0,
                "no_direct_inputs_with_hit": 0,
                "screen_hit_count": 0,
                "self_inverse_count": 0,
            }
            for menu in MENUS
        }
        for variant in ("raw", "unique")
    }
    concise_records = []
    for record in data["records"]:
        modulus = record["N"]
        assert modulus == record["p"] * record["q"]
        direct = bool(record["direct_events"])
        concise = {"N": modulus, "direct_source_hit": direct, "variants": {}}
        for variant_name in ("raw", "unique"):
            variant = record["variants"][variant_name]
            blocks = variant["blocks"]
            budgets = variant["exponent_budgets"]
            assert blocks == sorted(set(blocks))
            assert len(blocks) == len(budgets) == variant["block_count"]
            assert all(block > 1 and math.gcd(block, modulus) == 1 for block in blocks)
            assert all(budget >= 1 for budget in budgets)
            concise["variants"][variant_name] = {}
            for menu in MENUS:
                result = variant[menu]
                assert result["candidate_count"] == result["unique_residue_count"]
                assert 0 <= result["self_inverse_count"] <= result["candidate_count"]
                assert 0 <= result["screen_hit_count"] <= result["candidate_count"]
                hit = result["first_hit"]
                assert (hit is None) == (result["screen_hit_count"] == 0)
                if hit is not None:
                    validate_hit(hit, blocks, budgets, modulus)
                aggregate = totals[variant_name][menu]
                aggregate["candidate_count"] += result["candidate_count"]
                aggregate["screen_hit_count"] += result["screen_hit_count"]
                aggregate["self_inverse_count"] += result["self_inverse_count"]
                aggregate["inputs_with_hit"] += hit is not None
                aggregate["no_direct_inputs_with_hit"] += hit is not None and not direct
                concise["variants"][variant_name][menu] = {
                    "first_hit": hit,
                    "screen_hit_count": result["screen_hit_count"],
                }
        concise_records.append(concise)

    output = {
        "audit_scope": (
            "Pins all D01 artifacts, validates every stored positive certificate, "
            "and checks aggregate/internal count identities. It does not independently "
            "re-enumerate menus, so stored null results remain source-run evidence."
        ),
        "hashes": actual_hashes,
        "records": concise_records,
        "run": RUN,
        "totals": totals,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("x", encoding="utf-8") as handle:
        json.dump(output, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps(totals, sort_keys=True))
    print(f"wrote={OUTPUT}")


if __name__ == "__main__":
    main()

