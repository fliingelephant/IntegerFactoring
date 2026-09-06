# F275 statement — inherited monomial rows and inverse-square cycle holonomy

## Status and scope

This is a proof-only candidate. It contains no computation and no factoring
algorithm.

The first theorem identifies an exact boundary for attempts to remove
row-private parity pivots by replacing known square rows with exact products
of those rows. Such a replacement can make every old rational-prime factor
occur in many new rows. It cannot create a new useful normalized root. Every
new relation either is a structural incidence relation with global root, or
pulls back to an old square-class relation with the same root class.

The second theorem applies this boundary to a canonical inverse-square edge
source. An explicit even cycle is an exact square relation, but its normalized
root is exactly an alternating product of its public edge labels. A useful
cycle is therefore already exposed by two direct gcds on those labels.

These results do not cover additive carries, canonical reduction after a
product, or numerical rational-prime coincidences between independently
reduced rows.

## 1. Clean square rows and normalized roots

Let `N>=3` be odd. Let

\[
 a_1,\ldots,a_m>0,
 \qquad \gcd(a_i,N)=1,
\]

and let the public units `x_i mod N` satisfy

\[
 x_i^2\equiv a_i\pmod N.
\]

For a parity vector `d in F_2^m` such that

\[
 \prod_i a_i^{d_i}=r_d^2
\]

is an exact integer square, take `r_d>0` and define

\[
 \rho_a(d)
 =r_d\left(\prod_i x_i^{d_i}\right)^{-1}\pmod N.
\]

A normalized root is **global** when it is `+1` or `-1 mod N`. It is
**useful** when one of its two signed gcds with `N` is proper.

## 2. Exact inherited monomial transformation

For `1<=j<=t`, choose integers

\[
 s_j>0,
 \qquad M_{ji}\ge0,
\]

and define a new positive row

\[
 \boxed{A_j=s_j^2\prod_{i=1}^m a_i^{M_{ji}}.}       \tag{1}
\]

Assume every `A_j` is a unit modulo `N`. Give it the inherited supplied root

\[
 \boxed{
 X_j\equiv
 \varepsilon_j s_j\prod_{i=1}^m x_i^{M_{ji}}
 \pmod N,
 \qquad \varepsilon_j\in\{+1,-1\}.
 }                                                   \tag{2}
\]

For `c in F_2^t`, put

\[
 z_i(c)=\sum_j c_jM_{ji},
 \qquad
 d_i(c)=z_i(c)\bmod2.                               \tag{3}
\]

Thus `d(c)=M^T c mod 2` is the parity incidence left on the old rows.

## Theorem A — exact pullback of every monomial relation

Suppose

\[
 \prod_j A_j^{c_j}=R_c^2
\]

is an exact integer square, with `R_c>0`. Then:

1. `d(c)` is an exact square-class relation among the old rows;
2. the new normalized root is the old normalized root up to one global sign:

   \[
   \boxed{
   R_c\left(\prod_jX_j^{c_j}\right)^{-1}
   \equiv
   \left(\prod_j\varepsilon_j^{c_j}\right)
   \rho_a(d(c))
   \pmod N.
   }                                                 \tag{4}
   \]

Consequently, an inherited monomial transformation creates no useful root
class that was absent from the old square-class kernel.

### Structural-incidence corollary

If `M^Tc=0 mod 2`, then the transformed relation has normalized root

\[
 \boxed{\pm1\pmod N.}                               \tag{5}
\]

In particular, pair-product cycles, hypergraph even-incidence relations,
and exact unreduced product circuits are global decoys when their supplied
roots are inherited multiplicatively.

### Arbitrary supplied roots

For one row (1), its inherited value on the right side of (2) is itself a
public square root of `A_j mod N`. If another supplied root is used, compare
the two roots first. Their ratio squares to one. Either a signed gcd factors
`N`, or the two roots differ only by a global sign and Theorem A applies.

This direct comparison is essential. F275 does not silently assume that two
independently supplied roots are compatible.

## 3. Canonical inverse-square edges

Let `G=(V,E)` be a finite graph. Assign each vertex a positive carrier
`d_v` with `gcd(d_v,N)=1`. For an edge `e={u,v}`, define

\[
 A_e=d_ud_v                                             \tag{6}
\]

and supply a public unit `y_e` satisfying

\[
 y_e^2\equiv d_ud_v\pmod N.                            \tag{7}
\]

A factor-blind way to make one such edge is

\[
 T_y(d)=[y^2d^{-1}]_N,
 \qquad A=dT_y(d),                                    \tag{8}
\]

where the bracket is the canonical unit in `[1,N)`. The edge row is below
`N^2` and has supplied root `y`.

Every Eulerian edge set is an exact square relation because every carrier
has even degree. F275 isolates the sharper label-only formula for one simple
even cycle.

## Theorem B — even-cycle holonomy is a direct gcd

Let

\[
 v_0,e_0,v_1,e_1,\ldots,v_{2k-1},e_{2k-1},v_0
\]

be a simple even cycle, where `e_i={v_i,v_{i+1}}` and subscripts are modulo
`2k`. Put

\[
 P_0=\prod_{i\text{ even}}y_{e_i},
 \qquad
 P_1=\prod_{i\text{ odd}}y_{e_i}.                    \tag{9}
\]

The exact row product and its positive root are

\[
 \prod_i A_{e_i}=R^2,
 \qquad
 R=\prod_i d_{v_i}.                                  \tag{10}
\]

Take the positive integer product

\[
 X=\prod_i y_{e_i},
\]

which is the supplied cycle root modulo `N`. Then

\[
 \boxed{
 \rho=RX^{-1}
 \equiv P_0P_1^{-1}
 \equiv P_1P_0^{-1}
 \pmod N.
 }                                                    \tag{11}
\]

Moreover, the exact relation gcds equal the alternating-label gcds:

\[
 \boxed{
 \gcd(R-X,N)=\gcd(P_0-P_1,N),
 }                                                    \tag{12}
\]

\[
 \boxed{
 \gcd(R+X,N)=\gcd(P_0+P_1,N).
 }                                                    \tag{13}
\]

Thus an explicit inverse-square even cycle has only two outcomes.

1. One alternating-label gcd is proper. The public edge labels already
   factor `N`, without integer factorization or a P66 decode.
2. The cycle root is global. The guaranteed graph relation is a decoy.

The theorem does not classify odd cycles or square-class relations caused by
additional arithmetic dependencies among the vertex carriers.

## 4. Reduced complement products are outside Theorem A

For a canonical unit `1<=a<N` and a positive even exponent `E`, put

\[
 U_E(a)=[a^E]_{N^2},
 \qquad Y_E(a)=[a^{E/2}]_N.                           \tag{14}
\]

The unreduced complement product

\[
 P_E(a)=U_E(a)U_E(N-a)                               \tag{15}
\]

is an exact monomial in two prior rows. Its inherited root is
`Y_E(a)Y_E(N-a)`, so Theorem A applies.

The reduced complement product is instead

\[
 \boxed{
 C_E(a)=[(a(N-a))^E]_{N^2}
       =[P_E(a)]_{N^2}.
 }                                                    \tag{16}
\]

It has public root `a^E mod N`, up to a global sign. Write

\[
 a^2=qN+r,
 \qquad 1\le r<N,
 \qquad c=N-r,
 \qquad t=a-q-1.
\]

Then

\[
 a(N-a)=c+tN,
 \qquad c=[-a^2]_N,                                  \tag{17}
\]

so (16) is a deterministic, `a`-correlated principal-lift section above the
canonical base `c`.

Canonical reduction changes an exact product by an additive multiple of
`N^2`. It need not preserve any rational-prime factor of either operand.
Therefore Theorem A gives no rank, private-pivot, or root-image conclusion
for `C_E(a)` unless the reduction is vacuous.

F268 and the proposed F270 union use only canonical `t=0` scalar rows
`U_E(b)`. They can contain the two operand rows in (15), but they do not
contain the reduced row (16) as that operation. Thus (16) is genuinely
outside the frozen F268 row grammar and the proposed F270 arithmetic grammar.
F275 proves no success law or failure law for it.

## 5. Search consequence

F268-D04 found a nonsquare private parity pivot for every row of every
separate tested scalar bank. The proposed F270 analysis rebuilds one
gcd-free block system after uniting all twelve already authenticated
same-modulus families. Cross-family sharing can remove a pivot even when
each separate bank has full rank, so that union is not an inherited-monomial
decoy and is not closed by Theorem A.

Among the compared scalar proposals, F270 remains the justified next
search. F275 does not justify a new complement-product production packet:
the unreduced version is closed by Theorem A, while the reduced version no
longer deliberately preserves or shares operand factors. A later reduced-
section search would need a separate mechanism predicting repeated pivot
loss or a useful root law before resource-bearing implementation.
