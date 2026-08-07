# F64 — data-independent cross orientations remain uniform

**Status:** revised candidate proof-only selector obstruction. No research
computation was run. A hostile audit rejected the first version's final scope
claim while passing both numbered theorems.

Cross-relation products do not gain factor correlation merely by multiplying
independent uniform unit states. A fixed signed product is itself exactly
uniform. Even the broader direct screens of $z-1$ and $z+1$ then have only
square-root-scale probability on a balanced semiprime.

This result does not cover F62's data-dependent block selector. That selector
examines integer gcd refinements, occurrence multiplicities, and magnitudes.
Those operations are precisely how it can escape this theorem.

## 1. Fixed orientation law

Let $N\ge3$, let

\[
X_1,\ldots,X_m
\]

be independent uniform elements of $(\mathbb Z/N\mathbb Z)^\times$, and fix
a nonzero exponent vector

\[
\epsilon\in\{-1,0,1\}^m.
\]

Put

\[
Z=\prod_{i=1}^mX_i^{\epsilon_i}\pmod N.
\]

### Theorem 1

The output $Z$ is uniform in $(\mathbb Z/N\mathbb Z)^\times$.

### Proof

Choose an index $j$ with $\epsilon_j=1$ or $-1$, and condition on every
other $X_i$. The map

\[
X_j\longmapsto C X_j^{\epsilon_j}
\]

is a bijection of the unit group for the fixed conditioned unit $C$.
Therefore the conditional output, and hence the unconditional output, is
uniform. \(\square\)

The same proof permits a pattern and multiplier selected from any prior
history, provided at least one fresh uniform unit enters with exponent
$1$ or $-1$ and the choice is made before that fresh unit is observed.

## 2. Exact direct-screen probability

Let $N=pq$ for distinct odd primes. For uniform $Z$, screen

\[
\gcd(Z-1,N),\qquad\gcd(Z+1,N).
\]

### Theorem 2

The probability that at least one screen is a proper factor is

\[
\boxed{
\frac{2p+2q-10}{(p-1)(q-1)}.}
\]

The probability that $Z$ is itself a non-global square root of one is

\[
\boxed{
\frac{2}{(p-1)(q-1)}.}
\]

### Proof

CRT makes $Z$ uniform in

\[
\mathbb F_p^\times\times\mathbb F_q^\times.
\]

A proper $\pm1$ screen occurs exactly when at least one component is $1$
or $-1$, except for the two global points $(1,1)$ and $(-1,-1)$.
The union of the two local sign strips has size

\[
2(q-1)+2(p-1)-4.
\]

Removing the two global points leaves $2p+2q-10$ useful pairs. A
non-global square root of one is one of the two opposite-sign pairs
$(1,-1)$ and $(-1,1)$. Division by $(p-1)(q-1)$ proves both formulas.
\(\square\)

## 3. Polynomial menus remain sparse

For any fixed menu of $T$ signed patterns, independence between the
resulting products is not required. Patterns can reuse the same base units,
be equal, or be inverses. The union bound gives direct-screen success at most

\[
T\frac{2p+2q-10}{(p-1)(q-1)}.
\]

On any balanced semiprime family with $p,q=\Theta(\sqrt N)$, this is

\[
T\,N^{-1/2+o(1)}.
\]

Thus $T=\operatorname{poly}(\log N)$ gives exponentially small success in
the input bit length. For useful non-global involutions, the exact menu bound
is

\[
\Pr(\text{some useful involution})
\le \frac{2T}{(p-1)(q-1)}=O(T/N)
\]

on a balanced family. This is an upper bound. Repeated or equivalent patterns
need not make the actual probability grow with $T$.

The same conditional argument covers a sequence of at most $T$ trials in
which each trial uses a fresh unseen uniform pivot with exponent $\pm1$.
Conditioned on all previous failures, its candidate remains uniform, so the
same union bound applies.

## 4. Exact scope and escape conditions

Under the independent-uniform input model, the theorem closes fixed signed
orientations and adaptive products masked by a conditionally uniform unseen
pivot. A fixed menu can reuse base units. Reuse escapes only when it removes
the required independent-uniform coordinate inside a candidate, or when the
rule is chosen after observations.

The theorem does not cover a selector that observes a unit before deciding
whether or how to use it. Such a rule can destroy uniformity without using
integer presentation data. It also does not cover:

- gcd-free splitting of the integer endpoints;
- selection based on block sizes or multiplicities;
- completion-quotient or inverse-endpoint magnitude bias;
- reuse of a block across several relations; or
- adaptive feedback in which a new endpoint changes the block basis.

Therefore the result identifies, rather than removes, a live source-side
question. F62's named selector lies outside the theorem because it uses the
integer presentation of the relations. The theorem does not prove that this
is the only escape. Observed-residue dependence, correlated or nonuniform
base states, and other data-dependent operations also remain open.
