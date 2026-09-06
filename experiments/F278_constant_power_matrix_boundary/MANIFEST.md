# F278 manifest — explicit constant-power matrix boundary

## Status

F278 is a frozen proof-only candidate with an author self-audit. A fresh
hostile audit and an independent statement-only reconstruction are pending.
It is not promoted.

No source code, generator, runner, compilation, local run, remote run,
benchmark, fixture, corpus, empirical result, or durable-ledger edit belongs
to this packet.

## Frozen mathematical artifacts

| File | SHA-256 | Role |
|---|---|---|
| `STATEMENT.md` | `4232a1007700802b25acafed944f7b5adc227a913af26aec8ab6b17a7bdba0fa` | Normative theorems, named-model scope, and exclusions |
| `PROOF.md` | `194461e35d35a82ccea95df3c99ffb76cc414af5852c5fff7c917409a9403073` | Self-contained proofs |
| `SELF_AUDIT.md` | `e38766d07d42cbf7ee60ae3a1762f7e86362c220420bec5026f4ed1a4bc41829` | Author claim, scope, and resource audit |
| `PROVENANCE.md` | `1e1938fb9c49c45e1fdb496f4cef75479c45be7ec2a938e3214e42a6001c3cea` | Prior boundaries and search disposition |

These four hashes freeze the mathematical content. `FROZEN.sha256` also
records this manifest.

## Exact contents

1. Automatic numerical-quasipolynomial evaluation of `C_N^B` for an
   explicit fixed- or quasipolynomial-dimensional public matrix.
2. Exact equivalence of a bounded Jordan/binomial window and the direct
   consecutive-integer near-square scan below `B`.
3. Exact equivalence of clean semisimple powered collision and
   multiplicative eigenvalue-ratio torsion.
4. Exact reduction of a clean quadratic companion coordinate to an ordinary
   unit-group or norm-one-torus order residual.
5. Scoped exclusion of a genuine hidden local Frobenius construction and
   arbitrary `d>=3` additive cancellations from the proved model.
6. Exact Cayley-Hamilton equivalence with public recurrences whose
   coefficients can depend on `N` but are fixed in the exponent index.

## Search disposition

No C++ or numerical search is proposed. The named mechanisms reduce to a
direct near-square scan or multiplicative order residuals. The general
higher-dimensional additive lane remains open and has no exact all-input
signal law in F278.

F278 proves no universal recurrence lower bound and no all-input factoring
algorithm.

Any mathematical change requires a new packet version, new hashes, and fresh
audits.
