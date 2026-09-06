# F232-D01 V1 hostile pre-run audit

## Verdict

**FAIL before execution.**  No mathematical run occurred.

The audited bytes were:

```text
STATEMENT.md  90265a37e03e5f86874b953fc8248aa7699f2113035d4a6ffeeaae64570749ac
PROOF.md      6b77708a7d6b93775f30c22553dd57649f41c65db0b19b3403c01af14a9e0744
F232_D01.cpp  b1265ed60e06fd29d3cb8a5017572b493bad2351f3dd3c5978ef1b1ae9665ff4
```

## Decisive mismatch

The preregistration promised to preserve every direct gcd event.  The V1
source retained only the first event in scalar fields and guarded later
events with `direct_factor == 0`.  It also said that `A` was factored only
when the direct gcd was trivial, while the source continued to factor `A`
after a proper gcd.

## Proof correction

The V1 proof said that exactly `2C` nonzero residues have least absolute
value at most `C` under only `ell>C`.  The correct count is at most `2C`
unless `2C<=ell-1`.  The displayed union upper bound remains valid after
this correction.

V1 must not run.  A V2 packet must record all direct events, align the
post-hit factorization rule, correct the residue count, receive a new hash,
and pass a fresh pre-run audit.

