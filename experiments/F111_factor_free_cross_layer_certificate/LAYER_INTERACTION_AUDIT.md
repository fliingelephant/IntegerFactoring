# F111 Layer-Interaction Hostile Analysis

## Verdict

For the exact F111 source, stop, and exact-value deduplication:

| System | Columns | Rank | Nullity | Non-global root? |
| --- | ---: | ---: | ---: | --- |
| A. Frozen pre-append layer | 11,885 | 11,878 | 7 | **No** |
| B. Appended-only retained records | 837 | 837 | 0 | **No** |
| C. Globally deduplicated union | 12,569 | 12,551 | 18 | **Yes** |

Every useful union dependency necessarily crosses the frozen/appended boundary.
This is proved from the full kernels and the induced root map. It is not inferred
from the published 363-index support.

## Exact layer definition and deduplication

The frozen side contains all 14,351 retained records before appended generation.
This includes the 31 initial seeds and the complete frozen trajectory layer. The
appended side contains the 1,032 newly retained records through the exact public
stop at record count 15,383.

Canonical exact-value deduplication removes (P=1) and keeps the first source
occurrence of each exact integer (P=cw):

| Layer | Raw | Units | Repeated exact values | Unique nonunit values |
| --- | ---: | ---: | ---: | ---: |
| Frozen | 14,351 | 1 | 2,465 | 11,885 |
| Appended alone | 1,032 | 0 | 195 | 837 |
| Union | 15,383 | 1 | 2,813 | 12,569 |

The standalone layer value sets overlap in 153 exact values. Global first
occurrence assigns these values to the frozen side. Thus the union has 684 new
appended coordinates. Those 684 columns also have full rank.

For the alternative meaning “frozen trajectories without initial seeds,” the
result is unchanged: 11,881 columns, rank 11,874, nullity 7, and every kernel
root is (+1).

## Complete factor-free kernel computation

The named verifier regenerates the public source from only (N), (n), the
bound, and the stop count in `CERTIFICATE.json`. It does not read the 363
selected indices. It does not read or use known factors. It does not call an
integer-factorization or primality routine.

The verifier builds a parity-equivalent coprime refinement with gcd operations
on the exact endpoints. It removes square fragments and duplicate parity rows,
then performs GF(2) elimination. The refinement produced:

- 25,138 endpoint entries;
- 16,666 nonsquare coprime fragments;
- 13,864 distinct parity rows;
- 85,284 gcd refinements;
- 1,714,618,656 gcd tests.

Every returned kernel-basis vector was checked by multiplying its exact
relation values, taking the positive integer square root, and checking the root
modulo (N). `LAYER_INTERACTION_OUTPUT.json` stores every complete basis vector
as a hexadecimal mask, together with its support digest, exact-product digest,
positive-root digest, provenance counts, and root residue.

The complete root-map results are:

- Frozen kernel: dimension 7. All seven basis roots are (+1). Its full root
  image and its image modulo global sign are both trivial.
- Appended-only kernel: dimension 0. No nonempty dependency exists.
- Union kernel: dimension 18. Seventeen basis roots are (+1). One is the
  non-global residue (1{,}058{,}780{,}986). The normalized root-map image has
  rank one.

The non-global basis representative recovered independently has support 363,
with 327 frozen and 36 appended records, and has the same exact-product and
root digests as F111. This is a consistency result. The layer theorem uses all
18 kernel directions, not that representative alone.

## Projection and kernel criterion

Let (V_F) and (V_A) be the frozen and new-appended coordinate spaces after
global exact-value deduplication. Let

\[
M_F:V_F\to W,
\qquad
M_A:V_A\to W
\]

be the parity maps. Define

\[
K_F=\ker M_F,
\quad
K_A=\ker M_A,
\quad
K_U=\ker [M_F\;M_A].
\]

For ((x_F,x_A)\in K_U), the common parity projection is

\[
M_Fx_F=M_Ax_A.
\]

Its kernel is (K_F\oplus K_A). Therefore

\[
K_U/(K_F\oplus K_A)
\cong
\operatorname{im}M_F\cap\operatorname{im}M_A.
\]

The computed dimensions are

\[
\dim K_F=7,
\qquad
\dim K_A=0,
\qquad
\dim K_U=18,
\]

and hence

\[
\dim K_U/(K_F\oplus K_A)=11.
\]

Independently,

\[
\operatorname{rank}M_F+
\operatorname{rank}M_A-
\operatorname{rank}[M_F\;M_A]
=11{,}878+684-12{,}551
=11.
\]

Thus the parity-image intersection and cross-layer quotient dimensions agree
exactly.

For a dependency (x), define

\[
\rho(x)=\sqrt{\prod_i P_i^{x_i}}\pmod N.
\]

This is multiplicative on the kernel. For two dependencies, removing their
common columns divides the two exact products by a square; every removed
(P_i\) is congruent to one modulo (N). Quotienting the root image by the
global subgroup ({\pm1}) therefore gives a linear normalized-root map

\[
\bar\rho:K_U\to R/\{\pm1\}.
\]

Both pure-layer restrictions have rank zero. Hence (ar\rho) descends to the
11-dimensional cross-layer quotient. Its induced rank is one. A dependency is
useful exactly when its image is nonzero. Such a dependency cannot lie in
(K_F\oplus K_A), so it must have nonzero coordinates in both layers.

There are (2^{18}) union dependencies. The normalized root map has rank one,
so exactly (2^{17}=131{,}072) are useful. The quotient has (2^{11}) classes;
exactly (2^{10}=1{,}024) useful quotient classes each have (2^7) pure frozen
lifts. Every one crosses layers.

## Exact theorem boundary

This audit proves the following finite statement:

> For (N=3{,}241{,}632{,}473), the declared generation order, the exact stop
> at 15,383 retained records, and first-occurrence exact-value deduplication,
> neither pure layer contains a non-global square root. The union does. Every
> useful union dependency crosses the frozen/appended boundary.

This does not prove:

- how to select a useful dependency without computing the complete kernel;
- that the published 363 indices are available without advice;
- that another stop, source order, or provenance convention has the same
  coordinate-level statement;
- that another modulus has the same parity-image intersection or root map;
- an all-input, density, probability, or bit-runtime theorem.

The 153 cross-layer exact-value overlaps matter to provenance. The theorem uses
the canonical global first-occurrence convention. The standalone appended
system was also tested with all 837 of its unique values and is full rank.

## Reproducibility and preserved failure

Run:

```text
/opt/homebrew/bin/python3 experiments/F111_factor_free_cross_layer_certificate/LAYER_INTERACTION_run_with_timeout.py
```

The successful factor-free run completed within the 300-second hard timeout.
One earlier auditor-only failure is preserved as
`LAYER_INTERACTION_FAILED_20260808T034345655510Z_EXIT_1.*`. Its self-source
check searched for a forbidden certificate-key string and matched that string
inside the check itself. The replacement inspects actual AST subscript access.
The failed attempt did not find a candidate defect.
