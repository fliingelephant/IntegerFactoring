# Blind reconstruction: low-degree product--gcd laws

## 1. Setup and statement

Let

\[
N=pq
\]

for distinct primes \(p,q\), let \(k\geq 1\), and let

\[
F_1,\ldots,F_m\in \mathbb Z[T_1,\ldots,T_k].
\]

Write \(\overline F_{j,r}\in\mathbb F_r[T_1,\ldots,T_k]\) for the formal coefficientwise reduction of \(F_j\) modulo \(r\), where \(r\in\{p,q\}\). In the main theorem, assume every \(\overline F_{j,r}\) is a nonzero formal polynomial. Define its **local actual degree** by

\[
\delta_{j,r}=\deg(\overline F_{j,r}),
\qquad
\Delta_r=\sum_{j=1}^m\delta_{j,r}.
\]

These are degrees after reduction and cancellation, not degrees of an encoding and not merely syntactic degree bounds. Put

\[
G=\prod_{j=1}^m F_j,
\qquad
\overline G_r=\prod_{j=1}^m\overline F_{j,r},
\]

and, for uniform \(x_r\in\mathbb F_r^k\), define

\[
\alpha_r
=\Pr[\overline G_r(x_r)=0]
=\Pr[\exists j:\overline F_{j,r}(x_r)=0].
\]

Let \(X\) be uniform on \((\mathbb Z/N\mathbb Z)^k\), and let

\[
H(X)=\gcd(G(X),N).
\]

The gcd is independent of the chosen integer representative of \(G(X)\). The following claims hold.

1. The exact probability of a proper gcd is

   \[
   \Pr[1<H(X)<N]
   =\alpha_p+\alpha_q-2\alpha_p\alpha_q.
   \tag{1}
   \]

2. The local Schwartz--Zippel bounds are

   \[
   \alpha_r\leq \min\!\left\{1,\frac{\Delta_r}{r}\right\}.
   \tag{2}
   \]

3. If only \(0\leq\alpha_p\leq u\) and \(0\leq\alpha_q\leq v\), where \(u,v\in[0,1]\), are known, the sharp rectangular envelope is

   \[
   \Psi(u,v)=\max\{u,v,u+v-2uv\}.
   \tag{3}
   \]

   Thus (1)--(2), with

   \[
   u=\min\!\left\{1,\frac{\Delta_p}{p}\right\},
   \qquad
   v=\min\!\left\{1,\frac{\Delta_q}{q}\right\},
   \]

   give \(\Pr[1<H<N]\leq\Psi(u,v)\).

4. In particular, the capped linear estimate is

   \[
   \Pr[1<H<N]
   \leq
   \min\!\left\{1,\frac{\Delta_p}{p}+\frac{\Delta_q}{q}\right\}.
   \tag{4}
   \]

   Since \(\Delta_p,\Delta_q\leq D=\sum_j\deg(F_j)\), this also gives

   \[
   \Pr[1<H<N]\leq\min\!\left\{1,\frac Dp+\frac Dq\right\}.
   \tag{4'}
   \]

5. Let

   \[
   D=\sum_{j=1}^m\deg(F_j),
   \]

   where the degrees on the right are the ordinary total degrees over \(\mathbb Z\). If

   \[
   D\leq \frac{\min(p,q)}2,
   \]

   then

   \[
   \Pr[1<H<N]
   \leq
   \frac Dp+\frac Dq-\frac{2D^2}{pq}.
   \tag{5}
   \]

The qualifications concerning formal zero polynomials, random coefficients, adaptivity, and representation size are given below.

## 2. Exact CRT law

The Chinese remainder theorem identifies a uniform \(X\in(\mathbb Z/N\mathbb Z)^k\) with a pair

\[
(X_p,X_q)\in\mathbb F_p^k\times\mathbb F_q^k
\]

whose two coordinates are uniform and independent. Let

\[
E_r=\{\overline G_r(X_r)=0\}.
\]

The prime \(r\) divides \(G(X)\) exactly on \(E_r\). Consequently,

\[
\begin{array}{c|c}
\text{gcd value}&\text{probability}\\ \hline
1&(1-\alpha_p)(1-\alpha_q)\\
p&\alpha_p(1-\alpha_q)\\
q&(1-\alpha_p)\alpha_q\\
N&\alpha_p\alpha_q.
\end{array}
\tag{6}
\]

A proper gcd occurs precisely on the symmetric difference \(E_p\mathbin\triangle E_q\). Adding the middle two entries of (6) proves (1). This is an exact identity, not a union bound.

## 3. The local root bound

We first recall the elementary finite-field root estimate. If \(0\neq f\in\mathbb F_r[T_1,\ldots,T_k]\) has total degree \(d\), then

\[
|\{x\in\mathbb F_r^k:f(x)=0\}|\leq d r^{k-1}.
\tag{7}
\]

For \(k=1\), this is the usual fact that a nonzero univariate polynomial has at most its degree many roots. For the induction step, write

\[
f=\sum_{i=0}^t h_i(T_1,\ldots,T_{k-1})T_k^i,
\qquad h_t\neq0.
\]

The total degree of \(h_t\) is at most \(d-t\). By induction, at most \((d-t)r^{k-2}\) choices of the first \(k-1\) coordinates kill \(h_t\). For every other choice, the resulting nonzero polynomial in \(T_k\) has at most \(t\) roots; for an exceptional choice, it has at most \(r\) roots. Bounding the two contributions (even with overlap in this upper estimate) gives at most

\[
t r^{k-1}+r(d-t)r^{k-2}=d r^{k-1}
\]

roots. Dividing by \(r^k\) and also using the trivial probability bound \(1\) yields

\[
\Pr[f(x)=0]\leq\min\{1,d/r\}.
\tag{8}
\]

Because a polynomial ring over a field is an integral domain, the assumption that all \(\overline F_{j,r}\) are formally nonzero implies

\[
\overline G_r\neq0,
\qquad
\deg(\overline G_r)=\sum_j\deg(\overline F_{j,r})=\Delta_r.
\]

Applying (8) to \(\overline G_r\) proves (2). Equivalently, one may use that its zero set is the union of the zero sets of the factors and apply Schwartz--Zippel plus a union bound. No independence among the events \(\{\overline F_{j,r}(X_r)=0\}\) is assumed.

## 4. Optimal use of separate local upper bounds

Set

\[
h(a,b)=a+b-2ab=a(1-b)+b(1-a).
\]

On a rectangle \([0,u]\times[0,v]\), this bilinear function attains its maximum at a corner. Its four corner values are

\[
0,\quad u,\quad v,\quad u+v-2uv.
\]

This proves (3). The word “sharp” here has a precise scope: \(\Psi\) is the least upper bound obtainable from only the box constraints \(a\leq u\), \(b\leq v\). It does not assert that every real corner rate is realizable by a polynomial over every prescribed pair of fields.

Since an XOR probability is at most \(1\), and

\[
h(a,b)\leq a+b\leq u+v,
\]

we also have \(h(a,b)\leq\min\{1,u+v\}\). Substituting the local degree bounds proves (4).

Finally, reduction modulo a prime cannot increase total degree, so \(\Delta_r\leq D\). Under \(D\leq\min(p,q)/2\), both \(D/p\) and \(D/q\) lie in \([0,1/2]\). On that rectangle,

\[
\frac{\partial h}{\partial a}=1-2b\geq0,
\qquad
\frac{\partial h}{\partial b}=1-2a\geq0.
\]

Therefore the maximum is attained at \((D/p,D/q)\), which is exactly (5). The negative cross term in (5) is justified only because both local caps are at most \(1/2\); outside that range, the correct consequence of separate caps is the three-corner maximum \(\Psi\), not automatically \(u+v-2uv\).

## 5. Random coefficients: condition on all shared randomness

Let \(C\) be an arbitrary random seed determining the coefficients, supports, number of factors, or any other common construction data, and assume \(C\) is independent of the subsequently sampled \(X\). For a realized value \(c\), let

\[
a_c=\Pr[E_p\mid C=c],
\qquad
b_c=\Pr[E_q\mid C=c],
\]

where the remaining probability is over the fresh CRT coordinates of \(X\). Conditional on \(C=c\), those coordinates are independent, so

\[
\Pr[1<H<N\mid C=c]=a_c+b_c-2a_cb_c.
\tag{9}
\]

Thus the exact unconditional formula is

\[
\Pr[1<H<N]
=\mathbb E_C[a_C+b_C-2a_Cb_C].
\tag{10}
\]

If all local reductions are formally nonzero for every allowed seed, all deterministic degree estimates above apply pointwise and may then be averaged. More generally, define a pointwise cap

\[
U_r(c)=
\begin{cases}
1,&\overline G_{r,c}=0\text{ formally},\\
\min\{1,\deg(\overline G_{r,c})/r\},&\overline G_{r,c}\neq0\text{ formally}.
\end{cases}
\]

Then

\[
\Pr[1<H<N]\leq\mathbb E_C[\Psi(U_p(C),U_q(C))].
\tag{11}
\]

If deterministic caps \(U_p(C)\leq u\) and \(U_q(C)\leq v\) hold for every seed, (11) simplifies to \(\Psi(u,v)\).

It is generally wrong to replace (10) by the same XOR formula applied to the two unconditional marginal rates. Indeed, with \(\bar a=\mathbb E a_C\) and \(\bar b=\mathbb E b_C\),

\[
\mathbb E[h(a_C,b_C)]
=h(\bar a,\bar b)-2\operatorname{Cov}(a_C,b_C).
\tag{12}
\]

Only when the covariance vanishes does the marginal formula survive averaging. A sufficient condition is that all data controlling the reduction modulo \(p\) are independent of all data controlling the reduction modulo \(q\). For example, independently uniform coefficient residues modulo \(N\) have independent CRT reductions, provided there is no additional shared random structure that recouples the two local rate functions.

The covariance warning is genuine even while every local polynomial is formally nonzero. Coefficientwise CRT lifting can produce an integer polynomial whose reductions are any prescribed pair of finite-field polynomials. One lift of

\[
(T^p-T,1)
\]

has conditional rate pair \((a,b)=(1,0)\), and one lift of

\[
(1,T^q-T)
\]

has pair \((0,1)\). Choosing the two lifts with equal probability gives proper-gcd probability \(1\), although the two marginal rates are each \(1/2\), whose naively factorized XOR value is \(1/2\). Conversely, choosing equally between a lift of

\[
(T^p-T,T^q-T)
\]

and the constant polynomial \(1\) gives actual proper-gcd probability \(0\), again with both marginal rates \(1/2\). These examples use nonzero formal polynomials; \(T^r-T\) is zero only as a function on \(\mathbb F_r\).

## 6. Fresh-batch adaptive use

The fixed-polynomial law remains valid under adaptive choice exactly when every evaluation batch is fresh. Formally, let \(\mathcal H_{t-1}\) be the complete transcript before round \(t\). The algorithm may use \(\mathcal H_{t-1}\) and new coefficient randomness \(C_t\) to choose \(F_{t,1},\ldots,F_{t,m_t}\), but it must do so before drawing

\[
X_t\sim\operatorname{Unif}((\mathbb Z/N\mathbb Z)^k),
\]

independently of \((\mathcal H_{t-1},C_t)\). Conditional on the transcript and on all of \(C_t\), equation (9) applies to round \(t\). Thus adaptivity based on earlier batches does not alter the one-round law or its pointwise degree bounds.

Let \(S_t\) denote proper-gcd success in round \(t\). Suppose that for every possible surviving history and every coefficient seed, the conditional success probability is at most a deterministic \(b_t\). Then

\[
\Pr\!\left[\bigcup_{t=1}^T S_t\right]
\leq 1-\prod_{t=1}^T(1-b_t)
\leq\sum_{t=1}^T b_t.
\tag{13}
\]

To prove the first inequality, condition successively on failure in all preceding rounds: every next conditional failure probability is at least \(1-b_t\). Independence between different rounds' success indicators is not required. If the caps depend on the history, the exact statement is instead the corresponding iterated conditional expectation; one may always retain the union bound by averaging the conditional caps.

Freshness is essential. If a polynomial may be selected after seeing the very point at which it will be evaluated, then over any field the choice

\[
F_X(T)=T-X
\]

is formally nonzero of degree \(1\) but vanishes at that point with probability \(1\). Likewise, a nonuniform input distribution concentrated on a root invalidates the uniform Schwartz--Zippel conclusion. Previous samples may influence the next polynomial; the next sample itself may not.

## 7. What happens when a local product is formally zero

Drop the main theorem's formal-nonzero assumption and let

\[
z_r=\mathbf 1[\overline G_r=0\text{ as a formal polynomial}].
\]

If \(z_r=1\), then \(\alpha_r=1\). If \(z_r=0\), \(\alpha_r\) is still the actual zero-function probability and may also equal \(1\). The exact four cases are

\[
\begin{array}{c|c|c}
(z_p,z_q)&\text{possible gcds}&\Pr[1<H<N]\\ \hline
(0,0)&1,p,q,N&\alpha_p+\alpha_q-2\alpha_p\alpha_q\\
(1,0)&p,N&1-\alpha_q\\
(0,1)&q,N&1-\alpha_p\\
(1,1)&N&0.
\end{array}
\tag{14}
\]

Thus the XOR identity itself remains valid if one sets the rate of a formal zero product equal to \(1\); what fails is the degree-based Schwartz--Zippel premise. Also, since \(\mathbb F_r[T_1,\ldots,T_k]\) is a domain,

\[
\overline G_r=0\quad\Longleftrightarrow\quad
\overline F_{j,r}=0\text{ for at least one }j.
\tag{15}
\]

Formal zero and zero as a function must not be conflated. A formally nonzero product can have \(\alpha_r=1\), as the next section makes exact.

## 8. Coefficient content: what it extracts and what it cannot

For an explicitly coefficient-listed integer polynomial \(F\), let \(\operatorname{cont}(F)\) be the nonnegative gcd of its coefficients. Then

\[
\overline F_r=0\text{ formally}
\quad\Longleftrightarrow\quad
r\mid\operatorname{cont}(F).
\tag{16}
\]

Consequently, for \(N=pq\),

\[
d_F=\gcd(\operatorname{cont}(F),N)
\]

exactly classifies the formal pattern:

\[
\begin{array}{c|c}
d_F& (\overline F_p=0,\overline F_q=0)\\ \hline
1&(\text{false},\text{false})\\
p&(\text{true},\text{false})\\
q&(\text{false},\text{true})\\
N&(\text{true},\text{true}).
\end{array}
\tag{17}
\]

Thus a factor that is formally zero at exactly one prime already exposes that prime through an ordinary coefficient gcd; no random evaluation is needed. Gauss's lemma also gives

\[
\operatorname{cont}\!\left(\prod_jF_j\right)=\prod_j\operatorname{cont}(F_j)
\]

up to the harmless sign convention. It is better to inspect individual contents: for \(F_1=p\) and \(F_2=q\), the product content has gcd \(N\) with \(N\), while the two individual contents reveal the two proper factors.

There are three exact limitations.

First, content detects formal coefficientwise zero, not zero as a finite-field function. The primitive polynomial \(T^r-T\) has content \(1\), is formally nonzero modulo \(r\), and nevertheless vanishes at every element of \(\mathbb F_r\).

Second, (16)--(17) presume access to the expanded coefficient list (dense or sparse). An arithmetic circuit can represent a polynomial having exponentially many monomials, so this theorem does not supply a polynomial-time procedure for extracting the content of an arbitrary circuit output. No hardness claim is needed: the point is simply that coefficient scanning is unavailable from that representation without an additional algorithm and proof.

Third, the hypothesis “formally nonzero modulo both unknown primes” is a mathematical condition, not automatically a complexity guarantee. With explicit coefficients, scanning the individual contents either verifies the condition for a factor (gcd \(1\)), detects formal zero at both primes (gcd \(N\)), or already returns a proper divisor. With a circuit representation, the same inference is not licensed merely from the small circuit size.

## 9. The ideal of zero functions

For a prime \(r\), the kernel of evaluation on all of \(\mathbb F_r^k\) is exactly

\[
I_r=(T_1^r-T_1,\ldots,T_k^r-T_k)
\subseteq\mathbb F_r[T_1,\ldots,T_k].
\tag{18}
\]

Every generator vanishes on \(\mathbb F_r^k\), so \(I_r\) is contained in the kernel. Conversely, divide any polynomial successively by the monic polynomials \(T_i^r-T_i\). This gives a congruent remainder \(R\) satisfying

\[
\deg_{T_i}R<r\quad\text{for every }i.
\]

If the original polynomial is a zero function, so is \(R\). Fixing the first \(k-1\) coordinates turns \(R\) into a univariate polynomial in \(T_k\) of degree less than \(r\) with all \(r\) field elements as roots, so it is zero. Its coefficient polynomials therefore vanish on all of \(\mathbb F_r^{k-1}\); induction on \(k\) shows every coefficient is zero. Hence \(R=0\), proving (18).

In particular, a formally nonzero polynomial of total degree strictly less than \(r\) cannot be a zero function. At degree \(r\), \(T_1^r-T_1\) shows sharp failure. Even the factors need not individually be zero functions: in one variable,

\[
T(T^{r-1}-1)=T^r-T
\]

vanishes everywhere, while neither factor does. This is exactly a local OR whose two root sets cover the field. It also shows why content extraction cannot replace function analysis.

## 10. Actual degree is not description size

The degree bounds above concern actual formal total degree. They do not imply analogous bounds in terms of sparse encoding length or arithmetic-circuit size.

A sparse monomial \(T^{2^L}\) has an exponent describable in \(O(L)\) bits but actual degree \(2^L\). An arithmetic circuit can obtain the same monomial using \(L\) repeated squarings, and it can be evaluated modulo \(N\) using only \(L\) modular squarings. Thus polynomial-time evaluability does not force degree \(\operatorname{poly}(\log N)\). Conversely, reduction modulo a prime can erase leading coefficients or create cancellations, so a circuit's syntactic degree is only an upper bound and need not equal \(\delta_{j,r}\).

This distinction is decisive for any complexity conclusion: a lower bound on actual degree is not a lower bound on sparse or circuit description length, nor on modular evaluation time. The zero-function ideal also shows that very high formal degree can encode a simple or even identically zero function on a field.

## 11. Balanced-semiprime degree threshold

The theorem does give a precise barrier for genuinely low **actual degree**. Say the semiprime is \(\kappa\)-balanced if, after ordering \(p\leq q\),

\[
q\leq\kappa p
\]

for some \(\kappa\geq1\). Then

\[
p\geq\sqrt{N/\kappa}.
\tag{19}
\]

Consider fresh adaptive batches satisfying the formal-nonzero hypotheses, and let \(D_t\) be a deterministic upper bound on the sum of the ordinary total degrees used in batch \(t\), valid for every surviving history. Whenever \(D_t\leq p/2\), (5) gives

\[
b_t\leq
\frac{D_t}{p}+\frac{D_t}{q}-\frac{2D_t^2}{pq}
\leq D_t\left(\frac1p+\frac1q\right).
\tag{20}
\]

For \(B=\sum_{t=1}^T D_t\), equations (13), (19), and (20) yield

\[
\Pr[\text{some proper gcd}]
\leq B\left(\frac1p+\frac1q\right)
\leq\frac{2B}{p}
\leq\frac{2\sqrt\kappa\,B}{\sqrt N},
\tag{21}
\]

provided every batch is in the stated low-degree range.

Let \(n=\lceil\log_2(N+1)\rceil\). Then \(2^{n-1}\leq N<2^n\), so (21) implies

\[
\Pr[\text{some proper gcd}]
\leq 2\sqrt\kappa\,B\,2^{-(n-1)/2}.
\tag{22}
\]

For fixed \(\kappa\) and \(B=\operatorname{poly}(n)\), this is exponentially small. Conversely, if the success probability is at least \(\varepsilon\) while every batch remains in the low-degree range, then

\[
B\geq
\frac{\varepsilon}{1/p+1/q}
=\frac{\varepsilon pq}{p+q}
\geq\frac{\varepsilon p}{2}
\geq\frac{\varepsilon\sqrt N}{2\sqrt\kappa}.
\tag{23}
\]

If some batch leaves the low-degree range, it already has \(D_t>p/2\geq\sqrt N/(2\sqrt\kappa)\), which is an even stronger actual-degree threshold for \(0<\varepsilon\leq1\). Hence inverse-polynomial success within this product--gcd framework requires total actual degree

\[
\Omega\!\left(\frac{\sqrt N}{\operatorname{poly}(\log N)}\right)
\]

on constant-balanced semiprimes. Constant success requires \(\Omega(\sqrt N)\) actual degree.

This is not a bit-complexity lower bound. A sparse exponent or a repeated-squaring circuit can cross the \(\sqrt N\) degree threshold with a description of length \(O(\log N)\). Equation (23) rules out only approaches whose actual degree budget itself is polynomial in the input length.

## 12. Verdict: local OR/XOR, not joint decoding

For the operation analyzed here,

\[
\gcd\!\left(\prod_jF_j(X),N\right),
\]

the entire information flow is

\[
\text{within each field: }\bigvee_j[\overline F_{j,r}(X_r)=0],
\qquad
\text{between the two fields: }E_p\mathbin\triangle E_q.
\]

Thus this is exactly local OR followed by global XOR. It may amortize many divisibility tests into one product and one gcd, but it is not a genuine joint decoder: the product discards which factor vanished, uses no compatibility relation among the equations, and derives no benefit from correlations among the local root events beyond their union.

The loss of information can be strict. Suppose one polynomial has local functional profile \((1,0)\) and another has profile \((0,1)\), obtainable with the CRT lifts used in Section 5. Each individual gcd is proper, but their product is divisible by both primes and its gcd is \(N\). More generally,

\[
\left(\bigvee_j E_{j,p}\right)\mathbin\triangle
\left(\bigvee_j E_{j,q}\right)

\]

is not the same event as

\[
\bigvee_j(E_{j,p}\mathbin\triangle E_{j,q}).
\]

Computing all individual gcds retains at least as much information as the product gcd: whenever the product gcd is proper, at least one individual gcd is proper, while the converse can fail as above.

The exact scope is therefore narrow and clear.

* It covers a fixed squarefree semiprime, a uniform CRT sample, and a gcd of one product evaluation.
* It covers random coefficients only after conditioning on all coefficient and structural randomness, and adaptive rounds only with a fresh independent sample in each round.
* It does not cover coefficient choices depending on the same evaluation point, nonuniform samples, resultants, linear algebra on the vector of values, separate-gcd postprocessing, or any other decoder that retains more than the product's zero/nonzero bit.
* It does not by itself extend to prime powers: knowing only whether \(r\mid G(X)\) does not determine the valuation and hence does not determine the gcd with \(r^e\).
* For more than two distinct prime factors, the proper-nontrivial gcd event is not an XOR of two bits. For a fixed polynomial construction and independent CRT coordinates its probability is

  \[
  1-\prod_r(1-\alpha_r)-\prod_r\alpha_r,
  \]

  namely, at least one but not all local divisibility bits are on.
* The low-degree conclusion is about actual degree, not efficient representation. Compact high-degree sparse polynomials and circuits remain outside the claimed barrier.

Accordingly, all stated probability and degree bounds are valid with the qualifications proved above. Any stronger claim that this mechanism provides “joint decoding,” or that the balanced-semiprime degree threshold is a classical running-time lower bound, would be incorrect. The rigorous conclusion is a sharp analysis of a local-union/product-gcd mechanism and of its precise low-actual-degree limitation.
