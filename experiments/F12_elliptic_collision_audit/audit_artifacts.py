#!/usr/bin/env python3
"""Independent artifact and small-certificate audit for F12.

Approach-family ID: F12_elliptic_collision_audit.
Uses only the Python standard library.  It validates all manifest-named source
hashes, successful/partial outputs, failure signatures, and independently
recomputes the retained elliptic and torus examples.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


FAMILY = "F12_elliptic_collision_audit"

EXPECTED_SOURCE_HASHES = {
    "search_clean_synchronized.sage": "4b98339369bdb79e33d545a3e1fce54c8e19f252ecf136269722b24864a0d92e",
    "verify_torus_reduction.sage": "cb6b20adc412ed97f4c70f8c7942f6ad6e3ed552968959fca093d2f8c3f7a511",
    "verify_division_identity.sage": "cdd4196510c10936248a96223321be35a94ea25c2235dbb83815522ac54dd8a0",
    "verify_torus_prime_powers.sage": "6f4022faebe13be37ea67212dfecf18fbb0bc452ed9a60865ae79547f7c0bae4",
    "verify_floor_clean_witness.sage": "a933956d18248c6ffe5d0f49c0a765eb4495a5b7b2476639bba56b6b2b074334",
    "audit_certificates.py": "5c75400520647f7d9f92d1d6b5745c0560006743c98d97353973a5ca38f292c6",
}

SUCCESS_OUTPUTS = {
    "R01_clean_synchronized.json",
    "R04_torus_reduction.json",
    "R06_division_identity.json",
    "R07_torus_prime_powers.json",
    "R09_floor_clean_witness.json",
    "R10_audit.json",
}

PARTIAL_OUTPUTS = {
    "R03_torus_reduction.json",
    "R08_floor_clean_witness.json",
}

FAILURE_SIGNATURES = {
    "R02_torus_reduction.log": "TypeError: unsupported operand type(s)",
    "R03_torus_reduction.log": "TypeError: Object of type Integer is not JSON serializable",
    "R05_division_identity.log": "AssertionError",
    "R08_floor_clean_witness.log": "TypeError: Object of type Integer is not JSON serializable",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inverse(value: int, prime: int) -> int:
    return pow(value % prime, -1, prime)


def point_add(
    left: tuple[int, int] | None,
    right: tuple[int, int] | None,
    prime: int,
    curve_a: int,
) -> tuple[int, int] | None:
    if left is None:
        return right
    if right is None:
        return left
    x1, y1 = left
    x2, y2 = right
    if x1 == x2 and (y1 + y2) % prime == 0:
        return None
    if left == right:
        slope = (3 * x1 * x1 + curve_a) * inverse(2 * y1, prime) % prime
    else:
        slope = (y2 - y1) * inverse(x2 - x1, prime) % prime
    x3 = (slope * slope - x1 - x2) % prime
    y3 = (slope * (x1 - x3) - y1) % prime
    return x3, y3


def point_mul(
    scalar: int,
    point: tuple[int, int],
    prime: int,
    curve_a: int,
) -> tuple[int, int] | None:
    result = None
    addend = point
    while scalar:
        if scalar & 1:
            result = point_add(result, addend, prime, curve_a)
        addend = point_add(addend, addend, prime, curve_a)
        scalar >>= 1
    return result


def point_order(point: tuple[int, int], prime: int, curve_a: int, bound: int) -> int:
    current = None
    for order in range(1, bound + 1):
        current = point_add(current, point, prime, curve_a)
        if current is None:
            return order
    raise AssertionError("point order exceeded supplied Hasse bound")


def curve_order(prime: int, curve_a: int, curve_b: int) -> int:
    affine = sum(
        (y * y - x**3 - curve_a * x - curve_b) % prime == 0
        for x in range(prime)
        for y in range(prime)
    )
    return affine + 1


def division_values(
    prime: int,
    curve_a: int,
    curve_b: int,
    point: tuple[int, int],
) -> callable:
    x, y = point
    cache = {
        0: 0,
        1: 1,
        2: 2 * y % prime,
        3: (3 * x**4 + 6 * curve_a * x * x + 12 * curve_b * x - curve_a**2) % prime,
        4: (
            4
            * y
            * (
                x**6
                + 5 * curve_a * x**4
                + 20 * curve_b * x**3
                - 5 * curve_a**2 * x * x
                - 4 * curve_a * curve_b * x
                - 8 * curve_b**2
                - curve_a**3
            )
        )
        % prime,
    }

    def psi(index: int) -> int:
        if index in cache:
            return cache[index]
        if index % 2:
            half = (index - 1) // 2
            value = psi(half + 2) * psi(half) ** 3 - psi(half - 1) * psi(half + 1) ** 3
        else:
            half = index // 2
            value = (
                psi(half)
                * inverse(2 * y, prime)
                * (psi(half + 2) * psi(half - 1) ** 2 - psi(half - 2) * psi(half + 1) ** 2)
            )
        cache[index] = value % prime
        return cache[index]

    return psi


def multiplicative_order(base: int, prime: int) -> int:
    value = 1
    for order in range(1, prime):
        value = value * base % prime
        if value == 1:
            return order
    raise AssertionError("unit order not found")


def torus_product(base: int, length: int, modulus: int) -> int:
    value = 1
    power = base % modulus
    for difference in range(1, length):
        value = value * pow(1 - power, length - difference, modulus) % modulus
        power = power * base % modulus
    return value


def audit_elliptic() -> dict[str, object]:
    p, q, n, length = 101, 103, 101 * 103, math.isqrt(101 * 103)
    curve_a, curve_b = 1, 5
    global_point = (5461, 5889)
    discriminant = -16 * (4 * curve_a**3 + 27 * curve_b**2)
    assert length == 101 and 2 * length - 1 == 201
    assert discriminant % n == 9942 and math.gcd(discriminant, n) == 1
    assert (global_point[1] ** 2 - global_point[0] ** 3 - curve_a * global_point[0] - curve_b) % n == 0

    local_records = []
    for prime, expected_point, expected_group_order, expected_order, expected_collision in (
        (p, (7, 31), 112, 112, (11, 101)),
        (q, (2, 18), 106, 106, (5, 101)),
    ):
        point = (global_point[0] % prime, global_point[1] % prime)
        assert point == expected_point
        assert (point[1] ** 2 - point[0] ** 3 - curve_a * point[0] - curve_b) % prime == 0
        group_order = curve_order(prime, curve_a, curve_b)
        hasse_floor = prime + 1 + math.isqrt(4 * prime)
        order = point_order(point, prime, curve_a, hasse_floor)
        assert group_order == expected_group_order and order == expected_order
        assert group_order <= hasse_floor <= 201
        multiples = [point_mul(index, point, prime, curve_a) for index in range(1, length + 1)]
        assert all(multiple is not None for multiple in multiples)
        collisions = [
            (left, right)
            for left in range(1, length + 1)
            for right in range(left + 1, length + 1)
            if multiples[left - 1][0] == multiples[right - 1][0]
        ]
        assert collisions[0] == expected_collision
        assert all((left + right) % order == 0 for left, right in collisions)

        psi = division_values(prime, curve_a, curve_b, point)
        assert all(psi(index) != 0 for index in range(1, length + 1))
        assert [index for index in range(1, 202) if psi(index) == 0] == [order]
        for left in range(1, 11):
            for right in range(left + 1, 11):
                phi_left = (point[0] * psi(left) ** 2 - psi(left + 1) * psi(left - 1)) % prime
                phi_right = (point[0] * psi(right) ** 2 - psi(right + 1) * psi(right - 1)) % prime
                lhs = (phi_left * psi(right) ** 2 - phi_right * psi(left) ** 2) % prime
                rhs = psi(left + right) * psi(right - left) % prime
                assert lhs == rhs

        local_records.append(
            {
                "prime": prime,
                "hasse_upper_floor": hasse_floor,
                "group_order": group_order,
                "point_order": order,
                "first_floor_collision": list(collisions[0]),
                "floor_collision_count": len(collisions),
            }
        )
    return {"N": n, "m_floor_sqrt_N": length, "discriminant_mod_N": discriminant % n, "local": local_records}


def audit_torus() -> dict[str, object]:
    instances = []
    for p, q, expected_probability in ((101, 103, Fraction(16, 51)), (11, 101, Fraction(3, 5))):
        n = p * q
        length = math.isqrt(n)
        assert p <= length < q
        success_q = sum(multiplicative_order(base, q) >= length for base in range(1, q))
        probability = Fraction(success_q, q - 1)
        assert probability == expected_probability
        unit_count = success_count = 0
        for base in range(1, n):
            if math.gcd(base, n) != 1:
                continue
            unit_count += 1
            value = torus_product(base, length, n)
            expected = multiplicative_order(base % q, q) >= length
            assert value % p == 0
            assert (value % q != 0) == expected
            assert (math.gcd(value, n) == p) == expected
            success_count += expected
        assert unit_count == (p - 1) * (q - 1)
        assert success_count == (p - 1) * success_q
        instances.append(
            {
                "N": n,
                "m": length,
                "successful_units": success_count,
                "conditional_probability": str(probability),
            }
        )
    return {"instances": instances}


def audit_artifacts(source_dir: Path) -> dict[str, object]:
    source_hashes = {name: sha256(source_dir / name) for name in EXPECTED_SOURCE_HASHES}
    assert source_hashes == EXPECTED_SOURCE_HASHES

    output_dir = source_dir / "output"
    records = {name: json.loads((output_dir / name).read_text()) for name in SUCCESS_OUTPUTS}
    assert all(record["approach_family"] == "F12_elliptic_collision_kill" for record in records.values())
    for name in PARTIAL_OUTPUTS:
        try:
            json.loads((output_dir / name).read_text())
        except json.JSONDecodeError:
            pass
        else:
            raise AssertionError(f"expected invalid partial JSON: {name}")
    assert not (output_dir / "R02_torus_reduction.json").exists()
    assert not (output_dir / "R05_division_identity.json").exists()

    log_dir = source_dir / "logs"
    failure_logs = {}
    for name, signature in FAILURE_SIGNATURES.items():
        content = (log_dir / name).read_text()
        assert signature in content
        failure_logs[name] = sha256(log_dir / name)
    successful_logs = [
        "R01_clean_synchronized.log",
        "R04_torus_reduction.log",
        "R06_division_identity.log",
        "R07_torus_prime_powers.log",
        "R09_floor_clean_witness.log",
        "R10_audit.log",
    ]
    assert all((log_dir / name).read_bytes() == b"" for name in successful_logs)

    audit_record = records["R10_audit.json"]
    audit_inputs = {
        "elliptic": output_dir / "R01_clean_synchronized.json",
        "torus": output_dir / "R04_torus_reduction.json",
        "division": output_dir / "R06_division_identity.json",
        "prime_powers": output_dir / "R07_torus_prime_powers.json",
        "floor_witness": output_dir / "R09_floor_clean_witness.json",
    }
    actual_input_hashes = {name: sha256(path) for name, path in audit_inputs.items()}
    assert actual_input_hashes == audit_record["input_sha256"]
    assert audit_record["source_sha256"] == source_hashes["audit_certificates.py"]

    generated = {path.name: sha256(path) for path in sorted(source_dir.glob("*.sage.py"))}
    return {
        "manifest_source_hashes": source_hashes,
        "successful_output_hashes": {name: sha256(output_dir / name) for name in sorted(SUCCESS_OUTPUTS)},
        "partial_invalid_output_hashes": {name: sha256(output_dir / name) for name in sorted(PARTIAL_OUTPUTS)},
        "failure_log_hashes": failure_logs,
        "successful_logs_are_empty": successful_logs,
        "r10_input_hashes_reproduced": actual_input_hashes,
        "unmanifested_generated_sage_python_hashes": generated,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    source_dir = Path(args.source_dir).resolve()
    output_path = Path(args.output).resolve()
    result = {
        "approach_family": FAMILY,
        "artifact_audit": audit_artifacts(source_dir),
        "independent_elliptic_recomputation": audit_elliptic(),
        "independent_torus_recomputation": audit_torus(),
        "source": str(Path(__file__).resolve()),
        "source_sha256": sha256(Path(__file__).resolve()),
    }
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()

