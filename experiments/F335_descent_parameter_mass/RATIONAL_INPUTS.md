# Short rational inputs have an explicit count profile

**Family:** route:F31

Status: separate author-derived mechanism. Not part of STATEMENT_ONLY.md,
not independently reconstructed, and not a factor-success theorem. No
external novelty claim. The uniform-source obstruction does not cover this
cheaply generated biased input family.

## Exact periodic case

Let N>1 be odd, h=(N-1)/2, 1<=b<N, gcd(b,N)=1, and a=b^(-1) mod N.
Write b*a=1+c*N. Then gcd(c,b)=1. For 1<=y<=h,

    Q membership at y
      iff c*y mod b <= floor((b-1)/2).

Indeed a*y/N has fractional part
(c*y mod b)/b+y/(b*N), and 0<y/N<1/2. This gives the stated threshold,
including the even-b midpoint. Hence the sign word is periodic modulo b:

    Q_a(t)=ceil(b/2)*floor(t/b)
        +#{1<=v<=t mod b: c*v mod b<=floor((b-1)/2)}.

For odd b the main smaller-child ratio is (b-1)/(2b), rather than 1/2.
The b=3 case has a ternary main scale, and b=5 has ratio 2/5. For even b
the main ratio is 1/2 and only a bounded periodic defect remains. A large
continued-fraction digit sum by itself therefore does not specify what
the count dynamics will do: a small multiplier and its small-inverse
partner have the same digit sum but quite different descent profiles.

## A triangular-wave profile for r/b

Assume positive integers r,b satisfy

    1<=r<N, 1<=b<N, gcd(r,b)=gcd(r*b,N)=1.

Set a=r*b^(-1) mod N, represented in 1,...,N-1, and define

    T(s)=min({s},1-{s}),
    F_{r,b}(x)=x/2                         if b is even,
    F_{r,b}(x)=x/2+T(r*x)/(2*b*r)         if b is odd,
    f_{r,b}(x)=x-F_{r,b}(x),  0<=x<=1/2.

The author claim is the uniform deterministic bound

    |Q_a(t)-N*F_{r,b}(t/N)|<=B,
    B=4*(b+r),  0<=t<=h.

No hidden factor enters F, f, or the public input a. The constant is
conservative; it is not an empirically fitted error.

Write b*a=c*N+r. Since gcd(c,b)=1, splitting y into its b residue classes
permutes the phases j/b, 0<=j<b. In the class with phase j, the relevant
indicator at u=y/N is

    1_{0< fractional(j/b+r*u/b)<1/2}.

Its accepted set in 0<u<=x is a union of at most floor(r*x/b)+2 intervals.
Counting the arithmetic progression y/N in one such interval differs
from N/b times its length by at most two. Summing b classes gives error
at most r+4b<=B. The sum of the b continuous indicators equals b/2 almost
everywhere if b is even. If b is odd it equals

    b/2+(1/2)*sign(1/2-fractional(r*u))

almost everywhere. Integrating from zero gives exactly the displayed F,
since the integral of this alternating sign is T(r*x)/r. Endpoint
equalities affect the finite error bound and have measure zero in the
integral; actual orbit points cannot be zero or N/2.

## Public orbit windows, with controlled rounding

The ideal smaller child is N*f(t/N). The function min(q,t-q) is
one-Lipschitz in q, so the same B bounds its one-step error.

For even b, f and F have Lipschitz constant 1/2. For odd b>=3, both
functions have Lipschitz constant

    lambda=(b+1)/(2*b)<=2/3.

Let x_0=1/2 and x_{j+1}=f(x_j), and run the literal fixed-h count descent
until it stops. The initial error is |h-N*x_0|=1/2. Induction gives

    |t_j-N*x_j|<=1/2+B/(1-lambda).

The two screened children lie within the same radius of N*F(x_j) and
N*f(x_j). Thus radius 1+3B suffices for all even b and all odd b>=3.
The whole literal descent selects from O((b+r)*log N) public candidate
integers near this rational orbit. Directly screening those orbit windows
is the appropriate control; a biased parameter choice is not by itself
an extra success mechanism.

The ideal map also has only a short non-geometric prefix. On writing
z=r*x, its odd-b version is

    z' = z/2-T(z)/(2b).

After O(log(r+1)) steps z<1/2, after which
z'=(b-1)*z/(2b) exactly. This does not make the remaining number of
discrete factor screens small; it gives their explicit main locations.

The b=1 case has Lipschitz constant one and can have flat pieces. Its
small-multiplier behavior is covered separately by the exact residual
bound in STATEMENT_ONLY.md. Negative signed r can be reduced to positive
r by negating a, which swaps the two counts.

## A discriminating next experiment

Use publicly generated coprime r,b of small magnitude, form a=r/b mod N,
and compare the actual count descent against the whole radius-(1+3B)
orbit menu. Retain numerator r, denominator b, parity of b, the full
factor-generation cost, count cost, gcd cost, and every failure. Compare
with the uniform-source F334 control on the same public inputs. Use input
factors only as offline labels. Work at factor sizes substantially above
the menu radius; small moduli where each wide window necessarily contains
a factor do not discriminate the mechanism.

No such performance experiment is claimed in this note. The open
constructive question is whether a cheap distribution of these rational
orbits, or a different count source, has a useful per-N hitting law after
charging its direct candidate windows.
