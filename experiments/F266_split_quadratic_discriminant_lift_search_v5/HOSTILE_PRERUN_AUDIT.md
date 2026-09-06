# Verdict: FAIL

# F266-D05 fresh independent hostile pre-run audit

**DO NOT COMPILE, SELF-TEST, PREFLIGHT, OR LAUNCH THIS FROZEN PACKET.**

This was a read-only static audit. I did not compile or execute `search.cpp`,
invoke or parse-run `remote_run.sh`, access a remote host, generate or inspect
a cohort, or edit a frozen input, predecessor, or durable ledger.

## Frozen authentication

The coordinator supplied the D05 frozen root out of band. The observed
SHA-256 of the exact `FROZEN.sha256` bytes is identical:

```text
1ca5d0fa0748086c072399a6a1121a7bbe5d8bba984dd6615ca046a78c91a45a
```

The manifest has exactly seven unique filenames, and every entry matches its
local regular-file bytes:

```text
50ea42b05db7f1817e4cdde0847e4d0eee848ab6b5c6f2ef7d0bf8c368238157  ALGEBRA.md
ad937e55474ca8dd04e9c8d67f6406317082402d4f77149ad7e03c784c7dfce2  PREREGISTRATION.md
82e651211d2247d3a34ac39e561bdb908eacb70d1b8a547a25866181a5f54c9a  search.cpp
0a5de67c5aed282f224f5f066aa7520ddc87c44dd6e754733cc5d5666a90c695  remote_run.sh
57cfa9e4647d6eb862725b72a0211b8f4516f81b8fed9884da9ed18c028fe0c8  PROVENANCE.md
dfce437162930be20562d79f0721d62fe422867998cf3a4a8e9bf49a8a0a5ce9  AUDIT_REQUEST.md
8b569be2914009723c993398a57da3664684fce557bfcb977611dc2b257efa54  PRELAUNCH_MANIFEST.md
```

The immutable lineage also authenticates independently:

```text
F266-D01 FROZEN.sha256             1ebfeff0b66cdec024a9612279675f435ad668059289865b581bf4d2b74a70e8
F266-D01 HOSTILE_PRERUN_AUDIT.md   4880f3467e790519f39e278a78c0c808fd9b350afaafaf22c998823ec5cfc9c2
F266-D02 FROZEN.sha256             723314508048e2a2de692314764ad83ab78ffc84ce10d10cce27b39d759dde2e
F266-D02 HOSTILE_PRERUN_AUDIT.md   ca1fe923ce674d369aa75c8ef7557515e4ec88fc7acff84357950762fa5f104b
F266-D03 FROZEN.sha256             07257b9e0820b1b1763984d382fcd49e6e6cf3d2d5db5666299813d4cb691984
F266-D03 HOSTILE_PRERUN_AUDIT.md   a11cea775386f3d1178c46826c5db0b8042b49ad54bf056077ceaebd725bf73a
F266-D04 FROZEN.sha256             1d4bae47d520e5f98f239c2867240e4f1251fd61eb9aaa010bbee17d45590772
```

Every entry in all four predecessor manifests matches. Each D01--D03 audit
starts with its strict FAIL verdict. D04 contains neither
`HOSTILE_PRERUN_AUDIT.md` nor `AUDIT_REQUEST.md`, and no D04 verdict artifact
exists in the experiment tree.

## Decisive blocker

### The repeated sidecar gates do not authenticate their target bytes

The initial post-discovery gate authenticates both targets. It runs
`sha256sum -c` on the two sidecars and independently hashes the fixed
selection and corpus files before comparing both hashes with the read-only
digests captured from discovery stdout (`remote_run.sh:294-309`).

The two promised repeated gates are weaker. After heldout, lines 332-335 call
only `verify_sidecar_record`. Immediately before the complete uncompressed
manifest, lines 362-365 again call only `verify_sidecar_record`. That helper
(`remote_run.sh:130-141`) reads the sidecar record and checks its embedded
digest, fixed basename, byte count, and line count. It never opens or hashes
the named target.

Consequently, after heldout has read the authenticated selection and corpus,
either target can change while its canonical sidecar remains unchanged. Both
repeated gates still pass. The heldout program's final selection check hashes
its earlier in-memory copy, not the current file, and it has no corresponding
final corpus-file check (`search.cpp:1978-1984,2010-2011`). The heldout
program manifest covers only heldout outputs. The final uncompressed manifest
then records the changed target as ordinary evidence without requiring its
digest to equal the discovery-captured value, and the archive preserves that
inconsistent pair.

This violates the requested immutable sidecar-and-target closure and the
requirement that every repeated sidecar check authenticate the fixed target
bytes. Structural equality of the sidecar record is insufficient. This is a
launch blocker.

## Other priority checks

Subject to the blocker above, static inspection found the following closures:

- D05 `ALGEBRA.md`, `PREREGISTRATION.md`, and `search.cpp` are byte-identical
  to authenticated D04. The runner diff is limited to frozen-packet list
  assertion, authentication, evidence accounting, complete-manifest
  inclusion, and archive inclusion.
- The central seven-file runner list exactly equals the D05 manifest filename
  set. The same derived evidence list includes every frozen input,
  `FROZEN.sha256`, and the audit in evidence-size accounting, the complete
  uncompressed manifest, and the archive.
- The theory files, `DirectStage`, source/base allocations, 32 TSV columns,
  runner schema gate, counter partitions, and focused source/base self-test
  use the same eight-stage chronology. Source includes attempted `a,r,s,r-s`
  and inverse seed `u`; base includes `A0,B0,C0,Delta0,x` once per retained
  base and lift level.
- The shared gauge, fatal exact divisibility, direct-stage order, equal-row
  label, replay fields, opaque-block status, eligible distinct-row baseline,
  one-family null quantifier, ranking tuple and population, public/private
  boundary, factor-free decoder, cohort chronology, and declared resource and
  compression gates are present by static inspection.

These statements are source findings only. They do not claim compiler,
self-test, preflight, runtime, memory, remote, or cohort evidence.

## Required disposition

Preserve F266-D05 and this audit as an immutable failed packet. Do not execute
it. A successor must make each repeated sidecar gate hash the fixed target and
compare that hash with the captured discovery digest before final evidence is
accepted. Only a fresh hostile audit of the successor's new frozen root can
authorize dynamic validation.
