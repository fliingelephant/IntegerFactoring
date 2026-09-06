# F263-D02 V2 prelaunch manifest

## Decision

**FROZEN; NOT AUDITED; DO NOT LAUNCH COHORTS.**

This packet repairs F263-D01 without modifying or deleting any D01 input,
failure record, validation artifact, or hostile audit.  An independent
hostile pre-run audit must pass before `V2_remote_run.sh` may start discovery.

## Frozen source packet

```text
V2_PREREGISTRATION.md  6dd1c052cb4eebba07e40b75b527254c6daa6e771bd12082fe161fb1ae11946a
V2_ALGEBRA.md           fdf72364070e5b0ded549be171afcf005dc063afe4d7179968aa58ffdbb318d6
V2_symbolic_search.cpp  05c0b87a453eb3c2c40c01bf058b0559a6ff2e9b943d16ddcf68d147b1f4c827
V2_remote_run.sh        006e12b87552457c931eea7200a5eb6b5ba8417624a6d3b0b4d7969700b42d18
V2_preflight_remote.sh  18339cadf29d9f9fd3e9bf9dd7605b44aa9c2e4421d29481266f431df8eeaaf6
V2_PROVENANCE.md        fa8d69c29a92eead321fe069c337f40f2095074cb7e9dd3922c86392c42762bd
```

## Frozen final validation evidence

```text
V2_TARGET_CHECKS/benchmark.monitor   cae458f80880453dfdc4451691d259d201babc36078772adbaa33c3b16f16384
V2_TARGET_CHECKS/benchmark.stderr    e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
V2_TARGET_CHECKS/benchmark.stdout    e8ad67d813bb7862ec0e244d165fa263c636303dae14d9d546a24eb05a4fc0e3
V2_TARGET_CHECKS/compile.stderr      e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
V2_TARGET_CHECKS/compile.stdout      e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
V2_TARGET_CHECKS/final.sha256        6c478770c9bac50fa2001c5660006aba6cb571fb95943f26d1601a9634c15a43
V2_TARGET_CHECKS/resource_before.txt 5d59a3c89be8a895d1b1a2091c48b52166a6bbff7af4ab25ebefeec73402a15b
V2_TARGET_CHECKS/self-test.monitor   368255f16709b0acf5f62e3500b2a8fe225c000111c7b58615168897bc79b40a
V2_TARGET_CHECKS/self-test.stderr    e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
V2_TARGET_CHECKS/self-test.stdout    a704f95947f722b1a4df485d8f89b6335b390c5459bbbe3a9737e33e0e77f81c
```

## Preserved D01 boundary

At V2 freeze, the D01 hostile audit remained exactly:

```text
HOSTILE_PRERUN_AUDIT.md  2e5801933e3eb26b6aa1c3f8cb3e23d5d199297051ae451484cf26d791446099
```

The D01 audit decision remains `FAIL. Do not launch discovery or held-out
cohorts from this frozen packet.`  V2 does not reinterpret that decision.

## Validation result

The exact target source compiled with empty stdout and stderr.  The final
self-test passed with 12 controls, 70 columns, ranks `58,58`, nullities
`12,12`, 9,801 signed halves, 14 sparse identities, 12 small basis relations
from each prime, zero shortcuts, four adjacent recurrences, zero dyadic
recurrences, 148 candidates, and exact cohort counts `848,1152`.

The public benchmark passed with `modulus_bits=120`, 390 constructed states,
926,880 leaf touches, 4.995265 seconds inside the executable, and 32,024 KiB
peak process-tree RSS.  The corrected full bank contains 2,000 rows.  The
conservative time projection is 166.5 minutes after an eightfold load and
generation factor.  The conservative memory projection remains below
1.6 GiB.  Both fit the four-hour and 4 GiB caps.

## Launch requirements

Before any cohort launch:

1. authenticate every entry in `V2_FROZEN.sha256`;
2. obtain an independent hostile pre-run audit of this exact packet;
3. require audit decision `PASS` without a blocking qualification;
4. confirm no F258-D01 through F263-D01 production process is active;
5. preserve all prior remote validation and D01 artifacts;
6. launch only the frozen `V2_remote_run.sh` in a fresh remote directory.

This manifest records no cohort result and authorizes no ledger edit.
