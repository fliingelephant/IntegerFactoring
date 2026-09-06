# F264-D03 V3 independent static validation

These checks occurred before the V3 hash freeze. They did not compile or run
the C++ source, start the runner, generate a cohort, open cohort output, or use
the remote host. F258-D01 was active, so every dynamic V3 mode remained closed.

## Preserved provenance

`sha256sum -c FROZEN.sha256` and `sha256sum -c V2_FROZEN.sha256` passed for
every listed V1 and V2 artifact. The preserved hostile-audit hashes were:

```text
f00fee9eac5fb71c9403d0f3a39b8cbf0bb0eb5682d6776f5eca1d26e21e3c9c  HOSTILE_PRERUN_AUDIT.md
4206516a9ee14b831db4f3d9c148052f990faf209ffacf2673518f8de9eaf51a  V2_HOSTILE_PRERUN_AUDIT.md
```

## Static source comparison

The V2-to-V3 C++ diff was inspected in full. It is limited to:

- a fixed 14-proposal count;
- exhaustive proposal evaluation and compact check/match/hash recording;
- moving that complete evaluation before every order-path return;
- a 36-by-14 self-test assertion;
- 19 new row fields and the corresponding aggregate JSON fields;
- V3 identifiers and the exact 2,560-column description.

The family list, algebraic atom construction, candidate DAG, seeds, word/pair/
triple selection, cohorts, P205 programs, order schedules, lead predicates,
and factor-label firewall are unchanged. The V2-to-V3 algebra diff changes
only packet identifiers and states explicitly that every formula is unchanged.

The root loop has 14 iterations with no return. It records one check for every
index and hashes the index, trial order, proposal residue, square residual, gcd
value, and outcome. Only after the full loop can a retained proper gcd stop the
trial. A unit match remains only a conditional split certificate.

## Static runner checks

The following checks passed:

```text
BASH_SYNTAX_PASS
EMBEDDED_PYTHON_SYNTAX_PASS blocks=6
GIT_DIFF_CHECK_PASS
STATIC_SCHEMA_PASS columns=2560 root_checks=504 inputs=5280
```

The 2,560 columns decompose as 31 fixed row fields, 14 per-proposal check
fields, 20 typed basis transcript fields, 10 named decoy fields, 150 family
fields, and 2,335 P205 fields. The root arithmetic is `36*14=504`. The split
arithmetic is `2208+3072=5280`.

Every named executable stage after runner initialization uses `run_monitored`:
hash authentication, compile, self-test, self-test validation, benchmark,
benchmark validation, description, description validation, discovery,
discovery validation, held-out, held-out validation, compression, manifest,
and final output validation. The manifest stage precedes the final aggregate
gate. The final gate's child logs are included by the post-child byte check.
No owned file is written after that return.

Dynamic C++ parsing, Boost behavior, runtime, memory, output size, cohort
construction, and score semantics remain unauthenticated until a fresh hostile
audit passes and the frozen target runner completes.
