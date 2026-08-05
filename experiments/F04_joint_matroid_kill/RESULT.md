# F04 joint row-matroid kill result

**Approach-family ID:** `F04_joint_matroid_kill`.

**Result:** explicit finite counterexample for the coefficient-hard P11 input.
Stacking all standard AKS errors does not force the local row matroids, the
canonical row/column prefix ranks, or the lexicographic column basis to differ.
On this input both local row matroids are the same free matroid, and the
canonical maximal prefix determinant is a unit modulo `N`.

## Rigorously fixed joint scan

For standard shifts `a=1,...,A`, form

\[
H_a=(X+a)^N-X^N-a\pmod {X^r-1}
\]

first over `(Z/NZ)[X]/(X^r-1)`.  Let `M_N` be the `A`-by-`r` matrix whose
row `a` is the coefficient vector of that globally formed `H_a`, in column
order `0,...,r-1`.  Let `M_p,M_q` be coefficientwise reductions of this same
matrix.

The fixed scan consists of:

1. the row matroid on the standard shifts, with rank function
   `S -> rank(M_l[S,:])`;
2. the row-prefix ranks `rank(M_l[0:s,:])`;
3. the full-row column-prefix ranks `rank(M_l[:,0:t])`;
4. the lexicographically first column basis; and
5. the canonical maximal prefix minor

\[
\Delta_\ell=\det M_\ell[:,0:A].
\]

The displayed profiles have only `O(A+r)` entries.  The determinant is one
globally specified polynomial in entries of `M_N`; it can be evaluated over
`Z/NZ` without division or factor knowledge, for example by Berkowitz.

## A one-minor certificate determines all listed profiles

**Lemma.**  Let `M` be an `A`-by-`r` matrix over a field with `A<=r`.  If

\[
\det M[:,0:A]\ne0,
\]

then:

- all `A` rows are independent, so the row matroid is the free matroid and
  every row subset `S` has rank `|S|`;
- every row-prefix rank equals its number of rows;
- the first `A` columns are independent, so the column-prefix rank is
  `min(t,A)` for every `t`;
- the lexicographically first column basis is exactly `0,...,A-1`.

**Proof.**  The nonzero determinant makes the square prefix invertible.  Its
rows and columns are therefore independent.  Adding the remaining columns
cannot create a dependence among rows, every subset of an independent row
set is independent, and every subset of the first `A` independent columns
is independent.  The four conclusions follow immediately.  \(\square\)

Thus two nonzero local residues of the same global `Delta` certify equality
of the entire row matroids and every listed polynomial-size profile; no
exponential subset scan is needed.

## P14 survives the joint test

For context, the promoted P14 input

\[
N=79403=271\cdot293,\qquad r=269,\qquad A=266
\]

is a genuine joint separator.  The same globally formed `266`-by-`269`
matrix has

\[
\operatorname{rank}_{271}M=23,
\qquad
\operatorname{rank}_{293}M=266.
\]

The rank 23 has a direct explanation.  Lucas' theorem for `293=271+22`
shows that, after reducing nonzero shifts modulo 271, every coefficient
function lies in the span of

\[
a,a^2,\ldots,a^{23}.
\]

The 23 columns corresponding before the substitution to residues
`0,...,22` have a triangular coefficient pattern spanning all 23 monomials.
Their evaluations at the distinct shifts have rank 23.  Modulo 293, choose
the 266 unsubstituted coefficients with exponents `t=2,...,267` in
`h_(271,a)`.  Up to nonzero binomial column scalars and nonzero row scalars,
their evaluation matrix is the Vandermonde matrix on the 266 distinct shifts
with exponents `0,...,265`; substitution by `X^293` only permutes columns.
Hence the other rank is 266.

The canonical `266`-by-`266` prefix determinant has exact residues

\[
\Delta\equiv0\pmod {271},\qquad
\Delta\equiv30\pmod {293}.
\]

Its global residue is `71815 mod 79403`, and

\[
\gcd(71815,79403)=271.
\]

So joint rank can help on P14; this is not the kill witness.

## P11 is the counterexample

Use the promoted coefficient-hard input

\[
N=20000000499999937
=100000007\cdot199999991,
\qquad r=2953,
\qquad A=2942.
\]

All 2942 global rows were formed independently in both retained runs.  The
per-row hashes and aggregate hash agree exactly; the common global-matrix
SHA-256 is

```text
85c4bcda5ff5d0f23117721a503fedb77e3a84b9d708a3ceb0f7bed1673c6f53
```

The exact canonical maximal prefix residues are

\[
\Delta\equiv56136614\pmod {100000007},
\qquad
\Delta\equiv132391112\pmod {199999991}.
\]

Both are nonzero.  The lemma therefore proves, simultaneously in both local
fields:

- `rank(M)=2942`;
- every subset of standard-shift rows is independent, so both complete row
  matroids are the same free matroid on 2942 elements;
- every row-prefix rank is `s`;
- every column-prefix rank is `min(t,2942)`;
- the lexicographic column basis is `0,...,2941`.

CRT gives the globally defined prefix determinant

\[
\Delta\equiv16315256998204520\pmod N,
\]

and

\[
\gcd(16315256998204520,N)=1.
\]

Every one of the `2942*2953=8,687,726` raw global matrix entries is also a
unit modulo `N`.  Thus neither an entry scan nor the fixed joint row-matroid,
prefix-rank, lexicographic-basis, or maximal-prefix-minor scan exposes a
factor.

## Exact computations

R04 used a 1200-second hard timeout and exited 0.  It formed the global matrix
and reduced it modulo 100000007 in `145.4363500829968` seconds, then computed
the exact dense finite-field determinant in `10.390780665999046` seconds;
total internal time was `156.07906762499988` seconds.  The determinant was
`56136614`.

R05 used the same 1200-second hard timeout and exited 0.  It independently
formed the global matrix and reduced it modulo 199999991 in
`148.6143141249995` seconds, then computed the determinant in
`10.269350874998054` seconds; total internal time was
`159.1375450409978` seconds.  The determinant was `132391112`.

Both used `scan_maximal_prefix.sage`, SHA-256
`4c499aa8a7c10f5b7ac5e6520dcbb966e568591543c0b580cbad37eac1e36c24`.
R06 verified the identical global row hashes and performed CRT.  R07 checked
all retained parameters, ranks, determinants, pivots, hashes, and counts;
`audit_passed=true`.

## Scope

This counterexample refutes universal separation by the **row matroid** of
the standard AKS error family and by the rigorously fixed one-axis prefix and
lexicographic maximal-prefix scan above.  It does not prove that the complete
column matroids agree, and it does not exhaust arbitrary coordinate minors,
the two-dimensional table `rank(M[0:s,0:t])`, adaptive polynomial-size minor
families, nonstandard shifts or moduli, or nonlinear joint invariants.  Any
broader proposal must specify its globally computable minor family and still
needs a uniform theorem forcing a local zero-pattern difference.
