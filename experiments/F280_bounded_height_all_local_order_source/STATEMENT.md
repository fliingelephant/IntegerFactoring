# F280 — bounded-height all-local large-order source

## Status and scope

This is a proof-only literature-composition candidate. It uses two primary
2026 preprints and an explicit gcd postprocessor. It proves two deterministic
source interfaces.

1. Nir's arbitrary-\(D\) algorithm gives a bounded ordinary integer. The
   gcd postprocessor
   upgrades its global-order certificate to an all-local-order certificate.
2. Harvey--Hittmeir gives the same all-local conclusion faster, but its
   theorem does not promise an ordinary representative of height
   \(D^{O(1)}\).

The packet also records exact interface boundaries with the promoted order,
carry, reciprocity, and integer-word lanes. These are not lower bounds. They
do not exclude a future transfer theorem from the biased source into a useful
integer carry, quotient, or determinant.

No code, search, run, dataset, or durable-ledger edit belongs to this packet.

## 1. Notation

Let \(N\geq 3\), and let

\[
 n=\lceil\log _2(N+1)\rceil.
\tag{1}
\]

For a unit \(a\bmod N\), write \(\operatorname{ord}_N(a)\) for its
multiplicative order modulo \(N\). For each rational prime \(p\mid N\),
write \(\operatorname{ord}_p(a)\) for the order of its reduction modulo
\(p\).

Define the all-local predicate

\[
 \mathsf{Local}_{D}(a;N)
 \quad\Longleftrightarrow\quad
 \operatorname{ord}_p(a)>D
 \quad\text{for every rational prime }p\mid N.
\tag{2}
\]

Let \(\mathsf M(n)\) denote a valid deterministic bit-complexity bound for
multiplying two \(n\)-bit integers. Successive modular multiplication and
fast gcd computation evaluate the explicit scan below in

\[
 O\!\left(D\,\mathsf M(n)\log n\right)
\tag{3}
\]

bit operations. No sublinear claim is made for this postprocessor.

## 2. Primary theorem interfaces

### Harvey--Hittmeir

Use David Harvey and Markus Hittmeir, *Deterministic methods for finding
elements of large multiplicative order*, arXiv:2601.11131v2:

- abstract record: <https://arxiv.org/abs/2601.11131v2>;
- versioned PDF: <https://arxiv.org/pdf/2601.11131v2>.

Their Theorem 1.1 states the following. Given integers

\[
 N\geq3,\qquad 1\leq D<N-1,
\tag{4}
\]

a deterministic multitape-Turing algorithm returns either a nontrivial
factor of \(N\), or a unit \(\alpha\bmod N\) such that

\[
 \operatorname{ord}_N(\alpha)>D.
\tag{5}
\]

Its bit complexity is

\[
 T_{\rm HH}(N,D)=
 O\!\left(
 {D^{1/2}\log D\over\sqrt{\log\log D}}\log N
 \right),
\tag{6}
\]

with the source's small-\(D\) convention
\(\log\log D:=\log\log\max(D,3)\). The paper states the space bound

\[
 O\!\left({D^{1/2}\over\sqrt{\log\log D}}\log N\right).
\tag{7}
\]

The exact internal interfaces used for comparison are Lemmas 2.1--2.3 and
Algorithm 3.1. A bounded-order search either returns the exact order
\(m\leq D\) or certifies order greater than \(D\). Prime-divisor gcd screens
certify that an exact order \(m\) is the same modulo every prime divisor of
\(N\). The lcm construction explicitly combines known factored orders. If
all scanned small bases have low synchronized order, a smooth-number bound
leads to a direct arithmetic-progression factor scan.

### Nir

Use Itamar Nir, *Deterministically finding an element of large order in
\(\mathbb Z_N^*\)*, arXiv:2605.09592v1:

- abstract record: <https://arxiv.org/abs/2605.09592v1>;
- versioned PDF: <https://arxiv.org/pdf/2605.09592v1>.

Nir's Theorem 1.1 assumes

\[
 D<N,\qquad
 D>\exp\!\sqrt{2\log N\log\log N}.
\tag{8}
\]

It returns a global-order-\(>D\) unit, a nontrivial factor, or the report
that \(N\) is prime, in stated time

\[
 O(D^{1/2+o(1)}).
\tag{9}
\]

The hypothesis (8) absorbs the polynomial factors in \(\log N\).

The interface used in F280 is Nir's Proposition 1.2. For every pair of
positive integers \(D<N\), it returns one of the same three outcomes in

\[
 O(D^{5/2+o(1)}\operatorname{polylog}N)
\tag{10}
\]

time. If it returns a high-order unit, that unit is an ordinary integer from
the explicit scan

\[
 2\leq a\leq D^2+D.
\tag{11}
\]

## 3. Bounded-height all-local source

### Theorem 1 — Nir plus the explicit local gcd scan

For positive integers \(N\geq3\) and \(D<N\), there is a deterministic
algorithm that returns one of:

1. a nontrivial factor of \(N\);
2. the correct report that \(N\) is prime; or
3. an ordinary integer \(a\) satisfying
   \[
   2\leq a\leq D^2+D,
   \qquad
   \mathsf{Local}_{D}(a;N).
   \tag{12}
   \]

Its bit complexity is

\[
 \boxed{
 O(D^{5/2+o(1)}\operatorname{polylog}N).}
\tag{13}
\]

For the third outcome, a direct certificate transcript is

\[
 g_e=\gcd(a^e-1,N)=1,
 \qquad 1\leq e\leq D.
\tag{14}
\]

The powers in (14) are generated successively. The theorem makes no claim
that the length-\(D\) transcript is succinct.

## 4. Faster unrestricted-height source

### Theorem 2 — Harvey--Hittmeir plus the same postprocessor

For \(N\geq3\) and \(1\leq D<N-1\), there is a deterministic algorithm
that returns a nontrivial factor of \(N\), or a unit \(\alpha\bmod N\)
such that

\[
 \boxed{\mathsf{Local}_{D}(\alpha;N).}
\tag{15}
\]

Its bit complexity is

\[
 \boxed{
 O\!\left(
 {D^{1/2}\log D\over\sqrt{\log\log D}}\log N
 +D\,\mathsf M(n)\log n
 \right).}
\tag{16}
\]

This is asymptotically faster in \(D\) than (13). The explicit local scan,
not the Harvey--Hittmeir source construction, is the dominant term in (16)
for large \(D\). The theorem gives a canonical representative below \(N\),
but it gives no uniform bound \(\alpha\leq D^{O(1)}\). Algorithm 3.1 can
return a small scanned base on one branch and an lcm-combined residue on
another branch. Theorem 2 does not erase this distinction.

## 5. Numerical-quasipolynomial range

Call a numerical bound quasipolynomial when

\[
 Q(n)=\exp((\log n)^{O(1)}).
\tag{17}
\]

### Corollary 3 — exact QP threshold

For every fixed numerical-QP choice of \(D=D(n)\), Theorems 1 and 2 have
deterministic numerical-QP bit complexity and return their stated outcomes
for all sufficiently large admissible inputs. The bounded source in (12)
also has numerical-QP ordinary height.

Nir's main Theorem 1.1 does not have an asymptotic numerical-QP parameter
range. Its threshold has

\[
 \log D=\Theta(\sqrt{n\log n}),
\tag{18}
\]

which exceeds every fixed power of \(\log n\).

For comparison, if \(D=N^\delta\) with fixed \(\delta>0\), the
Harvey--Hittmeir global source construction alone costs

\[
 N^{\delta/2+o(1)}.
\tag{19}
\]

The explicit all-local postprocessor in Theorem 2 costs
\(N^{\delta+o(1)}\). These are upper-bound accounting statements. They are
not lower bounds for other order or factoring algorithms.

## 6. Exact synchronized-order capacity

### Proposition 4 — synchronized lcms are common capacity

Suppose an HH or Nir low-order transcript has passed the prime-divisor gcd
screens. Let \(m_1,\ldots,m_t\) be the accepted exact orders, and put

\[
 M=\operatorname{lcm}(m_1,\ldots,m_t).
\tag{20}
\]

Then

\[
 \boxed{M\mid p-1\quad\text{for every rational prime }p\mid N.}
\tag{21}
\]

For a semiprime \(N=pq\), if

\[
 d=\gcd(p-1,q-1),
\tag{22}
\]

then

\[
 \boxed{M\mid d\mid N-1.}
\tag{23}
\]

Thus \(M\) supplies exact common order capacity. It supplies no rational
prime support outside \(N-1\). This does not make \(M\) useless. A
sufficiently large common order can enter a common-order terminal, and the
all-low smooth-prefix branch uses \(M\) in a direct factor scan.

Against the F259/F260 saturated baseline, the statement is stronger. If
\(\ell\mid N-1\), then \((N-1)^n\) already contains the full
\(\ell\)-primary part of every \(p-1<N\). Therefore multiplying that
baseline by any \(M\mid N-1\) does not change its gcd with any \(p-1\).

## 7. Exact non-implications and interface boundary

### Proposition 5 — global high order is not local, rough, or a word

The predicate

\[
 \operatorname{ord}_N(a)>D
\tag{24}
\]

does not imply any of the following:

1. \(\mathsf{Local}_{D}(a;N)\);
2. equality of the local orders;
3. that the order is \(D\)-rough; or
4. that the ordinary integer \(a\) absorbs a P205 residual.

One counterexample proves all four failures relevant to the bare witness.
Take

\[
 N=77=7\cdot11,\qquad D=10,\qquad a=2.
\tag{25}
\]

Then

\[
 \operatorname{ord}_7(2)=3,\qquad
 \operatorname{ord}_{11}(2)=10,\qquad
 \operatorname{ord}_{77}(2)=30>D.
\tag{26}
\]

The global order is composed only of primes at most \(D\). The local orders
are unequal and neither exceeds \(D\). Moreover,

\[
 d=\gcd(6,10)=2,\qquad
 s_7=3,\qquad s_{11}=5,
\tag{27}
\]

while

\[
 \gcd(a,s_7)=\gcd(a,s_{11})=1.
\tag{28}
\]

Thus using the returned base itself as \(W\) gives no P205 residual
absorption in this example.

The last statement is deliberately narrow. Neither primary theorem outputs
a P205 word or a divisibility theorem for a word derived from its high-order
witness. F280 does not prove that no such derived word exists. It proves only
that the high-order predicate and the returned base do not supply it without
an additional transfer lemma.

## 8. Relation to current lanes

- **P139.** Theorem 2 is the primary Harvey--Hittmeir premise followed by
  P139's explicit local scan. The new source shape is Theorem 1's ordinary
  height bound \(a\leq D^2+D\).
- **P161.** Proposition 5 blocks the inference from large order to rough
  order. P161's primary-support filter remains separate.
- **P162--P164.** The source gives long local actions after (14). It gives no
  support list, resultant extinction certificate, recursive child, or
  independent direction.
- **P165.** The deterministic small integer is biased, so a uniform-source
  boundary does not apply to it. No success distribution follows from that
  exclusion.
- **P166--P167.** Neither source evaluates a segment Jacobi sum or retained
  Paley decoder.
- **P168--P170.** Neither source localizes hidden support, selects an ACD
  cluster, or constructs a separating non-diagonal representation.
- **P187.** The common modulus in (21) treats all hidden factors symmetrically
  and supplies no orientation of an inversion torsor.
- **P205.** Proposition 4 adds only common capacity. Proposition 5 shows that
  a bare high-order base is not the required public residual-absorbing word.
- **P212.** The bounded small integer is a biased source outside P212's
  restricted fresh-uniform grammar. This does not refute P212 and does not
  give an all-input or inverse-QP marker-hit law.
- **F259/F260.** A synchronized \(M\) is already covered by the saturated
  \((N-1)^n\) support. The high-order base has no proved Pell, carry,
  quotient, collision, or P205-word transfer law. F280 supplies no reason to
  change or run either frozen grammar.

These are interface comparisons. They do not say that the cited lanes are
the only possible uses of the source.

## 9. Search disposition

No symbolic or numerical search is justified from the order source alone.
A future search proposal must first prove a transfer lemma that maps the
biased source into an explicit integer carry, inverse quotient, or
determinant and proves one of:

\[
 \boxed{
 \text{an all-input divisibility law}
 \quad\text{or}\quad
 \text{an inverse-QP divisibility law}.}
\tag{29}
\]

Without that theorem, adding the source to F259 or F260 changes the grammar
but supplies no certified progress statistic.

## 10. Exact exclusions

F280 proves no factoring algorithm, no deterministic lower bound, no generic
order-search lower bound, no impossibility theorem for biased sources, no
P205-word impossibility theorem, and no carry-distribution theorem. It does
not claim that \(D^{1/2+o(1)}\) is necessary. It does not exclude batch order
certificates, new recursions, symbolic transfer identities, nonlinear
carries, or future source-aware decoders.
