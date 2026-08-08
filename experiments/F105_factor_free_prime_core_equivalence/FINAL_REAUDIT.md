# F105 final narrow re-audit

## Verdict

**PASS. No mathematical or wording caveat remains in the corrected
candidate.**

The complete corrected `RESULT.md` has SHA-256 hash

```text
ffcc2334acb34619ea2308ec9c544fbb1d0ecce4c696f9ce01c3caf9bbb53f45
```

The unchanged `DESIGN.md` has SHA-256 hash

```text
b9b5da6a2c3d564b1df4470af7da31bfe5e9b86366a675104f70cb574f25a28e
```

I read all 74 lines of the corrected result. I did not edit either candidate
file.

## Correction check

The correction closes exactly the two boundaries from the first audit.

1. Lines 19–20 now require an eligible pair to satisfy
   \(d=\gcd(x,y)>1\). Lines 38–41 give the decreasing \(\Omega\) potential
   and require refinement to continue until no eligible pair remains.
2. Lines 54–57 now compare the nonzero row sets explicitly. They state that
   duplicate nonzero rows are the only remaining difference after zero rows
   are omitted, and that an implementation which retains hidden zero rows can
   also differ by those rows.

Both statements are exact.

For an eligible split, the unomitted output values have total potential

\[
\Omega(d)+\Omega(x/d)+\Omega(y/d)
=\Omega(x)+\Omega(y)-\Omega(d).
\]

Discarding a value-one or zero-mask output only decreases this total further.
Because \(d>1\), every step strictly decreases a nonnegative integer.
Therefore every eligible schedule is finite. Exhaustion of all eligible pairs
is exactly pairwise coprimality of the surviving integers.

The zero-row wording is also complete. The one-entry batch
\((4,001)\) has a retained hidden zero row if an implementation chooses to
store it and no public nonsquare row. Lines 55–57 now describe this case
without claiming equality of raw row multisets. Zero rows and duplicate rows
do not affect any stated consequence.

## Scope comparison

The correction does not expand the theorem. It keeps:

- the same integer-mask inputs;
- the same per-prime invariant;
- the same finite explicit-batch quantifier;
- the same terminal nonzero-row-set equivalence;
- the same rank, kernel, peeling-core, and component consequences; and
- the same decoder-only limitation.

It only restricts the allowed refinement move and makes the zero-row
representation explicit. The first audit's proofs of unequal valuations,
initial or generated zero masks, repeated masks, row multiplicity,
degree-one peeling, order independence, and column components apply without
change.

## Evidence reuse and fresh check

Because the correction does not add an input, schedule, matrix consequence,
or factoring claim, the exhaustive evidence pinned in `AUDIT_MANIFEST.md`
still covers the corrected theorem. Its adversarial gcd-one and hidden-zero
examples are now handled expressly by the corrected text rather than being
live caveats.

After the scope comparison, I ran the unchanged verifier again. It exited
zero and reported `PASS` after checking:

- 14,400 one-step cases;
- 3,200 unequal-positive-valuation prime cases;
- 121,485 batches with zero and repeated masks; and
- 125,321 terminal schedule outcomes, including all peeling orders and
  column components in the bounded family.

The bounded run is supplementary. The universal verdict follows from the
proof in the first audit plus the exact correction check above.

## Final scope

The theorem is an exact decoder equivalence for a frozen finite explicit
batch. It does not assert a nonempty core, rank defect, non-global normalized
root, online deletion rule, success density, or all-input factoring source.
Within that scope, no caveat remains.
