# F320: approximate energy estimation and joint collision sampling

**Family:** route:F23

Status: author-derived identities and finite exact checks. Not independently
reconstructed or promoted. No quasipolynomial factoring algorithm is claimed.
Route: F23. Closest records read: P41, P43, P61, P34, and F162.

## Question and material difference

Can a positive variance-reduced estimator retain enough proper-gcd Fourier
mass without learning the exact normalizer? If the scalar estimator is poor,
can joint proposals create many readable candidates per stored random value?

P41 already allows approximate sampling. Its polynomial bound can be replaced
by a fixed quasipolynomial bound in the same stopped-cost proof. Exact total
variation approximation is also unnecessary: any explicit output law with
proper-gcd probability p(N), and independent-attempt expected cost a(N),
works if a(N)/p(N) has one uniform quasipolynomial bound. The work below tests
actual estimators and a joint proposal, rather than requiring an exact sampler.
The second construction changes both the source and the decoder from the
one-coordinate Gibbs kernels in P43/P61. Its batch arithmetic already exists
in P34/F162; it is not a new factoring-complexity claim.

## 1. Remove both known energy nuisances

For odd N, the target is pi(k)=gcd(k,N)/S, including k=0, where

    S = sum_{d|N} d phi(N/d),    S(p^a)=p^(a-1)((a+1)p-a).

Define the publicly evaluable nonnegative control residual

    h(k) = gcd(k,N)-1-(N-1) 1_{k=0}.

It vanishes on units and zero. Every positive observation is already a
verified factoring success. This handles the zero atom exactly and avoids
spending precision on the unit baseline. For uniform K,

    mu = E h(K) = (S-2N+1)/N,
    E h(K)^2 = (1/N) sum_{1<d<N, d|N} (d-1)^2 phi(N/d).

These follow by counting the phi(N/d) residues with gcd d. They apply to
repeated primes and arbitrary balance, not just squarefree inputs. The
mean of M independent observations has variance Var(h)/M. Evaluating it
uses M uniform n-bit residue draws and M gcds, hence M poly(n) bit cost.

For distinct primes N=pq,

    mu = 2(p-1)(q-1)/N,
    E h^2 = (p-1)(q-1)(p+q-2)/N,
    Var(h)/mu^2 = N(p+q-2)/(4(p-1)(q-1))-1.

Thus the exact relative variance is Theta(p+q) for large primes. This
control variate does remove the much worse zero contribution, but a
constant-relative-RMS estimate still requires Theta(p+q) iid gcd probes.
For p fixed and q large it is especially misleading: the mean is controlled
by large weights on rare multiples of q, although factoring via p is easy.
This is a failure of this estimator, not a lower bound on approximate
factor discovery.

For a random cyclic block, use H_B(A)=sum_{j<B}h(A+j)/B with A uniform.
Its exact variance is

    Var(H_B) = B^(-2) sum_{i,j<B} C(j-i),
    C(t) = (1/N) sum_k h(k)h(k+t)-mu^2.

The finite experiment computes this quantity by full cyclic enumeration.
One exact structural limit is simpler than its full divisor expansion:
put alpha=(N-phi(N)-1)/N. The probability that the block contains any useful
residue is at most B alpha, by the union bound. Any sampler that only
reweights the explicitly probed B residues inherits that limit. For
balanced semiprimes alpha=Theta(N^(-1/2)), so a quasipolynomial-size block
does not give constant useful mass. This bound is solely about that named
proposal; it does not cover an implicit arithmetic decoder of a large block.

Precision is not the decisive requirement here. The direct gcd decoder
already succeeds with probability alpha per probe. Rejecting or resampling
those same probes can improve a conditional output distribution but cannot
increase accepted proper factors per generated probe. No normalizer need be
estimated for that conclusion.

## 2. A genuinely joint proposal with an exact all-input success bound

Draw independent uniform residues A_1,...,A_m,B_1,...,B_m modulo N. The
candidate menu consists of K_ij=A_i-B_j. Let

    Z = sum_{i,j} 1_{1<gcd(K_ij,N)<N},    lambda=m^2 alpha.

Each K_ij is uniform. Any two distinct differences are independent, including
pairs sharing one A or one B: condition on that shared variable and the
other two uniforms remain independent uniform differences. Consequently

    E Z=lambda,    Var(Z)=lambda(1-alpha),
    lambda/(lambda+1-alpha) <= Pr(Z>0) <= min(1,lambda).

The lower bound is the second-moment inequality. It needs no CRT assumption
and covers every composite, including prime powers. For the least prime
factor p of a composite N, the nonzero multiples of p alone give

    alpha >= (N/p-1)/N >= 1/(2p).

Thus m>=sqrt(2p) gives success at least 1/2. The matching upper bound explains
why independent banks of quasipolynomial size have negligible success on
balanced semiprimes. This is a statement about this explicit random source.

### Decode in almost linear bank size

Deduplicate the A residues globally and form the monic polynomial
F(X)=product_{a in A}(X-a) modulo N. For each distinct b in the B bank,
evaluate F(b) if b is not in A and F'(b) if b is in A. The derivative removes
the single exact global equality, which cannot itself give a proper gcd.
Deduplication does not remove any useful difference. Test all resulting gcds.

If one gcd equals N, build the scalar product tree of b-a for a!=b and
descend through a nonunit child. Each leaf is nonzero modulo N, so the
descent ends with a proper gcd. Only one such descent is needed. If a useful
difference exists, some evaluated product has nonunit gcd, and this procedure
finds a factor. Equal global residues, units, and full-gcd pooled products
therefore do not cause an unaccounted failure.

P34 provides the monic composite-ring product/remainder arithmetic. F162
already gives this derivative deletion and localization technique in a
signed-inverse setting. The same arithmetic costs soft-linear time in m,
times polynomial factors in n, and comparable storage. Monic division never
inverts a point difference. The extra scalar descent costs O(m) modular
operations, so it does not change the bound. Fair-bit sampling is expected
O(m n); all accepted factors receive exact gcd/division verification.

The public algorithm does not know p. Use independent banks at m=1,2,4,...,
up to m=ceil(sqrt(2 ceil(sqrt(N)))); repeat the final stage if needed.
At successive stages beyond sqrt(2p), failure is at most 1/(m^2 alpha), so
the probability of reaching a stage decreases faster than geometrically.
Summing stage costs gives expected sqrt(p) times poly(n) bit cost with fast
arithmetic. The cap is sufficient because p<=sqrt(N). Prime testing first
prevents futile retries on primes. Even removal and recursive verified
splitting cover complete factorization, with O(n) factor-tree nodes.

This is an actual Las Vegas discovery algorithm, but its balanced-input
bound is N^(1/4) times polynomial logarithmic factors, not quasipolynomial
in n. It is recorded to distinguish a real joint proposal from a sampler
oracle. Neither the familiar birthday scale nor the batch decoder is
presented as novel.

## 3. Exact experiment and consequence

`check.py` checks the divisor energy identities and cyclic block variances
on 11 inputs, including 9,25,27,45,49,121,303,10403. It exhausts all two-bank
m=2 samples for N=9 and N=15. It confirms both exact collision variance and
the second-moment bound. For N=9 the success is 458/729 against lower bound
8/15; for N=15 it is 2918/3375 against lower bound 8/11. The code uses
divisors only as offline identity labels, never to choose a public bank.
The fast polynomial decoder is justified from the existing arithmetic
records above, not implemented or benchmarked by this small checker.

The sharper restart question is whether an efficiently represented joint
source can create far more than m^2 * alpha useful pair differences at
quasipolynomial m, or an implicit large menu can be decoded cheaply. P34's
subset sums are an existing example of a compact source with many rare
relations, but its decoder remains exponential. Approximate output quality
does not force exact product evaluation; no replacement construction is
proved here. The variance result and pairwise-independence result do not
exclude structured correlated proposals outside the two tested families.

## Source check

A focused primary-source search found Bostan, Gaudry and Schost,
*Linear Recurrences with Polynomial Coefficients and Application to Integer
Factorization and Cartier-Manin Operator*, SIAM J. Comput. 36 (2007),
1777-1806, DOI 10.1137/S0097539704443793:
https://epubs.siam.org/doi/abs/10.1137/S0097539704443793
and the authors' copy https://mathexp.eu/bostan/publications/BoGaSc07.pdf.
Its abstract confirms the established deterministic factoring context;
no unread theorem is used as a new primitive. The exact arithmetic used
here is the already-read P34/F162 construction. No novelty conclusion is
drawn from the focused search.
