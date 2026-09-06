# F231 candidate — QP-bit smooth exponent words close the smooth residual zero-defect state

## Status and boundary

This is a self-audited proof-only favorable-state theorem.  It strengthens
F230 in two ways.  The multiplier can have enormous numerical value as
long as its binary bit length and complete factor list have numerical-QP
size, and the complete
factor-first outcome has an exact stale-return formula.  It is not an
all-input factoring algorithm.

Let

\[
N=pq,
\qquad p<q<2p,
\qquad n=\lceil\log_2(N+1)\rceil,
\qquad B=2^{\lfloor n/2\rfloor},
\]

where `p` and `q` are distinct odd primes.  Work in the F230 zero-defect
branch

\[
B\mid N-1,
\qquad H={N-1\over B}.
\tag{1}
\]

Assume that a correct recursive dispatcher has supplied the complete
factorization of the public half-size integer `H`.  Put

\[
P=(p-1)_{\rm odd},
\qquad Q=(q-1)_{\rm odd},
\qquad D=\gcd(P,Q),
\]

\[
s_p={P\over D},
\qquad s_q={Q\over D}.
\tag{2}
\]

Then

\[
\gcd(s_p,s_q)=1,
\qquad
\gcd(H,P)=\gcd(H,Q)=D.
\tag{3}
\]

Maintain an odd certified common divisor `M|D`.  It is the lcm of primary
blocks obtained from any number of earlier, unrelated witnesses.  No one
witness is assumed to have order `M`.

## Theorem A — arbitrary factored-word return and exact stale law

Let `W` be any public completely factored positive integer and define

\[
r_p(W)={s_p\over\gcd(s_p,W)},
\qquad
r_q(W)={s_q\over\gcd(s_q,W)}.
\tag{4}
\]

Both are odd, and

\[
\gcd(r_p(W),r_q(W))=1.
\]

Choose `x` uniformly from the units modulo `N` and put

\[
a=x^{2^n}\pmod N,
\qquad A=WH.
\tag{5}
\]

The two coordinates of `a` are independent and uniform in the odd-order
subgroups of orders `P` and `Q`.  Their exact return probabilities are

\[
\Pr(a^A=1\bmod p)={1\over r_p(W)},
\qquad
\Pr(a^A=1\bmod q)={1\over r_q(W)}.
\tag{6}
\]

Run the initial gcd `gcd(a^A-1,N)`.  On a global return, use the complete
factorization of `A` to strip redundant prime powers.  Return a factor if
the two local orders differ.  Otherwise obtain their exact common order
and add all of its primary blocks to `M`.  A common order already dividing
`M` is stale and is not a stopping event.

Conditional on the sampled unit, the exact probability of a factor or
strict lcm growth is

\[
\boxed{
\begin{aligned}
\Pr(\text{factor or }M\text{-growth})
=\;&{1\over r_p(W)}+{1\over r_q(W)}
-{1\over r_p(W)r_q(W)}\\
&-{1\over PQ}\sum_{d\mid M}\varphi(d)^2.
\end{aligned}}
\tag{7}
\]

The last term is exactly the stale-global-return probability.  Formula
(7) includes arbitrary prime powers in `P`, `Q`, `D`, `M`, and `W`.

A sample may instead be uniform in `1,...,N-1`.  Screen `gcd(x,N)` first.
A nonunit is already a factor, and conditioning on a unit gives (7).

The stale term satisfies

\[
{1\over PQ}\sum_{d\mid M}\varphi(d)^2
\le {M^2\over PQ}
=\left({M\over D}\right)^2{1\over s_ps_q}.
\tag{8}
\]

If both residuals in (4) exceed one, the direct-factor probability alone is

\[
{1\over r_p}+{1\over r_q}-{2\over r_pr_q}
\ge {1\over\min(r_p,r_q)}.
\tag{9}
\]

## Theorem B — one smooth hidden residual gives constant Las Vegas progress

Fix a public integer `Y>=3`.  Let

\[
\Lambda_Y=\operatorname{lcm}(1,\ldots,Y),
\qquad
U_Y=\Lambda_Y^n.
\tag{10}
\]

The power `n` is essential for the stated arbitrary-prime-power result.
The unpowered `Lambda_Y` need not contain a high power of a small prime.
Every integer below `N` whose prime divisors are at most `Y` divides
`U_Y`.

Suppose at least one of `s_p,s_q` is `Y`-smooth, with no bound on its
numerical value or its prime-power exponents.  Equivalently,

\[
r_p(U_Y)=1
\quad\hbox{or}\quad
r_q(U_Y)=1.
\tag{11}
\]

The case `s_p=s_q=1` is impossible under the balanced zero-defect
hypotheses.  Indeed, it would force equal odd parts `P=Q=D`; balance then
forces the two-primary exponents of `p-1` and `q-1` to be consecutive,
which contradicts `B|N-1`.  Therefore

\[
s_ps_q>1.
\tag{12}
\]

Use `W=U_Y` in Theorem A.  At every history, one stage returns a factor or
strictly enlarges `M` with probability at least

\[
\boxed{1-{1\over s_ps_q}\ge {2\over3}.}
\tag{13}
\]

This bound does not need a terminal-capacity assumption.  Once `M=D`, every
useful event in (13) is a factor.  Repeating fresh stages factors `N` almost
surely in at most `3n/2` expected stages: before the factor there are fewer
than `n` strict lcm-growth events.

If a beta-two carry supplies `p mod 2^t`, let

\[
J=\left\lceil{N^{1/4}\over S_0(n)}\right\rceil
\]

for a fixed positive numerical-QP function `S_0`.  After every certified
growth, update

\[
L=\operatorname{lcm}(2^t,M).
\tag{14}
\]

If `L>=J`, the known-residue terminal factors immediately.  If this never
happens first, the repeated smooth-word stage itself factors with the stated
expected bound.  Thus the certificate lcm and beta-two residue compose
without requiring a single common-order generator or any terminal-capacity
hypothesis.

This is a Las Vegas numerical-QP theorem for the declared favorable state,
conditional on the correct half-size factorization of `H`.  It does not
supply an all-input dispatcher or prove that (11) holds for every input.

The factorization of `H` gives a strictly stronger integer-specific word at
negligible extra asymptotic cost.  Define

\[
\widehat U_Y
=U_Y\prod_{\substack{\ell\mid H\\\ell>Y}}\ell^n.
\tag{15}
\]

Then Theorem B remains valid under the broader condition that every prime
divisor of at least one of `s_p,s_q` either is at most `Y` or divides `H`.
The surviving residuals are exactly

\[
\widehat r_p
=\prod_{\substack{\ell\mid s_p\\\ell>Y,\ \ell\nmid H}}
\ell^{v_\ell(s_p)},
\qquad
\widehat r_q
=\prod_{\substack{\ell\mid s_q\\\ell>Y,\ \ell\nmid H}}
\ell^{v_\ell(s_q)}.
\tag{16}
\]

This uses actual integer information from the recursively factored child.
It is stronger than a generic small-prime filter.  It still need not make
either residual one.

## Theorem C — QP encoding and accumulation of multiplier words

If `Y` is bounded by one fixed numerical-QP function, both the binary length
and the complete factor-list size of `U_Y` are numerical-QP:

\[
\log_2 U_Y=n\log_2\Lambda_Y
\le n\log_2(Y!)
\le nY\log_2Y.
\tag{17}
\]

A sieve through `Y` constructs its factorization.  The exponent `U_YH` has
numerical-QP bit length, so all modular powers and all factor-first
punctures have numerical-QP bit cost.  Its binary exponent, or its equivalent
factored powering schedule, contains only numerical-QP many bits.  No
super-QP string or list indexed by the numerical value of `U_Y` is
materialized.

The extra child-supported word in (15) costs only

\[
\log_2\prod_{\ell\mid H}\ell^n
=n\log_2\operatorname{rad}(H)
\le n\log_2H=O(n^2).
\tag{18}
\]

More generally, let `W_1,...,W_k` be completely factored words whose count,
factor-list size, and total logarithmic height

\[
\sum_i\log_2 W_i
\]

are numerical-QP.  Their public lcm

\[
W_*=\operatorname{lcm}(W_1,\ldots,W_k)
\tag{19}
\]

has logarithmic height at most the displayed sum and also has a completely
factored numerical-QP-size list.  Theorem A applies
with `W_*`.  Thus separate word sources can absorb different primary parts
of a hidden residual.  This aggregation cannot reduce the useful-event
probability:

\[
\Pr_{W_*}(\text{factor or growth})
\ge \Pr_{W_i}(\text{factor or growth})
\qquad(1\le i\le k).
\tag{20}
\]

Their only canonical aggregate effect is the lcm in (19).

Once a word makes returns frequent, unrelated projected bases can certify
different common primary blocks.  Their lcm enlarges `M` exactly as in
P197.  No single projected base needs exact order `M`.  The words themselves
do not certify `M`; they only change the return kernels.

## Theorem D — exact rough residual boundary

For `W=U_Y`, equations (4) become

\[
r_p=\prod_{\substack{\ell\mid s_p\\\ell>Y}}
\ell^{v_\ell(s_p)},
\qquad
r_q=\prod_{\substack{\ell\mid s_q\\\ell>Y}}
\ell^{v_\ell(s_q)}.
\tag{21}
\]

Hence each residual is either one or has least prime divisor greater than
`Y`.  If both are nontrivial, one projected test has exact direct-factor
probability from (9), while every factor or common-order certificate from
the declared return-and-puncture decoder is bounded above by

\[
{1\over r_p}+{1\over r_q}.
\tag{22}
\]

Thus the uniform projected source is exponentially sparse on any family
where both residuals are `2^{Omega(n)}`.  Roughness alone does not imply
this sparsity: a `Y`-rough residual can still have numerical-QP size.

This normalization is the same primary-support operation as P161.  P161
guarantees nontrivial rough local orders on its surviving branch; it does
not force either residual in (21) to become one or numerical-QP-sized.

The smallest missing factored-word source statement for the uniform
projected decoder is now exact.  At each unresolved history, produce or
accumulate a completely factored
word `W` of numerical-QP logarithmic height and factor-list size for which

\[
\min(r_p(W),r_q(W))
\]

is bounded by one fixed numerical-QP function.  The special case `r_p=1`
or `r_q=1` is Theorem B.  For a nonuniform or carry-correlated base, the
necessary replacement is inverse-QP probability of exactly one local
return or of a nonstale global return.  One-coordinate identity mass alone
is insufficient because all of it can lie on the joint stale atom.  Neither
P161 roughness nor aggregate lcm bookkeeping supplies either
integer-specific source.
