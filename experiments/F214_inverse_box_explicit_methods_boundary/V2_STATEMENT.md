# F214 V2 candidate — the full inverse box is the factor pair, while explicit representations remain exponential

## Status

This is a frozen, self-audited, proof-only V2 candidate. It preserves F214
V1 and its hostile FAIL byte-for-byte. V1's mathematical collapse and named
explicit-method boundaries survive. V2 repairs the failed recursive
consequence by separating local child-size facts from an independently
granted all-input recursive dispatch. It also corrects the V1 manifest's
summary of the unit-scan cardinality.

This packet is not a numerical-QP inverse-box algorithm, not a general lower
bound, and not an all-input factoring algorithm.

## Setup

Let

\[
N=pq,
\qquad p<q<2p,
\qquad n=\lceil\log _2(N+1)\rceil,
\]

where \(p,q\) are distinct odd primes. Put

\[
B=\lfloor\sqrt N\rfloor,
\qquad K=\frac{N-1}{2},
\qquad E=N-B^2,
\qquad M=\operatorname{lcm}(K,E).
\]

The full factorization of \(K\) is granted. This is a permitted special case
of a fully factored modulus \(m\mid M\). Define the balanced integer sets

\[
P=\mathbb Z_{\rm odd}\cap(\sqrt{N/2},\sqrt N),
\qquad
Q=\mathbb Z_{\rm odd}\cap(\sqrt N,\sqrt{2N}).
\]

For \(m\mid M\) and \(a\in U(m)\), define

\[
P_m(a)=\{X\in P:X\equiv a\pmod m\},
\]

\[
Q_m(a)=\{Y\in Q:Y\equiv Na^{-1}\pmod m\}.
\]

A branch is *endpoint-live* when both sets are nonempty and

\[
\min P_m(a)\min Q_m(a)\leq N
\leq\max P_m(a)\max Q_m(a).
\tag{1}
\]

This is the F209 balanced product-range predicate. A representative of
\(Na^{-1}\bmod m\) in \(Q\) means any integer in that residue class, not
necessarily the least nonnegative representative.

## Theorem

### 1. Exact full-\(K\) collapse

Even without oddness or the endpoint condition,

\[
\boxed{
\{(X,Y)\in\mathbb Z^2:
\sqrt{N/2}<X<\sqrt N<Y<\sqrt{2N},\ XY\equiv N\pmod K\}
=\{(p,q)\}.}
\tag{2}
\]

In particular,

\[
\boxed{
\{(X,Y)\in P\times Q: Y\equiv NX^{-1}\pmod K\}
=\{(p,q)\}.}
\tag{3}
\]

Thus the full-modulus inverse-box task on this promise is exactly the task of
recovering the factor pair. The product-range test is redundant at \(m=K\).
Knowing the factorization \(N=pq\) gives the point, and any returned point
factors \(N\).

### 2. Singleton-step generalization

Let

\[
s_m=\operatorname{lcm}(2,m).
\]

If

\[
s_m>\max P-\min P,
\qquad
s_m>\max Q-\min Q,
\tag{4}
\]

then every nonempty \(P_m(a)\) and \(Q_m(a)\) is a singleton. Every
endpoint-live branch then has representatives \(X,Y\) satisfying

\[
\boxed{XY=N.}
\tag{5}
\]

Hence every such branch factors \(N\). This statement does not say how to
find a live branch before the singleton threshold.

### 3. Local child sizes and conditional all-input accounting

At the current balanced-semiprime node, \(K\) has at most \(n-1\) bits and
\(E\) has at most \(n/2+O(1)\) bits. These are local size facts only. The
balanced-semiprime promise need not hold for \(K\), so a selector proved only
under the present setup cannot be invoked recursively on \(K\).

Independently, suppose there is a correct recursive factoring dispatch on
all positive integer inputs. Suppose that at every node of bit length at
most \(r\), its immediate recursive calls consist of at most one child of at
most \(r-1\) bits and at most \(Q(r)\) children of at most \(r/2+C\) bits.
Suppose it also performs at most \(Q(r)\) additional bit operations, where
\(C\) is fixed and \(Q\) is numerical QP. If \(T(r)\) is the maximum cost on
inputs of at most \(r\) bits, then its worst-case time satisfies the P183
recurrence

\[
T(r)\leq T(r-1)+Q(r)T(r/2+C)+Q(r),
\tag{6}
\]

and is numerical QP.

For a balanced node, a numerical-QP full-\(K\) selector may be included in
the \(Q(n)\) local-work term after the independently correct all-input
dispatch has factored \(K\). This accounting conclusion is conditional on
that all-input closure. It is not implied by the balanced-semiprime selector
alone. In particular, it does not construct the missing selector or the
all-input dispatch.

Independently, suppose a method produces a numerical-QP-size list of
residues modulo an integer \(1<m<N\) with \(\gcd(m,N)=1\), one of which is
\(p\bmod m\), and

\[
m\geq \frac{N^{1/4}}{2^{(\log n)^{O(1)}}}.
\tag{7}
\]

Applying the Gao--Feng--Hu--Pan arithmetic-progression terminal cited by
P175 to every list element is numerical QP. A merely endpoint-live branch
does not meet this premise unless it identifies a true factor residue or
has already reached the singleton case.

### 4. Direct scans

The two literal balanced scans have

\[
|P|=\frac{1-2^{-1/2}}2\sqrt N+O(1),
\qquad
|Q|=\frac{\sqrt2-1}2\sqrt N+O(1).
\tag{8}
\]

Thus scanning either interval costs \(\Theta(\sqrt N)\) candidates. An
explicit scan of the full inverse torsor costs \(\varphi(K)\) candidates,
and

\[
\boxed{\varphi(K)\geq\sqrt{K/2}=\frac12\sqrt{N-1}.}
\tag{9}
\]

These are cardinalities of literal scans, not lower bounds against an
implicit selector.

### 5. Explicit paired-CRT meet in the middle

Write the known prime-power factorization as

\[
K=\prod_{i=1}^r k_i,
\qquad \gcd(k_i,k_j)=1\quad(i\neq j).
\]

An explicit two-list CRT method that assigns every local unit coordinate to
one of two blocks has list cardinalities \(A,B\) with

\[
AB=\varphi(K).
\]

Therefore

\[
\boxed{
\max(A,B)\geq\sqrt{\varphi(K)}
\geq(K/2)^{1/4}=N^{1/4+o(1)}.}
\tag{10}
\]

This applies only when all half states are explicitly materialized. It does
not cover compressed, adaptive, or non-list CRT algorithms.

### 6. Sum projection and explicit CRT-MCSS meet in the middle

Since \(N\equiv1\pmod K\), define

\[
\psi_K:U(K)\longrightarrow\mathbb Z/K\mathbb Z,
\qquad
\psi_K(u)=u+u^{-1}.
\]

For every \(s\bmod K\), the exact finite bound

\[
\boxed{
|\psi_K^{-1}(s)|
\leq4\,2^{\omega(K_{\rm odd})}\sqrt K
\leq4\,2^{\omega(K)}\sqrt K}
\tag{11}
\]

holds, where \(K_{\rm odd}\) is the odd part of \(K\). Consequently

\[
\boxed{
|\psi_K(U(K))|
\geq
\frac{\varphi(K)}{4\,2^{\omega(K)}\sqrt K}.}
\tag{12}
\]

The standard estimates

\[
\varphi(K)=K^{1-o(1)},
\qquad
2^{\omega(K)}=K^{o(1)}
\tag{13}
\]

make (12)

\[
|\psi_K(U(K))|\geq K^{1/2-o(1)}.
\tag{14}
\]

The little-\(o\) is only an asymptotic restatement of the explicit bound
(12); it is not a smoothness or randomness assumption.

Under CRT, the global sum image is the Cartesian product of the local sum
images. Therefore an explicit two-list multiple-choice-subset-sum (MCSS)
implementation that materializes every half choice has a list of size at
least

\[
\boxed{K^{1/4-o(1)}.}
\tag{15}
\]

This does not lower-bound an implicit MCSS solver or an algorithm that uses
more structure than explicit half-list materialization.

### 7. Continued-fraction reformulation

At the full modulus, every box point obeys

\[
XY-2K=1,
\qquad
\det\begin{pmatrix}X&K\\2&Y\end{pmatrix}=1.
\tag{16}
\]

Conversely, every positive solution of (16) is a divisor pair

\[
X\mid 2K+1=N,
\qquad Y=N/X.
\tag{17}
\]

Thus selecting the balanced determinant-one completion is exactly selecting
the nontrivial balanced divisor. The quotient \((XY-1)/K\) is the fixed
public integer \(2\); it supplies no separate public rational approximation
to which the usual continued-fraction small-error theorem can be applied.
This is an equivalence of the direct completion formulation, not a lower
bound against every algorithm using continued fractions.

### 8. Direct bivariate Coppersmith theorem range

Put

\[
a=B-X,
\qquad c=Y-B.
\]

The desired point is an integer root of the irreducible polynomial

\[
f(a,c)=Bc-Ba-ac-E.
\tag{18}
\]

On the complete balanced box, the variable bounds \(A,C\) satisfy

\[
A=\Theta(\sqrt N),
\qquad C=\Theta(\sqrt N),
\qquad AC=\Theta(N).
\tag{19}
\]

For the standard scaled height

\[
W=\|f(Ax,Cy)\|_\infty,
\]

one has \(W=\Theta(N)\). The proved direct bivariate Coppersmith guarantee
for separate degree \(\delta=1\) is in the range
\(AC<W^{2/3}\), with the theorem's stated constant or epsilon slack. Here

\[
\boxed{AC=\Theta(W),}
\tag{20}
\]

so this sufficient condition fails by a power \(N^{1/3}\). This is only
theorem-range nonapplicability. It is not a lattice lower bound, and it does
not cover factor-aware, nonstandard, or newly proved lattice constructions.

### 9. Termwise additive Fourier or Kloosterman expansion

Assume \(K\) is odd, as on the \(N\equiv3\pmod4\) branch. Let

\[
\mathcal A=\{a+2j:0\leq j<L\}\subset\mathbb Z/K\mathbb Z,
\qquad 1\leq L<K.
\]

Its discrete Fourier transform has exactly

\[
K-\gcd(K,L)+1
\tag{21}
\]

nonzero frequencies, and hence at least \(K-L+1\). The actual \(P\) and
\(Q\) progressions satisfy \(L=\Theta(\sqrt N)=o(K)\), so each has
\(K-o(K)\) nonzero modes.

Therefore a Fourier or incomplete-Kloosterman formula that explicitly
materializes and processes the nonzero modes term by term has
\(\Omega(K)\) terms. This does not cover an implicit exact transform,
closed-form cancellation, fast multipoint evaluation, or any other
compressed summation. The statement is restricted to odd \(K\).

## Exact consequence and open scope

At \(m=K\), the inverse-box point is not a weaker surrogate for the factors:
it is the factor pair itself. The direct scan, explicit unit scan, explicit
paired CRT, explicit CRT-MCSS half lists, direct continued-fraction
completion, the published direct bivariate Coppersmith guarantee, and
termwise Fourier expansion do not give numerical-QP localization at this
scale for the exact reasons above.

This packet leaves open a numerical-QP algorithm based on, among other
possibilities:

1. compressed exact counting or isolation in adaptive subboxes;
2. an implicit CRT or MCSS representation that never materializes the
   stated lists;
3. a non-termwise exact Kloosterman or Fourier evaluator;
4. a lattice theorem outside the direct bivariate Coppersmith range; or
5. a new integer-specific Archimedean selector before full disclosure.

In particular, the packet proves no lower bound against the requested
inverse-box problem as a whole.
