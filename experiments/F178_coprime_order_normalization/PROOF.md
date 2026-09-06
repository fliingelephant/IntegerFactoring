# Proof of the F178 coprime-order normalization

## 1. Order after the public exponent

For an element of finite order \(e\), its \(E\)-th power has order

\[
e/\gcd(e,E).
\]

This proves (6). Let \(r\mid N\) be any rational prime. Since
\(e_j<R_j\le N<2^n\),

\[
v_r(e_j)<n.
\]

On the other hand,

\[
v_r(E)=n\,v_r(N)\ge n.
\]

Therefore \(E\) removes the full \(r\)-primary part of every \(e_j\).
This holds for every \(r\mid N\), proving \(\gcd(f_j,N)=1\).

The exponent is public and compact: \(\log_2 E=n\log_2N=O(n^2)\).

## 2. The identity screen

The gcd \(H\) is the product of exactly those hidden prime-power components
on which \(f_j=1\). A partial set gives a proper factor. Suppose \(H=N\).

Let \(p\) be the least rational prime divisor of \(N\), and consider the
component \(p^a\). Put

\[
d=\operatorname{ord}_p(4).
\]

Then \(d\mid p-1\) and \(d\mid e_p\). Since \(f_p=1\), equation (6) gives
\(e_p\mid E\), hence \(d\mid E\). Every prime divisor of \(d\) is smaller
than \(p\), while every prime divisor of \(E=N^n\) is a prime divisor of
\(N\) and is at least \(p\). Thus \(d=1\). Hence \(4\equiv1\pmod p\), so
\(p=3\). Because \(N\) is composite, \(1<3<N\), and \(\gcd(3,N)=3\) is a
proper factor. The surviving branch is therefore exactly (9).

## 3. The lcm screen

If \(J=1\), no \(f_j\) divides \(\Lambda_T\). An integer divides
\(\Lambda_T\) exactly when each prime-power divisor in its factorization is
at most \(T\). Thus \(\sigma(f_j)>T\) for every \(j\), proving (14).

Suppose \(J=N\). The complete factorization of \(\Lambda_T\) is known.
The standard factor-first order reduction repeatedly tests

\[
\gcd(y^{M/\ell}-1,N)
\]

for prime divisors \(\ell\) of the current annihilator \(M\). A partial gcd
factors \(N\). On a no-factor run, a global gcd permits removal of \(\ell\),
and a gcd equal to one proves that no local order divides \(M/\ell\). At
termination, unequal local orders would differ in some prime-adic exponent
and the corresponding test would have been partial. Hence the routine either
factors or returns their common exact value \(m\), with its complete
factorization.

It remains to prove the small-common-order exit. Assume \(m\le n\), and let
\(p\) again be the least rational prime divisor of \(N\). Write

\[
d=\operatorname{ord}_p(4).
\]

The prime-power lifting law gives

\[
e_p=d p^u
\]

for some \(0\le u<a\). Since \(d\mid p-1\), every prime divisor of \(d\)
is smaller than \(p\), so \(\gcd(d,E)=1\). The exponent \(E\) contains the
entire \(p^u\) part. Consequently

\[
f_p=\frac{e_p}{\gcd(e_p,E)}=d=m.
\]

Thus \(p\mid 4^m-1\), and \(D>1\). If \(D=N\), then
\(e_j\mid m\) for every hidden component, contradicting

\[
e_j>C\ge n\ge m.
\]

Therefore \(1<D<N\), proving (13).

## 4. The sign quotient

For an element of order \(f\), its image modulo \(\langle-1\rangle\) has
order

\[
f/\gcd(f,2).
\]

If the prime-power divisor of \(f_j\) exceeding \(T\) is odd, it survives
unchanged in the quotient. If it is \(2^a\), the quotient loses only one
factor two and retains \(2^{a-1}>T/2\ge C\). This proves (16).

## 5. Cost and recursion

The sieve through \(T\) gives the prime powers in \(\Lambda_T\) and hence
its complete factorization. Its bit length is \(O(T\log T)\), a sufficient
QP bound. Modular exponentiation uses a number of ring operations polynomial
in the exponent bit length. The factor-first reductions make QP many such
calls. Every returned divisor is verified, and P159's factor-tree argument
uses fewer than \(2n\) recursive nodes. All claimed work is therefore uniform
deterministic QP bit complexity.

This completes the trichotomy and no more: the surviving \(f_j\) may remain
unequal and may have no known QP-size factored common annihilator.
