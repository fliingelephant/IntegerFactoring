# F137 proof — cross-star recenter-or-descend law

## 1. Canonical parent and child positions

Because \(q<N/C\) and \(\ell\le C\), the parent left endpoint satisfies

\[
\ell q<N.
\]

Also, \(0\le A<\ell\) and \(w<N\), so

\[
0<H=w+AN<\ell N.
\]

The congruence in the setup makes \(H/\ell\) a positive integer below
\(N\). Hence \((\ell q,H/\ell)\) is a canonical inverse pair and

\[
(\ell q)(H/\ell)=qH=V<N^2.
\]

For a child anchor \(a\le C\), the bound \(r<N/C\) gives \(ar<N\).
The induced digit satisfies \(0\le b_a<a\), so

\[
0<t+b_aN<aN.
\]

Therefore \(H'_{b_a}/a\) is a positive integer below \(N\), and the child
endpoint pair is canonical.

## 2. Canonical divisor carry

From (2)--(3),

\[
r(qS)=V\equiv1\pmod N.
\]

The integer \(H=w+AN\) is a unit modulo \(N\), so each divisor \(r,S\) is
also a unit modulo \(N\). Thus \(qS\) is a unit. Its Euclidean remainder
\(t\) in (4) satisfies \(1\le t<N\). Reduction of (4) modulo \(N\) gives

\[
rt\equiv r(qS)\equiv1\pmod N.
\]

By uniqueness of the least positive inverse,

\[
t=\iota_N(r).
\]

If \(t=1\), then \(r\equiv1\pmod N\); this contradicts
\(1<r<N\). Thus \(1<r,t<N\). Write \(rt=1+k_rN\). Then

\[
1\le k_r<r.
\]

Substitute (4):

\[
V=r(jN+t)
=1+(jr+k_r)N.
\]

Comparison with \(V=1+KN\) gives

\[
K=jr+k_r.
\]

Because \(0<k_r<r\), this is the Euclidean division of \(K\) by \(r\).
Hence \(j=\lfloor K/r\rfloor\) and \(k_r=K\bmod r\). This proves
(5)--(6). This remainder identity is the promoted P70/P80 divisor-carry
law. The new work below is its cross-star interpretation and quantitative
composition.

## 3. Exact recentering and overlap

Equation (4) is exactly

\[
qS=t+jN=H'_j,
\]

which proves (8). For any \(b\),

\[
H'_b-H'_j=N(b-j).
\]

Since \(qS=H'_j\) is a unit modulo \(N\), the Euclidean algorithm gives

\[
\gcd(qS,H'_b)
=\gcd(qS,N(b-j))
=\gcd(qS,b-j).
\]

If \(j<C\) and an observed child digit \(b_a\ne j\), then

\[
1\le|b-j|<C.
\]

This proves (9)--(10). At the formal digit \(b=j\),

\[
rH'_j=rqS=V,
\]

so the exact value is the old parent value. If a child anchor realizes this
digit, its endpoint screens run and its endpoints are retained before the
duplicate exact value is discarded.

## 4. The large-quotient descent

The base carry satisfies \(k<q\), because

\[
qw=1+kN<qN.
\]

Since \(A<C\),

\[
K=k+Aq<Cq.
\tag{1}
\]

If \(j\ge C\), then (6) gives

\[
Cr\le jr<K<Cq.
\]

Therefore \(r<q\), proving (11).

## 5. Two-step contraction

Let the first transition be \(q_0=q\) to \(q_1=r\). Put

\[
\delta=q_0-q_1>0.
\]

The first new carry satisfies, using (1) and \(j_0\ge C\),

\[
k_1
=K_0-j_0q_1
<Cq_0-Cq_1
=C\delta.
\tag{2}
\]

If

\[
\delta\ge\frac{q_0}{C+1},
\]

then

\[
q_1=q_0-\delta
\le\frac{C}{C+1}q_0.
\]

The second transition has \(q_2<q_1\), so (12) follows in this case.

Otherwise,

\[
\delta<\frac{q_0}{C+1}.
\tag{3}
\]

Let its anchored digit be \(A_1<C\), and let its quotient be \(j_1\ge C\).
Then

\[
Cq_2
\le j_1q_2
<k_1+A_1q_1
<C\delta+(C-1)q_1,
\]

where (2) was used in the last step. Therefore

\[
q_2
<\delta+\left(1-\frac1C\right)q_1.
\]

Substitute \(q_1=q_0-\delta\):

\[
q_2
<\left(1-\frac1C\right)q_0+\frac{\delta}{C}.
\]

Using (3),

\[
q_2
<\left(1-\frac1C\right)q_0
+\frac{q_0}{C(C+1)}
=\frac{C}{C+1}q_0.
\]

This proves (12).

For a run of \(m\) consecutive large-quotient transitions, every pair of
steps multiplies the block size by less than \(C/(C+1)\). Since

\[
\log(1+1/C)\ge\frac1{C+1},
\]

there are \(O(C\log q_0)=O(C\log N)\) transitions before a positive integer
block would fall below one. For \(C=n^3\) and \(\log N=O(n)\), this is
\(O(n^4)\).

## 6. Certificate and scope

For \(N=143,q=28,w=46\), direct calculation gives

\[
28\cdot46=1+9N.
\]

The digit \(A=1\) is realized by parent anchor \(\ell=3\), whose endpoints
are \((84,63)\). Here \(H=189=27\cdot7\), \(K=37\), and

\[
28\cdot27=756=5N+41,
\qquad
7\cdot41=1+2N.
\]

The digit \(A=3\) is realized by parent anchor \(\ell=5\), whose endpoints
are \((140,95)\). Here \(H=475=25\cdot19\), \(K=93\), and

\[
28\cdot25=700=4N+128,
\qquad
19\cdot128=1+17N.
\]

The released blocks satisfy \(7,19<N/C\). Child anchor \(a=5\) realizes
the virtual digit \(4\) with endpoints \((95,140)\). Its screens equal one.
All values, quotients, inverses, and branch labels in the statement follow.

The proof is pathwise. It does not bound the number of branches, forbid
alternating small- and large-quotient steps, force a parity cycle, or control
the normalized-root image.
