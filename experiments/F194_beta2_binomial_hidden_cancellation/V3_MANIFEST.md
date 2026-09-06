# F194 V3 manifest

Status: frozen metadata-repaired proof-only package. V3 reuses these exact
V2 mathematical inputs:

- `V2_STATEMENT.md`: `95764227ebc288a528c7425c5593e9a75d7ad9030556c4a9c12b00c0c85f48ab`
- `V2_PROOF.md`: `ea19a8a5fe2410e24841876a5b04c4e6e23e4f9f466838e0a9ebaf83ffcbb029`
- `V2_SELF_AUDIT.md`: `3b04854c356f7076841e47e088aff34b2007cc503400996e7efc011144bb8dbb`

It replaces only the provenance input:

- `V3_PROVENANCE.md`: `3d45bd68212f8231048e3fb7eb93d5e41a58da55c9cb075747d6d1c687d50c32`

Required review before promotion:

1. verify all reused hashes and the new provenance hash;
2. confirm that the V2 mathematical pass remains valid and the sole package
   defect is repaired;
3. obtain a strict statement-only reconstruction from `V2_STATEMENT.md` by
   an agent that has not read any F194 proof or audit file.

No mathematical computation or durable-ledger edit was used.
