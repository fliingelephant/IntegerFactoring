# F213 candidate — a polynomial near-square norm bank can have only global parity roots

## Status

This is a frozen, self-audited, proof-only candidate. It is an exact
method obstruction for the ordinary rational-prime valuation parity matrix
built from the near-square norms below. It is not a lower bound against
arbitrary postprocessing of the factored norms and is not a factoring
algorithm.

## Setup

For a positive integer \(N\) and a public positive integer \(a\), put

\[
r_a=\lfloor a\sqrt N\rfloor,
\qquad
E_a=a^2N-r_a^2,
\qquad
F_a=(r_a+1)^2-a^2N.
\]

The \(F_a\) column is optional. The exact relations are

\[
r_a^2\equiv-E_a\pmod N,
\qquad
(r_a+1)^2\equiv F_a\pmod N.
\]

For a finite set of positive integers, its ordinary parity matrix means the
matrix over \(\mathbb F_2\) whose rows are the rational primes, together with
one sign row, and whose columns are the valuation-parity vectors. The
\(E_a\) column is the vector of \(-E_a\); the \(F_a\) column is the vector of
\(F_a\). A dependency is a binary subset of columns whose signed product is
a positive rational square.

## Theorem

For every integer \(M\geq2\), there exist an even integer \(s>M\), an odd
composite integer

\[
N=s^2+1,
\]

and distinct rational primes \(\ell_1,\ldots,\ell_M\) such that the public
bank indexed by \(1\leq a\leq M\) has all of the following properties.

### 1. Exact no-carry norms

For every \(1\leq a\leq M\),

\[
\boxed{r_a=as,\qquad E_a=a^2,
\qquad F_a=2as+1-a^2.}
\]

In particular,

\[
0<E_a<N,\qquad 0<F_a<N.
\]

### 2. No direct gcd exit

For every \(a\),

\[
\gcd(a,N)=\gcd(r_a,N)=\gcd(r_a+1,N)
=\gcd(E_a,N)=\gcd(F_a,N)=1.
\]

Thus direct screening of the relation bases or norms does not factor the
constructed input.

### 3. One private valuation row for every adjacent norm

For every \(a\),

\[
v_{\ell_a}(F_a)=1,
\]

while

\[
\ell_a\nmid E_bF_b
\qquad(1\leq b\leq M,\ b\neq a)
\]

and \(\ell_a\nmid E_a\). Hence the \(\ell_a\)-row is a pivot appearing in
exactly the \(F_a\) column.

### 4. Exact kernel and root image

In the parity matrix containing all \(2M\) columns

\[
(-E_1),F_1,\ldots,(-E_M),F_M,
\]

every dependency excludes every \(F_a\) column and contains an even number
of \(E_a\) columns. Conversely, every even subset of the \(E_a\) columns is
a dependency. Thus the kernel is exactly

\[
\boxed{
\{(x_1,0,\ldots,x_M,0):
x_1+\cdots+x_M=0\text{ in }\mathbb F_2\}.}
\]

For a dependency using the \(E_a\) indices in a set \(S\), put

\[
X=\prod_{a\in S}r_a,
\qquad
Y=\prod_{a\in S}a,
\qquad k=|S|.
\]

Then \(Y\) is a unit modulo \(N\), \(X^2\equiv Y^2\pmod N\), and

\[
\boxed{XY^{-1}\equiv s^k=(-1)^{k/2}\in\{1,-1\}\pmod N.}
\]

Therefore every parity dependency gives only a global square root. The two
standard gcds are \(1\) and \(N\), in some order.

If only the \(E_a\) columns are used, the same kernel and root-image
description holds. If a sign-free implementation treats an odd product of
the \(E_a\)'s as a relation, it obtains the already public root \(s\) of
\(-1\), not a second root of \(1\); this also gives no factor.

### 5. Bank size and recursive accounting

The construction can be chosen so that, with

\[
n=\lceil\log_2(N+1)\rceil,
\]

one has

\[
\Omega(M^2)\leq n\leq O(M^2\log(M+1)).
\]

Consequently

\[
M=n^{1/2+o(1)}.
\]

The bank has \(2M\) columns and is polynomial in the input length. The
\(E_a\)'s have \(O(\log M)\) bits. Uniformly in \(1\leq a\leq M\),

\[
\operatorname{bits}(F_a)=\frac n2+O(\log M)
=\left(\frac12+o(1)\right)n.
\]

In particular, along the constructed family and for all sufficiently large
\(M\), the completely public schedule

\[
1\leq a\leq\lfloor n^{1/3}\rfloor
\]

is a subset of the constructed bank and inherits the same exact kernel and
global-root obstruction. Thus the counterexample does not rely on revealing
the construction parameter \(M\) to choose the multipliers.

Thus complete recursive factorization of all children is a valid
fixed-ratio collection of calls. A polynomial or numerical-QP number of
such calls is absorbed by the recurrence theorem of P183. The same remains
true if an outer construction also has one separate one-bit decrement
spine. This theorem grants the complete factorizations and shows that the
resulting parity matrix can nevertheless have only global roots.

## Exact consequence and scope

Cardinality, smaller child size, complete norm factorization, and positive
parity nullity do not by themselves force a non-global square root. This
remains false even for a polynomial-sized public bank of the exact
near-square and adjacent near-square norms above.

The theorem does not claim:

1. that every \(N\), every semiprime, or every balanced semiprime has this
   obstruction;
2. that the constructed \(N=s^2+1\) is a semiprime;
3. that an arbitrary nonlinear, Archimedean, adaptive, or non-parity use of
   the fully factored \(F_a\)'s cannot factor this special \(N\);
4. that a larger bank extending beyond \(a=M\) retains the private rows; or
5. that a specially proved all-input QP-size schedule cannot force a useful
   relation by additional arithmetic structure.

The exact obstruction is to the inference “QP-many fully factored norms
force a parity dependency with a non-global root.” Polynomial size is a
special case of numerical QP size, but the theorem does not quantify over
every possible QP schedule.
