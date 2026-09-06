# F171 statement-only blind reconstruction

## Verdict: PASS

The frozen statement has SHA-256

```text
22ee980dca180518170dde7d94df3a6a9225fffc880adf316738de6135e87b43
```

The theorem follows from an explicit CRT construction and Linnik's theorem.
No computation is needed.

Throughout, \(v_s(x)\) is the exponent of the prime \(s\) in \(x\).
For the selected values \(P_k\), let

\[
M_{s,k}=v_s(P_k)\pmod 2
\]

be the prime-exponent parity matrix over \(\mathbb F_2\).

## 1. Exact carry gate

Let \(r\nmid N\) be prime. From \(P_k=1+kN\),

\[
r\mid P_k
\iff kN\equiv-1\pmod r
\iff k\equiv-N^{-1}\pmod r.
\]

There is therefore one occupied carry class, namely
\(a_r=-N^{-1}\pmod r\). Merely finding \(j\equiv k\pmod r\)
does not show that either carry is in this class. Even two values divisible
by \(r\) reuse the parity row only when both valuations are odd. Finally,
row reuse alone does not imply a dependency among the full columns.

## 2. Classical prime inputs

We use two standard prime theorems.

1. The prime number theorem implies that the largest of the first \(m\)
   primes strictly larger than \(m\) is
   \((1+o(1))m\log m\).
2. Linnik's theorem gives absolute constants \(C,L>0\) such that, for every
   coprime pair \((a,Q)\), the class \(a\pmod Q\) contains a prime at most
   \(CQ^L\).

Fix a sufficiently large integer \(R\), and put \(m=4R\). Let
\(g_1,\ldots,g_m\) be the first \(m\) primes strictly larger than \(m\).
They are distinct, and

\[
m<g_k\le (1+o(1))m\log m.
\]

These primes are fixed from \(R\) before \(b,p,q\) are chosen, so they are
public construction data.

## 3. The CRT data

Prescribe a residue \(b\) by the following congruences.

For the prime \(2\), prescribe

\[
b\equiv1\pmod 4.
\]

For every odd prime \(r\le R\), prescribe

\[
b\equiv 2r-1\pmod {r^2}.
\]

For each \(1\le k\le m\), prescribe

\[
b\equiv (g_k-1)k^{-1}\pmod {g_k^2}.
\]

The last inverse exists because \(g_k>m\ge k\). The relevant prime powers
are pairwise coprime because every \(g_k>m=4R\). Hence the CRT gives one
class \(b\pmod A\), where

\[
A=\left(\prod_{\substack{r\le R\\r\ \mathrm{prime}}}r^2\right)
  \left(\prod_{k=1}^m g_k^2\right).
\]

Choose its representative with \(1\le b<A\). Every local residue is a
unit modulo its prime, so \(\gcd(b,A)=1\). Also \(4\mid A\) and
\(b\equiv1\pmod4\).

## 4. Producing the semiprime

Work modulo \(A^2\). Put

\[
\alpha=1+A.
\]

Choose \(t\in\{1,2\}\) by taking \(t=1\) when \(b\ne1\), and \(t=2\)
when \(b=1\), and put

\[
\beta=b+tA.
\]

For all sufficiently large \(A\), both \(\alpha\) and \(\beta\) lie
strictly between \(A\) and \(A^2\). They are distinct, and

\[
\gcd(\alpha,A^2)=\gcd(\beta,A^2)=1.
\]

Linnik's theorem supplies primes \(p,q\) such that

\[
p\equiv\alpha\pmod {A^2},\qquad
q\equiv\beta\pmod {A^2},
\]

and

\[
A<p,q\le C A^{2L}.
\]

The two residue classes are distinct, so \(p\ne q\). Both primes are odd:
their residues are odd because \(4\mid A\) and \(b\) is odd. Define

\[
N=pq.
\]

Then \(N\) is an odd distinct-prime semiprime and

\[
N\equiv 1\cdot b\equiv b\pmod A.
\]

This construction works for every sufficiently large integer \(R\), so it
gives an infinite family with \(R\to\infty\).

## 5. Canonical inverse relations

For each \(1\le k\le m\), the private-prime congruence gives

\[
1+kN\equiv 1+k(g_k-1)k^{-1}\equiv g_k\pmod {g_k^2}.
\]

Thus \(g_k\mid1+kN\). Define

\[
h_k=\frac{1+kN}{g_k}.
\]

We have \(g_k<N\), since \(p>A>g_k\), and \(\gcd(g_k,N)=1\). Also
\(h_k>0\), while \(g_k>m\ge k\) gives

\[
g_kN-(1+kN)=(g_k-k)N-1>0.
\]

Hence \(1\le h_k<N\). Since \(g_kh_k\equiv1\pmod N\), \(h_k\) is the
least positive inverse \(\iota_N(g_k)\). Therefore

\[
P_k=g_k\iota_N(g_k)=1+kN.
\]

In fact, \(N>A^2\) and \(g_k<A\) also give \(h_k>N/g_k>A>g_k\), so
\(g_k\) is the smaller endpoint if the canonical-pair convention orders
the two endpoints.

The selected bank has exactly one column for each carry
\(k=1,\ldots,m\), so its carries are exactly \(1,2,\ldots,m\).

## 6. Endpoint sign screens

The modulus \(A\) contains \(g_k^2\) and also the factor \(4\). Thus
\(A>g_k^2+1\). In particular,

\[
p,q>A>g_k^2+1.
\]

Let \(s\in\{p,q\}\). If \(s\mid g_k-h_k\), then
\(h_k\equiv g_k\pmod s\). Since \(g_kh_k\equiv1\pmod s\), this would give
\(s\mid g_k^2-1\), impossible because \(0<g_k^2-1<s\).

If \(s\mid g_k+h_k\), the same argument gives
\(s\mid g_k^2+1\), also impossible because \(0<g_k^2+1<s\).
Neither prime factor of \(N\) divides either signed endpoint combination.
Consequently,

\[
\gcd(g_k-h_k,N)=\gcd(g_k+h_k,N)=1.
\]

## 7. Exact small-prime coverage

First take \(r=2\). Since \(N\equiv1\pmod4\), the two distinct carries
\(k=1,5\) are available for \(m=4R\ge8\), and

\[
P_1=1+N\equiv2\pmod4,
\qquad
P_5=1+5N\equiv2\pmod4.
\]

Thus \(v_2(P_1)=v_2(P_5)=1\).

Now let \(r\le R\) be odd. The carries \(1\) and \(r+1\) are distinct
and lie in \([1,m]\). From \(N\equiv2r-1\pmod {r^2}\),

\[
P_1\equiv2r\pmod {r^2},
\]

so \(v_r(P_1)=1\), and

\[
P_{r+1}
 \equiv 1+(r+1)(2r-1)
 =r+2r^2
 \equiv r\pmod {r^2},
\]

so \(v_r(P_{r+1})=1\). This proves exact valuation-one coverage for every
prime \(r\le R\), including \(2\). Notice also that \(N\equiv-1\pmod r\)
for each such \(r\), so its unique occupied carry class is \(a_r=1\), and
the displayed pairs hit that class rather than only an arbitrary repeated
class.

## 8. Private rows and full rank

The congruence in Section 5 is nonzero modulo \(g_k^2\), so

\[
v_{g_k}(P_k)=1.
\]

Modulo \(g_k\), the same CRT condition says
\(N\equiv-k^{-1}\). For \(j\ne k\),

\[
P_j=1+jN\equiv 1-jk^{-1}
     =(k-j)k^{-1}\not\equiv0\pmod {g_k}.
\]

The last inequality holds because \(0<|k-j|<m<g_k\). Hence
\(g_k\nmid P_j\) for every \(j\ne k\). The rows
\(g_1,\ldots,g_m\), restricted to the selected columns, are exactly the
\(m\)-by-\(m\) identity matrix. Therefore

\[
\operatorname{rank}M=m,
\qquad
\ker M=0.
\]

Also, every nonzero difference between two selected carries has absolute
value at most \(m-1<g_k\). Thus no private endpoint prime divides a nonzero
selected carry difference.

The restriction \(M_{\le R}\) has only \(\pi(R)\) rows. Rank-nullity gives

\[
\dim\ker M_{\le R}
 =m-\operatorname{rank}M_{\le R}
 \ge m-\pi(R).
\]

It can therefore have many formal dependencies even though the complete
selected matrix has none.

## 9. Size of the family and endpoint bound

The private primes give

\[
\log A\ge 2\sum_{k=1}^m\log g_k>2m\log m.
\]

Conversely, the prime-number-theorem bound on \(g_m\) gives
\(\sum_k\log g_k=O(m\log m)\), and the elementary estimate

\[
\sum_{\substack{r\le R\\r\ \mathrm{prime}}}\log r
\le R\log R
\]

is also \(O(m\log m)\). Hence

\[
\log A=\Theta(m\log m).
\]

The Linnik construction gives

\[
A^2<N=pq\le C^2A^{4L}.
\]

Thus, for \(n=\lceil\log_2(N+1)\rceil\),

\[
n=\Theta(\log N)=\Theta(\log A)=\Theta(m\log m).
\]

It follows that \(\log n=\Theta(\log m)\), and therefore

\[
m=\Theta\!\left(\frac n{\log n}\right).
\]

There is no circularity in the endpoint bound. The lower bound
\(N>A^2\) gives

\[
n>2\log_2 A>4m\log_2m,
\]

while the chosen prime supply gives

\[
\max_k g_k=(1+o(1))m\log m.
\]

Thus \(g_k\le n\) for every \(k\) once \(R\) is sufficiently large.

## 10. Trial hardness and powers

From the Linnik upper bound,

\[
n\le 4L\log_2 A+O(1).
\]

Since \(A/(\log A)^2\to\infty\), the lower bounds \(p,q>A\) imply

\[
p,q>n^2
\]

for all sufficiently large family members. This is the stated trial-hard
property. Since \(N=pq\) has two distinct prime factors, both with exponent
one, \(N\) is not a perfect power.

The construction gives no constant-factor comparison between \(p\) and
\(q\). In particular, it proves no claim of the form \(p<q<2p\).

## 11. Consequence and exact scope

The selected values cover every prime row through \(R\) twice with odd
valuation, but their full parity matrix has zero kernel. Therefore complete
small-row coverage does not imply a selected square-class cycle. A
difference-cover locator cannot, by itself, provide the occupied class,
valuation parity, a full-matrix rank defect, or the later condition that a
normalized square root be non-global.

If an explicit carry list has quasipolynomial size
\(L(n)=\exp((\log n)^{O(1)})\), then a quadratic scan has size
\(L(n)^2=\exp((\log n)^{O(1)})\). Thus pair-location cost is not a source
existence theorem.

This proof concerns only the selected bank of \(m\) canonical-inverse
columns. A complete static grammar, or a later adaptive source, may append
columns that reuse the \(g_k\)-rows and create dependencies. Nothing here
rules that out. Such a source still needs its own full-source analysis and
the normalized-root gate.

The construction covers rows only through
\(R=\Theta(n/\log n)\). It does not establish an obstruction for every
quasipolynomial cutoff or every quasipolynomially generated source. It also
makes no claim about quotient-fingerprint groups. Accordingly, this is
neither a factoring lower bound nor a factoring algorithm.
