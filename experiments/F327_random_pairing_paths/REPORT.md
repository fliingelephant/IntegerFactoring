# F327: an exact capped-work law for lazy random matchings

**Family:** route:F31

The random auxiliary matching acts on F326's ranked inverse and
sign-selected residue path, so it belongs to the retained
modular-hyperbola family.

Status: author-derived theorem verified by fresh independent reconstruction,
with random sampling overhead interpreted in expected time. This is a
rigorous slow randomized benchmark, not a quasipolynomial factoring
algorithm and not a lower bound for structured matchings.

## Scope and route difference

F326 supplies the polynomial-bit rank, select, and involution F on an odd interval of size d. P02 supplies the hidden-root reduction. These were read through the F326 statement/Rabin documents and the Rust P02 head and body. The present mechanism randomizes both the known start and the auxiliary matching. It does not demand a deterministic short endpoint algorithm or completion of every attempt.

Fix N and a throughout the inner analysis. F denotes the ranked F326 involution. Let q be its number of fixed ranks; q is odd. The algorithm does not know or compute q. Choose a uniform start j from the d ranks. Give j a singleton auxiliary edge, and choose a uniform perfect matching of the other d-1 ranks. Reveal only edges encountered by the path. All random coins are independent of the hidden square root used by the outer generator.

## A lazy implementation without depletion rejection

Maintain a uniform-unused pool, initially all ranks. Sample j from the pool and remove it. At a current rank v, evaluate u=F(v). If u=v, decode and stop. Otherwise remove u from the pool, sample a uniform unused rank w, remove w, declare the auxiliary edge u<->w, and continue at w. Stop with failure if the chosen evaluation cap has been reached. The current rank was already removed when it was selected.

No previously removed rank can be the new nonfixed partner u. Every previously tested F edge has had both endpoints removed, and F is an involution. The current rank has not been tested. Thus a collision with an old F edge would contradict its being a new rank. Each newly exposed auxiliary partner is uniform among the still available vertices, exactly as in a uniform completion of the auxiliary matching with j as its unique fixed vertex. No full matching is constructed.

Implement the pool with sparse forward and inverse permutations P,Q of {0,...,d-1}; a missing map entry is the identity. Keep an active size m, initially d. To remove a known active label v, set p=Q(v), w=P(m-1), swap the permutation entries at p and m-1, update both inverses, and decrement m. Specifically set P(p)=w, P(m-1)=v, Q(w)=p, Q(v)=m-1. Sampling chooses a uniform position in [0,m-1] and returns its P-label. Maps may retain inactive entries. Each deletion adds at most a constant number of entries, so after T evaluations they use O(T) words, each O(log d) bits.

Balanced search trees give deterministic O(log(T+1)) map operations, avoiding a hidden hash-table assumption. Uniform positions use rejection from the next power of two, with fewer than two trials in expectation and O(log d) expected fair bits per selection. This rejection concerns bit encoding, not the shrinking unused fraction. Thus depletion causes no sampling slowdown. F326 arithmetic, dictionary comparisons, randomness and storage together cost poly(log N) per visited edge and O(T log N) bits of storage under cap T. The exact matching can remain implicit forever on unused ranks.

## Exact finite-cap identity

Let H be the number of F evaluations until the first fixed point, including its evaluation. Put m=(d-q)/2. After k unsuccessful evaluations, exactly k nonfixed F pairs have been removed, while all q fixed ranks remain. The next current rank is uniform among d-2k ranks. Hence, for 0<=k<=m,
\[
 h_k:=\Pr(H=k+1\mid H>k)=\frac{q}{d-2k}.
\]
Define S_0=1 and
\[
 S_T=\prod_{k=0}^{T-1}\frac{d-q-2k}{d-2k}
 \quad(1\le T\le m+1),\qquad S_T=0\quad(T>m+1).
\]
The factor at k=m is zero. There are no negative continuation factors beyond that point. The exact valid-output probability and expected capped number of calls are
\[
 \delta_T=1-S_T,\qquad W_T=\mathbb E\min(H,T)=\sum_{k=0}^{T-1}S_k.
\]
These are analysis identities, not values the algorithm must compute.

The uncapped expectation has the closed form
\[
 \boxed{\mathbb EH=\frac{d+2}{q+2}.}
\]
Indeed the process with d=q stops in one call. For d>q, its expectation obeys E(d,q)=1+(d-q)E(d-2,q)/d. Substitution of (d+2)/(q+2) satisfies both the recurrence and the base case.

Each fixed rank has the same probability S_k/(d-2k) of being the terminal current rank at evaluation k+1. Therefore the endpoint is uniform among the q fixed ranks, including after conditioning on H<=T. This assertion follows from the explicit sampling law, not an assumption about the arithmetic distribution of path vertices.

## Conditional square-input accounting

Let N have s>=2 distinct odd prime divisors, with arbitrary positive exponents, and fix any unit square a modulo N. Conditional on this a, the hidden outer root r is uniform among its 2^s roots. The inner algorithm receives only N,a and its independent matching coins.

The F326 involution has exactly 2^s-1 unit fixed ranks:

1. The first inverse branch contains the positive roots of 1 other than 1. There are 2^(s-1)-1. Each gives a verified proper gcd with x-1.
2. The scaled inverse branch contains exactly the x=c^-1 for negative roots c of a. There are 2^(s-1). These give valid root outputs c.

For the second claim, c<0 and c^2=a imply ax=c<0 and x^-1=c<0, so the branch condition and domain condition hold. Conversely its fixed equation is ax^2=1 with x^-1 negative. The two branch classes are disjoint. Nonunit fixed ranks supply proper divisors as specified in F326.

Using the specified F326 decoder, each root output has outer factor probability 1-2^(1-s), by P02. Since the endpoint is uniform, the total conditional failure mass among q fixed ranks is
\[
 \frac{2^{s-1}}q\,2^{1-s}=\frac1q.
\]
Thus the exact factor probability of the capped attempt, conditional on this a and on an initially unit outer root, is
\[
 \boxed{p_T(a)=\left(1-\frac1q\right)(1-S_T).}
\]
This averages over the matching coins and the hidden root conditional on a. A specific fixed hidden root need not have this success probability. The solver never sees that root. Initial proper gcds from outer sampling add immediate verified successes, as in F326/RABIN_MODE.md.

## Cap choice within this matching family

The hazards q/(d-2k) increase with k. Moreover
\[
 \delta_T=\sum_{k=0}^{T-1}S_kh_k.
\]
Therefore delta_T/W_T is a weighted average of the first T hazards. Adding the next, larger hazard cannot decrease this average. For a fixed a, W_T/delta_T and W_T/p_T(a) are nonincreasing in T. Any fixed nonnegative setup cost C preserves this monotonicity because C/delta_T also decreases.

This compares expected local-call cost per success, not worst-case attempt time. It is conditional on a; after mixing different a, the surviving input distribution changes, so a global monotonicity claim is not automatic. Polynomial dictionary/arithmetic costs can also vary with path length. The algorithm is free to use any cap. The identity supplies a precise benchmark for charging that choice.

## Verified gcd screens at visited edges

There is an exact extension beyond fixed endpoints. Fix any public, history-independent screen that checks proper divisors using both coordinates of an F edge. Examples are gcd(x-1,N), gcd(x+1,N), gcd(x-F(x),N), and gcd(x+F(x),N), in addition to coordinate gcds. Every returned divisor is verified. Define B to contain all fixed ranks and every nonfixed F pair for which this screen gives a divisor at either endpoint. B is F-invariant and its size b=q+2g is odd, where g is the number of screened nonfixed pairs.

Screen the edge before discarding its partner. Exactly the same proof gives survival S_T with q replaced by b, mean (d+2)/(b+2), and a uniform absorbing rank conditional on stopping. All absorbed nonfixed pairs give factors. There remain at most 2^(s-1) root-producing fixed ranks, so the hidden-root factor probability is at least (1-1/b)(1-S_T). Equality holds if no such root output is preempted by a screen. The algorithm need not know b or enumerate B.

History-dependent checks, such as gcds between coordinates from different visited edges, may also be added. They return only verified factors and can improve success. They are outside this static-set identity, and their arithmetic and storage must be charged. No lower bound here applies to those enhancements.

## What this proves about cost, and what it leaves to structured matching

For the baseline with the stated decoder, let M=N-phi(N)-1 be the number of nonzero nonunits. The positive half of F326's domain contains M/2 nonunits and its negative part contains between zero and M/2. Hence
\[
 M/2+2^s-1\le q\le M+2^s-1,
 \qquad (N+1)/2\le d\le N.
\]
For a squarefree semiprime N=p*l, these bounds give E H=Theta(p*l/(p+l))=Theta(min(p,l)), uniformly over every unit square a. Also 1-1/q is between 2/3 and 1. The conditional cap comparison therefore shows that no cap or resampling mixture over a improves the baseline's expected local-call order below this scale: each conditional work/success ratio already has this lower bound. This is a scoped statement about uniform auxiliary matchings and the baseline decoder. It does not cover structured matchings, extra gcd screens, adaptive cross-edge checks, or jumps.

The useful constructive target is now quantitative. A structured family such as S_j(i)=2j-i mod d, j uniform, should be compared against the exact capped law at the same N,a and the same screen. An improvement would have to create extra short-path absorption or reduce the cost of visiting a structured block. No worst-case-fast endpoint procedure is required. A sufficient goal contract remains expected attempt bit cost divided by actual factor probability, averaged over independent random squares and matching coins for each fixed N.

No heavy computation was run for this packet. The companion design specifies a bounded, discriminating finite test. The counting parameters q and b are diagnostic labels only; they are not required subroutines.
