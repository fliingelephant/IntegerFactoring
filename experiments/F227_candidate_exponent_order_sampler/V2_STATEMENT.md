# F227 V2 candidate — AP exponents do not rescue uniform order sampling

## Status and repair boundary

This is a self-audited proof-only V2 candidate. The V1 packet is preserved
unchanged. Its hostile audit returned **FAIL** for one formal defect: V1 used
`n`, numerical QP, and QP-diffuse adaptive laws without defining them or
binding one uniform envelope over all histories. The audit found no defect in
the AP estimate, probability bound, fixed-base progression, nonstale
classification, or rough-residual dichotomy.

V2 repairs only that quantifier defect. It defines the input length and fixes
one numerical-QP envelope for every adaptive law and stage. No promotion is
claimed.

## Complexity convention and one uniform adaptive envelope

Throughout,

\[
n=\left\lceil\log_2(N+1)\right\rceil.
\tag{Q0}
\]

A numerical-QP function is bounded above by

\[
2^{C(\log_2(n+1))^k}
\tag{Q1}
\]

for fixed constants `C>0` and `k>=1`, independent of `N`, its hidden
factors, the random history, and the stage.

Fix once and for all

\[
\mathcal Q(n)=2^{C_*(\log_2(n+1))^{k_*}}
\tag{Q2}
\]

with fixed `C_*>0` and `k_*>=1`. Enlarge these two fixed constants once, if
necessary, so that `Q` dominates the candidate-bank trial counts, relative
atom bounds, `S(n)`, and per-stage public arithmetic costs below. The
constants are thereafter fixed; they cannot depend on an input or an
adaptive history. The later roughness threshold `T(n)` may be a separate,
larger fixed numerical-QP function.

An adaptive candidate bank is called `Q`-diffuse precisely when:

1. it uses at most `Q(n)` trials;
2. at every trial and for every reachable history before the first useful
   event, its conditional candidate law has largest atom `eta` satisfying
   `eta H<=Q(n)`; and
3. after the candidate and all its public preprocessing have been fixed, the
   trial base is conditionally independent and uniform in
   `(Z/NZ)^times`.

The same function `Q` applies to every item, input, history, and stage.

## Setup and novelty boundary

Let

\[
N=pq,\qquad p<q<2p,
\tag{S1}
\]

where `p,q` are distinct odd primes. Define

\[
I_N=[\lceil\sqrt{N/2}\rceil,\lfloor\sqrt N\rfloor]\cap\mathbb Z.
\tag{S2}
\]

Suppose a certified beta-two plus aggregate state gives an even integer
`L>=2` and a residue `s mod L` such that

\[
\gcd(L,N)=1,\qquad p\equiv s\pmod L.
\tag{S3}
\]

Put

\[
\mathcal C=\{x\in I_N:x\equiv s\pmod L\},\qquad H=|\mathcal C|.
\tag{S4}
\]

The cell is nonempty because it contains `p`. For `x in C`, set
`A_x=x-1`. A trial may do the following.

1. Compute `gcd(x,N)` and `gcd(A_x,N)`.
2. Obtain the complete certified factorization of `A_x`, even by a free
   oracle for purposes of the probability upper bound.
3. Sample a fresh uniform unit `a mod N`.
4. Compute `gcd(a^A_x-1,N)`. On a global return, run arbitrary sound
   factor-first primary stripping using the known factorization of `A_x`.

A trial is useful if it returns a proper factor or certifies a primary block
which strictly enlarges the current modulus `L`.

The closest prior routes are P165/F187 and P194/F224. P165 fixes the exponent
`N-1` and samples uniform bases. P194 samples the certified factor arithmetic
progression, but tests modified-AKS values and Fermat midpoints. Here a sampled
factor candidate supplies the smaller exponent `x-1`; that exponent is
factored recursively; and a return is used to split `N` or certify common
primary support.

## Theorem A — AP gcd mean

Let `m,c,L,H` be positive integers, and let

\[
A_j=c+jL\qquad(j_0\le j<j_0+H).
\tag{A1}
\]

Let `mu` be any probability law on these `H` points, and let

\[
\eta=\max_j\mu(j).
\tag{A2}
\]

Then

\[
\boxed{
\mathbb E_\mu\frac{\gcd(A_j,m)}m
\le
\eta\left(\frac{HL\tau(m)}m+1\right),
}
\tag{A3}
\]

where `tau(m)` is the divisor-counting function. In particular, under the
uniform law,

\[
\boxed{
\frac1H\sum_j\frac{\gcd(A_j,m)}m
\le \frac{L\tau(m)}m+\frac1H.
}
\tag{A4}
\]

## Theorem B — one-trial bound and uniform adaptive obstruction

Let `mu` be a law on `C` with largest atom `eta`. Conditional on the chosen
`x` and all its public preprocessing, let `a` be an independent uniform unit
modulo `N`. Then the useful-event probability is at most

\[
\boxed{
\eta\left[
3+HL\left(
\frac{\tau(p-1)}{p-1}+
\frac{\tau(q-1)}{q-1}
\right)
\right].
}
\tag{B1}
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
\tag{B2}
\]

If the uniform unit is implemented by drawing uniform residues and
gcd-screening, the probability of obtaining a proper factor before an
accepted unit is

\[
\frac{p+q-2}{N-1}=O(1/p).
\tag{B2a}
\]

This additional useful mass is smaller than the bound below and does not
change its asymptotic conclusion.

Fix a positive function `S(n)>=1` bounded by `Q(n)`. In a nonterminal state

\[
L<\frac{N^{1/4}}{S(n)},
\tag{B3}
\]

one has `H=Theta(p/L)`, with absolute implied constants for all sufficiently
large `N`. There are constants `c_0>0` and `n_0`, depending only on the fixed
envelope `Q`, such that every conditional law satisfying

\[
\eta H\le\mathcal Q(n)
\tag{B4}
\]

obeys, for `n>=n_0`,

\[
\boxed{
\Pr(\text{useful}\mid\text{the fixed history})
\le 2^{-c_0n}.
}
\tag{B5}
\]

Consequently, for `n>=n_0`, any `Q`-diffuse adaptive bank whose only
progress exits are the declared per-trial screens, including the optional
unit-sampling gcd screen, has

\[
\boxed{
\Pr(\text{some useful trial before another mechanism changes the state})
\le \mathcal Q(n)2^{-c_0n}=2^{-\Omega(n)}.
}
\tag{B6}
\]

The constants in the final `Omega` are uniform over all inputs, histories,
and stages. Thus recursively factoring `x-1` does not turn a uniform, or
`Q`-diffuse, factor-cell draw followed by a fresh uniform base into the
missing inverse-QP drift source. The obstruction is gap-independent and
also covers the large-gap branch where the AP-Fermat terminal is unavailable.

## Theorem C — exact positive criterion for an integer-specific base

Fix a public unit `a mod N`, and write

\[
o_p=\operatorname{ord}_p(a),\qquad
o_q=\operatorname{ord}_q(a),\qquad
u_p=\frac{o_p}{\gcd(o_p,L)}.
\tag{C1}
\]

Call the base stale at `L` when

\[
o_p=o_q\quad\text{and}\quad o_p\mid L.
\tag{C2}
\]

If the base is not stale, then a uniform `x in C`, followed by complete
factor-first stripping of `A_x`, is useful with probability at least

\[
\boxed{
\frac{\lfloor H/u_p\rfloor}{H}
\ge \frac1{u_p}-\frac1H.
}
\tag{C3}
\]

In particular, if `u_p<=Q(n)` and `H>=2Q(n)`, the progress probability is
at least `1/(2Q(n))`. If `H<2Q(n)`, direct enumeration of `C` finds `p`
with fewer than `2Q(n)` gcds.

If such a nonstale fixed base is supplied at every recursive node, the
expected number of recursively factored children `A_x` per node is
`O(Q(n))`. Each child has at most `n/2+O(1)` bits, so the recurrence

\[
T(n)\le O(\mathcal Q(n))T(n/2+O(1))+\mathcal Q(n)
\tag{C4}
\]

is numerical QP. This is a conditional cost statement, not a construction
of the required base.

## Corollary D — the P161 rough branch has no intermediate residual regime

Let `T(n)>Q(n)` be a fixed integer-valued numerical-QP cap. Suppose every
prime divisor of `o_p` is greater than `T(n)`. If `u_p<=Q(n)`, then

\[
u_p=1,\qquad o_p\mid L.
\tag{D1}
\]

Thus a P161-normalized rough unit has only two branches at the fixed scale:
either its entire `p`-side order is already contained in `L`, in which case
every factor-cell exponent returns modulo `p`, or its residual order is
greater than `T(n)`. In the first branch one trial factors or grows `L`
unless the base is stale. In the second branch Theorem C supplies no
inverse-QP return bound.

## Exact remaining criterion

The AP-exponent mechanism reduces the positive source problem to this
specific condition:

> On every nonterminal history, produce with inverse-QP probability a public
> nonstale unit whose residual local order
> `ord_p(a)/gcd(ord_p(a),L)` is at most the one fixed envelope `Q(n)`.

Factoring `x-1` certifies progress after a return; it does not make the
return likely. Theorems A and B show that fresh uniform bases do not satisfy
the criterion. Corollary D shows that P161 rough-order normalization creates
no intermediate QP residual scale. P164's long-action branch does not imply
the criterion. Nonuniform integer bases, heavy candidate laws, joint
processing of nonreturns, and other smaller exponent families remain outside
this result.
