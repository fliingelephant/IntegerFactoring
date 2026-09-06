# F165-R06 source provenance

Status: frozen pre-run provenance. R06 has not run.

## Lineage

R06 preserves the completed R05 failure and starts from these byte-frozen
sources:

| Role | File | SHA-256 |
|---|---|---|
| Prior reconstruction | `f165_r04_v2_blind_reconstruct.py` | `a3b1a94440d3e6e580bccc6efe189a73a86adc366c4e617acc06a5a56377b42f` |
| Failed hostile comparison | `f165_r05_sequence_compare.py` | `2dcb4e871b890c16c575f2c0168295c757e40187b514a0d1c223a7034f85e397` |
| R05 authoritative output | `f165_r05_sequence_compare_output.json` | `9b61f73aa8b860ae6741b868edc1acaf309ce57f75e895c8a71dc3b637fba080` |
| R05 failure report | `F165_R05_SEQUENCE_COMPARISON_FAILURE.md` | `ef36a2c90a556d6d917ac9087c066487ca51fd3161a7b6b1bdf67d4431d0cc97` |
| R06 reconstruction | `f165_r06_v2_reconstruct.py` | `252123931d35856febfd93c07c8e22072564bf6310d75093d5eb169a07f09838` |
| R06 comparison | `f165_r06_sequence_compare.py` | `fa2742f2562f2288f7c93114fb4f02d1a6691ab920c46b62fbae23dfd4285c7b` |
| Frozen expectations | `F165_R06_EXPECTED_OUTPUTS.json` | `f4b066fbb1580a67846538c2381e9b7a377ad00225b9116fa3aaffa709eb1c68` |

## Sole mathematical change

R04 used one filtered list for two logically different tasks. It removed
`A=1` before factor-free integer refinement, which is correct, but then also
used the filtered list for parity-column construction, which differs from
D01.

R06 keeps all retained records in `active_records`. It applies `A>1` only to
the inputs of `factor_free_components`. The existing column loop then sees
the complete ledger. Thus each retained `A=1` becomes exactly the D01 column:

- square part 1;
- empty parity vector;
- decorated lift 1;
- one global-plus kernel dependency;
- no row, pivot, rank, or selected-basis effect.

The complete R04-to-R06 reconstruction diff is:

```diff
--- f165_r04_v2_blind_reconstruct.py
+++ f165_r06_v2_reconstruct.py
@@
-"""Statement-only reconstruction of the F165-R04 V2 finite replay.
+"""Corrected reconstruction of the F165-R06 V2 finite replay.
@@
 def decode(modulus: int, ledger: list[dict[str, Any]]) -> dict[str, Any]:
-    active_records = [
-        (label, record) for label, record in enumerate(ledger) if record["A"] > 1
-    ]
+    active_records = list(enumerate(ledger))
     components = factor_free_components(
-        [(label, record["A"]) for label, record in active_records]
+        [
+            (label, record["A"])
+            for label, record in active_records
+            if record["A"] > 1
+        ]
     )
@@
-        "schema": "F165-R04-V2-blind-reconstruction-1",
+        "schema": "F165-R06-V2-reconstruction-1",
```

The docstring and schema edits are identifiers. Moving the `A>1` filter is the
only mathematical edit. No corpus construction, relation generation, exact
ledger rule, factor-free component operation, row order, Gaussian elimination,
kernel arithmetic, selected-column rule, feedback support order, candidate
arithmetic, certificate check, aggregate expectation, or sequence encoding
changed.

## Comparison-source changes

The R06 comparison preserves every D01 normalization and semantic replay from
R05. Its changes are evidence plumbing:

1. read the fresh R06 reconstruction output;
2. pin the preserved R04/R05 evidence and R06 source/expectations;
3. require every R06 D01 comparison to pass;
4. compare every R06 sequence with the corresponding R04 sequence and require
   no sequence change;
5. require all 64 base decoder summaries to stay unchanged from R04;
6. at all 128 feedback snapshots, require columns, nullity, and global-plus
   count to increase by exactly one from R04, while rows, rank, global-minus,
   and non-global counts stay unchanged;
7. compare observed aggregate hashes and comparison counts with the frozen
   expected-output file.

The only changed comparison expectation is the one demanded by D01 semantics:
R06 column count equals the complete retained ledger size, not only the number
of records with `A>1`. Candidate, exact-value, block, and selected-column
normalization code is byte-derived from R05 and unchanged.

## Expected finite effect

R05 already certified that every input retains `A=1` by level one and keeps it
through level two. Therefore the frozen expected effect is:

| Scope | Columns | Nullity | Global plus | All four sequences |
|---|---:|---:|---:|---|
| 64 base snapshots | unchanged | unchanged | unchanged | unchanged |
| 128 feedback snapshots | R04 + 1 | R04 + 1 | R04 + 1 | unchanged |

Rows, rank, global-minus count, non-global count, selected bases, candidates,
exact ledgers, blocks, certificates, aggregate finite counts, and the four
detailed/value-only aggregate sequence hashes are frozen to remain unchanged.

## Boundary

R06 is a finite exact-reconstruction repair. It is not a retry of R05 at the
same paths. It does not erase or supersede the R01-R05 failure history. It
does not change or prove the fixed-depth theorem, and it makes no density,
growing-depth, all-input success, or factoring claim.
