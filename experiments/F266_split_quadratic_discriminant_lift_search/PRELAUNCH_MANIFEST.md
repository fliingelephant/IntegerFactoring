# F266-D01 prelaunch manifest

## Identity

- Experiment: `F266-D01`
- Family: canonical split-quadratic discriminant lifts under public
  `SL_2(Z)` words
- Status: `STATIC_FROZEN; HOSTILE_AUDIT_AND_TARGET_VALIDATION_PENDING`
- Search result: none
- Cohort launch: forbidden while `F258-D01` is active

## Approved theory seam

For a public split quadratic

`Q=a(X-rY)(X-sY) (mod N^h)`,

the exact discriminant has the supplied unit root `a(r-s) mod N`.
An integral `SL_2(Z)` change of variables preserves that discriminant exactly.
Canonical coefficient reduction modulo `N` or `N^2` breaks the integer
identity by an exact public carry. Its positive discriminant lift is at most
`4N^(2h)` and remains a modular square with the same supplied root.

F266 tests the individual carries, their exact quotients, named singleton and
square-multiple templates, and the complete residual P66 square-class kernel.
It removes raw discriminant invariance, `+/-M`, stabilizers, swapped roots,
equal rows, exact squares, and rational square-class duplicates first.

The seam was reported to and approved by the root agent before file creation.

## Frozen files

| File | SHA-256 |
|---|---|
| `ALGEBRA.md` | `909e20c4e90a74266e99e80d120b21fbe16414dd7a88e144a936032ce3669c24` |
| `PREREGISTRATION.md` | `8e3704f68b59286c1b8ef82d5da5bd2ed9d579802b1c8b2e840fc06ae38816c7` |
| `search.cpp` | `820d0989c3816f091f6ab1931b02c3ebee445970bd107ae858dd3093f2df477d` |
| `remote_run.sh` | `a83ad64e3bb396b4899080f522d695e8773b105c814c402b51557993b17465cf` |

## Static checks completed

- `F266` was free before directory creation.
- `bash -n remote_run.sh` passed.
- No line has trailing whitespace.
- The source has fixed word, matrix, row, pair, refinement, prime-generation,
  certificate, thread, wall, memory, output, and compression caps.
- The only analysis entry point accepts public `N` and a public family. It
  accepts no factor. Hidden corpus factors label the returned exact divisor
  only after public analysis returns.
- Every row has a proved positive bound and a source check.
- Every P66 certificate verifies its exact product square and both normalized
  root gcds.
- Opaque gcd-free blocks are labelled `UNKNOWN_OPAQUE_NOT_NEEDED` by contract.
  No opaque-block prime factorization or Pollard-rho path exists.
- Discovery writes a canonical four-family selection. Heldout reads those
  bytes once, verifies SHA-256 internally, verifies the public discovery
  corpus SHA-256, and parses the authenticated bytes.
- The runner refuses any existing evidence path and any overlapping F258--F266
  validation or production process.

## Pending checks

This Mac does not provide the Boost.Multiprecision header used by the frozen
C++17 source. No substitute integer type or alternate implementation was
used. No executable mode has run.

Before compilation, the exact frozen packet needs a fresh hostile pre-run
audit. A passing audit must contain these exact lines:

```text
# Verdict: PASS
frozen_manifest_sha256: <SHA-256 of FROZEN.sha256>
```

After F258 releases the remote host, the unchanged packet must then:

1. authenticate `FROZEN.sha256` and the pinned hostile-audit digest line;
2. record target CPU, load, memory, disk, and active processes;
3. compile with `/usr/bin/g++ -O3 -DNDEBUG -std=c++17 -pthread`;
4. pass SHA-256, discriminant, projective-root, resultant, P66, exact-square,
   normalized-root, word-source, and selection-parser self-tests;
5. run the fixed one-worker 1/16 preflight under the shared caps;
6. require an eight-worker projected wall time at most 12,600 seconds, peak
   RSS at most 3.5 GiB, projected output at most 900 MiB, and zero resource
   rejections; and
7. only then run discovery and authenticated heldout sequentially.

Any failure stays attached to this version. Do not change and rerun it
silently.

## Interpretation

All future output is finite guidance. A positive certificate factors its
displayed modulus. A heldout null closes only the frozen grammar and corpus.
Neither result proves an all-input probability law or the top-level factoring
claim.
