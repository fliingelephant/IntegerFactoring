# Final hostile whole-artifact check of F43 inverse-quotient descent

## Decision and pinned artifacts

I audited these exact files:

- `experiments/F43_inverse_quotient_descent_kill/RESULT.md` at SHA-256
  `139d11d7858cfdcd40880ddde86ed40316038a94c5269fba6e9be19f547568e2`;
- `experiments/F43_inverse_quotient_descent_kill/RUN_MANIFEST.md` at SHA-256
  `c36ee5112f7bb335ab39a938e4774c2bbe57733d85ea8ede68b0424796e2fcb9`.

Both hashes match. I read both earlier hostile audits in full. I then checked
the complete corrected candidate and manifest, reconstructed every unbounded
argument, checked the endpoint conditions, and compared the current retained
files with all hashes stated in the manifest.

The last provenance defect is repaired. I found no remaining mathematical,
scope, or provenance error.

**PASS.**

## Mathematics

The one-step law is exact. If \(v\) is the least positive inverse of a unit
\(u\bmod N\), and \(r\) is the least positive inverse of \(N\bmod u\), then
\(Nr-1=tu\) with \(1\le t<N\). Thus \(v=N-t\), and

\[
D_N(u)=\frac{uv-1}{N}=u-r.
\]

This proves strict descent for every nonterminal unit state. It also proves
the fixed-decrement equivalence in the candidate.

The repaired reverse description is exact:

\[
D_N^{-1}(k)=\{u:k<u<N,\ u\mid Nk+1\}.
\]

For \(v=(Nk+1)/u\), the displayed bounds imply \(k<v<N\). They also imply
that both factors are units modulo \(N\). Thus the complementary-factor
statement is correct, including its separate qualification for square and
non-square cases.

For one trajectory, states with a fixed decrement \(r\) are distinct divisors
of \(Nr-1<N^2\). Splitting the transitions at an integer \(B\) gives

\[
L\le \frac{N}{B}+B\Delta_N+1,
\qquad
\Delta_N=\max_{m<N^2}\tau(m).
\]

The maximal order of the divisor function and a balanced \(B\) give
\(L\le N^{1/2+o(1)}\). The candidate correctly says this is still
exponential in the binary input length.

For \(M_L=\operatorname{lcm}(2,\ldots,L+1)\) and
\(N_L=(M_L+1)^2\), one has \(N_L\equiv1\pmod u\) for every
\(2\le u\le L+1\). Hence the exact chain is
\(L+1\to L\to\cdots\to1\). Its length and the bit length of \(N_L\)
are both \(\Theta(L)\). The candidate correctly limits this result to a depth
warning because these moduli are easy perfect squares.

Both contraction counterexamples are correct. In particular,
\(7\to5\to4\) for \(N=11\), and \(19\to13\to10\) for the balanced
semiprime \(N=35\). Thus the universal two-step contraction claim is false
even in the intended semiprime regime.

## Finite evidence and provenance

The finite claims agree with the retained outputs:

- F43-D01 records 96 semiprimes, maximum depth 13, minima \(14/192\) and
  \(130/220\), and no tested offset menu without an extended hit.
- F43-D02 records six inputs. Its final input has 15 extended hits in 50,000
  seeded pseudorandom unit draws, zero hits in 1,369 offsets, and maximum
  sampled depth 46.
- F43-D03 records 593,870 strict violations among 3,887,362 eligible pairs.

All current source, runner, log, output, and failed-attempt hashes stated in
the manifest match their retained files. The attempt-3 gzip archive has hash
`f0c841388ef87ffae82d70daa566e1f64d354ad20c1288690fc3ea902d2eed79`.
Its decompressed payload has hash
`92af2cee0e33aabdd70f8ee4a4007a7abfbe613473cf231a84fb9a2f5a8b35e2`.
The current compact attempt-4 JSON has hash
`167970dfbb2ed60f489ebac16c59e7448564feb6c2191c31bbac204437bb7fef`
and size 254,235 bytes.

The manifest now gives the failed attempt-2 paths only as preserved historical
objects. It says that the canonical JSON path now contains attempt 4 and that
the full attempt-3 JSON remains only in the named gzip archive. Its top
recorded-object entry makes the same distinction: compact fields belong to
attempt 4, while raw trajectories and full collision groups belong only to
the historical archive. These two statements agree with the retained files.

The attempt-3 section records the output path used at that run. The top status,
the explicit source-snapshot limitation, and the attempt-4 section make clear
that this is historical, not a claim about the current file at that path.
Attempt 4 is unambiguously the sole authoritative D01 computation.

The earlier independent F43-A01 replay remains valid for the unchanged finite
data. Its retained output reconstructs the D01 compact records, D02 records,
and D03 summary and stored counterexamples. Its old failed-partial hash flag
belongs to the earlier manifest version; the corrected current manifest now
states the retained hash exactly.

## Scope

The artifact does not claim a factoring algorithm. The finite runs support no
infinite-family probability or runtime claim. The unbounded contribution is a
structural description of a real ordered descent, a near-square-root depth
bound, and a matching warning family. A whole-transcript decoder remains an
open algorithmic question.

**PASS.**
