# Independent proof-only reconstruction: ordinary-unit Dickson traces

## Protocol and scope

This document was reconstructed only from the theorem package in the task statement. I did not read any existing workspace artifact, use the web, or run finite, symbolic, or numerical computations. All arguments below are proofs from first principles.

Throughout, let
\[
N=pq,\qquad 3\le p<q
\]
with distinct odd primes. Put
\[
R=\mathbb Z/N\mathbb Z,\quad U=R^\times,\quad e=N-1,
\quad s=p+q,\quad t=s-2,\quad g=q-p,
\]
and
\[
L=\operatorname{lcm}(p-1,q-1).
\]
The Dickson polynomials are defined in \(\mathbb Z[X]\) by
\[
D_0=2,\qquad D_1=X,\qquad D_{j+1}=XD_j-D_{j-1},
\]
and \(D_{-j}=D_j\). For a unit \(a\) in a commutative ring, write
\[
T(a)=a+a^{-1},\qquad F_j(a)=D_j(T(a)).
\]

## 1. Trace identity and the three relevant indices

### Trace identity over an arbitrary commutative ring

Let \(A\) be any commutative ring and \(a\in A^\times\). I claim that, for every integer \(j\),
\[
D_j(a+a^{-1})=a^j+a^{-j}. \tag{1.1}
\]
For \(j=0,1\), this is exactly the definition. If it holds at \(j\) and \(j-1\), then
\[
\begin{aligned}
(a+a^{-1})(a^j+a^{-j})-(a^{j-1}+a^{-(j-1)})
 &=a^{j+1}+a^{-(j+1)}.
\end{aligned}
\]
Thus induction proves (1.1) for nonnegative \(j\), and the convention \(D_{-j}=D_j\) proves it for all integers. No field assumption or division other than the already available inverse of \(a\) was used.

### The power equality

The difference between the two exponents \(e\) and \(t\) is
\[
e-t=pq-1-(p+q-2)=(p-1)(q-1). \tag{1.2}
\]
For \(a\in U\), reduction modulo \(p\) and modulo \(q\) gives units in the two prime fields. Fermat's theorem and (1.2) therefore give
\[
a^{e-t}=1
\]
in both CRT components, hence in \(R\). Consequently
\[
a^e=a^t\quad\hbox{and}\quad a^{-e}=a^{-t},
\]
so
\[
F_e=F_t\quad\hbox{on }U. \tag{1.3}
\]

The comparison between \(t\) and \(g\) has different signs at the two primes. Modulo the local group orders,
\[
\begin{array}{c|cc}
 &p-1&q-1\\ \hline
t=p+q-2&q-1&p-1\\
g=q-p&q-1&-(p-1).
\end{array} \tag{1.4}
\]
Thus the exponents have the same sign modulo \(p-1\), and opposite signs modulo \(q-1\). Since a trace \(z^j+z^{-j}\) is unchanged when \(j\) is negated, (1.4) gives
\[
F_t=F_g
\]
in each CRT component and hence on all of \(U\). Combining this with (1.3),
\[
F_e=F_t=F_g\quad\hbox{on }U, \tag{1.5}
\]
with the local sign pattern for \(g\) being \((+,-)\) relative to \(e\) at \((p,q)\).

## 2. Complete alias classification

### Prime-field lemma, including self-inverse classes

Let \(r\) be an odd prime and \(n=r-1\). For integers \(u,v\),
\[
z^u+z^{-u}=z^v+z^{-v}\quad\hbox{for every }z\in\mathbb F_r^\times \tag{2.1}
\]
if and only if
\[
u\equiv v\pmod n\quad\hbox{or}\quad u\equiv-v\pmod n. \tag{2.2}
\]

The reverse implication is immediate. For the forward implication, choose a generator \(\xi\) of the cyclic group \(\mathbb F_r^\times\), and for \(k\in\mathbb Z/n\mathbb Z\) let
\[
\chi_k(\xi^j)=\xi^{kj}.
\]
These \(n\) functions are linearly independent over \(\mathbb F_r\). Indeed, the usual finite Fourier inversion is valid because \(n=r-1\ne0\) in \(\mathbb F_r\): if \(f=\sum_k c_k\chi_k\), then
\[
c_h=n^{-1}\sum_{j=0}^{n-1} f(\xi^j)\xi^{-hj}.
\]
This follows from the geometric-sum orthogonality relation.

Equation (2.1) now says
\[
\chi_u+\chi_{-u}=\chi_v+\chi_{-v}.
\]
Linear independence says that the coefficient vectors are equal. If \(u\not\equiv-u\), the left side has coefficient one at each of the two distinct classes \(u,-u\). If \(u\equiv-u\), it has coefficient two at the single class \(u\). Since \(r\) is odd, \(2\ne0\), so a self-inverse class cannot be confused with a pair of distinct classes. The same applies to \(v\), and equality is exactly equality of the two inversion orbits, which is (2.2).

This also covers \(r=3\): then \(n=2\), both exponent classes are self-inverse, and the coefficient-two argument remains valid. In general the only self-inverse classes modulo the even number \(n\) are \(0\) and \(n/2\), and neither was excluded.

### Global CRT classification

The projection \(U\to\mathbb F_p^\times\) is surjective, as is the projection to \(\mathbb F_q^\times\). Therefore \(F_m=F_e\) on all of \(U\) if and only if the prime-field lemma holds in both local components. Equivalently, independently choosing signs \(\epsilon_p,\epsilon_q\in\{1,-1\}\),
\[
m\equiv \epsilon_p e\pmod{p-1},\qquad
m\equiv \epsilon_q e\pmod{q-1}. \tag{2.3}
\]
Locally,
\[
e\equiv q-1\pmod{p-1},\qquad e\equiv p-1\pmod{q-1}. \tag{2.4}
\]
The four sign patterns in (2.3) are represented by
\[
t,\quad -t,\quad g,\quad -g,
\]
respectively: \(t\) has signs \((+,+)\), \(-t\) has \((-,-)\), \(g\) has \((+,-)\), and \(-g\) has \((-,+)\). Two simultaneous congruences modulo \(p-1\) and \(q-1\) determine exactly one class modulo their least common multiple. Hence the complete classification is
\[
\boxed{F_m=F_e\text{ on all }U
\iff m\equiv \pm t\text{ or }\pm g\pmod L.} \tag{2.5}
\]
The displayed classes are a union, not an assertion that four distinct classes always occur. Self-inverse local exponents or arithmetic relations between \(p-1\) and \(q-1\) can make some of them coincide.

### Comparison with the unsymmetrized power map

For unsymmetrized powers, surjectivity of the two CRT projections and cyclicity give
\[
a^m=a^e\text{ for every }a\in U
\iff
m\equiv e\pmod{p-1},\quad m\equiv e\pmod{q-1}.
\]
Thus
\[
\boxed{a^m=a^e\text{ on }U\iff m\equiv e\equiv t\pmod L.} \tag{2.6}
\]
There is no independent local sign choice.

Finally,
\[
t-g=2(p-1).
\]
Therefore \(g\) belongs to the power-map class exactly when \(L\mid2(p-1)\), equivalently when \(q-1\mid2(p-1)\). Since
\[
p-1<q-1
\]
and \((q-1)\) is a positive divisor of \(2(p-1)\), the quotient \(2(p-1)/(q-1)\) is a positive integer strictly below two, and hence is one. Consequently
\[
\boxed{g\equiv t\pmod L\iff q-1=2(p-1)\iff q=2p-1.} \tag{2.7}
\]

## 3. Exact-index factor decoders

These are exact integer decoders, not decoders from an unspecified residue class.

### Decoder from the exact gap \(g\)

Given the exact nonnegative integer \(d=g=q-p\), compute
\[
\Delta_d=d^2+4N.
\]
For the true gap,
\[
\Delta_d=(q-p)^2+4pq=(p+q)^2.
\]
Let \(S=\sqrt{\Delta_d}\) be the exact nonnegative integer square root. Then
\[
P=\frac{S-d}{2},\qquad Q_0=\frac{S+d}{2} \tag{3.1}
\]
are \(p,q\).

A verified implementation does not merely assume the promise. It checks that \(\Delta_d\) is a square; that \(S\equiv d\pmod2\); that \(S>d\), \(d>0\), and hence \(1<P<Q_0\); and finally that \(PQ_0=N\). These checks enforce exact parity, positivity, distinctness, and product correctness. On the theorem's input, \(S\) and \(d\) are both even because \(p,q\) are odd.

### Decoder from the exact sum index \(t\)

Given the exact nonnegative integer \(u=t\), set \(S=u+2\) and compute
\[
\Delta_u=S^2-4N.
\]
For the true index, \(S=p+q\) and
\[
\Delta_u=(p+q)^2-4pq=(q-p)^2.
\]
Let \(d=\sqrt{\Delta_u}\) be its exact nonnegative square root. Then again
\[
P=\frac{S-d}{2},\qquad Q_0=\frac{S+d}{2}. \tag{3.2}
\]
Verification checks \(\Delta_u\ge0\), exact squareness, \(S\equiv d\pmod2\), positivity and nontriviality of both outputs, their ordering, and \(PQ_0=N\). For the promised input, \(S,d\) are even and all checks pass.

If a candidate index has bit length polynomial in \(\log N\), integer addition, multiplication, exact integer square root, parity and comparison tests, and the final multiplication check all have polynomial bit complexity. No dense Dickson polynomial is involved in these decoders.

By contrast, knowing only that an observed representative is
\[
m=g+kL\quad\hbox{or}\quad m=t+kL
\]
for an unknown integer \(k\) (and, in the intended setting, unknown \(L\)) does not supply the exact integer needed in either discriminant. Substituting an arbitrary representative generally destroys exact squareness. Choosing the correct multiple requires an additional bounded search, metric, order computation, or other argument. The congruence itself supplies none, and there can be exponentially many plausible multiples in a natural \(O(N)\)-sized range. This is a limitation of these exact decoders, not an information-theoretic assertion that the already public integer \(N\) does not determine its factors.

## 4. Dickson identities and exact trace-interface nonidentifiability

Introduce an indeterminate \(Z\). The substitution homomorphism
\[
\mathbb Z[X]\longrightarrow\mathbb Z[Z,Z^{-1}],\qquad X\longmapsto Z+Z^{-1}
\]
is injective: if a nonzero polynomial has degree \(d\) and leading coefficient \(c\), its image has highest Laurent exponent \(d\) with coefficient \(c\).

Using (1.1) in the Laurent ring,
\[
\begin{aligned}
D_j(D_k(Z+Z^{-1}))
 &=D_j(Z^k+Z^{-k})\\
 &=Z^{jk}+Z^{-jk}\\
 &=D_{jk}(Z+Z^{-1}).
\end{aligned}
\]
Injectivity therefore proves the polynomial identity
\[
\boxed{D_j(D_k(X))=D_{jk}(X).} \tag{4.1}
\]
Likewise,
\[
\begin{aligned}
&D_{u+v}(Z+Z^{-1})+D_{u-v}(Z+Z^{-1})\\
&=Z^{u+v}+Z^{-(u+v)}+Z^{u-v}+Z^{-(u-v)}\\
&=(Z^u+Z^{-u})(Z^v+Z^{-v}),
\end{aligned}
\]
so
\[
\boxed{D_{u+v}(X)+D_{u-v}(X)=D_u(X)D_v(X).} \tag{4.2}
\]
Both identities lie in \(\mathbb Z[X]\), so they remain true after substitution into every commutative ring.

Now specify the exact interface statement. Suppose a representative index \(m\) is accessible only through the extensional trace map
\[
b\longmapsto F_m(b)
\]
on allowed unit bases, together with ring operations and Dickson operations on already returned trace values. If \(m,m'\) are in the same global alias class, then \(F_m(b)=F_{m'}(b)\) for every allowed base \(b\). Any fixed ring expression in returned values is consequently equal in the two worlds. The same remains true adaptively: by induction on calls, equal histories cause the same next chosen base and operation, which returns an equal value and preserves equal histories. Repeated calls, powers, products, and substitution of a trace into \(D_k\) are special cases. Choosing bases does not help because the functional equality holds for every unit base. Querying a powered base merely gives
\[
F_m(b^k)=F_{km}(b)=D_k(F_m(b)),
\]
which is again determined by the same trace.

This is deliberately an interface quotient, not a lower bound for arithmetic in the explicit ring \(\mathbb Z/N\mathbb Z\). In particular, (4.2) determines the sum of the two shifted traces \(F_{m+k}\) and \(F_{m-k}\), but it does not select either shifted value individually. An oracle that separately exposes a shift tied to the hidden representative would be a stronger interface and is not covered by this tautological argument.

The unsymmetrized public value \(a^e\) is also strictly stronger because it retains a local orientation rather than quotienting by inversion. Nevertheless (2.6) shows that its full functional alias is the still unknown same-sign class \(t\pmod L\). Knowing and evaluating the large public index \(e=N-1\) does not, by this identity alone, choose the exact short integer \(t\).

## 5. Shifted-trace quadratics and mixed roots

For public
\[
X=T(a),\quad Y=D_e(X),\quad K=D_k(X),\quad
A=D_{e+k}(X),\quad B=D_{e-k}(X),
\]
identity (4.2) immediately gives
\[
\boxed{A+B=YK.} \tag{5.1}
\]
For the product, use the Laurent representation:
\[
\begin{aligned}
AB
&=(a^{e+k}+a^{-(e+k)})(a^{e-k}+a^{-(e-k)})\\
&=a^{2e}+a^{-2e}+a^{2k}+a^{-2k}\\
&=D_{2e}(X)+D_{2k}(X)\\
&=(Y^2-2)+(K^2-2).
\end{aligned}
\]
Hence
\[
\boxed{AB=Y^2+K^2-4.} \tag{5.2}
\]
Thus \(A,B\) are two roots in \(R\) of
\[
Z^2-YKZ+(Y^2+K^2-4)=0. \tag{5.3}
\]

Define the hidden short-index shifts
\[
C=D_{g+k}(X),\qquad D=D_{g-k}(X).
\]
The local sign table (1.4) gives
\[
\begin{array}{c|cc}
 &\bmod p&\bmod q\\ \hline
C&A&B\\
D&B&A.
\end{array} \tag{5.4}
\]
Indeed, modulo \(p\), \(g\equiv e\), while modulo \(q\), \(g\equiv-e\); also \(D_{-j}=D_j\). Therefore \(C,D\) are precisely the two CRT-mixed roots obtained by retaining the \(A,B\) ordering at \(p\) and reversing it at \(q\). They also satisfy (5.3), because a polynomial equation over \(R\cong\mathbb F_p\times\mathbb F_q\) is componentwise.

There is an exact gcd trichotomy. Compute
\[
d_0=\gcd(A-B,N)
\]
using integer representatives.

* If \(1<d_0<N\), then one local difference is zero and the other is nonzero. This already returns a factor. This includes the case in which the quadratic has a double root at exactly one of the two primes.
* If \(d_0=1\), then \(A-B\) is nonzero at both primes. From (5.4),
  \[
  C-A\equiv0\pmod p,\qquad C-A\equiv B-A\not\equiv0\pmod q,
  \]
  so
  \[
  \gcd(C-A,N)=p.
  \]
  The other coherently mixed root analogously yields \(q\) when compared with \(A\). Thus, in the unit-difference case, selecting either genuinely mixed root is factoring-sufficient.
* If \(d_0=N\), then \(A=B\) at both primes. The quadratic is locally double on both sides, the two putative orientations coincide, and CRT mixing creates no new root. This particular instance contains no orientation to select.

The readily testable quantities
\[
Y^2-4,\qquad K^2-4
\]
are local squares of the corresponding oriented Laurent differences, and \(A-B\) is another orientation-sensitive difference. A proper gcd of any of these with \(N\) is a lucky factorization event and should be retained. No uniform success probability for those events is asserted here, for any choice or distribution of \(a,k\).

Equations (5.1)--(5.4) prove only that a coherent mixed-root selector would factor in the nondegenerate case. They do not construct such a selector. Polynomially many quadratics obtained from correlated bases or shifts remain correlated, and nothing above proves that their mixed orientations can be chosen consistently or with nonnegligible probability.

## 6. Derivative identities and the orientation that remains missing

Work first in \(\mathbb Z[Z,Z^{-1}]\) with \(X=Z+Z^{-1}\). Differentiating
\[
D_m(Z+Z^{-1})=Z^m+Z^{-m}
\]
with respect to \(Z\) gives
\[
D_m'(X)(1-Z^{-2})=m(Z^{m-1}-Z^{-m-1}),
\]
or
\[
(Z-Z^{-1})D_m'(X)=m(Z^m-Z^{-m}). \tag{6.1}
\]
Now
\[
X^2-4=(Z-Z^{-1})^2
\]
and
\[
D_{m+1}(X)-D_{m-1}(X)
=(Z-Z^{-1})(Z^m-Z^{-m}).
\]
Multiplying (6.1) by \(Z-Z^{-1}\) and using injectivity of the Laurent substitution proves
\[
\boxed{(X^2-4)D_m'(X)=m\bigl(D_{m+1}(X)-D_{m-1}(X)\bigr).} \tag{6.2}
\]
Squaring (6.1), or squaring (6.2) and cancelling the nonzero polynomial \(X^2-4\) in the integral domain \(\mathbb Z[X]\), gives
\[
\boxed{(X^2-4)(D_m'(X))^2=m^2(D_m(X)^2-4).} \tag{6.3}
\]
The formulas hold for nonnegative \(m\), and the convention \(D_{-m}=D_m\) shows that they also hold for negative \(m\) with the displayed signed first factor and squared second factor.

Equality as value functions on a finite trace set cannot be differentiated. To see this rigorously, let \(S\) be any finite set of distinct elements of a field and let
\[
V_S(X)=\prod_{x\in S}(X-x).
\]
The polynomials \(P\) and \(P+V_S\) agree at every point of \(S\), but at each \(x\in S\),
\[
V_S'(x)=\prod_{y\in S,\,y\ne x}(x-y)\ne0.
\]
Their derivatives therefore disagree there. A prime-field trace set \(\{z+z^{-1}:z\in\mathbb F_r^\times\}\) is just such a finite set. Hence the finite functional equality \(D_e=D_g\) on trace inputs is not a polynomial identity and does not imply \(D_e'=D_g'\) on those inputs.

This does not mean that \(D_e'(X)\) is unavailable. The index \(e=N-1\) is public, and its derivative value can be evaluated in polynomially many ring operations by binary Dickson recurrences while propagating derivatives. Formula (6.1) interprets it locally as
\[
(a-a^{-1})D_e'(T(a))=e(a^e-a^{-e}). \tag{6.4}
\]
Thus it is one known scaled comparison between an orientation at the base and the coherently transported orientation at exponent \(e\). Equivalently, (6.2) relates it to the known scaled shifted-root difference \(e(D_{e+1}-D_{e-1})\). It does not by itself choose the sign of either Laurent difference, especially where \(X^2-4\) is a zero divisor. What remains missing is the derivative/orientation belonging to a hidden short representative such as \(g\), or an independent comparator that would expose the local sign reversal. Functional trace equality does not provide that object.

Index division also needs care. Neither prime divides \(g=q-p\): if \(p\mid g\), then \(p\mid q\), and if \(q\mid g\), then \(q\mid p\), both impossible for distinct primes. Also
\[
t\equiv p-2\pmod q,
\]
which is nonzero because \(3\le p<q\), so \(q\nmid t\). But
\[
t\equiv q-2\pmod p
\]
can vanish; for example, \(p=3,q=5\) gives \(t=6\). Thus division by a hidden or guessed candidate index is not uniformly legal modulo \(N\). A failed inversion may itself reveal a factor by gcd, but it cannot be silently assumed away.

## 7. The lift-dependent first-order identity modulo \(N^2\)

Fix a unit lift \(\widetilde a\) modulo \(N^2\), and put
\[
\phi=(p-1)(q-1)=e-t.
\]
Euler's theorem modulo \(N\) gives \(\widetilde a^\phi\equiv1\pmod N\), so the lift-dependent Fermat quotient
\[
Q=\frac{\widetilde a^\phi-1}{N}\pmod N \tag{7.1}
\]
is well-defined. Thus
\[
\widetilde a^\phi\equiv1+NQ\pmod{N^2},\qquad
\widetilde a^{-\phi}\equiv1-NQ\pmod{N^2}.
\]
Since \(e=t+\phi\),
\[
\begin{aligned}
T(\widetilde a^e)-T(\widetilde a^t)
&=\widetilde a^t(\widetilde a^\phi-1)
 +\widetilde a^{-t}(\widetilde a^{-\phi}-1)\\
&\equiv NQ(\widetilde a^t-\widetilde a^{-t})\pmod{N^2}.
\end{aligned}
\]
Therefore
\[
\boxed{T(\widetilde a^e)-T(\widetilde a^t)
\equiv NQ(\widetilde a^t-\widetilde a^{-t})\pmod{N^2}.} \tag{7.2}
\]

Both \(Q\) and (7.2) are tied to the chosen lift. More precisely, every other lift of the same unit modulo \(N\) has the form
\[
\widetilde a'=\widetilde a(1+Nh)\pmod{N^2}
\]
for some \(h\pmod N\). Then
\[
Q'=Q+\phi h\pmod N. \tag{7.3}
\]
The change is coherent with the trace formula: for every integer \(j\),
\[
T((\widetilde a')^j)
\equiv T(\widetilde a^j)+Njh(\widetilde a^j-\widetilde a^{-j})\pmod{N^2}.
\]
Subtracting the cases \(j=e,t\), and using \(\widetilde a^e\equiv\widetilde a^t\pmod N\), changes the left side of (7.2) by
\[
N\phi h(\widetilde a^t-\widetilde a^{-t})\pmod{N^2},
\]
exactly matching (7.3) on the right side.

The exact value \(\phi\) is factor-determining, because
\[
p+q=N+1-\phi
\]
and the discriminant decoder then recovers \(p,q\). But (7.1) does not say that \(Q\) is supplied: computing it by its definition already uses the hidden \(\phi\). Nor does (7.2) isolate \(\phi\), \(Q\), or the oriented difference. Values modulo \(N^2\) carry first-order lift information absent from the original modulo-\(N\) trace equality, so pooling such data is genuinely a new public-data regime. The identity is neither a decoder nor an obstruction for that regime.

## 8. Intervals, BSGS, and representation cost

Let \(n=\lceil\log_2N\rceil\). A worst-case candidate interval of length \(\Theta(N)\) has \(2^{\Theta(n)}\) entries. Ordinary baby-step/giant-step search takes the square root of the cardinality, not its logarithm, and is still \(2^{\Theta(n)}\). Even a \(\Theta(\sqrt N)\)-sized interval has square-root search cost \(N^{1/4}=2^{\Theta(n)}\). No balance or distribution promise in the theorem supplies a polynomial-size interval around \(g\) or \(t\).

A Dickson value \(D_j(X)\) can be evaluated from the binary expansion of \(j\) in polynomially many ring operations, using identities such as
\[
D_{2u}=D_u^2-2,
\qquad D_{2u+1}=D_uD_{u+1}-X.
\]
That compact evaluation circuit does not make the dense polynomial \(D_j\), which has degree \(|j|\), a polynomial-size object. In particular, expanding high-degree polynomials or forming generic dense resultants and determinants may require exponentially many coefficients or exponentially long intermediate/output representations. Compact structure might permit a special algorithm, but it must be exhibited and analyzed; fast point evaluation alone does not supply it.

Conversely, a list of only polynomially many polynomial-bit candidate values for exact \(g\) or \(t\), together with a polynomial-time way to verify the list, would suffice: apply the decoders in Section 3 to every entry and retain a verified nontrivial product decomposition. No such metric, interval reduction, or list construction is proved here.

## 9. Generic quotient-by-inversion and full generic-group theorems

These theorems concern opaque random encodings. They are not the explicit ring \(\mathbb Z/N\mathbb Z\).

### Quotient-by-inversion model

Let \(\ell\) be an odd prime and let \(E\) be uniform in \(\mathbb F_\ell\). Write
\[
[z]=\{z,-z\}.
\]
There are \(K\ge1\) tags. In each tag, an independent random injective encoding of the orbit set is used, and handles for \([0],[1],[E]\) are initially exposed. Across all tags an adaptive algorithm makes \(Q\) oracle calls, with \(q_i\) calls in tag \(i\) and \(\sum_iq_i=Q\). Within one tag a call is either
\[
[u]\longmapsto[cu]
\]
for a publicly chosen scalar \(c\), or
\[
[u],[v]\longmapsto\{[u+v],[u-v]\}.
\]
The latter unordered pair is well-defined despite the choice of signs for \(u,v\). There are no cross-tag operations, and encodings are opaque: the algorithm can retain handles and test the equality information exposed by the oracle, but cannot decode a handle into a field element.

Suppose the algorithm outputs at most \(M\) field residues. Then
\[
\boxed{
\Pr[\exists h\text{ in the output list}:h=\pm E]
\le \min\left(1,\frac{2M+B}{\ell}\right),
} \tag{9.1}
\]
where
\[
\boxed{
B=2\sum_{i=1}^K\binom{2q_i+3}{2}
\le2\binom{2Q+3}{2}+6(K-1).
} \tag{9.2}
\]

#### Proof by a lazy random-encoding coupling

Use a formal indeterminate \(x\). Every handle that can arise in a tag has a formal orbit
\[
[ax+b],\qquad a,b\in\mathbb F_\ell,
\]
because this is true of \([0],[1],[x]\) and is preserved by both allowed calls. Two formal expressions are the same formal orbit exactly when their coefficient pairs differ by an overall sign. A lazy ideal oracle recognizes such formal equality and reuses the handle. Otherwise it assigns a fresh uniformly random unused encoding in that tag. Its random choices do not depend on the eventual value of \(E\).

A scalar call introduces at most one new formal orbit and an addition-pair call at most two. Thus tag \(i\) has at most
\[
H_i=2q_i+3
\]
formal handle appearances, including the three initial ones. Consider any two appearances that are distinct as formal orbits, say \([ax+b]\) and \([a'x+b']\). They collide after setting \(x=E\) exactly if
\[
(aE+b)=a'E+b'\quad\hbox{or}\quad
(aE+b)=-(a'E+b'). \tag{9.3}
\]
Neither equation is an identity, because an identity would make the two formal orbits equal. Each nonidentity affine linear equation has at most one root. Hence every pair has at most two bad secret values.

Counting all pairs accounts for every possible first surprise collision:

* collisions among the three initially exposed handles;
* a collision between the two outputs of the same addition-pair call;
* a collision of a new output with any old handle, including handles from earlier calls.

Formal identities are not surprises and only reduce the count. There are no cross-tag collision tests, so cross-tag pairs need not be counted. For a fixed ideal transcript, the union of all bad secret values therefore has size at most
\[
2\sum_i\binom{H_i}{2}=B. \tag{9.4}
\]

This counting remains valid under adaptivity. Fix the algorithm's random coins and all lazy random labels. The ideal transcript then fixes the subsequent choices of public scalars and operands, hence fixes all formal affine expressions and the bad set. If \(E\) is outside that set, induction over calls shows that the real encoded execution follows the same transcript: before the first alleged divergence all earlier handles agree under the coupling, and the next operation cannot create the surprise collision needed for a divergence. Conditioned on no surprise collision, the encountered actual orbits are distinct exactly when the formal orbits are distinct, so their random injective labels have the same distribution as the lazy labels.

For this fixed ideal transcript, the output list is independent of \(E\). Its up-to-sign coverage contains at most \(2M\) field residues. Success in the real experiment can therefore occur only when \(E\) lies in that coverage or in the bad set (9.4), a union of size at most \(2M+B\). Averaging over the fixed coins and lazy labels proves (9.1).

Finally,
\[
\binom{2q+3}{2}=2q^2+5q+3.
\]
Since \(\sum_iq_i^2\le Q^2\),
\[
\sum_i\binom{2q_i+3}{2}
\le2Q^2+5Q+3K
=\binom{2Q+3}{2}+3(K-1),
\]
which proves the second inequality in (9.2). If the bound exceeds \(\ell\), the outer minimum simply records the trivial probability bound one.

#### Public-subset, prior, and orbit-output variants

If \(E\) is uniform on a public subset \(\mathcal S\subseteq\mathbb F_\ell\) of size \(H\), the same fixed-transcript argument intersects both exceptional sets with \(\mathcal S\), giving
\[
\Pr[\text{success}]\le
\min\left(1,\frac{2M+B}{H}\right). \tag{9.5}
\]
For an arbitrary public prior \(\pi\) on field residues with maximum point mass
\[
\mu=\max_x\pi(x),
\]
the union has at most \(2M+B\) atoms, so
\[
\Pr[\text{success}]\le\min(1,(2M+B)\mu). \tag{9.6}
\]

The factor \(2M\) is a coverage count, not an intrinsic collision factor. If both the secret and the reported candidates are inversion-orbit objects, one reported orbit covers one secret-orbit atom, so \(2M\) is replaced by \(M\). For example, if the secret is uniform on a public set of \(H\) orbit atoms, then
\[
\Pr[\text{success}]\le\min\left(1,\frac{M+B_{\rm orb}}{H}\right), \tag{9.7}
\]
where \(B_{\rm orb}\) is the number of bad orbit atoms and \(B_{\rm orb}\le B\) is always a valid bound. With maximum orbit-atom prior mass \(\mu_{\rm orb}\), the corresponding bound is \(\min(1,(M+B_{\rm orb})\mu_{\rm orb})\). More generally, the coverage term is the number of secret atoms covered by the output semantics.

### Stronger-access ordinary generic-group model

Now give each tag an independent ordinary injective encoding of the field's additive group, so \(z\) and \(-z\) have distinct encodings unless \(z=0\). Initially expose encodings of \(0,1,E\), and allow \(q_i\) ordinary group-or-scalar operations in tag \(i\), one output handle per operation, with \(\sum_iq_i=Q\). The algorithm may retain oriented handles, but it still cannot inspect or decode their random encodings.

Every formal handle is an affine linear form \(ax+b\). There are at most \(q_i+3\) handle appearances in tag \(i\). Two distinct formal forms collide at \(E\) only if
\[
(a-a')E+(b-b')=0,
\]
which has at most one root. The identical lazy-coupling and first-divergence proof therefore gives the surprise-collision count
\[
\boxed{
C=\sum_{i=1}^K\binom{q_i+3}{2}
\le\binom{Q+3}{2}+3(K-1).
} \tag{9.8}
\]
Indeed,
\[
\binom{q+3}{2}=\frac{q^2+5q+6}{2}
\]
and \(\sum_iq_i^2\le Q^2\).

If the output is a list of at most \(M\) residues and success means listing \(E\) up to inversion, its coverage still has at most \(2M\) residues. Thus
\[
\boxed{
\Pr[\exists h:h=\pm E]
\le\min\left(1,\frac{2M+C}{\ell}\right).
} \tag{9.9}
\]
For a public \(H\)-element residue subset, replace the denominator by \(H\); for maximum residue prior mass \(\mu\), the bound is \(\min(1,(2M+C)\mu)\). If secret and output are orbit atoms, replace the \(2M\) coverage by \(M\) and count collision roots on that atom space, exactly as above.

### Why these generic theorems do not transfer to the factoring ring

The prime-field proofs rely on two facts: all formal handles are affine functions of one uniform field secret, and a nonidentity affine collision equation has a uniformly bounded number of roots. Composite-order groups and non-generating bases require explicit order and root-multiplicity information; congruences can collapse on proper subgroups, and their number of solutions depends on gcds with the relevant orders.

The explicit ring \(\mathbb Z/N\mathbb Z\) supplies much more than opaque handles. Its two CRT components have generally unequal composite exponent orders; chosen bases can be non-generators and have different local orders; encodings across bases are arithmetically correlated; integer representatives permit addition, multiplication, equality, and gcd with \(N\); CRT mixing itself is visible through proper gcds; and coordinates may be fed to resultants, determinants, or other arithmetic constructions. Moreover, the factoring secret \((p,q)\), or an index derived from it, is a worst-case arithmetic secret, not a uniform \(E\in\mathbb F_\ell\). Therefore neither (9.1) nor (9.9) is an explicit-ring hardness theorem or a bound on a concrete factoring algorithm.

## 10. Promise boundaries and unresolved branches

Every conclusion above is conditional on the distinct-odd-semiprime unit setting, and the following branches cannot be silently absorbed into it.

* **Nonunits.** Before using \(a^{-1}\), compute \(d=\gcd(a,N)\). A proper gcd already factors \(N\); gcd one enters the unit analysis; gcd \(N\) supplies no inverse. Trace formulas that require an inverse do not cover the last case.
* **Equal primes.** If \(p=q\), then \(g=0\), there is only one prime component rather than two independent sign choices, and the mixed-root argument disappears. A perfect-square test can detect \(N=p^2\), but that is a separate branch.
* **Prime powers and repeated factors.** Unit exponents modulo \(p^k\), lifting behavior, nilpotents, and repeated CRT factors differ from the squarefree two-prime proof. Prime-field sign classification alone does not establish the required identities or a full decoder there.
* **Three or more prime factors.** There can be an independent local inversion choice at every CRT component, producing up to \(2^r\) sign patterns. The two-factor quantities \(g,t\) and the two-root orientation argument no longer describe the problem, and obtaining one split would still require recursive factorization.
* **Even and prime inputs.** An even composite has the immediate factor \(2\), while \(2\) itself and odd primes require primality handling. The semiprime proof says nothing about producing a nontrivial factor of a prime.
* **Candidate-index divisibility.** Section 6 proves that \(g\) is a unit modulo \(N\) but \(t\) need not be. Arbitrary candidates can share either factor. Any algorithm that divides by a candidate must branch on its gcd, retaining a proper gcd as success rather than assuming invertibility.
* **Hidden expensive subroutines.** Computing \(L\), \(\phi\), local orders, discrete logarithms, CRT components, or a nontrivial square root modulo \(N\) cannot be inserted as a free step: each may contain the original factoring difficulty. Likewise, a purported root selector must not call factoring internally.
* **Bit complexity.** A polynomial-time result must bound the bit lengths of every output and intermediate object by a polynomial in the input length. Exponentially long lists, dense degree-\(\Theta(N)\) polynomials, or exponentially large generic determinants are not polynomial-time merely because individual modular evaluations are fast.
* **Recursion and all inputs.** Even a successful split on the promised semiprime family is not by itself an all-input factoring algorithm. One needs termination, primality tests, treatment of repeated factors and all arities, and a polynomial total-cost analysis over recursive calls.

Accordingly, this package establishes a narrow method failure: ordinary unit traces identify the four CRT sign aliases in (2.5), and ring expressions that only reuse the displayed trace interface cannot select among them. It also establishes an opaque generic-model boundary under the precise random-encoding assumptions of Section 9. It does **not** provide the requested all-input factoring algorithm, and it does **not** prove hardness for explicit arithmetic modulo \(N\).

In particular, the following remain open here: coherent mixed-root selection, structured explicit-coordinate resultants or determinants, recovery of a hidden derivative orientation or an independent comparator, pooling of lift-dependent \(N^2\) data, polynomial metric/interval/list methods, useful distributions for non-generating bases, and extension to all integer inputs.

## Verdict

**PASS.** Every claim in the stated narrow theorem package has an end-to-end proof above, with the generic-model and explicit-arithmetic boundaries kept separate.
