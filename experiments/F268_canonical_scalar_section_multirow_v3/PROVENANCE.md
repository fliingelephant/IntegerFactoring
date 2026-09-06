# F268-D03 provenance

F268-D02 is immutable. Its exact `FROZEN.sha256` digest is:

```text
31e05f0f310ff6f0b37421ccf68634bf57bce65cb708074408dec96b7801561b
```

Every D02 frozen entry authenticates. Its independent hostile pre-run audit is
`experiments/F268_canonical_scalar_section_multirow_v2/HOSTILE_PRERUN_AUDIT.md`
with SHA-256
`1b2c37510ec4680d0c8996d3654108e8727e9a44e92acf8523c550b79735a7b0`.
That audit gave `FAIL` before compilation, execution, corpus generation, or
remote access.

The audit found two independent defects. First, D02 preregistered 200,000
candidates for every prime request, but its marker source supplied an explicit
cap of 128 candidates to each congruence-class prime request. Second, its
runner recognized only selected F265 search and runner command lines. It did
not reject every F265 corpus, label, validator, compiler, preflight, or packet
process.

D03 makes the existing bounded marker construction exact instead of expanding
it. Each requested marker row retains 4,096 seeded pair attempts. Each pair
attempt retains at most 128 candidates for `p = 13 (mod 24)` and at most 128
candidates for `q = 11 (mod 72)`. The source now names all three marker caps,
and the preregistration states them. This preserves the D02 source cohort
without generating or viewing it. It also bounds one requested marker row by
1,048,576 constrained-prime candidate tests. Applying the ordinary 200,000-
candidate cap at both nested requests would instead admit 1,638,400,000 tests
per requested marker row and is not the intended resource-safe control.

D03 also broadens `refuse_overlap` to reject any process command line that
contains `F265` or `f265`. The bracketed grep expressions do not match the grep
process itself. This one conservative token rule covers F265 packet paths,
version tokens, corpus generators, search binaries, label auditors, validators,
compilers, preflights, and runners.

Apart from these two repairs, the packet/output version change, the corrected
D03 template-version sentence, and this provenance, the algebra, family
syntax, master seed, public grammar, marker candidates, ordinary cohorts,
screen chronology, ranks, caps, resource projections, and target commands are
unchanged from D02.

No D03 C++ source has been compiled or executed. No D03 cohort has been
generated or viewed.
