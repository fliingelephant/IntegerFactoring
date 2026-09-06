# Proof of the F150 V2 reciprocal-anchor cycle trap

## 1. Residual synchronization

Let \(N\ge3\) be odd and let the setup of `V2_STATEMENT.md` hold. Since
\(x,y\) are units modulo \(N\), their product has a unique least positive
residue. Write

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

The strict bound \(t<y\) follows from \(h<N\), which gives
\(yh<yN\). Reducing (1.3) modulo \(y\) gives

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

This proves Theorem 1. Oddness is not needed for this identity. It is needed
only for the no-factor conclusion from the global root below.

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

Under the P128/P131 convention, divide the positive exact root in (2.1) by
the supplied modular root in (2.2). This gives

\[
\rho
=x^2y^2h(xyh^2)^{-1}
=xyh^{-1}
\equiv1\pmod N,
\]

because \(h\equiv xy\pmod N\). All denominators are units: \(x\) and
\(y\) are units by hypothesis, and \(h\) is a unit because
\(h\equiv xy\pmod N\). The inverse orientation is
\(h(xy)^{-1}\), which has the same value \(1\).

Since \(N\) is odd,

\[
\gcd(\rho-1,N)=N,
\qquad
\gcd(\rho+1,N)=\gcd(2,N)=1.
\]

Thus the cycle cannot produce a proper terminal gcd on the preprocessed odd
branch. This proves Theorem 2.

### Exact-value deletion

For one P128 position, let

\[
A=cw,
\qquad
B=Uw,
\qquad
D=Uc.
\]

The actual retained columns \(A\) and \(B\) are both \(1\pmod N\) and
have supplied root \(1\). The transformed bridge \(D\) instead carries
the indexed supplied root \(c\).

For two equal actual columns \(P_i=P_j=P\), the duplicate direction that
selects both columns is a square dependency with exact product \(P^2\),
positive root \(P\), and normalized root \(P\equiv1\pmod N\). Thus every
duplicate direction lies in the kernel of the normalized-root map. Choosing
one first occurrence is the quotient by these root-\(1\) directions. A
selected later occurrence can be replaced by the retained occurrence
without changing its exact integer or supplied root. If both occurrences
were selected, their duplicate direction cancels with root \(1\). If no
corresponding dependency remains, deletion has removed the dependency
rather than changed its root.

Therefore global exact-value deletion among actual P128 columns cannot turn
this root-\(1\) dependency into a useful root. This argument does not permit
deletion of equal transformed \(D\) values with different indexed supplied
roots.

## 3. Ceiling-reciprocal corollary

Let \(a\in\mathbb Z\), \(1<a<\sqrt N\), put
\(q=\lceil N/a\rceil\), and let \(h=qa-N\). If \(h=0\), then
\(a\mid N\), and \(1<a<\sqrt N\) makes \(a\) a proper gcd. For the
remaining branch, \(h>0\), equivalently \(a\nmid N\), and

\[
qa=N+h,
\qquad
0<h<a.
\tag{3.1}
\]

Since \(a^2<N\), one has \(N/a>a\), and hence \(q>a\). Also
\(a\ge2\), so

\[
q\le\left\lceil\frac N2\right\rceil<N
\]

for odd \(N\ge3\). Now

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
(3.2)--(3.4) satisfy Theorem 1 with \((x,y)=(q,a)\). The normalized root
is therefore \(+1\).

Every operation in this corollary is ordinary integer division,
multiplication, modular reduction, inverse computation, and gcd on
\(O(n)\)-bit values. Applying it to an explicitly generated
quasipolynomial list of integer \(a\)'s has quasipolynomial bit cost.

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

The four sign differences and sums are \(-37,85,12,48\); each has gcd
\(1\) with \(77\). Finally,

\[
(10\cdot8^2)(24)=15{,}360,
\qquad
(8\cdot10^2)(30)=24{,}000,
\]

and their product is \(19{,}200^2\). The exact root \(19{,}200\) and
the supplied root \(720\) are both \(27\pmod{77}\). Hence their
standard normalized ratio is \(+1\).

## 5. Boundary

The proof uses both reciprocal-anchor divisibilities. It does not constrain
nonreciprocal cycles, longer cycles, cross-star factor overlaps,
hypercycles through older columns, signed presentations, or branches that
already factor by parity, endpoint gcd, or sign screens. It is a structural
trap for one natural metric path, not an impossibility theorem for F26-Q.
