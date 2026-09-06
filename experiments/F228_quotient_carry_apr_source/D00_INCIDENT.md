# F228-D00 workflow incident

After the dependency-only revision and before the remote D01 launch, a local
compile-check command mistakenly chained compilation to a full execution of
the frozen source.  The execution had `/usr/bin/time -p` but no timeout.  It
completed in 3.22 real seconds and wrote `/tmp/F228_D01_check.tsv`.

This was not the preregistered D01 command.  Its output is not used as D01
evidence.  The incident was disclosed immediately to the root agent.  The
source, cohort, menu, and decisive interpretation were not changed after
this accidental execution.  D01 remains the exact remote run declared in
`D01_PREREG.md`.

The accidental command was:

```sh
g++ -O3 -std=c++17 experiments/F228_quotient_carry_apr_source/run_F228_D01.cpp -o /tmp/run_F228_D01_check
/usr/bin/time -p /tmp/run_F228_D01_check /tmp/F228_D01_check.tsv
```

The source SHA-256 at execution was
`c3ebba44df3ba098e383fa84239c81503040fcf17e8dbed42927d5e601941256`.
The temporary output SHA-256 was
`1702c92fd32dddb33a9f309e660a50ce0066c819f6d6e8837cfe134ddfdcee33`.
