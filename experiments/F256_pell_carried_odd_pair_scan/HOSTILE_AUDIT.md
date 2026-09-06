# F256 hostile audit

## Verdict

**PASS WITH PROTOCOL QUALIFICATION.** The frozen artifacts support the stated
`null finite signal`: the held-out scan has zero square dependencies. I found
no counterexample, counter mismatch, cohort substitution, or scope inflation.

The packet is not fully compliant with its frozen measurement protocol.
`SUMMARY.json` omits preregistered source-cleanup and resource aggregates, and
the JSONL records do not preserve enough information to reconstruct every
per-`D` cleanup aggregate. This defect limits the completeness of the run
report. It does not change the dependency null because the decisive pair
counters and their input-level assertions are present and consistent.

## Authentication

I recomputed SHA-256 over the four frozen inputs and all nine run artifacts.
Every digest matches both `RUN_MANIFEST.md` and `output/REMOTE_SHA256SUMS`.
The checksum file itself has the manifested digest
`3b8fb2813a20f72d1604c49974e588c9e04f80eecf83eedf6ea02c66e099b5c3`.

The authenticated frozen-input digests are:

| File | SHA-256 |
|---|---|
| `PREREGISTRATION.md` | `129bcacc40359e4f433f3fea6496e81bdb515cca24aa202033052d6f79730237` |
| `ALGEBRA.md` | `c2b86b948fc1f286376997638002bc1ea470167a7cf0dd8291fdbc9cbbd7d349` |
| `scan.py` | `283eedcc3e924c9f1309d0320f19544d779929a68a01a3d55259a68817a2ea61` |
| `remote_run.sh` | `5d942d46dc9816b2f939c62951e5d0b1f7c603501cd160d097b10646c8307fd2` |

Both JSONL files have exactly 512 records. `RUN.stdout` has 1,024 progress
lines followed by one summary line. Both stderr files are empty. The
authenticated self-test says `SELF_TEST_PASS`, and an independent local
execution of the frozen self-test also passed.

## Independent consistency checks

I parsed all 1,024 records and checked the following conditions without using
`RESULT.md` as evidence:

- The deterministic hash-stream cohort regenerates every recorded metadata
  row in order. All 1,024 moduli are distinct. Each recorded `N=pq` has the
  requested bit length, `p<q<2p`, and two primes under the frozen deterministic
  Miller--Rabin test.
- On every input, generated rows partition exactly into retained, singleton,
  duplicate, and nonunit rows. Pre-wrap plus post-wrap equals generated. The
  eight recorded per-`D` retained counts sum to the total retained count.
- On every input and in every recorded `D` and multiplier bucket,
  `admissible=carried+uncarried` and `carried=(d=1)+(d>1)`. Each bucket sums
  exactly to its parent counter.
- A fresh aggregation of the JSONL records exactly equals every pair counter
  in `SUMMARY.json` by split, bit length, `D`, and multiplier. It also equals
  every recorded input-level outcome count.
- Every progress line agrees with its corresponding JSONL row, the training
  block ends before the held-out block starts, and the final stdout JSON is
  byte-content-equivalent to `SUMMARY.json` after parsing.
- I replayed one input at each of the eight bit lengths (eight inputs total).
  Every stable `source` and `pairs` field reproduced exactly.

The independently reconstructed decisive totals are:

| split | admissible | uncarried | carried | `d=1` | `d>1` | either quotient square | dependencies | non-global |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| training | 879,917 | 3 | 879,914 | 529,131 | 350,783 | 0 | 0 | 0 |
| held-out | 1,431,564 | 0 | 1,431,564 | 858,748 | 572,816 | 0 | 0 | 0 |
| total | 2,311,481 | 3 | 2,311,478 | 1,387,879 | 923,599 | 0 | 0 | 0 |

The code checks the polynomial norm, odd-multiple coordinate and root
relations, nonnegative canonical carry, exact carry identity, gcd identity,
coprimality of the two quotients, and equivalence between the quotient test
and direct product-square testing on every carried pair. Since neither
quotient is square for any tested pair, the zero dependency count follows
directly. The frozen interpretation therefore selects `null finite signal`.

## Protocol qualification

The preregistration requires source cleanup and resource measurements for
each input and in aggregates by split, bit length, `D`, and multiplier. The
delivered schema does not satisfy that requirement in full:

- `SUMMARY.json` aggregates pair counters, but not generated, retained,
  singleton, duplicate, or nonunit source counters.
- The JSONL source record has total cleanup counters and per-`D` retained
  counts. It does not have per-`D` singleton, duplicate, or nonunit counts.
  Split and bit totals can be reconstructed, but those per-`D` removal totals
  cannot be reconstructed from the frozen output.
- Each row has wall and CPU time, `SUMMARY.json` has only one process peak-RSS
  value, and `WALL_SECONDS.txt` has whole-run wall time. The requested resource
  aggregates and per-input peak-memory measurements are absent.

For reference, the reconstructible split-level source totals are 1,277,952
generated and 1,245,288 retained rows in training, and 2,064,384 generated
and 2,017,024 retained rows in held-out. These checks expose no hidden row
loss. They do not repair the missing per-`D` measurements.

This qualification bars a claim of complete preregistration compliance. It
does not bar the narrower finite null: the omitted fields are reporting
dimensions, not inputs to pair admission, the exact quotient-square test, or
the held-out interpretation. The result remains finite evidence only for the
frozen `D`, multiplier, cohort, and `12n` window. It proves no rarity bound or
impossibility theorem.

I changed no frozen input, output, result, manifest, or ledger. I wrote only
this audit.
