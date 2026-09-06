# F257 blind reconstruction — signed Pell-resultant refinement

## Authentication and scope

This reconstruction uses only `STATEMENT.md`, whose SHA-256 is

```text
de5c6833d7a5af14b144188b24cfa0c6e4734d5699824689baeed0bb45b2aa8a
```

The result is a proof-only refinement of P217 for two Pell rows with the
same positive discriminant. It proves three facts:

1. each odd rational prime power shared by the two specialized row values
   has a public, unique coordinate sign;
2. the two coordinate signs feed two explicit factors of the
   same-discriminant resultant; and
3. under a Jacobi-minus-one hypothesis, a short nonzero carry combination
   turns either factor into a one-sided Las Vegas gcd ticket.

The coordinate sign is not the normalized-root sign of a P66 square
relation. Nothing below proves an inverse-quasipolynomial lower bound for a
ticket event, so this is not a factoring algorithm.

## 1. Setup

Let \(N\geq 3\) be odd and let \(D>0\). For \(h=i,j\), take canonical Pell
rows

\[
 S_h^2-DT_h^2=1,\qquad T_h=y_h+k_hN,\qquad 0\leq y_h<N,
\]

and define

\[
 A_h=1+Dy_h^2,\qquad x_h=S_h\bmod N.
\]

Assume \(y_i\ne y_j\), as after duplicate-coordinate cleanup. Since both
coordinates are nonnegative, neither \(y_i-y_j\) nor \(y_i+y_j\) is zero.
The modular square-root comparison is made only after the public screens

\[
 \gcd(D,N)=\gcd(x_ix_j,N)=1.
\]

For the resultant claims, assume also \(k_i,k_j>0\), and put

\[
 f_h(X)=1+D(T_h-k_hX)^2,
 \qquad
 \Delta=T_ik_j-T_jk_i.
\]

Substitution of \(T_h=y_h+k_hN\) gives the three exact forms

\[
 \boxed{
 \Delta=y_ik_j-y_jk_i
       ={T_jy_i-T_iy_j\over N}.}
\]

Indeed, the \(k_ik_jN\) terms cancel in the first equality, and
\(T_jy_i-T_iy_j=N(k_jy_i-k_iy_j)\) proves the second.

## 2. Exact shared-gcd sign split

Set

\[
 u=y_i-y_j,\qquad v=y_i+y_j,\qquad d=\gcd(A_i,A_j),
\]

and

\[
 d_- =\gcd(A_i,u),\qquad d_+=\gcd(A_i,v).
\]

Because

\[
 A_i-A_j=D(y_i^2-y_j^2)=Duv
\]

and \(\gcd(A_i,D)=1\), Euclid's algorithm gives

\[
 \boxed{d=\gcd(A_i,uv),\qquad d_-\mid d,qquad d_+\mid d.}
\]

Here the two divisibilities follow because both \(u\) and \(v\) divide
\(uv\).

For a positive integer \(z\), write

\[
 z_{\rm odd}=z/2^{v_2(z)}.
\]

Let \(\ell\) be odd. If \(\ell\mid u\) and \(\ell\mid v\), then
\(\ell\mid 2y_i\), hence \(\ell\mid y_i\). This is incompatible with
\(\ell\mid A_i=1+Dy_i^2\). Thus no odd prime dividing \(A_i\) can divide
both \(u\) and \(v\). For every odd \(\ell\), therefore,

\[
 v_\ell(d)
 =\min\{v_\ell(A_i),v_\ell(u)+v_\ell(v)\}
\]

is the full valuation of exactly one of \(d_-\) and \(d_+\). Consequently

\[
 \boxed{
 d_{\rm odd}=(d_-)_{\rm odd}(d_+)_{\rm odd},\qquad
 \gcd((d_-)_{\rm odd},(d_+)_{\rm odd})=1.}
\]

Equivalently, every odd prime power in \(d\) occurs to its full exponent
in exactly one signed gcd. The minus channel means
\(y_i\equiv y_j\), and the plus channel means
\(y_i\equiv-y_j\), modulo that prime power.

### The two factor-of-two effects

First,

\[
 \gcd(d_-,d_+)=\gcd(A_i,u,v).
\]

Any common divisor of \(u\) and \(v\) divides \(2y_i\), while
\(\gcd(A_i,y_i)=1\). Hence

\[
 \boxed{\gcd(d_-,d_+)=\gcd(A_i,u,v)\in\{1,2\}.}
\]

Second, define

\[
 a=v_2(A_i),\qquad b=v_2(u),\qquad c=v_2(v).
\]

The 2-adic valuation of \(d\) is \(\min(a,b+c)\), while that of
\(\operatorname{lcm}(d_-,d_+)\) is
\(\max\{\min(a,b),\min(a,c)\}\). Thus

\[
 \boxed{d=\operatorname{lcm}(d_-,d_+)2^\eta,qquad \eta\in\{0,1\},}
\]

where exactly

\[
 \eta=\min(a,b+c)-
 \max\{\min(a,b),\min(a,c)\}.
\]

To identify the exceptional case, note first that a positive discrepancy
requires \(a,b,c>0\). The condition \(a>0\) forces \(D\) and \(y_i\) to be
odd, and \(b,c>0\) then forces \(y_j\) to be odd. Conversely, if
\(D,y_i,y_j\) are odd, both \(u,v\) are even and exactly one is divisible
by \(4\). Hence \(\min(b,c)=1\) and
\(\max(b,c)=b+c-1\). The displayed expression becomes

\[
 \eta=\min(a,b+c)-\min(a,b+c-1),
\]

which equals one exactly when \(a\geq b+c\). Therefore

\[
 \boxed{
 \eta=1\iff D,y_i,y_j\text{ are odd and }
 v_2(A_i)\geq v_2(uv).}
\]

For example, with \(D=7,y_i=1,y_j=3\),

\[
 A_i=8,\qquad A_j=64,\qquad u=-2,\qquad v=4,
\]

so

\[
 d=8,qquad d_-=2,qquad d_+=4.
\]

Thus the unconditional integer identity
\(d=\operatorname{lcm}(d_-,d_+)\) is false. The missing factor of two is
public and cannot affect gcd extraction against odd \(N\), but an exact
integer square-class decoder must retain it.

## 3. Signed resultant factors

Define

\[
 Q_-=D\Delta^2+(k_i-k_j)^2,
 \qquad
 Q_+=D\Delta^2+(k_i+k_j)^2.
\]

To compute the resultant, work temporarily in a quadratic extension and
choose \(\omega\) with \(D\omega^2=-1\). At the two roots of \(f_i\),
\(T_i-k_iX=\varepsilon\omega\), where \(\varepsilon=\pm1\). Since

\[
 k_j(T_i-k_iX)-k_i(T_j-k_jX)=\Delta,
\]

evaluation of \(f_j\) at those roots and multiplication over the two
values of \(\varepsilon\) gives

\[
 \operatorname{Res}_X(f_i,f_j)
 =D^2\left((D\Delta^2+k_i^2-k_j^2)^2
            +4Dk_j^2\Delta^2\right).
\]

The factor in parentheses satisfies

\[
 (D\Delta^2+k_i^2-k_j^2)^2+4Dk_j^2\Delta^2
 =\bigl(D\Delta^2+(k_i-k_j)^2\bigr)
  \bigl(D\Delta^2+(k_i+k_j)^2\bigr).
\]

Therefore P217's same-discriminant resultant has the exact factorization

\[
 \boxed{\operatorname{Res}_X(f_i,f_j)=D^2Q_-Q_+.}
\]

The signed gcds feed the corresponding factors over the full integers. If
working modulo \(d_-\), then \(y_j\equiv y_i\) and

\[
 \Delta=y_ik_j-y_jk_i\equiv-y_i(k_i-k_j),
\]

so

\[
 Q_-\equiv(k_i-k_j)^2(1+Dy_i^2)\equiv0\pmod {d_-}.
\]

Likewise, modulo \(d_+\), one has \(y_j\equiv-y_i\) and

\[
 \Delta\equiv y_i(k_i+k_j),\qquad
 Q_+\equiv(k_i+k_j)^2(1+Dy_i^2)\equiv0\pmod {d_+}.
\]

Hence

\[
 \boxed{d_-\mid Q_-,\qquad d_+\mid Q_+.}
\]

Every odd shared prime power is therefore assigned to one explicit
resultant factor without factoring \(A_i\), \(A_j\), or the resultant.
This is only a forward implication: either \(Q_-\) or \(Q_+\) can contain
prime divisors not shared by the row values.

### One-orbit formulas

Suppose the two rows are powers in one Pell orbit and \(i<j\). The standard
Pell multiplication identities are

\[
 S_{j-i}=S_iS_j-DT_iT_j,
 \qquad
 S_{i+j}=S_iS_j+DT_iT_j.
\]

Expanding the following expressions and using
\(S_h^2=1+DT_h^2\) gives

\[
\begin{aligned}
 &(k_iS_j-k_jS_i)^2+2k_ik_j(S_{j-i}-1)\\
 &\quad=(k_i-k_j)^2+D(k_iT_j-k_jT_i)^2=Q_-,
\end{aligned}
\]

and

\[
\begin{aligned}
 &(k_iS_j+k_jS_i)^2-2k_ik_j(S_{i+j}-1)\\
 &\quad=(k_i+k_j)^2+D(k_iT_j-k_jT_i)^2=Q_+.
\end{aligned}
\]

Thus

\[
 \boxed{
 Q_-=(k_iS_j-k_jS_i)^2+2k_ik_j(S_{j-i}-1),}
\]

\[
 \boxed{
 Q_+=(k_iS_j+k_jS_i)^2-2k_ik_j(S_{i+j}-1).}
\]

These formulas are exact in the orbit indices and canonical-wrap carries.
They do not force a useful hidden-prime divisor in either factor.

## 4. One-sided Jacobi-minus-one gcd tickets

Now specialize to

\[
 N=pq,qquad p<q<2p,
\]

for distinct odd primes \(p,q\), and assume

\[
 \left({-D\over N}\right)=-1.
\]

The public screen \(\gcd(D,N)=1\) makes the two Legendre symbols nonzero.
Their product is \(-1\), so \(-D\) is a quadratic residue at exactly one
hidden prime, denoted \(r_{\rm sp}\), and a nonresidue at the other,
denoted \(r_{\rm ns}\).

For \(\sigma\in\{-,+\}\), let

\[
 a_-=k_i-k_j,qquad a_+=k_i+k_j.
\]

Assume the short nonzero carry condition

\[
 \boxed{0<|a_\sigma|<\sqrt{N/2}.}
\]

The balance condition implies

\[
 p>\sqrt{N/2},
\]

because \(q<2p\) gives \(N=pq<2p^2\). Hence both hidden primes exceed
\(\sqrt{N/2}\), and neither can divide the nonzero integer
\(a_\sigma\).

If \(r_{\rm ns}\mid Q_\sigma=D\Delta^2+a_\sigma^2\), then either
\(\Delta\not\equiv0\pmod {r_{\rm ns}}\), in which case

\[
 -D\equiv(a_\sigma\Delta^{-1})^2\pmod {r_{\rm ns}}
\]

contradicts nonsquareness, or \(\Delta\equiv0\), in which case
\(r_{\rm ns}\mid a_\sigma\), contradicting the size bound. Thus the
nonsplit prime never divides \(Q_\sigma\), and

\[
 \boxed{\gcd(Q_\sigma,N)\in\{1,r_{\rm sp}\}.}
\]

It equals \(r_{\rm sp}\) exactly when
\(r_{\rm sp}\mid Q_\sigma\), and it can never equal \(N\).

Choose \(w\) such that

\[
 w^2\equiv-D\pmod {r_{\rm sp}}.
\]

Then

\[
 Q_\sigma\equiv a_\sigma^2-w^2\Delta^2
 =(a_\sigma-w\Delta)(a_\sigma+w\Delta)pmod {r_{\rm sp}}.
\]

The success event is therefore exactly the union

\[
 a_\sigma\equiv w\Delta\pmod {r_{\rm sp}},
 \qquad
 a_\sigma\equiv-w\Delta\pmod {r_{\rm sp}}.
\]

This is a conditional Las Vegas interface. If a public source of
admissible pairs makes this event occur with probability at least
\(1/Q(n)\), independent repetition needs at most \(Q(n)\) trials in
expectation, and every accepted output is certified by a proper gcd. No
inverse-quasipolynomial source law is proved here. Uniform and
source-independent heuristics do not apply, because \(D\), \(\Delta\),
and the carries are arithmetically coupled.

## 5. Factor-free refinement and the root-sign boundary

For an explicit bank with fixed \(D\), each \(d_{ij,-}\), \(d_{ij,+}\),
its odd part, each \(Q_{ij,-}\), \(Q_{ij,+}\), and its gcd with \(N\) is
computable in polynomial time in the materialized input length. Repeated
exact gcd refinement needs no prime factorization. It gives each resulting
odd fragment a public row-incidence mask. For a fragment shared by two
rows, the argument in Section 2 gives one consistent pairwise coordinate
sign. Primewise consistency follows because all solutions of
\(1+Dy^2\equiv0\) at a fixed odd prime differ only by sign. Binary parity
on the exponent-incidence vectors still computes the complete integer
square-class kernel. Thus P66 gcd refinement can be refined further by the
signed gcds without changing its factor-free nature.

This new sign is not the sign of a supplied modular square root. For a
two-row integer square relation

\[
 A_iA_j=R^2,
\]

the relevant normalized root is

\[
 \rho=R(x_ix_j)^{-1}\pmod N.
\]

The public screens make the inverse valid, and \(\rho^2\equiv1\pmod N\).
In contrast, \(d_-\) and \(d_+\) describe congruences of the coordinates
modulo rational primes dividing the exact integers \(A_i,A_j\). The two
notions live in different residue systems.

### Clean odd multiples

For odd \(h\), the Pell multiplication polynomials obey

\[
 1+DF_{h,D}(Y)^2=(1+DY^2)G_{h,D}(Y)^2.
\]

At every odd prime \(\ell\mid1+Dy^2\), expand the \(T\)-coordinate of the
odd power of a formal Pell element. All terms containing a positive power
of \(1+Dy^2\) vanish modulo \(\ell\), leaving

\[
 F_{h,D}(y)\equiv D^{(h-1)/2}y^h
 = (Dy^2)^{(h-1)/2}y
 \equiv(-1)^{(h-1)/2}y\pmod\ell.
\]

Thus

\[
 \boxed{F_{h,D}(y)\equiv(-1)^{(h-1)/2}y\pmod\ell.}
\]

An uncarried retained odd-multiple dependency is consequently in the minus
channel when \(h\equiv1\pmod4\), and in the plus channel when
\(h\equiv3\pmod4\). P218 nevertheless gives normalized root \(+1\) for
this dependency. Neither coordinate-sign channel therefore certifies a
useful P66 root.

### Exact same-channel contrast

First take the \(D=2,N=13859\) Pell orbit. It contains

\[
 (S_6,T_6)=(19601,13860),\qquad y_6=1,
\]

and its uncarried fifth multiple has \(y_{30}=109\). Hence

\[
 A_6=3,qquad A_{30}=23763=3\cdot89^2,qquad d_-=3.
\]

The exact root of the product is

\[
 R=3\cdot89=267.
\]

It equals the supplied product modulo \(N\), so this is a global
minus-channel relation.

Now take the preserved F253 arithmetic certificate

\[
 N=143,quad D=2,quad (y_i,x_i,A_i)=(1,17,3),
\]

\[
 (y_j,x_j,A_j)=(109,5,23763).
\]

It has the same minus-channel shared factor \(d_-=3\), the same exact root
\(R=267\), and supplied product \(x_ix_j=85\), but

\[
 \gcd(267-85,143)=13,
 \qquad
 \gcd(267+85,143)=11.
\]

Thus the exact and supplied roots agree at one hidden prime and disagree at
the other: the normalized root is non-global. This certificate has earlier
cleanup factors, so it is not a screen-free algorithmic hit. The two exact
examples have the same minus coordinate label but opposite outcomes for
globality. The coordinate label alone cannot determine the supplied-root
sign.

## 6. Exact remaining gap

What remains is an all-input theorem or an inverse-quasipolynomial law that
forces at least one of the following inside a numerical-quasipolynomial
bank:

1. a split-side zero of a short-carry \(Q_-\) or \(Q_+\), which gives the
   direct one-sided gcd ticket; or
2. a signed resultant-supported square dependency whose normalized root is
   non-global.

This reconstruction proves neither event. It also does not cover
cross-discriminant pairs, for which the \(y_i\pm y_j\) sign split is not
available.
