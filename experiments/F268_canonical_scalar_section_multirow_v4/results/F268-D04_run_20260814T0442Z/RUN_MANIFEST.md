# F268-D04 run package manifest

packaged_utc: `2026-08-13T21:31:42Z`

remote_source: `/root/autodl-tmp/F268-D04_source_20260814T0442Z`

remote_target: `/root/autodl-tmp/F268-D04_run_20260814T0442Z`

local_package:
`experiments/F268_canonical_scalar_section_multirow_v4/results/F268-D04_run_20260814T0442Z`

## Source authentication

The remote source mirror and the local frozen packet had the same manifest
and audit digests. Remote `sha256sum -c FROZEN.sha256` passed all eleven
entries.

| Item | SHA-256 |
|---|---|
| `FROZEN.sha256` | `de76f2e3fbb264b917cedb5639fde75c979f272e43841452c6f642b8132cdbf4` |
| `HOSTILE_PRERUN_AUDIT.md` | `22644c280c477e0d6f0272d343bdf15f9421036b9db7c169b951e647cbee26be` |
| `PRELAUNCH_MANIFEST.md` | `97e8dbb2635f798505f75d55603153ca0b815b2c0cf58c7e10e8a36c5fa80ad5` |

The authenticated frozen entry digests are preserved in the packet-level
`FROZEN.sha256` file. No frozen source file was changed during packaging.

## Raw result authentication

The raw remote target contained 45 files in eight directories. Its exact full
manifest is preserved as `F268-D04.final.sha256`. The manifest excludes only
itself and contains 44 absolute remote-path records.

| Item | Value |
|---|---|
| `F268-D04.final.sha256` SHA-256 | `bdc96777472722a05cd6ef22eb710d03bc1249fe6bda09cf03ef10514e058afc` |
| raw target file-byte sum | 44,663,722 bytes |
| remote `du -sb` size | 44,669,051 bytes |
| manifest records checked remotely | 44 of 44 passed |
| manifest records checked locally | 44 of 44 passed |

The transfer used recursive preservation mode. Raw file modification times
were preserved. The earliest recorded raw target time is
`2026-08-14T04:49:36+0800`. The final manifest and post-run audit files have
time `2026-08-14T05:27:18+0800`.

The local check replaced only the absolute remote path prefix while reading
the manifest. It did not modify the preserved manifest or any raw artifact.

## Main result hashes

| Artifact | SHA-256 |
|---|---|
| discovery public corpus | `8b6f8dbe4eae9aa10c042928fc19fbe20a0015487340e7478135ce6f37b5adb5` |
| heldout public corpus | `b4a4c976013dd62c58376b948c51a1c5c380265a46fbf932a5e0972fb6c389d5` |
| selection | `7117de790efaa2afb7a7f84ff2917ca744560671c1d0f7a8a271586418f89df5` |
| discovery bank table | `c908bfd6c30f73864dc1f2b83ace770b3d117f72d98e2e086c4f4f51064b2ef6` |
| discovery evidence | `a0ef66750b51aa311be854c207331f018d4a420c04c7bb749206cf8781dc67dc` |
| heldout bank table | `3c4cd71a9c705c4902e68cfc1d55bd108ad2b3f815740219448154d431677157` |
| heldout evidence | `80763b6d0f1a3c956586f46d9fb441659b072756f67bd58585173526132b626a` |
| heldout lead report | `2a85fda3458e603132066bbd1c862a32b68bf59c14a056285172323b036c8976` |
| discovery label audit | `015d7fc983b1158f913536bad6f698743e42c972818d414a30f1ac4c89d935da` |
| heldout label audit | `388ad098c46089c0f873e3f4ac2da24c023b2754eef4822503980275505ad278` |

The preserved full manifest is authoritative for every binary, corpus,
table, evidence file, log, metric file, and preflight artifact.

## Validation chronology

1. All three C++ programs compiled.
2. The corpus, search, and label-audit self-tests passed.
3. Corpus generation produced 484 cases and zero marker shortfalls.
4. The complete large-bank preflight passed.
5. The resource projection passed.
6. Discovery completed and froze the selection.
7. Discovery replay validation passed.
8. Heldout authenticated the frozen selection and completed.
9. Heldout replay validation passed.
10. Both post-run label audits passed.
11. The runner wrote the final full manifest.

This package records finite experimental evidence only.
