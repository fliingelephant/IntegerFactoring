# F260-D01 prelaunch manifest

Frozen before any discovery or held-out corpus generation.

| Artifact | SHA-256 |
|---|---|
| `ALGEBRA.md` | `09691b4f5d005a330b85952dd9bfe4a0b93c2e5de7c23832d53572d4db5700a2` |
| `PREREGISTRATION.md` | `3b9c13374e38cba1394e9528fccb5ab623a6164829a3394f434f6b81acf38714` |
| `search.cpp` | `d4263fb8ceef91caecc4480ee3b49d8cd670b6ff34bb0920d8469c47ddf7e44e` |
| `remote_run.sh` | `7215ee1d9e34ee34146ca8ed992e96c582defc0cfd7b40bba39a91b78e98d103` |
| `TARGET_CHECKS/RESOURCE_GATE.md` | `9625226fbb4a188f8cf40fece10a6d152274d4efafb7f1d339222f4e7752c48a` |
| `TARGET_CHECKS/compile_v1.stderr` | `de5d8f2cc69f08850bef2bc6b20366ca2b0245d41b295febdcfc1457903b80d6` |
| `TARGET_CHECKS/compile_v1.sha256` | `18f1d0db3b27e0cabb6abc79ca5a53532bf9bdfe65986c9b13e0832b5dc18465` |
| `TARGET_CHECKS/compile_final.stdout` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `TARGET_CHECKS/compile_final.stderr` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `TARGET_CHECKS/compile_final.sha256` | `19a93f524721be9b02a4ad3da4eea45fd8b8b0f5df0292c54a5ec89b1d568a1b` |
| `TARGET_CHECKS/selftest_final.stdout` | `94ccb142de7a0c8cf6013b7ef6ee94667ceda1cdad0ac3e4741fa652c9cf1732` |
| `TARGET_CHECKS/selftest_final.stderr` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `TARGET_CHECKS/selftest_final.sha256` | `1ffd55966a2b02a6aa72c87f436f834661be532d44119ead4582bd48289c9459` |
| `TARGET_CHECKS/benchmark.stderr` | `5fdf03370ed63b1b2dedd0118d4951d5f133b8c2c8d7070fb8769d90bf137a26` |
| `TARGET_CHECKS/benchmark_final.stdout` | `94fe872025647d6b9d6657b66c7a22a3e117b4c85a03cd20b8034a4b2cb177d6` |
| `TARGET_CHECKS/benchmark_final.stderr` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `TARGET_CHECKS/benchmark_final.sha256` | `2ff18eec6567e11950e46cb4617593575bf769d2a8d969939e870b24d0060321` |

The checked source hash was
`905001a2bc2a06a653bfad68bb22d09f9dee36a78472a288ba305632c5f7f01b`.
The final source differs only by the disclosed selection-fill repair.  It
must be compiled and self-tested again by the production runner before
corpus generation.  This qualification is part of the frozen protocol.

No F260 mathematical run has occurred.  The packet is queued behind the
incompatible F258, F259, and F261 runs.
