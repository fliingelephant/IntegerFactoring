# F214 V2: statement-only blind reconstruction

## Source integrity and scope

Before either permitted source was opened, the SHA-256 digest of
`V2_STATEMENT.md` was verified as

```text
3aa3260154c8f0f7848b5fd5f8f427de41be07c986c044ad3141e32bc1928e97
```

This reconstruction uses only the repository-root `PROMPT.md` and the
hash-verified V2 statement. It reconstructs the claims and their proofs. It
does not claim a numerical-quasipolynomial inverse-box selector, an all-input
factoring algorithm, or a general lower bound.

## Setup

Let

\[
N=pq,\qquad p<q<2p,
\]

where \(p\) and \(q\) are distinct odd primes, and put

\[
n=\lceil\log _2(N+1)\rceil,\qquad
B=\lfloor\sqrt N\rfloor,\qquad
K=\frac{N-1}{2},
\]

\[
E=N-B^2,\qquad M=\operatorname{lcm}(K,E).
\]

The complete factorization of \(K\) is granted. Thus \(K\) is one permitted
choice of a fully factored modulus \(m\mid M\).

Define the finite sets

\[
P=\mathbb Z_{\rm odd}\cap(\sqrt{N/2},\sqrt N),\qquad
Q=\mathbb Z_{\rm odd}\cap(\sqrt N,\sqrt{2N}).
\]

The promise \(p<q<2p\) puts \(p\in P\) and \(q\in Q\): indeed,
\(p<\sqrt N<q\), while \(q<2p\) gives
\(p>\sqrt{N/2}\) and \(q<\sqrt{2N}\).

For \(m\mid M\) and \(a\in U(m)\), set

\[
P_m(a)=\{X\in P:X\equiv a\pmod m\},
\]

\[
Q_m(a)=\{Y\in Q:Y\equiv Na^{-1}\pmod m\}.
\]

A branch is endpoint-live when both sets are nonempty and

\[
\min P_m(a)\min Q_m(a)\le N
\le \max P_m(a)\max Q_m(a). \tag{1}
\]

The representative of \(Na^{-1}\pmod m\) used in \(Q\) is any integer in
that residue class. It need not be the least nonnegative representative.

## 1. Exact collapse at the full modulus

The exact equality is

\[
\boxed{
\{(X,Y)\in\mathbb Z^2:
\sqrt{N/2}<X<\sqrt N<Y<\sqrt{2N},\ XY\equiv N\pmod K\}
=\{(p,q)\}.} \tag{2}
\]

This claim does not require either oddness of \(X,Y\) or the endpoint-live
condition.

To prove it, the box bounds give

\[
\frac{N}{\sqrt2}<XY<\sqrt2N. \tag{3}
\]

Since \(N=2K+1\), the congruence says \(XY=N+tK\) for some integer \(t\).
The nearest other possibilities are

\[
N-K=\frac{N+1}{2}<\frac{N}{\sqrt2}
\]

and

\[
N+K=\frac{3N-1}{2}>\sqrt2N.
\]

Both inequalities hold in the present setup (in particular, \(N\ge15\)).
All choices \(t\le-1\) are no larger than the first excluded value, and all
choices \(t\ge1\) are no smaller than the second. Hence \(t=0\), so
\(XY=N\).

The positive divisors of \(N=pq\) are \(1,p,q,N\). The condition
\(X<\sqrt N<Y\) forces \(X=p\) and \(Y=q\). This proves (2).

It follows in particular that

\[
\boxed{
\{(X,Y)\in P\times Q:Y\equiv NX^{-1}\pmod K\}
=\{(p,q)\}.} \tag{4}
\]

Indeed, multiplying the inverse congruence by \(X\) gives the congruence in
(2). Conversely, \(p\) is a unit modulo \(K\), since a common divisor of
\(p\) and \((pq-1)/2\) would divide \(1\), and \((p,q)\) satisfies the
congruence and lies in \(P\times Q\).

Thus the full-\(K\) inverse-box problem is exactly recovery of the factor
pair. The product-range predicate is redundant at \(m=K\). A known
factorization gives the point, and any returned point gives a nontrivial
factor of \(N\). This is an equivalence, not an algorithm for finding the
point.

## 2. Singleton-step generalization

For any permitted modulus define

\[
s_m=\operatorname{lcm}(2,m).
\]

Suppose

\[
s_m>\max P-\min P,\qquad
s_m>\max Q-\min Q. \tag{5}
\]

Two members of the same \(P_m(a)\) are both odd and are congruent modulo
\(m\). Their difference is therefore divisible by \(2\) and by \(m\), hence
by \(s_m\). Condition (5) makes a nonzero such difference larger than the
diameter of \(P\), which is impossible. Thus every nonempty \(P_m(a)\) is a
singleton. The same proof applies to \(Q_m(a)\).

If the branch is endpoint-live, write its two singleton representatives as
\(X,Y\). Then (1) becomes

\[
XY\le N\le XY,
\]

and consequently

\[
\boxed{XY=N.} \tag{6}
\]

Every endpoint-live branch beyond this singleton threshold therefore
factors \(N\). The conclusion neither locates a live branch nor proves that
a suitable branch can be found efficiently before the threshold.

## 3. Local child sizes and the conditional recursive consequence

Use \(\ell(t)=\lceil\log_2(t+1)\rceil\) for the bit length of a positive
integer. Since

\[
K+1=\frac{N+1}{2},
\]

we have

\[
\ell(K)=\lceil\log_2(N+1)-1\rceil=n-1. \tag{7}
\]

Also \(B^2\le N<(B+1)^2\), so, using integrality,

\[
1\le E=N-B^2\le2B<2\sqrt N.
\]

Therefore

\[
\ell(E)\le \frac n2+O(1). \tag{8}
\]

These are facts about children arising at the current balanced-semiprime
node. They do not preserve the balanced-semiprime promise. In particular,
an inverse-box selector established only under the current setup cannot be
called recursively to factor \(K\).

There is a separate, conditional all-input accounting statement. Assume an
independently correct recursive factoring dispatch on all positive integer
inputs. At each node of bit length at most \(r\), assume that it makes at
most one recursive call on a child of at most \(r-1\) bits and at most
\(Q(r)\) recursive calls on children of at most \(r/2+C_0\) bits. Assume
also that its other work is at most \(Q(r)\) bit operations, where \(C_0\)
is fixed and

\[
Q(r)=2^{C_1(\log_2(r+1))^k}
\]

for fixed \(C_1>0\) and \(k\ge1\). If \(T(r)\) is the maximum cost for an
input of at most \(r\) bits, then

\[
T(r)\le T(r-1)+Q(r)T(r/2+C_0)+Q(r). \tag{9}
\]

This is the P183 recurrence. It is numerical quasipolynomial. To see this,
choose a fixed
\(r_0>2C_0\), enlarge it if necessary to cover all small inputs, and unroll
the \(T(r-1)\) term down to \(r_0\). Monotonicity of \(T\) and \(Q\) gives

\[
T(r)\le T(r_0)+rQ(r)\bigl(T(r/2+C_0)+1\bigr). \tag{10}
\]

After replacing \(T\) by \(T+1\) and absorbing the fixed initial value,
(10) has the form

\[
T(r)+1\le A(r)\bigl(T(r/2+C_0)+1\bigr),
\qquad
\log_2 A(r)=O((\log(r+1))^k). \tag{11}
\]

Iteration uses the sequence \(r_{i+1}=r_i/2+C_0\), which reaches the fixed
base range in \(O(\log(r+1))\) steps. Multiplying the factors in (11) then
gives

\[
\log_2(T(r)+1)=O((\log(r+1))^{k+1}),
\]

or

\[
T(r)\le2^{C_2(\log_2(r+1))^{k+1}} \tag{12}
\]

for a fixed \(C_2\). Hence (9) has the required numerical-QP form.

At a balanced node, a numerical-QP full-\(K\) selector can be charged to
the \(Q(n)\) local-work term once the independently correct all-input
dispatch has factored \(K\). This remains conditional on the all-input
closure. Neither the balanced selector alone nor the recurrence accounting
constructs that closure, and no selector is constructed here.

There is also a logically independent arithmetic-progression terminal. If
a method produces a numerical-QP-size list of residues modulo an integer
\(m\) such that

\[
1<m<N,\qquad \gcd(m,N)=1,
\]

one list member equals \(p\bmod m\), and

\[
m\ge \frac{N^{1/4}}{2^{(\log n)^{O(1)}}}, \tag{13}
\]

then applying the Gao--Feng--Hu--Pan arithmetic-progression terminal cited
by P175 to every list member costs numerical QP in total. This follows
because both
the list length and each terminal invocation have numerical-QP cost, and a
product of numerical-QP bounds is numerical QP. Endpoint-liveness alone
does not certify that a branch residue is \(p\bmod m\). It satisfies the
terminal premise only if it identifies a true factor residue or if the
branch has already become a singleton.

## 4. Literal scans

The number of odd integers in a real interval of length \(L\) is
\(L/2+O(1)\). Therefore

\[
|P|=\frac{1-2^{-1/2}}2\sqrt N+O(1),\qquad
|Q|=\frac{\sqrt2-1}2\sqrt N+O(1). \tag{14}
\]

A literal scan of either balanced interval consequently examines
\(\Theta(\sqrt N)\) candidates.

A literal scan of the full inverse torsor enumerates all of \(U(K)\), so it
has \(\varphi(K)\) candidates. For every positive integer \(K\),

\[
\varphi(K)^2\ge \frac K2. \tag{15}
\]

One elementary proof factors \(K=\prod \ell^e\). Multiplicativity gives

\[
\frac{\varphi(K)^2}{K}
=\prod_{\ell^e\parallel K}\ell^{e-2}(\ell-1)^2.
\]

Every local factor is at least \(1\), except for \(\ell^e=2\), whose factor
is \(1/2\). Thus the product is at least \(1/2\). Since
\(K=(N-1)/2\), (15) yields

\[
\boxed{
\varphi(K)\ge\sqrt{K/2}=\frac12\sqrt{N-1}.} \tag{16}
\]

Equations (14) and (16) count candidates in the named literal scans. They
are not lower bounds on a selector that represents or isolates candidates
implicitly.

## 5. Explicit paired-CRT meet in the middle

Write the granted prime-power factorization as

\[
K=\prod_{i=1}^r k_i,
\qquad \gcd(k_i,k_j)=1\quad(i\ne j).
\]

CRT identifies

\[
U(K)\cong\prod_{i=1}^r U(k_i).
\]

Consider a two-list method that assigns every local unit coordinate to one
of two blocks and explicitly materializes every state in each block. If the
two list cardinalities are \(A\) and \(B\), then

\[
A=\prod_{i\in I}\varphi(k_i),\qquad
B=\prod_{i\notin I}\varphi(k_i),
\]

so

\[
AB=\varphi(K).
\]

Consequently,

\[
\boxed{
\max(A,B)\ge\sqrt{\varphi(K)}
\ge(K/2)^{1/4}=N^{1/4+o(1)}.} \tag{17}
\]

The final asymptotic equality can equally be written
\((K/2)^{1/4}=\Theta(N^{1/4})\). This obstruction applies only to the
two-list representation that explicitly materializes all half states. It
does not apply to compressed or adaptive CRT representations, nor to a
non-list CRT algorithm.

## 6. Sum projection and explicit CRT-MCSS meet in the middle

Because \(N\equiv1\pmod K\), the inverse torsor has the sum projection

\[
\psi_K:U(K)\longrightarrow\mathbb Z/K\mathbb Z,
\qquad \psi_K(u)=u+u^{-1}.
\]

For any \(s\bmod K\), a member of the fiber satisfies

\[
u^2-su+1\equiv0\pmod K. \tag{18}
\]

We first bound this quadratic congruence prime power by prime power. For an
odd prime power \(\ell^e\), multiplication by \(4\) and completion of the
square turn (18) into

\[
(2u-s)^2\equiv s^2-4\pmod{\ell^e}.
\]

The map \(u\mapsto2u-s\) is bijective. A square congruence modulo
\(\ell^e\) has at most \(2\ell^{e/2}\) roots. Indeed, if the target is zero,
the roots are divisible by \(\ell^{\lceil e/2\rceil}\); otherwise its
valuation must be \(2t<e\), after which there are at most two unit roots and
\(\ell^t\) lifts. Thus the local fiber has size at most
\(2\ell^{e/2}\).

For \(2^e\), a nonempty fiber forces \(s\) to be even. Write \(s=2t\).
Then (18) becomes

\[
(u-t)^2\equiv t^2-1\pmod{2^e}.
\]

A square congruence modulo \(2^e\) has at most \(4\,2^{e/2}\) roots. The
same valuation argument applies, with at most four unit square roots at the
remaining odd modulus and \(2^t\) lifts when the target valuation is
\(2t\). This bound also covers a zero target.

CRT multiplies the local root counts. If \(K_{\rm odd}\) is the odd part of
\(K\), this proves the exact finite bound

\[
\boxed{
|\psi_K^{-1}(s)|
\le4\,2^{\omega(K_{\rm odd})}\sqrt K
\le4\,2^{\omega(K)}\sqrt K.} \tag{19}
\]

Partitioning \(U(K)\) into these fibers gives

\[
\boxed{
|\psi_K(U(K))|
\ge\frac{\varphi(K)}{4\,2^{\omega(K)}\sqrt K}.} \tag{20}
\]

For completeness, the asymptotic estimates used here require no
distribution or smoothness hypothesis. If \(t=\omega(K)\), the product of
the \(t\) distinct prime divisors of \(K\) is at least a factorial of order
\(t\). Hence \(t=O(\log K/\log\log K)=o(\log K)\), and

\[
2^{\omega(K)}=K^{o(1)}.
\]

Also

\[
\frac{\varphi(K)}K=\prod_{\ell\mid K}(1-1/\ell)
\ge2^{-\omega(K)}=K^{-o(1)},
\]

so

\[
\varphi(K)=K^{1-o(1)}. \tag{21}
\]

Combining (20) and (21) gives

\[
|\psi_K(U(K))|\ge K^{1/2-o(1)}. \tag{22}
\]

Under CRT, \(\psi_K(U(K))\) is exactly the Cartesian product of the local
sum images. An explicit two-list multiple-choice-subset-sum implementation
partitions those local choices into two blocks. Even after local duplicate
sums are collapsed, its two list sizes \(A,B\) satisfy

\[
AB=|\psi_K(U(K))|.
\]

Thus at least one list has size

\[
\boxed{\max(A,B)\ge K^{1/4-o(1)}.} \tag{23}
\]

This conclusion is confined to an implementation that materializes every
half choice. It is not a lower bound for an implicit MCSS solver or for an
algorithm that exploits additional structure without constructing these
lists.

## 7. Continued-fraction reformulation

By the full-modulus collapse, every inverse-box point satisfies

\[
XY=N=2K+1.
\]

Equivalently,

\[
XY-2K=1,
\qquad
\det\begin{pmatrix}X&K\\2&Y\end{pmatrix}=1. \tag{24}
\]

Conversely, every positive integral solution of (24) obeys

\[
X\mid 2K+1=N,
\qquad Y=N/X. \tag{25}
\]

Therefore finding the balanced determinant-one completion is precisely
finding the nontrivial balanced divisor. The quotient

\[
\frac{XY-1}{K}=2
\]

is fixed and public. It supplies no additional public rational
approximation with a small unknown error to which the usual
continued-fraction recovery theorem can be applied. This argument shows an
equivalence with direct divisor completion. It is not a lower bound against
all algorithms that use continued fractions.

## 8. Range of the direct bivariate Coppersmith theorem

Put

\[
a=B-X,\qquad c=Y-B.
\]

Substitution of \(X=B-a\), \(Y=B+c\), and \(N=B^2+E\) shows that the desired
point is an integral root of

\[
f(a,c)=Bc-Ba-ac-E. \tag{26}
\]

This polynomial is irreducible. A reducible bilinear polynomial has a
rank-one coefficient matrix, hence zero determinant. For (26), the
coefficient matrix for \((ac,a,c,1)\) can be written

\[
\begin{pmatrix}-1&-B\\ B&-E\end{pmatrix},
\]

whose determinant is

\[
E+B^2=N\ne0.
\]

Bounds that cover the complete balanced box have

\[
A=\Theta(\sqrt N),\qquad
C=\Theta(\sqrt N),\qquad
AC=\Theta(N). \tag{27}
\]

Indeed, the available ranges for \(B-X\) and \(Y-B\) each have a fixed
positive-constant multiple of \(\sqrt N\) as their full width, up to
additive \(O(1)\).

For the standard scaled height

\[
W=\|f(Ax,Cy)\|_\infty,
\]

the coefficients are \(BC,-BA,-AC,-E\). Equations (27),
\(B=\Theta(\sqrt N)\), and \(E=O(\sqrt N)\) imply

\[
W=\Theta(N).
\]

The proved direct bivariate Coppersmith guarantee for separate degree
\(\delta=1\) requires

\[
AC<W^{2/3}
\]

with its stated constant or epsilon slack. Here instead

\[
\boxed{AC=\Theta(W).} \tag{28}
\]

The ratio between the present product bound and the theorem scale is
\(\Theta(W^{1/3})=\Theta(N^{1/3})\). Thus the sufficient theorem condition
fails by a power, not by a constant. This proves only that the published
direct theorem does not apply on the complete box. It is not a lattice
lower bound and says nothing against factor-aware, nonstandard, or newly
proved lattice constructions outside that theorem.

## 9. Termwise additive Fourier and Kloosterman expansions

Assume \(K\) is odd, which is the case on the branch \(N\equiv3\pmod4\).
For

\[
\mathcal A=\{a+2j:0\le j<L\}\subset\mathbb Z/K\mathbb Z,
\qquad1\le L<K,
\]

the Fourier coefficient at frequency \(t\) is, up to a nonzero phase,

\[
\sum_{j=0}^{L-1}\exp(2\pi i\,2tj/K). \tag{29}
\]

At \(t=0\), this equals \(L\). Since \(2\) is a unit modulo odd \(K\), a
nonzero frequency vanishes exactly when

\[
K\mid tL.
\]

There are \(\gcd(K,L)\) frequencies satisfying this divisibility, one of
which is \(t=0\), where the sum does not vanish. Hence the exact number of
nonzero Fourier frequencies is

\[
\boxed{K-\gcd(K,L)+1,} \tag{30}
\]

which is at least \(K-L+1\).

The actual \(P\) and \(Q\) intervals are progressions of consecutive odd
integers with

\[
L=\Theta(\sqrt N)=o(K).
\]

Their transforms therefore each have \(K-o(K)\) nonzero modes. A Fourier
or incomplete-Kloosterman formula that uses both transforms still has
\(K-o(K)\) frequencies in the intersection of their nonzero supports. Thus
an implementation that explicitly materializes and processes the nonzero
modes one by one has \(\Omega(K)\) terms.

This is a termwise-materialization boundary, and it is restricted to odd
\(K\). It does not cover an implicit exact transform, closed-form
cancellation, fast multipoint evaluation, compressed summation, or another
non-termwise evaluator.

## Exact consequence and remaining scope

At \(m=K\), the inverse-box point is the factor pair itself, rather than a
weaker surrogate. The following named routes do not yield numerical-QP
localization at this scale for the precise, limited reasons proved above:

1. the two direct balanced scans have \(\Theta(\sqrt N)\) candidates;
2. the explicit unit scan has \(\varphi(K)=\Omega(\sqrt N)\) candidates;
3. explicit paired-CRT meet in the middle has a list of size at least
   \((K/2)^{1/4}\);
4. explicit CRT-MCSS meet in the middle has a list of size
   \(K^{1/4-o(1)}\);
5. determinant-one continued-fraction completion is the original divisor
   completion, with no new public approximation datum;
6. the published direct bivariate Coppersmith sufficient range misses the
   full box by a power; and
7. on odd \(K\), a termwise Fourier or incomplete-Kloosterman expansion has
   \(\Omega(K)\) nonzero terms.

None of these statements is a lower bound on the inverse-box problem as a
whole. In particular, they leave open:

1. compressed exact counting or isolation in adaptive subboxes;
2. an implicit CRT or MCSS representation that never materializes the
   bounded lists;
3. a non-termwise exact Kloosterman or Fourier evaluator;
4. a lattice theorem beyond the direct bivariate Coppersmith range; and
5. a new integer-specific Archimedean selector before full disclosure.

Finally, the local sizes of \(K\) and \(E\), and the recurrence that would
account for them, do not close the factoring problem. The recurrence
conclusion requires an independently correct all-input recursive dispatch.
The arithmetic-progression terminal separately requires a list containing
an actual factor residue at a sufficiently large coprime modulus. The
balanced-semiprime setup alone supplies neither missing ingredient.
