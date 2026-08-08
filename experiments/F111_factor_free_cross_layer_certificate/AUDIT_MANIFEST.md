# F111 Hostile-Audit Manifest

## Scope and result

- Verdict: PASS.
- Candidate directory: `experiments/F111_factor_free_cross_layer_certificate`.
- Regeneration inputs: (N) and `CERTIFICATE.json` only.
- Algorithm specification read: the SHA-256-pinned F98 public-basis source.
- F109 or F110 artifacts read: none.
- Private factor files or endpoint prime factorizations read: none.
- Candidate files edited: none.
- Certificate boundary: the fixed indices verify existence; they are not a selector.

## Final run

```text
command=/opt/homebrew/bin/python3 experiments/F111_factor_free_cross_layer_certificate/audit_run_with_timeout.py
working_directory=/Users/zhou/autoresearch/IntegerFactoring
hard_timeout_seconds=60
outer_elapsed_seconds=0.348110
inner_elapsed_seconds=0.30216533300699666
timed_out=false
exit_code=0
status=PASS
audit_verdict=PASS
```

## Frozen candidate SHA-256

| File | SHA-256 |
| --- | --- |
| `DESIGN.md` | `cd78bb9d5ff030d2fbfff4dc1191e3a1603694351bf423254dbd1ed9e3864b31` |
| `FAILED_RUNS.md` | `727d794adb41bc14425786746d0b9a809c19312765fad3f69ac890c027b59949` |
| `run_with_timeout.py` | `9a87f000d1e20880f68b2304fad53d67e41cc2e5c766d40f0633c0540b137145` |
| `replay_public_certificate.py` | `c5028a63de7952a5e85c388af4254365d990c3514d846dd35806f87a2a36a6dc` |
| `RUN_MANIFEST.md` | `c01f1de370470a7f535e7e314874ed665e8add6f72107e0fabd728fa0c26c087` |
| `CERTIFICATE.json` | `735a8535eb8cd4e8bc5e1c0fbc71d78b3acd79b3e6efa1f865d9084dea67cf6b` |
| `OUTPUT.json` | `3f23f28ea3e4e0c36dfa83b1d50ea63b8da9e6a8ca5da43982c89514b70f300a` |
| `RUN.log` | `afe4e0851f9fb34ebc39f51d92dd2f8790a4bd9aaefd7941624ed6c8861a4ebf` |
| `RESULT.md` | `0429cafb988f0b5973420ad59bfd62bf983118f543e7b42d15d8ebd261b6d4d3` |
| `../F98_multiseed_presentation_closure_kill/public_factorization_free_replay.py` | `5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b` |

## Audit SHA-256

| File | SHA-256 |
| --- | --- |
| `independent_certificate_audit.py` | `794c5141d709942894bfa0c45454d25506d9395d87161d8a9f57e21c5785fe38` |
| `audit_run_with_timeout.py` | `7d5ad05d0524d8c6f71a5dffc7107c3aeb9d3c87d29405b5ee7c991a5f519b43` |
| `AUDIT_OUTPUT.json` | `5b6f4e8c3c52f429c38d2412ade00748b8e3abc20da43e22dd79e02cc08d6a19` |
| `AUDIT_RUN.log` | `c514d26fdafde9ac55727b8b2d274abfa65101608ac80eca3e768eba0f901f3d` |
| `AUDIT.md` | `2e69899f21fc809fdbb285e3591db18e36ee5120c7ec5604533b3e36ed080534` |

## Preserved audit failures

These failures are audit-tool failures. They are not candidate failures.

| File | SHA-256 |
| --- | --- |
| `AUDIT_FAILED_20260808T031046339104Z_EXIT_1.json` | `8bdacb3f1ebe5fde9787332f0dd4870669432cc354ff149e0cb789ce0b107e0f` |
| `AUDIT_FAILED_20260808T031046339104Z_EXIT_1.log` | `9eab1f1e21610675e03c8fe42323018162d98257b10aa5c6b65665fcc837e04c` |
| `AUDIT_FAILED_20260808T031120635333Z_EXIT_1.json` | `b32fad27d03811ae0622bc14b1ce46d8139acdc0cfa47d9abfe57b1922b37818` |
| `AUDIT_FAILED_20260808T031120635333Z_EXIT_1.log` | `a63910d1cdd35cd97f2b2bf6f6bf659b2af4add77ba36ce8140ebf32b73767e8` |
