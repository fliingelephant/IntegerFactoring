# F194 V2 manifest

Status: frozen repaired proof-only candidate. V1 and its failed hostile audit
remain preserved. No mathematical computation or durable-ledger edit was
used.

Frozen V2 inputs:

- `V2_STATEMENT.md`: `95764227ebc288a528c7425c5593e9a75d7ad9030556c4a9c12b00c0c85f48ab`
- `V2_PROOF.md`: `ea19a8a5fe2410e24841876a5b04c4e6e23e4f9f466838e0a9ebaf83ffcbb029`
- `V2_SELF_AUDIT.md`: `3b04854c356f7076841e47e088aff34b2007cc503400996e7efc011144bb8dbb`
- `V2_PROVENANCE.md`: `a7d5e7fdddfe9688797cf5bb0052ae12d4278d04eddb8df1fd3e995059077a61`

Required review before promotion:

1. a fresh hostile re-audit of the exact V2 bytes;
2. a strict V2 statement-only reconstruction by an agent that has not read
   any F194 proof or audit file.

Any further repair must preserve V1 and V2 as historical inputs.
