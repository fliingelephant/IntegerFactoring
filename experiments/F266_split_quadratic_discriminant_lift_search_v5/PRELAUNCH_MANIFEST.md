# F266-D05 prelaunch manifest

## Identity

- Packet: `F266-D05`
- Computational experiment: unchanged `F266-D04`
- Family: canonical split-quadratic discriminant lifts under public
  `SL_2(Z)` words
- Status: `STATIC_FROZEN; FRESH_HOSTILE_AUDIT_PENDING`
- Search result: none
- Dynamic validation: forbidden before a fresh D05 hostile audit passes

D05 is a packaging successor only. It adds the audit handoff that D04 lacked
and makes the runner preserve every frozen input in its evidence packet. It
does not create a new mathematical or numerical search.

## Immutable lineage

F266-D01 through D03 and their hostile FAIL audits remain unchanged. Their
authenticated roots and audit hashes are recorded in `PROVENANCE.md`.

F266-D04 also remains unchanged. Its frozen-manifest SHA-256 is
`1d4bae47d520e5f98f239c2867240e4f1251fd61eb9aaa010bbee17d45590772`.
The attempted fresh D04 audit stopped because its handoff named a missing
`AUDIT_REQUEST.md`. It produced no audit file and no verdict. It does not
authorize D04 or D05.

## Byte-identical computational payload

These D05 files are exact D04 copies:

| File | SHA-256 |
|---|---|
| `ALGEBRA.md` | `50ea42b05db7f1817e4cdde0847e4d0eee848ab6b5c6f2ef7d0bf8c368238157` |
| `PREREGISTRATION.md` | `ad937e55474ca8dd04e9c8d67f6406317082402d4f77149ad7e03c784c7dfce2` |
| `search.cpp` | `82e651211d2247d3a34ac39e561bdb908eacb70d1b8a547a25866181a5f54c9a` |

They retain the D04 identifiers by design. The algebra, source grammar,
families, decoys, cohorts, rankings, labels, output schemas, self-tests, and
resource constants did not change.

## Runner-list-only change

`remote_run.sh` retains every D04 command, path, phase, deadline, limit, and
output name. Its only change is frozen-packet bookkeeping:

- one central list names all seven entries required in `FROZEN.sha256`;
- a pre-compilation gate requires exact equality between that list and the
  manifest filenames;
- evidence-size and complete-uncompressed-manifest paths use that list; and
- the compression shell receives that list as exact arguments.

This makes `AUDIT_REQUEST.md`, `PROVENANCE.md`, and every other frozen input
part of authentication, evidence accounting, the complete uncompressed
manifest, and the final archive. `FROZEN.sha256` and the future hostile audit
are also included in evidence and the archive. The audit is not a frozen
input.

## D04 repair boundary retained

The preserved payload retains both D04 closures:

1. each convenience sidecar is one exact newline-terminated digest and fixed
   basename record, bound to a read-only discovery-stdout digest and checked
   after discovery, after heldout, and before the complete manifest; and
2. one eight-stage direct-screen chronology is identical in both theory
   files, the source enumeration and counters, the 32-column TSV schema, and
   runner validation.

It also retains all earlier repairs: one gauge per base and level, fatal exact
divisibility, registered screen order, correct equal/template labels,
replayable certificates, mandatory `UNKNOWN_OPAQUE_NOT_NEEDED`, the eligible
distinct-row baseline, one-family-across-all-cells null coverage, immutable
selection and corpus bytes, direct counters, measured serialized evidence
bytes, and whole-packet resource and compression gates.

## Frozen inputs

`FROZEN.sha256` authenticates exactly:

```text
ALGEBRA.md
PREREGISTRATION.md
search.cpp
remote_run.sh
PROVENANCE.md
AUDIT_REQUEST.md
PRELAUNCH_MANIFEST.md
```

The manifest cannot list its own digest. The coordinator must supply the
SHA-256 of its exact bytes to the fresh auditor out of band. The audit must
bind its verdict to that observed root.

## Static checks completed

- D01 through D04 manifest roots and all three predecessor FAIL audit hashes
  were authenticated before D05 creation.
- Every D04 frozen entry authenticated before D05 creation.
- D04 has no `HOSTILE_PRERUN_AUDIT.md` and no `AUDIT_REQUEST.md`.
- D05 algebra, preregistration, and source hashes equal D04 exactly.
- The runner diff is limited to one packet list, its exact manifest-name
  assertion, and reuse of that list in evidence and archive paths.
- The packet list and the frozen manifest name the same seven required files.
- The audit request names every frozen input, defines the out-of-band root
  binding, gives exact audit priorities, and forbids dynamic work.

These are static byte and source inspections. They are not compiler or runtime
claims.

## Pending gate

No D05 target command has executed. This preparation did not compile,
self-test, preflight, invoke the runner, access a remote host, generate an
input, or open a cohort.

Before any dynamic step, a fresh independent auditor must authenticate the
coordinator-supplied D05 root, every frozen entry, and the immutable lineage.
The auditor must write only `HOSTILE_PRERUN_AUDIT.md`. A passing audit must
contain these exact lines:

```text
# Verdict: PASS
frozen_manifest_sha256: <SHA-256 of the exact D05 FROZEN.sha256 bytes>
```

Only that PASS authorizes the unchanged D04 target validation sequence. It
does not authorize production after any failed host, conflict, resource,
self-test, preflight, output, or manifest gate. Any failure remains attached
to these exact D05 bytes and must not be edited or rerun silently.

## Interpretation

All future output is finite guidance. A positive certificate factors its
displayed modulus. A held-out null closes only the frozen grammar and corpus.
Neither result proves an all-input probability law or the top-level factoring
claim.
