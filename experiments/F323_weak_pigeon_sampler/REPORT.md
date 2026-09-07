# F323: arithmetic collisions in the actual WeakPigeon reduction

**Family:** route:F02

The primary mechanism is a succinct algebraic collision source and decoder.
The repeated-squaring null is only one scoped test of that collision menu.

Status: completed finite experiment and author-derived scoped propositions;
not independently reconstructed or promoted. No quasipolynomial factoring
bound has been established. Source: Emil Jerabek, *Integer factoring and
modular square roots*, arXiv:1207.5220, Theorem 3.5 and Lemma 3.3.

## Question and difference from prior work

Before reading the paper, the question was whether the arithmetic function
behind the WeakPigeon reduction admits a correlated collision source, public
bucket restriction, or inexpensive implicit menu that beats independent
birthday banks. P34 and F320 already provide product-tree decoding of
independent banks. P40 already covers low-actual-degree zero-ticket products.
This packet instead identifies the actual encoded function, tests its public
Jacobi buckets, and examines a high-actual-degree repeated-squaring menu.
It does not assert a new affine-polynomial bound or a generic oracle lower
bound. The Rust reader was used to inspect P34, P40 and related record heads.

## Exact source function and decoder

For odd N > 1 and units a,b modulo N, set a_0=1,a_1=a,a_2=b. The source map is

    f: {0,1,2} x {1,...,(N-1)/2} -> {1,...,N-1}
    f(i,x) = a_i*x^2 mod N, if gcd(x,N)=1;
             x, otherwise.

The domain/range ratio is 3/2. The otherwise branch matters: squares of
nonunits can be zero, which is outside this declared codomain. Any collision
containing a nonunit immediately supplies a proper gcd. For unit collisions:

* If i=j, x^2=y^2 modulo N and the half-interval rules out x=+-y modulo N.
  Thus gcd(x-y,N) is proper.
* If i<j, r=x/y modulo N satisfies r^2=a_j/a_i. For (i,j)=(0,1) or
  (0,2), this is a root of a or b. For (1,2), a*r is a root of ab.

Consequently an arbitrary collision solves FacRootMul. It does not always
factor N. WeakFacRoot additionally takes Jacobi(a,N)=1 and Jacobi(b,N)=-1;
b and ab cannot have roots, so a collision either factors or returns a root
of a. Lemma 3.3 samples the Jacobi-positive input so that a factor is forced
with constant probability on non-perfect-power composites. Independent
restarts with verified gcd outputs are permitted; exact collision sampling
is not needed. The reduction itself supplies no efficient collision source.

The formula in the cached Markdown is an image. It was read directly from
`.knowledge/.figures/arxiv__1207.5220/1207.5220.pdf-0009-01.png`.

## Scoped proposition A: Jacobi buckets erase the collisions

Let N=pq for distinct primes p,q congruent to 3 modulo 4. Use the public
choice a=-1 and any unit b with Jacobi(b,N)=-1. Restrict to unit inputs of
the source map. Then every output fiber has exactly two elements; they have
the same branch index and opposite Jacobi symbols of x. In particular each
restriction Jacobi(x,N)=+1 or -1 is injective, and retains zero collisions.

Proof. The square-class vectors over F_p and F_q of 1,-1,b are distinct:
(+,+),(-,-), and one of (+,-),(-,+). Their multiplied-square images are
disjoint, so collisions never cross branches. Every represented value has
four unit roots by CRT, hence two after identifying the global sign through
the half interval. The two remaining classes differ by changing exactly
one local sign. Since both primes are 3 modulo 4, this changes Jacobi(x,N)
by -1. Global sign changes leave that Jacobi symbol unchanged. This proves
the claim, including exact fiber size.

The full map still has easily decoded nonunit collisions. The proposition
does not suppress their gcd contribution. It says that conditioning already
screened units on one Jacobi bucket destroys the desired unit collisions.
The two opposite buckets map bijectively onto the same three square cosets.
Matching their images remains a concrete arithmetic inversion/matching
problem; this packet gives no lower bound for that problem.

## Scoped proposition B: repeated squaring stops coalescing immediately

Let N=pq be as in A. For any units x,y and any integer t>=1,

    gcd(x^(2^t)-y^(2^t),N) = gcd(x^2-y^2,N).

In particular the partitions of the half-interval units induced by
x -> x^(2^t) mod N are identical for all t>=1. Their fibers all have size 2.
The probability that two distinct uniform half-interval units collide is
exactly 1/(phi(N)/2-1), independently of t.

Proof. For each r in {p,q}, the order of x/y divides r-1=2m with m odd.
It divides 2^t if and only if it divides 2. Thus divisibility of the displayed
differences by r is identical. Squarefreeness converts equality of these
two local divisibility indicators to equality of gcds. Fiber size follows
from A with the coefficient 1. A unit class has exactly one other partner
among the phi(N)/2 half-interval units.

This is a high-degree circuit statement: evaluating x^(2^t) needs only t
modular squarings, but no number of these squarings adds useful gcd mass on
this family. It holds pointwise, so even a correlated choice of x,y cannot
make this final repeated-squaring transformation improve that pair's gcd.
It does not rule out other maps, shifted squaring, adaptive output-selected
roots, or a source that chooses better pairs before the transformation.

## Scoped proposition C: a common multiplicative seed adds no diversity

For any odd N and units c,x, with y=c*x modulo N,

    gcd(x^2-y^2,N) = gcd(1-c^2,N).

More generally a same-seed menu x_j=c_j*x has

    gcd(a_i*x_j^2-a_k*x_l^2,N)
      = gcd(a_i*c_j^2-a_k*c_l^2,N).

These follow by removing the unit factor x^2. Canonicalizing a point to
its half-interval representative does not affect its square. Therefore
varying only the common seed cannot improve the event for a fixed menu.
The coefficients may themselves contain useful arithmetic structure; no
bound is claimed on finding them or evaluating a succinct menu of them.

## Exact computation and costs

`probe.py` runs the real three-branch map on every input for 11 explicit N.
For each collision it checks the corresponding divisor or root decoder.
For powers 2^t, t=1,...,8, it enumerates exact fibers and compares partitions.
It also checks proposition C for every ordered pair of units (c,x).
Factors are trial-divided only as offline labels; public choices a=-1 and
the first Jacobi-negative b do not use these labels.

The eight Blum inputs are 21,33,77,161,209,341,437,589. Every unit collision
crossed the two Jacobi buckets and every power partition was unchanged.
At N=589 there are 405 unit collisions in the full three-branch map, all
same-branch and opposite-Jacobi. Each single squaring branch has 135 pairs
at every tested depth. Non-Blum controls 65,85,221 show genuine further
coalescence: at N=85 the collision-pair counts for t=1,2,3,4 are
16,112,240,496. Thus the test distinguishes the congruence-specific failure
from a universal assertion about repeated squaring.

The 30-second timeout was enforced by `signal.alarm`. Estimated memory was
16 MB, below the 512 MiB allocation. The full run took about 0.10 seconds;
no censors or failed assertions occurred. There was no random seed because
all enumerations were exhaustive. Exact per-instance map-evaluation,
modular-squaring, and common-seed identity counts are in `output.json`.
These are operation counts, not a claim of bit-complexity improvement.
The largest enumeration has fewer than 300,000 ordered unit pairs.

`preflight.txt` retains load and memory-pressure information. The process
inventory required a read-only sandbox escalation; it showed one system
filesystem daemon near one core and otherwise light CPU use. The bounded
pilot and full run coincide because every instance is tiny. No large run
was launched. `run.log` and `output.json` retain completion status.

## Remaining concrete direction

For the Blum public instance, the useful unit collision task is exactly
matching the two explicit Jacobi sheets of the square map. Restricting to
one sheet removes all collisions; repeating the square map and randomizing
a common multiplicative seed give no new gcd event. A useful next mechanism
must supply cross-sheet arithmetic correlation that is absent from these
operations. Nonlinear maps with shifts and adaptive histories remain open,
as do direct transcript decoders beyond pairwise square differences.
