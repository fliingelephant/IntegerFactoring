# F116 full-source corollary reconstruction SHA-256 manifest

Each hash is SHA-256 over the exact file bytes. This manifest has no embedded
self-hash because adding that value would change the file being hashed.

| Role | File | SHA-256 |
|:---|:---|:---|
| Supplied statement | `FULL_SOURCE_COROLLARY_RECONSTRUCT_STATEMENT.md` | `dacb0f606313045ce3f0e7b6ff75433bad437ac2b372056f71a021cfce5dce1b` |
| Supplied public input and advice | `RECONSTRUCT_INPUT.json` | `5194ee596916810edb78fa802c3179341746423c6fb65f2548a600c598b05015` |
| Reconstruction source | `FULL_SOURCE_COROLLARY_RECONSTRUCT_verify.py` | `fc667ff1976eebd1d6ab1966e7d598a72d8d0121bba5047966b8be8bea140656` |
| Named-timeout runner source | `FULL_SOURCE_COROLLARY_RECONSTRUCT_runner.py` | `f72f0488054518be87f64c68eb8f79bddc46a3400d1896718379d0487bfe8a1d` |
| Authoritative output | `FULL_SOURCE_COROLLARY_RECONSTRUCT_OUTPUT.json` | `0c1fdcbf734592fee9b9f7722816f5cbfbee6f00d53bc8a6fa1fc8d8b8fb0ca1` |
| Authoritative run log | `FULL_SOURCE_COROLLARY_RECONSTRUCT_RUN.log` | `24406cce701f1bc1700e33c4227e48a4b631d40aed64781d1bbc1dbe6b299bd9` |
| Failed-run ledger | `FULL_SOURCE_COROLLARY_RECONSTRUCT_FAILED_RUNS.md` | `7057211deaad6d2b151df5f92e450224c16f2b2451154fbf2ffdc5a134e3933c` |
| Proof and result report | `FULL_SOURCE_COROLLARY_RECONSTRUCT_REPORT.md` | `8e64015edf3dbd2df9002edbed7c81324d88ea8decc91cf114f9d06527e8e34f` |

The authoritative output status is `PASS`. The run used the named 900-second
timeout. It exited with code 0 and did not time out.
