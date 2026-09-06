# F280 V2 manifest — additive polynomial-range endpoint repair

## Status

F280 V2 is a frozen additive proof-only repair candidate. It is not
promoted. A fresh hostile audit and a fresh independent statement-only
reconstruction are required.

No V1 byte changes. No source code, generator, runner, local or remote
research run, benchmark, corpus, dataset, empirical result, or
durable-ledger edit belongs to V2.

## Immutable V1 anchors

```text
a3ecad88c09874a5fcbbe5025596561910aeb5330dbe91206fabc2d49d7965db  FROZEN.sha256
0d4a9ad469b961855cf77518b29926dfecaf958884a85b73e17f0ebf6f75016d  STATEMENT.md
6a7871d91a5bd44eb08778633b04f7f0239ded8ca95392481bd6059491c006df  PROOF.md
57292f18bea502f64b50639361492bab6e441a8b339f583658a654998a687533  HOSTILE_AUDIT.md
```

The V1 frozen root and hostile FAIL remain immutable evidence. V2 does not
overwrite or reclassify either one.

## Frozen V2 artifacts

| File | SHA-256 | Role |
|---|---|---|
| `V2_STATEMENT.md` | `36d2323aa63822f23b55b5daa5aa98032592a4c3112040ab6d4bb33427143083` | Normative authenticated overlay and exact statement replacement |
| `V2_PROOF.md` | `9d4e1a7d57c8fe2023f38e83cb42044f0b08d5852145c370b4edd18d2b9c94ab` | Imported-proof anchor and exact endpoint proof replacement |
| `V2_SELF_AUDIT.md` | `70207ee037ae0f6fe1f012e92fc4acfbb3662dc9ec6e494433685ea9d5c1b757` | Author repair and regression audit |
| `V2_PROVENANCE.md` | `80c3fe363f9552845c816b9dc1c9d03bb5471675ad3008e3289658794f0731d6` | V1, hostile-audit, and primary-source provenance chain |

These four hashes freeze the V2 mathematical overlay. `V2_FROZEN.sha256`
also records this manifest.

## Exact repair

V1 used the Harvey--Hittmeir cost comparison at
\(D=N^\delta\) for fixed \(\delta>0\). V2 replaces that range everywhere
it is normative with fixed

\[
0<\delta<1.
\]

For this range, \(D<N-1\) for all sufficiently large inputs. This is
precisely the input-domain condition in Harvey--Hittmeir Theorem 1.1. V2
makes no claim for \(\delta\ge1\).

## Statement-only reconstruction interface

A statement-only reviewer needs exactly:

1. V1 `STATEMENT.md` authenticated by
   `0d4a9ad469b961855cf77518b29926dfecaf958884a85b73e17f0ebf6f75016d`;
2. `V2_STATEMENT.md` authenticated by the hash above.

`V2_STATEMENT.md` identifies the exact V1 block and gives its complete
replacement. No proof file is needed to reconstruct the V2 statement.

## Preserved scope

All other V1 theorems, costs, primary-source hashes, height and primality
claims, synchronized-order and baseline-multiplicity claims, counterexamples,
project-lane boundaries, search methodology, and exact exclusions remain
unchanged.

Any further mathematical change requires a new packet version, new hashes,
and fresh audits.
