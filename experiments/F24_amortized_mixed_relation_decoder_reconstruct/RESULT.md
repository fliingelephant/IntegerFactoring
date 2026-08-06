# Proof-blind reconstruction: amortized mixed-relation product

## Scope and conventions

This reconstruction uses only the supplied theorem statement, the research protocol, and P21 for the requested comparison. It does not rely on the candidate proof.

Let

\[
N=pq,\qquad 53\le p<q<2p,
\]

where \(p,q\) are distinct odd primes. Put

\[
h=\lfloor\sqrt N\rfloor,\quad
b=\lfloor\log _2h\rfloor,\quad
K=b-3,\quad T=2^K,\quad m=T-1.
\]

For \(S\subseteq[K]\), write

\[
L_S=\sum_{i\in S}a_i,\qquad
Q_K=\prod_{\varnothing\ne S\subseteq[K]}L_S
\]

in \(R=\mathbb Z/N\mathbb Z\), with \(L_\varnothing=0\). For \(r\in\{p,q\}\), reduction to \(\mathbb F_r\) is understood whenever an event modulo \(r\) is discussed. Define

\[
I_{S,r}=\mathbf 1_{\{L_S=0\pmod r\}},\quad
Z_r=\sum_{\varnothing\ne S\subseteq[K]}I_{S,r},\quad
E_r=\{Z_r>0\},\quad
\mu_r=m/r.
\]

All empty products below are \(1\). I use the resultant convention

\[
\operatorname{Res}(f,g)
=a_f^{\deg g}\prod_{f(\alpha)=0}g(\alpha),
\]

where \(a_f\) is the leading coefficient of \(f\). This fixes every sign.

## 1. Local zero events and the promised factorer

### Pairwise independence

CRT sends a uniform \(a_i\pmod N\) to an independent uniform pair

\[
(a_i\bmod p,a_i\bmod q)\in\mathbb F_p\times\mathbb F_q.
\]

Thus, for fixed \(r\), \(a=(a_1,\ldots,a_K)\) is uniform in \(\mathbb F_r^K\). For every nonempty \(S\), its incidence vector \(v_S\in\{0,1\}^K\) is nonzero, so \(v_S\cdot a=L_S\) is uniform and

\[
\Pr(I_{S,r}=1)=1/r.
\]

If \(S\ne U\), the vectors \(v_S,v_U\) are linearly independent over every field. Two nonzero scalar multiples have the same zero-coordinate set, hence the same support; distinct incidence supports cannot be scalar multiples. Therefore

\[
a\longmapsto(L_S,L_U)
\]

has rank \(2\), its output is uniform in \(\mathbb F_r^2\), and

\[
\Pr(I_{S,r}=I_{U,r}=1)=1/r^2.
\]

There is no exceptional characteristic in this argument. It follows that

\[
\mathbb E Z_r=\frac mr=\mu_r,\qquad
\operatorname{Var}(Z_r)
=m\frac1r\left(1-\frac1r\right)
=\mu_r\left(1-\frac1r\right).
\]

Cauchy--Schwarz applied to \(Z_r\mathbf1_{E_r}\) gives

\[
(\mathbb EZ_r)^2\le \mathbb E(Z_r^2)\Pr(E_r).
\]

Since

\[
\mathbb E Z_r^2=\mu_r^2+\mu_r(1-1/r),
\]

we obtain

\[
\boxed{\Pr(E_r)\ge
\frac{\mu_r}{\mu_r+1-1/r}.}
\]

### Floor-sensitive bounds

From \(2^b\le h<2^{b+1}\) and \(T=2^{b-3}\),

\[
8T\le h<16T.
\]

Because \(h\) and \(16T\) are integers, \(h<16T\) implies \(h+1\le16T\). Hence

\[
\sqrt N<h+1\le16T,\qquad
T\le h/8\le\sqrt N/8.
\]

Also \(\sqrt N>p\ge53\), so \(h\ge53\), \(b\ge5\), \(K\ge2\), and \(T\ge4\).

For either \(r=p\) or \(r=q\),

\[
r\le q=\sqrt N\sqrt{q/p}<\sqrt2\sqrt N.
\]

Consequently,

\[
\frac{r}{32\sqrt2}
\le\frac{q}{32\sqrt2}
<\frac{\sqrt N}{32}
<\frac T2
\le T-1,
\]

which proves

\[
\frac{T-1}{r}>\frac1{32\sqrt2}.
\]

In the other direction,

\[
\frac{T-1}{r}<\frac{T}{r}
\le\frac{\sqrt N}{8r}.
\]

For \(r=p\), the last expression is

\[
\frac18\sqrt{q/p}<\frac{\sqrt2}{8};
\]

for \(r=q\), it is \(\frac18\sqrt{p/q}<1/8\). Thus every floor is retained in

\[
\boxed{\frac1{32\sqrt2}<\mu_r<\frac{\sqrt2}{8}.}
\]

### XOR probability and the precise OR statement

Let

\[
\alpha=\frac1{32\sqrt2+1},\qquad
\beta=1-\frac{\sqrt2}{8}.
\]

The second-moment estimate gives

\[
\Pr(E_r)
\ge\frac{\mu_r}{\mu_r+1-1/r}
>\frac{\mu_r}{\mu_r+1}
>\alpha.
\]

The union bound gives

\[
\Pr(E_r)\le\sum_{S\ne\varnothing}\Pr(L_S=0)
=\mu_r<\frac{\sqrt2}{8},
\]

so \(\Pr(E_r^c)>\beta\).

The entire \(p\)-coordinate array of the \(a_i\)'s is independent of the entire \(q\)-coordinate array under CRT. Since \(E_p,E_q\) depend on those separate arrays, they are independent. In the field \(\mathbb F_r\),

\[
Q_K=0\pmod r
\quad\Longleftrightarrow\quad
\bigvee_{S\ne\varnothing}(L_S=0\pmod r).
\]

This is the exact cancellation-free **local** OR. It is essential that “local” means in each field component. It is not a global OR in \(\mathbb Z/N\mathbb Z\): factors congruent to \(p\) and \(q\) can multiply to zero modulo \(N\) although neither factor is zero modulo \(N\). That is exactly why the useful event is an XOR.

Because \(N\) is squarefree,

\[
1<\gcd(Q_K,N)<N
\quad\Longleftrightarrow\quad
E_p\mathbin\triangle E_q.
\]

Independence now yields

\[
\begin{aligned}
\Pr(E_p\mathbin\triangle E_q)
&=\Pr(E_p)\Pr(E_q^c)+\Pr(E_q)\Pr(E_p^c)\\
&>2\alpha\beta.
\end{aligned}
\]

In particular,

\[
\boxed{
\Pr(1<\gcd(Q_K,N)<N)
\ge
\frac{2}{32\sqrt2+1}
\left(1-\frac{\sqrt2}{8}\right).}
\]

### Conditional Las Vegas conclusion

Assume a uniform exact evaluator computes \(Q_K\pmod N\) in bit time polynomial in \(\log N\) and \(K\). On a promised input of the displayed form, compute \(h,b,K\); sample fresh independent uniform residues \(a_1,\ldots,a_K\); evaluate \(Q_K\); compute \(d=\gcd(Q_K,N)\); and return \(d\) when \(1<d<N\), restarting otherwise.

Uniform residues are sampled exactly by rejection from a power-of-two interval, with acceptance probability greater than \(1/2\). Since \(K=O(\log N)\), sampling and gcd computation have polynomial bit cost. Every returned divisor is correct. The proved constant success probability makes the number of trials geometric with constant expectation and gives almost-sure termination. The output is \(p\) or \(q\), and the complementary prime is \(N/d\).

This is only a guarantee **on the balanced, squarefree semiprime promise**. “Only” is a scope statement, not a proof that the procedure fails elsewhere. Nothing here supplies a success bound for primes, prime powers, repeated factors, unbalanced semiprimes, or arbitrary composites, nor a way to recognize the promise without factoring.

## 2. Meet-in-the-middle identity, resultants, and exact bit complexity

### Product identity

Split \([K]=A\mathbin{\dot\cup}B\), and set

\[
x_U=\sum_{i\in U}a_i\quad(U\subseteq A),\qquad
y_V=\sum_{i\in V}a_i\quad(V\subseteq B).
\]

Thus \(x_\varnothing=y_\varnothing=0\). Define

\[
F_A(X)=\prod_{U\subseteq A}(X+x_U),\qquad
Q_A=\prod_{\varnothing\ne U\subseteq A}x_U.
\]

Every \(S\subseteq[K]\) decomposes uniquely as \(S=U\mathbin{\dot\cup}V\). Separating \(V=\varnothing\) from \(V\ne\varnothing\) gives, over every commutative ring,

\[
\begin{aligned}
Q_K
&=\left(\prod_{\varnothing\ne U\subseteq A}x_U\right)
  \left(\prod_{\varnothing\ne V\subseteq B}
  \prod_{U\subseteq A}(x_U+y_V)\right)\\
&=\boxed{Q_A\prod_{\varnothing\ne V\subseteq B}F_A(y_V)}.
\end{aligned}
\]

No distinctness of half sums and no field hypothesis is used.

### Equivalent resultant and signs

Put

\[
G_B(X)=\prod_{\varnothing\ne V\subseteq B}(X+y_V),\quad
n=2^{|A|},\quad d=2^{|B|}-1,
\]

and

\[
P_B(X)=\prod_{\varnothing\ne V\subseteq B}(X-y_V)
=(-1)^dG_B(-X).
\]

With the convention fixed above,

\[
\operatorname{Res}(F_A(X),G_B(-X))
=\prod_{U\subseteq A}G_B(x_U)
=\prod_{U\subseteq A}\prod_{V\ne\varnothing}(x_U+y_V),
\]

while

\[
\operatorname{Res}(P_B(X),F_A(X))
=\prod_{V\ne\varnothing}F_A(y_V).
\]

Therefore the sign-safe forms are

\[
\boxed{
Q_K
=Q_A\operatorname{Res}(F_A(X),G_B(-X))
=Q_A\operatorname{Res}(P_B(X),F_A(X)).}
\]

If the first resultant's arguments are reversed, the leading coefficient of \(G_B(-X)\) matters:

\[
\boxed{
Q_K=(-1)^{nd}Q_A
\operatorname{Res}(G_B(-X),F_A(X)).}
\]

The sign is automatically \(+1\) when \(A\ne\varnothing\), since then \(n\) is even, but it must not be dropped for a possibly empty split. These are integer polynomial identities and remain valid after specialization to \(\mathbb Z/N\mathbb Z\); no root extraction in the composite ring is invoked.

### Balanced sizes

Choose

\[
|A|=\lceil K/2\rceil,\qquad |B|=\lfloor K/2\rfloor,
\]

and write

\[
D_A=2^{|A|},\quad D_B=2^{|B|},\quad
D=\max(D_A,D_B)=2^{\lceil K/2\rceil}.
\]

The floor calculation gave

\[
\frac{\sqrt N}{16}<T\le\frac{\sqrt N}{8}.
\]

Since \(\sqrt T\le D\le\sqrt{2T}\),

\[
\frac{N^{1/4}}4<D\le\frac{N^{1/4}}2.
\]

Thus \(D_A+D_B=\Theta(N^{1/4})\), with absolute constants.

### Exact multipoint algorithm over the composite ring

Let \(\ell=\lceil\log_2N\rceil\). Enumerate all \(x_U\) and \(y_V\) by binary-reflected Gray codes. Consecutive subsets differ in one element, so each new sum costs one modular addition or subtraction. This takes \(O((D_A+D_B)\ell)\) bit operations apart from logarithmic factors and stores \(O((D_A+D_B)\ell)\) bits.

Build \(F_A\) using a monic product tree for the factors \(X+x_U\). Independently build the point subproduct tree

\[
M_v(X)=\prod_{V\text{ below }v}(X-y_V)
\]

over all nonempty \(V\subseteq B\). Reduce \(F_A\) modulo the root polynomial, then descend the tree: at each child take the parent remainder modulo the child's monic \(M_v\). At a leaf \(M_v=X-y_V\), the constant remainder is \(F_A(y_V)\) in every commutative ring. Multiply all leaf values and \(Q_A\) modulo \(N\).

Repeated points cause no problem. This is evaluation, not interpolation: it never requires an inverse of \(y_V-y_W\), and the parent congruence remains valid modulo a child because the child polynomial divides the parent polynomial.

Polynomial division by a monic polynomial is valid and unique over an arbitrary commutative ring. For fast division, let \(f\) have degree \(s\ge d=\deg g\), and define

\[
f^\star=X^sf(X^{-1}),\qquad
g^\star=X^dg(X^{-1}).
\]

Because \(g\) is monic, \(g^\star(0)=1\). If \(e=s-d\), the reversed quotient satisfies

\[
q^\star\equiv f^\star(g^\star)^{-1}\pmod{X^{e+1}}.
\]

The truncated reciprocal exists over \(R\) because its constant term is the unit \(1\). Starting with \(H_1=1\), Newton doubling is

\[
H_{2t}=H_t(2-g^\star H_t)\pmod{X^{2t}}.
\]

This uses multiplication, addition, subtraction, and truncation only. It does not divide by \(2\), by a leading coefficient, or by any data-dependent residue. Reverse \(q^\star\), then form \(f-qg\) to obtain the remainder.

### Carry-safe Kronecker multiplication

All ring coefficients are stored by canonical lifts in \([0,N-1]\). Suppose two polynomials have \(s\) and \(t\) coefficients, and let \(\nu=\min(s,t)\). Set

\[
w=2\ell+\lceil\log_2\nu\rceil+1,\qquad B=2^w.
\]

Pack

\[
A_{\rm int}=\sum_i a_iB^i,\qquad
C_{\rm int}=\sum_j c_jB^j.
\]

Every unreduced convolution coefficient obeys

\[
0\le\sum_{i+j=k}a_ic_j
\le\nu(N-1)^2
<\nu2^{2\ell}<B.
\]

Thus ordinary integer multiplication \(A_{\rm int}C_{\rm int}\) has those convolution coefficients as its exact base-\(B\) digits; no carry overlaps adjacent coefficients. Masking \(w\)-bit blocks and reducing each block modulo \(N\) gives the exact product in \(R[X]\). Negative formal coefficients are first normalized modulo \(N\), so signed packing is unnecessary.

The packed operands and product use

\[
O((s+t)(\ell+\log(s+t)))
\]

bits. A standard uniform integer multiplication algorithm with bit time and workspace \(L^{1+o(1)}\) gives a balanced degree-\(j\) polynomial product in

\[
(j(\ell+\log j))^{1+o(1)}
\]

bit time and comparable temporary space. Packing, extraction, and coefficient reductions add only \(\widetilde O(j\ell)\).

### Tree accounting

At any level of a product tree with \(D_0\) leaves, the sum of node degrees is \(D_0\), and the number of stored coefficients is at most \(D_0\) plus the number of nodes, hence at most \(2D_0\). Across all \(O(\log D_0)\) levels, the tree stores

\[
O(D_0\log D_0)
\]

residues, or \(O(D_0\log D_0\,\ell)\) bits. At a fixed level, summing the Kronecker multiplication costs over geometrically equal node sizes is \(\widetilde O(D_0\ell)\); summing over all levels stays \(\widetilde O(D_0\ell)\).

The point subproduct tree has the same bounds. In the remainder tree, the sum of divisor degrees and remainder-length bounds at each level is \(O(D_A+D_B)\). Newton iterations at one division have geometrically increasing precision, so their cost is controlled, up to logarithmic factors, by the final precision. Summing over nodes and levels gives

\[
\widetilde O((D_A+D_B)\ell)
\]

bit time. Storing both product trees and all level remainders uses

\[
O((D_A+D_B)\log D\,\ell)
\]

bits, plus a largest packed-multiplication workspace of \((D\ell)^{1+o(1)}\) bits. Multiplying all evaluations and constructing \(Q_A\) requires \(O(D_A+D_B)\) modular multiplications and fits the same bound.

Since \(D=\Theta(N^{1/4})\) and powers of \(\log N\) are \(N^{o(1)}\), the evaluator is uniform and exact with

\[
\boxed{
N^{1/4+o(1)}\text{ bit time and }
N^{1/4+o(1)}\text{ bit space}.}
\]

The algorithm needs no factorization of \(N\). The only ring inverse used is the fixed unit \(1\) as the initial reciprocal coefficient. There is no Sylvester-matrix elimination, interpolation denominator, leading-coefficient inverse, or point-difference inverse hidden in the resultant language.

### Polynomial-space Gray-code evaluator

Alternatively enumerate all \(2^K\) subsets in Gray-code order. Maintain the current subset, its sum modulo \(N\), and a running product; after each nonempty subset, multiply its sum into the accumulator. This uses \(O(2^K)\) modular additions and multiplications. Since \(T=2^K=\Theta(\sqrt N)\), its bit time is

\[
\boxed{N^{1/2+o(1)}}.
\]

It stores the \(K\) inputs, a \(K\)-bit Gray-code state, one sum, one accumulator, and one modular-multiplication workspace. Since \(K=O(\log N)\), this is polynomial space in the input length.

## 3. Direction-weighted cube trees and the binary specialization

Let the undirected \(K\)-cube have vertex set \(\{0,1\}^K\), and give every edge changing coordinate \(i\) weight \(a_i\). Its weighted Laplacian is

\[
\mathcal L=\sum_{i=1}^Ka_i(I-\sigma_i),
\]

where \(\sigma_i\) toggles coordinate \(i\). For \(S\subseteq[K]\), the Walsh character

\[
\chi_S(x)=(-1)^{\sum_{i\in S}x_i}
\]

is an eigenvector. Direction \(i\) contributes eigenvalue \(0\) if \(i\notin S\) and \(2a_i\) if \(i\in S\), so

\[
\lambda_S=2\sum_{i\in S}a_i=2L_S.
\]

Only \(\lambda_\varnothing=0\). The weighted matrix-tree theorem for \(2^K\) vertices gives

\[
\begin{aligned}
\tau_K
&=\frac1{2^K}\prod_{S\ne\varnothing}\lambda_S\\
&=2^{-K}2^{2^K-1}Q_K\\
&=\boxed{2^{2^K-K-1}Q_K}.
\end{aligned}
\]

This is first an identity over \(\mathbb Q(a_1,\ldots,a_K)\), hence an integer polynomial identity valid under every specialization.

If \(a_i=u2^{i-1}\), then

\[
L_S=u\sum_{i\in S}2^{i-1}.
\]

As \(S\) ranges over the nonempty subsets, the binary integers on the right range bijectively over \(1,\ldots,2^K-1\). Therefore

\[
\boxed{Q_K=u^{2^K-1}(2^K-1)!.}
\]

## 4. Formal representation facts and their limits

### Boolean diagonal and minimal polynomial

Let

\[
F=\mathbb Q(a_1,\ldots,a_K)
\]

with algebraically independent \(a_i\), and let \(V\) have basis \(e_S\) indexed by every \(S\subseteq[K]\). The formal subset-sum diagonal operator

\[
D e_S=L_Se_S
\]

acts on a space of dimension \(2^K\). Its diagonal entries are pairwise distinct elements of \(F\), because \(L_S-L_U\) is a nonzero linear polynomial for \(S\ne U\). The minimal polynomial is therefore

\[
\boxed{
\mu_D(X)=\prod_{S\subseteq[K]}(X-L_S),\qquad
\deg\mu_D=2^K.}
\]

This is a formal rational-function-field statement. Numerical or modular specialization can make subset sums collide and lower the minimal-polynomial degree.

### Vanishing on subset hyperplanes

Let \(k\) be a characteristic-zero field and \(P\in k[a_1,\ldots,a_K]\). Interpret “\(P\) vanishes on \(L_S=0\)” either as identically vanishing on that affine hyperplane or pointwise vanishing on all its \(k\)-points. The interpretations agree because \(k\) is infinite.

Fix nonempty \(S\). Make an invertible linear coordinate change whose first coordinate is \(L_S\). Vanishing when that coordinate is zero says the constant coefficient of \(P\), viewed as a polynomial in \(L_S\), is zero. Thus \(L_S\mid P\).

The \(L_S\) for distinct nonempty \(S\) are nonassociate irreducible linear polynomials. Unique factorization implies

\[
\boxed{
\left(\forall S\ne\varnothing,\ P|_{L_S=0}=0\right)
\Longrightarrow Q_K\mid P.}
\]

The infinite characteristic-zero field and polynomial-identity quantifiers matter. Pointwise vanishing over a finite field alone would not imply divisibility.

For a nonzero such \(P\),

\[
\deg P\ge\deg Q_K=2^K-1.
\]

Each \(a_i\) occurs in exactly \(2^{K-1}\) factors, so

\[
\deg_{a_i}Q_K=2^{K-1}.
\]

If \(P=\det M(a)\) for a \(d\times d\) matrix whose entries have total degree at most \(\delta\), then

\[
2^K-1\le\deg P\le d\delta.
\]

Likewise, an entrywise bound \(\deg_{a_i}M_{uv}\le\delta_i\) gives \(2^{K-1}\le d\delta_i\). These conclusions require a nonzero determinant and the stated entry-degree bounds.

None of this lower-bounds arbitrary arithmetic circuits. Exponential polynomial degree does not force exponential circuit size; repeated squaring is the elementary obstruction to that inference. Nor does the minimal polynomial of this particular \(2^K\)-dimensional operator show that every representation of \(Q_K\), or every modular specialization algorithm, must have that dimension or state size. High-degree entries, alternative identities, specialization-induced collisions, and ring-specific algorithms lie outside the argument.

### Literal support

There are two natural literal-support readings, and both are exponential without implying a compressed-state lower bound.

First, let

\[
W_r=\#\{S\ne\varnothing:L_S\ne0\pmod r\}.
\]

Then

\[
\mathbb EW_r=m(1-1/r)=\Theta(2^K).
\]

Second, let \(D_r\) be the number of distinct residues among all \(T=2^K\) subset sums. For \(S\ne U\), \(L_S-L_U\) is a nonzero linear form, so

\[
\Pr(L_S=L_U)=1/r.
\]

Let \(C_r\) count colliding unordered pairs. Then

\[
\mathbb EC_r=\binom T2/r.
\]

If the distinct values have multiplicities \(c_j\), then

\[
C_r=\sum_j\binom{c_j}{2}
\ge\sum_j(c_j-1)=T-D_r.
\]

Since \(T/r<\sqrt2/8\),

\[
\mathbb ED_r
\ge T-\frac{T(T-1)}{2r}
>T-\frac{\sqrt2}{16}(T-1)
=\Theta(T).
\]

These counts concern explicit diagonal positions or explicit residue lists. They do not preclude a small implicit description or compressed-state evaluator.

## 5. Relation to P21 and exclusions

The connection to P21 is structural, not a reduction. P21 studies exact products with many torus-structured factors and limits its obstructions to fixed positive-binomial compression, literal recursion, and dense/materialized representations. Here \(Q_K\) is another highly structured, exponentially long product, now over Boolean subset-linear forms. In both cases the missing polylogarithmic evaluator is the substantive algorithmic question, and degree or literal-support observations do not answer it.

The present theorem proves a constant-probability promised factoring reduction conditional on a uniform exact polylogarithmic evaluator; exact \(N^{1/4+o(1)}\)-time/space and \(N^{1/2+o(1)}\)-time polynomial-space evaluators; and the cube-tree, specialization, and representation-specific identities above.

It does **not** prove a polynomial-time evaluator for \(Q_K\), a factoring algorithm for all inputs, an arithmetic-circuit lower bound, a lower bound against compressed modular state, or a theorem that every recursion must materialize exponentially many states. The split identity is an algebraic decomposition and an upper-bound algorithm, not a recursion lower bound. Optional Hurwitz provenance is irrelevant to the proofs and is not used.

## Adversarial checklist

- Floors: retained; \(T\ge4\) and \(\sqrt N/16<T\le\sqrt N/8\) justify both strict constants.
- Pairwise-independence characteristic: no exception; distinct \(0/1\) supports are not scalar multiples.
- XOR inequality: uses the second-moment lower bound, the union-bound upper bound, and genuine CRT independence.
- OR scope: exact modulo each prime field; false if misread as a global OR modulo \(N\).
- Resultant signs: fixed by convention; reversed order carries \((-1)^{nd}\).
- Composite-ring division: every divisor is monic; reverse reciprocals have constant term \(1\); repeated points are allowed; no interpolation occurs.
- Packing: base \(2^w\) strictly exceeds every unreduced convolution coefficient.
- Tree bounds: \(O(D\log D)\) stored residues and \(\widetilde O(D\ell)\) bit time, with \(D=\Theta(N^{1/4})\).
- Matrix-tree exponent: \(2^K-1\) nonzero eigenvalues contribute powers of \(2\), followed by division by \(2^K\), giving \(2^K-K-1\).
- Formal quantifiers: minimal polynomial is over \(\mathbb Q(a)\); hyperplane divisibility is over an infinite characteristic-zero field; determinant consequences require a nonzero determinant and bounded entry degrees.
- Exclusions: no all-input result, polynomial evaluator, arbitrary-circuit lower bound, compressed-state lower bound, or recursion theorem follows.

## Final status

**RECONSTRUCTED.** No mathematical correction is needed under the explicit meanings above. “Local OR” must remain componentwise, and the formal-vanishing and resultant conventions must be retained; stronger readings would be false.

**Independent verifier backing:** YES for the proof-blind reconstruction requested here. This report independently derives every substantive claim from the statement. Under the protocol, the theorem has full verifier-backed status only if the separate hostile audit passed this same mathematical version; that separate audit is not certified by this report itself.
