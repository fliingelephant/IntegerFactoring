# Blind reconstruction of F213

## Evidence boundary

Before reading the F213 statement, I computed

\[
\operatorname{SHA256}(\texttt{STATEMENT.md})
=\texttt{9e74427637283e893c5a91bc5d0d24d7a4040526dbe5cf2e1599971474081fff},
\]

which is the required hash. This reconstruction uses only the repository-root
`PROMPT.md` and the hashed F213 `STATEMENT.md`. It does not use a proof, audit,
provenance file, manifest, ledger, or another reconstruction. No numerical
experiment was used.

## Construction

Fix an integer \(M\geq 2\). For each \(1\leq a\leq M\), Bertrand's theorem
gives a prime

\[
  2^{M+a+2}<\ell_a<2^{M+a+3}.
\]

These intervals are pairwise disjoint. Hence the \(\ell_a\)'s are distinct.
They are odd, and

\[
  \ell_a>M^2+1
\]

for all \(M\geq2\). Define

\[
 C=2\prod_{b=1}^M b(b^2+1).
\]

The prime \(\ell_a\) is coprime to \(C\), because it is larger than every
factor \(b\) and \(b^2+1\) occurring in this product. It is also coprime to
\(2a\). Therefore there is a unique residue \(t_a\pmod{\ell_a^2}\) satisfying

\[
 2a t_a+1-a^2\equiv \ell_a\pmod{\ell_a^2}.
\]

The moduli \(C,\ell_1^2,\ldots,\ell_M^2\) are pairwise coprime. By the Chinese
remainder theorem, there is a residue \(u\) modulo

\[
 B=C\prod_{a=1}^M\ell_a^2
\]

such that

\[
 u\equiv0\pmod C,
 \qquad
 u\equiv t_a\pmod{\ell_a^2}\quad(1\leq a\leq M).
\]

Choose any prime divisor \(q\) of \(B^2+1\). Then \(q\) is odd and
\(q\nmid B\). Apply the Chinese remainder theorem once more to obtain a
residue \(s_0\pmod{Bq}\) with

\[
 s_0\equiv u\pmod B,
 \qquad
 s_0\equiv B\pmod q.
\]

Take \(0\leq s_0<Bq\), and set

\[
 s=s_0+Bq,
 \qquad
 N=s^2+1.
\]

All earlier congruences are preserved. Since \(2\mid C\mid s\), the integer
\(s\) is even. Also \(s\geq Bq>M\). The congruence
\(s\equiv B\pmod q\), together with \(q\mid B^2+1\), gives \(q\mid N\).
Moreover \(s>q\), so \(1<q<N\). Thus \(N\) is an odd composite integer of
the required form.

This completes the simultaneous existence construction. The rest of the
proof checks all of its claimed properties.

## Exact norms and their ranges

Because

\[
 0<\sqrt{s^2+1}-s
   =\frac1{\sqrt{s^2+1}+s}
   <\frac1{2s},
\]

for \(1\leq a\leq M<s\) one has

\[
 as<a\sqrt N<as+1.
\]

Consequently

\[
 r_a=as,
 \qquad
 E_a=a^2(s^2+1)-a^2s^2=a^2,
\]

and

\[
 F_a=(as+1)^2-a^2(s^2+1)=2as+1-a^2.
\]

The inequalities \(0<E_a<N\) follow from \(a<s\). Also

\[
 F_a=a(2s-a)+1>0,
 \qquad
 N-F_a=(s-a)^2>0.
\]

Thus both norm families are strictly between \(0\) and \(N\).

## Direct gcd screening

For every \(a\leq M\), both \(a\mid s\) and \(a^2+1\mid s\), by the
definition of \(C\).

First, a common divisor of \(a\) and \(N=s^2+1\) divides both \(s\) and
\(s^2+1\). Hence

\[
 \gcd(a,N)=1.
\]

Also \(\gcd(s,N)=1\), so \(r_a=as\) is a unit modulo \(N\), and
\(E_a=a^2\) is a unit modulo \(N\).

If \(d\mid as+1\) and \(d\mid N\), then

\[
 d\mid a^2N-(as+1)(as-1)=a^2+1.
\]

Since \(a^2+1\mid s\), this implies \(d\mid s\). Together with \(d\mid
s^2+1\), it gives \(d=1\). Therefore \(\gcd(r_a+1,N)=1\). Finally,

\[
 F_a\equiv(as+1)^2\pmod N,
\]

so \(\gcd(F_a,N)=1\) as well. This proves every gcd equality in the
statement.

## Private valuation rows

The defining congruence for \(t_a\), inherited by \(s\), gives

\[
 F_a=2as+1-a^2\equiv\ell_a\pmod{\ell_a^2}.
\]

Hence

\[
 v_{\ell_a}(F_a)=1.
\]

Since \(\ell_a>M\), it divides none of the numbers \(E_b=b^2\).

It remains to exclude \(\ell_a\) from every other \(F_b\). Modulo
\(\ell_a\), the congruence \(\ell_a\mid F_a\) says

\[
 2as\equiv a^2-1.
\]

For \(b\ne a\), multiplication of \(F_b\) by the unit \(a\) gives

\[
 \begin{aligned}
 aF_b
 &=2abs+a-ab^2\\
 &\equiv b(a^2-1)+a-ab^2\\
 &=(a-b)(ab+1)\pmod{\ell_a}.
 \end{aligned}
\]

Here \(0<|a-b|<\ell_a\), and

\[
 0<ab+1\leq M^2+1<\ell_a.
\]

Neither factor is zero modulo \(\ell_a\). Thus \(\ell_a\nmid F_b\) for
\(b\ne a\). The \(\ell_a\)-valuation row is therefore nonzero in exactly
the \(F_a\) column, where its entry is one.

## Exact parity kernel

Consider a dependency in the signed ordinary rational-prime parity matrix.
For each \(a\), its \(\ell_a\)-row forces the coefficient of the \(F_a\)
column to be zero. After all \(F\)-columns are removed, a selected set
\(S\) of \(E\)-columns has signed product

\[
 \prod_{a\in S}(-E_a)
 =(-1)^{|S|}\left(\prod_{a\in S}a\right)^2.
\]

This is a positive rational square exactly when \(|S|\) is even. Conversely,
every even \(S\) visibly has a positive square product. In the stated column
ordering, the kernel is consequently exactly

\[
 \left\{(x_1,0,\ldots,x_M,0):
   \sum_{a=1}^M x_a=0\text{ in }\mathbb F_2\right\}.
\]

In particular its dimension is \(M-1>0\). If the bank contains only the
\(E_a\)-columns, the same proof gives the even-weight subspace of
\(\mathbb F_2^M\).

## Exact root image

Let an ordinary signed dependency select the even set \(S\), and write

\[
 k=|S|,
 \qquad
 X=\prod_{a\in S}r_a,
 \qquad
 Y=\prod_{a\in S}a.
\]

Every factor \(a\) is a unit modulo \(N\), so \(Y\) is a unit. The exact
formula \(r_a=as\) gives the integer equality

\[
 X=s^kY.
\]

Since \(s^2\equiv-1\pmod N\) and \(k\) is even,

\[
 XY^{-1}\equiv s^k=(-1)^{k/2}\in\{1,-1\}\pmod N.
\]

It follows at once that \(X^2\equiv Y^2\pmod N\). If the displayed ratio is
\(1\), then

\[
 \gcd(X-Y,N)=N,
 \qquad
 \gcd(X+Y,N)=1,
\]

because \(N\) is odd and \(Y\) is a unit. If the ratio is \(-1\), the two
values are reversed. Thus every dependency maps to a global square root and
the standard congruent-squares step never returns a nontrivial divisor.

In a sign-free treatment the unsigned \(E_a=a^2\) columns are all zero
parity columns. If such a treatment accepts an odd set \(S\), then instead

\[
 X^2\equiv-Y^2\pmod N,
 \qquad
 XY^{-1}=s^k\equiv(-1)^{(k-1)/2}s\pmod N.
\]

Thus the output is one of the two public roots \(\pm s\) of \(-1\), not a
second root of \(1\). The value \(s=\lfloor\sqrt N\rfloor\) is computable
from \(N\). The possible global sign supplies no new information and does
not give a congruent-squares factorization.

## Size bounds

The chosen prime intervals give, uniformly in \(a\),

\[
 M+a+2<\log_2\ell_a<M+a+3.
\]

Therefore

\[
 \sum_{a=1}^M\log_2\ell_a=\Theta(M^2).
\]

On the other hand,

\[
 \log_2 C
 =1+\sum_{a=1}^M\bigl(\log_2a+\log_2(a^2+1)\bigr)
 =O(M\log(M+1)).
\]

It follows that

\[
 \log_2B=\Theta(M^2).
\]

The selected divisor \(q\) satisfies \(q\leq B^2+1\), while the selected
representative satisfies

\[
 Bq\leq s<2Bq.
\]

Consequently

\[
 \log_2s=\Theta(M^2).
\]

Indeed the lower bound follows from \(s\geq B\), and the upper bound follows
from \(s<2B(B^2+1)\). Since

\[
 n=\left\lceil\log_2(s^2+2)\right\rceil
   =2\log_2s+O(1),
\]

this construction actually gives the stronger estimate

\[
 n=\Theta(M^2).
\]

In particular it gives exactly the stated, weaker bounds

\[
 \Omega(M^2)\leq n\leq O(M^2\log(M+1)),
\]

with absolute constants independent of \(M\). It also directly yields
\(M=\Theta(n^{1/2})\), and hence \(M=n^{1/2+o(1)}\). More generally, the two
bounds printed in the statement alone imply

\[
 \sqrt{\frac{n}{O(\log n)}}\leq M\leq O(\sqrt n),
\]

which also gives \(\log M/\log n\to1/2\).

There are \(2M\) columns, so the full bank is polynomial in \(n\). For
positive integers write \(\operatorname{bits}(x)=\lfloor\log_2x\rfloor+1\).
Then

\[
 \operatorname{bits}(E_a)=\operatorname{bits}(a^2)=O(\log M).
\]

Uniformly for \(1\leq a\leq M\),

\[
 as<F_a<2as+1\leq3Ms.
\]

Together with \(n/2=\log_2s+O(1)\), this proves

\[
 \operatorname{bits}(F_a)
 =\frac n2+O(\log M)
 =\left(\frac12+o(1)\right)n
\]

uniformly in \(a\). The last equality uses \(\log M=o(n)\).

## The public \(N\)-only subbank

Set

\[
 K=\lfloor n^{1/3}\rfloor.
\]

This number is computed from the public input \(N\) alone. From the stated
upper size bound,

\[
 \frac{n^{1/3}}M
 \leq O\!\left(\frac{\log(M+1)}M\right)^{1/3}
 \longrightarrow0.
\]

(For the explicit construction above, the stronger bound is
\(n^{1/3}/M=O(M^{-1/3})\).) Hence \(K\leq M\) for all sufficiently large
\(M\).

For every such \(M\), the algorithmically specified indices
\(1\leq a\leq K\) are therefore a prefix of the constructed bank. Restricting
columns cannot destroy any private-row assertion: for each retained
\(F_a\), its \(\ell_a\)-row still occurs in exactly that column. Repeating
the kernel proof on the prefix gives exactly

\[
 \left\{(x_1,0,\ldots,x_K,0):
   \sum_{a=1}^Kx_a=0\right\},
\]

and repeating the root calculation gives only \(\pm1\). The corresponding
claim for an \(E\)-only prefix also follows unchanged. Thus neither the
choice of the prefix nor the generation of its norms requires knowledge of
the hidden construction parameter \(M\).

## Recursive accounting

The norm bounds make every recursive factorization input a fixed-ratio
child for all sufficiently large \(M\). The \(E_a\)'s have \(o(n)\) bits,
and all \(F_a\)'s have \((1/2+o(1))n\) bits uniformly. Hence, for example,
all children have at most \(2n/3\) bits once \(M\) is sufficiently large.
There are only \(2M=\operatorname{poly}(n)\) of them. Complete recursive
factorization of every child is therefore a polynomial-sized collection of
fixed-ratio recursive calls.

For completeness, the recurrence assertion cited in the statement can be
proved directly. Suppose a size-\(m\) node makes at most

\[
 A(m)=2^{O((\log(m+1))^k)}
\]

calls, each of size at most \(\rho m\) for one fixed \(\rho<1\), and has at
most the same order of local work. Taking a monotone worst-case envelope
gives

\[
 T(m)\leq A(m)\bigl(1+T(\lceil\rho m\rceil)\bigr).
\]

There are \(O(\log m)\) fixed-ratio levels. Iteration yields

\[
 \log_2T(m)
 \leq O\!\left(
   \sum_{j=0}^{O(\log m)}
   (\log(m\rho^j+1))^k
 \right)
 =O((\log(m+1))^{k+1}).
\]

Thus \(T\) is still numerical quasipolynomial. A polynomial call count is
the special case \(k=1\).

If an outer construction additionally has one nonbranching one-bit
decrement call, unroll that single spine first. A recurrence of the form

\[
 T(m)\leq T(m-1)+A(m)\bigl(1+T(\lceil\rho m\rceil)\bigr)
\]

becomes, after at most \(m\) spine steps,

\[
 T(m)\leq T(m_0)+mA(m)
 \bigl(1+\max_{j\leq\rho m}T(j)\bigr).
\]

The factor \(mA(m)\) is still numerical quasipolynomial, so the preceding
fixed-ratio argument applies. This verifies the recursive-accounting claim
without relying on the content of the cited P183 result.

## Consequence and exact scope

The construction supplies, simultaneously:

1. a polynomial number of norms smaller than \(N\);
2. fixed-ratio bit sizes suitable for complete recursive factorization;
3. parity nullity \(M-1>0\); and
4. an exact proof that the image of every parity dependency is contained in
   the two global roots \(\{1,-1\}\).

Therefore cardinality, smaller child size, complete knowledge of every prime
valuation, and positive parity nullity do not force a useful non-global
square root. Polynomial size is numerical quasipolynomial size because
\(n^c=2^{c\log_2n}\).

Nothing in the construction establishes an obstruction for all inputs, for
semiprimes, or for balanced semiprimes. It does not constrain nonlinear,
Archimedean, adaptive, or other non-parity uses of the factored \(F_a\)'s.
The private-row proof applies only to the constructed range \(a\leq M\)
(and its subbanks), so it says nothing about a larger extension. Nor does
one constructed polynomial schedule rule out a different all-input
quasipolynomial schedule supported by additional arithmetic structure.
These are exactly limitations of the proved mechanism, not missing steps in
the parity obstruction.

## Verdict

Every mathematical assertion in the frozen statement follows from the
construction and arguments above. The construction in fact attains
\(n=\Theta(M^2)\), which is stronger than the stated size window. The
sign-free odd-subset sentence is exact up to the immaterial public global
sign: the computed root is \((-1)^{(k-1)/2}s\), hence one of \(\pm s\).
