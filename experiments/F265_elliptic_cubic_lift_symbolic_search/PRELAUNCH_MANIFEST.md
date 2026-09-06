# F265 prelaunch manifest

## Identity

- Experiment: `F265-D01`
- Family: canonical elliptic cubic-lift rows with complete P66 decoding
- Status: `STATIC_FROZEN; TARGET_VALIDATION_PENDING`
- Search result: none
- Cohort launch: forbidden while `F258-D01` is active

## Theory seam

The closest prior route is X14/P20. It pools cleared elliptic
`x`-coordinate collisions through a square-root-scale index. F265 instead
materializes a bounded small-index affine orbit, emits the exact public rows

`a_k = u_k^3 + A*u_k + B = v_k^2 (mod N)`,

and applies the complete factor-free square-class decoder to all admitted
rows. Its target is a nonduplicate multirow relation after denominator,
discriminant, row-root, singleton, equal-row, inverse, square-multiple,
coordinate-collision, and chord gcd controls.

The theory seam was reported to and approved by the root agent before this
directory was created.

## Frozen files

| File | SHA-256 |
|---|---|
| `ALGEBRA.md` | `be4a2d5b74656a0a34ee11da7972d92c78123386258e20eb28c726179fac42ca` |
| `PREREGISTRATION.md` | `f24e878f5d2080faa1a297969e638f4f15b1adba7c993c731861fc1408f1361b` |
| `search.cpp` | `96ba06af46e274836975c7e79f2bd2a5096e83c0ea4b35e770b12a701ac4a835` |
| `remote_run.sh` | `35465d726b42b52d07c821c9d26cac0e2cdd4647ed1c7fdf2060f1a9d0312f65` |

## Static checks completed

- `F265` was free before directory creation.
- `bash -n remote_run.sh` passed.
- `git diff --check -- experiments/F265_elliptic_cubic_lift_symbolic_search`
  passed.
- The runner is executable.
- The source has fixed row, block, split, retry, thread, wall, memory, and
  output caps.
- The discovery selection bytes include the discovery-cohort SHA-256.
- Heldout reads only the authenticated four-family selection.
- Opaque gcd-free blocks are never called prime and need no Pollard--Rho
  factorization.

## Pending target checks

This Mac does not provide the Boost multiprecision headers used by the
frozen C++17 source. No substitute integer type or local Python workflow was
used. Remote compilation and self-test are intentionally pending because
the approved protocol forbids dynamic validation while `F258-D01` uses the
target host.

Before any cohort, a fresh target check must do all of the following without
changing the frozen files:

1. authenticate `FROZEN.sha256`;
2. record target CPU, memory, disk, load, and active processes;
3. compile with `/usr/bin/g++ -O3 -DNDEBUG -std=c++17 -pthread`;
4. pass the exact P20, cubic identity, gcd-free decoder, integer-square, and
   normalized-root self-tests;
5. run the scaled preflight under eight workers, 4 GiB, `nice 15`, and the
   four-hour shared deadline;
6. require projected wall time at most 12,600 seconds and peak RSS at most
   3.5 GiB; and
7. obtain a fresh hostile pre-run audit PASS.

Failure is preserved under a new immutable version. No unchanged cohort is
launched after a failed gate.

## Scope

All future output is finite discovery evidence. Neither a positive
certificate nor a held-out null proves the all-input factoring statement or
an asymptotic success/failure law.
