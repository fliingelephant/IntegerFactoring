# F314: integer-valued symmetric powers and canonical cuts

**Family:** route:F31

Route: `route:F31`. Status: author-derived identities and bounded exact
certificates; no independent reconstruction and no promoted result.

## Question and closest prior

Can canonical interval cuts be inserted into a binary-encoded symmetric-power
character without expanding its exponentially large representation? P240
computes bounded numerical-degree moments of one canonical map; it does not
handle these sharp projectors. P227 examines different integer-valued
finite-difference families and their remote coefficients. C270 warns that
matrix rank does not establish scalar-summation complexity. The material
difference here is an integral representation carrying the entire canonical
permutation, with exact analysis of projector insertion and precision.

The focused source check found Mahler's original interpolation paper,
*An Interpolation Series for Continuous Functions of a p-adic Variable*,
J. reine angew. Math. 199 (1958), 23–34, catalogued at
https://eudml.org/doc/150354. The binomial lattice is classical. No novelty
claim is made, and no analytic interpolation theorem is needed below:
finite differences give all required lattice facts directly.

## Integral representation and the exact two-bit trace

Let L=2^s, d=L-1, A and B odd, C even, n integral, and K=AB+Cn odd.
Put g=[[-A,n],[C,B]], D(X)=B+CX, and T(X)=(n-AX)/D(X).
Let V consist of degree at most d polynomials over Q_2 taking Z_2 into Z_2.
It is free over Z_2 with basis binom(X,j), 0<=j<L: finite differences prove
one inclusion, and integer-valuedness of binomial polynomials plus continuity
proves the other. Weighted substitution

    rho(g) f(X) = D(X)^d f(T(X))

preserves V. The adjugate matrix has lower-right entry -A odd and lower-left
entry -C even, so rho(g)^(-1) also preserves V; its scalar denominator is
(-K)^d, a unit.

Evaluation at 0,...,L-1 has Pascal matrix E[i,j]=binom(i,j), hence is an
integral isomorphism. For j<L, binom(x,j) modulo two depends only on x mod L.
For nonnegative integral x this follows by coefficient extraction from
(1+t)^L=1+t^L in characteristic two; continuity extends the statement to Z_2.
Since D(x) is odd, the node matrix R=E rho(g) E^(-1) reduces to the canonical
permutation matrix U[i,j]=[j=T(i) mod L].

For arbitrary subsets I,J of the node set, define

    H(I,J)=tr(D_I R D_J R^(-1))
          =sum_{i in I,j in J} R[i,j] R^(-1)[j,i].

In fact H(I,J) equals the canonical rectangle count modulo FOUR. This holds
for every invertible integral lift R of every permutation U, without a
Möbius assumption. If j differs from the unique nonzero column y(i) of U,
both factors in R[i,j] R^(-1)[j,i] are even, so the product is zero mod four.
The identity RR^(-1)=1 makes the remaining product one mod four.

The modulus cannot universally be replaced by eight for the displayed lift.
An exact witness is

    L=8, A=3, B=5, C=2, n=7, I=[0,2), J=[0,1).
    canonical count = 0,
    H(I,J) = -231510796/258748144635 = 4 mod 8.

The denominator is odd. Full rational matrices and their exact inverse are
retained in pilot.json. The scope is the specific weighted interpolation
lift, not all possible alternative lifts.

## An O(p)-degree precision lift, with its missing contraction explicit

Write z[i,j]=R[i,j]R^(-1)[j,i]. Each is congruent to its canonical permutation
entry modulo four. For desired precision p>=1 choose m=ceil(p/2), and set

    F_m(z)=sum_{t=m}^{2m-1} binom(2m-1,t) z^t (1-z)^(2m-1-t).

This integral polynomial has degree 2m-1. It is divisible by z^m, and
1-F_m(z) is divisible by (1-z)^m, by the full binomial expansion. Therefore

    F_m(z[i,j]) = [j=y(i)] mod 2^p,
    count(I,J) = sum_{i in I,j in J} F_m(z[i,j]) mod 2^p.

Its coefficients and evaluation cost per entry are polynomial in p. There
are no nonunit divisions and no precision beyond p is required once each
z is available modulo 2^p. This gives a faithful polynomial lift, not a fast
sum: expanding F_m requires O(p) restricted Hadamard moments of z. In a
tensor-power representation, sum z[i,j]^k uses the projector onto equal-index
vectors e_i^(tensor k), not the product projector D_I^(tensor k). Ordinary
tensor characters do not insert this equal-index projector automatically.
The number of node pairs remains L^2 under literal evaluation.

## What Pascal tensor structure supplies

Modulo two E is the s-fold tensor power of [[1,0],[1,1]], in binary index
order. A prefix diagonal D_[0,h) has a width-two binary comparator circuit;
conjugating its local factors by this 2x2 matrix preserves a compact tensor
description. Thus cuts themselves are compact in this sense.

The exact coefficient-basis prefix projector P=E^(-1)D_[0,h)E has entries

    P[i,j]=delta(i,j)                 if i<h,
    P[i,j]=0                          if j>=h,
    P[i,j]=(-1)^(i+h-1) binom(i,j) binom(i-j-1,h-1-j)
                                         if i>=h and j<h.

The last block equals

    (-1)^(i+h-1) i! / ((i-h)! j! (h-1-j)! (i-j)).

It is diagonally scaled Cauchy data. This proves compact formulas for
individual entries and displacement structure, but no poly(log L) sum.

## Two precisely excluded character substitutions

1. **Reducing the ordinary symmetric-power lattice first.** The usual
   Frobenius tensor formula over F_2 only sees g mod two. It cannot describe
   this integral-lattice action. At L=8, g=[[1,1],[2,1]] reduces to an
   order-two matrix, while its canonical permutation is the eight-cycle
   0→1→6→3→4→5→2→7→0. The basis change from ordinary monomials uses factorial
   denominators, with v_2((L-1)!)=L-1-s. A naive common-denominator conversion
   therefore requires an exponentially large precision guard. This does not
   exclude another direct integral construction.

2. **Integral group-algebra replacement of the cut.** Let G contain only
   these lattice-preserving weighted Möbius operators and their inverses.
   Every reduction rho(g) mod two fixes the all-ones node vector. Every
   Z_2-linear combination of such matrices therefore sends that vector to
   a constant vector. A proper nonempty canonical projector sends it to a
   nonconstant indicator. Consequently no such projector lies in the
   Z_2 group-algebra image. This also applies to convergent integral sums.
   It excludes replacing a projector by an integral sum of group operators
   and then using uncut characters, regardless of term count. It does not
   exclude rational coefficients with even denominators, mixed character
   identities that never represent P, or nonlinear/direct scalar methods.

The uncut character remains computable by a 2x2 complete-symmetric recurrence
in polynomial cost in s, requested precision, and input bit length. Neither
of the excluded substitutions transfers this cost to cut traces. High
ordinary rank is not used as a scalar-summation obstruction here.

## Evidence, resources, and restart

Preflight used uptime, vm_stat, and ps. The sandbox rejected ps; the same
read-only command succeeded with approved resource-inspection escalation.
Load averages were 1.89/2.17/2.28. A background suggestd used one CPU core;
no large numerical research process was visible at the top of the list.
The designed pilot limit was 30 seconds and below 512 MiB; actual use was
0.074 seconds and 17,481,728 bytes peak RSS. The script installs a 30-second
alarm. Exact Fraction arithmetic checks 12 maps at L=2,4,8,16, every prefix
pair, both representation inverses, the projector formula, and the entrywise
precision lift through p=12, for 21,447 assertions. Files: pilot.py,
pilot.json, pilot.log. These finite checks complement the displayed algebra;
they do not establish an algorithmic complexity bound for the unresolved sum.

The concrete next operation is a uniform evaluator for the O(p) restricted
Hadamard moments, or a direct rational cut-character identity with explicit
denominator/precision control. No efficient implementation is provided.
