# F194 manifest

Status: frozen proof-only candidate. No mathematical computation and no
durable-ledger edit were used to establish the theorem.

Frozen inputs:

- `STATEMENT.md`: `d5ec288bb9b4f4e3fbf5cdad9c51bbcc1fb7d8560f9dd2c5a7b45c698a9ebd25`
- `PROOF.md`: `ac2f813a83a4c499aeda1defec5a1445b09bc1e94c24ce1b5048753116afc29a`
- `SELF_AUDIT.md`: `8fe673fbfba9116bed3444c0ad0133a80df943c3ce15439d06958a7cc5260cdf`

Required review before promotion:

1. a fresh hostile proof audit that checks all inequalities, signs,
   cancellations, local Frobenius expansions, and cyclic-sketch scope;
2. a strict statement-only reconstruction by an agent that has not read the
   proof or self-audit.

The candidate bytes must not change during either review. Any repair must be
preserved as a new version.
