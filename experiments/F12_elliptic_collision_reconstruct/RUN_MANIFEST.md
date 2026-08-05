# F12 reconstruction manifest

Approach-family ID: `F12_elliptic_collision_reconstruct`.

## Blindness and scope

This reconstruction used only the corrected bare statement, `AGENTS.md`, and
the status/computation rules in `PROMPT.md`.  No canonical research file was
listed, searched, or read.  Neither forbidden F12 experiment directory was
listed, searched, opened, or used.  All new work is confined to this fresh
directory; no canonical file was edited and no commit was created.  No web
search or subagent was used.

## Finite computation

The general arguments in `RESULT.md` are proofs, not extrapolations from the
finite run.  Only the explicit curve/point certificate was computed.

| Run | Hard timeout | Named source | Result | Combined log |
| --- | ---: | --- | --- | --- |
| 001a | 120 s | `src/verify_finite.py` | exit 0; global checks, curve counts, point orders, all affine denominators, and first collisions verified | `logs/run_001_combined.log` |
| 001b | 120 s | `src/audit_finite.py` | exit 0; independent double-and-add order/minimality and collision audit | same combined log |
| 002 | 120 s | `scripts/finalize_manifest.sh` | exit 0; immutable inputs/outputs and self-excluding final artifacts verified | `logs/run_002_combined.log` |

Before run 001, `manifests/run_001.inputs.sha256` fixed both sources, both run
scripts, parameters, and the timeout plan.  The primary certificate was hashed
in `manifests/run_001.primary_outputs.sha256` before the independent audit.
There were no failed runs or timeout dispositions.

The final `manifests/final_artifacts.sha256` excludes itself and the active
run-002 log/failure paths, whose contents are not stable while it is being
created.  It includes the proof, manifest, immutable run-001 evidence, source,
logs, and retained outputs.

## Evidence status

The result is self-audited.  The two finite implementations use distinct
addition strategies, but no fresh hostile agent, different model family, or
human has audited this reconstruction.  The conditional evaluator theorem is
proved symbolically; no evaluator computation or benchmark was substituted
for its missing algorithm.

