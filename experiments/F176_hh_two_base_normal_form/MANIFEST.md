# F176 V3 manifest

## Approach-family ID

F176_hh_two_base_normal_form

## Artifact type

Proof-only candidate. No computation is used as evidence.

## Question

Can the unique base-two hard normal form be made hard beyond arbitrary fixed
numerical QP absolute and quotient caps without losing exact-state progress?

## Candidate answer

Yes. Use \(\Lambda_B\) for any fixed numerical QP cap \(B\ge n\). A common
return of order \(m>n\), including \(n<m\le B\), is already an exact
common-order state. A common return at most \(n\) gives the same
Mersenne-factor or sign-doubling transition. The remaining block has a
local primary component above \(B\) and local sign-quotient order above
\(C\) in every hidden component.

This is a standalone QP source normal form. It does not factor the hard
base-two branch.

## Preserved review chains

The complete V1 chain is frozen under the V1 filenames. The complete V2
chain is frozen under the V2 filenames. Important V2 hashes are:

- V2_STATEMENT.md:
  c7634a4c9a72552ce7d822857abe381623c343e8920dc3a859277913b260aac1
- V2_PROOF.md:
  fc135fcb02b13900a5e97b130c80e1596d09841bf2da5382d59739f0095c50b4
- V2_SELF_AUDIT.md:
  eebf70ce764bf8baf35f87448330a3ff31c6a9f15bf2b39cfefaf77453b34070
- V2_MANIFEST.md:
  939fc2bdf4be1f502dfa08410673dbdc64aaa089252b700a58909d5385af5c97
- V2_HOSTILE_REAUDIT.md:
  990f8a12665ea100922df389a83a75aa81ec26efa4daa465b52cf4495f7efc2a
- V2_BLIND_RECONSTRUCTION.md:
  a425dfb273a00d2c891974f2509d6b9b89f6787cc0343febf52dcad6aab767e3

The V1 hashes remain recorded in V1_MANIFEST.md.

## Current files

- STATEMENT.md: V3 theorem, parameters, outputs, cost, and exclusions.
- PROOF.md: stripping, QP-cap, Mersenne/sign, relative, and recursion proofs.
- SELF_AUDIT.md: V3 delta, scope, prime-power, and history checks.

## Required next checks

1. Fresh hostile re-audit of V3.
2. Fresh statement-only reconstruction after a passing hostile re-audit.
3. Recheck the intermediate common-order range \(n<m\le B\).
4. Recheck the uniform QP cost of constructing \(\Lambda_B\).
5. Recheck that Outcome C quantifies over every fixed QP cap choice only.

No durable proof ledger should be updated before those checks.
