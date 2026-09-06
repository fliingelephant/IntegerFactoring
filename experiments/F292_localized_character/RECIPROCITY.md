# F292: phase-sensitive Cochrane and inverse reciprocity

Status: exact author-derived transformations with finite certificates.
Independent reconstruction is pending. The attempted reciprocal evaluation
has no proved quasipolynomial cost contraction.

## The target is a Cochrane moment, with a primitive difference

Let M=2^k, k>=4, and r be the odd representative of N modulo M in(0,M).
Write b_q(u)=u/q-1/2 for canonical units0<u<q, and define

    Co(r,q)=sum_{u unit mod q} b_q(u)*b_q(r/u mod q).

This is exactly the Cochrane sum: changing variable u=a^(-1) matches
sum_a ((a^(-1)/q))((ra/q)). Primary-source provenance is Wang--Xu--Jia,
*On the generalized Cochrane sum with Dirichlet characters*, AIMS Mathematics
8(12),30182--30193(2023), DOI10.3934/math.20231542, definition on page30183.
[Primary PDF](https://www.aimspress.com/aimspress-data/math/2023/12/PDF/math-08-12-1542.pdf).
Its Lemma2.1 includes two Gauss factors for the generalized character moment;
the lemma is stated for an odd prime, not for our dyadic modulus. It is used
to identify the correct object and phase, not to import a dyadic theorem.
The full text is retained at`.knowledge/10-3934-math-20231542.md`, citation key
`wang_2023_generalized`, with provenance in
`reference_cochrane_2023/SOURCE_MANIFEST.json`. The same official helper
succeeded on one retry after its first HTTP502 response.

Let epsilon_q(u)=1 when0<u<q/2 and-1 whenq/2<u<q, and put

    H_M(r)=sum_{u unit mod M} epsilon_M(u)*epsilon_M(r/u mod M).

The exact relation is

    H_M(r)=16*Co(r,M)-8*Co(r,M/2).

Indeed epsilon_M(u)=2*b_(M/2)(u mod M/2)-4*b_M(u). In the product expansion,
the lower/lower term sums to2*Co(r,M/2). Each mixed term sums toCo(r,M/2),
because b_M(v)+b_M(v+M/2 mod M)=b_(M/2)(v mod M/2). This proves the formula.

If B(chi)=-(1/M)sum_u u*chi(u), multiplicative orthogonality gives

    Co(r,M)=(1/phi(M))sum_{chi odd mod M} B(chi)^2*bar(chi(r)).

The square has no conjugation. The characters induced from M/2 contribute
Co(r,M/2)/2: their B values are unchanged and phi(M)=2*phi(M/2). Subtracting
them gives exactly the root's primitive-odd formula for H. The half-square
count is C_M(r)=M/8+H_M(r)/4.

## Preserve the Gauss phase through the functional equation

For a primitive odd character, the Bernoulli Fourier series gives

    B(chi)=tau(chi)*L(1,bar chi)/(pi*i).

For example, inserting
b(x)=-(1/(2*pi*i))sum_{n!=0}exp(2*pi*i*n*x)/n and pairing n with-n proves
this directly. Consequently

    H_M(r)=-16/(pi^2*phi(M))
       *sum_{chi primitive odd} tau(chi)^2*L(1,bar chi)^2*bar(chi(r)).

The root-number phase is tau(chi)^2, not its absolute square. Define the
unnormalized complete Kloosterman sum

    Kl_M(z)=sum_{a unit mod M} exp(2*pi*i*(a+z/a)/M).

An exact orthogonality identity is

    sum_{chi primitive odd} tau(chi)^2*bar(chi(z))
      =phi(M)/2*(Kl_M(z)-Kl_M(-z)),                  (z odd).

To prove it, first sum over all odd characters and expand the two Gauss sums.
Odd-character orthogonality imposes ab=z or ab=-z, with opposite signs.
Every imprimitive character's Gauss sum at M is zero: pairing a with a+M/2
cancels it. Thus the primitive restriction gives the same answer.

Expanding the squared Dirichlet series then yields the phase-sensitive dual

    H_M(r)=-(8/pi^2)sum_{n odd>=1} d(n)/n
                           *(Kl_M(r*n)-Kl_M(-r*n)).

The series can be understood by taking the limit from real s>1 in the
corresponding n^(-s) series. Ordinary convergence at1 also follows by the
Dirichlet hyperbola decomposition: for each nonprincipal character modulo M,
the summatory function of chi(n)*d(n) is O_M(sqrt(x)), since partial sums of
chi are bounded. This identifies the exact dual; it supplies no efficient
truncation bound uniform in M.

There are two Gauss factors here. Replacing them by a single additive twist
or an absolute-square moment changes the object. Applying an Estermann
reciprocity formula to individual additive twists after expanding Kl_M
still leaves a sum over the unit a. No compression of that sum has been
established in this attempt.

## An actual inverse-reciprocal map, with every boundary term

Before consulting the above source, the attempted reciprocal map was the
elementary inverse identity. For each odd1<=u<M/2, define canonical residues

    v=r*u^(-1) mod M, w=r*M^(-1) mod u.

For u=1, use w=0. Then exactly

    v=(r-M*w)/u+M*1_{w>0}.

This integer lies in(0,M) and has uv=r mod M. Equivalently, it is additive
inverse reciprocity with the integer representative correction retained.

When w>0, the lower-half condition v<M/2 is

    2*M*w > M*u+2*r.

Since u is odd, it is w>u/2 for r<M/2. For r>M/2 it is the same condition
with w=(u+1)/2 excluded. The w=0 case contributes precisely the divisors
u of r with1<=u<M/2 and2r<M*u.

Define the genuinely smaller-modulus sum

    U_M(r)=sum_{u odd<M/2} 1_{(r*M^(-1) mod u)>u/2}.

Writing d for the ordinary positive divisor-count function, the exact
half-square formula is

    C_M(r)=U_M(r)+d(r),                         r<M/2;
    C_M(r)=U_M(r)+d(r)-d(r-M/2)-1,             r>M/2.

For the first line, every divisor of r is in the allowed range. For the
second, the w=0 contribution is d(r)-2: remove1 and r. The excluded midpoint
w=(u+1)/2 is equivalent, for odd u>=3, to u|(r-M/2). Its contribution is
d(r-M/2)-1, because r-M/2 is positive, odd, and below M/2. These facts prove
the displayed boundary terms, including u=1. No divisor term is assumed
cheap: computing it would be additional work.

## The same map retains the short cap

Suppose the actual cap coordinates are below M and N=r+M*Q. For odd x in
its public coordinate range, use w=r*M^(-1) mod x and the same formula for y.
Its exact product is

    x*y=r                         if w=0;
    x*y=r+M*(x-w)                if w>0.

Thus xy>=N and ax+by<=T become, for w>0,

    Q <= x-w <= (T*x-a*x^2-b*r)/(b*M).

The strict cap bound T^2<4ab(N+M) makes the integer interval contain onlyQ,
when nonempty. This is the transformed geometry, not a completed sum. The
parameter Q is small for the specified choice of M, but the relation
r+M*Q=xy retains the original coefficient N. A constant product-level range
does not make the remaining x-sum small.

## Checked parameter and cost accounting

The reciprocal modulus u is strictly smaller than M/2 in the half-square
map. However, there are exactly M/4 distinct calls, even when r=1. Therefore
literal evaluation has an exponential-in-log(M) number of calls; it is not
a Euclidean recurrence on a bounded set of decreasing parameter pairs.
Memoizing equal moduli does not reduce that first level, because they are all
different. This is a cost statement about the displayed implementation only.

For the balanced short caps, the public x-range has O(sqrt(M)) entries.
The reciprocal map preserves that many smaller-modulus calls. The pilot
contains no aggregation that contracts their count. This is the exact point
where the constructive reciprocity attempt currently stops. Neither the
complete Kloosterman dual nor the explicit divisor boundary terms resolve it.

## Exact evidence

`reciprocal_boundaries.py` checked48768 pointwise reciprocal identities,
195 half-square formulas,123 Cochrane-difference formulas, and62 short caps
(including the retained two equal-histogram caps). The seeded half-square
family uses seed2922610, with exhaustive small moduli and random larger cases
through M=4096. It also cross-checked27 existing F293 counts at r=1,3,5 through
M=4096. It did not regenerate the large F293 sequence.

`gauss_square_kernel.py` checked20 exact cyclotomic Gauss-square kernel
identities at M=16,32,64,128. Coefficients were reduced modulo
z^(M/2)+1, so the checks retain phases and do not use floating-point equality.

Both programs retain source, JSON certificates, and logs. Each has an explicit
30-second timeout and estimated peak memory below64MiB. The resource snapshot
reported load2.04/2.03/2.02,73% free memory and no swap; approved same-command
process inspection showed one Apple process using one core. The boundary
pilot took0.034seconds. These finite checks do not certify an asymptotic
speedup or an independently verified theorem.
