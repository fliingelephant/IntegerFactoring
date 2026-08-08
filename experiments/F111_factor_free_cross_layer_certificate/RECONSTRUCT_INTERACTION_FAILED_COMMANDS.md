# Preserved non-computational command errors

The named reconstruction run passed on its first attempt. No decoder failure
or timeout occurred.

Three later read-only inspection commands had shell-string formatting errors:

1. A multiline `jq` filter was passed with literal `\n` sequences. `jq`
   rejected the filter before reading a result. A Python `-B` JSON summary
   command replaced it.
2. The first three-chunk overlap check passed literal `\n` sequences to
   Python `-c`. Python returned `SyntaxError` before importing the decoder or
   executing the check. The same check was then passed through Python
   `exec(...)` and completed with:

```text
three-chunk ordered-overlap equivalence passed
```

3. A digest-summary one-liner placed a compound `for` statement after a
   semicolon. Python rejected that syntax before reading the output. The same
   read-only summary was rerun through `exec(...)` and succeeded.

No failed command wrote or changed a file. They did not affect the
successful reconstruction output.
