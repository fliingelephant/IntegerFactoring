# Proof-blind reconstruction result — fixed orientations and fresh pivots

## Verdict

**PASS**, with one necessary terminology convention: a direct screen succeeds
when the gcd is a nontrivial proper divisor, meaning (1<d<N). This is the
standard factoring meaning of “proper” in this context. If (1) were counted
as proper, the stated direct-screen probability would be false (indeed, for
odd (N), at least one of the two gcds is always less than (N)).

Under the nontrivial-proper convention, all probability formulas and all
stated upper bounds hold in exactly the stated scope.

## 1. A fixed nonzero signed orientation is uniform

Let (G=(\mathbb Z/N\mathbb Z)^\times), and choose an index (j) for which
(\epsilon_j\in\{-1,+1\}). Condition on all (X_i) with (i\ne j).
Their contribution is then a fixed element

\[
C=\prod_{i\ne j}X_i^{\epsilon_i}\in G,
\]

and

\[
Z=CX_j^{\epsilon_j}.
\]

Both maps (x\mapsto x^{-1}) and (x\mapsto Cx) are bijections of (G).
Since (X_j) is uniform and independent of the conditioned variables,
(CX_j^{\epsilon_j}) is uniform on (G) for every conditioning value.
Averaging over the conditioned variables proves that (Z) is exactly
uniform. No property special to a cyclic group is needed.

## 2. Exact direct-screen counts

For (N=pq), the Chinese remainder theorem identifies a uniform (Z\in G)
with a uniform pair

\[
(a,b)\in \mathbb F_p^\times\times\mathbb F_q^\times.
\]

Thus all ((p-1)(q-1)) pairs are equally likely. Define

\[
E_+=\{\text{exactly one of }a,b\text{ equals }1\},\qquad
E_-=\{\text{exactly one of }a,b\text{ equals }-1\}.
\]

The gcd (\gcd(Z-1,N)) is nontrivial and proper exactly on (E_+), and
(\gcd(Z+1,N)) is nontrivial and proper exactly on (E_-). Their sizes are

\[
|E_+|=(q-2)+(p-2)=p+q-4,
\]

and likewise (|E_-|=p+q-4). Because (p) and (q) are odd, (1\ne-1)
in both fields, and

\[
E_+\cap E_-=\{(1,-1),(-1,1)\}.
\]

Inclusion-exclusion therefore gives

\[
|E_+\cup E_-|
=2(p+q-4)-2
=2p+2q-10,
\]

so

\[
\Pr(E_+\cup E_-)
=\frac{2p+2q-10}{(p-1)(q-1)}.
\]

The four square roots of one modulo (pq) are the CRT pairs

\[
(1,1),\quad(-1,-1),\quad(1,-1),\quad(-1,1).
\]

The first two are the global roots (+1) and (-1). The other two are the
useful non-global roots. Hence

\[
\Pr(\text{useful non-global square root of one})
=\frac{2}{(p-1)(q-1)}.
\]

The useful event is (E_+\cap E_-), whereas the direct-screen event is
(E_+\cup E_-). Thus the former is contained in the latter. The containment
is strict for distinct odd primes.

## 3. Fixed menus need no joint independence

Let the events for menu entry (r) be (D_r) (direct-screen success) and
(I_r) (useful involution). Every fixed nonzero signed pattern has a uniform
output by Section 1, even when different entries reuse the same base units.
Consequently,

\[
\Pr(D_r)=\alpha:=\frac{2p+2q-10}{(p-1)(q-1)},\qquad
\Pr(I_r)=\beta:=\frac{2}{(p-1)(q-1)}.
\]

If an all-zero signed pattern is allowed in the menu, its output is (1),
so it triggers neither event and has probability zero for both. Therefore
the union bound gives, without any joint-independence assumption,

\[
\Pr\!\left(\bigcup_{r=1}^T D_r\right)
\le \sum_{r=1}^T\Pr(D_r)
\le T\alpha,
\]

and

\[
\Pr\!\left(\bigcup_{r=1}^T I_r\right)
\le \sum_{r=1}^T\Pr(I_r)
\le T\beta.
\]

These are upper bounds, not equalities. For example, if all (T) patterns
are equal, all their events are equal and the union probability is only
(\alpha) or (\beta), not (T\alpha) or (T\beta). The bounds remain
valid when their displayed right-hand sides exceed (1).

This fixed-menu argument is unconditional. In particular, it does **not**
assert that the next reused output remains uniform after conditioning on
earlier menu failures. Such conditional uniformity is unnecessary for the
fixed-menu union bound.

For the usual meaning of a balanced semiprime, (p/q) is bounded above and
below by positive constants. Hence (p,q=\Theta(\sqrt N)), and

\[
\alpha=O(N^{-1/2}),\qquad \beta=O(N^{-1}).
\]

If (n=\lceil\log_2 N\rceil) and (T=\operatorname{poly}(n)), then

\[
T\alpha=2^{-\Omega(n)},\qquad T\beta=2^{-\Omega(n)}.
\]

Thus both fixed-menu upper bounds are exponentially small in the input bit
length.

## 4. Adaptive trials require a conditionally fresh pivot

Fix any realized history (h) before trial (t) that has positive
probability. Under the hypotheses, (C_t=c\in G) and (s_t=s\in\{+1,-1\})
are fixed at that history, while

\[
\Pr(U_t=u\mid\mathcal H_{t-1}=h)=\frac1{|G|}
\quad\text{for every }u\in G.
\]

The map

\[
u\longmapsto cu^s
\]

is a bijection of (G). Therefore, for every (z\in G),

\[
\Pr(Z_t=z\mid\mathcal H_{t-1}=h)=\frac1{|G|}.
\]

This remains true when (h) records that every previous trial failed,
because those failures are part of the complete past on which fresh
conditional uniformity is assumed.

For completeness, let (R_t) be the event that trial (t) is reached; it is
measurable with respect to (\mathcal H_{t-1}). On (R_t), the conditional
direct-screen and useful-involution probabilities are exactly (\alpha) and
(\beta). Thus

\[
\Pr(R_t\cap D_t)
=\mathbb E\!\left[\mathbf 1_{R_t}
  \Pr(D_t\mid\mathcal H_{t-1})\right]
=\alpha\Pr(R_t)\le\alpha,
\]

and similarly (\Pr(R_t\cap I_t)\le\beta). For any adaptive procedure
that performs at most (T) trials,

\[
\Pr(\text{some direct screen succeeds})\le T\alpha,
\qquad
\Pr(\text{some useful involution appears})\le T\beta.
\]

Again, these conclusions are upper bounds. The exact conditional per-trial
probabilities do not turn an arbitrary “at most (T)” adaptive schedule into
an equality statement.

Marginal uniformity alone cannot replace freshness. For example, let (V)
be uniform on a finite group, let the history reveal (V), and set the next
pivot (U=V). Then (U) is marginally uniform, but conditional on the
history it is deterministic. The same failure occurs when a stored pivot is
not directly inspected but the past reveals a correlated copy or function
of it. “Unseen” must therefore mean uniform conditional on the complete
past, not merely physically unobserved.

## 5. Exact scope and exclusions

The proved conclusions cover precisely these two mechanisms:

1. A fixed signed orientation of independent uniform units. A fixed menu may
   reuse units across entries, and its entries may coincide or be inverses.
   Reuse affects dependence between entries but not each entry's marginal
   uniformity or the unconditional union bound.
2. An adaptive candidate of the form (C_tU_t^{s_t}), where (C_t) and
   (s_t) are determined by the complete past and (U_t) is uniform
   conditional on that past. Here the fresh pivot supplies the required
   conditional uniformity after previous failures.

The first mechanism must not be silently upgraded to the second: a reused
fixed-menu output need not be uniform conditional on previous failures.

The result gives no conclusion for:

- an exponent selected after observing the same unit;
- an adaptive candidate with no independent-uniform coordinate remaining
  after reuse;
- correlated or nonuniform base states;
- integer gcd-free splitting, block sizes, occurrence multiplicities,
  completion quotients, endpoint magnitudes, or adaptive block refinement.

These are exclusions, not assertions that every excluded construction must
be nonuniform. The assumptions can, however, fail essentially. For example,
with a uniform (X\in(\mathbb Z/5\mathbb Z)^\times), choose exponent (-1)
when (X=3) and (+1) otherwise. Then both (X=2) and (X=3) produce
output (2), so the adaptively oriented output is not uniform. Likewise, if
(X_1=X_2) are correlated uniform variables and the fixed exponents are
((1,-1)), the output is always (1).

Thus dependence on integer presentation is not the only possible escape
from the uniformity argument: dependence on an observed residue can also
destroy it. Conversely, this probability theorem supplies neither an
all-input selector nor a factoring algorithm.
