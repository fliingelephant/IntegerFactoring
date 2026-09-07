# Pair-product aggregation at every dyadic scale

**Family:** route:F31

**Status:** root-derived exact identity and a non-enumerative modular
constructor. It is a complete-pair product, not a shifted carry evaluator.
Its precise loss of mixed-cut dependence is part of the result.

## Proposed mechanism

The P238/P240 products use a first-order perturbation of one marginal.
The attempted new operation was a Vandermonde product over pairs, grouped
by their dyadic separation. Its logarithm gives quadratic and higher
carry-difference constraints. Computing the entire product before
expansion could preserve cancellations that a per-branch calculation loses.

Reader searches found no matching permutation-sign record. The nearest
Vandermonde records concern Frobenius signs, AKS minors and a rank screen;
they do not state this dyadic inverse-graph product. The primitive for an
arithmetic-progression product is already available in P238/P240. No
novelty claim is made for that primitive or for the permutation sign.

## The exact band product

Let L=2^s, s>=2, and let

    T(x)=(n-Ax)/(B+Cx), D(x)=B+Cx, K=AB+Cn,

with A,B odd, C positive even, and n an integer. For integer cuts c,d in
[0,L], use the consecutive input representatives x_i=c+i, 0<=i<L.
Let y_i be the unique representative of T(x_i) modulo L in [d,d+L).
For 1<=r<=s define

    V_r(c,d)=product_(i<j, v2(j-i)=s-r)
                     (y_j-y_i)/(T(x_j)-T(x_i)).       (1)

The map is a 2-adic isometry: its exact difference is

    T(x_j)-T(x_i)=-K*(j-i)/(D(x_i)D(x_j)).

The canonical y differences have the same valuation as j-i, so every
factor in (1) is a 2-adic unit. Denominators are inverted only after the
common power of two has been cancelled.

Put Pi_D(c)=product_(i=0..L-1) D(c+i). Then

    V_1(c,d)=sigma(c,d)*Pi_D(c)/(-K)^(L/2),
    V_r(c,d)=V_1(c,d)^(2^(r-1)) for r>=2,             (2)

where

    sigma(c,d)=(-1)^(n+c+d+(-K-1)/2+C/2).             (3)

Thus all separation scales can be aggregated with one progression
product and repeated squaring. They do not supply independent product
parameters.

## Why the signs collapse

More generally, let pi be any permutation of 0,...,L-1 preserving the
valuation of differences. In a fixed band, the absolute differences
pi(j)-pi(i), as unordered pairs, form the same multiset as j-i.
Only an orientation sign remains.

Order the vertices by their reversed binary digits. Changing to this
order does not change the band sign: the fixed reordering has the same
orientation product on the domain and image edge sets. The band consists
of pairs joining the two children of each common low-bit prefix. Each
child has 2^(r-1) leaves. Exchanging the two children reverses
2^(2r-2) pair orientations, an even number for r>=2. All other
within-child permutations leave the orientation product unchanged.
Therefore the band sign is one for r>=2. At r=1 the components are
single pairs. Their orientation product is the sign of pi, since
permuting entire two-element components has even sign.

Each vertex has 2^(r-1) partners in band r, and there are
L*2^(r-2) unordered pairs. Substitution of the exact difference above
then gives (2).

For completeness, write h_t(x)=x/(1+tx), with t even. These maps satisfy
h_t h_u=h_(t+u). The generator h_2 has one even-length cycle on the odd
stratum. On the stratum v2(x)=a>=1, its nontrivial cycles have length
2^(s-1-2a) and occur 2^a times. Hence sign(h_t)=(-1)^(t/2).
Translation by b on Z/L has sign (-1)^b. Multiplication by an odd a has
sign (-1)^((a-1)/2): split the even and odd inputs into two half-size
blocks; the two multiplication signs cancel, leaving translation by
(a-1)/2 on the odd block. Finally,

    T(x)=n/B+(-K/B^2)*h_(C/B)(x) mod L.

The two signs above give sign(T)=(-1)^(n+(-K-1)/2+C/2).
Translating the source and target cuts adds c+d to its exponent, proving
(3). This concerns full residue permutations, not a restricted interval.

## Polynomial-bit evaluation

For requested precision P, put H=floor((P-1)/v2(C)). The finite product

    Pi_D(c)=(B+Cc)^L
          *sum_(j=0..H) e_j(0,...,L-1)*(C/(B+Cc))^j mod2^P

is exact at that precision. Terms past the number of variables are zero.
The ordinary elementary coefficients through H follow from power sums
and exact integer Newton identities. Their degrees, bit heights and
number of operations are polynomial in s,P and the input lengths.
Only the odd B+Cc and K are inverted. Equation (2) then takes O(s)
additional modular powers or squarings. No pair or graph-point list is
needed by this constructor.

## The selected-window limitation

For any two source cuts and two target cuts, (2)-(3) imply exactly

    V_r(b,d)*V_r(a,c)/(V_r(a,d)*V_r(b,c))=1.            (4)

The progression product depends only on the source cut. The target cut
enters only through a separable sign, which also cancels in (4).
Thus this specific complete-pair product contrast cannot replace P239's
binomial-carry contrast. The latter retains the selected rectangle;
the former cancels its mixed-cut dependence. This does not exclude a
weighted, restricted, or different product, and is not a lower bound on
other aggregation methods.

The next useful question for this mechanism is whether a nonseparable
pair weight has a comparable non-enumerative product identity. The
unweighted scale family (2) is already completely accounted for and
must not be counted as a new independent equation at each scale.

## Primary comparison

Lerch, *Sur un theoreme arithmetique de Zolotarev* (1896), pp.34-37,
gives the multiplication-sign formula used in the standard comparison:
https://dml.cz/bitstream/handle/10338.dmlcz/501494/Lerch_01-0000-124_1.pdf
Wang-Wu, https://arxiv.org/pdf/1810.03006, Theorem1.1 and equations(3.2)-(3.6), gives a
modern transcription and nearby normalized pair-difference products.
Neither is invoked for the scale-band identity, which is proved above.
No direct precedent for that exact identity was found in this focused
check; absence from that check is not a novelty result.

## Evidence

pilot.py passed 324 band comparisons on 72 signed-parameter maps, using
129,528 direct reference pairs at L<=128. The unweighted mixed contrasts
were all one on three rectangles whose exact counts were 1,0,16. These
come from the actual N=289, M=32 graph in its L=16 quotient coordinates;
the count-one rectangle is the factor point u=v=17.

A correctly coupled large case used original M=2^65, N=9M+1, quotient
L=2^64, and 128-bit output precision. Its degree-127 progression product
and all 64 bands took 0.062 seconds with no graph or pair enumeration.
The entire pilot took 0.115 seconds and used 17,694,720 bytes peak RSS.
The large products are computed from the formula; they are not checked
by an independent numerical pair enumeration. Source, JSON, log, timeout
status and resource preflight are retained.
