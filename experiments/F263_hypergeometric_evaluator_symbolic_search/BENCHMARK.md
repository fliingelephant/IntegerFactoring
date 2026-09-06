# F263 pre-freeze target benchmark

## Authoritative target

The target host was `seetacloud`.  Before preflight it reported 32 visible
CPUs, 503 GiB RAM with 367 GiB available, and 22 GiB free disk.  F258-D01
used one low-priority core.  F263 ran only its algebra self-test and one
public synthetic benchmark at nice 15.  It did not open a cohort.

The authoritative compile command was

```text
/usr/bin/g++ -O3 -DNDEBUG -std=c++17 -pthread symbolic_search.cpp \
  -o symbolic_search
```

Both compiler streams were empty.  The exact self-test printed

```text
SELF_TEST_PASS controls=12 columns=70 ranks=58,58 nullities=12,12 identities=14 shortcuts=0 adjacent=4 dyadic=0 candidates=148
```

The exact public benchmark printed

```text
BENCHMARK_PASS seconds=1.129952 blocks=330 leaf_touches=232440 candidates=148 symbolic_columns=70 symbolic_relations=14 shortcuts=0
```

The wrapper measured 1.193634116 seconds wall time and 7,968 KiB peak RSS.
The public benchmark uses the fixed synthetic pair in the source.  It does
not generate, write, or summarize a discovery or held-out cohort.

## Projection

The frozen cohorts contain 1,536 discovery rows and 2,016 held-out rows.
At the 60-bit maximum, one row took 1.13 seconds on one core, including the
symbolic search.  The symbolic search is repeated by phase, not by row, so
the direct conservative row projection is

```text
3552 * 1.13 / 8 = 502 seconds
```

under ideal eight-thread scaling.  A deliberately conservative factor of
eight for host load, cohort generation, output, and imperfect scaling gives
67 minutes.  The four-hour cap therefore has ample margin.

The measured row state is below 8 MiB.  Eight workers plus compact row and
summary output are conservatively below 256 MiB.  The frozen 4 GiB cap has
ample margin.  The compact TSV has 3,552 rows and two short candidate bitsets
per row.  Its output is far below the 1 GiB cap.

The full characteristic-size product tree is not part of this projection.
The source never materializes it on cohort rows.

## Preserved failures

`FAILED_SELF_TEST.md` preserves the wrong candidate-count assertion and the
test-only dangling-reference failure.  `FAILED_BENCHMARK.md` preserves the
first monitor wrapper's shell-precedence failure.  None generated a cohort.
The source was frozen only after the final exact target self-test and public
benchmark passed.

The exact final streams, monitor, and their target hashes are retained in
`TARGET_CHECKS/`.
