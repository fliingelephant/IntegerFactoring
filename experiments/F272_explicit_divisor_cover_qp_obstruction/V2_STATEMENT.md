# F272 V2 — rank-free obstruction to explicit QP divisor covers

## Status and correction history

This is a corrected proof-only candidate with an author self-audit. The V1
statement reconstructed under a blind statement-only review, but that review
found four literal defects outside the core inequalities:

1. only \(\alpha+2\beta\geq1\), not also
   \(\alpha+\beta\geq1/2\), is saturated at \((1/3,1/3)\);
2. an unspecified fixed bit-machine output rate gives an \(\Omega\) time
   lower bound, not a constant-free exact inequality;
3. a succinct product hierarchy is one sufficient surviving interface, not
   the unique possible escape; and
4. a reduction from an interval-product evaluator to factoring proves that
   evaluator factoring-hard, not factoring-equivalent.

V2 corrects those claims. No hostile audit, V2 statement-only
reconstruction, outside-family audit, or human audit has run. No computation
is used.

The theorem rules out explicit quasipolynomial-size divisor covers at the
scale needed for integer factoring. It is independent of generalized
arithmetic-progression rank. It does not rule out succinct integers with
large expanded bit length, modular evaluators that do not expand them,
adaptive constructions, compressed decoders, or unrelated factoring
mechanisms.

## Definitions

Fix an integer \(X\geq2\). Let \(S,T\subset\mathbb Z\) be finite sets and
define

\[
 D=D(S,T)=\{|s-t|:s\in S,\ t\in T,\ s\ne t\}
 \subset\mathbb Z_{>0}.
\tag{1}
\]

Thus \(D\) is a set. Equal absolute differences from different ordered
pairs occur once. Absolute value removes signs without changing positive
divisibility. Zero is excluded: if zero were a witness, every positive
integer would divide it and the cover property would be vacuous.

If the starting objects are finite multisets, replace each by its support.
This preserves every available difference and can only reduce cardinality.
All conclusions below therefore also hold for multisets when their displayed
sizes count multiplicity.

The set \(D\) has the \(X\)-divisor property when

\[
 \forall m\in\{1,\ldots,X\}\quad
 \exists d\in D\quad m\mid d.
\tag{2}
\]

This property makes \(D\) nonempty. Put

\[
 M=|D|,
 \qquad
 H=\max D,
 \qquad
 L=\max_{d\in D}\bigl(\lfloor\log_2d\rfloor+1\bigr),
\tag{3}
\]

and define the base-two Chebyshev function

\[
 \vartheta_2(X)=
 \sum_{p\leq X\atop p\ {\operatorname{prime}}}\log_2p.
\tag{4}
\]

The standard Chebyshev lower bound gives one absolute \(c>0\) such that

\[
 \vartheta_2(X)\geq cX
\tag{5}
\]

for all sufficiently large \(X\). The prime number theorem gives the
sharper asymptotic

\[
 \vartheta_2(X)=\frac{X}{\log 2}+o(X).
\tag{6}
\]

Only (5) is needed for the main quasipolynomial obstruction.

## Theorem 1 — prime-mass lower bound

Every \(D\) with the \(X\)-divisor property satisfies

\[
 \boxed{\vartheta_2(X)\leq\sum_{d\in D}\log_2d<ML.}
\tag{7}
\]

In particular,

\[
 \boxed{|S|\,|T|\,L>\vartheta_2(X).}
\tag{8}
\]

If every \(u\in S\cup T\) has signed binary magnitude at most \(B\) bits,
meaning \(|u|<2^B\), then every nonzero difference has at most \(B+1\)
bits and

\[
 \boxed{|S|\,|T|\,(B+1)>\vartheta_2(X).}
\tag{9}
\]

Let

\[
 n_X=\lceil\log_2(X+1)\rceil.
\]

There is no unbounded sequence of \(X\) for which \(|S|\), \(|T|\), and
the expanded bit length \(L\) are all bounded by fixed quasipolynomials in
\(n_X\). This conclusion holds for arbitrary sets and therefore for
generalized arithmetic progressions of every fixed, slowly growing, or
unrestricted rank.

## Theorem 2 — explicit-prefactor output and time lower bounds

Let

\[
 K=|\{(s,t)\in S\times T:s\ne t\}|\leq |S|\,|T|.
\tag{10}
\]

Suppose that, for every nonzero ordered pair \((s,t)\), a uniform procedure
outputs the complete prime factorization of \(|s-t|\) as explicit binary
prime/exponent pairs. If every call writes at most \(F_{\rm out}\) bits,
then

\[
 \boxed{K F_{\rm out}\geq\vartheta_2(X).}
\tag{11}
\]

For a fixed sequential bit-machine model, let \(C_0\geq1\) be a fixed
machine constant such that one time step writes at most \(C_0\) output bits.
If every call runs in at most \(F_{\rm time}\) steps, then

\[
 \boxed{K F_{\rm time}
 \geq \vartheta_2(X)/C_0
 =\Omega(\vartheta_2(X))=\Omega(X).}
\tag{12}
\]

Thus quasipolynomial \(|S|,|T|\) and quasipolynomial uniform explicit
prefactorization time in \(n_X\) are incompatible with the
\(X\)-divisor property, even when each difference has a short circuit or
another succinct description and a large expanded bit length.

Equation (11) applies to literal per-pair binary prime names. If outputs use
references into a shared dictionary, then either they do not meet this
literal hypothesis, or the dictionary's construction and materialized
binary prime names must be charged separately. The aggregate charged output
still has \(\Omega(\vartheta_2(X))\) bits, but it need not have the exact
per-call form (11).

## Theorem 3 — prime-pair incidence lower bound

Fix constants \(0<a<b\leq1\), assume \(a\sqrt X>1\), and let

\[
 \mathcal P=\{p\text{ prime}:a\sqrt X\leq p\leq b\sqrt X\},
 \qquad
 v=|\mathcal P|.
\tag{13}
\]

Put

\[
 h=\left\lfloor
 \frac{\log H}{\log(a\sqrt X)}
 \right\rfloor.
\tag{14}
\]

Then

\[
 \boxed{M\binom h2\geq\binom v2.}
\tag{15}
\]

This inequality is rank-free. It counts all products \(pq\leq X\) with
distinct \(p,q\in\mathcal P\) and the number of such pairs one difference
of height at most \(H\) can contain.

## Corollary 4 — exponent constraints

Suppose, along an unbounded sequence, that

\[
 |S|,|T|\leq X^{\beta+o(1)},
 \qquad
 \max_{u\in S\cup T}u
 \leq\exp\!\left(X^{\alpha+o(1)}\right),
\tag{16}
\]

with positive elements and nonzero differences used as witnesses. Then

\[
 \boxed{\alpha+2\beta\geq1}
\tag{17}
\]

and

\[
 \boxed{\alpha+\beta\geq\tfrac12.}
\tag{18}
\]

If complete factorization of every difference is explicitly output in time
\(X^{\gamma+o(1)}\) on one fixed bit machine, then

\[
 \boxed{\gamma+2\beta\geq1.}
\tag{19}
\]

At \((\alpha,\beta)=(1/3,1/3)\), (17) is saturated, while (18) has strict
slack because \(2/3>1/2\). These necessary conditions neither construct nor
refute a rank-two or higher-rank cover at that point.

### External-source boundary

The following are cited literature claims, not proved by F272 V2.

- He--Sahai state that if \(\log H=o(\sqrt X)\), an \(X\)-divisor set that
  is itself one arithmetic progression has length

  \[
  \Omega\!\left(\frac{X^{3/4}}{\sqrt{\log X}}\right).
  \tag{20}
  \]

  Their paper expressly limits this theorem to the one-dimensional AP
  version. Its at-most-one-intersection step does not automatically extend
  to rank two. F272 V2 makes no rank-two-through-six conclusion from (20).

- Umans--Wang state that their Strong Prefactored
  \((\alpha,\beta)\)-Divisor Conjecture implies deterministic integer
  factoring in time

  \[
  \widetilde O\!\left(
  N^{\max(\alpha,\beta)/2+o(1)}
  \right).
  \tag{21}
  \]

  If this cited reduction is accepted, the one-third point gives
  \(N^{1/6+o(1)}\), not quasipolynomial time in \(\log N\).

## Corollary 5 — explicit prime-separating families

Let \(A_1,\ldots,A_m\) be nonzero integers and assign every prime
\(p\leq X\) the divisibility codeword

\[
 c(p)=\bigl(
 \mathbf1_{p\mid A_1},\ldots,\mathbf1_{p\mid A_m}
 \bigr)\in\{0,1\}^m.
\tag{22}
\]

If every two distinct primes \(p,q\leq X\) are separated by some \(A_i\),
meaning exactly one of \(p,q\) divides \(A_i\), then

\[
 m\geq\lceil\log_2\pi(X)\rceil.
\tag{23}
\]

At most one prime has the all-zero codeword. If the complete prime
factorization of every \(A_i\) is explicitly written using at most
\(F_{\rm out}\) bits, then

\[
 \boxed{mF_{\rm out}
 \geq\vartheta_2(X)-\log_2X.}
\tag{24}
\]

On a fixed bit machine, a worst-case per-value time bound
\(F_{\rm time}\) satisfies

\[
 mF_{\rm time}
 =\Omega\!\left(\vartheta_2(X)-\log_2X\right)
 =\Omega(X).
\tag{25}
\]

Thus a static prime-separating gcd bank does not rescue quasipolynomial
explicit prefactorization. This does not cover adaptive banks or compressed
decoders that never print the factorizations of the \(A_i\).

## One precise sufficient seam outside the obstruction

The preceding lower bounds leave many logical possibilities open. One
precise sufficient interface is a uniform interval-product evaluator

\[
 (a,b,d)\longmapsto\prod_{j=a}^{b}j\pmod d
\tag{26}
\]

running in time quasipolynomial in \(\log b+\log d\), uniformly for
\(1\leq a\leq b\). A one-path binary gcd refinement proves that such an
evaluator would give deterministic quasipolynomial integer factoring.
Therefore this evaluator is factoring-hard under that reduction.

F272 V2 does not prove the reverse reduction and does not call the interface
factoring-equivalent. It also does not claim that (26) is the unique
surviving route. Succinct evaluators for other product families, adaptive
gcd strategies, compressed leaf decoders, and unrelated factoring
mechanisms remain outside the obstruction.

P174/F197 records that named explicit block and published
baby-step/giant-step factorial methods retain an exponential root cost, and
that the full residue of \(\lfloor\sqrt N\rfloor!\bmod N\) is already
factor-bearing on the balanced distinct-semiprime core. These are imported
local boundaries. F272 V2 proves no general circuit lower bound.
