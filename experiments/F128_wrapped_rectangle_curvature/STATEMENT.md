# F128 statement — wrapped multiplicative-rectangle curvature

This is a proof-only candidate. It concerns the P114 multiplicative rectangle.
It does not give an all-input factoring algorithm.

Let \(N\) be odd. Let \(u,a,b\) be units modulo \(N\), represented by
integers in \(\{1,\ldots,N-1\}\). Put

\[
d=b-a,
\qquad
e=ab-1.
\]

For \(i,j\in\{0,1\}\), define

\[
x_{ij}=[ua^ib^j]_N,
\qquad
y_{ij}=[x_{ij}^{-1}]_N,
\qquad
\kappa_{ij}=\frac{x_{ij}y_{ij}-1}{N},
\]

and

\[
\Omega_{\square}
=d(\kappa_{11}-\kappa_{00})
+e(\kappa_{10}-\kappa_{01}).
\]

The P114 local matrix has the four rows

\[
(1,x_{ij},y_{ij},\kappa_{ij}),
\qquad ij=00,10,01,11.
\]

Its unit conditions are

\[
\gcd\bigl(uab(a-1)(b-1)(b-a),N\bigr)=1.
\]

The named P114 eligibility-factor screens are the six separate gcds with

\[
u,\ a,\ b,\ a-1,\ b-1,\ b-a.
\]

A zero factor or zero residual gives the global gcd \(N\), not a proper hit.

## 1. Exact wrap-curvature decomposition

Put

\[
M=uab,
\qquad
z=[M^{-1}]_N,
\qquad
K=\frac{Mz-1}{N}.
\]

Define

\[
\begin{aligned}
A&=\left\lfloor\frac{ua}{N}\right\rfloor,&
B&=\left\lfloor\frac{ub}{N}\right\rfloor,&
C&=\left\lfloor\frac{uab}{N}\right\rfloor,\\
R_0&=\left\lfloor\frac{zab}{N}\right\rfloor,&
R_a&=\left\lfloor\frac{zb}{N}\right\rfloor,&
R_b&=\left\lfloor\frac{za}{N}\right\rfloor.
\end{aligned}
\]

Then

\[
\boxed{
\Omega_{\square}
=Ne(AR_a-BR_b)+u\Phi_y+z\Phi_x,
}
\]

where

\[
\Phi_x=e(aB-bA)-dC,
\qquad
\Phi_y=dR_0+e(bR_b-aR_a).
\]

Consequently,

\[
\boxed{
\gcd(\Omega_{\square},N)
=\gcd(u\Phi_y+z\Phi_x,N).
}
\]

Under the P114 unit conditions, reduction raises the local rectangle rank
from three to four modulo a prime \(\ell\) dividing \(N\) exactly when

\[
u\Phi_y+z\Phi_x\not\equiv0\pmod\ell.
\]

## 2. Exact density bound when \(a,b\) are fixed

Let \(N=pq\), where \(p<q\) are distinct odd primes. Hold \(a,b\) fixed
while \(u\) is uniform in \((\mathbb Z/N\mathbb Z)^\times\). Assume the P114
unit conditions and

\[
p>(ab)^2\bigl(ab+\max\{a,b\}\bigr).
\]

Then

\[
\Pr_u\!\left(1<\gcd(\Omega_{\square},N)<N\right)
\le
\frac{2a^4b^4(p+q)}{(p-1)(q-1)}
=O\!\left(\frac{a^4b^4}{p}\right).
\]

The bound includes both events: vanishing modulo \(p\) only and vanishing
modulo \(q\) only. Thus quasipolynomially many uniform \(u\)-samples do not
give an inverse-quasipolynomial hit law when \(a,b\) have quasipolynomial
magnitude and \(p\asymp\sqrt N\).

This is only a uniform-source bound. It gives no bound for an adaptive
selector that chooses \(u\) after it observes carries, quotient patterns,
blocks, or earlier relations.

## 3. Signed-small full-channel obstruction

Let

\[
u\equiv\epsilon_0s,
\qquad
a\equiv\epsilon_a a_0,
\qquad
b\equiv\epsilon_b b_0
\pmod N,
\]

where every \(\epsilon\) is in \(\{-1,+1\}\) and \(s,a_0,b_0\) are positive.
Assume

\[
L=sa_0b_0<N.
\]

The four signed corner magnitudes are

\[
r_{00}=s,
\quad r_{10}=sa_0,
\quad r_{01}=sb_0,
\quad r_{11}=sa_0b_0=L.
\]

For \(r\mid L\), put

\[
\bar r=[r^{-1}]_N,
\qquad
h_r=\frac{r\bar r-1}{N}.
\]

Let

\[
\tilde d=\epsilon_b b_0-\epsilon_a a_0,
\qquad
\tilde e=\epsilon_a\epsilon_ba_0b_0-1,
\]

and use weights

\[
(\lambda_{00},\lambda_{10},\lambda_{01},\lambda_{11})
=(-\tilde d,\tilde e,-\tilde e,\tilde d).
\]

If

\[
\eta_{ij}=\epsilon_0\epsilon_a^i\epsilon_b^j,
\]

define

\[
B_{\rm sign}
=\sum_{i,j}\lambda_{ij}
\left(
Lh_{r_{ij}}
-\mathbf 1_{\eta_{ij}=-1}
\left(Lr_{ij}+\frac{L}{r_{ij}}\right)
\right).
\]

When \(L\) is a unit modulo \(N\),

\[
\boxed{
\gcd(\Omega_{\square},N)=\gcd(B_{\rm sign},N),
}
\]

and

\[
\boxed{
|B_{\rm sign}|
<6L^2(a_0+b_0+a_0b_0+1).
}
\]

Let

\[
T=6L^2(a_0+b_0+a_0b_0+1).
\]

If \(N=pq\) and both prime factors exceed \(T\), then the P114 prefactor gcds,
all eight endpoint sign gcds

\[
\gcd(x_{ij}-y_{ij},N),
\qquad
\gcd(x_{ij}+y_{ij},N),
\]

and \(\gcd(\Omega_{\square},N)\) give no proper factor. A zero scalar or
endpoint difference can give the global gcd \(N\), which is not success.

This claim concerns one rectangle and these named channels. It does not
cover the multi-relation P66 decoder.

## 4. A fully wrapped infinite trap

Fix \(s,a,b>1\) with \(a\ne b\), and put \(L=sab\). Let \(N=pq\) satisfy

\[
N\equiv-1\pmod L,
\]

where \(p,q\) are distinct primes larger than

\[
L^2+a+b+1.
\]

Use the public rectangle

\[
u=N-s,
\qquad
\alpha=a,
\qquad
\beta=b.
\]

It is eligible for P114, all three nontrivial products wrap, and

\[
\boxed{\Omega_{\square}=0.}
\]

Thus both local ranks stay three. All named endpoint and prefactor screens
are also null or global.

There are infinitely many balanced semiprimes in this class. For example,
choose comparable primes \(p\equiv1\pmod L\) and
\(q\equiv-1\pmod L\).

For the boundary case \(s=1\), let \(N=pq\) have distinct prime factors
larger than

\[
(ab)^2+a+b+1,
\]

and assume \(a,b>1\), \(a\ne b\), and
\(N\equiv-1\pmod{ab}\). The same public rectangle gives

\[
\boxed{
\Omega_{\square}=(b-a)(1-N).
}
\]

Its gcd with \(N\) is one. All endpoint and prefactor screens are null,
except that \(x_{00}=y_{00}=N-1\) gives one global endpoint gcd.
