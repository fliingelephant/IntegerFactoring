# F272 V2 blind statement-only reconstruction

## Authentication and verdict

The SHA-256 digest of V2_STATEMENT.md is

    1b6c52624e5f957b2814f5e3e98572612e7cf9312b167ed117e01dddf0d4abb5

**Verdict: PASS for every internal mathematical claim examined below.** I
reconstructed the claims from the authenticated statement alone. I found no
counterexample, missing case, reversed reduction, or exponent error. The two
named literature attributions and the imported P174/F197 boundary are not
authenticated by a statement-only reconstruction; the deductions made
conditionally from them are correct.

## 1. Prime mass and the rank-free obstruction

For each prime \(p\le X\), apply the divisor property to \(m=p\). Some
\(d\in D\) is divisible by \(p\). Therefore every prime at most \(X\) occurs
at least once among the prime divisors of the integers in \(D\), and hence

\[
 \sum_{p\le X}\log_2p
 \le \sum_{d\in D}\log_2d.
\]

Every \(d\in D\) satisfies \(d<2^L\). Since \(D\ne\varnothing\), summing the
strict inequalities gives

\[
 \vartheta_2(X)\le\sum_{d\in D}\log_2d<ML.
\]

There are at most \(|S||T|\) distinct nonzero absolute differences, so

\[
 |S||T|L>\vartheta_2(X).
\]

If \(|u|<2^B\) for all \(u\in S\cup T\), then

\[
 0<|s-t|<2^{B+1}.
\]

Thus each difference has at most \(B+1\) bits, and

\[
 |S||T|(B+1)>\vartheta_2(X).
\]

Removing duplicate multiset elements does not change \(D\) and cannot
increase either displayed input size, so the multiset extension is valid.

Now \(n_X=\Theta(\log X)\). A product of finitely many fixed
quasipolynomials in \(n_X\) is still

\[
 2^{O((\log n_X)^k)}=2^{o(n_X)}=X^{o(1)}.
\]

It cannot dominate the declared Chebyshev bound
\(\vartheta_2(X)\ge cX\) on an unbounded sequence. Consequently
\(|S|,|T|,L\) cannot all have fixed quasipolynomial bounds in \(n_X\).
Nothing in this proof uses a progression representation, dimension, rank,
or additive structure. The rank-free scope is therefore literal.

## 2. Explicit-factorization output and time

Let \(\ell(p)=\lfloor\log_2p\rfloor+1\) be the length of the literal binary
name of \(p\). Across the \(K\) factorization outputs, every prime \(p\le X\)
must be named in at least one output: choose a covering difference for \(p\),
then choose an ordered pair producing that difference. Hence the aggregate
number of written bits is at least

\[
 \sum_{p\le X}\ell(p)\ge\vartheta_2(X).
\]

If each call writes at most \(F_{\rm out}\) bits, its aggregate output is at
most \(KF_{\rm out}\). This proves

\[
 KF_{\rm out}\ge\vartheta_2(X).
\]

On the stated fixed sequential machine, a call lasting at most
\(F_{\rm time}\) steps writes at most \(C_0F_{\rm time}\) bits. Summing
over the calls gives

\[
 KF_{\rm time}\ge \vartheta_2(X)/C_0=\Omega(X).
\]

Since \(K\le|S||T|\), quasipolynomial set sizes and a quasipolynomial
worst-case explicit-factorization time cannot coexist with the divisor
property. This proof never uses the expanded length or representation of a
difference.

The shared-dictionary qualification is also exact. A reference is not a
literal per-call binary prime name, so it leaves the hypothesis of the exact
\(KF_{\rm out}\) statement. If the dictionary separately materializes all
the required literal binary names, their charged writes have total length at
least \(\vartheta_2(X)\). A compressed dictionary or decoder that does not
materialize those names is outside the proved interface.

## 3. Prime-pair incidence

The divisor property for \(m=X\) implies \(H\ge X\), so the definition of
\(h\) is harmless under \(a\sqrt X>1\). For \(d\in D\), let

\[
 r_d=|\{p\in\mathcal P:p\mid d\}|.
\]

The primes counted by \(r_d\) are distinct and each is at least
\(a\sqrt X\). Therefore

\[
 (a\sqrt X)^{r_d}\le d\le H,
 \qquad r_d\le
 \left\lfloor\frac{\log H}{\log(a\sqrt X)}\right\rfloor=h.
\]

Each \(d\) is incident to at most \(\binom h2\) unordered distinct-prime
pairs from \(\mathcal P\). Conversely, if \(p,q\in\mathcal P\) are distinct,
then

\[
 pq\le b^2X\le X.
\]

The divisor property applied to \(pq\) supplies some \(d\in D\) divisible by
both primes. Thus all \(\binom v2\) pairs occur in the incidence relation.
Counting incidences proves

\[
 M\binom h2\ge\binom v2.
\]

Again, no structural property of \(S\) or \(T\) appears.

## 4. Exponent laws and the one-third point

Write \(U=\max(S\cup T)\). Positivity gives \(H<U\), and the hypotheses give

\[
 M\le |S||T|\le X^{2\beta+o(1)},
 \qquad
 \log H\le X^{\alpha+o(1)}.
\]

The prime-mass inequality and \(\vartheta_2(X)\ge cX\) now imply

\[
 X^{1+o(1)}\le X^{\alpha+2\beta+o(1)},
\]

so

\[
 \alpha+2\beta\ge1.
\]

For the second law, fix any constants \(0<a<b\le1\). The prime number
theorem in this fixed interval gives

\[
 v=\Theta\!\left(\frac{\sqrt X}{\log X}\right)
   =X^{1/2+o(1)}.
\]

Also

\[
 h\le \frac{X^{\alpha+o(1)}}{\Theta(\log X)}.
\]

Insert these estimates and \(M\le X^{2\beta+o(1)}\) into the prime-pair
bound. Ignoring only fixed constants and subpolynomial factors gives

\[
 X^{2\beta+2\alpha+o(1)}\ge X^{1+o(1)},
\]

and therefore

\[
 \alpha+\beta\ge\tfrac12.
\]

If every distinct difference is explicitly factored in at most
\(X^{\gamma+o(1)}\) time, the same output-mass argument can be summed over
the \(M\) differences (or over the \(K\) ordered pairs in Theorem 2). Since
\(M\le K\le|S||T|\), it yields

\[
 X^{\gamma+2\beta+o(1)}\ge X,
 \qquad
 \gamma+2\beta\ge1.
\]

At \((\alpha,\beta)=(1/3,1/3)\), the first left side is \(1\), while the
second is \(2/3>1/2\). Thus only \(\alpha+2\beta\ge1\) is saturated. Satisfying
necessary inequalities supplies neither a construction nor a refutation at
that point.

Conditionally accepting the quoted Umans--Wang running-time formula, direct
substitution at the one-third point gives \(N^{1/6+o(1)}\). This is
\(2^{\Theta(\log N)}\) up to the \(o(1)\) exponent, not quasipolynomial in
\(\log N\). The arithmetic deduction is correct; the source attribution is
not independently checked here.

## 5. Prime-separating families

Pairwise separation says precisely that \(c(p)\ne c(q)\) for distinct
primes \(p,q\le X\). The code map is injective, so

\[
 \pi(X)\le2^m,
 \qquad
 m\ge\lceil\log_2\pi(X)\rceil.
\]

Injectivity also permits at most one all-zero codeword. Every other prime
divides at least one \(A_i\), so its literal binary name occurs in at least
one complete factorization output. If \(p_0\) is the possible omitted prime,
the aggregate number of output bits is at least

\[
 \sum_{p\le X,\ p\ne p_0}\log_2p
 \ge\vartheta_2(X)-\log_2X.
\]

The aggregate is at most \(mF_{\rm out}\), proving

\[
 mF_{\rm out}\ge\vartheta_2(X)-\log_2X.
\]

The fixed-machine output-rate argument then gives

\[
 mF_{\rm time}
 \ge \frac{\vartheta_2(X)-\log_2X}{C_0}
 =\Omega(X).
\]

This is a statement about a fixed family with explicit factorization
outputs. An adaptive decision tree need not instantiate one such universal
code family, and a decoder that never prints the prime names does not meet
the output hypothesis. The stated scope exclusions are valid.

## 6. Interval products reduce factoring to the evaluator

Assume the evaluator

\[
 E(a,b,d)=\prod_{j=a}^b j\pmod d
\]

runs uniformly in quasipolynomial time in \(\log b+\log d\). Let \(n>3\) be
a composite integer, and put \(r=\lfloor\sqrt n\rfloor\). A prime divisor
\(p\le r\) exists, so

\[
 g=\gcd(n,E(2,r,n))>1.
\]

If \(g<n\), return \(g\). Otherwise \(n\) divides the interval product.
Maintain an interval \([a,b]\subseteq[2,r]\) with

\[
 n\mid\prod_{j=a}^b j.
\]

Split it at \(c=\lfloor(a+b)/2\rfloor\), evaluate the left product, and set
\(g_L=\gcd(n,E(a,c,n))\).

- If \(1<g_L<n\), return \(g_L\).
- If \(g_L=n\), retain \([a,c]\).
- If \(g_L=1\), the left product is a unit modulo \(n\). The invariant then
  implies that \(n\) divides the right product, so retain \([c+1,b]\).

Each retained interval has at most half the previous length. If the process
reached a singleton \(j\), its invariant would say \(n\mid j\), impossible
because \(2\le j\le r<n\). Therefore a nontrivial divisor is returned after
\(O(\log n)\) evaluator calls. All endpoints, moduli, residues, and gcd
operands have \(O(\log n)\) bits. The remaining arithmetic has polynomial
bit complexity.

For complete factorization, first run a deterministic polynomial-time
primality test. Output a prime input. For a composite input, use the
procedure above and recurse on the returned divisor and its exact quotient.
A factorization tree has at most \(\log_2 N\) prime leaves counted with
multiplicity and fewer than twice as many total nodes. Thus it makes at most
\(O((\log N)^2)\) evaluator calls, each on \(O(\log N)\)-bit arguments.
Polynomially many quasipolynomial-time calls remain quasipolynomial. This
also covers even inputs, prime powers, repeated factors, and arbitrary
composites.

This proves a deterministic quasipolynomial Turing reduction from integer
factoring to the interval-product evaluator. It justifies
“factoring-hard under that reduction.” It proves no evaluator-from-factoring
reduction, so it does not justify “factoring-equivalent.” Nor do the earlier
lower bounds show this evaluator to be the unique surviving interface: they
apply only to their explicit-cover, explicit-output, incidence, or static
separation hypotheses.

## Evidence boundary

The He--Sahai theorem statement, the description of the scope of its proof,
and the P174/F197 records are external or imported assertions. I did not
inspect those sources, as required by the blind statement-only protocol.
They are not premises of the reconstructed core bounds or the
interval-product reduction. The reconstruction also yields no general
circuit lower bound.

**Final verdict: PASS, with external attributions explicitly left
source-dependent.**
