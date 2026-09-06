# Proof of F229

## 1. One fixed prime gap

The bounded-prime-gap theorem supplies a constant \(D\) and infinitely many
consecutive prime pairs whose gap is at most \(D\). Only finitely many even
positive gaps are at most \(D\). One fixed even gap \(d\ge2\) therefore
occurs for infinitely many prime pairs. Fix it once and write

\[
q=p+d,
\qquad
N=pq.
\tag{1.1}
\]

For all sufficiently large pairs, \(q<2p\). Also

\[
\log _2N
=2\log _2p+\log _2(1+d/p)
=2\log _2p+o(1),
\tag{1.2}
\]

which proves the uniform relation (0.4), including the ceiling in the
definition of \(n\).

## 2. Exponent reduction in both fields

Let \(X\) be coprime to \(N\). Modulo \(p-1\),

\[
N-1=pq-1\equiv q-1=d\pmod {p-1},
\tag{2.1}
\]

because \(p\equiv1\pmod {p-1}\) and \(q=p+d\). Hence

\[
X^{N-1}\equiv X^d\pmod p.
\tag{2.2}
\]

Modulo \(q-1\),

\[
N-1=pq-1\equiv p-1=q-d-1\equiv-d\pmod {q-1}.
\tag{2.3}
\]

Since \(X\) is a unit modulo \(q\),

\[
X^{N-1}\equiv X^{-d}\pmod q,
\tag{2.4}
\]

and

\[
X^{-d}-1=-X^{-d}(X^d-1).
\tag{2.5}
\]

The multiplier in (2.5) is a unit. Thus \(p\) divides
\(X^{N-1}-1\) exactly when it divides \(X^d-1\), and the same equivalence
holds for \(q\). Since \(N=pq\) is squarefree, the two gcds have exactly the
same prime divisors with exponent one. This proves (A.1).

If the gcd is \(N\), the order of \(X\) in each hidden field divides \(d\).
Let \(\ell^e\parallel A\) be a primary power certified by the P197 test

\[
\gcd(X^{A/\ell}-1,N)=1.
\tag{2.6}
\]

That test says that both local orders have \(\ell\)-valuation exactly \(e\).
Since both orders divide \(d\), one has \(\ell^e\mid d\). Every certified
block is a product of such powers, so it divides \(d\). Lcm accumulation
preserves this divisibility. If factor-first stripping instead terminates
with one exact common order, that order equals both local orders and also
divides \(d\).

If \(\gcd(X,N)\) is proper, the initial screen has already returned a
factor. If the gcd is \(N\), \(X\) is not a unit and (0.5) is outside the
declared unit stage. Finally, \(X=1\) has order one in both fields. These
observations prove all edge cases in Theorem A.

## 3. Numerical-QP height is subexponential in \(p\)

For a fixed numerical-QP function \(H\),

\[
\log _2H(n)=O((\log n)^k)=o(n).
\tag{3.1}
\]

Equation (1.2) gives \(\log _2p=n/2+O(1)\). Since \(d\) is one fixed
integer,

\[
d\log _2H(n)=o(n)<\log _2p
\tag{3.2}
\]

eventually. This is (B.1).

For \(2\le X\le H\), one has

\[
1<X^d\le H^d<p.
\tag{3.3}
\]

Therefore \(0<X^d-1<p<q\), so neither hidden prime divides \(X^d-1\).
Also \(X<p\), so \(X\) is a unit modulo \(N\). Theorem A now gives
\(G_A(X)=1\), proving (B.2) and the history-wise zero law. Zero and one
behave as stated in Theorem A.

For a word (B.3), its total log-height is \(\log _2X\). Condition (B.4)
is exactly \(X^d<p\), so the same argument applies. Equation (1.2) converts
the first possible escape threshold to (B.5).

## 4. Uniform interval root counting

Fix \(H\ge2\) and sample uniformly from

\[
I_H=\{2,\ldots,H\},
\qquad |I_H|=H-1.
\tag{4.1}
\]

If \(H^d<p\), Section 3 gives useful probability zero.

Assume now \(H^d\ge p\), so

\[
H\ge p^{1/d}.
\tag{4.2}
\]

The number of multiples of \(p\) in \(I_H\) is at most \(H/p\), and the
number of multiples of \(q\) is at most \(H/q\). Their intersection only
makes the union bound looser. Since \(H/(H-1)\le2\), the initial proper-gcd
probability is at most

\[
2\left(\frac1p+\frac1q\right)\le\frac4p.
\tag{4.3}
\]

The polynomial \(T^d-1\) has at most \(d\) roots in either prime field.
Every residue class modulo \(p\) occurs in \(I_H\) at most \(H/p+1\)
times. Therefore

\[
\Pr(p\mid X^d-1)
\le
\frac{d(H/p+1)}{H-1}
\le\frac{2d}{p}+\frac{2d}{H}.
\tag{4.4}
\]

The same argument modulo \(q\) gives

\[
\Pr(q\mid X^d-1)
\le\frac{2d}{q}+\frac{2d}{H}.
\tag{4.5}
\]

Every useful outcome not already counted by the initial gcd requires a
return in at least one hidden field. Combining (4.3)--(4.5), and using
\(q>p\), gives

\[
\Pr(\text{useful})
\le
\frac{4+4d}{p}+\frac{4d}{H}.
\tag{4.6}
\]

By (4.2), \(H^{-1}\le p^{-1/d}\). Also \(p^{-1}\le p^{-1/d}\).
This proves (C.1). Equation (1.2) turns it into (C.2), with constants
depending only on the one fixed \(d\).

If a history selects \(H\) before drawing the fresh conditional uniform
integer, the same bound applies conditionally. A union bound over any one
fixed numerical-QP number of stages preserves \(2^{-\Omega(n)}\), because
the logarithm of the trial count is \(o(n)\). No independence between
different stages is needed.

## 5. Projection of a uniform subgroup element

Choose \(B\) as in (D.1). Since \(\log B=o(n)\) while
\(\log p=\Theta(n)\), eventually \(B<p<q\). Thus every rational prime
generator in (D.3) is a unit modulo \(N\).

Projection modulo \(p\) maps \(\mathcal G_N(B)\) surjectively onto
\(\mathcal G_p(B)\). Every fibre of a surjective homomorphism between finite
groups is a coset of its kernel and has the same size. Hence an exact uniform
element of \(\mathcal G_N(B)\) has an exact uniform projection in
\(\mathcal G_p(B)\). The two projections may be arbitrarily correlated;
their joint law is not used.

The group \(\mathbb F_p^\times\) is cyclic, so its subgroup
\(\mathcal G_p(B)\) is cyclic. A cyclic group of size \(m\) has exactly
\(\gcd(d,m)\) solutions to \(x^d=1\). Section 2 therefore gives the exact
first equality in (D.4). The proof for \(q\) is identical, using
\(x^{-d}=1\iff x^d=1\).

## 6. Small-prime subgroup size from smooth integers

Every positive \(B\)-smooth integer \(u<p\) is a product of the rational
prime generators in (D.3), so its residue lies in \(\mathcal G_p(B)\).
Distinct integers in \([1,p-1]\) give distinct residues. Because \(p>B\),
the integer \(p\) itself is not \(B\)-smooth. Consequently all
\(\Psi(p,B)\) positive \(B\)-smooth integers at most \(p\) lie in
\([1,p-1]\), and

\[
|\mathcal G_p(B)|\ge\Psi(p,B).
\tag{6.1}
\]

The argument for \(q\) is the same.

The smooth-number estimate already used in P172 is

\[
\log\Psi(x,B)
\ge
\log x-\frac{\log x}{\log B}\log\log x
\tag{6.2}
\]

in the present range, for all sufficiently large \(x\). Here
\(\log\log p=\Theta(\log n)=o(\log B)\), and similarly for \(q\).
Thus (6.2) gives

\[
\log\Psi(p,B)=(1-o(1))\log p,
\qquad
\log\Psi(q,B)=(1-o(1))\log q.
\tag{6.3}
\]

This proves (D.5)--(D.6).

A proper return or global return is contained in the union of the two local
return events. Apply (D.4), its \(q\)-analogue, and (D.5) to obtain (D.7).
Equation (1.2) gives its input-length form. Conditional exact uniformity at
each later history permits the same conditional union bound as in Section 4.
The lcm-capacity assertion is Theorem A.

## 7. Exact word/carry boundary

For every positive integer word value \(X\), Theorem A replaces the large
annihilator calculation, as far as divisibility by \(p\) and \(q\) is
concerned, by

\[
C_X=X^d-1.
\tag{7.1}
\]

If \(X>1\) and \(C_X<p\), neither hidden prime divides it. If exactly one
hidden prime divides it, then (E.2) holds with a positive integer quotient.
If both divide it, squarefreeness gives \(N\mid C_X\), which is (E.3).
The size thresholds in Theorem B follow immediately.

Theorem D shows that forgetting the word and mixing uniformly over the
entire generated subgroup makes the relevant \(d\)-torsion exponentially
sparse. Therefore the only unclosed regime is a long, deliberately
nonuniform word distribution whose modular wrap is correlated with the union
of the two local \(d\)-torsion sets in a factor- or new-block-producing
configuration. This is an exact boundary statement, not an assertion that
such a law is impossible.
