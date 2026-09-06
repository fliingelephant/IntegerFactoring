# F282 manifest — shifted normalized-difference random splitter

## Status

F282 is a frozen proof-only candidate. It is not promoted. A fresh
no-context hostile proof audit and a separate fresh statement-only
reconstruction are required.

No source code, evaluator, runner, local or remote research run, benchmark,
dataset, empirical result, proof-ledger edit, failure-ledger edit, registry
edit, staging action, or commit belongs to this packet.

## Frozen mathematical artifacts

| File | SHA-256 | Role |
|---|---|---|
| STATEMENT.md | 831ac1a429968a20fdeffa2e0c0e7d1972fe43deec3a22e43ee4b71a2d01f0bf | Normative theorem, conditional evaluator interface, and exclusions |
| PROOF.md | 0a5e20cb27f671d5e797196b1a987e776547b2f67be5a2e95af21b663ce69d2c | First-principles proof and bit-complexity boundary |
| SELF_AUDIT.md | f6b27283bc901fcf1959ed9bb393696194f6b4bc740248354cb34a2add52ef3f | Author consistency check; not independent evidence |
| PROVENANCE.md | f2423dffeb2bad01d05f09acb2f6fd1010f599b3cbbb2cb8a7d776680b95d2ed | F277/F281 relationship and no-run provenance |

FROZEN.sha256 is the machine-readable authentication boundary. It records
these four files and this manifest. Later hostile or reconstruction reports
are post-freeze evidence and must not be added to FROZEN.sha256.

## Exact theorem boundary

For \(N=pq\) with distinct odd primes \(p<q<2p\), put
\(B=\lfloor\sqrt N\rfloor\). The direct \(\gcd(B,N)>1\) branch factors.
On the remaining branch, for

\[
 F_B(a)=\frac{\Delta^B X^{2B}|_{X=a}}{B!},
\]

the packet proves:

1. \(F_B(a)=h_B(a,a+1,\ldots,a+B)\) in \(\mathbb Z[a]\);
2. \(F_B(a)=0\pmod q\) for every integer \(a\);
3. modulo \(p\), it is a nonzero polynomial in \(a\) of degree \(s+1\);
4. a uniform shift gives the proper gcd \(q\) with probability above one
   half; and
5. independent repetition needs fewer than two expected trials.

The raw difference \(B!F_B(a)\) is zero modulo \(N\) on the unresolved
branch. The local splitter appears only after exact division by the
factor-bearing nonunit \(B!\).

## Conditional consequence and surviving gap

A uniform numerical-QP algorithm that evaluates \(F_B(a)\bmod N\) from
public \((N,a)\) would yield a classical Las Vegas numerical-QP factorer for
the balanced distinct-odd-semiprime promise. F282 does not construct that
evaluator or its exact normalization.

The theorem gives no all-input factoring algorithm, no reduction of
arbitrary composites to its promise, no result for other composite shapes,
no F281 joint-saturation resolution, and no evaluator lower bound.

## Audit interfaces

The hostile reviewer must authenticate FROZEN.sha256 and every entry, then
reconstruct the branch geometry, divided-difference identity, both local
generating-series arguments, zero-node partial-fraction case, exact leading
coefficient, probability law, normalization boundary, and complexity scope.
The reviewer must not infer an evaluator from the identity.

The statement-only reviewer receives only the authenticated STATEMENT.md.
It must reconstruct the precise theorem, promise, probability, conditional
algorithm, and exclusions without reading PROOF.md, SELF_AUDIT.md,
PROVENANCE.md, or any hostile report.
