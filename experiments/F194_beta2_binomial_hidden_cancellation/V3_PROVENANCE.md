# F194 V3 provenance

V1 is preserved byte for byte and failed hostile audit. V2 is also preserved
byte for byte. Its mathematical statement and proof passed hostile re-audit,
but its package failed because `V2_PROVENANCE.md` said “four repairs” while
`V2_SELF_AUDIT.md` listed five.

V3 reuses the exact frozen V2 statement, proof, and self-audit. It excludes
the defective V2 provenance file from the V3 input set. The five V2 repairs
were:

1. replace the false inequality in the central-binomial proof;
2. restrict cyclic aliasing to Boolean source incidence;
3. state that the gap bound is numerical QP;
4. require the joint modular residues of the coefficient and signed carry;
5. remove unsupported holonomic-algorithm language.

No mathematical claim or proof byte changes between V2 and V3.

Preserved failed audits:

- V1 hostile audit: `a3f49a53f54ac7bb69488958e7b1141d2206c61a834ef28bdd6e6c46d1be5fb9`;
- V2 hostile re-audit: `1e48b4c793a5502c2ada9d1058d8252d239487703cc99dbf53381da65b397385`.
