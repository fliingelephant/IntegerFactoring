# F194 — beta-two binomial hidden cancellation

## Scope

Let

\[
N=pq,
\qquad p<q<2p,
\]

where \(p,q\) are distinct odd primes, and put

\[
B=\lfloor\sqrt N\rfloor,
\qquad
A_k=(-1)^k\binom{N-1}{k}.
\]

This is a proof-only theorem about a balanced semiprime. It isolates one
integer-specific sufficient statistic for factoring. It does not give a QP
algorithm for evaluating that statistic.

## Theorem 1 — exact one-jump word

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

The canonical residue is

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

shows the mechanism. The unique jump occurs when the coefficient index
becomes the hidden nonunit \(p\). It releases the exact quotient \(N/p=q\).

## Theorem 2 — two interval-product comparisons

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

Equation (6) is the ordinary interval-product zero predicate up to the unit
\(m!^{-1}\bmod N\). Equations (1)--(4) are stronger as an observable: the
remote unit coefficient itself contains the cofactor through hidden exact
cancellation.

## Theorem 3 — polynomial index moments collapse

For every polynomial \(W(T)\in\mathbb Z[T]\),

\[
\sum_{k=1}^{N-1}W(k)\binom Nk
\equiv W(0)(2^N-2)\pmod N.
\tag{8}
\]

Thus polynomial index weighting, of any degree or succinct description,
does not isolate the hidden coefficient. It collapses to the ordinary scalar
Fermat witness.

## Theorem 4 — succinct Frobenius block and cyclic-support boundary

Put

\[
E_N(X)=(1+X)^N-1-X^N,
\qquad d=q-p.
\tag{9}
\]

The polynomial has an \(O(\log N)\)-size powering circuit and derivative
zero in \((\mathbb Z/N\mathbb Z)[X]\). Locally,

\[
E_N=\bigl((1+X)^q-1-X^q\bigr)^p\pmod p,
\tag{10}
\]

\[
E_N=\bigl((1+X)^p-1-X^p\bigr)^q\pmod q.
\tag{11}
\]

Its local \(X\)-adic orders are exactly \(p\) and \(q\). More explicitly,

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

Let a cyclic sketch reduce exponents modulo an integer \(r\le R<p\). If
\(d<R\), trial division through the \(R\) possible gaps factors \(N\). If
\(d\ge R\), then every residue bucket modulo \(r\) receives a source term
in both hidden components. Therefore support or provenance alone cannot
separate the local first nonzero terms in a QP-size cyclic sketch. This does
not rule out cancellation-sensitive arithmetic processing of such sketches.

## Corollary — exact missing carry

Let \(C=\binom{N-1}{B}\), and define the signed quotient

\[
h=\frac{(-1)^B C-(1-q)}N.
\tag{14}
\]

Then

\[
q=1+hN-(-1)^BC.
\tag{15}
\]

Knowing \(h\bmod 2^t\) together with \(C\bmod2^t\), for \(2^t>q\),
recovers \(q\). The public Kummer valuation of \(C\), or \(C\bmod2^t\)
alone, does not constrain \(q\): since \(N\) is odd, every candidate \(q\)
has one compatible value of \(h\bmod2^t\).

The surviving positive primitive is therefore a QP evaluator for the signed
base-\(N\) quotient carry (14), the threshold residue in (3), or the first
nonzero local Hasse derivative of the succinct circuit (9). Standard
truncation materializes \(B=2^{\Theta(n)}\) coefficients, and ordinary
baby-step/giant-step product or holonomic methods remain exponential in
\(n\). No lower bound against a different succinct evaluator is claimed.
