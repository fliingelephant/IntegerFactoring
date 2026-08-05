# F09: narrow obstruction for scalar higher-residue phase sieves

## Carrier class

Let `ell` be an odd prime and let `N=pq`, where the distinct primes `p,q` are
both `1 mod ell`.  Fix local order-`ell` characters

`chi_p(a)=zeta^{u_p(a)}` and `chi_q(a)=zeta^{u_q(a)}`,

so a unit has hidden phase vector `u(a)=(u_p(a),u_q(a))` in
`F_ell^2`.  The class considered here exposes scalar multiplicative
characters of this phase vector, does not orient the two rational factors,
allows multiplicative twists `a -> t*a^k`, and combines exposed labels only
by addition or subtraction.

## Theorem (diagonal-carrier obstruction)

Every factor-swap-invariant scalar character of `F_ell^2` has the form

`L_alpha(x,y)=alpha*(x+y)`.

Consequently, even the joint output of arbitrarily many such scalar
characters factors through the single quotient

`Sigma(x,y)=x+y`,

whose kernel is the anti-diagonal

`K={(t,-t): t in F_ell}`.

Multiplicative twists do not increase this rank: for `a -> t_j*a^k_j`, the
dependence on `a` is only `alpha_j*k_j*Sigma(u(a))`; the twist supplies an
additive constant `alpha_j*Sigma(u(t_j))`.  Any sequence of `+/-`
combinations and any postselection based on exposed labels still factors
through `Sigma`.  In particular, a zero exposed phase cannot certify that
both local phases are zero.

### Proof

A scalar character has exponent `L(x,y)=alpha*x+beta*y`.  Swap invariance for
all `(x,y)` says

`alpha*x+beta*y = alpha*y+beta*x`,

hence `alpha=beta`.  This proves the first claim and the common kernel claim.
The twist formula follows from multiplicativity of the local characters.
The combination claim follows by induction because `Sigma(u+/-v)` is
`Sigma(u)+/-Sigma(v)`.

## Exact cubic counterexample

Take `ell=3`, `N=91=7*13`, primitive roots `3 mod 7` and `2 mod 13`, and
reduce their discrete-log exponents modulo 3.  Exhaustive run F09-R04 gives:

- `a=15` has local pair `(0,1)`;
- `b=18` has local pair `(1,0)`;
- both expose the same global product exponent `1`;
- subtracting their carrier labels gives zero, but the local difference is
  `(2,1)`, so neither local phase vanishes;
- equivalently, `15/18 = 16 mod 91` has local pair `(2,1)` and global product
  one.

All nine local phase pairs occur.  Each of the three global-product fibers
contains 24 of the 72 units.  Thus the collapse is exact, not a sampling
artifact.

## What a globally defined higher symbol requires

Let `K=Q(zeta_ell)`.  If one defines a rational-denominator symbol by taking
the product over every prime ideal above a rational prime `p=1 mod ell`, then
for rational numerator `a` that product is trivial.  Indeed, if one local
symbol is `zeta^e`, its Galois conjugates are `zeta^{r*e}` for
`r in F_ell^*`, and their product is

`zeta^{e*sum_{r=1}^{ell-1} r}=1`

because `ell` is odd.  The quadratic case is exceptional because there is
only one nonzero Galois exponent.

To obtain a nontrivial odd-power symbol, one must instead select a prime ideal
above each rational prime.  For `ell=3`, this is an oriented ideal

`I=(N, zeta-rho)`

of norm `N`, where `rho` is a root of `Phi_3(X)=X^2+X+1 mod N`.  Thus the
nontrivial scalar symbol presupposes a cyclotomic ideal orientation; it is not
a canonical symbol of the rational integer `N` alone.

For `N=91`, F09-R04 finds four roots with CRT pairs

`(2,9), (2,3), (4,9), (4,3)`.

Globally conjugate orientations differ by a unit modulo both factors, but two
orientations that agree at exactly one CRT component factor `N` by
`gcd(rho-rho',N)`.  The observed nontrivial gcds are 7 and 13.  This proves
that access to multiple independent orientations can expose the factors.  It
does **not** prove that one orientation alone is rational-factoring-equivalent;
the exact claim is that a nontrivial evaluation requires cyclotomic ideal
selection beyond the input `N`.

## Scope

This closes only the scalar, multiplicative, factor-symmetric, diagonal
carrier with multiplicative twists and `+/-` combining.  It does not rule out
ring-valued CRT carriers, additive/nonmultiplicative probes, an explicitly
factor-oriented carrier, or higher-residue methods in general.
