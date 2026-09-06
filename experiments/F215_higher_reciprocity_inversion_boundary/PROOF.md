# F215 proof

## 1. Elementary beta-two identities

Because $N=pq=2K+1$, every divisor $d\mid K$ satisfies

\[
pq\equiv1\pmod d.
\tag{1}
\]

Neither $p$ nor $q$ divides $K$: for example, reduction of
$2K=pq-1$ modulo $p$ gives $2K\equiv-1\pmod p$. Hence both are units
modulo $d$, and (1) gives

\[
q\equiv p^{-1}\pmod d.
\tag{2}
\]

Both factors are smaller than $K$. Indeed,

\[
2(K-q)=q(p-2)-1>0
\]

because $p\geq3$ and $q\geq5$. Then $p<q<K$ as well. Therefore the
least positive residues of the true inverse pair modulo $K$ are the
integer factors themselves.

The congruence (2) is the exact inversion torsor. It uses no probabilistic,
smoothness, or distribution assumption.

## 2. Cyclotomic Frobenius and decomposition

Fix $d\mid K$. Since $p,q\nmid d$, both primes are unramified in

\[
L_d=\mathbb Q(\zeta_d).
\]

The cyclotomic Artin map is

\[
\sigma_c(\zeta_d)=\zeta_d^c,
\qquad
c\in(\mathbb Z/d\mathbb Z)^\times.
\]

Thus

\[
\operatorname{Frob}_p=\sigma_p,
\qquad
\operatorname{Frob}_q=\sigma_q.
\]

Equation (2) proves

\[
\operatorname{Frob}_q=\operatorname{Frob}_p^{-1}.
\tag{3}
\]

An element and its inverse generate the same cyclic subgroup. Hence the
decomposition subgroups are identical. Equivalently,

\[
\operatorname{ord}_d(p)=\operatorname{ord}_d(p^{-1})
=\operatorname{ord}_d(q).
\]

The irreducible factors of $\Phi_d$ modulo $p$ all have degree
$\operatorname{ord}_d(p)$, and those modulo $q$ all have the same
degree. This proves the asserted boundary for residue degrees and
unlabelled decomposition data. It does not claim that every coefficient or
every attempted polynomial factorization over $\mathbb Z/N\mathbb Z$ is
identical in the two rational components.

## 3. Ray characters, genus characters, and higher reciprocity

Let $\chi$ be a one-dimensional character of the cyclotomic Galois group
or, equivalently for the rational cyclotomic statement, a Dirichlet
character modulo $d$. Put

\[
z=\chi(\sigma_p).
\]

From (3),

\[
\chi(\sigma_q)=\chi(\sigma_p^{-1})=z^{-1}.
\tag{4}
\]

The character of the composite ideal is multiplicative, so

\[
\chi(N)=\chi(p)\chi(q)=zz^{-1}=1.
\tag{5}
\]

Equation (5) also follows directly from $N\equiv1\pmod d$. Thus the
standard scalar output is a public value and imposes no equation on the
choice of $p\bmod d$: for every
$u\in(\mathbb Z/d\mathbb Z)^\times$, the pair $(u,u^{-1})$ gives the same
product.

If $\chi$ is quadratic, then $z^{-1}=z$, proving the genus assertion. In
an arbitrary abelian ideal or ray class group, the same one-line proof
applies to an inverse pair $C,C^{-1}$:

\[
\chi(C^{-1})=\chi(C)^{-1}.
\]

For a genus character the two values are again equal.

If a conductor $c$ coprime to $N$ does not divide $K$, or has an additional
$2$-part,
write

\[
\alpha=\chi(N).
\]

Multiplicativity gives

\[
\chi(q)=\alpha\chi(p)^{-1}.
\tag{6}
\]

This is the affine inversion stated in the theorem. It includes the
quadratic supplementary-sign phenomenon. For example,
$\chi_4(N)=-1$ on the present branch, so the two $\chi_4$-values are
opposite. The product still does not label the smaller factor.

Classical cubic, quartic, and octic reciprocity laws are explicit formulas
for these Artin or power-residue characters, including corrections at the
ramified primes. Transposing a symbol does not alter the information count.
For a known prime $r\mid K$, multiplicativity on the known-denominator
side gives schematically

\[
\left(\frac p{\mathfrak r}\right)_m
\left(\frac q{\mathfrak r}\right)_m
=\left(\frac N{\mathfrak r}\right)_m.
\tag{7}
\]

The right side is public. Reciprocity rewrites the two factors on the left
and adds explicit ramified-place corrections, but multiplication still
leaves only the public product. Evaluating one transposed factor requires
the unknown numerator $p$, or a choice of data above it. A fully symmetric
product over conjugate prime ideals cannot supply that choice.

## 4. Hilbert-symbol boundary

Let $F_v$ contain $\mu_m$. The $m$-th Hilbert symbol is
bimultiplicative on

\[
F_v^\times/F_v^{\times m}\times
F_v^\times/F_v^{\times m}.
\]

For public $a$, this gives

\[
(p,a)_{m,v}(q,a)_{m,v}
=(pq,a)_{m,v}
=(N,a)_{m,v}.
\tag{8}
\]

The same identity holds with the slots reversed. Global Hilbert
reciprocity says that the product over all places is one. Moving all known
places to one side can therefore determine a product of hidden local terms,
but not an ordered pair of them. Interchanging $p$ and $q$ leaves every
such equation unchanged.

There is a sharper local collapse at the known odd primes of $K$. Let
$r\mid K$ and $r\nmid m$. Consider

\[
f(X)=X^m-N\in\mathbb Z_r[X].
\]

Since $N\equiv1\pmod r$,

\[
f(1)\equiv0\pmod r,
\qquad
f'(1)=m\not\equiv0\pmod r.
\]

Hensel's lemma gives an $m$-th root of $N$ in $\mathbb Q_r$. Hence a
Hilbert symbol having $N$ in either slot is one at $r$. If $r\mid m$,
this Hensel argument is unavailable; the theorem makes no triviality claim
there. Bimultiplicativity (8) and the swap boundary remain valid.

## 5. Adaptive scalar transcript closure

At one query, the allowed factor-dependent scalar is a product of local
one-dimensional character values, or a Hilbert product. Sections 3 and 4
show that it is a function of a public global value such as $\chi(N)$ or
$(N,a)_{m,v}$. It is unchanged when the two hidden factors are swapped.

Assume inductively that the transcript through step $j$ has this property.
A rule using only public randomness and that transcript makes the same next
choice for the two orientations. The next allowed scalar again has the
product form, so the extended transcript remains invariant. Variable-length
stopping and postselection based only on the transcript preserve the same
induction.

For $d\mid K$, equation (5) is stronger than swap invariance: the
character product is identically one on every inversion candidate
$(u,u^{-1})$. This proves Theorem A5. The argument does not cover a vector
with two rational CRT coordinates, a nonlinear trace, or external
Archimedean information.

## 6. The exact input $N=527$

Direct multiplication gives

\[
527=17\cdot31=2\cdot263+1.
\]

Both 17 and 31 are prime, $17<31<34$, and $527\equiv3\pmod4$. To check
that 263 is prime, it is enough to test the primes at most
$\sqrt{263}<17$. The exact remainders are displayed by

\[
263=2\cdot131+1
=3\cdot87+2
=5\cdot52+3
=7\cdot37+4
=11\cdot23+10
=13\cdot20+3.
\]

Thus none of the primes $2,3,5,7,11,13$ divides 263.

The multiplicative group modulo a prime is cyclic, so

\[
(\mathbb Z/263\mathbb Z)^\times\cong C_{262},
\qquad 262=2\cdot131.
\tag{9}
\]

The displayed square roots are exact:

\[
65^2=4225=16\cdot263+17,
\]

\[
174^2=30276=115\cdot263+31.
\tag{10}
\]

For a homomorphism $C_{262}\to\mu_3$, the image order divides
$\gcd(262,3)=1$, so the map is trivial. For a homomorphism to
$\mu_4$ or $\mu_8$, the image order divides respectively

\[
\gcd(262,4)=2,
\qquad
\gcd(262,8)=2.
\]

Its nontrivial possibility is the unique quadratic character. Equations
(10) show that this character takes value one on both factors. This proves
Theorem B1.

The fixed-order restriction is essential. Since 17 is a nonidentity square
and the square subgroup has prime order 131, the order of 17 modulo 263 is
131. A character of order 131 can distinguish 17 from its inverse. F215
does not claim otherwise; the standard global character value remains their
product one.

## 7. Cyclotomic residue-symbol collapse at 263

Fix $m\in\{3,4,8\}$. In every case

\[
263\equiv-1\pmod m,
\]

so the order of 263 in $(\mathbb Z/m\mathbb Z)^\times$ is two. Therefore
every prime $\mathfrak R\mid263$ in $\mathbb Q(\zeta_m)$ has residue
degree two and

\[
N\mathfrak R=263^2.
\]

Let $a$ be rational and $263\nmid a$. The power-residue Euler criterion
gives

\[
\left(\frac a{\mathfrak R}\right)_m
\equiv a^{(263^2-1)/m}\pmod{\mathfrak R}.
\tag{11}
\]

The rational residue of $a$ lies in the subfield
$\mathbb F_{263}^\times$, so $a^{262}=1$. Since

\[
\frac{263^2-1}{m}
=262\cdot\frac{264}{m}
\]

and $m\mid264$ for $m=3,4,8$, the right side of (11) is one. The
power-residue symbol is the unique $m$-th root of unity with that residue,
so it is one. This proves Theorem B2 at every prime above 263, not only
after a symmetric product.

The rationality assumption matters. A nonrational primary factor in a
cyclotomic integer ring need not lie in the $\mathbb F_{263}$ subfield and
need not have trivial symbol.

## 8. Exact rational common-order bound

For a general pair $p,q$, put

\[
d_0=\gcd(p-1,q-1).
\]

Reduction of $N-1=pq-1$ modulo $p-1$ gives $q-1$, and reduction modulo
$q-1$ gives $p-1$. Hence

\[
\gcd(N-1,p-1)=d_0
=\gcd(N-1,q-1).
\tag{12}
\]

If a unit $a\bmod N$ satisfies $a^{N-1}=1\pmod N$, its two exact local
orders divide the two gcds in (12), and therefore both divide $d_0$.

There is also an exact $K$-torsion identity on the $N\equiv3\pmod4$
branch. Write

\[
q-p=2h.
\]

The factors have opposite classes modulo four, so $h$ is odd. Directly,

\[
K=\frac{q(p-1)}2+\frac{q-1}2
\equiv h\pmod{p-1},
\]

where the odd multiplier $q$ contributes $(p-1)/2$ modulo $p-1$.
Similarly,

\[
K\equiv-h\pmod{q-1}.
\]

Since $v_2(d_0)=1$,

\[
\gcd(K,p-1)=\gcd(K,q-1)=\frac{d_0}{2}.
\tag{13}
\]

For $p=17,q=31$, $d_0=\gcd(16,30)=2$. Equation (12) proves that every
$(N-1)$-return has local orders at most two. Therefore each local residue
of $a$ is $1$ or $-1$. Since $K=263$ is odd, $a^K$ has the same
local signs. Different signs give a proper gcd with $a^K-1$ or
$a^K+1$. Equal signs give exact common order one or two. This proves
Theorem B3.

## 9. Coherent non-diagonal coefficient-content extraction

Let

\[
A_m=\mathbb Z[Z]/(\Phi_m(Z)).
\]

Because $\Phi_m$ is monic, the power basis

\[
1,\zeta_m,\ldots,\zeta_m^{\varphi(m)-1}
\]

is a $\mathbb Z$-basis. It remains a basis after reduction modulo any
prime.

The assumption $\gcd(m,N)=1$ makes $\Phi_m$ separable modulo $p$ and
modulo $q$. Thus

\[
A_m/pA_m,
\qquad A_m/qA_m
\]

are finite products of finite fields. In every field component, the image
of $\zeta_m$ has exact order $m$.

We need the following exact unit fact. If $r\nmid m$ is prime and
$a\not\equiv b\pmod m$, then

\[
\zeta_m^a-\zeta_m^b
\]

is a unit in $A_m/rA_m$. Indeed, in every field component it equals

\[
\zeta_m^b(\zeta_m^{a-b}-1).
\]

The first factor is nonzero. The second is nonzero because the image of
$\zeta_m$ has exact order $m$ and $m\nmid a-b$. An element of a finite
product of fields is a unit exactly when all its components are nonzero.

Now assume (C1). At $e=a$, the congruence in the full component
$A_m/pA_m$ says that every power-basis coefficient of

\[
Y-\zeta_m^a
\]

is zero modulo $p$. Therefore $p\mid g_a$. In the full $q$-component,
the same difference is

\[
\zeta_m^b-\zeta_m^a,
\]

which is a unit by the preceding fact. In particular, not all its
power-basis coefficients vanish modulo $q$, so $q\nmid g_a$. Since
$N=pq$,

\[
g_a=p.
\]

The symmetric argument gives $g_b=q$.

There are $m$ trials, each with $\varphi(m)$ explicit coefficients of
$O(n)$ bits. Powers of $\zeta_m$ can be reduced modulo $\Phi_m$ by
ordinary polynomial arithmetic. Under the stated bounds on $m$ and
$\varphi(m)$, all serialization, polynomial reduction, coefficient gcds,
and proper-gcd verification take numerical-QP bit complexity.

This proof explains why congruence at one selected prime ideal is not enough
for coefficient content: vanishing in one field factor of $A_m/pA_m$
does not make every rational power-basis coefficient zero modulo $p$.

For the norm variant, choose a polynomial representative $y(Z)$ for
$Y$. Up to sign,

\[
\operatorname{N}_{A_m/\mathbb Z}(Y-\zeta_m^e)
=\operatorname{Res}_Z(\Phi_m(Z),y(Z)-Z^e).
\tag{14}
\]

The resultant is zero modulo a prime precisely when the two polynomials
have a common root over an algebraic closure. Thus a zero at at least one
prime above $p$, together with no zero at any prime above $q$, makes the
gcd of (14) with $N$ equal to $p$. Distinct values at one selected prime
above each rational factor do not alone prove the required no-collision at
all other primes.

## 10. Trace coefficients separate inversion orbits

Let $G$ be a finite abelian group. For $u\in G$, form the symmetric
measure

\[
\mu_u=\delta_u+\delta_{u^{-1}}.
\]

Its Fourier transform at a character $\chi\in\widehat G$ is

\[
\widehat\mu_u(\chi)
=\chi(u)+\chi(u^{-1})
=\chi(u)+\chi(u)^{-1}
=t_\chi(u).
\]

Characters form a basis for the functions on $G$, so Fourier inversion is
injective. If all traces for $u$ and $v$ agree, then

\[
\mu_u=\mu_v.
\]

Therefore the multisets

\[
\{u,u^{-1}\},
\qquad
\{v,v^{-1}\}
\]

are equal, proving $v=u$ or $v=u^{-1}$.

Now take $G=(\mathbb Z/K\mathbb Z)^\times$ and $u=p\bmod K$. Since
$\chi(N)=1$, the four divisors of the squarefree semiprime give

\[
\sum_{c\mid N}\chi(c)
=\chi(1)+\chi(p)+\chi(q)+\chi(N)
=2+\chi(p)+\chi(p)^{-1}.
\tag{15}
\]

Thus exact divisor-coefficient evaluations provide the Fourier data of the
inversion orbit. If a numerical-QP subfamily separates the live candidates
and has a numerical-QP decoder, it recovers the orbit. Section 1 then turns
the residues into the integer factors and verifies them by exact division.

Equation (15) is deliberately conditional. A full character table can be
exponential, exact roots of unity can require large representations, and
evaluating the divisor coefficient is the missing arithmetic operation.
Ordinary multiplicative reciprocity provides $\chi(N)=1$, not (15).

## 11. Relation to named cyclotomic algorithms

The Bach--Shallit cyclotomic factoring construction starts from a known
multiple of a hidden local group order $\Phi_j(p)$. Complete factorization
of

\[
2K=pq-1
\]

does not imply that $\Phi_j(p)$ or $\Phi_j(q)$ divides a known
$K$-supported exponent. Therefore that theorem is a valid positive
transition under a different hypothesis, not a consequence of the present
recursive child.

Jacobi-sum cyclotomy and the Adleman--Pomerance--Rumely/Cohen--Lenstra
framework provide primality and prime-divisor congruence tests. On a known
composite input, failure of a test identity is a compositeness certificate,
not automatically a rational zero divisor. F215 does not claim that every
Jacobi-sum computation is scalar or cannot factor. It classifies the
one-dimensional global product and identifies the additional non-diagonal
or trace object that would be needed here.

This completes all claims in the frozen statement.
