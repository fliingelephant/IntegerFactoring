# F138 preserved non-authoritative runs

## Accidental syntax-check execution

The command intended as a parse check loaded and executed `verify.sage`.
It completed with `PASS` before `PRE_RUN_PINS.md` existed. The output is
preserved as `UNREGISTERED_SYNTAX_CHECK_OUTPUT.json` with SHA-256

```text
900aec82966ab9d082095f038e3dff3aabef560fd1d1641bb1a434e02aac0462
```

It is not used as evidence. The preregistration and verifier already existed,
their hashes were computed before that command, and neither file changed.
The authoritative run occurs only after `PRE_RUN_PINS.md` is present.

