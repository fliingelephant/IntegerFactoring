# Gauss-weighted Salié/Cauchy sums retain a quadratic digit observable

**Family:** route:F31

**Status:** root-derived identities and exact finite checks. No fast mixed
Cauchy evaluator or factoring bound is promoted. The complete weighted sum
and the Cauchy-weighted sum must be distinguished.

## Sum the complete frequency before handling the window

Let m=2^k, k>=3, let gamma,d be odd, and put e_m(x)=exp(2*pi*i*x/m).
Define G_m(a)=sum_(x modm)e_m(a*x^2). For arbitrary integers w,V, define

    K_m(w,V)=sum_(b odd modm)G_m(b*gamma)
                              *e_m(-w^2/(b*gamma)+V*b).

Square completion gives

    G_m(b*gamma)*e_m(-w^2/(b*gamma))
       =sum_(x modm)e_m(b*gamma*x^2+2w*x).

The complete odd-b Ramanujan sum is m/2 at residue0, -m/2 at residue m/2,
and zero elsewhere. Therefore

    K_m(w,V)=(m/2)*[
       sum_(gamma*x^2+V=0 modm)e_m(2w*x)
       -sum_(gamma*x^2+V=m/2 modm)e_m(2w*x)].            (1)

This is a complete Gauss-weighted Salié evaluation. Singular square-root
sets are not enumerated: modulo powers of two they have at most four
arithmetic-progression descriptions after removing their valuation, or one
progression in the zero case. The additive sum on each progression is
geometric. Thus the bare complete sum has a polynomial-bit evaluation using
the usual power-of-two square-root rules. It has no retained sharp window.

## One Cauchy denominator changes the retained observable

Write epsilon_m(y)=+1 if y modm<m/2 and -1 otherwise. The exact odd-axis
identity from F295 is

    sum_(b odd modm)e_m(P*b)/(1-e_m(-b))=(m/4)*epsilon_m(P).

After the same square completion and the permutation b->d*b, this gives

    sum_(b odd modm)G_m(b*gamma)*e_m(-w^2/(b*gamma)+V*b)
                         /(1-e_m(-d*b))
      =(m/4)*sum_(x modm)e_m(2w*x)
                         *epsilon_m(d^(-1)*(gamma*x^2+V)).       (2)

Every original b is summed, and the linear Fourier phase in x is retained.
The remaining object is a Fourier transform of a *canonical quadratic
digit*. Replacing it by an unweighted quadratic-value histogram would lose
that phase.

For two denominators, let

    W_(a,m)(h)=#{0<=y<m/2:(a*y+h) modm<m/2}.

Its finite Fourier formula similarly yields

    sum_(b odd modm)G_m(b*gamma)*e_m(-w^2/(b*gamma)+V*b)
                    /((1-e_m(-d*b))*(1-e_m(-b)))
      =(m/4)*sum_(x modm)e_m(2w*x)
                         *[W_(-d,m)(gamma*x^2+V)-m/4].           (3)

Thus the global frequency can be removed exactly, but the position-sensitive
quadratic window survives. This agrees with the F295/F298 family, rather
than making P236's single quadratic-phase Cauchy theorem apply automatically.

## An exact parity filter, with its remaining core

For odd a and m>=16, put

    D_m(a,c,w)=sum_(x modm)e_m(2w*x)*epsilon_m(a*x^2+c).

The shift x->x+m/4 leaves the digit unchanged for even x and changes its
sign for odd x. Its Fourier multiplier is(-1)^w. Consequently, if w is odd,
only odd x contribute; if w is even, only even x contribute. This is exact
cancellation of one parity class, not a generic stationary-phase estimate.

In the even-w case, writing x=2y gives the explicit descent

    D_m(a,c,w)=2*D_(m/4)(a mod(m/4),floor(c/4),w/2).     (4)

The y domain initially contains two copies of the smaller period. In
particular w=0 reaches a fixed small modulus in logarithmically many steps.
For odd w, the surviving x=2y+1 term instead contains

    epsilon_(m/8)(a*y*(y+1)/2+floor((a+c)/8))

with its nontrivial Fourier phase. No efficient aggregate for that triangular
digit transform is provided here. The parity filter does not evaluate the
generic odd-frequency core.

## Relation to prior mechanisms and the full target

`SOURCE_LEADS.md` distinguishes the inspected complete Gauss/character
weighted Kloosterman evaluations from complete Fourier--Dedekind Cauchy sums.
Neither source class supplies their combination in(2)--(3). This is a scope
comparison, not a claim that these elementary identities are externally new.

`SCOPE_MAP.md` records another essential distinction: F294's original
inverse modulus is m^3, while q=m^2 is internal to one of m/2 odd-base
charts. Even summing all internal frequencies leaves the chart union and
the original factor-isolating windows. F299 subsequently identifies its
faithful residue-class method with exactly P235's affine cover.

F301 therefore supplies a public rectangle interface at the actual modulus
M approximately N. Its later ordinary rational-coordinate filters use a
different Cauchy kernel from(2): neither the exponential denominator above
nor P236 may be substituted for that new mixed resolvent without a proved
transformation.

## Exact computation

`salie_digits.py` works in Z[X]/(X^(m/2)+1) using integer coefficient arrays.
It checks72 complete identities(1),72 one-denominator identities(2), nine
two-denominator identities(3), and60 parity filters for m=8,...,256. All
parameters are retained, including zero/nonunit w and shifted V cases.
No floating-point root comparison is involved.

The run took0.081seconds and17,334,272bytes peak RSS, under a30-second
source alarm and35-second wrapper. The preflight reported73% available
memory, load2.25/2.11/2.03, and no numerical process. Source, sparse exact
coefficient output, log, and timeout status are retained. The reference
computation enumerates numerical ranges and is not an implementation of an
unproved fast weighted-sum algorithm.
