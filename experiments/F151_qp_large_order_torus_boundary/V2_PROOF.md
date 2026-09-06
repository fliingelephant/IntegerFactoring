# Proof of the F151 V2 large-order and torus boundary

## 1. External large-order theorem and cost

Harvey and Hittmeir, *Deterministic methods for finding elements of large
multiplicative order*, arXiv:2601.11131v2, Theorem 1.1, give a deterministic
algorithm which, on integers `N>=3` and `1<=B<N-1`, returns either a proper
factor of `N` or a unit `alpha` with

\[
\operatorname{ord}_N(\alpha)>B.
\tag{1.1}
\]

Its stated bit cost is

\[
O\!\left(
{B^{1/2}\log B\over(\log\log B)^{1/2}}\log N
\right).
\tag{1.2}
\]

For `B=2^((log n)^O(1))`, this is quasipolynomial in `n`. The harmless
small-`B` convention in the cited theorem is irrelevant because F151 takes
`B>=4`.

Compute the powers `alpha^e modulo N` iteratively for `1<=e<=B`, and take
the gcd in (3) of the statement after each multiplication. This adds
`B*poly(n)` bit operations and remains quasipolynomial.

Let `r` be a rational prime divisor of `N`. Suppose

\[
e=\operatorname{ord}_r(\alpha)\le B.
\]

Then `r` divides `gcd(alpha^e-1,N)`, so this gcd is not one. If it were all
of `N`, then `alpha^e=1 modulo N`, contradicting (1.1). Therefore it is a
proper factor. On the surviving branch no such `r` exists, which proves
(2).

This argument also covers repeated prime factors in `N`. It asserts large
order in each residue field; it does not claim a particular order modulo
each prime power. It also makes no assertion about collisions at exponents
larger than `B`.

## 2. Local injectivity and the listed null sign screens

Fix a prime `r` dividing `N`. On the surviving branch,

\[
\operatorname{ord}_r(\alpha)>B.
\tag{2.1}
\]

If `c_e=c_f modulo r`, then `alpha^(e-f)=1 modulo r`. Since
`0<|e-f|<B`, this contradicts (2.1). If `c_e=-c_f modulo r`, then
`alpha^(2(e-f))=1 modulo r`, again with a positive absolute exponent below
`B`.

If `c_ec_f=1 modulo r`, then `alpha^(e+f)=1 modulo r`. If
`c_ec_f=-1 modulo r`, then `alpha^(2(e+f))=1 modulo r`. For
`e,f<=floor(B/4)`, all nonzero exponents displayed here are at most `B`.
Thus no prime divisor of `N` divides any integer in (5), proving that all
four gcds are one.

Because `c_e` is a unit and `c_ew_e=1 modulo N`, multiplication by `c_e`
gives

\[
\gcd(c_e-w_e,N)=\gcd(c_e^2-1,N),
\]

\[
\gcd(c_e+w_e,N)=\gcd(c_e^2+1,N).
\tag{2.2}
\]

The first can have a prime divisor `r` only if `alpha^(2e)=1 modulo r`.
The second can have one only if `alpha^(4e)=1 modulo r`. Both exponents are
at most `B`, contradicting (2.1). This proves (6).

Nothing in this proof refers to the integer factorization of
`P_e=c_ew_e`. Distinct locally noninverse residues can still give exact
integer values with shared prime factors or different factorizations. Thus
carry and factor-free refinement remain open inside the current exact-value
decoder. The proof does not exclude a larger-exponent order collision or a
different decoder applied to the same public residues.

## 3. Exact scale of Pilatte's theorem

Pilatte, *Unconditional correctness of recent quantum algorithms for
factoring and computing discrete logarithms*, arXiv:2404.16450v2, takes

\[
d=\lceil\sqrt{\log N}\rceil
\]

and proves that, with high probability over the small-prime generators, the
relation lattice has a basis of Euclidean norm `exp(O(d))`. In the factoring
application the generator bound is

\[
X=d^{1000d},
\]

which does not change the following catalogue count.

Let `R=exp(Cd)` be a radius large enough to cover the stated norm bound. The
number of integer points in the enclosing coordinate box is at most

\[
(2R+1)^d=\exp(O(d^2)).
\tag{3.1}
\]

Conversely, the Euclidean ball contains the box with coordinate radius
`floor(R/sqrt(d))`, so that full ball has

\[
\exp(\Theta(d^2))
\tag{3.2}
\]

integer points for fixed positive `C` and large `d`. Since
`d^2=Theta(log N)=Theta(n)`, exhaustive enumeration of the whole promised
region has exponential size in `n`.

The theorem gives an upper norm bound, not a support bound below `d` and not
a classical sampler. Equations (3.1)--(3.2) therefore establish only the
catalogue boundary stated in Theorem 3. They do not prove that every useful
basis is dense or that no structured quasipolynomial algorithm can find it.

## 4. Failure of the direct Jacobi-torus splice

Let `r` be `p` or `q`. The local-order condition with `B>=4` implies
`alpha` is neither `1` nor `-1 modulo r`. Hence

\[
x^2-1
=
\left({\alpha-\alpha^{-1}\over2}\right)^2
\tag{4.1}
\]

is a nonzero square modulo `r`. The quadratic character is unchanged by
inversion, so

\[
\left(\frac{\Delta^{-1}(x^2-1)}r\right)
=
\left(\frac\Delta r\right).
\tag{4.2}
\]

This proves (13). Since the Jacobi symbol of `Delta` is minus one, its two
Legendre symbols are opposite. Equation (14) is equivalent to `y^2=b`, so
it is soluble in exactly one local field and has no solution modulo `N`.

In the split field, choosing a square root `s^2=Delta` would give the usual
embedding

\[
x+ys=\alpha,
\qquad
x-ys=\alpha^{-1},
\qquad
y={\alpha-\alpha^{-1}\over2s}.
\tag{4.3}
\]

The nonsplit field has no coefficient `y` with the same `x`. Therefore
(4.3) cannot be assembled as one public norm-one point over `Z/NZ` without
first separating the local components.

Finally, for every nonnegative integer `m`, the defining identity for
Chebyshev polynomials gives

\[
T_m\!\left({z+z^{-1}\over2}\right)
={z^m+z^{-m}\over2}
\]

in every ring where `2` and `z` are units. Substitute `z=alpha` to obtain
(15). The discriminant `Delta` has disappeared. Thus the Kummer projection
keeps the scalar order relation but loses the forced torus orientation.

This proves Theorem 4 and its stated scope.
