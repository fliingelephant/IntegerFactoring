# Monotone reconstruction SHA-256 manifest

All hashes are SHA-256 over the exact file bytes. The manifest does not list a
self-hash because changing the embedded self-hash would change that hash.

| Role | File | SHA-256 |
|:---|:---|:---|
| Supplied statement | `MONOTONE_RECONSTRUCT_STATEMENT.md` | `1cdea0d4292e3f80a54551a3cc5f4c1160cfdf4af2e4ed6a110f35fbeef8936b` |
| Supplied public input | `MONOTONE_RECONSTRUCT_INPUT.json` | `4b1615f7eb4fbb5cb820d51c10c8ce317c919adc0738046db8367ec0398bfa79` |
| Verifier source | `MONOTONE_RECONSTRUCT_verify.py` | `1305f5cf4669d47c5c75a7d3d0855751348d07c19fdfc7558f4b4731f8cf8fa2` |
| Named-timeout runner source | `MONOTONE_RECONSTRUCT_runner.py` | `f29617f2c59c85fbe164014598b53a8c261601bdd0752bb3c42bc08fefc92123` |
| Authoritative output | `MONOTONE_RECONSTRUCT_OUTPUT.json` | `94f3550d27f2a5d6101b648c4e8432a7fb2e6ed9cdb1e12ad5695b70938dd4fd` |
| Authoritative run log | `MONOTONE_RECONSTRUCT_RUN.log` | `cd21ebfc335ea1b0f6eab74ad358f9628e38be923aa000f31281d9cb1cf20b08` |
| Failed-run ledger | `MONOTONE_RECONSTRUCT_FAILED_RUNS.md` | `e903d64a7e0a555c55e3b875a4d89308a9ba88d8ab30acad5f349f3fd4e86345` |
| Proof and result report | `MONOTONE_RECONSTRUCT_REPORT.md` | `138a41f1506ae5a4261e0b390d731f7413efc9232fe366bfedad577f04f9735c` |

The authoritative output status is `PASS`. The authoritative run used the
named 900-second timeout. It exited with code 0 and did not time out.
