# F268-D02 provenance

F268-D01 is immutable and failed its author's post-freeze static audit before
any dynamic work. Its exact `FROZEN.sha256` digest is:

```text
b99d47d7ba7a01c456a0b755a5e77f42a237be73ffd6ea422e38d03b076a1cc9
```

Every D01 frozen entry still authenticates. Its post-freeze failure record is
`experiments/F268_canonical_scalar_section_multirow/SELF_AUDIT_FAIL.md` with
SHA-256
`8ab91efa95e1aa20f0985f80c28790340987d4b61f3bbb662707587a4b2642c2`.

The exact defect is standards-level: D01 `label_audit.cpp` uses `std::tie`
without directly including `<tuple>`. D02 adds that include. It also changes
the packet and serialized version token from `F268-D01` to `F268-D02`, updates
the frozen hashes, and adds this provenance. The algebra, family syntax,
master seed, public grammar, cohorts, screen chronology, ranks, caps, resource
gate, and runner commands are otherwise unchanged. D01 produced no corpus or
numerical observation, so D02 does not reuse a viewed cohort.

No D02 C++ source has been compiled or executed.
