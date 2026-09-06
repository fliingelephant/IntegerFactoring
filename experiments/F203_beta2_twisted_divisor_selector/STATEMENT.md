# F203 candidate — a twisted divisor coefficient selects the beta-two child, while the quotient child can forget its orientation

## Status and scope

This is a frozen proof-only candidate awaiting hostile audit. It gives an
exact integer-specific reformulation of the P175 next-bit gate. It supplies
no quasipolynomial coefficient evaluator and no factoring algorithm.

The positive theorem is a promise-function equivalence for distinct balanced
odd semiprimes. The quotient theorem validates one-child recursion accounting
but also proves an exact coalescence on the first hard opposite-orientation
branch. It is not a lower bound against adaptive deterministic use of a
recursively factored child.

Assume

\[
 N=pq,\qquad p<q<2p,
 \qquad B=\lfloor\sqrt N\rfloor,
\]

where \(p,q\) are distinct odd primes. Let

\[
 m=2^t,\qquad t\geq1,\qquad 2m<p,
\]

and grant a correct reciprocal prefix

\[
 u\equiv p^{-1}\pmod m.
\]

Write \(r,c\in\{1,3,\ldots,m-1\}\) for the canonical residues

\[
 r\equiv u^{-1}\equiv p\pmod m,
 \qquad
 c\equiv Nu\equiv q\pmod m.
\]

## The two child progressions

Define the public \(2m\)-periodic weight

\[
 w_{m,r}(d)=
 \begin{cases}
 +1,&d\equiv r\pmod{2m},\\
 -1,&d\equiv r+m\pmod{2m},\\
 0,&d\not\equiv r\pmod m.
 \end{cases}
\]

The two children of the parent prefix are

\[
 J_+=\{j:\lceil B/2\rceil<j\leq B,\ j\equiv r\pmod{2m}\},
\]

\[
 J_-=\{j:\lceil B/2\rceil<j\leq B,\ j\equiv r+m\pmod{2m}\}.
\]

The balance promise gives \(B/2<p\leq B<q\). Hence exactly one child
contains \(p\), and

\[
 \epsilon:=w_{m,r}(p)\in\{+1,-1\}
\]

is the desired next bit.

## Public relation between the two hidden factors

Let

\[
 v\equiv r^{-1}\pmod{2m},
 \qquad
 c_0\equiv Nv\pmod{2m}
\]

be canonical odd residues modulo \(2m\). If \(c\ne r\), then

\[
 w_{m,r}(q)=0.
\]

If \(c=r\), put

\[
 \lambda=w_{m,r}(c_0)\in\{+1,-1\}.
\]

Then

\[
 \boxed{w_{m,r}(q)=\lambda\epsilon.}
\]

Thus the sibling relation is public even though the orientation
\(\epsilon\) is hidden.

## Twisted divisor selector

Define the exact twisted divisor coefficient

\[
 S_{m,r}(N)=\sum_{d\mid N}d\,w_{m,r}(d)
\]

and remove the two public divisors:

\[
 T=S_{m,r}(N)-w_{m,r}(1)-Nw_{m,r}(N).
\]

Then

\[
 \boxed{
 T=
 \begin{cases}
 \epsilon p,&c\ne r,\\
 \epsilon(p+q),&c=r,\ \lambda=+1,\\
 \epsilon(p-q),&c=r,\ \lambda=-1.
 \end{cases}}
\]

In particular, \(T\ne0\), and the next bit is

\[
 \boxed{
 \epsilon=
 \begin{cases}
 \operatorname{sgn}(T),&c\ne r\text{ or }\lambda=+1,\\
 -\operatorname{sgn}(T),&c=r\text{ and }\lambda=-1.
 \end{cases}}
\]

The same value factors \(N\) in deterministic polynomial time:

1. If \(c\ne r\), then \(p=|T|\).
2. If \(c=r\) and \(\lambda=+1\), then \(|T|=p+q\).
3. If \(c=r\) and \(\lambda=-1\), then \(|T|=q-p\), so

   \[
   p+q=\sqrt{T^2+4N}.
   \]

Conversely, the factorization of \(N\) computes \(S_{m,r}(N)\) directly.
Therefore exact evaluation of \(S_{m,r}(N)\) and factoring are
polynomial-time equivalent on this promise. This is an evaluator target,
not an evaluator.

The coefficient has the exact formal Lambert-series representation

\[
 \boxed{
 S_{m,r}(N)
 =[X^N]\sum_{a\geq1}
       \frac{a\,w_{m,r}(a)X^a}{1-X^a}.}
\]

For \(m=2\) and \(r=1\), the weight is the primitive character
\(\chi_4\). Hence the fixed coefficient

\[
 \sum_{d\mid N}d\chi_4(d)
\]

already factors every promised odd semiprime. The factor \(d\) is essential:
the usual sum-of-two-squares coefficient uses
\(\sum_{d\mid N}\chi_4(d)\), which need not orient the two factors.

## The contracted quotient and its two lifts

Define

\[
 K=\frac{N-rc}{m}.
\]

Then

\[
 0<K<N/2,
 \qquad
 \gcd(K,N)=1.
\]

Thus \(K\) has at least one fewer input bit than \(N\). Let

\[
 \delta=K\bmod2.
\]

Write the true next bits as

\[
 p\equiv r+am\pmod{2m},
 \qquad
 q\equiv c+bm\pmod{2m},
 \qquad a,b\in\{0,1\}.
\]

They obey the public relation

\[
 \boxed{b=a\mathbin{\mathsf{xor}}\delta.}
\]

For either candidate \(a\), put \(b=a\mathbin{\mathsf{xor}}\delta\) and
define

\[
 \boxed{
 K'_a=
 \frac{K-ac-br-abm}{2}
 =\frac{N-(r+am)(c+bm)}{2m}.}
\]

Both \(K'_0,K'_1\) are positive integers smaller than \(N/(2m)\), and
both are coprime to \(N\). For the true bit \(a\), \(K'_a\) is the next
quotient state after lifting the modulus from \(m\) to \(2m\).

Their exact separation is

\[
 \begin{array}{c|c|c}
 \delta&K'_0&K'_1\\ \hline
 0&K/2&(K-r-c-m)/2\\
 1&(K-r)/2&(K-c)/2.
 \end{array}
\]

Consequently,

\[
 \boxed{K'_0=K'_1\iff \delta=1\text{ and }r=c.}
\]

This is exactly the case in which the two factors occupy opposite sibling
classes inside the same parent class. The contracted quotient then forgets
which orientation belongs to the smaller factor.

At the first stage \(m=2\), one always has \(r=c=1\). If
\(N\equiv3\pmod4\), then

\[
 K=\frac{N-1}{2}\quad\text{is odd}
\]

and both orientations give

\[
 \boxed{K'_0=K'_1=\frac{N-3}{4}.}
\]

Thus even the exact next quotient value cannot select the smaller factor's
first nontrivial bit on this branch.

## Recursion accounting and exact boundary

If a future construction reduces one selector stage to at most one recursive
factorization of \(K\) or of one selected \(K'_a\), plus numerical-QP local
work, then the recurrence

\[
 \mathcal T(n)\leq\mathcal T(n-1)+\operatorname{QP}(n)
\]

is numerical QP. No fixed-ratio contraction is needed.

F203 supplies no such reduction and no rule for selecting \(a\). On the
coalescing branch, the two proposed next states are literally the same
integer, so their factorizations cannot orient the lift. At \(m=2\), factoring
\((N-1)/2\) is the one-child preprocessing already studied in P165. P165
closes only independent uniform-base return after that preprocessing; it does
not close adaptive deterministic uses of the factorization.

The surviving positive targets are therefore exact and narrow:

- evaluate the twisted divisor coefficient implicitly in QP time;
- extract the orientation from a nonlocal integer statistic weaker than the
  full coefficient; or
- use a noncoalesced recursively factored quotient through a new adaptive
  deterministic decoder.
