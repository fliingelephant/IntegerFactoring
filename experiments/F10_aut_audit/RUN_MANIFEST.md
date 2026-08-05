# F10/X11 hostile-audit run manifest

## Scope and provenance

- Family ID: `F10-aut-audit`.
- Canonical inputs were read only. No file outside `experiments/F10_aut_audit/` was created or edited by this audit.
- Every mathematical execution used the named Sage source `experiments/F10_aut_audit/audit_cubic_automorphisms.sage` and an external timeout. No inline Python, Sage, or other interpreter snippet was run.
- The fresh source uses polynomial remainders, substitution, and basis matrices. It does not import the canonical F10 source or its multiplication routine. It reads canonical `output/R06.json` only to compare the fully expanded symbolic expressions with expressions derived afresh.

The principal read-only inputs and their SHA-256 hashes at audit time were:

| Input | SHA-256 |
|---|---|
| `experiments/F10_autkill/REPORT.md` | `3baf1daebd0a313f0b823d156b813b18dc62ee714bd00e5947e78aea66710147` |
| `experiments/F10_autkill/RUN_MANIFEST.md` | `b998ff8f9ebdb20fb9a33d9550aea5973e20a168db1e8d941959bd287852be31` |
| `experiments/F10_autkill/cubic_automorphism_analysis.sage` | `00d939d1fc224d010387e6f15b127b9f474b35cd5010a190610418435816b147` |
| `experiments/F10_autkill/output/R05.json` | `bd22d06705a965f7e812d7322ec34e6961501f5ac6a202fff3881734330652b1` |
| `experiments/F10_autkill/output/R06.json` | `eb75cfe0e0f2327476d35508eaa09ba652a4215e926dbff75d5311683469ce6c` |
| `FAILED.md` | `5a82268bf3622cded3d70d16cfc7a689839f73919230746b9bc7fefffef62c40` |
| `notes/Progress.md` | `f663e450c002d72a47e48db0c737f4559236a66d808a2706cb3ecd9661912838` |
| `REGISTRY.md` | `b024f1699a010966dcea09aef5a11eb7647e43f5bc6b7615893c3d533e676433` |

## Runs

### A01 — initial comprehensive audit; failed final status serialization

- Exact command:

  `DOT_SAGE=/private/tmp/f10_aut_audit_sage /opt/homebrew/bin/timeout 180s sage experiments/F10_aut_audit/audit_cubic_automorphisms.sage --run-id A01 > experiments/F10_aut_audit/logs/A01.log 2>&1`

- Timeout: 180 seconds.
- Observed wall time: approximately 4.67 seconds.
- Log: `experiments/F10_aut_audit/logs/A01.log`.
- Output written before failure: `experiments/F10_aut_audit/output/A01.json`.
- Disposition: failed, exit status 1. All assertions and the output write completed, but the final one-line stdout summary contained a Sage integer without `default=int`, causing JSON serialization to fail. Because the run ended nonzero and the source subsequently changed, A01 is retained but supports no claim.

### A02 — JSON-safe rerun

- Exact command:

  `DOT_SAGE=/private/tmp/f10_aut_audit_sage /opt/homebrew/bin/timeout 180s sage experiments/F10_aut_audit/audit_cubic_automorphisms.sage --run-id A02 > experiments/F10_aut_audit/logs/A02.log 2>&1`

- Timeout: 180 seconds.
- Observed wall time: approximately 2.03 seconds.
- Log: `experiments/F10_aut_audit/logs/A02.log`.
- Output: `experiments/F10_aut_audit/output/A02.json`.
- Disposition: passed, exit status 0. It checked all canonical compact and expanded equations, exact type counts at 3, 5, 7, and 11, discriminant characters, mismatch probabilities, conjugation orbits, six characteristic-3 scheme fibers, characteristic-3 order-3 constructions, and the independent `N=35` enumeration. It was later superseded by A04 after the source gained additional checks.

### A03 — extended reverse-construction and `N=15` audit

- Exact command:

  `DOT_SAGE=/private/tmp/f10_aut_audit_sage /opt/homebrew/bin/timeout 180s sage experiments/F10_aut_audit/audit_cubic_automorphisms.sage --run-id A03 > experiments/F10_aut_audit/logs/A03.log 2>&1`

- Timeout: 180 seconds.
- Observed wall time: approximately 2.07 seconds.
- Log: `experiments/F10_aut_audit/logs/A03.log`.
- Output: `experiments/F10_aut_audit/output/A03.json`.
- Disposition: passed, exit status 0. It added split-`(111)` transposition interpolation, type-`(12)` Frobenius in characteristic 3, and a fresh exhaustive `N=15` gcd audit. It was superseded by A04 after the source gained primality and lexicographic-first checks.

### A04 — authoritative complete audit

- Exact command:

  `DOT_SAGE=/private/tmp/f10_aut_audit_sage /opt/homebrew/bin/timeout 180s sage experiments/F10_aut_audit/audit_cubic_automorphisms.sage --run-id A04 > experiments/F10_aut_audit/logs/A04.log 2>&1`

- Timeout: 180 seconds.
- Observed wall time: approximately 2.27 seconds.
- Log: `experiments/F10_aut_audit/logs/A04.log`.
- Output: `experiments/F10_aut_audit/output/A04.json`.
- Disposition: passed, exit status 0. This is the authoritative run. In addition to all A03 checks, it proves the named small primes prime and independently repeats the lexicographic searches giving `(u,v,w)=(0,1,1)` at `N=15` and `(0,0,2)` at `N=35`.

## Authoritative artifact hashes

| Artifact | SHA-256 |
|---|---|
| `audit_cubic_automorphisms.sage` | `588c8d18bc1baafdfd722bdfadc52e400ec471b1c60365dd3999356b64442611` |
| `logs/A04.log` | `8eff8e9cd16dbad3f874582951ed67f87ac205f98105bda46eed327614737d15` |
| `output/A04.json` | `9944d77d77e93b4a41dad7bdec46c987146c6ab8bcda68fce7e592b5fb275676` |

Retained superseded/failed artifacts have hashes:

| Artifact | SHA-256 |
|---|---|
| `logs/A01.log` | `fc2feaa40722a41c32dcf4ea96e8f8cc937a426ac0e9d5873ac98ca0011cdb23` |
| `output/A01.json` | `c884d4f4d590e5730b40d929fa9c2b16e68c0761911fde9b882a19370d0146bf` |
| `logs/A02.log` | `ae631ce0120fc65b7a98789ddf73a83a953f5bd8b15f6e2eea5ce219de9f1068` |
| `output/A02.json` | `1231e53fc5168acbfca744c8a64f564c131361c11b5abdee3bfe76506586f42e` |
| `logs/A03.log` | `8dd66610e45bc4c2554f075876bbe54cafad014a945a8164414c2ce20237ea61` |
| `output/A03.json` | `ae1760a3871a248f7d508420de98fbf86e64840ff9c2039b44c962f51211c48d` |

The final read-only hash command was:

`shasum -a 256 experiments/F10_aut_audit/audit_cubic_automorphisms.sage experiments/F10_aut_audit/logs/A01.log experiments/F10_aut_audit/logs/A02.log experiments/F10_aut_audit/logs/A03.log experiments/F10_aut_audit/logs/A04.log experiments/F10_aut_audit/output/A01.json experiments/F10_aut_audit/output/A02.json experiments/F10_aut_audit/output/A03.json experiments/F10_aut_audit/output/A04.json`

## Evidence boundary

The exact computations certify the displayed finite enumerations, symbolic identities, and the characteristic-3 representative ideals. The general theorem in `RESULT.md` is proved mathematically; it is not inferred from the finite samples. A01 is the only failed mathematical run. No run timed out, no output was deleted, and there were no unrecorded inline-interpreter attempts.
