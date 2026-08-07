#!/usr/bin/env python3
"""Exact SageMath replay of the allowed F59-D02 finite certificate artifact."""

from __future__ import annotations

import argparse
import json
import math
import signal
import traceback
from collections import Counter, defaultdict
from pathlib import Path

from sage.all import PolynomialRing, QQ


POLYS = PolynomialRing(QQ, "T")
T = POLYS.gen()


def affine_lift(N: int, start_offset: int, step_index: int) -> dict:
    """Lift one inverse-descent provenance branch to Q[T]."""
    u = N - start_offset
    U = POLYS(T - start_offset)
    history = []

    for step in range(step_index + 1):
        v = pow(u, -1, N)
        k, rem = divmod(u * v - 1, N)
        assert rem == 0

        u0 = QQ(U[0])
        assert u0 != 0
        v0 = 1 / u0
        slope = (QQ(v) - v0) / N
        V = POLYS(slope * T + v0)
        numerator = U * V - 1
        K, remainder = numerator.quo_rem(T)

        assert remainder == 0
        assert K.degree() <= 1
        assert QQ(U(N)) == u
        assert QQ(V(N)) == v
        assert QQ(K(N)) == k
        assert U * V == T * K + 1

        history.append(
            {
                "step": step,
                "u": u,
                "v": v,
                "k": k,
                "U": str(U),
                "V": str(V),
                "K": str(K),
            }
        )
        if step != step_index:
            u = k
            U = POLYS(K)

    return {
        "u": u,
        "v": v,
        "k": k,
        "U_expr": U,
        "V_expr": V,
        "K_expr": K,
        "A_expr": U * V,
        "history": history,
    }


def rational_square_root(q):
    q = QQ(q)
    if q < 0:
        return None
    numerator = int(q.numerator())
    denominator = int(q.denominator())
    root_numerator = math.isqrt(numerator)
    root_denominator = math.isqrt(denominator)
    if root_numerator**2 != numerator or root_denominator**2 != denominator:
        return None
    return QQ(root_numerator) / root_denominator


def polynomial_square_root(expr):
    factorization = POLYS(expr).factor()
    root_coefficient = rational_square_root(factorization.unit())
    if root_coefficient is None or any(exponent % 2 for _, exponent in factorization):
        return None
    root = POLYS(root_coefficient)
    for factor, exponent in factorization:
        root *= factor ** (exponent // 2)
    return POLYS(root)


def coefficient_denominator(expr) -> int:
    denominator = 1
    for coefficient in POLYS(expr).list():
        denominator = math.lcm(denominator, int(QQ(coefficient).denominator()))
    return denominator


def canonical_expr(expr) -> str:
    return str(POLYS(expr))


def verify(input_path: Path) -> dict:
    artifact = json.loads(input_path.read_text())
    results = []
    template_groups = defaultdict(list)
    arithmetic_template_groups = defaultdict(list)
    certificate_count = 0
    relation_count = 0
    provenance_count = 0

    for record_index, record in enumerate(artifact["records"]):
        N = int(record["N"])
        certificates = record["full_offset_batch"]["certificates"]
        assert len(certificates) == record["full_offset_batch"]["kernel_dimension"]

        for certificate_index, certificate in enumerate(certificates):
            certificate_count += 1
            product_expr = POLYS(1)
            product_integer = 1
            lifted_relations = []
            endpoint_counts = Counter()

            for relation_index, relation in enumerate(certificate["selected_relations"]):
                relation_count += 1
                primary = affine_lift(
                    N,
                    int(relation["start_offset"]),
                    int(relation["step_index"]),
                )
                assert primary["u"] == relation["u"]
                assert primary["v"] == relation["v"]
                assert primary["k"] == relation["k"]
                assert relation["A"] == relation["u"] * relation["v"]
                assert relation["A"] == relation["k"] * N + 1
                assert QQ(primary["A_expr"](N)) == relation["A"]
                assert QQ(primary["A_expr"](0)) == 1

                all_provenances = [
                    [int(relation["start_offset"]), int(relation["step_index"])]
                ] + [list(map(int, branch)) for branch in relation["duplicate_provenance"]]
                provenance_lifts = []
                for provenance_index, (start_offset, step_index) in enumerate(all_provenances):
                    provenance_count += 1
                    lifted = affine_lift(N, start_offset, step_index)
                    if provenance_index == 0:
                        assert lifted["u"] == relation["u"]
                        assert lifted["v"] == relation["v"]
                        orientation = "selected"
                    elif (lifted["u"], lifted["v"]) == (relation["u"], relation["v"]):
                        orientation = "same"
                    elif (lifted["u"], lifted["v"]) == (relation["v"], relation["u"]):
                        orientation = "swapped"
                    else:
                        orientation = "distinct_factorization"
                    assert lifted["k"] == relation["k"]
                    assert QQ(lifted["A_expr"](N)) == relation["A"]
                    assert QQ(lifted["A_expr"](0)) == 1
                    provenance_lifts.append(
                        {
                            "start_offset": start_offset,
                            "step_index": step_index,
                            "endpoint_orientation": orientation,
                            "U": canonical_expr(lifted["U_expr"]),
                            "V": canonical_expr(lifted["V_expr"]),
                            "K": canonical_expr(lifted["K_expr"]),
                            "A": canonical_expr(lifted["A_expr"]),
                            "same_symbolic_A_as_primary": lifted["A_expr"]
                            == primary["A_expr"],
                        }
                    )

                product_expr *= primary["A_expr"]
                product_integer *= int(relation["A"])
                endpoint_counts[int(relation["u"])] += 1
                endpoint_counts[int(relation["v"])] += 1
                lifted_relations.append(
                    {
                        "relation_index": relation_index,
                        "A_at_N": relation["A"],
                        "primary_A": canonical_expr(primary["A_expr"]),
                        "primary_U": canonical_expr(primary["U_expr"]),
                        "primary_V": canonical_expr(primary["V_expr"]),
                        "primary_K": canonical_expr(primary["K_expr"]),
                        "provenance_lifts": provenance_lifts,
                    }
                )

            odd_labels = sorted(label for label, count in endpoint_counts.items() if count % 2)
            assert odd_labels == certificate["odd_endpoint_labels"]

            root_expr = polynomial_square_root(product_expr)
            assert root_expr is not None
            root_at_N = QQ(root_expr(N))
            if root_at_N < 0:
                root_expr = -root_expr
                root_at_N = -root_at_N
            assert root_at_N.denominator() == 1

            exact_integer_root = math.isqrt(product_integer)
            assert exact_integer_root**2 == product_integer
            assert int(root_at_N) == exact_integer_root
            assert int(root_at_N) % N == certificate["root_mod_N"]

            constant = QQ(root_expr(0))
            assert constant in (QQ(-1), QQ(1))
            denominator = coefficient_denominator(root_expr)
            denominator_gcd = math.gcd(denominator, N)
            residual, remainder = (root_expr - constant).quo_rem(T)
            assert remainder == 0
            assert root_expr == constant + T * residual

            residual_key = canonical_expr(residual)
            cert_id = f"record-{record_index:02d}-certificate-{certificate_index:02d}"
            template_groups[residual_key].append(cert_id)
            if not certificate["contains_N_minus_1_loop"]:
                arithmetic_template_groups[residual_key].append(cert_id)

            results.append(
                {
                    "certificate_id": cert_id,
                    "N": N,
                    "support_size": certificate["support_size"],
                    "formal_endpoint": certificate["contains_N_minus_1_loop"],
                    "product_is_symbolic_square": True,
                    "root": canonical_expr(root_expr),
                    "root_constant": int(constant),
                    "least_coefficient_denominator": denominator,
                    "denominator_gcd_N": denominator_gcd,
                    "root_at_N": int(root_at_N),
                    "root_mod_N": int(root_at_N) % N,
                    "residual_template": residual_key,
                    "relations": lifted_relations,
                }
            )

    assert certificate_count == 19
    assert all(result["denominator_gcd_N"] == 1 for result in results)
    assert all(result["root_constant"] in (-1, 1) for result in results)
    assert len(arithmetic_template_groups) == 4

    return {
        "run_id": "F60-RECON-D02-VERIFY-SAGE-04",
        "source_artifact_run": artifact["run"],
        "certificate_count": certificate_count,
        "selected_relation_count": relation_count,
        "provenance_branch_count_including_duplicates": provenance_count,
        "all_products_symbolic_squares": True,
        "all_root_constants_global_signs": True,
        "all_denominator_gcds_one": True,
        "distinct_residual_template_count_all": len(template_groups),
        "distinct_residual_template_count_arithmetic": len(arithmetic_template_groups),
        "arithmetic_residual_template_groups": dict(arithmetic_template_groups),
        "all_residual_template_groups": dict(template_groups),
        "certificates": results,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--log", required=True, type=Path)
    args = parser.parse_args()

    signal.signal(signal.SIGALRM, lambda _signum, _frame: (_ for _ in ()).throw(TimeoutError()))
    signal.alarm(120)
    try:
        result = verify(args.input)
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        summary = [
            "F60-RECON-D02-VERIFY-SAGE-04: PASS",
            f"certificates={result['certificate_count']}",
            f"selected_relations={result['selected_relation_count']}",
            f"provenance_branches={result['provenance_branch_count_including_duplicates']}",
            f"all_templates={result['distinct_residual_template_count_all']}",
            f"arithmetic_templates={result['distinct_residual_template_count_arithmetic']}",
            "all_products_symbolic_squares=true",
            "all_root_constants_global_signs=true",
            "all_denominator_gcds_one=true",
        ]
        args.log.write_text("\n".join(summary) + "\n")
    except Exception:
        args.log.write_text("F60-RECON-D02-VERIFY-SAGE-04: FAIL\n" + traceback.format_exc())
        raise
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    main()
