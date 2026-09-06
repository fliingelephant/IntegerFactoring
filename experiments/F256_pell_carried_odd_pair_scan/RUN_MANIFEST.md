# F256 run manifest

## Frozen inputs

```text
PREREGISTRATION.md  129bcacc40359e4f433f3fea6496e81bdb515cca24aa202033052d6f79730237
ALGEBRA.md           c2b86b948fc1f286376997638002bc1ea470167a7cf0dd8291fdbc9cbbd7d349
scan.py              283eedcc3e924c9f1309d0320f19544d779929a68a01a3d55259a68817a2ea61
remote_run.sh        5d942d46dc9816b2f939c62951e5d0b1f7c603501cd160d097b10646c8307fd2
```

## Runtime

```text
host                 seetacloud
python               3.12.3, Anaconda build, GCC 11.2.0
processes            one
priority             nice -n 15
virtual-memory cap   2 GiB
hard timeout         1,800 seconds
measured wall time   66 seconds
reported max RSS     29,188 Linux ru_maxrss units
self-test stdout     SELF_TEST_PASS
self-test stderr     empty
run stderr           empty
exit status          0
```

## Frozen outputs

```text
TRAIN.jsonl          34552d9d94c67774d734b233a613584d367595aa9ec559488520c4d41e6be412
HELDOUT.jsonl        1d8f2b60aa99b0f3379d5879e4bca8fcfd3679b091f69f7c3214d98b815cf3cd
SUMMARY.json         c4d0322f6638ecd8f2f59517ba2aa76ac636b7f70f0c2afa96d9e04b0fff3c21
RUN.stdout           5d76f26c5c4f1addea7c59815c35006c81a06cd454fa16f7a6c3cf6653dc6ab1
RUN.stderr           e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
SELF_TEST.stdout     f3beaa43aef045f805e9d53d3d01088bc2b8fe66ac1b4eac7af001e0e90d6933
SELF_TEST.stderr     e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
WALL_SECONDS.txt     8e37bed9dff3949ffd23ae638260dff869f5cc26e551f2a9e5e289a8888949fa
REMOTE_SHA256SUMS    3b8fb2813a20f72d1604c49974e588c9e04f80eecf83eedf6ea02c66e099b5c3
```

Both JSONL files contain exactly 512 records.  Local hashes match the
remote manifest.  A separate `jq` aggregation over all 1,024 copied records
reconstructed the split totals in `RESULT.md` and confirmed zero quotient
squares, dependencies, certificates, and non-global classes.

## Remote chronology

The runner did not write application-level UTC timestamps.  The following
are the remote filesystem birth and modification times on `seetacloud`, in
the host's `+0800` timezone.  They establish the run order without claiming
more timing precision than filesystem metadata supplies.

```text
2026-08-13 20:40:57.074739194  SELF_TEST.stdout born
2026-08-13 20:40:57.154741355  SELF_TEST.stdout finished: SELF_TEST_PASS
2026-08-13 20:40:57.194742434  RUN.stdout and RUN.stderr born
2026-08-13 20:40:57.326745999  TRAIN.jsonl born
2026-08-13 20:41:19.415345900  TRAIN.jsonl finished: 512 rows
2026-08-13 20:41:19.455346993  HELDOUT.jsonl born
2026-08-13 20:42:03.576565513  HELDOUT.jsonl finished: 512 rows
2026-08-13 20:42:03.676568304  SUMMARY.json written; RUN.stdout finished
2026-08-13 20:42:03.736569978  WALL_SECONDS.txt written: 66
2026-08-13 20:42:03.756570536  REMOTE_SHA256SUMS finished
```

The stdout boundary is exactly

```text
train 512/512 bits=32 pairs=2116 deps=0 non_global=0
heldout 1/512 bits=36 pairs=2392 deps=0 non_global=0
```

Thus the complete training output preceded the first held-out record, as
required by the preregistration.

## Verified aggregate counts

```text
                         training       held-out           total
JSONL rows                    512             512           1,024
admissible pairs          879,917       1,431,564       2,311,481
zero-carry pairs                3               0               3
carried pairs             879,914       1,431,564       2,311,478
d = 1                     529,131         858,748       1,387,879
d > 1                     350,783         572,816         923,599
left quotient square            0               0               0
right quotient square           0               0               0
square dependencies              0               0               0
non-global dependencies          0               0               0
dependency certificates          0               0               0
```

The identities `admissible = carried + zero-carry` and
`carried = (d=1) + (d>1)` hold in each split and globally.

## Evidence boundary

The exact algebra in `ALGEBRA.md` is proof evidence.  It applies to every
admitted carried pair satisfying its public root-unit assumptions.

The zero dependency count is finite evidence only.  It applies only to the
frozen cohorts and to

```text
D in {2,3,5,6,7,10,11,13}
h in {3,5,7,9}
1 <= j,hj <= 12*bitlength(N)
```

It is not an asymptotic rarity bound.  It does not cover other
discriminants, multipliers, windows, unrelated pairs, or dependencies of
three or more rows.  No impossibility or inverse-QP conclusion follows.
