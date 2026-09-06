# F212 proof

## 1. Elementary interval bounds

Write \(t=\sqrt N\). Since \(N\) is odd,

\[
\lfloor N/2\rfloor=\frac{N-1}{2}.
\]

The definitions give

\[
t-1<B\leq t,
\]

\[
L\leq\sqrt{N/2}+1=\frac{t}{\sqrt2}+1,
\]

and

\[
\sqrt2\,t-2<U\leq\sqrt{2N-1}<\sqrt2\,t.
\]

The lower bound on \(U\) follows from

\[
\lfloor\sqrt{2N-1}\rfloor
>\sqrt{2N-1}-1
>\sqrt{2N}-2.
\]

Consequently

\[
B-L>\left(1-\frac1{\sqrt2}\right)t-2
\]

and

\[
U-(B+1)>(\sqrt2-1)t-3.
\]

## 2. Odd representatives and their step

Fix \(z\in U(m)\). If \(m\) is even, then \(z\) is odd and the odd integers
congruent to \(z\bmod m\) have step \(m\). If \(m\) is odd, parity alternates
between consecutive lifts and the odd lifts have step \(2m\). Thus, in both
cases, the odd lifts form one residue class of step

\[
s=\operatorname{lcm}(2,m).
\]

Any integer interval of span at least \(s-1\) meets every compatible residue
class. If it meets a class, its first member is less than the lower endpoint
plus \(s\), and its last member is greater than the upper endpoint minus
\(s\).

Because \(\gcd(m,N)=1\), \(y_x=Nx^{-1}\bmod m\) is also a unit. Therefore
the same observations apply simultaneously to \(x\) and \(y_x\).

## 3. Proof of Theorem 1

Assume \(t\geq32\) and \(s\leq t/8\). The lower bounds from Section 1 give

\[
B-L>\left(1-\frac1{\sqrt2}\right)t-2\geq s-1
\]

and

\[
U-(B+1)>(\sqrt2-1)t-3\geq s-1.
\]

The final inequalities already hold for \(t\geq32\). Hence every unit class
meets both factor intervals.

For every \(x\in U(m)\), Section 2 and the bounds on \(B,L,U\) give

\[
\begin{aligned}
P_x^-Q_x^-
&<(L+s)(B+1+s)\\
&\leq
\left(\left(\frac1{\sqrt2}+\frac18\right)t+1\right)
\left(\frac98t+1\right).
\end{aligned}
\]

The quadratic coefficient on the last line is

\[
\left(\frac1{\sqrt2}+\frac18\right)\frac98<1.
\]

At \(t=32\), \(t^2\) minus the displayed product is

\[
839-592\sqrt2>0,
\]

where positivity follows by squaring:
\(839^2-2\cdot592^2=2993>0\). Its derivative as a function of \(t\) is
positive for \(t\geq32\): the quadratic coefficient of the difference is
greater than \(1/16\), while the magnitude of its linear coefficient is less
than \(2\). Thus the last product is less than \(t^2=N\) for every
\(t\geq32\).

Similarly,

\[
\begin{aligned}
P_x^+Q_x^+
&>(B-s)(U-s)\\
&>
\left(\frac78t-1\right)
\left(\left(\sqrt2-\frac18\right)t-2\right).
\end{aligned}
\]

The quadratic coefficient is

\[
\frac78\left(\sqrt2-\frac18\right)>1,
\]

and its excess over \(1\) is greater than \(1/8\), since
\(56\sqrt2>79\). The magnitude of the linear coefficient is less than
\(25/8\). Hence the product minus \(t^2\) is greater than

\[
\frac{t^2-25t}{8}+2>0
\]

for \(t\geq32\). Thus every unit class also passes the endpoint product test,
and

\[
\mathcal F_N(m)=U(m).
\]

The asymptotic statement follows because
\(s(m_i)/\sqrt{N_i}\to0\) eventually implies both \(N_i\geq1024\) and
\(s(m_i)\leq\sqrt{N_i}/8\). Since \(s(m)\leq2m\), \(m=o(\sqrt N)\) is a
sufficient hypothesis.

For completeness, the elementary inequality

\[
\varphi(m)\geq\sqrt{m/2}
\]

holds for every \(m\geq1\). One proof checks prime powers and multiplies:
for odd \(\ell^a\),
\(\varphi(\ell^a)^2/\ell^a=\ell^{a-2}(\ell-1)^2\geq1\), while the total
loss from the \(2\)-power component is at most the displayed factor \(2\).
This yields the explicit-frontier corollary.

## 4. Proof of Theorem 2

Two distinct members of one nonempty odd progression differ by at least
\(s\). If

\[
s>\max\{B-L,U-(B+1)\},
\]

each progression appearing in the frontier definition therefore has at
most one member. Write the two singleton members as \(X\in P\) and
\(Y\in Q\). The endpoint condition becomes

\[
XY\leq N\leq XY,
\]

which is equivalent to \(XY=N\). Conversely, if \(X\in P\), \(Y=N/X\in Q\),
and \(X\mid N\), then the two residues obey

\[
Y\equiv NX^{-1}\pmod m
\]

because \(X\) is a unit modulo \(m\), and their singleton progressions pass
the endpoint equality. This proves the exact set identity.

Under the balanced-semiprime promise, only \(X=p,Y=q\) lie in the ordered
factor intervals. Finally \(W_P,W_Q=O(\sqrt N)\) and \(s(m)\geq m\), so
\(m/\sqrt N\to\infty\) implies the singleton hypothesis eventually.

## 5. Proof of Theorem 3

Since \(K\mid N-1\), one has

\[
\gcd(K,N)=1
\qquad\hbox{and}\qquad
N\equiv1\pmod K.
\]

Every promised input has \(N\geq15\), and

\[
K=\frac{N-1}{2}>\sqrt{2N-1}\geq U.
\]

Indeed the squared inequality is \(N^2-10N+5>0\), which holds for
\(N\geq15\). Thus each residue class modulo \(K\) has at most one
representative in either factor interval.

For \(X\in P\), the definition of \(L\) implies

\[
X^2>\frac{N-1}{2}.
\]

For \(Y\in Q\), one has \(Y>B\), hence \(Y>\sqrt N\). Therefore

\[
XY>\sqrt{\frac{N(N-1)}2}>\frac{N+1}{2}=N-K
\]

for \(N\geq5\). At the other endpoint,

\[
XY\leq B U<\sqrt{N(2N-1)}<\frac{3N-1}{2}=N+K.
\]

The last strict inequality follows after squaring from

\[
4N(2N-1)< (3N-1)^2,
\]

whose difference is \((N-1)^2>0\). Thus

\[
|XY-N|<K.
\]

If \(XY\equiv N\pmod K\), the only multiple of \(K\) in this open interval
is zero, so \(XY=N\). The converse is immediate.

For any positive integer \(X\),

\[
\left\lfloor\frac NX\right\rfloor
-\left\lfloor\frac{N-1}{X}\right\rfloor
=\mathbf1_{X\mid N}.
\]

If \(L\leq X\leq B\) and \(X\mid N\), put \(Y=N/X\). Since \(N\) is not a
square, \(Y>B\). Also \(X^2\geq(N+1)/2\), because \(X^2\) is an integer
strictly greater than \((N-1)/2\). Hence

\[
Y^2=\frac{N^2}{X^2}\leq\frac{2N^2}{N+1}\leq2N-1,
\]

so \(Y\leq U\). Thus every divisor counted by the floor jump gives exactly a
frontier branch, and Section 4 proves the reverse implication. This proves
the divisor-spike identity.

For the quotient-partition statement, if \(L\leq X<B\), then

\[
X(X+1)\leq B(B-1)<B^2\leq N.
\]

Therefore

\[
\frac NX-\frac N{X+1}
=\frac{N}{X(X+1)}\geq1,
\]

and consequently

\[
\left\lfloor\frac NX\right\rfloor
>\left\lfloor\frac N{X+1}\right\rfloor.
\]

The interval contains

\[
B-L+1=\Theta(\sqrt N)
\]

integers, so the ordinary equal-quotient partition has that many blocks.

## 6. The exact Coppersmith dependency

We use the following standard univariate unknown-divisor theorem.

**Unknown-divisor Coppersmith theorem.** Fix constants
\(0<\beta\leq1\), \(\delta\geq1\), and \(\eta>0\). Given an integer \(N\)
and a monic \(f\in\mathbb Z[T]\) of degree \(\delta\), deterministic lattice
reduction finds, in time polynomial in \(\log N\) for fixed parameters, every
integer \(t_0\) satisfying

\[
|t_0|\leq N^{\beta^2/\delta-\eta}
\]

for which there exists a divisor \(D\mid N\) with

\[
D\geq N^\beta
\qquad\hbox{and}\qquad
f(t_0)\equiv0\pmod D.
\]

F212 uses this theorem only for degree \(\delta=1\), fixed constants, and the
balanced divisor \(D=p\) or \(q\). It does not invoke an unproved general
bivariate small-root heuristic.

## 7. Proof of Theorem 4

It is enough to treat \(0<\varepsilon\leq1/8\), because replacing a larger
\(\varepsilon\) by \(1/8\) weakens the modulus lower bound. Consider a listed
pair whose residue contains \(p\). Write

\[
p=r+mt,\qquad
0\leq t<\frac{p}{m}<\frac{\sqrt N}{m}
\leq N^{1/4-\varepsilon}.
\]

The balance promise gives

\[
p>\sqrt{N/2}.
\]

Choose the fixed constant

\[
\beta=\frac12-\frac\varepsilon4.
\]

For all sufficiently large \(N\),

\[
p>\sqrt{N/2}\geq N^\beta.
\]

Moreover

\[
\beta^2-\left(\frac14-\frac\varepsilon2\right)
=\frac{\varepsilon}{4}+\frac{\varepsilon^2}{16}>0.
\]

Choose any fixed Coppersmith margin \(\eta\) strictly between zero and this
difference. Then

\[
|t|\leq N^{1/4-\varepsilon}
\leq N^{1/4-\varepsilon/2}
\leq N^{\beta^2-\eta}
\]

for all sufficiently large \(N\).

Compute

\[
c\equiv r m^{-1}\pmod N
\]

and use the monic linear polynomial

\[
f(T)=T+c.
\]

Modulo \(p\),

\[
m f(t)\equiv mt+r=p\equiv0\pmod p.
\]

Since \(\gcd(m,p)=1\), \(f(t)\equiv0\pmod p\). The theorem in Section 6
therefore returns \(t\). Compute

\[
\gcd(r+mt,N)
\]

to obtain the proper factor.

If the correct listed residue contains \(q\), then

\[
q<\sqrt{2N}
\quad\hbox{and}\quad
t<\sqrt2\,N^{1/4-\varepsilon}.
\]

For sufficiently large \(N\),
\(\sqrt2\,N^{1/4-\varepsilon}\leq N^{1/4-\varepsilon/2}\), while
\(q>\sqrt N\geq N^\beta\). Thus the same \(\beta,\eta\) and the identical
monic-linear argument recover \(q\).

There are only \(Q(n)\) listed pairs. Their moduli have \(O(n)\) bits by the
assumption \(m_j\leq N^{O(1)}\). A QP number of polynomial-time lattice and
gcd calls is numerical QP, proving the terminal theorem. Finitely many small
inputs excluded while choosing \(N\) sufficiently large can be absorbed into
a fixed lookup or direct trial division.

## 8. Exact Fourier identity and its scope

Let

\[
e_m(z)=e^{2\pi iz/m},\qquad
\widehat f(a)=\sum_{z\bmod m}f(z)e_m(-az).
\]

Fourier inversion gives

\[
f(x)=\frac1m\sum_{a\bmod m}\widehat f(a)e_m(ax),
\]

and similarly for \(g\). Substitution into

\[
\sum_{x\in U(m)}f(x)g(Nx^{-1})
\]

gives exactly

\[
\frac1{m^2}\sum_{a,b\bmod m}
\widehat f(a)\widehat g(b)
\sum_{x\in U(m)}e_m(ax+bNx^{-1}).
\]

The inner sum is \(K_m(a,bN)\). This proves the displayed identity in the
statement. The identity alone supplies neither a short exact sum nor a lower
bound against one. Standard square-root estimates are error bounds for
approximate distribution; they do not determine an exact zero or one. The
F209 endpoint product predicate is not a product \(f(x)g(y_x)\), so it is not
even included without an additional decomposition.

## 9. Adaptive-order scope

Theorem 1 is independent of the factorization of \(m\), the public CRT root,
and the order in which components were accumulated. Thus every prefix in
its uniform range has the entire unit torsor. Theorem 2 is equally
order-independent and identifies the endpoint predicate with exact
divisibility once both progressions are singleton.

It follows that changing only the component order cannot repair the two
literal F209 generators: explicit expansion must construct the unit states
in the first range, and the interval fallback examines
\(\Theta(\sqrt N)\) representatives. This conclusion says nothing about a
new implicit representation which crosses the transition without
materializing either set.
