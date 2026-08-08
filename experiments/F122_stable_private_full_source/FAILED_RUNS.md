# F122 Failed Runs

## 2026-08-08T06:15:21Z — external task interruption

The first registered run was interrupted when the parent task continued in a
new execution context. The source did not report a timeout, exception, failed
check, or nonzero exit. Its last exact checkpoint was in the all-pairs phase
after 437,360 of 2,758,520 attempts and 90 of 780 pairs.

The checkpoint already had two proper direct screens and 2,928 non-global
fundamental roots. It is valid prefix evidence, but it is not a complete
source result.

Preserved artifacts:

- `OUTPUT_FAILED_20260808T061521Z_INTERRUPTED.json`, SHA-256
  `5f56256a37773068fd759e88d9fffd0e35744a497795b13d877e5dbad39374ed`;
- `RUN_FAILED_20260808T061521Z_INTERRUPTED.log`, SHA-256
  `91ee1a6285f2203aef56bf6478cdcc3d41bceb9149f040b84025339e849f5e7b`.

The registered source, corpus, runner, timeout, and acceptance condition are
unchanged for the retry.

## 2026-08-08T06:22:06Z — stopped to limit memory pressure

The unchanged retry reached 1,278,360 of 2,758,520 attempts and 340 of 780
all-pairs menus. Peak resident memory was 992,903,168 bytes. The user reported
a computer memory problem while the run was active. The parent stopped the
run with an interrupt to avoid further pressure.

The exact checkpoint had 704,274 distinct exact columns, nullity 86,763,
42,071 non-global basis roots, and three proper direct screens. Every basis
dependency excluded the private seed-2 column. This is decisive prefix
evidence that both direct extraction and `ROOT` succeed before feedback, but
it is not a complete-source terminal record.

Preserved artifacts:

- `OUTPUT_FAILED_20260808T062206Z_STOPPED_MEMORY.json`, SHA-256
  `8ac59375e8f6f478e1a801068e4ae66756c5714217d16d956da6c5ca95cf7c47`;
- `RUN_FAILED_20260808T062206Z_STOPPED_MEMORY.log`, SHA-256
  `e0ba341f4161740f757330b30bd1a956a1577acb4e98694a18158c8e333dbd89`.

No further full no-stop retry is justified for this input. The registered
feedback gate is already closed by exact prefix witnesses.
