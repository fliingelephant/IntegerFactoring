# F239 run log

## Preregistration

- `PREREG.md` was frozen before any F239 scan at
  `0ae27d2388282828ca10150d13abe5213a81d718f1a7d28d9eb899579dd5f412`.
- The pre-run word-size correction was frozen at
  `ddea9130f780d44acf7234628fbb6cd646227359c6a3b6eafa92420ae608b2cd`.
- After the first broad attempt rejected the two-primary cross-check, the
  approved protocol repair was frozen before rerun at
  `4f89d5a9041a7d4137a8d9c1978d6421fcf2fd0144c931192262533ebadc78ce`.

No domain, word menu, bound, ranking, or stopping rule changed.

## Resource check

The local Mac reported 16 GiB physical memory, 51% system-wide free memory,
load averages `2.27, 2.35, 2.08`, and 12 GiB free disk.  Sandbox policy
blocked `sysctl` CPU-count and `ps` details.

The authorized `seetacloud` host reported 32 CPUs, 503 GiB RAM, 367 GiB
available memory, no swap, and 22 GiB free disk.  Its load averages were
`56.79, 57.18, 57.29`.  Because the remote host was overloaded and the
scanner needed only one core and about 40 MiB, the exact runs stayed local.

The broad-domain row estimate was about 18 million.  The expected working
set was 32 MiB for the SPF table plus less than 10 MiB for primes and fixed
summaries.  No word was materialized.

## Environment and sources

- Date: 2026-08-13, Asia/Hong_Kong.
- Python: `3.14.5`.
- C++ compiler: `Apple clang 21.0.0`.
- Final `scan.cpp` SHA-256:
  `da11558445b91814225ec55c5be10a23bb1b9a42dc8b2c3857fdd8c3630bfe3e`.
- `named_scan.py` SHA-256:
  `ee00057017cc7b1ef1af03930d0edb331bacc3650f54e5a2397e030616f368e2`.

The C++ source compiled with

```text
clang++ -std=c++20 -O3 -Wall -Wextra -Werror scan.cpp
```

## Runs

1. The named Python scan completed in less than one second.  A requested
   positive nice value was denied by the local sandbox, but the process was
   single-threaded and negligible.
2. The first C++ F236-domain validation completed all 34,463 rows in
   `0.115923` seconds.
3. The first broad attempt opened `broad.out`, then aborted with exit `134`
   and `quotient incidence mismatch`.  The file remained empty.  The cause
   was the invalid local-congruence cross-check at `ell=2`.  No broad result
   was produced.  `ABORTED_ATTEMPT.md` preserves the event.
4. After the frozen repair, the unchanged F236-domain rerun completed all
   34,463 rows in `0.112158` seconds.
5. The unchanged broad rerun completed all 18,474,958 rows in `41.091`
   seconds on one process.

Each evaluated residual was checked twice: by prime incidence and by the
corresponding modular word.  The scanner aborted on any disagreement.

## Preserved outputs

- Pre-repair F236 output `zero.out`:
  `17bf0a432f2806fea7f0bfb92e1f6f04e38b471ef156d5a983d5a1c679f37cd4`.
- Empty aborted `broad.out`:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Named output `named.out`:
  `2f60d0a8a49bf5cedf252bef12126160b2aec113dccad4848159d8a39cd45b4c`.
- Corrected F236 output `zero_v2.out`:
  `e31176462ba5617b3555249df6b6ea5149aff3fbd6a367fb34d550a5f6fdbc6f`.
- Corrected broad output `broad_v2.out`:
  `b1914784d6babc2b3026260bcc0de82c7277c914aa94de2d17fe052bab0f75dd`.

No durable project ledger was edited.
