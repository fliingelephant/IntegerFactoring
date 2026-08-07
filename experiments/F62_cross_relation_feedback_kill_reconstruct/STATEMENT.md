# F62 reconstruction statement

Reconstruct and check the following claims without reading any candidate proof
or audit.

Let (N\ge3). Let

\[
A_i=x_i y_i=1+k_iN,
\qquad 1\le x_i,y_i<N,
\]

be canonical inverse relations. Let (q_1,\ldots,q_r) be a complete
pairwise-coprime gcd-free block refinement of all retained endpoints, with
full nonnegative exponent vectors. For an indexed submultiset (S), put

\[
P_S=\prod_{i\in S}A_i=1+K_SN
\]

and let (E_j(S)) be the total exponent of (q_j) in (P_S). Select

\[
g=\prod_jq_j^{c_j},
\qquad 0\le c_j\le E_j(S),
\qquad 1<g<N.
\]

If (w) is the least positive inverse of (g\bmod N) and

\[
gw=1+k(g)N,
\]

then the claimed exact law is

\[
k(g)=K_S\bmod g
\]

with the least nonzero residue in ({1,\ldots,g-1}).

Check these exact witnesses:

1. (N=21), seed relations (2\cdot11=22) and
   (5\cdot17=85), selected (g=2\cdot5=10). The new relation is
   (10\cdot19=190), the new three-column square-class kernel is zero,
   and the direct screen (gcd(10-1,21)) factors.
2. (N=55), seed relations (2\cdot28=56) and
   (3\cdot37=111), selected (g=3\cdot7=21). The old square-class
   kernel is zero, but (21^2=1+8\cdot55) gives both factors.
3. (N=21), three deliberately authorized uses of (22=2\cdot11),
   selected power (g=2^3=8). The old decoder gives only global roots,
   while (8^2=1+3\cdot21) splits (21). Repeated copies are an exponent
   budget, not independent observations.
4. For every odd (t\ge3), let (g=2^t) and
   (N=(g^2-1)/3). Using (t) authorized copies of the quotient-one
   relation (N+1=2(N+1)/2), the old decoder gives only global roots,
   while the selected (g) satisfies (g^2=1+3N), and the two gcds are
   (g-1) and ((g+1)/3). Check all integrality, coprimality, magnitude,
   and bit-size claims.

Also check:

- one selected state has a unique quotient even when it has several subset
  certificates;
- reducing a selected divisor (G>N) modulo (N) is a different rule and
  does not satisfy the same quotient formula in general;
- a new complementary endpoint can introduce a new gcd-free block, so P69's
  one-block fixed-point proof does not apply;
- polynomially many explicitly selected products have polynomial bit cost,
  but exhaustive subset and exponent-vector enumeration can be exponential;
  and
- the correct all-input factoring target must first preprocess even inputs
  and perfect powers. Odd prime powers have no non-global square root of one.

The intended scope is only an exact new feedback operation relative to P69,
with explicit useful examples and an infinite special family. No all-input
selector, success probability, classical polynomial-time factoring theorem,
or publication-level novelty is claimed.

