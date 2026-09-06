# F291: direction families and global dominance certificates

**Family:** route:F31

Status: new proof candidates and exact finite pilots. Not independently
reconstructed or promoted. No quasipolynomial factorization claim is made.

## Question and prior comparison

Can many coarse inverse classes be handled through common dual directions,
without running a separate Gauss reduction on each class? The object and
stride calculation were stated before prior lookup. The closest mechanism
is F288/CAP_LINES: a node chooses a short rectangle-scaled dual vector and
enumerates its translated lattice lines. The current packet studies reuse
and pruning of the **direction family**, rather than changing the per-line
quadratic test.

P47 was retrieved through the Rust reader. Its multiplier-window bounds do
not classify the input-dependent modular direction selection here. However,
the final test `C^2-4ABN is a square` is still the same classical near-tangent
linear-form mechanism described in F286/FAST_FORWARD and its Harvey source.
Counting short direction pairs is not by itself a new algorithmic improvement.

## Exact stride, root, and phase identities

Let N be odd, r>=1, s=2^r, Q=2s^2, and u odd. On its coarse patch use

    v=N/u mod Q, delta=N((u+s)^(-1)-u^(-1)) mod Q, d=delta/s.

For a primitive integer direction D=(A,B), the image of the difference
lattice under Ax+By has positive stride

    g_u(D)=gcd(As+B*delta,BQ)=s*gcd(A+B*d,2s).

Primitivity is essential in the second equality. Since

    d = -N/[u(u+s)] mod 2s,
    u(u+s) = u^2+s mod 2s,

the maximal stride Q occurs exactly when

    A(u^2+s)-BN=0 mod 2s.

This forces both A and B odd. For r>=3 the root condition is solvable exactly
when A=BN mod 8. A fixed such direction has precisely two u classes modulo s,
obtained by solving

    u^2 = BN/A-s mod 2s.

For r=2 the explicit existence test is BN=5A modulo 8, with two classes.
For r=1 it is BN=3A modulo 4, with one class.

There is an additional phase identity. At a maximal-stride class, put
C=Au+Bv mod Q. Then

    C^2-4ABN = s^2 mod Q.

Indeed Au-Bv is congruent to s modulo 2s, because A and u are odd and
`Au^2-BN=-As mod 2s`. Squaring gives the displayed equation. The two
classes u and s-u have phases C and -C modulo Q: moving u by s does not
change its form value modulo Q at maximal stride, and inversion is odd.
Thus the two classes share a direction but generally **do not share a line
phase**. That distinction is visible in the pilot.

## A genuine global direction-pruning certificate

Write R=2s, and temporarily allow any shear d modulo R. For a primitive
direction D=(A,B) with B odd, define

    g_d(D)=s*gcd(A+B*d,R),  d_star=-A/B mod R.

At d_star its stride is Q. Let F be any fixed positive weight on nonzero
primitive directions; in the implementation F is the Euclidean norm from
the CAP_LINES rectangle scaling. If a primitive direction E satisfies

    F(E)/g_d_star(E) < F(D)/Q,

then E is strictly better than D for **every** shear d modulo R. Therefore
one short-vector query at d_star can discard D for all inverse classes,
without visiting those classes.

**Proof.** Since B is odd, the capped 2-adic valuation of d-d_star equals
that of A+B*d. Writing the residue of E at d as its residue at d_star plus
E_B(d-d_star) gives

    g_d(E) >= min(g_d_star(E),g_d(D)).

If g_d_star(E)<=g_d(D), then
`F(E)/g_d(E)<=F(E)/g_d_star(E)<F(D)/Q<=F(D)/g_d(D)`.
If g_d_star(E)>g_d(D), the hypothesis also gives F(E)<F(D), while
g_d(E)>=g_d(D). The same strict conclusion follows. QED.

This certificate may use a shear d_star not realized by any inverse class;
it is still a valid algebraic domination certificate. If the maximal shear
is realized, the contrapositive says that a direction optimal at any class
must also be optimal at its own maximal-stride class. Equality is not a
strict exclusion: ties must be retained.

The certificate is a batched **candidate rejection**, not yet an efficient
enumerator of the surviving direction catalogue.

## Three infinite low-stride families can be aggregated completely

For r>=3 all inverse shears obey d(u)=-N mod 8. Hence, if

    t=v2(A-NB) is 0, 1, or 2,

the direction's stride is the constant s*2^t at every inverse class. All
directions in each of these three categories can be replaced by one
minimum-weight representative. This is an exact common-class aggregation.

It is implementable with three two-dimensional closest-vector calculations.
For category t, minimize F(A,B) on the coset

    (A-NB)=2^t mod 2^(t+1).

Its basis can be taken as `(2^(t+1),0),(N mod 2^(t+1),1)`, with translate
`(2^t,0)`. Transform by the CAP_LINES metric and Gauss-reduce. In a reduced
two-dimensional basis, checking the floor and ceiling of the target's
second orthogonal coordinate, and rounding the first coordinate for each,
finds an exact closest vector. The usual reduced-basis inequality bounds
the second-coordinate search radius below one.

A raw minimizer cannot have an odd common divisor, since dividing by it
preserves the category and decreases F. Its content is therefore a power
of two. Normalize it to a primitive vector; both its weight and its constant
stride decrease by that same power, preserving its comparison score. Thus
at most three primitive representatives dominate these infinite categories.

This removes a complete family, but that family was **not** responsible for
the observed large catalogue: none of the chosen Gauss directions in the
main reuse pilot had stride below 8s.

## Exact pilots with random and late-DFS controls

The inputs are retained seeded random and all-one-low-bit controls from
F288, with factor scale exponents 16,20,24,28. The pilot reads only N when
choosing normals, depth, directions, strides, or phases. Normals are (1,1)
and (2,1); depth is `max(2,floor(bit_length(N)/3)-3)`.

`direction_reuse.py` checks the stride, maximal-root, phase-square, and
opposite-phase identities at every visited class. It then counts common
directions and complete `(direction,stride,phase)` keys. All checks passed.

Selected results:

| Input/control | Classes | Distinct directions | Distinct direction/stride/phase keys |
|---|---:|---:|---:|
| Random, 33–34 bits, normal 1 | 128 | 45 | 126 |
| Random, 41–42 bits, normal 1 | 512 | 188 | 508 |
| Random, 57–58 bits, normal 1 | 32768 | 10928 | 30144 |
| Late DFS, 33–34 bits, normal 1 | 128 | 1 | 66 |
| Late DFS, 57–58 bits, normal 1 | 32768 | 10741 | 30030 |

In all sixteen queries, every observed direction also occurred at its two
maximal-stride classes. The dominance lemma explains the optimality part of
this observation when those classes exist; exact tie selection is a separate
implementation detail. For the random 41–42-bit normal-1 query, 2478 raw line
equations collapsed to 2458 distinct equations. Reusing the direction alone
therefore overstates the savings: most line phases remain different.

`global_dominance.py` proposed 64 primitive odd-second-coordinate directions
for each of four random/late normal cases. It issued 234 strict global
certificates from 256 proposals. Every certificate was checked over all 256
shears: 59,904 exact comparisons, with no failure. Directions actually
selected by Gauss were never incorrectly rejected. This is finite certificate
validation, not a factoring success rate or an efficient proposal theorem.

`low_layers.py` implements the three exact CVP representatives. It checked
their raw minima against 58,240 directions in a bounded coefficient square.
Those checks passed; the unbounded CVP guarantee comes from the reduced-basis
argument, not from the finite square.

## Cost, scope, and next action

Preflight showed 72% available memory and load 2.33. The reuse pilot ran in
1.01 seconds under a 25-second alarm; the global certificate pilot took
0.019 seconds under a 15-second alarm; the low-layer pilot took 0.031 seconds
under a 10-second alarm. All used one process and estimated <128 MB. Sources,
input provenance, certificates, logs, and JSON outputs are retained here.

The positive result is an exact global rejection test plus complete
aggregation of three low-stride direction families. The pilot also shows
why simple direction caching is insufficient: the dominant high-stride
catalogue still grows with the numerical class scale, and most translated
phases remain distinct. No all-input net reduction to quasipolynomial size
has been proved.

The next useful operation would enumerate surviving high-stride directions
in groups and apply the dominance certificate to a whole coefficient region,
without first proposing every primitive pair. Merely traversing all roots
u, or all short pairs (A,B), would restore the same cost. This packet does
not count that exchange as progress toward the full target.
