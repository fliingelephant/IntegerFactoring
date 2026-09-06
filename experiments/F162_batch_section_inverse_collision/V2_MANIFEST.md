# F162 V2 manifest

- Date: 2026-08-12
- Type: narrow proof-only correction
- Computation: none
- Durable ledgers: not edited
- V1 preservation:
  - `STATEMENT.md` SHA-256:
    `0cbc91e95b6068674f04d96b7af281b5cb9a28505bbcede043f284a15f3ca89e`
  - `PROOF.md` SHA-256:
    `a4f1767cf71d1eeeec8334ae6e293143e8c4ed886b828d99e90d07ee3134dbc9`
  - `MANIFEST.md` SHA-256:
    `451f164f5d46197192c977a3ae98093ccd11a7194d0acaa72d8db97b7ca9dde1`
  - `HOSTILE_AUDIT_FAILED.md` SHA-256:
    `a22f1f0f5d12fdb3c96804b32b85f0adf79d374b2902830f84998f9e7213ea76`
- V2 statement SHA-256:
  `89eb6821c394e70b779a014212a1d5ac50f3658ccfe6ffd21248a27f244b4899`
- V2 proof SHA-256:
  `582c100d7e39f85bd1cd4c154e77d6dea9de98d91581db4a6a1771f7ec3cfaa1`
- Exact repair: the total detector cost now includes
  `\widetilde O(rn)` for reading, canonicalizing, and deduplicating the
  explicit `r`-position input. The storage text now distinguishes resident
  input, multiplicity metadata, and post-normalization polynomial work.
- Shared-block accounting: `S_t` counts owner positions before deduplication,
  so it covers the sum of all V2 input-normalization terms.
- Unchanged claims: algebraic detection, derivative deflation, localization,
  shared-block normalization, F157 evidence, and all nonclaims.
- Review status: candidate; V2 requires a fresh hostile re-audit and an
  independent statement-only reconstruction before promotion.
