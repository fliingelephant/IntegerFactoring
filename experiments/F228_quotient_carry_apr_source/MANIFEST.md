# F228 frozen manifest

## Status

F228 is a self-audited theorem candidate with verifier-backed finite
artifacts.  The mathematical theorem has not had a fresh hostile audit or a
proof-blind reconstruction.  Do not promote it before both reviews pass.

## Candidate theorem files

- `STATEMENT.md`
  - `d7b55ac83089b7b67783fe58f5669ae4ee035de8087b9303da07e9f8bb7f4f12`
- `PROOF.md`
  - `9ee7b7f2b7a9c70b210eed28c6b254f2c5f9ddebbb3753431d4cac04ce48c269`
- `SELF_AUDIT.md`
  - `5967451fcc4deab476dbce92d3d8f8394f447556e7eacc5c22a294aad771da50`
- `PROVENANCE.md`
  - `5260fe203030413612721e045e3247a91e0191c8fc2cd4531e9be5d5377bd486`

## D00 incident

- `D00_INCIDENT.md`
  - `5a938f06b839f51d8ef0785766617a23e5ca3b8d2e21c59049d0c23b221d721e`

## D01 files

- `D01_PREREG.md`
  - `3dc98596abf7c71191bb750b10e59901b68604bbf90fcc328551b9eda6e59e6f`
- `run_F228_D01.cpp`
  - `c3ebba44df3ba098e383fa84239c81503040fcf17e8dbed42927d5e601941256`
- `D01_OUTPUT.tsv`
  - `1702c92fd32dddb33a9f309e660a50ce0066c819f6d6e8837cfe134ddfdcee33`
- `D01_RUN.log`
  - `942e0c411cd3685c694049a09da3c953aac1a4d9a723b5d2be095a936d74d942`

## D02 files

- `D02_PREREG.md`
  - `337560cb1c35b78a80b026610f30fa3ce5ced1e1ed94daaca4f5954a19689f3a`
- `run_F228_D02.cpp`
  - `0a1b68b31e2029fafdcf6ec7ff6bc05666c0c4485e7e5ce4ea6129ec094aa606`
- `D02_OUTPUT.tsv`
  - `314ab2df46ba6b56c0a429266e050182725b4a28aa33b0b3d6b4b29ab1cd9392`
- `D02_RUN.log`
  - `e38839d743941696d709fcfa5910adda6e52343027d993631c1162d6b272a6aa`

## D03 files

- `D03_PREREG.md`
  - `040eb7a5bd5b25b271aa0c61a5f27fa380813e58ae0a4f3c01d2d54e2fbe0a67`
- `run_F228_D03.cpp`
  - `af923ebe14525856c360e1f62c9a390bd4ede95031b68d5680f6feafad0288d5`
- `D03_OUTPUT.tsv`
  - `a6de38c9e5a448d6dd5c1548989bd23e39787dd0054997f1e30e771901a5abc9`
- `D03_RUN.log`
  - `b9fec96c9c0a5d8546c9777878a8d02978e4af06d55307971ad24bedbb0a0da2`

## Local verifier

- `VERIFY_PREREG.md`
  - `c99d60afcaf47134cf7e4211635a0bb7510324b9074bca3820b71aaf083f00d6`
- `verify_F228.py`
  - `23204fb244392db96aba1c4f9868730c05437b26aa160dca2628733ffa2a5ea4`
- `VERIFY_OUTPUT.txt`
  - `6ab95948da2a42e462eb601ae23f5f26a79b0fffb5ec584762fa668b8e34cd06`
- `VERIFY_RUN.log`
  - `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

## Frozen material claims

1. Numerical-QP bounded quotient shifts have half-plus-polylog bit length
   and a fixed-ratio QP recursion.
2. Direct quotient gcds equal carry-defect gcds.
3. Every odd common-primary block in a shifted quotient is already present
   in `u-R_u+cB`.
4. APR-compatible quotient primes obey the exact inverse-lift laws
   (10)--(14).
5. Uniform random shifts have the harmonic tail (18); this does not cover
   integer-biased multiplier laws.
6. The finite safe-prime search remains positive without the divisor cap;
   it does not prove an all-input probability bound.

## Highest-risk audit points

1. Distinguish common-primary support capacity from the global-return event
   that certifies it.
2. Keep equation (8) restricted to odd primary support.
3. Check all signs in (5), (6), and the inverse lift.
4. Check the `ell|u` exclusion and `i=0` endpoint.
5. Verify that random-shift dominance does not silently claim a bound for
   random multipliers or adaptive heavy shifts.
6. Treat D02 capped zeros as cap artifacts, as corrected by D03.
