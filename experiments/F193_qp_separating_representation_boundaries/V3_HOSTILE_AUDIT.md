# F193 V3 hostile audit

## Verdict

**PASS.** The frozen V3 candidate is promotable as exact text, subject to the
separate statement-only blind-reconstruction gate.

No mathematical computation was used.

## Freeze verification

The files match `V3_MANIFEST.md`:

- `V3_STATEMENT.md`:
  `286ff3962751262c7256e5d78cfb0b510fb9563523765c9c9776e949eaeadc05`
- `V3_PROOF.md`:
  `71b21f064ddbc3e03bdaef8989125d7e3d68d88939a71845e16a6d184fbc188b`
- `V3_SELF_AUDIT.md`:
  `50bc537b117aec8705c4dc9017ef7914d8ca441a37fcbc2059d684ae44fd08c6`
- `V3_PROVENANCE.md`:
  `348e7f7659d21cfc9651f58a4784452cb556664b768687aa2d630ddb11589e9c`

The exact V2-to-V3 diff in the statement and proof contains only version
labels, one Greek-letter TeX cleanup, the explanation of the revision, and
the two repairs

\[
X^2-\operatorname{Tr}(\alpha)X+\operatorname{Nm}(\alpha).
\]

No bare `+operatorname{Nm}` or other malformed `operatorname` remains in the
frozen V3 statement or proof.

## Claim checks

1. **Sparse cusp boundary: PASS.** At squarefree level, prime divisibility of
   the reduced denominator is invariant under `Gamma_0(N)`, and the usual
   cusp classification has no extra residue label. Thus an explicit endpoint
   of type `p` or `q` exposes a gcd, while a chain supported only at types `1`
   and `N` has boundary in their degree-zero line. The good-prime Hecke,
   Fricke, and explicitly labeled selective Atkin--Lehner conclusions follow
   with exactly the restrictions stated. The candidate does not claim control
   of the boundary coefficient, cuspidal classes, dense encodings, bad-prime
   operators, or opaque Atkin--Lehner circuits.

2. **Small-modulus CRT amplification: PASS.** The bound
   `0 < b_N < 2(N+1) <= 2^(n+1)` is sufficient. A bank of `n+2` distinct
   primes below `C n log(n+2)` has product above that bound. Uniform QP calls,
   CRT, and the discriminant recover `p+q` and then `p,q`. The claim remains
   conditional on one uniform growing-bank evaluator and does not cover a
   fixed modulus or finite fixed bank.

3. **Dirichlet-twist rank: PASS.** The coefficient identity holds also for
   imprimitive characters with zero values. The bank is the image of one
   coefficient under public scalar multiplication, so its rank is at most
   one. An all-zero bank has rank zero; one nonzero row permits division by a
   root of unity. V3 correctly distinguishes the defining modulus from the
   conductor and makes no evaluator lower-bound claim.

4. **Connected-base auxiliary torsion: PASS.** Since `r` is invertible,
   `E[r]` is a rank-two lisse `F_r`-module. On a connected base, etale path
   transport is natural in the globally descended endomorphism, so its two
   fiber matrices are conjugate. The listed invariants follow. For a global
   CM endomorphism, Tate-module trace and determinant give the now correctly
   typeset characteristic polynomial. Local Frobenius, reduction-only maps,
   characteristic-primary torsion, and disconnected CRT gluings remain
   explicitly outside the theorem.

## Strict scope

The combined conclusion is four narrow boundary results. It is not a lower
bound for arbitrary modular-symbol, modular-form, finite-etale, elliptic-
torsion, or separating-representation methods. No blocking mathematical or
scope issue was found.
