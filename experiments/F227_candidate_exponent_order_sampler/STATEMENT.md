# F227 candidate — AP exponents do not rescue uniform order sampling

## Status and novelty boundary

This is a self-audited proof-only candidate. It studies one Las Vegas source
for the beta-two residue plus aggregate-order framework.

The closest prior routes are P165/F187 and P194/F224. P165 fixes the exponent
`N-1` and samples uniform bases. P194 samples the certified factor arithmetic
progression, but tests modified-AKS values and Fermat midpoints. The mechanism
here is materially different: a sampled factor candidate `x` supplies the
smaller exponent `A=x-1`; `A` is completely factored recursively; and a return
of a unit modulo the hidden factors is used either to split `N` or to certify
new common primary support.

The negative result below grants the complete factorization of every sampled
`A`. Thus recursive preprocessing does not repair the probability bound.

## Setup

Let

\[
N=pq,\qquad p<q<2p,
\]

where `p,q` are distinct odd primes. Define

\[
I_N=[\lceil\sqrt{N/2}\rceil,\lfloor\sqrt N\rfloor]\cap\mathbb Z.
\]

Suppose a certified beta-two plus aggregate state gives an even integer
`L>=2` and a residue `s mod L` such that

\[
\gcd(L,N)=1,\qquad p\equiv s\pmod L.
\]

Put

\[
\mathcal C=\{x\in I_N:x\equiv s\pmod L\},\qquad H=|\mathcal C|.
\]

For `x in C`, set `A_x=x-1`. A trial may do the following.

1. Compute `gcd(x,N)` and `gcd(A_x,N)`.
2. Obtain the complete certified factorization of `A_x`, even by a free
   oracle for purposes of the probability upper bound.
3. Sample a fresh uniform unit `a mod N`.
4. Compute `gcd(a^A_x-1,N)`. On a global return, run arbitrary sound
   factor-first primary stripping using the known factorization of `A_x`.

A trial is useful if it returns a proper factor or certifies a primary block
which strictly enlarges the current modulus `L`.

## Theorem A — AP gcd mean

Let `m,c,L,H` be positive integers, and let

\[
A_j=c+jL\qquad(j_0\le j<j_0+H).
\]

Let `mu` be any probability law on these `H` points, and let

\[
\eta=\max_j\mu(j).
\]

Then

\[
\boxed{
\mathbb E_\mu\frac{\gcd(A_j,m)}m
\le
\eta\left(\frac{HL\tau(m)}m+1\right),
}
\]

where `tau(m)` is the divisor-counting function. In particular, under the
uniform law,

\[
\boxed{
\frac1H\sum_j\frac{\gcd(A_j,m)}m
\le \frac{L\tau(m)}m+\frac1H.
}
\]

## Theorem B — diffuse candidate laws give exponentially sparse progress

Let `mu` be a law on `C` with largest atom `eta`. Conditional on every chosen
`x` and all its public preprocessing, let `a` be a fresh uniform unit modulo
`N`. Then the useful-event probability is at most

\[
\boxed{
\eta\left[
3+HL\left(
\frac{\tau(p-1)}{p-1}+
\frac{\tau(q-1)}{q-1}
\right)
\right].
}
\]

For the uniform candidate law this becomes

\[
\boxed{
\Pr(\text{useful})
\le
\frac3H+
\frac{L\tau(p-1)}{p-1}+
\frac{L\tau(q-1)}{q-1}.
}
\]

Fix any numerical-QP function `S(n)>=1`. In a nonterminal state

\[
L<\frac{N^{1/4}}{S(n)},
\]

one has `H=Theta(p/L)`. Since `tau(m)=m^{o(1)}`, every law satisfying

\[
\eta H\le 2^{(\log n)^{O(1)}}
\]

has

\[
\boxed{
\Pr(\text{useful})\le p^{-1/2+o(1)}=2^{-\Omega(n)}.
}
\]

The same conditional estimate applies at each adaptive stage whose fresh
candidate law remains QP-diffuse and whose base is fresh uniform. A
numerical-QP bank therefore has total useful probability only
`2^(-Omega(n))` before another mechanism changes the state.

Thus recursively factoring `x-1` does not turn a uniform, or merely
QP-diffuse, factor-cell draw followed by a uniform base into the missing
inverse-QP drift source. This obstruction is gap-independent. It also holds
when the AP-Fermat terminal is unavailable in the large-gap branch.

## Theorem C — exact positive criterion for an integer-specific base

Fix a public unit `a mod N`, and write

\[
o_p=\operatorname{ord}_p(a),\qquad
o_q=\operatorname{ord}_q(a),\qquad
u_p=\frac{o_p}{\gcd(o_p,L)}.
\]

Call the base stale at `L` when

\[
o_p=o_q\quad\text{and}\quad o_p\mid L.
\]

If the base is not stale, then a uniform `x in C`, followed by complete
factor-first stripping of `A_x`, is useful with probability at least

\[
\boxed{
\frac{\lfloor H/u_p\rfloor}{H}
\ge \frac1{u_p}-\frac1H.
}
\]

In particular, if `u_p<=Q(n)` for a numerical-QP function `Q` and
`H>=2Q(n)`, the progress probability is at least `1/(2Q(n))`. If
`H<2Q(n)`, direct enumeration of `C` finds `p` with numerical-QP many gcds.
The recursive factorizations of the `A_x`, each of at most half the input
bit length, preserve a numerical-QP recurrence.

## Corollary D — the P161 rough branch has no intermediate residual regime

Suppose every prime divisor of `o_p` is greater than a chosen QP cap `T`.
If `Q<T` and `u_p<=Q`, then necessarily

\[
u_p=1,\qquad o_p\mid L.
\]

Thus for a P161-normalized rough unit, the fixed-base criterion has only two
branches at scale `T`: either its entire `p`-side order is already contained
in `L`, in which case every factor-cell exponent returns modulo `p`, or its
residual order is greater than `T`. In the first branch one trial factors or
grows `L` unless the base is stale. In the second branch Theorem C supplies
no inverse-QP return bound.

## Exact remaining criterion

The AP-exponent mechanism reduces the positive source problem to this
specific condition:

> Produce, on every nonterminal history and with inverse-QP probability, a
> public nonstale unit whose residual local order
> `ord_p(a)/gcd(ord_p(a),L)` is numerical QP.

The factorization of `x-1` certifies progress after a return. It does not
make the return likely. Theorems A and B show that a fresh uniform base does
not satisfy the criterion. Corollary D shows that P161 rough-order
normalization does not create a hidden intermediate return scale. P164's
long-action branch does not imply the criterion either. Nonuniform integer
bases, heavy candidate laws derived from the factorization pattern of
`x-1`, joint processing of nonreturns, and other smaller exponent families
remain outside this result.
