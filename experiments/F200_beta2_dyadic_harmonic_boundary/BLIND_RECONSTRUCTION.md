# F200 blind reconstruction

## Verdict and evidence boundary

**PASS**, relative to the named imported P173, P175, and normalized-P161
interfaces. All claims that are internal to F200 follow from first principles.
The claimed obstructions have the limited scope stated in the candidate.

Before I read the statement, I computed this SHA-256 digest:

```text
e6516eb85462f577d899bb4bfe50fd62b6ceea58e5752bb2c806208b42440713  STATEMENT.md
```

I read only the repository-root `PROMPT.md` and the F200 `STATEMENT.md`. I did
not inspect a proof, self-audit, manifest, other audit, candidate message, or
durable ledger. I ran no mathematical computation.

The statement cites earlier results for three facts: the definition and role
of the P173 carry, the P173 endpoint evaluator, the P175 terminal precision,
and the order property on a normalized P161 branch. A statement-only review
cannot re-prove those unavailable interfaces. The deductions from them are
checked below.

## Preliminary range facts

Since \(p<q\),

\[
p<\sqrt{pq}<q.
\]

The square root is not an integer because \(p\ne q\). Therefore

\[
p\le B=\lfloor\sqrt N\rfloor<q<2p.
\tag{A}
\]

Consequently, among \(1,\ldots,B\), the only integer that is not coprime to
\(N=pq\) is \(p\). There is no multiple \(2p\), and there is no multiple of
\(q\), in this range. These strict endpoints drive Theorem 1.

## Theorem 1: the one-denominator delta

The signed binomial recurrence is

\[
A_j=-\frac{N-j}{j}A_{j-1}.
\]

Thus

\[
j(A_j-A_{j-1})=-(N-j)A_{j-1}-jA_{j-1}=-NA_{j-1},
\]

and hence

\[
x_j=\frac{A_{j-1}}j=\frac{A_{j-1}-A_j}{N}.
\tag{B}
\]

If \(j\ne p\), (A) gives \(\gcd(j,N)=1\). The integral recurrence says
\(j\mid NA_{j-1}\), so \(j\mid A_{j-1}\). Hence \(x_j\) is an integer.

At \(j=p\),

\[
A_{p-1}=\binom{N-1}{p-1}
=\prod_{r=1}^{p-1}\frac{N-r}{r}
\equiv\prod_{r=1}^{p-1}\frac{-r}{r}
=(-1)^{p-1}=1\pmod p.
\]

Here all denominators are units modulo \(p\), and \(p\) is odd. Therefore

\[
x_p=\frac{A_{p-1}}p\in\mathbb Z+\frac1p.
\]

The sign of the exceptional fraction is exactly positive. Passing to
\(\mathbb Q/\mathbb Z\) proves

\[
\bar x_j=\frac1p\mathbf1_{j=p}.
\tag{C}
\]

For any subset \(I\), (C) gives

\[
S_I\in
\begin{cases}
\mathbb Z,&p\notin I,\\
\mathbb Z+1/p,&p\in I.
\end{cases}
\]

Equation (B) makes \(D_I=NS_I\) an integer. In the two cases,

\[
D_I\equiv0\pmod N,
\qquad
D_I\equiv N/p=q\pmod N,
\]

respectively. Thus the gcd values are \(N\) and \(q\), including the case
\(D_I=0\), for which \(\gcd(0,N)=N\).

By (A), a product of distinct indices from \(1,\ldots,B\) contains a prime
factor of \(N\) exactly when it contains the index \(p\). It then contains
one factor \(p\), no factor \(q\), and no second multiple of \(p\). This proves
the interval-product gcd formula.

Finally, for \(I=[a,b]\), equation (B) telescopes with the exact sign

\[
S_{[a,b]}=\frac1N\sum_{j=a}^b(A_{j-1}-A_j)
=\frac{A_{a-1}-A_b}{N}.
\]

Thus all four tests in Theorem 1 detect the same event \(p\in I\). This is an
equivalence of exact tests. It does not make any one test inexpensive.

## Theorem 2: the carry is an Archimedean floor

Apply the last formula to the root interval and use \(A_0=1\):

\[
\sum_{j=1}^Bx_j=\frac{1-A_B}{N}.
\]

The definition \(A_B=1-q+Nh\) yields

\[
\frac{1-A_B}{N}=\frac{q-Nh}{N}=\frac1p-h.
\tag{D}
\]

Since \(h\in\mathbb Z\) and \(0<1/p<1\), equation (D) has floor \(-h\).
This proves the boxed formula, including its minus sign.

For any \(I\) containing \(p\), Theorem 1 gives a unique expression

\[
S_I=\lfloor S_I\rfloor+\frac1p.
\]

Because \(p\) is odd, \(1/p\) is a well-defined element of \(\mathbb Z_2\),
and its reduction modulo \(2^t\) is exactly
\(p^{-1}\bmod2^t=u_t\). The operation that separates the ordinary integer
part from this rational number is the Archimedean floor, or equivalently an
exact rational integrality test after a proposed correction. Interpreting the
same displayed rational in \(\mathbb Z_2\) retains its full 2-adic value but
does not, by that interpretation alone, apply the Archimedean floor map. The
later density argument makes this boundary precise for value-local continuous
2-adic tests.

## Theorem 3: exact transform behavior

Let \(f\) be the zero-padded length-\(M\) signal in
\((\mathbb Q/\mathbb Z)^M\). Equation (C) says that it is the delta
\(p^{-1}\delta_p\).

### Walsh transform

For any Walsh character \(\chi\), the unnormalized coefficient is

\[
\sum_j\chi(j)f(j)=\frac{\chi(p)}p=\pm\frac1p
\quad\text{in }\mathbb Q/\mathbb Z.
\]

Neither sign is zero in this quotient. Hence all \(M\) Walsh coefficients
are nonzero.

### Fourier transform and its quotient ring

Let \(K=\mathbb Q(\zeta_M)\). With either Fourier sign convention, the
coefficient at frequency \(s\) is

\[
\frac{\zeta_M^{\pm sp}}p+\mathcal O_K.
\tag{E}
\]

This construction is well-defined: changing a rational lift of any
\(\bar x_j\) by an integer changes its coefficient by an algebraic integer.
The class in (E) is nonzero because \(\zeta_M^{\pm sp}\) is an algebraic
unit, whereas its quotient by the rational prime \(p\) is not an algebraic
integer. Thus the Fourier spectrum has full support in \(K/\mathcal O_K\).

The quotient is an additive quotient group. The proof uses only multiplication
of chosen lifts by algebraic integers. It does not treat
\(K/\mathcal O_K\) as a quotient ring, because \(\mathcal O_K\) is not an
ideal of the field \(K\).

### Haar transform

Use the unnormalized dyadic Haar system. At each dyadic scale, the support
point \(p\) lies in one wavelet support. That wavelet takes value \(+1\) or
\(-1\) at \(p\), so its coefficient is \(\pm1/p\). Every other wavelet at
that scale misses \(p\) and has coefficient zero. The active internal nodes
are exactly the ancestors of the leaf \(p\), which is the unique
root-to-leaf path. The root scaling coefficient is additionally \(1/p\); it
is not a wavelet coefficient and does not alter the stated count.

### Cyclic differences

For one convention, \(\Delta_hf(j)=f(j+h)-f(j)\). Fourier transformation
multiplies the coefficient at \(s\) by
\(\zeta_M^{sh}-1\). Reversing either convention changes only harmless signs
or inverses. Iteration therefore gives

\[
\frac{\zeta_M^{\pm sp}}p
\prod_r(\zeta_M^{\pm s h_r}-1).
\]

If \(M=2^r\) and \(h\) is odd, the multiplier vanishes exactly when
\(M\mid s\), namely only at zero frequency. More generally, for a nonzero
shift modulo \(M\) with \(a=\nu_2(h)<r\), its zero set consists of the
multiples of \(2^{r-a}\) and has \(2^a\le M/2\) frequencies. The zero sets
for several nonzero shifts are nested according to \(a\). Thus any iterated
nontrivial difference retains at least half of the frequencies. In
particular, iterated odd differences retain every nonzero frequency. A shift
\(h=0\) is the trivial zero operator and is outside this non-sparsity claim.

For the rational lift \(p^{-1}\delta_p\), the unnormalized cyclic
autocorrelation is

\[
R(h)=\sum_{j\bmod M}f(j)f(j+h)
=p^{-2}\mathbf1_{h=0},
\]

which is independent of \(p\)'s location. This is the convention consistent
with the exact scalar displayed in the statement. If “average” is instead
defined with the normalized measure \(M^{-1}\sum_j\), the value has the
additional factor \(1/M\); the location-independence conclusion is unchanged.

### Reciprocal-prefix cells

Inversion is a permutation of the odd residue classes modulo \(2^t\). The
index \(p\) belongs to exactly the cell

\[
C_{t,u_t},\qquad u_t=p^{-1}\pmod{2^t}.
\]

All other members of all cells have integral \(x_j\). Therefore the vector of
cell sums in \(\mathbb Q/\mathbb Z\) is a single delta of height \(1/p\) at
\(u_t\). Any bijective Boolean labelling of the \(2^{t-1}\) odd residue
classes turns it into a Boolean delta, whose Walsh transform has full support.
Finally,

\[
j^{-1}\equiv a\pmod{2^t}
\quad\Longleftrightarrow\quad
j\equiv a^{-1}\pmod{2^t},
\]

so the time-domain cell is exactly the claimed arithmetic progression.
“Every Boolean labelling” must mean every bijective labelling; a collapsing
noninjective map would not be a labelling of the residue classes.

## Theorem 4: finite 2-adic consistency and tree gauge

Theorem 1 places every \(x_j\) in \(\mathbb Z[1/p]\subset\mathbb Z_2\), so
its reduction modulo \(2^t\) is defined. If a node is the disjoint union of
its children, then

\[
s_v=s_{v_0}+s_{v_1}.
\]

Fix arbitrary \((\ell,u)\). Exactly one child of \(v\) contains \(\ell\)
when \(v\) contains \(\ell\), and no child contains it otherwise. Hence

\[
\mathbf1_{\ell\in v}
=\mathbf1_{\ell\in v_0}+\mathbf1_{\ell\in v_1}.
\]

Subtracting \(u\) times this identity from the first proves every fork
equation for \(c^{(\ell,u)}\). This works for every leaf and every residue;
it is the exact gauge symmetry. Every class modulo \(2^t\) has an ordinary
integer representative, so that additional condition is vacuous at finite
precision.

For the true pair \((p,p^{-1})\), let \(S_v=\sum_{j\in v}x_j\) as a rational
number. If \(p\notin v\), then \(S_v\) is an integer. If \(p\in v\), then
\(S_v=\lfloor S_v\rfloor+1/p\). Therefore in both cases

\[
c_v^{(p,p^{-1})}\equiv\lfloor S_v\rfloor\pmod{2^t}.
\]

Thus the exact floors are representatives for the true gauge, but finite
residues do not identify that gauge.

It remains to check nonemptiness at a one-bit lift. The two lifts of an odd
residue modulo \(2^r\) are odd residues modulo \(2^{r+1}\), and inversion
maps them to two odd index classes modulo \(2^{r+1}\). Every residue class
modulo \(2^{r+1}\) has a positive representative at most \(2^{r+1}\). In the
sub-quarter range,

\[
2^{r+1}\le O(N^{1/4})<B
\]

for all sufficiently large \(N\). Therefore both cells are nonempty. The
same fork identities hold for a proposed leaf in either cell, so additive
feasibility cannot choose the correct child.

An invertible linear coordinate change sends this family of indistinguishable
additive solutions bijectively to another such family. Haar and Walsh changes
therefore cannot remove the gauge. This is not a claim about a nonlinear or
Archimedean constraint.

## Theorem 5: the exact evaluation boundary

Use \(Nx_j=A_{j-1}-A_j\). Then

\[
\begin{aligned}
N\sum_{j=1}^Bw_jx_j
&=\sum_{j=1}^Bw_jA_{j-1}-\sum_{j=1}^Bw_jA_j\\
&=w_1A_0+\sum_{j=1}^{B-1}(w_{j+1}-w_j)A_j-w_BA_B.
\end{aligned}
\]

The signs and endpoints match the statement. If exactly \(R\) adjacent
differences \(w_{j+1}-w_j\) are nonzero, at most those \(R\) internal terms
and the two endpoint terms survive. This proves the \(R+2\) bound. The
coefficients need not be \(\pm1\); “signed binomial values” here means the
corresponding weighted signed-binomial terms.

Conditional on the cited P173 evaluator, a numerical-QP number of selected
\(A_j\bmod2^t\) values can be evaluated in numerical-QP total time. The
displayed identity then gives the finite 2-adic sums used in Theorem 4. It
does not give their ordinary floors.

A contiguous interval indicator has only its entry and exit changes, so its
run count is \(O(1)\). An exact support test of its sum determines whether
the interval contains \(p\), and Theorem 1 then yields a factor. This explains
why efficient residue evaluation is not the same as an efficient exact
nonzero or integrality test.

For a residue-prefix cell, put \(L=2^t\) and let \(r\) be its odd index
residue. Its members are

\[
r,r+L,r+2L,\ldots\le B.
\]

Since \(L\ge2\), each member is an isolated run in the Boolean indicator.
The number of runs is

\[
\frac BL+O(1)=\Theta(B/2^t)
\]

in the P175 range. If

\[
t=\left\lfloor\frac{log_2N}{4}\right\rfloor-L_0(n),
\qquad L_0(n)=(\log n)^{O(1)},
\]

then

\[
\frac B{2^t}
=\Theta\!\left(N^{1/4}2^{L_0(n)}\right)
=N^{1/4}2^{(\log n)^{O(1)}}
\]

up to fixed floor factors. This is \(2^{\Theta(n)}\), not numerical QP.
The adjacent-change count differs from the run count by only a factor at most
two and boundary terms, so literal endpoint materialization is also
exponential.

The active cell contains exactly one exceptional index, \(p\). Uniform
sampling from its \(\Theta(B/2^t)\) members hits that index with probability

\[
\Theta(2^t/B)
=N^{-1/4}2^{-(\log n)^{O(1)}}.
\]

Its reciprocal is exponential in \(n\). These are exact accounting facts for
the literal endpoint and uniform-sampling methods. They do not bound a
succinct or implicit circuit.

## Theorem 6: residue, phase, and local-cyclotomic boundaries

### Factor-free auxiliary residue rings

Let \(M\) be public. Computing \(g=\gcd(M,N)\) either yields a proper factor
when \(1<g<N\), or enters a branch with no such factor. On the branch
\(\gcd(M,N)=1\), \(N\) is a unit modulo \(M\), so the universal property of
localization gives

\[
\mathbb Z[1/N]\longrightarrow\mathbb Z/M\mathbb Z.
\]

Since \(1/p=q/N\), its image is \(qN^{-1}=p^{-1}\pmod M\). Choose an
ordinary integer \(r\equiv p^{-1}\pmod M\). Then every
\(m+1/p\) has the same residue as the ordinary integer \(m+r\). Therefore no
predicate of that residue alone can accept all ordinary integers and reject
all values of the second form.

For finitely many factor-free moduli, take their least common multiple
\(L\). It is still coprime to \(N\), and an integer
\(r\equiv p^{-1}\pmod L\) realizes the required compatible tuple. This
proves the product-ring version even when the moduli are not pairwise
coprime. If \(N\mid M\), the localization map is unavailable because \(N\)
is not a unit. That composite-characteristic case is correctly outside the
claim.

For \(M=2^t\), surjectivity of \(\mathbb Z\to\mathbb Z/2^t\mathbb Z\)
is the same finite argument. At infinite precision, \(\mathbb Z\) is dense
in \(\mathbb Z_2\). If a continuous function to a Hausdorff target is
constant on \(\mathbb Z\), continuity makes it constant on its closure,
which is all of \(\mathbb Z_2\). Thus a value-local continuous Mahler
function or finite-precision 2-adic character cannot implement the stated
integer-versus-fractional separator. An algorithm that also reads the
succinct rational expression and applies an Archimedean operation is not a
value-local function and is not covered.

### Ordinary additive phases

For integer \(m\), Theorem 1 gives

\[
e^{2\pi i mS_I}
=\begin{cases}
1,&p\notin I,\\
e^{2\pi i m/p},&p\in I.
\end{cases}
\]

The elementary bound \(|e^{i\theta}-1|\le|\theta|\) gives, for
\(|m|\le Q(n)\),

\[
|e^{2\pi i m/p}-1|\le\frac{2\pi Q(n)}p.
\]

Fixed balance gives \(p>\sqrt{N/2}=2^{n/2-O(1)}\), whereas numerical QP has
\(\log_2Q(n)=(\log n)^{O(1)}=o(n)\). Hence the upper bound is
\(2^{-\Omega(n)}\). In particular it is smaller than every inverse numerical
QP bound for all sufficiently large inputs.

If \(m\) is uniform modulo \(N\), then \(m\bmod p\) is uniform modulo \(p\).
A constant fraction of these residues have circular distance at least, for
example, \(p/6\) from zero. Their active phases have a fixed positive distance
from one. This proves the constant-separation probability.

Because \(D_I=NS_I\), the exact identity

\[
e^{2\pi i mS_I}=e^{2\pi i mD_I/N}
\]

has no sign ambiguity. If \(\gcd(m,N)=1\), this phase is one exactly when
\(N\mid D_I\). By Theorem 1, this is exactly the condition \(p\notin I\).
Thus exact equality testing of the phase is the same factor-bearing support
test. An exact numerical-QP evaluator for adaptively selected dyadic cells
would test one child at each of \(O(\log B)=O(n)\) forks, isolate \(p\), and
factor \(N\). The claim does not say that such an evaluator exists.

### Exact 2-adic cyclotomic representations

Let \(E/\mathbb Q_2\) be finite with residue field
\(\mathbb F_{2^f}\), and suppose \(E\) contains a primitive \(p\)-th root
\(\zeta\). Reduction is injective on the odd-order roots of unity: an
odd-order root in the pro-2 group \(1+\mathfrak m_E\) must be trivial.
Therefore the reduction of \(\zeta\) still has order \(p\). It follows that

\[
p\mid 2^f-1,
\qquad
\operatorname{ord}_p(2)\mid f.
\tag{F}
\]

In particular, the extension degree satisfies
\([E:\mathbb Q_2]\ge f\ge\operatorname{ord}_p(2)\).

On the normalized P161 branch cited in the statement, assume the surviving
element is \(2^a\bmod p\). Its multiplicative order is

\[
\frac{\operatorname{ord}_p(2)}
{\gcd(\operatorname{ord}_p(2),a)},
\]

so it divides \(\operatorname{ord}_p(2)\). If the branch certifies that this
order exceeds the selected numerical-QP dimension cap, then
\(\operatorname{ord}_p(2)\) also exceeds the cap. Equation (F) excludes a
finite extension within that cap that contains a primitive \(p\)-th root,
which is the active phase when \(\gcd(m,p)=1\).

This last deduction is only a representation-degree boundary. It depends on
the cited P161 normalization and its order certificate. It does not exclude
complex approximations, implicit encodings, extensions not bounded by that
cap, or a different phase representation.

## Final scope audit

- Exact support, integrality, endpoint-gcd, and interval-product tests are
  equivalent factor-bearing events. F200 does not make them numerical QP.
- Walsh and Fourier spread the delta. Haar localizes it to a path but does not
  label the active path without an exact support test.
- Finite additive tree constraints have a gauge for every proposed leaf.
  Archimedean floors and other nonlinear constraints are outside that gauge.
- Literal residue-cell endpoint evaluation and uniform coordinate sampling
  have exponential run or trial counts at P175 precision. This is not a
  circuit lower bound.
- Factor-free residue rings and continuous value-local 2-adic functions cannot
  detect the Archimedean integer part. Succinct rational representations are
  outside this claim.
- Bounded ordinary frequencies have exponentially small signal. Exact
  high-order phases would factor, but no such QP evaluator is constructed.
- The local cyclotomic result bounds explicit finite-extension degree on the
  specified P161 branch only.
- The exact remaining opening in the statement is therefore consistent with
  all six theorems. It is an open research direction, not a terminal factoring
  result.

