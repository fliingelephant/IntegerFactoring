# F187 manifest

## Frozen candidate files

- `STATEMENT.md`
  - SHA-256: `9434188bf8c35cbd54d0f6f553b7e0698f19470745515bb1fe503fbe8b67f14e`
- `PROOF.md`
  - SHA-256: `0f3790117a8e6ed34fbdaa934b576cbdec2ef248865ef9c5268aeb262f77f7cb`
- `SELF_AUDIT.md`
  - SHA-256: `cc77bd2116d0e2309e1ee20c57dfbf225a814546a20228478ada7cf2b008854b`

## Evidence class

Proof-only candidate. No mathematical computation was run. No durable
proved/failed ledger was changed by these candidate files.

The deterministic stripping theorem and exact probability laws are
elementary. The obstruction for each bounded-gap prime pair is elementary.
The passage to infinitely many such inputs invokes the standard
bounded-prime-gap theorem as an external proved result.

## Exact scope

F187 closes an inverse-QP success claim for independent uniform random-base
sampling after complete recursive factorization of \((N-1)/2\). It does not
close adaptive or deterministic base selection, other exponent families,
or integer factoring. Its QP recurrence covers only an enclosing stage whose
unique recursive child is \((N-1)/2\); it does not charge additional children
used to complete a returned factor split.

## Required next reviews

1. Fresh hostile audit of the frozen statement and proof.
2. If the hostile audit passes, fresh statement-only blind reconstruction.
