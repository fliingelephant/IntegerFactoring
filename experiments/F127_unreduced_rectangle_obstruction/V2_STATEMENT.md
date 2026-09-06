# F127 V2 statement — unreduced rectangle obstruction

## Definitions

Let \(N>1\) be composite, and let \(h\) be its least prime divisor. For
each positive unit \(m<N\), define

\[
K_m=(-N^{-1})\bmod m,
\qquad 0\le K_m<m,
\]

with \(K_1=0\). Then

\[
w_m=\frac{1+K_mN}{m}
\]

is the canonical inverse of \(m\) in \(\{1,\ldots,N-1\}\), and \(K_m\)
is its canonical carry.

Let \(u,a,b\) be positive integers with

\[
\gcd(uab,N)=1,
\qquad
uab<N.
\]

The four unreduced rectangle corners are

\[
c_{00}=u,
\quad c_{10}=ua,
\quad c_{01}=ub,
\quad c_{11}=uab.
\]

For each corner, an endpoint sign screen is

\[
\gcd(c_{ij}-w_{c_{ij}},N)
\quad\text{or}\quad
\gcd(c_{ij}+w_{c_{ij}},N).
\]

The P114 eligibility factors are

\[
u, a, b, a-1, b-1, b-a.
\]

Each factor is screened separately against \(N\). A zero factor is a global
degeneracy, not a proper hit. The P114 residual is

\[
\Omega_{\square}
=(b-a)(K_{uab}-K_u)+(ab-1)(K_{ua}-K_{ub}).
\]

A screen is a *proper hit* only when its gcd with \(N\) lies strictly between
\(1\) and \(N\). The *complete local rectangle channel* consists of the
eight endpoint sign screens, the six separate eligibility-factor screens,
and the residual screen.

## Nested-carry theorem

There are unique digits

\[
0\le A<a,
\quad
0\le B<b,
\quad
0\le T<ab
\]

such that

\[
K_{ua}=K_u+uA,
\quad
K_{ub}=K_u+uB,
\quad
K_{uab}=K_u+uT,
\]

and

\[
T\equiv A\pmod a,
\qquad
T\equiv B\pmod b.
\]

No coprimality assumption on \(a\) and \(b\) is needed. The residual is

\[
\boxed{
\Omega_{\square}
=u[(b-a)T+(ab-1)(A-B)].
}
\]

It satisfies

\[
|\Omega_{\square}|<2uab\max(a,b).
\]

Consequently:

1. If \(a,b>1\), \(a\ne b\), and
   \(h>2uab\max(a,b)\), the residual and every eligibility-factor screen
   give only gcd \(1\) or \(N\). This claim does not include the endpoint
   sign screens.
2. If \(R\ge2\), \(u,a,b\le R\), and \(h>R^6+1\), then the complete local
   rectangle channel gives only gcd \(1\) or \(N\).

## Menu-tail consequence

Let a declared menu contain exactly \(Q\ge1\) distinct canonical unit residues in
\(\{1,\ldots,N-1\}\). Scan all \(Q^3\) ordered triples, with repetition
permitted. Let \(T_R\) be the number of menu entries whose canonical integer
representative is greater than \(R\).

If \(2R^4<h\), the fraction of all \(Q^3\) ordered triples that can give a
proper residual or eligibility-factor hit is at most

\[
\frac{Q^3-(Q-T_R)^3}{Q^3}\le\frac{3T_R}{Q}.
\]

If also \(R\ge2\) and \(R^6+1<h\), the same bound covers the complete local
rectangle channel, including endpoint signs. This is a raw ordered-triple
fraction, not a conditional density among eligible triples.

For balanced \(n\)-bit semiprimes, \(h=2^{\Theta(n)}\). Thus every numerical
bound \(R=2^{O((\log n)^k)}\), for fixed \(k\), eventually satisfies both
least-prime inequalities. This statement concerns numerical residue
magnitude, not description length.

## Two infinite fixed traps

1. If \(u=1,a=2,b=3\) and \(N\equiv5\pmod6\), then
   \((K_1,K_2,K_3,K_6)=(0,1,1,1)\) and \(\Omega_{\square}=1\).
   Infinitely many balanced distinct-prime semiprimes in this class are
   obtained from comparable primes \(p\equiv1\pmod6\) and
   \(q\equiv5\pmod6\).
2. If \(u=1,a=3,b=7\) and \(N\equiv23\pmod{42}\), then
   \((K_1,K_3,K_7,K_{21})=(0,1,3,10)\) and
   \(\Omega_{\square}=0\). Infinitely many balanced distinct-prime
   semiprimes in this class are obtained from comparable primes
   \(p\equiv1\pmod{42}\) and \(q\equiv23\pmod{42}\). The odd mod-42 class
   makes every nonzero eligibility factor a unit.

Once the hidden factors exceed the fixed corner squares plus one, every
endpoint screen in both families is also nonproper. More generally, every
fixed finite bank of literal, \(N\)-independent unreduced integer triples is
defeated by every balanced semiprime whose least factor exceeds one fixed
bank-dependent constant.

## Scope

The theorem does not cover wrapped rectangles, numerically large canonical
rectangles, an \(N\)-dependent or adaptive rectangle selector, or the P66
retained-value decoder.
