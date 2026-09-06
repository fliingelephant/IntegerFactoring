# F228 local verification preregistration

This verification reads the frozen D01--D03 TSV files.  It performs no new
search.  It checks hashes, row counts, declared summaries, D02/D03 cap-20
row equality, safe-prime cohort arithmetic, exact fourth-root thresholds,
and every D03 selected compatible-prime certificate.

The process is single-threaded, uses below 64 MiB, and should finish in less
than 30 seconds.  Source:
`experiments/F228_quotient_carry_apr_source/verify_F228.py`.

Command:

```sh
/opt/homebrew/bin/gtimeout 30s /usr/bin/python3 experiments/F228_quotient_carry_apr_source/verify_F228.py experiments/F228_quotient_carry_apr_source > experiments/F228_quotient_carry_apr_source/VERIFY_OUTPUT.txt 2> experiments/F228_quotient_carry_apr_source/VERIFY_RUN.log
```

A timeout or failed assertion ends verification.  No substitute verifier
will be used silently.

The first preregistration draft named `/usr/bin/timeout`.  A pre-run check
found that macOS path absent and found `/opt/homebrew/bin/gtimeout`.  This
dependency-only correction was made before the verifier ran.  The source,
checks, inputs, timeout duration, and output paths did not change.
