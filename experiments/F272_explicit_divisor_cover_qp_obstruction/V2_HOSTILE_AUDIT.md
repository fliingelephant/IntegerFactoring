# F272 V2 hostile audit

## Verdict

**PASS.** I found no false inequality, quantifier slip, omitted edge case,
invalid exponent transfer, output-model overclaim, citation-scope leak, or
fault in the interval-product reduction in the authenticated V2 packet.

The result remains a proof-only obstruction. It does not provide an
interval-product evaluator or an integer-factoring algorithm. It also does
not rule out succinct, adaptive, compressed, or unrelated factoring
mechanisms.

I did not edit a frozen input or a durable ledger. This report is the only
file created by the audit.

## Authentication

I authenticated the freeze file and all five assigned V2 files before
auditing their contents. Every digest matched the required value.

| File | Required and observed SHA-256 |
|---|---|
| V2_FROZEN.sha256 | 92cc4fdd65aab4345f39b4edca112cb5345debd1c003a197612459431c4eb795 |
| V2_STATEMENT.md | 1b6c52624e5f957b2814f5e3e98572612e7cf9312b167ed117e01dddf0d4abb5 |
| V2_PROOF.md | 671c6810a753791fa7c08e3c8eec89b68a0b9fa64fc129d7263130a2b19b67d8 |
| V2_SELF_AUDIT.md | bac1638fd459b0bd3d5b3f8dc0dd022e92a1e50afbcb0ab7cafdfccc3458ada7 |
| V2_PROVENANCE.md | 32c5e939f057b9c449b5df6fd1fcdfcadd43d4e66c10fad843d82ec172568616 |
| V2_MANIFEST.md | 935e0131301a6b17806af2cf7342791b5dd049e10802765b5f3f1a25b0aebae2 |

The six preserved V1/blind files also match the immutable hashes in the V2
manifest. In particular, the V1 statement and blind reconstruction have
hashes

    103722d5cf46884678867fd093e1ce5bcef9d57a797275c0f0e3c262615d67d0
    4be8415b7dd33e26a8a75f893b7a89d99d763ad2ce7ee3f0f72fe1f3665c9500

so the repair comparison below is against the declared V1 bytes.

## Rank-free mass and representation edge cases

For each prime \(p\leq X\), the divisor property supplies a positive
difference divisible by \(p\). Hence the product of all such primes divides

\[
\prod_{d\in D}d.
\]

Taking logarithms gives the first inequality in (7). Each positive \(L\)-bit
difference is strictly below \(2^L\), which gives

\[
\vartheta_2(X)\leq\sum_{d\in D}\log_2d<ML.
\]

No additive representation or rank property enters this argument. Since
\(M\leq K\leq |S||T|\), (8) follows. A fixed quasipolynomial in
\(n_X=\Theta(\log X)\) is \(X^{o(1)}\), so a fixed product of the three
claimed quasipolynomial bounds contradicts
\(\vartheta_2(X)=\Omega(X)\) along every unbounded sequence.

The representation edge cases do not evade the proof:

- Replacing multisets by their supports preserves all available differences
  and can only reduce the displayed cardinalities.
- Taking absolute values preserves divisibility by positive integers.
- Excluding zero is necessary; admitting it would make the cover property
  vacuous. The \(X\geq2\) property makes \(D\) nonempty, so \(H\) and \(L\)
  exist.
- Collapsing repeated differences loses no coverage. Repetition only adds
  calls in the output argument.
- The value one contributes zero logarithmic mass and has one-bit length.
- If endpoint magnitudes are below \(2^B\), every nonzero difference is
  below \(2^{B+1}\), exactly as required for (9).

## Explicit output, time, dictionaries, and prime separation

Invoking the literal factor-output procedure on all \(K\) nonzero ordered
pairs causes the binary name of every prime \(p\leq X\) to appear in at
least one output. Therefore the prime-name bits alone have aggregate length
at least \(\vartheta_2(X)\), proving

\[
K F_{\rm out}\geq\vartheta_2(X).
\]

On a fixed sequential bit machine, at most \(C_0\) output bits are written
per step. Thus the time conclusion is correctly weakened to

\[
K F_{\rm time}\geq\vartheta_2(X)/C_0=\Omega(X).
\]

The proof does not apply this exact per-call formula to a different output
contract. Dictionary references fail the literal binary-pair hypothesis. If
a shared dictionary materializes the prime names, charging it restores only
the stated aggregate mass bound. A compressed decoder that never
materializes those names remains outside the theorem.

For the static prime-separating bank, separation makes all prime codewords
distinct. Hence \(2^m\geq\pi(X)\), at most one prime has the zero codeword,
and every other prime name occurs in some explicit factorization. Subtracting
at most \(\log_2X\) for the possible missing prime proves (24) and, with the
same fixed write-rate constant, (25). Negative \(A_i\) do not change positive
prime divisibility; zero is excluded. The static and explicit-output scope is
stated and does not reach adaptive banks or compressed decoders.

## Prime-pair incidence and exponent deductions

For one difference \(d\), let \(r(d)\) be the number of distinct band primes
that divide it. Their product divides \(d\), so

\[
(a\sqrt X)^{r(d)}\leq d\leq H,
\qquad r(d)\leq h.
\]

Every distinct band pair has product at most \(b^2X\leq X\), and is therefore
covered by at least one difference. A difference containing \(r(d)\) band
primes covers exactly \(\binom{r(d)}2\) such pairs. Counting with possible
multiple coverage gives the claimed direction

\[
\binom v2
\leq\sum_{d\in D}\binom{r(d)}2
\leq M\binom h2.
\]

This also handles \(v<2\). If \(h<2\) when \(v\geq2\), the inequality itself
rules out the cover.

Under the positive-height hypotheses, \(H<\max(S\cup T)\), so
\(\log H\leq X^{\alpha+o(1)}\), while
\(M,K\leq X^{2\beta+o(1)}\). Prime mass then gives
\(\alpha+2\beta\geq1\). A fixed square-root prime band has
\(v=X^{1/2+o(1)}\) and \(h\leq X^{\alpha+o(1)}\), so incidence gives
\(\alpha+\beta\geq1/2\). Fixed-machine output mass similarly gives
\(\gamma+2\beta\geq1\). At \((1/3,1/3)\), only the first constraint is
saturated; the second has strict slack.

## Citation boundaries

The two literature claims are isolated from the internal proof and are
source-accurate.

- [He--Sahai](https://arxiv.org/abs/2608.06681) prove the quoted
  \(\Omega(X^{3/4}/\sqrt{\log X})\) length lower bound for a positive
  one-dimensional divisor arithmetic progression when
  \(\log H=o(\sqrt X)\). Their scope discussion says that this does not
  disprove the higher-rank Strong Divisor Conjecture and identifies the
  at-most-one-intersection step that fails to transfer automatically.
- [Umans--Wang, Theorem 5.5](https://arxiv.org/abs/2511.10851) states that
  the Strong Prefactored \((\alpha,\beta)\)-Divisor Conjecture implies a
  deterministic complete integer-factorization algorithm in
  \(\widetilde O(N^{\max(\alpha,\beta)/2+o(1)})\) time. Substitution at the
  one-third point gives \(N^{1/6+o(1)}\), not quasipolynomial time in
  \(\log N\).

V2 treats both as imported statements, not as consequences of its elementary
mass or incidence proofs. Its local F197 reference is also boundary context:
it records published upper bounds for named factorial methods, not a general
lower bound. None of these citations is a premise of Theorems 1--3.

## Succinct interval-product evaluator reduction

Assume the uniform evaluator in (26). A deterministic primality test handles
prime inputs. For composite \(N\), a least prime factor is at most
\(X=\lfloor\sqrt N\rfloor\), so

\[
\gcd(E(1,X,N),N)>1.
\]

If this gcd is proper, the reduction is done. If it equals \(N\), the exact
product of the current interval is divisible by \(N\). For a split
\(I=I_0\sqcup I_1\), let \(P_i\) be the exact child products. If
\(\gcd(P_0,N)=N\), descend to \(I_0\). If it is one, \(P_0\) is invertible
modulo \(N\), and \(N\mid P_0P_1\) forces \(N\mid P_1\), so descend to
\(I_1\). Every other gcd is proper.

Balanced splitting has depth \(O(\log X)\). The invariant cannot hold at a
singleton, since it would require \(N\mid j\) with \(1\leq j\leq X<N\).
Thus a proper divisor must appear. This logic covers even composites, prime
powers, repeated factors, and arbitrary composites; it uses no
squarefreeness or balance promise.

Recursive splitting plus deterministic primality testing yields prime
leaves. Equal prime leaves can be collected into exponents. There are at
most \(\log_2N\) leaves and fewer internal nodes. Each node uses
\(O(\log N)\) evaluator calls on \(O(\log N)\)-bit endpoints and moduli;
gcds, square roots, primality tests, division, and output aggregation add
only polynomial bit cost. Multiplying a fixed quasipolynomial evaluator
bound by this polynomial number of calls remains quasipolynomial. The
reduction is therefore a valid one-way Turing reduction from factoring to
the evaluator. Calling the evaluator factoring-hard, while declining an
equivalence or uniqueness claim, is exact.

## V1 blind defects

Each V1 blind defect is repaired in substance throughout the V2 statement,
proof, self-audit, provenance, and manifest.

| V1 blind finding | V2 repair | Result |
|---|---|---|
| Both exponent constraints were called tight at \((1/3,1/3)\). | Only \(\alpha+2\beta\geq1\) is called saturated; \(2/3>1/2\) is explicit. | repaired |
| Output length was transferred to time with a constant-free exact bound. | V2 separates \(F_{\rm out}\) from \(F_{\rm time}\), introduces fixed \(C_0\), and uses an \(\Omega\) time conclusion. | repaired |
| A succinct product hierarchy was presented as the unique surviving route. | V2 calls the interval evaluator one sufficient interface and lists adaptive, compressed, succinct, and unrelated alternatives outside scope. | repaired |
| "Factoring-equivalent" overstated the one-way evaluator reduction. | V2 proves and claims only factoring-hardness and expressly denies a reverse reduction. | repaired |
| The named literature claims were not internal consequences. | V2 puts them in an external-source boundary, marks their use conditional, and the attributions agree with the primary papers. | repaired |

The blind report's further qualifications about dictionaries, static banks,
multisets, signs, zero, and named-method scope are also explicit in V2. No
unchanged V1 defect remains, and no correction weakens a core inequality.
