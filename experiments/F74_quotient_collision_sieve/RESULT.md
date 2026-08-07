# F74 — quotient-collision batch feedback

**Status:** corrected proof-only candidate after a failed first hostile audit.
No research computation was run. This note proves an exact polynomial-time
feedback-fibre gate and its quotient-bounded domination boundary. It does not
prove that the gate opens often enough to factor every input.

## 1. Setup

Let \(N\ge 3\). Retain an indexed list of canonical inverse relations

\[
A_i=x_i y_i=1+k_iN,
\qquad
1\le x_i,y_i<N,
\qquad
1\le i\le m.
\]

Equal relation values remain separate occurrences. Put

\[
P=\prod_{i=1}^m A_i=1+KN.
\]

The endpoint presentations are completely refined into a gcd-free integer
block basis. Exact exponents and occurrence capacities are retained. Thus a
divisor of \(P\) can be represented after gcd-free refinement against that
divisor, without factoring an unknown integer.

For an integer \(r\ge1\), define

\[
A_r=1+rN,
\qquad
D_r=\gcd(P,A_r).
\tag{1}
\]

The informative collision values satisfy \(r\ne k_i\) for every \(i\). If
\(r=k_i\), then \(A_r\mid P\) and \(D_r=A_r\). The gcd gate then gives no
localization inside \(A_r\). This does **not** mean that every new endpoint
presentation of the old value is redundant; Section 7 gives a counterexample.

## 2. Exact collapse to quotient differences

### Theorem 1 — three equal forms of the gate

For every \(r\ge1\),

\[
\boxed{
D_r
=\gcd(P,A_r)
=\gcd(P,K-r)
=\gcd\!\left(A_r,\prod_{i=1}^m(k_i-r)\right).
}
\tag{2}
\]

The last gcd uses the absolute value of the product. It is interpreted as
\(A_r\) when one factor is zero.

### Proof

Because \(P=1+KN\),

\[
P-N(K-r)=1+rN=A_r.
\]

Also \(\gcd(P,N)=1\). Therefore

\[
\gcd(P,K-r)=\gcd(P,N(K-r))=\gcd(P,A_r).
\]

Modulo \(A_r\),

\[
A_i=1+k_iN
=A_r+(k_i-r)N
\equiv(k_i-r)N.
\]

Multiplication gives

\[
P\equiv N^m\prod_i(k_i-r)\pmod {A_r}.
\]

Since \(\gcd(A_r,N)=1\), multiplication by \(N^m\) does not change the
gcd with \(A_r\). This proves (2). \(\square\)

### Corollary 1 — exact valuation and support law

Assume \(r\ne k_i\) for all \(i\). For every prime \(p\),

\[
v_p(D_r)
=\min\!\left(
v_p(1+rN),
\sum_{i=1}^m v_p(k_i-r)
\right).
\tag{3}
\]

In particular, every prime divisor of \(D_r\) divides at least one quotient
difference \(k_i-r\). Hence

\[
p\mid D_r
\quad\Longrightarrow\quad
p\le \max_i|k_i-r|.
\tag{4}
\]

Thus a bounded-quotient scan does not reveal a hidden large prime. It
aggregates the supported small-prime part of \(1+rN\). Relation multiplicity
matters through the sum of valuations in (3).

## 3. Exact feedback-candidate gate

Let \(g\) be an occurrence-certified divisor of \(P\) with \(1<g<N\). Let
\(w\) be its canonical inverse modulo \(N\), and write

\[
gw=1+k(g)N.
\]

### Theorem 2 — necessary and sufficient divisor condition

The feedback quotient is \(r\) exactly under the following conditions:

\[
\boxed{
k(g)=r
\quad\Longleftrightarrow\quad
g\mid D_r\ \text{ and }\ r<g<N.
}
\tag{5}
\]

Here the forward direction already implies \(r<g\).

### Proof

If \(k(g)=r\), then

\[
gw=1+rN=A_r.
\]

Thus \(g\mid A_r\). The source certificate gives \(g\mid P\), so
\(g\mid D_r\). Every canonical inverse quotient satisfies
\(1\le k(g)<g\), hence \(r<g\).

Conversely, suppose \(g\mid D_r\) and \(r<g<N\). Put

\[
w=\frac{1+rN}{g}.
\]

This is a positive integer, and

\[
w
\le\frac{1+rN}{r+1}
<N.
\]

Therefore \(w\) is the canonical inverse of \(g\), and its exact quotient is
\(r\). \(\square\)

### Theorem 3 — constructive opening criterion

Assume \(N>r^2\). After gcd-free refinement of the retained block basis by
\(D_r\), a legal quotient-\(r\) feedback candidate exists if and only if

\[
\boxed{D_r>r.}
\tag{6}
\]

When it exists, one can construct it without enumerating block subsets.

### Proof

Necessity follows from Theorem 2.

For sufficiency, express \(D_r\) as a product of retained refined block
occurrences

\[
D_r=a_1a_2\cdots a_t,
\qquad
2\le a_j<N.
\]

The occurrence list has polynomial length because
\(t\le\log_2D_r\le\log_2P\).

If some \(a_j>r\), take \(g=a_j\). Otherwise multiply occurrences in any
order until the running product first exceeds \(r\). Its preceding value and
its last multiplier are both at most \(r\), so

\[
r<g\le r^2<N.
\]

In either case \(g\mid D_r\), and Theorem 2 gives the required canonical
relation. \(\square\)

If \(N\le r^2\) and the scan restricts \(r\le n^c\), where
\(n=\lceil\log_2N\rceil\), trial division through \(\sqrt N\le r\) handles
this small branch in polynomial time. Thus (6) is an exact effective gate for
every polynomially bounded scan.

## 4. Duality with the CRT quotient state

For every unit \(1<g<N\), define

\[
\rho_N(g)=(-N^{-1})\bmod g
\]

in the least-positive range \(1,\ldots,g-1\). Then

\[
g\,\iota_N(g)=1+\rho_N(g)N.
\tag{7}
\]

Thus \(\rho_N(g)\) is exactly the canonical inverse quotient \(k(g)\).
When \(g\mid P=1+KN\), it is also \(K\bmod g\), as in P70.

The two search orders are exact duals:

- a CRT product search chooses \(g\) and computes its fibre label
  \(r=\rho_N(g)\);
- the quotient-collision sieve chooses \(r\) and computes \(D_r\), the
  largest integer divisor common to \(P\) and \(1+rN\).

By Theorem 2, every supported quotient-\(r\) candidate divides \(D_r\), and
every divisor of \(D_r\) in \((r,N)\) is such a candidate. The integer
\(D_r\) can exceed \(N\), and it can aggregate many candidates. It is not
itself necessarily legal or useful. This target-first scan is exact for the
scanned \(r\)'s and needs no beam pruning.

## 5. Polynomial-time scan

Assume \(m\le n^a\) and scan \(1\le r\le R\le n^b\), for fixed constants
\(a,b\).

Each canonical relation satisfies \(A_i<N^2\). Hence \(P\) has
\(O(mn)\) bits. Compute \(P\) once. For every \(r\), compute

\[
D_r=\gcd(P,1+rN).
\]

If \(D_r\le r\), Theorem 3 certifies that this \(r\) gives no legal
feedback divisor. If \(D_r>r\), refine the current block basis by \(D_r\),
construct \(g\) as in Theorem 3, and put \(w=(1+rN)/g\).

All integer products, gcds, exact divisions, and gcd-free refinements have
polynomial bit complexity in the retained transcript size and \(n\). The
complete scan is therefore polynomial time.

A subproduct tree can localize which indexed relation occurrences contribute
to a factor of \(D_r\). At a tree node \(T\), the same collapse gives

\[
\gcd\!\left(\prod_{i\in T}A_i,A_r\right)
=
\gcd\!\left(A_r,\prod_{i\in T}(k_i-r)\right).
\tag{8}
\]

This tree supplies provenance. It is not a proof that a successful \(r\)
exists, and it does not by itself solve arbitrary subset selection.

## 6. Quotient-bounded domination

The first hostile audit identified the exact regime in which the preceding
scan is only a compressed form of an existing polynomial source.

### Theorem 4 — bounded quotients give no new source state

Assume

\[
1\le r,k_i\le B,
\qquad
r\ne k_i,
\qquad
B=\operatorname{poly}(\log N).
\]

If \(D_r>r\), then either trial division resolves \(N\) in polynomial time
(finding a factor when \(N\) is composite), or a direct prior scan of all
canonical states

\[
2\le g\le B^2
\]

already emits the same relation value \(A_r=1+rN\). With the retained product
\(P\), that scan then computes the same \(D_r\) and the same gcd-free
provenance as the quotient-collision gate.

### Proof

Every prime divisor of \(D_r\) divides a nonzero difference \(k_i-r\), so it
is at most \(B\). Trial division completely factors all these differences,
and hence \(D_r\), in polynomial time.

Multiply prime occurrences of \(D_r\) until the running product first exceeds
\(r\). The last prime is at most \(B\), so the resulting divisor satisfies

\[
r<g\le rB\le B^2.
\]

If \(N\le B^2\), trial division through \(B\) resolves \(N\). Otherwise
\(g<N\), and Theorem 2 gives

\[
g\,\iota_N(g)=A_r.
\]

The prior state scan includes this \(g\). Once it has emitted \(A_r\), taking
\(\gcd(P,A_r)\) recovers the identical \(D_r\); gcd-free refinement against
the unchanged endpoint ledger recovers the identical divisor provenance.
\(\square\)

Therefore a quotient-collision scan has a genuinely different source role
only when some relevant quotient difference is not polynomially bounded, or
when it is used only as a faster implementation of an already-polynomial
bounded scan. Even in the large-difference regime, Theorem 4 gives no success
law.

## 7. The equal-quotient case can still have new presentations

At \(N=55\), retain

\[
56=2\cdot28=1+55.
\]

The displayed endpoints pass their sign screens:

\[
\gcd(2\pm1,55)=1,
\qquad
\gcd(28\pm1,55)=1.
\]

The same relation value has the alternative legal presentation

\[
56=14\cdot4,
\]

and

\[
\gcd(14+1,55)=5.
\]

For \(r=k_i=1\), however, \(D_r=A_r=56\). The quotient-collision gcd does
not select \(14\) from its divisors. This is the correct scope boundary: an
equal-quotient presentation can matter, but this gate does not localize it.

## 8. The direct screen must keep the two signs

For a canonical inverse pair \((g,w)\),

\[
\gcd(g-w,N)=\gcd(g^2-1,N).
\tag{9}
\]

This gcd is not a complete factor extractor. If \(g\) is a non-global square
root of one, then its canonical inverse is \(w=g\), so both sides of (9)
equal \(N\). The proper factors are instead

\[
\gcd(g-1,N)
\quad\text{and}\quad
\gcd(g+1,N).
\]

For example, at \(N=55\), the useful state \(g=w=21\) gives

\[
\gcd(g-w,55)=55,
\qquad
\gcd(g-1,55)=5,
\qquad
\gcd(g+1,55)=11.
\]

Therefore a feedback closure must test the two signs of each candidate. One
gcd of \(g-w\) cannot replace them.

## 9. Decoder compression is not source compression

The relation lattice and the source occurrence ledger are different state
objects.

Duplicate relation rows can be removed from a decoder basis. They cannot be
discarded from the source state unless their endpoint presentation and usable
multiplicity remain encoded. Equation (3) gives a sharp reason: repeating a
quotient increases the supported valuation of \(D_r\), even when it adds no
new lattice row.

Use the separator-free \(N=4033\) instance and scan \(r=3\). One retained
copy of the quotient-one relation gives

\[
D_3=\gcd(1+3N,1-3)=2\le3.
\]

Two indexed copies give

\[
D_3=\gcd(1+3N,(1-3)^2)=4>3.
\]

The second copy changes no decoder row span, but it opens the exact feedback
gate and authorizes \(g=4\). Thus an HNF or SNF basis alone is not a complete
recursive-feedback state. A sound implementation can compress repeated
relations, but it must retain multiplicity or an equivalent reusable-capacity
rule.

## 10. Earlier witnesses contained in the gate

The gate contains and certifies the displayed P70/P78 witness choices without
enumerating all block subsets. The generic greedy divisor from Theorem 3 is
not claimed to select the useful member on every input.

| \(N\) | seed quotient multiset | \(r\) | \(D_r\) | selected \(g\) | result |
|---:|:---|---:|---:|---:|:---|
| 21 | \(\{1,4\}\) | 9 | 10 | 10 | \(\gcd(g-1,N)=3\) |
| 55 | \(\{1,2\}\) | 8 | 21 | 21 | non-global square root |
| 21 | \(\{1,1,1\}\) | 3 | 8 | 8 | repeated-relation square root |
| 4033 | \(\{1,1\}\) | 3 | 4 | 4 | new non-global square closure |
| 4033 | \(\{1,63,7\}\) | 1983 | \(10240=2^{11}\cdot5\) | 2048 | splits the old block 1985 by 5 |

For the last row, the gate itself exposes

\[
\gcd(D_r,1985)=5.
\]

It then permits \(g=2^{11}=2048\), whose complementary endpoint is 3905.
This certifies a genuine high-support witness. Its target quotient \(1983\)
is not shown to lie below a fixed polynomial in \(\log N\) on any all-input
family.

The infinite P70 power family is also one line of (3). With \(t\) copies of
\(k_i=1\), target \(r=3\), and

\[
N=\frac{2^{2t}-1}{3},
\]

one has

\[
A_3=2^{2t},
\qquad
\prod_i(k_i-3)=(-2)^t,
\qquad
D_3=2^t>3.
\]

The gate constructs the useful state \(g=2^t\).

## 11. Exact contribution and remaining gap

For each declared target quotient \(r\), this result replaces a scan over all
supported block subsets by one gcd, followed by gcd-free refinement. It
computes the complete supported quotient fibre \(D_r\). This is a genuine
target-first operation when old quotient differences are large. Theorem 4
proves that it gives no new source state in the bounded-quotient regime.

The same theorem gives its limitation. For bounded seed quotients and bounded
\(r\), \(D_r\) is only the quotient-difference-supported smooth part of
\(1+rN\). No theorem here shows that some \(r\le\operatorname{poly}(n)\)
satisfies \(D_r>r\) for every composite \(N\). Even when the gate opens, the
new relation need not directly factor \(N\), split an old block, or create a
non-global decoder root.

The next source question is therefore precise:

> Can a public polynomial-size process create large, correlated old quotient
> differences and make
> \(\gcd(1+rN,\prod_i(k_i-r))>r\) for some polynomially bounded \(r\), with
> an inverse-polynomial all-input probability, and can the resulting relation
> be shown to make factor-bearing progress?

No such law is proved here. No classical polynomial-time factoring algorithm
is claimed.

The failed first hostile audit is preserved at
`experiments/F74_quotient_collision_sieve_audit/RESULT.md`. It accepted the
algebra but rejected the unqualified high-support scope claim and the first
version's treatment of \(r=k_i\). This corrected version addresses both
defects and requires a fresh hostile audit.
