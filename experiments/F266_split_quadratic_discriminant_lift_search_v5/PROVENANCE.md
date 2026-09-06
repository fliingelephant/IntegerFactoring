# F266-D05 provenance

## Successor boundary

F266-D05 is a packaging successor to the immutable F266-D04 packet. It does
not define a new mathematical search. It preserves the D04 experiment ID,
families, source grammar, cohort construction, ranking tuple, output schema,
resource constants, and all computational behavior.

D05 exists because the attempted fresh D04 audit handoff named
`AUDIT_REQUEST.md`, but D04 did not contain that file. The audit stopped at
that missing-input boundary. It did not inspect or validate D04, did not
write `HOSTILE_PRERUN_AUDIT.md`, and returned no PASS or FAIL verdict. This
stopped handoff is a workflow event only. It is not audit evidence.

## Immutable D04 packet

The D04 directory remains unchanged. Its exact `FROZEN.sha256` SHA-256 is:

```text
1d4bae47d520e5f98f239c2867240e4f1251fd61eb9aaa010bbee17d45590772
```

Its frozen entries are:

```text
50ea42b05db7f1817e4cdde0847e4d0eee848ab6b5c6f2ef7d0bf8c368238157  ALGEBRA.md
ad937e55474ca8dd04e9c8d67f6406317082402d4f77149ad7e03c784c7dfce2  PREREGISTRATION.md
82e651211d2247d3a34ac39e561bdb908eacb70d1b8a547a25866181a5f54c9a  search.cpp
3441213ba996860f4bb87f599a9f0501795b8181314d09d3352d7b3ba74646b4  remote_run.sh
187c776797fedf07398d65e4cfc9332ae4caf2f6150c162db342266d61ac0746  PRELAUNCH_MANIFEST.md
```

D04 has no hostile audit artifact. It remains static and unauthorized for a
target invocation.

## Earlier immutable FAIL boundaries

The predecessor roots and hostile FAIL audits remain unchanged:

| Packet | `FROZEN.sha256` SHA-256 | Hostile FAIL audit SHA-256 |
|---|---|---|
| F266-D01 | `1ebfeff0b66cdec024a9612279675f435ad668059289865b581bf4d2b74a70e8` | `4880f3467e790519f39e278a78c0c808fd9b350afaafaf22c998823ec5cfc9c2` |
| F266-D02 | `723314508048e2a2de692314764ad83ab78ffc84ce10d10cce27b39d759dde2e` | `ca1fe923ce674d369aa75c8ef7557515e4ec88fc7acff84357950762fa5f104b` |
| F266-D03 | `07257b9e0820b1b1763984d382fcd49e6e6cf3d2d5db5666299813d4cb691984` | `a11cea775386f3d1178c46826c5db0b8042b49ad54bf056077ceaebd725bf73a` |

Those verdicts attach only to their exact packets. None authorizes D04 or
D05.

## Exact D05 delta

The following D05 files are byte-for-byte copies of D04:

```text
ALGEBRA.md        50ea42b05db7f1817e4cdde0847e4d0eee848ab6b5c6f2ef7d0bf8c368238157
PREREGISTRATION.md ad937e55474ca8dd04e9c8d67f6406317082402d4f77149ad7e03c784c7dfce2
search.cpp         82e651211d2247d3a34ac39e561bdb908eacb70d1b8a547a25866181a5f54c9a
```

`remote_run.sh` changes only frozen-packet bookkeeping:

1. it defines one required frozen-packet filename list;
2. before compilation, it requires that list and the filenames in
   `FROZEN.sha256` to be exactly equal;
3. it uses the same list for evidence-size accounting and the complete
   uncompressed evidence manifest; and
4. it passes the same list to the final archive, so `AUDIT_REQUEST.md` and
   every other frozen input are preserved.

The runner retains the D04 work directory, output names, audit-verdict
syntax, phase order, deadlines, limits, and target commands. The list-only
change does not alter a cohort, computation, selection, schema, or resource
constant.

D05 adds this provenance file and `AUDIT_REQUEST.md`. It replaces the D04
prelaunch description with a D05 packaging description. `FROZEN.sha256`
authenticates all D05 frozen inputs. It cannot contain its own digest, so the
coordinator supplies the expected digest of its exact bytes out of band.

## Static-only preparation

D05 preparation did not compile or execute `search.cpp`. It did not invoke
or parse-run `remote_run.sh`. It did not access a remote host, generate an
input, inspect a cohort, or edit a durable ledger. A fresh independent
hostile audit is required before any dynamic validation.
