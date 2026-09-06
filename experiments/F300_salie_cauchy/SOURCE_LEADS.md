# Primary-source leads for dyadic Salié/Cauchy sums

Checked 2026-09-07. The packet path was absent from both the filesystem and
the Rust catalog before creation. The local knowledge base contained no
source for the combined dyadic weighted sum. Its cached Kloosterman paper
treats complete shifted products only at odd prime-power moduli.

Terminology varies across these sources. A classical Salié sum usually means
a Kloosterman sum with a quadratic character at an odd modulus. At modulus
\(2^r\), the sources below use explicit characters or elementary weights on
the odd units and call the result a twisted Kloosterman sum. Also,

\[
 \frac{1}{1-e^{2\pi i x}}=\frac12+\frac{i}{2}\cot(\pi x)
 \qquad (x\notin\mathbb Z),
\]

so the cited cotangent and Fourier--Dedekind results cover the bare Cauchy
denominators, but not a simultaneous inverse-exponential numerator.

## 1. Gauss-weighted complete sums over \(\mathbb Z/2^r\mathbb Z\)

Michelle R. DeDeo, "Generalized Kloosterman Sums over the Rings of Order
\(2^r\)," *Congressus Numerantium* **165** (2003), 65--75.
[Institutional metadata](https://scholars.unf.edu/en/publications/generalized-kloosterman-sums-over-the-rings-of-order-2r/);
[author-uploaded full text](https://www.researchgate.net/publication/265676442_Generalized_Kloosterman_Sums_over_Rings_of_Order_2_r).

- Section 2 defines the complete sum
  \[
  K'(a,b)=\sum_{v\in(\mathbb Z/2^r\mathbb Z)^\times}
     (G_v^{(r)})^n e_{2^r}(av+b\bar v)
  \]
  and, for \(r\geq3\), decomposes it according to \(n\bmod4\) into at most
  two complete Kloosterman sums with the four elementary unit weights shown
  there: the trivial weight, \(i^v\), \((2/v)\), and their product.
- Theorem 2 states that the trivial-character sum vanishes when
  \(ab\not\equiv1\pmod8\), for \(r\geq6\). Theorem 3 gives its explicit
  sine/cosine evaluation when \(a,b\) are odd and
  \(ab\equiv c^2\pmod{2^r}\): the stated ranges are even \(r\geq6\) and odd
  \(r\geq9\).
- Theorem 5 gives the corresponding explicit trigonometric evaluations for
  the other three unit weights under the same square-root hypothesis. Its
  thresholds are \(r\geq6\) for the \(i^v\) weight and \(r\geq8\) for the
  two weights involving \((2/v)\). Section 6 substitutes these evaluations
  back into the Gauss-weighted sum.

This is an exact evaluation of a **complete power-of-two Gauss-weighted
sum**. It has no Bernoulli, cotangent, Cauchy, or truncation weight, and it
states no bit-complexity bound.

## 2. Complete character-twisted Kloosterman sums at prime powers

Adrián Barquero-Sánchez, Juan Pablo De Rasis, Nicolás Sirolli, and Jean
Carlos Villegas-Morales, "On the efficient computation of Fourier
coefficients of eta-quotients," arXiv:2504.01384v3, 12 August 2026.
[Primary PDF](https://arxiv.org/pdf/2504.01384).

- Section 3 defines
  \(S_\chi(a,b;k)=\sum_{h\bmod k}^{*}\chi(h)e_k(ah+b\bar h)\).
  Proposition 3.3, equations (3.3)--(3.4), reduces common
  \(p\)-adic valuations, including the separate terminal case at \(p=2\).
- For \(q=p^\alpha\), with \(\chi\) defined modulo \(p^\beta\), Proposition
  3.7 assumes \(\alpha/2\leq\beta<\alpha\), and additionally
  \(\alpha>\beta+2\) when \(p=2\). It gives zero unless the remaining
  argument is a unit square modulo \(q\); equation (3.6) is the exact
  stationary-class reduction. Remark 3.8 records the imprimitive
  power-of-two specialization \(\beta=\alpha-3\), \(\alpha>5\).
- Proposition 3.9 lists the exceptional formulas for \(2^\alpha\) with
  \(1\leq\alpha\leq5\). Proposition 3.12 assumes \(p=2\), \(\beta\geq3\),
  and odd \(u\), and gives closed formulas for \(S_\chi(u,u;2^\alpha)\) when
  \(\alpha=2\beta\) or \(2\beta+1\). Equation (3.7) reduces the sum to the
  displayed solutions of \(v^2\equiv1\pmod{2^{\lfloor\alpha/2\rfloor}}\).
- Propositions 3.10--3.11 are the separate odd-prime formulas and do not
  supply a power-of-two statement.

These are exact formulas for **complete character-twisted prime-power
sums**. They contain no extra Cauchy denominator or sharp truncation. The
paper uses them in an eta-quotient coefficient algorithm; it does not state a
bit-complexity theorem for the combined weighted family considered here.

## 3. Cotangent/Bernoulli reciprocity and fixed-dimensional computation

Matthias Beck, "Dedekind cotangent sums," *Acta Arithmetica* **109** (2003),
109--130, DOI 10.4064/aa109-2-1.
[Primary journal PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83280).

- Definition 1 is a complete residue sum of products of cotangent
  derivatives, omitting singular summands. Theorem 2 gives its reciprocity
  law for \(a_0,\ldots,a_d\in\mathbb N\),
  \(m_0,\ldots,m_d\in\mathbb N_0\), and \(z_0,\ldots,z_d\in\mathbb C\),
  under the explicit no-common-pole condition
  \((m+z_i)/a_i-(n+z_j)/a_j\notin\mathbb Z\) for distinct \(i,j\) and all
  integers \(m,n\).
- Lemma 6 gives the discrete Fourier expansion of periodic Bernoulli
  functions in cotangent derivatives. Corollary 7 applies it to
  Dedekind--Bernoulli sums under pairwise coprimality and the stated parity
  condition.
- Theorem 5 states polynomial-time computability in the input sizes of
  \(a_0,\ldots,a_d\). Its proof invokes Theorem 15, Barvinok's theorem in
  fixed dimension; the other displayed parameters are outside the stated
  input-size list.

This is **complete cotangent/Bernoulli-weighted reciprocity and
fixed-dimensional computation** for general moduli, hence also admissible
power-of-two moduli when its pole conditions hold. It has no Kloosterman
inverse phase, character, or Gauss weight.

## 4. Direct algorithm for complete Cauchy-denominator sums

Guoce Xin and Xinyu Xu, "A Polynomial Time Algorithm for Calculating
Fourier-Dedekind Sums," *Experimental Mathematics* **34** (2025), 342--349,
DOI 10.1080/10586458.2024.2364264.
[Primary preprint](https://arxiv.org/pdf/2303.01185);
[journal record](https://doi.org/10.1080/10586458.2024.2364264).

- Equation (1.1) defines
  \[
  s_n(a_1,\ldots,a_d;b)=\frac1b\sum_{k=1}^{b-1}
    \frac{\xi_b^{kn}}
    {\prod_{j=1}^d(1-\xi_b^{ka_j})},
  \]
  for \(b>1\) and \(\gcd(a_j,b)=1\) for every \(j\).
- Proposition 3 converts a nonsingular root-of-unity average to a constant
  term. Corollary 4 applies that identity to (1.1). Algorithm 5 computes the
  resulting exact value by a simplicial-cone decomposition and slack-variable
  elimination.
- The polynomial-time statement uses Barvinok decomposition, so its
  polynomial guarantee is in fixed denominator count \(d\). The modulus
  \(b\) is unrestricted and can equal \(2^r\).

This is an exact algorithm for a **complete Cauchy-denominator sum**. Its
numerator is one linear root-of-unity phase. It has no inverse phase,
multiplicative character, or Gauss weight.

## Scope boundary of the four leads

The first two sources evaluate complete dyadic inverse-phase sums but have no
Cauchy or cotangent denominator. The last two handle complete Cauchy,
cotangent, or Bernoulli weights but have no inverse-phase or Salié numerator.
This focused search did not locate a primary theorem that combines both
structures, nor one that gives an exact algorithm or reciprocity for their
truncated combination. This is only a statement about the sources inspected,
not a novelty claim.
