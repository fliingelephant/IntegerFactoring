# F272 — rank-free obstruction to explicit QP divisor covers

## Status and scope

This is a proof-only candidate with an author self-audit. No hostile audit,
statement-only reconstruction, outside-family audit, or human audit has run.
No computation is used.

The theorem rules out an explicit quasipolynomial-size divisor-cover route at
the scale needed for integer factoring. It is independent of generalized
arithmetic-progression rank. It does not rule out succinct integers whose
expanded bit lengths are large, modular interval-product evaluators that do
not expand those integers, adaptive constructions, or compressed leaf
decoders that do not output complete factorizations of the cover values.

## Definitions

Fix an integer \(X\geq 2\). Let \(S,T\subset\mathbb Z\) be finite sets. Define

\[
 D=D(S,T)=\{|s-t|:s\in S,\ t\in T,\ s\ne t\}\subset\mathbb Z_{>0}.
\tag{1}
\]

Thus \(D\) is a set: equal differences from different ordered pairs occur
only once. Signs are removed by absolute value. Zero is excluded. Allowing
zero as a divisor witness would make the condition vacuous because every
positive integer divides zero.

The set \(D\) has the \(X\)-divisor property when

\[
 \forall m\in\{1,\ldots,X\}\quad \exists d\in D\quad m\mid d.
\tag{2}
\]

Put

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
 \vartheta_2(X)=\sum_{p\leq X\atop p\ {\operatorname{prime}}}\log_2p.
\tag{4}
\]

The prime number theorem gives

\[
 \vartheta_2(X)=\frac{X}{\log 2}+o(X).
\tag{5}
\]

Only the weaker standard Chebyshev bound
\(\vartheta_2(X)\geq cX\) for all sufficiently large \(X\), with one
absolute \(c>0\), is needed for the main obstruction.

## Theorem 1 — prime-mass lower bound

Every \(D\) with the \(X\)-divisor property satisfies

\[
 \boxed{\vartheta_2(X)\leq\sum_{d\in D}\log_2d<ML.}
\tag{6}
\]

In particular,

\[
 \boxed{|S|\,|T|\,L>\vartheta_2(X).}
\tag{7}
\]

If all elements of \(S\cup T\) have signed binary magnitude at most \(B\)
bits, so \(|u|<2^B\), then every difference has at most \(B+1\) bits and

\[
 \boxed{|S|\,|T|\,(B+1)>\vartheta_2(X).}
\tag{8}
\]

Consequently, with input parameter

\[
 n_X=\lceil\log_2(X+1)\rceil,
\]

there is no unbounded sequence of \(X\) for which \(|S|\), \(|T|\), and
the expanded bit length \(L\) are all quasipolynomial in \(n_X\). This
conclusion holds for arbitrary sets and therefore for generalized arithmetic
progressions of every fixed, slowly growing, or unrestricted rank.

## Theorem 2 — explicit-prefactor output lower bound

Let

\[
 K=|\{(s,t)\in S\times T:s\ne t\}|\leq |S|\,|T|.
\tag{9}
\]

Suppose that, for every nonzero ordered pair \((s,t)\), a uniform procedure
outputs the complete prime factorization of \(|s-t|\) as explicit binary
prime/exponent pairs. If every call writes at most \(F\) bits, then

\[
 \boxed{KF\geq\vartheta_2(X).}
\tag{10}
\]

The same inequality holds when \(F\) is a worst-case bit-time bound, because
writing \(F\) output bits costs at least \(F\) bit operations up to a fixed
machine constant.

Therefore quasipolynomial \(|S|,|T|\) and quasipolynomial uniform explicit
prefactorization time are incompatible with the \(X\)-divisor property,
even if each difference has a short circuit or another succinct description
and an arbitrarily large expanded bit length.

Equation (10) counts the actual binary prime names. A shared dictionary does
not evade the statement if the dictionary construction and storage are
charged. References to an uncharged nonuniform dictionary are not explicit
factorization in the uniform bit model.

## Theorem 3 — prime-pair incidence lower bound

Fix constants \(0<a<b\leq1\) and assume \(a\sqrt X>1\). Let

\[
 \mathcal P=\{p\text{ prime}:a\sqrt X\leq p\leq b\sqrt X\},
 \qquad v=|\mathcal P|,
\tag{11}
\]

and put

\[
 h=\left\lfloor\frac{\log H}{\log(a\sqrt X)}\right\rfloor.
\tag{12}
\]

Then

\[
 \boxed{M\binom h2\geq\binom v2.}
\tag{13}
\]

This is also rank-free. It counts all products \(pq\leq X\) with distinct
\(p,q\in\mathcal P\), and how many such pairs one difference of height at
most \(H\) can contain.

## Corollary 4 — Umans--Wang exponent constraints

Suppose, along an unbounded sequence, that

\[
 |S|,|T|\leq X^{\beta+o(1)},
 \qquad
 \max_{u\in S\cup T}u\leq\exp\!\left(X^{\alpha+o(1)}\right),
\tag{14}
\]

with positive elements and nonzero differences used as witnesses. Then
Theorem 1 gives the necessary condition

\[
 \boxed{\alpha+2\beta\geq1.}
\tag{15}
\]

Theorem 3 and the prime number theorem in the fixed square-root band give

\[
 \boxed{\alpha+\beta\geq\tfrac12.}
\tag{16}
\]

If complete factorization of every difference is explicitly output in time
\(X^{\gamma+o(1)}\), Theorem 2 also gives

\[
 \boxed{\gamma+2\beta\geq1.}
\tag{17}
\]

At \((\alpha,\beta)=(1/3,1/3)\), both (15) and (16) are tight as exponent
constraints. They neither prove nor refute a rank-two or higher-rank
construction at that scale.

He--Sahai's unconditional theorem rules out the one-dimensional
arithmetic-progression version at this point: when \(\log H=o(\sqrt X)\),
an \(X\)-divisor arithmetic progression has length

\[
 \Omega\!\left(\frac{X^{3/4}}{\sqrt{\log X}}\right).
\tag{18}
\]

Their at-most-one-intersection step does not extend automatically to a
rank-two generalized arithmetic progression. Thus (18) must not be cited as
an obstruction to ranks two through six, or to the full Strong Divisor
Conjecture.

Even a successful prefactored construction at the one-third point would
give the published deterministic integer-factoring exponent \(1/6\), not
quasipolynomial time in \(\log N\).

## Corollary 5 — explicit prime-separating families

Let \(A_1,\ldots,A_m\) be nonzero integers and assign to every prime
\(p\leq X\) the divisibility codeword

\[
 c(p)=\bigl(\mathbf1_{p\mid A_1},\ldots,
             \mathbf1_{p\mid A_m}\bigr)\in\{0,1\}^m.
\tag{19}
\]

If every two distinct primes \(p,q\leq X\) are separated by some
\(A_i\), meaning exactly one of \(p,q\) divides \(A_i\), then

\[
 m\geq\lceil\log_2\pi(X)\rceil.
\tag{20}
\]

At most one prime has the all-zero codeword. If the complete prime
factorization of each \(A_i\) is explicitly written using at most \(F\)
bits, then

\[
 \boxed{mF\geq\vartheta_2(X)-\log_2X.}
\tag{21}
\]

Thus replacing full divisor coverage by a static prime-separating gcd bank
does not rescue quasipolynomial explicit prefactorization. This corollary
does not cover adaptive banks or a compressed decoder that never prints the
prime factors of the \(A_i\).

## Exact remaining seam

The surviving possibility is not another explicit low-rank cover. It is a
uniform succinct product hierarchy. Such a hierarchy would provide:

1. a root value divisible by all relevant candidate divisors;
2. quasipolynomial-time modular evaluation of every recursively requested
   child product without expanding it; and
3. a terminal rule that either returns a proper factor or descends to a
   genuinely smaller integer without outputting the full factorization of a
   huge cover value.

The narrow canonical instance is the interval-factorial evaluator

\[
 (a,b,d)\longmapsto\prod_{j=a}^{b}j\pmod d
\tag{22}
\]

in time quasipolynomial in \(\log b+\log d\), uniformly for
\(1\leq a\leq b\leq X\). One-path binary gcd splitting of \([1,X]\)
would then return a proper divisor before reaching a singleton. F197 records
that the known explicit block and
Bostan--Gaudry--Schost/Costa--Harvey methods retain an exponential root
cost, and that even the full residue of \(\lfloor\sqrt N\rfloor!\bmod N\)
already factors the balanced semiprime core. Therefore (22) is a precise
live interface, but it is theorem-strength and factoring-equivalent on that
core, not evidence that another GAP grammar will solve it.
