# Proof of the F192 P164-derived ACD lattice obstruction

## 1. Local distinctness of the public power word

Fix \(S\in\{P,Q\}\), and suppose that

\[
x_i\equiv x_j\pmod S,
\qquad 0\le i<j<R.
\tag{1.1}
\]

By the definition of \(x_i,x_j\),

\[
w^{a^i}\equiv w^{a^j}\pmod S.
\tag{1.2}
\]

Since \(w\) has order \(g_S\) modulo \(S\),

\[
g_S\mid a^j-a^i=a^i(a^{j-i}-1).
\tag{1.3}
\]

Every rational prime divisor of \(g_S\) is coprime to \(a\) by (3) of the
statement. Hence \(\gcd(a,g_S)=1\), and (1.3) gives

\[
g_S\mid a^{j-i}-1.
\tag{1.4}
\]

Choose any prime \(\ell\mid g_S\). Then

\[
\operatorname{ord}_\ell(a)\mid j-i\le R-1=K,
\tag{1.5}
\]

contrary to \(\operatorname{ord}_\ell(a)>K\). Thus no equality (1.1) is
possible. The argument applies to both hidden primes, proving simultaneous
local distinctness.

The word is public and numerical QP in the P164 parameter regime. It may be
generated recursively by

\[
x_0=w,
\qquad
x_{j+1}=x_j^a\bmod N,
\tag{1.6}
\]

using \(R-1\) modular exponentiations. This cost observation is not used in
the obstruction proof.

## 2. Circular cluster lemma

Fix \(S\in\{P,Q\}\). Write the \(R\) distinct residues \(x_j\bmod S\) in
increasing cyclic order, and let

\[
d_0,\ldots,d_{R-1}>0
\tag{2.1}
\]

be the clockwise gaps between consecutive residues. Their sum is \(S\).

For each starting position, sum the next \(m\) gaps. Every gap occurs in
exactly \(m\) of these \(R\) sums. Therefore the average \(m\)-gap arc has
length

\[
{mS\over R}.
\tag{2.2}
\]

At least one such arc has length at most (2.2). Let \(j_0\) label its first
point, and let \(j_i\) label its \(i\)-th successor for \(1\le i\le m\).
Define \(r_i\) as the clockwise distance modulo \(S\) from \(x_{j_0}\) to
\(x_{j_i}\). Then

\[
0<r_i\le {mS\over R}
\le\left\lceil{mS\over R}\right\rceil.
\tag{2.3}
\]

Let

\[
z_i=[x_{j_i}-x_{j_0}]_N\in\{0,\ldots,N-1\}.
\tag{2.4}
\]

Reduction modulo \(S\) commutes with reduction modulo \(N\), because
\(S\mid N\). Hence

\[
z_i\equiv r_i\pmod S,
\tag{2.5}
\]

and there is an integer \(t_i\) with

\[
z_i=St_i+r_i.
\tag{2.6}
\]

This proves the hidden all-inlier cluster.

For either hidden prime \(T\in\{P,Q\}\), local distinctness gives

\[
x_{j_i}-x_{j_0}\not\equiv0\pmod T.
\tag{2.7}
\]

Equation (2.4) has the same residue modulo \(T\), so \(T\nmid z_i\).
Therefore

\[
\gcd(z_i,N)=1.
\tag{2.8}
\]

For completeness, suppose the public balance promise is \(P/Q\le C\). Then

\[
\widehat B_{\rm pub}
=\left\lceil {m\sqrt{CN}\over R}\right\rceil
\tag{2.9}
\]

is a public valid upper bound because \(P\le\sqrt{CN}\). Local distinctness
also implies \(R\le P\). Therefore

\[
{\widehat B_{\rm pub}\over P}
\le
{m\over R}\sqrt{CQ\over P}+{1\over P}
\le(\sqrt C+1){m\over R}.
\tag{2.10}
\]

Moreover,

\[
{\widehat B_{\rm pub}\over Q}
\le C{m\over R}+{1\over Q}.
\tag{2.11}
\]

Thus \(\widehat B_{\rm pub}<Q\) for all sufficiently large inputs whenever
\(m/R\) is bounded above by a sufficiently small constant depending only on
\(C\). This verifies the public constant-factor assertion in the statement.

## 3. Lattice determinant and factor vector

Every vector of the lattice (9) in the statement has the unique form

\[
u(c,k_1,\ldots,k_m)
=
(c\widehat B,
cz_1-Nk_1,\ldots,cz_m-Nk_m),
\tag{3.1}
\]

with \(c,k_i\in\mathbb Z\). The displayed basis is triangular with diagonal
\(\widehat B,N,\ldots,N\), so

\[
\det L=\widehat B N^m.
\tag{3.2}
\]

For the cluster modulo \(P\), equation (7) is

\[
z_i=Pt_i+r_i.
\tag{3.3}
\]

Multiplying by \(Q=N/P\) gives

\[
Qz_i=Nt_i+Qr_i.
\tag{3.4}
\]

Taking \(c=Q\) and \(k_i=t_i\) in (3.1) yields

\[
v_Q=(Q\widehat B,Qr_1,\ldots,Qr_m)\in L.
\tag{3.5}
\]

Since \(0<r_i\le\widehat B\),

\[
Q\widehat B\le\|v_Q\|_2
\le Q\widehat B\sqrt{m+1}.
\tag{3.6}
\]

For \(D=m+1\), \(N=PQ\), and
\(\epsilon=\widehat B/P\), direct simplification gives

\[
{Q\widehat B\over(\widehat B N^m)^{1/D}}
=Q\epsilon P\,
  (\epsilon P(PQ)^m)^{-1/D}
=\left(Q\epsilon^m\right)^{1/D}.
\tag{3.7}
\]

This proves the determinant and scale formulas.

## 4. Simultaneous Dirichlet lemma

Let \(\alpha_1,\ldots,\alpha_m\in\mathbb R\), and let \(A\ge2^m\) be an
integer. Put

\[
H=\lfloor A^{1/m}\rfloor.
\tag{4.1}
\]

Then \(H\ge A^{1/m}/2\). Partition the torus
\([0,1)^m\) into \(H^m\) half-open boxes of side length \(1/H\). Among the
\(H^m+1\) points

\[
(\{j\alpha_1\},\ldots,\{j\alpha_m\}),
\qquad 0\le j\le H^m,
\tag{4.2}
\]

two lie in the same box. Subtract their indices. This gives an integer
\(c\) satisfying

\[
1\le c\le H^m\le A,
\qquad
\max_i\|c\alpha_i\|_{\mathbb R/\mathbb Z}
\le {1\over H}
\le2A^{-1/m}.
\tag{4.3}
\]

No distribution assumption is used.

## 5. A coprime vector below every factor-bearing coefficient

Apply the lemma with

\[
\alpha_i={z_i\over N}.
\tag{5.1}
\]

For the integer \(A\) in (14), choose nearest integers \(k_i\). Equations
(4.3) and (14) give

\[
|cz_i-Nk_i|
\le2N A^{-1/m}
<{\epsilon N\over\sqrt D}
={Q\widehat B\over\sqrt D}.
\tag{5.2}
\]

Also

\[
|c|\widehat B
\le A\widehat B
<{Q\widehat B\over\sqrt D}.
\tag{5.3}
\]

The vector (3.1) therefore has all \(D\) coordinates shorter than
\(Q\widehat B/\sqrt D\), and hence

\[
\|u(c,k_1,\ldots,k_m)\|_2<Q\widehat B.
\tag{5.4}
\]

This proves \(\lambda_1(L)<Q\widehat B\).

Now let \(u(c,k_1,\ldots,k_m)\) be any shortest nonzero vector. If \(c=0\),
then it is a nonzero vector in

\[
\{0\}\times N\mathbb Z^m,
\tag{5.5}
\]

so its norm is at least \(N\). But

\[
Q\widehat B<Q^2\le PQ=N,
\tag{5.6}
\]

because \(\widehat B<Q\le P\). Thus a shortest vector cannot have \(c=0\).

If \(\gcd(c,N)>1\), then \(c\) is divisible by \(P\) or \(Q\). Since
\(Q\le P\),

\[
|c|\ge Q,
\tag{5.7}
\]

and its first coordinate has magnitude at least \(Q\widehat B\), contrary
to (5.4). Therefore every shortest vector satisfies

\[
\gcd(c,N)=1.
\tag{5.8}
\]

Because \(0<\widehat B<Q\le P\), the first coordinate
\(c\widehat B\) is a unit modulo \(N\). By (2.8), every \(z_i\) is a unit
modulo \(N\). Hence, for each hidden prime \(T\in\{P,Q\}\),

\[
cz_i-Nk_i\equiv cz_i\not\equiv0\pmod T.
\tag{5.9}
\]

Every residual coordinate is also a unit modulo \(N\). Thus gcd-testing any
coordinate of any shortest vector returns one. This proves the exact-SVP
obstruction.

## 6. Polylogarithmic-dimension corollary

Assume fixed balance, so

\[
\log_2Q={n\over2}+O(1).
\tag{6.1}
\]

Let \(R\) be numerical QP, let \(m\) be polylogarithmic in \(n\), and assume

\[
\epsilon={\widehat B\over P}\le C_0{m\over R}
\tag{6.2}
\]

for a fixed constant \(C_0\), while \(\widehat B<Q\). Equation (8) also
gives \(\epsilon\ge m/R\). Hence the logarithm of the lower endpoint in
(14) satisfies

\[
m\log_2\left({2\sqrt D\over\epsilon}\right)
\le
m\left(
\log_2{R\over m}
+{1\over2}\log_2D
+1
\right)
=(\log n)^{O(1)}.
\tag{6.3}
\]

This is \(o(n)\), while

\[
\log_2{Q\over\sqrt D}={n\over2}-o(n).
\tag{6.4}
\]

The interval in (14) therefore contains an integer for all sufficiently
large \(n\). Its lower endpoint is at least \(2^m\), because
\(\epsilon<1\) and \(D\ge1\). The exact obstruction applies.

This corollary says nothing about exact SVP in larger dimension or a
different lattice construction.

## 7. Cyclic-order subset-bank count

Fix \(2\le s<R\). There are

\[
(R-1)!
\tag{7.1}
\]

oriented cyclic orders of \(R\) labeled elements. Fix one \(s\)-subset
\(F\). If its elements form one consecutive block, collapse that block to
one object. The block has \(s!\) internal linear orders, and the resulting
\(R-s+1\) objects have \((R-s)!\) oriented cyclic orders. Thus \(F\) is a
consecutive block in exactly

\[
s!(R-s)!
\tag{7.2}
\]

cyclic orders, a fraction

\[
{s!(R-s)!\over(R-1)!}
={R\over{R\choose s}}.
\tag{7.3}
\]

If a family \(\mathcal F\) covers every cyclic order, a union bound over its
members gives

\[
1\le|\mathcal F|{R\over{R\choose s}}.
\tag{7.4}
\]

This is equivalent to

\[
|\mathcal F|\ge {1\over R}{R\choose s}.
\tag{7.5}
\]

The count uses only the unknown cyclic label order. It does not prove that
all these orders can arise from the P164 power recurrence. Therefore it is
a lower bound for predeclared order-oblivious subset banks, not for
source-aware algorithms.
