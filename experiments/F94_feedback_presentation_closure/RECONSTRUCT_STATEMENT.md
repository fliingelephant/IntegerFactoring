# F94 proof-blind reconstruction statement

Do not inspect `RESULT.md`, any audit file, or any other F94 artifact. Prove
or refute the following claims from this statement and the listed key ideas
only. Report every needed correction and the exact algorithmic scope.

## Setup

Let \(N\ge2\). Let \(q_1,\ldots,q_s>1\) be pairwise-coprime integer
units modulo \(N\). The algorithm knows \(m\) relations

\[
\prod_{j=1}^s q_j^{e_{ji}}\equiv1\pmod N,
\qquad
E=(e_{ji})\in\mathbb Z_{\ge0}^{s\times m}.
\]

The columns of \(E\) are only the relations that the algorithm knows.

Joint exact gcd-free refinement with new endpoints gives pairwise-coprime
blocks \(b_1,\ldots,b_t>1\) and exact exponents

\[
q_j=\prod_{r=1}^t b_r^{\alpha_{rj}}.
\]

The nonempty supports
\(D_j=\{r:\alpha_{rj}>0\}\) are pairwise disjoint. Let \(F\) contain the
rows that divide no old \(q_j\). Define the exponent map

\[
(\Delta_\alpha x)_r=\sum_j\alpha_{rj}x_j,
\qquad
E'=\Delta_\alpha E.
\]

Fix a prime \(\ell\) and reduce matrices modulo \(\ell\).

## Claim 1 — exact multiplicity-refinement gate

Prove

\[
\ker E'=\{c:Ec\in\ker\Delta_\alpha\}
\]

and

\[
\dim\ker E'-\dim\ker E
=\dim(\operatorname{im}E\cap\ker\Delta_\alpha).
\]

Using disjoint supports, prove

\[
\ker\Delta_\alpha
=\operatorname{span}\{e_j:
\ell\mid\alpha_{rj}\text{ for every }r\in D_j\}.
\]

Therefore refinement adds a known \(\ell\)-saturation dependency exactly
when \(\operatorname{im}E\cap\ker\Delta_\alpha\ne0\). It preserves the old
kernel when each old block has some descendant exponent not divisible by
\(\ell\). Check the example

\[
N=3,
\quad q_1=4\equiv1\pmod3,
\quad E=[1],
\quad4=2^2,
\]

where the mod-two kernel grows after refinement.

## Claim 2 — exact appended-column gate

Append one known relation column \(u\) in the refined coordinates. Put

\[
V_\ell=\ker E',
\qquad
\kappa_\ell(E')=m-\operatorname{rank}(E').
\]

Prove the exact dichotomy:

- if \(u\notin\operatorname{colspan}(E')\), then

  \[
  \ker[E'\mid u]=V_\ell\times\{0\},
  \qquad
  \kappa_\ell([E'\mid u])=\kappa_\ell(E');
  \]

- if \(E'c+u=0\), then

  \[
  \ker[E'\mid u]
  =(V_\ell\times\{0\})\oplus\langle(c,1)\rangle,
  \qquad
  \kappa_\ell([E'\mid u])=\kappa_\ell(E')+1.
  \]

Thus the known saturation kernel can grow only through the multiplicity gate
of Claim 1 or the column-closure gate of Claim 2.

Under the full hypotheses of P91—\(N=pq\) for distinct odd primes, failure
of the complete old decoder on the explicit known root image, and
numerically polynomial \(\ell\)—explain why a closing column gives one new
root coset and at most \(\ell\) complete gcd tests. Do not extend this P91
consequence to arbitrary \(N\).

## Claim 3 — fresh-row obstruction

Every vector in \(\operatorname{colspan}(E')\) is zero on the fresh rows
\(F\). Therefore, if the new column has a nonzero entry modulo \(\ell\) on
one fresh row, it is nonclosing. If that entry is the integer one, it is
nonclosing for every prime \(\ell\).

Apply this to canonical-inverse feedback. A current block product \(g\) and
its least positive inverse \(w\) give

\[
gw=1+kN.
\]

If refinement leaves a new cofactor of \(w\), absent from all old rows and
occurring in the new relation to exponent one, the new column cannot close
on that step. This does not rule out a direct gcd, a power or mixed-word
decoder, the multiplicity gate, or later block reuse.

## Claim 4 — many private columns do not amortize

Fix one final refined coordinate system. Let \(M_0\) be the lifted old
matrix and append \(u_1,\ldots,u_M\). For each \(i\), suppose there is a
distinct row \(r_i\) such that

\[
(M_0)_{r_i,*}=0,
\qquad
(u_i)_{r_i}\not\equiv0\pmod\ell,
\qquad
(u_j)_{r_i}\equiv0\pmod\ell\quad(j<i).
\]

Prove

\[
\ker[M_0\mid u_1\mid\cdots\mid u_M]
=\ker(M_0)\times\{0\}^M.
\]

Hence a batch in which every relation retains its own private fresh block to
exponent one adds no new prime-saturation direction. Later refinement can
invalidate the premise only by opening Claim 1's multiplicity gate.

## Claim 5 — full-group source changes the progress measure

Condition on retained raw units \(a_1,\ldots,a_d\) that generate

\[
G_N=(\mathbb Z/N\mathbb Z)^\times.
\]

If every \(a_i\) is represented by current unit blocks \(B\), prove

\[
\langle B\rangle=G_N.
\]

This remains true after any no-factor refinement that retains those exact
representations. Feedback cannot enlarge the abstract residue subgroup on
this P99 source event. It can still expose named integer blocks and known
relations. The complete relation lattice or an exponent word for a new block
is not supplied by abstract generation.

## Claim 6 — complexity and deletion scope

Show that matrix lifting, kernel-basis updates, span tests, and the promoted
prime-root decoder menus are polynomial in the total bit size of the
explicit maintained presentation and scanned primes, plus \(\log N\). They
are polynomial in \(\log N\) only under explicit polynomial caps on all
retained blocks, relations, scanned primes, and feedback steps. The algorithm
must use a kernel basis or a promoted polynomial-size menu, not enumerate all
vector-space directions.

Verify the deletion warning over \(\mathbb F_2\): the first column \([1]\)
is nonclosing against an empty matrix, while a second \([1]\) closes and
creates \((1,1)\). Deleting the first column destroys that known dependency.
This shows only that ephemeral deletion can lose future closure information;
it does not show that the dependency factors \(N\).

## Required scope judgment

Decide whether these claims prove only exact presentation accounting. They
must not be interpreted as an all-input source law, a polynomial state cap,
a guarantee that a root is non-global, a factoring algorithm, or a
computational lower bound.

## Claimed key ideas

1. Use the full exponent map, not row duplication.
2. Restrict the old relation map to the refined kernel and apply
   rank-nullity.
3. Use disjoint descendant supports to identify
   \(\ker\Delta_\alpha\).
4. For private columns, inspect the last nonzero appended coordinate.
5. For the P99 consequence, sandwich the block subgroup between the retained
   generator subgroup and the full unit group.
