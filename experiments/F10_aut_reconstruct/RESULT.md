# Cubic automorphisms: proof-blind reconstruction

Let

\[
f=X^3+AX^2+BX+C,\qquad A_k=\mathbf F_k[X]/(f),
\]

and assume the reduction of (f) is squarefree whenever a finite-field
factorization type is discussed.  For (N=pq), (p\ne q) are odd primes and
(A_N=(\mathbf Z/N\mathbf Z)[X]/(f)).

## 1. Local classification and exact probabilities

Factoring (f) gives

| type | algebra | automorphism group | nonidentity (2)-torsion? | nonidentity (3)-torsion? |
|---|---|---:|---:|---:|
| ((111)) | (\mathbf F_\ell^3) | (S_3) | yes | yes |
| ((12)) | (\mathbf F_\ell\times\mathbf F_{\ell^2}) | (C_2) | yes | no |
| ((3)) | (\mathbf F_{\ell^3}) | (C_3) | no | yes |

Indeed, automorphisms permute isomorphic field factors and act by finite-field
Galois automorphisms inside each factor.  The linear and quadratic factors in
type ((12)) cannot be exchanged.

Among all monic cubics over (\mathbf F_\ell), the respective counts are

\[
 n_{111}=\binom{\ell}{3},\quad
 n_{12}=\ell\frac{\ell^2-\ell}{2},\quad
 n_3=\frac{\ell^3-\ell}{3},\quad
 n_{\rm nsf}=\ell^2.
\]

Thus there are (\ell^3-\ell^2) squarefree cubics, and conditional on
squarefreeness,

\[
 \Pr(111)=\frac{\ell-2}{6\ell},\qquad
 \Pr(12)=\frac12,\qquad
 \Pr(3)=\frac{\ell+1}{3\ell}.
\]

Define a (j)-mismatch to mean that exactly one of the two local algebras has
nonidentity (j)-torsion.  Local types are independent under uniform sampling
modulo (N).  With

\[
 S=\Pr(f\text{ squarefree mod }p,q)=\frac{(p-1)(q-1)}{pq},
\]

the exact probabilities are

\[
\begin{aligned}
 \Pr(M_2\mid\mathrm{sf})
   &=\frac{4pq+p+q-2}{9pq},
&\Pr(\mathrm{sf}\cap M_2)
   &=S\frac{4pq+p+q-2}{9pq},\\
 \Pr(M_3\mid\mathrm{sf})&=\frac12,
&\Pr(\mathrm{sf}\cap M_3)&=\frac S2.
\end{aligned}
\]

The second equality follows because, locally, the probability of type
((111)) or ((3)) is exactly (1/2).

## 2. Discriminant and the recognizable (3)-mismatch

Let (\Delta=\operatorname{disc}(f)).  If (\Delta\ne0\pmod\ell), write the
roots in a separable closure and put

\[
 \delta=\prod_{i<j}(r_i-r_j),\qquad \delta^2=\Delta.
\]

Frobenius permutes the roots by a permutation (\pi), so

\[
 \Delta^{(\ell-1)/2}=\delta^{\ell-1}=\operatorname{sgn}(\pi).
\]

Consequently

\[
 \left(\frac{\Delta}{\ell}\right)=
 \begin{cases}
 +1,&(111)\text{ or }(3),\\
 -1,&(12).
 \end{cases}
\]

For (N=pq), therefore,

\[
 \gcd(\Delta,N)=1,quad \left(\frac{\Delta}{N}\right)=-1
\]

is a factorization-free, exact recognition criterion for (M_3).  This proof
also covers (\ell=3); only odd characteristic and squarefreeness were used.

## 3. Coefficient equations over a general base ring

Write the proposed image of (x=X\bmod f) as

\[
 y=a+bx+cx^2.
\]

Reduction using (x^3=-Ax^2-Bx-C) gives (y^2=d_0+d_1x+d_2x^2), where

\[
\begin{aligned}
d_0&=a^2-2Cbc+ACc^2,\\
d_1&=2ab-2Bbc+(AB-C)c^2,\\
d_2&=b^2+2ac-2Abc+(A^2-B)c^2.
\end{aligned}
\]

The assignment (x\mapsto y) is an endomorphism exactly when the three
coefficients below vanish:

\[
\begin{aligned}
E_0={}&ad_0-C(bd_2+cd_1)+ACcd_2+Ad_0+Ba+C,\\
E_1={}&ad_1+bd_0-B(bd_2+cd_1)+(AB-C)cd_2+Ad_1+Bb,\\
E_2={}&ad_2+bd_1+cd_0-A(bd_2+cd_1)+(A^2-B)cd_2+Ad_2+Bc.
\end{aligned}
\]

In the basis (1,x,x^2), its matrix has columns
((1,0,0)^T,(a,b,c)^T,(d_0,d_1,d_2)^T).  Hence it is invertible exactly when

\[
D=bd_2-cd_1
 =b^3-2Ab^2c+(A^2+B)bc^2+(C-AB)c^3
\]

is a unit.  Over (\mathbf Z/N\mathbf Z), this is (\gcd(D,N)=1).

For the torsion equations, set

\[
(s_0,s_1,s_2)=\bigl(a(1+b)+cd_0,\ b^2+cd_1,\ bc+cd_2\bigr).
\]

Together with (E_0=E_1=E_2=0), the exact conditions are

\[
 \sigma^2=1\iff(s_0,s_1,s_2)=(0,1,0),
\]

and

\[
 \sigma^3=1\iff
 (s_0+as_1+d_0s_2,\ bs_1+d_1s_2,\ cs_1+d_2s_2)=(0,1,0).
\]

For either torsion identity, invertibility follows automatically; imposing the
endomorphism equations remains essential.

## 4. Exact (3)-torsion factoring theorem

CRT gives (A_N\simeq A_p\times A_q), and every global automorphism is a pair
of local automorphisms.  On the Jacobi-recognizable promise above, let (r_-)
be the prime having type ((12)).  Its (C_2) automorphism group has no
nonidentity cube-torsion.  The other local group, (S_3) or (C_3), has exactly
three cube-torsion elements.

It follows that the global cube-torsion set has exactly three elements.  For
every nonidentity one,

\[
 \sigma(x)-x=a+(b-1)x+cx^2
\]

vanishes modulo (r_-) and is not the zero vector modulo the other prime.
Therefore

\[
 \boxed{\gcd(N,a,b-1,c)=r_-}.
\]

Equivalently, at least one of the three individual coefficient gcds is the
proper factor.  The word *nonidentity* is indispensable.

Conversely, known (p,q) construct such an automorphism.  Put the identity on
the type-((12)) side.  On a type-((3)) side use Frobenius (x\mapsto x^r);
on a type-((111)) side factor into three roots and interpolate either
3-cycle.  CRT combines the three coefficients.

This gives a genuine Las Vegas equivalence with factoring distinct odd
semiprimes.  If (L=\lceil\log_2N\rceil), sample the three nonleading
coefficients uniformly modulo (N), compute (g=\gcd(\Delta,N)), and:

- return (g) if (1<g<N);
- invoke the automorphism solver only if (g=1) and
  ((\Delta/N)=-1);
- otherwise resample.

The probability of reaching a promised instance in one trial is

\[
 \frac{(p-1)(q-1)}{2pq}\ge \frac4{15},
\]

so at most (15/4) trials are expected; direct discriminant gcds only improve
this.  Rejection sampling uses fewer than (6L) expected random bits for the
three coefficients.  Each trial costs (O(M(L)\log L)) bit operations for
fast gcd/Jacobi computation (or (O(L^2)) with elementary arithmetic).
Checking the returned equations and extracting the coefficient gcd have the
same polynomial bound.  A uniform sampler from the three cube-torsion points
returns a nonidentity point with probability (2/3), hence needs (3/2)
samples on average.  A uniform sample from the whole automorphism group hits a
nonidentity cube-torsion point with probability (1/3) in the (C_3\times C_2)
case and (1/6) in the (S_3\times C_2) case.

In the reverse direction, degree-three finite-field factorization is Las Vegas
in (O(\log r)) fixed-degree field operations: on a split cubic, a random
(h) and (\gcd(h^{(r-1)/2}-1,f)) split nontrivially with probability

\[
1-\left(\frac{r+1}{2r}\right)^3-
  \left(\frac{r-1}{2r}\right)^3
=\frac{3(r^2-1)}{4r^2}\ge\frac23.
\]

Thus, after a factoring call, construction costs (O(LM(L))=
\widetilde O(L^2)) expected bit operations with standard modular
exponentiation, plus constant-size CRT work.

## 5. What is and is not true for order (2)

The exact instancewise theorem is parallel: if exactly one local type is
((3)), then every global nonidentity involution is identity on that side,
exposes its prime by the same coefficient gcd, and factors construct an
involution on the other side.

There is no corresponding Jacobi recognizer.  Jacobi (-1) permits both
((12,3)), which is an order-(2) mismatch, and ((12,111)), which is not.
Conditioned on squarefreeness and Jacobi (-1), the off-promise probability is

\[
 \Pr((12,111)\text{ in either orientation})
 =\frac13-\frac1{3p}-\frac1{3q}>0.
\]

This is a real correctness failure, not just a missing proof.  For

\[
 N=15,quad f=X^3+10X^2+6X+10,quad \Delta\equiv11\pmod {15},
\]

the types are ((12)) modulo (3) and ((111)) modulo (5), so the Jacobi
symbol is (-1).  Yet

\[
 \sigma(x)=2+3x+8x^2
\]

is an involution nonidentity at both primes and

\[
 \gcd(15,2)=\gcd(15,3-1)=\gcd(15,8)=1.
\]

Therefore random sampling plus a promise solver for exact order-(2) mismatch
does **not** justify a reduction from arbitrary semiprimes: one cannot know
when the solver is being called on-promise, and a promise solver may fail or
fail to terminate off-promise.  Such a reduction would need an additional
recognizer or an explicit total/off-promise guarantee.  This does not assert
that no different reduction can exist.

## 6. Geometric rank, rational descent, and characteristic (3)

Over a separable closure every squarefree cubic algebra is three copies of the
field.  Hence the full automorphism scheme has geometric rank (6); its
(2)-torsion and (3)-torsion subschemes have geometric ranks (4) and (3),
corresponding to

\[
\{1,\text{ three transpositions}\},\qquad
\{1,\text{ two 3-cycles}\}.
\]

These schemes remain finite étale in characteristic (3).  Rational points
are the permutations commuting with the Frobenius permutation, giving

| type | rational automorphisms | rational (\sigma^2=1) | rational (\sigma^3=1) |
|---|---:|---:|---:|
| ((111)) | 6 | 4 | 3 |
| ((12)) | 2 | 2 | 1 |
| ((3)) | 3 | 1 | 3 |

Thus the changing counts are rational descent, not changing geometric rank.
For the linear operator (\sigma-1), identity, transposition, and 3-cycle have
ranks (0,1,2), respectively.  In characteristic (3), a 3-cycle is
unipotent and ((\sigma-1)^3=0), but its rank is still (2).  Matrix equations
such as (M^3=I) considered without the endomorphism equations can be
nonreduced in characteristic (3); that does not make the finite étale
automorphism subscheme nonreduced.

No claim about *every* coordinate eliminant follows from these ranks.
Projection can merge geometric points, leading coefficients can specialize,
and an eliminant can lose information.  The safe conclusions here concern the
full finite étale schemes and the explicit coefficient gcd on a supported
automorphism.

## 7. Explicit promised examples

For (N=35), (f=X^3+2) has discriminant (-108\equiv32\pmod {35}), type
((12)) modulo (5), and type ((3)) modulo (7).  The two nonidentity
cube-torsion maps are

\[
 x\mapsto11x,\qquad x\mapsto16x,
\]

and both give (\gcd(35,b-1)=5).  The unique nonidentity involution is
(x\mapsto15x+28x^2), exposing (7).

Characteristic (3) is visible already at

\[
 N=15,qquad f=X^3+2X+5,qquad \Delta=-707\equiv13\pmod {15}.
\]

The types are ((3)) modulo (3) and ((12)) modulo (5).  The nonidentity
cube-torsion maps are (x\mapsto x+5) and (x\mapsto x+10), both exposing
(5); the involution (x\mapsto4x) exposes (3).

## Verification record

`verify.py`, run only through `run.sh` with a 120-second wall timeout,
exhaustively checked the local counts for $\ell=3,5,7,11$, all coefficient
triples for both composite examples, the stated torsion lists, mismatch counts,
and the off-promise involution.  The run finished with `status=PASS`; exact
output is in `verification.json`, the combined log in `run.log`, and failure
dispositions in `RUN_MANIFEST.md`.  These finite checks support but are not
used as proofs of the general statements above.
