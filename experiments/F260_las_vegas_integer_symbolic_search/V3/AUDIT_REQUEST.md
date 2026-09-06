# F260-D03 V3 fresh hostile pre-run audit request

Audit the exact frozen F260-D03 packet from first principles. This must be a
fresh independent review. Do not reuse the D01 or D02 verdict.

## Frozen inputs before manifest assembly

```text
f94ad4119a2bb6bb4e795da536a7bf29823b6e2d1c509c51e9b42e27a26d490f  ALGEBRA.md
b8cd3e88b77aa2dd84ca655436a8e2dbd1e68100f827c89eb0b64abb006aefcf  PREREGISTRATION.md
1359cd6cdec022e01c19d6b704cd6705fdee2cb3db190058386aa3c49debdebc  search.cpp
098b586bb237c821ec47919e6667ff0abe8ccf785e8fc703492636185a9e2699  remote_run.sh
05e1b77d6182350039a24f120e49231894d0367b2b246d65ee05458b9782fc3f  PROVENANCE.md
d2dc1ef9e96549304debb34c859b5c7f698e2a9c3b1e4d7a8f62d22353cbcd59  VALIDATION_PENDING.md
64b97371317aab2f15fb5a8e68153a6cb1df07652d62ef25676780abbc156bfd  STATIC_REVIEW.md
```

Authenticate all final files through `FROZEN.sha256`. Authenticate that file
itself and record its SHA-256. Authenticate both predecessor FAIL boundaries
listed in `PROVENANCE.md` before relying on them.

## Decisive D03 regression scope

Reconstruct these repairs exactly:

1. every two-sequence product sorts complete normalized child syntax before
   construction of the word name;
2. the canonical word name is the exact byte string used by the modulo-five
   syntax hash and is preserved through semantic fingerprinting, IDs,
   grammar output, tie-breaks, selection output, and held-out parsing;
3. sequence, word, and factored candidates are completely enumerated before
   duplicate removal;
4. every duplicate fingerprint keeps the lexicographically first complete
   normalized syntax, independent of depth and syntax length, before the
   `(depth,length,syntax)` type sort and 4,096 cap;
5. the D02 forced `dyadic_carry` duplicate now keeps the correct general-rule
   representative, with no special-case patch;
6. each word cell stores exact rowwise minimum and maximum for both residual
   logarithms, worker merges preserve global extrema, output has the four new
   fields, non-word fields are zero, and both runner checks require 45 fields;
7. the D02 master seed, score formulas, source bases, transforms, grammar
   admission scope, cohorts, ranks, literal top-eight union, lead gates, and
   resource limits did not change; and
8. every source, runner, manifest, digest, output, and status label uses D03,
   while the conflict firewall also refuses D02 production.

Then audit all inherited boundaries from the D02 request: exact factored and
dyadic laws; P205 and distinct-value collision semantics; all gcd screens;
hypergeometric scope; oracle separation; bounded cohorts; data firewall;
authenticated selection; per-size aggregates and lead gates; and every
overwrite, output, manifest, audit, conflict, resource, benchmark, and shared
deadline gate.

The D01 quadratic loop, D01 top-eight drift, D02 canonical representative,
and D02 missing-extrema output are mandatory hostile regression checks.

## Audit constraints and output

Do not compile or execute `search.cpp`. Do not invoke or parse-run
`remote_run.sh`. Do not use a remote host. Do not generate, inspect, or score
a tiny or full cohort. Do not edit a frozen file or durable ledger.

Write only new audit artifacts:

```text
HOSTILE_PRERUN_AUDIT.md
HOSTILE_PRERUN_AUDIT.sha256
```

If and only if there is no blocker, the audit must contain these two exact
standalone lines:

```text
Verdict: **PASS — CLEARED FOR LAUNCH**
FROZEN_SHA256=<lowercase SHA-256 of the exact FROZEN.sha256 bytes>
```

The sidecar must contain one standard `sha256sum` record for
`HOSTILE_PRERUN_AUDIT.md`. A failure must use an explicit FAIL verdict and
must not contain the PASS line. The audit cannot claim compile, self-test,
benchmark, runtime, memory, runner-execution, or cohort evidence while
validation is pending.
