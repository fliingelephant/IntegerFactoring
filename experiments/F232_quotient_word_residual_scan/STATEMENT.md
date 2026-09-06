# F232 candidate — shifted quotient factors form an exact residual-order word

## Status and scope

This is a symbolic candidate plus a preregistered finite discovery test.  It
is not an all-input factoring algorithm.  The finite test cannot prove an
asymptotic success bound.

The closest prior routes are F228, F230, and F231.  F228 factors quotient
children one at a time and identifies their carry support.  F230 and F231
use the zero-defect exponent `H`, but their multiplier words contain only
public smooth primes and primes supported by `H`.  F232 differs materially:
it factors a public numerical-QP bank of the shifted, `N`-dependent quotient
children and inserts every exposed prime, to saturating exponent, into one
F231 multiplier word.

Let

\[
N=pq,\qquad p<q<2p,\qquad
n=\lceil\log_2(N+1)\rceil,\qquad
B=2^{\lfloor n/2\rfloor},
\]

where `p` and `q` are distinct odd primes.  Work in the zero-defect branch

\[
B\mid N-1,\qquad H={N-1\over B}.
\tag{1}
\]

Put

\[
P=(p-1)_{\rm odd},\quad Q=(q-1)_{\rm odd},\quad
D=\gcd(P,Q),\quad s_p=P/D,\quad s_q=Q/D.
\tag{2}
\]

For odd positive `u` and an integer `c`, define

\[
A_{u,c}=uH+c.
\tag{3}
\]

This is exactly the F228 shifted quotient child in branch (1).

## Lemma A — exact asymmetric residual support

For every admissible `(u,c)`,

\[
\boxed{
\gcd(A_{u,c},s_p)
=\gcd\bigl(u(q-1)+cB,s_p\bigr),
}
\tag{4}
\]

\[
\boxed{
\gcd(A_{u,c},s_q)
=\gcd\bigl(u(p-1)+cB,s_q\bigr).
}
\tag{5}
\]

The equalities include complete prime-power valuations.  Thus a nonzero
shift can expose a prime from one exclusive residual order without exposing
it from the other.  This support does not collapse to generic ring
operations.

More exactly, assume `H>C`, and let `ell>Y>=max(U,C)` be a residual prime
with `ell` not dividing `H`.  The quotient menu captures `ell` if and only
if

\[
\boxed{
\min_{\substack{1\le u\le U\\u\ {m odd}}}
\left|uH\right|_\ell\le C,
}
\tag{5a}
\]

where `|z|_ell` is the least absolute residue modulo `ell`.  If `H` were
uniform in the nonzero residues modulo this fixed prime, a union bound would
give capture probability at most

\[
{2C\lceil U/2\rceil\over \ell-1}.
\tag{5b}
\]

This is not a distribution claim for the actual integer source.  It shows
that any advantage on an exponential residual prime must come from the
factor-correlated arithmetic of `H`, not from generic mixing.

The unshifted child adds no prime support beyond `u` and `H`.  In this branch
the F228 carry defect is

\[
E_{u,c}=cB.
\tag{6}
\]

If `|c|<=C<=Y`, every odd prime in a nonzero defect is already in the public
smooth bank through `Y`.  Hence the nonzero shifted quotient children, not
the defects or unshifted children, are the only new source in this menu.

## Lemma B — maximal saturating quotient word

Fix public numerical-QP bounds `Y,U,C` with `3<=Y`, `U<=Y`, and `C<=Y`.
Let

\[
\Lambda_Y=\operatorname{lcm}(1,\ldots,Y),\qquad U_Y=\Lambda_Y^n.
\]

After direct gcd screens, assume a recursive dispatcher supplies complete
factorizations of `H` and every positive `A_{u,c}` for odd `u<=U` and
`|c|<=C`.  Define

\[
W_Q=\operatorname{lcm}\!\left(
U_Y,
\operatorname{rad}(H)^n,
\left\{\operatorname{rad}(A_{u,c})^n\right\}_{u,c},
\left\{\operatorname{rad}(|E_{u,c}|)^n\right\}_{E_{u,c}\ne0}
\right).
\tag{7}
\]

The exponent `n` grants maximal saturation: every exposed prime occurs to
at least its full valuation in either residual order.  It introduces no new
prime support.  The word has numerical-QP logarithmic height and a
numerical-QP-size complete factor list.

Define

\[
r_p={s_p\over\gcd(s_p,W_Q)},\qquad
r_q={s_q\over\gcd(s_q,W_Q)}.
\tag{8}
\]

For a uniform unit `x mod N`, put

\[
a=x^{2^n}\pmod N,\qquad A=W_QH.
\tag{9}
\]

Then

\[
\Pr(a^A=1\bmod p)={1\over r_p},\qquad
\Pr(a^A=1\bmod q)={1\over r_q}.
\tag{10}
\]

If `M|D` is the accumulated common-order certificate, complete
factor-first processing has exact factor-or-growth probability

\[
\boxed{
{1\over r_p}+{1\over r_q}-{1\over r_pr_q}
-{1\over PQ}\sum_{d\mid M}\varphi(d)^2.
}
\tag{11}
\]

Thus the exact missing theorem for this source is an inverse-QP,
history-wise bound on (11), or a guarantee that one residual in (8) is
numerical-QP.  F232 does not assert either bound.

## Finite discovery question

Experiment D01 grants the maximal saturation in (7).  It measures how much
the shifted children reduce `(r_p,r_q)` beyond the smooth and `H`-supported
baseline.  It also evaluates (11) at `M=1` and at the hostile state `M=D`.
The source word uses only `N,n,B,H` and the complete factorizations of the
declared public children.  Hidden `p,q` are used only to build the frozen
corpus and to evaluate labels after the public word is complete.
