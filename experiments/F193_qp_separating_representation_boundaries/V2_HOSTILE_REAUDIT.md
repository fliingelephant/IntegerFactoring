# Hostile re-audit of F193 V2

## Verdict

**FAIL as frozen.** The only blocking defect I found is a literal formula
defect in equation (4.2), present in both `V2_STATEMENT.md` and
`V2_PROOF.md`:

```tex
+operatorname{Nm}(\alpha)
```

must be

```tex
+\operatorname{Nm}(\alpha).
```

Without the backslash, the frozen source does not denote the norm operator;
in TeX mathematics it is a product of letter variables followed by
`Nm(\alpha)`. Thus the displayed characteristic-polynomial identity is not
the claimed identity as written. This is a transcription defect, not a
failure of the underlying theorem. I found no other blocking defect. After
this exact two-file correction and a new freeze, all four substantive claims
pass within their stated narrow scopes.

No mathematical computation was run. No durable ledger was edited.

## Frozen-input verification

Before reading the candidate, I recomputed all four V2 hashes. They agree
with `V2_MANIFEST.md`:

- `V2_STATEMENT.md`:
  `742c92183596cb2e3e2da8a9fa05234912d3c295312e8cdc79caed03ea375441`;
- `V2_PROOF.md`:
  `fa9d6231c42887be1f3231d0f71c04f2aa059bbf0dfd549f31fee8f50a8db523`;
- `V2_SELF_AUDIT.md`:
  `afcebb4495496986d74fc47672e42978c5db54f910b5a1f1e5b4a495a9c3dc0a`;
- `V2_PROVENANCE.md`:
  `b6100b0e74aa9b0d0c7e1f461185ae85e25e32eb42df9e8829799c73c5df8fea`.

I attacked `V2_STATEMENT.md` and `V2_PROOF.md` before consulting
`V2_SELF_AUDIT.md`, `V2_PROVENANCE.md`, or the V1 hostile audit.

## 1. Explicit sparse modular-symbol cusp boundary

This section passes under its stated integral sparse-chain convention.

For each prime `s | N`, the proof handles rational reduction in both
directions. If `s | c`, then the transformed denominator is zero modulo `s`
and the transformed numerator is `Aa != 0` modulo `s`; cancellation cannot
remove `s`. If `s` does not divide `c`, the transformed denominator is
`Dc != 0` modulo `s`. Hence `gcd(c,N)` is invariant. The standard cusp
classification has one orbit for each divisor `d | N` because
`gcd(d,N/d)=1` when `N` is squarefree.

The total sparse-chain scope is adequate: coefficients, reduced endpoint
numerators, and reduced endpoint denominators all count toward one
numerical-QP total encoding. Thus all endpoint reductions and gcds have
numerical-QP total cost. If no endpoint has type `p` or `q`, every endpoint
maps to one of the two global cusp orbits. The degree-zero boundary of an
integral chain is then an integer multiple of `[c_N]-[c_1]`. This is only a
support statement. It does not constrain that integer coefficient.

For a standard upper-triangular branch of `T_m` with `gcd(m,N)=1`, both
diagonal entries are units at every level prime. The same cancellation
argument proves exact type preservation branch by branch. This does not
cover bad-prime Hecke operators or opaque nonstandard implementations.

Fricke has the exact action `d -> N/d`. It swaps `1` with `N` and `p` with
`q`, so the frozen text correctly states preservation of the two-block
global/hidden partition.

For a squarefree exact divisor `Q`, the stated Atkin--Lehner action toggles
the primes in `Q`. At level `pq`, a proper selective label is exactly `p` or
`q`. The determinant statement is correctly restricted to a standard
unnormalized integral representative. It is not asserted for normalized
analytic matrices or opaque circuits.

There is no hidden cancellation inference here. The theorem does not cover
boundary-zero cuspidal classes, metric boundary coefficients, periods, or
compressed dense chains.

## 2. Uniform small-prime bank and CRT

This section passes.

On the promised distinct-prime semiprime input,

```text
b_N = (1+p)(1+q) = N+p+q+1
```

and `0 < b_N < 2(N+1) <= 2^(n+1)`. Taking `n+2` distinct auxiliary primes
gives a CRT modulus strictly above this bound. The standard bound on the
`k`-th prime places the required bank below `C n log(n+2)` for one absolute
constant `C`. Every bank prime has `O(log n)` bits, and the bank has `O(n)`
members.

A bank prime sharing a proper gcd with `N` gives a factor before an oracle
call. In the `24b_N` interface, omission of 2 and 3 makes 24 invertible.
CRT then recovers the unique exact integer `b_N`. The discriminant
`(p+q)^2-4N=(p-q)^2` recovers the factors. Polynomially many numerical-QP
calls and polynomial postprocessing remain numerical QP.

The premise is uniform in the varying auxiliary prime. A fixed modulus or a
fixed finite bank is not amplified by this proof. The section supplies no
coefficient evaluator.

## 3. Arbitrary Dirichlet twists

This section passes and fully repairs the V1 principal-character
counterexample.

For every Dirichlet character under the stated zero-extension convention,
including an imprimitive character,

```text
a_(f tensor chi)(N) = chi(N) a_f(N).
```

The identity remains valid when `chi(N)=0`. After fixing compatible
embeddings into explicitly represented composita, the bank is the image of
one coefficient under the public linear map

```text
x -> (chi_1(N)x, ..., chi_L(N)x).
```

Its rank is therefore at most one. An all-zero bank has rank zero. If one
row is nonzero, its scalar is a public root of unity, so division recovers
the base coefficient.

V2 no longer infers nonvanishing from the conductor of an arbitrary
imprimitive character. It only asserts nonvanishing when the defining
modulus is coprime to `N`, or when a primitive character is presented at a
conductor coprime to `N`. The principal character modulo `N` has conductor
one but value zero at `N`; it is now an allowed rank-zero row, not a
counterexample.

A defining modulus can itself reveal a gcd with `N`. That separate public
leak does not change the coefficient-rank identity. The theorem also does
not say that different twist evaluators have equal cost. It gives no lower
bound and does not cover different forms, Rankin convolutions, nontwist
operations, or other indices.

## 4. One descended endomorphism on auxiliary-prime torsion

The substantive theorem in this section passes.

Because `r` is invertible on the connected base, `E[r]` is a rank-two lisse
`F_r`-module. Etale path transport between geometric fibers is natural in a
globally defined endomorphism. Therefore it intertwines the two fiber
actions, and their matrices are conjugate over `F_r` after basis choices.
Conjugacy preserves the characteristic polynomial, the unique monic minimal
polynomial over the field `F_r`, and the group order when the matrix is
invertible. The prime-torsion restriction removes the noncanonical
composite-ring minimal-polynomial problem from V1.

For a globally defined CM endomorphism, the prime-to-characteristic Tate
module has trace `Tr(alpha)` and determinant
`Nm(alpha)=deg(alpha)`. Hence its characteristic polynomial is

```tex
X^2-\operatorname{Tr}(\alpha)X+\operatorname{Nm}(\alpha),
```

and reduction modulo `r` gives the common polynomial on both `r`-torsion
fibers. This trace-and-norm argument is sufficient; it does not rely only on
an annihilating quadratic. The frozen prose states the trace and determinant
correctly. Only the two displayed copies of (4.2) have the transcription
defect identified in the verdict.

The result requires one endomorphism descended over one connected base. It
does not control local Frobenius, endomorphisms appearing only after
reduction, characteristic-primary torsion, disconnected CRT bases, or
CRT-glued local maps.

## Non-implications and required disposition

No combination of these sections proves a general modular-symbol,
modular-form, finite-etale, or elliptic-torsion obstruction. The stated live
interfaces remain live: boundary-zero cuspidal data, compressed dense
presentations, informative boundary coefficients, genuinely different
forms, new coefficient evaluators, local Frobenius, reduction-only
endomorphisms, and fine CRT orientations.

Do not promote the frozen V2 files. Correct the two occurrences of
`+operatorname{Nm}` to `+\operatorname{Nm}`, freeze new hashes, and submit
that corrected freeze to the next required review. No mathematical rewrite
is otherwise required by this re-audit.
