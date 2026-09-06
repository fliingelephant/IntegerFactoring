# F236 candidate — centered multiplier carries give a verified factor bank

## Status and scope

This packet has two separate parts.

1. The centered-carry identities and factor bank below are exact proof-only
   statements.
2. The numerical scans are finite evidence and named-family counterexamples.

This is not an all-input factoring algorithm.  It proves no inverse-QP
small-carry probability and no asymptotic upper bound on the best carry.

Let

\[
N=pq,\qquad p<q<2p,
\]

where `p,q` are distinct odd primes.  Put

\[
n=\lceil\log_2(N+1)\rceil,\qquad
B=2^{\lfloor n/2\rfloor},
\]

assume `B | N-1`, and define `H=(N-1)/B`.

## Exact centered-carry theorem

Fix an integer `u>=1`.  Use the fixed round-half-up convention

\[
K_p=\left\lfloor{up+B/2\over B}\right\rfloor,
\qquad
K_q=\left\lfloor{uq+B/2\over B}\right\rfloor,
\]

and write

\[
up=K_pB+x,\qquad uq=K_qB+y,
\qquad -B/2\le x,y<B/2.
\]

Then

\[
c={xy-u^2\over B}\in\mathbb Z.                       \tag{1}
\]

Moreover

\[
T:=K_pq+K_qp
 ={u^2H+K_pK_qB-c\over u}\in\mathbb Z.               \tag{2}
\]

The factor `p` is a root of

\[
K_qX^2-TX+K_pN=0,                                     \tag{3}
\]

and

\[
\Delta=T^2-4K_pK_qN=(K_pq-K_qp)^2.                   \tag{4}
\]

Thus a public guessed tuple `(u,K_p,K_q,c)` is checked by the divisibility
in (2), an integer-square test on (4), the two candidate divisions

\[
X={T\pm\sqrt\Delta\over2K_q},
\]

and exact division into `N`.  The algorithm returns only verified factors.
False tuples are harmless.

Balance gives `p>B/2`.  The size bounds below give the public range
`1<=K_p,K_q<=3u`.  Therefore the complete bank

\[
1\le u\le U,\qquad 1\le K_p,K_q\le3u,
\qquad |c|\le C,
\]

has `O(CU^3)` tuples and numerical-QP bit cost when `C,U` have numerical-QP
value.  It factors whenever the true tuple lies in the bank.  Sampling `u`
gives a Las Vegas procedure only under an additional inverse-QP lower bound
on `Pr(|c_u|<=C)`.

## Generic approximation boundary

Simultaneous Dirichlet approximation of `p/B` and `q/B` gives some `u<=U`
with

\[
|x|,|y|=O(B/\sqrt U).
\]

Substitution into (1) gives only

\[
|c|=O(B/U+U^2/B).                                     \tag{5}
\]

For numerical-polynomial `U`, this is still exponential in `n`.  Equation
(5) is a sufficient generic bound.  It does not rule out a stronger theorem
using `pq=1+BH`; this packet proves no such improvement.

## Frozen finite evidence

The preregistered domain contains every pair with

\[
3\le p<2^{22},\qquad p<q<2p,
\]

that satisfies all displayed hypotheses.  It contains 34,463 pairs and
inputs through 45 bits.

The frozen scans establish only these finite facts.

1. The public word combining `N^k-1`, `H^k-1` for `k<=n`, all
   `(uH+c)^n` for `u<=n, |c|<=n`, and `n!` can leave both P204 residuals
   large.  The exact worst row has residual minimum 2,095,493.
2. The carry residue can itself have maximal multiplicative order modulo
   both residual primes.  Taking its first `n` powers does not repair the
   word bank.
3. On the finite domain, the maxima of `min_{u<=U}|c_u|` are 27,483,
   414, and 14 for `U=n,n^2,n^3`.
4. The fully public synchronized center `round(uH/B)` has no multiplier
   improvement in this domain: the worst minimum remains 1,322,450 for all
   three caps.
5. For uniform `u` in `[1,n^3]`, the minimum finite hit fraction for
   `|c_u|<=n` is `15/91125`.  No asymptotic inference is made.

All raw sources, preregistrations, outputs, hashes, and run provenance are
part of the frozen packet.
