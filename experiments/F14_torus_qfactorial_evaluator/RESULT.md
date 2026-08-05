# F14: exact torus q-factorial evaluation

## Outcome

I did not find a uniform algorithm that evaluates

\[
S_m(a)=\prod_{d=1}^{m-1}(1-a^d)^{m-d}\pmod N
\]

in time polynomial in \(\log N+\log m\).

The positive result of this experiment is a narrow obstruction: an exact order-threshold observable represented as a product of binomials \(1-a^L\) requires at least \(\lceil(m-1)/2\rceil\) distinct exponents. Thus replacing the product by a polylogarithmic number of lcm-like binomials cannot work. An explicit order-12 counterexample also kills the most direct lcm compression. Exact q-Pochhammer addition laws, dense shifted boundary states, explicit resultants, and equal-floor cyclotomic grouping all retain super-polylogarithmic work for separately proved reasons below.

These statements do **not** prove that an arbitrary arithmetic circuit or an unrelated evaluator must take super-polylogarithmic time.

## 1. Notation and the unweighted collision observable

Put \(M=m-1\), and define

\[
P_M(a)=\prod_{d=1}^{M}(1-a^d).
\]

If \(a\) is a unit in a field and has multiplicative order \(t\), then

\[
P_M(a)=0\quad\Longleftrightarrow\quad S_m(a)=0
\quad\Longleftrightarrow\quad t\le M.
\]

Over \(\mathbb Z/N\mathbb Z\), the two residues need not be equal and zero divisors prevent the same elementwise inference. Nevertheless they have the same prime support:

\[
\gcd(P_M(a),N)>1\quad\Longleftrightarrow\quad
\gcd(S_m(a),N)>1,
\]

because modulo each prime divisor of \(N\), either product vanishes exactly when one of the common binomial factors vanishes. Hence \(P_M\) is a legitimate equivalent collision observable if only separation by a gcd is required; it is not an evaluator for the requested residue \(S_m(a)\).

## 2. Exact q-Pochhammer/q-Barnes addition law and its cost

For a shifted block, define

\[
Q(s,n)=\prod_{d=1}^{n}(1-a^{s+d}),\qquad
T(s,n)=\prod_{d=1}^{n}(1-a^{s+d})^{n+1-d}.
\]

Then \(S_m(a)=T(0,M)\), and direct splitting gives the exact laws

\[
Q(s,n+k)=Q(s,n)Q(s+n,k),
\]

\[
T(s,n+k)=T(s,n)Q(s,n)^kT(s+n,k).
\]

The second identity follows because every exponent in the left block gains \(k\), while the right block has the triangular weights of \(T(s+n,k)\).

These laws compose two already-evaluated adjacent blocks using constant-size numeric state. They do not derive the shifted right child from the left child. In particular, dyadic recursion at length \(2n\) requires both \((Q,T)(s,n)\) and \((Q,T)(s+n,n)\). The direct addition-law evaluator therefore has

\[
W(2n)=2W(n)+\operatorname{poly}(\log n,\log N),
\]

so it reaches \(n\) singleton leaves. Binary splitting changes the multiplication tree, not the number of leaf factors. This is a cost accounting for this addition-law mechanism, not a lower bound for all possible evaluators.

## 3. The shift-capable symbolic boundary is large when materialized densely

Introduce a start variable \(X\):

\[
Q_n(X)=\prod_{d=1}^{n}(1-Xa^d),\qquad
T_n(X)=\prod_{d=1}^{n}(1-Xa^d)^{n+1-d}.
\]

Substitution \(X=a^s\) supplies the shifted block. The q-binomial theorem shows that \(Q_n\) has degree \(n\) and all \(n+1\) coefficients are nonzero in \(\mathbb Z[a]\). Also

\[
\deg_X T_n=\frac{n(n+1)}2,
\]

and every coefficient from degree \(0\) through \(n(n+1)/2\) is nonzero: every contribution to the coefficient of \(X^k\) has the common sign \((-1)^k\) and a positive integer coefficient times a monomial in \(a\), so cancellation is impossible.

Consequently, a divide-and-conquer method that explicitly materializes the shift-capable boundary polynomial stores at least \(n+1\) scalars for \(Q_n\), or \(n(n+1)/2+1\) for \(T_n\). A factored expression or arithmetic DAG can remain syntactically small, so this coefficient count is not an arithmetic-circuit lower bound. It only closes the proposed dense-boundary-state implementation.

## 4. A linear lower bound for exact threshold binomial products

### Lemma (threshold-binomial compression)

Fix \(M\ge 2\). Let

\[
F(a)=\prod_{h=1}^{r}(1-a^{L_h})^{w_h},
\]

where \(L_h,w_h\) are positive integers. Suppose that in every finite field containing an element \(a\) of order \(t\),

\[
F(a)=0\quad\Longleftrightarrow\quad t\le M.
\]

Then the exponent list contains every integer

\[
\lfloor M/2\rfloor+1,\ldots,M.
\]

In particular, it contains at least \(\lceil M/2\rceil\) distinct exponents.

### Proof

First, every \(L_h\le M\). If some \(L_h>M\), take an element of order exactly \(L_h\). Its corresponding factor vanishes, hence \(F(a)=0\), contradicting the required threshold.

Now fix \(t\) with \(M/2<t\le M\), and take an element of order exactly \(t\). Since a field has no zero divisors, \(F(a)=0\) implies \(1-a^{L_h}=0\) for some \(h\), hence \(t\mid L_h\). But \(L_h\le M<2t\), so necessarily \(L_h=t\). This holds for every integer in the stated interval. \(\square\)

The order instances exist without assuming a special characteristic: choose any prime \(q\nmid t\); Euler's theorem gives \(t\mid q^{\varphi(t)}-1\), and the cyclic group \(\mathbb F_{q^{\varphi(t)}}^\times\) therefore contains an element of order \(t\). If the claimed representation is restricted specifically to prime fields, the same conclusion additionally uses the standard theorem that a prime \(p\equiv1\pmod t\) exists (Dirichlet), after which \(\mathbb F_p^\times\) contains such an element.

Thus no exact all-field threshold product can replace the \(M\) original factors by \(\operatorname{poly}(\log M)\) binomials, even if their exponents are written succinctly. The lemma does not cover sums, cancellations, rational functions, non-binomial factors, or arbitrary arithmetic circuits.

### Concrete failure of the single-lcm construction

For \(M=4\), \(\operatorname{lcm}(1,2,3,4)=12\). In \(\mathbb F_{13}\), the element \(a=2\) has order \(12\): \(2^6=-1\pmod {13}\), and its powers at every proper divisor of \(12\) are not \(1\). Therefore

\[
1-a^{12}=0\pmod {13},
\]

although \(\operatorname{ord}(a)=12>4\). Equivalently, the compressed resultant

\[
\operatorname{Res}_X(X^{12}-1,X-2)
\]

vanishes modulo \(13\) and gives a false positive. Divisibility by the lcm is much weaker than being at most the threshold.

## 5. Resultant and determinant encodings

A standard Sylvester resultant or diagonal determinant that explicitly forms either the factor list or \(Q_n(X)\) inherits dimension/state at least linear in \(n\). It repackages the product rather than eliminating its factors. Calling a determinant representation "succinct" only helps if there is also an algorithm exploiting its special structure; an oracle that evaluates precisely this structured determinant in polylogarithmic time is the missing evaluator under another name.

The lcm example above is an exact counterexample to one-factor resultant compression. It is not a proof that every possible structured resultant is large or slow.

## 6. Cyclotomic grouping and equal floors

Cyclotomic factorization gives

\[
S_m(a)=(-1)^{\binom m2}\prod_{e=1}^{M}\Phi_e(a)^{E_e},
\]

where, with \(h=\lfloor M/e\rfloor\),

\[
E_e=hm-e\frac{h(h+1)}2.
\]

Grouping indices with the same quotient \(h\) does not give a polylogarithmic number of groups. If \(q=\lfloor\sqrt M\rfloor\), the quotient set

\[
\{\lfloor M/e\rfloor:1\le e\le M\}
\]

has at least \(2q-1\) distinct values. Indeed, the quotients for \(e=1,\ldots,q\) are strictly decreasing and at least \(q\), while every value \(1,\ldots,q\) occurs; the two sets overlap in at most the value \(q\).

Even inside one equal-floor group, \(E_e\) varies linearly with \(e\). Replacing the group by only \(\prod_e\Phi_e(a)\) loses the weighted product. Reconstructing it using ratios or negative exponents is invalid modulo a composite \(N\), where the relevant values may be nonunits or zero divisors. A division-free representation still needs a weighted interval product. Therefore the literal strategy "one constant-size aggregate per equal-floor group" needs \(\Omega(\sqrt M)\) groups and does not meet a polylogarithmic target. This does not rule out a different fast cyclotomic evaluator.

## 7. Explicit polynomial root-set materialization is also large

In characteristic zero, any polynomial that vanishes at every root of unity of order at most \(M\) is divisible by

\[
R_M(X)=\prod_{t=1}^{M}\Phi_t(X).
\]

Hence its degree is at least

\[
D_M=\sum_{t=1}^{M}\varphi(t).
\]

An elementary bound is enough here. If \(t\) has \(r\) distinct prime factors \(p_1<\cdots<p_r\), then \(p_i\ge i+1\), so

\[
\frac{t}{\varphi(t)}
=\prod_{i=1}^{r}\frac{p_i}{p_i-1}
\le\prod_{i=1}^{r}\frac{i+1}{i}
=r+1
\le1+\log_2 t.
\]

For the at least \(M/2\) integers \(t\in(M/2,M]\), this yields

\[
D_M\ge \frac{M^2}{4(1+\log_2 M)}.
\]

Thus explicitly materializing the squarefree threshold polynomial, or a conventional resultant containing it densely, has superlinear degree. High-degree polynomials can still have tiny circuits (for example \(X^{2^k}-1\)), so degree is not a general circuit-size or evaluation-time lower bound.

## 8. Circularity of period/order shortcuts

If the order \(t\) of \(a\) in each field component were already known, the factors would be periodic and the threshold test would be immediate. But deciding whether that local order is at most \(M\) is exactly the zero predicate supplied by \(P_M\) or \(S_m\). A proposed cycle compression that branches on the unknown period, on the relevant field component, or on a factor of \(N\) therefore assumes the separator information it is meant to produce. This diagnoses circularity; it is not a complexity lower bound.

## 9. Remaining gap

The straightforward recurrence

\[
P_d=P_{d-1}(1-a^d),\qquad S_{d+1}=S_dP_d
\]

uses \(O(M)\) modular iterations. Baby-step/giant-step or structured polynomial techniques may reduce that dependence, but any \(M^c\) bound with \(c>0\) is still exponential in the requested input length \(\log M\).

The F14 conclusion is therefore option (ii), not a construction: the threshold-binomial lemma and the order-12 example materially close lcm/binomial-product compression, while the exact addition laws and state counts explain why the most direct q-Pochhammer, dense-boundary, conventional resultant, and equal-floor implementations do not supply the missing polylogarithmic evaluator. The broader evaluator question remains open here.
