# F146 manifest

**Family:** F146_qpoly_aks_exchange_boundary.

**Type:** proof-only boundary.

**Computation:** none.

## Version history

V1 is preserved and failed hostile audit because it claimed a false
local-field if-and-only-if for non-squarefree inputs. The failed audit is
also preserved.

| Artifact | Status | SHA-256 |
|---|---|---|
| STATEMENT.md | frozen V1; failed | 0cc469a3e44393ed6ec28517b3de0c3b64b8cb473fe37d9835c4f220168bb257 |
| PROOF.md | frozen V1; failed | 0c89b48f29979b3b0d0d8bdbae76d0b2bdecefdf9445d9cda87f923b7344d007 |
| HOSTILE_AUDIT_FAILED.md | frozen V1 audit | 1b69e598ceadabe26f9402aa3125898e8dc1fb826936876cc7a2ee72b4c96640 |
| V2_STATEMENT.md | promoted V2 statement | 886ca7aafa5d5cd42514fa4fbd6223a9e7ca12a368820a8c53b9731b3553ac57 |
| V2_PROOF.md | promoted V2 proof | d4836162de32274bf253461b3f712c8e6d5662127ac2a907dc723d7c028a093c |
| V2_HOSTILE_REAUDIT.md | V2 hostile re-audit: pass | 2b42343c0ba2edcc88b9d3c32cf4769a4b395c4b5590286781f3359788b07dc0 |
| V2_BLIND_RECONSTRUCTION.md | V2 statement-only reconstruction: pass | 3faaf0f299da164a31d30ed7a2a853476418c64b149c033e983bb0b18d70ac22 |

MANIFEST.md describes these frozen artifacts and is not self-hashed.

V2 passed a fresh hostile re-audit and an independent statement-only blind
reconstruction. It is promoted as P133. The blind reconstruction verified
the exact P11 comparison formulas and integer counts; it could not recompute
four quoted decimal evaluations because the statement intentionally omits
the two P11 prime values. This does not affect a theorem claim.

## Exact V2 repairs

1. V2 defines the gcd-success radius \(\gamma_B\). For every composite
   \(N\), scan success is equivalent to \(\gamma_B\le s\).
2. The local-field disagreement radius \(\delta_B\) is only a sufficient
   condition for arbitrary composite \(N\).
3. V2 states \(\gamma_B=\delta_B\) only for squarefree \(N\).
4. Valuation-only splits on non-squarefree inputs are explicitly retained as
   extra successes.
5. The count bound is

   \[
   Q_s(A,t)\le(s+1)\max\{1,At\}^{s},
   \]

   so it includes \(t=0\).

All other V1 theorems retain their prior scope.

## V2 claims

1. exact exchange-minor count through support \(s\);
2. quasipolynomial bit complexity for \(s=\operatorname{polylog}(n)\);
3. completeness for local column-matroid comparison when the tail is
   polylogarithmic;
4. a near-threshold prime-modulus condition that makes the AKS tail
   polylogarithmic;
5. an explicit balanced CRT family with first matroid disagreement at an
   arbitrary exchange support;
6. a random-singularity scale calibration of the finite P11 certificate.

## Claims excluded

- no AKS-specific local-disagreement theorem;
- no equality of gcd success and residue-field mismatch for general
  non-squarefree inputs;
- no claim that AKS minors are random;
- no all-input factoring algorithm;
- no computation or empirical search.
