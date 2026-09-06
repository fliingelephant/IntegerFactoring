# Proof of F194

## 1. Numerical range

Because \(p<q<2p\),

\[
p^2<N<2p^2.
\]

Hence

\[
p\le B<\sqrt2p<2p,
\qquad B<q.
\tag{16}
\]

Thus the interval \(1,\ldots,B\) contains exactly one positive multiple of
either hidden prime: it contains \(p\), and it contains neither \(2p\) nor
\(q\).

## 2. The one-jump word

Write

\[
A_k=(-1)^k\binom{N-1}{k}
=\prod_{i=1}^k\frac{i-N}{i}.
\tag{17}
\]

If \(k<p\), every denominator is a unit modulo \(N\), and every factor in
(17) is congruent to one. Hence \(A_k\equiv1\pmod N\).

Now let \(p\le k\le B\). In the cross-multiplied identity

\[
k!A_k=\prod_{i=1}^k(i-N),
\tag{18}
\]

isolate the unique nonunit index \(i=p\). Put

\[
U=\prod_{\substack{1\le i\le k\\i\ne p}}i.
\]

The integer \(U\) is a unit modulo \(N\), and (18) becomes

\[
pUA_k=(p-N)\prod_{i\ne p}(i-N).
\]

Since \(p-N=p(1-q)\), exact integer cancellation of \(p\), followed by
reduction modulo \(N\), gives

\[
UA_k\equiv(1-q)U\pmod N.
\]

Cancel the unit \(U\). This proves (1).

For \(k\ne p\), \(k\) is a unit modulo \(N\), so

\[
k\binom Nk=N\binom{N-1}{k-1}
\]

gives \(\binom Nk\equiv0\pmod N\). At \(k=p\),

\[
\binom Np=q\binom{N-1}{p-1}\equiv q\pmod N,
\]

because \(p-1<p\) and (1) gives
\(\binom{N-1}{p-1}\equiv1\). This proves (2).

The standard alternating prefix identity is

\[
\sum_{k=0}^B(-1)^k\binom Nk=(-1)^B\binom{N-1}{B}.
\tag{19}
\]

Only \(k=0\) and \(k=p\) survive modulo \(N\). Since \(p\) is odd, (19)
becomes

\[
(-1)^B\binom{N-1}{B}\equiv1-q\pmod N.
\tag{20}
\]

The residue in (3) is therefore \(-q\pmod N\). Since \(0<q<N\), its gcd
with \(N=pq\) is exactly \(q\). Equation (4) follows from (20) and the
canonical residue convention.

Finally, Pascal's identity gives

\[
A_{k+1}
=-\binom{N-1}{k+1}
=-\frac{N-1-k}{k+1}\binom{N-1}{k},
\]

and cross-multiplication yields

\[
(k+1)(A_{k+1}-A_k)=-NA_k.
\]

This is (5). No division modulo \(N\) was used.

## 3. Interval-product comparisons

Let \(m=\lceil B/2\rceil\). Since \(B\ge p\), one has \(2m\ge B\ge p\).
Also \(m\le(B+1)/2<p\), because \(B<\sqrt2p\) and \(p\ge3\). Finally
\(2m\le B+1<q\): if \(B=p\), then \(B+1\le q\); if \(B>p\), then
\(B+1<2p\le q+1\), and equality with \(q\) would force \(B+1=q\), which
still gives \(2m\le q\); when \(2m=q\), parity is impossible because
\(2m\) is even and \(q\) is odd. Thus \(2m<q\).

In \(\binom{2m}{m}\), the denominator \(m!\) is coprime to \(N\), while
the numerator interval contains \(p\) and not \(q\). Its gcd with \(N\) is
therefore \(p\), proving (6).

For \(\binom{2B}{B}\), the denominator contains one \(p\). The numerator
interval \(B+1,\ldots,2B\) contains \(2p\), because \(B<2p\le2B\), and
contains \(q\), because \(B<q<2p\le2B\). It contains no second multiple of
\(q\), and its extra \(p\)-valuation cancels the denominator's
\(p\)-valuation. Thus the binomial is divisible by \(q\) but not by \(p\),
which proves (7).

## 4. Polynomial moments

For \(W\in\mathbb Z[T]\), write

\[
W(T)-W(0)=TV(T)
\]

with \(V\in\mathbb Z[T]\). Then

\[
\sum_{k=1}^{N-1}(W(k)-W(0))\binom Nk
=N\sum_{k=1}^{N-1}V(k)\binom{N-1}{k-1},
\]

which is zero modulo \(N\). Since

\[
\sum_{k=1}^{N-1}\binom Nk=2^N-2,
\]

equation (8) follows.

## 5. Frobenius blocks

In characteristic \(p\),

\[
(1+X)^{pq}=((1+X)^q)^p,
\qquad
X^{pq}=(X^q)^p.
\]

Because Frobenius is additive,

\[
E_N=((1+X)^q-1-X^q)^p\pmod p.
\]

The proof modulo \(q\) is symmetric. The inner polynomial modulo \(p\) has
linear coefficient \(q\not\equiv0\pmod p\), so its \(X\)-adic order is one;
raising to the \(p\)-th power gives local order \(p\). Symmetrically the
other local order is \(q\).

For (12), write \(q=p+d\). In characteristic \(p\),

\[
(1+X)^q=(1+X^p)(1+X)^d,
\qquad
X^q=X^pX^d.
\]

Raise the difference to the \(p\)-th power and expand. This gives exactly
the two displayed sums in (12). Since \(1\le d<p\), every
\(\binom dj\) is nonzero modulo \(p\). Equation (13) follows directly from
(11); every \(\binom pj\), \(1\le j<p\), is nonzero modulo \(q>p\).

If \(d\ge R\ge r\), the exponents \(p,2p,\ldots,rp\) occupy every residue
class modulo \(r\), because \(p\) is invertible modulo \(r\) whenever the
cyclic sketch is admissible with \(\gcd(r,N)=1\). The same argument applies
to \(q,2q,\ldots,rq\). Thus every bucket has source support in both fields.
If \(d<R\), test the integers \(1,\ldots,R-1\) as possible gaps. For a
candidate \(\delta\), test whether \(\delta^2+4N\) is a square. At the
correct value its square root is \(p+q\), and

\[
p=\frac{\sqrt{\delta^2+4N}-\delta}{2},
\qquad
q=\frac{\sqrt{\delta^2+4N}+\delta}{2}.
\]

The theorem asserts only the support dichotomy; it does not preclude
cancellation among aliased terms.

## 6. Signed quotient carry

Equation (20) says that the numerator in (14) is divisible by \(N\), so
\(h\in\mathbb Z\). Rearrangement gives (15). Reducing (15) modulo \(2^t\)
recovers \(q\bmod2^t\). If \(2^t>q\), this is the integer \(q\).

Conversely, given only \(C\bmod2^t\), every candidate \(q\) determines
exactly one \(h\bmod2^t\) from (15), because \(N\) is invertible modulo
\(2^t\). Hence the missing information is the quotient carry, not the
public binary valuation or the remote coefficient residue by itself.
