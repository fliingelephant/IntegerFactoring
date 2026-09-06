# F227 V5 candidate — AP exponent sampling, with an explicit all-input oracle boundary

## Status and repair boundary

This is a self-audited proof-only V5 candidate. V1, V2, V3, V4, and their
four hostile FAILs are preserved unchanged.

V4's hostile re-audit passed every substantive argument but rejected the
frozen statement of (B6): it asserted an equality instead of the proved
upper bound. V5 changes only that claim. It restores “at most” and the
inequality in (B6). The proof is mathematically unchanged.

V3's probability, fixed-base, same-size potential, and geometric-cost
calculations survived hostile review. Its failure was a promise-closure
error: a candidate exponent `x-1` is an arbitrary even integer, not another
distinct odd balanced semiprime. V4 and V5 therefore make the child factorer
an explicit all-input oracle. V5 states no self-recursive factoring
recurrence and no complete numerical-QP factoring algorithm.

## Complexity convention and one fixed envelope

Let

\[
n=\left\lceil\log_2(N+1)\right\rceil.
\tag{Q0}
\]

A numerical-QP function is bounded by

\[
2^{C(\log_2(n+1))^k}
\tag{Q1}
\]

for fixed constants `C>0` and `k>=1`. Fix one such integer-valued envelope

\[
Q(n)=\left\lceil2^{C_*(\log_2(n+1))^{k_*}}\right\rceil,
\tag{Q2}
\]

enlarged once to bound every declared candidate-bank size, relative atom
bound, source cap, and public cost below. It is uniform over inputs,
histories, and stages.

An adaptive candidate bank is `Q`-diffuse when:

1. it makes at most `Q(n)` trials;
2. at each trial and each reachable no-progress history, the largest
   conditional candidate atom `eta` satisfies `eta H<=Q(n)`; and
3. after the candidate and its public preprocessing are fixed, the base is
   conditionally independent and uniform in `(Z/NZ)^times`.

## Balanced factor-cell setup

Let

\[
N=pq,\qquad p<q<2p,
\tag{S1}
\]

where `p,q` are distinct odd primes, and define

\[
I_N=[\lceil\sqrt{N/2}\rceil,\lfloor\sqrt N\rfloor]\cap\mathbb Z.
\tag{S2}
\]

Suppose a certified beta-two plus aggregate state supplies an even integer
`L>=2` and a residue `s mod L` such that

\[
\gcd(L,N)=1,\qquad p\equiv s\pmod L.
\tag{S3}
\]

Put

\[
\mathcal C=\{x\in I_N:x\equiv s\pmod L\},\qquad H=|\mathcal C|,
\qquad A_x=x-1.
\tag{S4}
\]

The cell contains `p`. A declared trial may test direct gcds, obtain the
complete prime factorization of `A_x`, compute a return gcd
`gcd(a^{A_x}-1,N)`, and use factor-first stripping. A trial is useful when
it returns a proper factor or certifies a common primary block whose lcm
strictly enlarges `L`.

## Theorem A — AP gcd mean

Let `m,c,L,H` be positive integers and

\[
A_j=c+jL\qquad(j_0\le j<j_0+H).
\tag{A1}
\]

For any probability law `mu` on these points, let

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

## Theorem B — diffuse candidates plus fresh uniform bases are sparse

Let `mu` be a law on `C` with largest atom `eta`. Conditional on the chosen
candidate and its preprocessing, let the base be an independent uniform
unit modulo `N`. Then

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
\frac{p+q-2}{N-1}=O(1/p).
\tag{B3}
\]

Fix an integer-valued `1<=S(n)<=Q(n)`. In a nonterminal state

\[
L<\frac{N^{1/4}}{S(n)},
\tag{B4}
\]

there are fixed constants `c_0>0,n_0`, depending only on the fixed
envelope, such that every law with `eta H<=Q(n)` satisfies, for `n>=n_0`,

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
\Pr(\text{at least one useful trial})
\le Q(n)2^{-c_0n}=2^{-\Omega(n)}.
}
\tag{B6}
\]

This obstruction grants complete factorizations of all candidate exponents.
It does not cover heavy candidate atoms, candidate/base coupling,
integer-biased bases, or joint processing of nonreturns.

## Theorem C — fixed-base progress and oracle-relative current-node cost

Fix a public unit `a mod N`, and write

\[
o_p=\operatorname{ord}_p(a),\qquad
o_q=\operatorname{ord}_q(a),\qquad
u_p=\frac{o_p}{\gcd(o_p,L)}.
\tag{C1}
\]

The base is stale at `L` exactly in the declared channel when

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

Thus, if `u_p<=Q(n)` and `H>=2Q(n)`, one trial is useful with probability
at least `1/(2Q(n))`. If `H<2Q(n)`, direct enumeration finds `p` with fewer
than `2Q(n)` gcds.

For the cost statement, let `FactorAll` be an external Las Vegas oracle that
correctly factors every positive integer and uses fresh internal randomness
on each call. Let `F_all(m)` be a nondecreasing uniform bound on its expected
cost for every input of at most `m` bits, including every conditional
history. F227 neither constructs nor bounds this oracle.

Suppose each nonterminal same-size state receives a nonstale base satisfying
`u_p<=Q(n)`. Include the full acquisition and verification cost of that base
in `P_st(n)`. Define

\[
J_N=\left\lceil\frac{N^{1/4}}{S(n)}\right\rceil,
\qquad
\Phi_N(L)=
\max\left\{0,\left\lceil\log_2\frac{J_N}{L}\right\rceil\right\},
\tag{C4}
\]

and put

\[
R_N(L_0)=\Phi_N(L_0).
\tag{C5}
\]

Every useful nonfactor update replaces `L` by a strict multiple
`lcm(L,c)>=2L`. Therefore the number of same-size progress states is at
most

\[
\boxed{
R_N(L_0)\le\lceil\log_2J_N\rceil=O(n).
}
\tag{C6}
\]

Let `P_tr(n)` bound nonoracle public work in one candidate trial. Let
`P_st(n)` bound one-time public work at one same-size state. Let `G(n)`
bound the terminal and output verification. Assume

\[
P_{\rm tr}(n),P_{\rm st}(n),G(n)\le Q(n).
\tag{C7}
\]

For one absolute constant `C_0`, one progress state has expected cost at
most

\[
2Q(n)\left(F_{\rm all}(n/2+C_0)+P_{\rm tr}(n)\right)
+P_{\rm st}(n).
\tag{C8}
\]

The geometric reach-tail proof of (C8) does not assume independence between
a trial's success and its cost. Summing all same-size states gives the
oracle-relative balanced-node bound

\[
\boxed{
\begin{aligned}
\mathbb E[\operatorname{NodeCost}(N,L_0;\mathrm{FactorAll})]
\le R_N(L_0)\bigl[&2Q(n)F_{\rm all}(n/2+C_0)\\
&+2Q(n)P_{\rm tr}(n)+P_{\rm st}(n)\bigr]+G(n).
\end{aligned}
}
\tag{C9}
\]

This is not a recurrence for `F_all`. The children `A_x` are arbitrary even
integers, and the F227 balanced-semiprime transition is not an all-input
dispatcher.

## Corollary D — P161 rough residual dichotomy

Let `T(n)>Q(n)` be a fixed integer-valued numerical-QP cap. On the named
P161 rough-descendant branch, suppose every prime divisor of `o_p` exceeds
`T(n)`. Then

\[
u_p=1\quad\text{or}\quad u_p>T(n).
\tag{D1}
\]

In particular, `u_p<=Q(n)` forces

\[
u_p=1,\qquad o_p\mid L.
\tag{D2}
\]

Every factor-cell exponent then returns modulo `p`, so the fixed base
factors or grows `L` unless it is stale. P161 does not supply a nonstale
base and does not supply `FactorAll`.

## Exact remaining gaps

Two independent gaps remain.

1. **Source gap.** At every nonterminal same-size history, produce with
   certified inverse-QP probability a public nonstale unit whose residual
   local order is at most one fixed QP envelope. A randomized source also
   needs capped batching or another recognizable-success argument.
2. **Dispatch gap.** Correctly factor every arbitrary child `A_x=x-1` with
   a uniform all-input cost bound. F227 supplies only the oracle-relative
   call count in (C9).

No numerical-QP recursion or complete factoring theorem is claimed.
