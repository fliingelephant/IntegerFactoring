# F287 fourth cycle: what compressed rational degree does and does not amplify

Status: author-derived identities and exact finite observations; independent
reconstruction pending. No all-input success theorem is asserted.

## Experiment

For h=2,3, two cheap public paths were tested through j=bit_length(ell):

    A: R_h^j(t^N)=t,
    B: R_h^j(t^N)=R_h^j(t).

The local prime ell and partner r are offline labels only. The initial
field value t^N=t^r was used for exact local enumeration, with t!=0,1
and t^N!=t. Thus the counts condition on the elementary Fermat gcd
being1 at both factors. Every denominator is tested before its inverse;
a path stops permanently at its first pole. The two paths in B stop
separately, so subsequent equality counts never include undefined values.
Every first-pole root set is retained separately from equality root sets.

Ten balanced pairs were used, from11*17 through4001*6007, including
383*643, the earlier high-root pair. The source uses no large polynomial:
each rational step needs constant many field operations. All counts,
root sets, survivors, and first-pole stages are in iteration_counts.json.
The run took0.39 seconds, under30 seconds and128 MB.

## A: exponentially growing degree did not produce growing fixed-point sets

The degree of R_h^j is2^j, but A's root counts in this pilot were
usually0,2,or4 and were not monotone in j. The maximum was12, at
ell=101,r=149,h=2,j=4. At ell=383,r=643,h=2 the whole sequence was
0,0,0,0,2,0,0,0,0. At the partner643, h=2 gave
6,0,4,2,2,0,2,2,2,0.

Testing all stages can accumulate additional roots, but this is a union
of j tests. At ell=643,r=383,h=3 the union had20 roots, while each
stage had at most10. These observations distinguish compressed degree
from demonstrated amplification. They do not bound arbitrary maps or
longer compositions.

## B at h=2: the large amplification has an exact 2-primary explanation

Assume ell!=2,3. Let alpha,beta solve x^2-x+1=0 and
M(v)=(v-alpha)/(v-beta). For noncritical inputs x,y,

    R_2^j(x)=R_2^j(y)
      iff [M(x)/M(y)]^(2^j)=1,

provided both finite paths have survived. If alpha,beta lie in F_ell,
M maps the remaining projective points to F_ell^*. Otherwise it maps
P^1(F_ell) into the norm-one group in F_(ell^2)^*. The group order is

    m_ell=ell-chi_ell(-3).

Thus no new collision equivalences can arise after j reaches the
2-adic valuation of m_ell. Surviving collision counts can still decrease
because a previously merged path later reaches a pole. The two critical
points, when rational, swap under R_2 and require separate handling.

The pole criterion is equally explicit. Infinity has M(infinity)=1.
For finite noncritical x, its first pole is at step j exactly when M(x)
has multiplicative order2^j. This is a familiar 2-primary mechanism in
quadratic multiplicative groups, not evidence for non-group amplification.

The strongest example here was ell=383,r=643. Its group order384 has
2-part128. B's stage counts were

    2,4,10,21,27,48,74,74,74.

Each individual path had127 first-pole initial values. Of380 eligible
initial values,160 retained both paths at the end. The union of B roots
over all stages had87 elements, greater than the terminal74 because
some merged paths subsequently reached poles. At the partner643 the
group order642 has 2-part2: B had no roots at any tested stage, and
each path had only one pole label.

These local asymmetries can yield factors. Their density gain here is
fully accounted for by the large2-part. It is not uniform in prime
factors: for example both group orders at4001 and6007 have2-part2,
and their terminal B counts were0 and2.

`iteration_torus_audit.py` checked the exact equivalences in the quadratic
algebra F_ell[a]/(a^2-a+1), including split cases. It passed261,334
stage checks. This is a separate finite algebraic audit of the formula,
not an independent proof reconstruction.

## B for arbitrary h: a product of same-time collision gates

There is an exact factorization whenever the displayed denominators
are nonzero:

    R_h(x)-R_h(y)
      = (x-y)(x+y-hxy-h)/[(hx-1)(hy-1)].

For h^2!=1 the nontrivial second preimage is the Möbius involution

    J_h(x)=(x-h)/(hx-1).

Consequently, with x_i=R_h^i(x), y_i=R_h^i(y),

    x_j-y_j=(x-y) product_{i=0}^{j-1}
      [(x_i+y_i-hx_i y_i-h)/((hx_i-1)(hy_i-1))].

Before a pole, a new B equality is precisely a first same-time collision
x_i=J_h(y_i). Once the paths merge they remain equal until a pole.
Thus a final compressed-degree equality is exactly the union of j
explicit collision gates, not an automatically dense test of2^j
independent possibilities. This identity does not forbid a distribution
of iterates from making one of those gates dense; that is the missing
success-law question.

For h=3, B did grow beyond a constant finite count in several pilots.
At ell=1783,r=1259 the sequence was

    4,4,4,10,10,14,16,20,22,24,26.

At ell=6007,r=4001 it was

    2,8,8,8,8,8,8,8,10,10,12,12,14.

These are ordinary same-time coalescences under a rational map, with no
established uniform basin size. In this pilot they give small fractions
of the eligible field, rather than an inverse-quasipolynomial law.

## Non-group pole growth has a sharp first branching test

For h=3 the immediate finite preimage of infinity is1/3. Its own
preimages solve

    3x^2-6x-1=0,

whose discriminant is48. At ell!=2,3 with chi_ell(3)=-1, there are no
such preimages. Therefore the entire finite pole basin is just{1/3}:
further iteration cannot amplify denominator events for that fixed map.
This conclusion is about this pole basin only, not the other collision
or fixed-point equations.

The pilot illustrates both behaviors. At ell=6007 the first-pole counts
were1,0,0,... for h=3. At ell=887 they were
1,2,4,8,6,6,6,8,8,6, totaling55 by step10. The latter is actual pole-set
growth and is retained as a separate source of factor events. It is not
explained by the h=2 torus formula.

## Precise next gap

The next useful target is a public non-group rational family with a
provable large pole basin or same-time collision basin after only
quasipolynomially many cheap steps, asymmetric between factors with
adequate probability. For the fixed h=3 map, the quadratic-character
test already determines whether its pole tree stops immediately.
A structured parameter choice that forces useful deeper branching,
without reverting to a smooth-order torus case, would change the
mechanism. The present data does not supply such a choice or an
all-input lower bound.

Fresh load was about2.2 and no heavy work was launched. All artifacts
use new iteration_* names. No mathematical records or catalogs were
modified, and no commit was created by this worker.
