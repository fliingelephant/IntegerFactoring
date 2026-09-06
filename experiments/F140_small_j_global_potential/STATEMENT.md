# F140 statement — public small-quotient paths can have polynomial depth

## Status and closest boundary

This is a proof-only candidate.  It is not a complete-source null, a global
path bound, or a factoring algorithm.

The closest boundaries are X73--X77 and P120--P125.  P124 proves that a
released transition with quotient at least the anchor cap decreases the
active block, and that two consecutive such transitions contract.  It leaves
open whether small-quotient recentering can interrupt descent only a few
times.  P125 separates public row reuse from a final rank defect.

F140 gives an exact material difference: for arbitrarily large input length,
one deterministic selected path can make polynomially many consecutive
public releases with quotient exactly one.  All selected exact values are
new, every selected or pre-dedup duplicate endpoint screen is null, and the
selected parity matrix has full column rank because every column has a public
private row.

## The theorem

There is an absolute constant \(c>0\) and an infinite sequence of odd
distinct semiprimes \(N\) with

\[
n=\lceil\log_2(N+1)\rceil
\]

for which the following holds.  Starting from one already named unit block
\(q_0<N/n^3\), there is a deterministic factor-free selected path of length

\[
\boxed{t\ge c n^{1/3}}
\]

through the canonical-inverse anchored source.  At transition \(i\), complete
retention already contains a public base value \(B_{i+1}\); the selected
anchored value \(V_i\) gives

\[
\boxed{\gcd(V_i,B_{i+1})=q_{i+1}},
\]

so gcd-free refinement publicly names the next unit block.  The P124 divisor
quotient is

\[
\boxed{j_i=1<n^3}
\]

at every transition.  The active blocks increase instead of descend.

All base values \(B_i\) and selected anchored values \(V_i\) are distinct.
Their binary valuation matrix has full column rank.  Therefore this selected
transcript has no square dependency and no normalized root to test.  Every
canonical endpoint sign screen on the selected path, including duplicate
base presentations before exact-value deduplication, is null.

The source labels used in the construction are at most \(n^3\), and the
selected work is polynomial in \(n\).

## Exact construction

Fix a target transition count \(t\).  Put

\[
k_i=i+2\qquad(0\le i\le t).
\]

Choose an even integer \(D_t>t+2\) divisible by every prime factor of

\[
\prod_{i=0}^{t}k_i
\prod_{d=1}^{t}(2^d-1),
\]

with \(\log D_t=O(t^2)\), and define

\[
q_i=2^iD_t+1.
\]

Then the \(q_i\) are pairwise coprime and \(\gcd(k_i,q_i)=1\).  Define

\[
K_i=k_i+2q_i\qquad(0\le i<t).
\]

The exact recurrence is

\[
\boxed{K_i=q_{i+1}+k_{i+1}}.
\]

Choose distinct public seed primes \(\sigma_i>k_i\) and distinct anchor
primes \(\lambda_i>2\).  Choose all of them outside the prime divisors of the
\(q_i\) and of every nonzero difference between two carries in

\[
\mathcal C_t=\{k_0,\ldots,k_t,K_0,\ldots,K_{t-1}\}.
\]

They can be chosen with

\[
\max(\sigma_i,\lambda_i)=O(t^4\log t).
\]

Use the Chinese remainder theorem to choose one unit class \(N_0\) modulo

\[
R=
\left(\prod_{i=0}^{t}q_i\right)
\left(\prod_{i=0}^{t}\sigma_i^2\right)
\left(\prod_{i=0}^{t-1}\lambda_i^2\right)
\]

such that

\[
\begin{aligned}
k_iN_0&\equiv-1\pmod{q_i},\\
v_{\sigma_i}(1+k_iN_0)&=1,\\
v_{\lambda_i}(1+K_iN_0)&=1.
\end{aligned}
\]

Take distinct primes \(P,Q>R\) in reduced arithmetic progressions whose
product is \(N_0\bmod R\), and put \(N=PQ\).  The progressions can be chosen
so that Linnik's theorem gives

\[
\log N=O(\log R)=O(t^3).
\]

For this \(N\), define

\[
B_i=1+k_iN,
\qquad
V_i=1+K_iN.
\]

The public seed \(\sigma_i\) gives the canonical endpoint presentation

\[
\left(\sigma_i,\frac{B_i}{\sigma_i}\right).
\]

At state \(q_i\), the anchor \(\lambda_i\) has induced digit two and gives

\[
\left(
\lambda_iq_i,
\frac{V_i}{\lambda_iq_i}
\right).
\]

The next base value and selected high value satisfy

\[
\gcd(V_i,B_{i+1})=q_{i+1}.
\]

Thus the release uses only exact integer gcd refinement.  It does not use a
factor of \(N\), integer factorization, or an oracle.

## Exact scope

The theorem assumes that \(q_0\) has already been named, as P124 does.  It
controls one selected path, not all branches or all source columns.  Other
unselected relations can still factor \(N\), cancel a private selected row,
or create a useful normalized root.

The construction rules out a polylogarithmic bound derived only from the
local P124 state, public release, exact-value novelty, endpoint screens, and
selected-path rank.  It does not rule out a polynomial global potential.
Indeed, the displayed path has polynomial length.  It also does not rule out
a selector that deliberately avoids this path.

The remaining positive target is therefore sharper: use the complete source
or a specified selection rule to prove a polynomial global bound, or prove a
final rank defect and non-global normalized root before such a path can keep
adding private pivots.
