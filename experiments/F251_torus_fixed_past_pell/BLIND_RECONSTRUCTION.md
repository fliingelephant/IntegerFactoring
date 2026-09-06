# Blind reconstruction of F251

**Status:** PASS  
**Authenticated statement SHA-256:** `2fce8c0126d1454c68a39068ab28b8fda95cc3f270a1d83d7cd758a66c50c5e6`

This reconstruction uses only the authenticated statement, the root prompt, and the root instructions.

## 1. Uniform fixed-\(P\) bound

Write

\[
P=s^2\kappa,
\]

where \(s\ge 1\) and \(\kappa\) is squarefree. For each \(y\),

\[
P(1+Dy^2)\text{ is a square}
\quad\Longleftrightarrow\quad
\kappa a^2-Dy^2=1
\tag{1}
\]

for some positive integer \(a\). Indeed, if
\(R^2=s^2\kappa(1+Dy^2)\), then \(s\mid R\). After writing
\(R=sT\), squarefreeness gives \(\kappa\mid T\). Thus
\(T=\kappa a\) and \(1+Dy^2=\kappa a^2\). The converse follows by
reversing these steps.

For a solution of (1), define

\[
U(a,y)=\sqrt\kappa\,a+\sqrt D\,y.
\]

Equation (1) gives

\[
U(a,y)^{-1}=\sqrt\kappa\,a-\sqrt D\,y.
\tag{2}
\]

For \(y>0\), this implies

\[
1<U(a,y)=2\sqrt D\,y+U(a,y)^{-1}
       <1+2Y\sqrt D
\tag{3}
\]

whenever \(y<Y\). Also,
\(U(a,y)=\sqrt{1+Dy^2}+\sqrt D\,y\), so the height is strictly
increasing with \(y\).

Put \(K=\kappa D\). First suppose that \(K\) is a square. Since
\(\kappa\) is squarefree, \(D=\kappa d^2\) for an integer \(d\).
Equation (1) becomes

\[
\kappa(a^2-d^2y^2)=1.
\]

There are no solutions if \(\kappa>1\). If \(\kappa=1\), then
\((a-dy)(a+dy)=1\), so the only solution is \((a,y)=(1,0)\).
Hence the claimed bound holds in the square-\(K\) case.

Now suppose that \(K\) is not a square. Take two solutions
\((a_i,y_i)\) and \((a_j,y_j)\) with \(y_i<y_j\), and write
\(U_i=U(a_i,y_i)\) and \(U_j=U(a_j,y_j)\). By (2),

\[
\frac{U_j}{U_i}
=c+d\sqrt K,
\]

where

\[
c=\kappa a_i a_j-Dy_i y_j,
\qquad
d=a_i y_j-a_j y_i
\]

are integers. The conjugate is

\[
c-d\sqrt K=\frac{U_i}{U_j}.
\]

Thus \(c^2-Kd^2=1\). Since \(U_j/U_i>1\), both the ratio and its
reciprocal are positive, and

\[
c=\frac{U_j/U_i+U_i/U_j}{2}>1.
\]

Therefore \(c\ge2\), and

\[
 d\sqrt K=\frac{U_j/U_i-U_i/U_j}{2}>0,
\qquad
\frac{U_j}{U_i}
=c+\sqrt{c^2-1}
\ge 2+\sqrt3
>2+\sqrt2=\Lambda.
\tag{4}
\]

This spacing applies in particular to consecutive solutions.

Let

\[
L=\frac{\log(1+2Y\sqrt D)}{\log\Lambda}.
\]

If \(\kappa>1\), equation (1) has no \(y=0\) solution. If there are
\(m\ge1\) positive solutions, order their heights as
\(U_1<\cdots<U_m\). Equations (3) and (4) give

\[
\Lambda^{m-1}<U_m<1+2Y\sqrt D.
\]

Hence \(m-1<L\), so

\[
m\le 1+\lfloor L\rfloor.
\tag{5}
\]

If \(\kappa=1\), the unique \(y=0\) solution is \((a,y)=(1,0)\),
with height \(1\). Apply (4) also between this solution and the first
positive solution. If there are \(m\ge1\) positive solutions, then
\(\Lambda^m<U_m<1+2Y\sqrt D\). Consequently
\(m\le\lfloor L\rfloor\), and adding the \(y=0\) solution again gives
(5). If there are no positive solutions, (5) is immediate.

Combining the square-\(K\) and nonsquare-\(K\) cases proves

\[
\#\{0\le y<Y:P(1+Dy^2)\text{ is an integer square}\}
\le
1+\left\lfloor
\frac{\log(1+2Y\sqrt D)}{\log(2+\sqrt2)}
\right\rfloor
=B(D,Y).
\]

The final expression contains no \(P\), \(s\), or \(\kappa\). The
bound is therefore uniform in both the size and the squarefree kernel of
\(P\). Restricting to admitted rows, or to useful squares, can only
decrease the count.

## 2. Normalized roots

For an admitted row, \(A_y\equiv x_y^2\pmod N\) is a unit. If
\(P A_y=R^2\), then

\[
\zeta_y=R(Xx_y)^{-1}\pmod N
\]

satisfies

\[
\zeta_y^2\equiv
R^2(X^2x_y^2)^{-1}
\equiv PA_y(PA_y)^{-1}
\equiv1\pmod N.
\]

For \(N=pq\) with distinct odd primes, a square root of \(1\) chooses
one sign modulo \(p\) and one sign modulo \(q\). If \(\zeta_y\) is not
globally \(1\) or \(-1\) modulo \(N\), these signs differ. The two gcds
\(\gcd(\zeta_y-1,N)\) and \(\gcd(\zeta_y+1,N)\) then recover the two
proper prime factors in some order.

## 3. Size of the bound

Because \(Y\sqrt D\ge1\),

\[
1+2Y\sqrt D\le3Y\sqrt D.
\]

Therefore

\[
B(D,Y)=O(\log Y+\log D).
\]

For \(Y=N\) and \(1\le D<N\), this is \(O(n)\), where
\(n=\lceil\log_2N\rceil\). If \(D\) has polynomially many bits in
\(n\), then \(\log D=n^{O(1)}\), so \(B(D,N)=n^{O(1)}\).

## 4. Conditional and pair-sampling consequences

Condition on the full past. Suppose the resulting distribution of the
fresh coordinate \(y\) has maximum point mass \(\mu\), while \(P\) and
its supplied root \(X\) are fixed by that past. At most \(B(D,Y)\)
coordinates can give an exact square, and usefulness is an additional
restriction. Hence

\[
\Pr[P A_y\text{ is a useful exact square}\mid\text{past}]
\le \mu B(D,Y).
\]

For uniform \(y\in\{0,\ldots,Y-1\}\), take \(\mu=1/Y\).

Now let \(\mathcal Y\subseteq\{0,\ldots,N-1\}\) be a nonempty set of
admitted coordinates, and let \(y,z\) be independent and uniform on
\(\mathcal Y\). Condition on \(z\). Set \(P=A_z\) and use its supplied
root \(X=x_z\). The theorem leaves at most \(B(D,N)\) possible values
of \(y\) for which \(A_yA_z\) is a square. Thus

\[
\Pr[A_yA_z\text{ is an exact square}]
\le \frac{B(D,N)}{|\mathcal Y|}.
\]

The event that the associated root
\(R(x_yx_z)^{-1}\pmod N\) is useful is a subset of this event, so it has
the same upper bound.

More generally, consider a uniform set of \(H\) admitted points whose
canonical \(y\)-fibres have size at most \(c\). After conditioning on
the first point, at most \(B(D,N)\) second-coordinate values work. Each
such coordinate supports at most \(c\) points. Therefore two independent
uniform points satisfy

\[
\Pr[A_yA_z\text{ is an exact square}]
\le\frac{cB(D,N)}H.
\]

Again, useful normalized roots form a subset. Substituting the stated
fibre caps gives \(c=4\) for the clean raw norm-one torus and \(c=2\)
for a clean powered image with fibres of size at most two.

For \(T\) independent rows, apply the preceding estimate to each
unordered pair and then use the union bound:

\[
\Pr[\text{at least one two-row product is an exact square}]
\le
\binom T2\frac{cB(D,N)}H.
\]

The same conclusion holds with “useful exact square” in place of “exact
square.” If

\[
T=2^{(\log n)^{O(1)}},\qquad
B(D,N)=n^{O(1)},\qquad
H=2^{\Omega(n)},
\]

then \(T^2B(D,N)=2^{o(n)}\), while \(H=2^{\Omega(n)}\). The displayed
probability is therefore \(2^{-\Omega(n)}\).

## 5. Exact scope

The proof controls the following situations.

1. A product \(P\) determined by the past is tested against one fresh
   row. The value of \(P\) may depend on the past, but it must not depend
   on the fresh coordinate.
2. Every pair in an independent bank is controlled by conditioning on
   one member. A quadratic-size union bound controls all pairs.
3. In a prescribed adaptive sequence, each closure is controlled when
   its product and supplied root are fixed before the next coordinate is
   sampled. Conditional bounds can then be combined by the tower rule
   and a union bound.

The argument does not give one bound simultaneously uniform over a
family of products selected after the fresh row is visible. In
particular, it does not control a P66 step that inspects a fresh row and
then selects one of exponentially many past subset products. Applying
the theorem separately would introduce the size of that family.

Likewise, it does not control a general product of three or more rows
chosen retrospectively. A prescribed multi-row product can fit the
fixed-past rule by exposing its last row only after the earlier product
is fixed; retrospective selection among many candidate products does
not.
