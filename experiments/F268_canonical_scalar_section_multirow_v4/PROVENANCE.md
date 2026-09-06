# F268-D04 provenance

F268-D03 is immutable. Its exact `FROZEN.sha256` digest is:

```text
19e856152caebdddc374c72444acc5f1bbd727a9c722e0e183ee2f6c70cf720f
```

Every D03 frozen entry authenticates. Its independent hostile pre-run audit is
`experiments/F268_canonical_scalar_section_multirow_v3/HOSTILE_PRERUN_AUDIT.md`
with SHA-256
`23a3e7921fa54ee1c7048ed7fc05b116f61ee76b88af2fb2275d7b13f8bd3a04`.
That audit gave `PASS` and authorized only the frozen validation sequence.

The packaged D03 validation failure is
`experiments/F268_canonical_scalar_section_multirow_v3/results/F268-D03_remote-validation-fail_20260814T0416Z/RESULT.md`
with SHA-256
`399fcea77a78c26cbfdab214dc00d186474a3ed898acb3ff0ddc2ebf16e6e459`.
Its `RUN_MANIFEST.md` has SHA-256
`f493a1302f44a9d3b3798156813bde2c3a88e7a1ba5225b3246c841974d295e9`.

The unchanged D03 runner compiled all three C++ programs. Its corpus self-test
passed. Its search self-test then failed with `family syntax SHA mismatch` and
returned 70. The label self-test, corpus generation, preflight, discovery, and
heldout phases did not run. The failed target contains no search evidence.

The frozen family file, runner digest, and compiled expected digest all agree.
The D03 custom SHA-256 table instead contains `0x2748774U` at round constant
46, while the standard constant is `0x2748774cU`. D03 also authenticates the
family file before it executes the `sha256_bytes("abc")` known-answer test, so
the artifact-authentication error hid the implementation failure.

D04 changes that one constant to `0x2748774cU` and moves the existing `"abc"`
known-answer test immediately before the first family-file authentication in
the search self-test. It also changes packet and output tokens from D03 to D04
and updates frozen provenance, validation, audit, and manifest metadata.

Apart from those validation repairs and version/metadata changes, the algebra,
family syntax, master seed, public grammar, marker candidates, ordinary
cohorts, screen chronology, ranks, caps, resource projections, and target
commands are byte-for-byte unchanged from D03 after normalizing `F268-D04` to
`F268-D03` and the two specified search-self-test repairs.

No D04 C++ source has been compiled or executed. No D04 cohort has been
generated or viewed. No local or remote target command has run.
