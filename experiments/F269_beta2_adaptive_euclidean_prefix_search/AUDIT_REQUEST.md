# F269-D01 hostile static audit request

Audit every byte named in `FROZEN.sha256`. Do not compile or execute the
source during this static gate.

Try to return `KILL` for one exact defect in any of these areas:

1. algebra or transcript mismatch;
2. incomplete normalizer or chamber-mask semantics;
3. root, tuple, provenance, tail-alias, value-alias, or invalid-reason drift;
4. cohort constructor, field fold, cap, or stage-count drift;
5. label leakage before the public-only collision pass;
6. selector or direct total-order drift;
7. selection authentication or heldout firewall drift;
8. missing aggregate, partition, certificate replay, witness, or verdict data;
9. preflight formula, serialization, compression, memory, disk, cgroup,
   deadline, F265 overlap, or evidence-cap bypass;
10. a C++17 or shell error visible by static inspection.

If the packet passes, create `HOSTILE_PRERUN_AUDIT.md` with these exact first
two lines:

```text
# Verdict: PASS
frozen_manifest_sha256: <SHA-256 of FROZEN.sha256>
```

Then state what was independently reconstructed. Do not claim a dynamic test.
Any source or contract edit after the audit invalidates that audit and needs a
new immutable packet and a new hostile review.

