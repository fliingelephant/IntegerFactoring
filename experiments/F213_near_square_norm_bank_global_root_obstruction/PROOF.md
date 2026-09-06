# F213 proof

## 1. Construction without a prime-density hypothesis

Fix \(M\geq2\). Define

\[
R=\operatorname{rad}\left(\prod_{a=1}^M a(a^2+1)\right),
\]

where \(\operatorname{rad}\) is the product of the distinct prime divisors.
The factor for \(a=1\) shows that \(R\) is even.

Choose any prime divisor \(d\) of \(R^2+1\). Then \(d\) is odd and
\(d\nmid R\). Since

\[
R^2\equiv-1\pmod d,
\]

the standard criterion for \(-1\) to be a quadratic residue modulo an odd
prime gives

\[
d\equiv1\pmod4.
\]

Put

\[
H=\max\{R^2+1,\ M(M^2+1)\}.
\]

Bertrand's postulate gives a prime \(\ell_1\) with

\[
H<\ell_1<2H.
\]

Inductively, after \(\ell_a\) is chosen, apply Bertrand's postulate to
\(2\ell_a\) and choose a prime \(\ell_{a+1}\) with

\[
2\ell_a<\ell_{a+1}<4\ell_a.
\]

This produces \(M\) distinct primes. Every one satisfies

\[
\ell_a>H\geq M(M^2+1),
\]

and every \(\ell_a\) is coprime to \(Rd\). No theorem about the number of
primes in a fixed short interval is used.

For each \(a\), consider the linear polynomial

\[
g_a(U)=2aU+1-a^2.
\]

Because \(\ell_a>2a\), its coefficient is a unit modulo \(\ell_a\).
There is one root class modulo \(\ell_a\). Among the \(\ell_a\) lifts of
that class modulo \(\ell_a^2\), exactly one is a root modulo
\(\ell_a^2\). Choose any other lift \(u_a\). Then

\[
\ell_a\mid g_a(u_a),
\qquad
\ell_a^2\nmid g_a(u_a).
\tag{1}
\]

There is also a residue \(v\bmod d^2\) such that

\[
d\mid v^2+1,
\qquad
d^2\nmid v^2+1.
\tag{2}
\]

Indeed, start with the root \(R\bmod d\). Its derivative \(2R\) is
nonzero modulo \(d\), so exactly one of its \(d\) lifts modulo \(d^2\) is
a root modulo \(d^2\). Choose any other lift.

The moduli

\[
R,\quad d^2,\quad \ell_1^2,\ldots,\ell_M^2
\]

are pairwise coprime. The Chinese remainder theorem therefore gives one
class \(x\bmod\mathcal L\), where

\[
\mathcal L=Rd^2\prod_{a=1}^M\ell_a^2,
\]

satisfying

\[
x\equiv0\pmod R,
\qquad
x\equiv v\pmod{d^2},
\qquad
x\equiv u_a\pmod{\ell_a^2}quad(1\leq a\leq M).
\tag{3}
\]

Take the least residue \(0\leq x_0<\mathcal L\) and set

\[
s=x_0+\mathcal L,
\qquad
N=s^2+1.
\tag{4}
\]

Then

\[
\mathcal L\leq s<2\mathcal L.
\tag{5}
\]

Because \(R\) is even, \(s\) is even and \(N\) is odd. Equation (2)
and (3) give

\[
d\parallel N.
\]

Also \(d<\mathcal L\leq s<N\). Hence \(d\) is a proper divisor and
\(N\) is composite. This proves only compositeness; it does not prove that
\(N\) has two prime factors or balanced prime factors.

Finally, \(\mathcal L>\ell_1>M(M^2+1)>M\), so \(s>M\), as required.

## 2. Exact floor and norm identities

Since \(N=s^2+1\),

\[
\sqrt N-s=\frac1{\sqrt N+s}.
\]

For \(1\leq a\leq M<s\),

\[
0<a(\sqrt N-s)=\frac a{\sqrt N+s}<1.
\]

Therefore

\[
r_a=\lfloor a\sqrt N\rfloor=as.
\tag{6}
\]

Substitution gives

\[
E_a=a^2(s^2+1)-a^2s^2=a^2
\tag{7}
\]

and

\[
F_a=(as+1)^2-a^2(s^2+1)=2as+1-a^2.
\tag{8}
\]

Because \(1\leq a<s\),

\[
E_a=a^2<N
\]

and

\[
F_a=a(2s-a)+1>0.
\]

Moreover,

\[
N-F_a=s^2+1-(2as+1-a^2)=(s-a)^2>0.
\tag{9}
\]

Thus both children lie strictly between zero and \(N\).

## 3. Every displayed quantity passes the direct gcd screen

Suppose a prime \(h\) divides both \(a\) and \(N\). Since every prime
divisor of every \(a\leq M\) divides \(R\), equation (3) gives
\(s\equiv0\pmod h\). But then

\[
N=s^2+1\equiv1\pmod h,
\]

a contradiction. Hence

\[
\gcd(a,N)=1.
\tag{10}
\]

Also \(\gcd(s,N)=1\), so (6) and (10) give

\[
\gcd(r_a,N)=1.
\tag{11}
\]

Now suppose a prime \(h\) divides both \(F_a\) and \(N\). The exact
identity

\[
(as+1)^2-F_a=a^2N
\tag{12}
\]

implies \(h\mid as+1\). In particular, \(h\nmid a\). Squaring
\(as\equiv-1\pmod h\) and using \(s^2\equiv-1\pmod h\) gives

\[
a^2\equiv-1\pmod h.
\]

Thus \(h\mid a^2+1\), so \(h\mid R\). Equation (3) again gives
\(s\equiv0\pmod h\), contradicting \(h\mid s^2+1\). Therefore

\[
\gcd(F_a,N)=1.
\tag{13}
\]

The same argument beginning with \(h\mid as+1,N\) proves

\[
\gcd(r_a+1,N)=1.
\tag{14}
\]

Finally, (7), (10), and (13) give the complete gcd claim for \(E_a\) and
\(F_a\).

## 4. The adjacent norms have private valuation-one primes

Equations (1), (3), and (8) give

\[
\ell_a\mid F_a,
\qquad
\ell_a^2\nmid F_a.
\tag{15}
\]

Thus \(v_{\ell_a}(F_a)=1\).

For distinct indices \(a,b\), direct expansion gives

\[
bF_a-aF_b=(b-a)(1+ab).
\tag{16}
\]

If \(\ell_a\mid F_b\), then (15) and (16) imply

\[
\ell_a\mid(b-a)(1+ab).
\]

The integer on the right is nonzero, while

\[
|(b-a)(1+ab)|<M(M^2+1)<\ell_a.
\tag{17}
\]

This is impossible. Hence \(\ell_a\nmid F_b\) for \(b\neq a\).
Also \(\ell_a>M\geq b\), so \(\ell_a\nmid b^2=E_b\) for every \(b\).
The \(\ell_a\)-row is therefore a valuation-one row supported on exactly
the \(F_a\) column.

## 5. Exact parity kernel

The prime valuations of \(E_a=a^2\) are all even. Since the signed norm is
\(-E_a\), its parity column consists only of a one in the sign row.

Let a binary dependency select some \(E_a\) and \(F_a\) columns. The
private \(\ell_a\)-row from Section 4 forces the coefficient of every
\(F_a\) column to be zero. The remaining selected columns are copies of the
sign vector, so their number must be even. Conversely, every even subset of
the \(E_a\)'s has zero prime rows and zero sign row. This proves the exact
kernel formula in the statement.

Let \(S\) be such an even subset, with \(k=|S|\). Its positive integer
square is

\[
\prod_{a\in S}(-E_a)=\prod_{a\in S}a^2
=\left(\prod_{a\in S}a\right)^2,
\]

where the first equality uses even \(k\). Put

\[
X=\prod_{a\in S}r_a,
\qquad
Y=\prod_{a\in S}a.
\]

Equation (10) makes \(Y\) a unit modulo \(N\). Equation (6) gives

\[
XY^{-1}\equiv s^k\pmod N.
\]

Since \(s^2\equiv-1\pmod N\) and \(k\) is even,

\[
XY^{-1}\equiv(-1)^{k/2}\in\{1,-1\}\pmod N.
\tag{18}
\]

Thus the normalized root is global. If it is \(1\), then
\(\gcd(X-Y,N)=N\), while
\(\gcd(X+Y,N)=\gcd(2Y,N)=1\), because \(N\) is odd and \(Y\) is a unit.
For root \(-1\), the two outcomes swap.

An odd subset of \(E_a\) columns has odd sign parity and is not a
congruence-of-positive-squares dependency. If an implementation separately
uses the public equality \(s^2\equiv-1\pmod N\) to absorb that sign, it only
recovers \(s\). Moreover

\[
\gcd(s-1,N)=\gcd(s+1,N)=1,
\]

because any common divisor divides both \(s^2+1\) and respectively
\(s-1\) or \(s+1\), hence divides \(2\), while \(N\) is odd. This does not
create a factor either.

## 6. CRT bit length and bank size

The radical is bounded by the integer inside it:

\[
R\leq\prod_{a=1}^M a(a^2+1)
\leq(2M^3)^M.
\]

Hence

\[
\log_2R=O(M\log(M+1)).
\tag{19}
\]

Since \(d\leq R^2+1\),

\[
\log_2d=O(M\log(M+1)),
\qquad
\log_2H=O(M\log(M+1)).
\tag{20}
\]

The Bertrand construction gives

\[
\ell_a<2H\,4^{a-1}.
\tag{21}
\]

Therefore

\[
\sum_{a=1}^M\log_2\ell_a
\leq M\log_2(2H)+2\sum_{a=1}^M(a-1)
=O(M^2\log(M+1)).
\tag{22}
\]

Conversely, \(\ell_{a+1}>2\ell_a\), so

\[
\sum_{a=1}^M\log_2\ell_a=\Omega(M^2).
\tag{23}
\]

By the definition of \(\mathcal L\), equations (19)--(23) give

\[
\Omega(M^2)\leq\log_2\mathcal L
\leq O(M^2\log(M+1)).
\tag{24}
\]

Equations (4) and (5), followed by \(N=s^2+1\), show

\[
n=\lceil\log_2(N+1)\rceil
=2\log_2\mathcal L+O(1)
\]

up to constant-factor inequalities sufficient for

\[
\Omega(M^2)\leq n\leq O(M^2\log(M+1)).
\tag{25}
\]

Taking logarithms in (25) yields

\[
\log M=\left(\frac12+o(1)\right)\log n,
\]

and therefore \(M=n^{1/2+o(1)}\). In particular, the \(2M\)-column bank
is polynomial-sized. This conclusion uses only Bertrand's postulate and the
elementary factor-size bound on \(d\), not an unproved or unstated prime
density estimate.

The upper bound in (25) also implies

\[
n^{1/3}=O\!\left(M^{2/3}(\log(M+1))^{1/3}\right)<M
\]

for all sufficiently large \(M\). Hence the schedule
\(a=1,\ldots,\lfloor n^{1/3}\rfloor\), which depends only on the public
input length, is contained in the constructed bank. Restricting to an
initial subset preserves every private row and the global-root calculation.

## 7. Child bit lengths and recursion

Equation (7) gives

\[
\operatorname{bits}(E_a)=O(\log M)=o(n).
\]

For (1\leq a\leq M<s\), the function
\(2as+1-a^2\) is increasing in \(a\), so

\[
s<F_a\leq2Ms+1.
\]

Together with \(n=2\log_2s+O(1)\), this gives uniformly in \(a\)

\[
\operatorname{bits}(F_a)
=\log_2s+O(\log M)
=\frac n2+O(\log M)
=\left(\frac12+o(1)\right)n.
\tag{26}
\]

Thus, for all sufficiently large \(M\), every child has at most
\(\rho n\) bits for one fixed \(\rho<1\), for example \(\rho=2/3\).
There are only \(2M\leq\operatorname{poly}(n)\) children.

If an already correct all-input recursive routine is granted, these calls
fit the fixed-ratio side-call term in P183. Polynomially or numerical-QP
many fixed-ratio calls change only the numerical-QP overhead. P183 also
proves that one separate \(n\mapsto n-1\) spine can coexist with those side
calls. Therefore weak contraction is not the obstruction here. Even after
all child factorizations are granted, Sections 4 and 5 show that the exact
parity decoder returns only global roots.

This recursion discussion is conditional accounting. It does not use the
parent's special form as a promise for the child routine, and it does not
claim that F213 itself supplies an all-input factoring routine.
