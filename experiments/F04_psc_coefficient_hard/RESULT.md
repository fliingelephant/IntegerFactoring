# F04 coefficient-hard canonical-PSC kill result

**Approach-family ID:** `F04_psc_coefficient_hard`.

**Result:** exact finite counterexample.  On the P11 witness, every canonical
principal Sylvester determinant in the complete standard AKS shift range is a
unit modulo `N`.  Thus canonical PSCs do not recover a factor even though every
standard AKS identity fails locally.

## Fixed objects

Use the determinant convention fixed in `experiments/F04_psckill/RESULT.md`:

\[
P=X^r-1,\qquad Q_a=H_a=(X+a)^N-X^N-a\pmod P,
\]

and, for `m=deg(P)`, `n=deg(Q_a)`, let `D_j(P,Q_a)` be the determinant of
the coefficient map

\[
(U,V)\longmapsto UP+VQ_a,
\quad \deg U<n-j,\quad\deg V<m-j,
\]

projected to degrees `j,...,m+n-j-1`, with increasing output degrees and
the increasing shifts of `P` followed by the increasing shifts of `Q_a`.

The parameters from P11 are

\[
N=20000000499999937=100000007\cdot199999991=pq,
\quad r=2953,
\]

and the complete standard shift range is `1 <= a <= 2942`.  The source forms
each `Q_a` first over `(Z/NZ)[X]/(X^r-1)` and only then reduces that same
coefficient vector modulo `p` and modulo `q`.  It does not compare PSCs of two
independently substituted local polynomials.

## Degree-sequence theorem

**Lemma.**  Let `K` be a field, let `F,G in K[X]` have degrees `m>n`, and
define `D_j(F,G)` by the fixed determinant above.  Run the ordinary Euclidean
algorithm

\[
R_0=F,\quad R_1=G,\quad
R_{i+1}=R_{i-1}\bmod R_i
\]

until the next remainder is zero, and write

\[
m=d_0>d_1=n>d_2>\cdots>d_s=g,
\quad d_i=\deg R_i.
\]

Then, for every `0 <= j <= n`,

\[
D_j(F,G)\ne0
\quad\Longleftrightarrow\quad
j\in\{d_1,d_2,\ldots,d_s\}.
\]

In particular, if `g>0`, every `D_j` with `j<g` is zero.  The top index is
always present:

\[
D_n(F,G)=\operatorname{lc}(G)^{m-n}\ne0.
\]

**Proof.**  The fixed matrix is the determinant-form principal
subresultant matrix, so `D_j` is the coefficient of `X^j` in the `j`th
subresultant polynomial (the fixed row and column order removes the usual
sign ambiguity, which is irrelevant to vanishing).

Consider one Euclidean step `F=AG+R` with `d=deg(R)<n`.  Apply the same
elimination `F-AG=R` to the shifted `F` columns in the defining Sylvester
blocks.  Fraction-free block elimination gives the fundamental
subresultant step:

- `D_j(F,G)=0` for `d<j<n`;
- for `0<=j<=d`, `D_j(F,G)=u_j D_j(G,R)` for a product `u_j` of signs and
  nonzero powers of leading coefficients, hence `u_j` is a unit in `K`;
- at `j=n`, the defining matrix is triangular with diagonal
  `lc(G)`, giving `D_n=lc(G)^(m-n)`.

These statements can also be read directly from the same block elimination:
the gap block has a zero diagonal block when `d<j<n`, whereas below `d` the
only discarded pivots are nonzero leading coefficients.  Therefore one step
adds exactly the degree `n` to the set of nonzero principal coefficients and
then passes the question to `(G,R)`.  If `R=0`, `G` divides `F`; for every
`j<n`, choosing nonzero `U` and `V=-UA` gives a kernel vector within the
degree bounds, so those determinants vanish, while `D_n` remains nonzero.
Induction down the Euclidean chain proves that the nonzero indices are
exactly `d_1,...,d_s`.  This includes the gcd-positive and top-index cases.
\(\square\)

`validate_prs_convention.sage` also checks the fixed matrices directly on
small exact examples containing an internal degree gap and a positive-degree
gcd.  It verifies both the determinant/Sage-subresultant indexing and the
degree-sequence criterion; this is a convention check, not a substitute for
the proof.

## Exhaustive computation

For every one of the 2942 standard shifts, the globally formed `Q_a` has
degree 2952 and all 2953 of its coefficients are nonzero modulo both `p` and
`q`.  Thus every raw coefficient is a unit modulo `N`, independently
reconfirming the P11 coefficient-hard property on the scanned rows.

In both prime fields and for every shift, the ordinary Euclidean remainder
degree sequence is exactly

\[
2953,2952,2951,\ldots,1,0.
\]

The lemma therefore gives

\[
D_j(P,Q_a)\not\equiv0\pmod p,
\qquad
D_j(P,Q_a)\not\equiv0\pmod q
\]

for every `1<=a<=2942` and every `0<=j<=2952`.  Hence each globally defined
`D_j mod N` is a unit and

\[
\gcd(D_j,N)=1.
\]

The exhausted range contains

\[
2942\cdot2953=8,687,726
\]

canonical determinants per field, or 17,375,452 exact local statuses.  There
is no zero/nonzero mismatch anywhere in the complete standard scan.

The decisive R08 command was

```text
DOT_SAGE=/tmp/f04_psc_coefficient_hard_sage timeout 900 sage experiments/F04_psc_coefficient_hard/scan_degree_patterns.sage --shift-start 1 --shift-stop 2942 --rows experiments/F04_psc_coefficient_hard/output/R08_full_degree_rows.jsonl --output experiments/F04_psc_coefficient_hard/output/R08_full_degree_scan.json > experiments/F04_psc_coefficient_hard/logs/R08_full_degree_scan.log 2>&1
```

It exited 0 after an internally measured `305.53568024999913` seconds.  The
source SHA-256 is
`be12f869a9002d5c37b8217cf545f8785d72a117c1830502af189ef6d06be904`.
The summary and row-stream SHA-256 hashes are respectively
`aba2385f2bbdf0056346dc06b177720689304dc63d9f27e6cb88c05df3db7cc2`
and
`93f611868864f43d914e0a53778a89950e8ae5610294a95b576e61b641728e40`.

R05 and R09 independently materialized all 2953 exact subresultant residues
in each field at shifts 1 and 2942.  Their zero sets are empty and their
global coefficient-vector hashes agree with the corresponding R08 rows.
R10 audited all 2942 checkpoint rows, both endpoints, all source/artifact
hashes, and the exact count; `audit_passed=true`.

## Factor-free meaning and scope

Each `D_j` is a polynomial with integer coefficients in the globally
available coefficients of `P,Q_a`.  It can therefore be evaluated modulo
`N` without knowing `p,q`; for example, Berkowitz evaluates the determinant
using only ring addition and multiplication, with no divisions.  Reduction
of that one global value gives the two local determinants analyzed above.
Here both reductions are always nonzero, so the factor-free gcd step always
returns 1.

This is a finite counterexample only to the universal claim that the fixed
canonical PSC family must localize compositeness somewhere in the **standard
minimal-`r`, standard-shift scan**.  It does not rule out nonstandard shifts,
other moduli, other minors or polynomial relationships, or a different
factor-free construction, and it does not address a top-level factoring
theorem.
