# F263-D02 V2 result

Status: completed exactly; independent result audit **PASS**.

The frozen C++17 runner completed discovery and held-out evaluation with
status zero on both phases.

```text
start_utc=2026-08-13T17:30:27Z
end_utc=2026-08-13T17:37:41Z
discovery rows=848
held-out rows=1152
output bytes=761893
selected candidates=64
held-out lead passes=0
```

All compile, self-test, discovery, and held-out stderr streams are empty.
The retrieved manifest has SHA-256
`f8a352f85b373b9310b231a055e9594f60f4219cf4e1b30bcf51322a7206b1ee`.

## Symbolic outcome

The authenticated symbolic layer found exactly the registered merge
controls:

```text
columns=70
ranks=58,58
nullities=12,12
sparse relations=14
authenticated controls=12
operational shortcuts=0
adjacent full-scan recurrences=4
dyadic recurrences=0
```

Every mined identity either expands through the complete recursive merge
tree or has more than one parent target.  None supplies a numerical-QP block
evaluator.

## Held-out numerical outcome

All proper-gcd hits occur in the consecutive-prime cohort.  The random,
safe-safe, and bounded-common-capacity cohorts have zero hits for all 148
candidates.

The strongest selected counts are direct small-gap effects:

```text
central.u0 and equivalent transfer determinants: 248 / 256 consecutive rows
shifted.v0:                                    248 / 256 consecutive rows
shifted adjacent v0 controls:                  239 / 256 consecutive rows
```

Six selected candidates have at least one nondirect hit.  Five have at least
16 held-out hits and a nondirect hit.  No candidate has a hostile-cohort hit,
and no candidate maps to an authenticated operational target.  Therefore:

```text
gate1 (>=16 hits):                       16 / 64 selected candidates
gate2 (size + hostile coverage):          0 / 64
gate3 (nondirect hit):                    6 / 64
gate4 (operational symbolic target):      0 / 64
all four gates:                           0 / 64
```

The independent audit sharpened the cohort split:

```text
random:                         0 / 512 rows hit
safe-safe:                      0 / 128 rows hit
bounded common capacity <=16:   0 / 256 rows hit
consecutive primes:           248 / 256 rows hit; 8 cleanup exits
```

All 256 consecutive rows satisfy `B+1=(p+q)/2`, so one public Fermat trial
factors every one.  The six nondirect candidates have a 67-row union.  Each
row is consecutive-prime, and each hit lies at or next to a power-of-two
query boundary.  Thus the nondirect labels are genuine support labels but do
not represent a factoring gain.

The finite evidence therefore rejects the frozen grammar as a new all-input
source.  It does not prove an asymptotic lower bound.  The independent audit
is `V2_RESULT_AUDIT.md`, SHA-256
`320427df65f9d45f63cfaf4ad93194fe7e09cc499b4bd6d86b9a5ad7fb92b976`.
