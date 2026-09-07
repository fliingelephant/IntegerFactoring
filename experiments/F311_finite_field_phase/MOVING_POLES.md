# Two moving finite simple poles

**Status:** exact bounded extension of F311. Moving the two finite simple
poles produces complete models for some `q=32` phases, but none for the
larger tested coverage. This is a statement about the specified
ordinary/sign-log coordinates and at-most-three-simple-pole family. It is
not a general genus lower bound or a selected-window complexity result.

## Model and exact quotient search

For each retained Boolean table on `GF(q)`, the search tests

    epsilon + Tr(a*X + b/(X-r) + c/(X-s)),

where `r!=s`, `b,c!=0`, and `a` is arbitrary. Inverses at their zero
arguments are temporarily set to zero. Independent bits fill the two
singular terms at `r` and `s`, so both actual truth-table values at the poles
are free.

Affine Boolean functions are removed by the canonical quotient

    Q(f)=f xor f(0) xor
         sum_i (f(2^i) xor f(0))*coordinate_i.

The trace pairing identifies every residual linear mask with a unique field
coefficient `a`. A single-pole table

    Tr(b/(X-r)) xor t*delta_r

is obtained by XOR-translating a precomputed pole-at-zero table. The search
hashes its affine quotient and retains at most two witnesses with different
pole locations for each key. Complement lookup then finds two-pole sums
without enumerating all pole pairs and coefficient pairs. Every returned
model is verified against the complete truth table, including both filled
poles.

In this run every single-pole parameter triple had a distinct affine
quotient. The witness cap therefore discarded nothing:

| q | Generated triples | Quotient keys | Retained witnesses |
|---:|---:|---:|---:|
| 32 | 1,984 | 1,984 | 1,984 |
| 64 | 8,064 | 8,064 | 8,064 |
| 128 | 32,512 | 32,512 | 32,512 |
| 256 | 130,560 | 130,560 | 130,560 |

## Scoped Walsh rejection

Two finite simple poles and a possible simple pole at infinity have genus at
most two. Filling the two finite pole values changes any complete Walsh sum
by at most two. The search therefore rejects a table only when

    WalshMax > 4*sqrt(q)+2.

This prescreen applies only to this specified family. Rejected cases are
retained separately and are not reported as failed hash searches.

## Results

| q | Coverage | Targets | Walsh rejected | Fully searched | Fitted targets | Models |
|---:|---|---:|---:|---:|---:|---:|
| 32 | exhaustive residues up to complement, both coordinates | 64 | 0 | 64 | 18 | 20 |
| 64 | exhaustive residues up to complement, both coordinates | 128 | 12 | 116 | 0 | 0 |
| 128 | exhaustive residues up to complement, both coordinates | 256 | 74 | 182 | 0 | 0 |
| 256 | 16 seeded residues, both coordinates | 32 | 17 | 15 | 0 | 0 |

The `q=32` fits include both ordinary and sign-log coordinates. All 20
coefficient and pole witnesses, temporary singular bits, actual filled pole
bits, and truth-table checks are in `MOVING_POLES_output.json` and the run
log. For example, the ordinary phase for `N=1025` has

    a=17, epsilon=0,
    (r,b,t)=(12,23,1), (s,c,u)=(19,23,1).

Both actual filled pole bits are zero, and the model matches all 32 inputs.

At `q=64` and `q=128`, every original residue phase in both coordinates is
either rejected by the scoped Walsh bound or fully searched with no model.
The `q=256` result has the same conclusion for seeded original residues

    3,17,31,113,135,171,203,303,
    367,373,415,427,461,469,489,505.

These finite nonmemberships extend the fixed-pole tests to arbitrary pairs
of finite simple poles. They do not exclude higher pole orders, more poles,
other coordinate changes, or another algebraic summation mechanism.

## Resources and evidence

All four scales completed in 1.988 seconds with 86,982,656 bytes peak RSS.
The run used one Python process, a hard 30-second outer timeout, a 28-second
internal alarm, and a 512 MiB RSS watchdog. No factor of any original input
was used.

Evidence:
`MOVING_POLES.py`, `MOVING_POLES_output.json`, `MOVING_POLES_run.log`, and
`MOVING_POLES_RESOURCE.md`. The truth tables, finite fields, and sign-log
coordinate permutations are reused unchanged from `output.json`.
