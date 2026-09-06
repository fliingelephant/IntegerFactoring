# F260-D03 V3 prelaunch manifest

Status: **FROZEN STATIC NARROW REPAIR — VALIDATION AND HOSTILE AUDIT PENDING**

F260-D03 is a new sibling packet. F260-D01 and F260-D02 remain immutable and
failed. Their hostile audit SHA-256 values are
`9e49fb75f86b5ccdd7b3290053099cd822ab547a06495dbee82f64ff7a5e636d`
and
`281945088bf2b9d701c55c0cab6663ad8842daf80a6fe883129a4ea5b22d6a29`.

## D03 packet bytes

```text
f94ad4119a2bb6bb4e795da536a7bf29823b6e2d1c509c51e9b42e27a26d490f  ALGEBRA.md
b8cd3e88b77aa2dd84ca655436a8e2dbd1e68100f827c89eb0b64abb006aefcf  PREREGISTRATION.md
1359cd6cdec022e01c19d6b704cd6705fdee2cb3db190058386aa3c49debdebc  search.cpp
098b586bb237c821ec47919e6667ff0abe8ccf785e8fc703492636185a9e2699  remote_run.sh
05e1b77d6182350039a24f120e49231894d0367b2b246d65ee05458b9782fc3f  PROVENANCE.md
d2dc1ef9e96549304debb34c859b5c7f698e2a9c3b1e4d7a8f62d22353cbcd59  VALIDATION_PENDING.md
64b97371317aab2f15fb5a8e68153a6cb1df07652d62ef25676780abbc156bfd  STATIC_REVIEW.md
b7f9b7e1dc6a8329ac1cc1a6ce916452b84d4c310cc0a959d6757b1c6258aa4c  AUDIT_REQUEST.md
```

`FROZEN.sha256` is the machine-readable authentication boundary. It also
authenticates this manifest. A later hostile audit is not part of the frozen
repair bytes. The runner authenticates that audit through a one-record
sidecar, exact PASS text, and the SHA-256 of the exact `FROZEN.sha256` bytes.

## Narrow repair scope

D03 changes only normalized commutative syntax ordering, lexicographic
duplicate representatives, D03 packet/output labels, word residual-log
extrema, the 45-field aggregate checks, and the predecessor conflict gate.
It retains D02's score formulas, admitted grammar scope, seed, cohorts,
ranking orders, selector, lead gates, and resource limits.

## Qualification state

The packet received a static source and document review only. It was not
compiled, executed, self-tested, benchmarked, or transferred. No corpus or
cohort was generated or inspected. No durable ledger changed.

Do not start discovery or held-out directly. The only registered path is:

1. obtain the independent hostile audit requested in `AUDIT_REQUEST.md`;
2. transfer the exact frozen packet and authenticated audit artifacts;
3. invoke `remote_run.sh` in its registered target directory; and
4. let the runner authenticate, compile, self-test, benchmark, and enforce all
   resource and production gates.

Any change to a listed byte invalidates the audit request and requires a new
experiment freeze.
