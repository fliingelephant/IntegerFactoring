# F264-D02 V2 frozen prelaunch manifest

Frozen on 2026-08-14 before the first successful V2 compile or any V2
execution.

## Status

**DO NOT LAUNCH pending fresh hostile pre-run audit.**

F264-D02 is an immutable repair packet. It is not promoted. The local Mac has
no Boost Multiprecision header. The target had an active incompatible F258-D01
process at preparation time. Therefore V2 has no successful compile,
self-test, benchmark, cohort, or score result. `V2_FAILED_LOCAL_COMPILE.md`
preserves the environment failure and target resource observation.

## Frozen V2 core hashes

```text
894ca1338c5cc7ce74e8bf60dbf987f2566928bdbe2a9e6d6542d02d969e98a5  V2_ALGEBRA.md
973727b78b07c7f9a455cb002b010c4f423ebeae9d6f4c3788d053aa7cad6d46  V2_PREREGISTRATION.md
bf47d8d973433c645489ca5ce094b32eee7afa1f352b31e814354b0b42f8718d  V2_symbolic_search.cpp
696219d0615bbb6f7a4da2bad1db8bf2aad699271ace25f63264de7c9d218e3b  V2_remote_run.sh
9bdd657ab552353de158dc60b8e25688ccaf0101e28a4b3eb66a48469dc4d2a4  V2_FAILED_LOCAL_COMPILE.md
9b6c7042ea0c7698c39a7654aac772e6a36c299153842625ba6b83030f90c852  V2_VALIDATION_PENDING.md
9bb70a1b0829f31187370a01b0c12dee18f31798af3eeb0f032904f8848336a6  V2_AUDIT_REQUEST.md
b1e2665027f874f42e3d29c95693ac636ef8c439fce37e4a29e42bba16360c97  V2_STATIC_VALIDATION.md
```

`V2_FROZEN.sha256` authenticates these files and this manifest. The manifest
cannot list its own final hash without a cycle.

## V1 immutable provenance

Every V1 byte and its FAIL audit remains unchanged:

```text
d15b020f26d5daaff1debfb57b765c5305264466f5882cae451acc62b513d52f  ALGEBRA.md
200926250aeb1a7a9839f8a50e0fdc6c8ab211254ad61aed229bacc6048f650b  PREREGISTRATION.md
5fb4e172b9edb441e211b276e13ccabc810f657d9f44fcc8f728a3e157f73c0e  symbolic_search.cpp
1fdaa2648797731b87d04a229003c05ad467bea14bb64efcc494fc4ce69adb0c  remote_run.sh
507ecd4c5c56d44867b0f34ca9262b7df5bb4d6450cd8121791d4912cb39e522  PRELAUNCH_MANIFEST.md
23d7aa6bd72f9cb7cf66b63ea9680fbd3adabcd4b543150929b249d8b0a2bb22  FROZEN.sha256
f00fee9eac5fb71c9403d0f3a39b8cbf0bb0eb5682d6776f5eca1d26e21e3c9c  HOSTILE_PRERUN_AUDIT.md
```

## Repair map

V2 addresses every V1 hostile finding without interpreting finite evidence as
proof:

- discards the all-zero ternary vector and freezes five unique controls;
- expands the associator into its exact six ordered scalar summands;
- emits all three projected minor pairs among `K,C_parent,C_word`;
- evaluates all seven root forms in the original and conjugate bases;
- removes the false primitive-gcd invariant and retains units in sums and
  products;
- replaces incomplete random refill with bounded, factor-blind full-scope rank
  permutations;
- adds bounded exhaustion gates to every generator and scope search;
- preserves ten separately named global-zero counts and five separately typed
  original/conjugate coordinate-and-carry transcript pairs;
- records exact certified lcms, exact P205 residual gcds and improvement
  multipliers, integer residual losses, complete cell summaries, and literal
  finite-lead predicates;
- verifies that both public generator profiles are noncommuting;
- opens discovery and held-out in separate monitored processes and enforces the
  firewall, 4 GiB memory cap, one shared four-hour deadline, 1 GiB owned-byte
  cap, resource checks, and report dimensions at every stage.

Static checks completed before freeze: `bash -n V2_remote_run.sh`,
`git diff --check` on every V2 artifact, hash authentication of V1, and manual
source/spec comparison. `V2_STATIC_VALIDATION.md` preserves independent exact
checks of the combinatorial unranking formulas and all five nullspace ranks and
ternary relations. Dynamic C++ validation remains mandatory and unopened.

No durable ledger was edited.
