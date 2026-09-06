# F265-D05 draft algebra: peeled elliptic cubic-row kernel

## Status and exact predecessor boundary

This is an unfrozen theory draft. It has not received a hostile audit. There
is no D05 source, compilation, preflight, freeze, or launch authorization.

D05 uses the following immutable F265-D02 bytes as its predecessor boundary.
No unqualified phrase such as "the D02 implementation" imports any other
bytes.

| predecessor artifact | SHA-256 |
|---|---|
| `experiments/F265_elliptic_cubic_lift_symbolic_search_v2/FROZEN.sha256` | `26f7940244242edc549a2612fc08120372e0f8fab64a2dca154b69ed02d55d6a` |
| `experiments/F265_elliptic_cubic_lift_symbolic_search_v2/ALGEBRA.md` | `d20b5271bb4441fe7d280e35e09a73ff5b0142abf2ed6d3e9839fe22ff4914c4` |
| `experiments/F265_elliptic_cubic_lift_symbolic_search_v2/PREREGISTRATION.md` | `8e3c90420014939ba3ae58490bac2e85fc0a7a45523e12d332cadb5e1f6b384f` |
| `experiments/F265_elliptic_cubic_lift_symbolic_search_v2/search.cpp` | `eeceba4db014346cc78dae3cbae29a65fb32946163becc5d9f5617fc465a7957` |

The future D05 packet must authenticate these whole files before copying any
routine. Its prelaunch manifest must hash each copied routine after the D05
changes. D05 changes the bank grammar and the order of factor-free
square-class work. It does not alter the public cubic-row identity or infer
prime factors of row values.

## 1. Public mixed bank

Let `N >= 3` be odd. A public short-Weierstrass curve is specified by

\[
 E_N:y^2=x^3+Ax+B\pmod N,
 \qquad 0\le A,B<N.
\]

Before using it, compute `gcd(4A^3+27B^2,N)`. Before every affine inversion,
compute the denominator gcd with `N`. Before admitting an affine row, compute
the row-root gcd with `N`. A proper gcd is a certified direct factor. A full
gcd or an unresolved affine exception makes the bank incomplete. A partial
orbit never reaches the square-class decoder.

For a clean affine point `(u_i,v_i)`, retain the positive integer

\[
 a_i=u_i^3+A u_i+B,
 \qquad a_i\equiv v_i^2\pmod N.
\]

Thus every admitted `v_i` is a unit modulo `N`. If
`n=ceil(log2(N+1))`, each of the two curves contributes every scalar index
from `1` through

\[
 K=\min(2n,160).
\]

The first curve uses the public `U` construction and the second uses the
public `POWER` construction fixed in the preregistration. Their exact random
domains are disjoint. The row order is curve zero, then curve one, and
increasing scalar index within each curve. The bank has at most 320 rows.

Every discriminant, denominator, row-root, singleton, coordinate, signed
coordinate, same-curve chord, and normalized-root gcd is a public
factor-first screen. A factor may be recorded, but it is never fed back into
orbit generation, peeling, P66, or relation construction.

## 2. Saturated private-primary theorem

Let `S` be a nonempty active row set. For `i in S`, put

\[
 P_i=\prod_{j\in S\setminus\{i\}}a_j,
 \qquad L_i=\operatorname{bitlen}(a_i),
\]

with the empty product equal to one. Compute

\[
 r_i=P_i^{L_i}\bmod a_i,
 \qquad g_i=\gcd(a_i,r_i),
 \qquad b_i=a_i/g_i.
\]

The large power is never materialized. Since reduction modulo `a_i` does not
change the gcd,

\[
 g_i=\gcd(a_i,P_i^{L_i}).
\]

Fix a rational prime `ell`, and write

\[
 e_i=v_\ell(a_i),
 \qquad E_i=\sum_{j\in S\setminus\{i\}}v_\ell(a_j).
\]

Then

\[
 v_\ell(g_i)=\min(e_i,L_iE_i).
\]

If `E_i=0`, this valuation is zero. If `E_i>0`, then

\[
 e_i\le\lfloor\log_2 a_i\rfloor<L_i\le L_iE_i,
\]

so the valuation is `e_i`. Therefore

\[
 \boxed{b_i=\prod_{\ell:\,\ell\nmid P_i}
                  \ell^{v_\ell(a_i)}.}
\]

This is the complete product of primary parts absent from all other active
rows. Plain `a_i/gcd(a_i,P_i)` is not equivalent: it can leave a shared
primary excess when `v_ell(a_i)>v_ell(P_i)`.

If `b_i` is not an integer square, some prime absent from every other active
row occurs to odd exponent in `a_i`. For every binary vector `c` such that

\[
 \prod_{j\in S}a_j^{c_j}
\]

is an integer square, the parity equation at that private prime forces
`c_i=0`. This certificate uses only multiplication, modular powering, gcd,
exact division, and an integer square test. It does not factor `a_i`.

## 3. Canonical fixed-point peel

Start with the full row set `S_0`. At round `t`, compute all `b_i` against
the same active set `S_t`. Define

\[
 D_t=\{i\in S_t:b_i\text{ is not an integer square}\}.
\]

Delete all rows in `D_t` simultaneously. Preserve row order in the survivor
list. Stop at the first empty deletion set. This rule is independent of
thread scheduling and of an arbitrary one-row deletion order.

Let

\[
 \mathcal K(S)=\left\{c\in\mathbf F_2^S:
       \prod_{i\in S}a_i^{c_i}\text{ is an integer square}\right\}.
\]

Every coordinate in `D_t` is zero on every vector in `K(S_t)`. Restriction
therefore gives a linear bijection

\[
 \mathcal K(S_t)\simeq\mathcal K(S_{t+1}),
\]

whose inverse inserts zeros on `D_t`. Induction gives

\[
 \boxed{\mathcal K(S_0)\simeq\mathcal K(S_*)}.
\]

The supplied modular root and the exact positive root are unchanged after
zero coordinates are inserted. Thus the normalized root is also unchanged.
A row can acquire a private primary part after another row is deleted, so a
single round is not complete.

Run the complete P66 gcd-free parity decoder only on `S_*`. Embed every
returned vector into the original bank by inserting zeros. If `S_*` is
empty, the theorem proves that the original kernel is zero.

## 4. Complete support-zero, support-one, and support-two layer

The zero vector is ignored. A support-one vector `e_i` is in the kernel
exactly when `a_i` is an integer square. Its positive root and supplied root
are compared by both signed gcds before residual classification.

For distinct rows put `d=gcd(a_i,a_j)`. Then

\[
 \boxed{a_i a_j\text{ is a square}
 \iff a_i/d\text{ and }a_j/d\text{ are squares}.}
\]

At a prime with valuations `alpha,beta`, the two quotient valuations are
`max(alpha-beta,0)` and `max(beta-alpha,0)`. They are both even exactly when
`alpha+beta` is even. If

\[
 a_i/d=x^2,\qquad a_j/d=y^2,
\]

the exact positive product root is `d*x*y`. This test is factor-free and
complete. It contains equal-row, inverse-row, and integer square-multiple
templates.

For every unordered pair, D05 unconditionally performs exactly:

1. one integer gcd `d=gcd(a_i,a_j)`;
2. two exact divisions `a_i/d` and `a_j/d`; and
3. two exact integer-square tests, including roots when square.

Only when both square tests pass does D05 perform the exact root multiply,
the supplied-root modular multiply and inverse, and the two signed gcds
`gcd(z-1,N)` and `gcd(z+1,N)`. The preregistration gives separate exact
counters for these unconditional operations and for the data-dependent
hits and signed gcds.

Enumerate every support-one and support-two kernel generator in canonical
bit-vector order. Verify each hit by its exact positive product root and its
two normalized-root signed gcds. Let `L_low` be their binary span and compute
its canonical RREF basis.

### 4.1 Normalized-root homomorphism

For `c in K(S_*)`, define

\[
 A(c)=\prod_i a_i^{c_i},\qquad
 s(c)=\sqrt{A(c)}>0,\qquad
 V(c)=\prod_i v_i^{c_i}\pmod N,
\]

and

\[
 z(c)=s(c)V(c)^{-1}\pmod N.
\]

The admitted roots are units, and

\[
 s(c)^2\equiv V(c)^2\pmod N,
\]

so `z(c)^2=1 (mod N)`. For `c,d in K(S_*)`, let

\[
 I(c,d)=\prod_{i:c_i=d_i=1}a_i.
\]

Positive roots and supplied roots obey

\[
 s(c)s(d)=s(c+d)I(c,d)
\]

over the integers and

\[
 V(c)V(d)\equiv V(c+d)I(c,d)\pmod N.
\]

Cancellation is valid because every `a_i` is a unit modulo `N`. Hence

\[
 \boxed{z(c+d)=z(c)z(d)\pmod N.}
\]

Thus `z` is a group homomorphism from the binary kernel to the square roots
of one modulo `N`. Let `G={+1,-1}` be the global-root subgroup. Checking a
basis of `L_low` is sufficient to decide whether `z(L_low)` is contained in
`G`; no enumeration of all vectors in `L_low` is required. D05 still checks
and reports every individual support-one and support-two hit before forming
the basis.

If the low basis has a non-global image, D05 already has a terminal public
factor certificate. It labels the operational quotient question
`UNDEFINED_LOW_IMAGE`; quotienting the codomain by `G` would not descend
through `L_low`. This terminal certificate does not stop public bank work.
D05 still constructs and verifies the complete P66 kernel, the canonical low
basis, and the canonical structural complement. All counters and
relation-local diagnostics therefore have one deterministic meaning on both
branches. A complement vector on this branch is structural evidence only.
It is never called a quotient vector and cannot count as a quotient hit.

Compute a canonical P66 basis of `K(S_*)`. Opaque blocks are ordered by
integer value. Matrix columns and pivots use original row order. Free columns
are visited left to right. Reduce this basis against the canonical basis of
`L_low` and then against earlier quotient pivots. The nonzero retained
vectors form a canonical complement basis `Q` with

\[
 \mathcal K(S_*)=L_{\rm low}\oplus\operatorname{span}(Q).
\]

On the branch where the low basis is global, `z` induces a homomorphism

\[
 \bar z:\mathcal K(S_*)/L_{\rm low}\longrightarrow \mu_2(N)/G.
\]

The induced map is nontrivial exactly when at least one vector of the
complement basis `Q` has a non-global normalized root. Consequently, basis
checks are complete for the finite quotient question. The implementation
must say "each complement-basis vector", not "every vector in the
complement". If the low image is non-global, `Q` is still the same canonical
linear complement, but `bar z` is undefined. D05 verifies each vector of `Q`
and records its root under `STRUCTURAL_ONLY_LOW_IMAGE`. It does not interpret
those roots in a quotient.

Thus a finite quotient-null statement is defined only on banks for which
all of the following hold: the bank is eligible, the full kernel and both
bases were verified, and `z(L_low)` is contained in `G`. A corpus-level
quotient-null label must require this condition for every eligible bank and
must require zero non-global images on every quotient-complement basis. A
low-support factor cannot be silently counted as a quotient null.

## 5. Relation-local elliptic diagnostics

Chord labels do not construct a parity equation and do not determine
normalized-root usefulness. They are computed only after a relation has
been exactly verified and after its result classification has been
committed.

For a verified support `C` and a pair of rows `i,j in C` on the **same
curve**, cache

\[
 H_{ij}=u_i^2+u_i u_j+u_j^2+A,
\]

\[
 d_{ij,\mathrm{tan}}=\gcd(a_i,a_j,u_i-u_j),
\]

\[
 d_{ij,\mathrm{chord}}=\gcd(a_i,a_j,H_{ij}),\qquad
 d_{ij,\mathrm{disc}}=\gcd(a_i,a_j,4A^3+27B^2).
\]

A third row `k` is admissible for this anchor only when `k` is in `C` and
on that same curve. When `d_chord>1`, its third-root predicate is

\[
 u_i+u_j+u_k\equiv0\pmod {d_{ij,\mathrm{chord}}}.
\]

For each unordered same-curve triple `{i,j,k}`, D05 evaluates all three pair
anchors

\[
 (i,j;k),\qquad(i,k;j),\qquad(j,k;i).
\]

This is necessary because the chord gcd depends on the chosen pair. A
cross-curve pair or third row is never a chord-root candidate.

For one anchor, order the two pair scalar indices as `alpha<=beta` and call
the third scalar index `gamma`. The complete frozen index menu is

`alpha+beta=gamma`, `beta-alpha=gamma`, `2*alpha=beta`,
`3*alpha=beta`, `alpha*beta=gamma`, and
`v2(alpha)=v2(beta)`.

Here `v2(r)` is the exponent of 2 in the positive integer `r`.

These predicates are evaluated separately for all three anchors. No
post-discovery predicate can be applied to heldout without a new version.

Diagnostics use only the first eight canonical complement-basis vectors
whose support is at most 16. Inside each selected support they are exhaustive
over same-curve pairs and the three anchors of every same-curve unordered
triple. The all-on-one-curve maxima are

\[
 8\binom{16}{2}=960\text{ pair tasks per bank},
\]

\[
 8\cdot3\binom{16}{3}=13{,}440
 \text{ anchored-third-row tasks per bank}.
\]

Across 768 intended banks, the second maximum is exactly `10,321,920`.
These counts describe tests, not retained detailed records. The
preregistration fixes smaller deterministic serialization caps and retains
complete aggregate counters. A support or record cap cannot change bank
eligibility, a kernel, a normalized-root result, a split label, or the
held-out decision.

## 6. Complexity and fail-safe boundary

In an active round with `r` rows of at most `R` bits, the active product has
at most `rR` bits. A product tree uses `r-1` integer multiplications. For
each row, exact division gives `P_i`; binary modular powering uses at most

\[
 2\lfloor\log_2 L_i\rfloor+1
\]

modular multiplications, followed by one gcd, one exact division, and one
square test. No `P_i^{L_i}` is materialized.

There are at most `m` nonterminal peel rounds and

\[
 \sum_t|S_t|\le m(m+1)/2.
\]

At `m<=320` and `R<=361`, this is at most 51,360 row-round tests per
maximum bank, and an active product has at most 115,520 bits. D05 rejects a
bank visibly if a fixed cap is crossed. It never interprets a partial peel,
partial P66 matrix, partial low-support scan, or partial relation check as an
eligible null.

The complete P66 phase is restricted to at most 64 surviving rows. This is a
resource boundary, not a theorem about the source. A larger fixed point is a
resource rejection.

## 7. Relation to P217/F252 and exact novelty

P217/F252 already supplies the important conceptual precedent: a
factor-free saturation can expose private odd-valuation pivots, delete their
coordinates, and leave a smaller exact numerical parity problem. It also
uses Pell polynomial structure and pairwise resultants to prove a zero
generic kernel and localize specialization-only sharing.

D05 proves no analogous elliptic source theorem. It has no polynomial
parameter, irreducibility theorem, resultant localization, generic-kernel
theorem, source success law, or bound on the fixed-point core. Its only new
claim relative to that boundary is a source-agnostic **iterative decoder
optimization**: saturate against the current numerical rows, delete all
certified private coordinates, and repeat without changing the exact
kernel or normalized roots.

P20 remains different: it pools elliptic coordinate collisions through a
scalar near `sqrt(N)`. D05 materializes at most 320 cubic rows and never
forms that product. P66 remains the complete factor-free decoder on the
surviving explicit core.

## 8. Exact scope

The peel proves preservation and a finite cost reduction. It does not prove
that any D05 bank has a private pivot, that a residual core is small, or that
a useful relation exists. D02 preflight artifacts are heuristic motivation
only and must be imported by the exact hashes in the preregistration. A
fresh hostile theory audit is required before any source is written.
