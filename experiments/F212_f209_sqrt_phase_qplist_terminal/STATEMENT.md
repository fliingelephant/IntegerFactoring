# F212 candidate — the F209 interval frontier has a square-root phase transition and an \(N^{1/4+\varepsilon}\) QP-list terminal

## Status and scope

This is a frozen, self-audited, proof-only candidate. It formalizes the
implicit problem left by F209-D01. It proves:

1. an explicit uniform sub-square-root range in which every unit residue is
   live under the exact F209 interval relaxation;
2. an exact singleton-progression range in which the F209 product test is
   the original divisor event;
3. an exact reduction at the fully factored child
   \(K=(N-1)/2\) to the divisor-jump sum from P184; and
4. a positive terminal: a quasipolynomial-size list containing the correct
   factor residue modulo any \(m\geq N^{1/4+\varepsilon}\) suffices to factor
   \(N\) in quasipolynomial time by the standard univariate
   unknown-divisor Coppersmith theorem.

The result is specific to the integer intervals and endpoint product test
used by F209. It is not a lower bound against compressed modular-hyperbola
algorithms, exact incomplete-Kloosterman evaluators, nonlinear floor
aggregates, adaptive CRT algorithms, or factoring itself.

F211 is reserved for the dyadic quotient experiment. This packet uses F212.

## Setup

Let

\[
N=pq,\qquad p<q<2p,
\]

where \(p,q\) are distinct odd primes. Put

\[
B=\lfloor\sqrt N\rfloor,\qquad
L=\left\lfloor\sqrt{\lfloor N/2\rfloor}\right\rfloor+1,\qquad
U=\lfloor\sqrt{2N-1}\rfloor.
\]

The exact F209 factor intervals are

\[
P=[L,B]\cap(2\mathbb Z+1),\qquad
Q=[B+1,U]\cap(2\mathbb Z+1).
\]

Let \(m\geq1\) satisfy \(\gcd(m,N)=1\). Every F209 prefix modulus has this
property after its public \(\gcd(E,N)\) exit. For a unit residue
\(z\bmod m\) and an integer interval \(I\), define

\[
\mathcal A_m(z;I)
=\{Z\in I\cap(2\mathbb Z+1):Z\equiv z\pmod m\}.
\]

If nonempty, this is an arithmetic progression of step

\[
s=s(m)=\operatorname{lcm}(2,m).
\]

Write its first and last members as \(A_m^-(z;I)\) and
\(A_m^+(z;I)\). For \(x\in U(m)=(\mathbb Z/m\mathbb Z)^\times\), put

\[
y_x=Nx^{-1}\pmod m.
\]

Define the exact F209 relaxed frontier in \(x\)-coordinates by

\[
\begin{aligned}
\mathcal F_N(m)=\{x\in U(m):{}&
\mathcal A_m(x;[L,B])\neq\varnothing,\\
&\mathcal A_m(y_x;[B+1,U])\neq\varnothing,\\
&P_x^-Q_x^-\leq N\leq P_x^+Q_x^+\},
\end{aligned}
\]

where the four endpoints come from the two displayed progressions.
Multiplication by F207's public root \(R\in U(m)\) bijects its \(u\)-frontier
with this \(x\)-frontier, so their cardinalities and pruning behavior are
identical.

## Theorem 1: a uniform full-torsor range

If

\[
N\geq1024
\qquad\hbox{and}\qquad
s(m)\leq\frac{\sqrt N}{8},
\]

then

\[
\boxed{\mathcal F_N(m)=U(m).}
\]

Thus the exact live count is the public number

\[
\boxed{|\mathcal F_N(m)|=\varphi(m).}
\]

In particular, for every sequence of promised inputs \(N_i\to\infty\) and
coprime moduli \(m_i\) satisfying

\[
\frac{s(m_i)}{\sqrt{N_i}}\longrightarrow0,
\]

there is an \(i_0\) such that

\[
\mathcal F_{N_i}(m_i)=U(m_i)
\qquad(i\geq i_0).
\]

Since \(s(m)\leq2m\), the same conclusion holds whenever
\(m=o(\sqrt N)\). If \(m=N^{\alpha+o(1)}\) for a fixed
\(0<\alpha<1/2\), then an explicit frontier contains at least

\[
\varphi(m)\geq\sqrt{m/2}=N^{\alpha/2+o(1)}
\]

states. More importantly, neither its count nor an arbitrary live state
identifies the hidden factor: every unit state is live.

## Theorem 2: the singleton-progression range

Let

\[
W_P=B-L,\qquad W_Q=U-(B+1).
\]

If

\[
\boxed{s(m)>\max\{W_P,W_Q\},}
\]

then each nonempty progression in the definition of
\(\mathcal F_N(m)\) is a singleton. Consequently

\[
\boxed{
\mathcal F_N(m)
=\{\,X\bmod m:X\in P,\ N/X\in Q,\ X\mid N\,\}.}
\]

For the promised balanced semiprime this set contains exactly the ordered
branch \(X=p,\ Y=q\).

In particular, for every sequence with

\[
\frac{m_i}{\sqrt{N_i}}\longrightarrow\infty,
\]

the singleton conclusion holds for all sufficiently large \(i\), because
\(s(m_i)\geq m_i\) and \(W_P,W_Q=O(\sqrt{N_i})\).

Thus the exponent ranges below and above \(1/2\) have different exact
meanings. The only unresolved transition scale for the declared geometry is

\[
\boxed{m=\Theta(\sqrt N).}
\]

This is a phase statement about F209's relaxation, not a hardness result for
the transition scale.

## Theorem 3: the fully factored \(K\)-modulus is exactly the divisor spike

Put

\[
K=\frac{N-1}{2}.
\]

Then \(\gcd(K,N)=1\), and for every \(X\in P,\ Y\in Q\),

\[
XY\equiv N\pmod K
\quad\Longleftrightarrow\quad
XY=N.
\]

Therefore

\[
\boxed{
|\mathcal F_N(K)|
=\sum_{X=L}^{B}
\left(
\left\lfloor\frac NX\right\rfloor
-\left\lfloor\frac{N-1}{X}\right\rfloor
\right).}
\]

Every summand is \(\mathbf1_{X\mid N}\). Even \(X\) contribute zero because
\(N\) is odd, so the displayed unrestricted integer sum equals the odd
frontier count. On the promised input it equals one and its unique witness is
\(p\).

The ordinary quotient partition does not compress this particular shell:
\(\lfloor N/X\rfloor\) is strictly decreasing for
\(L\leq X<B\), so it has \(\Theta(\sqrt N)\) distinct values there. This
classifies only literal termwise evaluation and standard equal-quotient
grouping. It is not a lower bound against another exact floor algorithm.

## Theorem 4: a QP residue list above \(N^{1/4+\varepsilon}\) terminates the branch

Let \(n=\lceil\log_2(N+1)\rceil\), and let \(Q(n)\) be a numerical
quasipolynomial. Fix \(\varepsilon>0\). Suppose a public procedure outputs at
most \(Q(n)\) pairs

\[
(m_j,r_j),\qquad 1\leq j\leq Q(n),
\]

such that

\[
\gcd(m_j,N)=1,\qquad
N^{1/4+\varepsilon}\leq m_j\leq N^{O(1)},\qquad
0\leq r_j<m_j,
\]

and for at least one index \(j\),

\[
p\equiv r_j\pmod{m_j}
\quad\hbox{or}\quad
q\equiv r_j\pmod{m_j}.
\]

Then \(N\) can be factored deterministically in numerical QP time, assuming
the standard deterministic polynomial-time lattice-reduction formulation of
the univariate unknown-divisor Coppersmith theorem.

For an F207/F209 branch \(u_j\bmod m_j\), take

\[
r_j=R_j u_j\bmod m_j.
\]

Hence a QP-size list of live torsor branches at any modulus above the stated
threshold is already a complete terminal. Singleton isolation is not
required.

The theorem does not construct the list. In particular, Theorem 1 proves
that the current F209 interval relaxation returns the whole unit group
through a uniform sub-square-root range.

## Named boundaries, not lower bounds

### Exact incomplete-Kloosterman expansion

For residue-set indicators \(f,g\) on \(\mathbb Z/m\mathbb Z\), the count

\[
C=\sum_{x\in U(m)}f(x)g(Nx^{-1})
\]

has the exact Fourier expansion

\[
C=\frac1{m^2}\sum_{a,b\bmod m}
\widehat f(a)\widehat g(b)
K_m(a,bN),
\]

where

\[
K_m(A,B)=\sum_{x\in U(m)}e^{2\pi i(Ax+Bx^{-1})/m}.
\]

Factoring \(m\) gives standard multiplicative access to complete local sums,
but this displayed expansion does not itself give a QP exact aggregation of
the interval weights. Square-root-error distribution estimates cannot
certify an exact zero or singleton. The product-endpoint predicate is an
additional nonseparable condition. These observations delimit the standard
dense Fourier and approximation routes only; they prove no lower bound
against an exact compressed Kloosterman algorithm.

### Adaptive CRT component ordering

Every prefix satisfying Theorem 1 has the full unit torsor. Every prefix
satisfying Theorem 2 has reduced the endpoint predicate to exact divisibility.
Therefore merely reordering components does not make F209's two explicit
generators QP: explicit CRT expansion stores the live unit states, while its
fallback scans \(\Theta(\sqrt N)\) interval representatives. A jump across the
transition still requires an implicit solver for the new child frontier.

This is a boundary for the declared explicit expansion/scan construction.
It does not exclude an adaptive order coupled to a new compressed state,
meet-in-the-middle representation, exact counter, or nonlinear decoder.

## Exact remaining gap

Construct, without enumerating a fixed power of \(N\), one of:

1. a QP-size list containing the correct branch at some
   \(m\geq N^{1/4+\varepsilon}\);
2. an exact compressed finder or isolating counter in the critical band
   \(m=\Theta(\sqrt N)\); or
3. another integer-specific statistic that bypasses the F209 endpoint
   frontier.

The packet gives no unconditional factoring algorithm.
