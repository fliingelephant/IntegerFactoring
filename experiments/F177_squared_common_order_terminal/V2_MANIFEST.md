# F177 V2 manifest

## Status

V1 is preserved in `STATEMENT.md`, `PROOF.md`, `SELF_AUDIT.md`, and
`HOSTILE_AUDIT.md`. Its hostile audit found one interface defect: the public
F170 torus state does not reveal the sign \(\epsilon\), while V1 scanned one
sign class.

V2 repairs only that defect. It scans both signs. The total torus candidate
count is

\[
2+\frac{\sqrt{2N}}{B^2},
\]

so the V1 numerical threshold still gives QP cost. The ordinary theorem is
unchanged.

## V1 frozen hashes

- `STATEMENT.md`: `bc1ec03dd8f9ac47e90d7e0108f3188d9639f0bb4f3f36074be047ba37da4944`
- `PROOF.md`: `82ec538a073e22566eb6e7429f03193b86fac119e24a551d144df89a33c73a09`
- `SELF_AUDIT.md`: `62942bd1ebb95d14c02ff2d876026acf660c44efb683c9a7264cde17e2774e26`
- `HOSTILE_AUDIT.md`: `eb99727ceba8f2f040187237d4f27dcd26133e3ff5396cfb59bb89b3ec4a6d2f`

## V2 review gate

1. Fresh hostile re-audit of `V2_STATEMENT.md` and `V2_PROOF.md`.
2. Fresh statement-only reconstruction after the re-audit passes.
3. No durable-ledger promotion before both checks pass.
