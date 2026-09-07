# F303 source leads: inverse moments and odd unit products

**Status.** Focused primary-source search. This note records the closest exact
overlaps found for the F303 statement. It is not a novelty claim and does not
assess the feasibility of the claimed universal product-ratio algorithm.

## 1. Generalized Cochrane sums contain the canonical-inverse moments

Jiankang Wang, Zhefeng Xu, and Minmin Jia, “On the generalized Cochrane sum
with Dirichlet characters,” *AIMS Mathematics* 8 (2023), 30182–30193,
[DOI 10.3934/math.20231542](https://doi.org/10.3934/math.20231542),
[official PDF](https://www.aimspress.com/aimspress-data/math/2023/12/PDF/math-08-12-1542.pdf).
The full text is also retained at
[.knowledge/10-3934-math-20231542.md](../../.knowledge/10-3934-math-20231542.md).

For positive integers \(m,n\), an integer \(q>0\), a Dirichlet character
\(\chi\pmod q\), and the least positive inverse \(\bar a\) satisfying
\(a\bar a\equiv1\pmod q\), the paper defines

\[
C(h,m,n,q,\chi)=
\sum_{a=1}^{q}{}'\chi(a)\,
\overline B_m(a/q)\,\overline B_n(h\bar a/q),
\tag{definition on p. 30184}
\]

where the prime restricts the sum to \((a,q)=1\), and \(\overline B_j\) is
the periodic Bernoulli function. With the principal character, this is the
literature object containing polynomial moments of a canonical residue and
its canonical modular inverse. Expanding the two Bernoulli polynomials gives
a triangular linear combination whose leading mixed power moment is

\[
q^{-(m+n)}
\sum_{a=1}^{q}{}'a^m(h\bar a\bmod q)^n.
\]

The paper's analytic theorems have narrower hypotheses. Lemma 2.1 assumes
that \(p\) is an odd prime, \((h,p)=1\), \(\chi_1\pmod p\) is a Dirichlet
character, and \(m,n>0\). It expresses \(C(h,m,n,p,\chi_1)\) as a character
sum with two Gauss factors and two Dirichlet \(L\)-values, subject to its
stated parity condition. Theorem 1.1, again for an odd prime \(p\), states

\[
C(h,m,n,p,\chi)\ll
\frac{m!n!}{(2\pi)^{m+n}}p^{1/2}\log^2p,
\]

and \(C(h,m,n,p,\chi)=0\) when
\(\chi(-1)\ne(-1)^{m+n}\).

**F303 boundary.** The definition applies to \(q=2^k\), but the cited lemma
and theorem do not. They are analytic identities and estimates, not
congruences modulo \(q^2\), and they do not give a bit-complexity algorithm
for one fixed \(h\). They identify the established object and its character
phase. They do not supply F303's uniform computation of every
\(S_{ab}\pmod{M^2}\).

## 2. Generalized Wilson quotients give higher prime-power congruences

Ladislav Skula, “Fermat and Wilson quotients for \(p\)-adic integers,”
*Acta Mathematica et Informatica Universitatis Ostraviensis* 6 (1998),
167–181, [EuDML record](https://eudml.org/doc/23810),
[primary PDF](https://dml.cz/bitstream/handle/10338.dmlcz/120531/ActaOstrav_06-1998-1_21.pdf).

Definition 5.1 sets

\[
W(m)=\frac{1}{m}
\left(
\prod_{\substack{1\le j\le m\\(j,m)=1}}j-\varepsilon_m
\right),
\]

where \(\varepsilon_m=-1\) for
\(m=2,4,p^\alpha,2p^\alpha\), with \(p\) an odd prime, and
\(\varepsilon_m=1\) otherwise. Thus, for \(m=2^k\) and \(k\ge3\),
\(W(m)=(\Pi_m-1)/m\). Equation (5.1) and Proposition 5.1 state

\[
W(p^{n+1})\equiv W(p^n)\pmod{p^{\,n-1}},
\qquad
v_p\!\left(W_p-W(p^n)\right)\ge n-1.
\]

For \((a,m)=1\), let
\(q(a,m)=(a^{\varphi(m)}-1)/m\), and define

\[
\sigma_1(m)=\sum_{(a,m)=1}q(a,m),\qquad
\sigma_2(m)=
\sum_{\substack{a<b\\(a,m)=(b,m)=1}}q(a,m)q(b,m).
\]

Proposition 5.2 states, for every integer \(m\ge3\),

\[
\varepsilon_m\varphi(m)W(m)
+\binom{\varphi(m)}2mW(m)^2
\equiv \sigma_1(m)+m\sigma_2(m)\pmod{m^2}.
\tag{Proposition 5.2}
\]

**F303 boundary.** This is a higher congruence for the same unit product,
and it includes powers of two. It does not give a polynomial-bit method to
evaluate that product: its finite sums range over the units, and its
\(p\)-adic limit has no algorithmic cost bound. Also,
\(q(a,m)=(a^{\varphi(m)}-1)/m\) is an Euler quotient. It is different from
F303's \((u(Nu^{-1}\bmod M)-N)/M\).

## 3. A power-sum/Newton algorithm computes the odd product

Mugurel Ionut Andreica, “A Fast Algorithm for Computing Binomial
Coefficients Modulo Powers of Two,” *The Scientific World Journal* (2013),
Article 751358, [DOI 10.1155/2013/751358](https://doi.org/10.1155/2013/751358),
[full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC3856163/).

Use the paper's notation: \(N\) is the requested 2-adic precision and
\(0\le P\le N\). Section 4 defines

\[
\operatorname{PSUM}(P,Q)=
\sum_{j=1}^{2^P}j^Q\pmod{2^N}
\tag{9}
\]

and gives the divide-and-shift recurrence (13), with terms omitted when
their 2-adic valuation reaches \(N\). Section 5 defines
\(\operatorname{SSP}(P,Q)\) as the \(Q\)-th elementary symmetric sum of
\(1,\ldots,2^P\), and uses the Newton recurrence

\[
\operatorname{SSP}(P,Q)=\frac1Q
\sum_{j=1}^{Q}(-1)^{j-1}
\operatorname{SSP}(P,Q-j)\operatorname{PSUM}(P,j).
\tag{15}
\]

The algorithm does not invert an even \(Q\). It writes \(Q=A2^B\), with
\(A\) odd, inverts only \(A\), performs exact division by \(2^B\), and
tracks

\[
\operatorname{Precision}(P,Q)=N-v_2(Q!),\qquad
v_2(Q!)=\sum_{j\ge1}\left\lfloor Q/2^j\right\rfloor.
\tag{17 and its surrounding algorithm}
\]

Section 6 then treats the exact F303 product. Equations (19)–(20) are

\[
\prod_{j=1}^{2^{P-1}}(2j-1)\pmod{2^N}
\tag{19}
\]

and

\[
\sum_{j=0}^{2^{P-1}}
2^j\operatorname{SSP}(P-1,j)(-1)^{2^{P-1}-j}
\pmod{2^N}.
\tag{20}
\]

Terms with \(j\ge N\) vanish modulo \(2^N\). The paper gives preprocessing
time
\(O(N^3\operatorname{Multiplication}(N)+N^4)\), followed by \(O(N)\)
multiplications of \(N\)-bit numbers for (19), once the tables are
available. It does not form a list of the \(2^{P-1}\) odd factors.

**F303 boundary.** Setting the paper's \(P=k\) and its \(N\) equal to
F303's requested precision gives a published polynomial-bit algorithm for
\(\Pi_{2^k}\bmod 2^N\) in the stated range \(k\le N\). This is the one
source here that supplies an actual uniform algorithm, instead of only a
related congruence. It does not construct F303's rational function \(R(T)\),
extract the carry moments \(Q_j\), or compute the mixed moments \(S_{ab}\).

## Scope conclusion

- The Cochrane paper fixes the established mixed canonical-inverse object
  and its character phase. Its cited exact results are for odd primes and
  are not uniform algorithms.
- Skula gives prime-power, including dyadic, higher Wilson congruences. The
  formulas retain numerical-size unit sums and use a different quotient.
- Andreica gives a non-enumerative power-sum/Newton primitive for the odd
  unit product, with explicit precision guards and a polynomial
  bit-operation bound in its stated parameter range.
- None of these three sources states the universal product ratio or the full
  uniform algorithm for all F303 mixed moments. This describes only the
  scope of the three checked sources.
