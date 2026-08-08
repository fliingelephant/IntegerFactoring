# F119 final re-audit preserved rejected extensions

No program was run. The corrected theorem passed. These stronger readings
remain rejected and are preserved to prevent scope regression.

## 1. Retroactively relabel the original theorem as a clean pass

Rejected. The original `RESULT.md` hash
`990952a8175733959ef8d7f67429a330c27378ba897426a81c11f536dbd8a500`
required a scope correction. The clean `PASS` applies only to corrected hash
`552a54c8382341709305e53bd535efd9ef0ec0bc7957fa32be8ddc5c061f4575`.

## 2. Transfer named-residue screens to a different representative

Rejected. Equality of exact products preserves valuations but does not fix an
endpoint residue modulo the factors of `N_t`. The corrected theorem expressly
declines this claim.

## 3. Treat value retention as named raw-provenance retention

Rejected. Exact-value deduplication retains the integer value once. Its first
raw representative can be different from the named exponent-two residue.

## 4. Promote selected privacy to complete-source privacy

Rejected. An unselected column with a congruent carry can reuse a protected
row. Condition `(FSP)` is still missing.

## 5. Promote trial-hardness and named null screens to operational survival

Rejected. An earlier unselected sign screen can still expose a factor.

## 6. Infer a dependency or factor from the selected identity submatrix

Rejected. The identity submatrix proves selected-column independence, not a
dependency. A complete factoring theorem separately needs `(CLOSE)` and
`(ROOT)`.
