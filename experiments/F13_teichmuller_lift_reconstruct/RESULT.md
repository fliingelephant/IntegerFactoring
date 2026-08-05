# F13 blind reconstruction: the exponent-\(N\) lift

## Result

Let \(N=pq\), where \(p\ne q\) are odd primes, and let

\[
\tau_N(z)=z^N\pmod {N^2}.
\]

The corrected statement in the task is true with the following precise scopes:

- the kernel, quotient, Teichmüller, inverse-exponent, and order-congruence claims hold for units;
- the additive-defect formula also covers \(a+1\) when it is a nonunit;
- consecutive-difference claims below start after the first application of \(\tau_N\), so both compared values are in the Teichmüller image;
- the high-digit probability bound is for direct gcd tests on any fixed, nonadaptive collection of iterates of a uniformly random unit;
- no factoring equivalence, hardness result, or general impossibility theorem follows.

## 1. The full principal kernel and factorization through reduction modulo \(N\)

Let

\[
\rho:(\mathbb Z/N^2\mathbb Z)^\times\longrightarrow
(\mathbb Z/N\mathbb Z)^\times
\]

be reduction. Its kernel is exactly

\[
K=\{1+kN\pmod {N^2}:k\in\mathbb Z/N\mathbb Z\}.
\]

Indeed, every unit reducing to \(1\) has this form, the \(N\) displayed residues are distinct modulo \(N^2\), and all are units. Moreover,

\[
(1+kN)^N\equiv 1+NkN\equiv1\pmod {N^2};
\]

all higher binomial terms are also divisible by \(N^2\). Thus \(\tau_N(K)=\{1\}\). Since exponentiation is a homomorphism on the abelian unit group,

\[
\tau_N(a(1+kN))=\tau_N(a),
\]

so \(\tau_N\) factors through \(\rho\). This is the full principal kernel, not merely a subgroup killed by \(\tau_N\).

## 2. Exact local Teichmüller formula

For \(x\in\mathbb F_p\), write \([x]_p\) for its unique Teichmüller lift modulo \(p^2\):

\[
[x]_p\equiv x\pmod p,\qquad [x]_p^p=[x]_p\pmod {p^2}.
\]

For a unit \(a\), its local decomposition is uniquely

\[
a=[a\bmod p]_p(1+pu)\pmod {p^2}.
\]

Raising to \(N=pq\) kills the principal factor,

\[
(1+pu)^{pq}\equiv1+p^2qu\equiv1\pmod {p^2},
\]

and Frobenius fixes the Teichmüller factor. Hence

\[
\tau_N(a)\equiv[a\bmod p]_p^q\pmod {p^2}.
\]

Symmetrically,

\[
\boxed{\quad
\tau_N(a)=\bigl([a\bmod p]_p^q,[a\bmod q]_q^p\bigr)
\quad}
\]

under CRT modulo \(p^2q^2\). This proves locally, as well as from the kernel calculation, that the output depends only on \(a\bmod N\).

The same local formula remains valid for a nonunit input \(z\): if \(p\mid z\), then \(z^N=0\pmod {p^2}\), which agrees with \([0]_p^q=0\). This observation is used for \(z=a+1\) in the additive defect.

## 3. The quotient power map and factor-aware untwisting

Reduction identifies

\[
(\mathbb Z/N^2\mathbb Z)^\times/K
\cong(\mathbb Z/N\mathbb Z)^\times
\cong C_{p-1}\times C_{q-1}.
\]

The exponent of this group is

\[
L=\operatorname{lcm}(p-1,q-1).
\]

On a finite abelian group of exponent \(L\), the map \(x\mapsto x^N\) is invertible exactly when \(\gcd(N,L)=1\):

- if \(\gcd(N,L)=1\), choose \(e\) with \(Ne\equiv1\pmod L\); then exponentiation by \(e\) is its inverse;
- if a prime \(\ell\mid\gcd(N,L)\), one cyclic component contains an element of order \(\ell\), and exponentiation by \(N\) kills that nonidentity element.

Therefore

\[
\boxed{\quad x\mapsto x^N\text{ on the quotient is invertible}
\iff \gcd\!\left(N,\operatorname{lcm}(p-1,q-1)\right)=1.\quad}
\]

When the factors are known and this condition holds, compute

\[
e=N^{-1}\pmod L.
\]

For \(A=\tau_N(a)\), one then has

\[
A^e=\bigl([a\bmod p]_p,[a\bmod q]_q\bigr)\pmod {N^2}.
\]

For example, \(Ne\equiv1\pmod {p-1}\) and \(p\equiv1\pmod {p-1}\) imply \(qe\equiv1\pmod {p-1}\), so \(([a]_p^q)^e=[a]_p\); the \(q\)-component is identical. Reduction recovers \(a\bmod N\), while the lift recovered modulo \(N^2\) is the Teichmüller section, not an arbitrary original lift.

This is a factor-aware construction because \(L\) was formed from \(p,q\). Nothing here proves that computing an untwisting exponent is equivalent to factoring \(N\), and no such claim is made.

## 4. The \(A^{N+1}=A^{p+q}\) identity is an order congruence

Every \(A\) in the image of \(\tau_N\) lies in the product of the two local Teichmüller groups, so its local orders divide \(p-1\) and \(q-1\). Since

\[
(N+1)-(p+q)=pq+1-p-q=(p-1)(q-1),
\]

the two exponents are congruent modulo both local orders. Consequently

\[
\boxed{\quad A^{N+1}=A^{p+q}\pmod {N^2}.\quad}
\]

Equivalently, \(A^{(p-1)(q-1)}=1\). The identity holds on the Teichmüller image (more generally, whenever the order divides \(\operatorname{lcm}(p-1,q-1)\)); it need not hold for an arbitrary unit modulo \(N^2\). It is therefore an order congruence, not by itself an extraction of the hidden integer \(p+q\).

## 5. Consecutive image iterates: exact probabilities and no second stage

Let

\[
A_r=\tau_N^r(a),\qquad r\ge1,
\]

where \(a\bmod N\) is uniform in \((\mathbb Z/N\mathbb Z)^\times\). Iterating the local formula gives

\[
A_r\equiv[a\bmod p]_p^{q^r}\pmod {p^2},\qquad
A_r\equiv[a\bmod q]_q^{p^r}\pmod {q^2}.
\]

Thus

\[
A_{r+1}=A_r\pmod {p^2}
\iff [a\bmod p]_p^{q^r(q-1)}=1.
\]

The Teichmüller unit group modulo \(p^2\) is cyclic of order \(p-1\), and \(x^d=1\) has \(\gcd(d,p-1)\) solutions in that group. Therefore the exact local equality probabilities are

\[
u_{p,r}=\frac{\gcd(q^r(q-1),p-1)}{p-1},
\]

\[
u_{q,r}=\frac{\gcd(p^r(p-1),q-1)}{q-1}.
\]

The two events are independent under a uniform CRT input. A gcd of the consecutive difference with \(N\) is a proper factor exactly when one event occurs and the other does not, giving

\[
\boxed{\quad
\Pr\bigl(1<\gcd(A_{r+1}-A_r,N)<N\bigr)
=u_{p,r}+u_{q,r}-2u_{p,r}u_{q,r}.
\quad}
\]

There is no residual local valuation-one case. Both compared residues are Teichmüller lifts, and two Teichmüller lifts equal modulo \(p\) are the same lift modulo \(p^2\). Hence

\[
p\mid A_{r+1}-A_r\quad\Longrightarrow\quad
p^2\mid A_{r+1}-A_r,
\]

and similarly for \(q\). If the first gcd is \(N\), both square divisibilities hold, so the difference is already \(0\pmod {N^2}\); division by \(N\) cannot reveal a second-stage factor.

This assertion is for \(r\ge1\). Comparing the raw, arbitrary lift \(a\) with \(\tau_N(a)\) is a different experiment and is not covered. Nor are nonconsecutive pairs covered by the displayed probability formula.

## 6. Additive defect and the exact valuation-category formula

Define the one-step additive defect

\[
\Delta(a)=\tau_N(a+1)-\tau_N(a)-1\pmod {N^2}.
\]

For \(x=a\bmod p\) and \(y=a\bmod q\), its exact local forms are

\[
\boxed{\quad
\Delta_p(x)=[x+1]_p^q-[x]_p^q-1\pmod {p^2},
\quad}
\]

\[
\boxed{\quad
\Delta_q(y)=[y+1]_q^p-[y]_q^p-1\pmod {q^2}.
\quad}
\]

Here \([0]_r=0\), so the formulas include \(x=-1\) or \(y=-1\). Reducing once gives the field polynomials

\[
\Delta_p(x)\equiv(x+1)^q-x^q-1\pmod p,
\]

\[
\Delta_q(y)\equiv(y+1)^p-y^p-1\pmod q.
\]

For each prime \(s\in\{p,q\}\), partition its \(s-1\) nonzero input residues into three counts

\[
c_{s,0}=\#\{v_s(\Delta)=0\},\quad
c_{s,1}=\#\{v_s(\Delta)=1\},\quad
c_{s,2}=\#\{v_s(\Delta)\ge2\},
\]

where only divisibility modulo \(s^2\) is relevant.

Consider the exact two-stage procedure:

1. compute \(g_1=\gcd(\Delta,N)\), succeeding if it is proper;
2. only when \(g_1=N\), take the canonical \(\Delta\in[0,N^2)\), form \(\Delta/N\pmod N\), and gcd that quotient with \(N\).

The CRT categories are independent for uniform \(a\in(\mathbb Z/N\mathbb Z)^\times\). Stage one succeeds in categories

\[
(0,1),(0,2),(1,0),(2,0),
\]

and stage two adds exactly

\[
(1,2),(2,1).
\]

Therefore the exact total success probability is

\[
\boxed{
\frac{
c_{p,0}(c_{q,1}+c_{q,2})
+(c_{p,1}+c_{p,2})c_{q,0}
+c_{p,1}c_{q,2}+c_{p,2}c_{q,1}
}{(p-1)(q-1)}.}
\]

This formula is an exhaustive category identity; it does not assume that category-one roots are absent.

## 7. Twin primes

Assume now

\[
q=p+2,\qquad p>3
\]

(hence \(q>5\)). Twin primes above \((3,5)\) satisfy

\[
p\equiv5\pmod6,\qquad q\equiv1\pmod6.
\]

### The \(p\)-component

Because \(q=p+2\), reduction of the field defect gives

\[
(x+1)^q-x^q-1=(x+1)^3-x^3-1=3x(x+1)\pmod p.
\]

On \(\mathbb F_p^\times\), its sole root is \(x=-1\). At that residue the exact defect is

\[
[0]_p^q-[-1]_p^q-1=0-(-1)-1=0\pmod {p^2}.
\]

Thus

\[
(c_{p,0},c_{p,1},c_{p,2})=(p-2,0,1).
\]

### The \(q\)-component

Here \(p=q-2\equiv-1\pmod {q-1}\). For \(y\ne-1\), the field defect vanishes exactly when

\[
(y+1)^{-1}-y^{-1}-1=0
\iff y^2+y+1=0.
\]

Since \(q\equiv1\pmod3\), there are exactly two such nontrivial cube roots, in addition to the separate root \(y=-1\). All three lift to exact zeros modulo \(q^2\). For a nontrivial cube root \(y\), put \(Y=[y]_q\). Then \(Y^3=1\), and

\[
[y+1]_q=[-y^2]_q=-Y^2.
\]

Consequently

\[
[y+1]_q^{-1}-[y]_q^{-1}-1
=-Y^{-2}-Y^{-1}-1
=-Y-Y^2-1=0.
\]

The root \(y=-1\) is again identically zero. Hence

\[
(c_{q,0},c_{q,1},c_{q,2})=(q-4,0,3).
\]

Substitution in the general formula gives

\[
\Pr(\text{two-stage success})
=\frac{3(p-2)+(q-4)}{(p-1)(q-1)}
=\boxed{\frac{4(p-2)}{(p-1)(p+1)}}.
\]

Both category-one counts vanish, so stage two adds no success probability.

### Exceptional twin \((3,5)\)

The coefficient \(3\) degenerates at the smaller prime. Directly in the Teichmüller groups:

- modulo \(3^2\), the two unit inputs give categories \((0,1,1)\): at \(x=1\), the defect is \(-1-1-1=-3=6\pmod9\), while \(x=-1\) gives exact zero;
- modulo \(5^2\), the field defect is \((y+1)^3-y^3-1=3y(y+1)\pmod5\), so only \(y=-1\) is a unit root and it is exact, giving \((3,0,1)\).

The two-stage numerator is

\[
0(0+1)+(1+1)3+1\cdot1+1\cdot0=7,
\]

so the exceptional success probability is

\[
\boxed{7/8}.
\]

Here the category-one/category-two mismatch contributes the additional second-stage \(1/8\).

## 8. Canonical high digits and the balanced-family bound

For \(r\ge1\), choose the canonical representative \(A_r\in[0,N^2)\), put

\[
b_r=[A_r\bmod N]\in[0,N),
\]

and define

\[
H_r=\frac{A_r-b_r}{N}\pmod N.
\]

Because the representatives are canonical, the quotient is an ordinary integer in \([0,N)\). This convention matters.

Assume now that

\[
p<q<2p
\]

are odd primes. The low-residue map at any fixed iterate is

\[
a_p\longmapsto a_p^{q^r}\quad\text{on }\mathbb F_p^\times,
\qquad
a_q\longmapsto a_q^{p^r}\quad\text{on }\mathbb F_q^\times.
\]

Both are permutations. Certainly \(\gcd(q,p-1)=1\). Also \(p\nmid q-1\): otherwise \(0<q-1<2p\) forces \(q-1=p\), but then the odd prime \(p\) would have the even successor \(q=p+1>2\). Thus \(\gcd(p,q-1)=1\). It follows that for uniform input \(a\), each fixed \(b_r\) is uniform in \((\mathbb Z/N\mathbb Z)^\times\).

Now \(A_r\) is the unique global Teichmüller lift of \(b_r\). If \(p\mid H_r\), then

\[
A_r-b_r=NH_r
\]

is divisible by \(p^2\). Therefore

\[
b_r\equiv[b_r\bmod p]_p\pmod {p^2}.
\]

For each of the \(p-1\) nonzero residues modulo \(p\), this specifies one residue class modulo \(p^2\). The canonical interval \([0,N)\) has length

\[
N=pq<2p^2,
\]

so it contains at most two representatives of each such class. Hence

\[
\Pr(p\mid H_r)\le\frac{2(p-1)}{(p-1)(q-1)}=\frac2{q-1}.
\]

Likewise, \(q\mid H_r\) forces

\[
b_r\equiv[b_r\bmod q]_q\pmod {q^2}.
\]

Now \(N=pq<q^2\), so the canonical interval contains at most one representative of each of the \(q-1\) nonzero Teichmüller classes. Therefore

\[
\Pr(q\mid H_r)\le\frac{q-1}{(p-1)(q-1)}=\frac1{p-1}.
\]

A direct high-digit gcd succeeds only if at least one of these divisibilities occurs. For any fixed collection \(R\) of \(K\) positive iterate indices, a union bound—requiring no independence between iterates—gives

\[
\boxed{\quad
\Pr\left(\exists r\in R:\ 1<\gcd(H_r,N)<N\right)
\le K\left(\frac2{q-1}+\frac1{p-1}\right)
\le\frac{3K}{p-1}.
\quad}
\]

The last inequality uses \(q>p\).

There are infinitely many balanced pairs: take any sequence of odd primes \(p\to\infty\), and for each \(p\), Bertrand's postulate supplies a prime \(q\) with \(p<q<2p\). Thus for every fixed \(K\), the displayed upper bound tends to zero along an infinite family of balanced semiprimes.

The probability statement is deliberately narrow. It assumes a uniformly random unit and a collection of iterate indices fixed independently of that unit. It does not cover adaptive choices, specially constructed bases, cross-base combinations, or a different use of the high digits.

## 9. What has and has not been established

Established:

1. the full principal kernel and exact local image;
2. the exact quotient automorphism criterion and a factor-aware inverse;
3. the exponent identity as an order congruence;
4. exact probabilities for consecutive differences between image iterates, with no valuation-one second stage;
5. exact local additive-defect formulas and the complete two-stage valuation formula;
6. the twin-prime counts, general twin success probability, and exceptional \((3,5)\) behavior;
7. the fixed-iterate canonical-high-digit upper bound on every balanced pair and an infinite family on which it vanishes for fixed \(K\).

Not established:

- that untwisting is equivalent to factoring;
- that adaptive or special bases obey the uniform-input bounds;
- a formula for arbitrary nonconsecutive iterate differences;
- an impossibility theorem for all information in \(\mathbb Z/N^2\mathbb Z\);
- hardness or a top-level factoring result.

## 10. Independent finite certificate

`verify_reconstruction.py` exhaustively checks representative small and balanced pairs. It verifies the kernel, local Teichmüller formula, quotient criterion, factor-aware inverse, order identity, consecutive-difference root counts and valuation gap, additive categories and two-stage formula, the twin and exceptional counts, canonical-high-digit counts, uniformity of every checked low iterate, and the stated high-digit bounds.

The retained structured output reports all assertions passed. The computation is supporting evidence only; every general claim above has an independent proof.
