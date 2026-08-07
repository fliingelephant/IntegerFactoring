#!/usr/bin/env python3
"""Exact symbolic replay of the allowed F59-D02 finite certificate artifact."""

from __future__ import annotations

import argparse
import json
import math
import signal
import traceback
from collections import Counter, defaultdict
from pathlib import Path

import sympy as sp


T = sp.Symbol("T")


def affine_lift(N: int, start_offset: int, step_index: int) -> dict:
    """Lift one inverse-descent provenance branch to Q[T]."""
    u = N - start_offset
    U = T - start_offset
    history = []

    for step in range(step_index + 1):
        v = pow(u, -1, N)
        k, rem = divmod(u * v - 1, N)
        assert rem == 0

        u0 = sp.Rational(U.subs(T, 0))
        assert u0 != 0
        v0 = 1 / u0
        slope = (sp.Rational(v) - v0) / N
        V = sp.expand(slope * T + v0)
        K = sp.cancel((U * V - 1) / T)

        assert sp.rem(sp.Poly(sp.together(U * V - 1), T), sp.Poly(T, T)) == 0
        assert sp.degree(K, T) <= 1
        assert sp.Rational(U.subs(T, N)) == u
        assert sp.Rational(V.subs(T, N)) == v
        assert sp.Rational(K.subs(T, N)) == k
        assert sp.expand(U * V - (T * K + 1)) == 0

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
            U = sp.expand(K)

    return {
        "u": u,
        "v": v,
        "k": k,
        "U_expr": sp.expand(U),
        "V_expr": sp.expand(V),
        "K_expr": sp.expand(K),
        "A_expr": sp.expand(U * V),
        "history": history,
    }


def rational_square_root(q: sp.Rational) -> sp.Rational | None:
    q = sp.Rational(q)
    if q < 0:
        return None
    rn = math.isqrt(int(q.p))
    rd = math.isqrt(int(q.q))
    if rn * rn != q.p or rd * rd != q.q:
        return None
    return sp.Rational(rn, rd)


def polynomial_square_root(expr: sp.Expr) -> sp.Expr | None:
    coeff, factors = sp.factor_list(sp.Poly(sp.expand(expr), T, domain=sp.QQ))
    root_coeff = rational_square_root(sp.Rational(coeff))
    if root_coeff is None or any(exponent % 2 for _, exponent in factors):
        return None
    root = root_coeff
    for factor, exponent in factors:
        root *= factor.as_expr() ** (exponent // 2)
    return sp.expand(root)


def coefficient_denominator(expr: sp.Expr) -> int:
    denominator = 1
    for coefficient in sp.Poly(sp.expand(expr), T, domain=sp.QQ).all_coeffs():
        denominator = math.lcm(denominator, int(sp.Rational(coefficient).q))
    return denominator


def canonical_expr(expr: sp.Expr) -> str:
    return str(sp.Poly(sp.expand(expr), T, domain=sp.QQ).as_expr())


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
            product_expr = sp.Integer(1)
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
                assert sp.Rational(primary["A_expr"].subs(T, N)) == relation["A"]
                assert sp.Rational(primary["A_expr"].subs(T, 0)) == 1

                all_provenances = [
                    [int(relation["start_offset"]), int(relation["step_index"])]
                ] + [list(map(int, branch)) for branch in relation["duplicate_provenance"]]
                provenance_lifts = []
                for start_offset, step_index in all_provenances:
                    provenance_count += 1
                    lifted = affine_lift(N, start_offset, step_index)
                    assert lifted["u"] == relation["u"]
                    assert lifted["v"] == relation["v"]
                    assert lifted["k"] == relation["k"]
                    assert sp.Rational(lifted["A_expr"].subs(T, N)) == relation["A"]
                    assert sp.Rational(lifted["A_expr"].subs(T, 0)) == 1
                    provenance_lifts.append(
                        {
                            "start_offset": start_offset,
                            "step_index": step_index,
                            "U": canonical_expr(lifted["U_expr"]),
                            "V": canonical_expr(lifted["V_expr"]),
                            "K": canonical_expr(lifted["K_expr"]),
                            "A": canonical_expr(lifted["A_expr"]),
                            "same_symbolic_A_as_primary": sp.expand(
                                lifted["A_expr"] - primary["A_expr"]
                            )
                            == 0,
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
            assert not odd_labels

            product_expr = sp.expand(product_expr)
            root_expr = polynomial_square_root(product_expr)
            assert root_expr is not None
            root_at_N = sp.Rational(root_expr.subs(T, N))
            if root_at_N < 0:
                root_expr = -root_expr
                root_at_N = -root_at_N
            assert root_at_N.q == 1

            exact_integer_root = math.isqrt(product_integer)
            assert exact_integer_root * exact_integer_root == product_integer
            assert int(root_at_N) == exact_integer_root
            assert int(root_at_N) % N == certificate["root_mod_N"]

            constant = sp.Rational(root_expr.subs(T, 0))
            assert constant in (sp.Integer(-1), sp.Integer(1))
            denominator = coefficient_denominator(root_expr)
            denominator_gcd = math.gcd(denominator, N)
            residual = sp.cancel((root_expr - constant) / T)
            assert sp.expand(root_expr - (constant + T * residual)) == 0

            key = canonical_expr(root_expr)
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
                    "root": key,
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
        "run_id": "F60-RECON-D02-VERIFY-01",
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
            "F60-RECON-D02-VERIFY-01: PASS",
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
        args.log.write_text("F60-RECON-D02-VERIFY-01: FAIL\n" + traceback.format_exc())
        raise
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    main()
