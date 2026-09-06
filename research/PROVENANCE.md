# Evidence Provenance

The 2026-09-06 cleanup preserves the mathematical ledger bodies and historical
experiment paths. Catalogs provide navigation; they do not reclassify claims as
independently verified or rewrite old audit conclusions.

## Ledger snapshot

These SHA-256 values identify the working-tree sources at the start of cleanup:

| Source | SHA-256 |
| --- | --- |
| `PROVED.md` | `90ce03e6b5c7c8763a0b638b001029bd6160012328351f2c2779f17c3852447b` |
| `FAILED.md` | `4e3e0ebd92dae2cf081018caf09a46a46e2b0bcf08287e073cfe14c7888b70e6` |
| `REGISTRY.md` | `38f625074e1e924d20fe32d387aa2ff953da533b16e762c4128f7b69c771e61a` |
| `STATEMENT.md` | `19ddee417e1eb402af7d3ea26cd6e31467a3b96a762ebbe45fe262a90a961ac9` |
| `notes/Progress.md` | `fc5697d3a4bcfdef3b1a61f9180c9ea78439d96769f78cbc4082935d084aafb3` |

The starting Git checkpoint is `00c2a80`. Substantial later research was already
present as uncommitted changes and untracked experiment packets. The cleanup
checkpoint includes that work; it does not claim to have performed it.

The later Rust migration replaces the Python navigation tool and normalizes
the catalogs to schema 3. Existing IDs, mathematical bodies, recorded status
and scope text, route assignments, and source selectors are preserved. The
partial graph contains explicitly sourced relations selected for navigation;
it is not an independent proof audit or a completed dependency map.

## Known missing working-tree artifacts

The following tracked files had already been deleted before cleanup:

- `experiments/F04_joint_matroid_audit/output/matrices/A03_P11_mod_100000007.sobj`
- `experiments/F04_joint_matroid_audit/output/matrices/A03_P11_mod_199999991.sobj`

They occupy about 830 MB combined and remain recoverable from Git checkpoint
`00c2a80`. Their working-tree absence is preserved. This cleanup does not claim
that every historical run can be replayed without retrieving missing artifacts
and recreating its environment. Do not rewrite Git history to remove them.

## Motivation source

`notes/Zhihu.md` was absent in the starting working tree. Its English translation
is restored for future reading. The Chinese source is retained in Git at
`00c2a80:notes/Zhihu.md`; the translation is not a mathematical audit.

## Runtime files

Python bytecode and Sage runtime cache directories are no longer tracked.
Existing local cache files may remain for reuse. Source programs, reports, logs,
finite outputs, and certificates are retained. Cache removal is not an evidence
review, and the catalogs do not certify every historic hash or external path.

Historical artifacts also retain their original whitespace. Some source diffs
and TSV rows trigger Git whitespace warnings, including meaningful empty final
TSV fields. The cleanup does not reformat those bytes to silence a style check.
New navigation documents and tooling are checked separately.
