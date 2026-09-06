# F268-D03 failed-run manifest

packaged_utc: `2026-08-13T20:33:11Z`

remote_source: `/root/autodl-tmp/F268-D03_source_20260814T0416Z`

remote_target: `/root/autodl-tmp/F268-D03_run_20260814T0416Z`

local_package: `experiments/F268_canonical_scalar_section_multirow_v3/results/F268-D03_remote-validation-fail_20260814T0416Z`

Remote file times below use `+0800`. The raw target files were copied with
timestamps preserved. Every local SHA-256 was checked against a remote
`sha256sum` taken before the copy.

## Frozen source authentication

The exact remote source mirror matched the local frozen source for every file.
The exact `FROZEN.sha256` bytes have SHA-256
`19e856152caebdddc374c72444acc5f1bbd727a9c722e0e183ee2f6c70cf720f`.

| Source file | SHA-256 |
|---|---|
| `ALGEBRA.md` | `e372c8953ccdaec003b2db7885083c713ec065af73a38caa2373dbfe7d41af1b` |
| `PREREGISTRATION.md` | `919888209364123d8530af6b3e0e9023443fb08766a9c36b0c3048a691fc9523` |
| `FAMILY_SYNTAX.tsv` | `aea7c29e0c077c701ba8201ec6acb6ff8ca26adbccf1e3096f97b659604bc6ce` |
| `corpus.cpp` | `00b987833a508a939d4b17e798bd439839769d35a51699e43ae49c747362c822` |
| `search.cpp` | `184c1e25545a7922c5ba8c203fff5e728bee636d2d3a67515733daf6041e7bb6` |
| `label_audit.cpp` | `948753dca0d30880094b4244d99718c275742df0c5da3777dcbc0301101bc108` |
| `remote_run.sh` | `49788f707eb47798de30bcb2db554cf4fb5a9476f30defb56bd2628824a82b3a` |
| `PROVENANCE.md` | `068244ca314db5e8eef242b637a6820e214a0d2a4ab647f404ca11173c82e31b` |
| `AUDIT_REQUEST.md` | `80123b75bcc401c7937c4db38cb3a8e1b62bdb991dff1f64e98476f49a99ea74` |
| `VALIDATION_PENDING.md` | `1b8fbec12e6c94fca569d890dfb41ea0cee0c5ae0f61686335e32c79cc6b880a` |
| `PRELAUNCH_MANIFEST.md` | `ca88ce44b11ef31df7d0af27985d1f20182b103ee35f3a17c39b573bb2afe997` |
| `FROZEN.sha256` | `19e856152caebdddc374c72444acc5f1bbd727a9c722e0e183ee2f6c70cf720f` |
| `HOSTILE_PRERUN_AUDIT.md` | `23a3e7921fa54ee1c7048ed7fc05b116f61ee76b88af2fb2275d7b13f8bd3a04` |

## Copied target artifacts

| Remote modification time | Bytes | Local path | SHA-256 |
|---|---:|---|---|
| 2026-08-14 04:26:48.467708110 +0800 | 0 | `logs/compile_corpus.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 2026-08-14 04:26:48.467708110 +0800 | 1768 | `logs/resource_before.txt` | `84b1bbeef5e696ccbeaf37ca4c308d78b66170518eccb06fd7c414bd80518e3f` |
| 2026-08-14 04:26:52.596087518 +0800 | 65928 | `bin/f268_corpus` | `0d42f0645e1f537998ebe73b34ea9233dd98f9274afeab6006f9e2f2fd1351fc` |
| 2026-08-14 04:26:52.604088252 +0800 | 0 | `logs/compile_search.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 2026-08-14 04:27:37.208074566 +0800 | 481080 | `bin/f268_search` | `ed54b210b419d47f585768aad9e1711dd4a9b8c457d58be6bf2d7094734f1533` |
| 2026-08-14 04:27:37.216075263 +0800 | 0 | `logs/compile_label_audit.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| 2026-08-14 04:27:45.872825864 +0800 | 94952 | `bin/f268_label_audit` | `7c13a7950067611137b0ef68a9534ff3730d4a94f9d1b75096262171cfecee1a` |
| 2026-08-14 04:27:45.892827591 +0800 | 22 | `logs/corpus_self_test.log` | `3f6d2b83c1f92f15a77a542be7c1d5cc7e0c1dae3478b0ab3b6711251bae6b8c` |
| 2026-08-14 04:27:45.904828627 +0800 | 45 | `logs/search_self_test.log` | `4804995e04fa8d9454188f643a95e66b02edbb10a03c6758c7d4e569699de25a` |

The copied package also contains an empty `preflight/` directory, matching the
remote target. No `label_self_test.log`, corpus, preflight result, discovery,
heldout, final hash list, or success marker exists.

## Copied environment evidence

These are full raw log snapshots. They were copied after the failed run.

| Remote modification time | Bytes | Local path | SHA-256 |
|---|---:|---|---|
| 2026-08-14 04:26:36.166566699 +0800 | 48086 | `environment/history.log` | `da2ded84bbd092028e46539f1b0d17b2cb66dba19d56488bc692369325bc1535` |
| 2026-08-14 04:26:36.146564831 +0800 | 468389 | `environment/dpkg.log` | `35188134e78730d01f3556a3bdbe0a13b899cc4de276438369dfdb3b7cd1d644` |

`environment/history.log:558-561` records `apt-get install -y time` and package
version `1.9-0.1build2`. `environment/dpkg.log:6665-6673` records unpacking,
configuration, and installed status at 04:26:36 +0800.
