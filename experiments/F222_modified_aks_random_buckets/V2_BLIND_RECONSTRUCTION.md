# F222 V2 blind reconstruction

**Statement authentication.** Before reading the statement, its SHA-256 was
verified as

```text
586d2edd549a8c580aa9d66c9dd2cee7866ee4f0d74ed0956bc3f07772ad6cd9
```

Only the authenticated statement and the mandatory project instructions were
used in this reconstruction.

## 1. Setup and cyclic-coefficient notation

Let

\[
N=pq,\qquad p<q<2p,\qquad d=q-p,
\]

where \(p,q\) are distinct odd primes. Let \(r\geq 2\),
\(\gcd(r,N)=1\), and

\[
R_\ell=\mathbb F_\ell[X]/(X^r-1),\qquad
E_a=(X+a)^N-X^N-a^N.
\]

For a polynomial in \(R_\ell\), write \([X^k]_r\) for its coefficient at
the cyclic position \(k\in\mathbb Z/r\mathbb Z\). Thus
\(e_{\ell,k}(a)=[X^k]_rE_a\). Throughout Theorem A assume

\[
r<d<p-1. \tag{1}
\]

In particular, \(r<p,q\), and every binomial coefficient
\(\binom d j\), \(0\leq j\leq d\), is nonzero modulo either prime.

## 2. The exact local law modulo \(p\)

For \(a\in\mathbb F_p\), Frobenius and \(q=p+d\) give

\[
\begin{aligned}
(X+a)^{pq}
  &=(X^p+a)^q\\
  &=(X^{p^2}+a)(X^p+a)^d,
\end{aligned}
\]

while \(a^{pq}=a^{d+1}\). Therefore the following degree-\(d\)
representative gives the value of \(E_a\) for every \(a\in\mathbb F_p\):

\[
\boxed{
E_a=
\sum_{j=0}^{d-1}\binom d j X^{p^2+pj}a^{d-j}
+\sum_{j=1}^{d}\binom d j X^{pj}a^{d-j+1}
\quad\text{in }R_p.}
\tag{2}
\]

Consequently,

\[
e_{p,k}(a)=
\sum_{\substack{0\leq j<d\\p^2+pj\equiv k\ (r)}}
 \binom d j a^{d-j}
+
\sum_{\substack{1\leq j\leq d\\pj\equiv k\ (r)}}
 \binom d j a^{d-j+1}. \tag{3}
\]

This has degree at most \(d\). It is nonzero for every \(k\). To see this,
choose \(t\pmod r\) with \(pt\equiv k\pmod r\). The interval
\(1,\ldots,d\) contains a representative of every residue modulo \(r\),
so the second sum in (3) contains a term. Terms within either sum have
different powers of \(a\). A term indexed by \(j_1\) in the first sum and
a term indexed by \(j_2\) in the second sum can have the same power of
\(a\) only when \(j_2=j_1+1\). Their cyclic positions then agree only if

\[
p(p-1)\equiv0\pmod r,
\]

or equivalently \(p\equiv1\pmod r\). If this congruence fails, no
cross-cancellation is possible. If it holds, each overlapping coefficient
is

\[
\binom d{j_1}+\binom d{j_1+1}
=\binom{d+1}{j_1+1},
\]

which is nonzero modulo \(p\) because \(d+1<p\). Hence every
\(e_{p,k}\) is a nonzero polynomial of degree at most \(d\).

A nonzero polynomial of degree at most \(d\) has at most \(d\) roots.
Taking a union bound over the \(r\) cyclic positions gives

\[
\Pr_{a\in\mathbb F_p^\times}
 \bigl(\exists k:e_{p,k}(a)=0\bigr)
\leq \frac{rd}{p-1}. \tag{4}
\]

## 3. The exact local law modulo \(q\)

Put \(Y=X^q\) in \(R_q\). Since \(p+d=q\), Frobenius gives, for
\(a\in\mathbb F_q^\times\),

\[
E_a=(Y+a)^p-Y^p-a^p
\]

and

\[
(Y+a)^dE_a=Y^q+a-Y^p(Y+a)^d-a^p(Y+a)^d.
\]

After multiplication by \(a^{d-1}\) and use of
\(a^{p+d-1}=a^{q-1}=1\), this becomes

\[
\boxed{a^{d-1}(Y+a)^dE_a=G_a,} \tag{5}
\]

where

\[
G_a=a^{d-1}(Y^q+a)
     -a^{d-1}Y^p(Y+a)^d
     -(Y+a)^d. \tag{6}
\]

As a polynomial in \(a\), \(G_a\) has degree at most \(2d-1\).

Because \(Y^r=1\), define

\[
C_a=\sum_{u=0}^{r-1}(-a)^uY^{r-1-u},
\qquad
D(a)=1-(-a)^r.
\]

The geometric identity gives

\[
(Y+a)C_a=D(a). \tag{7}
\]

Thus, outside the common exceptional set \(D(a)=0\), which has at most
\(r\) elements,

\[
a^{d-1}E_a=\frac{C_a^dG_a}{D(a)^d}. \tag{8}
\]

For every cyclic position \(k\), define

\[
W_k(a)=[X^k]_r\bigl(C_a^dG_a\bigr)\in\mathbb F_q[a]. \tag{9}
\]

Equations (8) and (9) show that, for every nonexceptional unit shift,

\[
e_{q,k}(a)=0\quad\Longrightarrow\quad W_k(a)=0. \tag{10}
\]

Moreover,

\[
\deg W_k\leq d(r-1)+(2d-1)=d(r+1)-1. \tag{11}
\]

It remains to prove that no \(W_k\) is the zero polynomial. This is the
step that prevents (11) from being only a formal degree estimate.

Use cyclic \(Y\)-coordinates. They are the same \(r\) cyclic positions in
a different order because \(\gcd(q,r)=1\). From (7),

\[
C_a^dG_a
=a^{d-1}A_a-(1+a^{d-1}Y^p)D(a)^d,
\qquad
A_a=C_a^d(Y^q+a). \tag{12}
\]

Let \(c_m\) be the coefficient of \(z^m\) in
\((1+z+\cdots+z^{r-1})^d\). Since

\[
C_a=\sum_{u=0}^{r-1}(-a)^uY^{-1-u},
\]

we have

\[
C_a^d=\sum_{m=0}^{d(r-1)}(-1)^mc_ma^mY^{-d-m}. \tag{13}
\]

The part of \(A_a\) obtained by multiplication by \(Y^q\) has, at
degree \(m\), coefficient \((-1)^mc_m\) in the cyclic position
\(Y^{p-m}\). As \(m=0,\ldots,r-1\), these positions exhaust all cyclic
positions. For these values of \(m\), the upper bounds on the summands in
\(1+z+\cdots+z^{r-1}\) do not bind, so

\[
c_m=\binom{d+m-1}{m}. \tag{14}
\]

The term obtained by multiplying (13) by \(a\) can contribute to the same
cyclic position at the same degree \(m\geq1\) only if

\[
p-m\equiv1-d-m\pmod r,
\]

that is, only if \(q\equiv1\pmod r\). If \(q\not\equiv1\pmod r\), the
coefficient selected above is simply \((-1)^mc_m\). If
\(q\equiv1\pmod r\), it is

\[
(-1)^m(c_m-c_{m-1})
=(-1)^m\binom{d+m-2}{m} \qquad (m\geq1), \tag{15}
\]

and it is \(c_0=1\) when \(m=0\). All binomial coefficients in (14) and
(15) are nonzero modulo \(q\): their top arguments are less than \(q\)
because \(r<d<p<q\). Hence every cyclic coefficient of \(A_a\) is a
nonzero polynomial.

The two scalar corrections in (12) affect only the cyclic positions
\(Y^0\) and \(Y^p\). At \(Y^0\), the constant coefficient of
\(C_a^dG_a\) is \(-1\), so that position is nonzero. At \(Y^p\), the term
\(-a^{d-1}Y^pD(a)^d\) has degree

\[
rd+d-1=d(r+1)-1,
\]

whereas \(a^{d-1}A_a\) has degree at most \(rd\). Its leading term cannot
cancel. The two positions are distinct because \(\gcd(p,r)=1\) and
\(r\geq2\). All other positions equal \(a^{d-1}\) times the corresponding
nonzero coefficient of \(A_a\). This proves that every \(W_k\) is
nonzero.

Let \(L=d(r+1)-1\). The common exceptional set has size at most \(r\),
and each of the \(r\) nonzero polynomials \(W_k\) has at most \(L\) roots.
Therefore

\[
\begin{aligned}
\#\{a\in\mathbb F_q^\times:\exists k,\ e_{q,k}(a)=0\}
&\leq r+rL\\
&=rd(r+1),
\end{aligned}
\]

and hence

\[
\Pr_{a\in\mathbb F_q^\times}
 \bigl(\exists k:e_{q,k}(a)=0\bigr)
\leq\frac{rd(r+1)}{q-1}. \tag{16}
\]

## 4. The complete raw-coefficient scan

A uniform unit modulo \(N=pq\) corresponds under CRT to independent
uniform elements of \(\mathbb F_p^\times\) and
\(\mathbb F_q^\times\). If an integer coefficient \(e_k(a)\) satisfies

\[
1<\gcd(e_k(a),N)<N,
\]

then either its reduction modulo \(p\) or its reduction modulo \(q\) is
zero. Combining (4) and (16) gives

\[
\boxed{
\Pr\bigl(\exists k:1<\gcd(e_k(a),N)<N\bigr)
\leq
\frac{rd}{p-1}+\frac{rd(r+1)}{q-1}.}
\tag{17}
\]

The union over \(k\) was already taken locally. Thus (17) bounds a scan
of every raw coefficient, not a preselected coefficient.

## 5. Local nullity

Let

\[
\nu_\ell(a,r)=\deg\gcd(E_a\bmod\ell,X^r-1).
\]

Since \(\ell\nmid r\), the polynomial \(X^r-1\) has exactly \(r\)
distinct roots in an algebraic closure of \(\mathbb F_\ell\). Therefore
\(\nu_\ell>0\) precisely when \(E_a(\zeta)=0\) for at least one of those
roots \(\zeta\).

### 5.1 The \(p\)-side

Fix \(\zeta^r=1\) in \(\overline{\mathbb F}_p\). Evaluating (2), grouping
by the power \(a^m\), and putting

\[
c=\zeta^{p(p-1)},
\]

gives

\[
E_a(\zeta)=
\sum_{m=1}^d
\zeta^{p(d+1-m)}
\left(\binom d m c+\binom d{m-1}\right)a^m. \tag{18}
\]

This polynomial has degree at most \(d\). If it were zero identically,
its coefficients at \(m=1\) and \(m=d\) would give

\[
dc+1=0,\qquad c+d=0,
\]

and hence \(d^2=1\pmod p\).

The gap \(d=q-p\) is a positive even integer because \(p,q\) are distinct
odd primes. Under \(d<p-1\),

\[
2\leq d\leq p-2.
\]

The only solutions of \(x^2=1\) in \(\mathbb F_p\) are \(x=1\) and
\(x=-1\). Thus \(d^2\neq1\pmod p\), and (18) is nonzero. Each fixed
\(\zeta\) therefore excludes at most \(d\) shifts in
\(\mathbb F_p^\times\). A union bound over the \(r\) roots gives

\[
\Pr(\nu_p(a,r)>0)\leq\frac{rd}{p-1}. \tag{19}
\]

This argument uses \(d<p-1\), but it does not use a stronger condition
such as \(p>d^2+1\).

### 5.2 The \(q\)-side

Fix \(\zeta^r=1\) in \(\overline{\mathbb F}_q\) and put
\(Y=\zeta^q\). If \(E_a(\zeta)=0\), equation (5) implies
\(G_a(\zeta)=0\). As a polynomial in \(a\), (6) has degree at most
\(2d-1\), and it is nonzero because

\[
G_0(\zeta)=-Y^d\neq0.
\]

Thus each fixed \(\zeta\) excludes at most \(2d-1\) unit shifts. A union
bound gives

\[
\Pr(\nu_q(a,r)>0)
\leq\frac{r(2d-1)}{q-1}
\leq\frac{2rd}{q-1}. \tag{20}
\]

Combining (19) and (20) under CRT gives

\[
\boxed{
\Pr\bigl(\nu_p(a,r)>0\text{ or }\nu_q(a,r)>0\bigr)
\leq\frac{rd}{p-1}+\frac{2rd}{q-1}.}
\tag{21}
\]

The proof of (21) needs only \(d<p-1\), together with the basic setup; it
does not need \(r<d\).

## 6. The resultant channel and the one-trial bound

Over a field, the resultant of \(E_a\) and \(X^r-1\) is zero exactly when
the two polynomials have a common root. Thus, if the integer resultant has
a proper gcd with \(N\), at least one of the two local nullities is
positive. A union bound between the complete raw-coefficient event (17)
and the nullity/resultant event (21) gives

\[
\boxed{
\Pr(\text{either channel is useful})
\leq
\frac{2rd}{p-1}+\frac{rd(r+3)}{q-1}.}
\tag{22}
\]

## 7. The Baker--Harman--Pintz family

Use the stated Baker--Harman--Pintz theorem: for every sufficiently large
\(x\), the interval

\[
[x-x^{0.525},x]
\]

contains a prime. Let \(p\) range through unbounded primes, put

\[
H=\lfloor p^{3/5}\rfloor,
\qquad x=p+H,
\]

and choose a prime \(q\in[x-x^{0.525},x]\). Since

\[
x^{0.525}=p^{0.525}(1+o(1))=o(p^{3/5}),
\]

we have, for all sufficiently large \(p\),

\[
0<H-x^{0.525}\leq q-p\leq H.
\]

Consequently \(q>p\), \(q<2p\), and

\[
\boxed{d=q-p=\Theta(p^{3/5}).} \tag{23}
\]

This produces infinitely many balanced pairs. It also gives
\(d<p-1\) for all sufficiently large pairs.

## 8. An adaptive numerical-QP bank

Consider trial \(i\) after conditioning on its complete previous public
transcript. The bank fixes \(r_i\), with \(\gcd(r_i,N)=1\), before drawing
the next shift. The new shift is conditionally uniform in
\((\mathbb Z/N\mathbb Z)^\times\). Therefore (22) applies conditionally,
even though \(r_i\) depends on earlier trials:

\[
\Pr(U_i\mid\text{previous transcript})
\leq
d\left(
\frac{2r_i}{p-1}+
\frac{r_i(r_i+3)}{q-1}
\right), \tag{24}
\]

where \(U_i\) is the event that either allowed channel is useful in trial
\(i\). No independence between different trials is needed. Sequential
conditioning followed by the union bound gives, for a predictable and
possibly random sequence \((r_i)\),

\[
\boxed{
\Pr\left(\bigcup_iU_i\right)
\leq
\mathbb E\!\left[
d\sum_i\left(
\frac{2r_i}{p-1}+
\frac{r_i(r_i+3)}{q-1}
\right)\right].}
\tag{25}
\]

Equivalently, the expression inside the expectation is the conditional
union-bound budget accumulated along a transcript. If the resource limits
give a deterministic bound on that sum, the expectation can be omitted and
the probability is at most

\[
d\sum_i\left(
\frac{2r_i}{p-1}+
\frac{r_i(r_i+3)}{q-1}
\right), \tag{25a}
\]

with the right-hand side read as that deterministic bound. These statements
apply once every \(r_i<d\).

For a numerical quasi-polynomial trial count and numerical
quasi-polynomial values of the moduli, the trial count, every \(r_i\),
and the two numerator sums in (25) are \(2^{o(n)}\), where \(n\) is the
bit length of \(N\). On the family (23), \(p<q<2p\) implies

\[
n=2\log_2p+O(1),
\]

while \(d=\Theta(p^{3/5})=2^{\Theta(n)}\). Hence every numerical-QP
\(r_i\) is eventually less than \(d\), and (25) is

\[
\frac d p\,2^{o(n)}
=p^{-2/5+o(1)}
=2^{-\Omega(n)}. \tag{26}
\]

Thus

\[
\boxed{
\Pr(\text{some trial is useful})=2^{-\Omega(n)}.}
\tag{27}
\]

## 9. Exact scope

The proof covers a fresh conditionally uniform unit shift in each trial. It
allows the numerical-QP modulus to depend on the full earlier public
transcript, provided the modulus is fixed before that trial's shift. Each
trial can scan every raw cyclic coefficient and can use the full
resultant/local-nullity event.

The proof depends on four integer-specific inputs:

1. \(N=pq\) supplies the two Frobenius collapses.
2. The actual prime gap \(d=q-p\) supplies the local polynomial degrees.
3. The identity \(a^{q-1}=1\) clears the negative exponent on the
   \(q\)-side for unit shifts.
4. The unconditional short-interval theorem supplies the infinite balanced
   family.

It does not cover biased, nonuniform, or carry-correlated shifts; a modulus
chosen after seeing the same shift; fixed shifts with random evaluation
points; joint processing of typical nonzero coefficients; multi-shift
elimination; or implicitly represented moduli whose numerical values are
larger than numerical quasi-polynomial. It therefore proves the stated
obstruction only for the two specified single-trial channels and their
adaptive fresh-uniform repetition.

## Verdict

**PASS.** The authenticated statement's coefficient bounds, nullity bound,
adaptive union bound, BHP calibration, exponential estimate, and stated
scope all follow from the identities above.
