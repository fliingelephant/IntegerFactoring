# F284 — Blind reconstruction

Input: RECONSTRUCTION_STATEMENTS.md

SHA-256 of the exact input:

    3744a4d9d3e7561fed0bf51917fb02ab70bed64d24d2ed93ae7e90d6103e7d21

## Outcome

1. **Proved.** The coefficient polynomial has exact degree \(2j\), leading
   coefficient \(1/(2^j j!)\), and no denominator prime larger than \(j+1\).
2. **Proved.** An explicit truncated-series algorithm uses a number of exact
   arithmetic operations polynomial in \(J\), on integers of bit length
   polynomial in \(J+\log(b+1)\).
3. **Proved.** The stated probability follows from the degree-\(2j\) root
   bound modulo each prime and a union bound.

## 1. Coefficient polynomials

Put

\[
\phi(x)=\frac{e^x-1}{x}=\sum_{m\geq 0}\frac{x^m}{(m+1)!},
\qquad
\log\phi(x)=\sum_{n\geq 1}a_nx^n.
\]

The Gaussian-binomial product formula and

\[
\binom{2b}{b}=\prod_{r=1}^b\frac{b+r}{r}
\]

give, in formal power series,

\[
R_b(z)=\prod_{r=1}^b
\frac{\phi((b+r)z)}{\phi(rz)}.
\]

This also holds for \(b=0\), when the product is empty. If

\[
S_n(x)=\sum_{r=1}^x r^n
\]

denotes its Faulhaber polynomial, then

\[
\begin{aligned}
\log R_b(z)
&=\sum_{r=1}^b\sum_{n\geq1}a_n
  \bigl((b+r)^n-r^n\bigr)z^n\\
&=\sum_{n\geq1}a_nD_n(b)z^n,
\end{aligned}
\]

where

\[
D_n(b)=S_n(2b)-2S_n(b).
\]

Write

\[
\ell_n(b)=a_nD_n(b).
\]

The polynomial \(S_n\) has degree \(n+1\), so

\[
\deg \ell_n\leq n+1.
\]

Also, \(a_1=1/2\) and

\[
D_1(b)=S_1(2b)-2S_1(b)=b^2.
\]

Thus

\[
\ell_1(b)=\frac{b^2}{2}.
\]

Exponentiating the logarithmic series gives a polynomial whose restriction
to nonnegative integers is \(c_j(b)\):

\[
P_j(b)=
\sum_{\substack{k_1,\ldots,k_j\geq0\\
                  \sum_{n=1}^j nk_n=j}}
\prod_{n=1}^j\frac{\ell_n(b)^{k_n}}{k_n!}.
\]

For a summand in this expression, put \(K=\sum_n k_n\). Its degree is at
most

\[
\sum_{n=1}^j(n+1)k_n=j+K\leq2j.
\]

Equality can occur only when \(K=j\). Together with
\(\sum_n nk_n=j\), this forces \(k_1=j\) and all other \(k_n=0\).
Consequently the degree-\(2j\) term is uniquely supplied by

\[
\frac{\ell_1(b)^j}{j!}
=\frac{b^{2j}}{2^j j!}.
\]

Therefore \(P_j\) has exact degree \(2j\) and leading coefficient
\(1/(2^j j!)\). The empty coefficient is \(P_0=c_0=1\).

It remains to control coefficient denominators. For an integer \(M\geq2\),
let

\[
\mathcal A_M=\mathbb Z[1/r:\ r\text{ is prime and }r\leq M].
\]

First, \(a_n\in\mathcal A_{n+1}\). Indeed, with
\(u(x)=\phi(x)-1\),

\[
a_n=[x^n]\sum_{k=1}^n\frac{(-1)^{k+1}}{k}u(x)^k.
\]

Every contributing coefficient of \(u\) has the form \(1/(m+1)!\) with
\(m\leq n\), and the extra divisor \(k\) satisfies \(k\leq n\). Hence every
prime in a denominator is at most \(n+1\).

Second, \(D_n\in\mathcal A_{n+1}[b]\). The Stirling-number identity

\[
r^n=\sum_{k=1}^n
\left\{\begin{matrix}n\\k\end{matrix}\right\}k!\binom{r}{k}
\]

and the hockey-stick identity give

\[
S_n(x)=\sum_{k=1}^n
\left\{\begin{matrix}n\\k\end{matrix}\right\}k!
\binom{x+1}{k+1}.
\]

As a polynomial in \(x\), each displayed binomial coefficient has denominator
dividing \((k+1)!\). Thus its denominator primes are at most \(k+1\leq n+1\).
Substitution of \(b\) and \(2b\), and subtraction, introduce no new
denominator primes. It follows that

\[
\ell_n\in\mathcal A_{n+1}[b].
\]

In the displayed formula for \(P_j\), only \(n\leq j\) occurs. The remaining
divisors are the \(k_n!\), whose prime factors are at most \(k_n\leq j\).
Therefore

\[
P_j\in\mathcal A_{j+1}[b].
\]

After reducing its rational coefficients, no coefficient denominator can
contain a prime larger than \(j+1\). This proves Claim 1.

## 2. Polynomial-time short-jet evaluation

The preceding proof yields an exact algorithm that never constructs either
\(G_b\) or \(\binom{2b}{b}\).

First compute \(A_m=1/(m+1)!\) for \(0\leq m\leq J\), where
\(\phi(z)=\sum_m A_mz^m\). The identity

\[
\phi(z)(\log\phi(z))'=\phi'(z)
\]

gives the triangular recurrence

\[
a_m=A_m-\frac1m\sum_{i=1}^{m-1}(m-i)A_i a_{m-i}
\qquad(1\leq m\leq J).
\]

Next compute the Stirling numbers of the second kind through row \(J\) from

\[
\left\{\begin{matrix}n\\k\end{matrix}\right\}
=k\left\{\begin{matrix}n-1\\k\end{matrix}\right\}
+\left\{\begin{matrix}n-1\\k-1\end{matrix}\right\}.
\]

For \(x=b\) and \(x=2b\), compute
\(\binom{x+1}{k}\) for \(0\leq k\leq J+1\) by the exact recurrence

\[
\binom{x+1}{k+1}
=\binom{x+1}{k}\frac{x+1-k}{k+1}.
\]

The Stirling formula above then evaluates every \(S_n(b)\) and \(S_n(2b)\),
and hence every

\[
\ell_n=a_n\bigl(S_n(2b)-2S_n(b)\bigr),
\qquad 1\leq n\leq J.
\]

Finally set \(c_0=1\). From \(R_b'=R_b(\log R_b)'\), compute

\[
c_m=\frac1m\sum_{n=1}^m n\ell_n c_{m-n}
\qquad(1\leq m\leq J).
\]

All loops have \(O(J^2)\) exact arithmetic operations. A coarse bit-size
bound is enough. Factorials and Stirling numbers through row \(J\) have
polynomially many bits in \(J\). For \(x\in\{b,2b\}\), the binomial values
above have \(O(J(\log(b+1)+\log(J+1)))\) bits. The integers
\(S_n(x)\) have \(O(J\log(b+1)+J)\) bits.

For a fully explicit denominator bound, put \(H=(J+1)!\). In the finite
logarithm formula for any \(a_n\), \(n\leq J\), every product denominator
divides \(H^J\), and the outer divisor \(k\) divides \(J!\). Hence

\[
Q=J!H^J
\]

is a common denominator for \(a_1,\ldots,a_J\), with
\(O(J^2\log(J+1))\) bits. In the partition formula for any \(c_m\),
\(m\leq J\), there are at most \(J\) factors \(\ell_n\), while every
\(k_n!\) divides \(J!\). Thus \(Q^J(J!)^J\) is a common denominator for
all its summands. Each numerator factor has
\(O(J\log(b+1)+\operatorname{poly}(J))\) bits, and there are at most
\((J+1)^J\) summands. Therefore the numerator and denominator bit lengths
of every result, and of the reduced intermediate values in the triangular
recurrence, are polynomial in \(J+\log(b+1)\).

Standard exact integer and rational arithmetic is polynomial in operand bit
length. Therefore the total bit complexity is polynomial in
\(J+\log(b+1)\). This proves Claim 2, with \(J\) itself as the output-count
parameter.

## 3. Uniform-index gcd probes

Assume first that \(J\geq1\). Choose a common positive denominator \(d_j\)
for the coefficients of \(P_j\). Claim 1 shows that every prime factor of
\(d_j\) is at most \(j+1\leq J+1\). Hence \(d_j\) is invertible modulo both
\(p\) and \(q\), and therefore modulo \(N=pq\).

The reduction of \(P_j\) modulo \(p\) is a nonzero polynomial of degree
exactly \(2j\): its leading coefficient is the reduction of

\[
\frac1{2^j j!},
\]

which is nonzero because \(p>J+1>j\) and \(p>2\). The same statement holds
modulo \(q\). Thus the root bound over a field gives

\[
\#\{u\in\mathbb F_p:P_j(u)=0\}\leq2j,
\qquad
\#\{v\in\mathbb F_q:P_j(v)=0\}\leq2j.
\]

Uniform \(b\) in \(\{0,\ldots,N-1\}\) is uniform modulo each of \(p\) and
\(q\). Consequently

\[
\Pr[p\mid P_j(b)]\leq\frac{2j}{p},
\qquad
\Pr[q\mid P_j(b)]\leq\frac{2j}{q},
\]

where divisibility refers to the well-defined modular evaluation using
\(d_j^{-1}\).

If \(1<\gcd(P_j(b),N)<N\), then at least one of these two divisibility events
occurs. A union bound over both primes and all \(1\leq j\leq J\) yields

\[
\begin{aligned}
\Pr[\exists j:\ 1<\gcd(P_j(b),N)<N]
&\leq\sum_{j=1}^J 2j\left(\frac1p+\frac1q\right)\\
&=J(J+1)\left(\frac1p+\frac1q\right).
\end{aligned}
\]

For \(J=0\), the event and the right-hand side are both zero. This proves
Claim 3 exactly for the stated uniform-index coefficient probes.
