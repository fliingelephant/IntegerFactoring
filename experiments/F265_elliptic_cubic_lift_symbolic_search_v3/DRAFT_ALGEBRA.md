# F265-D03 draft algebra: peeled elliptic cubic-row kernel

## Status

This is an unfrozen theory draft. It has not received a hostile audit. There
is no source, compilation, preflight, or launch authorization.

The public elliptic row law and all factor-first affine screens are unchanged
from F265-D02. The redesign changes only the bank grammar and the order of the
factor-free square-class work. It removes bank-wide chord-pattern mining.

## 1. Public mixed bank

Let `N >= 3` be odd. Construct two public short-Weierstrass curves as in
F265-D02.

1. The first curve uses the frozen `U` source.
2. The second curve uses the frozen `POWER` source.

Use disjoint deterministic seed domains. Reject and regenerate the second
curve if its complete public seed tuple equals the first. For

\[
 n=\lceil\log_2(N+1)\rceil,
 \qquad K=\min(2n,160),
\]

retain every scalar index `1,...,K` from both complete affine orbits. The row
order is `U` first, `POWER` second, and increasing scalar index within each
curve. Thus the bank has at most 320 rows.

For a clean affine point `(u_i,v_i)` on a curve with public coefficients
`A_i,B_i`, retain

\[
 a_i=u_i^3+A_i u_i+B_i>0,
 \qquad a_i\equiv v_i^2\pmod N.
\]

The D02 factor-first curve, denominator, row-root, singleton, pair-coordinate,
signed-coordinate, chord, equal-row, and exact square-relation screens remain
complete. A partial orbit never reaches the decoder.

The fixed mixed bank replaces the twelve D02 candidates. `ODD`, `PRIME`, and
`LOWHAM` were subsets of `ALL`. `XS`, `YS`, `AS`, and `CENTER` were sampling
biases, not different algebraic row laws. D03 asks one smaller finite question
instead of ranking these biases.

## 2. Saturated private-primary theorem

Let `S` be a nonempty active row set. For `i in S`, put

\[
 P_i=\prod_{j\in S\setminus\{i\}}a_j,
 \qquad L_i=\operatorname{bitlen}(a_i),
\]

with the empty product equal to one, and define

\[
 g_i=\gcd(a_i,P_i^{L_i}),
 \qquad b_i=a_i/g_i.
\]

The power is evaluated modulo `a_i`. It is not materialized.

Fix a rational prime `ell`, and write

\[
 e_i=v_\ell(a_i),
 \qquad E_i=\sum_{j\in S\setminus\{i\}}v_\ell(a_j).
\]

Then

\[
 v_\ell(g_i)=\min(e_i,L_iE_i).
\]

If `E_i=0`, this valuation is zero. Hence `b_i` contains the full primary
part `ell^{e_i}`. If `E_i>0`, then

\[
 e_i\le\lfloor\log_2 a_i\rfloor<L_i\le L_iE_i,
\]

so `v_ell(g_i)=e_i` and `b_i` contains none of that primary part. Therefore

\[
 \boxed{b_i=\prod_{\ell:\,\ell\nmid P_i}\ell^{v_\ell(a_i)}.}
\]

This is exact. In particular, plain `a_i/gcd(a_i,P_i)` is not a valid
replacement: it can leave a shared primary excess when
`v_ell(a_i)>v_ell(P_i)`.

If `b_i` is not an integer square, it contains a prime absent from every
other active row with odd exponent in `a_i`. In every binary vector `c` for
which

\[
 \prod_{j\in S}a_j^{c_j}
\]

is an integer square, the parity equation at this private prime forces
`c_i=0`. Thus a nonsquare `b_i` is a certified private parity pivot. The
certificate uses only products, modular powering, gcd, exact division, and an
integer square test. It does not factor any integer.

## 3. Canonical fixed-point peel

Start with the full row set `S_0`. At round `t`, compute every `b_i` against
the same active set `S_t`. Let

\[
 D_t=\{i\in S_t:b_i\text{ is not an integer square}\}.
\]

Delete all of `D_t` simultaneously, in row order, and put
`S_{t+1}=S_t\setminus D_t`. Stop at the first empty deletion set. This batch
rule makes the fixed point independent of thread scheduling and of an
arbitrary one-row deletion order.

Let

\[
 \mathcal K(S)=\left\{c\in\mathbf F_2^S:
       \prod_{i\in S}a_i^{c_i}\text{ is an integer square}\right\}.
\]

For every `i in D_t`, the private-pivot theorem gives `c_i=0` for all
`c in K(S_t)`. Restriction therefore defines a linear bijection

\[
 \boxed{\mathcal K(S_t)\simeq\mathcal K(S_{t+1}).}
\]

Its inverse inserts zeros on `D_t`. Induction gives

\[
 \boxed{\mathcal K(S_0)\simeq\mathcal K(S_*)}
\]

at the fixed point. The peel cannot remove a square dependency or change its
normalized root. A row can acquire a private primary part after another row
is deleted, which is why the fixed-point iteration is required.

Run the complete P66 gcd-free parity decoder on `S_*`. Embed every returned
vector into the original bank by inserting zeros. If `S_*` is empty, the
theorem itself proves that the original kernel is zero.

## 4. Complete support-zero, support-one, and support-two layer

The zero vector is ignored. A support-one vector `e_i` is in the kernel
exactly when `a_i` is an integer square. Its positive root and supplied root
`v_i` are compared by both signed gcds before residual classification.

For distinct rows set `d=gcd(a_i,a_j)`. Then

\[
 \boxed{a_i a_j\text{ is a square}
 \iff a_i/d\text{ and }a_j/d\text{ are squares}.}
\]

Indeed, at each prime the two quotient valuations are
`max(alpha-beta,0)` and `max(beta-alpha,0)`. They are both even exactly when
`alpha+beta` is even. If

\[
 a_i/d=x^2,\qquad a_j/d=y^2,
\]

then the exact positive product root is `d*x*y`. This is a complete
factor-free support-two test. It strictly contains equal-row and integer
square-multiple templates.

Enumerate every support-one and support-two kernel vector in canonical
bit-vector order. Verify its exact positive root and normalized-root signed
gcds. Let `L_low` be their binary span. Compute a canonical RREF basis of
`L_low`.

Compute a canonical P66 basis of `K(S_*)`: opaque blocks are ordered by
integer value, matrix pivots and columns use row order, and free columns are
visited from left to right. Reduce these basis vectors against `L_low` and
against earlier retained quotient pivots. The nonzero reduced vectors form a
canonical complement `Q` with

\[
 \mathcal K(S_*)=L_{\rm low}\oplus\operatorname{span}(Q).
\]

Every vector in `L_low` is checked first. If all of them have global
normalized root, multiplication by `L_low` changes any other normalized root
only by a global sign. Hence non-globality is well defined on the quotient.
Testing every vector of `Q` is complete: a non-global relation exists outside
the low-support span if and only if at least one complement basis vector is
non-global.

## 5. Relation-local elliptic diagnostics

Chord labels do not construct a P66 parity equation and do not determine
normalized-root usefulness. D03 therefore computes them only after a
relation has been verified.

For a verified relation support `C` and a same-curve pair `i,j in C`, cache
the exact public values

\[
 H_{ij}=u_i^2+u_i u_j+u_j^2+A,
\]

\[
 d_{ij,\mathrm{tan}}=\gcd(a_i,a_j,u_i-u_j),
\]

\[
 d_{ij,\mathrm{chord}}=\gcd(a_i,a_j,H_{ij}),
 \qquad
 d_{ij,\mathrm{disc}}=\gcd(a_i,a_j,4A^3+27B^2).
\]

For `d_chord>1`, a third row `k in C` is a chord-root match exactly when

\[
 u_i+u_j+u_k\equiv0\pmod {d_{ij,\mathrm{chord}}}.
\]

The frozen index predicates can then be evaluated on this same support.
There is no scan over an opaque block's bank-wide incidence list.

Diagnostics are emitted only for the first eight canonical complement
vectors whose support is at most 16. They are exhaustive within each emitted
support. The maximum is

\[
 8\binom{16}{2}=960\text{ pair records},
 \qquad
 8\binom{16}{3}=4480\text{ unordered triple records per bank}.
\]

The support limit and emission limit affect only explanatory output. They do
not affect bank eligibility, kernel construction, root verification, result
classification, or family selection; D03 has no family selection. A large
relation remains fully verified and counted even when it has no diagnostic
record.

Thus a kernel-zero bank performs zero chord-pattern work after P66. This is
an output-sensitive replacement for D02's bank-wide
`sum_b binom(deg(b),2) deg(b)` scan.

## 6. Complexity and relation to P217

Let an active round contain `r` rows, each with at most `R` bits. Its exact
active product has at most `rR` bits. A product tree uses `r-1` integer
multiplications. For each row, exact division gives `P_i`; binary modular
powering uses at most
`2*floor(log2(L_i))+1` modular multiplications, followed by one gcd, one exact
division, and one square test. No `P_i^{L_i}` is materialized.

There are at most `m` nonterminal peel rounds. Hence

\[
 \sum_t |S_t|\le m(m+1)/2.
\]

At the D03 caps `m<=320` and `R<=361`, this is at most 51,360 row-round
tests and every active product has at most 115,520 bits. The algorithm is
polynomial in the explicit bank length. The preregistration can impose a
small residual-core cap before the complete P66 phase; a cap crossing is a
visible resource rejection, never an eligible null.

P217 is different. It uses the polynomial form of Pell rows to prove a zero
generic kernel and to localize specialization-only sharing on explicit
pairwise resultants. The theorem above is source-agnostic and purely
numerical. It has no polynomial parameter, no resultant localization, and no
normalized-root law. Its new value for F265 is iterative: after certified
coordinates are deleted, shared numerical primes can become private and
force more coordinates. It preserves the complete numerical kernel but does
not prove that the fixed-point core is small.

The other closest boundaries remain intact. P20 pools elliptic coordinate
collisions through a scalar near `sqrt(N)`; D03 materializes at most 320 cubic
rows and never forms that product. P66 is still the complete decoder on the
surviving explicit list; the peel only proves that deleted coordinates are
zero in its kernel. P211 and P213 concern randomized or rigid principal lifts
and canonical powers modulo `N^2`; D03 uses ordinary integer representatives
of modular cubic values and makes no high-digit distribution claim. F257's
signed resultant split is specific to same-discriminant Pell rows and does not
assign a normalized-root sign here.

## 7. Exact scope

The peel proves a cost and preservation theorem. It does not prove that any
F265-D03 bank has a private pivot, that a residual core is small, or that a
useful relation exists. The nine-case D02 preflight is heuristic evidence
only. A fresh hostile theory audit is required before source is written or a
preflight is run.
