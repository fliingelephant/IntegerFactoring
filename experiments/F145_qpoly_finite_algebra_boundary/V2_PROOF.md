# Proof of the F145 finite-algebra boundary

## 1. Uniform nonunits

Let \(A\) be a finite-dimensional commutative algebra over
\(K=\mathbb F_r\), and let \(J=\operatorname{Jac}(A)\). The quotient is a
finite reduced commutative \(K\)-algebra, so

\[
A/J\simeq\prod_{i=1}^{s}\mathbb F_{r^{e_i}}.
\tag{1.1}
\]

The quotient map has fibres of the same size. An element of \(A\) is a
unit if and only if its image in \(A/J\) is a unit. A uniform element of
the quotient has independent uniform field coordinates. Therefore

\[
\Pr[a\in A^\times]=\prod_{i=1}^{s}(1-r^{-e_i}).
\]

The union bound gives

\[
1-\prod_i(1-r^{-e_i})
\le\sum_i r^{-e_i}
\le s/r.
\]

Since every \(e_i\ge1\) and

\[
\sum_i e_i=\dim_K(A/J)\le\dim_K A=d,
\]

we have \(s\le d\). This proves Statement (2).

Now let \(\mathcal A\) be finite free of rank \(d\) over
\(R=\mathbb Z/N\mathbb Z\). CRT gives

\[
\mathcal A\simeq\mathcal A_p\times\mathcal A_q.
\]

A uniform element gives independent uniform local elements. The determinant
of multiplication reduces to the two local determinants. Over a
finite-dimensional algebra over a field, multiplication by \(a\) is
invertible exactly when \(a\) is a unit. Thus a proper gcd occurs exactly
when one local element is a unit and the other is not. Its probability is

\[
\alpha_p(1-\alpha_q)+(1-\alpha_p)\alpha_q
=\alpha_p+\alpha_q-2\alpha_p\alpha_q.
\]

Statement (3) follows from the local bound. A union bound proves (4).
Conditional freshness is sufficient because the same bound applies after
conditioning on each prior transcript. Finally,

\[
\log_2(Md)=(\log n)^{O(1)}=o(n),
\]

whereas \(\log_2\min(p,q)=\Omega(n)\) on the stated balanced family. This
proves the exponential sparsity claim.

## 2. Monogenic etale algebras and the Krylov bound

Write a finite etale algebra as

\[
A\simeq\prod_{e\ge1}\left(\mathbb F_{r^e}\right)^{m_e},
\qquad
\sum_e e m_e=d<r.
\tag{2.1}
\]

Let \(I_r(e)\) be the number of monic irreducible polynomials of degree
\(e\) over \(\mathbb F_r\). The standard formula is

\[
I_r(e)=\frac1e\sum_{t\mid e}\mu(t)r^{e/t}.
\tag{2.2}
\]

It gives \(I_r(1)=r\). For \(e\ge2\), count elements of exact degree \(e\)
in \(\mathbb F_{r^e}\). Every proper divisor of \(e\) is at most
\(\lfloor e/2\rfloor\). A union bound over the proper subfields gives at
most

\[
\sum_{j=1}^{\lfloor e/2\rfloor}r^j\le r^e-r
\]

elements of smaller degree. Thus at least \(r\) elements have exact degree
\(e\). Each irreducible polynomial accounts for exactly \(e\) conjugates.
Consequently,

\[
I_r(e)\ge r/e.
\tag{2.3}
\]

Since

\[
m_e\le d/e<r/e\le I_r(e),
\]

we can choose \(m_e\) distinct monic irreducible polynomials of degree
\(e\). In the corresponding copies of \(\mathbb F_{r^e}\), choose roots
of these polynomials. Let \(b\) be the tuple of all chosen roots. The
component minimal polynomials are pairwise distinct. Therefore the minimal
polynomial of \(b\) is their product and has degree

\[
\sum_e e m_e=d.
\]

Hence \(1,b,\ldots,b^{d-1}\) span \(A\), which proves that \(A\) is
monogenic.

Over an algebraic closure, the \(d\) geometric coordinate maps

\[
\sigma_1,\ldots,\sigma_d:
A\longrightarrow\overline{\mathbb F}_r
\]

are distinct linear forms. Define

\[
\Delta(a)=\prod_{1\le i<j\le d}
(\sigma_i(a)-\sigma_j(a))^2.
\tag{2.4}
\]

This is the discriminant of the characteristic polynomial of multiplication
by \(a\). It descends to a polynomial over \(\mathbb F_r\), and its total
degree is \(d(d-1)\). The generator \(b\) constructed above has \(d\)
distinct conjugate coordinates, so \(\Delta(b)\ne0\). Thus \(\Delta\) is
not the zero polynomial.

If \(\Delta(a)\ne0\), multiplication by \(a\) has \(d\) distinct geometric
eigenvalues. Its minimal polynomial has degree \(d\), and the Krylov matrix
in Statement (6) has full rank. Schwartz--Zippel on the \(d\) affine
coordinates of \(a\) gives

\[
\Pr[\operatorname{rank}K(a)<d]
\le\Pr[\Delta(a)=0]
\le\min\left(1,\frac{d(d-1)}r\right).
\]

Unequal local ranks imply that at least one local Krylov matrix is not
full. A union bound proves Statement (8). For \(M\) probes that are fresh,
including probes that are conditionally fresh after an adaptive transcript,
another union bound gives

\[
\Pr[\text{some local-rank mismatch}]
\le M d(d-1)\left(\frac1p+\frac1q\right).
\]

If \(Md^2=2^{o(n)}\) and \(\min(p,q)=2^{\Omega(n)}\), the right side is
\(2^{-\Omega(n)}\). Both conditions hold in the intended specialization in
which \(M\) and the explicit algebra rank \(d\) are quasipolynomial in
\(n\) and the semiprime is balanced. This proves Statements (8a)--(8b)
without a claim for larger ranks.

## 3. Characteristic polynomial of true Frobenius

For one field factor \(\mathbb F_{r^e}\), the normal basis theorem gives a
basis in which absolute Frobenius is the permutation matrix of an
\(e\)-cycle. Its characteristic polynomial is \(T^e-1\). Characteristic
polynomials multiply across direct products, proving Statement (9).

To prove injectivity, factor over \(\mathbb Z[T]\):

\[
H_\lambda(T)
=\prod_{m\ge1}\Phi_m(T)^{c_m(\lambda)},
\qquad
c_m(\lambda)=\#\{e\in\lambda:m\mid e\}.
\tag{3.1}
\]

Unique factorization recovers all \(c_m\). The number \(b_e\) of parts
equal to \(e\) is then recovered, from large \(e\) downwards, by

\[
b_e=c_e-\sum_{j\ge2}b_{je}.
\tag{3.2}
\]

Thus \(H_\lambda=H_\mu\) implies \(\lambda=\mu\).

Each \(H_\lambda\) is a product of at most \(d\) binomials. Every
coefficient has absolute value at most \(2^d\). If
\(\lambda_p\ne\lambda_q\), some coefficient difference between
\(H_{\lambda_p}\) and \(H_{\lambda_q}\) is a nonzero integer of absolute
value at most \(2^{d+1}\).

Compute \(\chi_F\) division-free over \(R\). Enumerate every integer
partition \(\lambda\) of \(d\), form \(H_\lambda\), and take the gcd with
\(N\) of each coefficient of \(\chi_F-H_\lambda\). When
\(\lambda=\lambda_p\), all differences vanish modulo \(p\). At the
coefficient just identified, the difference modulo \(q\) is the nonzero
integer coefficient of \(H_{\lambda_q}-H_{\lambda_p}\). Assumption (10)
prevents its reduction modulo \(q\) from vanishing. The gcd is \(p\).
The symmetric argument applies to \(\lambda_q\).

There are

\[
\exp(O(\sqrt d))
\]

integer partitions of \(d\). If \(d=(\log n)^{O(1)}\), partition
enumeration, polynomial formation, a division-free characteristic
polynomial, and all gcds use quasipolynomial bit complexity. Known factors
construct \(F\) by the local powers \(X^p,X^q\bmod f\) and coefficientwise
CRT. This proves the reverse construction and the exact promise scope.

## 4. Monomial powers and hidden orders

The nonzero elements of \(\mathbb F_{r^e}\) form a cyclic group of order
\(r^e-1\). Besides the solution \(x=0\), the equation \(x^E=x\) is

\[
x^{E-1}=1.
\]

A cyclic group of order \(m\) has exactly \(\gcd(E-1,m)\) solutions to
this equation. This proves Statements (11) and (12). Statement (14) is the
case in which all nonzero elements are solutions.

Every function on \(\mathbb F_{r^e}\) has a unique polynomial
representative of degree less than \(r^e\). The additive functions are
exactly the linearized polynomials

\[
\sum_{j=0}^{e-1}c_jX^{r^j}.
\tag{4.1}
\]

Reduce \(E\) modulo \(r^e-1\), using the representative in
\(\{1,\ldots,r^e-1\}\). The function \(x^E\) is represented by the
corresponding single monomial. Uniqueness in (4.1) shows that it is
additive exactly when its exponent is one of
\(1,r,\ldots,r^{e-1}\). This proves Statement (13).

Modulo \(p-1\), one has \(p\equiv1\), and therefore

\[
N^k=(pq)^k\equiv q^k\pmod{p-1}.
\]

This proves (15). If \(q\) is a unit modulo \(p-1\), the definition of
multiplicative order gives (16). When \(e\mid k\),
\(p^k\equiv1\pmod{p^e-1}\), which gives (17). More generally, requiring
\(N^k\) to represent a Frobenius power on \(\mathbb F_{p^e}\) is exactly
the congruence

\[
N^k\equiv p^j\pmod{p^e-1}.
\]

This is an order or discrete-log relation in the hidden local modulus.
These identities locate the missing source theorem. They do not supply or
refute such a theorem.

## 5. Binomial-jet cutoff

For \(1\le k<p\), one has \(\gcd(k,N)=1\). The identity

\[
k\binom Nk=N\binom{N-1}{k-1}
\tag{5.1}
\]

then implies

\[
N\mid\binom Nk,
\]

which proves Statement (19).

At \(k=p\),

\[
\binom{pq}{p}=q\binom{pq-1}{p-1},
\]

so \(q\) divides the coefficient. Lucas's theorem in base \(p\) gives

\[
\binom{pq}{p}\equiv q\pmod p.
\tag{5.2}
\]

The base-\(p\) digits of \(pq\) are the base-\(p\) digits of \(q\) shifted
one place, while \(p\) has digit \(1\) in that place and zeros elsewhere.
Because \(p\ne q\), the right side is nonzero. Hence \(p\) does not divide
the coefficient. This proves (20).

For a balanced semiprime, \(p=2^{\Omega(n)}\), whereas every fixed
quasipolynomial numerical cutoff \(Q(n)\) satisfies

\[
\log_2 Q(n)=(\log n)^{O(1)}=o(n).
\]

Thus \(Q(n)<p\) for all sufficiently large inputs, and every coefficient
in that truncation vanishes modulo both local factors. This argument says
nothing about algorithms that address large indices in binary or process a
large interval in compressed form.

## 6. Conclusion

Parts I and II show that quasipolynomial rank and quasipolynomially many
fresh uniform probes remain far below the local-field scale. Part III
shows that the missing genuine Frobenius map is already factor-bearing on
a splitting mismatch. Part IV identifies the exact hidden-order condition
behind the simplest succinct high-degree substitute. Part V shows that the
first selective low-order jet is itself indexed by the least factor.

None of these arguments is a lower bound for general factoring, arithmetic
circuits, adaptive biased sources, or joint nonzero-value decoders.
