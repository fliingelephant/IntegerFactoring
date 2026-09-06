# F146 V2 blind reconstruction

## Scope and verdict

I read only `V2_STATEMENT.md` in the F146 directory. Its SHA-256 is

```text
886ca7aafa5d5cd42514fa4fbd6223a9e7ca12a368820a8c53b9731b3553ac57
```

This matches the supplied hash. I used no search, computer algebra, or
numerical experiment.

**Verdict: verified.** The exchange criterion, the distinction between
arbitrary composite and squarefree moduli, the scan bound, the
near-threshold estimate, and the delayed-mismatch construction all admit
independent proofs. The P11 integer count and probability formulas also
check. The four quoted decimal expectations cannot be independently
recomputed from this statement alone because the two P11 primes are not
given; they are evaluations of the verified formulas, not inputs to the
theorem.

## 1. Exchange normal form

Work over \(R=\mathbb Z/N\mathbb Z\). Since \(\det B\) is a unit, \(B\) is
invertible and left multiplication by \(B^{-1}\) takes

\[
M_N=[B\mid T]
\quad\hbox{to}\quad
[I_A\mid C],\qquad C=B^{-1}T.
\]

Choose \(k\) tail columns \(J\) and delete the \(k\) base columns \(I\).
After row and column permutations, expansion along the unchanged identity
columns gives

\[
\det [I_A\mid C]_{([A]\setminus I)\cup J}
   =\varepsilon(I,J)\det C[I,J].
\]

Undoing the left multiplication gives

\[
\det E_{I,J}
 =\varepsilon(I,J)\det(B)\det C[I,J].
\]

Multiplication by \(\pm\det B\) does not change a gcd with \(N\). Thus the
gcd scan on exchanged maximal minors is exactly the gcd scan on the square
minors of \(C\). The empty exchange has determinant \(1\), so including
\(k=0\) never creates a success.

## 2. The two radii

Let \(x\) be an integer representative of one minor of \(C\).

If \(x\equiv0\pmod\ell\) for some but not all distinct primes
\(\ell\mid N\), then at least one prime divides \(\gcd(x,N)\) and at least
one prime divisor of \(N\) does not. Hence

\[
1<\gcd(x,N)<N.
\]

This proves that every local-field disagreement is a gcd success. Taking
the first support at which either event occurs gives

\[
\gamma_B\le\delta_B
\]

for every composite \(N\), with the usual extended ordering when one radius
is infinite. It also proves the stated sufficiency of
\(\delta_B\le s\). The equivalence between scan success and
\(\gamma_B\le s\) follows directly from the exchange normal form.

If \(N\) is squarefree, write \(N=\prod_{\ell\mid N}\ell\). Then

\[
1<\gcd(x,N)<N
\]

holds exactly when the set of primes dividing \(x\) is a nonempty proper
subset of the primes dividing \(N\). This is exactly the local-field
disagreement condition. The qualifying supports are therefore identical,
so

\[
\gamma_B=\delta_B.
\]

Squarefreeness is necessary for this converse. For example, take
\(N=9\), \(B=[1]\), and \(C=[3]\). The one-exchange determinant has gcd
\(3\) with \(9\), so \(\gamma_B=1\). There is only one distinct prime
divisor, and the determinant is zero in that field, so no minor can be zero
for some but not all prime divisors. Thus \(\delta_B=\infty\). This is a
valuation-only split.

## 3. Exact scan count and cost

At support \(k\), an exchange is determined uniquely by the omitted base
set \(I\) and included tail set \(J\). There are

\[
\binom Ak\binom tk
\]

such pairs. Therefore

\[
Q_s(A,t)=\sum_{k=0}^{\min(s,A,t)}\binom Ak\binom tk.
\]

For \(At\ge1\), each summand satisfies

\[
\binom Ak\binom tk\le A^kt^k=(At)^k\le(At)^s,
\]

and there are at most \(s+1\) summands. If \(At=0\), only the \(k=0\)
term survives. Both cases give

\[
Q_s(A,t)\le(s+1)\max\{1,At\}^{s}.
\]

In particular, \(t=0\) gives \(Q_s(A,0)=1\), not zero.

Suppose \(A,r\le n^c\) for a fixed \(c\). Then \(t\le r\le n^c\), and

\[
\log_2 Q_s(A,t)
 \le O(\log(s+1))+s\,O(\log(n+1)).
\]

For \(s\le(\log(n+1))^d\), this is

\[
O((\log(n+1))^{d+1}).
\]

Computing \(C\) is polynomial-time because \(B\) is invertible. Each
candidate needs a determinant of order at most \(s\) over
\(\mathbb Z/N\mathbb Z\) and one integer gcd. Division-free determinant
algorithms and the Euclidean algorithm make this polynomial in \(A,s,n\)
per candidate. Polynomial preprocessing and per-candidate work are absorbed
by the same exponential bound. Hence the total bit complexity is

\[
2^{O((\log(n+1))^{d+1})}.
\]

Every maximal minor contains some \(k\le\min(A,t)\) tail columns and omits
the same number of base columns. Thus radius \(t\) includes every maximal
minor. If \(t\le(\log(n+1))^d\), the complete scan has the stated
quasipolynomial cost.

The reductions modulo primes dividing \(N\) all have rank \(A\), since they
all contain the base \(B\). Rank-\(A\) matroids are determined by their
bases, and their bases are exactly the nonzero maximal minors. The complete
scan therefore detects every difference among the local column matroids.
For squarefree \(N\), Section 2 makes this equivalent to gcd success. For a
nonsquarefree \(N\), gcd success can additionally arise from a valuation
split that no residue-field matroid records.

## 4. Near-threshold prime modulus

Put

\[
D=r-1-L^2,
\qquad 0<D\le(\log(n+1))^d.
\]

Since \(D>0\),

\[
L\sqrt{r-1}>L^2.
\]

For every real \(y\), \(\lfloor y\rfloor>y-1\). Hence

\[
A=\lfloor L\sqrt{r-1}\rfloor>L^2-1.
\]

It follows that

\[
\begin{aligned}
r-A
 &=L^2+D+1-A\\
 &<D+2\\
 &\le(\log(n+1))^d+2.
\end{aligned}
\]

Also \(L<\sqrt{r-1}\), so \(L\sqrt{r-1}<r-1\) and \(A<r\), as required
for a positive tail. The integral tail size is therefore
\(O((\log(n+1))^d+1)\). Scanning through that radius includes all maximal
minors and remains quasipolynomial. None of these inequalities supplies the
prime modulus, the unit base, or a mismatch, so the conclusion is only a
conditional cost statement.

## 5. A delayed mismatch at exactly \(s+1\)

Fix \(s\ge1\) and put \(m=s+1\). Define the integer \(m\)-by-\(s\)
Vandermonde matrix

\[
U_{ia}=i^a,
\qquad 1\le i\le m,
\quad 0\le a\le s-1,
\]

and set

\[
D=UU^{\mathsf T},
\qquad
D_{ij}=\sum_{a=0}^{s-1}(ij)^a.
\]

For increasing positive nodes and increasing nonnegative exponents, every
square generalized Vandermonde determinant is positive. One way to see this
is its factorization into an ordinary Vandermonde determinant and a Schur
polynomial with nonnegative coefficients.

For row and column sets \(I,J\subseteq[m]\) with
\(|I|=|J|=k\le s\), Cauchy--Binet gives

\[
\det D[I,J]
 =\sum_{K\subseteq\{0,\ldots,s-1\},\ |K|=k}
   \det U[I,K]\det U[J,K].
\]

Every summand is positive, so every such minor is a positive integer.
However, \(\operatorname{rank}D=s<m\), and therefore

\[
\det D=0.
\]

For the other field, use the full \(m\)-by-\(m\) Vandermonde matrix

\[
G_{ij}=i^{j-1},
\qquad 1\le i,j\le m.
\]

Every square minor of \(G\), including its determinant, is a positive
generalized Vandermonde determinant.

It remains to choose primes large enough that reduction does not erase any
of these positive minors. Crude bounds suffice. The entries of \(D\) are at
most \(m^{2s-1}<m^{2m}\), while the entries of \(G\) are at most
\(m^s<m^m\). The Leibniz determinant bound then puts every proper minor of
\(D\), and every minor of \(G\), below

\[
X=m^{4m^2}.
\]

Bertrand's postulate supplies a prime \(q\) with \(X<q<2X\), and then an
odd prime \(p\) with

\[
q<p<2q.
\]

Both primes exceed all of the relevant nonzero integer minors. By entrywise
CRT, choose \(C\in(\mathbb Z/pq\mathbb Z)^{m\times m}\) such that

\[
C\equiv D\pmod q,
\qquad
C\equiv G\pmod p.
\]

For every \(k\le s\), every \(k\)-minor of \(C\) is nonzero modulo both
primes. At size \(m=s+1\),

\[
\det C\equiv0\pmod q,
\qquad
\det C\not\equiv0\pmod p.
\]

Consequently

\[
M_N=[I_m\mid C],\qquad N=pq,
\]

has every exchange through support \(s\) as a basis over both fields, while
the unique exchange of all \(m\) base columns disagrees. Its first local
disagreement is exactly \(s+1\).

The size claim also follows from the prime choice. Since

\[
\log_2 q=\Theta(m^2\log m),
\qquad q<p<2q,
\]

we have

\[
n=\lceil\log_2(pq+1)\rceil
 =\Theta(m^2\log m)
 =\Theta(s^2\log(s+1)).
\]

### Padding

Let \(A'=n^2\). Append \(A'-m\) zero rows to \(C\), call the result
\(C'\), and use the base \(I_{A'}\):

\[
M'_N=[I_{A'}\mid C'].
\]

A minor using a padded row is zero in both fields. A minor using only the
original rows is the corresponding minor of \(C\). Thus padding introduces
common dependencies but no earlier disagreement, while the original
\(m\)-by-\(m\) determinant still disagrees at support \(m\). Hence

\[
A'=n^2,
\qquad
r=A'+m=A'+s+1,
\]

without changing the first disagreement. This proves precisely the padding
claim; it does not claim that every small exchange remains a basis after
zero-row padding.

Finally,

\[
\log(n+1)=\Theta(\log(s+1)).
\]

For every fixed \(d\),
\((\log(n+1))^d=o(s)\). Sufficiently large family members therefore have no
local mismatch in the entire polylogarithmic exchange ball, although the
two full column matroids differ at support \(s+1\). The construction uses
generic representable matrices, not the arithmetic form of an AKS error
matrix, so it is a boundary theorem rather than an AKS counterexample.

## 6. P11 calibration

The exact number of two-exchanges is

\[
\binom{2942}{2}\binom{11}{2}
=4{,}326{,}211\cdot55
=237{,}941{,}605.
\]

A uniformly random \(2\)-by-\(2\) matrix over \(\mathbb F_\ell\) is
invertible with probability

\[
\frac{(\ell^2-1)(\ell^2-\ell)}{\ell^4}
=(1-\ell^{-2})(1-\ell^{-1}).
\]

Its singularity probability is therefore

\[
z_\ell
=1-(1-\ell^{-1})(1-\ell^{-2})
=\ell^{-1}+\ell^{-2}-\ell^{-3}.
\]

If the reductions in fields \(\mathbb F_p\) and \(\mathbb F_q\) are
independent in the comparison model, the expected zero counts among
\(H=237{,}941{,}605\) minors are \(Hz_p\) and \(Hz_q\). The expected number
of zero-pattern mismatches is

\[
H\bigl(z_p(1-z_q)+(1-z_p)z_q\bigr)
=H(z_p+z_q-2z_pz_q).
\]

For one-tail exchanges there are

\[
2942\cdot11=32{,}362
\]

entries. Their zero probability is \(u_\ell=1/\ell\), so the analogous
expected mismatch count is

\[
32{,}362\,(u_p+u_q-2u_pu_q).
\]

These formulas are the claimed independent-random calibration. The quoted
values \(2.3794\), \(1.1897\), \(3.5691\), and \(0.000485\) require the
actual P11 primes, which are not present in the allowed source. The observed
counts \(0,2,2\), and \(0\) are also external data rather than consequences
of the model. Conditional on those inputs, the interpretation is correct:
an observed count of two is on the model's constant expected-count scale,
but an expectation calculation supplies no forcing law and no independence
claim for the AKS matrix.

## 7. Boundary established

The proof separates a generic limitation from the remaining AKS-specific
problem. A growing local radius can miss the first representable-matroid
disagreement even when \(A,r\) are polynomial in the input bit length and
are nearly equal. Therefore a positive F04 result must use extra arithmetic
structure: it must bound \(\gamma_B\) or \(\delta_B\), force a sufficiently
small tail, or replace exhaustive local exchange scanning with another
factor-correlated selector. None of those conclusions follows from the
generic exchange geometry proved here.
