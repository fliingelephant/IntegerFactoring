# F144 manifest — cross-star residual cycles

## Preserved failed V1

V1 claimed a near-\(N\) short-cycle surplus theorem.  Its hostile audit
showed that the antecedent was impossible.  The same bounds that made every
edge wrapped forced each proposed cycle anchor product below \(\sqrt N\),
while the exact cycle identity requires it to exceed \(\sqrt N\).

| Artifact | SHA-256 |
|---|---|
| STATEMENT.md | 937a41ce493c65f14ad2ab9c826542188e904b2ff1762d38efc380d96e13420d |
| PROOF.md | affcb1bdb8db25da2a81d5e27b827553039c3bf49e0ed9a56358bd8f2e841aa3 |
| HOSTILE_AUDIT_FAILED.md | 696016da383e646b05c6268e7ddb7217008ea0e4ca8778f398677aa7359821a9 |

## Preserved failed V2

V2 removed the vacuous surplus theorem.  Its hostile audit passed.  A fresh
statement-only blind reconstruction then found one exact strictness error:

\[
\mathcal A^2-S^2=mN,\quad m\ge1
\]

implies

\[
\mathcal A\ge\sqrt{N+S^2}>\sqrt N,
\]

not a strict first inequality.  The \(N=35\) certificate attains equality.
The blind reconstruction found no structural failure beyond this
strictness and interval wording.

| Artifact | SHA-256 |
|---|---|
| V2_STATEMENT.md | a07a992ac3d43dac6f25c2cc337e470f81c9a8265eb54e091922ecd63cef138b |
| V2_PROOF.md | f4c8f8fef6ca21b18f2bce70c400cf2ab6c748a55d32b8a1836ab2dd92de6df9 |
| V2_HOSTILE_AUDIT.md | 9927bfb2993c82aa892a886df0789376f9c4daaa1e96b4b6ffdad00e2e9e39a0 |
| V2_BLIND_RECONSTRUCTION.md | a092b9ba2520bac65923c054226bba25500f2fdfdb71152d67fd4aefa63b1f23 |

## Promoted V3 result

V3 makes the exact non-strict correction everywhere and states the two
metric ranges separately.

- Every stored positive-direction containment cycle satisfies
  \(N\mid A_{\mathcal C}^2-T_{\mathcal C}\).
- A cycle with a wrapped edge satisfies
  \(A_{\mathcal C}^2\ge N+T_{\mathcal C}\) and
  \(A_{\mathcal C}>\sqrt N\), without a residual-square assumption.
- If a collection of cycles has combined residual \(S^2\), its actual P128
  columns have normalized root \(\mathcal A/S\).
- A wrapped collection satisfies
  \(\mathcal A^2-S^2=mN\), \(m\ge1\), and therefore
  \(\mathcal A\ge\sqrt{N+S^2}>\sqrt N\).
- If also \(2\mathcal A<N\), both gcds of
  \(\mathcal A-S\) and \(\mathcal A+S\) with \(N\) are proper.
- For fixed \(S\), these bounds place
  \(\mathcal A\) in
  \(\sqrt{N+S^2}\le\mathcal A<N/2\).
  After projecting away \(S\), the coarser anchor-only interval is
  \(\sqrt N<\mathcal A<N/2\).
- Two wrapped cycles already have combined anchor product above \(N\).
  Unwrapped cycles have root \(+1\) and do not help one wrapped cycle close
  its residual.
- Wrapped positive-direction cycles with total raw anchor product
  \(2^{\operatorname{polylog}n}=2^{o(n)}\) are asymptotically impossible.
- A polynomial-length selected path or a compact F130 anchor above
  \(\sqrt N\) remains possible within quasipolynomial work.
- The conditional \(N=35\) certificate has
  \(\mathcal A=6=\sqrt{35+1}\), \(S=1\), and gives factors \(5,7\).
- A zero two-endpoint carry determinant gives root \(+1\), and the
  four-endpoint cross-star grid is the existing P114 rectangle.

V3 proves no cycle-existence law, no residual-square law at characteristic
scale, and no factoring algorithm.

| Artifact | SHA-256 |
|---|---|
| V3_STATEMENT.md | 87dacd7af5121f66561cea4136d1445f10cfe0185bd9229277fd48b358bf5f6f |
| V3_PROOF.md | 2635270473001fa32b6b9db15d9abb7460f31384ed9a8cec7de61f1c6717089e |
| V3_HOSTILE_AUDIT.md | 52cefa0f458d5c78c987d2353865e8220a8efcf63c93466b6a15ee6bc4216a95 |
| V3_BLIND_RECONSTRUCTION.md | b706ca6fed8c0e45969814238854ae90142ee348fbb23e4a69d34a35294c71b7 |

## Evidence and scope

No research computation was used.  The \(N=35\) arithmetic is an exact hand
certificate first supplied by the V1 hostile audit.  V3 is proof-only.

V3 passed a fresh hostile audit and a separate statement-only blind
reconstruction.  It is promoted as P131.  No cross-family audit, human
audit, or publication-level literature review has run.
