# Proof-blind reconstruction: low-degree products over a semiprime

## Status and compliance

**Status: RECONSTRUCTED WITH CORRECTIONS.**

The fixed-polynomial claim is true, and its strongest elementary form is an exact CRT XOR formula followed by a Schwartz--Zippel bound. The qualifications are essential:

1. a nonzero formal polynomial can be the zero function over a finite field;
2. a polynomial-size sparse representation or division-free arithmetic circuit can have characteristic-scale or exponentially large actual degree;
3. random coefficients preserve the argument only after conditioning on coefficients independent of the evaluated sample;
4. fresh-sample adaptation is covered, but same-sample adaptation is not; and
5. formal-zero factors on opposite CRT sides can occur in different factors and make the *product* zero on both sides.

This reconstruction did not read `REGISTRY.md`, `notes/Progress.md`, or any pre-existing path whose basename begins `F31_`. The mandated output directory and this file were created/written without inspecting any pre-existing `F31_` material. Only the permitted general-context files `PROMPT.md`, `notes/Zhihu.md`, `notes/Inspirations.md`, `PROVED.md`, and `FAILED.md` were consulted. No computational experiment was performed.

## 1. Setup

Let

\[
N=pq
\]

for distinct primes. Let

\[
X=(X_1,\ldots,X_k)\sim\operatorname{Unif}((\mathbb Z/N\mathbb Z)^k).
\]

Under CRT, write \(X_p\in\mathbb F_p^k\) and \(X_q\in\mathbb F_q^k\). The CRT bijection gives the important fact

\[
X_p\sim\operatorname{Unif}(\mathbb F_p^k),\qquad
X_q\sim\operatorname{Unif}(\mathbb F_q^k),
\qquad X_p\perp X_q.
\]

Let \(F_1,\ldots,F_m\in\mathbb Z[T_1,\ldots,T_k]\), and put

\[
G=\prod_{j=1}^m F_j.
\]

Write \(\overline F_{j,r}\) and \(\overline G_r\) for formal coefficient reduction modulo \(r\in\{p,q\}\). When \(\overline F_{j,r}\ne0\), define its actual total degree

\[
\delta_{j,r}=\deg \overline F_{j,r},
\qquad
\Delta_r=\sum_j\delta_{j,r}.
\]

If \(d_j=\deg F_j\) over \(\mathbb Z\) and \(D=\sum_jd_j\), then \(\delta_{j,r}\le d_j\), hence \(\Delta_r\le D\). Reduction can lower degree when all top-degree coefficients vanish modulo \(r\).

No disjoint-variable hypothesis is made. All factors may use exactly the same variables, and each factor may depend on all \(k\) coordinates.

## 2. Main theorem

Assume first that every \(\overline F_{j,p}\) and every \(\overline F_{j,q}\) is a nonzero formal polynomial. Define

\[
\alpha_r=Pr\bigl(\overline G_r(X_r)=0\bigr),
\qquad r\in\{p,q\}.
\]

Then:

### Exact probability

\[
\boxed{
\Pr\left(1<\gcd(N,G(X))<N\right)
=\alpha_p(1-\alpha_q)+(1-\alpha_p)\alpha_q
=\alpha_p+\alpha_q-2\alpha_p\alpha_q.
}
\tag{1}
\]

### Local root bounds

Because \(\mathbb F_r[T_1,\ldots,T_k]\) is an integral domain,

\[
\overline G_r=\prod_j\overline F_{j,r}\ne0,
\qquad
\deg\overline G_r=\Delta_r.
\]

Consequently

\[
\boxed{
\alpha_r\le u_r:=\min\left(1,\frac{\Delta_r}{r}\right)
\le \min\left(1,\frac D r\right).
}
\tag{2}
\]

### Sharp envelope from degree information alone

For \(u,v\in[0,1]\), define

\[
\Psi(u,v)=\max\{u,\ v,\ u+v-2uv\}.
\]

Equations (1)--(2) imply

\[
\boxed{
\Pr\left(1<\gcd(N,G(X))<N\right)
\le \Psi(u_p,u_q).
}
\tag{3}
\]

This is the sharp rectangular envelope obtainable from only
\(0\le\alpha_p\le u_p\) and \(0\le\alpha_q\le u_q\): the bilinear function in (1) attains its maximum over that rectangle at a corner.

In particular, the simpler bound valid at every degree is

\[
\boxed{
\Pr\left(1<\gcd(N,G(X))<N\right)
\le
\min\left\{1,\frac{\Delta_p}{p}+\frac{\Delta_q}{q}\right\}
\le
\min\left\{1,D\left(\frac1p+\frac1q\right)\right\}.
}
\tag{4}
\]

If \(u_p,u_q\le1/2\), then \(\Psi(u_p,u_q)=u_p+u_q-2u_pu_q\). Therefore, if \(D\le\min(p,q)/2\),

\[
\boxed{
\Pr\left(1<\gcd(N,G(X))<N\right)
\le
\frac Dp+\frac Dq-\frac{2D^2}{pq}.
}
\tag{5}
\]

The analogous sharper local-degree version replaces \(D/p,D/q\) by \(\Delta_p/p,\Delta_q/q\).

## 3. Proof

For any residue \(y\pmod N\), squarefreeness gives

\[
\begin{array}{c|c}
\text{local state of }y & \gcd(N,y)\\ \hline
y\ne0\pmod p,\ y\ne0\pmod q & 1\\
y=0\pmod p,\ y\ne0\pmod q & p\\
y\ne0\pmod p,\ y=0\pmod q & q\\
y=0\pmod p,\ y=0\pmod q & N.
\end{array}
\]

Thus the desired event is exactly

\[
\{\overline G_p(X_p)=0\}\mathbin\triangle
\{\overline G_q(X_q)=0\}.
\]

The first event is a function only of \(X_p\), and the second only of \(X_q\). CRT independence therefore proves (1). Notice that this is independence *between the two prime components*, not independence among the factors \(F_j\).

It remains to prove (2). The following standard root bound is included for completeness.

**Finite-field root lemma.** If \(H\in\mathbb F_r[T_1,\ldots,T_k]\) is a nonzero formal polynomial of total degree \(\delta\), then

\[
\#\{x\in\mathbb F_r^k:H(x)=0\}\le \delta r^{k-1},
\]

where the right side may exceed \(r^k\); probabilistically,

\[
\Pr(H(U)=0)\le\min(1,\delta/r)
\]

for uniform \(U\in\mathbb F_r^k\).

**Proof.** Induct on \(k\). The univariate assertion is the usual root bound. For \(k>1\), write

\[
H=\sum_{i=0}^t h_i(T_1,\ldots,T_{k-1})T_k^i,
\qquad h_t\ne0.
\]

For a fixed first \(k-1\) coordinates where \(h_t\ne0\), there are at most \(t\) choices of \(T_k\) giving a root. Where \(h_t=0\), use the trivial bound of \(r\) choices. Since \(\deg h_t\le\delta-t\), induction gives at most \((\delta-t)r^{k-2}\) exceptional prefixes. The total number of roots is therefore at most

\[
(\delta-t)r^{k-2}\cdot r+r^{k-1}\cdot t
=\delta r^{k-1}.
\]

Apply this lemma to the nonzero product \(\overline G_r\), whose degree is \(\Delta_r\), to obtain (2). Equations (3)--(5) then follow from maximizing (1) and from the union bound. \(\square\)

## 4. Exact formal-zero and content alternatives

For a nonzero integer polynomial \(F\), let

\[
\operatorname{cont}(F)=\gcd\{\lvert c\rvert:c\text{ is a coefficient of }F\}.
\]

Use \(\operatorname{cont}(0)=0\). Then

\[
\overline F_r=0\text{ as a formal polynomial}
\quad\Longleftrightarrow\quad
r\mid\operatorname{cont}(F).
\tag{6}
\]

For each prime component define

\[
Z_r=\{j:r\mid\operatorname{cont}(F_j)\}.
\]

Since a polynomial ring over a field is an integral domain,

\[
\overline G_r=0\text{ formally}
\quad\Longleftrightarrow\quad
Z_r\ne\varnothing.
\tag{7}
\]

The complete alternatives are as follows. In the table, when \(Z_r=\varnothing\), \(\alpha_r\) denotes the root probability of the nonzero formal product on that side and obeys (2).

| \(Z_p\) | \(Z_q\) | Exact proper-gcd probability | Degree consequence |
|---|---|---|---|
| empty | empty | \(\alpha_p+\alpha_q-2\alpha_p\alpha_q\) | (2)--(5) |
| nonempty | empty | \(1-\alpha_q\) | \(1-u_q\le P\le1\) |
| empty | nonempty | \(1-\alpha_p\) | \(1-u_p\le P\le1\) |
| nonempty | nonempty | \(0\) | \(G(X)=0\pmod N\) always |

The last line includes two logically different situations:

- one factor is formally zero modulo both primes; or
- one factor is formally zero only modulo \(p\), while a *different* factor is formally zero only modulo \(q\).

For example, \(F_1=p\) and \(F_2=q\) are each one-sided formal-zero factors, but their product is \(N\), so the product gcd is always \(N\), not a proper divisor. Testing the factors separately would immediately succeed; multiplying them first masks both successes.

For explicit coefficients, set

\[
c_j=\gcd(N,\operatorname{cont}(F_j)).
\]

Then \(c_j=1\) means nonzero formal reduction on both sides, \(c_j=p\) or \(q\) is already a proper factor of \(N\), and \(c_j=N\) means formal zero on both sides. It is important to inspect factor contents separately: if different factors have contents divisible by \(p\) and \(q\), respectively, the product content has gcd \(N\) and loses the separation. Gauss's lemma gives \(\operatorname{cont}(\prod_jF_j)=\prod_j\operatorname{cont}(F_j)\) for nonzero integer polynomials, but (6)--(7) are all that the probability proof needs.

## 5. Formal nonzero is not functional nonzero

A formal polynomial \(H\in\mathbb F_r[T_1,\ldots,T_k]\) is a **zero function** on \(\mathbb F_r^k\) exactly when

\[
H\in I_r:=(T_1^r-T_1,\ldots,T_k^r-T_k).
\tag{8}
\]

Indeed, division by the monic polynomials \(T_i^r-T_i\) produces a unique remainder having degree below \(r\) in every variable and the same values on \(\mathbb F_r^k\). A nonzero such remainder cannot vanish everywhere, by induction on the variables. Hence the remainder is zero exactly for polynomials in \(I_r\).

Thus \(T_1^r-T_1\) is nonzero formally but zero at every field point. More generally, a product can be a zero function even if no factor is a zero function: the factors' zero sets can cover the whole affine space. The univariate identity

\[
T^r-T=\prod_{a\in\mathbb F_r}(T-a)
\]

is the basic example.

This distinction is fully compatible with (2): a nonzero formal polynomial of total degree below \(r\) cannot be a zero function, whereas at degree \(r\) the bound becomes vacuous and zero functions appear. Degree at least \(r\) is necessary, not sufficient, for a nonzero formal polynomial to vanish everywhere. If every individual variable degree is below \(r\), formal and functional zero are again equivalent even when the total degree exceeds \(r\).

Two useful counterexamples mark the boundary.

1. The integer polynomial

   \[
   (T^p-T)(T^q-T)
   \]

   has nonzero formal reduction over both fields, but its reduction is a zero function over both fields. Its gcd is therefore always \(N\).

2. Choose a CRT idempotent integer \(e\) satisfying

   \[
   e\equiv1\pmod p,\qquad e\equiv0\pmod q.
   \]

   Then

   \[
   H(T)=e(T^p-T)+(1-e)
   \tag{9}
   \]

   is primitive because \(\gcd(e,1-e)=1\), and both formal reductions are nonzero. Modulo \(p\), it is the nonzero formal zero function \(T^p-T\); modulo \(q\), it is the constant function \(1\). Hence

   \[
   \gcd(N,H(x))=p
   \]

   for every \(x\). Its actual degree is \(p\), exactly the characteristic scale. This is an existential sharpness example, not a factoring algorithm: constructing \(e\) already encodes the factorization.

## 6. Shared variables and sharpness

No independence among the events \(\{F_j(X)=0\}\) is available or needed. If \(F_1=F_2=T_1\), their local zero events are identical. At the other extreme, disjoint root sets make the degree union bound tight.

More precisely, suppose \(D\le\min(p,q)/2\). Let

\[
L=T_1+\cdots+T_k.
\]

For each \(r\in\{p,q\}\), choose \(D\) distinct elements \(a_{r,1},\ldots,a_{r,D}\in\mathbb F_r\), and use CRT to choose integers \(a_1,\ldots,a_D\) with \(a_\ell\equiv a_{r,\ell}\pmod r\). Set

\[
G=\prod_{\ell=1}^D(L-a_\ell).
\]

The linear form \(L(X_r)\) is uniform in \(\mathbb F_r\), so

\[
\alpha_p=D/p,qquad \alpha_q=D/q.
\]

All factors share all coordinates, yet equality holds in (5). For prescribed positive degrees \(d_j\) summing to \(D\), group the linear factors into blocks of sizes \(d_j\). This shows both that shared variables give no extra power saving and that (5) is a genuinely sharp worst-case bound in the low-degree range.

## 7. Random coefficient families

Let \(\Theta\) denote an arbitrary random coefficient family, possibly with strong dependence among its coefficients and between its modulo-\(p\) and modulo-\(q\) reductions. Assume only

\[
\Theta\perp X.
\]

Conditioned on \(\Theta=\theta\), the polynomials are fixed while \(X_p,X_q\) remain independent uniform vectors. Therefore, with conditional local probabilities \(\alpha_r(\theta)\),

\[
\Pr(1<\gcd(N,G_\Theta(X))<N\mid\Theta=\theta)
=\alpha_p(\theta)+\alpha_q(\theta)
-2\alpha_p(\theta)\alpha_q(\theta).
\tag{10}
\]

One must average (10), not multiply unconditional marginals:

\[
P=\mathbb E_\Theta[
\alpha_p(\Theta)+\alpha_q(\Theta)
-2\alpha_p(\Theta)\alpha_q(\Theta)].
\tag{11}
\]

Shared random coefficients can correlate the two local root probabilities even though the fresh CRT sample is locally independent.

If every realization has nonzero formal reductions on both sides and \(\Delta_r(\theta)\le B_r\), then

\[
P\le\Psi\left(\min(1,B_p/p),\min(1,B_q/q)\right).
\]

The linear form (4) also averages cleanly when degrees vary:

\[
P\le\mathbb E\left[\frac{\Delta_p(\Theta)}p+
\frac{\Delta_q(\Theta)}q\right].
\tag{12}
\]

When formal-zero realizations are possible, let \(Z_r(\Theta)\) be the event that at least one factor is formally zero modulo \(r\). The exact four-case table applies pointwise. A useful unconditional summary is

\[
P\le
\Pr(Z_p\mathbin\triangle Z_q)
+\mathbb E\left[
\mathbf1_{\neg Z_p\wedge\neg Z_q}\Psi(u_p,u_q)
\right].
\tag{13}
\]

The term \(\Pr(Z_p\triangle Z_q)\) cannot in general be removed: one-sided formal-zero coefficients can yield a proper factor with probability one.

Nor are unconditional local events necessarily independent. For example, using the idempotent \(e\) above, let a fair coin select either

\[
e(T^p-T)+(1-e)
\quad\text{or}\quad
(1-e)(T^q-T)+e.
\]

Every selected polynomial has nonzero formal reductions on both sides and gives a proper gcd with probability one, but the unconditional local zero marginals are each \(1/2\). Treating them as independent would incorrectly predict XOR probability \(1/2\) instead of \(1\). Conditioning as in (10) is exact. Again, this example embeds the factorization and serves only to disprove an invalid probabilistic inference.

## 8. Adaptation: fresh batches versus reusing the sample

### Fresh-batch adaptation is valid

At round \(t\), let an algorithm choose a polynomial family from the complete previous history, then draw a fresh

\[
X^{(t)}\sim\operatorname{Unif}((\mathbb Z/N\mathbb Z)^k)
\]

independently of that history and of the newly chosen coefficients. Conditioned on the history and coefficients, the theorem applies unchanged. If every chosen family is formally nonzero on both sides and has integer total degree \(D_t\), then for any fixed or stopping-time collection of rounds,

\[
\Pr(\text{some round returns a proper gcd})
\le
\left(\frac1p+\frac1q\right)
\mathbb E\left[\sum_tD_t\right].
\tag{14}
\]

This is conditional union bounding; independence between rounds is unnecessary. A sharper per-round use of (3) is possible, but (14) is the clean amortized statement.

### Same-sample adaptation is outside the theorem

If coefficients are selected after seeing the sample to which the polynomial will be applied, the conditional sample is no longer uniform. No degree-only statement survives. For \(k=1\), after seeing \(X=x\), choose

\[
F_x(T)=T-x+p.
\]

For every fixed \(x\), this is a primitive degree-one polynomial with nonzero formal reductions over both fields, but

\[
F_x(x)=p,
\]

so the proper-gcd probability is one. The example uses the hidden factor and is not an algorithm; it proves that independence from the evaluated sample is a logically necessary hypothesis. More generally, conditioning on a same-sample transcript is safe only if one separately proves that the remaining sample law is still the required independent uniform CRT product law.

## 9. Representation models and actual degree

The probability theorem is semantic: it concerns the formal polynomial actually represented and its actual degree. Representation size is a separate issue.

### Explicit dense coefficients

After like monomials are combined, formal zero, content, and actual degree are explicit. In an ordinary dense univariate encoding, degree \(D\) requires \(D+1\) coefficient slots. Thus characteristic-scale degree is already exponentially large to materialize on balanced semiprimes. Multivariate dense encodings can be larger still.

### Explicit sparse coefficients

Formal zero and content remain explicit after duplicate monomials are combined, but exponents are normally encoded in binary. A three-term polynomial can therefore have exponentially large actual degree. Polynomial (9), for example, is sparse of degree \(p\). Sparse input size is not a surrogate for degree.

### Succinct branch-free division-free circuits

A circuit using constants, inputs, addition, subtraction, and multiplication, with no data-dependent branches or divisions, defines a formal polynomial. CRT reduction commutes with every gate, so the theorem applies to the output polynomial. Shared subcircuits and shared variables cause no problem.

However, repeated squaring gives degree \(2^s\) using \(s\) multiplication layers. A polynomial-size circuit can therefore have exponential actual degree. Syntactic degree obeys

\[
\deg(A+B)\le\max(\deg A,\deg B),
\qquad
\deg(AB)\le\deg A+\deg B,
\]

but cancellation can lower the actual degree over \(\mathbb Z\), and reduction can lower it differently modulo \(p\) and \(q\). The theorem requires a proved actual or valid upper degree bound; circuit size alone is insufficient.

For a succinct circuit, the expanded content and even formal nonzeroness modulo an unknown prime need not be readily certifiable without expansion or a separate identity argument. The theorem does not supply that certification.

Branches and division gates are materially different. A branch can select a polynomial using information about the current sample, while a division can fail in only one CRT component and itself expose a zero divisor. Such computations are piecewise-polynomial or rational, not covered by the branch-free division-free statement.

## 10. Balanced-semiprime threshold

Assume, after relabeling, that

\[
p<q\le Cp
\]

for a fixed constant \(C\ge1\). Then

\[
p\ge\sqrt{N/C},\qquad q\ge\sqrt N,
\]

so (4) yields

\[
\boxed{
P\le(\sqrt C+1)\frac D{\sqrt N}.
}
\tag{15}
\]

For the common promise \(p<q<2p\), this is

\[
P<(1+\sqrt2)\frac D{\sqrt N}.
\tag{16}
\]

If \(n=\lceil\log_2(N+1)\rceil\), then \(N\ge2^{n-1}\), and hence

\[
P\le(\sqrt C+1)D\,2^{-(n-1)/2}.
\tag{17}
\]

Thus actual degree \(D=\operatorname{poly}(n)\) gives exponentially small single-batch success on balanced semiprimes. For fresh adaptive batches with expected total actual degree budget

\[
B=\mathbb E\sum_tD_t,
\]

equation (14) gives the same bound with \(B\) in place of \(D\). Polynomially many polynomial-degree batches remain exponentially unlikely to split a balanced semiprime.

Conversely, success probability at least \(\varepsilon\) requires

\[
B\ge\frac{\varepsilon\sqrt N}{\sqrt C+1}
\tag{18}
\]

under these hypotheses. Even inverse-polynomial success \(\varepsilon=1/\operatorname{poly}(n)\) therefore requires exponential total actual degree. Constant success requires characteristic-scale total degree \(\Theta(\sqrt N)\). The shared-linear-form construction in Section 6 with \(D=\Theta(p)\) gives constant probability, so this threshold is sharp in order.

This is not a representation-size lower bound. Sparse polynomials and poly-size circuits can reach this actual degree, and a putative succinct evaluator of an exponentially large product is not excluded.

## 11. Counterexample audit and exact scope

The following tempting strengthenings are false.

1. **“All coordinates are used, so the root probability gains a factor \(r^{-k}\).”** False: all factors can depend on the single shared uniform linear form \(T_1+\cdots+T_k\), and Section 6 attains \(D/r\).

2. **“The factor-zero events are independent.”** False when variables are shared; they can be identical or mutually exclusive. Only the \(p\)-vector and \(q\)-vector are independent.

3. **“Nonzero formal reduction means the evaluation is sometimes nonzero.”** False at characteristic-scale degree; \(T^r-T\) is the standard counterexample.

4. **“If the product is formally zero on both sides, one factor must be zero on both sides.”** False: \(F_1=p,F_2=q\) are opposite one-sided factors.

5. **“Polynomial-size sparse/circuit description implies low degree.”** False by binary exponents and repeated squaring.

6. **“Coefficients independent of \(X\) make the unconditional local events independent.”** False because shared coefficient randomness can correlate the two conditional root probabilities. Condition first, then average.

7. **“Fresh adaptation and same-sample adaptation are equivalent.”** False by \(F_x(T)=T-x+p\).

8. **“The full-affine sampling assumption is cosmetic.”** False: if \(X\) is concentrated at any known zero divisor, the degree-one polynomial \(T\) succeeds with probability one. More generally, arbitrary CRT correlations invalidate (1).

9. **“Multiplying all factors is equivalent to checking them separately.”** False: opposite one-sided factors can each split \(N\) while their product has gcd \(N\).

The proved scope is exactly:

- a squarefree semiprime \(N=pq\) with distinct primes;
- a sample uniform on the *full* affine space, giving independent uniform CRT vectors;
- fixed polynomials, or random/adaptive polynomials chosen independently of the fresh sample being evaluated;
- actual formal degree bounds, not advertised degrees, term counts, circuit sizes, or multiplicative complexities;
- arbitrary sharing of variables among factors; and
- polynomial outputs, including outputs of fixed branch-free division-free circuits.

The result does not prove an arithmetic-circuit lower bound, an evaluator lower bound, or a factoring lower bound. It does not cover rational functions, data-dependent branching, nonuniform sample sets, same-sample selection, or a genuine joint decoder that uses the vector of ubiquitous nonzero evaluations through ranks, resultants, kernels, nonlinear reconstruction, or another statistic rather than merely OR-ing rare zeros through a product.

## 12. Interpretation: not genuine joint decoding

This mechanism is **not genuine joint decoding**. Locally, because a field has no zero divisors,

\[
\prod_jF_j(X_r)=0
\quad\Longleftrightarrow\quad
\exists j:F_j(X_r)=0.
\]

The product is only a cancellation-free OR of local zero tickets. The total-degree bound is the corresponding additive root budget, and CRT independence converts the two local OR events into an XOR. Shared variables are handled by Schwartz--Zippel or a union bound; they are not decoded.

A genuinely new joint decoder would have to combine information present in typical nonzero outputs, or evaluate a characteristic-scale pooled observable succinctly. This theorem rules out only polynomial total actual degree as a way to amortize rare polynomial-zero tickets on balanced semiprimes.
