# F194 V2 — beta-two binomial hidden cancellation

## Scope

Let

\[
N=pq,
\qquad p<q<2p,
\]

where \(p,q\) are distinct odd primes. Put

\[
B=\lfloor\sqrt N\rfloor,
\qquad
A_k=(-1)^k\binom{N-1}{k}.
\]

This is a proof-only balanced-semiprime theorem. It isolates an
integer-specific sufficient statistic for factoring. It does not construct a
QP evaluator for that statistic.

## Theorem 1 — exact one-jump word and endpoint factor

For every \(0\le k\le B\),

\[
A_k\equiv
\begin{cases}
1\pmod N,&0\le k<p,\\[2mm]
1-q\pmod N,&p\le k\le B.
\end{cases}
\tag{1}
\]

Equivalently, for \(1\le k\le B\),

\[
\binom Nk\equiv
\begin{cases}
q\pmod N,&k=p,\\
0\pmod N,&k\ne p.
\end{cases}
\tag{2}
\]

Consequently,

\[
\boxed{
\gcd\!\left(N,(-1)^B\binom{N-1}{B}-1\right)=q.}
\tag{3}
\]

The canonical endpoint residue is

\[
\binom{N-1}{B}\bmod N=
\begin{cases}
q-1,&B\text{ odd},\\
N-q+1,&B\text{ even}.
\end{cases}
\tag{4}
\]

The exact integer recurrence

\[
(k+1)(A_{k+1}-A_k)=-NA_k
\tag{5}
\]

shows the integer-specific mechanism. The sole jump occurs at the hidden
nonunit index \(k+1=p\), where exact integer cancellation releases
\(N/p=q\). No division by \(p\) modulo \(N\) is used.

## Theorem 2 — two central-binomial comparisons

Let \(m=\lceil B/2\rceil\). Then

\[
m<p\le2m<q,
\qquad
\gcd\!\left(N,\binom{2m}{m}\right)=p.
\tag{6}
\]

Also,

\[
\gcd\!\left(N,\binom{2B}{B}\right)=q.
\tag{7}
\]

Equation (6) is an interval-product zero predicate up to the unit
\(m!^{-1}\bmod N\). Equation (3) is different: the remote coefficient is a
unit, but a signed shift of its residue exposes the cofactor.

## Theorem 3 — polynomial index moments collapse

For every \(W(T)\in\mathbb Z[T]\),

\[
\sum_{k=1}^{N-1}W(k)\binom Nk
\equiv W(0)(2^N-2)\pmod N.
\tag{8}
\]

This is an exact algebraic identity with no degree bound. It shows that
polynomial index weights do not isolate the exceptional prefix coefficient;
it is not a circuit or evaluation lower bound.

## Theorem 4 — succinct Frobenius block

Put

\[
E_N(X)=(1+X)^N-1-X^N,
\qquad d=q-p.
\tag{9}
\]

The polynomial has an \(O(\log N)\)-gate powering circuit and derivative
zero in \((\mathbb Z/N\mathbb Z)[X]\). Locally,

\[
E_N=\bigl((1+X)^q-1-X^q\bigr)^p\pmod p,
\tag{10}
\]

\[
E_N=\bigl((1+X)^p-1-X^p\bigr)^q\pmod q.
\tag{11}
\]

Its exact local \(X\)-adic orders are \(p\) and \(q\). Explicitly,

\[
E_N\equiv
\sum_{j=1}^{d}\binom djX^{pj}
+\sum_{j=0}^{d-1}\binom djX^{p^2+pj}
\pmod p,
\tag{12}
\]

and

\[
E_N\equiv
\sum_{j=1}^{p-1}\binom pjX^{qj}
\pmod q.
\tag{13}
\]

Every displayed coefficient is nonzero in its field.

For a positive numerical-QP bound \(R(n)<p\), let \(1\le r\le R\). If
\(d<R\), enumerating \(1\le\delta<R\) and testing whether
\(\delta^2+4N\) is a square recovers \(p,q\) in numerical-QP time. If
\(d\ge R\), then after reducing exponents modulo \(r\), the Boolean source
support of each local expansion (12) and (13) is every class in
\(\mathbb Z/r\mathbb Z\). This is only an incidence statement. It does not
cover coefficients, cancellation, multiplicity, source labels, or any richer
notion of provenance.

## Corollary — precise modular carry interface

Let \(C=\binom{N-1}{B}\), and define the signed integer quotient

\[
h=\frac{(-1)^BC-(1-q)}N.
\tag{14}
\]

For any \(t\) with \(2^t>q\), the pair

\[
(C\bmod2^t,\ h\bmod2^t)
\tag{15}
\]

recovers \(q\), because

\[
q=1+hN-(-1)^BC.
\tag{16}
\]

For a fixed value of \(C\bmod2^t\), every candidate \(q\bmod2^t\) has
exactly one compatible \(h\bmod2^t\), since \(N\) is odd. This is only a
statement about the displayed congruence. No QP evaluator for either residue
in (15), and no information-theoretic lower bound, is claimed.

Any one of the following would be a sufficient new factoring primitive on
the stated promise:

1. compute the residue in (3) in QP time;
2. compute the pair (15) in QP time for \(t=O(n)\) and \(2^t>q\);
3. recover either exact local \(X\)-adic order of the succinct circuit (9).

The theorem supplies none of these evaluators. Direct coefficient
truncation uses \(B+1=2^{\Theta(n)}\) coordinates. No lower bound against a
different succinct algorithm is claimed.
