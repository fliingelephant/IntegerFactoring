# Proof-blind reconstruction result

## Verdict

**FAIL as a universal statement exactly as written.**

The square-class theorem itself passes. Claims 1--4, the algebraic part of
Claim 5, and the sequential accounting in Claim 6 are correct. The failure is
the last factoring sentence in Claim 5 unless \(N\) is odd, or unless factor
\(2\) has already been removed. For example, take \(N=6\) and the canonical
self-inverse endpoint \(g=w=1\). Then \(g\) is a global root of one, but

\[
\gcd(g+1,N)=\gcd(2,6)=2
\]

still factors \(N\). No odd-\(N\) hypothesis appears in the statement.

With the following exact scope, the result is a **PASS**:

1. "odd total multiplicity" in Claim 4 means odd multiplicity in the full
   product \(gw\), not in \(w\) alone;
2. \(N\) is odd, or the factor-\(2\) screen has already run; and
3. "no dependency ever appears" in Claim 6 means that no *new* dependency is
   created. Absolute absence also requires the initial nullity to be zero.

The proof below establishes this corrected scope and isolates every
qualification.

## Intrinsic square-relation map

For positive integers \(B_1,\ldots,B_m\), define

\[
\Phi:\mathbb F_2^m\longrightarrow
\mathbb Q_{>0}^{\times}/(\mathbb Q_{>0}^{\times})^2,
\qquad
x\longmapsto
\left[\prod_{j=1}^m B_j^{x_j}\right].
\]

Thus \(x\in\ker\Phi\) exactly when the indexed subproduct selected by \(x\)
is a rational square. For a positive integer, being a rational square is
equivalent to every prime valuation being even, and hence to being an integer
square. Therefore \(\ker\Phi\) is the exact indexed square-relation space. It
is defined by the integers themselves and does not depend on a gcd-free
representation.

## Claim 1: independent composite blocks

Let \(q_1,\ldots,q_r\) be pairwise-coprime positive nonsquares. Suppose a
nonempty subset product \(\prod_{i\in S}q_i\) were a square. Choose
\(i\in S\). Since \(q_i\) is not a square, some prime \(p\mid q_i\) has odd
valuation in \(q_i\). Pairwise coprimality gives \(p\nmid q_k\) for every
\(k\ne i\). Hence

\[
v_p\!\left(\prod_{k\in S}q_k\right)=v_p(q_i)
\]

is odd, a contradiction. Consequently the square classes
\([q_1],\ldots,[q_r]\) are linearly independent over \(\mathbb F_2\).

This proof does not require the blocks to be prime. If a block is a prime
power, nonsquareness says precisely that its prime exponent is odd. If a
block is composite, one of its prime valuations is odd and cannot be
cancelled by a coprime block.

Write an exact refined representation as

\[
B_j=s_j^2\prod_{i=1}^r q_i^{E_{ij}},
\qquad M_{ij}=E_{ij}\bmod 2.
\]

The independent block classes define an injective coordinate map
\(\iota:\mathbb F_2^r\to
\mathbb Q_{>0}^{\times}/(\mathbb Q_{>0}^{\times})^2\), and
\(\Phi=\iota\circ M\). Therefore

\[
\ker M=\ker\Phi.
\]

Claim 1 passes, including its composite-block and prime-power cases.

## Claim 2: later refinement

Let \(M_{\rm before}\) and \(M_{\rm after}\) be two complete exact gcd-free
representations of the same indexed old integers. Applying the preceding
argument to each representation gives

\[
\ker M_{\rm before}=\ker\Phi=\ker M_{\rm after}.
\]

Thus a split need not induce an invertible square row change, and the number
of rows can change. Neither fact matters. Both matrices compute the same
intrinsic predicate: whether each selected old product is a square. Square
pieces can be omitted from parity coordinates because they are zero in the
square-class group. Their exact exponents can still be retained for later
integer-root construction.

In particular, refining after a later relation arrives cannot create or
destroy a dependency among the fixed old indexed columns. Claim 2 passes.

## Claim 3: one appended indexed column

Let \(\rho=\operatorname{rank}M\). For the augmented matrix
\(A=[M\ b]\), elementary linear algebra gives

\[
\operatorname{rank}A=
\begin{cases}
\rho,&b\in\operatorname{colspan}M,\\
\rho+1,&b\notin\operatorname{colspan}M.
\end{cases}
\]

Rank-nullity then gives

\[
\dim\ker A-\dim\ker M=
\begin{cases}
1,&b\in\operatorname{colspan}M,\\
0,&b\notin\operatorname{colspan}M.
\end{cases}
\]

If row \(i\) is zero in every old column while \(b_i=1\), then every vector
in \(\operatorname{colspan}M\) has coordinate \(i\) equal to zero. Hence
\(b\notin\operatorname{colspan}M\), so no immediate dependency is created.
Claim 3 passes.

## Claim 4: the exact arithmetic witness

In a fully refined exact representation, let \(q_i\) be a nonsquare block and
let \(E_{ij}\) be its exponent in old value \(B_j\). Its row is new-only and
detects the new relation precisely when

\[
E_{ij}\equiv0\pmod2\quad(1\le j\le m),
\qquad
E_{i,m+1}\equiv1\pmod2.
\]

The old exponents may be positive and even. Thus "new-only" is a parity
statement, not an assertion that the integer block was absent from every old
value.

A clean sufficient version of the coprime-factor case is this: there is a
prime \(p\mid w\) such that

\[
p\nmid\prod_{j=1}^m B_j
\quad\text{and}\quad
v_p(gw)\text{ is odd}.
\]

Let \(q_i\) be the refined block containing \(p\). Exactness gives

\[
v_p(gw)\equiv v_p(q_i)E_{i,m+1}\pmod2,
\]

because any omitted square contribution has even valuation. Since the left
side is odd, both factors on the right are odd. Thus \(q_i\) is nonsquare and
its new exponent is odd. If \(q_i\) occurred to a positive exponent in an old
value, then \(p\) would divide that old value, contrary to the coprimality
condition. Hence this is a new-only row. The same argument applies to a
coprime component of \(w\) whose contribution to \(gw\) has nontrivial square
class.

The phrase "odd total multiplicity" must refer to \(gw\). Odd multiplicity in
\(w\) alone is not sufficient. For a hand check, take \(N=15\), \(g=2\), and
its canonical inverse \(w=8\). The prime \(2\) has odd exponent \(3\) in
\(w\), but exponent \(4\) in \(gw=16\), so the new parity column is zero.

The coprime condition is not necessary. For example, let the old value be
\(B_1=4\), and append \(B_2=gw=8\) (one realization is
\(N=7,g=2,w=4\)). The refined block \(2\) has exponent row \((2,3)\), hence
parity row \((0,1)\). It is new-only even though \(2\) already divides the
old value. Claim 4 passes under the stated total-\(gw\) reading.

## Claim 5: self-inverse feedback

Assume "canonical" means that each invertible residue class has one chosen
representative and that \(w\) is the chosen representative of \(g^{-1}\).
If \(g^{-1}\equiv g\pmod N\), uniqueness of the representative gives \(w=g\)
as integers. Therefore the new exact value is \(g^2\), an integer square, and
its square-class column is zero. If the algorithm really appends a new
indexed column, then

\[
e_{m+1}\in\ker[M\ 0]
\]

is a new singleton dependency. This part of Claim 5 passes.

Also \(g^2\equiv1\pmod N\). For odd \(N\), set

\[
d_- = \gcd(g-1,N),\qquad d_+=\gcd(g+1,N).
\]

If \(g\not\equiv\pm1\pmod N\), neither \(d_-\) nor \(d_+\) equals \(N\). If,
say, \(d_-=1\), then \(N\mid(g-1)(g+1)\) and invertibility of \(g-1\) modulo
\(N\) would imply \(g\equiv-1\pmod N\), a contradiction. Thus both gcds are
nontrivial proper divisors. Conversely, for odd \(N\), a global residue
\(g\equiv1\) or \(-1\pmod N\) gives one gcd equal to \(N\) and the other equal
to \(1\). This is the standard non-global-root criterion.

For even \(N\), the converse fails because the two global integer roots differ
by \(2\), which can share a factor with \(N\). The \(N=6,g=1\) counterexample
in the verdict therefore refutes the unrestricted final sentence of Claim 5.
Running the direct screens first is correct operationally, but it does not
make that unrestricted sentence true; it instead supplies the needed
factor-\(2\) preprocessing.

## Claim 6: sequential closure accounting

After step \(t\), let \(n_t\) be the number of actual indexed columns and let
\(R_t\) be the dimension of the span of their intrinsic square classes. Then

\[
d_t=n_t-R_t=\dim\ker\Phi_t.
\]

Refinement changes neither the integers nor \(n_t\), so it changes neither
\(R_t\) nor \(d_t\). On appending one actual indexed relation, \(n_t\) rises
by one. Its class is either outside the old span, in which case \(R_t\) also
rises by one and \(d_t\) stays fixed, or inside the old span, in which case
\(R_t\) stays fixed and \(d_t\) rises by one. These are the only cases.

A formerly new-only block can recur and help close a later column. For
example, append the distinct indexed values \(B_1=2\) and then \(B_2=8\). At
the first insertion, the block \(2\) is new-only. At the second insertion the
parity columns are both \(1\), and \(B_1B_2=16\) gives the dependency
\((1,1)\).

Suppose instead that every newly appended column has, at its insertion time,
a nonsquare row that is zero on every earlier column and one on the new
column. Claim 3 shows at every step that the new class is outside the current
span. Therefore rank and column count rise together at every insertion and

\[
d_t=d_0\quad\text{for all }t.
\]

Later refinement cannot invalidate this conclusion by Claim 2. Later columns
may contain an earlier private block, but each must also have its own fresh
row, so the induction still holds.

Thus the exact conclusion is "no new dependency appears." If \(d_0=0\), no
dependency exists at any time. If \(d_0>0\), old dependencies remain. For
example, an initial square column already has a singleton dependency even if
every later column has a private new-only row. Claim 6 passes with this
necessary reading of its final sentence.

## Indexed columns, deduplication, and usefulness

The domain of \(\Phi\) has one coordinate per column that the algorithm
actually appends.

- If equal values are appended as two indexed columns, their columns are
  equal and the vector selecting those two indices is a dependency. The
  second append raises nullity by one.
- If the algorithm deduplicates the value, it appends no column, so neither
  column count nor nullity changes.
- If an appended value is a square, its column is zero and its indexed unit
  vector is a singleton dependency.

These statements count exact rational-square products only. They do not show
that the two modular square roots obtained from a dependency differ by
non-global signs. A duplicate or square column can therefore produce only a
globally trivial root. Composite gcd-free blocks are coordinate objects, not
a fixed prime factor base, and later splitting is allowed. None of the rank
arguments supplies smoothness, a selector, a recurrence bound, a probability,
a runtime estimate, or a factoring algorithm.

## Finite checks

For \(N=21\),

\[
10\cdot19=190=1+9\cdot21,
\qquad
\gcd(10-1,21)=3.
\]

The factor \(19\) occurs oddly in \(190\). If, as the check states, its old
parity row is zero, Claim 3 proves that the new column is outside the old
span. If the two old columns were independent, the three columns are then
independent. The old relation values are not supplied in the statement, so
the numerical data \(N=21,g=10,w=19\) alone cannot independently verify either
the old-zero premise or the old rank; those parts of the check are
conditional on the stated old data.

For \(N=55\),

\[
21^2=441=1+8\cdot55,
\quad
\gcd(21-1,55)=5,
\quad
\gcd(21+1,55)=11.
\]

Thus \(21\) is self-inverse, the appended square has zero parity column, the
indexed singleton dependency exists, and the direct screens expose both
proper factors. This check passes exactly.

## Claim-by-claim status

| Claim | Status | Exact scope |
|---|---|---|
| 1 | PASS | Positive pairwise-coprime nonsquare blocks; indexed binary square relations. |
| 2 | PASS | Both refinements must be complete exact representations of the same old integers. |
| 3 | PASS | One actually appended indexed column. |
| 4 | PASS | Odd multiplicity is measured in \(gw\); the coprime case must contain a nontrivial square-class contribution. |
| 5 | FAIL as written | The canonical/zero-column part passes. The factoring-only clause needs odd \(N\) or prior removal of factor \(2\). |
| 6 | PASS with scoped wording | Private rows keep \(d_t=d_0\); absolute absence of dependencies needs \(d_0=0\). |
