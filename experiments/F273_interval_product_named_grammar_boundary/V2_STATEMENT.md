# F273 V2 — corrected named-grammar boundary for the interval-product seam

## Status and correction history

This is an additive corrected proof-only candidate with an author
self-audit. Every V1 file and both V1 audits remain byte-for-byte
unchanged.

The V1 hostile audit passed and is preserved at HOSTILE_AUDIT.md, SHA-256

a8ff865f43d29e5af1c8956bd2c1bcb65fbf53f97339da024db4e8f2a35e0cb6.

The strict V1 statement-only reconstruction failed and is preserved at
BLIND_RECONSTRUCTION.md, SHA-256

9bc7775fd05ec20c9f78923043857504a5795fef03966893d16535ae7a50cda9.

It found two exactness defects outside the core boxed identities:

1. for \(\operatorname{diag}(1,\ldots,B)\), the last determinantal
   divisor is \(B!\), but the last Smith invariant is
   \(\operatorname{lcm}(1,\ldots,B)\);
2. \(2^{t+1}-1\) counts the base frontier of one cross-resultant
   expansion, while the full memoized DAG has
   \(2^{t+2}-t-3\) cross-resultant states.

V2 repairs both distinctions and all dependent prose and resource counts.
No V2 hostile audit, V2 statement-only reconstruction, outside-family
audit, human audit, or research computation has run.

## Scope

The packet studies four named attempts to compress a consecutive interval
product:

1. division-free polynomial combinations of two child product states;
2. Smith determinantal divisors for one local rank defect;
3. the full derivative resultant, or discriminant, of a rising factorial;
4. literal dyadic recursion for cross-resultants of separated blocks.

The conclusions are exact only under the hypotheses stated below. They do
not give a lower bound for general arithmetic circuits, algebraic circuits
with special affine identities, modular interval-product evaluators,
succinct matrices, nonlinear Archimedean operations, adaptive algorithms,
or integer factoring.

The practical conclusion is narrow. Enlarging F263 by more
division-free child-state polynomials or full rising-factorial resultants
does not yet justify a new C++ search. A literal Smith calculation reaches
a factor-bearing last invariant, but V2 does not identify that invariant
with the factorial or provide its evaluator. The named grammars either
retain an original child product, reach a direct but unevaluated
factor-bearing product or lcm gate, or have an exponential literal
dependency closure.

A future search is materially new only after it supplies a finite
transition whose coefficients are independently evaluable in numerical
quasipolynomial time and whose semantics lie outside these hypotheses.

## 1. Child-product coordinate ring

Let \(A\) be an integral domain of public symbolic descriptors, and let

\[
 R=A[e_0,o_0,z_1,\ldots,z_r]
\tag{1}
\]

be a polynomial ring. The variables \(e_0,o_0\) denote the zero-th product
coordinates of two children. The variables \(z_i\) denote every other
child coordinate, such as fixed-order jets or transfer entries. In this
theorem they are algebraically independent. This independence hypothesis
is essential.

### Theorem 1 — child-zero ideal

For \(F\in R\):

\[
 F(0,o_0,z)=0
 \quad\Longrightarrow\quad
 e_0\mid F.
\tag{2}
\]

If both child orientations vanish identically,

\[
 F(0,o_0,z)=F(e_0,0,z)=0,
\tag{3}
\]

then

\[
 \boxed{e_0o_0\mid F.}
\tag{4}
\]

The same numerator conclusion holds for a rational observable \(F=G/H\)
when \(H\) is defined and nonzero on both generic child axes. A denominator
containing \(e_0\) or \(o_0\) is not total at the corresponding singular
orientation and is outside this statement.

Thus an exact characteristic-zero polynomial that vanishes for the left
orientation contains \(e_0\). An orientation-blind polynomial guaranteed
to vanish for either orientation contains \(e_0o_0\), the parent product
coordinate.

This is an algebraic divisibility statement. It does not prove that every
arithmetic circuit must separately materialize either factor, and it does
not apply when the other state coordinates satisfy special affine,
characteristic-dependent, or row-specific identities.

### Corollary 1.1 — formal short-block dependency

Let \(y_0,\ldots,y_{M-1}\) be algebraically independent leaves. Suppose
each available base summary depends on at most \(q_0\) leaves, and an exact
arithmetic expression obtains leaf dependence only through \(K\) such
summaries. If the expression equals

\[
 \prod_{j=0}^{M-1}y_j,
\tag{5}
\]

then

\[
 \boxed{Kq_0\geq M.}
\tag{6}
\]

This includes a literal fixed-order jet merge: its zero-th coordinate is
the product in (5). It is a formal independent-leaf statement, not a lower
bound after the specialization \(y_j=x+j\). An affine-specific identity
can lie outside it.

## 2. Smith determinantal divisors and invariant factors

Let \(N=pq\), where \(p\ne q\) are primes. Let \(M\) be an
\(m\times m\) integer matrix. For \(1\leq k\leq m\), let
\(\Delta_k(M)\) be the nonnegative gcd of all integer \(k\times k\)
minors, with zero minors included harmlessly. Put \(\Delta_0(M)=1\), and
let

\[
 d_k(M)=\frac{\Delta_k(M)}{\Delta_{k-1}(M)}
\tag{7}
\]

be the ordinary integer Smith invariant factors.

### Theorem 2 — one local rank defect reaches only the last invariant

Assume

\[
 \operatorname{rank}_{\mathbb F_p}(M\bmod p)=m-1,
 \qquad
 \operatorname{rank}_{\mathbb F_q}(M\bmod q)=m.
\tag{8}
\]

Then

\[
 \boxed{
 \gcd(\Delta_k(M),N)=
 \begin{cases}
 1,&0\leq k<m,\\
 p,&k=m.
 \end{cases}}
\tag{9}
\]

Consequently, the guaranteed \(p\)-support first appears in the last Smith
invariant and

\[
 \boxed{\gcd(d_m(M),N)=p.}
\tag{10}
\]

For a balanced distinct semiprime

\[
 N=pq,\qquad p<q<2p,\qquad B=\lfloor\sqrt N\rfloor,
\tag{11}
\]

the diagonal factor matrix

\[
 A_B=\operatorname{diag}(1,2,\ldots,B)
\tag{12}
\]

has exactly this rank profile: the interval contains exactly one multiple
of \(p\) and no multiple of \(q\). Its last determinantal divisor and last
Smith invariant are different:

\[
 \boxed{\Delta_B(A_B)=B!,}
\tag{13}
\]

\[
 \boxed{
 \Delta_{B-1}(A_B)
 =\frac{B!}{\operatorname{lcm}(1,\ldots,B)},}
\tag{14}
\]

\[
 \boxed{
 d_B(A_B)=\operatorname{lcm}(1,\ldots,B).}
\tag{15}
\]

Both displayed terminal values are factor-bearing:

\[
 \boxed{
 \gcd(\Delta_B(A_B),N)
 =\gcd(d_B(A_B),N)=p.}
\tag{16}
\]

The determinantal divisor \(\Delta_B\) is the F197 factorial gate. The
last Smith invariant \(d_B\) is instead an lcm gate. F273 V2 proves no
reduction between evaluating these two residues and no
numerical-quasipolynomial evaluator for either.

The theorem does not cover a matrix with local nullity larger than one, a
different structured matrix, or a new algorithm that computes the last
invariant of an exponentially large succinct matrix.

## 3. Full derivative resultant

For \(m\geq1\), define

\[
 P_m(X)=\prod_{j=1}^{m}(X+j)
\tag{17}
\]

and let

\[
 D_m=\left|\operatorname{Res}(P_m,P_m')\right|
\tag{18}
\]

be its unsigned discriminant.

### Theorem 3 — the discriminant is a superfactorial gate

One has

\[
 \boxed{
 D_m
 =\prod_{d=1}^{m-1}d^{\,2(m-d)}
 =\left(\prod_{k=1}^{m-1}k!\right)^2.}
\tag{19}
\]

The adjacent ratio is

\[
 \boxed{\frac{D_{m+1}}{D_m}=(m!)^2.}
\tag{20}
\]

Moreover,

\[
 \operatorname{bitlen}(D_m)=\Theta(m^2\log(m+1)).
\tag{21}
\]

On the balanced promise (11), first compute \(\gcd(B,N)\). If it is
proper, the input is already factored. On the unresolved branch \(B>p\),
and

\[
 \boxed{\gcd(D_B,N)=p.}
\tag{22}
\]

Thus the full derivative resultant is a valid factor-bearing scalar, but
its exact formula is a weighted interval product. Equation (22) does not
provide a numerical-quasipolynomial evaluator for that scalar.

## 4. Literal cross-resultant closure

For integers \(a\geq0\) and \(m\geq1\), put

\[
 P_{a,m}(X)=\prod_{j=0}^{m-1}(X+a+j).
\tag{23}
\]

For \(c\geq1\), define the positive adjacent-scale cross-resultant

\[
 R_c(m)
 =\operatorname{Res}\!\left(P_{0,m},P_{cm,m}\right)
 =\prod_{i=0}^{m-1}\prod_{j=0}^{m-1}(cm+j-i).
\tag{24}
\]

### Theorem 4 — dyadic offsets expand or telescope to a weighted gate

For all \(c,m\geq1\),

\[
 \boxed{
 R_c(2m)
 =R_{2c-1}(m)R_{2c}(m)^2R_{2c+1}(m).}
\tag{25}
\]

Start with \(R_1(2^tq_0)\). After exactly \(s\) recursive expansions of
(25), the level-\(s\) frontier contains precisely

\[
 C_s=\{1,\ldots,2^{s+1}-1\},
\qquad 0\leq s\leq t.
\tag{26}
\]

Therefore the base frontier has exactly

\[
 \boxed{|C_t|=2^{t+1}-1}
\tag{27}
\]

distinct offsets. The complete memoized DAG, keyed by both length and
offset, has exactly

\[
 \boxed{
 \sum_{s=0}^{t}(2^{s+1}-1)
 =2^{t+2}-t-3}
\tag{28}
\]

cross-resultant states. Both counts are \(\Theta(2^t)\).

The same values have an exact telescoped description. Define

\[
 S(k)=\prod_{r=1}^{k-1}r!,
 \qquad S(0)=S(1)=1.
\tag{29}
\]

Then

\[
 \boxed{
 R_c(m)
 =\frac{S((c+1)m)S((c-1)m)}{S(cm)^2},}
\tag{30}
\]

\[
 \boxed{D_m=S(m)^2,\qquad \frac{S(m+1)}{S(m)}=m!.}
\tag{31}
\]

The quotient in (30) is an exact integer identity. It does not authorize
modular inversion when \(S(cm)\) is a zero divisor modulo a composite
modulus. Treating remote values of \(S\) as primitive replaces the
cross-resultant problem by the weighted product in (29). On the unresolved
balanced branch,

\[
 \gcd(S(B),N)=p.
\tag{32}
\]

Hence the literal resultant grammar has the following named-model
boundary:

- expanding (25) to short blocks gives a linear number of base offsets and
  a linear-size full memoized DAG in the remote length;
- telescoping those offsets invokes \(S\), whose target value is already a
  factor-bearing weighted interval product.

This dichotomy is not exhaustive for all arithmetic identities or
algorithms.

### Resource consequence for the literal grammar

Let a remote length be \(M=2^tq_0\), where each base block has
\(q_0\leq Q(n)\) and \(Q\) is a fixed numerical quasipolynomial. If
\(M=2^{\Theta(n)}\), then

\[
 \frac{M}{q_0}=2^{\Theta(n)}.
\tag{33}
\]

For the standalone expansion of \(R_1(M)\), the base frontier and complete
cross-resultant DAG have respectively

\[
 \boxed{\frac{2M}{q_0}-1}
\tag{34}
\]

and

\[
 \boxed{\frac{4M}{q_0}-t-3}
\tag{35}
\]

states.

When \(t\geq1\), the discriminant recursion

\[
 D_{2m}=D_m^2R_1(m)^2,
\tag{36}
\]

the top cross term is \(R_1(M/2)\). Expanding down to length \(q_0\)
has exactly

\[
 \boxed{\frac{M}{q_0}-1}
\tag{37}
\]

base-frontier offsets and

\[
 \boxed{\frac{2M}{q_0}-t-2}
\tag{38}
\]

cross-resultant DAG states. The lower discriminant cross terms are already
substates of this top cross-resultant DAG. Including the \(t+1\)
discriminant states gives exactly

\[
 \boxed{\frac{2M}{q_0}-1}
\tag{39}
\]

states in the full literal discriminant/resultant DAG.

When \(t=0\), there is one discriminant state and no cross-resultant
state, so (39) still gives the correct total.

Storing one residue word per keyed state takes
\(\Theta((M/q_0)n)\) bits, and even streaming the distinct states takes
\(\Omega(M/q_0)\) state operations. These are exact costs for this literal
recursion only.

## 5. Carry and finite-residue boundary

No carry theorem is reproved here. The exact local imported boundaries are:

- P173/F196: statement SHA-256
  07d2bccb9f508248a44f39faba3bd13a87cc0b2a1bc3dafa1464c348ae871c5c
  and proof SHA-256
  9f6e71c1c69661ad62780f0864b8fa460bd43df9f262b2774b7d231d20bba19b;
- P174/F197: statement SHA-256
  774ce7c5496c28942d6cb11814b95cc2487ae10477127d40d8609332090e49c3
  and proof SHA-256
  6b30bd83a52b380c6f04e32c4839b924324b5e55688e48077265abd06e83bc84;
- P177/F200 V2: statement SHA-256
  1edaedf1e0121e4603b8502cfb2473de250366cdc4b35acb216c3be314c8b7e5
  and proof SHA-256
  b573b44d35d577e4c567448092997923c0a83cdeda8a1a1cb89ec9e1cf03e30b.

Those promoted results respectively identify the beta-two signed quotient
carry, the factorial quotient-bit gate, and the failure of factor-free
finite-residue integrality tests to orient the harmonic path. A genuinely
Archimedean nonlinear carry is outside F273 V2 and remains a possible new
mechanism. Searching such a carry is not the product/resultant grammar
studied here.

## Exact exclusions

F273 V2 proves no:

1. lower bound for arbitrary arithmetic or Boolean circuits;
2. lower bound for the uniform interval-product evaluator left open by
   P221/F272;
3. impossibility result for affine-specific, characteristic-specific, or
   nonlinear identities;
4. lower bound for succinct determinant, Smith, resultant, or matrix
   algorithms outside the stated literal models;
5. equivalence between the diagonal factorial and lcm gates;
6. claim that the interval evaluator is the unique surviving factoring
   route;
7. numerical-quasipolynomial evaluator;
8. integer-factoring algorithm; or
9. computational or empirical result.
