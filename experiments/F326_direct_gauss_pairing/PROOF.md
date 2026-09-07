# F326 independent mathematical examination

Status: candidate proof independently derived by the F323 Astra worker from
the root's proposed statement. Not a blind support reconstruction, not a
novelty determination, and not a factoring complexity result.

## The all-residue Gauss identity

For an odd N and a unit a, multiplication by a permutes all residues modulo
N, including the nonunits. Partition these residues into {0} and the pairs
{y,-y}, 1<=y<=(N-1)/2. A permutation of two-element blocks has positive
sign. Inside these blocks multiplication by a reverses the chosen positive
representative exactly K(h) times. Thus its permutation sign is (-1)^K(h).

Here is a self-contained derivation that this sign is Jacobi(a,N). For an
odd prime p, the Vandermonde product on the residues 0,...,p-1 changes under
multiplication by a by a^{p(p-1)/2}. Euler's criterion shows that this is
Legendre(a,p) modulo p. The permutation sign and Legendre symbol are both
in {+1,-1}; since p is odd, equality modulo p implies equality as integers.

For p^e, write each residue as r+p*z with 0<=r<p. The block permutation on
r has sign Legendre(a,p) raised to the odd power p^{e-1}. The induced map
inside each block is z -> a*z+c_r modulo p^{e-1}. A translation of an odd
cyclic group has positive sign, since every cycle has odd length. Therefore
each internal block map has the multiplication sign at modulus p^{e-1}.
There are p blocks, also odd. Induction gives sign Legendre(a,p)^e.

Finally, under CRT the sign of a product permutation on sets of odd sizes
is the product of the component signs. Factoring N in this proof therefore
gives the product of Legendre(a,p)^e, namely Jacobi(a,N). No step of the
algorithm needs this factorization.

Since Jacobi(a,N)=+1, K(h) is even and d=N-K(h) is odd. This is the key
distinction from a unit-only domain: the full residue permutation supplies
both the needed parity identity and a rankable subset.

## Closure, involution, and fixed-point decoding

First temporarily keep 1 fixed and omit 0. For a unit x in D put w=x^{-1}
in centered representatives. There are precisely three cases:

1. x>0,w>0. The map sends x to w and w back to x.
2. a*x<0,w<0. Put z=a^{-1}w. Then a*z=w<0 and z^{-1}=a*x<0.
   If z>0 it belongs to D automatically; if z<0 its negative product a*z
   puts it in D. Thus z is in the same second case and maps back to x.
3. Either x>0,a*x>0,w<0 or x<0,a*x<0,w>0. Negation interchanges these
   two subcases, and both x and -x are in D.

These cases exhaust the unit domain and are disjoint. In the first case,
a fixed point satisfies x^2=1. In the second case, a fixed point satisfies
(x^{-1})^2=a. The third case has no fixed point because N is odd and x is
a nonzero unit.

The point 1 is fixed by the first case. Adding 0 and replacing this one
fixed point by the transposition (0,1) preserves the involution. Its other
first-case fixed points are positive and different from 1, so they cannot
be either of the global roots +1,-1. If x^2=1 modulo N, gcd(x-1,N) cannot
be N since x is not 1 modulo N. If it were 1, x-1 would be invertible,
forcing x+1=0 modulo N, again impossible for the positive representative.
This gcd is therefore proper, including when N has repeated factors.

Every nonzero nonunit is independently fixed. Its representative has
absolute value below N and is nonzero, so its gcd with N is also proper.
This modification cannot interfere with the unit involution: multiplication,
negation, and inversion in the unit branches never produce a nonunit.

## Exact size, rank, and selection

For remainder r=a*y mod N in {1,...,N-1},

    floor((a*y+h)/N)-floor(a*y/N) = 1 iff r>h.

Thus Q(t) counts exactly the positive y<=t whose negative -y lies in D.
Negative coordinates appear in increasing order when their accepted y
appear in decreasing order. For accepted y, L-Q(y) is exactly the number
of accepted values larger than y. This proves the rank formula. Inverting
it uses the smallest y with Q(y)>=L-i for negative rank i. Since Q rises
only by 0 or 1, this y is accepted and has the required exact rank.

For completeness, the required floor sums are reducible to

    S(m,n,a,b)=sum_{0<=j<n} floor((a*j+b)/m).

Normalize a=q_a*m+a_0 and b=q_b*m+b_0 to extract
q_a*n*(n-1)/2+q_b*n. For 0<=a,b<m, let y=a*n+b. If y<m the remaining
sum is zero. Otherwise the lattice-point transpose gives the recurrence

    S(m,n,a,b)=S(a, floor(y/m), m, y mod m).

The zero-slope case terminates before division by a. Iterated normalization
and transpose follow the Euclidean algorithm. Each integer has O(log N)
bits for our inputs and sums have O(log N) bits as well (a bound O(N^2)
suffices). The recursion has O(log N) stages; even schoolbook arithmetic
gives polynomial bit complexity. In this notation

    K(t)=S(N,t,a,a+h)-S(N,t,a,a).

Selection requires O(log N) such evaluations. No unit test or hidden
factor-dependent ordering occurs in the count.

## Auxiliary matchings and finite traversal

For adjacent pairing, remove rank L and index the remaining d-1 ranks by
j=0,...,d-2. This size is even, so j XOR 1 is a fixed-point-free involution.
Restore rank L and fix it. For cyclic reflection, solving 2L-i=i modulo d
gives i=L because d is odd. Hence it also fixes only L.

Consider the colored multigraph given by nontrivial F edges and nontrivial
A edges. Every vertex has at most one edge of each color. Rank L has only
an F edge because F swaps coordinates 0 and 1. Its component is therefore
an alternating path, not a cycle. Its other endpoint must be F-fixed,
because no other rank is A-fixed. Coincident F and A edges form doubled
two-edge cycle components and cannot lie in this starting path.

Traversing from L reaches a decoded output in O(d) local evaluations.
Only the current rank and phase need be stored. This yields a polynomial
space traversal with a numerical O(N) evaluation bound. Neither exact
rankability nor the parity proof supplies a shorter path, a path-jumping
algorithm, or a useful randomized mass bound.

## Comparison with the cached paper

The domain and unit map agree with Jerabek's Lemma 4.3 after adding all
nonunits as fixed points. The paper's Lemma 4.5 makes this extension for
special constants where the domain is an interval, and its subsequent
general construction uses additional reciprocity machinery. Section 2
explicitly permits an involution on an odd interval of polynomial-time-computable size
as the Lonely formulation. Thus the proposed exact rank/select construction
meets that formulation directly if this proof and the floor-sum implementation
pass reconstruction. It does not claim that this simplification is absent
from the broader literature. No auxiliary Jacobi-negative b is needed for
this FacRoot instance; factoring still requires a suitable outer reduction
or an independent successful root-to-factor protocol.
