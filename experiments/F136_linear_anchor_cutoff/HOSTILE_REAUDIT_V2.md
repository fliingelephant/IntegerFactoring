# F136 corrected hostile re-audit v2 — PASS

## Verdict

**PASS.** The exact replacement repairs the only failure in
`HOSTILE_REAUDIT_FAILED.md`. I found no collateral change and no new error.

Audited frozen hashes:

- `STATEMENT.md`:
  `7f751c757ce61b341e1845abf04c7f1076b6417af827480520a9f77ebd6c9a3e`
- `PROOF.md`:
  `ecb2a92c7c382473ec0466f8dc544d7118e6ac160f927df9e7d0e31f11eb0655`

The accepted result remains a source-side linear-cutoff theorem and an
explicit conditional composition corollary. It is not a parity-closure
theorem or a factoring algorithm.

## Exact repair check

From

\[
L=\lceil\log_2(n+1)\rceil
\]

one gets

\[
n+1\le2^L,
\qquad
n\le2^L-1.
\]

Here \(n\) is an integer, so

\[
B=\lceil12n\rceil=12n<12\mathbin{\cdot}2^L.
\]

For \(L\ge15\),

\[
L^2-L\ge210,
\qquad
12<2^{L^2-L}.
\]

Multiplication by \(2^L\) gives

\[
12\mathbin{\cdot}2^L<2^{L^2}=E.
\]

Therefore \(B<E\) for every declared \(n\ge21846\). This is a direct
uniform inequality. It does not use the false monotonic-gap claim preserved
in the earlier failed report.

## No-collateral-change check

I reversed only the new paragraph in Section 6, replacing it by the exact
failed-version paragraph. The reconstructed SHA-256 was

```text
754f9c1d552b9a98fe59cda16233bc776119de2bf47bc06506fcdf702fab8473
```

This exactly matches the frozen proof hash audited in
`HOSTILE_REAUDIT_FAILED.md`. Thus the repair changed only the stated
justification of \(B<E\). Sections 1--5, the conditional source hypothesis,
the finite preprocessing statement, and every theorem constant are
unchanged.

## Accepted conclusions

The new Definitions section remains sufficient for a statement-only
reconstruction of Theorems 1--3. Theorem 4 explicitly assumes the all-block
source and its full cost. Since the repaired proof establishes \(B<E\), the
linear anchor bank is a literal subbank and adds no source position.

All previous limits remain in force. F136 does not cover blocks
\(q\ge N/B\), force a binary kernel, or produce a non-global normalized
root.
