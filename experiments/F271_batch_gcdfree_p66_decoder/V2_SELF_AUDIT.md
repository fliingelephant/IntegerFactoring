# F271 V2 self-audit

## Verdict

**PASS as a narrow author self-audit.** This is not a fresh hostile audit or
a proof-blind reconstruction. F271 V2 remains a candidate until both are run
on the frozen V2 bytes.

## 1. Delta check

V2 imports the exact frozen V1 statement and proof by SHA-256. It changes
only these two boundaries:

1. supplied modular roots use canonical representatives `0<=v_i<N`; and
2. the terminal tree has an explicit empty case and uses
   `delta_S=max(S-1,0)` in its operation counts.

No decoder algorithm, recursion, invariant, relation basis, peel rule,
constant, or scope claim changed.

## 2. Empty-tree arithmetic

- At `S=0`, every terminal count is zero.
- At `S=1`, the counts are one leaf squaring, no internal multiplication,
  no remainder division, one final exact division, and one gcd.
- At `S>=2`, `delta_S=S-1`, so the V2 formula is exactly the former V1
  formula.
- `S+delta_S` counts the `S` leaf squarings plus the internal modulus-tree
  multiplications. It is zero at `S=0` and `2S-1` at `S>=1`.
- `2delta_S` is the exact number of remainder-tree edges.
- Terminal gcds remain exactly `S`, so no gcd-call cap changes.

The all-one row case now has a defined empty product `P=1`, vacuous block
coprimality, and no negative coefficient in the detailed bit bound.

## 3. Residue encoding arithmetic

Canonical `v_i` have at most `bitlen(N)` bits. Since `m<=R`, their complete
encoding has at most `R*bitlen(N)` bits. Reading that input and all modular
root operations remain within `O((R+bitlen(N))^4)`.

V2 deliberately chooses the canonical-representative option. It does not
add an independent supplied-root-length parameter. Arbitrarily long
unreduced spellings are outside the V2 input domain.

## 4. Frozen V1 findings

The V1 hostile audit failed the exact packet on the two repaired boundaries.
Its core reconstruction and maximum F265 call arithmetic passed. The V1
blind reconstruction passed the theorem from the statement alone and
explicitly read “residue” as canonical modulo `N`. V2 makes that convention
normative and repairs the detailed empty-tree count that appeared only in
the V1 proof.

Neither V1 report is an audit of V2. Their exact hashes and verdicts are
pinned in `V2_PROVENANCE.md`.

## 5. Computation boundary

The checker source and every V1 candidate byte are unchanged. No new
computation was needed or run for these symbolic boundary repairs. The V1
finite checker remains sanity evidence only.
