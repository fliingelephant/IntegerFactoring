# F193 V3 self-audit

## Verdict

V3 repairs the only blocking issue found by the V2 hostile re-audit. It
changes the malformed TeX

```text
+operatorname{Nm}(\alpha)
```

to

```text
+\operatorname{Nm}(\alpha)
```

in the statement and proof. It also normalizes two literal Greek beta
characters to TeX commands and updates version labels. No mathematical claim
changes from V2.

The V2 re-auditor found no deeper mathematical defect and passed all four
substantive claims within their exact scopes. V3 still needs a fresh strict
hostile audit of its new frozen hashes and then a statement-only blind
reconstruction before promotion.

No mathematical computation was run. No durable ledger was edited.

## Inherited mathematical checks

1. The squarefree `Gamma_0(N)` cusp theorem concerns explicit rational
   boundary support only. It does not control the coefficient on the global
   cusp line, a boundary-zero class, or a compressed dense presentation.
2. Good-prime Hecke branches preserve the denominator divisor. Fricke sends
   `d` to `N/d`. A standard selective Atkin--Lehner operator is explicitly
   labeled by a proper exact divisor.
3. The uniform small-modulus theorem requires one evaluator over a growing
   bank. CRT over `O(n)` small primes reconstructs the exact `b_N`.
4. An arbitrary imprimitive twist bank has rank at most one. Public zero rows
   are allowed. Recovery requires one nonzero row. The defining modulus and
   conductor are not conflated.
5. The torsion theorem uses one global endomorphism on auxiliary-prime
   torsion over a connected base. Local Frobenius, reduction-only
   endomorphisms, and mixed CRT maps remain outside it.
6. The auxiliary-prime restriction makes the minimal polynomial canonical.
   The CM characteristic polynomial is justified through Tate-module trace
   and determinant.

## Scope check

V3 remains a collection of four named boundaries. It is not a general
modular-symbol, cusp-form, modular-form, finite-etale, elliptic-torsion, or
factoring lower bound.
