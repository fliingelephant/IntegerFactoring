# F268-D04 validation status

F268-D04 has not been compiled or executed. No C++ self-test, corpus
generation, preflight, discovery, heldout evaluation, evidence replay, label
audit, local numerical search, or remote command has run.

D04 is the narrow validation successor to immutable D03. D03 passed its fresh
hostile pre-run audit. During the authorized validation sequence, all three C++
programs compiled and the corpus self-test passed. The search self-test then
failed before the label self-test, corpus generation, preflight, discovery, or
heldout phases. The failed target contains no search evidence.

D03 used `0x2748774U` for SHA-256 round constant 46 instead of the standard
`0x2748774cU`. It also authenticated `FAMILY_SYNTAX.tsv` before its `"abc"`
known-answer test. D04 changes that one constant and executes the known-answer
test before family-file authentication. No other search logic changes.

Completed checks are static only:

- the immutable D03 manifest root, hostile `PASS`, failed validation result,
  and failed-run manifest have the exact hashes recorded in `PROVENANCE.md`;
- the exact algebra and closest-route distinctions remain unchanged;
- the complete low-support chronology remains unchanged across algebra,
  preregistration, source, self-test, and audit request;
- the family syntax, seed, cohorts, screens, ranks, caps, projections, and
  target commands remain unchanged after normalizing D04 version tokens and
  the two specified validation repairs;
- the SHA-256 table now contains the standard `0x2748774cU` constant exactly
  once and no `0x2748774U` token;
- the `"abc"` known-answer test precedes family-file authentication in the
  search self-test;
- discovery ranking still has an arithmetic-only interface;
- `FAMILY_SYNTAX.tsv` has one compiled SHA-256 in C++ and the runner;
- `bash -n remote_run.sh` passed;
- the D01, D02, and D03 immutable files and all post-freeze artifacts were not
  changed;
- `git diff --check -- experiments/F268_canonical_scalar_section_multirow_v4`
  passed; and
- no durable research ledger was edited by this packet author.

Static review does not establish C++ syntax, runtime correctness, resource
feasibility, marker availability, or a mathematical search result. A fresh
no-context hostile audit is required before the target sequence. A hostile
`PASS` still does not replace compile, self-test, complete-corpus, largest-bank
preflight, replay, and label-audit gates.
