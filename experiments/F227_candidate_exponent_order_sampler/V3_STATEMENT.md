# F227 V3 candidate — AP exponents do not rescue uniform order sampling

## Status and repair boundary

This is a self-audited proof-only V3 candidate. The V1 and V2 packets and
their hostile FAILs are preserved unchanged.

V1 omitted the definition of the input length and a uniform adaptive QP
envelope. V2 repaired that defect. Its hostile re-audit validated the AP
mean, the uniform adaptive probability obstruction, the fixed-base success
law, and the rough residual-order dichotomy. It rejected only V2 equation
(C4): that recurrence counted one useful transition as a complete current
node, omitted later same-size lcm-growth states, and did not multiply public
per-trial work by the expected trial count.

V3 changes only the conditional cost statement and proof. It separates:

1. one candidate trial;
2. one same-size progress state;
3. all strict lcm-growth states at the current integer; and
4. recursive complete factorization of the half-size candidate exponents.

No promotion is claimed.

## Complexity convention and fixed envelope

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

with fixed `C_*>0` and `k_*>=1`. The constants are enlarged once so that
this one function bounds every candidate-bank trial count, relative atom
bound, source cap `S(n)`, per-trial public cost, same-size state
initialization cost, terminal call, and verification cost below. They cannot
depend on an input, history, or stage. A later P161 roughness threshold may
be a separate larger fixed numerical-QP function.

An adaptive candidate bank is `Q`-diffuse when:

1. it uses at most `Q(n)` trials;
2. at every trial and every reachable no-progress history, its conditional
   law on the current `H` candidates has largest atom `eta` satisfying
   `eta H<=Q(n)`; and
3. after the candidate and all its public preprocessing are fixed, its base
   is conditionally independent and uniform in `(Z/NZ)^times`.

Here and below inline `Q(n)` denotes the fixed function `mathcal Q(n)` in
(Q2).

## Setup

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

The cell contains `p`. For `x in C`, set `A_x=x-1`. A trial may compute the
two direct gcds, recursively factor `A_x`, sample a fresh uniform unit
`a mod N`, compute `gcd(a^A_x-1,N)`, and on global return run sound
factor-first primary stripping. It is useful when it returns a proper factor
or certifies a primary block that strictly enlarges `L`.

The closest prior routes are P165/F187, which fixes exponent `N-1`, and
P194/F224, which samples the factor cell through Fermat and modified-AKS
values. F227 instead uses the recursively factored smaller exponent `x-1`.

## Theorem A — AP gcd mean

Let `m,c,L,H` be positive integers and

\[
A_j=c+jL\qquad(j_0\le j<j_0+H).
\tag{A1}
\]

For any probability law `mu` on these points, put

\[
\eta=\max_j\mu(j).
\tag{A2}
\]

Then

\[
\boxed{
\mathbb E_\mu\frac{\gcd(A_j,m)}m
\le
\eta\left(\frac{HL\tau(m)}m+1\right).
}
\tag{A3}
\]

For the uniform law,

\[
\boxed{
\frac1H\sum_j\frac{\gcd(A_j,m)}m
\le \frac{L\tau(m)}m+\frac1H.
}
\tag{A4}
\]

## Theorem B — one-trial bound and uniform adaptive obstruction

Let `mu` be a law on `C` with largest atom `eta`. Conditional on the chosen
candidate and its preprocessing, let the base be an independent uniform
unit. Then

\[
\boxed{
\Pr(\text{useful})
\le
\eta\left[
3+HL\left(
\frac{\tau(p-1)}{p-1}+
\frac{\tau(q-1)}{q-1}
\right)
\right].
}
\tag{B1}
\]

For a uniform candidate,

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

Exact rejection sampling of a uniform unit adds proper-factor mass

\[
\frac{p+q-2}{N-1}=O(1/p),
\tag{B3}
\]

which is smaller than the bound below.

Fix `1<=S(n)<=Q(n)`. In a nonterminal state

\[
L<\frac{N^{1/4}}{S(n)},
\tag{B4}
\]

one has `H=Theta(p/L)` with absolute constants. There are fixed constants
`c_0>0,n_0`, depending only on the fixed envelope, such that every law with
`eta H<=Q(n)` obeys, for `n>=n_0`,

\[
\boxed{
\Pr(\text{useful}\mid\text{fixed history})\le2^{-c_0n}.
}
\tag{B5}
\]

Consequently, any `Q`-diffuse adaptive bank whose only progress exits are
the declared per-trial screens has total useful probability at most

\[
\boxed{
Q(n)2^{-c_0n}=2^{-\Omega(n)}.
}
\tag{B6}
\]

The constants are uniform over inputs, histories, and stages. Factoring
`x-1` therefore does not rescue uniform or QP-diffuse candidates followed by
fresh uniform bases. The result does not cover heavy candidate atoms,
candidate/base coupling, integer-biased bases, or joint processing of
nonreturns.

## Theorem C — fixed-base progress and corrected complete-node cost

Fix a public unit `a mod N`, and write

\[
o_p=\operatorname{ord}_p(a),\qquad
o_q=\operatorname{ord}_q(a),\qquad
u_p=\frac{o_p}{\gcd(o_p,L)}.
\tag{C1}
\]

The base is stale at `L` when

\[
o_p=o_q\quad\text{and}\quad o_p\mid L.
\tag{C2}
\]

If the base is not stale, a uniform `x in C` followed by complete
factor-first stripping is useful with probability at least

\[
\boxed{
\frac{\lfloor H/u_p\rfloor}{H}
\ge\frac1{u_p}-\frac1H.
}
\tag{C3}
\]

If `u_p<=Q(n)` and `H>=2Q(n)`, one trial is useful with probability at
least `1/(2Q(n))`. If `H<2Q(n)`, direct enumeration finds `p` with fewer
than `2Q(n)` gcds.

For the conditional cost claim, suppose every nonterminal same-size state
receives a nonstale base with `u_p<=Q(n)`. Any cost of producing and
verifying that base is included in the public state cost below. Define

\[
J_N=\left\lceil\frac{N^{1/4}}{S(n)}\right\rceil,
\qquad
\Phi_N(L)=
\max\left\{0,
\left\lceil\log_2\frac{J_N}{L}\right\rceil
\right\}.
\tag{C4}
\]

Let `L_0` be the modulus at entry to the current integer and put

\[
R_N(L_0)=\Phi_N(L_0).
\tag{C5}
\]

Every useful nonfactor transition replaces `L` by a strict multiple
`lcm(L,c)>=2L`; a factor sets the potential to zero. Therefore the number of
same-size progress states is at most

\[
R_N(L_0)\le\lceil\log_2J_N\rceil=O(n).
\tag{C6}
\]

Let `F(n)` be a nondecreasing bound for the expected complete cost of the
conditional recursive routine on inputs of at most `n` bits. Let
`P_tr(n)` bound the nonrecursive public work in one candidate trial,
excluding the recursive factorization of `A_x`. Let `P_st(n)` bound the
one-time public work at one same-size state, including production and
verification of its supplied base. Let `G(n)` bound the final congruence
terminal and output verification. By the fixed-envelope convention,

\[
P_{\rm tr}(n),P_{\rm st}(n),G(n)\le Q(n).
\tag{C7}
\]

One progress state uses at most `2Q(n)` expected candidate trials. Each
trial invokes at most one complete factorization of an integer of at most
`n/2+O(1)` bits and incurs at most `P_tr(n)` public work. Hence

\[
\mathbb E[\text{one-state cost}]
\le
2Q(n)\left(F(n/2+C_0)+P_{\rm tr}(n)\right)
+P_{\rm st}(n)
\tag{C8}
\]

for one fixed absolute constant `C_0`. The small-cell enumeration branch
has no recursive candidate preprocessing and is also bounded by (C8).

Unrolling every same-size lcm-growth state before the terminal or a factor
gives the corrected complete-node recurrence

\[
\boxed{
F(n)
\le
R_N(L_0)\left[
2Q(n)F(n/2+C_0)
+2Q(n)P_{\rm tr}(n)
+P_{\rm st}(n)
\right]+G(n).
}
\tag{C9}
\]

Using (C6)--(C7),

\[
\boxed{
F(n)
\le
C_2nQ(n)F(n/2+C_0)
+C_2nQ(n)^2
}
\tag{C10}
\]

for one fixed `C_2`. This recurrence is numerical QP:

\[
F(n)\le2^{O((\log_2(n+1))^{K+1})},
\qquad K=\max\{1,k_*\}.
\tag{C11}
\]

Equations (C9)--(C10) count recursive candidate preprocessing once per
trial and public work once per trial. They also count all later same-size
aggregate-growth states. The conclusion remains conditional on the missing
nonstale-base source.

## Corollary D — no intermediate P161 rough residual regime

Let `T(n)>Q(n)` be a fixed integer-valued numerical-QP cap. If every prime
divisor of `o_p` exceeds `T(n)` and `u_p<=Q(n)`, then

\[
u_p=1,\qquad o_p\mid L.
\tag{D1}
\]

Thus a P161 rough unit has only two residual branches: its entire `p`-order
is already in `L`, or its residual order exceeds `T(n)`. The first branch
returns modulo `p` for every factor-cell exponent and factors or grows `L`
unless stale. The second branch gives no inverse-QP return bound.

## Exact remaining criterion

The positive source problem is still:

> At every nonterminal same-size history, produce with inverse-QP
> probability a public nonstale unit whose residual local order
> `ord_p(a)/gcd(ord_p(a),L)` is at most the one fixed envelope `Q(n)`.

Theorem C proves that this premise would give both progress and a complete
numerical-QP cost after all same-size growth stages and recursive candidate
factorizations are counted. It does not produce the premise and is not a
complete factoring algorithm.
