# F12 elliptic-collision hostile-audit manifest

Approach-family ID: `F12_elliptic_collision_audit`.

## Inputs inspected in full

- `AGENTS.md`
- `PROMPT.md`
- `experiments/F12_elliptic_collision_kill/RESULT.md`
- `experiments/F12_elliptic_collision_kill/RUN_MANIFEST.md`
- all six manifest-named successful sources
- all ten retained logs
- all eight retained output files, including the two invalid partial JSON files

The five Sage-generated `.sage.py` intermediates were inventoried and hashed
by the audit run.  They are not treated as authoritative sources.

## Run A01

- Source: `audit_artifacts.py`
- Source SHA-256:
  `e32162fcacca47edb20bfa0f4647e10a502e895cb9e7ea45cbfebfd626b89ae1`
- Runner: `run.sh`
- Command: `./experiments/F12_elliptic_collision_audit/run.sh`
- Hard wall timeout: 60 seconds, enforced by `/opt/homebrew/bin/timeout`
- Dependencies: Python 3 standard library only
- Combined stdout/stderr log:
  `logs/R01_artifact_and_certificate_audit.log`
- Output: `output/R01_artifact_and_certificate_audit.json`
- Output SHA-256:
  `6f8158a73bee5093b1f4501303f10e2fa315e3e77f663d7e50a6587bc1098c37`
- Disposition: exit 0, `status=PASS`

The run independently enumerated both elliptic curves over their finite
fields, recomputed the retained point orders and floor-threshold collisions,
evaluated standard division-polynomial recurrences, exhaustively reproduced
the two torus success counts, parsed every successful/partial certificate, and
recomputed all manifest/R10 hashes.

Failure dispositions for this audit run:

- exit 0 plus `status=PASS`: use the output as finite certificate evidence;
- exit 124 plus `status=TIMEOUT`: retain log/output, draw no conclusion from a
  partial artifact;
- any other nonzero exit plus `status=FAIL`: retain artifacts, diagnose the
  named source, and do not cite partial calculations.

## Proof-only checks

The general division-polynomial identity, exponent collection, order
threshold, Hasse argument, probability formulas, hidden-exponent scan,
perfect-power handling, conditional recursion cost, and evaluator scope were
rederived symbolically in `RESULT.md`.  They are not inferred from A01.

No canonical file was edited and no commit was created.
