# F139 pre-run pins

These hashes were recorded before the authoritative fixed-certificate run.

| File | SHA-256 |
|---|---|
| `PREREGISTRATION.md` | `80db48b2d87ccbdfe2d9661d89a0af97fb9769e55809c66d6122dd04c34a0ae7` |
| `verify.sage` | `87faa9568373ca0915f7aebc19184a23ee957a790025017d8e2b0d03d35a2229` |

The authoritative command is:

```text
gtimeout 300 sage verify.sage
```

Its standard output is stored as `OUTPUT.json`.
