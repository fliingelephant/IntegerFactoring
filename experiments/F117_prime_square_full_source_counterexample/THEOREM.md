# F117 exact result: literal source counterexample and intended-domain reduction

## 1. Literal F116 counterexample

Let

\[
p=1{,}000{,}000{,}007,
\qquad
N=p^2=1{,}000{,}000{,}014{,}000{,}000{,}049.
\]

Complete trial division through \(\lfloor\sqrt p\rfloor\) proves that \(p\)
is prime. Also, \(n=\operatorname{bitlength}(N)=60\), \(B=n^2=3600\),
and \(p>B\). Thus every trial gcd for \(2\le t\le B\) is one.

The exact F116 seed basis has 46 blocks and gives 59 frozen pairs. The full
source has

\[
59+59\cdot2(3600+1)+\binom{59}{2}\cdot2(3600+1)
=12{,}747{,}599
\]

attempt occurrences. `verify_full_source_counterexample.py` enumerated all
of them in the specified order. It found no proper residue gcd and no proper
direct sign gcd. Seven occurrences had residue \(1\). Their minus gcd was the
improper value \(N\). Every other sign gcd was one.

The verifier screens every occurrence, including duplicates. This is stronger
than the F116 rule, which skips a duplicate before its screen. Therefore the
zero-proper-screen result also holds for the retained F116 source.

The verifier can test the sign screens without computing every inverse. For a
unit \(c\) and its inverse \(w\), multiplication by \(c\) does not change a gcd
with \(N\), and \(cw\equiv1\pmod N\). Hence

\[
\gcd(c-w,N)=\gcd(c^2-1,N),
\qquad
\gcd(c+w,N)=\gcd(c^2+1,N).
\]

The known prime \(p\) is used only to accelerate this exhaustive
counterexample check. Every possible nonunit case is confirmed with the exact
integer gcd.

For every odd prime \(p\) and integer \(k\ge1\),

\[
x^2\equiv1\pmod {p^k}
\quad\Longrightarrow\quad
x\equiv\pm1\pmod {p^k}.
\]

Indeed, \(p^k\mid(x-1)(x+1)\), while
\(\gcd(x-1,x+1)\mid2\). The odd prime \(p\) divides at most one factor, so
its full power \(p^k\) divides that factor.

Every P66 normalized dependency root is a square root of one modulo \(N\).
It is therefore global for this \(N=p^2\), independent of whether the exact
parity kernel is zero or nonzero. The complete literal F116 source has no
direct factor and cannot have a non-global decoded root. This is an exact
finite counterexample to a claim over all odd trial-hard inputs.

## 2. Scope boundary

P70 states that a full factorization algorithm must handle exact perfect
powers before it uses this source. Thus the counterexample above refutes only
the literal unpreprocessed claim. It does not refute the intended remaining
claim for odd non-perfect-powers.

## 3. Dependency and useful-root conditions are different

For a fixed retained source, let \(M_N\) be its exact P66 parity matrix and
let

\[
K_N=\ker M_N.
\]

The normalized-root map is a homomorphism

\[
\rho_N:K_N\longrightarrow\mu_2(N),
\]

where \(\mu_2(N)\) is the group of square roots of one modulo \(N\). Put
\(G_N=\{1,-1\}\), and compose with the quotient map:

\[
\bar\rho_N:K_N\longrightarrow\mu_2(N)/G_N.
\]

Then:

- An exact-value dependency exists exactly when \(K_N\ne0\).
- A non-global normalized root exists exactly when
  \(\bar\rho_N\ne0\).

The first condition does not imply the second. For a distinct odd semiprime,
\(\mu_2(N)/G_N\) has order two. The whole missing root claim is therefore
that one binary functional on \(K_N\) is nonzero. A rank defect alone proves
only that the functional has a nonempty domain.

## 4. Reduction to deterministic polynomial-time integer factorization

Define the intended full-source assertion as follows.

> For every odd composite non-perfect-power \(N\), after trial division
> through \(B=n^2\), the complete fixed F116 source either gives a proper
> direct gcd or satisfies \(\bar\rho_N\ne0\).

If this assertion is true, then worst-case integer factorization is in
deterministic polynomial time.

Proof. Remove factors of two. Use deterministic primality testing and exact
perfect-power detection. Trial-divide through \(n^2\). On every remaining
composite, enumerate the fixed source. It has \(O(n^4)\) attempts. Every
retained relation value is less than \(N^2\), so the complete explicit P66
input has \(O(n^5)\) bits. Run P66, test a kernel basis, and use the asserted
proper direct gcd or non-global root to split \(N\). Recurse on the two proper
factors. The factor tree has \(O(n)\) nodes. Every step has polynomial bit
cost. Therefore the full factorization has deterministic polynomial bit
cost. \(\square\)

This is a one-way reduction. A proof of the intended universal F116 source
claim would resolve the named open problem `integer factorization in FP`. An arbitrary
polynomial-time factoring algorithm would not make this specific source
property true.

## 5. Named computation artifacts

- Timeout: `F117_FULL_SOURCE_COUNTEREXAMPLE_HARD_TIMEOUT`, 600 seconds.
- Verifier: `verify_full_source_counterexample.py`.
- Runner: `run_with_timeout.py`.
- Log: `RUN.log`.
- Output: `OUTPUT.json`.
- Result: `PASS` in 6.719060 wrapper seconds.
- Attempt-sequence SHA-256:
  `97b156a3434cb597cac377f8858c286c04a665e3a921f0f668c295204db85326`.

Artifact SHA-256 values:

- Verifier:
  `b6ff35851b514c624eded4781ead54f0ff8ed41e3569a460bc20030dd5365906`.
- Runner:
  `5f9a0cacb3afe33a83db48d4cfa72459d060631856b707484f1abf6af1c143fc`.
- Log:
  `ed7991f546407b9a37da8910551a1ae66e2ecc78c03e1b9aa180a688b48b3dfe`.
- Output:
  `b1c762efabda5863946d63ab6cdf6508b0522e8b3e78e40230408d567fb48664`.

No durable ledger was edited.
