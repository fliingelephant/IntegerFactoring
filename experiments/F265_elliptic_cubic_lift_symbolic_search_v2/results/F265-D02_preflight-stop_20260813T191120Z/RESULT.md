# F265-D02 preflight-only stop

## Result

The frozen packet authenticated on the remote host. Compilation and the
mandatory self-test passed. Preflight stopped with status `2` because its
projected full-run wall time was `335199.191096s`, which is greater than the
registered `12600s` gate. The preflight JSON records `"pass":false`, and
stderr records `F265_D02_ERROR preflight projection rejected full packet`.

No discovery or held-out cohort was generated or opened. The remote
`output/` directory was empty. The terminal manifest retains
`discovery_status=125`, `selection_status=125`, `heldout_status=125`, and
`summary_status=125`.

This is a resource-feasibility stop. It gives no mathematical conclusion.

## Authentication and transfer

- Local and remote `FROZEN.sha256` SHA-256:
  `26f7940244242edc549a2612fc08120372e0f8fab64a2dca154b69ed02d55d6a`.
- All seven remote frozen entries authenticated against that manifest.
- `logs/` and `preflight/` were copied once with `scp -rp` after the remote
  process had ended.
- All 19 copied files match their pre-transfer remote SHA-256 values.
- `REMOTE_ARTIFACTS.sha256` is the remote hash manifest.
- `ARTIFACT_HASHES.tsv` records byte counts, remote source timestamps, and
  both remote and local hashes.

## Exact chronology

All timestamps below are UTC. The terminal manifest supplies the start and
end seconds. Remote source mtimes supply the finer ordering.

1. `2026-08-13T18:15:31Z`: runner started and recorded resources.
2. `2026-08-13T18:15:31.786019930Z`: frozen authentication output closed;
   every entry was `OK`.
3. `2026-08-13T18:16:04.611373756Z`: remote `search` binary mtime;
   the terminal manifest records `compile_status=0`.
4. `2026-08-13T18:16:04.651375401Z`: self-test output closed with
   `SELF_TEST_PASS`; the terminal manifest records `selftest_status=0`.
5. `2026-08-13T18:16:04.671376223Z`: the preflight stdout file was opened;
   preflight followed the self-test in the frozen runner chronology.
6. `2026-08-13T19:11:20.895581711Z`: all eight preflight artifacts and the
   rejection stderr closed. The terminal manifest records
   `preflight_status=2`.
7. `2026-08-13T19:11:20.915582410Z`: final resource evidence closed.
8. `2026-08-13T19:11:20Z`: terminal manifest end time. Its file closed at
   `2026-08-13T19:11:20.967584230Z`.

No rerun, audit, or ledger update was performed while packaging this result.
