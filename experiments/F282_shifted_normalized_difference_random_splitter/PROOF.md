# Proof of F282

## 1. Geometry of the unresolved branch

Because \(p<q\),

\[
 p<\sqrt{pq}<q.
\]

Hence \(p\le B<q\). Also \(q<2p\), so \(B<2p\). If
\(\gcd(B,N)>1\), then \(p\mid B\) or \(q\mid B\). The second alternative is
impossible because \(B<q\). The only multiple of \(p\) in
\([p,2p)\) is \(p\), so this direct branch has \(B=p\) and returns \(p\).

Assume now that \(\gcd(B,N)=1\). Then \(B\ne p\), and therefore

\[
 B=p+s\qquad(s\ge1).
\]

Since \(B<q\), write \(q=B+h\) with \(h\ge1\). The inequality
\(B^2<N=pq\) gives

\[
 (p+s)^2<p(p+s+h),
\]

and hence

\[
 s(p+s)<ph.
\]

Thus \(h>s\), so \(h\ge s+1\). Both hidden primes are odd, so

\[
 q-p=s+h
\]

is even. Equality \(h=s+1\) would make it odd. Therefore

\[
 h\ge s+2.
\tag{9}
\]

Finally \(q<2p\) says \(s+h<p\). Combining this with (9) gives

\[
 2s+2\le s+h<p.
\]

In particular \(p\ge2s+3\), which proves (1). Notice also that

\[
 h<B,
 \qquad B<q-1.
\tag{10}
\]

Indeed, \(q<2p<2B\) gives the first inequality, and \(h\ge2\) gives the
second.

## 2. Normalized differences are complete homogeneous polynomials

For pairwise distinct nodes \(x_0,\ldots,x_m\), the standard monomial
divided-difference identity is

\[
 [x_0,\ldots,x_m]X^{m+d}=h_d(x_0,\ldots,x_m).
\tag{11}
\]

For completeness, the Lagrange formula for the left side is

\[
 \sum_{j=0}^{m}
 \frac{x_j^{m+d}}{\prod_{k\ne j}(x_j-x_k)}.
\]

It equals the coefficient of \(t^d\) in

\[
 \prod_{j=0}^{m}(1-x_jt)^{-1}.
\]

This proves (11) as a symmetric polynomial identity.

Set \(m=B,d=B\), and \(x_j=a+j\). Since

\[
 \prod_{0\le k\le B,\ k\ne j}(j-k)
 =(-1)^{B-j}j!(B-j)!,
\]

the Lagrange formula becomes

\[
 [a,a+1,\ldots,a+B]X^{2B}
 =\frac1{B!}\sum_{j=0}^{B}
   (-1)^{B-j}\binom Bj(a+j)^{2B}
 =\frac{\Delta^B X^{2B}|_{X=a}}{B!}.
\]

Equation (11) now proves (3). Its right side lies in \(\mathbb Z[a]\), so
the displayed division by \(B!\) is exact over the integers.

## 3. The \(q\)-component vanishes for every shift

Reduce the \(B+1\) nodes \(a,a+1,\ldots,a+B\) modulo \(q\). They are
distinct because \(B<q\). Let \(E\) be this subset of \(\mathbb F_q\), and
let \(C=\mathbb F_q\setminus E\). Then

\[
 |C|=q-(B+1)=h-1.
\]

Over \(\mathbb F_q[t]\),

\[
 \prod_{x\in\mathbb F_q}(1-xt)=1-t^{q-1}.
\tag{12}
\]

Therefore, in \(\mathbb F_q[[t]]\),

\[
 \prod_{x\in E}(1-xt)^{-1}
 =\frac{\prod_{c\in C}(1-ct)}{1-t^{q-1}}.
\tag{13}
\]

The numerator in (13) has degree at most \(h-1<B\), while \(B<q-1\) by
(10). Hence the coefficient of \(t^B\) is zero. By (3), this coefficient is
\(F_B(a)\bmod q\). This proves (4) for every integer \(a\).

## 4. The \(p\)-component reduces to a short shifted polynomial

Modulo \(p\), the \(p+s+1=B+1\) consecutive nodes consist of one complete
copy of \(\mathbb F_p\) and the extra multiset

\[
 E_a=(a,a+1,\ldots,a+s).
\]

Using (12) with \(p\) in place of \(q\), their complete-homogeneous
generating series is

\[
 \prod_{j=0}^{B}(1-(a+j)t)^{-1}
 =\frac{H_{E_a}(t)}{1-t^{p-1}},
\qquad
 H_{E_a}(t)=\prod_{j=0}^{s}(1-(a+j)t)^{-1}.
\tag{14}
\]

Since \(B=p+s\), the coefficient of \(t^B\) in (14) is

\[
 h_{p+s}(E_a)+h_{s+1}(E_a).
\tag{15}
\]

There are no further terms. Indeed, the next possible index is

\[
 p+s-2(p-1)=s-p+2<0
\]

because \(p\ge2s+3\).

It remains to compare the two terms in (15). The nodes
\(x_j=a+j\), \(0\le j\le s\), are pairwise distinct modulo \(p\). The
distinct-node formula (11) gives, for every \(r\ge0\),

\[
 h_r(x_0,\ldots,x_s)
 =\sum_{j=0}^{s}
   \frac{x_j^{r+s}}{\prod_{k\ne j}(x_j-x_k)}.
\tag{16}
\]

For \(r=p+s\), the exponent in (16) is \(p+2s\). For \(r=s+1\), it is
\(2s+1\). If \(x_j\ne0\), Fermat's theorem gives

\[
 x_j^{p+2s}=x_j^{2s+1}.
\]

If \(x_j=0\), both powers are zero because both exponents are positive.
Thus (16) also covers the possible node \(a+j=0\), without dividing by that
node. Every denominator in (16) is a product of nonzero node differences.
Term by term,

\[
 h_{p+s}(E_a)=h_{s+1}(E_a)\pmod p.
\tag{17}
\]

Combining (3), (15), and (17) proves (5).

## 5. Exact degree and root count

Put

\[
 P_s(a)=2h_{s+1}(a,a+1,\ldots,a+s)\in\mathbb Z[a].
\]

Each monomial in \(h_{s+1}\) has total degree \(s+1\) in its \(s+1\)
arguments. After substituting \(a+j\), every weak composition of \(s+1\)
into \(s+1\) parts contributes one to the coefficient of \(a^{s+1}\).
There are

\[
 \binom{(s+1)+(s+1)-1}{(s+1)-1}
 =\binom{2s+1}{s}
\]

such compositions. Hence \(P_s\) has degree \(s+1\) and leading
coefficient \(2\binom{2s+1}{s}\).

Because \(2s+1<p\), none of the factorials in

\[
 \binom{2s+1}{s}=\frac{(2s+1)!}{s!(s+1)!}
\]

is divisible by \(p\). Since \(p\) is odd, the factor \(2\) is also a unit.
The reduction of \(P_s\) in \(\mathbb F_p[a]\) is therefore a nonzero
polynomial of exact degree \(s+1\). It has at most \(s+1\) roots. This proves
(6) and the stated root bound.

## 6. Probability, gcd, and expected trials

A uniform residue \(a\pmod N\) projects to an exactly uniform residue
modulo \(p\): every \(p\)-residue has exactly \(q\) lifts modulo \(N\).
By the root bound,

\[
 \Pr[p\nmid F_B(a)]\ge1-\frac{s+1}{p}.
\]

Equation (4) always gives \(q\mid F_B(a)\). Thus

\[
 \gcd(F_B(a),N)=q
\]

whenever \(p\nmid F_B(a)\); when \(p\mid F_B(a)\), the gcd is \(N\).
Since \(p\ge2s+3\),

\[
 1-\frac{s+1}{p}
 \ge 1-\frac{p-1}{2p}
 =\frac{p+1}{2p}>\frac12.
\]

Independent trials therefore have expected count at most
\(2p/(p+1)<2\). Every proposed divisor is checked by ordinary integer
division before output, so the procedure never returns a false factor.

## 7. Conditional bit complexity and normalization boundary

Integer square root, gcd, exact uniform sampling in \([0,N-1]\), and factor
verification have polynomial bit complexity in
\(n=\lceil\log_2(N+1)\rceil\). Exact uniform sampling can use rejection from
an \(n\)-bit interval and has expected fewer than two draws. If the modular
evaluator in the statement has a uniform numerical-QP worst-case bit bound,
then fewer than two expected evaluator calls preserve numerical-QP expected
bit complexity. This proves the conditional Las Vegas consequence on the
promise.

No such evaluator is constructed here. On the unresolved branch,

\[
 p<B<q<2p.
\]

Thus \(B!\) contains \(p\) exactly once and contains no \(q\), so
\(\gcd(B!,N)=p\). Equation (4) gives \(q\mid F_B(a)\) for every \(a\).
Consequently the raw difference

\[
 \Delta^B X^{2B}|_{X=a}=B!F_B(a)
\]

is divisible by all of \(N\) for every shift. Its residue has no splitting
signal. The useful \(q\)-only residue appears only after the exact integer
division by the factor-bearing \(B!\). F282 supplies a constant-success
dispatcher for already normalized residues; it supplies no way to perform
that normalization modulo \(N\) without exposing or otherwise handling its
nonunit factor.

The alternating-sum representation has \(B+1\) terms. The direct
complete-homogeneous recurrence has a range of length \(B\). At \(a=0\), all
terms are nonnegative and the monomial \(B^B\) occurs in
\(h_B(0,1,\ldots,B)\), while

\[
 h_B(0,1,\ldots,B)
 \le \binom{2B}{B}B^B.
\]

Thus this exact value has \(\Theta(B\log B)\) bits. On the balanced promise,
\(B=2^{\Theta(n)}\). These observations reject only the literal methods just
named. They do not preclude a succinct modular algorithm.

The proof uses the balanced distinct-odd-semiprime promise. It does not
recognize that promise, reduce every composite to it, or analyze other input
shapes. Therefore it is not an unconditional factoring theorem.
