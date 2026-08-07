# Proof-blind reconstruction statement — fixed orientations and fresh pivots

Reconstruct or refute every claim below. Work only from this file. Do not read
the candidate, either audit, `PROVED.md`, `FAILED.md`, or
`notes/Progress.md`.

## Fixed orientation

Let $N\ge3$. Let $X_1,\ldots,X_m$ be independent uniform elements of
$G=(\mathbb Z/N\mathbb Z)^\times$. Fix a nonzero vector
$\epsilon\in\{-1,0,1\}^m$ and put

\[
Z=\prod_iX_i^{\epsilon_i}\pmod N.
\]

Claim: $Z$ is exactly uniform in $G$.

## Direct-screen probabilities

Let $N=pq$ for distinct odd primes. For uniform $Z\in G$, claim that

\[
\Pr\bigl(\gcd(Z-1,N)\text{ or }\gcd(Z+1,N)
          \text{ is proper}\bigr)
=\frac{2p+2q-10}{(p-1)(q-1)}.
\]

Claim also that the probability that $Z$ is a useful non-global square root
of one is

\[
\frac{2}{(p-1)(q-1)}.
\]

The first event is broader than the second.

## Fixed menus

For any fixed menu of $T$ signed patterns, the outputs can share base units,
be equal, or be inverses. Joint independence is not assumed. Claim the union
bounds

\[
\Pr(\text{some direct screen succeeds})
\le
T\frac{2p+2q-10}{(p-1)(q-1)},
\]

and

\[
\Pr(\text{some useful involution appears})
\le\frac{2T}{(p-1)(q-1)}.
\]

These are upper bounds, not asymptotic equalities. On balanced semiprimes and
$T=\operatorname{poly}(\log N)$, both are exponentially small in the input
bit length.

## Adaptive fresh-pivot extension

Let $\mathcal H_{t-1}$ be the complete history before trial $t$. Conditional
on that history, let $C_t\in G$ and $s_t\in\{+1,-1\}$ already be fixed. Let
$U_t$ be uniform in $G$ and independent of $\mathcal H_{t-1}$, and set

\[
Z_t=C_tU_t^{s_t}.
\]

Claim: $Z_t$ is uniform conditional on every realized history. Conditioning
on all previous failures does not change this. Therefore the same per-trial
and union bounds hold for at most $T$ adaptive fresh-pivot trials.

`Fresh` means conditionally uniform given the complete past. Marginal
uniformity or being physically unobserved is insufficient if the pivot is
correlated with the past.

## Exact scope

The result covers fixed signed orientations over independent uniform units,
including reuse across menu entries, and adaptive products masked by a
conditionally uniform unseen pivot. It does not cover:

- choosing an exponent after observing that same unit;
- a candidate with no independent-uniform coordinate left after reuse;
- correlated or nonuniform base states;
- integer gcd-free splitting, block sizes, occurrence multiplicities,
  completion quotients, endpoint magnitudes, or adaptive block refinement.

The theorem does not claim that dependence on integer presentation is the
only escape. Observed-residue dependence can also destroy uniformity. It
supplies no all-input selector or factoring algorithm.

Give a self-contained proof or a counterexample, with a clear PASS/FAIL
verdict and exact scope.
