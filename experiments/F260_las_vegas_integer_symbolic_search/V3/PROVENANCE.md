# F260-D03 V3 provenance

## Immutable predecessors

F260-D01 and F260-D02 remain failed immutable predecessors. D03 does not
replace, edit, reinterpret, or promote any predecessor byte.

The authenticated D01 boundary is:

```text
09691b4f5d005a330b85952dd9bfe4a0b93c2e5de7c23832d53572d4db5700a2  ../ALGEBRA.md
3b9c13374e38cba1394e9528fccb5ab623a6164829a3394f434f6b81acf38714  ../PREREGISTRATION.md
d4263fb8ceef91caecc4480ee3b49d8cd670b6ff34bb0920d8469c47ddf7e44e  ../search.cpp
7215ee1d9e34ee34146ca8ed992e96c582defc0cfd7b40bba39a91b78e98d103  ../remote_run.sh
7087694e8019280675f660eae88eec88620f33ffca323d29b180c33100d13d05  ../PRELAUNCH_MANIFEST.md
9e49fb75f86b5ccdd7b3290053099cd822ab547a06495dbee82f64ff7a5e636d  ../HOSTILE_PRERUN_AUDIT.md
```

The D01 hostile verdict is `FAIL — DO NOT LAUNCH`.

The authenticated D02 boundary relevant to D03 is:

```text
d0ceeddbab866cc9d35f85565ffc0f3282a955fd22603d666e9d00790dd00229  ../V2/ALGEBRA.md
2ebd75dea01d34fe72682d45524abc2e6072618866393d963ba6dccd221059d7  ../V2/PREREGISTRATION.md
c6d0f016e471911c115a497311ef05e5682c796df6c3887626ac5cb25bcb3911  ../V2/search.cpp
6812855a4ef7b87c351cfe1c29d098dae0470788139d9ca27b7c8d94f5de43be  ../V2/remote_run.sh
f85d202ea5bf7247a74da99c57b76703ba9d91b6d04430c4cccfda42b09918eb  ../V2/PRELAUNCH_MANIFEST.md
6a87e1dba63d60a9a5d94c08f22960db337bad9ea3eadd3f39868a87d25c0b3e  ../V2/FROZEN.sha256
281945088bf2b9d701c55c0cab6663ad8842daf80a6fe883129a4ea5b22d6a29  ../V2/HOSTILE_PRERUN_AUDIT.md
e8b23b346715fd23964db11496932522228af6a69948ad65c963af75fe82e975  ../V2/HOSTILE_PRERUN_AUDIT.sha256
```

The D02 sidecar verifies its audit. The D02 hostile verdict is
`FAIL — DO NOT LAUNCH`.

## D03 repair boundary

D03 is a narrow new experiment. It retains D02's exact score formulas,
candidate sources and transforms, master seed, cohorts, ranks, literal
top-eight selection, lead gates, and resource limits.

It repairs only the two D02 hostile findings:

1. Every commutative word child list is sorted by complete normalized syntax
   before the word syntax is constructed or hashed. For each candidate type,
   all candidates are enumerated, the lexicographically first normalized
   syntax is chosen for every duplicate fingerprint, and only then are the
   representatives sorted by `(depth, syntax length, syntax)` and assigned
   IDs.
2. Every word aggregate cell stores and outputs the minimum and maximum of
   both residual logarithms, in addition to their means. Worker-local extrema
   merge into exact aggregate-cell extrema. Non-word extrema fields are zero.

The experiment label and exact-output names advance from D02 to D03. The
runner checks 45 aggregate fields and refuses concurrent D02 production.
These are mechanical consequences of the new packet, not score or cohort
changes.

## Preparation record

The D03 packet was prepared as new sibling files. It is intentionally
uncommitted. No predecessor or durable ledger was edited. No C++ source or
shell runner was compiled or executed. No local or remote corpus was
generated, opened, or scored. No remote transfer occurred.

