# F184 manifest

## Scope

Proof-only result. No mathematical computation was run. V1 passed a hostile
audit, but its statement-only reconstruction required deletion of one stray
comma in equation (5). V1 is preserved byte-for-byte. V2 makes only that
one-character deletion. It passed a fresh hostile re-audit and a strict V2
statement-only reconstruction, and root promoted it as P164.

## Frozen V1 files and review history

- `STATEMENT.md`: SHA-256
  `8bb68536d92e58cbbbcc6059950d0a3478e4854b50186bdc413af6919068ef3b`.
- `PROOF.md`: SHA-256
  `52c4c1ba6410241db7e03d739ee973af3b918d0a422999f1b6b67d6aec0c8c72`.
- `SELF_AUDIT.md`: SHA-256
  `c3be718e44f0bb4c4c206fdd4899ea72a918390b0d30505233616fceb3a373be`.
- `HOSTILE_AUDIT.md`: PASS with the equation-(5) typo noted; SHA-256
  `d60ffb94dea6465eec45e696875edd03d71e2f4335eabc8c36ed5b4562f0442c`.
- `BLIND_RECONSTRUCTION.md`: VERIFIED AFTER TYPO REPAIR; SHA-256
  `b03aa1cace54d97fecc20099c9f4af8917a11d9956061a0d0127d9fdb6e82236`.

## Frozen V2 files

- `V2_STATEMENT.md`: SHA-256
  `cf14b7ad25ecb9092419deaddca08327bcfe43d4bc9e35f89923a4f7e45f1632`.
- `PROOF.md` is reused unchanged at SHA-256
  `52c4c1ba6410241db7e03d739ee973af3b918d0a422999f1b6b67d6aec0c8c72`.
- `V2_HOSTILE_REAUDIT.md`: PASS; SHA-256
  `fa9b9cf22098d59a18334f0c8b8ca8bdc267323cafc57567b7042ed1a4fa6278`.
- `V2_BLIND_RECONSTRUCTION.md`: VERIFIED; SHA-256
  `aec36c26d664261abd71f2bb92c2a44b55392d796f11d000ed2d49c8556e8f83`.

The exact V1-to-V2 diff is the deletion of the comma after the opening
brace in equation (5). No theorem, proof, algorithm, or cost claim changed.

## Closest prior routes

- F180 / primary-period resultant filtering;
- F182 / two fixed wide shift menus;
- F183 / fully factored small-base extinction.

F184 is materially different because root counting forces one surviving
candidate in each block and therefore permits an arbitrary numerical QP
action-period cap without factoring any annihilator or resultant.
