# F268-D04 finite search result

status: `FINITE_NULL_SIGNAL`

The frozen C++ packet completed. All self-tests, replay validations, label
audits, and resource gates passed. The strict finite-lead gate failed. The
finite-null gate passed.

This is finite evidence only. It closes only the frozen F268-D04 grammar and
cohorts. It does not prove an all-input factoring claim, an event law, or a
runtime law.

## Result

| Metric | Discovery | Heldout |
|---|---:|---:|
| cases | 188 | 296 |
| banks | 2,256 | 1,184 |
| eligible banks | 2,256 | 1,184 |
| resource-rejected banks | 0 | 0 |
| banks with any public factor | 356 | 0 |
| banks with an earlier direct factor | 356 | 0 |
| strict stage-8 factor banks | 0 | 0 |
| useful singleton certificates | 0 | 0 |
| useful support-two certificates | 0 | 0 |
| low-support relations | 0 | 0 |
| residual relations | 0 | 0 |
| total P66 kernel dimension | 0 | 0 |
| total residual dimension | 0 | 0 |

The discovery direct screens recorded 4,936 proper-gcd events across stages
1--3. They occurred in 356 banks. These factors are discovery-corpus direct
controls. No heldout bank produced a proper gcd at any stage.

Every eligible bank had full row rank. Thus every P66 kernel had dimension
zero. The low-support and residual stages had no relation to test. No symbolic
multirow pattern survived into heldout.

## Frozen selection

The selected family order was:

1. family 10, `multi_exponent`;
2. family 0, `hash_nm1`;
3. family 1, `hash_np1`;
4. family 2, `hash_n2m1`.

The selected template IDs were `0,1,2,3,4,5`: support-three, support-four,
same-exponent, mixed-exponent, multiplication-triple, and power-chain.

All families had zero strict banks, zero residual-positive banks, and zero
residual dimension. Family 10 ranked first because it used fewer frozen rows.
The other selected families followed the frozen tie-break. Every template had
zero incidence, so the frozen ID tie-break selected templates 0--5.

## Lead and cohort gates

- `strict_finite_lead = 0`.
- `finite_null_signal = 1`.
- Heldout eligibility was 1,184 of 1,184 intended banks.
- Every ordinary heldout family/bit/shape cell had all 24 intended cases.
- Both splits had eight marker rows.
- The corpus had zero marker-shortfall cells.
- The discovery and heldout label audits passed.

The null gate is therefore valid for this exact finite experiment. It has no
asymptotic meaning.

## Time, memory, and output

- Corpus generation: 0.04 wall seconds; 4,060 KiB peak RSS.
- Bank preflight: 50.81 wall seconds; 11,148 KiB peak RSS.
- Discovery: 59.146005 wall seconds; 107,388 KiB peak RSS;
  16,651,834 output bytes.
- Heldout: 1,082.001378 wall seconds; 159,664 KiB peak RSS;
  26,181,829 output bytes.
- Resource-capture interval for the complete runner: 2,262 seconds.
- Final raw remote target size: 44,669,051 bytes by `du -sb`.

The preflight projected 7,282.846667 wall seconds, 1,404,560 KiB live memory,
and 225,349,437 output bytes. These values passed the frozen limits of 12,600
seconds, 3.5 GiB, and 768 MiB. The gate observed zero resource rejects and 44
completed large banks.

## Authentication

- Frozen-manifest bytes:
  `de76f2e3fbb264b917cedb5639fde75c979f272e43841452c6f642b8132cdbf4`.
- Hostile pre-run audit bytes:
  `22644c280c477e0d6f0272d343bdf15f9421036b9db7c169b951e647cbee26be`.
- Remote full result manifest bytes:
  `bdc96777472722a05cd6ef22eb710d03bc1249fe6bda09cf03ef10514e058afc`.
- Frozen selection bytes:
  `7117de790efaa2afb7a7f84ff2917ca744560671c1d0f7a8a271586418f89df5`.
- Discovery evidence bytes:
  `a0ef66750b51aa311be854c207331f018d4a420c04c7bb749206cf8781dc67dc`.
- Heldout evidence bytes:
  `80763b6d0f1a3c956586f46d9fb441659b072756f67bd58585173526132b626a`.

The exact remote `F268-D04.final.sha256` file remains in this directory. It
lists every raw target artifact except itself. Every listed digest passed on
the remote host before transfer and passed again against the local copy.
