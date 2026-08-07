# F83 hostile audit — prime-saturation decoder

## Verdict: PASS

I audited
`experiments/F83_prime_saturation_decoder/RESULT.md` at SHA-256

```text
9fef7c952aa61895552374f6f64e360f09c25d4ec12b2fa8937727f8f0fd4163
```

The hash matches the requested artifact. This was a proof-only audit. I ran
no research computation.

The canonical root map, local-kernel classification, density formula,
support-two completeness theorem, binary specialization, and bit-complexity
claim are correct. The decoder uses no hidden factor, local order, or local
character.

The \(N=215\) witness proves exactly the separation it states:
\(3\)-saturation has a useful relation while \(2\)-saturation has no
nonzero relation. It does not prove that odd-prime saturation is necessary
against all simple endpoint screens. In fact,

\[
\gcd(8+27,215)=5,
\]

and the equivalent inverse-endpoint discriminant screen also factors. The
candidate names only endpoint sign and difference gcds, which are indeed
trivial, and its final scope makes no exclusivity or novelty claim. This is
therefore a scope limit, not a counterexample to a stated theorem.

## 1. Exact roots are well-defined

For \(c\in V=\ker(E\bmod\ell)\), choose the displayed representatives
\(0\leq c_i<\ell\). For every block row \(j\),

\[
\sum_i e_{ji}c_i\equiv0\pmod\ell.
\]

Thus each exponent

\[
\frac{\sum_i e_{ji}c_i}{\ell}
\]

in \(\widetilde R(c)\) is a nonnegative integer. Raising to the
\(\ell\)-th power gives the exact identity

\[
\widetilde R(c)^\ell
=\prod_jq_j^{\sum_i e_{ji}c_i}
=\prod_iA_i^{c_i}.
\]

Every \(A_i\equiv1\pmod N\), so \(R(c)^\ell\equiv1\pmod N\). Since all
blocks are units, every \(R(c)\) is a unit.

Pairwise coprimality of the blocks is appropriate provenance for the
relation presentation, but the homomorphism proof itself needs only the
exact block exponent representation and \(A_i\equiv1\).

## 2. Canonical lifts do not break the homomorphism

Let \(c,d\) use canonical coordinate representatives, and let
\(e=c+d\) in \(\mathbb F_\ell^m\), again with canonical representatives.
There is an integer carry vector \(t\) such that

\[
c+d=e+\ell t.
\]

Comparing the block exponent of \(q_j\) gives

\[
\frac{\sum_i e_{ji}c_i}{\ell}
+\frac{\sum_i e_{ji}d_i}{\ell}
=\frac{\sum_i e_{ji}e_i}{\ell}
+\sum_i e_{ji}t_i.
\]

Therefore, as exact positive integers,

\[
\widetilde R(c)\widetilde R(d)
=\widetilde R(e)\prod_iA_i^{t_i}.
\]

The carry factor is congruent to \(1\pmod N\). Hence

\[
R(c)R(d)\equiv R(e)\pmod N.
\]

Taking least nonnegative or least positive canonical representatives does
not alter the local residue. The map \(\rho\) is a homomorphism into the
two local root groups. No invalid exact-integer multiplicativity is claimed.

## 3. Local hyperplanes and the gcd gate

The group \(\mu_\ell(\mathbb F_r)\) has order
\(\gcd(\ell,r-1)\). Because \(\ell\) is prime, this order is either \(1\)
or \(\ell\). This remains true if \(\ell=r\): then the only
\(\ell\)-th root of one in \(\mathbb F_\ell\) is one.

Thus each local image of the elementary abelian group \(V\) is trivial or
cyclic of order \(\ell\). Its kernel is respectively all of \(V\) or a
codimension-one subspace. After a hidden identification of a nontrivial
root group with the additive group \(\mathbb F_\ell\), the local map is an
\(\mathbb F_\ell\)-linear functional.

For \(N=pq\),

\[
\gcd(R(c)-1,N)
\]

is proper exactly when \(R(c)=1\) in one local field and not in the other.
This is precisely membership in
\(K_p\mathbin\triangle K_q\). The decoder computes the public residue and
gcd; the two hidden kernels occur only in the proof.

## 4. Exact density

Let the two local functional ranks be \(d_p,d_q\in\{0,1\}\), and let their
joint rank be \(d\). Uniform \(c\in V\) satisfies

\[
\Pr(c\in K_p)=\ell^{-d_p},
\qquad
\Pr(c\in K_q)=\ell^{-d_q},
\]

and

\[
\Pr(c\in K_p\cap K_q)=\ell^{-d}.
\]

Symmetric-difference inclusion-exclusion yields

\[
\Pr(c\in K_p\mathbin\triangle K_q)
=\ell^{-d_p}+\ell^{-d_q}-2\ell^{-d}.
\]

If exactly one local map is zero, the ranks are \(0,1,1\), and the density
is

\[
1-\frac1\ell.
\]

If both are nonzero with distinct kernels, they are linearly independent,
so the ranks are \(1,1,2\), and the density is

\[
\frac2\ell-\frac2{\ell^2}
=\frac{2(\ell-1)}{\ell^2}.
\]

If the kernels agree, both maps are zero or the two nonzero functionals are
proportional. In either case the formula is zero. For numerically
polynomial-size \(\ell\), either positive value is inverse polynomial.

## 5. Support-two completeness: immediate basis cases

Choose any basis \(b_1,\ldots,b_D\). After hidden local identifications,
write the two functionals as coefficient vectors

\[
\alpha_i=\alpha(b_i),\qquad
\beta_i=\beta(b_i).
\]

If \(\alpha_i=0\) and \(\beta_i\neq0\), or conversely, then \(b_i\) lies in
exactly one kernel and the basis part of the menu succeeds.

This includes every case in which one functional is zero and the other is
nonzero. It also covers \(D=1\): two nonzero functionals on a
one-dimensional space have the same kernel, while a zero/nonzero pair is
detected by the sole basis vector. For \(D=0\), both kernels are the
zero-dimensional space and the empty menu is correctly unsuccessful.

## 6. Support-two completeness: equal zero patterns

Assume no basis vector separates. Then

\[
\alpha_i=0\iff\beta_i=0
\]

for every \(i\). If the kernels still differ, both functionals are nonzero
and their coefficient vectors are not scalar multiples. Hence some
\(2\times2\) minor is nonzero:

\[
\alpha_i\beta_j-\alpha_j\beta_i\neq0.
\]

The common zero pattern forces all four coefficients in this minor to be
nonzero. With the indices ordered so \(i<j\), put

\[
t=-\alpha_i/\alpha_j\in\mathbb F_\ell^\times.
\]

Then

\[
\alpha(b_i+t b_j)=0.
\]

Meanwhile,

\[
\beta(b_i+t b_j)
=\frac{\alpha_j\beta_i-\alpha_i\beta_j}{\alpha_j}
\neq0.
\]

This exact menu element lies in one kernel only. Conversely, if the kernels
agree, no vector in all of \(V\) can pass, so no menu vector can pass.
The theorem handles zero coordinates, zero functionals, proportional
nonzero functionals, every basis, and every dimension.

Because basis representations are unique, the menu elements in (6) are
distinct. Its exact size is

\[
D+(\ell-1)\binom D2.
\]

## 7. The \(\ell=2\) specialization

Over \(\mathbb F_2\), every nonzero coefficient equals one. Two nonzero
coefficient vectors with the same zero pattern are therefore equal. If no
basis vector separates the two kernels, the coefficient vectors have the
same zero pattern and hence are equal; the kernels agree.

Thus a kernel difference is always detected by a basis vector. The
support-two portion is unnecessary for \(\ell=2\), exactly as stated.
This certifies the binary identity-kernel behavior, not every historical
description of P66.

## 8. Polynomial bit complexity

Let \(L\) be the total bit length of the explicit relation presentation.
Standard encoding gives

\[
D\leq m\leq L.
\]

Gaussian elimination over the public prime field uses polynomial time in
the matrix dimensions and \(\log\ell\). Because the numerical value of
\(\ell\) is polynomial in \(L+\log N\), the
\(O(\ell D^2)\) menu size is polynomial.

For a menu vector, each numerator

\[
\sum_i e_{ji}c_i
\]

is computed from binary integers of input length at most \(L\) and
coefficients below \(\ell\). Its bit length is polynomial in
\(L+\log\ell\), and division by \(\ell\) is exact. Binary modular
exponentiation computes

\[
\prod_jq_j^{(\sum_i e_{ji}c_i)/\ell}\pmod N
\]

without materializing \(\widetilde R(c)\). All products and gcds have
polynomial bit complexity.

The decoder needs only \(N,\ell\), the explicit blocks, and exponent matrix.
The prime factors, local orders, local ranks, and hidden identifications are
not executable inputs. Primality of the polynomial-size public \(\ell\) can
also be checked in polynomial time if it is not supplied with a
certificate.

## 9. The \(N=215\) certificate

The factorization and relation are

\[
215=5\cdot43,
\qquad
8\cdot27=216=1+215.
\]

The pairwise-coprime unit blocks are \(2,3\), with exponent column

\[
E=\begin{pmatrix}3\\3\end{pmatrix}.
\]

Modulo \(2\), this column is nonzero. The map
\(\mathbb F_2\to\mathbb F_2^2\) has zero kernel, so there is no nonzero
binary saturation relation.

The named endpoint tests are indeed trivial:

\[
\begin{aligned}
\gcd(8-1,215)&=1,&\gcd(8+1,215)&=1,\\
\gcd(27-1,215)&=1,&\gcd(27+1,215)&=1,\\
\gcd(27-8,215)&=1.
\end{aligned}
\]

Modulo \(3\), the exponent column is zero, so \(V=\mathbb F_3\). For
\(c=1\), formula (2) gives

\[
\widetilde R(1)=2^{3/3}3^{3/3}=6.
\]

Its cube is

\[
6^3=216\equiv1\pmod{215}.
\]

The local identity labels differ:

\[
6\equiv1\pmod5,\qquad6\not\equiv1\pmod{43}.
\]

Therefore

\[
\gcd(6-1,215)=5.
\]

This proves that the \(3\)-saturation relation space and decoder can succeed
while the \(2\)-saturation relation space is trivial.

## 10. Limit of the fixed witness

The endpoint sum is

\[
8+27=35,
\qquad
\gcd(35,215)=5.
\]

Because \(8\cdot27\equiv1\pmod N\),

\[
(8-27)^2+4\equiv(8+27)^2\pmod N,
\]

and in fact

\[
\gcd(19^2+4,215)=\gcd(365,215)=5.
\]

Thus this manufactured witness is not clean against a broader menu that
includes endpoint sums or the usual inverse-pair discriminant screen. The
candidate does not say those screens fail. It claims only that endpoint
signs and the raw difference fail, and that no binary saturation relation
exists.

Accordingly, the witness proves an algebraic and decoder-operation
separation from \(2\)-saturation. It does not prove that odd-prime
saturation is necessary on \(215\), that it is the first public operation
to factor this relation, or that it gives an algorithmic advantage over all
known screens.

## 11. Exact scope

The support-two theorem is conditional on an explicit relation list,
pairwise-coprime unit blocks, and a public numerically polynomial-size prime
\(\ell\). It supplies a decoder, not a source of states satisfying
\(K_p\neq K_q\).

If two nontrivial local characters are proportional, their kernels agree
and the identity-target set is empty. Other comparisons between their
nonidentity labels could contain information, but they are outside this
theorem.

The fixed witness is manufactured, and its cube relation and broader
endpoint factor are publicly recognizable. F83 proves no all-input useful
prime, relation source, inverse-polynomial source law, literature novelty,
or factoring algorithm. Within these limits, every formal theorem and
stated arithmetic claim passes.
