# Proof of the F150 reciprocal-anchor cycle trap

## 1. Residual synchronization

Since \(x,y\) are units modulo \(N\), their product has a unique least
positive residue. Write

\[
xy=mN+h,
\qquad
1\le h<N.
\tag{1.1}
\]

Multiplication by \(y\) gives

\[
xy^2=myN+yh.
\]

Hence

\[
[xy^2]_N=[yh]_N.
\tag{1.2}
\]

Write the ordinary quotient-remainder division

\[
yh=tN+[yh]_N=tN+yT,
\qquad
0\le t<y.
\tag{1.3}
\]

The strict bound \(t<y\) follows from \(h<N\), which gives \(yh<yN\).
Reducing (1.3) modulo \(y\) gives

\[
tN\equiv0\pmod y.
\]

Because \(\gcd(y,N)=1\), one has \(y\mid t\). Together with
\(0\le t<y\), this forces \(t=0\). Therefore

\[
yh=yT,
\qquad
T=h,
\qquad
yh<N.
\tag{1.4}
\]

The same argument with \(x,y\) interchanged gives

\[
S=h,
\qquad
xh<N.
\tag{1.5}
\]

This proves Theorem 1.

## 2. Exact square and normalized root

For the first P128 bridge, the unreduced word is \(U_x=xy^2\) and its
canonical residue is \(c_x=yh\). Thus

\[
D_x=U_xc_x=xy^3h.
\]

For the reverse bridge, \(U_y=yx^2\) and \(c_y=xh\), so

\[
D_y=U_yc_y=yx^3h.
\]

Their product is

\[
D_xD_y=x^4y^4h^2=(x^2y^2h)^2.
\tag{2.1}
\]

Each bridge congruence supplies its canonical residue as a modular square
root. The product of the supplied roots is

\[
c_xc_y=(yh)(xh)=xyh^2.
\tag{2.2}
\]

Dividing (2.2) by the positive exact root in (2.1) gives

\[
\rho
=xyh^2(x^2y^2h)^{-1}
=h(xy)^{-1}
\equiv1\pmod N,
\]

because \(h\equiv xy\pmod N\). The inverse convention gives the same
global root. Thus the cycle cannot produce a proper gcd through its
normalized-root image. This proves Theorem 2.

## 3. Ceiling-reciprocal corollary

Let \(1<a<\sqrt N\), put \(q=\lceil N/a\rceil\), and assume \(a\nmid N\).
Then

\[
qa=N+h,
\qquad
0<h<a.
\tag{3.1}
\]

Since \(a^2<N\), one has \(q>a\). Also \(a>1\) gives \(q<N\). Now

\[
qa^2=aN+ah,
\]

and \(0<ah<a^2<N\), so

\[
[qa^2]_N=ah.
\tag{3.2}
\]

Similarly,

\[
aq^2=qN+qh.
\]

Because \(q>h\),

\[
qh\le q(a-1)=qa-q=N+h-q<N.
\tag{3.3}
\]

Thus

\[
[aq^2]_N=qh.
\tag{3.4}
\]

After the ordinary gcd screens certify that \(a\) and \(q\) are units,
(3.2)--(3.4) satisfy Theorem 1 with \((x,y)=(q,a)\). The normalized root is
therefore \(+1\).

Every operation in this corollary is ordinary integer division,
multiplication, modular reduction, and gcd on \(O(n)\)-bit values. Applying
it to a quasipolynomial list of \(a\)'s has quasipolynomial bit cost.

## 4. Exact certificate

For \(N=77\) and \(a=8\),

\[
q=\left\lceil77/8\right\rceil=10,
\qquad
h=80-77=3.
\]

Direct reduction gives

\[
10\cdot8^2=640=8\cdot77+24,
\qquad
8\cdot10^2=800=10\cdot77+30.
\]

Also

\[
24\cdot61=19\cdot77+1,
\qquad
30\cdot18=7\cdot77+1.
\]

The four sign differences and sums are \(-37,85,12,48\); each has gcd 1
with 77. Finally,

\[
(10\cdot8^2)(24)=15{,}360,
\qquad
(8\cdot10^2)(30)=24{,}000,
\]

and their product is \(19{,}200^2\). Since both \(19{,}200\) and 720 are
27 modulo 77, the normalized root is \(+1\).

## 5. Boundary

The proof uses both reciprocal-anchor divisibilities. It does not constrain
nonreciprocal cycles, longer cycles, cross-star factor overlaps, or direct
screens. It is a structural trap for one natural metric path, not an
impossibility theorem for F26-Q.
