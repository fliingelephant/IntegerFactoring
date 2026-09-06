# F235 candidate — any unfactored word gives an exact Miller-amplified zero-defect law

## Status and scope

This is a proof-only conditional theorem for the balanced zero-defect branch.
It is not an all-input factoring algorithm.  It does not assert that a
quasipolynomial-height word saturating either residual always exists.

Let

\[
 N=pq,\qquad p<q<2p,
\]

where `p,q` are distinct odd primes.  Put

\[
 n=\lceil\log _2(N+1)\rceil,\quad
 B=2^{\lfloor n/2\rfloor},\quad
 H=(N-1)/B,
\]

and assume the zero-defect condition `B | N-1`.  Write

\[
 p-1=2^eP,\qquad q-1=2^fQ,
\]

with `P,Q` odd, and put

\[
 D=\gcd(P,Q),\qquad s_p=P/D,\qquad s_q=Q/D.
\]

Then `gcd(s_p,s_q)=1`, `gcd(H,P)=gcd(H,Q)=D`, and in fact

\[
 e=f\ge1.                                                    \tag{1}
\]

Let `W>=1` be any public integer whose binary length is numerical
quasipolynomial in `n`.  Its factorization is not supplied or required.
Define

\[
 E=(N-1)W=BH W,
\]

\[
 r_p={s_p\over\gcd(s_p,W)},\qquad
 r_q={s_q\over\gcd(s_q,W)},
\]

and

\[
 \alpha_p={1\over r_p},\qquad \alpha_q={1\over r_q}.
\]

## The exact trial

Choose `x` uniformly from the units modulo `N`.  Compute

\[
 g=\gcd(x^E-1,N).
\]

If `g` is proper, return it.  If `g=N`, write

\[
 E=2^v u,\qquad u\text{ odd},
\]

and run the standard Miller square chain from `x^u mod N`: test the gcds
with `N` of the square roots immediately before the first local value `1`.
Equivalently, test every displayed `gcd(z_i-1,N)` and `gcd(z_i+1,N)` for
`z_i=x^{2^iu}`.  Return only a verified proper gcd.  If no proper gcd
appears, declare this trial null and use a fresh unit.

The two local return events are independent and have exact probabilities

\[
 \Pr(x^E=1\bmod p)=\alpha_p,
 \qquad
 \Pr(x^E=1\bmod q)=\alpha_q.                         \tag{2}
\]

Let

\[
 \mu_e={2\over3}\left(1-4^{-e}\right).               \tag{3}
\]

Conditional on the global return `g=N`, the Miller chain returns a proper
factor with exact probability `mu_e`.  Consequently one complete trial
returns a factor with exact probability

\[
 \boxed{
  \alpha_p+\alpha_q-(2-\mu_e)\alpha_p\alpha_q .
 }                                                        \tag{4}
\]

Since `e>=1`,

\[
 \mu_e\ge {1\over2}.                                    \tag{5}
\]

Therefore, if `s_p | W` or `s_q | W`, every trial succeeds with probability
at least `1/2`.  Fresh trials then factor `N` almost surely in at most two
expected trials.  This conclusion includes the case in which both residuals
divide `W`.  A global return is useful through the Miller chain and is not
a stale common-order event.

No factor-first stripping is used.  In particular, no factorization of
`W`, `H`, or `E` is required.

## Two public word families

For a public integer `K>=1`, define

\[
 W_K=\prod_{k=1}^K(N^k-1).                               \tag{6}
\]

Let

\[
 t_p=\operatorname{ord}_{s_p}(N),\qquad
 t_q=\operatorname{ord}_{s_q}(N),                        \tag{7}
\]

where the order modulo `1` is defined to be `1`.  These orders exist because
`gcd(N,s_p)=gcd(N,s_q)=1`.  Then

\[
 t_p\le K\Longrightarrow s_p\mid W_K,
 \qquad
 t_q\le K\Longrightarrow s_q\mid W_K.                   \tag{8}
\]

Thus `min(t_p,t_q)<=K` gives factor probability at least `1/2` per trial.
The word has

\[
 \log_2 W_K< {nK(K+1)\over2}.                            \tag{9}
\]

More generally, let `A_1,...,A_J` be any public positive integers, for
example shifted zero-defect quotient children

\[
 A_{u,c}=uH+c.
\]

The unfactored word

\[
 W=\prod_{j=1}^J A_j^n                                  \tag{10}
\]

saturates the complete primary part of `s_p` or `s_q` supported on the
union of the child prime supports.  The children need not be factored.
If their total encoded length and count are numerical quasipolynomial, then
the word and the complete trial have numerical-quasipolynomial bit cost.

## Exact boundary

F235 removes the factored-word requirement and the recursive factorization
of `H` from the direct-factor branch of P202.  Its remaining source question
is exact:

\[
 \boxed{
 \text{construct a public QP-bit word }W
 \text{ with }s_p\mid W\text{ or }s_q\mid W
 \text{ on every zero-defect input.}
 }
\]

For the power word (6), this is the missing all-input bound
`min(t_p,t_q)=QP(n)`.  F235 does not prove that bound.  The identities

\[
 N\equiv q\equiv1+(q-p)\pmod {s_p},\qquad
 N\equiv p\equiv1-(q-p)\pmod {s_q}                       \tag{11}
\]

show the integer-specific coupling, but do not by themselves bound either
order.
