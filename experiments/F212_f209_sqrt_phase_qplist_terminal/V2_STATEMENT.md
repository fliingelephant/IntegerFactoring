# F212 V2 candidate — the F209 interval frontier has a square-root phase transition and an \(N^{1/4+\varepsilon}\) QP-list postprocessor

## Status and repair

This is a frozen proof-only V2 candidate. It preserves F212 V1 and its
self-hostile failed audit.

V1's square-root phase results were not challenged. Its terminal theorem,
however, bounded the output-list size without bounding the time needed to
produce that list. V2 repairs the interface exactly:

1. an explicit granted QP-size list is an auxiliary input and has a
   deterministic QP postprocessor; and
2. an end-to-end factoring terminal follows only if a public list generator
   itself runs in numerical QP time.

F211 remains reserved for the dyadic quotient experiment.

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

Let \(m\geq2\) satisfy \(\gcd(m,N)=1\). For a unit residue
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
&P_x^-Q_x^-\leq N\leq P_x^+Q_x^+\}.
\end{aligned}
\]

Multiplication by F207's public root \(R\in U(m)\) bijects its \(u\)-frontier
with this \(x\)-frontier.

## Theorem 1: uniform full-torsor range

If

\[
N\geq1024
\qquad\hbox{and}\qquad
s(m)\leq\frac{\sqrt N}{8},
\]

then

\[
\boxed{\mathcal F_N(m)=U(m)}
\qquad\hbox{and}\qquad
\boxed{|\mathcal F_N(m)|=\varphi(m)}.
\]

Consequently, for every sequence \(N_i\to\infty\) of promised inputs and
coprime \(m_i\) satisfying

\[
\frac{s(m_i)}{\sqrt{N_i}}\longrightarrow0,
\]

the frontier is all of \(U(m_i)\) for all sufficiently large \(i\). Since
\(s(m)\leq2m\), this applies whenever \(m=o(\sqrt N)\).

If \(m=N^{\alpha+o(1)}\) for fixed \(0<\alpha<1/2\), an explicit frontier
has at least

\[
\varphi(m)\geq\sqrt{m/2}=N^{\alpha/2+o(1)}
\]

states, and every unit state passes the declared relaxation.

## Theorem 2: singleton-progression range

Let

\[
W_P=B-L,\qquad W_Q=U-(B+1).
\]

If

\[
\boxed{s(m)>\max\{W_P,W_Q\},}
\]

then each nonempty progression is a singleton and

\[
\boxed{
\mathcal F_N(m)
=\{\,X\bmod m:X\in P,\ N/X\in Q,\ X\mid N\,\}.}
\]

For the promised balanced semiprime this is exactly the ordered branch
\((p,q)\). In particular, \(m/\sqrt N\to\infty\) implies this conclusion for
all sufficiently large inputs.

Thus the only unresolved transition scale for this declared geometry is

\[
\boxed{m=\Theta(\sqrt N).}
\]

This is not a hardness result for that scale.

## Theorem 3: the fully factored \(K\)-modulus is the divisor spike

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

Each summand is \(\mathbf1_{X\mid N}\). The sum equals one on the promised
input, with unique witness \(p\).

Moreover, \(\lfloor N/X\rfloor\) is strictly decreasing for \(L\leq X<B\),
so ordinary equal-quotient grouping has \(\Theta(\sqrt N)\) blocks on this
shell. This is a named boundary for that literal method, not a lower bound
against another exact floor algorithm.

## Theorem 4A: granted-list QP postprocessing

Let

\[
n=\lceil\log_2(N+1)\rceil
\]

and let \(Q(n)\) be a numerical quasipolynomial. Fix a rational
\(\varepsilon>0\).

The input to this theorem is \(N\) together with an explicit auxiliary list

\[
\mathcal L=((m_j,r_j))_{j=1}^{J},
\qquad J\leq Q(n),
\]

encoded in binary, such that for every \(j\),

\[
\gcd(m_j,N)=1,\qquad
N^{1/4+\varepsilon}\leq m_j\leq N^C,\qquad
0\leq r_j<m_j,
\]

where \(C\geq1\) is a fixed integer independent of \(N,j\).

Suppose at least one entry satisfies

\[
p\equiv r_j\pmod{m_j}
\quad\hbox{or}\quad
q\equiv r_j\pmod{m_j}.
\]

Then a deterministic postprocessor factors \(N\) in numerical QP bit
complexity in \(n\). Each binary pair, including self-delimiting field
lengths, uses \(O_C(n)\) bits. The explicit list therefore contains at most

\[
Q(n)\,O_C(n)
\]

bits, so reading and validating its syntax, entry count, bit lengths,
residue ranges, and \(\gcd(m_j,N)=1\) conditions is itself numerical QP.
The algorithm does not need to verify in advance which entry contains a
factor residue.

This theorem is a granted-auxiliary-input result. It makes no claim about
the time required to construct \(\mathcal L\).

For an F207/F209 torsor branch \(u_j\bmod m_j\), the corresponding residue is

\[
r_j=R_j u_j\bmod m_j.
\]

Thus a granted QP-size live-branch list above the threshold is sufficient;
singleton isolation is unnecessary.

## Corollary 4B: end-to-end QP terminal

Suppose there is a deterministic public algorithm \(G\) which, on every
promised input \(N\),

1. runs in numerical QP bit complexity in \(n\);
2. outputs an explicit list satisfying every syntactic, size, modulus, and
   correctness promise of Theorem 4A; and
3. performs no hidden-factor oracle call.

Then composing \(G\) with Theorem 4A factors \(N\) deterministically in
numerical QP bit complexity.

The output bound follows both from the explicit list promise and from the
runtime of \(G\). All list construction, serialization, reading, validation,
Coppersmith, modular-inverse, multiplication, and gcd costs are included.

V2 does not construct \(G\).

## Named boundaries, not lower bounds

### Exact incomplete-Kloosterman expansion

For residue-set indicators \(f,g\) on \(\mathbb Z/m\mathbb Z\),

\[
\sum_{x\in U(m)}f(x)g(Nx^{-1})
=\frac1{m^2}\sum_{a,b\bmod m}
\widehat f(a)\widehat g(b)K_m(a,bN),
\]

where

\[
K_m(A,B)=\sum_{x\in U(m)}e^{2\pi i(Ax+Bx^{-1})/m}.
\]

This exact dense expansion does not itself give a QP exact aggregation of
the interval weights. Approximate square-root-error estimates do not certify
an exact zero or singleton, and the endpoint-product predicate is additional
and nonseparable. These are boundaries for the standard displayed methods,
not lower bounds against a compressed exact evaluator.

### Adaptive CRT component ordering

Every prefix satisfying Theorem 1 has the full unit torsor. Every prefix
satisfying Theorem 2 has reduced the endpoint predicate to exact
divisibility. Reordering alone does not make F209's explicit expansion or
full interval scan QP. This does not exclude an adaptive order coupled to a
compressed state, exact counter, meet-in-the-middle representation, or
nonlinear decoder.

## Exact remaining gap

Construct, in numerical QP time and without enumerating a fixed power of
\(N\), one of:

1. a list generator \(G\) satisfying Corollary 4B;
2. an exact compressed finder or isolating counter in the critical band
   \(m=\Theta(\sqrt N)\); or
3. another integer-specific statistic that bypasses the F209 frontier.

The V2 packet gives no unconditional factoring algorithm.
