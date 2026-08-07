# PASS

The SHA-256 digest of the reconstruction statement is

~~~text
fa3b1b9f81e14b8c054a0b8b9b0f589781f46615277cf12adc25da98ee5a6cc7
~~~

It matches the pinned digest. Every identity, stable-image claim,
complexity claim, infinite-family construction, fixed case, and scope
statement is correct.

## 1. The basic identity and its coprimality consequences

Write

\[
p=1+gA,\qquad q=1+gB.
\]

Then

\[
\begin{aligned}
E=pq-1
&=(1+gA)(1+gB)-1\\
&=gA+gB+g^2AB\\
&=g(gAB+A+B).
\end{aligned}
\]

Therefore

\[
\frac Eg=gAB+A+B. \tag{1}
\]

By definition,

\[
\gcd(A,B)=1.
\]

Reducing (1) modulo \(A\) gives

\[
\frac Eg\equiv B\pmod A,
\]

and reducing modulo \(B\) gives \(E/g\equiv A\pmod B\). Hence

\[
\gcd(A,E/g)=\gcd(A,B)=1,
\qquad
\gcd(B,E/g)=\gcd(B,A)=1.
\]

The same identity proves \(g\mid E\).

## 2. The quotient above the full powered rectangle

CRT gives

\[
G\cong C_{p-1}\times C_{q-1}
=C_{gA}\times C_{gB}.
\]

By the supplied full-rectangle theorem, \(S=G^E\) is the product of the
unique local subgroups of orders \(A\) and \(B\). In a cyclic group, the
quotient of the order-\(gA\) group by its unique order-\(A\) subgroup is
cyclic of order \(g\). The same holds at \(q\). Thus

\[
G/S\cong C_g\times C_g. \tag{2}
\]

Let \(S\le K\le G\). The quotient \(K/S\) is a subgroup of (2), so its
exponent divides \(g\). Since \(g\mid E\),

\[
(K/S)^E=1.
\]

Equivalently, \(k^E\in S\) for every \(k\in K\), which gives

\[
K^E\le S.
\]

The inclusion \(S\le K\) and functoriality of the power map give

\[
S^E\le K^E.
\]

Therefore

\[
S^E\le K^E\le S. \tag{3}
\]

No quotient in this argument is assumed to be publicly represented.

## 3. Stabilization at the coprime core

For a cyclic group of order \(r\), the image of the
\(E^t\)-power map has order

\[
\frac r{\gcd(r,E^t)}. \tag{4}
\]

For a prime \(\ell\nmid E\), its valuation in (4) is unchanged. For a prime
\(\ell\mid E\), the surviving valuation is

\[
\max\{v_\ell(r)-t\,v_\ell(E),0\}. \tag{5}
\]

Thus, once \(t\) is large enough to remove every prime component supported
on \(E\), the surviving cyclic subgroup is the unique subgroup of order
\(r_{\perp E}\).

Let

\[
n=\lceil\log_2(N+1)\rceil.
\]

Since \(A<N<2^n\), for every prime \(\ell\),

\[
v_\ell(A)\le n-1.
\]

The same holds for \(B\). If \(\ell\mid E\), then
\(v_\ell(E)\ge1\), so \(t=n-1\) in (5) kills every \(E\)-supported prime
component of both \(A\) and \(B\). Consequently

\[
S^{E^{\,n-1}}=T. \tag{6}
\]

By construction,

\[
\gcd(|T|,E)=\gcd(A_*B_*,E)=1.
\]

The \(E\)-power map is therefore an automorphism of \(T\), and (6) also
gives

\[
S^{E^n}=T. \tag{7}
\]

Raise the sandwich (3) by \(E^{n-1}\). This gives

\[
S^{E^n}\le K^{E^n}\le S^{E^{n-1}}.
\]

Both outer groups equal \(T\) by (6)--(7), so

\[
\boxed{K^{E^n}=T}
\]

for every \(S\le K\le G\).

### Public bit complexity

The integer \(n\) is the public bit length of \(N+1\), up to the stated
ceiling, and is \(O(\log N)\). The exponent \(E=N-1\) has \(O(\log N)\)
bits.

Given a polynomial-size public generator list for \(K\), repeatedly replace
each generator residue \(y\) by

\[
y^E\bmod N
\]

for \(n\) rounds. Because powering is a homomorphism in the abelian unit
group, the resulting list generates \(K^{E^n}=T\). Each modular
exponentiation uses polynomial bit complexity, there are \(n\) rounds, and
the generator list never grows. The total time and storage are polynomial
in the input bit length.

Equivalently, one could use the single exponent \(E^n\), whose bit length is
\(O(n^2)\), but forming it is unnecessary.

## 4. The immediate-stability criterion

Assume

\[
\gcd(AB,g)=1.
\]

Section 1 gives

\[
\gcd(AB,E/g)=1,
\]

because each of the coprime factors \(A,B\) is coprime to \(E/g\). Since
\(E=g(E/g)\),

\[
\gcd(AB,E)=1.
\]

No prime component of \(A\) or \(B\) is supported on \(E\), so

\[
A_*=A,\qquad B_*=B,\qquad T=S.
\]

The \(E\)-power map is an automorphism of \(S\), giving \(S^E=S\). The
sandwich (3) becomes

\[
S\le K^E\le S,
\]

and hence

\[
K^E=S
\]

for every intermediate subgroup \(K\).

## 5. Powering supported on primes of \(E\)

Let \(d>0\) and suppose every prime divisor of \(d\) divides \(E\). Since
\(\gcd(|T|,E)=1\), one also has

\[
\gcd(|T|,d)=1.
\]

Powering by \(d\) is therefore an automorphism of the finite abelian group
\(T\). Its restrictions to both local projections are also automorphisms.
For every \(x\in T\),

\[
x_p^d=1\iff x_p=1,
\qquad
x_q^d=1\iff x_q=1.
\]

Repeated \(N-1\) powers correspond to \(d=E^t\), whose prime support is
contained in that of \(E\). Every puncture

\[
d=E/\ell^j
\]

with \(\ell^j\mid E\) is a positive divisor of \(E\) and has the same
property; removing several prime powers or composing such powers also
introduces no prime outside the support of \(E\). Thus the claim covers all
the stated repeated and punctured powers, including the identity exponent
\(d=1\).

## 6. An infinite Dirichlet/CRT family

Fix a positive numerical bound \(H\).

First require a prime \(p\) to satisfy

\[
p\equiv3\pmod4,
\qquad
p\equiv5\pmod6.
\]

CRT combines these conditions into

\[
p\equiv11\pmod{12}.
\]

The residue class is reduced because \(\gcd(11,12)=1\). Dirichlet's theorem
therefore supplies arbitrarily large primes in it. Choose one with

\[
A=\frac{p-1}{2}>H.
\]

Writing \(p=12u+11\) gives

\[
A=6u+5.
\]

Thus \(A\) is odd and \(3\nmid A\).

Now consider the progression

\[
q\equiv3\pmod{4A}. \tag{8}
\]

It is a reduced residue class: \(A\) is odd, and \(3\nmid A\), so

\[
\gcd(3,4A)=1.
\]

Dirichlet's theorem supplies arbitrarily large primes in (8). Choose
\(q>p\) and

\[
B=\frac{q-1}{2}>H.
\]

Writing \(q=3+4At\) gives

\[
B=1+2At.
\]

Therefore \(B\) is odd and

\[
B\equiv1\pmod A.
\]

It follows that

\[
\gcd(A,B)=1.
\]

The primes are distinct and odd, and

\[
\gcd(p-1,q-1)
=\gcd(2A,2B)
=2.
\]

Thus \(g=2\). Finally,

\[
E=pq-1
=2(2AB+A+B).
\]

The factor inside parentheses is congruent to \(B\) modulo \(A\) and to
\(A\) modulo \(B\), so it is coprime to \(AB\). Both \(A\) and \(B\) are
odd, hence \(AB\) is also coprime to the leading factor \(2\). Therefore

\[
\gcd(AB,E)=1.
\]

This proves the required existence for every \(H\), with both residual
orders arbitrarily large.

## 7. Fixed cases

### \(N=4033\)

\[
4033=37\cdot109,
\qquad
p-1=36,
\qquad
q-1=108.
\]

Hence

\[
g=\gcd(36,108)=36,
\qquad
(A,B)=(1,3).
\]

Also \(E=4032\), which is divisible by \(3\). The first fixed claim is
correct.

### \(N=2047\)

\[
2047=23\cdot89,
\qquad
p-1=22,
\qquad
q-1=88.
\]

Thus

\[
g=22,
\qquad
(A,B)=(1,4).
\]

The exponent \(E=2046\) is even, so \(2\mid E\). The second fixed claim is
correct.

### \(N=2773\)

\[
2773=47\cdot59,
\qquad
p-1=46,
\qquad
q-1=58.
\]

Both \(47\) and \(59\) are prime, and

\[
g=\gcd(46,58)=2,
\qquad
(A,B)=(23,29).
\]

Moreover,

\[
E=2772=2^2\cdot3^2\cdot7\cdot11.
\]

Neither \(23\) nor \(29\) divides this factorization, so

\[
\gcd(23\cdot29,2772)=1.
\]

All fixed arithmetic is correct.

## 8. Exact algorithmic scope

On a batch that genuinely generates the full powered rectangle \(S\),
canonical feedback can still enlarge or otherwise change the unpowered
subgroup \(K\), and the first few powered images can contain transient
components. For every intermediate state \(S\le K\le G\), however, the
public \(n\)-round operation sends it to the same stable core \(T\).

Furthermore, any later power whose prime support is contained in that of
\(N-1\) acts invertibly on \(T\) and cannot change which local components
are identities. This is only a structural stability statement.

The result does not give public coordinates for the two hidden axes, make a
large axis element accessible, or bound the size or sampling density of
\(T\). It does not provide a factoring algorithm or computational lower
bound. Feedback can still expose useful integer information or transient
states before stabilization; none of those operations is ruled out.
