# F260-D03 V3 algebra — exact public integer-source scores

## Scope

Let `N=pq`, where `p` and `q` are distinct odd primes. Hidden factors are
labels for exact finite scoring only. Every candidate integer and every
candidate operation is a function of public `N`.

D03 keeps the authenticated D02 score algebra unchanged. It ranks factored
annihilators at two operational certified states:

```text
M=1  no accumulated common-primary certificate;
M=2  the universal public certificate for odd p and q.
```

The hidden state `M=gcd(p-1,q-1)` is diagnostic. It cannot enter selection.

## Completely factored annihilators

Let

\[
A=\prod_\ell \ell^{e_\ell}
\]

be public and completely factored. For a uniform unit `a mod N`, put

\[
\alpha_p={\gcd(A,p-1)\over p-1},\qquad
\alpha_q={\gcd(A,q-1)\over q-1}.
\]

The direct identity gcd is proper with probability

\[
D=\alpha_p+\alpha_q-2\alpha_p\alpha_q.                 \tag{1}
\]

On simultaneous return, fix `ell^e || A` and put

\[
f_i=\min(e,v_\ell(i-1)),\qquad i\in\{p,q\}.
\]

If `T_i` is the `ell`-adic exponent of the returned local order, then

\[
P_{\ell,i}(0)=\ell^{-f_i},
\]

and, for `1<=t<=f_i`,

\[
P_{\ell,i}(t)=(\ell-1)\ell^{t-1-f_i}.                 \tag{2}
\]

For a certified state `M`, define

\[
E_\ell=\sum_t P_{\ell,p}(t)P_{\ell,q}(t),
\]

\[
S_\ell(M)=\sum_{t\le v_\ell(M)}
P_{\ell,p}(t)P_{\ell,q}(t),
\]

and

\[
G_\ell(M)=\sum_t P_{\ell,p}(t)P_{\ell,q}(t)
\max(t-v_\ell(M),0)\log_2\ell.
\]

Different rational primaries are independent. The exact stripping-factor
probability is

\[
F=D+\alpha_p\alpha_q\left(1-\prod_\ell E_\ell\right). \tag{3}
\]

The exact nonfactor strict-growth probability is

\[
Q(M)=\alpha_p\alpha_q
\left(\prod_\ell E_\ell-\prod_\ell S_\ell(M)\right).  \tag{4}
\]

Thus exact factor-or-growth probability is `F+Q(M)`. Expected certified
log-lcm gain is

\[
\mathbb E[\log_2(M'/M)]
=\alpha_p\alpha_q\left(\prod_\ell E_\ell\right)
\sum_\ell {G_\ell(M)\over E_\ell}.                    \tag{5}
\]

Every `E_ell` is positive. Formula (5) is linear in the prime support of `A`.
V3 forbids the D01 quadratic product-over-all-other-primaries loop.

## Exact dyadic terminal distribution

For public precision

\[
t\in\{\lfloor n/8\rfloor,\lfloor n/6\rfloor,
       \lfloor n/5\rfloor\},
\]

put

\[
J=\left\lceil{N^{1/4}\over n^4}\right\rceil,
\qquad L=\operatorname{lcm}(2^t,M).
\]

Define

\[
\Phi(L)=\max(0,\lceil\log_2(J/L)\rceil).               \tag{6}
\]

On a nonfactor equality outcome `T_p=T_q=u_ell` for every primary, put

\[
L'=\operatorname{lcm}\left(L,\prod_\ell\ell^{u_\ell}\right),
\qquad
\Delta\Phi=\Phi(L)-\Phi(L').                           \tag{7}
\]

V3 computes the exact analytic distribution

\[
\Pr(\text{nonfactor and }\Delta\Phi=k)
\]

by dynamic programming on `min(L',J)`. States at or above `J` merge. All
comparisons use integer arithmetic. The dyadic channel score is

\[
F+{\mathbb E[\Delta\Phi]\over\max(1,\Phi(L))}.         \tag{8}
\]

Factored-program row score is the maximum of `F+Q(1)`, `F+Q(2)`, and the
three scores in (8) with `M=2`. The complete distributions and expectations
remain separate diagnostics. They are never added across independent
candidate channels.

## Unfactored words and P205

Put

\[
d=\gcd(p-1,q-1),\quad s_p=(p-1)/d,\quad s_q=(q-1)/d.
\]

For a public positive word `W`, set

\[
r_p={s_p\over\gcd(s_p,W)},\qquad
r_q={s_q\over\gcd(s_q,W)}.
\]

For exponent `(N-1)W`, put

\[
\alpha_i=1/r_i,
\quad h_i=\min(v_2(i-1),v_2((N-1)W)),
\]

`a=min(h_p,h_q)`, and `b=max(h_p,h_q)`. The exact conditional Miller
probability is

\[
\mu_{a,b}=1-{4^a+2\over3\,2^{a+b}}.
\]

The complete exact factor probability is

\[
P_{205}(W)=\alpha_p+\alpha_q-(2-\mu_{a,b})
\alpha_p\alpha_q.                                      \tag{9}
\]

V3 records (9), `H(W)=max(alpha_p,alpha_q)`, both residuals through their
exact logarithms and extrema, and improvement over baseline `(N-1)^n`.

## Distinct-pair collision sources

Let `Z=(z_1,...,z_m)` be a public sequence. Canonical evaluation combines
equal integer values. Define the admissible ordered-pair set

\[
\mathcal D(Z)=\{(i,j):i\ne j,\ z_i\ne z_j\}.
\]

If `D_Z=|\mathcal D(Z)|`, define

\[
\kappa_\ell(Z)={1\over D_Z}
\#\{(i,j)\in\mathcal D(Z):z_i\equiv z_j\pmod\ell\}.    \tag{10}
\]

Set every score to zero when `D_Z=0`. Equal-index and equal-integer pairs are
not converted to a unit word and do not enter a denominator.

The baseline `(N-1)^n` already saturates each rational-primary support that
divides `N-1`. For side `i`, V3 therefore scores only

\[
s_i^\perp=\prod_{\ell^e\parallel s_i,\ \ell\nmid N-1}\ell^e.
\]

The captured log mass is

\[
C_i(Z)=\sum_{\ell^e\parallel s_i^\perp}
\kappa_\ell(Z)e\log_2\ell.                             \tag{11}
\]

V3 records each primary contribution and `min(C_p/log2(s_p^perp),
C_q/log2(s_q^perp))`. It also computes the exact joint collision score by
directly averaging

\[
{\gcd(s_i^\perp,|z_i-z_j|^n)\over s_i^\perp}           \tag{12}
\]

over `mathcal D(Z)`. This equals the complete P241 inclusion--exclusion
formula. It does not assume independent residual primes.

The exact distinct-pair Miller score is the average of (9) for

\[
W=(N-1)^n|z_i-z_j|^n,
\qquad(i,j)\in\mathcal D(Z).                            \tag{13}
\]

## Hypergeometric operational boundary

For `B=floor(sqrt(N))`, `H=floor(B/2)`, and fixed `r,c`, define

\[
R_{r,c}={\binom{B+c}{H+r}\over\binom BH}={P_{r,c}\over Q_{r,c}}
\]

in lowest terms. V3 constructs each endpoint by short signed interval
products. It never forms either central binomial coefficient.

Operational hypergeometric sequences are only:

```text
the reduced P endpoints;
the reduced Q endpoints;
horizontal adjacent determinants P_i Q_j-P_j Q_i;
vertical adjacent determinants P_i Q_j-P_j Q_i.
```

Only the identity transform is legal on these four sequences. Generic
adjacent sums, differences, quotients, remainders, and pair transforms are
ineligible. The full central-binomial value remains a named nonoperational
control and is never materialized or ranked.

## Gcd boundary

Every public scalar leaf, every exact numerator and denominator, every
determinant, and every scalar produced by an admitted sequence transform is
screened with `gcd(abs(x),N)` before multiplication into a word. A proper gcd
is an exact certificate and has row score one. A gcd of `1` is null. A gcd of
`N` is a recorded saturation and is not a factor.

Common leaf screening is shared by every candidate. Candidate-specific
transform screening is attributed to that candidate and every word that uses
it. Every admitted distinct-pair difference is also screened before its pair
word is scored. Completely factored support is screened either directly or
by the public balanced-factor lower bound before annihilator scoring.
Recursive-oracle primaries are screened only as nonoperational diagnostics.
Exact certificate source syntax and factor are preserved.
