# Independent reconstruction: the inverse-mod-\(N\) metric cloud

## Attestation and verdict

I did not inspect any existing F39 candidate, audit, or other experiment artifact, and I did not use any proof from such an artifact. This reconstruction uses only the bare statement in the task. No computation was used.

**Verdict.** All of the requested mathematical claims are true with the scopes stated below. In particular, the sampling lower bounds proved here concern one raw empirical mean (or one raw regular-bin count), and the total-variation statement concerns only a disjoint exhaustive rectangular partition. None of the stronger excluded conclusions follows.

Throughout,

\[
e_m(t):=\exp(2\pi i t/m),\qquad
\varphi(N)=(p-1)(q-1),\qquad N=pq,
\]

where \(p\neq q\) are odd primes. A balanced family means \(p,q=N^{1/2+o(1)}\); the usual bounded-ratio definition is stronger. Balance is needed only to call a one-local-component mode an \(N^{-1/4+o(1)}\)-scale mode. The exact identities and the discrepancy proof do not need it.

## 1. Exact CRT factorization and the complete local table

For a prime \(r\), define the unnormalized prime Kloosterman sum

\[
K_r(A,B):=\sum_{x\in\mathbb F_r^\times}e_r(Ax+Bx^{-1})
\]

and its normalized version \(k_r(A,B):=K_r(A,B)/(r-1)\).

Let \(\bar q_p q\equiv1\pmod p\) and \(\bar p_q p\equiv1\pmod q\). Since

\[
q\bar q_p+p\bar p_q\equiv1\pmod{pq},
\]

we have the exact character identity

\[
e_N(t)=e_p(\bar q_p t)e_q(\bar p_q t).
\]

Under CRT, \(u\in U_N\) corresponds bijectively to \((x,y)\in\mathbb F_p^\times\times\mathbb F_q^\times\), and \(u^{-1}\) corresponds to \((x^{-1},y^{-1})\). Therefore

\[
\boxed{
\hat\mu_N(a,b)
=k_p(a\bar q_p,b\bar q_p)
 k_q(a\bar p_q,b\bar p_q).}
\tag{1}
\]

The twists are essential: both coefficients at a prime are multiplied by the inverse of the *other* prime.

### Local \(Z/D/K\) table

The three possible local states at \(r\) are as follows. Divisibility refers to the original integers \(a,b\); the CRT twist is a unit and does not change the state.

| State | Divisibility at \(r\) | Exact sum | Normalized value/bound |
|---|---|---:|---:|
| \(Z\) | \(r\mid a\) and \(r\mid b\) | \(K_r(0,0)=r-1\) | \(k_r=1\) |
| \(D\) | exactly one of \(a,b\) is divisible by \(r\) | \(K_r(A,0)=K_r(0,B)=-1\) | \(k_r=-1/(r-1)\) |
| \(K\) | \(r\nmid a\) and \(r\nmid b\) | nondegenerate | \(|k_r|\le 2\sqrt r/(r-1)\) |

The \(D\) identity is just \(\sum_{x\neq0}e_r(Ax)=-1\), with \(x\mapsto x^{-1}\) for the other orientation. The \(K\) entry is the prime Weil bound.

For completeness, the full global product table is below. In a \(K\) entry, \(k_p\) and \(k_q\) denote the appropriately twisted factors in (1).

| \(p\)-state \\ \(q\)-state | \(Z\) | \(D\) | \(K\) |
|---|---:|---:|---:|
| \(Z\) | \(1\) | \(-1/(q-1)\) | \(k_q\), \(|k_q|\le2\sqrt q/(q-1)\) |
| \(D\) | \(-1/(p-1)\) | \(1/\varphi(N)\) | \(-k_q/(p-1)\), \(|\cdot|\le2\sqrt q/\varphi(N)\) |
| \(K\) | \(k_p\), \(|k_p|\le2\sqrt p/(p-1)\) | \(-k_p/(q-1)\), \(|\cdot|\le2\sqrt p/\varphi(N)\) | \(k_pk_q\), \(|\cdot|\le4\sqrt N/\varphi(N)\) |

This table also resolves coordinate-zero cases. For example,

\[
\hat\mu_N(0,b)=
\begin{cases}
1/\varphi(N),&\gcd(b,N)=1,\\
-1/(q-1),&\gcd(b,N)=p,\\
-1/(p-1),&\gcd(b,N)=q,\\
1,&N\mid b.
\end{cases}
\tag{2}
\]

Thus a literal zero coordinate is not by itself an \(N^{-1/4}\)-scale effect.

## 2. Factor-free bound, baseline, and factor-aware modes

If \(\gcd(a,b,N)=1\), neither prime can be in local state \(Z\). The remaining four cases are \(D/D,D/K,K/D,K/K\), and every entry in the table is bounded by the \(K/K\) envelope. Hence, for every nonzero factor-free frequency,

\[
\boxed{
|\hat\mu_N(a,b)|\le \frac{4\sqrt N}{\varphi(N)}.}
\tag{3}
\]

The global zero character \((a,b)\equiv(0,0)\pmod N\) has coefficient exactly \(1\). It is the common baseline, not a distinguishing bias.

Here “one component zero” means one *CRT-local frequency pair* is \((0,0)\). A \(Z/K\) mode at \(p/q\) has size at most

\[
\frac{2\sqrt q}{q-1}=q^{-1/2+o(1)}=N^{-1/4+o(1)},
\]

and symmetrically for \(K/Z\). But local \(Z\) at \(p\) means \(p\mid a\) and \(p\mid b\). If the other local state is nonzero, then

\[
\gcd(a,b,N)=p.
\]

Thus the publicly computable gcd of the proposed frequency already reveals a nontrivial factor. The same holds with \(p,q\) interchanged. This is an algebraic screening fact, not a factoring lower bound.

### Exact second moment and attainment of the scale

For a prime \(r\), put \(S_r(t):=K_r(1,t)\). If \(A,B\neq0\), the substitution \(y=Ax\) gives

\[
K_r(A,B)=S_r(AB).
\tag{4}
\]

Now compute, exactly,

\[
\begin{aligned}
\sum_{t\neq0}|S_r(t)|^2
&=\sum_{x,y\neq0}e_r(x-y)
  \sum_{t\neq0}e_r\bigl(t(x^{-1}-y^{-1})\bigr).
\end{aligned}
\]

The inner sum is \(r-1\) when \(x=y\), and \(-1\) otherwise. Also

\[
\sum_{x,y\neq0}e_r(x-y)
=\bigl|\sum_{x\neq0}e_r(x)\bigr|^2=1,
\]

while its diagonal part is \(r-1\), so its off-diagonal part is \(2-r\). Consequently

\[
\boxed{
\sum_{t\neq0}|S_r(t)|^2=r^2-r-1,}
\qquad
\frac1{r-1}\sum_{t\neq0}|S_r(t)|^2
=r-\frac1{r-1}.
\tag{5}
\]

Equivalently,

\[
\sum_{A,B\neq0}|K_r(A,B)|^2
=(r-1)(r^2-r-1).
\]

It follows that some \(t\neq0\) obeys

\[
|S_r(t)|\ge\sqrt{r-\frac1{r-1}}.
\tag{6}
\]

Choose such a \(t\) for \(r=q\), and take the public frequency integers \(a=p\), \(b=pt\). Its \(p\)-local state is \(Z\); after the CRT twist, its \(q\)-local Kloosterman parameters are exactly \((1,t)\). Therefore

\[
|\hat\mu_N(p,pt)|
\ge
\frac{\sqrt{q-1/(q-1)}}{q-1}
=q^{-1/2}(1+o(1))
=N^{-1/4+o(1)}.
\tag{7}
\]

At the same time, \(\gcd(p,pt,N)=p\). Thus the larger scale is genuinely attained, but only by a frequency carrying a public nontrivial gcd. The symmetric construction uses \(q\).

## 3. Fixed finite trigonometric observables

Let

\[
T(x,y)=\sum_{h=(a,b)\in F}c_h e^{2\pi i(ax+by)}
\]

have finite frequency set \(F\), and let \(A=\sum_{h\in F_{\mathrm{nz}}}|c_h|\), where \(F_{\mathrm{nz}}\) contains the nonbaseline frequencies retained after the following public screen:

* \(\gcd(a,b,N)=1\): retain it;
* \(1<\gcd(a,b,N)<N\): the frequency itself reveals a factor, so it is outside the factor-free assertion;
* \(\gcd(a,b,N)=N\): it is the zero character modulo \(N\) and contributes no gap from the uniform \(N\times N\) grid.

Let \(\lambda_N\) be the uniform measure on that grid. Then the constant/zero-character terms cancel, and (3) plus the triangle inequality gives the exact advertised envelope

\[
\boxed{
\bigl|\mathbb E_{\mu_N}T-\mathbb E_{\lambda_N}T\bigr|
\le \frac{4A\sqrt N}{\varphi(N)}.}
\tag{8}
\]

For a fixed frequency set and all sufficiently large \(N\), the uniform-grid and continuous-Haar expectations coincide term by term, because no fixed nonzero frequency is a multiple of \(N\). Equation (8) is a linear, finite-\(\ell^1\) statement only. It says nothing about nonlinear processing.

## 4. Two-dimensional Erdős–Turán–Koksma, including hidden divisible frequencies

Represent the cloud in \([0,1)^2\) by

\[
\nu_N:=\frac1{\varphi(N)}\sum_{u\in U_N}
\delta_{(u/N,\;u^{-1}/N)},
\]

using the representatives in \({0,\ldots,N-1}\). Its Fourier coefficient at \((a,b)\) is \(\hat\mu_N(a,b)\).

### A self-contained ETK form

We first record the one-dimensional bracketing fact used below. For every interval \(I\) on the circle and integer \(H\ge1\), there is a nonnegative trigonometric polynomial \(P_{I,H}^+\) of degree \(H\) such that

\[
\mathbf1_I\le P_{I,H}^+,\qquad
\int_0^1P_{I,H}^+=|I|+\frac1{H+1},\qquad
|\hat P_{I,H}^+(h)|\le\frac2{\max(1,|h|)}.
\tag{9}
\]

Here is an explicit derivation. Let

\[
F_H(x)=\sum_{|h|\le H}\bigl(1-\frac{|h|}{H+1}\bigr)e^{2\pi ihx}
\]

be the Fejér kernel, and let \(\psi(x)={x}-1/2\) away from integers, with the midpoint value at integers. The finite Vaaler polynomial

\[
V_H(x)=-\sum_{1\le|h|\le H}
\frac{W(h/(H+1))}{2\pi i h}e^{2\pi ihx},
\qquad
W(t)=\pi t(1-|t|)\cot(\pi t)+|t|,
\]

satisfies the finite pointwise identity/inequality

\[
|\psi(x)-V_H(x)|
\le \frac{F_H(x)}{2H+2}.
\tag{10}
\]

This follows directly by expanding \(F_H\), pairing the \(h\) and \(-h\) terms, and completing the resulting finite positive square; thus (10) has no limiting or regularity assumption. For \(I=[\alpha,\beta)\), use

\[
\mathbf1_I(x)=|I|+\psi(\alpha-x)+\psi(x-\beta)
\]

with the appropriate one-sided endpoint convention, replace both sawtooth terms by \(V_H\), and add the two error polynomials from (10). This gives (9): its integral excess is \(1/(H+1)\), and for \(0<|h|\le H\) its coefficient is at most

\[
\frac1{\pi|h|}+\frac1{H+1}\le\frac2{|h|}.
\]

For a rectangle \(R=I\times J\), the product \(P_{I,H}^+P_{J,H}^+\) majorizes \(\mathbf1_R\), has integral excess at most \(3/(H+1)\), and has Fourier coefficients bounded by

\[
\frac4{\max(1,|a|)\max(1,|b|)}.
\]

Applying this to a probability measure \(\nu\), and applying the same upper estimate to the two disjoint rectangles making up \(R^c\), proves

\[
D^*(\nu)
\le \frac6{H+1}
+8\!\sum_{\substack{0<\max(|a|,|b|)\le H}}
\frac{|\hat\nu(a,b)|}
{\max(1,|a|)\max(1,|b|)}.
\tag{11}
\]

The constants are inessential, but (11) explicitly exhibits the weights needed below.

### Bounding every frequency class

Take \(H=\lfloor\sqrt N\rfloor\), so \(H<N\). Write

\[
w(a,b)=\frac1{\max(1,|a|)\max(1,|b|)},\qquad
L(M)=\sum_{1\le|m|\le M}\frac1{|m|}\le2(1+\log\max(1,M)).
\]

Partition the nonzero ETK frequencies into

\[
\mathcal G={(a,b):\gcd(a,b,N)=1},\qquad
\mathcal P={(a,b):p\mid a,b},\qquad
\mathcal Q={(a,b):q\mid a,b}.
\]

Since \(H<N\), the last two sets are disjoint in the nonzero box, and the three sets exhaust it.

For \(\mathcal G\), (3) gives

\[
\sum_{\mathcal G}w(a,b)|\hat\mu_N(a,b)|
\le\frac{4\sqrt N}{\varphi(N)}
\bigl((1+2\mathrm H_H)^2-1\bigr)
=O\bigl(N^{-1/2}\log^2N\bigr),
\tag{12}
\]

where \(\mathrm H_H\) is the \(H\)-th harmonic number and \(\varphi(N)\asymp N\).

It remains to include, rather than silently omit, the hidden divisible frequencies. Fix \(d\in{p,q}\), put \(s=N/d\), and set \(M_d=\lfloor H/d\rfloor\). A nonzero frequency divisible in both coordinates by \(d\) is \((dm,dn)\).

* If \(mn\neq0\), its local types are \(Z/K\), because a nonzero coordinate of size below \(N\) cannot also be divisible by \(s\). Its coefficient is at most \(2\sqrt s/(s-1)\).
* If exactly one of \(m,n\) is zero, its local types are \(Z/D\), and its coefficient has exact magnitude \(1/(s-1)\).

Thus the full weighted contribution of the \(d\)-divisible class is bounded by

\[
\boxed{
\frac{2L(M_d)}{d(s-1)}
+\frac{2\sqrt s\,L(M_d)^2}{d^2(s-1)}.}
\tag{13}
\]

The first term is \(O(N^{-1}\log N)\). For the second, use

\[
\frac{\sqrt s}{d^2(s-1)}
\le\frac{3}{2d^2\sqrt s}
=\frac{3}{2\sqrt N\,d^{3/2}}
=O(N^{-1/2}).
\]

Summing (13) for \(d=p,q\) therefore costs only \(O(N^{-1/2}\log^2N)\). Combining (11)--(13) proves

\[
\boxed{D^*(\nu_N)=O\bigl(N^{-1/2}\log^2N\bigr).}
\tag{14}
\]

This proof explicitly accounts for the \(p\)- and \(q\)-divisible modes. Their larger Fourier coefficients are offset by the ETK weights of frequencies whose two coordinates are multiples of the same divisor.

### Rectangles and the precise TV scope

Any half-open axis-parallel rectangle is an inclusion--exclusion combination of four anchored rectangles. Hence

\[
|\nu_N(R)-\lambda(R)|\le4D^*(\nu_N)
=O\bigl(N^{-1/2}\log^2N\bigr).
\tag{15}
\]

For any fixed collection \(R_1,\ldots,R_B\), the maximum error has the same order and the sum of absolute errors is at most \(4B D^*\).

Only if \(R_1,\ldots,R_B\) are disjoint and exhaust \([0,1)^2\) do they define two bin-label probability distributions \(P_j=\nu_N(R_j)\) and \(Q_j=\lambda(R_j)\). In that case, and only in that sense,

\[
\mathrm{TV}(P,Q)
=\frac12\sum_{j=1}^B|P_j-Q_j|
\le2B D^*(\nu_N)
=O_B\bigl(N^{-1/2}\log^2N\bigr).
\tag{16}
\]

An overlapping collection of rectangles does not define a bin distribution, so its \(\ell^1\) error is not total variation.

## 5. What raw empirical means do and do not prove

Let \(U_1,\ldots,U_m\) be iid uniform samples from \(U_N\), and for one fixed frequency define

\[
X_j=e_N(aU_j+bU_j^{-1}),\qquad
\theta=\mathbb EX_j=\hat\mu_N(a,b),\qquad
\bar X_m=\frac1m\sum_{j=1}^mX_j.
\]

Because \(|X_j|=1\), independence gives the exact complex MSE

\[
\boxed{
\mathbb E|\bar X_m-\theta|^2
=\frac{1-|\theta|^2}{m}.}
\tag{17}
\]

For \(\theta\neq0\), the relative RMSE is therefore

\[
\frac{\sqrt{\mathbb E|\bar X_m-\theta|^2}}{|\theta|}
=\sqrt{\frac{1-|\theta|^2}{m|\theta|^2}}.
\tag{18}
\]

For a factor-free nonzero frequency, put \(c_N=4\sqrt N/\varphi(N)\). Requiring relative RMSE at most \(\epsilon\) forces

\[
m\ge\frac{1-|\theta|^2}{\epsilon^2|\theta|^2}
\ge\frac{(1-c_N^2)\varphi(N)^2}{16\epsilon^2N}
=\Omega_\epsilon(N).
\tag{19}
\]

In particular this is \(N^{1-o(1)}\). If the actual nonzero coefficient is smaller than the envelope, more samples are required.

### Complex fourth moment and a correctly quantified confidence statement

An MSE identity alone is not a high-probability lower bound. Here is the precise constant-confidence statement that follows from a fourth moment and Paley--Zygmund.

Let \(Y=X-\theta\), and define

\[
\sigma^2=\mathbb E|Y|^2=1-|\theta|^2,\qquad
\tau=\mathbb EY^2,\qquad
\kappa=\mathbb E|Y|^4.
\]

A direct enumeration of the index coincidences in
\(\mathbb E|\sum_jY_j|^4\) gives the exact complex fourth moment

\[
\boxed{
\mathbb E|\bar X_m-\theta|^4
=\frac{m\kappa+m(m-1)(2\sigma^4+|\tau|^2)}{m^4}.}
\tag{20}
\]

Indeed, the three two-index pairings are the two conjugate pairings, each contributing \(\sigma^4\), and the like-with-like pairing, contributing \(|\tau|^2\); the all-equal terms contribute \(\kappa\).

For a factor-free frequency, oddness of \(N\) implies that \((2a,2b)\) is also factor-free. Put

\[
\gamma=\mathbb EX^2=\hat\mu_N(2a,2b).
\]

Then \(|\theta|,|\gamma|\le c_N\), and direct expansion yields

\[
\tau=\gamma-\theta^2,\qquad
\kappa=1-3|\theta|^4+2\operatorname{Re}(\overline{\theta}^{,2}\gamma).
\tag{21}
\]

Since \(c_N\to0\), (20)--(21) imply, uniformly in \(m\), that for all sufficiently large \(N\) (for example once \(c_N\le1/10\)),

\[
\frac{\mathbb E|\bar X_m-\theta|^4}
{\bigl(\mathbb E|\bar X_m-\theta|^2\bigr)^2}
\le3.
\tag{22}
\]

For clarity, an explicit upper bound before replacing it by \(3\) is

\[
\frac{1+2c_N^3}{m(1-c_N^2)^2}
+\frac{m-1}{m}\left(2+\frac{(c_N+c_N^2)^2}{(1-c_N^2)^2}\right).
\]

Apply Paley--Zygmund to \(W=|\bar X_m-\theta|^2\). For every \(0<\lambda<1\),

\[
\mathbb P\left(|\bar X_m-\theta|
\ge\sqrt{\lambda}\frac{\sigma}{\sqrt m}\right)
\ge\frac{(1-\lambda)^2}{3}.
\tag{23}
\]

Consequently, if one demands

\[
\mathbb P\bigl(|\bar X_m-\theta|\le\epsilon|\theta|\bigr)
>1-\frac{(1-\lambda)^2}{3},
\]

then necessarily

\[
m\ge\frac{\lambda\sigma^2}{\epsilon^2|\theta|^2}.
\tag{24}
\]

For the concrete choice \(\lambda=1/2\), confidence strictly above \(11/12\) forces

\[
m\ge\frac{1-|\theta|^2}{2\epsilon^2|\theta|^2}
\ge\frac{(1-c_N^2)\varphi(N)^2}{32\epsilon^2N}
=\Omega_\epsilon(N).
\tag{25}
\]

The confidence threshold is part of the theorem. Paley--Zygmund as used here does not justify asserting (25) at every lower confidence level, and (25) concerns this raw empirical mean only.

### Analogous statement for one regular rectangular bin

Fix one half-open axis-parallel rectangle \(R\), independent of \(N\), whose area \(v=\lambda(R)\) lies in \([\eta,1-\eta]\) for some fixed \(\eta>0\). Let

\[
\pi_N=\nu_N(R),\qquad
\Delta_N=\pi_N-v,\qquad
\hat\pi_m=\frac1m\sum_{j=1}^m\mathbf1_R(Z_j),
\]

where \(Z_j\) are iid cloud samples. Equation (15) gives

\[
|\Delta_N|\le K\frac{\log^2N}{\sqrt N}
\tag{26}
\]

for a fixed \(K\), and hence, for all large \(N\),

\[
\pi_N\in[\eta/2,1-\eta/2],\qquad
\sigma_R^2:=\pi_N(1-\pi_N)\ge
s_\eta:=\frac{\eta}{2}\left(1-\frac{\eta}{2}\right)>0.
\]

The raw bin-discrepancy estimator is \(\hat\Delta_m=\hat\pi_m-v\). Its exact MSE is

\[
\boxed{
\mathbb E(\hat\Delta_m-\Delta_N)^2
=\frac{\pi_N(1-\pi_N)}m.}
\tag{27}
\]

For a nonzero \(\Delta_N\), relative RMSE at most \(\epsilon\) requires

\[
m\ge\frac{\sigma_R^2}{\epsilon^2\Delta_N^2}
\ge\frac{s_\eta}{\epsilon^2K^2}\frac{N}{\log^4N}
=N^{1-o(1)}.
\tag{28}
\]

There is also a precisely scoped confidence analogue. For a centered Bernoulli variable,

\[
\kappa_R=\mathbb E|\mathbf1_R-\pi_N|^4
=\sigma_R^2(1-3\sigma_R^2),
\]

so the exact real fourth moment is

\[
\mathbb E(\hat\pi_m-\pi_N)^4
=\frac{\kappa_R+3(m-1)\sigma_R^4}{m^3}.
\tag{29}
\]

The fourth-to-second-moment ratio is at most

\[
R_\eta:=3+\frac1{s_\eta}.
\]

Paley--Zygmund with \(\lambda=1/2\) therefore shows that confidence strictly above \(1-1/(4R_\eta)\) for the event

\[
|\hat\Delta_m-\Delta_N|\le\epsilon|\Delta_N|
\]

forces

\[
m\ge\frac{\sigma_R^2}{2\epsilon^2\Delta_N^2}
=\Omega_{\eta,\epsilon}\left(\frac{N}{\log^4N}\right).
\tag{30}
\]

This bin statement is one-bin-at-a-time. It applies equally to each fixed cell of a fixed finite regular axis-parallel partition whose cell areas stay bounded away from \(0\) and \(1\). It is not a lower bound for arbitrary joint, nonlinear, adaptive, or nonrectangular statistics.

## 6. Explicit exclusions

Nothing above establishes any of the following:

1. a lower bound for factoring \(N\), or any computational hardness reduction;
2. a sample lower bound for arbitrary nonlinear processing, arbitrary estimators, or arbitrary hypothesis tests;
3. a conclusion about dense or adaptive searches for hidden \(p\)- or \(q\)-divisible frequencies (the ETK proof sums them analytically; it is not a search algorithm);
4. discrepancy or sample claims for curved, diagonal, or otherwise non-axis-parallel bins;
5. an approximate-common-divisor, hidden-number-problem, Coppersmith, or related lattice conclusion.

The proved content is exactly: CRT-local Fourier structure, linear finite-observable bounds after public gcd screening, axis-parallel discrepancy and fixed-bin consequences, and raw-mean sampling statements with their stated confidence thresholds.
