# Proof of the F225 fixed-shift obstruction

## 1. Frobenius collapse

Modulo `p`, Frobenius gives, for every residue `x`,

\[
x^{pq}=(x^p)^q=x^q.
\]

Since `q=p+d`, a second use of `x^p=x` gives

\[
H_N(x)\equiv (x+1)^{d+1}-x^{d+1}-1\pmod p.
\tag{1}
\]

Modulo `q`, the same argument gives

\[
H_N(x)\equiv (x+1)^p-x^p-1\pmod q.
\tag{2}
\]

These reductions include `x=0` and `x=-1`.  Because all relevant
exponents are odd, both points are roots in both fields.

## 2. The `p`-side reciprocal polynomial

Write `c=2p-q`, so `d=p-c`.  Under `c>=3`, put `k=c-2>=1`.  Then

\[
d+1=p-c+1=(p-1)-k.
\tag{3}
\]

For `x` different from `0,-1`, Fermat's theorem turns (1) into

\[
(x+1)^{-k}-x^{-k}-1=0.
\tag{4}
\]

Multiplication by the nonzero value `[x(x+1)]^k` shows that (4) is
equivalent to

\[
P_k(x):=x^k-(x+1)^k-[x(x+1)]^k=0.
\tag{5}
\]

The polynomial `P_k` has degree exactly `2k`: its leading coefficient is
`-1`, while the other two terms have degree at most `k`.  Hence it has at
most `2k` roots in `F_p`.  Adding the two exceptional roots gives

\[
A_p
=2+\#\{x\notin\{0,-1\}:P_k(x)=0\}
\le2+2k=2c-2.
\tag{6}
\]

This is the first exact decomposition and its bound.

## 3. The `q`-side character cells

The relation `q=2p-c` gives

\[
p={q-1\over2}+s,
\qquad s={c+1\over2}.
\tag{7}
\]

For nonzero `y mod q`, Euler's criterion therefore gives

\[
y^p=\chi(y)y^s.
\tag{8}
\]

For `x` different from `0,-1`, put

\[
\epsilon=\chi(x+1),\qquad \delta=\chi(x).
\]

Equation (2) is then exactly

\[
Q_{\epsilon,\delta}(x)
=\epsilon(x+1)^s-\delta x^s-1=0.
\tag{9}
\]

The four character cells are disjoint, so summing their root counts and
adding `0,-1` proves the exact formula for `A_q`.

It remains to bound those counts.  If `epsilon` and `delta` have opposite
signs, the coefficient of `X^s` in `Q_(epsilon,delta)` is `epsilon-delta`,
which is `+2` or `-2`.  These two polynomials have degree exactly `s`.
If the signs agree, their leading terms cancel, but the coefficient of
`X^(s-1)` is `epsilon*s`.  The inequalities

\[
2\le s<q
\]

show that this coefficient is nonzero modulo `q`.  These two polynomials
have degree exactly `s-1`.  The number of nonexceptional roots is therefore
at most

\[
2s+2(s-1)=4s-2.
\tag{10}
\]

After adding `0,-1`,

\[
A_q\le 2+(4s-2)=4s=2c+2.
\tag{11}
\]

This proves Theorem A.

## 4. CRT and proper gcds

Let `Z_p` and `Z_q` be the two local zero sets.  For a uniform residue
modulo `N`, the CRT coordinates are independent and uniform.  The gcd is
proper exactly when one local coordinate belongs to its zero set and the
other does not.  Thus

\[
\Pr(1<\gcd(H_N(x),N)<N)
={A_p\over p}\left(1-{A_q\over q}\right)
+{A_q\over q}\left(1-{A_p\over p}\right).
\tag{12}
\]

Dropping the two factors bounded by `1`, using (6), (11), and `q>p`, gives

\[
\Pr(1<\gcd(H_N(x),N)<N)
\le {2c-2\over p}+{2c+2\over q}
\le {4c\over p}.
\tag{13}
\]

For a uniform unit, the local coordinates are independent and uniform in
`F_p^*` and `F_q^*`.  The point `0` is in each zero set and is the only one
removed by this restriction.  Replacing `(A_p,p,A_q,q)` in (12) by
`(A_p-1,p-1,A_q-1,q-1)` gives the exact unit formula.  Its upper bound is

\[
{2c-3\over p-1}+{2c+1\over q-1}
\le {4c-2\over p-1}.
\tag{14}
\]

If a uniform residue is first gcd-screened, a proper nonunit itself factors
`N`.  Its probability is `(p+q-2)/(pq)=O(1/p)`.  Conditional on a unit, the
law is exactly the one used in (14).  Since `c>=3`, this extra term is
`O(c/p)`.  This proves Theorem B and the screening claim.

## 5. The unconditional near-double-prime family

Baker--Harman--Pintz, *The Difference Between Consecutive Primes, II*,
Proceedings of the London Mathematical Society 83 (2001), Theorem 1,
proves that, for every sufficiently large real `X`, the interval

\[
[X-X^{0.525},X]
\tag{15}
\]

contains a prime.  The DOI is `10.1112/plms/83.3.532`.

Let `p` run through unbounded odd primes and set

\[
X_p=2p-\lfloor p^{3/5}\rfloor.
\tag{16}
\]

For large `p`, the lower endpoint in (15) is greater than `p`.  Choose a
prime `q` in the guaranteed interval.  It is also at most `X_p<2p`, so
`p<q<2p`.  The upper-balance defect satisfies

\[
\lfloor p^{3/5}\rfloor
\le c=2p-q
\le\lfloor p^{3/5}\rfloor+X_p^{0.525}.
\tag{17}
\]

Because `0.525<3/5`, equation (17) gives

\[
c=\Theta(p^{3/5}).
\tag{18}
\]

In particular, `c>=3` eventually.  The hidden-prime gap is

\[
d=p-c=p-\Theta(p^{3/5})=\Theta(p),
\tag{19}
\]

so it is eventually larger than `p^(2/3)` and hence lies in the advertised
large-gap regime.

Equations (13)--(14) give, for either uniform sampling model,

\[
\Pr(\text{proper scalar gcd})=O(p^{-2/5}).
\tag{20}
\]

Balance and (19) give `N=Theta(p^2)`, so for
`n=ceil(log_2 N)`,

\[
p^{-2/5}=2^{-n/5+O(1)}=2^{-\Omega(n)}.
\tag{21}
\]

At an adaptive stage whose next point is fresh and uniform, the same bound
holds conditioned on the previous transcript.  A numerical-QP trial bank
has `2^(o(n))` stages.  A conditional union bound applied to (21) leaves
total success probability `2^(-Omega(n))`.  This proves Theorem C.

## 6. Logical boundary

The proof uses the integer-specific near-double relation twice.  Modulo
`p`, it turns the exponent into a small negative exponent.  Modulo `q`, it
turns the exponent into a small positive exponent times the quadratic
character.  A generic degree bound on the original degree-`d` polynomial
would miss both collapses.

The argument bounds only local zeros and their individual gcds.  It makes
no claim about information in nonzero values or a nonuniform point law.
