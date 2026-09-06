# F253 V2 manifest

## Status

V2 is frozen after self-audit. It repairs the V1 strict-review failure. It
has not received a fresh hostile audit or a fresh statement-only
reconstruction. It makes no durable-ledger claim.

## V2 mathematical files

- V2_STATEMENT.md:
  53c7f59bc3f2a2e1b2f38d77661abfe94465945f5ce8691516e5c5c76ec277ba
- V2_PROOF.md:
  b76aed1d24455ec1a32d9c586d1b9f55f9b0c713273a9a3a7f1ba54b5ba1afec
- V2_SELF_AUDIT.md:
  d57ef56bffba57a3a4c6ecf46867ddbc8030b6cd9c9f88f367a1915c31ea64a0
- V2_PROVENANCE.md:
  7e104bfb26a75283d557168f525dab5af33d7d5fd6591e27ae59e6f97af6856f

## Frozen V1 packet and reviews

- STATEMENT.md:
  a9b32bd8bfdc68da9fb789ffae7640d1ae504b4ba382363a80427626a75bf2a0
- PROOF.md:
  8e4152f81aa709138003317bfc35b713746dbdcc385517284437ad34b59e6b90
- SELF_AUDIT.md:
  d1049f7a678ae51bf9ea8c19eda86604706ae1f7cbad93c73d34f42170b0ccaf
- PROVENANCE.md:
  dbfb371a979b919e383686c125eca1c95d77bc68baf33594191b5d8b17d0dc39
- MANIFEST.md:
  dc12ba42c05adc0c84ab693c99464a9a79887dc73f2b91c2b04229a5be37fa65
- HOSTILE_AUDIT.md, PASS with computation qualifications:
  ed2eeaa272cd7a6e85769ec64efab83acd4481993e0f39e4b09ecdf00a51abac
- BLIND_RECONSTRUCTION.md, FAIL on two-column scope:
  05386c64670c09c99b236d668959a5c6ff8428e01aa3095a1c52e06c38b9c906

## Preserved computation files

- V1_PREREGISTRATION.md:
  d30118370efb835b4585743499c72629641e74cba5205d8da6d002b9eb7a3f65
- search.py:
  8c037e858a85366932d187bb303d1de204c41da6619621586494ceb73d450d2a
- V1_STDOUT.txt:
  5ec9773a5030051a9dc0c8c7e01de0c065284ab0543fdb4cea8d756add6965ad
- V2_PREREGISTRATION.md:
  a94f5ab913fbc8899d977b65b62c5fa58014121de84588bac2f2afe078bff617
- search_v2.py:
  3dfa9fa6d4d753f76618fb51e219c5aa681f7ae07a24a2518511b04be66d4f89
- V2_STDOUT.txt:
  8b563b359363dac927fa8fd17b3d011c4ec54a6ff2ab25b8ef20a486e344e35e
- COMPUTATION.md:
  9ed4823c56462470b8e816af540e8494331b73560c857a709c35207e95b96415

## Repair and scope

V2 retains the P214 class-fibre rank and square-subset bounds, their abstract
rank sharpness, the odd-multiple polynomial identity, the carry identity,
and the finite \(N=4331\) certificate.

Its P66 pair theorem now requires odd \(k>1\), both index rows present and
retained, and \(y_{kj}\ne y_j\). The decoy span is generated only by these
actual nonzero two-column vectors. Modular repetitions, missing indices,
and cleanup-removed rows are excluded.

The repaired theorem does not bound carried or other arithmetic-
specialization dependencies. It is not a factoring algorithm.

