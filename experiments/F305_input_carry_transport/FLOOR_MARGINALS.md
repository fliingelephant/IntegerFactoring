# Polynomial-time reciprocal-power floor marginals

**Scope:** M=2^k, k>=3, odd0<N<M, integer d, and odd w in an ordinary
integer interval. The needed quantities are

    R1*(N,d)=sum_w w^(-1)*floor((N*w-d)/M) mod2M,
    R2(N,d)=sum_w w^(-2)*floor((N*w-d)/M)^2 mod2M.       (1)

The inverse powers are2-adic rational residues. These sums have an explicit
polynomial-bit evaluator. It does not enumerate w and does not integrate
the unknown carry measure from REPORT.md.

## Reciprocal-power expansion has a uniform integral remainder

Write w=a+4x with a=1 or3, restricting x to the required interval. For
inverse degree s=1 or2,

    w^(-s)=sum_{l=0}^{h}(-1)^l*binom(s+l-1,l)
                     *4^l*a^(-s-l)*x^l mod2^P,
    h=floor((P-1)/2).

Every omitted term has a factor4^l and an integral binomial coefficient.
It vanishes modulo2^P uniformly for every integer x. Multiplication by an
integer floor value, or its square, preserves this congruence. For(1),
P=k+1 and the polynomial degree is O(k).

It remains to compute polynomially weighted ordinary floor sums. The
following recurrence is used by the implementation, with exact rational
Faulhaber coefficients rather than modular division of those coefficients.

## Degree-preserving Euclidean recurrence

Define

    F_(p,q)(n,m,a,b)=sum_{x=0}^{n-1}x^p*floor((a*x+b)/m)^q,
    S_p(n)=sum_{x=0}^{n-1}x^p.

For q=0 use S_p(n). Reduce a=A*m+a0, b=B*m+b0, with0<=a0,b0<m. Expand
(A*x+B+floor((a0*x+b0)/m))^q by the binomial theorem. Every resulting
moment has total degree at most p+q and uses the same reduced geometry.

For0<a<m,0<=b<m, put H=floor((a*(n-1)+b)/m). Summing by levels gives

    F_(p,q)=S_p(n)*H^q
      -sum_{j=0}^{H-1}((j+1)^q-j^q)
                         *S_p(floor((m*j+m-b+a-1)/a)). (2)

Expand the two polynomials in(2). If
S_p(y)=sum_s c_(p,s)*y^s, then the second term is

    sum_{l=0}^{q-1}sum_s binom(q,l)*c_(p,s)
                         *F_(l,s)(H,a,m,m-b+a-1).

Its total degree is at most(q-1)+(p+1)=p+q, and the modulus decreases
from m to a. Negative original b is handled by the initial quotient B.
There is no assumption that the original floor values are positive.

For one initial geometry, the normalized child geometry is independent of
p,q. Memoizing the complete degree-D bank therefore uses O(D^2 log m)
states and O(D^4 log m) rational arithmetic operations. For the physical
range0<N<M,|d|<=M, the floor values and transformed index ranges are O(M).
Faulhaber coefficients have a common denominator dividing(D+1)! and
O(D log(D+1))-bit numerators. The exact arithmetic therefore uses
O(D*(k+log(D+1))) bits per operand, up to absolute constants. Standard
integer arithmetic gives a polynomial bit bound from these stated counts.
For arbitrary signed d, add its binary length to the operand bound; the
Euclidean state count is unchanged.
The coefficient bound follows, for example, from
S_p(n)=sum_{j=0}^p StirlingSecond(p,j)*n^(falling j+1)/(j+1),
whose factors have O(D log(D+1))-bit coefficients.

In(1), D=floor(k/2)+2. The implementation uses exact Fractions and asserts
that every returned floor moment is an integer. No modular division of a
Faulhaber denominator is used. This supplies polynomial bit complexity
for the two uniform marginals, including signed initial intercepts.

The same routine evaluates reciprocal prefixes and the first-power
reciprocal-square marginals used by the reflection identity. An arbitrary
interval is the difference of two prefixes; the two progressions may have
different lengths.

## Implementation evidence

`input_transport.py` computes the bank with inverse degrees0,1,2 and floor
powers0,1,2. It checks450 such values against small direct sums. The small
N=1,d=floor(M/3) controls exercise negative initial intercepts a*N-d.
The large runs enumerate no units:

| k | N | d | Cached Euclidean states | Total degree | Largest returned integer bits | Seconds |
|---:|---:|---:|---:|---:|---:|---:|
|24|5904339|12345|6306|14|328|0.096|
|32|1511510961|123456789|15442|18|567|0.36|

The final source, exact outputs and log are retained. An initial prototype
accidentally converted a leading Faulhaber coefficient to a binary float;
its assertion failure is in `input_transport_setup.log`. It was repaired
by constructing that coefficient as Fraction(1). No mathematical recurrence
was changed and no alternate evaluation workflow was substituted.

This is a computable marginal, not a claim that all ordinary or
carry-weighted floor sums are polynomial-time evaluable.
