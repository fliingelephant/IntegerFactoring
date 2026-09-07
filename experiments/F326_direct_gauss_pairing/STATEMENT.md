# F326 candidate statement: direct Gauss-ranked FacRoot involution

Status: precise author-derived candidate for independent reconstruction.
This document states the result without its candidate proof.

Let N>1 be odd, let 1<=a<N with gcd(a,N)=1 and Jacobi(a,N)=+1, and let
h=(N-1)/2. Write rep(z) for the representative of z modulo N in [-h,h].
All modular products and inverses below use rep. Define

    D = {0,1,...,h} union {-y: 1<=y<=h and rep(a*y)>0}.

Nonunits are included in D. Define F on D as follows:

* F(0)=1 and F(1)=0.
* If x is a nonzero nonunit modulo N, F(x)=x.
* Otherwise x is a unit different from 1. Put w=rep(x^{-1}). Set
  F(x)=w when x>0 and w>0; set F(x)=rep(a^{-1}*w) when rep(a*x)<0
  and w<0; in the remaining cases set F(x)=-x.

For 0<=t<=h define

    K(t) = sum_{y=1}^t (floor((a*y+h)/N)-floor(a*y/N)),
    Q(t) = t-K(t), L=Q(h), d=1+h+L=N-K(h).

The proposed conclusions are:

1. d is odd and F is an involution on D. Its fixed points decode in
   deterministic polynomial bit time to either a proper divisor of N or
   a square root of a modulo N. Nonunit x gives gcd(x,N). A unit fixed
   by the first unit branch gives gcd(x-1,N). A unit fixed by the second
   unit branch gives rep(x^{-1}) as the square root.
2. The increasing-order rank R:D -> {0,...,d-1} is

       R(-y)=L-Q(y),    R(x)=L+x for x>=0.

   Both R and its inverse are computable in deterministic polynomial bit
   time using Euclidean floor sums and binary search, without factoring N.
   For rank i<L, select the (L-i)-th smallest accepted y using Q, and
   return -y. For i>=L return i-L.
3. Consequently R F R^{-1} is a uniformly polynomial-time involution on
   an explicitly computable odd interval. Its fixed-point search is a
   single direct FacRoot-to-Lonely reduction. There is no auxiliary b.
4. On the rank interval, either of the following involutions A has exactly
   one fixed point r0=L, the coordinate corresponding to x=0:

   (a) A fixes L; delete L from the interval, pair successive remaining
       ranks (compressed index j paired with j XOR 1), and restore L.
   (b) A(i)=(2L-i) mod d, using the residue in {0,...,d-1}.

   Alternately traversing R F R^{-1} edges and A edges from r0 must reach
   an F fixed point. No polynomial or quasipolynomial traversal bound is
   asserted; the elementary bound is O(d) local evaluations, d<=N.

Permitted mathematical dependencies for reconstruction are the Euclidean
algorithm, polynomial-time gcd/modular inversion, CRT, Euler's criterion
over odd prime fields, and elementary permutation signs. A polynomial-time
floor-sum algorithm should either be reconstructed or explicitly supplied.
Factoring N may be used in a mathematical proof, but cannot be an algorithmic
subroutine for rank, select, size, involution evaluation, or decoding.
