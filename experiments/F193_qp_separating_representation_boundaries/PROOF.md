# Proof of the F193 separating-representation boundaries

## 1. Squarefree cusp types and explicit sparse boundaries

### 1.1 The denominator gcd is a cusp invariant

Let \(a/c\) be reduced and let

\[
\gamma=
\begin{pmatrix}A&B\\ C&D\end{pmatrix}
\in\Gamma _0(N).
\]

Then \(C\equiv0\pmod N\), and

\[
\gamma(a/c)={Aa+Bc\over Ca+Dc}.
\tag{1.1}
\]

Fix a prime \(r\mid N\). Modulo \(r\), the determinant relation gives
\(AD\equiv1\), so both \(A\) and \(D\) are nonzero. If \(r\mid c\), then
the denominator in (1.1) is divisible by \(r\), while the numerator is
congruent to \(Aa\ne0\pmod r\). Thus reduction of the fraction does not
cancel \(r\). If \(r\nmid c\), its new denominator is congruent to
\(Dc\ne0\pmod r\). Therefore

\[
r\mid c
\quad\Longleftrightarrow\quad
r\mid\operatorname{denominator}(\gamma(a/c)).
\tag{1.2}
\]

The standard cusp classification for \(\Gamma _0(N)\) says that the cusps
with denominator gcd \(d\mid N\) are additionally indexed by residue classes
modulo \(\gcd(d,N/d)\). When \(N\) is squarefree, this latter gcd is one.
Hence (1.2) is a complete orbit invariant and there is exactly one cusp for
each divisor \(d\mid N\). For \(N=pq\), these are the four types
\(1,p,q,N\).

The convention includes \(\infty=1/0\), whose type is
\(\gcd(0,N)=N\).

### 1.2 Boundary support

For an oriented modular symbol,

\[
\partial\{\alpha,\beta\}=[\beta]-[\alpha].
\tag{1.3}
\]

Reduce every explicitly supplied endpoint and compute the gcd of its
denominator with \(N\). If one gcd is \(p\) or \(q\), it is already a
nontrivial factor. If no such gcd occurs, every endpoint in (1.3) is one of
the two cusp types \(1,N\). By linearity, the degree-zero boundary is then
supported on two points and has the form

\[
\partial C=t([c_N]-[c_1])
\tag{1.4}
\]

for an integer \(t\).

There are only QP-many explicitly listed integers, each of QP bit length.
Euclid's algorithm on all of them has QP total bit complexity. No assertion
about the arithmetic information in \(t\) follows from its one-dimensional
support.

### 1.3 Good-prime Hecke branches preserve type

For \(\gcd(m,N)=1\), use the standard upper-triangular representatives of a
good-prime Hecke correspondence,

\[
M=
\begin{pmatrix}a&b\\0&d\end{pmatrix},
\qquad ad=m.
\tag{1.5}
\]

They send a reduced \(x/y\) to

\[
{ax+by\over dy}.
\tag{1.6}
\]

For every \(r\mid N\), both \(a\) and \(d\) are units modulo \(r\). If
\(r\mid y\), the numerator of (1.6) is \(ax\ne0\pmod r\), so cancellation
does not remove \(r\) from the denominator. If \(r\nmid y\), then
\(r\nmid dy\). Thus every branch preserves exactly the set of primes of
\(N\) dividing the reduced denominator, and hence preserves cusp type.

This argument is only for good-prime Hecke correspondences. An operator with
index sharing a prime with \(N\) is not covered.

### 1.4 Fricke and Atkin--Lehner operators

The Fricke matrix

\[
w_N=
\begin{pmatrix}0&-1\\N&0\end{pmatrix}
\tag{1.7}
\]

sends \(a/c\) to \(-c/(Na)\). Since \(\gcd(a,c)=1\), reducing this fraction
cancels exactly \(d=\gcd(c,N)\) from the part of its denominator supported on
\(N\). Its new type is therefore

\[
d\longmapsto N/d.
\tag{1.8}
\]

In particular, \(W_N\) swaps the two global cusps and swaps the two hidden
cusps; it does not move a global cusp into a hidden one.

For an exact divisor \(Q\parallel N\), a standard integral Atkin--Lehner
representative has the form

\[
w_Q=
\begin{pmatrix}Qa&b\\Nc&Qd\end{pmatrix},
\qquad
\det w_Q=Q.
\tag{1.9}
\]

Its action toggles, in the squarefree divisor label, precisely the prime
divisors of \(Q\):

\[
d\longmapsto {dQ\over\gcd(d,Q)^2}.
\tag{1.10}
\]

For example, the global labels \(1,N\) go to \(Q,N/Q\). If \(N=pq\), a
proper nontrivial exact divisor is \(p\) or \(q\). The operator's standard
label \(Q\), or the determinant in (1.9), is then itself a nontrivial factor
of \(N\). The two divisor-free cases are \(Q=1\), which is trivial, and
\(Q=N\), which is Fricke and obeys (1.8).

This proves the first boundary. It concerns standard explicitly represented
operators and boundary support. It does not classify every endomorphism of a
modular-symbol or cuspidal module.

## 2. CRT amplification of small modular outputs

For distinct odd primes,

\[
b_N=(1+p)(1+q)=N+p+q+1.
\tag{2.1}
\]

Also

\[
p+q<N+1,
\]

because \((p-1)(q-1)>0\). Therefore

\[
0<b_N<2(N+1)\le2^{n+1}.
\tag{2.2}
\]

Choose \(k=n+2\) distinct auxiliary primes, omitting \(2\) and \(3\) if the
oracle returns \(24b_N\). The product \(M\) of these primes satisfies

\[
M>2^{n+1}>b_N.
\tag{2.3}
\]

The first \(O(n)\) primes have size \(O(n\log(n+2))\), by the standard
elementary bound for the \(k\)-th prime. They therefore have \(O(\log n)\)
bits and can be generated and certified in polynomial time. This gives the
claimed fixed range \(\ell\le Cn\log(n+2)\) for a sufficiently large
absolute constant \(C\).

Call the uniform evaluator once for each prime and apply the ordinary Chinese
remainder algorithm. Equations (2.2)--(2.3) make the canonical residue
modulo \(M\) equal to the ordinary integer \(b_N\). If the oracle gives
\(24b_N\bmod\ell\), multiply by \(24^{-1}\bmod\ell\) before CRT.

Now compute

\[
s=b_N-N-1=p+q,
\qquad
D=s^2-4N=(p-q)^2.
\tag{2.4}
\]

An exact integer square root followed by

\[
\{p,q\}=\left\{{s-\sqrt D\over2},{s+\sqrt D\over2}\right\}
\tag{2.5}
\]

recovers the factors. Parity, primality, and product checks verify them.

The number of calls is \(O(n)\), all moduli have \(O(\log n)\) bits, and
CRT and the terminal arithmetic are polynomial time. Multiplying one
numerical-QP running-time bound by \(O(n)\) leaves it numerical QP. This
proves Section 2.

The proof needs a single uniform evaluator over the growing modulus bank. It
does not amplify one fixed residue modulo one fixed integer into an exact
coefficient.

## 3. Dirichlet twists

By the definition of the Dirichlet twist of a modular form,

\[
f\otimes\chi
=\sum_{m\ge1}\chi(m)a_f(m)q^m.
\tag{3.1}
\]

If the conductor of \(\chi\) is coprime to \(N\), then \(\chi(N)\) is a
nonzero root of unity in its explicitly supplied coefficient field. Taking
the coefficient at \(N\) in (3.1) gives

\[
a_{f\otimes\chi}(N)=\chi(N)a_f(N).
\tag{3.2}
\]

The value \(\chi(N)\) is computable from the public character and public
integer \(N\), and its inverse is public. Hence all entries in any twist bank
are public scalar multiples of one unknown. One entry and its public inverse
recover that unknown. This proves the information-rank-one claim.

If a proposed character conductor has a proper gcd with \(N\), that gcd
already factors \(N\). If its conductor is a multiple of all of \(N\), the
coefficient can vanish for the uninformative public reason \(\chi(N)=0\).
Neither case supplies a counterexample to the stated coprime-conductor
theorem.

Equation (3.2) is an information identity, not an algorithmic lower bound.
It permits the possibility that a twist is easier to evaluate. Such an
evaluator would immediately evaluate \(a_f(N)\) through the same identity.

## 4. Globally defined endomorphisms on elliptic torsion

Because \(m\) is invertible on \(S\), the group scheme \(E[m]\) is finite
etale of rank \(m^2\). Over a connected base, it is a rank-two lisse
\(\mathbb Z/m\mathbb Z\)-module. Choose one geometric fiber and a basis.
Transport along geometric paths identifies all other geometric fibers up to
change of basis.

The global endomorphism \(\alpha\) induces one endomorphism of this lisse
module. Path transport commutes with \(\alpha\). Consequently, the matrices
of \(\alpha\) on the geometric \(p\)- and \(q\)-fibers are conjugate in

\[
\operatorname{Mat}_2(\mathbb Z/m\mathbb Z).
\tag{4.1}
\]

Conjugate matrices have the same characteristic polynomial and minimal
polynomial. If the matrix is invertible, conjugacy also preserves its order
in \(GL_2(\mathbb Z/m\mathbb Z)\).

For a CM endomorphism, the degree-two reduced characteristic equation is

\[
\alpha^2-\operatorname{Tr}(\alpha)\alpha
+[\operatorname{Nm}(\alpha)]=0.
\tag{4.2}
\]

On \(E[m]\), this gives the common characteristic polynomial

\[
X^2-\operatorname{Tr}(\alpha)X+operatorname{Nm}(\alpha)pmod m.
\tag{4.3}
\]

For \([a]\), the action is the scalar matrix \(aI_2\), with characteristic
polynomial \((X-a)^2\).

The connected-base descent premise is essential. Local Frobenius depends on
the residue characteristic and is not the reduction of one characteristic-
zero endomorphism over \(S\). An endomorphism that appears only in one
ordinary or supersingular fiber is likewise outside the global lisse
endomorphism. Finally, a pair of local endomorphisms glued with a hidden CRT
idempotent over \(\mathbb Z/N\mathbb Z\) need not descend to \(S\); allowing
such a pair would assume exactly the factor-local orientation that B5 seeks.

This proves the fourth boundary and all claims in the statement.
