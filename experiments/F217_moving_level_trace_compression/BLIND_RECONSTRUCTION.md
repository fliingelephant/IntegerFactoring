# F217 moving-level trace compression: statement-only blind reconstruction

## Integrity and verdict

Before the statement was opened, its SHA-256 digest was verified as

```text
f6bada7e65dc7c6617760cb1ce1e7b87618953cea6f46d11dc0d1fd8416e384d
```

This matches the preregistered digest.

**Verdict: PASS within every stated conditional and named-model scope.**
Theorems A--E admit symbolic end-to-end reconstructions. They provide
conditional factor transitions and exact boundaries for explicit
representations. They do not construct any of the missing coefficient
evaluators, do not give an unconditional factoring algorithm, and do not
prove a lower bound against arbitrary compressed algorithms.

This reconstruction uses only the repository-root `PROMPT.md` and the
hash-verified F217 `STATEMENT.md`. It uses no mathematical computation.

## 1. Setup and elementary consequences

Assume

\[
N=pq,\qquad p<q<2p,\qquad N\equiv3\pmod4, \tag{1}
\]

where \(p,q\) are distinct odd primes. Put

\[
K=\frac{N-1}{2},\qquad
G=(\mathbb Z/K\mathbb Z)^\times,
\qquad n=\lfloor\log_2N\rfloor+1. \tag{2}
\]

The complete factorization of \(K\) is granted.

Because \(N\equiv3\pmod4\), \(K\) is odd. The smallest input in (1) is
\(15=3\cdot5\), so \(K\ge7\). Also

\[
N=2K+1\equiv1\pmod K. \tag{3}
\]

Every divisor of \(N\) is a unit modulo \(K\). For example, a common
divisor of \(p\) and \(K\) would divide both \(pq=N\) and \(2K=N-1\),
hence would divide \(1\). The same argument applies to \(q\). Equation
(3) gives

\[
q\equiv p^{-1}\pmod K. \tag{4}
\]

Both unknown factors are strictly below \(K\). Indeed,

\[
2(K-q)=pq-1-2q=q(p-2)-1>0,
\]

and \(p<q\). Thus a residue modulo \(K\) known to be either \(p\) or
\(q\) is already the corresponding integer factor.

The balance condition implies

\[
\sqrt{N/2}<p<\sqrt N<q<\sqrt{2N}. \tag{5}
\]

In particular, \(p,q=2^{\Omega(n)}\) as numerical quantities. All QP
claims below, however, are in the bit length \(n\). They charge all work,
precision, character and coordinate encodings, retained decoder state,
queries, and output bits at the current node.

For any character \(\chi:G\to\mathbb C^\times\), define

\[
D_N(\chi)=\sum_{d\mid N}\chi(d). \tag{6}
\]

Equations (3) and (4) give the basic trace identity

\[
\boxed{D_N(\chi)=2+\chi(p)+\chi(p)^{-1}.} \tag{7}
\]

## 2. Theorem A: at most \(2r-1\) traces align the inversion orbit

### 2.1 Separate premises

In addition to the granted factorization of \(K\), assume all of the
following independently:

1. A certified isomorphism
   \[
   \iota:\prod_{i=1}^r C_{m_i}\xrightarrow{\sim}G,
   \qquad m_i\ge2, \tag{8}
   \]
   whose forward and inverse coordinate maps run in QP time.
2. Succinct QP-size encodings of the coordinate characters
   \[
   \chi_i(\iota(a_1,\ldots,a_r))
   =\exp(2\pi i a_i/m_i) \tag{9}
   \]
   and of their pairwise products.
3. A certified evaluator that, for each adaptively requested character in
   the bank used below, returns \(D_N(\chi)\) with absolute error at most
   \[
   \epsilon=2^{-4n-20}, \tag{10}
   \]
   using QP time and QP total state.

Factoring \(K\) alone does not supply (8), an inverse coordinate map or
discrete logarithms, succinct evaluation of high-order characters, or the
evaluator in premise 3. The proof below invokes each as an explicit
premise.

### 2.2 Recovering every coordinate up to sign

Write the hidden coordinate vector of \(p\) as

\[
x=(x_1,\ldots,x_r)\in\prod_i\mathbb Z/m_i\mathbb Z.
\]

Then \(q=p^{-1}\) has coordinate vector \(-x\). By (7),

\[
D_N(\chi_i)
=2+2\cos(2\pi x_i/m_i). \tag{11}
\]

One query therefore determines the inversion orbit
\(\{x_i,-x_i\}\), provided the precision separates distinct orbits.
For integers \(a,b\) that are not congruent up to sign modulo \(m\),

\[
\begin{aligned}
&\left|2+2\cos(2\pi a/m)-2-2\cos(2\pi b/m)\right|\\
&\quad=4\left|\sin\frac{\pi(a+b)}m\right|
          \left|\sin\frac{\pi(a-b)}m\right|.
\end{aligned} \tag{12}
\]

Both sine factors are nonzero. For a nonzero residue \(j\pmod m\),

\[
|\sin(\pi j/m)|\ge\sin(\pi/m)\ge2/m.
\]

Thus distinct inversion-orbit traces in (11) are separated by at least

\[
16/m_i^2. \tag{13}
\]

Since \(m_i\le|G|<K<N<2^n\), this separation is greater than
\(2^{-2n+4}\), far larger than (10).

This decoding does not require enumeration of the \(m_i\) possible
coordinates. Let \(b_i\) be the unique representative of
\(\{x_i,-x_i\}\) in \([0,m_i/2]\). A certified evaluation of
\(\arccos((D_N(\chi_i)-2)/2)\), followed by scaling by
\(m_i/(2\pi)\) and rounding, recovers \(b_i\). Near \(0\) or \(\pi\),
the inverse-cosine conditioning loses at most a square root of the input
accuracy. The square root of (10) is still \(2^{-2n-10}\), much smaller
than the angular spacing \(2\pi/m_i>2\pi2^{-n}\). Standard certified
arithmetic to \(O(n)\) bits performs this step in polynomial, hence QP,
time. Equivalently, (12)--(13) certify the unique rounded answer.

A coordinate is self-inverse exactly when

\[
2x_i=0\pmod{m_i}; \tag{14}
\]

these are precisely the cases \(b_i=0\), and also \(b_i=m_i/2\) when
\(m_i\) is even. All other coordinates are active.

### 2.3 Aligning the signs

At least one coordinate must be active. Otherwise \(x=-x\), so
\(p\equiv q\pmod K\). Because \(0<p<q<K\), this is impossible.

Choose one active coordinate \(i_0\), and orient its recovered
representative arbitrarily. For every other active coordinate \(i\), query
the product character \(\chi_{i_0}\chi_i\). Put

\[
\alpha=2\pi b_{i_0}/m_{i_0},
\qquad \beta=2\pi b_i/m_i.
\]

Depending on whether the two hidden signs agree or disagree, the returned
trace is one of

\[
2+2\cos(\alpha+\beta),
\qquad
2+2\cos(\alpha-\beta). \tag{15}
\]

Their difference in absolute value is

\[
4|\sin\alpha\sin\beta|. \tag{16}
\]

Because both coordinates are active, neither sine vanishes. Moreover,

\[
|\sin\alpha|\ge2/m_{i_0},
\qquad |\sin\beta|\ge2/m_i,
\]

so (16) is at least

\[
\frac{16}{m_{i_0}m_i}>2^{-2n+4}. \tag{17}
\]

The precision (10), together with QP certified evaluation of the two
predicted values, therefore determines the relative sign uniquely.
Self-inverse coordinates need no alignment.

The assembled coordinate vector is either \(x\) or \(-x\) in all
coordinates. Applying the forward map in (8) returns either \(p\bmod K\)
or \(q\bmod K\), and hence the actual integer \(p\) or \(q\). Division
and multiplication verify the factor and recover the unordered pair.

### 2.4 Query and cost bounds

The decoder makes \(r\) coordinate-character queries and at most one
product query for each coordinate other than the anchor. Hence it uses at
most

\[
\boxed{2r-1} \tag{18}
\]

coefficient evaluations. Since

\[
2^r\le\prod_i m_i=|G|=\varphi(K)<K<N<2^n,
\]

we have \(r\le n\), and therefore

\[
\boxed{2r-1\le2n-1.} \tag{19}
\]

All numerical precision is \(O(n)\) bits, the assumed coordinate maps and
encodings are QP, and the evaluator is assumed QP in both total time and
state. The number of queries is polynomial. Thus the complete conditional
decoder is QP.

The conclusion is exactly conditional: it proves that a small separating
bank of traces suffices once all three premises are supplied. It does not
derive those premises from \(\operatorname{factor}(K)\), and in particular
does not construct the divisor-coefficient evaluator.

## 3. Theorem B: the tautological ring coefficient

In the integral group algebra \(\mathbb Z[G]\), define

\[
\mathcal A_N=\sum_{d\mid N}[d\bmod K]. \tag{20}
\]

The tautological map \(G\to(\mathbb Z/K\mathbb Z)^\times\),
\(a\mapsto a\), extends \(\mathbb Z\)-linearly to a ring map

\[
\Theta_K:\mathbb Z[G]\longrightarrow\mathbb Z/K\mathbb Z,
\qquad \Theta_K([a])=a\pmod K. \tag{21}
\]

It is multiplicative because \([a][b]=[ab]\), and additive by its linear
extension.

The four divisors of \(N\), together with (3)--(4), give the exact identity

\[
\boxed{\mathcal A_N=2[1]+[p]+[p^{-1}].} \tag{22}
\]

Applying (21) gives

\[
\boxed{
\Theta_K(\mathcal A_N)
=\sigma_1(N)\pmod K
\equiv2+p+q\pmod K.} \tag{23}
\]

To interpret the residue, observe that

\[
2\bigl(K-(p+q)\bigr)
=pq-1-2p-2q
=(p-2)(q-2)-5. \tag{24}
\]

If \(p\ge5\), then \(q\ge7\), and the last expression is positive. If
\(p=3\), balance forces \(3<q<6\), hence \(q=5\) and \(N=15\). Thus,
except for \(N=15\),

\[
0<p+q<K. \tag{25}
\]

Consequently, if

\[
s=\bigl(\Theta_K(\mathcal A_N)-2\bigr)\bmod K \tag{26}
\]

is represented by its least nonnegative residue, then \(s=p+q\) for every
nonexceptional input. The polynomial

\[
X^2-sX+N \tag{27}
\]

has roots \(p,q\). An exact integer square root of its discriminant and
the quadratic formula recover them in polynomial bit complexity. For
\(N=15\), trial division by \(3\) gives the factorization directly.

Therefore one exact \(O(n)\)-bit evaluator for

\[
\Theta_K(\mathcal A_N)=\sigma_1(N)\pmod K
\]

is a factor transition on this setup. The theorem identifies that target;
it supplies no algorithm for evaluating it.

## 4. Theorem C: the moving-weight Eisenstein coefficient

Since \(K>1\) is odd, \(\varphi(K)\) is even. Set

\[
k=\varphi(K)+2. \tag{28}
\]

Then \(k\ge4\) is even. The granted factorization of \(K\) makes \(k\)
explicitly computable. Define

\[
\mathcal G_k(\tau)
=-\frac{B_k}{2k}
+\sum_{m\ge1}\sigma_{k-1}(m)q^m,
\qquad q=e^{2\pi i\tau}. \tag{29}
\]

Equivalently,

\[
\mathcal G_k=-\frac{B_k}{2k}E_k,
\qquad
E_k=1-\frac{2k}{B_k}
\sum_{m\ge1}\sigma_{k-1}(m)q^m. \tag{30}
\]

The constant coefficient in (29) can be nonintegral, but every
nonconstant coefficient is the integer \(\sigma_{k-1}(m)\).

Every divisor \(d\mid N\) is coprime to \(K\), so Euler's theorem gives

\[
d^{\varphi(K)}\equiv1\pmod K.
\]

As \(k-1=\varphi(K)+1\), it follows that

\[
d^{k-1}\equiv d\pmod K.
\]

Summing over the divisors of \(N\) proves

\[
\boxed{
[q^N]\mathcal G_k
=\sigma_{k-1}(N)
\equiv\sigma_1(N)
\equiv2+p+q\pmod K.} \tag{31}
\]

Thus a QP evaluator that returns this single coefficient directly modulo
\(K\), with every same-node operation charged, factors \(N\) through
Theorem B.

The output size and standard internal state must be distinguished. For an
odd prime power \(\ell^e\),

\[
\frac{\varphi(\ell^e)^2}{\ell^e}
=\ell^{e-2}(\ell-1)^2\ge1.
\]

Multiplicativity therefore gives

\[
\varphi(K)\ge\sqrt K=2^{\Omega(n)}. \tag{32}
\]

Hence the numeric weight \(k\), and the dimension
\(\dim M_k(\mathrm{SL}_2(\mathbb Z))=\Theta(k)\) of a dense level-one
weight-\(k\) modular-form representation, are exponential in \(n\).
Moreover,

\[
\sigma_{k-1}(N)
=1+p^{k-1}+q^{k-1}+N^{k-1}
\]

has \(\Theta(kn)=2^{\Omega(n)}\) exact output bits. By contrast, the binary
encoding of \(k\le K+1\) and the requested residue modulo \(K\) each have
only \(O(n)\) bits.

This establishes a boundary for standard methods whose state is dense in
the numeric weight, or which first produce the unrestricted exact integer.
It is not a lower bound on a random-access algorithm that accepts the
binary encoding of \(k\) and returns only the modular residue in (31).

## 5. Theorem D: the prime-\(K\) eta quotient

Assume now, in addition, that \(K=r\) is prime. The setup has \(r\ge7\).
Define

\[
P(q)=\prod_{a\ge1}(1-q^a),
\qquad
F_r(q)=\frac{P(q)^r}{P(q^r)}
=\frac{\eta(\tau)^r}{\eta(r\tau)}. \tag{33}
\]

The equality follows from \(\eta(\tau)=q^{1/24}P(q)\): the powers of
\(q\) cancel.

### 5.1 Modularity, character, and cusps

The eta exponents at divisors \(1,r\) of the level are

\[
e_1=r,qquad e_r=-1.
\]

Their half-sum is the integral weight

\[
w=\frac{r-1}{2}. \tag{34}
\]

The two eta-quotient congruences are

\[
\sum_{\delta\mid r}\delta e_\delta=r-r=0\pmod{24}, \tag{35}
\]

and

\[
\sum_{\delta\mid r}\frac r\delta e_\delta
=r^2-1=0\pmod{24}. \tag{36}
\]

Equation (36) holds because every prime \(r>3\) satisfies
\(r^2\equiv1\pmod{24}\). The eta-quotient transformation criterion thus
gives a weight-\(w\) form on \(\Gamma_0(r)\). Its quadratic character is

\[
\boxed{
\chi_r(d)=\left(\frac{(-1)^w r}{d}\right).} \tag{37}
\]

In the usual character formula the eta product contributes the square
class of \(r^{-1}\); multiplying by the square \(r^2\) gives the equivalent
square class \(r\), yielding (37) for \(d\) coprime to \(r\).

The order at infinity is

\[
\frac1{24}\sum_{\delta\mid r}\delta e_\delta=0. \tag{38}
\]

At the other cusp, the Fricke transformation follows from
\(\eta(-1/\tau)=(-i\tau)^{1/2}\eta(\tau)\), up to its harmless root of
unity. After the weight factor is removed, it is a nonzero constant times

\[
\frac{\eta(r\tau)^r}{\eta(\tau)}.
\]

Its order at infinity is

\[
\frac{r^2-1}{24}>0. \tag{39}
\]

Thus \(F_r\) is holomorphic at both cusps, with order zero at infinity and
positive Fricke-cusp order (39). This proves the asserted holomorphic
eta-quotient modularity, including its level, weight, and character.

### 5.2 The coefficient modulo \(r^2\)

For an indeterminate \(x\), the binomial theorem gives

\[
\frac{(1-x)^r}{1-x^r}
=1+\sum_{j=1}^{r-1}(-1)^j\binom rj
\frac{x^j}{1-x^r}. \tag{40}
\]

For \(1\le j<r\),

\[
\binom rj=\frac rj\binom{r-1}{j-1},
\qquad
\binom{r-1}{j-1}\equiv(-1)^{j-1}\pmod r.
\]

Therefore

\[
(-1)^j\binom rj\equiv-rj^{-1}\pmod{r^2}, \tag{41}
\]

where \(j^{-1}\) is understood modulo \(r\); after multiplication by
\(r\), this specifies a residue modulo \(r^2\). Expanding
\((1-x^r)^{-1}\) in (40) yields

\[
\frac{(1-x)^r}{1-x^r}
\equiv1-r\sum_{j=1}^{r-1}\sum_{h\ge0}
j^{-1}x^{j+hr}\pmod{r^2}. \tag{42}
\]

Apply (42) with \(x=q^a\) and multiply over \(a\ge1\). Coefficientwise,
only finitely many factors contribute to any fixed power of \(q\), and
every product of two nonconstant terms is divisible by \(r^2\). Hence

\[
\boxed{
F_r(q)\equiv
1-r\sum_{a\ge1}\sum_{j=1}^{r-1}\sum_{h\ge0}
j^{-1}q^{a(j+hr)}
\pmod{r^2}.} \tag{43}
\]

Let \(r\nmid m\). The triples contributing to \(q^m\) in (43) correspond
bijectively to divisors \(b\mid m\): write

\[
b=j+hr,qquad a=m/b,
\]

with \(j\in\{1,\ldots,r-1\}\) the nonzero residue of \(b\pmod r\).
It follows that

\[
-\frac{[q^m]F_r}{r}
\equiv\sum_{b\mid m}b^{-1}
\equiv m^{-1}\sum_{b\mid m}\frac mb
\equiv m^{-1}\sigma_1(m)\pmod r. \tag{44}
\]

Equation (43) also shows that \([q^m]F_r\) is divisible by \(r\), and
that its residue modulo \(r^2\) determines the quotient in (44) modulo
\(r\).

At \(m=N=2r+1\), one has \(r\nmid N\) and \(N^{-1}\equiv1\pmod r\).
Therefore

\[
\boxed{
-\frac{[q^N]F_r}{r}
\equiv\sigma_1(N)
\equiv2+p+q\pmod r.} \tag{45}
\]

One coefficient residue modulo \(r^2\) has \(O(n)\) bits. If a QP
evaluator returns it, division by \(r\) modulo \(r\), followed by Theorem
B, factors every member of the prime-\(K\) subfamily. The input \(N=15\),
for which \(r=7\) but the least-residue lifting in Theorem B fails, is
handled by trial division by \(3\).

### 5.3 Exact Lambert-series packaging and cost boundary

Formal logarithmic differentiation gives

\[
q\frac d{dq}\log P(q)
=-\sum_{a\ge1}\frac{aq^a}{1-q^a}
=-\sum_{m\ge1}\sigma_1(m)q^m
=-L(q). \tag{46}
\]

The same formula with \(q^r\) gives

\[
q\frac d{dq}\log P(q^r)=-rL(q^r).
\]

Using (33),

\[
\boxed{
-\frac1r q\frac d{dq}\log F_r(q)
=L(q)-L(q^r),
\qquad
L(q)=\sum_{m\ge1}\sigma_1(m)q^m.} \tag{47}
\]

Thus the eta quotient packages the original Lambert-series target exactly;
it does not create an evaluator for it. Standard power-series truncation
through \(q^N\) retains \(N+1=\Theta(N)=2^{\Omega(n)}\) coefficient
positions. Standard dense modular-form state also uses the numeric level
\(r\) and weight \((r-1)/2\), both \(2^{\Omega(n)}\). These are boundaries
for those standard explicit states, not lower bounds against random-access
coefficient extraction or compressed products.

## 6. Theorem E: the twisted Ramanujan expansion

Let \(\chi\) be a Dirichlet character modulo \(K\), and let
\(\Re(s)>0\). Define

\[
A_{\chi,s}(n)=\sum_{d\mid n}\chi(d)d^{-s}, \tag{48}
\]

and

\[
c_m(n)=\sum_{e\mid(m,n)}e\,\mu(m/e). \tag{49}
\]

For fixed \(n\) and \(\sigma=\Re(s)>0\), the relevant series is absolutely
convergent. Indeed,

\[
\begin{aligned}
\sum_{m\ge1}\frac{|c_m(n)|}{m^{\sigma+1}}
&\le\sum_{e\mid n}e
\sum_{k\ge1}\frac{|\mu(k)|}{(ek)^{\sigma+1}}\\
&=\sum_{e\mid n}e^{-\sigma}
\sum_{k\ge1}\frac{|\mu(k)|}{k^{\sigma+1}}<\infty.
\end{aligned} \tag{50}
\]

Therefore sums may be rearranged. Substituting (49), writing \(m=ek\),
and using complete multiplicativity of \(\chi\) gives

\[
\begin{aligned}
\sum_{m\ge1}\frac{\chi(m)c_m(n)}{m^{s+1}}
&=\sum_{e\mid n}e
  \sum_{k\ge1}
  \frac{\chi(ek)\mu(k)}{(ek)^{s+1}}\\
&=\left(\sum_{e\mid n}\chi(e)e^{-s}\right)
  \left(\sum_{k\ge1}\frac{\chi(k)\mu(k)}{k^{s+1}}\right).
\end{aligned} \tag{51}
\]

For \(\Re(s+1)>1\), the last factor is the absolutely convergent Euler
product \(1/L(s+1,\chi)\). Hence

\[
\boxed{
A_{\chi,s}(n)
=L(s+1,\chi)
\sum_{m\ge1}\frac{\chi(m)c_m(n)}{m^{s+1}}.} \tag{52}
\]

For \(n=1\), one has \(A_{\chi,s}(1)=1\) and
\(c_m(1)=\mu(m)\). Subtracting this public baseline from (52) gives

\[
A_{\chi,s}(N)-1
=L(s+1,\chi)
\sum_{m\ge1}
\frac{\chi(m)(c_m(N)-\mu(m))}{m^{s+1}}. \tag{53}
\]

If \(m<p\), then \((m,N)=1\), so (49) gives

\[
c_m(N)=\mu(m).
\]

Every term before index \(p\) in (53) is therefore exactly zero. At
\(m=p\),

\[
c_p(N)=\mu(p)+p\mu(1)=p-1,
\qquad c_p(N)-\mu(p)=p. \tag{54}
\]

Since \((p,K)=1\), \(\chi(p)\ne0\). The first factor-sensitive term before
the common prefactor is consequently

\[
\boxed{
\frac{\chi(p)p}{p^{s+1}}=\chi(p)p^{-s}\ne0.} \tag{55}
\]

By (5), \(p=2^{\Omega(n)}\). A literal sequential, term-by-term
Ramanujan implementation must therefore pass through exponentially many
index positions before it encounters any factor-sensitive multiplier.
This statement concerns direct termwise access; it does not say that a
compressed treatment of the tail or of the whole series is impossible.

For a nonprincipal \(\chi\), the unweighted trace is the finite limit

\[
A_{\chi,0}(N)=\lim_{s\downarrow0}A_{\chi,s}(N).
\]

The right side of (52) or (53) at this boundary is interpreted by the same
Abel limit, or by analytic continuation. The proof asserts absolute
convergence only for \(\Re(s)>0\), and makes no ordinary-convergence claim
at \(s=0\). Theorem E is therefore not a lower bound on an arbitrary
weight-one coefficient evaluator.

## 7. Other named-model boundaries

### 7.1 Direct Hecke representatives

Because \((N,K)=1\), the standard upper-triangular representatives for the
good-index correspondence \(T_N\) are indexed by

\[
ad=N,qquad0\le b<d. \tag{56}
\]

For each divisor \(d\mid N\), there are \(d\) choices of \(b\), so their
number is

\[
\sum_{d\mid N}d=\sigma_1(N)\ge N+1=2^{\Omega(n)}. \tag{57}
\]

Directly materializing them is numeric-exponential. Moreover, their
factor-pair labels \((a,d)\) already include \((p,q)\) and \((q,p)\).
This does not exclude a compressed Hecke evaluator.

### 7.2 Diamond is not Hecke

The level-\(K\) diamond operator depends on the unit class of its index.
Equation (3) gives

\[
\langle N\rangle=\langle1\rangle.
\]

This trivial operator is not the degree-\(N\) Hecke correspondence
\(T_N\), whose explicit representatives are counted in (57). Conflating
the two loses the target rather than compressing it.

### 7.3 Standard moving-level and moving-weight state

Standard Manin-symbol state at level \(K\) materializes a set on the scale
of \(\mathbb P^1(\mathbb Z/K\mathbb Z)\), whose cardinality is
\[
K\prod_{\ell\mid K}(1+1/\ell)\ge K=2^{\Omega(n)}.
\]

Standard symmetric-power or dense modular-form state at moving weight
\(k\) has dimension on the numeric scale of \(k=2^{\Omega(n)}\), as in
Theorem C. These are explicit-state costs only. They say nothing about a
compressed representation that never materializes these coordinates.

### 7.4 Abelian representation packaging

For every representation \(\rho\) of \(G\), equations (3)--(4) give

\[
\boxed{
\sum_{d\mid N}\rho(d)
=2I+\rho(p)+\rho(p)^{-1}.} \tag{58}
\]

Over a characteristic-zero splitting field, Maschke semisimplicity and
the commutativity of \(G\) decompose every finite-dimensional
representation into one-dimensional characters. Thus inducing, summing,
or placing the coordinate characters into matrices repackages scalar
traces; it does not itself evaluate their missing divisor coefficients.
Representations that do not factor through \(G\) are outside (58) and
outside this boundary.

### 7.5 Gcd-only moving-level insertion

Since \((K,N)=1\), for every integer \(m\),

\[
\boxed{(Km,N)=(m,N).} \tag{59}
\]

Therefore inserting the moving level \(K\) into an explicit formula whose
only factor-sensitive arithmetic datum is this gcd does not make the first
noncoprime multiplier occur before \(p\). Formulae with other
factor-sensitive terms are not covered by this observation.

### 7.6 Recursion

The integer \(K=(N-1)/2\) has one fewer bit than \(N\). If a correct
all-input recursive dispatch produces only a single surviving chain and
satisfies

\[
T(n)\le T(n-1)+Q(n), \tag{60}
\]

where \(Q\) is numerical QP, unrolling gives

\[
T(n)\le T(n_0)+\sum_{j=n_0+1}^nQ(j)
\le T(n_0)+nQ(n), \tag{61}
\]

after replacing \(Q\) by a monotone QP majorant. Multiplication by \(n\)
preserves the QP form. Hence lack of a fixed-ratio size contraction is not,
by itself, an obstruction to one-child recursion.

When many recursive children survive, their number and sizes require a
branching bound; fixed-ratio contraction is one possible such control, not
a prerequisite for the single chain in (60). F217 grants
\(\operatorname{factor}(K)\). It neither rejects recursive factorization of
\(K\) nor constructs and proves a correct all-input recursive dispatch.

## 8. Exact remaining scope

Theorems A--D expose several equivalent or conditionally sufficient exact
targets:

1. a small separating bank of scalar divisor traces;
2. the tautological group-ring residue \(\sigma_1(N)\pmod K\);
3. the moving-weight Eisenstein coefficient modulo \(K\); and
4. when \(K\) is prime, the eta-quotient coefficient modulo \(K^2\).

Theorem E identifies the first factor-sensitive position in one explicit
Ramanujan expansion. The other observations delimit direct Hecke,
diamond-operator, standard dense-state, abelian-representation, gcd-only,
and recursion arguments.

The common unresolved object is a compressed exact evaluator for one of
the divisor-sum targets. F217 neither constructs such an evaluator nor
rules one out. In particular, it leaves open compressed modular symbols,
compressed Hecke or product algorithms, trace-formula and nonholomorphic
methods, nonabelian extensions, random-access residue extraction,
characteristic-specific ring circuits, and every method not confined to
the named explicit representations above.

Accordingly, none of these conditional factor transitions resolves the
all-input Las Vegas QP factoring task in `PROMPT.md`: the setup is a
balanced semiprime subfamily, essential evaluators remain premises, and no
all-input correctness or recursive cost closure is supplied.
