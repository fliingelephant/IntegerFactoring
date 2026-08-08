# F119 final re-audit SHA-256 manifest

Each hash is SHA-256 over the exact file bytes. This manifest does not embed a
self-hash because adding that value would change the file being hashed.

| Role | File | SHA-256 |
|:---|:---|:---|
| Preregistered question | `QUESTION.md` | `7dba1e0092302380bd9989d218cc144aa6026c44214ee215145285424f5e9c7f` |
| Corrected proof and result | `RESULT.md` | `552a54c8382341709305e53bd535efd9ef0ec0bc7957fa32be8ddc5c061f4575` |
| Corrected preserved routes | `FAILED_ROUTES.md` | `be2afb89c6299e8de5ca0b818796d12994bb51f8a0ba912c020a908066eca563` |
| Corrected F119 manifest | `MANIFEST.md` | `0eae5b2c53fa87b54b4f9d3f4c99faee205e3dc5f6b18278a5e799089835308d` |
| Reconstruction statement | `RECONSTRUCT_STATEMENT.md` | `4a4aaf43119609e7745b5f88623a3ea9fb3c72aac7d15b16062d1aef0e692986` |
| Historical hostile audit of original theorem | `HOSTILE_AUDIT_REPORT.md` | `e01ef19c93ac09c1909f2b4bf5f4c9f479df0b7fb8db9d3179d756bc053bd468` |
| Historical hostile-audit failed routes | `HOSTILE_AUDIT_FAILED_ROUTES.md` | `4eb3315406ad196a01b80d9f72efc35c29968554d27cc27f590ce5951f3e8d24` |
| Final corrected-theorem re-audit | `FINAL_REAUDIT_REPORT.md` | `a629dc043d915caaf9ac1240b018f5c72014849f89bf31969a57c992121cf6ae` |
| Final re-audit rejected extensions | `FINAL_REAUDIT_FAILED_ROUTES.md` | `51f443e071e0a4b1787fdeb0faa2c615fc9c83e1bb0345929b71e2977540ec76` |

The final verdict is `PASS` for the corrected `RESULT.md` hash shown above.
The historical verdict remains `PASS_WITH_CORRECTIONS` for the original result
hash recorded in `MANIFEST.md` and `FINAL_REAUDIT_REPORT.md`.

This was a proof-only audit. No evidentiary program or mathematical computation
ran. SHA-256 was used only for artifact integrity. There is no source, timeout,
run log, program output, or failed program-run artifact to pin.
