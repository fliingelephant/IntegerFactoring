# F208 blind reconstruction

## Protocol and scope

This reconstruction uses only the repository prompt and the frozen F208
statement. The checked SHA-256 digest of the statement is

```text
e036b99dd345aacad134e716929e410a3ed083d601d7a5d50cf013957522f330
```

The global prompt asks for a classical Las Vegas quasipolynomial-time
factorization algorithm for every integer. F208 does not supply such an
algorithm. Its exact scope is the promised input

\[
N=pq,\qquad p<q<2p,
\]

where \(p,q\) are distinct odd primes. Set

\[
B=\lfloor\sqrt N\rfloor,\qquad \chi=\chi_4,\qquad
\eta=\chi(N)=\chi(p)\chi(q)\in\{1,-1\},
\]

and

\[
J_d(N)=\left\lfloor\frac Nd\right\rfloor-
       \left\lfloor\frac{N-1}{d}\right\rfloor.
\]

The two floors differ exactly when \(d\mid N\), so

\[
J_d(N)=\mathbf 1_{d\mid N}.
\]

The coefficient under study is

\[
A(N)=\sum_{d\mid N}d\chi(d).
\]

## 1. Reciprocal-floor divisor pairing and the sign

Because \(N\) is not a square, every divisor belongs to exactly one pair
\(\{d,N/d\}\) with \(d\le B<N/d\). For a divisor \(d\mid N\), all relevant
integers are odd and

\[
\chi(N/d)=\chi(N)\chi(d)=\eta\chi(d).
\]

The contribution of its pair is therefore

\[
d\chi(d)+\frac Nd\chi(N/d)
=\chi(d)\left(d+\eta\frac Nd\right).
\]

Inserting the exact divisor indicator gives the reciprocal-floor identity

\[
\boxed{
A(N)=\sum_{d\le B}\chi(d)
\left(d+\eta\left\lfloor\frac Nd\right\rfloor\right)J_d(N).}
\]

Only \(d=1,p\) survive below \(\sqrt N\). The \(d=1\) pair is public and
equals \(1+\eta N\). Thus, for

\[
T=A(N)-(1+\eta N),
\]

one gets

\[
\boxed{T=\chi(p)(p+\eta q).}
\]

If \(\eta=1\), the parenthesis is positive. If \(\eta=-1\), it is
\(p-q<0\). Hence in both cases

\[
\boxed{\operatorname{sgn}T=\eta\chi(p)=\chi(q).}
\]

Deleting the public event \(d=1\) instead gives the exact selector

\[
\boxed{
\chi(p)=\sum_{2\le d\le B}\chi(d)J_d(N).}
\]

In the opposite-character branch, equivalently \(N\equiv3\pmod4\),
\(\eta=-1\), so the corrected value specializes to

\[
\boxed{T=A(N)-(1-N)=\chi(p)(p-q).}
\]

This is a relocation of the character bit to a signed divisor-event OR. It
does not evaluate that OR.

## 2. Totalized floor reciprocity and its interval selector

For odd \(d\), define

\[
\begin{aligned}
\Delta_N(d)
&=\sum_{i=1}^{(N-1)/2}\left\lfloor\frac{id}{N}\right\rfloor
 +\sum_{j=1}^{(d-1)/2}\left\lfloor\frac{jN}{d}\right\rfloor\\
&\qquad-\frac{(d-1)(N-1)}4.
\end{aligned}
\]

Let \(g=\gcd(d,N)\). Consider the rectangle

\[
1\le i\le\frac{N-1}{2},\qquad
1\le j\le\frac{d-1}{2}.
\]

The first floor sum counts its points satisfying \(Nj\le di\), and the
second counts those satisfying \(di\le Nj\). Every point is counted once,
except a point on \(di=Nj\), which is counted twice. Writing
\(N=gN'\), \(d=gd'\), the equality points are

\[
(i,j)=(N't,d't),\qquad 1\le t\le\frac{g-1}{2}.
\]

Consequently the excess over the rectangle size is exactly
\((g-1)/2\):

\[
\boxed{\Delta_N(d)=\frac{\gcd(d,N)-1}{2}.}
\]

Balance gives the precise inequalities

\[
\boxed{\frac B2<p\le B<2p.}
\]

Indeed \(p<\sqrt N\) gives \(p\le B\), while \(q<2p\) gives
\(B<\sqrt2p<2p\). If \(B/2<d\le B\) and \(\gcd(d,N)>1\), then \(d\)
cannot be divisible by \(q>B\). It must be divisible by \(p\), and
\(d<2p\) forces \(d=p\). Thus \(p\) is the unique integer in that interval
with a nontrivial gcd with \(N\). It is odd, and totalized reciprocity yields

\[
\boxed{
2\sum_{\substack{B/2<d\le B\\d\ \mathrm{odd}}}
\chi(d)\Delta_N(d)=\chi(p)(p-1).}
\]

The absolute value of this aggregate, plus one, is \(p\). This exact
aggregate is therefore factoring-equivalent on the promised inputs. The
identity is not an efficient evaluator: termwise Euclidean evaluation uses
\(2^{\Theta(\log N)}\) candidate values of \(d\).

## 3. Dedekind reduction and cotangent poles

Use the sawtooth function

\[
((x))=\begin{cases}
x-\lfloor x\rfloor-\tfrac12,&x\notin\mathbb Z,\\
0,&x\in\mathbb Z,
\end{cases}
\]

and

\[
s(h,k)=\sum_{r=0}^{k-1}
\left(\left(\frac rk\right)\right)
\left(\left(\frac{hr}{k}\right)\right).
\]

Let \(g=\gcd(h,k)\), \(h=gh'\), and \(k=gk'\). Group
\(r=a+tk'\), with \(0\le a<k'\) and \(0\le t<g\). The second sawtooth is
independent of \(t\), and the sawtooth distribution identity gives

\[
\sum_{t=0}^{g-1}
\left(\left(\frac{a+tk'}{gk'}\right)\right)
=\left(\left(\frac a{k'}\right)\right).
\]

Therefore

\[
\boxed{s(h,k)=s(h/g,k/g).}
\]

For \(g=1\), the classical expression

\[
s(h,k)=\frac1{4k}\sum_{r=1}^{k-1}
\cot\left(\frac{\pi r}{k}\right)
\cot\left(\frac{\pi hr}{k}\right)
\]

is nonsingular. For \(g>1\), the second cotangent has a pole exactly when
\(k\mid hr\), namely at

\[
\boxed{r=j\,k/g,\qquad 1\le j<g.}
\]

There are exactly \(g-1\) such poles. Thus continued-fraction reciprocity
either operates at the full modulus on a unit slope, or first contracts by
the gcd. At \((h,k)=(p,N)\), contraction gives \((1,q)\), but only after
the hidden proper gcd \(p\) has already been extracted. This leaves open a
compressed aggregate of unit-slope Dedekind sums and nonlinear use of their
exact rational values.

## 4. The triangular HNF determinant shell

Adopt the triangular Hermite-normal-form convention

\[
H_{a,b,d}=\begin{pmatrix}d&b\\0&a\end{pmatrix},
\qquad a,d>0,\quad 0\le b<a.
\]

For fixed \(a,d\), there are exactly \(a\) values of \(b\). Therefore the
determinant-\(N\) weighted count is

\[
\boxed{
\sum_{\substack{ad=N\\0\le b<a}}\chi(a)
=\sum_{a\mid N}a\chi(a)=A(N).}
\]

For the cumulative region

\[
\mathcal C(X)=
\sum_{\substack{a,d\ge1\\ad\le X}}
\sum_{0\le b<a}\chi(a),
\]

the adjacent shell is consequently

\[
\boxed{A(N)=\mathcal C(N)-\mathcal C(N-1).}
\]

A hyperbola rearrangement of the cumulative lattice region does not change
the fact that this adjacent determinant shell is the same divisor jump
\(J_d(N)\) from the reciprocal-floor identity.

## 5. The diagonal reduced quadratic form and its class

The form

\[
\boxed{[p,0,q]}
\]

is positive definite and primitive, and its discriminant is

\[
0^2-4pq=-4N.
\]

It is reduced because \(0\le p<q\), and it is ambiguous because changing
the sign of its middle coefficient leaves it unchanged. A literal diagonal
form \([a,0,c]\) of this discriminant satisfies \(ac=N\). With \(a\le c\),
the only possibilities are

\[
\boxed{[1,0,N]\quad\text{and}\quad[p,0,q].}
\]

The first is the public principal form. The second represents \(p\) via
\((1,0)\). The principal form cannot represent \(p\): an equality
\(x^2+Ny^2=p\) has \(y=0\), since otherwise its left side is at least
\(N>p\), and then it would require \(x^2=p\). Hence \([p,0,q]\) is not in
the principal class. Its leading coefficient has character \(\chi(p)\).

Locating this nontrivial diagonal reduced form therefore returns the factor
itself, not a smaller public class-group state. This does not rule out an
implicit class-group statistic that extracts only the character bit.

## 6. Pair-symmetric cancellation and \(r_2\)

Let a divisor weight obey

\[
W_N(d)=W_N(N/d).
\]

When \(\eta=-1\), the two terms in every complementary divisor pair cancel:

\[
\chi(d)W_N(d)+\chi(N/d)W_N(N/d)
=\chi(d)W_N(d)+\eta\chi(d)W_N(d)=0.
\]

Thus

\[
\boxed{\sum_{d\mid N}\chi(d)W_N(d)=0\qquad(\eta=-1).}
\]

This applies to every representation total whose divisor formula has the
declared pair-symmetric twisted weight. The asymmetric choice
\(W_N(d)=d\) in \(A(N)\) is what retains the orientation.

For the ordinary signed-and-ordered two-square representation count,

\[
\boxed{r_2(N)=4(1+\chi(p))(1+\chi(q)).}
\]

If \(\eta=1\), then \(\chi(q)=\chi(p)\), and

\[
\boxed{r_2(N)=8(1+\chi(p)).}
\]

Thus it is \(16\) when both primes are \(1\bmod4\), and zero when both are
\(3\bmod4\); on this branch, two-square representability restates the sign
selector. If \(\eta=-1\), the two characters are opposite and

\[
\boxed{r_2(N)=0}
\]

for both orientations. No algorithm for deciding the needed representation
predicate is obtained.

## 7. Exact magnitude and the difference-of-squares witness

Since \(|\chi(p)|=1\), the corrected magnitude is

\[
\boxed{
|T|=\begin{cases}
p+q,&\eta=1,\\
q-p,&\eta=-1.
\end{cases}}
\]

It follows that

\[
\boxed{|T|^2-4N=(q-p)^2\qquad(\eta=1)}
\]

and

\[
\boxed{|T|^2+4N=(p+q)^2\qquad(\eta=-1).}
\]

In the first branch, \(|T|\) gives \(p+q\) and the displayed square gives
\(q-p\). In the second, \(|T|\) gives \(q-p\) and the displayed square
gives \(p+q\). In either case

\[
p=\frac{(p+q)-(q-p)}2,\qquad
q=\frac{(p+q)+(q-p)}2.
\]

Thus exact magnitude extraction returns the ordinary difference-of-squares
witness and already factors the promised input. It is not a smaller
recursive child.

## Exact remaining gap

All seven models relocate the same hidden event or expose a quantity that is
already factoring-equivalent. The one-bit target that remains is an implicit
evaluation of

\[
\boxed{\sum_{2\le d\le B}\chi(d)J_d(N)}
\]

without locating the unique nonzero proper-divisor event term by term. F208
provides no evaluator, no selector algorithm, and no top-level factoring
result. It proves no lower bound against nonlinear integer algorithms,
compressed signed divisor-OR evaluation, adaptive floor or cotangent
aggregates, implicit class-group navigation, asymmetric representation
statistics, or a future one-child recursive construction. In particular,
nonlinear integer statistics, adaptive signed aggregates, support-preserving
smaller children, and globally nested recursive selectors remain open.
