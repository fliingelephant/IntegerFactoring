# F275 V2 statement — canonical-carrier repair

## Status

This is a minimal additive repair to the frozen F275 V1 statement. V2 is a
proof-only candidate. It contains no computation, source code, or empirical
claim.

V2 incorporates the complete V1 statement at SHA-256

`4fa048b441cbb9e6177e3577ebbdd910d5e6555b5ee904ff7a184a2eecbbaa34`

except for the single replacement below. No other V1 definition, theorem,
scope boundary, or search disposition changes.

## Exact replacement after equation (8)

Replace the V1 paragraph

> where the bracket is the canonical unit in `[1,N)`. The edge row is below
> `N^2` and has supplied root `y`.

with the following paragraph:

> In the factor-blind construction (8), require the input carrier to be
> canonical: `1<=d<N`. The bracket `T_y(d)` is also the canonical unit in
> `[1,N)`. Hence the positive edge row satisfies
> 
> \[
>  1\le A=dT_y(d)\le(N-1)^2<N^2,
> \]
> 
> and it has supplied root `y`.

This extra bound applies only to the explicit construction (8).

## Unchanged general graph scope

The general graph setup before (6) is unchanged. Each graph carrier may be
any positive integer `d_v` with `gcd(d_v,N)=1`; it need not be below `N`.
For every edge, the exact row remains `A_e=d_ud_v`, and its supplied unit
root still satisfies

\[
 y_e^2\equiv d_ud_v\pmod N.
\]

Theorem A is unchanged. Its monomial pullback formula, structural-incidence
corollary, and direct alternative-root screen retain their V1 hypotheses and
conclusions.

Theorem B is unchanged. Its exact cycle square, alternating-label normalized
root, and two signed-gcd equalities hold for the general positive graph
carriers. Its proof does not use a carrier-size bound.

The unreduced and reduced complement-product boundary is unchanged. F270
remains outside the inherited-monomial obstruction for the reasons stated in
V1. V2 proves no result about F270.

## Exact exclusions

V2 does not impose `d_v<N` in the general graph theorem. It does not extend
the label-only formula to odd cycles. It proves no graph-carrier kernel
classification, canonical-section lower bound, event law, runtime law, or
factoring algorithm.
