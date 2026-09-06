# F195 — latest common-order terminal and the beta-two interface

## Scope and external premises

Let \(n=\lceil\log_2(N+1)\rceil\). This proof-only statement combines two
published algorithmic premises with elementary group deductions and the
existing P159--P161 beta-two hard state.

External premises:

1. Gao--Feng--Hu--Pan 2025, Theorem 3.1 and Corollary 3.2: if a public unit
   modulus \(m\) and residue \(s\) satisfy

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

   bit operations under the paper's stated hypotheses.
2. Harvey--Hittmeir 2026, Theorem 1.1, Lemma 2.1, and Algorithm 3.1: given
   \(D<N-1\), the algorithm returns a factor or a unit of order above \(D\)
   in

   \[
   O\!\left(
   \frac{D^{1/2}\log D}{\sqrt{\log\log D}}\log N
   \right)
   \tag{2}
   \]

   bit operations.

The exact claims below are conditional only on these published premises.
They do not assert that either paper proves a QP factoring algorithm.

## Theorem 1 — exact common order is an \(N^{1/4}/M\) terminal

Suppose a public unit \(g\bmod N\) has one fully known exact order \(M\) in
every hidden prime-power component of \(N\), and suppose

\[
\gcd(M,N)=1.
\tag{3}
\]

Then every rational prime \(p\mid N\) satisfies

\[
\operatorname{ord}_p(g)=M,
\qquad
p\equiv1\pmod M.
\tag{4}
\]

Therefore (1), with \(s=1\) and \(m=M\), factors \(N\) in

\[
O\!\left(
\left\lceil\frac{N^{1/4}}M\right\rceil
\log^{7+3\epsilon}N
\right).
\tag{5}
\]

In particular, the state is a QP terminal whenever

\[
\frac{N^{1/4}}M=\operatorname{QP}(n).
\tag{6}
\]

Compared with the balanced \(\sqrt N/M^2\) enumeration terminal, (5) has a
smaller search exponent and applies beyond the balanced squarefree promise.
It does not change the asymptotic QP threshold class \(M=N^{1/4}/\operatorname{QP}(n)\),
because numerical-QP functions are closed under fixed powers.

## Theorem 2 — Harvey--Hittmeir stops at beta two on the hard branch

Assume the P159 beta-two branch certifies

\[
\operatorname{ord}_N(2)>C(n),
\tag{7}
\]

where \(C\) is an arbitrary fixed numerical-QP cap. Run Harvey--Hittmeir
Algorithm 3.1 with any \(D\le C\).

If its initial size test does not already return \(2\), then the first loop
base is \(\beta=2\). Lemma 2.1 reports \(\operatorname{ord}_N(2)>D\), and
line 10 returns \(\alpha=2\). The smooth-number stage is not reached.

QP time in (2) requires \(D=\operatorname{QP}(n)\). Taking \(D=N^\delta\)
costs \(N^{\delta/2+o(1)}\) on the current input. A valid one-child recurrence

\[
T(n)\le T(n-1)+\operatorname{QP}(n)
\]

does not alter this conclusion, because (2) is same-node work and supplies no
smaller recursive child carrying the order search.

## Theorem 3 — the direct rank-three interface retains an exponential list

On the balanced-semiprime promise, Gao--Feng--Hu--Pan Algorithm 4.3 uses a
legal integer

\[
72<m<N^{1/4}/2
\]

and a list length

\[
k=\Theta\!\left(\frac{N^{1/2}}{m^{3/2}}\right).
\tag{8}
\]

Thus every legal choice has

\[
k=\Omega(N^{1/8}).
\tag{9}
\]

Its two principal costs are

\[
\varphi(m)log^3N
\quad\text{and}\quad
\frac{N^{1/2}}{m^{3/2}}\log^2N.
\tag{10}
\]

They balance at \(m=N^{1/5+o(1)}\), giving the known
\(N^{1/5+o(1)}\) scale.

For a beta-two-derived P160 unit whose local orders exceed \(C\), the needed
noncollision prefix follows directly from that order bound only if

\[
m^2k\le C.
\tag{11}
\]

But the left side is

\[
\Theta(N^{1/2}m^{1/2}),
\tag{12}
\]

which is exponential in \(n\) throughout the legal range. P161 roughness can
certify the prefix when all exponents are smooth below its cap, but this
requires a cap at least \(k=\Omega(N^{1/8})\). Hence the direct published
rank-three interface does not cross the QP beta-two gate.

## Corollary — an integer-specific low/high small-prime fork

On the balanced distinct-semiprime core \(N=pq\), choose numerical-QP caps
\(B(n),D(n)\), with

\[
\log n\ll\log B=o(n).
\]

Scan the ordinary rational primes \(\beta\le B\). Factor-first order search
through \(D\) gives one of:

1. a proper factor of \(N\);
2. a synchronized exact low order for \(\beta\) in every hidden component;
3. a small ordinary prime \(\beta\) of order above \(D\).

If every scanned prime is in case 2, let \(M\) be the lcm of their exact
orders. Every \(B\)-smooth integer at most a hidden prime \(p\) is then a
root of \(X^M-1\) modulo \(p\), so

\[
\Psi(p,B)\le M.
\tag{13}
\]

On balanced inputs, standard smooth-number bounds give
\(\Psi(p,B)=p^{1-o(1)}\). Thus (6) holds for all sufficiently large inputs,
and Theorem 1 terminates the branch.

Therefore a nonterminal balanced branch contains small *ordinary integers*
of high order; beta two is the first such witness in the P159 hard state.
The theorem does not show that multiple high witnesses generate independent
directions, reveal their exact orders, or factor. A restricted-smoothness or
integer-localization theorem for this mixed low/high branch remains missing.

Canonical residue carries

\[
x_e=[2^e]_N,
\qquad
x_{e+1}=2x_e-c_eN,
\qquad c_e\in\{0,1\},
\]

remain one rank-one orbit modulo every hidden factor. They supply neither a
known residue \(p\bmod m\) for the rank-three method nor the independent
small-integer low-order bank required by the smooth-number branch. No lower
bound against a new carry-sensitive construction is claimed.

## Primary references

- Yiming Gao, Yansong Feng, Honggang Hu, and Yanbin Pan, *On Factoring and
  Power Divisor Problems via Rank-3 Lattices and the Second Vector*,
  Cryptology ePrint Archive 2025/1004,
  <https://eprint.iacr.org/2025/1004>.
- David Harvey and Markus Hittmeir, *Deterministically finding elements of
  large order*, arXiv:2601.11131v2,
  <https://arxiv.org/abs/2601.11131>.
