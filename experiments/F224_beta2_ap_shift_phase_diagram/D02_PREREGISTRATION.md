# F224-D02 preregistration: timing-wrapper repair

F224-D01 failed before mathematical work because the remote image lacks
`/usr/bin/time`.  D02 preserves the D01 cohort, statistic, source, compiler,
memory limit, process priority, and 600-second timeout exactly.  It changes
only the unavailable timing wrapper:

```text
/usr/bin/time -v
```

is replaced by the Bash keyword

```text
time -p
```

The evidence is weaker only in resource telemetry: D02 records real, user,
and system time but no maximum-RSS field.  The 2-GiB virtual-memory limit
remains enforced by `ulimit -v 2097152`.

The unchanged source SHA-256 is
`c41f93502da4ea19e42633bb4aca3d95d7c65055cfeb09f70866f573241e753f`.
The D01 preregistration remains the complete definition of the cohort and
outputs.  The exact D02 command is

```text
bash D02_remote_run.sh scan.c D02_OUTPUT.tsv D02_RUN.log
```

No further substitution is allowed.
