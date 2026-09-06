# F288: exact integer support points above the hyperbola

**Family:** route:F31

Status: self-contained proof candidates and exact finite enumeration. Not
promoted. The oracle implementation and full-text novelty comparison remain
separate unfinished tasks. This is not an all-input factoring algorithm.

## Object and difference from closest prior records

For positive public integers a,b, query an exact integer minimizer of

    a x+b y  over  B<=x,y<=2B, xy>=N.

Optionally restrict to one public residue coset `(x,y)=(u,v) mod M`.
The positive region xy>=N is convex. This is an integer support query, not
minimization over real arcs followed by rounding. The oracle must return a
verified integer optimizer. If the optimal face contains several points,
two secondary linear optimizations can return its extreme endpoints; select
the one with smaller product. A numerical approximate optimum is insufficient.

The candidate was stated before Rust-reader lookup. P233 only treats the
continuous global-tangent relaxation; F286's iterated packet studies rounded
real arcs. P19's exact multiplication-CVP encoding has growing dimension and
does not classify this two-dimensional convex source. No matching convex
integer-support mechanism was found by the focused catalog queries.

A fixed-dimensional convex-integer method is the intended implementation
interface. This packet does not silently assume that a generic numerical
solver has a proved polynomial bit bound. Its finite pilot implements the
oracle by exact enumeration, explicitly linear in the numerical box width.

## Positive descent identity

Given any feasible P=(x,y), query normal (a,b)=(y,x), and let Q=(u,v) be an
optimizer. Then

    2 sqrt(xyuv) <= yu+xv <= 2xy,

so uv<=xy. Equality implies equality in AM-GM and therefore Q=P. Hence every
actual move strictly reduces the integer product defect xy-N. The direction
and this verification use only public returned points.

This initially suggested a genuine adaptive source. The next result explains
why it does not give a useful descent after a support vertex is obtained.

## Reflection theorem: every unboxed hull vertex is a strict fixed point

Let L be a translate of a lattice, and define

    S = { (x,y) in L : x>0, y>0, xy>=N }.

Every vertex P=(x,y) of conv(S) uniquely minimizes the linear form yX+xY
over S.

**Proof.** Suppose Q=(u,v) differs from P and yu+xv<=2xy. The reflected point
R=2P-Q is in L. Dividing the support inequality by xy gives
u/x+v/y<=2. Both summands are positive, so both coordinates of R are positive.
Moreover,

    R_x R_y = 4xy - 2(yu+xv) + uv >= uv >= N.

Thus R is feasible, and P is the midpoint of the distinct feasible points
Q,R. This contradicts vertexhood. QED.

The result includes every modular residue coset, because it is a lattice
translate and is closed under this reflection. Thus an exact support oracle
returning an extreme optimizer has already landed at a strict fixed point
of the proposed normal update in the unboxed positive region.

For a box-constrained vertex the same argument applies whenever the reflected
point remains in the box. Moves observed only after introducing a box can
therefore arise from the added box boundaries. The theorem does not rule out
other normal choices, perturbations, joint retained constraints, or other
integer optimization queries.

## Factor points have a guaranteed support fan

Let P=(p,q), pq=N, lie in a residue coset of modulus M. Its support slope
lambda=a/b has an open interval of unique exposure containing

    (q-M)/p < lambda < (q+M)/p,

intersected with positive slopes. To see the lower bound, a tradeoff competitor
has the form Q=(p+h,q-k), where h,k are positive multiples of M. Feasibility
gives qh-pk>=hk, hence

    q/p - k/h >= k/p >= M/p.

The upper bound follows from Q=(p-h,q+k) in the same way. A competitor that
does not trade one coordinate for the other cannot improve a positive linear
objective. Strict slopes in the stated interval therefore expose P uniquely.

The lower width is useful but small: for M=1 it is 2/p. Raising M enlarges
this conditional fan but also requires selecting the correct residue coset.
No uniform all-input advantage for that selection is proved here.

For a general vertex with defect d=xy-N, a tradeoff Q=(x+h,y-k) obeys

    y/x - k/h = k/x + (Q_x Q_y-N-d)/(xh).

Unlike at d=0, the last term can be negative. This records exactly where
defect enters the fan geometry; it does not give a monotone direction toward
an unknown zero-defect vertex.

## Exact experiment and discriminating witnesses

`support.py` enumerates the points `(x,ceil(N/x))` in each box, constructs their
lower convex hull with exact integer cross products, and performs exact
binary-search support queries on that hull. All normal boundaries, basin
weights, support ties, and products use exact arithmetic.

The six labelled inputs use p=first prime >=5B/4 and q=first prime
>=floor(sqrt(2p^2)). Factors only construct and audit inputs. Every adaptive
normal is obtained from the returned point itself. The continuous uniform
normal distribution on [1/2,2] is used only to compute exact fan measures;
it is not claimed as an implementable exact continuous random sampler.

| B | Hull vertices | Strict nonfactor fixed points | Maximum moves | Direct and post-descent factor fan mass |
|---:|---:|---:|---:|---:|
| 64 | 8 | 6 | 0 | 0.542857 |
| 256 | 20 | 14 | 1 | 0.098413 |
| 1024 | 50 | 46 | 1 | 0.044282 |
| 4096 | 134 | 130 | 1 | 0.013645 |
| 16384 | 340 | 334 | 1 | 0.004902 |
| 65536 | 850 | 842 | 2 | 0.002872 |

The factor fan mass did not increase under descent in any of these six cases.
This is finite evidence only, not a general basin theorem or fitted runtime.

Two exact small witnesses are useful:

* N=10541=83*127 in [64,128]^2 has the strictly exposed nonfactor vertex
  (95,111), defect 4. Its support cone is 1<lambda<5/4; its own normal slope
  111/95 lies strictly inside. The true factors are also inside the box.
* N=158549=331*479 in [256,512]^2 has the strictly exposed vertex (350,453),
  defect 1, between neighbors (341,465) of defect 16 and (362,438) of defect 7.
  It is a strict local minimum of defect along the hull, yet is not a factor
  point. Its support cone is 5/4<lambda<4/3 and contains 453/350. Neighbor
  defects therefore do not provide a universally valid descent direction.

`output.json` retains every hull vertex, its predecessor/successor normal,
defect, next support index, terminal state, step count, and exact rational
fan width. The run took 0.049 seconds, one process, estimated memory <64 MB,
with an internal 20-second alarm. The root's fresh shared process snapshot
showed no competing mathematical job, 72% available memory, and load 1.96;
the local preceding read showed 73% and load 2.10. `run.log` is empty on success.

## Novelty check and unfinished work

Focused primary-source search found two directly relevant papers after the
mechanism and reflection proof were derived:

* Alcántara, Blanco, Criado, Santos, *On the convex hull of integer points
  above the hyperbola*, arXiv:2501.19193 (2025). Its abstract describes
  logarithmic time per enumerated vertex.
  https://arxiv.org/abs/2501.19193
* Balog and Bárány, *The integer hull of the set {xy>=N}*, arXiv:2602.06897
  (2026). Its abstract states a vertex count of order N^(1/3) log N.
  https://arxiv.org/abs/2602.06897

These abstracts confirm substantial overlap with the general source family.
They do not establish whether the reflection statement or its algorithmic
interpretation is new. Full-text retrieval through the required reference
skill has been requested from the root/shared support; comparison is pending.
No novelty claim is made. Independent reconstruction is also pending.

The concrete remaining research question is a different adaptive support
normal or joint support certificate that can leave strict nonfactor vertices
with a useful law. The self-normal map, an interior tie artifact, or raw hull
enumeration does not supply that law.
