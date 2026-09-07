# Continued-fraction mass along the gap induction

**Family:** route:F31

Status: root derivation, unpromoted and not yet finitely checked. The
three-gap description in RETURN_MAP_JUMPS.md is a declared dependency here;
its finite checks do not constitute independent proof promotion. P250 supplies
the separately promoted fixed-denominator mean bound used at the end.

## Exact conservation law

For a reduced fraction x/y in (0,1), let S(x,y) be the sum of its canonical
continued-fraction digits, with the final digit at least two. For positive
coprime integers x,y, define E(x,y) as the number of individual subtractions
of the smaller from the larger needed to reach (1,1). Euclidean division
gives

    S(x,x+y)=E(x,y)+2.

Fix N>1, gcd(a,N)=1 and 1<=a<N. For any orbit prefix {0,a,...,t*a},
1<=t<N, use its extremal gaps alpha,beta and indices u,v from F339, and
put L=u+v. Then

    S(u,L)+S(alpha,alpha+beta)=S(a,N)+2,                 (1)
    S(u,L)<=S(a,N).                                    (2)

Here is the induction. At the initial two-point prefix,

    (u,v)=(1,1),   (alpha,beta)=(a,N-a).

The same extrema hold while max(u,v)<=t<u+v. At the next index u+v,
the new residue is alpha-beta modulo N. If alpha>beta, the update is

    u <- u+v,    alpha <- alpha-beta;

if beta>alpha it is

    v <- u+v,    beta <- beta-alpha.

These are precisely the gap-induction updates. Equality alpha=beta occurs
only at alpha=beta=1 and L=N, because the gap gcd is invariant and the
positive gap equation is alpha*v+beta*u=N. There is no further index in
the allowed prefix range.

At each update E(u,v) increases by one, while E(alpha,beta) decreases by
one. Their initial sum is E(a,N-a)=S(a,N)-2. This proves (1); since every
positive coprime pair has continued-fraction sum at least two, (2) follows.
The induction is a proof device. Enumerating its potentially many individual
subtractions is not required by any runtime implementation.

## Uniform displacement control for arbitrary public jumps

Let m=t+1 and d=L-m. For any phase 0<=k<L and any 0<=q<L, let

    h(k,q)=#{0<=j<q : (k+j*u mod L)>=m}.

Then

    |h(k,q)-q*d/L|<=5*S(u,L)<=5*S(a,N).                (3)

To verify the constant, take any convergent denominator v_j of u/L.
A block of v_j orbit points is paired with a translated equally spaced
v_j-grid. All paired displacements have one direction and length at most
one grid spacing. For a half-open interval of length d/L, at most four
grid memberships change, including endpoint cases. The grid count differs
from v_j*d/L by at most one. Thus a whole block has count discrepancy at
most five. The denominator-one block also obeys this bound. Decompose q<L
greedily into convergent-denominator blocks; their number is at most S(u,L).
This is the same block argument as P250, with an arbitrary interval instead
of the lower half-circle. It proves (3) for every phase and every prefix.

For an accepted coupled pair the forward retained rank distance is
D=q-h(k,q), so

    |D-q*m/L|<=5*S(a,N).                               (4)

The ordinary rank difference is D or D-m. Therefore every coupled factor
under one public (a,t,q) is covered by the integer windows of radius
5*S(a,N) around q*m/L and q*m/L-m. Clip the windows to -(N-1),...,N-1
and ignore zero and full gcds. Streaming this menu uses O((1+S(a,N))*poly(n))
bit work and polynomial space, with n=bitlength(N). No sampled endpoint or
hidden factor is used to construct the centers or the radius.

## An expected-cost consequence, without a cutoff

Suppose N is odd and each independent attempt has a marginally uniform
Jacobi-positive unit a. The public t and q may depend arbitrarily on a and
on other coins, with their full generation cost charged. P250 gives

    E S(a,N)<=M_N<=4*(1+log_2 N)*(1+ln N)^2.

Hence the extra expected cost of enumerating the entire window menu is
polynomial in n. Rare parameters with a very large menu are retained and
paid for. There is no need to require a deterministic small-S certificate,
reject those parameters, or assume that their cost is independent of success.

For each fixed parameter triple the menu succeeds whenever any coupled
endpoint succeeds, so its unconditional source success probability is at
least the original coupling's. If generation has polynomial mean cost and
that probability is inverse-QP uniformly for each N, independent retries
of this menu would meet the expected-QP splitter contract.

This is a conditional simplification, not a source-mass theorem or a
factoring obstruction. The centers q*m/L can depend on N and the sampled
parameter. No fixed-coefficient cofactor count may be applied to them
without proving its hypotheses. Deliberately biased sources can have a
different mean S and are outside this expectation argument. A retained
parameter reused for an adaptive number of triples also needs its own
total cost accounting; the one-triple attempt bound does not pay for that
reuse automatically.

## Check and provenance

The bounded F339 identity corpus can check (1) for each extremal state and
(3) against its direct deleted counts, using exact integer comparisons.
Numerical validation remains finite. Scoped Rust searches found no indexed
Stern--Brocot statement and only P62, P189 and P250 for the exact
continued-fraction query; this is not an external novelty claim. The gap
induction and Euclidean accounting are classical structures. The research
point is the explicit expected-cost menu consequence and its precise source
scope, not a claim to have invented those structures.
