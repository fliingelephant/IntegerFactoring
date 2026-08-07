# Fresh hostile re-audit of F43 inverse-quotient descent

## Decision and pinned artifacts

I audited the corrected candidate at these exact SHA-256 values:

- `experiments/F43_inverse_quotient_descent_kill/RESULT.md`:
  `139d11d7858cfdcd40880ddde86ed40316038a94c5269fba6e9be19f547568e2`
- `experiments/F43_inverse_quotient_descent_kill/RUN_MANIFEST.md`:
  `ccae8bc0fcbe8c27f62e4fe1c73bf74af505205f0896a6f299db37c1707c7259`

Both pinned hashes matched before the audit. I read the prior hostile audit in
full. I then checked every requested correction, reconstructed the unbounded
proofs, checked the two counterexamples directly, and verified the retained
artifact hashes and archive hash.

The corrected mathematics is sound. The artifact still has one provenance
contradiction in its manifest. The contradiction does not change any
mathematical result, but it prevents a strict whole-artifact pass.

**FAIL AS WRITTEN.**

## Mathematics that passes

### The map and one-step identity

The candidate now defines

\[
D_N(u)=\frac{uv-1}{N},
\]

where \(v\) is the least positive inverse of \(u\bmod N\). For a unit
\(2\le u<N\), let \(r\) be the least positive inverse of \(N\bmod u\).
Writing \(Nr-1=tu\) gives \(1\le t<N\), so \(v=N-t\) and

\[
D_N(u)=u-r.
\]

The fixed-decrement equivalence is exact. It proves strict descent at every
nonterminal unit state.

### Reverse preimages

The repaired reverse statement is exact:

\[
D_N^{-1}(k)=\{u:k<u<N,\ u\mid Nk+1\}.
\]

For \(v=(Nk+1)/u\), the assumptions imply both missing bounds:

- \(u<N\) gives \(Nk+1>ku\), hence \(v>k\).
- \(k<u\) gives \(Nk+1<Nu\), hence \(v<N\).

They also imply \(\gcd(u,N)=\gcd(v,N)=1\). Thus both complementary factors
are valid preimages. The earlier out-of-domain ambiguity is gone.

### Trajectory bound

For decrements \(r_i=u_i-u_{i+1}\), the total decrease is less than \(N\).
There are at most \(N/B\) steps with \(r_i>B\). For each fixed
\(1\le r\le B\), all current states are distinct divisors of \(Nr-1<N^2\).
Therefore

\[
L\le \frac{N}{B}+B\Delta_N+1,
\qquad
\Delta_N=\max_{m<N^2}\tau(m).
\]

The maximal order of the divisor function gives
\(\Delta_N=N^{o(1)}\). A balanced \(B\) gives
\(L\le N^{1/2+o(1)}\). The candidate now calls this a
near-square-root bound. It also says correctly that it is exponential in the
binary input length.

### Slow chain

For

\[
M_L=\operatorname{lcm}(2,\ldots,L+1),
\qquad N_L=(M_L+1)^2,
\]

one has \(N_L\equiv1\pmod u\) for every \(2\le u\le L+1\). Hence the
trajectory is exactly

\[
L+1\to L\to\cdots\to1.
\]

Its length and the bit length of \(N_L\) are both \(\Theta(L)\). The
candidate correctly limits the conclusion: these inputs are easy perfect
squares, so the family is only a depth warning.

### Contraction counterexamples

Both displayed witnesses are correct:

- \(D_{11}(7)=5\) and \(D_{11}(5)=4\), so \(2\cdot4>7\).
- \(D_{35}(19)=13\) and \(D_{35}(13)=10\), so \(2\cdot10>19\).

The second witness is a balanced distinct semiprime. It closes the scope gap
in the first audit.

## Scope corrections that pass

The candidate now makes the required limits clear:

- It claims unbounded structural mathematics, but it does not claim a
  polynomial-time factoring result or an unbounded success probability.
- It says only that the gcd tickets were sparse on the larger finite D02
  inputs. It does not infer an infinite-family hit bound.
- It leaves a whole-transcript decoder open.
- Its inline mathematics is delimited correctly.

## Provenance that passes

All current hashes stated for retained files match. In particular:

- the failed attempt-2 partial JSON has the corrected hash
  `61a3dd7260425baabacf7a00687c7d6ff477e4c8b821904776a7a42452e67fc6`;
- the compressed attempt-3 archive has hash
  `f0c841388ef87ffae82d70daa566e1f64d354ad20c1288690fc3ea902d2eed79`;
- its decompressed payload has hash
  `92af2cee0e33aabdd70f8ee4a4007a7abfbe613473cf231a84fb9a2f5a8b35e2`;
- the authoritative compact attempt-4 JSON has hash
  `167970dfbb2ed60f489ebac16c59e7448564feb6c2191c31bbac204437bb7fef`;
- every stated D02 and D03 source, runner, log, and output hash matches.

The manifest now states the attempt-3 source limitation explicitly and names
attempt 4 as the sole authoritative D01 computation. It also uses the correct
D02 description, "seeded pseudorandom unit draws," and records Python 3.14.5.
The independent F43-A01 replay from the prior audit remains applicable to the
unchanged data: it reconstructs all D01 compact records, all D02 records, and
the complete D03 summary and stored prefix.

## Mandatory correction

The attempt-2 disposition still says:

> the canonical paths now contain the successful attempt-3 artifacts

This is false after attempt 4. The canonical JSON path now contains the
254,235-byte compact attempt-4 certificate. The full attempt-3 JSON exists
only in the named compressed archive. This sentence also conflicts with the
correct top-level status, which makes attempt 4 authoritative.

Replace the stale sentence with a time-accurate statement. For example:

> Before attempt 3, the exact log was preserved at
> `logs/F43-D01-attempt2.log` and the partial output at
> `output/F43-D01-attempt2-partial.json`. The canonical JSON path now contains
> the authoritative compact attempt-4 certificate. The full attempt-3 JSON is
> retained only in `output/F43-D01-attempt3-full.json.gz`.

For the same reason, the top-level "Recorded objects" line should distinguish
the current compact attempt-4 fields from the complete raw trajectories and
collision groups held only in the historical attempt-3 archive. This is a
clarity correction to the same provenance defect, not a new mathematical
objection.

After this manifest-only correction, the candidate needs one more pinned
whole-artifact check. I found no remaining mathematical correction.
