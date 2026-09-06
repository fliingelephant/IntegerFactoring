# F231 hostile audit

## Verdict

**FAIL.** The return-kernel algebra, stale law, smooth-word bounds,
constants, stage bound, child-supported enrichment, and lcm monotonicity
survive hostile reconstruction. However, the final claimed exact missing
source statement is false as written.

## Decisive objection

The last paragraph of Theorem D offers, as a sufficient alternative, a
carry-correlated base with inverse-QP identity mass in one residual cyclic
group. One-coordinate identity mass is not useful-event mass when the two
coordinates may be correlated. All of that mass can lie on simultaneous
stale returns.

For example, use the admissible F230/F231 state

\[
N=2881=43\cdot67,
\qquad (P,Q,D,s_p,s_q)=(21,33,3,7,11),
\]

and let the proposed correlated source output `a=1 mod N` with probability
one. It has identity mass one in each residual coordinate, hence certainly
inverse-QP identity mass in one coordinate. Nevertheless, every test is a
global return of exact common order one. Since `1|M` for every maintained
state, every such return is stale. The factor-or-growth probability is
zero.

Thus the stated alternative does not imply the P197 drift condition. It
must require inverse-QP conditional probability of exactly one local
return or a nonstale global return, equivalently inverse-QP probability of
a verified factor or strict `M`-growth. Another sufficient formulation is
one-coordinate identity mass together with an explicit upper bound on the
joint stale atom. Identity mass alone is insufficient.

This objection also invalidates the provenance claim that the remaining
source gap has been characterized exactly. It does not invalidate
equations (4)--(22) or the factored-word favorable theorem.

## Checks that passed

1. From `gcd(H,P)=D`, primewise valuation gives
   `gcd(WH,P)=D gcd(W,s_p)=P/r_p`, including primes shared by `D` and
   `s_p`. The symmetric formula holds at `q`. Since the two residuals
   divide coprime `s_p,s_q`, they are coprime.
2. Complete divisor stripping is exhaustive for the declared decoder.
   Exactly one initial return factors. Neither return makes every divisor
   puncture useless. On a global return, unequal local order valuations
   factor, while equal valuations recover the exact common order.
3. A stale sample is exactly `o_p=o_q=d` for some `d|M`. As `M|D|H`, all
   such pairs return globally. Independence and the exact-order count in a
   cyclic group give

   \[
   {1\over PQ}\sum_{d\mid M}\varphi(d)^2.
   \]

   This term is independent of `W`, so equation (7) and lcm monotonicity
   (20) are correct.
4. The bounds `sum phi(d)^2 <= M^2`, `s_ps_q>=3`, and `D/M>=3` give the
   stated `2/3` and `8/9` constants. Strict growth of odd `M` multiplies it,
   and hence `lcm(2^t,M)`, by at least three. There are fewer than `n`
   useful events before a factor or terminal state, so the `3n/2` expected
   stage bound follows from the history-wise `2/3` bound.
5. `Lambda_Y^n` contains every prime power occurring in any integer below
   `N` whose prime support is at most `Y`: each relevant valuation is less
   than `n`, while every prime `ell<=Y` occurs in `Lambda_Y^n` to valuation
   at least `n`. Equations (11) and (21) follow.
6. The factorization of `H` exposes its prime support without hidden-factor
   access. Multiplying each listed prime to exponent `n` removes precisely
   the additional residual primaries stated in (16), at logarithmic cost
   at most `n log_2 H=O(n^2)`.
7. A numerical-QP bound on the numerical value of `Y` makes the sieve,
   factor list, logarithmic height `O(nY log Y)`, modular powers, and all
   punctures numerical-QP in bit complexity. Lcm aggregation takes maximum
   listed valuations and has height and list size bounded by the input
   totals.
8. The beta-two terminal is used only conditionally. The packet does not
   claim an all-input dispatcher, and the factorization of the half-size
   public child `H` is an explicit assumption.

## The suggested equal-group edge case

The apparent case `s_p=s_q=1` with `M=D` is not itself a counterexample
inside the declared balanced zero-defect domain. In fact that hidden state
is impossible. If `P=Q=D`, write

\[
p=2^eD+1,
\qquad q=2^fD+1.
\]

The inequalities `p<q<2p` force `f=e+1`. Hence

\[
v_2(N-1)
=v_2\!\left(2^eD(2^{e+1}D+3)\right)=e.
\]

But `N>2^{2e+1}` implies
`floor(n/2)>=e+1`, contradicting `2^{floor(n/2)}|N-1`.
Consequently, the packet's separate `s_p=s_q=1` assertions are vacuous
under its own opening hypotheses. A degenerate qualifier would be needed
if the final source sentence were exported to a broader setting, but it is
not the reason for this verdict.

## Candidate-input authentication

The audited SHA-256 hashes are:

| File | SHA-256 |
|---|---|
| `STATEMENT.md` | `3da8d99937bc792021f79486d53753c5f8d114cd7544ce73cf0a927253748fd3` |
| `PROOF.md` | `d6d366974b71b006e3d27420b0a2b34b7ede9d7b3674e2722532970f8c92ff75` |
| `SELF_AUDIT.md` | `fb88991b048ae8777ef4281846716996265e3a1f1447425ffa1bc113d490eb33` |
| `PROVENANCE.md` | `e325ff3fbb6fa905d417ef7d2385cd0828137347610af6d7c2df802df9c61db3` |

I modified none of those four candidate inputs. I used no web search or
numerical experiment.
