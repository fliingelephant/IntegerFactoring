# Hostile audit of C13: the finite determinant separator survives

**Approach-family ID:** `F04_psc_audit`.

**Status:** focused hostile audit passed for the finite theorem below.  C13 is
still not verifier-backed: the required proof-blind end-to-end reconstruction
has not yet run.  This audit does not promote or edit any canonical claim.

## Verdict and necessary wording corrections

No numerical or mathematical part of the decisive certificate was refuted.
The retained presentation does need two code-level qualifications:

1. The retained local sources recompute the image of the same expression for
   `H_1` in each field; they do not literally read and reduce one stored global
   coefficient vector.  This is mathematically valid because quotient-ring
   evaluation commutes with the coefficient homomorphisms.  A04 enforces the
   stronger literal data flow and then independently reconstructs each local
   polynomial as a cross-check.
2. Retained R05 is factor-free after being handed `j=47`, but by itself it
   does not show factor-free discovery of that index.  A02 takes only
   `N=79403`, `r=269`, and `a=1`, scans `j` increasingly, obtains gcd 1 at
   every `j=0,...,46`, and first obtains a nontrivial gcd at `j=47`.  Its
   source contains neither prime divisor and calls no factoring routine.

Accordingly, “lexicographically smallest” means precisely: first among pairs

\[
(a,j),\qquad a\in\{1,\ldots,266\},\quad
0\le j\le \deg H_a,
\]

ordered first by the standard positive shift and then by increasing `j`, for
this fixed `N`, `r`, and determinant convention.  It is not a minimality claim
over inputs, arbitrary shifts, arbitrary minors, or other PSC conventions.

## Narrowest audited theorem

Let

\[
N=79{,}403,\qquad r=269,\qquad
P=X^{269}-1,
\]

and form, without using a factor of `N`,

\[
H_1=(X+1)^N-X^N-1
\quad\text{in}\quad
(\mathbb Z/N\mathbb Z)[X]/(X^{269}-1).
\]

Read `n=deg(H_1)` from its global coefficient vector.  For `0<=j<=n`,
let `D_j` be the determinant whose columns are, in order,

\[
P,XP,\ldots,X^{n-j-1}P,
H_1,XH_1,\ldots,X^{269-j-1}H_1,
\]

after restricting coefficient rows, in increasing order, to degrees
`j,...,269+n-j-1`.  Then `n=268`,

\[
\gcd(D_j,N)=1\quad(0\le j\le46),
\]

while

\[
D_{47}\equiv30352\pmod{79403},\qquad
\gcd(30352,79403)=271.
\]

The reductions of the same saved global coefficient vector have degrees 46
and 268 and give

\[
D_{47}\equiv0\pmod{271},\qquad
D_{47}\equiv173\pmod{293}.
\]

The defining matrix has dimension

\[
269+268-2\cdot47=443.
\]

For the canonical lifts used in the retained computation, its exact integer
determinant has 3907 bits.  A02 independently recovered the same bit length
and additionally records SHA-256
`47b73ba0ca30e1704fb93e22ef3838b752b8ff6aec07010f4f23812f6dcf4869`
for the signed decimal determinant.

Finally,

\[
[X^{268}]H_1=31978\pmod{79403},\qquad
31978\equiv(0,41)\pmod{(271,293)},
\]

so its gcd with `N` is already 271.  This witness therefore shows no PSC
advantage over scanning individual coefficients.

## Convention, reduction, and degree-drop checks

The domain dimensions in the definition are `n-j` and `m-j`, and the retained
row interval has

\[
(m+n-j-1)-j+1=m+n-2j
\]

entries.  Thus the matrix is square of the claimed dimension.  A02 and A04
construct exactly this row/column order by independent code paths.

Every entry is an integer polynomial coefficient reduced modulo the base
ring, and determinant is a polynomial with integer coefficients in those
entries.  Therefore coefficient reduction and determinant formation commute.
A04 checks this literally at `j=47`: the canonical integer-lift matrix reduced
entrywise modulo each factor equals the matrix built from the saved global
`H_1` reduction.

There is also an exact formal-degree specialization lemma.  Let a monic `P`
have degree `m`, let the formal degree of `Q` be `n`, and suppose a reduction
of `Q` has actual degree `d<=n`.  If `D_j^(n)` denotes the displayed padded
matrix and `D_j^(d)` the corresponding actual-degree matrix, then for
`j<=d`,

\[
D_j^{(n)}=(-1)^{(n-d)(m-j)}D_j^{(d)}.
\]

Indeed, split the `P` columns after shift `d-j` and split off the last `n-d`
rows.  Moving the extra `P` columns past the `m-j` `Q` columns leaves a block
triangular matrix whose new lower-right block is triangular with diagonal
`lc(P)=1`; the displayed column-swap sign is the only factor.  For `j>d`, the
unshifted `Q` column is zero because every retained row degree is at least
`j>d`, so `D_j^(n)=0`.

Here `n-d=222` modulo 271, so the padding sign is always +1; modulo 293 there
is no degree drop.  A04 directly checked the formula at every applicable
index and checked the structural zero column at every `j>d`, with no failure.
In particular the degree-46 reduction forces `D_47=0` under exactly the fixed
convention.

## PSC/PRS correspondence

The theorem above is about the explicitly defined determinants and therefore
does not depend on a library PRS convention.  Nonetheless, the retained
discovery scan used Sage's subresultant sequence to predict zero positions.
A04 formed all 269 determinant pairs directly and found:

- no PRS-versus-direct zero disagreement in either characteristic;
- direct/PRS coefficient ratio 1 whenever the compared coefficient was
  nonzero;
- no formal-degree padding disagreement;
- zeros modulo 271 exactly at `j=47,...,268`;
- the sole zero modulo 293 at `j=157`.

Thus the direct mismatch set is `47,...,156,158,...,268`, exactly the retained
R03 discovery mask.  At `j=157` both determinants vanish, so the global gcd is
`N`, not a separator.  The decisive prefix through 47 is independent of any
PRS shortcut, and A06 matches all 48 retained direct-prefix residue pairs
exactly.  A04 checked all indices only to audit the complete PRS mask; the
lexicographic first-mismatch claim needs, and uses, only the direct checks at
`j=0,...,47` for the first standard shift `a=1` under the fixed convention and
increasing-index order.

## Retained-artifact provenance check

The retained failure dispositions match the files on disk.  R01 stops on the
previously unhandled local degree 46; R02 prints the 221-mismatch discovery
before leaving a truncated JSON file at serialization; R03 is the corrected
discovery output; R04 and R05 agree on the global determinant fields, with R05
adding the leading-coefficient diagnostic; and R06 is the retained direct
prefix calculation.  A06 compares R03, R05, and R06 against the independent
artifacts: every retained global field matches, all 48 direct prefix rows
match exactly, and the complete 269-index discovery zero masks and mismatch
indices match the independent direct determinants.

## Factor use and uniform bit complexity

Known factors occur only in A04's local certificate and in the retained local
discovery/certificate sources.  A02's factor-free source:

- receives only `N`, `r`, and `a`;
- constructs `H_a` by dense cyclic binary powering;
- derives the global degree from that vector;
- computes exact determinants for increasing `j` and takes ordinary integer
  gcds;
- contains neither `271` nor `293` and invokes no factorization, order-finding,
  local-field, or PRS routine.

Its global `H_1` hash equals the retained hash
`5dc346453110135fd6f2ccf69227cc95caecc6480be58b2a3d0d37e13dec704c`.
The known factors were therefore not used to form the decisive global
coefficient or to select `j` in the independent scan.

For the uniform computation claim, put
`L=ceil(log2(N+1))`.  Cyclic binary powering uses `O(L)` products of vectors
of length `r`; schoolbook multiplication costs `O(r^2)` operations in
`Z/NZ`, with every scalar reduced back to `O(L)` bits.  There are at most `r`
determinants per shift and each dimension is at most `2r`.  The
Samuelson-Berkowitz construction computes a determinant over any commutative
ring using no division and `O(r^4)` ring operations per matrix under a naive
implementation.  Matrix formation, modular gcds, and loop control are also
polynomial.  Thus `A` shifts cost, conservatively,

\[
O\!\left(A(r^2L+r^5)\operatorname{poly}(L)\right)
\]

bit operations.  Hence the coefficient scan is uniform polynomial time
whenever `r` and `A` are polynomial in `L`, including the standard AKS
parameter bounds.  The exact-integer determinant method used by A02 is only
an independent certificate implementation; the uniform algorithm can use
Berkowitz directly modulo `N` and keep all residues short.

## Exact scope

This audit establishes one finite separator and the uniform computability of
the determinant family.  It does not establish that a separator exists for
every composite input, that random shifts find one with inverse-polynomial
probability, or that the scan yields a factoring algorithm.  It does not
re-audit P14's proof that `r=269` and shifts `1,...,266` are the standard AKS
parameters; the determinant theorem itself only needs the displayed public
parameters.  It says nothing about arbitrary Sylvester minors, adaptive
elimination transcripts, nonstandard moduli, coefficient-hard witnesses such
as P11, or complete integer factoring.

Authoritative runs are A02, A04, and A06 in `RUN_MANIFEST.md`.  A01 and A03
are preserved serialization failures and support no claim beyond their logs.
