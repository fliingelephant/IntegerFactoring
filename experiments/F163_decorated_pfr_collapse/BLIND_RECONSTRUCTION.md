# F163 blind reconstruction

## Verdict

**PASS**, with the scope qualifications in the final section. I found no
mathematical counterexample to the graph theorem, the sumset claims, either
doubling example, or the factor-assisted completion construction.

This reconstruction used only `STATEMENT.md`, whose SHA-256 was verified as

```text
82ff2a0fef918e3c4e992ca70b334656fcd661146e4b61dac7c871c0216dbd95
```

## 1. Reconstructing the extension

The product referred to in the statement must be the standard
carry-corrected product. Write

\[
Q(v)=\prod_i q_i^{v_i},\qquad
c(v,w)=\prod_i q_i^{v_iw_i}.
\]

For roots represented modulo \(N\), it is

\[
(v,z)+(w,y)=
\left(v+w,\;zyc(v,w)^{-1}\right),
\tag{R1}
\]

where vector addition is over \(\mathbb F_2\). Indeed,

\[
Q(v)Q(w)=Q(v+w)c(v,w)^2,
\]

so the second coordinate in (R1) squares to \(Q(v+w)\). The bit-carry
identity makes this product associative. It is commutative, and

\[
(v,z)+(v,z)=(0,z^2Q(v)^{-1})=(0,1).
\]

Thus \(E_Q(N)\) is an elementary abelian 2-group. Its parity image
\(V_Q(N)\) is a binary vector space. The parity-zero fiber is \(R_N\).
Quotienting the global-sign subgroup
\(\Delta=\{(0,1),(0,-1)\}\) gives

\[
0\longrightarrow R_N/\Delta
\longrightarrow E_Q(N)/\Delta
\overset{\pi}{\longrightarrow}V_Q(N)
\longrightarrow0.
\]

This proves (1), under the referenced product. Rational square-class
independence is not needed for this short exact-sequence argument; it is
relevant to the intended block interpretation.

## 2. Kernel detection and the public graph

Process the explicit generators in \(A\) by binary elimination on their
parity vectors. Retain the decorated lift attached to each parity pivot.
When a new parity vector reduces to zero, applying the same row operations to
its decorated lift produces an element \([(0,r)]\in K\).

If this class is nonzero, then \(r^2\equiv1\pmod N\) and
\(r\not\equiv\pm1\pmod N\). For odd \(N\), roots of one on each odd
prime-power component are signs. A nonglobal choice of signs therefore gives
a proper nontrivial divisor through \(\gcd(r-1,N)\) (equivalently one can
also use \(\gcd(r+1,N)\)). Hence the first branch really factors \(N\).

The zero-parity reductions generated during elimination span the full kernel
of \(\pi|_H\). Therefore, if every such reduction is the zero class in
\(K\), then

\[
H\cap K=0.
\]

Now \(\pi|_H\) is injective, and it is onto \(W=\pi(H)\) by definition.
It is consequently an isomorphism. Its inverse is public: express
\(w\in W\) in the retained parity basis and apply the same coefficients to
the retained decorated lifts. Injectivity proves that the result is
independent of the expression. This constructs

\[
h=(\pi|_H)^{-1}:W\to H
\]

before any PFR step. In particular,

\[
H=\{h(w):w\in W\},
\]

so the claimed graph description is exact.

## 3. Sumsets and additive structure

Because \(\pi|_H\) is an isomorphism and \(A\subseteq H\), for every
\(k\geq1\),

\[
\pi(kA)=k\pi(A).
\]

Surjectivity onto the right side follows by lifting each summand. Injectivity
follows from injectivity on all of \(H\). This proves the bijection and
cardinality equality in (4).

The same argument handles arbitrary additive words. Two decorated words are
equal exactly when their parity words are equal. Thus every quantity defined
only from additive equations and equality patterns is preserved. This
includes Freiman relations of every fixed order, additive energy, intrinsic
affine-subspace containment, and intrinsic coset or subspace covers.

An ambient affine coset \(x+L\) intersects \(H\), if at all, in an affine
coset of \(L\cap H\). Hence an ambient cover of \(A\) can be intersected
with \(H\) without increasing its number of cells, and the resulting cover
can then be transported through \(\pi|_H\). No conclusion follows about
ambient kernel directions outside \(H\), exactly as the statement says.

It follows that a *purely additive and isomorphism-invariant* PFR conclusion
for \(A\) has an equivalent conclusion for \(\pi(A)\), and conversely via
the already computed \(h\). Small doubling is not used to build this
inverse. The preliminary elimination either exposes a nonglobal kernel root,
or all subsequent intrinsic additive structure is already the public lift of
parity structure.

## 4. Large-doubling example

Since \(h\) is linear, it is enough to count in \(W=\mathbb F_2^d\). For

\[
C_1=\{0,e_1,\ldots,e_d\},
\]

the distinct pair sums have weights zero, one, or two. They are

\[
0,\quad e_i,\quad e_i+e_j\ (i<j).
\]

Therefore

\[
|B_1+B_1|=1+d+\binom d2,
\]

and

\[
\frac{|B_1+B_1|}{|B_1|}
=\frac d2+\frac1{d+1}\sim\frac d2.
\]

The set already contains a basis, so \(\langle B_1\rangle=h(W)\). Also,
if \(h(w)\in K\), its parity is both \(w\) and zero; hence \(w=0\).
Thus \(h(W)\cap K=0\).

For Hamming balls, one inclusion in (6) follows from
\(\operatorname{wt}(x+y)\leq\operatorname{wt}(x)+
\operatorname{wt}(y)\). Conversely, any support of size at most \(s+t\)
can be partitioned into a part of size at most \(s\) and one of size at most
\(t\). Hence

\[
B_s+B_t=B_{\min(s+t,d)}.
\]

Starting with \(B_1\), repeated doubling strictly increases the ball until
it reaches all \(2^d\) elements of \(h(W)\), although its generated subgroup
was all of \(h(W)\) from the start. With input size \(|B_1|=d+1\), explicitly
listing the terminal sumset costs \(2^d\), which exceeds every standard
quasipolynomial bound in \(|B_1|\). A basis representation instead consists
of the same lifted parity basis that already specifies \(h\). This verifies
the claimed separation between cardinality growth and subgroup or kernel
growth.

## 5. Doubling-one example

For a subspace \(U\leq W\), linearity gives

\[
h(U)+h(U)=h(U+U)=h(U).
\]

For \(u\notin U\), the affine coset \(h(u+U)=h(u)+h(U)\) omits the identity,
and characteristic two gives

\[
(h(u)+h(U))+(h(u)+h(U))=h(U).
\]

The two sets have the same cardinality. Thus both the subgroup and
identity-free affine versions have doubling one while staying wholly inside
the same kernel-free graph.

## 6. Factor-assisted completion realization

Put \(M=2^d-1\). Choose the stated primes \(p,q\), and primitive roots
\(a_p,a_q\). Each CRT class \(c_j\) in (8) is coprime to \(N=pq\).
Dirichlet's theorem therefore gives infinitely many rational primes in each
class, so the \(\ell_j\) can be chosen distinct. Distinct rational primes are
pairwise coprime, are units modulo \(N\), and have independent nonsquare
classes in \(\mathbb Q^*/\mathbb Q^{*2}\).

The CRT element \(z_j\) satisfies

\[
z_j^2\equiv a_p^{2^{j+1}}\equiv\ell_j\pmod p,
\qquad
z_j^2\equiv a_q^{2^{j+1}}\equiv\ell_j\pmod q.
\]

Thus \(z_j^2\equiv\ell_j\pmod N\). The lifts \((e_j,z_j)\) have independent
parity projections. Their span has trivial intersection with \(K\), and the
map obtained by summing these basis lifts is a section
\(h:\mathbb F_2^d\to\overline E\).

For \(v\), choose a representative root \(z_v\) of \(h(v)\), and let
\(s_v\) be its least positive modular inverse. Then

\[
s_vz_v\equiv1\pmod N,
\qquad
z_v^2\equiv Q(v)=\prod_j\ell_j^{v_j}\pmod N.
\]

Consequently the positive integer in (10) obeys

\[
T_v=s_v^2Q(v)\equiv s_v^2z_v^2\equiv1=\alpha_v^2\pmod N.
\]

Its normalized decorated root is
\(\alpha_vs_v^{-1}\equiv z_v\pmod N\), so its decorated lift is exactly
\(h(v)\). Any binary dependency among these records has parity sum zero.
Linearity of \(h\) then puts its normalized root in \(\Delta\), so every
such dependency is global.

It remains to check that the individual endpoints do not already factor
\(N\). For nonzero \(v\), set

\[
k=\sum_jv_j2^j,
\qquad 1\leq k\leq M.
\]

Modulo either hidden prime \(r\in\{p,q\}\),

\[
Q(v)\equiv a_r^{2k}.
\]

The order of \(a_r\) is \(r-1>4M\), while
\(0<2k\leq2M<(r-1)/2\). Hence this power is neither \(1\) nor \(-1\).
It follows that \(Q(v)-1\) and \(Q(v)+1\) are units modulo both \(p\) and
\(q\).

Finally, multiplication by the unit \(s_v\) gives the congruences

\[
z_v-s_v\equiv s_v(z_v^2-1)\equiv s_v(Q(v)-1)\pmod N,
\]

\[
z_v+s_v\equiv s_v(z_v^2+1)\equiv s_v(Q(v)+1)\pmod N.
\]

Therefore both gcd equalities in (11) hold, and all four gcds equal one.
Selecting the records indexed by \(0,e_1,\ldots,e_d\), by a Hamming ball,
by a linear subspace, or by an affine subspace reproduces exactly the sets
in Sections 4 and 5. The construction explicitly uses the hidden factors to
choose the simultaneous primitive-root residues and their roots. It proves
existence, not a factor-free source algorithm.

## 7. Remaining-hypothesis and scope audit

If two public sections have a public common parity vector \(u\) with
\(h_1(u)\ne h_2(u)\), then

\[
h_1(u)-h_2(u)\in K\setminus\{0\}.
\]

The kernel argument in Section 2 converts this disagreement into a
nontrivial factor. Thus (12) is a sufficient extra arithmetic target.
Likewise, a theorem that forces a strictly decreasing, quasipolynomially
bounded integer-state capacity would be extra progress by hypothesis; it is
not supplied by the additive isomorphism itself.

The exact limitations are:

1. The statement invokes the P138 product and the meanings of
   \(V_Q(N)\), decorated lift, canonical inverse, and P142 completion rather
   than defining all of them. The reconstruction above uses the unique
   standard carry-corrected product (R1) compatible with the displayed
   formulas. The historical attributions to P108, P138, P142, P143, P146,
   and P148 cannot be independently verified from this statement alone.
2. “Every Freiman-relation statistic” is correct for statistics intrinsic to
   the additive group and invariant under isomorphism. It is not a claim
   about encoding-dependent behavior of an arbitrary software routine.
   Similarly, the two-outcome PFR language is valid as a structural claim,
   not as a literal restriction on every possible program's control flow.
3. “Exceed a quasipolynomial budget” needs a size parameter. Taking the
   natural parameter to be the explicit input size \(|B_1|=d+1\) makes the
   claim precise and true because the terminal set has size \(2^d\).
4. The proof transports only the additive object inside \(H\). Exact integer
   representatives, carries, sizes, incidences, and provenance are not
   invariants of \(\pi|_H\). The stated non-claims about richer sources and
   incompatible lifts are therefore necessary and correct.

These are scope qualifications, not counterexamples to the stated pure
decorated-group obstruction.
