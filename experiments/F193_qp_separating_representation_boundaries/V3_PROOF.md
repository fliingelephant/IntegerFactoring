# Proof of the F193 V3 separating-representation boundaries

## 1. Explicit squarefree cusp boundaries

### 1.1 Denominator type

Let \(a/c\) be reduced and let

\[
\gamma=
\begin{pmatrix}A&B\\C&D\end{pmatrix}
\in\Gamma _0(N).
\]

Then \(C\equiv0\pmod N\) and

\[
\gamma(a/c)={Aa+Bc\over Ca+Dc}.
\tag{1.1}
\]

Fix \(s\mid N\) prime. Modulo \(s\), the determinant relation gives
\(AD\equiv1\), so \(A,D\ne0\). If \(s\mid c\), the new denominator is zero
modulo \(s\), while the numerator is \(Aa\ne0\); reduction cannot cancel
\(s\). If \(s\nmid c\), the new denominator is \(Dc\ne0\). Therefore

\[
s\mid c
\quad\Longleftrightarrow\quad
s\mid\operatorname{denominator}(\gamma(a/c)).
\tag{1.2}
\]

The standard cusp classification indexes the cusps with denominator divisor
\(d\mid N\) further by a residue class modulo \(\gcd(d,N/d)\). At squarefree
level this gcd is one. Hence

\[
d(a/c)=\gcd(c,N)
\tag{1.3}
\]

is a complete cusp-orbit label. Infinity is \(1/0\) and has type \(N\).

For a modular symbol,

\[
\partial\{\alpha,\beta\}=[\beta]-[\alpha].
\tag{1.4}
\]

Scan every explicitly listed reduced denominator. A gcd equal to \(p\) or
\(q\) factors \(N\). Otherwise every endpoint is one of the two global
cusps, so degree zero forces

\[
\partial C=t([c_N]-[c_1]).
\tag{1.5}
\]

The total encoded chain is numerical-QP, so reduction and all endpoint gcds
have numerical-QP total bit cost. Equation (1.5) is a support statement and
places no restriction on \(t\).

### 1.2 Standard operators

For \(\gcd(m,N)=1\), a standard branch of \(T_m\) has an upper-triangular
representative

\[
M=\begin{pmatrix}a&b\\0&d\end{pmatrix},
\qquad ad=m.
\tag{1.6}
\]

It sends a reduced \(x/y\) to

\[
{ax+by\over dy}.
\tag{1.7}
\]

For every \(s\mid N\), both \(a\) and \(d\) are units modulo \(s\). If
\(s\mid y\), the numerator in (1.7) is \(ax\ne0\), so \(s\) cannot cancel.
If \(s\nmid y\), then \(s\nmid dy\). Thus each branch preserves the exact
denominator type.

The Fricke matrix

\[
w_N=\begin{pmatrix}0&-1\\N&0\end{pmatrix}
\tag{1.8}
\]

sends \(a/c\) to \(-c/(Na)\). Because \(\gcd(a,c)=1\), reduction toggles
each prime divisor of \(N\), giving

\[
d\longmapsto N/d.
\tag{1.9}
\]

It therefore preserves the two-set partition
\(\{1,N\}\cup\{p,q\}\).

For an exact divisor \(Q\parallel N\), a standard unnormalized integral
Atkin--Lehner representative can be chosen as

\[
w_Q=
\begin{pmatrix}Qa&b\\Nc&Qd\end{pmatrix},
\qquad\det(w_Q)=Q.
\tag{1.10}
\]

At squarefree level it toggles the primes in \(Q\):

\[
d\longmapsto{dQ\over\gcd(d,Q)^2}.
\tag{1.11}
\]

For \(N=pq\), the proper nontrivial exact divisors are precisely \(p,q\).
Thus a standard explicitly labeled selective operator already names a
factor. Equations (1.10)--(1.11) make no assertion about a normalized
analytic matrix or an opaque implementation. This proves Section 1.

## 2. Uniform small-modulus CRT amplification

For distinct odd primes,

\[
b_N=(1+p)(1+q)=N+p+q+1.
\tag{2.1}
\]

Since \((p-1)(q-1)>0\),

\[
p+q<N+1,
\qquad
0<b_N<2(N+1)\le2^{n+1}.
\tag{2.2}
\]

Choose \(k=n+2\) distinct auxiliary primes, omitting 2 and 3 for the
\(24b_N\) interface. Their product \(M\) is greater than \(2^{n+1}\). The
standard bound for the \(k\)-th prime places these \(O(n)\) primes below
\(Cn\log(n+2)\) for a sufficiently large absolute \(C\). They have
\(O(\log n)\) bits and can be generated and certified in polynomial time.

If an auxiliary prime has a proper gcd with \(N\), return that gcd. Otherwise
call the uniform evaluator. In the \(24b_N\) interface, multiply by
\(24^{-1}\bmod\ell\). CRT gives \(b_N\bmod M\), and (2.2) makes its canonical
representative the exact integer \(b_N\).

Now set

\[
s=b_N-N-1=p+q,
\qquad
D=s^2-4N=(p-q)^2.
\tag{2.3}
\]

Exact square root and

\[
\{p,q\}=\left\{{s-\sqrt D\over2},{s+\sqrt D\over2}\right\}
\tag{2.4}
\]

recover the factors. Exact division, primality, and product checks verify the
answer.

There are polynomially many uniform numerical-QP calls. CRT and terminal
arithmetic are polynomial. Their composition is numerical QP. A fixed
finite modulus bank does not meet the growing-product premise. This proves
Section 2.

## 3. Dirichlet twists

For every Dirichlet character, including an imprimitive character extended
by zero away from the units of its defining modulus, the twist is defined by

\[
f\otimes\chi
=\sum_{m\ge1}\chi(m)a_f(m)q^m.
\tag{3.1}
\]

Therefore

\[
a_{f\otimes\chi}(N)=\chi(N)a_f(N).
\tag{3.2}
\]

Place the exact values in an explicitly represented compositum containing
the coefficient field of \(f\) and the character values. For a bank, define
the public linear map

\[
L:x\longmapsto
(\chi_1(N)x,\ldots,\chi_L(N)x).
\tag{3.3}
\]

Its image has dimension at most one. If every public scalar is zero, it has
dimension zero. If one scalar is nonzero, it is a root of unity and hence a
unit; division in that row recovers \(x=a_f(N)\).

For a character modulo \(M\), \(\gcd(M,N)=1\) implies
\(\chi(N)\ne0\). The same holds for a primitive character presented at its
conductor when that conductor is coprime to \(N\). By contrast, the
principal character modulo \(N\) has conductor one but value zero at \(N\);
this is why V3 uses rank **at most** one and does not infer nonvanishing from
the conductor alone.

Equation (3.2) compares information only. It does not prove that evaluating
different twists has equal cost, and it does not concern different base
forms or nontwist operations. This proves Section 3.

## 4. One global endomorphism on prime torsion

Let \(r\) be invertible on the connected arithmetic base \(S\). Then
\(E[r]\) is a finite etale group scheme of rank \(r^2\), equivalently a
rank-two lisse \(\mathbb F_r\)-module.

Choose a geometric fiber and a basis. An etale path to another geometric
fiber transports the entire finite-etale fiber functor. Naturality makes
this transport commute with every morphism defined over \(S\), including
\(\alpha\). Consequently, after choices of bases, the two fiber matrices
satisfy

\[
A_q=P A_p P^{-1}
\tag{4.1}
\]

for some \(P\in GL_2(\mathbb F_r)\).

Over the field \(\mathbb F_r\), conjugacy preserves the characteristic
polynomial, the unique monic minimal polynomial, and, for invertible
matrices, the group order. Hence no one of these invariants differs between
the two good fibers.

For a globally defined CM endomorphism, its action on every prime-to-
characteristic Tate module has trace \(\operatorname{Tr}(\alpha)\) and
determinant \(\operatorname{Nm}(\alpha)=\deg(\alpha)\). Its Tate-module
characteristic polynomial is therefore

\[
X^2-\operatorname{Tr}(\alpha)X+\operatorname{Nm}(\alpha).
\tag{4.2}
\]

Reducing (4.2) modulo \(r\) gives the characteristic polynomial on \(E[r]\)
in each good fiber. For \([a]\), the matrix is \(aI_2\).

The descent premise is essential. Local Frobenius is indexed by the residue
characteristic. Extra ordinary or supersingular endomorphisms can appear
only after reduction. A pair of local maps glued over the disconnected CRT
base \(\operatorname{Spec}(\mathbb Z/N\mathbb Z)\) need not descend from one
endomorphism on \(S\). None of these objects is controlled by (4.1). This
proves Section 4 and completes V3.
