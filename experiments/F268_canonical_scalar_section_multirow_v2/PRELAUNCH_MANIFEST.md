# F268-D02 prelaunch manifest

## Identity

- Experiment: `F268-D02`
- Parent: immutable failed `F268-D01`
- Family: fixed canonical `t=0` scalar-section power residues with complete
  low-support classification and retrospective P66 decoding
- Status: `STATIC_FROZEN; FRESH_HOSTILE_AUDIT_PENDING; TARGET_VALIDATION_PENDING`
- Search result: none
- Dynamic work: forbidden before the frozen hostile audit passes and every
  F265 process has ended

F268 is finite heuristic guidance. It is not an integer-factoring theorem or
an asymptotic success claim.

## Narrow D02 repair

D01 was frozen at manifest root
`b99d47d7ba7a01c456a0b755a5e77f42a237be73ffd6ea422e38d03b076a1cc9`.
Before any compilation or run, its author found that `label_audit.cpp` used
`std::tie` without directly including `<tuple>`. The immutable D01 failure
record hashes to
`8ab91efa95e1aa20f0985f80c28790340987d4b61f3bbb662707587a4b2642c2`.

D02 adds that standard header, changes the packet/output version token, and
adds `PROVENANCE.md`. Its algebra, family syntax, seed, grammar, cohorts,
screens, ranks, caps, and resource sequence are unchanged. D01 generated no
corpus or numerical output.

## Exact nonduplicate seam

The P66 inputs are only

```text
U_E(a) = [a^E]_(N^2),  Y_E(a) = [a^(E/2)]_N,
E in {N-1,N+1,N^2-1,2(N-1),2(N+1)}.
```

The public source fixes the canonical `t=0` section. It has no fresh
principal lift coordinate. P211/F247 and P213/F248 bound fresh principal
coordinates and leave this fixed retrospective multirow interface open.
P212/F245 studies fresh inverse quotients and torus words. P66/P138 supply
decoding/section results but no row source. F262, F264, F265, and F266 use,
respectively, polynomial, matrix, elliptic-cubic, and quadratic-form rows.
F26 uses canonical inverse endpoint carries. F268 tests those carries only as
direct controls; none enters P66.

## Freeze-critical chronology

For every bank the source:

1. completes the factor-blind source grammar and every stage-1 gcd;
2. completes direct stages 2 through 4 without changing the retained rows;
3. tests every singleton and unordered pair for an exact rational square;
4. serializes every useful low-support factor certificate;
5. inserts only verified `GLOBAL_PLUS` or `GLOBAL_MINUS` vectors into the
   low-support basis;
6. authenticates the complete factor-free P66 kernel; and
7. only on the no-useful branch, extends the global-decoy basis to the kernel
   and tests residual representatives, each of support at least three.

A later P66 or evidence cap cannot erase a completed useful singleton or
pair. The packet preserves the complete low-support evidence, keeps the bank
`RESOURCE_REJECT`, and excludes it from eligible and null counts.

## Staged scale and resource gate

Discovery evaluates all 12 families at 20/24 rows. Heldout evaluates only the
four authenticated selected families at 45/48 rows. With all bounded marker
controls present, the exact conservative scale is:

```text
banks                                      3,440
row powers and singleton tests           110,224
unordered row-pair bundles             1,942,040
stage-3 pair gcds                      15,536,320
support-two squareclass tests           1,942,040
```

F265-D02 measured 2,369,895 pair bundles in 3,316.220420 wall seconds, or
714.637358152448 bundles per wall second. The compiled F268 floor is therefore
5,435.036324 seconds after the factor-two safety multiplier. The target gate
uses the maximum of this floor, the measured pair-scaled projection, and the
measured task-scaled projection. It adds twice complete corpus-generation
wall time and gates at 12,600 seconds, 3.5 GiB RSS, and 768 MiB output.

Preflight uses the largest real case in every available shape and all twelve
families. Ordinary samples use the heldout 45/48-row layouts. It executes and
replays source construction, every row power, every singleton, all eight
stage-3 gcds per pair, every support-two test, P66, the quotient, and
serialization. A pass requires exact count identities, zero resource rejects,
and a completed 48-row bank.

## Frozen source hashes

| File | SHA-256 |
|---|---|
| `ALGEBRA.md` | `7ca8d31d0d352d885d323a5dc1f755e8371d39dc1f6cfc58729330e3caf76626` |
| `PREREGISTRATION.md` | `ac5b674cf96f3dbab59f1813cb6ab89c7e97911a021f30f16a4ba9665a5320df` |
| `FAMILY_SYNTAX.tsv` | `aea7c29e0c077c701ba8201ec6acb6ff8ca26adbccf1e3096f97b659604bc6ce` |
| `corpus.cpp` | `d86b9c14149dacf316326b81965c2d56543a138b409a040307477564790ef42c` |
| `search.cpp` | `b6c96a58f8064b0d3efad8f4f74fa84a70e778a42e24f65f84820f36aba642ee` |
| `label_audit.cpp` | `b511548de92d4ad3a26a925597f122c42e55553a025fc9268c42b7572638e2eb` |
| `remote_run.sh` | `2a6bcffc54684bed54fcea75852346d9fbffd9b8934b983e9775b48a76cd9fa4` |
| `PROVENANCE.md` | `51cf2f5b64f017b2cb0b87ad2590b31c10bb21a29704e0f08e0b422bcc5f1063` |
| `AUDIT_REQUEST.md` | `e48f1077917c00da0282ecf0be32c6d88694b429597b5fb4a0854c7e32f266bc` |
| `VALIDATION_PENDING.md` | `9ac18d8362d8045e1e9b28097a519cf224e06dcd67e3f2e74815b133b5aea5a0` |

## Static checks completed

- The exact family-syntax bytes hash to the digest compiled into C++ and the
  runner.
- `FAMILY_SYNTAX.tsv` advertises the real split semantics and 45/48 maxima.
- Discovery ranking has an arithmetic-only interface and no case metadata.
- The search `Case` has no factor or marker fields.
- The label auditor is a separate post-heldout C++ process and checks mode
  0600, factor construction, marker conditions, and exact marker shortfalls.
- `label_audit.cpp` directly includes `<tuple>` before using `std::tie`.
- The D01 manifest and post-freeze self-audit failure were authenticated.
- `bash -n remote_run.sh` passed.
- `git diff --check -- experiments/F268_canonical_scalar_section_multirow`
  passed.
- `remote_run.sh` is executable.
- No durable research ledger was edited by this packet author.

No C++ compilation, self-test, corpus generation, preflight, local search,
remote command, discovery, or heldout evaluation occurred. Static inspection
does not establish C++ syntax or runtime correctness.

## Frozen inputs

`FROZEN.sha256` authenticates exactly the ten files in the source-hash table
above plus this manifest. The manifest cannot list its own digest. The
coordinator supplies the SHA-256 of the exact `FROZEN.sha256` bytes to the
fresh auditor out of band.

The hostile audit writes only `HOSTILE_PRERUN_AUDIT.md`, which is a post-freeze
artifact. The runner requires exact `PASS` and manifest-digest lines before it
creates a target or compiles.

## Kill gates

Any digest mismatch, algebra assertion, source exhaustion, registered cap,
corpus failure, preflight reject, count mismatch, projected-resource excess,
selection mismatch, evidence replay failure, label-audit failure, output-cap
crossing, deadline, or visible F265 process stops the exact packet. A failed
gate stays attached to these bytes. It does not authorize an unchanged rerun
or a silently reduced bank.
