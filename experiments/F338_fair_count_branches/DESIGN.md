# Fair branches on the frozen F336 source corpus

**Family:** route:F31

Status: root-specified finite comparison. No success law, asymptotic
extrapolation, or quasipolynomial claim is part of this design.

## Frozen inputs

Use every one of the 21,504 standalone policy rows in the frozen F336
aggregate. This is 12 moduli, 14 profiles per modulus, and 128 source trials
per profile. Keep all four generation-factor rows produced by the two shared
direct/inverse generation events. Do not select a row from its outcome.

The source parameters, public transforms, profile names, row IDs, and
generation-factor outcomes are unchanged. A direct/inverse pair can share its
source draw, but each row remains a standalone algorithm and receives the
complete source-generation cost. An inverse or ratio row also receives its
complete public transform cost.

## Changed branch law

For each accepted unit row, retain its multiplier for the full attempt and
start at h=(N-1)/2. At each reached t>=2:

1. gcd-screen t;
2. compute q=Q_a(t) with the frozen F334 CountOracle;
3. gcd-screen each positive child q and t-q in the same declared order;
4. return the first declared verified factor outcome after completing both
   child screens;
5. fail if either child is zero;
6. otherwise draw one independent fair bit and select q for bit zero or t-q
   for bit one;
7. fail if the selected child is at most one, else continue.

There is no Jacobi filter, added factor or root screen, or per-attempt path
cap. A generation-factor row terminates before a branch bit.

The branch seed is derived from the fixed new seed 33820260907 and the frozen
row ID. This seed domain is independent of every F336 source seed.

## Counter recovery

For every accepted source row, replay the frozen F334 minimum-child descent.
Its status, stopping reason, stopping stage, retained defects, and verified
output must match the F336 row. Subtract its additive operation counters from
the original F336 standalone counter vector. The nonnegative remainder is the
source-generation and public-transform vector. Add the new fair-descent
counter vector to this remainder.

Maximum fields are not additive. Retain the original combined maximum and the
replayed minimum maximum separately. Form the new maximum by a max operation,
never subtraction. Do not subtract wall-clock timings. Preserve the original
F336 standalone timing only as an undecomposed historical measurement, and
record F338 processing time separately. Cost-per-success comparisons use
operation counters, not a fabricated generation time.

## Retained evidence

Each compact row keeps its frozen source row ID and digest, source artifact
hash, branch seed, source and fair counter vectors, total operation vector,
branch-bit count, first-hit stage, stop reason, output, source profile, and
dependency hashes. It retains all failure work.

Keep full traces for:

- the exact small controls N=25,a=8 and N=35,a=4;
- every row in the two-trial pilot on b20_i0 and b20_i1;
- the first witness for every distinct verified output key in each retained
  batch; and
- every anomaly.

All other scale rows remain reproducible from the frozen source row, fixed
branch seed, and named source.

Summaries compare minimum and fair branches for each input and profile. They
report generation and count factors separately, stopping failures, Q/gcd/
Euclid/branch-bit totals, first-hit stages, and total charged operations per
observed success. A zero-success cost cell is null.

## Runs

The pilot first checks the two exact DP examples, then transforms source trial
indices 0 and 1 for both 20-bit inputs. If it passes, process all source rows
in the original 64-index batches. Each process is single-threaded, has a
28-second internal alarm, a 30-second external timeout, and a 512 MiB RSS
ceiling.
