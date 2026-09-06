# F287 follow-up: reciprocal structure and exact local success counts

Status: author-derived identities and exact finite counts. Independent
reconstruction of these follow-up claims is pending. This file supplements
REPORT.md; it does not replace that proof or its source.

## Rational correspondence and reciprocal reduction

At a prime ell dividing N=pq, let r be the other prime. On F_ell,
t^N=t^r. With v=t^r, the original coefficient-three equation is

    t F_N(t) = v^2 + 3(t-1)v - t = 0.

When 3v-1 is nonzero this is

    t=R(v),  R(v)=v(3-v)/(3v-1).

At odd ell, 3v-1=0 cannot solve the original equation: substituting
v=1/3 leaves v^2-3v=-8/9 nonzero. At ell=3 the denominator is -1.
Thus the rational correspondence introduces no missing admissible root.

It obeys R(1/v)=1/R(v). More directly,

    F(t)=t^(2r-1)+3(t-1)t^(r-1)-1,
    t^(2r-1) F(1/t)=-F(t).

Every admissible root has a distinct reciprocal root. Indeed t=1 is
screened out, while F(-1)=-8 for odd r and odd ell. Consequently the
admissible root count is even.

Dividing by (t-1)t^(r-1) yields the reciprocal polynomial

    3 + sum_{j=-(r-1)}^(r-1) t^j
      = 4 + sum_{j=1}^{r-1} D_j(x),   x=t+t^(-1),

where D_0(x)=2, D_1(x)=x, and D_{j+1}=x D_j-D_{j-1}.
This is an exact one-variable reduction. The exponent may first be
reduced modulo ell-1 when ell is an offline known field label; doing
that in the public algorithm is not licensed by this analysis.

Two special-order cases have no admissible roots. If r=1 modulo the
order of t, v=t and the equation is 4t(t-1)=0. If r=-1 modulo that
order, v=t^(-1), and the equation after multiplication by t^2 is
(1-t)^3=0. These are exclusions for particular cyclic subgroups, not
an obstruction to the general correspondence.

The Cayley coordinates x=(v+1)/(v-1), y=(t+1)/(t-1) give
y=2/x-x where the coordinates are defined. This repackages the degree-two
map; no additive or multiplicative group homomorphism is asserted.

## Exact positive law on twin-prime semiprimes

Suppose p and q=p+2 are odd primes, p>3. In the q-field the exponent
p equals -1 modulo q-1, so there are no admissible roots. In the
p-field q equals 3 modulo p-1. Therefore

    F(t)=(t-1)(t^4+t^3+4t^2+t+1),

as a function on F_p^*. After removing t-1, put x=t+t^(-1):

    x^2+x+2=0.

For the quadratic character chi_p extended by chi_p(0)=0, the exact
number of admissible roots is

    R_p = sum_{x in F_p : x^2+x+2=0} [1+chi_p(x^2-4)].

Here x=2 and x=-2 are not roots at p>3, and none of the resulting t
is a nontrivial cube root of unity (x=-1 does not solve the quadratic).
Hence all these roots pass the t^q!=1 screen. They also have t^q!=t.

If chi_p(-7)=-1, R_p=0. If chi_p(-7)=1 and chi_p(2)=-1, R_p=2:
the two values x^2-4 have product 32, so their characters are opposite.
The character-sum formula covers the other cases without a guess.

Condition on a uniform CRT sample t modulo pq passing
gcd(t(t-1)(t^N-1),N)=1 and having Fermat gcd
gcd(t^(N-1)-1,N)=1. The p-field has p-3 choices and the q-field has
q-3 choices: precisely t=0,1,-1 are excluded in this twin-prime case.
Then the exact conditional probability that the F gcd is proper is

    R_p/(p-3).

Thus this family has an explicit positive law when R_p>0, with examples
R_29=2, R_137=4, R_239=4. The law is of order 1/p on these positive
instances and is zero on other instances, such as p=17 and p=41.
This is not an inverse-quasipolynomial success law. No infinitude claim
about twin primes or any character pattern is used.

## General local counts and comparison convention

For each field ell let E_ell be the t with t!=0,1 and t^r!=1.
Let H_ell be its subset with t^r!=t, and let Z_ell be its F roots.
Every root belongs to H_ell. Write their sizes e_ell,h_ell,z_ell.
For a uniform CRT sample conditioned on the screens E_p x E_q:

    P(F split)=[z_p(e_q-z_q)+z_q(e_p-z_p)]/(e_p e_q),
    P(Fermat split)=[(e_p-h_p)h_q+(e_q-h_q)h_p]/(e_p e_q).

Conditioning further on Fermat gcd=1 gives

    P(F split | Fermat gcd=1)
      =[z_p(h_q-z_q)+z_q(h_p-z_p)]/(h_p h_q).

These are exact counts from CRT independence, not independence assumptions
about the two tests. The source retains all numerators, denominators,
local roots and root orders. Rounded values below are only presentation.
The prime pairs are a fixed short increasing list, not random samples.

| p,q | ord_p(q), ord_q(p) | z_p,z_q | F split given Fermat gcd 1 | Fermat split on E |
| --- | --- | --- | ---: | ---: |
| 7,11 | 3,10 | 0,2 | .25000 | .26667 |
| 11,17 | 10,16 | 2,2 | .32143 | .16296 |
| 17,23 | 16,22 | 0,0 | 0 | .10794 |
| 23,31 | 11,10 | 4,0 | .20000 | .07882 |
| 31,47 | 5,46 | 0,0 | 0 | .05517 |
| 47,67 | 46,33 | 2,0 | .04545 | .03692 |
| 67,101 | 66,100 | 0,0 | 0 | .02517 |
| 101,149 | 100,148 | 0,0 | 0 | .04947 |
| 149,211 | 148,210 | 2,0 | .01370 | .01152 |
| 211,307 | 35,102 | 0,0 | 0 | .03953 |
| 307,431 | 306,215 | 0,0 | 0 | .00559 |
| 431,613 | 215,51 | 0,0 | 0 | .00396 |
| 613,887 | 612,886 | 2,0 | .00328 | .00276 |
| 887,1259 | 886,629 | 0,2 | .00159 | .00192 |
| 1259,1783 | 1258,81 | 2,2 | .00271 | .00136 |
| 1783,2521 | 891,90 | 0,0 | 0 | .01617 |

The concrete pattern is a small even number of local roots, including
many zero-root pairs. Positive conditional rates decrease as the fields
grow in this list. This does not prove a typical root count or establish
an asymptotic bound on arbitrary balanced pairs.

## Matrix witness outside both P232 order exceptions

N=187=11*17, t=3, with the original fixed A and B=diag(0,1,3), gives
ord_11(17)=10 and ord_17(11)=16. Both exceed d=3; also 17!=2*11-1.
Direct block-power derivative matrices give:

| Field | rank L_A | rank L_B | rank L_A L_B | rank L_B L_A | rank L_A L_B L_A |
| --- | ---: | ---: | ---: | ---: | ---: |
| F_11 | 6 | 6 | 5 | 5 | 4 |
| F_17 | 6 | 6 | 5 | 5 | 5 |

u=25, F=154 modulo 187, gcd(F,187)=11, and gcd(u-1,187)=1.
This establishes that the earlier witness was not dependent on a small
mutual-order exception. It does not improve the success law by itself.

## An explicit coefficient family and its order-test endpoint

The coefficient can vary through a public matrix family:

    A_h=[[0,1,1],[1,0,1],[1,h-1,0]].

Its characteristic polynomial is (x+1)(x^2-x-h), its discriminant is
(1+4h)(2-h)^2, and diag(A_h^2)=(2,h,h). On the squarefree branch,
C_(A_h) intersect V=span(A_h). Its inverse-weight pairing gives

    F_h(t)=t u^2+h(t-1)u-1.

The same triple-rank proof applies when A_h also has collision-free
N-th powers. At h=0 the eigenvalues are -1,0,1. For odd N they remain
distinct in every odd field, and L_(A_0)=P_(A_0). The scalar test becomes

    F_0(t)=t^(2N-1)-1.

This is a multiplicative-order test with public exponent 2N-1. Locally
its roots form the subgroup of order gcd(2r-1,ell-1). All its nonidentity
roots pass the previous screens and have Fermat gcd 1 locally, because
gcd(2r-1,r)=gcd(2r-1,r-1)=1. Its exact admissible root count is therefore
gcd(2r-1,ell-1)-1. This gives a positive special-order mechanism when
those gcds are large, while clearly exposing the underlying scalar test.

At h=1, F_h=(u+1)(tu-1); at h=-1, F_h=(u-1)(tu+1).
Thus several coefficient choices reduce exactly to ordinary power-residue
conditions. Uniformly sampling h does not create a density gain by itself:
for each screened t the equation has exactly one h in the field.

## Next mathematical question

Can a short public family of exponents or coefficients exploit the
reciprocal structure to create a large structured root set on one CRT
field, without reducing solely to the favorable-order event visible at
h=0? A precise candidate target is a deterministic quasipolynomial-size
list of h values with a provable split law on balanced semiprimes after
the Fermat gcd=1 condition. The evidence here supplies exact test cases
and laws for h=3 and h=0, but does not justify such a list.

Carmichael failure from REPORT.md is only a limitation of that isolated
unit family. It is not a decisive obstruction to a factoring algorithm
that includes other tests, and no Carmichael number is a distinct-prime
two-factor semiprime. The present follow-up addresses that semiprime
success question directly.

## Reproduction

`python3 experiments/F287_joint_power_operators/counts.py` produces
`counts.json`. The run used about 0.02 seconds, tiny lists and 9-by-9
matrices, under a 30-second/128-MB budget. The source stops its loop at
25 seconds. All computations use standard Python integer arithmetic;
an initial optional SymPy import was unavailable, and no result depends
on it. Factors select offline field labels only. The public witness
family and exponent depend on N and t, not on the labels.
