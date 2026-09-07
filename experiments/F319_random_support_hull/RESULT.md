# F319: random support normals, divisor fan mass, and adaptive proposal cost

**Family:** route:F31

Family: route:F31. Status: the normal-cone inequality and discrete probability
bound are independently reconstructed in P244, with composite N explicit
for the probability claim. The source-based support implementation and
adaptive experiments remain outside that promotion. This is a
randomized verified-divisor generator with an elementary
O(N^(1/3)*poly(log N)) expected bound, not the quasipolynomial target.

## Material difference and source check

The question is whether random integer support queries and product-residual
feedback can discover a divisor with a useful cost/success ratio. Neither
exact counting nor hull enumeration is required as an algorithmic interface.

The closest prior is C247 and F288_integer_hyperbola_support, inspected via
the Rust reader and its RESULT/LITERATURE packets. F288 already establishes
that every unboxed support vertex is a strict fixed point of its own normal,
records nonfactor local defect minima, and derives a support reduction from
SEEK/NEXT. Thus self-normal descent is not retried here. The new work is an
implemented exact support query, an explicit discrete random proposal, a
per-divisor logarithmic fan-width bound, and actual adaptive first-hit tests.

The source is Alcantara, Blanco, Criado, Santos, *On the convex hull of
integer points above the hyperbola*, arXiv:2501.19193v1. Its cached original
full text was checked at Theorem 3.10/Algorithm 2, Proposition 3.12,
Corollary 3.13, Theorem 3.14, Lemmas 3.15--3.16, and Remark 1.6.
The public arXiv page still lists v1 on 2026-09-07:
https://arxiv.org/abs/2501.19193.
Balog--Barany arXiv:2602.06897 still lists v1. Its global hull-size theorem
is context, not a probability assumption or an oracle in this construction.
https://arxiv.org/abs/2602.06897.
No external novelty claim is made.

## A concrete exact support operation

Let S_N={(x,y) in Z^2: x,y>0, xy>=N}. Its finite lower vertex chain lies
in [1,N]^2. For a,b>0, SUPPORT(N,a,b) returns a vertex minimizing ax+by.
Tied face endpoints are compared by product; either endpoint is acceptable
when their products agree. A true hyperbola point cannot be an interior
point of such an edge because the hyperbola is strictly convex.

support.py implements the following operations using integers only.

1. RAYCAST computes the first nonnegative integer step at which membership
   changes on a lattice ray. Substitute the ray into xy-N, find the floors
   of its at most two quadratic roots with integer square roots, and test
   nearby integers by exact positive-coordinate/product membership.
2. NEXTPT is ABCS Algorithm 2 for the standard lattice basis (1,0),(0,1).
   It alternately updates inside/outside primitive directions by RAYCAST.
   Theorem 3.10 supplies O(log N) arithmetic operations. On an existing
   hull vertex it returns the next vertex, or the terminal ray.
3. SEEK starts at (t,ceil(N/t)). Make bit_length(N)+2 forward NEXTPT calls,
   or stop at the rightmost vertex. Corollary 3.13 guarantees that the final
   finite point is a global vertex. Reverse NEXTPT by swapping coordinates
   until the previous vertex has x<t. This returns the first global vertex
   with x>=t. There are O(log N) forward and reverse calls.
4. Binary-search the integer x range [1,N]. At t, obtain V=SEEK(t) and its
   successor W. The sign of a(W_x-V_x)+b(W_y-V_y) determines whether to
   search right of V or below t. Always retain the best visited vertex.
   In the latter case there are no vertices between t and V, and V is
   retained, so no optimum is lost. A zero sign returns optimal endpoints.
   If W is absent, retain V and search below t.

Convexity makes the edge-objective signs monotone. Each coordinate-search
round halves its integer range. This is O(log^3 N) arithmetic operations,
independent of the number of hull vertices. The standard lattice has no
rational-translation exception near an asymptote: all y coordinates are
integers. No box truncation or lattice-coset union is used.

ABCS Remark 1.6 explicitly converts its rational arithmetic algorithms to
the bit model. Here geometric inputs/intermediates have O(log N) bits;
dot products also include the bit lengths of a,b. For the proposal normals
below these are O(log N). A conservative schoolbook bound of O(n^6) bit
operations per SUPPORT includes integer root/division work and all nested
calls, where n=bit_length(N). Memory is polynomial in n. The bounded
simulation uses a precomputed hull only to accelerate repeated trials;
support.py itself never constructs that hull.

## Exact factor cone endpoints and a uniform width theorem

Let P=(p,q) be a nontrivial factor point, pq=N and p,q>=2. Let its adjacent
vertices be P_L=(p-h,q+k) and P_R=(p+H,q-K), with h,H,k,K positive integers.
The exact normal interval for unique exposure is

    lambda_minus=K/H < lambda=a/b < k/h=lambda_plus.       (1)

Equivalently the lower endpoint is the maximum of

    floor(q*H/(p+H))/H,  1<=H<=N-p,

and the upper endpoint is the minimum of

    ceil(q*h/(p-h))/h,  1<=h<p.

These formula ranges are characterizations, not enumeration instructions.
Once P is known, two NEXT calls give its actual adjacent endpoints quickly.

**Claim.** With r=lambda_plus/lambda_minus, every such point satisfies

    N*(r-1)^3 >= 4.                                      (2)

Proof: put lambda0=q/p, u=lambda_plus-lambda0>0, and
v=lambda0-lambda_minus>0. Neighbor feasibility gives

    h <= p*u/lambda_plus,
    H <= p*v/lambda_minus.

Because the two endpoint slopes are distinct lattice rationals,

    u+v=(k*H-K*h)/(h*H) >= 1/(h*H).

Combining them gives (u+v)*u*v >= lambda_plus*lambda_minus/p^2.
Set A=u/lambda0 and B=v/lambda0. Then 0<B<1 and

    (A+B)*A*B/((1+A)*(1-B)) >= 1/N.

Also r-1=(A+B)/(1-B), so the left side equals
(r-1)*A*B/(1+A). Since A*B <= (A+B)^2/4 and A+B<=r-1,
it is at most (r-1)^3/4. This proves (2).

In particular the logarithmic angular width is at least
log(1+(4/N)^(1/3)), uniformly for every nontrivial divisor point. This is
stronger than merely knowing that factors are vertices. It supplies a
probability bound for every input, not an average-case hull heuristic.
It does not imply quasipolynomial mass. Literal Euclidean angular mass is
also retained in the finite output, but is not the proposed distribution.

## Public discrete proposal and full expected-cost accounting

Set R=2^(4n). Independently choose e uniformly from {-n,...,n-1} and U
uniformly from {0,...,R-1}. Query the exact positive rational normal

    lambda=2^e*(1+U/R).

Clear its power-of-two denominator to get positive integer a,b. This uses
O(n) expected random bits, O(n)-bit normals, and polynomial arithmetic.
After every query compute gcd(x,N) and gcd(y,N), accepting only a verified
value strictly between 1 and N. In particular a nontrivial exact factor
vertex always succeeds. No hidden factor or label chooses a direction.

Each dyadic bin has probability 1/(2n). The continuous version has density
at least 1/(2n*lambda), so (2) gives factor mass at least
log(1+(4/N)^(1/3))/(2n). Every nontrivial cone lies inside the sampled
range: its positive rational endpoints lie between 1/(N-1) and N-1.
Passing to the discrete grid loses at most 2/R in interval mass, even if
all boundary ties are discarded. For N>=4, log(1+(4/N)^(1/3)) is at least
(4/N)^(1/3)/2, and the chosen R makes the grid loss less than half this
lower mass. Conservatively,

    Pr(verified divisor in one attempt) >= 1/(8*n*N^(1/3)). (3)

Independent restarts therefore terminate almost surely on every composite
and have expected O(n*N^(1/3)) SUPPORT calls. With the conservative query
bound, their total expected bit cost is O(n^7*N^(1/3)). All randomness,
arithmetic, intermediate sizes, and gcd verification are included. Standard
polynomial primality testing before this loop handles primes; recursively
processing proper divisors adds only a polynomial factor. This is a valid
slower Las Vegas route, not the requested quasipolynomial factoring result.

## Residual weighting versus actual first discovery

For a returned vertex define d=xy-N. An attractive ideal distribution has
mass proportional to its proposal mass divided by d+1. A scale-normalized
variant uses

    w(x,y)=min(x,y,ceil(N^(1/3)))/(d+1).

The scale factor avoids excessive preference for small-coordinate vertices
whose residual is small simply because ceil(N/x) rounds in an interval of
length x. The output records both ideal target masses as diagnostics only.
Computing their normalizers by summing the finite hull is not an algorithm
for sampling them at large N.

There is an exact first-discovery limitation for **independence proposals**.
If every proposal still comes independently from the same public normal
law, checking every candidate gives precisely the same first-success time
regardless of whether a residual Metropolis rule accepts or rejects it as
the next state. Residual acceptance cannot alter which candidates were
generated. Rejection sampling has the same cancellation when all rejected
proposal costs count. An increased stationary factor mass is consequently
not a faster discovery theorem. This statement is restricted to unchanged
independent proposals, not adaptive or correlated candidate generation.

Three actual adaptive proposal rules were tested. Each uses a fresh global
proposal with probability 1/4. Otherwise it centers at y/x and adds an
integer-grid symmetric perturbation of radius

    W=4*(isqrt(N*(d+1))+1)/x^2.

The second rule multiplies that displacement by a public dyadic scale with
exponent uniform in {-3,...,floor(n/2)}. Negative proposed normals fall back
to the global proposal. The third uses the first proposal but scale-normalized
acceptance w(new)/w(old). The first two accept non-success candidates with
probability min(1,(d_old+1)/(d_new+1)). Trivial endpoints do not become the
state. Every candidate gets its gcd check before the acceptance decision.
These proposals depend only on public returned values. Since they are
state-dependent, no Metropolis stationary-law claim is made without the
missing proposal-ratio correction. The global component alone retains
almost-sure termination and at most four times bound (3).

## Bounded evidence and resource use

The exact-support implementation passed 126 checks, including comparisons
with complete small hulls, SEEK/NEXT checks, endpoint extremality, and (2).
Two nonenumerating SUPPORT calls used N=10^24+39 and N=10^48+151 at normal
(17,11). They took approximately 0.077 and 0.460 seconds. Their returned
points and adjacent objective comparisons are retained in pilot.json.

The seven offline-labelled composites include balanced prime pairs near a
sqrt(2) ratio and two unbalanced examples. Factors are used to construct
inputs and label results only. Exact integer-grid fan masses give the
following true independent expected call counts; adaptive means are capped
sample averages, not expected-runtime estimates.

| N | Hull vertices | Exact-law independent mean calls | Ideal scale-weighted factor-point mass |
|---:|---:|---:|---:|
| 10,541 | 100 | 56.54 | 0.1616 |
| 158,549 | 272 | 184.39 | 0.0728 |
| 1,441,861 | 634 | 735.00 | 0.0529 |
| 141,529,001 | 3,486 | 3,692.50 | 0.0332 |
| 14,144,324,317 | 18,718 | 21,369.02 | 0.0120 |
| 101,000,303 | 3,056 | 101.08 | 0.0170 |
| 1,009,003,027 | 7,020 | 6,678.33 | 0.0226 |

For N=101,000,303, gcd checks raise success from factor-point mass 0.00106
to 0.00989; restricting acceptance to xy=N would discard this real gain.
Each adaptive mode ran 24 trials with a 3,000-query cap. No tested adaptive
rule improved on independent proposals in the small uncensored cases.
For larger inputs, many trials hit the cap; those finite results cannot
support a comparison of uncapped expectations. All seeds and censored
trajectories are retained.

Preflight found load 1.71/2.10/2.16 and zero swap activity. Process inspection
used an approved read-only ps call; suggestd and fseventsd were the main
CPU users, with no large mathematical process visible. The planned budget
was 30 seconds and 512 MiB. The final pilot took 5.07 seconds and 65.2 MB
peak RSS, with a source alarm. Source, output, log, and completion status
are retained as support.py and pilot.py/json/log/status.json.

## Remaining operation

The support oracle and a nonzero per-input probability are now concrete.
The unresolved requirement is to improve the total candidate-cost/success
ratio to quasipolynomial. A useful next mechanism must change which normals
are generated, with a proved per-input hitting law or an amortized argument;
stationary reweighting without its discovery/mixing cost does not suffice.
The tested residual perturbations do not supply that law. Neither this
finite result nor (3) rules out another adaptive support mechanism.
