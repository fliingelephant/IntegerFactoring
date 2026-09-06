# Exact support on a sheared patch, and shared dyadic bounds

Status: implemented exact prototype, bounded exhaustive checks, and a
hierarchical union-support construction. No uniform pruning bound or complete
factoring algorithm is claimed. All prior F288 files are unchanged.

## One patch: reduction and heights

Let M=2^k, h=max(1,floor(k/2)), and s=2^h. For odd u0 in [1,s), define

    v0 = N/u0 mod M,
    delta = N((u0+s)^(-1)-u0^(-1)) mod M.

Use the affine lattice

    (u0,v0) + Z(s,delta) + Z(0,M).

The root's second-difference identity supplies the exact affine cover; this
packet takes that identity as its declared dependency. Here is the relevant
ABCS normalization. If s<M, then

    delta = -Ns/[u0(u0+s)] mod M

has 2-adic valuation exactly h. Thus delta=s*d with d odd modulo m=M/s.
Divide both coordinates by s. The lattice becomes the rational translate
(u0/s,v0/s) of the reduced integer lattice with standard basis

    (1,d), (0,m),

and the product threshold becomes N/s^2. Its determinant is m, and both
coordinate projections are Z, as required by ABCS Definition 3.1. When s=M,
the case is d=0,m=1 and the same conclusion holds.

The actual implementation keeps the original **integer** coordinates and
basis (s,delta),(0,M). Uniform coordinate scaling leaves all ray tests and
basis updates unchanged. It therefore avoids rational-denominator growth
while being equivalent to the normalized instance used for the complexity
argument.

Every vertex of this unboxed positive patch satisfies x,y<=N+M. Indeed,
(M,0) and (0,M) belong to its difference lattice. A point with x>=N/y+M
could be moved left by M and remain feasible, so could not be a vertex.
All positive integer y are >=1, and the analogous argument bounds y.
This bound includes extreme vertices near the asymptotes, unlike a balanced
box bound.

For SEEK at original coordinate t, the initial vertical lattice line is

    x0=u0+s*ceil((max(1,t)-u0)/s), j=(x0-u0)/s.

Its y residue is v0+delta*j modulo M. Raising that residue by the smallest
multiple of M giving x0*y>=N constructs the required feasible starting point.
The scaled point can have its y-coordinate in (1,2); the implementation
handles ABCS Lemma 3.9's last-row exception explicitly. Swapping coordinates
uses the inverse shear d^(-1) modulo m (and d=0 when m=1), rather than
incorrectly reusing the same shear.

## Implemented oracle and bit-cost accounting

`PATCH_SUPPORT.py` implements exact quadratic lattice ray casting, ABCS
Algorithm 2 NEXTPT, translated last-row handling, forward/reverse SEEK, and
the coordinate binary-search SUPPORT reduction in `LITERATURE.md`.

SUPPORT returns the lexicographic minimum `(a*x+b*y, x*y, x, y)` over the
patch. A tied supporting face needs only its two extreme endpoints: product
is concave along a negative-slope line, so its minimum is at an endpoint.
This tie rule matters for product-descent applications.

Let L include log(N+M+2) and the bit lengths of a,b. The normalized ABCS
theorems give O(L) arithmetic operations for NEXT, O(L^2) for SEEK, and
O(L^3) for the support binary search. Basis and ray coordinates have O(L)
bits up to constant factors: the primitive target-direction bound in ABCS
Lemma 3.9 is numerical-polynomial in the scaled threshold and determinant;
the Euclidean basis updates and quadratic root calculations preserve
polynomial numerical heights. All prototype arithmetic is integral. Using
integer multiplication cost M_int(L), the corresponding conservative form
is O(L^3 M_int(cL)) bit operations for a fixed constant c, including division
and square-root primitives. Preprocessing and modular inverses are polynomial
in L as well. This is a one-patch statement, independent of the hull's vertex
count. It neither optimizes over a union for free nor assumes a box theorem.

### Exact-root indexing correction

The first adaptation stalled and hit its internal 55-second alarm. The
retained source is `PATCH_SUPPORT_v0_timeout.py`. The cause was a literal use
of the candidate root indices printed in ABCS Lemma 3.16: `{r_i,r_i+1}`.
Under the paper's displayed membership-change definition, an integral entry
root can instead create a change from r_i-1 to r_i. For example N=1,
p=(0,1),v=(1,0) has root 1 but its first membership change is at m=0.

The corrected routine tests `{r_i-1,r_i,r_i+1}` and checks positive-coordinate
membership exactly. This finite superset is sufficient for each quadratic
root, including isolated tangent points. No floating tolerance is used.
This is a local indexing correction to the ray primitive, not a replacement
of the lattice-search workflow or an assertion that the whole paper is false.

## Shared structure: a binary tree of integer lower bounds

For each depth r>=1 set

    m_r = 2^min(k,2r+1), s_r=2^r.

On each odd class u modulo s_r, build the analogous affine lattice using
inverses modulo m_r. The second-difference valuation ensures that it is
exactly the inverse graph at this **coarser modulus**, within that class.
Every target-M descendant lies in it, so its integer support value is a
certified lower bound for the entire descendant subtree.

The children are u and u+s_r modulo 2s_r. Each child recomputes its modulus,
inverse residue, and shear; a parent shear is not inherited beyond its
valid modulus. Child regions are contained in the parent's region. At depth
h the modulus is M and the leaves are the root's exact patches.

For a fixed query normal:

1. Query the single root r=1,u=1 and retain its optimizer as a lower bound.
2. If that optimizer already satisfies xy=N mod M, it is a valid support
   answer for its whole subtree. With the stated tie rule, its full
   lexicographic bound is attained as well.
3. Otherwise query the two children. Process lower bounds in increasing
   order and discard nodes whose bound cannot improve a known target-valid
   incumbent. The prototype conservatively prunes only on strictly worse
   objective value, preserving all objective ties.

This is a complete exact union-support procedure even without favorable
pruning: the finite leaves form the exact cover. Its worst-case node count
remains O(sqrt(M)). The meaningful new quantity to investigate is the number
of integer lower-bound nodes actually required, not the speed of a numerical
enumerator inside a node.

## Bounded checks and observed gain

Preflight: 73% available memory, load 2.44; the root's recent process snapshot
showed only a 17 MB mathematical process. The corrected single-process run
took 0.146 seconds and used an estimated <128 MB. The timeout remains 55
seconds. Source, progress log, and JSON output are retained with the
`PATCH_SUPPORT` prefix.

Eighteen one-patch queries, covering all leaf patches at (N,k)=(10541,4)
and (147053,6), matched a separate numerical-width exhaustive search in the
script, including the full tie order. These include normals (1,1),(2,1),
and (465,317). The checks are finite validation, not the runtime proof.

Three hierarchy probes compared against all exact leaf SUPPORT results:

| N | k | Normal | Leaves | Hierarchical support calls | Returned point |
|---:|---:|---|---:|---:|---|
| 147053 | 8 | (465,317) | 8 | 1 | (307,479) |
| 147053 | 12 | (1,1) | 32 | 13 | (307,479) |
| 147053 | 12 | (3,2) | 32 | 1 | (307,479) |

All have zero defect, and all outputs match the exhaustive leaf support
cost. These examples demonstrate shared-structure pruning but give no
asymptotic claim. The separate Sol pilot in F289 studies broader query counts
with an independent enumeration oracle.

The next mathematical gap is an all-input law controlling accepted coarse
optimizers or pruned subtrees. A logarithmic one-patch oracle and a binary
hierarchy do not by themselves bound the number of live patches. No part of
the one-lattice reflection theorem is applied to this union.
