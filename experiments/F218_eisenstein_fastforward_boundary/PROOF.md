# Proof of F218

## 1. Local reduction of the moving exponent

Let `ell^e || K`.  The Carmichael exponent of the odd prime power is

\[
\lambda(\ell^e)=\varphi(\ell^e)=\ell^{e-1}(\ell-1).
\]

It divides `lambda(K)`, hence it divides `Lambda`.  Also

\[
\ell^{e-1}(\ell-1)\ge e
\]

for every odd prime `ell` and `e>=1`, so `Lambda+1>=e`.

Write a divisor of `m` as `d=ell^a c` with `ell` not dividing `c`.  If
`a>=1`, then

\[
d^{\Lambda+1}\equiv0\pmod{\ell^e}.
\]

If `a=0`, Carmichael's theorem gives

\[
d^{\Lambda+1}=c^{\Lambda+1}\equiv c\pmod{\ell^e}.
\]

Summing over all divisors leaves exactly the divisors of the `ell`-free
part of `m`:

\[
\sigma_{\Lambda+1}(m)
\equiv\sum_{c\mid m_{(\ell)}}c
=\sigma_1(m_{(\ell)})\pmod{\ell^e}.
\]

This proves (A1).

The positive coefficient of `E_2` is `-24 sigma_1(m)`.  Therefore

\[
[q^m]\frac{\ell E_2(\ell\tau)-E_2(\tau)}{24}
=\sigma_1(m)-\ell\mathbf1_{\ell\mid m}\sigma_1(m/\ell).
\]

If `m=ell^v u`, the right side is

\[
(1+\ell+\cdots+\ell^v)\sigma_1(u)
-\ell(1+\ell+\cdots+\ell^{v-1})\sigma_1(u)
=\sigma_1(u).
\]

This proves (A2).  The standard quasimodular anomalies in
`ell E_2(ell tau)-E_2(tau)` cancel on `Gamma_0(ell)`, giving the stated
weight-two modular form.  Only positive coefficients are reduced, so the
rational constant `(ell-1)/24` causes no modular-reduction issue.

Finally `(N,K)=1`, so every `ell`-free part of `N` is `N`.  CRT over all
`ell^e || K` proves (A3).

## 2. The eta quotient through every index

For prime `r` and `1<=j<=r-1`,

\[
\frac{(-1)^j}{r}\binom rj
=\frac{(-1)^j}{j}\binom{r-1}{j-1}
\equiv-\frac1j\pmod r.
\]

Thus

\[
\frac{(1-x)^r}{1-x^r}
\equiv1-r\sum_{j=1}^{r-1}\sum_{h\ge0}j^{-1}x^{j+hr}
\pmod{r^2}.
\]

Substitute `x=q^a` and multiply over `a>=1`.  Products of two
nonconstant corrections vanish modulo `r^2`, so

\[
F_r(q)
\equiv1-r\sum_{a\ge1}\sum_{j=1}^{r-1}\sum_{h\ge0}
j^{-1}q^{a(j+hr)}\pmod{r^2}.
\tag{1}
\]

Fix `m=r^v u`, `(u,r)=1`.  A contribution to `q^m` in (1) is a
factorization `m=ab` with `r` not dividing `b`.  Hence

\[
a=r^v c,\qquad b=u/c,qquad c\mid u.
\]

The corresponding inverse is

\[
b^{-1}\equiv c u^{-1}\pmod r.
\]

Summing over `c|u` proves

\[
-[q^m]F_r/r\equiv u^{-1}\sigma_1(u)\pmod r.
\]

At `m=N=2r+1`, one has `v=0` and `N^(-1)=1 mod r`, proving (B2).

## 3. Big-Witt dependency invariant

At a fixed ghost coordinate, big-Witt ring addition and multiplication do
not change the coordinate index.  A Frobenius gate changes an inward
dependency index from `m` to `dm`; a nonzero Verschiebung gate changes it
from `m` to `m/d`, with `d|m`.

Every allowed `d` has only prime factors dividing `K`.  Multiplication or
exact division by such a `d` changes only the valuations at those primes.
It leaves

\[
\rho_K(m)=m/\prod_{\ell\mid K}\ell^{v_\ell(m)}
\]

unchanged.  Induction over the circuit proves (C1), including circuits
with fan-out and arbitrary ring gates.

Because `N=2K+1`, `(N,K)=1`; hence `rho_K(N)=N`.  If a dependency path
from a seed `s` reached the target coordinate `N`, (C1) would force
`rho_K(s)=N`, and therefore `s>=N`.  No seed below `N` can do so.  This is
an index-support statement only; it does not cover operations that mix
ghost indices additively.

## 4. Frobenius compression of the theta power

In characteristic `r`,

\[
\vartheta(q)^r=\vartheta(q^r).
\]

Since `4k=2r+2`,

\[
\vartheta(q)^{4k}
\equiv\vartheta(q^r)^2\vartheta(q)^2\pmod r.
\]

Let `R_2(m)=[q^m]theta(q)^2`, with `R_2(0)=1`, `R_2(1)=4`, and
`R_2(2)=4`.  Since `N=2r+1`, coefficient convolution permits only the
three exponents `0,r,2r` from the first factor.  Therefore

\[
[q^N]\vartheta^{4k}
\equiv R_2(N)+4R_2(r+1)+4R_2(1)
\pmod r,
\]

which is (D2).

For completeness, the Eisenstein subspace of weight `2k` and trivial
character on `Gamma_0(4)` is spanned by the three degeneracy forms
`E_(2k)(tau), E_(2k)(2tau), E_(2k)(4tau)`.  Put `w=2k` and
`x=2^(-w)`.  Directly applying the `E_w` and theta transformations at the
three cusps gives this constant-term table, in the order of those three
degeneracy forms:

\[
\begin{array}{c|ccc|c}
\text{cusp}&E_w(\tau)&E_w(2\tau)&E_w(4\tau)&\vartheta^{4k}\\ \hline
\infty&1&1&1&1\\
0&1&x&x^2&(-1)^k x\\
1/2&1&1&x&0.
\end{array}
\]

Indeed, the cusp-zero row follows from
`E_w(-1/tau)=tau^w E_w(tau)` and
`theta(-1/tau)=(-i tau/2)^(1/2) theta(tau/4)` in the present
`q=exp(2 pi i tau)` convention.  At the cusp `1/2`, the alternating theta
sum has zero constant term; the oldform constants are the displayed
gcd-scaled values.

If `a,b,c` are the three Eisenstein coordinates, matching constants gives

\[
a+b+c=1,\qquad
a+bx+cx^2=(-1)^k x,\qquad
a+b+cx=0.
\]

The first and third equations give `c=1/(1-x)`.  Substitution into the
second gives

\[
 a=\frac{(-1)^k x}{1-x}
 =\frac{(-1)^k}{2^{2k}-1}.
\]

odd indices.  Since
Only `E_(2k)(tau)` has nonzero coefficients at odd indices.  Since
odd indices.  Since

\[
E_{2k}=1-\frac{4k}{B_{2k}}\sum_{m\ge1}\sigma_{2k-1}(m)q^m,
\]

the odd-index Eisenstein coefficient is

\[
(-1)^{k+1}\frac{4k}{(2^{2k}-1)B_{2k}}
\sigma_{2k-1}(m),
\]

proving (D3).

Now `2k=r+1`.  Kummer congruence gives

\[
\frac{B_{r+1}}{r+1}\equiv\frac{B_2}{2}=\frac1{12}\pmod r,
\]

so `B_(r+1)=1/12 mod r`.  Fermat gives

\[
2^{r+1}-1\equiv3\pmod r,
\qquad 4k=2(r+1)\equiv2\pmod r.
\]

The scalar in (D3) is consequently

\[
(-1)^{k+1}\frac{2}{3/12}
=(-1)^{k+1}8\pmod r.
\]

Every divisor of `N` is an `r`-adic unit, so

\[
\sigma_r(N)\equiv\sigma_1(N)\pmod r.
\]

This proves (D4).

## 5. Exact branch counterexample

Take

\[
r=17,\qquad N=35=5\cdot7,\qquad k=9.
\]

This is a balanced distinct semiprime and `K=(N-1)/2=17` is prime.  For
the smaller primes, `r=5,11` give prime `N`, and `r=13` gives `N=27`, which
is not a distinct semiprime.  At the sole smaller branch input
`r=7, N=15`, one has `R_2(15)=0`, `R_2(8)=4`, and hence the full theta
coefficient is `32=4 mod 7`.  Also `k=4` and
`-8 sigma_1(15)=-192=4 mod 7`.  Its cusp difference is zero.  Therefore
`r=17` is the smallest nonzero witness.
Because `35=3 mod 4`, `R_2(35)=0`.  The two-square divisor formula gives

\[
R_2(18)=4\sum_{d\mid18}\chi_4(d)
=4(1-1+1)=4,
\qquad R_2(1)=4.
\]

Thus (D2) is

\[
0+4\cdot4+16=32\equiv15\pmod{17}.
\]

On the other hand,

\[
\sigma_1(35)=1+5+7+35=48\equiv14\pmod{17},
\]

and `k=9` makes the sign in (D4) positive.  Hence the Eisenstein
coefficient is

\[
8\cdot14=112\equiv10\pmod{17}.
\]

Their difference is `5 mod 17`, proving the nonzero cusp contaminant and
the claimed counterexample.

## 6. Nonperiodicity of the affine Cartier section

Fix a prime `r`.  Suppose for contradiction that `b_r(j)` is eventually
periodic, with positive period `T` after some threshold.

Dirichlet's theorem supplies a prime

\[
\ell\equiv1\pmod{rT}.
\]

For every positive integer `a`, put

\[
j_a=\frac{\ell^a-1}{r}.
\]

These are integers, they tend to infinity, and

\[
j_{a+1}-j_a
=\frac{\ell^a(\ell-1)}r
\equiv0\pmod T.
\]

Choose `a` large enough that both indices lie beyond the eventual-period
threshold.  Since

\[
rj_a+1=\ell^a
\]

and `ell=1 mod r`, one has

\[
b_r(j_a)
=\sigma_1(\ell^a)
=1+\ell+\cdots+\ell^a
\equiv a+1\pmod r.
\]

Likewise `b_r(j_(a+1))=a+2 mod r`.  The indices are congruent modulo the
alleged period, but the values differ by one.  This contradiction proves
(E1).

Every constant-coefficient affine recurrence over the finite field
`F_r` evolves a finite state vector, after adjoining a constant coordinate
if necessary.  Its output is eventually periodic.  Thus (E1) excludes all
such recurrences.  A power series over a finite field is rational exactly
when its coefficient sequence is eventually linearly recurrent, hence
eventually periodic; the generating series is not rational.

For every positive integer `s`, the same prime powers satisfy

\[
\sigma_s(\ell^a)
=1+\ell^s+\cdots+\ell^{as}
\equiv a+1\pmod r,
\]

so the proof is unchanged.

## 7. Scope

The proof never evaluates `sigma_1(N)` without the hidden factorization.
The local reductions show that several moving-weight and moving-level
packagings contain the same target.  The Witt theorem is restricted to
standard `K`-supported ghost operations.  The theta witness refutes only
the claim that the Frobenius-simple full theta coefficient equals its
factor-sensitive Eisenstein projection.  The Cartier theorem excludes
fixed linear recurrences but not nonlinear or growing state.  No general
coefficient lower bound follows.
