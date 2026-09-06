# F261 blind reconstruction: exact centered-carry theorem

## Authentication and verdict

The only experiment artifact used for this reconstruction was
`ALGEBRA.md`. Its observed SHA-256 was

```text
df27b6557ac2fe2ae29a495241c66741e864f8d667237f04855aa82f499aa67f
```

This equals the required SHA-256.

**Exact conditional theorem: PASS.** All bounds, identities, congruences,
decoder cases, and candidate counts below follow from the stated assumptions.

**All-input or quasipolynomial factoring consequence: FAIL.** The theorem
does not produce a factor prefix, bound the true carry by a useful cap, or
give efficient access to the true point of the inverse map.

## 1. Assumptions and dyadic scale

Assume

\[
N=pq,\qquad p<q<2p,
\]

where \(p,q\) are distinct odd primes. Define

\[
n=\lceil\log _2(N+1)\rceil,\qquad
m=\lfloor n/2\rfloor,\qquad B=2^m,
\]

and impose the zero-defect condition

\[
B\mid N-1,\qquad H=(N-1)/B.
\]

Since the smallest product of distinct odd primes is \(15\), one has
\(n\ge 4\), \(m\ge 2\), and \(B\ge 4\). The definition of \(n\) gives

\[
2^{n-1}\le N\le 2^n-1.
\]

The exact parity split is

\[
\begin{array}{c|c|c}
n&N&H\\ \hline
2m&B^2/2\le N\le B^2-1&B/2\le H\le B-1,\\
2m+1&B^2\le N\le 2B^2-1&B\le H\le 2B-1.
\end{array}
\]

The bounds on \(H\) use \(N=BH+1\). In particular,

\[
B^2/2\le N<2B^2,
\qquad {B\over\sqrt2}\le\sqrt N<\sqrt2B.
\]

The balance assumption gives

\[
\sqrt{N/2}<p<\sqrt N<q<\sqrt{2N}<2B. \tag{1}
\]

Indeed, \(q<2p\) implies \(N=pq<2p^2\) and \(q^2<2pq=2N\).
Also \(p^2<N<q^2\). Since \(N\ge B^2/2\), (1) implies
\(p>B/2\), and hence both factors exceed \(B/2\).

These assumptions describe only the balanced, zero-defect source family.
They do not describe every balanced semiprime or every composite integer.

## 2. Round-half-up centers and ties

For each integer \(u\ge1\), define separate centers

\[
K_p=\left\lfloor{up+B/2\over B}\right\rfloor,
\qquad
K_q=\left\lfloor{uq+B/2\over B}\right\rfloor
\]

and centered residues

\[
x=up-K_pB,\qquad y=uq-K_qB.
\]

Then

\[
-B/2\le x,y<B/2. \tag{2}
\]

This follows directly from
\(K_r\le(ur+B/2)/B<K_r+1\), for \(r=p,q\). The two
centers are not forced to be equal.

For an odd integer \(r\), a half tie occurs exactly when

\[
ur\equiv B/2\pmod B.
\]

Because \(r\) is a unit modulo \(B\) and
\(r(B/2)\equiv B/2\pmod B\), this is equivalent to

\[
u\equiv B/2\pmod B. \tag{3}
\]

If \(ur=jB+B/2\), the literal floor rule selects \(K_r=j+1\), so
the centered residue is \(-B/2\), not \(+B/2\). Thus (2) is half-open
on the positive side. For example, \(p=101,q=109,B=128,u=64\)
gives \(x=y=-64\).

## 3. Carry, weighted trace, and exact decoder

Since \(N\equiv1\pmod B\), expansion of

\[
u^2N=(K_pB+x)(K_qB+y)
\]

shows that \(xy\equiv u^2\pmod B\). Therefore the carry

\[
c={xy-u^2\over B} \tag{4}
\]

is an integer. Substituting \(N=BH+1\) and (4) into the same expansion
gives

\[
u^2H=K_pK_qB+K_py+K_qx+c. \tag{5}
\]

Define the weighted trace

\[
T=K_pq+K_qp. \tag{6}
\]

Multiplying (6) by \(u\), substituting
\(up=K_pB+x\), \(uq=K_qB+y\), and then using (5), yields

\[
uT=u^2H+K_pK_qB-c,
\qquad
T={u^2H+K_pK_qB-c\over u}\in\mathbb Z. \tag{7}
\]

The hidden factor \(p\) is a root of

\[
K_qX^2-TX+K_pN=0, \tag{8}
\]

because substitution of (6) makes the left side at \(X=p\) equal to
zero. Its discriminant is the exact square

\[
D=T^2-4K_pK_qN=(K_pq-K_qp)^2. \tag{9}
\]

Equations (7)--(9) give a sound exact decoder for guessed tuples:

1. Require \(u\mid u^2H+K_pK_qB-c\), or construct \(T\) directly as
   in Section 5.
2. If \(K_q>0\), require \(D\ge0\) and require \(D\) to be a square.
   Test each of
   \[
   X={T\pm\sqrt D\over2K_q}
   \]
   whose numerator is divisible by \(2K_q\).
3. Accept only an integer \(X\) satisfying \(1<X<N\) and \(X\mid N\).

The final exact-division test makes every accepted output a correct proper
divisor, even for a false guessed tuple. For a true tuple, (8)--(9) ensure
that the decoder tests \(p\).

If \(K_q=0\), (8) is linear. When \(T\ne0\) and \(T\mid K_pN\), test

\[
X={K_pN\over T}.
\]

Reject when \(T=0\). If \(K_p=K_q=0\), every weighted trace consistent
with (6) is \(T=0\), so (8) is identically uninformative; reject this
center pair. These are only decoder endpoint conventions:
in the source family, (1) and \(u\ge1\) imply the true
\(K_p,K_q\ge1\).

## 4. Exact public center intervals

Define

\[
p_- =\left\lfloor\sqrt{\lfloor N/2\rfloor}\right\rfloor+1,
\qquad p_+=\lfloor\sqrt N\rfloor,
\]

\[
q_-=p_++1,
\qquad q_+=\left\lfloor\sqrt{2N-1}\right\rfloor.
\]

The strict inequalities in (1), together with integrality, give

\[
p_-\le p\le p_+,
\qquad q_-\le q\le q_+. \tag{10}
\]

For example, \(p^2>N/2\) is equivalent, for odd \(N\), to
\(p^2\ge\lfloor N/2\rfloor+1\), and \(q^2<2N\) is equivalent to
\(q^2\le2N-1\).

Round-half-up is monotone. Hence the true centers lie in the public
integer intervals

\[
\left\lfloor{up_-+B/2\over B}\right\rfloor
\le K_p\le
\left\lfloor{up_++B/2\over B}\right\rfloor, \tag{11}
\]

\[
\left\lfloor{uq_-+B/2\over B}\right\rfloor
\le K_q\le
\left\lfloor{uq_++B/2\over B}\right\rfloor. \tag{12}
\]

All endpoints in (11)--(12) are public functions of \(N,B,u\).
Moreover, (1) places every possible factor between \(B/2\) and \(2B\).
Thus each center interval is contained in \([1,2u]\), has at most
\(2u\) integer entries, and in particular has \(O(u)\) entries. The
weaker advertised bound \(1\le K_p,K_q\le3u\) follows immediately.

## 5. Filtering by a known dyadic prefix

First assume

\[
R=2^t,\qquad 2\le R\mid B,
\]

and that the labeled prefix

\[
a=p\bmod R
\]

is supplied. Use the least nonnegative residue for \(a\). It is odd and
therefore invertible modulo \(R\). Define the other factor prefix by

\[
b=q\bmod R=N a^{-1}\bmod R. \tag{13}
\]

Once \(a\) is supplied, (13) uses only public arithmetic. Reducing (6)
modulo \(R\) gives

\[
T\equiv K_pb+K_qa\pmod R. \tag{14}
\]

Put

\[
A=u^2H+K_pK_qB,
\qquad S=K_pb+K_qa.
\]

Since \(c=A-uT\), (14) is equivalent to

\[
c\equiv A-uS\pmod{uR}. \tag{15}
\]

The term \(K_pK_qB\) in \(A\) cannot be removed. The assumption
\(R\mid B\) only proves \(R\mid K_pK_qB\); vanishing modulo \(uR\)
would additionally require

\[
u\mid K_pK_q(B/R),
\]

which is not an assumption. As an exact source-family instance,
\(p=101,q=109,B=R=128,u=5\) has \(K_p=K_q=4\), and
\(K_pK_qB=2048\not\equiv0\pmod{640}\).

Let \(C\ge0\) be an integer carry cap. Instead of enumerating signed
carries, enumerate all integers \(T\) such that

\[
\left\lceil{A-C\over u}\right\rceil
\le T\le
\left\lfloor{A+C\over u}\right\rfloor,
\qquad T\equiv S\pmod R, \tag{16}
\]

and set \(c=A-uT\). Then (7) is automatic, negative carries need no
remainder convention, and (16) is exactly equivalent to
\(|c|\le C\) plus (14). Therefore every true tuple whose carry satisfies
the cap survives.

Two consecutive allowed values of \(T\) differ by \(R\), and their
carries differ by \(uR\). An interval of carry width \(2C\) consequently
contains at most

\[
1+\left\lfloor{2C\over uR}\right\rfloor \tag{17}
\]

values for each fixed center pair. In particular, if \(uR>2C\), there
is at most one.

Let \(U\ge1\) be an integer. Count candidate tuples before deduplication.
By Section 4, there are at most \(4u^2\) center pairs for a fixed \(u\).
Thus the complete bank defined by (11), (12), and (16) satisfies the
explicit bound

\[
\begin{aligned}
\#\mathcal B(U,C,R)
&\le4\sum_{u=1}^Uu^2
 \left(1+\left\lfloor{2C\over uR}\right\rfloor\right)\\
&\le {2\over3}U(U+1)(2U+1)
   +{4C\over R}U(U+1)\\
&=O\!\left(U^3+{CU^2\over R}\right). \tag{18}
\end{aligned}
\]

Here the implicit constant is absolute. Since \(H<2B\) and
\(K_p,K_q\le2U\), every candidate can be formed and checked using a
number of bit operations polynomial in
\(n+\log(U+1)+\log(C+1)\). Equation (18) is therefore a candidate-count
improvement times polynomial-bit exact arithmetic. It is not a
quasipolynomial bound unless separate bounds on \(U,C\), and access to the
prefix, establish one.

### The \(R=1\) convention

For no supplied prefix, set \(R=1\), do not call a modular inverse, and
treat every congruence modulo \(1\) as vacuous. Equivalently take
\(S=0\) in (15)--(16). Then (15) is

\[
c\equiv A\pmod u,
\]

which is exactly the integrality condition in (7). Equations (17)--(18)
become

\[
1+\left\lfloor{2C\over u}\right\rfloor
\quad\text{and}\quad
O(U^3+CU^2),
\]

respectively. Thus integrality alone improves the crude enumeration that
independently scans every carry for every center pair.

## 6. One-dimensional inverse-quotient map

Return to \(R\ge2\), and additionally assume that \(u\) is odd. Since
\(p\) is odd and \(K_pB\) is even, the true centered residue \(x\) is
odd and is a unit modulo \(B\). Equation (4) gives

\[
y\equiv u^2x^{-1}\pmod B. \tag{19}
\]

Also \(R\mid B\) and the known prefix imply

\[
x\equiv up\equiv ua\pmod R.
\]

Define

\[
Z_{u,a}=\{z\in\mathbb Z:-B/2\le ua+Rz<B/2\},
\qquad x(z)=ua+Rz. \tag{20}
\]

The half-open interval has length \(B\), and \(R\mid B\), so

\[
|Z_{u,a}|=B/R. \tag{21}
\]

Every \(x(z)\) is odd because \(u,a\) are odd and \(R\) is even. For
each \(z\in Z_{u,a}\), let \(y(x(z))\) be the unique representative of
\(u^2x(z)^{-1}\pmod B\) in

\[
[-B/2,B/2).
\]

This representative uses the same tie rule: the class \(B/2\) is
represented by \(-B/2\). Define

\[
c(z)={x(z)y(x(z))-u^2\over B}. \tag{22}
\]

The quotient is integral by construction. The true \(x\) occurs exactly
once in (20); (19) and uniqueness of the centered representative then
give the true \(y\), so (22) gives the true carry. This is an exact
one-dimensional representation of the hidden centered-residue pair.

Direct exhaustion takes exactly \(B/R=2^{m-t}\) map evaluations. If the
known prefix has about \(n/4\) bits, then \(m-t\) is about \(n/4\), so
this cost is exponential in the input length. This statement is an
exhaustive-search cost, not a lower bound against every possible method.
Sampling this map is only diagnostic unless a separate theorem identifies
the true point or proves a useful density of decodable points. The map does
not apply as stated when \(R=1\) or when \(u\) is even, because the needed
unit property is then not guaranteed.

## 7. Exact scope boundary

The proved content is conditional and algebraic:

- it enumerates all capped-carry candidates for the balanced zero-defect
  family when the labeled factor prefix is supplied;
- it verifies every returned divisor by exact integer arithmetic;
- it proves the exact count (18), including the no-prefix convention; and
- for odd \(u\) and \(R\ge2\), it gives the exact inverse-map
  parameterization (20)--(22).

It does **not** prove that a useful \(u\le U\) has \(|c_u|\le C\), an
inverse-quasipolynomial law for the carries, a useful distribution of the
inverse map, an efficient way to find its true point, a way to obtain
\(a=p\bmod R\), or a public rule that selects the two true centers without
enumeration. If a separate known-residue terminal already factors from the
supplied prefix at modulus \(R\), that terminal, not this bank, is the
factorization mechanism.

Finite-cohort extrema and regression maxima are not theorem consequences
and are not used in this reconstruction. Therefore the exact conditional
theorem passes, while any claim that it alone resolves general integer
factoring fails.
