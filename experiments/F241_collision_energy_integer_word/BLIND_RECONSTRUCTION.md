# Blind reconstruction of F241

## Verdict

**PASS, with the stated conditional scope.**  All quantitative identities and
the capture-bank conclusion reconstruct from first principles.  The result is
not an all-input factoring theorem.  Its random-divisor bank assumes the
complete factorization of \(N-1\) and the subgroup-image hypothesis `(S)`.
The generic law in Section 2 is a probability identity; an arbitrary exactly
samplable law needs separate sample-size and bit-cost bounds before it gives a
quasipolynomial-time algorithm.  The radix conclusion applies to a common
fixed multiplier \(u\); it must not be read as a claim about independently
varying multipliers.

I authenticated `STATEMENT.md` before reading it:

```text
11cbe1a262a546ad05c3462f8189f3704a98e73b1725d334a487ad36f0d5c48b
```

I used only the root `PROMPT.md` and that authenticated statement.  I did not
read the proof, prior audits, provenance, manifest, history, messages, or any
other F241 file.

## 1. The exponent interface behind P205

For a positive public exponent \(E\), define its residual at a prime factor
\(v\in\{p,q\}\) by

\[
\rho_v(E)=\frac{v-1}{\gcd(v-1,E)}.
\]

If a previous exponent \(E_0\) has residual \(s=\rho_v(E_0)\), then appending
a multiplicative word \(V\) gives

\[
\rho_v(E_0V)=\frac{s}{\gcd(s,V)}. \tag{1}
\]

This is valuation-wise.  If \(a=v_\ell(v-1)\), \(b=v_\ell(E_0)\), and
\(c=v_\ell(V)\), the two sides have \(\ell\)-adic valuation

\[
\max(a-b-c,0)
=\max(\max(a-b,0)-c,0).
\]

The P205 probability bound also follows directly.  For a fresh uniform unit
\(x\bmod N\), the CRT components are independent and uniform.  In the cyclic
group \(\mathbb F_v^\times\), exactly \(\gcd(E,v-1)\) elements satisfy
\(x^E=1\).  Hence, with

\[
\alpha=\frac1{\rho_p(E)},\qquad
\beta=\frac1{\rho_q(E)},
\]

the elementary gcd \(\gcd(x^E-1,N)\) is nontrivial with probability

\[
D=\alpha(1-\beta)+\beta(1-\alpha). \tag{2}
\]

Assume without loss that \(\alpha\ge\beta\).  Since \(\alpha\) is the
reciprocal of an integer, either \(\alpha\le1/2\) or \(\alpha=1\).  In the
first case,

\[
D\ge \alpha(1-\beta)\ge\alpha/2.
\]

If \(\alpha=1\) and \(\beta\le1/2\), then
\(D=1-\beta\ge1/2\).  The only remaining case is
\(\alpha=\beta=1\), so \(E\) is a multiple of both \(p-1\) and \(q-1\).
Write \(E=2^t u\), with \(u\) odd, and use the standard repeated-squaring
factor extraction on \(x^u\).

For completeness, put \(c_v=v_2(v-1)\).  Because \(v-1\mid E\), exponentiation
by \(u\) kills the odd-order component of \(\mathbb F_v^\times\) and is an
automorphism on its Sylow-2 subgroup.  Thus \(x^u\) is uniform on a cyclic
group of order \(2^{c_v}\).  If \(L_v\) is the base-two logarithm of its order,

\[
\Pr(L_v=0)=2^{-c_v},\qquad
\Pr(L_v=j)=2^{j-1-c_v}\quad(1\le j\le c_v).
\]

The two levels are independent.  If they differ, repeated squaring reaches a
stage where one CRT component is \(-1\) and the other is \(+1\), and a gcd
extracts a factor.  With \(c=\min(c_p,c_q)\), the probability that they agree is

\[
2^{-c_p-c_q}\left(1+\sum_{j=1}^{c}2^{2j-2}\right)
=2^{-c_p-c_q}\frac{4^c+2}{3}\le\frac12.
\]

Consequently a complete exponent trial, using the elementary gcd and the
repeated-squaring fallback, has factor probability

\[
\Pr(\text{factor}\mid E)
\ge \frac12\max\left\{\frac1{\rho_p(E)},
                           \frac1{\rho_q(E)}\right\}. \tag{3}
\]

This proof uses a unit that is fresh after \(E\) is fixed.  It therefore also
holds conditional on any public adaptive history.  Sampling a uniform unit is
Las Vegas: sample a uniform residue and take a gcd; a nontrivial gcd is already
a factor, while rejection continues until a unit is obtained.

## 2. Exact residual after \((N-1)^n\)

Let \(A=N-1\).  The identity

\[
A=pq-1=(p-1)(q-1)+(p-1)+(q-1)
=d\bigl(ds_ps_q+s_p+s_q\bigr)
\]

shows that \(d\mid A\).  Consider any prime \(\ell\mid p-1\).  If
\(\ell\mid A\), then

\[
v_\ell(p-1)<n,
\]

because \(\ell^{v_\ell(p-1)}\le p-1<N<2^n\).  Hence

\[
v_\ell(A^n)=n v_\ell(A)\ge n>v_\ell(p-1),
\]

so the full \(\ell\)-primary part of \(p-1\) is removed.  If
\(\ell\nmid A\), then \(\ell\nmid d\), and its primary part in \(p-1=ds_p\)
is exactly its primary part in \(s_p\); none of it is removed by \(A^n\).
Therefore

\[
\rho_p(A^n)=s_p^\perp.
\]

The same proof gives \(\rho_q(A^n)=s_q^\perp\).  Also

\[
\log_2(A^n)=n\log_2 A=O(n^2),
\]

so the word has the claimed bit length.  By (3), if either residual is at most
a numerical quasipolynomial, independent repetition has numerical-QP expected
trial count.  Each trial uses arithmetic on an \(O(n^2)\)-bit exponent, and
verification is a gcd, so the full expected bit cost is numerical QP.

## 3. Collision energy

Let the current residual be

\[
s=\prod_{\ell\in\mathcal P}\ell^{e_\ell}<N.
\]

For every \(\ell\in\mathcal P\), the inequality
\(\ell^{e_\ell}\le s<N<2^n\) implies \(e_\ell<n\).  Hence
\(\Delta^n\) contains the whole primary \(\ell^{e_\ell}\) exactly when
\(\ell\mid\Delta\).  With

\[
I_\ell=\mathbf 1_{\{\ell\mid\Delta\}},
\]

we get

\[
\gcd(s,\Delta^n)
=\prod_{\ell\in\mathcal P}
 \left(1+(\ell^{e_\ell}-1)I_\ell\right). \tag{4}
\]

Expanding (4), and writing \(m_S=\prod_{\ell\in S}\ell\), gives

\[
\mathbb E\frac{\gcd(s,\Delta^n)}s
=\frac1s\left[
1+\sum_{\varnothing\ne S\subseteq\mathcal P}
\left(\prod_{\ell\in S}(\ell^{e_\ell}-1)\right)
\Pr(m_S\mid\Delta)
\right]. \tag{5}
\]

For nonempty \(S\), the special definition \(\Delta=1\) on \(Z=Z'\)
implies

\[
\Pr(m_S\mid\Delta)
=\Pr(Z\ne Z'\text{ and }Z\equiv Z'\pmod {m_S})
=\kappa_{m_S}.
\]

Substitution in (5) is exactly `(CE)`.  By (1),

\[
\frac{1}{r}=\frac{\gcd(s,\Delta^n)}s,
\]

so the left side is exactly \(\mathbb E[1/r]\).  Applying (3) after the word
is sampled and averaging gives

\[
\begin{aligned}
\Pr(\text{factor})
&\ge \frac12\mathbb E\max\{1/r_p,1/r_q\}\\
&\ge \frac12\max\{\mathbb E(1/r_p),\mathbb E(1/r_q)\},
\end{aligned}
\]

which is `(P205-CE)`.  Conditioning on public history changes none of the
steps if \(Z,Z'\), and the later unit are conditionally fresh.  Exact
samplability alone proves this probability statement, not a runtime bound for
an unbounded integer law.

## 4. Uniform-divisor Fourier law

Assume the granted factorization

\[
A=\prod_{j=1}^k b_j^{a_j},\qquad
T=\prod_{j=1}^k(a_j+1),
\]

and let \(Z=\prod_jb_j^{J_j}\), where the \(J_j\) are independent and
uniform on \(\{0,\ldots,a_j\}\).  The exponent vectors parameterize the
divisors bijectively, so \(Z\) is exactly uniform on a set of \(T\) distinct
integers.

For squarefree \(m\) coprime to \(A\), let \(G=(\mathbb Z/m\mathbb Z)^\times\)
and let \(\mu(g)=\Pr(Z\equiv g\pmod m)\).  Total modular collision is

\[
C_m=\sum_{g\in G}\mu(g)^2.
\]

Finite-group Parseval gives

\[
C_m=\frac1{|G|}\sum_{\chi\in\widehat G}
\left|\mathbb E\chi(Z)\right|^2. \tag{6}
\]

Independence of the exponents factorizes the Fourier coefficient:

\[
\mathbb E\chi(Z)
=\prod_{j=1}^k
\left(\frac1{a_j+1}\sum_{e=0}^{a_j}\chi(b_j)^e\right). \tag{7}
\]

Since \(|G|=\varphi(m)\), (6)-(7) give the first term in `(D)`.  Exact
integer equality has probability \(1/T\), and is contained in total modular
collision.  Removing it gives

\[
\kappa_m=C_m-\frac1T,
\]

which proves `(D)` including its essential subtraction.

All residues of sampled divisors lie in \(H_m=\langle b_1,\ldots,b_k\rangle\).
Thus Cauchy--Schwarz yields

\[
1=\left(\sum_{g\in H_m}\mu(g)\right)^2
\le h_m\sum_{g\in H_m}\mu(g)^2=h_m C_m.
\]

Therefore \(C_m\ge1/h_m\) and

\[
\kappa_m\ge\frac1{h_m}-\frac1T,
\]

which is `(H)`.

## 5. Capture bank

Fix one side \(i\in\{p,q\}\), and assume `(S)` for every prime
\(\ell\mid s_i^\perp\).  For one independent divisor pair,

\[
\Pr(\ell\mid\Delta)=\kappa_\ell
\ge\frac1{h_\ell}-\frac1T
\ge\frac1Q-\frac1{2Q}=\frac1{2Q}. \tag{8}
\]

Across \(R\) independent pairs, the probability that a fixed \(\ell\) is
never hit is at most

\[
\left(1-\frac1{2Q}\right)^R
\le \exp\left(-\frac{R}{2Q}\right)
\le\frac1{2n}. \tag{9}
\]

There are fewer than \(n\) distinct primes in \(s_i^\perp<N<2^n\).
A union bound in (9) therefore shows that, with probability at least
\(1/2\), every such prime is hit.  No independence between different primes
is used.

When \(\ell\) is hit, the factor \(\Delta_t^n\) supplies its entire primary
part in \(s_i^\perp\), by the same saturation argument used in (4).
The baseline \(A^n\) supplies the complementary primary parts of \(s_i\) and
also the common factor \(d\).  Consequently

\[
\Pr(s_i\mid W)\ge\frac12,
\qquad
s_i\mid W\Longrightarrow i-1\mid W.
\]

For every captured word, (3) gives conditional factor probability at least
\(1/2\).  Freshness of the unit permits multiplication of the bounds, so the
bank success probability is at least \(1/4\).

Every sampled divisor is at most \(A<2^n\), hence every \(\Delta_t<2^n\).
Thus each \(\Delta_t^n\), and also \(A^n\), has \(O(n^2)\) bits, while their
product has

\[
O((R+1)n^2)
\]

bits.  Exact uniform sampling of each bounded exponent \(J_j\) uses rejection
from a binary interval with constant expected repetitions.  There are at most
\(n\) prime-power factors of \(A\).  Since \(Q\) and hence
\(R=O(Q\log n)\) are numerical QP, sampling, word construction, modular
exponentiation, gcd verification, and independent bank repetition all have
expected numerical-QP bit cost, conditional on the granted factorization of
\(A\).

## 6. The one-base obstruction

Let \(A=b^a\), \(T=a+1\), and \(h=\operatorname{ord}_m(b)\).  The residues
of \(b^0,\ldots,b^{T-1}\) agree exactly when their exponents agree modulo
\(h\).  If

\[
T=qh+r,\qquad0\le r<h,
\]

then \(r\) residue classes contain \(q+1\) exponents and \(h-r\) contain
\(q\).  The total ordered-pair modular-collision probability is

\[
\frac{r(q+1)^2+(h-r)q^2}{T^2}
=\frac{hq^2+2rq+r}{T^2}.
\]

Subtracting the \(T\) diagonal ordered pairs, whose probability is \(1/T\),
gives

\[
\kappa_m
=\frac{hq^2+2rq+r-(qh+r)}{T^2}
=\frac{hq(q-1)+2rq}{T^2},
\]

which is `(P)`.  If \(h\ge T\), then either \(q=0,r=T\) or
\(q=1,r=0\), so \(\kappa_m=0\).  Equivalently, a nonzero difference of two
sampled exponents has absolute value below \(h\), and therefore cannot be a
multiple of the order.  This proves injectivity and shows why support size by
itself does not force useful distinct-integer collisions.

## 7. Quotient-radix scope

For a divisor \(B\mid A\), put \(H=A/B\).  If a common public integer \(u\)
satisfies \(1\le u<B\), then

\[
uN=u(A+1)=(uH)B+u
\]

is already Euclidean division by radix \(B\).  Complementation
\(B\mapsto A/B\) is an involution of the divisor set, so a law on \(B\)
induces only its known pushforward law on \(H\).  At \(u=1\), every
\(B>1\) has quotient \(H\) and remainder one.  The atom \(B=1\) instead has
remainder zero and must be separated, exactly as stated.

If \(m\) is coprime to \(uA\), then \(u\) is invertible modulo \(m\), and
for two sampled divisors

\[
uH_1\equiv uH_2\pmod m
\quad\Longleftrightarrow\quad
H_1\equiv H_2\pmod m.
\]

Thus a fixed-\(u\) quotient carry creates no new collision entropy.  This
equivalence need not hold if a different multiplier \(u\) is sampled with
each radix; that case is outside the displayed construction.

Any other public construction, including products of public prime bases,
still defines a positive-integer law and therefore obeys `(CE)`.  For a hard
residual \(s\), the exact useful condition supplied by this interface is

\[
1+
\sum_{\varnothing\ne S\subseteq\mathcal P}
\left(\prod_{\ell\in S}(\ell^{e_\ell}-1)\right)
\kappa_{\prod_{\ell\in S}\ell}
\ge \frac{s}{\operatorname{QP}(n)}.
\]

Without such inverse-QP distinct-integer modular aliasing, with enough weight
from the residual prime powers, `(CE)` supplies no all-input inverse-QP P205
success bound.  The subgroup-image hypothesis is one sufficient route to this
condition; F241 does not prove it for all inputs.
