# F197: the factorial gate in explicit block, BGS, lift, and quotient models

Status: frozen literature-dependent proof-only candidate.

## Scope

Let

\[
N=pq,
\qquad p<q<2p,
\]

where \(p\) and \(q\) are distinct odd primes. Put

\[
n=\left\lceil\log_2(N+1)\right\rceil,
\qquad B=\lfloor\sqrt N\rfloor,
\qquad F=B!.
\tag{1}
\]

All bit-complexity statements use the deterministic multitape Turing model.
“Numerical QP” means quasipolynomial in the input bit length \(n\).

F197 gives exact boundaries for named representations and published
algorithms. It is not a lower bound for general arithmetic circuits, modular
factorial evaluation, or integer factoring.

## Theorem 1: the exact-division route reaches the factorial gcd first

The balanced promise gives

\[
p\le B<q,
\qquad B<2p,
\qquad v_p(F)=1,
\qquad v_q(F)=0.
\tag{2}
\]

Consequently,

\[
\gcd(F,N)=p,
\qquad
\gcd(F,N^2)=p.
\tag{3}
\]

Let

\[
D=\prod_{j=1}^{B}(N-j)
 =F\binom{N-1}{B}.
\tag{4}
\]

Then also

\[
\gcd(D,N)=p,
\qquad
\gcd(D,N^2)=p.
\tag{5}
\]

Thus a route that first materializes the exact denominator \(F\), the exact
numerator \(D\), or either canonical residue modulo \(N\) or \(N^2\), has
already obtained a factor-bearing gcd before performing the exact division
\(D/F\). This statement does not cover a compressed algorithm that never
materializes any of these values.

## Theorem 2: explicit one-width block schemes have a square-root balance

Fix an integer \(1\le u\le B\). Consider the explicit dense block scheme
that materializes the coefficient vector of

\[
P_u(X)=\prod_{j=1}^{u}(X+j)
\tag{6}
\]

and then materializes one block value for each of the
\(\lceil B/u\rceil\) consecutive blocks needed to cover \(1,\ldots,B\).
Even before polynomial multiplication and evaluation costs are charged, the
scheme exposes at least

\[
u+\left\lceil\frac Bu\right\rceil
\ge u+\frac Bu
\ge2\sqrt B
\tag{7}
\]

nonconstant coefficient/value positions. Hence this explicitly defined
model has \(\Omega(\sqrt B)\) work or output positions for every block
width. Since \(B=2^{\Theta(n)}\), this is exponential in \(n\).

The conclusion is only about the stated dense coefficient-and-block-value
representation. It is not an arithmetic-circuit lower bound.

## Theorem 3: the published BGS/holonomic route has the same upper scale

The factorial sequence is the scalar holonomic recurrence

\[
U_0=1,
\qquad U_k=kU_{k-1}.
\tag{8}
\]

Bostan, Gaudry, and Schost prove that a factorial of length \(L\) can be
computed in an arbitrary ring by a baby-step/giant-step method in

\[
O\!\left(\mathsf M_R(\sqrt L)\log L\right)
\tag{9}
\]

ring operations, and their refined recurrence algorithms remove
polylogarithmic factors under their stated hypotheses. Here
\(\mathsf M_R(d)\) is the cost of degree-\(d\) polynomial multiplication
over the ring.

For \(L=B\) and \(R=\mathbb Z/N\mathbb Z\), this is a
\(B^{1/2+o(1)}\operatorname{poly}(n)\) bit upper bound under fast
arithmetic. As \(B=\Theta(\sqrt N)\), its scale is

\[
N^{1/4+o(1)}=2^{\Theta(n)},
\tag{10}
\]

not numerical QP. Costa and Harvey place the same construction in the
multitape Turing bit model and improve the complete deterministic
factorization bound by a factor of \(\sqrt{\log\log N}\); this changes no
power of \(N\).

Equations (9) and (10) are published upper bounds. F197 does not infer a
lower bound for every holonomic or factorial algorithm from them.

## Theorem 4: modular division and its lifts

Write \(F=pU\), where \(\gcd(U,N)=1\). Multiplication by \(F\) modulo
\(N\) satisfies

\[
Fx\equiv Fy\pmod N
\quad\Longleftrightarrow\quad
x\equiv y\pmod q.
\tag{11}
\]

Thus cancellation by \(F\) modulo \(N\) loses the full \(p\)-component;
\(F\) is not a unit.

Modulo \(N^2\),

\[
Fx\equiv Fy\pmod {N^2}
\quad\Longleftrightarrow\quad
pq^2\mid x-y.
\tag{12}
\]

The map on all of \(\mathbb Z/N^2\mathbb Z\) still has a kernel of size
\(p\), although its restriction to canonical inputs \(0\le x<N\) is
injective. Ordinary inverse-based modular division is unavailable at both
levels, and computing the denominator residue needed for such a division
exposes \(p\) by (3). This is an exact nonunit-division boundary, not a
lower bound against a custom restricted-domain decoder.

Let

\[
F=NQ+R,
\qquad Q=\left\lfloor\frac FN\right\rfloor,
\qquad 0\le R<N.
\tag{13}
\]

Then \(\gcd(R,N)=p\). If

\[
a_2=F\bmod N^2,
\qquad 0\le a_2<N^2,
\tag{14}
\]

the exact base-\(N\) digits are

\[
a_2=R+N(Q\bmod N),
\qquad
R=a_2\bmod N,
\qquad
Q\bmod N=\left\lfloor\frac{a_2}{N}\right\rfloor.
\tag{15}
\]

Therefore a full lift modulo \(N^2\) contains a quotient digit, but its low
digit already factors \(N\).

## Theorem 5: exact output is too large, but quotient bits are a precise gate

The exact integers \(F\), \(D\), and, outside finitely many small inputs,
\(Q\) have \(2^{\Theta(n)}\) bits. Any sequential bit algorithm that
materializes one of them takes exponential time from output size alone.
This says nothing about a residue-only algorithm.

The power-of-two residue

\[
f_2=F\bmod2^n
\tag{16}
\]

is computable in deterministic polynomial time. Therefore the single
\(n\)-bit quotient residue

\[
Q_2=Q\bmod2^n
\tag{17}
\]

is a sufficient factoring primitive: compute

\[
R=\left(f_2-NQ_2\right)\bmod2^n.
\tag{18}
\]

Because the true remainder satisfies \(0<R<N<2^n\), the canonical residue
in (18) is the exact \(R\), and \(\gcd(R,N)=p\).

Equivalently, if

\[
a=F\bmod(N2^n),
\qquad 0\le a<N2^n,
\tag{19}
\]

then

\[
a=R+NQ_2,
\qquad
Q_2=\left\lfloor\frac aN\right\rfloor.
\tag{20}
\]

F197 proves only that (17) is sufficient. It does not prove that factoring
allows (17) to be evaluated in numerical QP time.

## Theorem 6: one-child recursion is explicitly allowed

If a recursion has one surviving child and satisfies

\[
T(m)\le T(m-1)+\operatorname{QP}(m),
\tag{21}
\]

then \(T(m)\) is quasipolynomial. Fixed-ratio contraction is not necessary
for a single chain.

This correction does not rescue the named factorial methods above. The
explicit block model already has \(\Omega(\sqrt B)\) work at the root, and
the published BGS/Costa--Harvey bounds at that root are exponential in
\(n\). F197 makes no claim against a different QP per-node primitive used
along a one-child chain.
