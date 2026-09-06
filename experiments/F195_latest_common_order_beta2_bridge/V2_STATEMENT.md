# F195 V2 — latest common-order terminal and the beta-two interface

## Scope and published premises

Let \(n=\lceil\log_2(N+1)\rceil\). This proof-only statement combines
published algorithms with elementary deductions and the existing
P159--P161 beta-two hard state. It uses these primary-source results:

1. Gao--Feng--Hu--Pan 2025, Theorem 3.1 and Corollary 3.2: if
   \(m\in(\mathbb Z/N\mathbb Z)^*\), \(s,m<N\), and

   \[
   p\equiv s\pmod m
   \quad\text{for every rational prime }p\mid N,
   \]

   then \(N\) can be factored in

   \[
   O\!\left(
   \left\lceil\frac{N^{1/4}}m\right\rceil
   \log^{7+3\epsilon}N
   \right)
   \tag{1}
   \]

   bit operations, for fixed \(\epsilon>0\).
2. Gao--Feng--Hu--Pan 2025, Algorithm 4.3 and Proposition 4.5: the published
   rank-three balanced-semiprime routine and its parameter range and cost.
3. Harvey--Hittmeir 2026, Theorem 1.1, Lemmas 2.1--2.4, and Algorithm 3.1:
   bounded order search, exact lcm-order combination, local-order
   synchronization, the smooth-number lower bound, and the main control
   flow.

All uses of those algorithms remain conditional on their published
hypotheses. This statement does not claim an all-input QP factorer.

## Theorem 1 — exact common order is an \(N^{1/4}/M\) terminal

Suppose a public unit \(g\bmod N\) has one fully known exact order \(M\) in
every hidden prime-power component of \(N\), with

\[
\gcd(M,N)=1.
\tag{2}
\]

Then every rational prime \(p\mid N\) satisfies

\[
\operatorname{ord}_p(g)=M,
\qquad
p\equiv1\pmod M.
\tag{3}
\]

Gao--Feng--Hu--Pan Corollary 3.2, with \(s=1,m=M\), therefore factors
\(N\) in

\[
O\!\left(
\left\lceil\frac{N^{1/4}}M\right\rceil
\log^{7+3\epsilon}N
\right).
\tag{4}
\]

This is QP whenever

\[
N^{1/4}/M=\operatorname{QP}(n).
\tag{5}
\]

Compared with the balanced \(\sqrt N/M^2\) enumeration terminal, (4) has a
smaller same-node search cost and applies to a broader input scope. It does
not change the asymptotic QP threshold class, because

\[
\sqrt N/M^2=(N^{1/4}/M)^2.
\]

## Theorem 2 — the P159 branch exits no later than beta two

Assume an odd input \(N\ge N_0\) and a fixed numerical-QP cap \(C(n)\)
satisfy the P159 beta-two certificate

\[
\operatorname{ord}_N(2)>C(n).
\tag{6}
\]

Run Harvey--Hittmeir Algorithm 3.1 with \(1\le D\le C\). The order
inequality implies \(D<N-1\), as required by the published theorem.

If \(2^D<N\), line 3 returns \(2\). Otherwise the algorithm reaches the
loop, initializes \(M=1\), tests \(\beta=2\), and Lemma 2.1 reports order
above \(D\); line 10 returns \(2\). Thus the later smooth-number stage is
not reached on this branch.

The time bound is

\[
O\!\left(
\frac{D^{1/2}\log D}{\sqrt{\log\log D}}\log N
\right).
\tag{7}
\]

QP time requires numerical-QP \(D\). Taking \(D=N^\delta\) costs
\(N^{\delta/2+o(1)}\) on the current input. A valid recurrence

\[
T(n)\le T(n-1)+\operatorname{QP}(n)
\]

does not change this same-node cost, because the published order search
produces no smaller recursive child before doing the work.

## Theorem 3 — the direct rank-three interface retains an exponential list

On a balanced semiprime, Gao--Feng--Hu--Pan Algorithm 4.3 uses

\[
72<m<N^{1/4}/2
\]

and

\[
k=\Theta\!\left(\frac{N^{1/2}}{m^{3/2}}\right).
\tag{8}
\]

Every legal choice therefore has

\[
k=\Omega(N^{1/8}).
\tag{9}
\]

Its two principal costs are

\[
\varphi(m)\log^3N
\quad\text{and}\quad
\frac{N^{1/2}}{m^{3/2}}\log^2N.
\tag{10}
\]

They balance at \(m=N^{1/5+o(1)}\).

For a beta-two-derived P160 unit whose local orders exceed \(C\), the
published noncollision prefix follows directly from the order bound only if

\[
m^2k\le C.
\tag{11}
\]

But

\[
m^2k=\Theta(N^{1/2}m^{1/2}),
\tag{12}
\]

which is exponential in \(n\) throughout the legal range.

For the P161 rough-order route, let \(P(k)\) denote the largest prime at
most \(k\). If \(m\) is \(T\)-smooth and \(P(k)\le T\), every exponent
\(m^2i\), \(1\le i\le k\), is \(T\)-smooth and hence coprime to each
\(T\)-rough local order. Conversely, covering every integer \(i\le k\) by
this smoothness argument requires \(P(k)\le T\). Bertrand's postulate gives

\[
T\ge P(k)>k/2=Omega(N^{1/8})
\tag{13}
\]

for the large values in scope. Thus the direct published rank-three
interface does not cross the numerical-QP beta-two gate.

## Corollary — integer-specific low/high small-prime fork

On the balanced distinct-semiprime core \(N=pq\), choose numerical-QP caps
\(B(n),D(n)\) with

\[
\log n\ll\log B=o(n).
\tag{14}
\]

Scan the ordinary rational primes \(\beta\le B\). Factor-first bounded order
search gives one of:

1. a proper factor of \(N\);
2. a synchronized exact low order for \(\beta\) in both hidden components;
3. a small ordinary prime \(\beta\) of order above \(D\).

If every scanned prime is in case 2, let \(M\) be the lcm of their exact
orders. Then

\[
M\mid p-1,
\qquad
M\mid q-1,
\qquad
\Psi(p,B)\le M.
\tag{15}
\]

Harvey--Hittmeir's smooth-number bound gives

\[
M\ge p^{1-o(1)}=N^{1/2-o(1)}.
\tag{16}
\]

The already-proved congruences in (15) meet Gao--Feng--Hu--Pan Corollary
3.2 directly with \(s=1,m=M\). Hence the all-low branch factors in QP time.

Therefore a nonterminal balanced branch contains small *ordinary integers*
of high order; beta two is the first such witness in the P159 hard state.
The theorem does not show that several high witnesses generate independent
directions, reveal their exact orders, or factor. A restricted-smoothness or
integer-localization theorem for the mixed low/high branch remains missing.

The canonical carries

\[
x_e=[2^e]_N,
\qquad
x_{e+1}=2x_e-c_eN,
\qquad c_e\in\{0,1\},
\]

remain one rank-one orbit modulo every hidden factor. They do not by
themselves provide the factor-specific residue input of Algorithm 4.3 or the
independent low-order small-integer bank used in (15). No lower bound against
a new carry-sensitive construction is claimed.

## Primary references

- Yiming Gao, Yansong Feng, Honggang Hu, and Yanbin Pan, *On Factoring and
  Power Divisor Problems via Rank-3 Lattices and the Second Vector*,
  Cryptology ePrint Archive 2025/1004,
  <https://eprint.iacr.org/2025/1004>.
- David Harvey and Markus Hittmeir, *Deterministic methods for finding
  elements of large multiplicative order*, arXiv:2601.11131v2,
  <https://arxiv.org/abs/2601.11131>.
