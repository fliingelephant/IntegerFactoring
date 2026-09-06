# F212 V2 proof

## 1. Interval bounds

Write \(t=\sqrt N\). Since \(N\) is odd,

\[
\lfloor N/2\rfloor=\frac{N-1}{2}.
\]

The definitions imply

\[
t-1<B\leq t,
\qquad
L\leq\frac{t}{\sqrt2}+1,
\qquad
\sqrt2\,t-2<U<\sqrt2\,t.
\]

Therefore

\[
B-L>\left(1-\frac1{\sqrt2}\right)t-2
\]

and

\[
U-(B+1)>(\sqrt2-1)t-3.
\]

## 2. Odd progression step

If \(m\) is even, every unit residue is odd and its odd lifts have step
\(m\). If \(m\) is odd, parity alternates between consecutive lifts and the
odd lifts have step \(2m\). Thus their exact common step is

\[
s=\operatorname{lcm}(2,m).
\]

An inclusive integer interval of span at least \(s-1\) meets each compatible
class. A nonempty class has its first member below the lower endpoint plus
\(s\), and its last member above the upper endpoint minus \(s\).

Since \(\gcd(m,N)=1\), \(Nx^{-1}\bmod m\) is a unit whenever \(x\) is.

For the F207 coordinates, \(R^2\equiv N\pmod m\) and \(R\in U(m)\) give

\[
N(Ru)^{-1}\equiv Ru^{-1}\pmod m.
\]

Thus multiplication by \(R\) is the claimed frontier bijection.

## 3. Proof of Theorem 1

Assume \(t\geq32\) and \(s\leq t/8\). Section 1 gives

\[
B-L\geq s-1,
\qquad
U-(B+1)\geq s-1,
\]

so every unit class meets both intervals.

Uniformly in the unit \(x\),

\[
\begin{aligned}
P_x^-Q_x^-
&<(L+s)(B+1+s)\\
&\leq
\left(\left(\frac1{\sqrt2}+\frac18\right)t+1\right)
\left(\frac98t+1\right).
\end{aligned}
\]

At \(t=32\), \(t^2\) minus the last product is

\[
839-592\sqrt2>0,
\]

because \(839^2-2\cdot592^2=2993\). The difference has positive derivative
for \(t\geq32\): its quadratic coefficient exceeds \(1/16\), while the
magnitude of its linear coefficient is less than \(2\). Hence
\(P_x^-Q_x^-<N\).

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

The quadratic coefficient exceeds \(1+1/8\), because
\(56\sqrt2>79\), while the magnitude of the linear coefficient is less than
\(25/8\). The product minus \(t^2\) is therefore greater than

\[
\frac{t^2-25t}{8}+2>0
\]

for \(t\geq32\). Hence \(P_x^+Q_x^+>N\), proving

\[
\mathcal F_N(m)=U(m).
\]

The sequence statement follows by eventually entering the explicit
\(s/\sqrt N\leq1/8\) range. Since \(s\leq2m\), \(m=o(\sqrt N)\) suffices.

Finally,

\[
\varphi(m)\geq\sqrt{m/2}.
\]

For every odd prime power \(\ell^a\),

\[
\frac{\varphi(\ell^a)^2}{\ell^a}
=\ell^{a-2}(\ell-1)^2\geq1.
\]

The \(2\)-power component contributes a factor at least \(1/2\), proving the
bound multiplicatively.

## 4. Proof of Theorem 2

Two members of one odd lift progression differ by at least \(s\). If

\[
s>\max\{B-L,U-(B+1)\},
\]

each nonempty progression is a singleton. Write its members as \(X\in P\)
and \(Y\in Q\). The endpoint condition becomes

\[
XY\leq N\leq XY,
\]

or \(XY=N\).

Conversely, if \(X\in P\), \(X\mid N\), and \(Y=N/X\in Q\), then
\(\gcd(X,m)=1\) and

\[
Y\equiv NX^{-1}\pmod m.
\]

The two singleton progressions therefore form a live branch. This proves the
set identity.

Balance places \(p\) in \(P\) and \(q\) in \(Q\):

\[
p^2>N/2,\quad p^2<N,\quad q^2>N,\quad q^2<2N.
\]

No other divisor of \(pq\) lies in these ordered intervals. The asymptotic
corollary follows from \(s\geq m\) and both interval spans being
\(O(\sqrt N)\).

## 5. Proof of Theorem 3

For \(K=(N-1)/2\),

\[
\gcd(K,N)=1,\qquad N\equiv1\pmod K.
\]

Every promised input has \(N\geq15\), and

\[
K>\sqrt{2N-1}\geq U,
\]

because \(N^2-10N+5>0\). Thus each interval contains at most one
representative of a residue class modulo \(K\).

For \(X\in P,\ Y\in Q\),

\[
XY>\sqrt{\frac{N(N-1)}2}>\frac{N+1}{2}=N-K
\]

and

\[
XY\leq BU<\sqrt{N(2N-1)}<\frac{3N-1}{2}=N+K.
\]

The last inequality follows because the squared right side minus the
squared left side is \((N-1)^2/4>0\). Hence

\[
|XY-N|<K.
\]

Congruence modulo \(K\) therefore forces \(XY=N\), and the converse is
immediate.

For every positive integer \(X\),

\[
\left\lfloor\frac NX\right\rfloor
-\left\lfloor\frac{N-1}{X}\right\rfloor
=\mathbf1_{X\mid N}.
\]

If \(L\leq X\leq B\) divides \(N\), then \(Y=N/X>B\), because \(N\) is not a
square. Moreover \(X^2\geq(N+1)/2\), so

\[
Y^2\leq\frac{2N^2}{N+1}\leq2N-1.
\]

Thus \(Y\leq U\), proving the exact divisor-spike identity.

For \(L\leq X<B\),

\[
X(X+1)\leq B(B-1)<B^2\leq N.
\]

Therefore

\[
\frac NX-\frac N{X+1}\geq1
\]

and \(\lfloor N/X\rfloor\) strictly decreases. Since
\(B-L+1=\Theta(\sqrt N)\), ordinary equal-quotient grouping has that many
blocks.

## 6. Imported univariate unknown-divisor theorem

V2 uses the following standard theorem.

**Unknown-divisor Coppersmith theorem.** Fix constants
\(0<\beta\leq1\), \(\delta\geq1\), and \(\eta>0\). Given \(N\) and a monic
polynomial \(f\in\mathbb Z[T]\) of degree \(\delta\), deterministic lattice
reduction finds, in time polynomial in the bit lengths of \(N\) and the
coefficients of \(f\), every integer \(t_0\) satisfying

\[
|t_0|\leq N^{\beta^2/\delta-\eta}
\]

for which there is a divisor \(D\mid N\) with

\[
D\geq N^\beta,
\qquad
f(t_0)\equiv0\pmod D.
\]

V2 uses only fixed degree \(\delta=1\) and fixed constants. It invokes no
general bivariate small-root heuristic.

## 7. Proof of Theorem 4A

It is enough to consider \(0<\varepsilon\leq1/8\); for larger
\(\varepsilon\), use the weaker fixed value \(1/8\).

Process each explicit list entry independently. Its syntax, binary lengths,
range \(0\leq r<m\), and \(\gcd(m,N)=1\) promise can be checked in polynomial
bit complexity in \(n+\log m\). Since \(m\leq N^C\),

\[
\log_2 m\leq C\log_2 N=O(n).
\]

Thus every checked entry has \(O(n)\) bits.

Write the fixed rational exponent \(1/4+\varepsilon=A/D\) in lowest terms.
The lower modulus bound is checked exactly by comparing \(m^D\) with
\(N^A\); the upper bound is checked by comparing \(m\) with \(N^C\).
All exponents are fixed, so these operands have \(O_{C,\varepsilon}(n)\)
bits and both checks take polynomial bit complexity.

Suppose first that a checked entry satisfies

\[
p\equiv r\pmod m.
\]

Write

\[
p=r+mt.
\]

Then

\[
0\leq t<\frac{\sqrt N}{m}\leq N^{1/4-\varepsilon}.
\]

Choose

\[
\beta=\frac12-\frac\varepsilon4.
\]

For all sufficiently large \(N\), balance gives

\[
p>\sqrt{N/2}\geq N^\beta.
\]

Also

\[
\beta^2-\left(\frac14-\frac\varepsilon2\right)
=\frac\varepsilon4+\frac{\varepsilon^2}{16}>0.
\]

Fix a theorem margin \(\eta\) smaller than this difference. Then

\[
|t|\leq N^{1/4-\varepsilon}
\leq N^{1/4-\varepsilon/2}
\leq N^{\beta^2-\eta}.
\]

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
mf(t)\equiv mt+r=p\equiv0\pmod p.
\]

Since \(m\) is a unit modulo \(p\), \(f(t)\equiv0\pmod p\). The imported
theorem returns \(t\), and

\[
\gcd(r+mt,N)=p.
\]

If the correct residue contains \(q\), then

\[
0\leq t<\frac{\sqrt{2N}}m
\leq\sqrt2\,N^{1/4-\varepsilon}
\leq N^{1/4-\varepsilon/2}
\]

for sufficiently large \(N\). Also \(q>\sqrt N\geq N^\beta\). The same
\(\beta,\eta\) and monic normalization recover \(q\).

The Coppersmith routine may return a polynomial-size root list for each
entry. Test each returned integer by computing \(r+mt\), its gcd with \(N\),
and whether that gcd is proper. Incorrect residue entries cause no
soundness problem; only a nontrivial verified gcd is returned.

There are at most \(Q(n)\) entries. Each has \(O(n)\) bits. Therefore:

1. reading the list costs \(Q(n)O(n)\) bit operations;
2. checking the entry count, field encodings, size bounds, residue ranges,
   and gcd promises costs \(Q(n)\operatorname{poly}(n)\);
3. modular inverses and construction of the degree-one polynomials cost
   \(Q(n)\operatorname{poly}(n)\);
4. fixed-parameter univariate Coppersmith calls cost
   \(Q(n)\operatorname{poly}(n)\); and
5. all candidate multiplications and gcd verifications cost
   \(Q(n)\operatorname{poly}(n)\).

Their sum is numerical QP. Finitely many small inputs excluded by the fixed
asymptotic inequalities can be absorbed by fixed trial division.

This proves QP postprocessing of the granted explicit list. No cost for
constructing the auxiliary list is silently included.

## 8. Proof of Corollary 4B

By premise, \(G\) runs in numerical QP time and outputs the explicit list in
Theorem 4A's binary format. A machine cannot serialize more bits than its
runtime permits; independently, the stated list and modulus bounds give
total output length

\[
Q(n)O_C(n).
\]

Run \(G\), then the postprocessor from Theorem 4A. The first stage is QP by
hypothesis. The second is QP by Theorem 4A. The sum and composition of two
fixed numerical quasipolynomial bounds is numerical QP.

Every returned factor is verified by exact gcd and division. Thus the
composition is a deterministic end-to-end QP factoring algorithm on the
promise.

## 9. Exact Fourier identity and scope

With

\[
e_m(z)=e^{2\pi iz/m},
\qquad
\widehat f(a)=\sum_{z\bmod m}f(z)e_m(-az),
\]

Fourier inversion gives

\[
\sum_{x\in U(m)}f(x)g(Nx^{-1})
=\frac1{m^2}\sum_{a,b\bmod m}
\widehat f(a)\widehat g(b)
\sum_{x\in U(m)}e_m(ax+bNx^{-1}).
\]

The inner sum is \(K_m(a,bN)\). This is an exact identity, not a QP
evaluator or a lower bound. Approximate square-root errors do not decide an
exact zero or singleton, and the endpoint product predicate needs an
additional nonseparable treatment.

## 10. Adaptive-order scope

Theorem 1 is independent of CRT component order and gives the full unit
torsor throughout its range. Theorem 2 is also order-independent and turns
the endpoint bracket into exact divisibility.

Thus changing only the reveal order does not repair F209's literal explicit
torsor expansion or full interval scan. This statement does not cover a new
compressed representation, adaptive exact counter, meet-in-the-middle
algorithm, or nonlinear decoder.
