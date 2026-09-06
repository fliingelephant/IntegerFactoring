# Proof of the F254 negative-Pell component boundary

## 1. Exact construction identities

From (b^2-2y^2=-1), reduction modulo two shows that (b) and (y) are
odd. Set (T=N+y), (D=T^2-2), and (S=T^2-1). Then

\[
S^2-DT^2
=(T^2-1)^2-(T^2-2)T^2
=1.
\]

Also (D) lies strictly between ((T-1)^2) and (T^2) for (T\ge2), so
it is positive and nonsquare. Canonical reduction sends (T) to (y) and
(S) to (y^2-1) modulo (N). Therefore

\[
(y^2-1)^2\equiv S^2\equiv1+DT^2\equiv1+Dy^2=A\pmod N.
\]

Write (u=(b-1)/2) and (v=(b+1)/2). The negative-Pell equation gives

\[
2u^2=y^2-b,
\qquad
2v^2=y^2+b,
\qquad
2uv=y^2-1.
\]

Hence

\[
\begin{aligned}
A
&=1+(T^2-2)y^2
=(Ty)^2-b^2\\
&=(Ty-b)(Ty+b)\\
&=(yN+2u^2)(yN+2v^2).
\end{aligned}
\]

Modulo (N), a product of (2h) chosen components is

\[
2^{2h}\prod_iw_i^2
=\left(2^h\prod_iw_i\right)^2.
\]

Thus every even component subset that is an exact integer square is a valid
congruence-of-squares certificate with a completely known modular root.

## 2. Affine resultant localization

For (F_i(X)=y_iX+2w_i^2) and
(F_j(X)=y_jX+2w_j^2), direct elimination gives

\[
y_iF_j(X)-y_jF_i(X)
=2(y_iw_j^2-y_jw_i^2).
\]

The right side is the resultant in the stated sign convention. Therefore
every prime dividing both (F_i(N)) and (F_j(N)) divides the public
resultant. The forms are primitive: if a positive integer divides both
(y) and (w\in\{u,v\}), then (b\equiv\pm1) modulo it, while the
negative-Pell equation gives (b^2\equiv-1); the divisor is at most two,
and (y) is odd.

Two primitive linear forms are associates over the rationals exactly when
their resultant is zero. Pairwise nonassociate irreducible factors occur
with exponent one in a product of distinct forms. Such a product cannot be
a square in \(\mathbb Q(X)\). This proves the generic boundary. At an
integer specialization, shared prime rows can occur, but the elimination
identity confines their support to the pairwise resultants.

## 3. Completeness of the (N=143) solution window

Every positive solution of (b^2-2y^2=-1) is generated from ((1,1)) by

\[
(b,y)\longmapsto(3b+4y,\;2b+3y).
\]

For completeness, this follows by descent. If (y>1), then (y\ge5), and

\[
(b',y')=(3b-4y,\;3y-2b)
\]

is a positive integer solution with (0<y'<y). Indeed
(4/3<b/y<3/2) for (y\ge5), and multiplication by
(3-2\sqrt2) preserves norm (-1). Repeating reaches ((1,1)), and the
displayed forward map is inverse to the descent.

Starting from ((1,1)), the consecutive solutions are

\[
(1,1)\mapsto(7,5)\mapsto(41,29)\mapsto(239,169).
\]

Since (5,29<143<169), the admissible condition (1<y<143) selects
exactly the middle two solutions.

## 4. Exact arithmetic certificate

For ((b,y)=(7,5)),

\[
T=148,\qquad D=21902,\qquad S=21903,\qquad u=3,\qquad v=4,
\]

and

\[
F_-(143)=5\cdot143+18=733,
\qquad
F_+(143)=5\cdot143+32=747=3^2\cdot83.
\]

Thus (A=547551), (S\equiv24\pmod{143}), and both sides of the root
congruence are (4\pmod{143}).

For ((b,y)=(41,29)),

\[
T=172,\qquad D=29582,\qquad S=29583,\qquad u=20,\qquad v=21,
\]

and

\[
F_-(143)=29\cdot143+800=4947=3\cdot17\cdot97,
\]

\[
F_+(143)=29\cdot143+882=5029=47\cdot107.
\]

Thus (A=24878463), (S\equiv125\pmod{143}), and both sides of the root
congruence are (38\pmod{143}).

The primes (733,83,17,47) each occur to odd valuation in exactly one of
the four component columns. They are four pivot rows, so the parity matrix
has full column rank. No nonempty component subset is an exact square.

For reference, the six pairwise resultants, in component order
((5,3),(5,4),(29,20),(29,21)), are

\[
70,\qquad3478,\qquad3888,\qquad3072,\qquad3482,\qquad2378.
\]

Each is coprime to (143). Direct reduction also shows that all four
components, (24,125), and every associated (b,y,u,v,T,D) are coprime
to (143). Hence no direct gcd screen factors the modulus. This completes
the counterexample.
