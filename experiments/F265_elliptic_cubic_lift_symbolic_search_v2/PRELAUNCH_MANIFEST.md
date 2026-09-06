# F265-D02 prelaunch manifest

## Identity

- Experiment: `F265-D02`
- Family: canonical elliptic cubic-lift rows with complete P66 decoding
- Parent: immutable failed `F265-D01`
- Status: `STATIC_FROZEN; HOSTILE_AUDIT_PENDING; TARGET_VALIDATION_PENDING`
- Search result: none
- Target commands: forbidden while `F258-D01` is active

The V1 packet remains at
`experiments/F265_elliptic_cubic_lift_symbolic_search`. Its observed
`FROZEN.sha256` hash is
`9de9af4b9da746b8732913cf1cc4495ffb4b612d556cfd5e0ca8d7089cdcbb13`.
Its FAIL audit remains unchanged with hash
`7219be54b5a82ff4c043f86562118a23578f369e9e5869a51f61dbe5e8e9a67b`.

## Unchanged theory seam

F265-D02 keeps the exact V1 public curve, cubic row

`a_k=u_k^3+A*u_k+B=v_k^2 (mod N)`,

signed carry, direct controls, gcd-free P66 parity matrix, exact
product-square verification, normalized-root gcd classification, twelve
families, selection tuple, held-out decision labels, and finite-only scope.
It adds no elliptic family, scalar schedule, word, or asymptotic claim.

## Narrow V2 repairs

1. `POWER` retains the exact `A=0` outcome at `s=N-1`.
2. Both curves and every orbit must complete. A full row root or unresolved
   global affine exception is `BANK_SKIP`; no partial bank is eligible or
   strict.
3. Every final opaque block emits its value, sparse exponent vector,
   exact-square bit, and literal `UNKNOWN_NOT_NEEDED` status.
4. Every eligible bank exhausts the capped chord-block support and third-root
   miner. It records tangent/discriminant overlap, coordinates, and all six
   frozen index predicates. Exact aggregate counters continue after the
   deterministic witness cap.
5. Public `Case` objects contain no factors. The worker closure captures only
   public cases and jobs. Public cohort files contain no `p,q`. Factor labels
   attach only after every public batch has finished.
6. Uniform residue sampling is bounded. Pattern work is bounded. Evaluation
   uses deterministic 64-bank batches to bound retained memory.
7. Preflight times corpus generation and analysis/output separately, records
   CPU, RSS, rows, pair controls, gcd-free splits, and pattern work, and gates
   projected runtime and output.
8. Authentication, compilation, self-test, preflight, discovery, selection,
   heldout, and summary share one nice-15 deadline and global memory/file
   limits. Host and aggregate-output gates run between phases.

## Frozen source hashes

| File | SHA-256 |
|---|---|
| `ALGEBRA.md` | `d20b5271bb4441fe7d280e35e09a73ff5b0142abf2ed6d3e9839fe22ff4914c4` |
| `PREREGISTRATION.md` | `8e3c90420014939ba3ae58490bac2e85fc0a7a45523e12d332cadb5e1f6b384f` |
| `search.cpp` | `eeceba4db014346cc78dae3cbae29a65fb32946163becc5d9f5617fc465a7957` |
| `remote_run.sh` | `7d2e214d4fda2b6cc9ca15c4c30c34962f9865b356451fd0aee0e0c23be525b7` |
| `VALIDATION_PENDING.md` | `a6d88c8c8422c0cd46d55a98d157c239e9b7150a07e83cc3e14bd8467f6f689a` |
| `AUDIT_REQUEST.md` | `d53747fa102ef27405a0ae629a94667de6cf4b9f700a0cecd3c2aee86ad89aee` |

## Static checks completed

- `bash -n remote_run.sh` passed.
- `git diff --check -- experiments/F265_elliptic_cubic_lift_symbolic_search_v2`
  passed.
- `remote_run.sh` is executable.
- Every old V1 version/output token was removed from the V2 source and runner.
- The public cohort schema ends at `N`; only post-evaluation output contains
  `p,q`.
- No C++ compilation, source execution, remote command, input generation, or
  cohort inspection occurred.

Static checks are not dynamic validation. In particular, the source requires
the target Boost multiprecision headers and has not passed a compiler.

## Pending target sequence

A fresh independent hostile audit must first authenticate the freeze and give
PASS. Only after `F258-D01` and every incompatible process have ended may the
frozen runner:

1. authenticate `FROZEN.sha256`;
2. pass load, memory, disk, and process gates;
3. compile under the common resource envelope;
4. pass the exact self-test;
5. pass the generation-plus-analysis preflight time, RSS, and output gates;
6. run discovery and create authenticated selection bytes;
7. run heldout using only the four authenticated family IDs; and
8. create the finite summary and complete hash manifest.

Any failed gate is preserved. No unchanged cohort follows a failed gate.

## Scope

All future output is finite evidence. A displayed useful relation is an exact
factor certificate for its displayed modulus. A positive signal is not an
all-input success theorem. A null is not an asymptotic failure theorem.
