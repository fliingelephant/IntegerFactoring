# F200 V2 candidate statement: the beta-two defect is a one-denominator harmonic delta

## Status and scope

Candidate, proof-only, and not yet independently checked.  V2 repairs the
two defects identified by the V1 hostile audit: the frozen hashes and the
scope of the optional P159--P161 cyclotomic corollary.  This is an exact
boundary for dyadic, Walsh, Haar, Mahler, floor, and sparse-transform attacks
on the promoted P175 gate.  It is not a lower bound for arbitrary arithmetic
circuits and it is not a factoring algorithm.

Assume

\[
N=pq,\qquad p<q<2p,
\qquad B=\lfloor\sqrt N\rfloor,
\]

where \(p,q\) are distinct odd primes.  Put

\[
A_k=(-1)^k\binom{N-1}{k}\qquad(0\leq k\leq B)
\]

and, for \(1\leq j\leq B\), put

\[
x_j={A_{j-1}\over j}\in\mathbb Q,
\qquad \bar x_j=x_j+\mathbb Z\in\mathbb Q/\mathbb Z.
\]

## Theorem 1: one-denominator delta

The exact recurrence

\[
j(A_j-A_{j-1})=-NA_{j-1}
\]

gives

\[
x_j={A_{j-1}-A_j\over N}.
\]

Every \(x_j\) except \(x_p\) is an integer, while

\[
x_p\in\mathbb Z+{1\over p}.
\]

Equivalently,

\[
\boxed{\bar x_j={1\over p}\,\mathbf 1_{j=p}}
\qquad\text{in }\mathbb Q/\mathbb Z.
\]

For an arbitrary subset \(I\subseteq\{1,\ldots,B\}\), define

\[
S_I=\sum_{j\in I}x_j,
\qquad D_I=NS_I=\sum_{j\in I}(A_{j-1}-A_j)\in\mathbb Z.
\]

Then

\[
\begin{array}{c|c|c|c}
&S_I\bmod\mathbb Z&D_I\bmod N&\gcd(D_I,N)\\ \hline
p\notin I&0&0&N\\
p\in I&1/p&q&q.
\end{array}
\]

Also, because \(q>B\) and \(B<2p\),

\[
\gcd\!\left(N,\prod_{j\in I}j\right)
=\begin{cases}1,&p\notin I,\\p,&p\in I.\end{cases}
\]

Thus exact support testing for the harmonic delta, exact rational
integrality testing, the endpoint-difference gcd, and the corresponding
interval-product test are the same factor-bearing event.

For a contiguous interval \(I=[a,b]\), the sum telescopes:

\[
\boxed{S_{[a,b]}={A_{a-1}-A_b\over N}.}
\]

## Theorem 2: the P175 carry is an Archimedean floor

Let \(A=A_B\), and let

\[
h={A-(1-q)\over N}
\]

be the P173 carry.  The root interval satisfies

\[
\sum_{j=1}^{B}x_j={1-A\over N}={1\over p}-h.
\]

Consequently,

\[
\boxed{
h=-\left\lfloor\sum_{j=1}^{B}{A_{j-1}\over j}\right\rfloor .}
\]

More generally, if \(p\in I\), then

\[
S_I=\lfloor S_I\rfloor+{1\over p}.
\]

The low 2-adic digits of the fractional correction are exactly the P175
target \(u_t=p^{-1}\bmod 2^t\).  Hence the integer-specific operation in
this identity is ordinary floor/integrality.  Merely embedding and evaluating
the displayed rational sum in \(\mathbb Z_2\) does not perform that
operation.

## Theorem 3: Haar is path-sparse, but Walsh and Fourier are full

Pad \((\bar x_j)\) by zeros to a dyadic length \(M\geq B\).

1. Every unnormalized Walsh coefficient is \(\pm1/p\) in
   \(\mathbb Q/\mathbb Z\).  Thus the Walsh spectrum has full support.
2. In \(K=\mathbb Q(\zeta_M)\), every discrete Fourier coefficient is
   \(\zeta_M^{sp}/p+\mathcal O_K\), up to the Fourier sign convention.
   Thus the Fourier spectrum has full support in
   \(K/\mathcal O_K\).
3. The unnormalized dyadic Haar transform has exactly one nonzero wavelet
   coefficient at every scale.  These coefficients are \(\pm1/p\).  The
   active wavelets form the unique root-to-leaf path ending at \(p\).
4. For a cyclic difference \(\Delta_h\), the Fourier transform of any
   iterated difference is

   \[
   {\zeta_M^{sp}\over p}\prod_r(\zeta_M^{s h_r}-1)
   \]

   up to sign convention.  In particular, an odd shift kills only the zero
   frequency.  Differencing does not create a sparse nonzero-frequency
   spectrum.  The translation-averaged autocorrelation of the rational
   delta is \(p^{-2}\mathbf1_{h=0}\), independent of its location.

For the bit-prefix tree of \(u_t=p^{-1}\bmod2^t\), define a cell by

\[
C_{t,a}=\{j\leq B:j\text{ odd and }j^{-1}\equiv a\pmod {2^t}\}.
\]

The cell sums in \(\mathbb Q/\mathbb Z\) form a delta at \(a=u_t\).
Therefore their Walsh transform has full support under every Boolean
labelling of the odd residue classes.  The time-domain cell indicator is
the arithmetic progression \(j\equiv a^{-1}\pmod {2^t}\).

## Theorem 4: finite 2-adic multiscale consistency is exactly path-blind

Let a binary tree partition \(\{1,\ldots,B\}\).  For every node \(v\), let

\[
s_v=\sum_{j\in v}x_j\pmod {2^t}.
\]

These values are additive from children to parents.  For any proposed leaf
\(\ell\), and any proposed residue \(u\in\mathbb Z/2^t\mathbb Z\), set

\[
c_v^{(\ell,u)}=s_v-u\,\mathbf 1_{\ell\in v}.
\]

Then

\[
c_v^{(\ell,u)}
=c_{v_0}^{(\ell,u)}+c_{v_1}^{(\ell,u)}\pmod {2^t}
\]

at every fork \(v=v_0\sqcup v_1\), for every \(\ell\).  Every residue
\(c_v^{(\ell,u)}\) has an ordinary integer representative.  The true
choice is \((\ell,u)=(p,p^{-1})\), where the representatives are the exact
floors, but finite 2-adic additivity and integer representability do not
select it.  The two possible next lifts of a correct prefix therefore have
exactly the same additive feasibility whenever both corresponding cells are
nonempty.  Throughout P175's sub-quarter precision range, both cells are
nonempty for all sufficiently large inputs.

This is a gauge symmetry of the whole dyadic tree.  An invertible linear
change to Haar or Walsh coordinates cannot remove it.  A selector must add
an Archimedean floor, exact rational integrality, a denominator test, a
nonlinear distribution theorem about the integer parts, or another
non-additive input.

## Theorem 5: exact evaluation boundary

For public integer weights \(w_1,\ldots,w_B\), summation by parts gives

\[
N\sum_{j=1}^{B}w_jx_j
=w_1A_0+
\sum_{j=1}^{B-1}(w_{j+1}-w_j)A_j-w_BA_B.
\]

Thus a weight with \(R\) adjacent changes has an endpoint expression using
at most \(R+2\) signed binomial values.  P173's corrected power-of-two
binomial algorithm evaluates any QP number of these endpoints modulo
\(2^t\) in QP time.  This gives the path-blind values in Theorem 4, not
their ordinary floors.

Contiguous Haar cells have \(O(1)\) changes, but an exact nonzero/support
test on one of them is Theorem 1's gcd and already factors.  A residue-prefix
cell modulo \(2^t\) has \(\Theta(B/2^t)\) isolated runs.  At P175 precision

\[
t=\left\lfloor{\log_2N\over4}\right\rfloor-(\log n)^{O(1)},
\]

this is \(N^{1/4}2^{(\log n)^{O(1)}}\), up to constant factors, and is
exponential in \(n\).  Hence the literal endpoint evaluator does not become
QP.  Uniform coordinate sampling in such a cell hits its sole exceptional
index with probability only
\(\Theta(2^t/B)=N^{-1/4}2^{-(\log n)^{O(1)}}\).  This is an accounting
statement for those evaluators and samplers, not a circuit lower bound.

## Theorem 6: continuous 2-adic tests and exact high-order phases

More generally, let \(M\) be a public modulus and gcd-screen it against
\(N\).  A proper gcd already factors.  On the factor-free unit branch
\(\gcd(M,N)=1\), reduction

\[
\mathbb Z[1/N]\longrightarrow\mathbb Z/M\mathbb Z
\]

maps \(1/p\) to the ordinary residue \(p^{-1}\bmod M\).  Since
\(\mathbb Z\to\mathbb Z/M\mathbb Z\) is surjective, no predicate of this
one residue can distinguish an ordinary integer from an integer plus
\(1/p\).  A finite product of factor-free auxiliary residue rings has the
same boundary.  The case \(N\mid M\), where \(N\) is not a unit, is outside
this claim and contains the original composite-characteristic gate.

The inclusion \(\mathbb Z\to\mathbb Z/2^t\mathbb Z\) is surjective.
Therefore no predicate of one finite 2-adic residue can accept every
ordinary integer and reject \(m+1/p\).  More generally, \(\mathbb Z\) is
dense in \(\mathbb Z_2\), so every continuous function on \(\mathbb Z_2\)
that is constant on \(\mathbb Z\) is constant everywhere.  This covers
value-local convergent Mahler expansions and finite-precision 2-adic
characters.  It does not cover an algorithm that also uses the succinct
rational representation, \(N\), and an Archimedean operation.

An ordinary additive character would be an ideal selector:

\[
\exp(2\pi i mS_I)
=\begin{cases}
1,&p\notin I,\\
\exp(2\pi i m/p),&p\in I.
\end{cases}
\]

For \(|m|\leq Q(n)\), where \(Q\) is numerical QP,

\[
\left|\exp(2\pi i m/p)-1\right|
\leq {2\pi Q(n)\over p}=2^{-\Omega(n)}.
\]

Thus bounded-frequency smooth correlations do not have inverse-QP bias on
this signal.

For random \(m\bmod N\), the active phase has constant separation from one
with constant probability.  But

\[
\exp(2\pi i mS_I)
=\exp(2\pi i mD_I/N),
\]

and for \(\gcd(m,N)=1\), deciding whether this phase is one is exactly the
support test in Theorem 1.  A QP evaluator for these phases on adaptively
chosen dyadic cells would binary-search \(p\) and factor \(N\).

There is one conditional exact 2-adic representation boundary.  Fix a
public integer-valued numerical-QP extension-degree cap \(D(n)\).  Run
P160--P161 from the beta-two normalized hard branch with a roughness
parameter \(T\geq D(n)\).  A factor or a factored exact common-order state
is a separate exit.  Condition only on P161's surviving branch

\[
H=\gcd(w-1,N)=1.
\]

At the same hidden prime \(p\), P161 then gives

\[
\operatorname{ord}_p(w)>T.
\]

The element \(w\) is a public power of two, so

\[
\operatorname{ord}_p(w)\mid\operatorname{ord}_p(2),
\qquad
\operatorname{ord}_p(2)>T\geq D(n).
\]

A finite extension of \(\mathbb Q_2\) containing a primitive \(p\)-th root
of unity has degree at least \(\operatorname{ord}_p(2)\).  Consequently no
extension of degree at most \(D(n)\) contains the active phase on this
specific surviving branch.  This is a conditional representation boundary
only.  It makes no claim on either earlier P160--P161 exit, complex
approximation, or implicit encodings.

## Exact remaining opening

The obstruction leaves one materially new harmonic possibility: prove a
QP-time nonlinear statistic of the *specific integer parts*
\(\lfloor S_I\rfloor\), or a QP-time implicit evaluator of a high-order
phase, that avoids endpoint materialization and has a uniform inverse-QP
lift bias.  Linear additivity, finite 2-adic integrality, bounded-frequency
characters, factor-free auxiliary residue rings, literal residue-cell
materialization, and transform sparsity by themselves do not provide that
statistic.
