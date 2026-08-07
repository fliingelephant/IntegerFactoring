# Proof-blind statement — metric-guided cross-feedback boundary

Reconstruct or refute every claim below from this file only. Do not read the
candidate, either audit, ledgers, or prior proof records. Give a self-contained
PASS/FAIL verdict and keep every menu and occurrence convention exact. Do not
use computational search as proof.

## Setup and exact menu

Let $N=pq$ for distinct odd primes. For a canonical unit
$r\in\{1,\ldots,N-1\}$, let $w$ be its canonical inverse and put

\[
d=r-w,
\qquad
\delta=|d|,
\qquad
\Delta=\delta^2+4.
\]

Let the current pairwise-coprime integer block types be
$B_1,\ldots,B_s$. Define the exact distinct-block pair menu

\[
\mathcal O_{=2}(B)=
\left\{
\{u,u^{-1}\}:
u=\operatorname{can}(B_i^\epsilon B_j^\eta\bmod N),\
i<j,\ \epsilon,\eta\in\{-1,1\}
\right\},
\]

with duplicate unordered inverse orbits removed. It excludes support-zero and
support-one terms, repeated indices, other exponents, and an independent
global minus sign. The filtered algorithm runs all immediate public screens,
removes $\{1\}$ and $\{N-1\}$, and then ranks the remaining distinct
factor-free orbits. It has no implicit occurrence budget. Re-appending an
identical endpoint relation is ignored unless a separate algorithm explicitly
authorizes and charges a new occurrence.

## Claims

### 1. Exact torsion meaning of inverse distance

For every prime $\ell\mid N$,

\[
\ell\mid d
\Longleftrightarrow r^2\equiv1\pmod\ell,
\qquad
\ell\mid d^2+4
\Longleftrightarrow r^2\equiv-1\pmod\ell.
\]

Because $N$ is squarefree,

\[
\gcd(d,N)=\gcd(r^2-1,N),
\qquad
\gcd(d^2+4,N)=\gcd(r^2+1,N),
\]

and these two gcds are coprime. The second equality is not claimed for
nonsquarefree moduli.

If $\delta>0$, a proper direct screen on $r-1$ or $r+1$ occurs exactly when
$\gcd(\delta,N)>1$. In that case $\gcd(\delta,N)$ is itself proper. Hence
every non-self-inverse direct separator satisfies

\[
\delta\ge\min(p,q).
\]

If $\delta=0$, $r$ is self-inverse and the separate two sign screens
distinguish global from mixed CRT roots. The canonical inverse $w$ has exactly
the same direct sign gcds as $r$.

The discriminant gcd detects the separate local event $r^2=-1$. Once both
torsion gcds are one, the remaining numerical size of $\delta$ has no further
proved local torsion meaning.

### 2. Public square endpoint certificate and fibres

If $r\ne w$ and the exact endpoint product is a square,

\[
rw=m^2,
\]

then $2\le m\le N-2$, $m^2\equiv1\pmod N$, and $m$ is a non-global root.
Both sign gcds of $m$ return the two factors. In particular, a distance-one
inverse pair cannot have square product.

For each fixed signed $d$, the inverse-fibre congruence

\[
r^2-dr-1\equiv0\pmod N
\]

has at most four roots. Thus the full inverse graph has at most $4+8D$
oriented states, and at most $4+4D$ unordered inverse pairs, with
$\delta\le D$. This upper bound does not prove that a transcript-derived menu
contains a useful low-distance state.

### 3. Ranking an exhausted menu

If a polynomial menu is exhaustively screened, sorting cannot change its
current-round direct success. After a miss, a retained inverse relation can
matter only if it strictly changes the integer gcd-free block presentation or
an explicitly charged occurrence box. Otherwise rebuilding the same menu is a
no-op. An equal relation value with a different endpoint factorization can
still matter because it can create new integer gcd overlaps.

### 4. Finite obstructions to metric monotonicity

At $N=77$, the old relation $2\cdot39=78$ has blocks $2,39$. The raw menu
before global filtering has exactly the inverse orbits

\[
\{1\},\qquad\{4,58\}.
\]

Both direct and discriminant tickets fail on the nontrivial orbit. If a faulty
variant keeps the identity, takes $K=1$, and an identity append changes no
block or occurrence state, it is an exact conditional fixed point. The
filtered algorithm removes it. Also, $77$ is the smallest product of distinct
odd primes for which there is a unit $r\not\equiv\pm1$ whose two torsion gcds
are both one.

At $N=209$, the inverse pair $80,81$ has distance one and survives the direct
and discriminant screens, while the farther pair $10,21$ has distance eleven
and $\gcd(10+1,209)=11$. Thus smaller positive distance is not monotone toward
a direct factor.

At $N=143$, the four inverse pairs

\[
(9,16),\ (61,68),\ (75,82),\ (127,134)
\]

all have distance seven and identical trivial direct/discriminant outcomes.
The first product is $144=12^2$ and exposes $11,13$ through the root, while
the other three products are nonsquares. Thus the metric does not determine
even singleton square closure.

### 5. Genuine representation-level feedback at (N=209)

Start from

\[
31\cdot27=837=1+4\cdot209,
\qquad
3\cdot70=210=1+209.
\]

Complete gcd-free refinement gives old block types $\{3,31,70\}$. Apart
from the global identity, the exact menu has precisely

\[
\{80,81\},
\qquad
\{9,93\}.
\]

Both survive the immediate screens, and $\{80,81\}$ is the unique lowest
positive-score orbit. Appending

\[
80\cdot81=1+31\cdot209
\]

and jointly refining the exact endpoints

\[
80=2^4\cdot5,
\quad81=3^4,
\quad70=2\cdot5\cdot7,
\quad27=3^3
\]

creates the block types

\[
\{2,3,5,7,31\}.
\]

The next exact menu contains $2\cdot5=10$, and
$\gcd(10+1,209)=11$.

This is a strict modular-subgroup change at the block level. Before feedback,

\[
70\equiv3^{-1},
\qquad31\equiv3^{-3}\pmod{209},
\]

so all old block residues generate $H_0=\langle3\rangle$. The residue
$10$ is not in $H_0$: modulo $11$, $3$ has order five and its subgroup does
not contain $-1\equiv10$. Therefore no old-block monomial with arbitrary
integer exponents and no free global minus sign produces $10$.

The feedback endpoint residues $80,81$ are still in $H_0$. The strict
enlargement happens only because integer gcd refinement exposes the factors
$2$ and $5$ separately. Their product $10$ lies in the enlarged
block-generated subgroup and outside $H_0$. Thus feedback can change the
available modular generator subgroup through integer representation even when
the new whole endpoint residue is already in the old subgroup.

## Scope

The inverse-distance score gives no universal monotonicity, closure, or
all-input hitting law. The result does not kill adaptive canonical-endpoint
feedback: the final $N=209$ example proves that it can cause a real algorithm
change. The surviving problem is to prove that polynomially many precisely
defined candidates and rounds produce such useful refinement with an
all-input inverse-polynomial law.
