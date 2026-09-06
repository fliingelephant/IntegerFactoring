# F218 local weight collapse and multiplicative-index boundary

## Integrity and verdict

Before the statement was opened, its SHA-256 digest was verified as

```text
458924ffa7bf4554fd697e36bd45acf29930e414a0dd09bab10a7e388a95a481
```

This matches the preregistered digest.

**Verdict: PASS within every stated named-model scope.** The local
Eisenstein and eta congruences, the big-Witt path invariant, the theta
counterexample, and the nonperiodicity theorem all have symbolic proofs.
They neither evaluate the remaining divisor coefficient nor give a
factoring algorithm or an unrestricted lower bound.

This reconstruction uses only the repository-root `PROMPT.md` and the
hash-verified F218 `STATEMENT.md`. No numerical experiment or external
mathematical computation is used.

## 1. Setup and the common divisor-sum target

Assume

\[
N=pq,\qquad p<q<2p,\qquad N\equiv3\pmod4, \tag{1}
\]

where \(p,q\) are distinct odd primes, and put

\[
K=\frac{N-1}{2}. \tag{2}
\]

The complete factorization of \(K\) is granted. Since \(N=2K+1\),

\[
(N,K)=1. \tag{3}
\]

Every divisor of \(N\) is consequently a unit modulo \(K\). Moreover,

\[
\sigma_1(N)=1+p+q+N\equiv2+p+q\pmod K. \tag{4}
\]

This is the additive divisor-sum target shared by the constructions below.
For context, if \(N\ne15\), then \(p+q<K\). Indeed,

\[
2(K-p-q)=(p-2)(q-2)-5, \tag{5}
\]

which is positive for \(p\ge5\); balance forces \((p,q)=(3,5)\) when
\(p=3\). Thus an evaluator for (4), together with the explicit exceptional
case \(N=15\), would recover \(p+q\) and factor the quadratic
\(X^2-(p+q)X+N\). F218 identifies equivalent coefficient targets but does
not construct such an evaluator.

## 2. Theorem A: local collapse of the moving weight

Let \(\Lambda\) be any positive multiple of the Carmichael exponent
\(\lambda(K)\), and set

\[
k=\Lambda+2. \tag{6}
\]

Because \(K>1\) is odd, \(-1\) is a unit of order two modulo \(K\).
Hence \(\lambda(K)\), and therefore \(\Lambda\), is even and at least two.
It follows that \(k\) is even and \(k\ge4\).

### 2.1 The local congruence for every positive index

Fix a prime power \(\ell^e\parallel K\), and write an arbitrary positive
integer \(m\) as

\[
m=\ell^v m_{(\ell)},
\qquad \ell\nmid m_{(\ell)}. \tag{7}
\]

The local Carmichael exponent

\[
\lambda(\ell^e)=\ell^{e-1}(\ell-1)
\]

divides \(\lambda(K)\), and hence divides \(\Lambda\). It is also at least
\(e\): this is immediate for \(e=1\), while for \(e\ge2\),
\(\ell^{e-1}(\ell-1)\ge3^{e-1}\cdot2\ge e\). In particular,

\[
k-1=\Lambda+1\ge e. \tag{8}
\]

Expand the divisor sum. A divisor containing a positive power of \(\ell\)
has the form \(\ell^a d\), with \(a\ge1\) and
\(d\mid m_{(\ell)}\). By (8),

\[
(\ell^a d)^{k-1}\equiv0\pmod{\ell^e}. \tag{9}
\]

For a divisor \(d\mid m_{(\ell)}\), \(d\) is a unit modulo \(\ell^e\),
so the Carmichael congruence gives

\[
d^{k-1}=d^{\Lambda+1}\equiv d\pmod{\ell^e}. \tag{10}
\]

Only the \(\ell\)-free divisors survive, and summing (9)--(10) proves

\[
\boxed{
\sigma_{k-1}(m)
\equiv\sigma_1(m_{(\ell)})\pmod{\ell^e}.} \tag{A1}
\]

Both parts of the proof are necessary: the Carmichael exponent controls
the unit divisors, while the inequality \(k-1\ge e\) kills divisors with a
positive \(\ell\)-adic valuation.

### 2.2 A fixed-weight modular form with that coefficient

Use the standard quasimodular Eisenstein series

\[
E_2(\tau)=1-24\sum_{m\ge1}\sigma_1(m)q^m,
\qquad q=e^{2\pi i\tau}, \tag{11}
\]

and define

\[
\mathcal H_\ell(\tau)
=\frac{\ell E_2(\ell\tau)-E_2(\tau)}{24}. \tag{12}
\]

Although \(E_2\) is quasimodular, its anomaly cancels in (12). To see
this, let

\[
\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma_0(\ell),
\qquad c=\ell c_0,
\]

and put

\[
\gamma'=\begin{pmatrix}a&\ell b\\c_0&d\end{pmatrix}
\in\mathrm{SL}_2(\mathbb Z).
\]

Then \(\ell\gamma\tau=\gamma'(\ell\tau)\). In the transformation law

\[
E_2(\gamma\tau)
=(c\tau+d)^2E_2(\tau)
+\frac{12}{2\pi i}c(c\tau+d), \tag{13}
\]

the anomalous term for \(\ell E_2(\ell\gamma\tau)\) contains
\(\ell c_0=c\), so it cancels the anomalous term for \(E_2(\gamma\tau)\).
Thus (12) transforms with weight two on \(\Gamma_0(\ell)\).

It is holomorphic at infinity by its Fourier expansion. Since \(\ell\) is
prime, the other cusp is zero. Under the normalized Fricke operator

\[
W_\ell=\begin{pmatrix}0&-1\\\ell&0\end{pmatrix},
\]

the inversion formula for \(E_2\) gives

\[
\bigl(\ell E_2(\ell\tau)-E_2(\tau)\bigr)|_2W_\ell
=-\bigl(\ell E_2(\ell\tau)-E_2(\tau)\bigr). \tag{14}
\]

The anomalous terms again cancel, and (14) has a holomorphic expansion at
infinity. Hence \(\mathcal H_\ell\in M_2(\Gamma_0(\ell))\). Its constant
term is \((\ell-1)/24\), and all of its coefficients are rational.

For a positive index \(m\), equation (11) gives

\[
[q^m]\mathcal H_\ell
=\sigma_1(m)-\ell\mathbf1_{\ell\mid m}\sigma_1(m/\ell). \tag{15}
\]

If \(m=\ell^v u\), with \(\ell\nmid u\), multiplicativity gives

\[
\sigma_1(m)=\sigma_1(u)(1+\ell+\cdots+\ell^v).
\]

When \(v\ge1\), the subtracted term in (15) removes all terms except the
initial \(1\); when \(v=0\), it is absent. Therefore

\[
\boxed{
[q^m]\mathcal H_\ell
=\sigma_1(m)-\ell\mathbf1_{\ell\mid m}\sigma_1(m/\ell)
=\sigma_1(m_{(\ell)}).} \tag{A2}
\]

This is an exact identity, not only a congruence.

Combining (A1) and (A2), the positive-index coefficients of the
moving-weight Eisenstein series reduce modulo every \(\ell^e\parallel K\)
to those of this fixed-weight, moving-level, \(\ell\)-depleted form.

At \(m=N\), equation (3) implies \(\ell\nmid N\) for every \(\ell\mid K\),
so no depletion occurs. The Chinese remainder theorem then gives

\[
\boxed{
\sigma_{k-1}(N)\equiv\sigma_1(N)\pmod K.} \tag{A3}
\]

Thus moving to weight \(k=\Lambda+2\) does not produce a new target. This
is an exact target equivalence. It is not an impossibility theorem for a
compressed evaluator of the common coefficient.

## 3. Theorem B: the prime-level eta quotient at every \(r\)-adic valuation

Assume \(K=r>3\) is prime, and define

\[
P(q)=\prod_{a\ge1}(1-q^a),
\qquad
F_r(q)=\frac{P(q)^r}{P(q^r)}. \tag{16}
\]

For an indeterminate \(x\),

\[
\frac{(1-x)^r}{1-x^r}
=1+\sum_{j=1}^{r-1}(-1)^j\binom rj
  \frac{x^j}{1-x^r}. \tag{17}
\]

For \(1\le j<r\),

\[
\binom rj=\frac rj\binom{r-1}{j-1},
\qquad
\binom{r-1}{j-1}\equiv(-1)^{j-1}\pmod r.
\]

It follows that

\[
(-1)^j\binom rj\equiv-rj^{-1}\pmod{r^2}, \tag{18}
\]

where \(j^{-1}\) is taken modulo \(r\). Expanding the geometric series in
(17), substituting \(x=q^a\), and multiplying over all \(a\ge1\) gives,
coefficientwise,

\[
F_r(q)\equiv
1-r\sum_{a\ge1}\sum_{j=1}^{r-1}\sum_{h\ge0}
j^{-1}q^{a(j+hr)}\pmod{r^2}. \tag{19}
\]

Only finitely many factors affect any fixed coefficient, and a product of
two nonconstant terms in (19) is divisible by \(r^2\). In particular,
every positive coefficient of \(F_r-1\) is divisible by \(r\). This also
follows directly from the Frobenius congruence
\(P(q)^r\equiv P(q^r)\pmod r\).

Let

\[
m=r^vu,\qquad (u,r)=1, \tag{20}
\]

with arbitrary \(v\ge0\). A triple in (19) contributes to \(q^m\) exactly
when

\[
m=a(j+hr).
\]

Writing \(b=j+hr\), the allowed values are precisely the divisors
\(b\mid m\) not divisible by \(r\). By (20), these are exactly the
divisors of \(u\). Therefore

\[
-\frac{[q^m]F_r}{r}
\equiv\sum_{b\mid u}b^{-1}\pmod r. \tag{21}
\]

Since \(u\) is a unit modulo \(r\), the involution \(b\mapsto u/b\) on
its divisors gives

\[
\sum_{b\mid u}b^{-1}
\equiv u^{-1}\sum_{b\mid u}\frac ub
=u^{-1}\sigma_1(u)\pmod r. \tag{22}
\]

Thus, for every \(r\)-adic valuation \(v\), including \(v=0\),

\[
\boxed{
-\frac{[q^m]F_r}{r}
\equiv u^{-1}\sigma_1(u)\pmod r.} \tag{B1}
\]

The quotient on the left is an integer, and its residue modulo \(r\) is
determined by the coefficient modulo \(r^2\).

At the target \(N=2r+1\), one has \(v=0\), \(u=N\), and
\(N^{-1}\equiv1\pmod r\). Hence

\[
\boxed{
-\frac{[q^N]F_r}{r}
\equiv\sigma_1(N)\pmod r.} \tag{B2}
\]

More generally, (B1) differs from Theorem A's depleted coefficient
\(\sigma_1(u)\) only by the public invertible factor \(u^{-1}\). At the
target even that factor is one. The first \(r\)-adic eta lift and the
depleted weight-two Eisenstein coefficient therefore encode the same local
divisor-sum datum. Neither construction evaluates it in QP time.

## 4. Theorem C: the big-Witt rough-index invariant

Let \(M_K\) be the multiplicative monoid generated by the prime divisors
of \(K\), including \(1\). Consider a big-Witt ghost-coordinate circuit
whose allowed operations are ring addition, multiplication, constants,
and Frobenius and Verschiebung operators \(F_d,V_d\) only for
\(d\in M_K\). At ghost coordinate \(m\),

\[
w_m(F_dX)=w_{dm}(X),
\qquad
w_m(V_dX)=d\mathbf1_{d\mid m}w_{m/d}(X). \tag{23}
\]

Define the \(K\)-rough part of an index by

\[
\rho_K(m)=
\frac{m}{\prod_{\ell\mid K}\ell^{v_\ell(m)}}. \tag{24}
\]

Trace a dependence path backward from an output ghost coordinate with
index \(s\) to an input coordinate with index \(j\):

1. Addition and multiplication at ghost coordinates are coordinatewise,
   so they leave the index unchanged. A constant introduces no input
   dependence.
2. Passing backward through \(F_d\) changes an index \(m\) to \(dm\).
3. Passing backward through a nonzero branch of \(V_d\) changes \(m\) to
   \(m/d\); if \(d\nmid m\), there is no dependence path.

Every prime factor of an allowed \(d\) divides \(K\). Multiplying or
dividing by such a \(d\) changes only the valuations removed in (24).
Induction along the path proves

\[
\boxed{\rho_K(j)=\rho_K(s).} \tag{C1}
\]

By (3),

\[
\rho_K(N)=N. \tag{25}
\]

For every queried seed coordinate \(s<N\), however,

\[
\rho_K(s)\le s<N.
\]

Equation (C1) therefore forbids a dependence path from such a seed to the
input ghost coordinate at index \(N\). The affine relation
\(N=2K+1\) cannot be implemented by operations that move indices only by
multiplication and division by \(K\)-supported numbers.

This is exactly a circuit invariant for the declared ghost-coordinate
model. Allowing \(F_N\) lets the coordinate at seed index \(1\) *name*
\(w_N(X)\), because \(w_1(F_NX)=w_N(X)\), but it does not derive or
evaluate that coordinate from smaller data. Cartier operations,
coefficient convolution in a different representation, nonlinear
encodings, and non-Witt state do not obey the declared circuit grammar and
are outside the theorem.

## 5. Theorem D: Frobenius-simple theta state and cusp contamination

Let \(r>3\) be prime, let \(N=2r+1\), and put

\[
\vartheta(q)=\sum_{a\in\mathbb Z}q^{a^2},
\qquad k=\frac{r+1}{2}. \tag{26}
\]

### 5.1 Frobenius compression of the full theta coefficient

Over \(\mathbb F_r[[q]]\), Frobenius gives

\[
\vartheta(q)^r\equiv\vartheta(q^r). \tag{27}
\]

Since \(4k=2r+2\),

\[
\boxed{
\vartheta(q)^{4k}
=\vartheta(q)^{2r+2}
\equiv\vartheta(q^r)^2\vartheta(q)^2\pmod r.} \tag{D1}
\]

Let

\[
R_2(m)=[q^m]\vartheta(q)^2,
\]

the number of ordered signed representations of \(m\) as two squares.
Then

\[
\vartheta(q^r)^2=\sum_{h\ge0}R_2(h)q^{rh}.
\]

Because \(N=2r+1\), only \(h=0,1,2\) can contribute to the target
coefficient. The exact values

\[
R_2(0)=1,\qquad R_2(1)=4,\qquad R_2(2)=4
\]

give

\[
\begin{aligned}
[q^N]\vartheta^{2r+2}
&\equiv R_2(0)R_2(N)
 +R_2(1)R_2(r+1)
 +R_2(2)R_2(1)\\
&=R_2(N)+4R_2(r+1)+16\pmod r.
\end{aligned}
\]

Therefore

\[
\boxed{
[q^N]\vartheta^{2r+2}
\equiv R_2(N)+4R_2(r+1)+16\pmod r.} \tag{D2}
\]

### 5.2 The odd coefficient of the Eisenstein projection

The function \(f=\vartheta^{4k}\) is a weight-\(2k\) modular form on
\(\Gamma_0(4)\). For weight \(2k>2\), write its Eisenstein projection as

\[
\mathcal E_f
=A E_{2k}(\tau)+B E_{2k}(2\tau)+C E_{2k}(4\tau). \tag{28}
\]

These three old Eisenstein series span the Eisenstein space at the three
cusps of \(\Gamma_0(4)\). The coefficient \(A\) can be recovered directly
from cusp constants.

At infinity, \(f\) has constant term one. Poisson summation gives

\[
\vartheta\left(-\frac1{4\tau}\right)
=(-2i\tau)^{1/2}\vartheta(\tau). \tag{29}
\]

Under the normalized Fricke operator
\(W_4=\left(\begin{smallmatrix}0&-1\\4&0\end{smallmatrix}\right)\),
raising (29) to the \(4k\)-th power gives

\[
f|_{2k}W_4=(-1)^k f. \tag{30}
\]

Thus the constant at cusp zero is \((-1)^k\). At the cusp \(1/2\), the
theta series has zero constant. One direct way to see this is to approach
\(1/2\) vertically: the summands acquire the factor
\((-1)^{a^2}=(-1)^a\), and Poisson summation turns the resulting alternating
Gaussian into a dual sum over half-integers, which decays exponentially
after application of the cusp scaling matrix. Hence the constant of
\(f\) at \(1/2\) is zero.

For the basis in (28), the normalized constants at cusp zero are

\[
2^{2k},\qquad1,\qquad2^{-2k}, \tag{31}
\]

respectively. This follows from

\[
E_{2k}(d\tau)|_{2k}W_4
=\left(\frac2d\right)^{2k}E_{2k}\left(\frac4d\tau\right),
\qquad d=1,2,4. \tag{32}
\]

Using the scaling matrix
\(\left(\begin{smallmatrix}1&0\\2&1\end{smallmatrix}\right)\) at cusp
\(1/2\), their constants are

\[
1,\qquad1,\qquad2^{-2k}. \tag{33}
\]

Matching (30)--(33) gives

\[
2^{2k}A+B+2^{-2k}C=(-1)^k,
\]

\[
A+B+2^{-2k}C=0.
\]

Subtracting proves

\[
A=\frac{(-1)^k}{2^{2k}-1}. \tag{34}
\]

Only \(E_{2k}(\tau)\) contributes at an odd index; the other two series
are supported on even indices. With the normalization

\[
E_{2k}(\tau)
=1-\frac{4k}{B_{2k}}
\sum_{m\ge1}\sigma_{2k-1}(m)q^m, \tag{35}
\]

equations (34)--(35) give the target coefficient of the Eisenstein
projection:

\[
\boxed{
[q^N]\mathcal E_f
=(-1)^{k+1}
\frac{4k}{(2^{2k}-1)B_{2k}}
\sigma_{2k-1}(N).} \tag{D3}
\]

### 5.3 Reduction modulo \(r\)

Here \(2k=r+1\). Kummer's congruence at the indices \(r+1\) and \(2\)
states

\[
\frac{B_{r+1}}{r+1}
\equiv\frac{B_2}{2}
=\frac1{12}\pmod r. \tag{36}
\]

These rational residues are well-defined because their denominators are
prime to \(r>3\). Thus

\[
B_{2k}=B_{r+1}\equiv\frac1{12}\pmod r. \tag{37}
\]

Fermat's theorem gives

\[
4k=2(r+1)\equiv2\pmod r,
\qquad
2^{2k}-1=2^{r+1}-1\equiv3\pmod r. \tag{38}
\]

Every divisor \(d\mid N\) is prime to \(r\), and
\(d^r\equiv d\pmod r\). Hence

\[
\sigma_{2k-1}(N)=\sigma_r(N)\equiv\sigma_1(N)\pmod r. \tag{39}
\]

Substitution of (37)--(39) into (D3) gives

\[
\boxed{
[q^N]\mathcal E_f
\equiv(-1)^{k+1}8\sigma_1(N)\pmod r.} \tag{D4}
\]

### 5.4 Exact counterexample and minimality on the branch

Take

\[
r=17,qquad N=35=5\cdot7,qquad k=9. \tag{40}
\]

This satisfies every prime-\(K\), balanced-semiprime hypothesis. There are
no representations of \(35\) as two squares, so \(R_2(35)=0\); equivalently,
the prime \(7\equiv3\pmod4\) occurs to an odd exponent. The only signed,
ordered representations of \(18\) are \((\pm3,\pm3)\), so
\(R_2(18)=4\). Equation (D2) gives

\[
0+4\cdot4+16=32\equiv15\pmod{17}. \tag{41}
\]

On the other hand,

\[
\sigma_1(35)=(1+5)(1+7)=48,
\qquad (-1)^{k+1}=1,
\]

so (D4) gives

\[
8\cdot48=384\equiv10\pmod{17}. \tag{42}
\]

The full theta coefficient minus its Eisenstein projection is therefore

\[
\boxed{15-10=5\pmod{17}\ne0.} \tag{D5}
\]

This is the cusp contribution.

It is the smallest such branch instance. For primes \(3<r<17\), the
values \(r=5,11\) give prime \(N=11,23\), while \(r=13\) gives
\(N=27\), not a product of two distinct primes. The only earlier branch
input is \(r=7,N=15=3\cdot5,k=4\). There,
\(R_2(15)=0\), \(R_2(8)=4\), and (D2) is
\(32\equiv4\pmod7\). Formula (D4) is
\(-8\sigma_1(15)=-8\cdot24\equiv4\pmod7\), so its cusp difference is
zero. The first nonzero difference is therefore (40)--(42).

Frobenius has compressed the *full* theta coefficient to data at the
smaller index \(r+1\), but the Eisenstein component containing the desired
divisor sum does not separately obey that compression. The nonzero cusp
coefficient is exactly the obstruction to the proposed isolation. This is
an exact counterexample to that isolation claim, not a lower bound against
a computable cusp projector or another theta-based algorithm.

## 6. Theorem E: no fixed linear state for the affine Cartier section

Fix a prime \(r\), and, more generally than the weight-one case, let

\[
b_{r,s}(j)=\sigma_s(rj+1)\pmod r,
\qquad j\ge0,\qquad s\in\mathbb Z_{>0}. \tag{43}
\]

The stated sequence is \(b_r=b_{r,1}\). We prove nonperiodicity for every
positive \(s\), treating \(r=2\) separately.

### 6.1 An elementary supply of primes congruent to one

For every integer \(M\ge2\), there are infinitely many primes
\(L\equiv1\pmod M\). A short cyclotomic proof suffices. If there were only
finitely many such primes \(L_1,\ldots,L_h\), choose a sufficiently large
integer \(A\) divisible by \(M L_1\cdots L_h\). Since
\(\Phi_M(0)=1\), every prime divisor \(L\) of \(\Phi_M(A)>1\) is outside
that finite list and does not divide \(M\). In characteristic \(L\), the
roots of \(\Phi_M\) are primitive \(M\)-th roots when \(L\nmid M\).
Thus the multiplicative order of \(A\pmod L\) is exactly \(M\), so
\(M\mid L-1\). This constructs another prime \(L\equiv1\pmod M\), a
contradiction.

### 6.2 Odd primes \(r\)

Suppose, toward a contradiction, that \(b_{r,s}\) is eventually periodic
with period \(T\ge1\), after some index \(J\). Put

\[
M=rT.
\]

Using the preceding lemma, choose three distinct, sufficiently large
primes \(L,P,Q\), each congruent to \(1\pmod M\), so that the indices

\[
j_1=\frac{L-1}{r},
\qquad
j_2=\frac{PQ-1}{r}
\]

both exceed \(J\). The two indices are divisible by \(T\), and hence lie
in the same eventual-period class. But

\[
\sigma_s(L)=1+L^s\equiv2\pmod r, \tag{44}
\]

while multiplicativity and distinctness of \(P,Q\) give

\[
\sigma_s(PQ)=(1+P^s)(1+Q^s)\equiv4\pmod r. \tag{45}
\]

For odd \(r\), \(2\not\equiv4\pmod r\). Equations (44)--(45) contradict
eventual periodicity. This proof is independent of the value of the
positive exponent \(s\).

### 6.3 The prime \(r=2\)

Every divisor of \(2j+1\) is odd, so for every positive \(s\),

\[
\sigma_s(2j+1)
\equiv\#\{d:d\mid2j+1\}\pmod2. \tag{46}
\]

An integer has an odd number of positive divisors exactly when it is a
perfect square. Thus \(b_{2,s}(j)=1\) exactly when \(2j+1\) is an odd
square. These events occur infinitely often, at

\[
j_h=\frac{(2h+1)^2-1}{2}=2h(h+1),
\]

and their successive gaps are

\[
j_{h+1}-j_h=4(h+1), \tag{47}
\]

which are unbounded. An eventually periodic binary sequence with
infinitely many ones has bounded gaps between its ones. Equation (47) is a
contradiction.

Combining the two cases proves, for every prime \(r\) and every positive
integer \(s\),

\[
\boxed{(b_{r,s}(j))_{j\ge0}\text{ is not eventually periodic}.} \tag{E1}
\]

### 6.4 Linear recurrences and rationality

Over the finite field \(\mathbb F_r\), a sequence satisfying a homogeneous
constant-coefficient recurrence of finite order has a finite state vector
of consecutive values. Its deterministic state evolution on a finite set
is eventually periodic. An affine recurrence has the same property,
either directly or after adjoining a constant coordinate equal to one.
Equation (E1) rules out both kinds of recurrence at every finite order.

If the generating series

\[
B_{r,s}(x)=\sum_{j\ge0}b_{r,s}(j)x^j \tag{48}
\]

were rational over \(\mathbb F_r\), multiplying it by a denominator with
nonzero constant term would yield a constant-coefficient homogeneous
recurrence for all sufficiently large coefficients. This is impossible,
so \(B_{r,s}(x)\) is not rational.

This eliminates every fixed finite *linear* Cartier state for the full
progression \(rj+1\). It does not eliminate a nonlinear, nonrational, or
growing-state Cartier algorithm. Nor does it address an identity designed
only for the single digit \(j=2\) while the prime \(r\) varies; that is a
different quantifier pattern from one fixed sequence with all \(j\).

## 7. Exact boundary and remaining scope

The proved conclusions fit together as follows:

1. Every moving weight \(k=\Lambda+2\), for arbitrary positive
   \(\Lambda\) divisible by \(\lambda(K)\), reduces locally to the
   fixed-weight \(\ell\)-depleted coefficient (A2), including at indices
   divisible by arbitrarily high powers of \(\ell\).
2. For prime \(K=r\), the first eta lift modulo \(r^2\) gives the same
   depleted datum for every decomposition \(m=r^vu\); at the target it is
   exactly \(\sigma_1(N)\pmod r\).
3. Within the declared big-Witt ghost circuit, \(K\)-supported
   Frobenius/Verschiebung operations preserve the rough part of every
   dependence-path index and cannot convert the affine index
   \(N=2K+1\) into a smaller queried coordinate.
4. Frobenius compresses the full theta coefficient, but the exact
   \(r=17,N=35\) witness proves that a cusp component can contaminate the
   result and prevent isolation of the Eisenstein divisor sum.
5. For every prime \(r\), the complete affine section
   \(\sigma_s(rj+1)\pmod r\) has no fixed finite linear recurrence, for
   every positive \(s\).

These statements leave the divisor coefficient itself unevaluated. They
do not rule out a genuinely compressed random-access coefficient
algorithm, nonlinear or growing Cartier state, a computable cusp
projector, a nonlinear characteristic identity, coefficient convolution
outside the ghost model, or a different integer statistic.

Finally, the setup is only the balanced beta-two semiprime branch and the
factorization of \(K\) is granted. F218 supplies neither an all-input
algorithm nor recursive and Las Vegas bit-complexity closure. It therefore
does not resolve the factoring task in `PROMPT.md`.
