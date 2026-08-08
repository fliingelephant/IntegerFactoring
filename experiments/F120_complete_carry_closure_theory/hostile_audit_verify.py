#!/usr/bin/env python3
"""Independent exact verifier for the F120 hostile audit.

This program reads the registered candidate artifacts as data. It does not
import or execute the candidate search source.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_prime_test(value: int) -> tuple[bool, int | None]:
    """Prove primality by complete trial division through sqrt(value)."""
    if value < 2:
        return False, None
    for divisor in (2, 3):
        if value == divisor:
            return True, None
        if value % divisor == 0:
            return False, divisor
    divisor = 5
    step = 2
    limit = isqrt(value)
    while divisor <= limit:
        if value % divisor == 0:
            return False, divisor
        divisor += step
        step = 6 - step
    return True, None


def next_exact_prime(value: int) -> int:
    candidate = max(2, value)
    if candidate == 2:
        return 2
    if candidate % 2 == 0:
        candidate += 1
    while not exact_prime_test(candidate)[0]:
        candidate += 2
    return candidate


def factorization(value: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    remainder = value
    divisor = 2
    while divisor * divisor <= remainder:
        while remainder % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            remainder //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remainder > 1:
        factors[remainder] = factors.get(remainder, 0) + 1
    return factors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registration", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    audit_registration_path = Path(args.registration).resolve()
    directory = audit_registration_path.parent
    audit_registration = json.loads(audit_registration_path.read_text())

    artifact_hash_checks: dict[str, bool] = {}
    for name, expected_hash in audit_registration["candidate_artifact_sha256"].items():
        artifact_hash_checks[name] = sha256_file(directory / name) == expected_hash
    assert all(artifact_hash_checks.values())

    candidate_registration = json.loads((directory / "REGISTRATION.json").read_text())
    candidate_output = json.loads((directory / "OUTPUT.json").read_text())
    assert candidate_output["registration"] == candidate_registration
    assert (
        sha256_file(directory / candidate_registration["source"])
        == candidate_registration["source_sha256"]
    )

    p = next_exact_prime(int(candidate_registration["p_start"]))
    ell = next_exact_prime(int(candidate_registration["ell_start"]))
    rejection_certificates: list[dict[str, int | str]] = []
    independent_trace = hashlib.sha256()
    reproduced_candidate_trace = hashlib.sha256()
    found: dict[str, int] | None = None

    for ordinal in range(1, int(candidate_registration["pair_cap"]) + 1):
        modulus = p * ell
        private_prime = (modulus + 1) // 2
        bit_length = modulus.bit_length()
        trial_bound = bit_length**2
        is_private_prime, divisor = exact_prime_test(private_prime)

        trace_record = {
            "N": modulus,
            "ell": ell,
            "ordinal": ordinal,
            "p": p,
            "private_prime": private_prime,
        }
        independent_trace.update(
            (json.dumps(trace_record, sort_keys=True, separators=(",", ":")) + "\n").encode()
        )
        reproduced_candidate_trace.update(
            f"{ordinal}:{p}:{ell}:{modulus}:{private_prime}\n".encode()
        )

        accepted = (
            is_private_prime
            and p != ell
            and p > trial_bound
            and ell > trial_bound
        )
        if accepted:
            found = {
                "ordinal": ordinal,
                "p": p,
                "ell": ell,
                "N": modulus,
                "private_prime": private_prime,
                "bit_length": bit_length,
                "trial_bound": trial_bound,
            }
            break

        rejection: dict[str, int | str] = {
            "ordinal": ordinal,
            "p": p,
            "ell": ell,
            "private_prime": private_prime,
        }
        if not is_private_prime:
            rejection["reason"] = "private_prime_composite"
            if divisor is not None:
                rejection["divisor"] = divisor
        elif p == ell:
            rejection["reason"] = "equal_factors"
        else:
            rejection["reason"] = "trial_bound_failure"
        rejection_certificates.append(rejection)

        p = next_exact_prime(p + 2)
        ell = next_exact_prime(ell + 2)

    assert found is not None
    recorded = candidate_output["candidate"]
    for key in ("ordinal", "p", "ell", "N", "private_prime", "bit_length", "trial_bound"):
        assert found[key] == int(recorded[key])
    assert candidate_output["status"] == "FOUND"
    assert candidate_output["pairs_tested"] == found["ordinal"]

    modulus = found["N"]
    private_prime = found["private_prime"]
    p_is_prime, p_divisor = exact_prime_test(found["p"])
    ell_is_prime, ell_divisor = exact_prime_test(found["ell"])
    private_is_prime, private_divisor = exact_prime_test(private_prime)
    arithmetic_checks = {
        "p_prime_by_complete_trial_division": p_is_prime and p_divisor is None,
        "ell_prime_by_complete_trial_division": ell_is_prime and ell_divisor is None,
        "private_prime_by_complete_trial_division": private_is_prime
        and private_divisor is None,
        "factorization_identity": found["p"] * found["ell"] == modulus,
        "distinct_factors": found["p"] != found["ell"],
        "odd_modulus": modulus % 2 == 1,
        "bit_length_41": modulus.bit_length() == 41,
        "trial_bound_1681": modulus.bit_length() ** 2 == 1681,
        "trial_hard": min(found["p"], found["ell"])
        > modulus.bit_length() ** 2,
        "not_perfect_power_from_prime_exponents": p_is_prime
        and ell_is_prime
        and found["p"] != found["ell"],
        "seed_inverse": pow(2, -1, modulus) == private_prime,
        "exact_value": 2 * private_prime == modulus + 1,
        "carry_one": (2 * private_prime - 1) // modulus == 1,
        "private_valuation_one": factorization(modulus + 1).get(private_prime) == 1,
        "large_row": private_prime > (modulus - 1) // 2,
        "minus_sign_screen_null": gcd(2 - private_prime, modulus) == 1,
        "plus_sign_screen_null": gcd(2 + private_prime, modulus) == 1,
        "coprime_to_15": gcd(modulus, 15) == 1,
    }
    assert all(arithmetic_checks.values())

    manifest_pin_checks = {
        "QUESTION.md": sha256_file(directory / "QUESTION.md")
        == "d11a55ce9dc747af2c43935fd352f083d483fd478400512bf7e9c01328064ad6",
        "RESULT.md": sha256_file(directory / "RESULT.md")
        == "a8a63cc9a2bfab6acea2ded42e851fe3d6a185e15f9962bbe802a0ecb1866445",
        "FAILED_ROUTES.md": sha256_file(directory / "FAILED_ROUTES.md")
        == "a87f6076ff69a9bc1c95976cc95849cd9971d5334a00830adaba3b4ccba20c47",
    }
    assert all(manifest_pin_checks.values())

    small_universe_checks = 0
    first_equal_product_distinct_orbits: dict[str, object] | None = None
    for small_modulus in range(3, 302, 2):
        value_orbits: dict[int, set[tuple[int, int]]] = {}
        for residue in range(1, small_modulus):
            if gcd(residue, small_modulus) != 1:
                continue
            inverse = pow(residue, -1, small_modulus)
            exact_value = residue * inverse
            orbit = tuple(sorted((residue, inverse)))
            value_orbits.setdefault(exact_value, set()).add(orbit)

        if first_equal_product_distinct_orbits is None:
            for exact_value, orbits in sorted(value_orbits.items()):
                if len(orbits) > 1:
                    first_equal_product_distinct_orbits = {
                        "N": small_modulus,
                        "P": exact_value,
                        "orbits": [list(orbit) for orbit in sorted(orbits)],
                    }
                    break

        row_degrees: dict[int, int] = {}
        for exact_value in value_orbits:
            if exact_value == 1:
                continue
            for prime, exponent in factorization(exact_value).items():
                if exponent % 2 == 1:
                    row_degrees[prime] = row_degrees.get(prime, 0) + 1
        for prime, degree in row_degrees.items():
            assert degree <= (small_modulus - 1) // prime
            if prime > (small_modulus - 1) // 2:
                assert degree == 1
        small_universe_checks += 1

    assert first_equal_product_distinct_orbits == {
        "N": 11,
        "P": 12,
        "orbits": [[2, 6], [3, 4]],
    }
    raw_n11_columns_for_p12 = [
        residue
        for residue in range(1, 11)
        if gcd(residue, 11) == 1 and residue * pow(residue, -1, 11) == 12
    ]
    assert raw_n11_columns_for_p12 == [2, 3, 4, 6]

    trace_checks = {
        "candidate_trace_reproduced": reproduced_candidate_trace.hexdigest()
        == candidate_output["candidate_trace_sha256"],
        "first_accepted_ordinal_23": found["ordinal"] == 23,
        "all_earlier_private_values_composite": len(rejection_certificates) == 22
        and all(item["reason"] == "private_prime_composite" for item in rejection_certificates),
    }
    assert all(trace_checks.values())

    payload = {
        "status": "PASS",
        "method": {
            "candidate_code_imported_or_executed": False,
            "primality_method": "complete trial division through integer square root",
            "small_universe_range": "odd N from 3 through 301",
        },
        "artifact_hash_checks": artifact_hash_checks,
        "manifest_pin_checks": manifest_pin_checks,
        "arithmetic_checks": arithmetic_checks,
        "trace_checks": trace_checks,
        "independent_trace_sha256": independent_trace.hexdigest(),
        "rejection_certificates": rejection_certificates,
        "candidate": found,
        "small_universe": {
            "moduli_checked": small_universe_checks,
            "degree_bound_and_stable_corollary_passed": True,
            "first_equal_product_distinct_orbits": first_equal_product_distinct_orbits,
            "raw_N11_residues_for_P12": raw_n11_columns_for_p12,
            "exact_value_columns_for_P12": 1,
        },
    }
    Path(args.output).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "first_accepted_ordinal": found["ordinal"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
