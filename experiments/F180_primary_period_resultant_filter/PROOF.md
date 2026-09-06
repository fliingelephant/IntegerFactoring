# Proof of the F180 primary-period resultant filter

## 1. Exact deletion of primary components

Fix \(\ell^a\parallel f_j\). Since \(f_j<N<2^n\), one has \(a<n\).
The order of the \(A_\delta^n\)-th power of \(y\) retains its
\(\ell^a\) part exactly when \(\ell\nmid A_\delta\).

If \(\ell\mid N+\delta\), then

\[
(N+\delta)^k-1\equiv-1\pmod\ell
\]

for every \(k\), so \(\ell\nmid A_\delta\). If \(N+\delta\) is a unit
modulo \(\ell\), then \(\ell\mid A_\delta\) exactly when

\[
\operatorname{ord}_\ell(N+\delta)\le K.
\]

Whenever \(\ell\mid A_\delta\), raising to the \(n\)-th power supplies at
least \(n>a\) copies of \(\ell\), so the complete \(\ell^a\) part is
removed. This proves (7).

The equality \(H_\delta=N\) holds exactly when the filtered order is one on
every hidden prime-power component. The equality \(H_\delta=1\) means that
every component retains a listed primary part. Any intermediate gcd,
including one that contains only a proper subpower of a hidden prime-power
component, is already a proper factor of \(N\). For \(\delta=0\),
\(\gcd(f_j,N)=1\), so only the long-period alternative remains in (7).
This proves (8).

## 2. Resultant support in the double-identity branch

Assume (9), and fix \(\ell^a\parallel f_j\). From

\[
f_j\mid A_0^n,
\qquad
f_j\mid A_3^n,
\]

one gets \(\ell\mid A_0\) and \(\ell\mid A_3\). Hence there are
\(k,l\le K\) such that

\[
N^k-1\equiv0\pmod\ell,
\qquad
(N+3)^l-1\equiv0\pmod\ell.
\tag{1}
\]

The Sylvester-matrix Bezout identity shows that the resultant in (10) is an
integer combination of the two polynomials. Evaluation at \(X=N\) and (1)
therefore give

\[
\ell\mid R_{k,l}.
\tag{2}
\]

The two polynomials have no common complex root. Such a root \(u\) would
satisfy \(|u|=|u+3|=1\), contrary to
\(|u+3|\ge3-|u|=2\). Thus every resultant is nonzero.

Using the roots of \(X^k-1\),

\[
R_{k,l}
=
\prod_{u^k=1}\left|(u+3)^l-1\right|
<2^{k(2l+1)},
\]

which proves (11). Equation (2) puts at least one copy of every prime
supporting every \(f_j\) into the product in (12). The outer \(n\)-th power
then supplies every multiplicity \(a<n\), proving (13).

## 3. Exact recovery and cost

There are \(K^2\) integer resultants of degrees at most \(K\) and bit length
\(O(K^2)\). Exact Sylvester determinants take polynomial time in those
parameters. Trial division of all of them costs at most \(2^{O(K^2)}\), so
the complete factorization of \(M\) is public in QP time.

Because every local order divides \(M\), factor-first divisor stripping
either finds unequal local prime-adic exponents and returns a proper factor,
or terminates at their common exact order \(m\). Equation (2) of the
statement gives \(m>T\ge n\).

The products \(A_\delta\) have \(O(nK^2)\) bits and their \(n\)-th powers
have \(O(n^2K^2)\) bits. All modular powers and gcds are therefore QP. This
proves the trichotomy and its total bit bound.

No step forces the nonidentity primary-hard branch to disappear.
