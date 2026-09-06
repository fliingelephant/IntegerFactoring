# Grouped subtree certificates from narrow lattice lines

Status: exact prototype and proof candidate, with completed finite bias audit.
No quasipolynomial bound or novelty claim is established. This operation
replaces many affine descendant queries by a bounded set of quadratic equations.

## A public fixed cap removes the optimization requirement

Let N be odd and choose the largest power of two M<=N/8. Small cases with
M<2 can be handled directly. For a public positive integer normal (a,b), set

    U=floor(sqrt(17abN/4)).

Any positive target-modulus point with ax+by<=U satisfies

    xy <= U^2/(4ab) <= 17N/16 < N+M.

Since its product is at least N and congruent to N modulo M, its product is
exactly N. Thus searching this cap is a factor-point feasibility problem;
it does not require an incumbent or exact support minimization. The root's
dyadic-normal bound in F289/AFFINE_PATCHES.md puts a proper factor point in
this cap for at least one of O(log N) normals. Other normals can have an empty
proper-factor cap. Trivial factor points are explicitly discarded.

## One coarse lattice, many target descendants

At depth r use Q=2^min(k,2r+1), s=2^r, and the coarse affine lattice

    P0 + Z(s,delta) + Z(0,Q),  P0=(u,v).

It contains every target-M descendant of that node. Write D0=sQ for its
determinant. The cap is contained in the following rectangle after the
invertible linear transformation z=ax+by, w=ax-by:

    zlo=ceil(2sqrt(abN)) <= z <= U,
    -W <= w <= W,  W=floor(sqrt(U^2-4abN)).

Let T=U-zlo. When T or W is zero, one direct line equation covers the cap.
Otherwise find a short vector in the dual lattice after scaling its two
coordinates by T and 2W. Exact two-dimensional Gauss reduction is sufficient.

More explicitly, for integers j1,j2, a dual functional in original
coordinates has the form

    ell(x,y)=(A1*x+A2*y)/D0,
    A1=Q*j1-delta*j2, A2=s*j2.

The integer lattice used by the Gauss routine has basis

    (T*b*Q,                    2W*b*Q),
    (T*(-b*delta+a*s),         2W*(-b*delta-a*s)).

Keep the integer basis-combination coefficients during reduction to recover
(j1,j2). All points in the original affine lattice lie on lines

    A1*x+A2*y=A1*u+A2*v+D0*t,  t in Z.

The exact smallest and largest t whose lines meet the enclosing rectangle
are computed by rational linear extrema and integer ceiling/floor. This
gives a certificate covering the whole node, without iterating its target
affine patches. The code retains the phase A1*u+A2*v; dropping it would
incorrectly replace a translated lattice by the lattice through the origin.

On each line, impose xy=N. If A1 is nonzero, solve

    A1*x^2-C*x+A2*N=0.

An integer square-root test and divisibility checks recover every integer
root. If A1=0, one linear equation fixes y and a direct division checks x.
Check positivity, nontriviality, the cap, and the coarse affine congruence.
Every accepted point is a verified factor. If no root survives on any covered
line, the entire subtree contains no proper factor point in this cap.

## Exact width bound and what it costs

In z,w coordinates the lattice determinant is 2abD0. The rectangle-scaled
dual has determinant TW/(abD0). A shortest Euclidean dual vector, found by
Gauss reduction, has rectangle width less than

    2 sqrt(TW/(abD0)).

For example, this follows from Minkowski's disk bound followed by the
two-dimensional Cauchy–Schwarz inequality. The fixed cap gives

    T <= sqrt(abN)/16,  W <= sqrt(abN)/2.

Therefore the number of intersecting integer-indexed lines is at most

    1 + sqrt(N/(8sQ)).

This is a deterministic bound, not a fitted scaling law. Before the modulus
saturates, sQ=2^(3r+1). With a fixed budget K of lines per terminal node,
the bound guarantees termination by depth approximately

    r >= (log2(N/(16(K-1)^2)))/3.

All ray, dual-reduction, line-bound, and quadratic operations use integers
of polynomial bit length. A binary tree that splits until at most K lines
remain consequently has an O(N^(1/3) poly(log N)) upper bound for fixed K,
including the O(log N) normal menu. This is a numerical-power algorithm,
not the fixed research target. Near-tangent line searches and short dual
directions are classical ingredients; the packet establishes a concrete
new-to-repository subtree operation, not a new general exponent claim.

## Implementation and the original biased inputs

`CAP_LINES.py` implements the exact certificate, with K=8 and low-child-first
DFS. The first checks used the existing F289 inputs. The 41-bit input could
be split after only 144–315 nodes, much faster than the earlier support
prototype. Root then identified the construction's low-bit bias. Those
first-detection numbers are retained in `CAP_LINES_output.json` but must not
be interpreted as representative search cost.

The following completed audit separates early detection from full tree work.
Every query continues after a factor is detected and records the final node
and line-equation counts. No hidden factor chooses a normal, node order,
dual direction, cutoff, or line equation.

## Seeded random and high-residue audit

`CAP_LINES_RANDOM.py`, seed 202609070213, generates two random-candidate
prime pairs and one high-residue pair at each scale e=12,16,20,24,28. The
candidate intervals are [9*2^e/8,11*2^e/8) and [3*2^e/2,15*2^e/8).
Primality is checked exactly by trial division. These are reproducible
random-candidate/next-prime samples, not claimed uniform samples of primes.
Actual pairs and their residues are retained in the output.

The high-residue family places both factors in the upper quarter modulo
2^r, where r=max(2,floor(2e/3)-3). This stresses numeric residue size, but
not necessarily DFS order, because this DFS reads residue bits from low to
high. A large numeric residue can occur early in that bit-reversed order.

All 30 line-cap queries completed, including two empty normal caps. Their
complete factor sets matched the offline prime-factor labels. The labels
were used only after each public query to audit completeness.

| Input bit lengths | Complete-tree nodes, range over six queries | Line equations, range | Deepest visited level |
|---:|---:|---:|---:|
| 25–26 | 7–31 | 17–68 | 5 |
| 33–34 | 87–187 | 246–352 | 8 |
| 41–42 | 859–991 | 2262–2568 | 11 |
| 49–50 | 6663–6951 | 13222–14413 | 13 |
| 57–58 | 39403–42015 | 85394–86655 | 16 |

The largest initial integer line cover was 16,766,299; every terminal node
needed at most eight lines. Largest-scale full queries took about 0.20–0.22
seconds. The increasing node counts, rather than these small timings, are
the relevant scaling observation. They are compatible with the explicit
N^(1/3) upper-bound mechanism and do not establish a lower bound.

Six same-input small baselines used `PATCH_SUPPORT` under the identical
fixed cap and DFS order. They processed 99–161 nodes versus 7–31 for the
line certificates. Both first-detection and completion counts are retained.
The baseline continues after a discovery to discharge its remaining cap
tree. This is a cap-search comparison, not a claim about exact optimal-value
termination times. All six baselines completed and agreed with the offline
factor audit.

## Explicitly late traversal stress

To remove the remaining ordering ambiguity, `CAP_LINES_LATE.py`, seed
202609070214, chooses both primes congruent to -1 modulo the same 2^r.
That is the last subtree at depth r in this low-bit-first traversal.
This family is targeted at traversal order; it is not a model of generic
factoring hardness.

All ten queries completed. In every case the first factor was found at the
last visited node. At 57–58 bits the two normals required respectively
45,207 and 45,675 nodes, with 89,437 and 89,540 line equations. Full query
times were about 0.24 seconds. Thus early discovery can be removed without
removing the grouped-line speed improvement, but the full tree remains
numerically large.

## Resource and evidence record

The fresh preflight showed 73% available memory and load 1.77. The random
audit and six baselines ran in one process for 3.10 seconds with a 28-second
hard alarm. The late-order continuation took 0.55 seconds under a 10-second
hard alarm. Both retained 1.5-second/300,000-node soft query limits; no query
hit either limit. Estimated peak memory was below 128 MB. Source, seeds,
all pairs, first-detection times, complete counts, depths, maximum line
covers, logs, and outputs are retained under the `CAP_LINES_RANDOM` and
`CAP_LINES_LATE` prefixes. No remote job or additional agent was started.

The useful outcome is an exact grouped certificate and a bias-controlled
performance distinction from one-patch support calls. Independent proof
reconstruction is still pending. The next improvement must reduce the
number of coarse classes or group many such line certificates; merely
reporting first-factor timings or adding a higher-degree representation
would not resolve that resource.
