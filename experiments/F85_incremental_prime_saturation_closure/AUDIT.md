# Hostile proof-only audit: PASS with scope qualifications

The audited RESULT.md has SHA-256
7a56d477a93ced216974f858645510488e0c7a115e1a6306488d88999d05d0da,
which matches the pinned value.

I found no counterexample to either theorem under the intended explicit
factor-block convention: the exponent entries are nonnegative integers, the
final refinement only splits blocks and copies their old exponent rows, and
“numerically polynomial-size” means that the value of \(\ell\), not merely
its bit length, is polynomially bounded. The direct-sum gate, root-coset
invariance, incremental decoder, and exact separator count are correct.

Three scope qualifications should be made explicit:

1. Nonnegativity of the exponents is used but is not formally declared.
2. The coset is canonical relative to the full lifted relation presentation,
   not relative to \([E\mid b]\bmod\ell\) alone.
3. If the public prime \(\ell\) equals \(p\) or \(q\), then
   \(\gcd(\ell,N)\) already factors \(N\). The local-group proof remains
   correct, but the “factor-free” interpretation is then vacuous.

These are specification and scope qualifications. They do not invalidate the
core result with its intended presentation semantics.

## 1. Refinement invariance

Suppose a final gcd refinement splits an old block \(q_j\) into pairwise
coprime factors. Every such factor occurs in every old relation with the same
exponent that \(q_j\) had. Thus the old row

\[
(e_{j1},\ldots,e_{jm})
\]

is replaced by one or more identical copies. Repeating a linear equation
does not change its solution set, so duplicating rows preserves
\(\ker(E\bmod\ell)\). A block that is new relative to all old relations adds
an all-zero old row, which also leaves the old kernel unchanged.

This verifies the claimed invariance for genuine factor-splitting
refinement. It would not justify arbitrary reblocking that changes old
exponent rows, but the candidate does not need such a broader operation.
The closing test must, as the candidate says, be applied to the final refined
pair \([E\mid b]\). A partial overlap with a new block can give different
entries of \(b\) on two copied old rows; this changes the new-column gate but
does not change the old kernel.

The refinement is public. Repeated gcd and exact-division splitting uses no
factorization of \(N\). Its number and bit cost are polynomial in the
explicit block presentation because every nontrivial split replaces an
integer by proper factors and the total represented bit length bounds the
number of such splits.

## 2. The closure direct sum

All linear algebra here is over \(\mathbb F_\ell\). A vector \((x,t)\) is in
the new kernel precisely when

\[
Ex+tb=0.
\]

If \(t\ne0\), then \(b=-t^{-1}Ex\) lies in the column span of \(E\).
Consequently, when \(b\) is outside that span, every kernel vector has
\(t=0\), and

\[
\ker[E\mid b]=V\times\{0\}.
\]

If \(Ec+b=0\), put \(z=(c,1)\). For any new kernel vector,

\[
(x,t)-tz=(x-tc,0),
\]

and \(E(x-tc)=0\). Hence every vector is in
\((V\times\{0\})+\langle z\rangle\). The intersection is zero because a
nonzero multiple of \(z\) has a nonzero last coordinate. Therefore

\[
\ker[E\mid b]=(V\times\{0\})\oplus\langle z\rangle.
\]

There is no missing rank case. This also works when \(V=0\), \(m=0\), or
\(\ell=2\).

## 3. The root map and the canonical coset

For \(x\in V\), choose its coordinates in
\(\{0,\ldots,\ell-1\}\). Each component of \(Ex\) is divisible by \(\ell\),
so the exponents in \(R(x)\) are integers. Raising to the \(\ell\)-th power
gives

\[
R(x)^\ell
=\prod_jq_j^{(Ex)_j}
=\prod_i A_i^{x_i}
\equiv1\pmod N.
\]

The homomorphism claim can be checked without appealing to F83. Let
\(\bar{x+y}\) be the canonical coordinate representative of \(x+y\), and
write

\[
x+y=\bar{x+y}+\ell k
\]

for an integer carry vector \(k\). Then

\[
\frac{E\bar{x+y}}{\ell}
=\frac{Ex}{\ell}+\frac{Ey}{\ell}-Ek.
\]

The last term contributes

\[
\prod_jq_j^{-(Ek)_j}
=\prod_iA_i^{-k_i}
\equiv1\pmod N.
\]

Thus \(R(x+y)=R(x)R(y)\).

In the closing case, \(Ec+b\equiv0\pmod\ell\), so the exponent vector
\((Ec+b)/\ell\) is integral and

\[
s_c^\ell
=A_*\prod_iA_i^{c_i}
\equiv1\pmod N.
\]

Applying the same homomorphism argument to the new kernel and using the
direct-sum decomposition gives

\[
H'=\langle H,s_c\rangle.
\]

If \(c'\) is another solution, let
\(v=c'-c\in V\) in field coordinates. Accounting for canonical-coordinate
carries as above gives

\[
s_{c'}=s_cR(v)\pmod N.
\]

Hence \(s_{c'}H=s_cH\). The coset is independent of the chosen solution.

The word “canonical” needs one qualification. The coset is canonical after
the integer exponent lift \(E,b\), the block list, and the appended relation
have been fixed. It is not determined by the reduced matrix
\([E\mid b]\bmod\ell\) alone. Replacing an integer lift \(b\) by
\(b+\ell d\) leaves the reduced column unchanged but multiplies \(s_c\) by
\(\prod_jq_j^{d_j}\), which need not lie in \(H\). The candidate's formulas
use the full fixed presentation, so the proof itself is sound.

The assertion that all displayed exponents are nonnegative additionally
requires

\[
e_{ji},b_j\in\mathbb Z_{\geq0}.
\]

This is the natural factor-block convention, but it should be stated. If
signed exponent relations are allowed, integrality still holds but
nonnegativity can fail. Public execution remains possible by modular
inversion because every \(q_j\) is a unit, but the literal nonnegativity
sentence would then be false.

## 4. Classification after old-decoder failure

For either prime factor, the local group of \(\ell\)-th roots has size

\[
|\mu_\ell(\mathbb F_p)|=\gcd(\ell,p-1)\in\{1,\ell\},
\]

and similarly at \(q\). After choosing an additive coordinate when the
group has order \(\ell\), the two projections of \(R\) are linear
functionals

\[
\alpha,\beta:V\longrightarrow\mathbb F_\ell,
\]

with the zero functional used for a trivial local root group.

An identity separator exists exactly at a vector in
\(\ker\alpha\mathbin\triangle\ker\beta\). Therefore failure of a genuinely
complete old decoder is equivalent to

\[
\ker\alpha=\ker\beta.
\]

If one functional is zero, equality forces both to be zero, and \(H=1\).
If both are nonzero, equal kernels imply that they are nonzero scalar
multiples. Their joint image is a one-dimensional graph whose two coordinate
projections are nontrivial. This verifies the dichotomy used by Theorem 2.

If every basis root is \(1\), homomorphism of \(R\) and spanning by the
basis imply \(H=1\). Otherwise a nonidentity basis root lies in the
order-\(\ell\) graph line and therefore generates all of \(H\).

This step is conditional on the old decoder actually being complete. The
candidate states that premise explicitly. The incremental theorem does not
by itself re-prove the scheduling theorem attributed to F83.

## 5. Completeness and the exact separator count

### Trivial old image

If \(H=1\), then \(H'=\langle s_c\rangle\). Each coordinate of \(s_c\) is
either the identity or has exact order \(\ell\). Every nonzero power preserves
whether that coordinate is the identity. Hence:

- if exactly one coordinate of \(s_c\) is the identity, \(s_c\) separates;
- if neither is the identity, no nonzero power separates; and
- if both are the identity, the image is unchanged.

Thus the single gcd test on \(s_c-1\) is complete.

### Nontrivial graph image

Use additive local coordinates and write

\[
h=(a,b),\qquad s_c=(u,v),
\]

where \(a,b\ne0\). The menu is the affine line

\[
s_cH=\{(u+ta,v+tb):t\in\mathbb F_\ell\}.
\]

If \(s_c\in H\), this is the old graph line. Its zero vector has two identity
coordinates, and every nonzero vector has two nonidentity coordinates. It
has no separator.

If \(s_c\notin H\), the first coordinate is zero at the unique value

\[
t_p=-u/a,
\]

and the second is zero at the unique value

\[
t_q=-v/b.
\]

If \(t_p=t_q\), then \(s_c=-t_ph\in H\), a contradiction. The two values are
therefore distinct. At \(t_p\) only the first coordinate vanishes, and at
\(t_q\) only the second vanishes. No other element has an identity
coordinate. Exactly two, not merely at least one, of the \(\ell\) menu
elements are separators.

This proves the equivalence between a separator in \(H'\) and a proper gcd
in the displayed menu. When \(s_c\notin H\), \(h,s_c\) span the full local
two-dimensional product, and the scanned coset already contains two
separators. The other cosets do not need to be scanned for the existence
test.

## 6. Local-group edge cases

### The case \(\ell=2\)

Since \(p,q\) are odd, both local root groups are
\(\mu_2=\{1,-1\}\). A nontrivial separator-free graph is the diagonal line
in \(\mathbb F_2^2\). Its other coset consists exactly of

\[
(0,1),\qquad(1,0)
\]

in additive coordinates. Both are separators. Thus the “exactly two”
statement remains true even though the complete menu itself has only two
elements. The trivial-image branch also works: one test of \(s_c\) detects
the only possible separator pattern.

### The cases \(\ell=p\) or \(\ell=q\)

If \(\ell=p\), then

\[
|\mu_p(\mathbb F_p)|=\gcd(p,p-1)=1.
\]

The \(p\)-local functional is zero. Equal old identity kernels force the
\(q\)-local functional to be zero as well, so only the \(H=1\) branch can
occur. Any new \(s_c\) has identity \(p\)-coordinate; if its \(q\)-coordinate
is nonidentity, the single test \(\gcd(s_c-1,N)\) returns \(p\). The case
\(\ell=q\) is symmetric. The graph-line and two-separator branch cannot
occur in either case, so there is no hidden exception to its proof.

There is an algorithmic scope issue: a public \(\ell\) equal to \(p\) or
\(q\) is already a public proper divisor, found immediately by
\(\gcd(\ell,N)\). A practical boundary check should perform this gcd before
the saturation logic. Also, if that factor has exponential numerical size
in \(\log N\), the candidate's polynomial scan claim does not apply because
its explicit hypothesis requires numerically polynomial \(\ell\).

## 7. Public executability

Every required operation is public:

- reduce \(E,b\) modulo \(\ell\);
- compute a basis of \(V\) and test whether \(b\) is in the column span;
- when it closes, obtain a solution \(c\) by the same linear algebra;
- form the exactly divisible integer exponent vectors for \(R(b_i)\) and
  \(s_c\);
- use modular exponentiation of the public \(q_j\);
- choose a basis root whose public residue is not \(1\), if one exists; and
- enumerate \(s_ch^t\) and compute \(\gcd(s_ch^t-1,N)\).

No step asks for \(p,q\), a local discrete logarithm, a local root-group
order, or a test of whether \(s_c\in H\). The scan succeeds or exhausts
without that hidden branch decision.

## 8. Bit complexity

Let the explicit presentation length include the dimensions of \(E\), the
bit lengths of all exponent entries and blocks, and \(\log N\). Gaussian
elimination over \(\mathbb F_\ell\) is polynomial in the matrix dimensions
and \(\log\ell\). Canonical coordinates are less than \(\ell\), so the
integer sums and exact quotients used for roots have bit length polynomial
in the presentation length and \(\log\ell\). Modular exponentiation is
polynomial in those exponent bit lengths and \(\log N\).

The menu can be generated recurrently from \(s_c\) by multiplication by
\(h\), using \(O(\ell)\) modular multiplications and gcds. This is polynomial
only when the numerical value of \(\ell\) is polynomially bounded in the
input length. If “polynomial-size” meant only
\(\log\ell=\operatorname{poly}(\log N)\), the scan could be exponential and
the complexity claim would be false. The candidate avoids that error by
saying “numerically polynomial-size”; that phrase should be retained and,
ideally, defined as \(\ell\leq\operatorname{poly}(\text{input length})\).

Computing every old basis root costs at most \(\dim V\) additional modular
root constructions, which is polynomial because \(\dim V\leq m\). The cost
paragraph mentions only one new induced-root construction, but the theorem
assumes the complete old decoder has already run; its basis roots can be
retained. Even if they are recomputed, the total remains polynomial.

## 9. Final scope judgment

The candidate correctly proves an incremental decoder, not a closure source.
It does not show that \(b\) enters the old column span, that the new coset
leaves the old graph, or that a useful numerically small prime can be selected
on every input. It therefore proves neither a general factoring algorithm
nor a success-density theorem.

The statement that one should not test only one induced odd-prime root is
supported: for \(\ell>2\), an outside affine coset has exactly two separators
among \(\ell\) elements, and the initially induced root need not be one of
them. The broader recommendation to retain prime saturations remains
conditional on the relevant public primes and relations being supplied; the
candidate's final source-gap paragraph states that limitation.

Verdict: **PASS**, subject to the explicit presentation and scope
qualifications listed above.
