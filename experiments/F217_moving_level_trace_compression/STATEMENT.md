# F217 candidate — moving-level trace compression and exact ring-coefficient targets

## Status

This is a frozen, self-audited, proof-only candidate for the balanced
beta-two branch. It proves conditional factor-extraction interfaces and
sharp boundaries for named explicit models. It does not construct the
missing coefficient evaluator. It is not an unconditional factoring
algorithm and is not a lower bound against arbitrary compressed
algorithms.

## Setup and cost convention

Assume

\[
N=pq,\qquad p<q<2p,\qquad N\equiv3\pmod4,
\]

where \(p,q\) are distinct odd primes. Put

\[
K=\frac{N-1}{2},\qquad
G=(\mathbb Z/K\mathbb Z)^\times,
\]

and let \(n=\lfloor\log _2N\rfloor+1\). The complete prime
factorization of \(K\) is granted.

All complexity bounds include every operation performed at the current
node, all oracle queries, all requested precision, all character and
coordinate encodings, all state retained by the decoder, and all output
bits. Quasipolynomial, abbreviated QP, always means QP in \(n\).

For a character \(\chi:G\to\mathbb C^\times\), define its divisor
coefficient

\[
D_N(\chi)=\sum_{d\mid N}\chi(d).
\]

Every divisor of \(N\) is a unit modulo \(K\), so this is well-defined.

## Theorem A — at most \(2r-1\) traces align the inversion orbit

Assume, in addition to \(\operatorname{factor}(K)\), all of the following
explicit premises.

1. A certified cyclic decomposition

   \[
   \iota:\prod_{i=1}^{r}C_{m_i}\xrightarrow{\sim}G,
   \qquad m_i\ge2,
   \]

   is supplied. Its forward and inverse coordinate maps run in QP time.
2. The associated coordinate characters

   \[
   \chi_i\!\left(\iota(a_1,\ldots,a_r)\right)
   =\exp(2\pi i a_i/m_i)
   \]

   and their pairwise products have succinct QP-size encodings.
3. A certified evaluator returns \(D_N(\chi)\), for each adaptively
   requested character in the bank below, with absolute error at most

   \[
   \epsilon=2^{-4n-20},
   \]

   in QP time and QP total state.

Then the unordered factor pair \(\{p,q\}\) is recovered in QP time using
at most

\[
\boxed{2r-1\le2n-1}
\]

coefficient evaluations.

The bank consists of the \(r\) coordinate characters and, after choosing
one active coordinate \(i_0\), at most \(r-1\) products
\(\chi_{i_0}\chi_i\). A coordinate is active when its hidden coordinate
is not self-inverse.

This theorem does not assert that \(\operatorname{factor}(K)\) supplies
the cyclic decomposition, its inverse coordinate map, a discrete-log
algorithm, succinct high-order character evaluation, or the divisor
coefficient evaluator. Each of those items is a separate premise or a
charged cost.

## Theorem B — the tautological ring character is exactly the additive target

In the integral group algebra \(\mathbb Z[G]\), put

\[
\mathcal A_N=\sum_{d\mid N}[d\bmod K].
\]

Let

\[
\Theta_K:\mathbb Z[G]\longrightarrow\mathbb Z/K\mathbb Z,
\qquad
\Theta_K([a])=a\bmod K,
\]

be the ring map induced by the tautological group character
\(a\mapsto a\). Then

\[
\boxed{
\mathcal A_N=2[1]+[p]+[p^{-1}],
\qquad
\Theta_K(\mathcal A_N)
\equiv2+p+q\pmod K.}
\]

Except for \(N=15\), the least residue

\[
s=\bigl(\Theta_K(\mathcal A_N)-2\bigr)\bmod K
\]

is the integer \(p+q\). The roots of

\[
X^2-sX+N
\]

are therefore \(p,q\). The exceptional input \(N=15=3\cdot5\) is
recognized by trial division by \(3\).

Thus one exact \(O(n)\)-bit residue evaluator for
\(\Theta_K(\mathcal A_N)=\sigma_1(N)\bmod K\) is a factor transition.
The theorem identifies that evaluator; it does not construct it.

## Theorem C — a high-weight level-one Eisenstein coefficient has the same residue

Because \(K\) is odd and \(K>1\), set

\[
k=\varphi(K)+2.
\]

Then \(k\ge4\) is even. Define the arithmetic normalization of the
level-one Eisenstein series by

\[
\mathcal G_k(\tau)
=-\frac{B_k}{2k}
+\sum_{m\ge1}\sigma_{k-1}(m)q^m,
\qquad q=e^{2\pi i\tau}.
\]

Equivalently,

\[
\mathcal G_k=-\frac{B_k}{2k}E_k,
\qquad
E_k=1-\frac{2k}{B_k}
\sum_{m\ge1}\sigma_{k-1}(m)q^m.
\]

Its nonconstant coefficients are integers, even though its constant term
need not be integral. The moving-weight target satisfies

\[
\boxed{
[q^N]\mathcal G_k
=\sigma_{k-1}(N)
\equiv\sigma_1(N)
\equiv2+p+q\pmod K.}
\]

Consequently, a QP evaluator that returns this coefficient directly
modulo \(K\), with all same-node work charged, factors \(N\) by Theorem B.

The requested output is only one \(O(n)\)-bit residue. This must not be
confused with standard numeric state or unrestricted exact output:

1. \(\varphi(K)\ge\sqrt K=2^{\Omega(n)}\), so the numeric weight and
   the dimension of a dense level-one weight-\(k\) modular-form space are
   exponential in \(n\).
2. The exact integer \(\sigma_{k-1}(N)\) has
   \(\Theta(kn)=2^{\Omega(n)}\) bits.
3. The binary encoding of \(k\) itself has only \(O(n)\) bits.

This is a boundary for standard dense weight-based methods, not a lower
bound against a random-access modular-residue evaluator.

## Theorem D — prime-\(K\) eta quotient identity

Assume additionally that \(K=r\) is prime. In the present semiprime
setup, \(r\ge7\). Define

\[
P(q)=\prod_{a\ge1}(1-q^a),
\qquad
F_r(q)=\frac{P(q)^r}{P(q^r)}
=\frac{\eta(\tau)^r}{\eta(r\tau)}.
\]

For prime \(r>3\), \(F_r\) is a holomorphic eta-quotient modular form of
weight

\[
w=\frac{r-1}{2}
\]

on \(\Gamma_0(r)\), with quadratic eta-quotient character

\[
\chi_r(d)=
\left(\frac{(-1)^w r}{d}\right)
\]

in Kronecker-symbol notation. It is holomorphic at both cusps; its order
at infinity is zero, and its Fricke transform has positive order
\((r^2-1)/24\).

Coefficientwise in \(\mathbb Z[[q]]/r^2\mathbb Z[[q]]\),

\[
F_r(q)\equiv
1-r\sum_{a\ge1}\sum_{j=1}^{r-1}\sum_{h\ge0}
j^{-1}q^{a(j+hr)}
\pmod{r^2},
\]

where \(j^{-1}\) is taken modulo \(r\). Hence, for \(r\nmid m\),

\[
\boxed{
-\frac{[q^m]F_r}{r}
\equiv m^{-1}\sigma_1(m)\pmod r.}
\]

The coefficient \([q^m]F_r\) is divisible by \(r\), and its residue
modulo \(r^2\) determines the displayed quotient modulo \(r\). At
\(m=N=2r+1\),

\[
\boxed{
-\frac{[q^N]F_r}{r}
\equiv\sigma_1(N)
\equiv2+p+q\pmod r.}
\]

Thus one \(O(n)\)-bit coefficient residue modulo \(r^2\) factors every
input in this prime-\(K\) subfamily, with \(N=15\) again handled by trial
division.

The exact logarithmic derivative is

\[
\boxed{
-\frac1r q\frac d{dq}\log F_r(q)
=L(q)-L(q^r),\qquad
L(q)=\sum_{m\ge1}\sigma_1(m)q^m.}
\]

Therefore the eta quotient is an exact modular packaging of the original
Lambert-series target. Standard truncation to \(q^N\) retains
\(\Theta(N)\) coefficient positions, and standard dense modular-form
state has numeric weight and level of size \(2^{\Omega(n)}\). The theorem
does not provide a QP random-access coefficient algorithm.

## Theorem E — twisted Ramanujan expansion and its exact first sensitive term

Let \(\chi\) be a Dirichlet character modulo \(K\), and for
\(\Re(s)>0\) put

\[
A_{\chi,s}(n)=\sum_{d\mid n}\chi(d)d^{-s}.
\]

With

\[
c_m(n)=\sum_{e\mid(m,n)}e\,\mu(m/e),
\]

one has the absolutely convergent identity

\[
\boxed{
A_{\chi,s}(n)
=L(s+1,\chi)
\sum_{m\ge1}\frac{\chi(m)c_m(n)}{m^{s+1}}.}
\]

After subtracting the public \(n=1\) baseline,

\[
A_{\chi,s}(N)-1
=L(s+1,\chi)
\sum_{m\ge1}
\frac{\chi(m)(c_m(N)-\mu(m))}{m^{s+1}}.
\]

For every \(m<p\), the summand is zero. At \(m=p\), it is nonzero before
the common prefactor and equals

\[
\frac{\chi(p)\,p}{p^{s+1}}=\chi(p)p^{-s}.
\]

Thus the first factor-sensitive multiplier in this explicit Ramanujan
channel is exactly the smaller factor \(p\). Direct termwise summation
therefore takes \(p=2^{\Omega(n)}\) positions on balanced inputs.

For a nonprincipal \(\chi\), the unweighted trace at \(s=0\) is the
limit of the finite left side as \(s\downarrow0\); the right side at the
boundary is understood only by this Abel limit or analytic continuation.
No ordinary-convergence assertion at \(s=0\) is made. The theorem is not
a lower bound against compressed tail summation or an arbitrary
weight-one coefficient evaluator.

## Named-model boundary and remaining scope

The following exact observations delimit, but do not close, the surviving
problem.

1. At good index \((N,K)=1\), direct upper-triangular representatives for
   the Hecke correspondence \(T_N\) are indexed by

   \[
   ad=N,\qquad 0\le b<d,
   \]

   and number \(\sum_{d\mid N}d=\sigma_1(N)\). Direct materialization is
   numeric-exponential and its divisor labels already include \(p,q\).
   A compressed Hecke evaluator remains open.
2. The level-\(K\) diamond operator is trivial:
   \(\langle N\rangle=\langle1\rangle\), because \(N\equiv1\pmod K\).
   It is not the Hecke operator \(T_N\).
3. Standard Manin-symbol state at moving level \(K\), and standard
   symmetric-power state at moving weight \(k\), are numeric-exponential.
   This says nothing about a compressed state not materialized by those
   models.
4. For every representation \(\rho\) of the abelian group \(G\),

   \[
   \sum_{d\mid N}\rho(d)
   =2I+\rho(p)+\rho(p)^{-1}.
   \]

   Over a characteristic-zero splitting field, finite-dimensional
   semisimple representations of \(G\) decompose into characters.
   Inducing or packaging such characters into matrices does not itself
   evaluate the missing divisor coefficient. Representations not
   factoring through \(G\) are outside this statement.
5. Since \((K,N)=1\),

   \[
   (Km,N)=(m,N).
   \]

   Hence inserting the moving level into an explicit formula whose only
   factor-sensitive arithmetic input is this gcd does not move the first
   noncoprime multiplier below \(p\). Other formula terms can carry more
   information and are not covered.
6. Recursively factoring \(K\) is not rejected for lack of a fixed-ratio
   contraction. A single chain satisfying

   \[
   T(n)\le T(n-1)+\operatorname{QP}(n)
   \]

   remains QP. Fixed-ratio contraction or another branching bound becomes
   necessary only when many recursive children survive. F217 grants
   \(\operatorname{factor}(K)\) and makes no claim that the recursive
   step itself is unavailable.

The core unresolved object is therefore one compressed exact evaluator
for a divisor sum: a small separating bank of scalar traces, the
tautological ring residue, the Eisenstein residue, or the prime-level eta
coefficient residue. F217 proves equivalences and conditional decoders. It
does not solve that evaluator problem and does not rule out modular
symbols, trace formulas, nonholomorphic methods, compressed products,
nonabelian extensions, or characteristic-specific ring circuits.
