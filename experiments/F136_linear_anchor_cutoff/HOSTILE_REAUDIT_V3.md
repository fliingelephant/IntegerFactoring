# F136 final hostile re-audit v3 — PASS

## Verdict

**PASS.** The two statement-only clarifications requested by the strict
blind reconstruction are exact. They introduce no stronger mathematical
claim and make the statement consistent with the frozen proof.

Audited frozen hashes:

- `STATEMENT.md`:
  `e17c70e87c87d0893814ffb503f636087e60a373e31e06659ef524d1f8561c49`
- `PROOF.md`:
  `ecb2a92c7c382473ec0466f8dc544d7118e6ac160f927df9e7d0e31f11eb0655`
- `BLIND_RECONSTRUCTION_V2.md`:
  `402658881c1235b05e0b69b287ad5370894c2c4df6e9dfda90e5ba9b0487cd51`

F136 remains a source-side linear-cutoff theorem and a conditional
composition result. It is not a closure theorem or a factoring algorithm.

## Exact change audit

I mechanically removed the sentence

> Use the empty-product convention \(L_A=1\) when
> \(\mathcal L_A\) is empty.

and changed

> For the width conclusion below, assume \(n\ge21846\) and that no occupied
> bucket meets either release threshold

back to

> Assume that no occupied bucket meets either release threshold.

The reconstructed SHA-256 was

```text
7f751c757ce61b341e1845abf04c7f1076b6417af827480520a9f77ebd6c9a3e
```

This exactly matches the statement read by the strict blind reconstruction
and the statement accepted by hostile re-audit v2. Thus these are the only
two statement changes. The proof hash is unchanged from hostile re-audit v2.

## Empty-product convention

The eligible primes are partitioned by their carry digits. For each digit,

\[
L_A=\prod_{\ell\in\mathcal L_A}\ell.
\]

If the zero digit is unoccupied, the factor for that bucket must be one in

\[
G_B(N,q)=L_0\prod_{A>0}L_A.
\]

The added convention states exactly this standard meaning. It does not add
an anchor, a relation, or a prime factor. It also makes the condition
\(L_0\le B\) truth-valued when the zero bucket is empty.

The release implication for \(A=0\) remains conditional on \(L_0>B\).
An empty zero bucket has \(L_0=1\), so it cannot trigger that branch. No
release claim is enlarged.

## Width scope

The width proof uses

\[
\vartheta(B)>\frac6{25}B,
\]

which the artifact proves only after

\[
B\ge2^{18}.
\]

Since \(B=12n\), the declared sufficient condition is

\[
n\ge\left\lceil\frac{2^{18}}{12}\right\rceil=21846.
\]

Adding this hypothesis immediately before the no-release branch is therefore
necessary and sufficient for the displayed derivation. The residual-size
implications above it remain unrestricted. The statement now matches the
proof's use of Theorems 1 and 2.

The final trichotomy and the \(\Omega(n/\log n)\) width alternative are in
the scope of this explicit high-\(n\) hypothesis. Smaller inputs remain in
the already declared fixed finite trial-division branch.

## Fresh falsification checks

The two additions do not affect the earlier arithmetic audit. I nevertheless
rechecked every inference that touches their scope.

1. **Prime product.** Removing primes through \(B\) which divide \(Nq\)
   costs a squarefree product at most \(Nq<N^2/B\). The full primorial is
   greater than \(N^4\), so \(G_B(N,q)>N^2B\) remains strict.
2. **Digit collisions.** For \(r>B\), two different digits cannot both have
   \(r\mid H_A\), because their difference is \(N(A-C)\),
   \(r\nmid N\), and \(0<|A-C|<B<r\).
3. **Exact-value deletion.** Different digits give different integers
   \(qH_A\). Repeated anchors inside one digit can delete only duplicate
   copies of the same value. The certified row degree remains at least two.
4. **Release.** Complete refinement removes all named anchor-prime powers.
   The residual bounds are still \(H_0/L_0<N/B\) when \(L_0>B\), and
   \(H_A/L_A<NB/B^2=N/B\) when \(A>0\) and \(L_A>B^2\).
5. **Width.** On the high-\(n\) no-release branch,
   \(G_B(N,q)\le B^{2d+1}\). Combining this with the primorial lower bound
   still gives

   \[
   d>\frac{37n}{50\log(13n)}.
   \]

   For each fixed covered row, at most one nonzero digit is bad, so at least
   \(d-1\) distinct columns reuse it. This remains a per-row statement, not
   a common-column or kernel statement.
6. **Conditional cost.** The proof still establishes \(B<E\) from
   \(n\le2^L-1\) and
   \(12\cdot2^L<2^{L^2}\) for \(L\ge15\). Theorem 4 assumes the complete
   all-block source cost. Selecting its linear subbank adds no position.

No endpoint-range, empty-bucket, small-\(n\), valuation-parity,
deduplication, strict-inequality, or conditional-composition attack produced
a counterexample.

## Accepted boundary

F136 proves the linear cutoff only in its declared high-\(n\) range, with
finite preprocessing below it. It does not cover \(q\ge N/B\), force a
binary dependency, close fresh private rows, or prove a non-global
normalized-root image. The expanding-forest obstruction remains compatible
with every conclusion.
