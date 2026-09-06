# F191 V2 manifest

## Frozen V2 candidate files

- `V2_STATEMENT.md`
  - SHA-256: `4666ed13b2318932a357c5a35ef4021c83355bf78cfeab3ffa1eb7bd6c8ac9ce`
- `V2_PROOF.md`
  - SHA-256: `807d7c7e30ec7950e083bd9624050a1859fe724ce74843bcb16b64f3b184ca39`
- `V2_SELF_AUDIT.md`
  - SHA-256: `6ef91e68f5bd64ef3640049b07cf9132306ce6fa706933065cdcfb18afe8f275`
- `V2_PROVENANCE.md`
  - SHA-256: `105a343c01b27abf467cf740d080af6bae012f754315988c6f2e491562ba753e`

## Preserved V1 review state

V1 remains frozen under the hashes in `MANIFEST.md`. Its fresh hostile audit
returned **FAIL** and is preserved in `HOSTILE_AUDIT.md`, SHA-256
`d3ae15732f7f1beccd1d5a9c37cabf2a8ab11d821069822b7e7f69755ee2de69`.
V2 does not overwrite or retroactively repair V1.

## Evidence class

Proof-only candidate. No mathematical computation was run. Hashing was used
only to freeze the text. No durable proved, failed, registry, or progress
ledger was changed.

The support-conservation identity and canonical counterexample are elementary
integer congruences. The finite bank theorem uses an exact endpoint count and
a union bound. No external theorem is invoked beyond the already-promoted
P161 and P163 interfaces in the conditional application.

## Exact repaired scope

V2 preserves the V1 named-model obstruction. It now distinguishes a merely
divisible quotient or carry from a direct P163 auxiliary. The latter must
satisfy `0 < |A_j| < N/2`, or a separate support-preserving size-localization
theorem is required. It also excludes `D = 0` as a usable carrier and fixes
the order of the QP bank-budget and roughness-cap quantifiers.

## Required next reviews

1. Fresh hostile audit of the frozen V2 statement, proof, self-audit, and
   provenance record.
2. If that audit passes, fresh statement-only blind reconstruction.
