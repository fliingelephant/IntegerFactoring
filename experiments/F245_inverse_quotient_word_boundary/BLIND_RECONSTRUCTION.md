# F245 blind reconstruction

## Authentication and evidence boundary

Before reading it, I authenticated `STATEMENT.md` as

```text
c12d744be03815b942010c13637225a9d889f7724f1f5c95c4e5dc35d2a05a21
```

This equals the required SHA-256. I then read the repository-root
`PROMPT.md` and `AGENTS.md`, followed by that authenticated statement. I did
not inspect any proof, audit, provenance, manifest, or earlier F243/F244
artifact. No numerical experiment was used.

## 1. Inverse-quotient mass

Write \(\mathcal U_N\) for the canonical units in
\(\{1,\ldots,N-1\}\). For \(u\in\mathcal U_N\), its canonical inverse
\(v\) satisfies

\[
 uv=1+NK(u).
\]

Since \(1\le u,v\le N-1\),

\[
0\le K(u)\le N-2.
\]

Thus the statement's looser range \(0\le K(u)\le N-1\) is valid. For a
fixed value \(k\), every preimage \(u\) gives a factorization
\(1+kN=uv\). Once \(u\) is chosen, \(v\) is fixed. Hence

\[
\#\{u\in\mathcal U_N:K(u)=k\}\le \tau(1+kN)\le\Delta_N,
\]

because every arising product \(uv\) is less than \(N^2\). Uniformity on
the \(\varphi(N)\) canonical units gives

\[
\Pr(K(U)=k)\le \frac{\Delta_N}{\varphi(N)}.
\]

Replacing zero by one only merges the fibers \(K=0\) and \(K=1\).
Therefore every atom of \(\widehat K(U)\) has mass at most
\(2\Delta_N/\varphi(N)\).

The support contains fewer than \(N\) integers, and any residue class
modulo \(\ell\) meets it at most \(\lceil N/\ell\rceil\) times. It follows
that

\[
\Pr(\widehat K(U)\equiv r\pmod\ell)
\le \frac{2\lceil N/\ell\rceil\Delta_N}{\varphi(N)}
=\beta_{N,\ell}.
\]

For \(\ell<N\), \(\lceil N/\ell\rceil<2N/\ell\). Also, because \(p,q\)
are distinct odd primes, the two smallest possible primes are \(3,5\), so

\[
\frac N{\varphi(N)}=rac p{p-1}\frac q{q-1}
\le\frac32\frac54<2.
\]

Consequently \(\beta_{N,\ell}<8\Delta_N/\ell\), as claimed.

For independent \(K_i,K_j\), condition on \(K_j=t\). The event
\(\ell\mid\Gamma_{ij}\) requires \(K_i\ne t\) and
\(K_i\equiv t\pmod\ell\). Its conditional probability is at most the mass
of one residue class of \(K_i\), hence at most \(\beta_{N,\ell}\).
Similarly, \(\ell\mid\widehat K_i\) is its zero residue class. This proves
(2). The same argument remains valid after a prior transcript is fixed if
the next seed is exactly uniform on the same canonical unit set: condition
on the earlier quotient and apply the one-seed bound to the later seed.

## 2. Adaptive bank

Suppose there are \(t\le Q(n)\) seeds. Form the complete bank before any
selection. It has at most \(t\) positive quotient entries and
\(\binom t2\) positive unequal-value differences. Positive powers introduce
no new prime divisors. If \(\ell\) divides an adaptively selected product,
then it already divides at least one entry in this complete bank. The union
bound and (2) give

\[
\Pr(\ell\mid W_{\rm iq})
\le\left(t+\binom t2\right)\beta_{N,\ell}
\le\left(Q(n)+\binom{Q(n)}2\right)\beta_{N,\ell}.
\]

The selection rule need not be independent of the transcript. Adaptivity
does not alter the containment of the selected-divisibility event in the
union over the complete bank.

## 3. The reconstructible part of the marker estimate

The divisor estimate used in the statement can be derived without an
external theorem. Fix \(\varepsilon>0\). For all sufficiently large primes
\(r\),

\[
a+1\le 2^a\le r^{\varepsilon a}\qquad(a\ge0).
\]

For each of the finitely many smaller primes, the ratio
\((a+1)/r^{\varepsilon a}\) has a finite maximum over \(a\ge0\). Multiplying
those finitely many maxima gives a constant \(C_\varepsilon\) such that

\[
\tau(m)\le C_\varepsilon m^\varepsilon
\]

for every \(m\). Since \(m<N^2<2^{2n}\), this yields

\[
\log_2\Delta_N\le 2\varepsilon n+O_\varepsilon(1).
\]

As \(\varepsilon\) is arbitrary, \(\Delta_N=2^{o(n)}\).

Now assume, but do not certify, the statement's imported existence of four
distinct marker primes \(\ell>2^{cn}\). Applying (3) to each marker and
taking a union bound gives, for \(Q(n)\ge1\),

\[
\Pr\!\left(\gcd(W_{\rm iq},\ell_1\ell_2\ell_3\ell_4)>1\right)
<32Q(n)^2\Delta_N,2^{-cn}.
\]

For fixed numerical-quasipolynomial \(Q\),
\(\log_2 Q(n)=O((\log(n+1))^k)=o(n)\). Together with
\(\Delta_N=2^{o(n)}\), the displayed bound is \(2^{-\Omega(n)}\). Thus (4)
is a valid consequence of the imported marker existence and size
assertions.

The markers are within the range required by (1): a prime greater than two
that divides \(p+1\) cannot equal the even integer \(p+1\), and hence it is
less than \(p<N\); the other three shifted cases are no larger.

## 4. Hilbert--90 carry identities

Direct expansion gives the public identity

\[
A^2-DB^2=(a^2+Db^2)^2-D(2ab)^2=(a^2-Db^2)^2=g^2.
\]

Because \(gv\equiv1\pmod N\), the integer
\(\widetilde d=(gv-1)/N\) is exact. From
\(X=Av-Nq_A\),

\[
\begin{aligned}
gX-A
&=g(Av-Nq_A)-A\\
&=A(gv-1)-gNq_A\\
&=N(A\widetilde d-gq_A).
\end{aligned}
\]

This proves the first identity in (5); replacing \((A,X,q_A)\) by
\((B,Y,q_B)\) proves the second.

Moreover,

\[
X^2-DY^2\equiv v^2(A^2-DB^2)=v^2g^2\equiv1\pmod N,
\]

so the norm carry is an integer. The definitions of \(k,l\) give
\(gX=A+Nk\) and \(gY=B+Nl\). Therefore

\[
\begin{aligned}
g^2(X^2-DY^2)
&=(A+Nk)^2-D(B+Nl)^2\\
&=g^2+2N(Ak-DBl)+N^2(k^2-Dl^2).
\end{aligned}
\]

Subtracting \(g^2\), then dividing by \(Ng^2\), proves (6).

All quantities in (5)--(6) are determined by the public values and the one
inverse transcript containing \(v\) (equivalently \(\widetilde d\) together
with public nonzero \(g\)). The norm expression is nonlinear in the carry
data. Nothing in Sections 1--2 bounds the residue law of these transformed
values. Also, if \(g=u+sN\) with canonical residue \(u\), then

\[
\widetilde d=K(u)+sv,
\]

so \(\widetilde d\) itself need not have the fresh canonical-\(K\) law.
This confirms the statement's warning that (3) does not cover these
transforms.

## Imported interfaces that this statement does not certify

The following are essential external premises, not reconstructible from the
authenticated statement:

1. The definition and infinitude of the “unconditional F244 family.”
2. The existence, distinctness, shifted-factor placement, and uniform
   exponential lower bound for the four marker primes.
3. The assertion that every allowed signed-power word misses all four
   markers, including the exact meaning of “numerical-QP-bit.”
4. The F244 square-baseline incidence property needed to pass from marker
   avoidance by \(W_{\rm sp}W_{\rm iq}\) to one surviving marker on each
   hidden side.
5. The definition of a P208 orientation and the theorem that a surviving
   marker forces exponentially small success for every clean powered trial.
6. The definition and proof of shifted common-order capacity \(12\), and the
   implication that arbitrary exact-common-order accumulation cannot repair
   the failure.
7. The formal algorithmic grammar behind “inverse-QP Las Vegas progress.”
   Without it, the final nonprogress claim cannot be checked for its stated
   scope.

Equation (4) is conditionally reconstructed once items 1--2 are granted.
The subsequent combined-word, powered-trial, common-order, and overall
obstruction conclusions require items 3--7 and cannot be derived from the
statement alone.

## Verdict

**FAIL — not internally reconstructible.**

The exact mass law, residue and difference bounds, adaptive-bank bound,
subexponential divisor estimate, conditional derivation of (4), and
identities (5)--(6) all reconstruct from first principles. The claimed
infinite factoring obstruction does not. Its decisive F244/P208 interfaces
are neither defined nor proved in the statement. Therefore this document
cannot certify the global conclusion, although it finds no internal defect
in the self-contained local claims.
