# Random thresholds and useful rank collisions

**Family:** route:F31

Status: author-derived randomized mechanism and bounded pilot design. Not
independently reconstructed, not executed in this note, and not a QP factoring
claim. This is separate from DESIGN.md, the min-count descent, and the root's
fair-branch policy. All sampling and verification described here are public.

## Concrete question

Can gaps in a modular orbit put substantial rank mass in a hidden congruence
class, without putting the same mass on identical integer ranks? If so, two
cheap random threshold queries can expose a factor even when that class is
not the zero class used by direct count gcds.

Fix odd N>1, a unit a, and a public integer 1<=t<N. First gcd-screen t as a
charged factor-success control. Sample U,V independently and uniformly from
{0,...,N-1}. Put

    C(U)=#{1<=y<=t: a*y mod N<=U},
    I=C(U), J=C(V).

Return gcd(I-J,N) only when it is proper. In particular I=J is failure, not
useful concentration. Keep ranks 0 and t distinct. The parameters a and t
may come from any publicly implemented biased distribution, including F336
r/b laws and several t scales. No Jacobi restriction is needed.

For FS(t,N,a,b)=sum_{j=0}^{t-1} floor((a*j+b)/N),

    C(U)=t+FS(t,N,a,a)-FS(t,N,a,a+N-1-U).

Indeed the floor difference detects whether a*y mod N exceeds U. Standard
Euclidean floor sums compute this in polynomial bit cost with O(log N)-bit
operands. Exact fair-bit rejection samples U in expected O(log N) bits.
Two threshold counts and a verified gcd therefore implement an attempt;
there is no complete path, full sorting, count oracle, or hidden normalizer.

## The exact sampled law

Sort the t+1 points {0,a,...,t*a} modulo N as

    0=z_0<z_1<...<z_t<N,  z_{t+1}=N,
    g_i=z_{i+1}-z_i,  0<=i<=t.

Then C(U)=i exactly for z_i<=U<z_{i+1}. Thus

    mu_i=Pr(I=i)=g_i/N.

The sorted array defines the law for analysis; the algorithm does not build
it. Sampling U=a*Y mod N with Y uniform on {0,...,t} would instead make I
uniform on {0,...,t}. That is an important, cheaper uniform-rank control,
not a gap-biased sampler.

For any d|N define the grouped collision energy

    kappa_d=sum_{r mod d} (sum_{i congruent r mod d} mu_i)^2,
    kappa_same=sum_i mu_i^2.

Since |I-J|<=t<N, divisibility by N is exactly integer equality I=J.
For N=p*q with distinct primes, the pair's proper-factor probability is

    delta(a,t)=kappa_p+kappa_q-2*kappa_same.

For N=p^e, e>=2, it is kappa_p-kappa_same. More generally, with the usual
Moebius function mob and radical rad(N), it is

    delta(a,t)=1-kappa_same
        -sum_{d|rad(N)} mob(d)*kappa_d.

These formulas are diagnostic identities. They do not give the algorithm
the factorization of N. They follow by inclusion-exclusion on the events
p divides I-J, then removing integer equality. An equivalent all-input
formula, requiring no symbolic factorization, is

    delta(a,t)=sum_{i,j} mu_i*mu_j
        *1_{1<gcd(i-j,N)<N}.

The target is this off-diagonal useful energy. A large kappa_same can make
total concentration look strong while supplying no factors.

## Three gap classes can be computed and sampled

There is an elementary exact description of this rational orbit. Let

    alpha=min_{1<=k<=t} (a*k mod N),  u=its unique index,
    beta=N-max_{1<=k<=t} (a*k mod N), v=the maximum's unique index,
    m=t+1.

Then u+v>=m. The cyclic successor of the point with orbit index k, rather
than its sorted rank, has the following index and gap:

| Orbit-index interval | Successor index | Gap |
| --- | --- | --- |
| 0<=k<m-u | k+u | alpha |
| v<=k<m | k-v | beta |
| m-u<=k<v | k+u-v | alpha+beta |

Empty intervals are omitted. Equal numerical gap lengths may occur; the
listed index classes can remain separate. Their sizes are m-u, m-v, and
u+v-m. Therefore

    kappa_same=((m-u)*alpha^2+(m-v)*beta^2
        +(u+v-m)*(alpha+beta)^2)/N^2.

Both extremal residues are found by binary search using C. Multiplication
by a^(-1) recovers u and v. This needs O(log N) count calls and one inverse,
all explicitly charged. No continued-fraction cutoff or factorization is
needed. A proper gcd discovered during these public calculations can be
reported separately, but is not part of the two-threshold baseline.

For completeness, u+v<=t would give a point at alpha-beta modulo N,
contradicting either extremum (or giving a forbidden zero). In the first
index interval the +u successor is available. Any closer positive-index
move contradicts minimality of alpha; a closer negative-index move of
size w<=k would make u+w<=t and again contradict an extremum. The second
interval is the reflected argument. In the middle interval neither +u nor
-v is available. The move u-v stays in range and has gap alpha+beta. A
closer positive move d<u would give a point u-d whose negative gap is
less than beta; a closer negative move -w, w<v, would give a point v-w
whose positive gap is less than alpha. This proves the table, including
the cases with only one or two numerical gap lengths.

Let S_c be the set of sorted ranks whose orbit indices lie in one nonempty
class above, with size n_c and gap length ell_c. Uniform k in its displayed
integer interval, followed by I=C(a*k mod N), samples S_c uniformly.
Choosing class c with probability n_c*ell_c/N exactly reproduces mu.

This permits one explicit alternative bias without expensive rejection:
choose a nonempty class uniformly, then choose k uniformly in its index
interval and return its rank. Its law is

    nu_i=1/(s*n_c)  for i in S_c,

where s<=3 is the number of nonempty classes. Two independent samples from
nu have the same useful-energy formulas with nu replacing mu. Sampling
uniform gap classes may reduce domination by one large empty arc, but it
has no established advantage. Setup, inversion, and rank queries must be
charged; an exact full-array diagnostic is not its runtime implementation.

## Exact batch law and average charged cost

For a fixed parameter pair let X_1,...,X_K be independent samples from the
chosen rank law, mu or nu. Let

    h(i,j)=1_{1<gcd(i-j,N)<N},
    d(i)=sum_j mu_j*h(i,j),
    delta=sum_i mu_i*d(i),  eta=sum_i mu_i*d(i)^2,
    T=sum_{r<s} h(X_r,X_s).

Replace mu by nu throughout for that sampler. Then

    E T=binom(K,2)*delta,
    E T^2=binom(K,2)*delta+6*binom(K,3)*eta
        +6*binom(K,4)*delta^2.

The three terms come from equal pairs, pairs sharing one sample, and
disjoint pairs. Cauchy--Schwarz gives Pr(T>0)>=(E T)^2/E T^2 when E T>0.
This distinguishes useful local collisions from repeated integer ranks;
no birthday gain follows from kappa_same alone.

If one public parameter pair is sampled first and retained for the whole
batch, average each term over that source. In particular the disjoint-pair
term contains E[delta^2], not (E delta)^2. Rare good parameter pairs are
not made common by drawing more ranks from a bad retained pair. A public
parameter-dependent K can be included by averaging the displayed binomial
coefficients times their corresponding energies.

The simplest batch implementation checks all pairs and costs

    setup(a,t)+K*count_cost(a,t)+O(K^2*poly(log N)).

No faster product-tree implementation is assumed. For a chosen source and
batch policy let c be its unconditional expected charged cost and s its
unconditional verified-success probability, including parameter-generation
gcds and t screens. Fresh independent attempts have expected cost c/s.
Their cost may be correlated with success, and some parameters may be very
expensive. The required research result is a per-input expected-QP bound
on this ratio, not a uniformly small certificate or a bound on every a,t.

## A useful control example

For a=2^(-1) mod N and t=2P-1<N/2, the orbit has two clusters of P points.
The two large gaps follow ranks P-1 and 2P-1, whose difference is P.
If P is a proper prime divisor, their off-diagonal collision can have large
factor mass even when the two individual ranks are units. But then
gcd(t+1,N)=gcd(2P,N) already exposes P. This example verifies what the
coset mechanism measures; it is not a new factoring improvement. Retain
the t+1 control so such effects are not misattributed.

## Bounded exact pilot for Sol

Run after the active F336 numerical job has released its resource slot.
One thread, 30-second external timeout, below 256 MiB; estimate under ten
seconds for the explicit arrays below. Keep a named source, preflight, log,
JSON, and hashes. Begin with N=209 before the complete small plan.

1. Inputs N in {209,1333,10807}; the known factors are offline labels only.
   Use t in {floor(sqrt N),floor((N-1)/8),(N-1)/2}, deduplicated and clipped
   to 1<=t<N. Preserve charged gcd(t,N) and a separate gcd(t+1,N) control.
   Do not discard cells because either control already finds a factor.
2. For each N, draw eight parameters from each of seven laws: uniform;
   direct and inverse at gamma in {1/4,1/2}, and ratio at gamma in
   {1/4,3/8}. Use the exact public
   integer samplers specified in F336 DESIGN.md. Preserve source labels,
   duplicate parameters, seeds, r,b, all generation attempts, and factors.
   No Jacobi filter is applied. A generation factor is an actual success;
   it does not supply a unit parameter for a later diagnostic cell.
3. For each eligible a,t, sort {0,a,...,t*a} only in this offline diagnostic.
   Check positive gaps summing to N, the three-index-class successor table,
   the closed kappa_same formula, and C(U) against binary-search ranks for
   U in {0,N-1} plus sixteen independent public thresholds. Keep 0 and t
   separate. Validate class sampling by its full image-rank sets.
4. Compute exact kappa_p, kappa_q, kappa_same, direct-count factor mass,
   and delta for mu, for uniform ranks on 0,...,t, and for nu. Compute the
   nine possible class-pair useful energies as diagnostics; no offline
   energy may choose an actual sampling class. Use rational arithmetic or
   integer numerators with declared denominators. Also compute eta and the
   displayed batch lower bound at K in {2,8,32}. Report per-input ratios
   against uniform ranks only when the denominator is nonzero.
5. Validate the useful-energy identity by direct O(t^2) pair enumeration
   only for the N=209 cells. Larger cells use grouped residue sums from
   offline factors. Keep the output compact: per-cell energies, class
   sizes/lengths, controls, and first anomaly. Do not retain large arrays.

The next decision depends on useful energy, not total concentration: does a
biased r/b source increase off-diagonal hidden-coset collisions enough to
pay for its threshold counts and setup, after the t,t+1 and uniform-rank
controls? Exact small arrays can reveal a pattern; they cannot establish a
uniform success theorem. Large-input sampling is a later experiment only
if a specific observed structure justifies it.

## Prior work and scope

Scoped Rust navigation read P25, P41, and P43, and the F335/F336 notes.
P25 supplies a different source-specific collision analysis. P41/P43 give
positive factor-energy targets with unresolved samplers. Here the rank
sampler is explicit; its useful local collision mass is the missing fact.
No old collision obstruction is imported to this law.

The gap structure itself is classical. A focused primary-source abstract
check asked whether the at-most-three-gap statement and interval-exchange
view were already standard; see Jens Marklof and Andreas Stroembergsson,
[The three gap theorem and the space of lattices](https://arxiv.org/abs/1612.04906),
and Diaaeldin Taha,
[The Three Gap Theorem, Interval Exchange Transformations, and Zippered Rectangles](https://arxiv.org/abs/1708.04380).
Only their abstracts were needed for this provenance check. The elementary
finite successor argument above is provided independently; no full-text
result, external distribution law, or novelty claim is assumed.
