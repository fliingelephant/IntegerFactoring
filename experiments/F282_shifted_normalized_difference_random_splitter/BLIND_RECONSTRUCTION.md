# F282 blind reconstruction

## Authentication and method

Before this reconstruction, the SHA-256 digest computed for STATEMENT.md was

\[
831ac1a429968a20fdeffa2e0c0e7d1972fe43deec3a22e43ee4b71a2d01f0bf,
\]

which is the required digest. This reconstruction used only that authenticated
statement. It used no other F282 artifact, numerical search, empirical data, or
remote resource.

## Verdict

**PASS.** Every mathematical and algorithmic claim in the authenticated
statement follows. The factorer is conditional on the stated public modular
evaluator. Nothing here constructs that evaluator or extends the promise.

## 1. The unresolved branch

Because \(p<q\),

\[
p<\sqrt{pq}<q.
\]

Thus \(p\le B<q\). Also \(B<q<2p\), so the only positive multiple of either
prime that \(B\) could equal is \(p\). If \(B=p\), then
\(\gcd(B,N)=p\), and the public screen succeeds. On the remaining branch,
\(B>p\). Define

\[
s=B-p,\qquad h=q-B.
\]

Then \(s,h\) are positive integers and

\[
B=p+s,\qquad q=B+h.
\]

The integer \(N=pq\) is not a square because \(p\ne q\). Hence \(B^2<N\).
Substitution gives

\[
(B-s)(B+h)>B^2
\quad\Longrightarrow\quad
B(h-s)>sh.
\]

As \(s,h>0\), this forces \(h>s\). The difference

\[
h-s\equiv h+s=q-p\equiv0\pmod 2
\]

is even because \(p\) and \(q\) are odd. Therefore \(h-s\ge2\), or

\[
h\ge s+2.
\]

Finally, \(q<2p\) gives

\[
p+s+h<2p,\qquad s+h<p.
\]

Together with \(h\ge s+2\), this yields \(2s+2<p\), and therefore

\[
p\ge2s+3.
\]

All three bounds remain valid at their possible endpoints. In particular, if
\(h=s+2\), the parity argument is exact; if \(p=2s+3\), the last inequality is
an equality after integer rounding.

## 2. Exact divided-difference identity

For any polynomial \(f\), its divided difference on the consecutive integer
nodes \(a,a+1,\ldots,a+B\) is

\[
\begin{aligned}
f[a,a+1,\ldots,a+B]
&=\sum_{j=0}^{B}
 \frac{f(a+j)}
 {\prod_{0\le i\le B,\ i\ne j}(j-i)}\\
&=\frac1{B!}\sum_{j=0}^{B}
 (-1)^{B-j}\binom Bj f(a+j)\\
&=\frac{\Delta^B f(a)}{B!}.
\end{aligned}
\]

For indeterminates \(x_0,\ldots,x_B\), the standard monomial
divided-difference identity is

\[
X^m[x_0,\ldots,x_B]=h_{m-B}(x_0,\ldots,x_B)
\qquad(m\ge B).
\]

One direct proof is to sum the Lagrange formula over \(m\): its generating
function is

\[
\sum_{m\ge0}
\left(\sum_{j=0}^{B}
\frac{x_j^m}{\prod_{i\ne j}(x_j-x_i)}\right)z^m
=\frac{z^B}{\prod_{j=0}^{B}(1-x_jz)}.
\]

Comparison with

\[
\sum_{d\ge0}h_d(x_0,\ldots,x_B)z^d
=\frac1{\prod_{j=0}^{B}(1-x_jz)}
\]

proves the identity. Applying it with \(m=2B\) and \(x_j=a+j\) gives

\[
\frac{\Delta^B X^{2B}|_{X=a}}{B!}
=h_B(a,a+1,\ldots,a+B).
\]

The right side belongs to \(\mathbb Z[a]\). It follows at once that the
division by \(B!\) is exact for every integer \(a\), without interpreting
\(B!\) as a modular denominator.

## 3. A finite-field product identity

For either odd prime \(r\), work in \(\mathbb F_r[[z]]\). The factorization
of \(X^{r-1}-1\) over \(\mathbb F_r^\times\) gives

\[
\prod_{x\in\mathbb F_r}(1-xz)=1-z^{r-1}.
\tag{A}
\]

The factor belonging to \(x=0\) is simply \(1\). Thus (A) and every use of
it below require no inverse of a field element that might be zero.

For any finite multiset \(S\) in the field,

\[
\sum_{d\ge0}h_d(S)z^d
=\prod_{x\in S}(1-xz)^{-1}.
\tag{B}
\]

All inverses in (B) are formal power-series inverses of polynomials with
constant term \(1\).

## 4. The \(q\)-local zero

Modulo \(q\), the \(B+1\) residues

\[
S_q=\{\bar a,\bar a+1,\ldots,\bar a+B\}
\]

are distinct because \(B<q\). They can wrap around and can include zero;
neither fact changes the argument. Their complement \(T_q\) in
\(\mathbb F_q\) has

\[
q-(B+1)=h-1
\]

elements. Equations (A) and (B) give

\[
\sum_{d\ge0}h_d(S_q)z^d
=\frac{\prod_{x\in T_q}(1-xz)}{1-z^{q-1}}.
\tag{C}
\]

Here \(h\ge s+2\ge3\), so

\[
B=q-h<q-1.
\]

Also \(s+h<p\), hence

\[
\deg\prod_{x\in T_q}(1-xz)\le h-1<B=p+s.
\]

If \(T_q\) contains zero, the numerator degree only decreases. Since
\((1-z^{q-1})^{-1}=1+z^{q-1}+\cdots\), the coefficient of \(z^B\) in
(C) is zero. Therefore

\[
F_B(a)=h_B(S_q)\equiv0\pmod q
\]

for every integer \(a\).

## 5. The short \(p\)-local formula

Since \(B=p+s\), reduction of the multiset

\[
a,a+1,\ldots,a+B
\]

modulo \(p\) consists of one complete block \(\mathbb F_p\), followed by
the additional multiset

\[
R=\{\bar a,\bar a+1,\ldots,\bar a+s\}.
\]

The elements of \(R\) are distinct because \(s<p\), although they of course
duplicate elements already present in the complete block. From (A) and
(B),

\[
\sum_{d\ge0}h_d(a,a+1,\ldots,a+B)z^d
=\frac{1}{1-z^{p-1}}
 \sum_{d\ge0}h_d(R)z^d.
\]

The product on the right means

\[
\frac{1}{1-z^{p-1}}
\left(\sum_{d\ge0}h_d(R)z^d\right).
\tag{D}
\]

Because

\[
p-1<p+s<2(p-1),
\]

where the second inequality follows from \(p\ge2s+3\), only the powers
\(1\) and \(z^{p-1}\) from
\((1-z^{p-1})^{-1}\) contribute to degree \(p+s\). Thus (D) yields

\[
F_B(a)\equiv h_{p+s}(R)+h_{s+1}(R)\pmod p.
\tag{E}
\]

Write the elements of \(R\) as \(x_i=\bar a+i\), \(0\le i\le s\). For
pairwise distinct nodes, the monomial divided-difference identity from
Section 2 gives

\[
h_d(x_0,\ldots,x_s)
=\sum_{i=0}^{s}
\frac{x_i^{d+s}}{\prod_{j\ne i}(x_i-x_j)}.
\tag{F}
\]

Only node differences are inverted in (F), and
\(x_i-x_j=i-j\ne0\) in \(\mathbb F_p\). A node \(x_i\) itself may be
zero. Since Frobenius gives \(x_i^p=x_i\), including at zero,

\[
x_i^{p+2s}=x_i^{2s}x_i^p=x_i^{2s+1}.
\]

Using (F) first with \(d=p+s\) and then with \(d=s+1\) proves

\[
h_{p+s}(R)=h_{s+1}(R).
\]

Substitution in (E) gives the claimed short law

\[
F_B(a)\equiv2h_{s+1}(a,a+1,\ldots,a+s)\pmod p.
\]

This proof does not use the invalid zero-sensitive replacement
\(x_i^{p-1}=1\). It therefore covers every shift for which one of the short
nodes is zero.

## 6. Degree, leading coefficient, and roots

The polynomial \(h_{s+1}\) in \(s+1\) variables is the sum of one monomial
for each weak composition of \(s+1\) into \(s+1\) parts. After substituting
\(x_i=a+i\), each such monomial contributes \(1\) to the coefficient of
\(a^{s+1}\). The number of these compositions is

\[
\binom{(s+1)+(s+1)-1}{(s+1)-1}
=\binom{2s+1}{s}.
\]

Therefore the leading coefficient of the local polynomial is

\[
2\binom{2s+1}{s}.
\]

The bound \(p\ge2s+3\) gives \(2s+1<p\). Hence none of the factorials in

\[
\binom{2s+1}{s}=\frac{(2s+1)!}{s!(s+1)!}
\]

contains a factor \(p\). The binomial coefficient is nonzero in
\(\mathbb F_p\), and so is \(2\) because \(p\) is odd. The polynomial
therefore has exact degree \(s+1\), including at the endpoint
\(p=2s+3\). A nonzero polynomial of this degree over a field has at most
\(s+1\) roots in \(\mathbb F_p\).

## 7. Split probability and Las Vegas behavior

A uniform residue \(a\bmod N\) induces a uniform residue modulo \(p\).
The \(q\)-local law shows that \(q\mid F_B(a)\) on every trial. Outside at
most \(s+1\) classes modulo \(p\), the root bound shows that
\(p\nmid F_B(a)\). On those classes,

\[
\gcd(F_B(a),N)=q.
\]

Consequently,

\[
\Pr[d=q]\ge1-\frac{s+1}{p}.
\]

The endpoint inequality \(p\ge2s+3\) gives

\[
1-\frac{s+1}{p}
=\frac{p-s-1}{p}
\ge\frac{p+1}{2p}
>\frac12.
\]

Equality in the middle is possible when \(p=2s+3\), so the endpoint is
fully covered.

If a trial is not successful, then \(p\mid F_B(a)\) as well as
\(q\mid F_B(a)\). Since \(N=pq\), its gcd is then \(N\). Thus no trial
returns \(1\) or the wrong proper divisor. Independent repetition has a
geometric waiting time with

\[
\mathbb E[T]\le\frac{2p}{p+1}<2.
\]

The algorithm checks \(1<d<N\) before output. It therefore never outputs
an unverified answer and is Las Vegas on the stated promise.

## 8. Conditional complexity consequence

The public operations outside the assumed evaluator have polynomial bit
complexity in

\[
n=\lceil\log_2(N+1)\rceil.
\]

They are exact integer square root, gcd, comparison, and random sampling.
For example, exact uniform sampling modulo \(N\) follows by drawing an
\(n\)-bit integer and rejecting values at least \(N\). Since
\(N\ge2^{n-1}\), its expected number of draws is at most two.

Assume the stated single uniform classical algorithm evaluates
\(F_{\lfloor\sqrt N\rfloor}(a)\bmod N\) from only \((N,a)\) in
numerical-quasipolynomial bit complexity. Compose it with the public
\(\gcd(B,N)\) screen and the repeated trials above. The expected number of
evaluator calls is less than two, and all other work is polynomial.
Therefore the composition is a uniform classical Las Vegas
numerical-quasipolynomial factorer for balanced products of two distinct odd
primes. No factor, hidden parameter, field decomposition, or nonunit inverse
is supplied at this interface. The conclusion depends essentially on the
evaluator assumption.

Even-factor removal, exact primality recognition, and perfect-power
reduction are separate standard preprocessing operations. They do not imply
that every remaining composite is a balanced product of two distinct odd
primes. In particular, they do not establish the stated local laws for an
unbalanced semiprime, a repeated-prime semiprime, or an integer with at
least three prime factors.

## 9. Evaluator boundary

The literal formula is

\[
\Delta^B X^{2B}|_{X=a}
=\sum_{j=0}^{B}(-1)^{B-j}\binom Bj(a+j)^{2B},
\]

so it explicitly has \(B+1\) terms before the exact division by \(B!\).
On the unresolved branch,

\[
p<B<q<2p.
\]

The factorial \(B!\) therefore contains the multiple \(p\) exactly once
and contains no multiple of \(q\). Hence

\[
\gcd(B!,N)=p,
\]

and \(B!\) has no inverse modulo \(N\).

Moreover,

\[
\Delta^B X^{2B}|_{X=a}=B!F_B(a).
\]

The first factor is divisible by \(p\), and the second is always divisible
by \(q\). Thus the raw difference is zero modulo \(N\) for every shift.
Reduction of the raw numerator modulo \(N\), followed by modular division,
cannot recover the normalized residue because the required denominator is
a nonunit. On successful shifts, the useful gcd-\(q\) residue becomes
visible only after the exact factor-bearing normalization.

The size obstruction for direct exact materialization is also explicit.
At \(a=0\),

\[
F_B(0)=h_B(0,1,\ldots,B).
\]

The monomial \(B^B\) gives the lower bound \(F_B(0)\ge B^B\). There are
\(\binom{2B}{B}\le4^B\) degree-\(B\) monomials, each at most \(B^B\), so

\[
B^B\le F_B(0)\le4^B B^B.
\]

Its bit length is therefore \(\Theta(B\log B)\). The standard
complete-homogeneous dynamic recurrence also explicitly retains degrees
through \(B\), so its named representation has characteristic range
\(\Theta(B)\).

Finally,

\[
2^{n-1}<N+1\le2^n
\]

implies \(B=\lfloor\sqrt N\rfloor=2^{\Theta(n)}\). Hence enumerating
\(B+1\) terms, traversing a degree range of length \(B\), or exactly
materializing the displayed value is not numerical-quasipolynomial in
\(n\).

These observations apply only to the literal forward-difference
representation, the standard recurrence, and exact materialization. They
are not lower bounds for arithmetic circuits or for all uniform succinct
modular algorithms. A different evaluator could in principle avoid these
representations.

## 10. Exact scope

The reconstruction proves no construction of the assumed evaluator and
hence no unconditional factorer, even on the promise. It supplies no
reduction from arbitrary composite inputs to the promise. It says nothing
that resolves the F281 central joint-saturation conjecture. Its
representation-specific cost calculations are not evaluator lower bounds.
It contains no empirical claim or evidence.

## Final audit

- The least allowed shift width \(s=1\) causes no exceptional exponent or
  denominator.
- The endpoints \(h=s+2\) and \(p=2s+3\) preserve every strict coefficient
  range needed in the two local generating functions.
- Wrap-around modulo either prime does not merge nodes in the short sets:
  \(B<q\) and \(s<p\).
- A zero node is harmless. Full-field products include it as the factor
  \(1\), and the only Lagrange denominators used are nonzero node
  differences.
- The success bound is uniform in \(a\) and does not assume that the
  degree-\(s+1\) polynomial attains its maximum possible number of roots.

The authenticated statement is therefore verified as written, with its
conditional evaluator hypothesis and exact exclusions intact.
