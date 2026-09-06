# F288 full-text comparison and usable interfaces

Read on 2026-09-07 from the two project Markdown renderings and their retained
equation images. No abstract-only conclusion is used below. Both papers have
`full_text: yes` and are indexed in `.knowledge/INDEX.md`; their citation keys
are `alcantara_2025_convex` and `balog_2026_integer`. The offline cache checker
passed. Imported author spellings and BibTeX preprint metadata were corrected
against the papers; the vendored download skill is unchanged.

Sources:

* Alcántara, Blanco, Criado, Santos (ABCS), *On the convex hull of integer
  points above the hyperbola*, arXiv:2501.19193, v1, 2025.
  Local body: `.knowledge/2501.19193_on-the-convex-hull-of-integer-points-above-the-hyperbola.md`.
* Balog and Bárány (BB), *The integer hull of the set {xy>=N}*,
  arXiv:2602.06897, v1, 2026.
  Local body: `.knowledge/2602.06897_the-integer-hull-of-the-set-x-y-in-mathbb-r-2-xy-ge-n.md`.

## Novelty assessment

The general integer-hyperbola source, the fact that exact factor points are
hull vertices, and efficient access to individual vertices are already in
ABCS. Its introduction, p.1, explicitly identifies factor pairs with
hyperbola points and observes that they are hull vertices by strict convexity.
It is therefore incorrect to describe integer support access itself as a
new factoring mechanism.

More specifically, BB §3, Lemma 3.1, p.5, uses the same central reflection
body that underlies F288: for a vertex P of the integer hull, the intersection
`H_N ∩ (2P-H_N)` contains no other lattice point. BB applies Minkowski's
theorem to this body and obtains `0<=xy-N<=2 N^(1/3)` for the standard integer
lattice and positive integer N.

The explicit F288 statement that P uniquely minimizes its own normal (y,x)
was not found stated in either inspected text. However, it is a short
algebraic consequence of BB's already-used reflection argument: a competing
Q with `y Q_x+x Q_y<=2xy` has a positive reflected point `2P-Q` of product
at least N. The application to a self-normal iteration is new to this
repository, but not a defensible claim of a substantially new geometric
principle. The lattice-translate extension is equally elementary because
reflection about a point of an affine lattice preserves that affine lattice.

The explicit factor exposure interval

    (q-M)/p < a/b < (q+M)/p

for one coordinate residue coset was not found among the statements or
normal/cap arguments of either paper. F288 supplies a self-contained proof.
Classify it as an elementary new-to-repository observation, with external
novelty unestablished. Neither this interval nor the self-normal corollary
provides an all-input success law.

## Exact ABCS interfaces

The region is the **positive** branch `H_N={x>0,y>0,xy>=N}`. It is unbounded;
for Z^2 its finite vertex chain lies in [1,N]^2, with horizontal and vertical
rays at the ends. A bounding box is not part of the following theorems.

| Interface | Exact output | Source and arithmetic cost |
|---|---|---|
| FIRST | Leftmost hull vertex | Proposition 3.5: O(1), after a standard lattice basis is supplied |
| NEXT from a vertex | The next vertex in increasing x, or infinity at the end | Corollary 3.8 with Theorem 3.10; for Z^2, Theorem 1.3 gives O(log N) |
| NEXTPT from a feasible point | Furthest lattice point in the primitive minimum-slope direction to the right | Definition 3.6 and Theorem 3.10; this need not be a global hull vertex |
| SEEK(x_start) | First global hull vertex with x>=x_start | Theorem 3.14: O(log^2(N+det Lambda)) after reduction; Proposition 1.7 states the Z^2 case as O(log^2 N) |
| Enumerate | All V vertices | Corollary 3.11: O(V log(N+det Lambda)); standard case Corollary 1.4 gives O(N^(1/3) log^2 N) |

The introduction calls 1.7 a proposition and points to Corollary 3.13;
the full final SEEK statement is **Theorem 3.14**. Corollary 3.13 supplies
the logarithmic number of NEXTPT calls used inside that construction.

Algorithm 2, §3.3.3, p.25, is the concrete NEXTPT procedure. It maintains a
standard-basis-derived pair of inside/outside directions, then alternates
exact lattice ray casts. Lemmas 3.20 and 3.21 justify the search cone updates;
the proof of Theorem 3.10 relates their iteration count to Euclidean gcd
steps. Lemmas 3.15–3.16 compute a ray crossing using a constant number of
arithmetic operations including integer square roots. Thus this algorithm
is a genuine batched geometric operation, not F286's repeated ceil maps.

SEEK does not scan all preceding vertices. Proposition 3.12 proves a
halving of distance to the relevant hull edge from a nonvertex starting
point. Corollary 3.13 bounds the number of NEXTPT calls. Theorem 3.14 then
uses forward calls and reverse backtracking to identify the first global
vertex, rather than an artificial vertex created by x>=x_start.

## Arithmetic model, translations, and boxes

ABCS explicitly uses a unit-cost arithmetic model, including integer
division and integer square root. O(log N) arithmetic operations must not be
reported as O(log N) bit operations. Remark 1.6, p.4, states that for rational
inputs its bounds convert to the bit model by a multiplier M(L), with L
the input bit size and M the integer multiplication cost. A concrete
implementation must include the starting point, rational translation,
lattice basis, and query data in L and retain exact arithmetic.

Correctness of NEXTPT is stated for arbitrary **rational** lattices with a
standard basis. Its O(log(N+det Lambda)) analysis assumes a reduced sublattice
of Z^2 (Definition 3.1: both coordinate projections are Z). Proposition 3.4
computes the standard basis by gcd operations. The apparent exception
`p_y in (1,2)` in Theorem 3.10 is handled separately by Lemma 3.9 in
O(log det Lambda) arithmetic operations. It must not be omitted when rational
translations put a vertex near an asymptote.

For one residue coset `(u,v)+M Z^2`, division of both coordinates by M gives
the translated Z^2 lattice `(u/M,v/M)+Z^2` and threshold N/M^2. This is a
single rational lattice translate, within the paper's framework after the
stated normalization. The translation denominators and bit lengths still
count even if the rescaled threshold is small. This observation does not
extend the algorithm or F288 reflection to a union of different cosets.

ABCS Remark 3.22 gives a correctness extension to a general convex epigraph
when exact lattice ray casting is available, but explicitly leaves its
complexity dependent on the function. Consequently, a box-clipped support
oracle must not simply inherit the unboxed logarithmic bound. The truncated
integer hull can contain vertices absent from the global hull; §3.2.4
explicitly discusses this issue already for a one-sided x cutoff. Arbitrary
box queries need a separate truncation reduction or a suitable exact convex
integer optimizer.

## A usable unboxed support oracle, derived from SEEK and NEXT

ABCS does not directly state the arbitrary-normal support oracle used in
F288. For the standard positive Z^2 hull, the following reduction supplies
one without enumerating V vertices. This reduction is new to the repository
and should be verified before implementation.

For a,b>0, minimize `a x+b y` along the vertex chain. Consecutive edge slopes
are increasing, so the sign of `a dx+b dy` changes at most once from negative
to positive. Binary-search the **integer x-coordinate range [1,N]**, keeping
the best returned vertex:

1. Let t be the midpoint of the current range and V=SEEK(t). If no such
   vertex exists, search below t.
2. Record V and obtain W=NEXT(V).
3. If W is absent, or the objective increases on V to W, keep V as a
   candidate and search below t. No vertex lies between t and V.
4. If the objective decreases, search strictly to the right of V.
5. If the edge objective is zero, V and W are both optimal face endpoints.

The range shrinks by at least half each time. Convexity and the defining
property of SEEK ensure that no better vertex is discarded without retaining
an equally good candidate. There are O(log N) rounds, each costing
O(log^2 N) arithmetic operations for SEEK plus O(log N) for NEXT. Thus this
gives O(log^3 N) arithmetic support access, independent of V. Dot products
add the normal's bit lengths to L. Under the paper's rational bit accounting,
this is polynomial in input length, not a factoring oracle: it returns one
of many usually nonfactor vertices.

## What the 2026 theorem adds, and what to do next

BB Theorem 1.1 establishes Theta(N^(1/3) log N) vertices for the complete
standard positive hull. Lemma 3.1 supplies the narrow product-defect strip.
These are structural counting results, not a faster normal selector or a
zero-defect recovery rule. Their stated lattice is Z^2; constants and
scaling must be reconsidered before applying the defect bound to a rescaled
or translated lattice. A global vertex count also does not automatically
give a lower bound for every bounded box.

The next concrete question is now sharper: using the polynomial-cost unboxed
SUPPORT, SEEK, and NEXT interfaces, can a nonzero defect together with the
two adjacent facet normals certify a **whole interval of normals** contains
no zero-defect vertex, without visiting its internal vertices? Such a
certificate would skip actual hull vertices, which the known Euclidean
algorithm only enumerates one at a time. Self-normal descent is already
stationary, and a defect local minimum is not sufficient, as F288's exact
defect-1 witness shows. No certificate of this stronger kind is supplied by
these papers or by the current packet.
