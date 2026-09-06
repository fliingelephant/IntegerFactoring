# F281-D01 fresh hostile pre-run audit

Verdict: **FAIL — NOT CLEARED FOR LAUNCH**

FROZEN_SHA256=ff3717ce237bac9f69ab6aff118a8bdb48b9c967c8af85e8590170f865755bea

## Authentication and scope

Audit root:
`/Users/zhou/autoresearch/IntegerFactoring/experiments/F281_central_stirling_joint_saturation`

The SHA-256 of the exact `FROZEN.sha256` bytes is
`ff3717ce237bac9f69ab6aff118a8bdb48b9c967c8af85e8590170f865755bea`.
Every record in that authenticated manifest matches its listed file:

| Frozen entry | SHA-256 | Result |
|---|---|---|
| `ALGEBRA.md` | `77ec1762b5afdaa5cc7a3f15dfe5b5249d423595b31fefdf88697a4614707557` | authenticated |
| `PREREGISTRATION.md` | `5be742e5e6a05f0566f4cd4944252c5bdfc0589539a79f5d01a0eb9ff15eccda` | authenticated |
| `PROVENANCE.md` | `46ad8be1c1a26eca5d3f9cb7a3702ff069158307ef15a5454bbdca416a3f455f` | authenticated |
| `search.cpp` | `b3f9df35d576124e875d67b0a38d6ba42786bc0cb9610f2a4ffba3fb60877c8c` | authenticated |
| `remote_run.sh` | `e15cc08767105f1bf97d5433ca8bf02e1552278243b89ca9a492d71ff4ecbd96` | authenticated |
| `VALIDATION_PENDING.md` | `1444c84d2ac7123ff0da1b1bad0474120cf158813f2f4c01b2190d4bd37bb12a` | authenticated |
| `AUDIT_REQUEST.md` | `9d77c1a2a88197319d8d6f68c9c1b126dd788adabc64fb8e839f8ee8190557a7` | authenticated |
| `PRELAUNCH_MANIFEST.md` | `5e87afdb90b490230fb468a659f5adb75480cc6f8048a1e683eeaf0cacb9c13c` | authenticated |

I read the complete authenticated packet. I did not compile or preprocess the
source. I did not execute or syntax-run the runner. I did not run a self-test,
pilot, replay, search, or remote command. I did not create a cohort. I did not
edit a frozen byte or a ledger. This report provides static evidence only.

## Decisive launch blockers

### 1. The related-process admission gate misses this experiment

`remote_run.sh:163-166` searches process arguments only for versions
`F258-D` through `F280-D`. It does not search for `F281-D01`. A second
F281-D01 packet can therefore pass `refuse_overlap` while the first F281-D01
scientific process is active, provided the coarse load and memory thresholds
also pass. The argument-pattern test can also miss a related binary whose
path or arguments do not contain one of those uppercase version fragments.

This violates the mandatory active-related-process admission check. It also
invalidates the claim that every expensive phase excludes overlapping related
production.

Minimal first-principles repair: acquire one atomic, host-scoped experiment
lock before target creation. Also inspect `/proc` structurally by executable
identity and packet identity. Exclude only this runner and its owned direct
child. Do not use a finite historical-version regex as process identity.

### 2. The dependency gate does not authenticate the dependency set used

`remote_run.sh:93-108` gates `flint` and the GMP C package. It does not gate
the required GMP C++ package. `remote_run.sh:343-345` then ignores GMP's
pkg-config compile and link flags and uses ambient `-lgmpxx -lgmp` lookup.
Consequently:

- a host can pass the precompile gate without GMP C++ headers or `libgmpxx`,
  and discover that missing dependency only during compilation; and
- a non-default GMP selected by pkg-config need not be the GMP found by the
  compiler and linker.

This contradicts the frozen requirements that missing dependencies stop
before compilation and that compilation has no substitute dependency or host
path.

Minimal first-principles repair: gate FLINT, GMP, and GMP C++ as explicit
pkg-config identities. Consume and record the compile and link flags for all
three identities. Fail before target creation if any required identity is
absent. Refreeze the exact dependency contract if a target distribution does
not provide a GMP C++ pkg-config identity.

### 3. The frozen closing and replay reserves are not hard reserves

`PREREGISTRATION.md:175` requires 600 seconds for closing checks and
manifests. The runner instead sets `MANIFEST_RESERVE_SECONDS=300` at
`remote_run.sh:28`, and all live phase deadlines preserve only that 300-second
value. The selection inequality at `remote_run.sh:632` contains an additional
600 seconds, but it is not a runtime reserve: production may run beyond its
projection up to the larger cap at `remote_run.sh:658-663`. A subsequent
replay can then run until only 300 seconds remain.

The runner also reserves 1,800 seconds once, although production can emit two
witnesses, one from each lane, and `remote_run.sh:693-704` requires two serial
replays. The second replay has no frozen worst-case reserve.

The outer timeout still prevents a late PASS. Thus this defect fails closed,
but it does not implement the registered schedule and can turn an otherwise
valid two-witness production into a resource failure.

Minimal first-principles repair: make 600 seconds the reserve used by every
deadline calculation. Before production, reserve that closing interval plus
the maximum registered number of replay intervals. Alternatively, freeze a
rule that closes after one independently validated counterexample and never
requires a second replay.

### 4. Output validation does not implement the promised fail-closed schema

`validate_lane_output` at `remote_run.sh:444-468` checks selected summary
columns and the witness line count. It does not check the exact complete
summary header. It does not check the headers or field counts of
`checkpoints.tsv` or `telemetry.tsv`. It does not check the contents of
`DONE`. `production_output_set` also ignores unexpected non-file entries.
These artifacts can therefore be malformed and still move from staging to a
final directory. This contradicts `PREREGISTRATION.md:279-281`, which says
that missing headers and extra output are rejected.

The final 512 MiB cap is also checked before `resource_final.txt` is written
at `remote_run.sh:706-709`, and the EXIT trap writes the final manifest after
that last check. The asserted aggregate live cap is therefore not closed over
the final artifact set.

Minimal first-principles repair: validate every fixed file against one exact
header, exact field count, exact row-count rule, and exact `DONE` record before
moving it. Reject every unexpected filesystem entry type. Reserve bounded
space for all closing artifacts before the last cap check, and verify the
complete final set without permitting an over-cap success.

Any one of these four defects is sufficient for FAIL. They require a source
packet change and a complete refreeze. There is no safe audit-only repair.

## Mathematics audit

The mathematical seam is correct.

- From
  `sum_(n>=k) S(n,k)t^(n-k)=product_(j=1)^k (1-jt)^(-1)`, coefficient
  extraction gives `S(n,k)=h_(n-k)(1,...,k)`.
- Thus `A_s=h_(s+1)(1,...,s)` and
  `B_s=h_(s+2)(1,...,s-1)`. The last-variable recurrence gives
  `h_(s+2)(1,...,s)=B_s+sA_s`. The two displayed joint-zero formulations are
  therefore equivalent over every field.
- For `p=2s+1+2h`, put `r=p-s-1=s+2h`. Since
  `product_(a=1)^(p-1)(1-at)=1-t^(p-1)`, degrees below `p-1` give
  `h_d(1,...,s)=e_d(1,...,r)` modulo `p`. In
  `product_(j=1)^r(x+j)=sum_k c(r+1,k+1)x^k`, the target degrees `s+1,s+2`
  are the polynomial degrees `2h-1,2h-2`. They are exactly
  `c(s+2h+1,2h)` and `c(s+2h+1,2h-1)`. Keeping the leading factor `x` shifts
  the polynomial-degree labels by one but does not change those literal
  `c(n,k)` indices. The signs are positive.
- With `m=s-1` and `n=2m+3`, the standard forward-difference expansion gives
  `P_m(0)=m!B_s` and `P_m(1)-P_m(0)=(m+1)!A_s`. Substitution
  `j -> m-j` gives `P_m(-m-x)=(-1)^(m+1)P_m(x)`. For primes above `2s+1`,
  the scaling factorials are units, so the scaled and unscaled joint
  divisibility tests are equivalent.
- The norm identity follows by pairing the nonzero residues into their
  squares and complementing `1,...,s` inside `1,...,(p-1)/2`. It does not
  identify coefficients at degrees `s+1,s+2` with degrees `2h-2,2h-1`.
- At `s=3,p=43,h=18`, `A=S(7,3)=301=0` and `B=S(7,2)=63=20` modulo 43.
  Using `S(n,3)=(3^n-3*2^n+3)/6` gives
  `h_34(1,2,3)=S(37,3)=13` and
  `h_35(1,2,3)=S(38,3)=36` modulo 43. This refutes the discarded target.
- The fixed divisor divides the scaled two-entry gcd because its defining
  tail contains both endpoint terms. It also divides `n!`, so it has no prime
  support above `n`. At `s=73`, the defining exact tail-gcd calculation gives
  `G/Delta=1679=23*73`; it does not divide `146=2*73`.

No fixed-divisor, norm, or Eulerian-gamma observation is promoted to a proof.
The packet correctly calls every completed finite search evidence rather than
a proof.

## Scientific source audit

No mathematical acceptance blocker was found in `search.cpp`.

- Lane A performs the exact descending second-kind update through
  `k=min(n,S_A)`. Higher columns never feed lower columns, so truncation loses
  no registered value. Odd rows `n=2s+1` cover each `1<=s<=S_A` once.
- The prime sieve is complete through `2S_A+1`. `mpz_remove` removes each
  prime at most the row bound to exhaustion. A nonunit residual is checked for
  divisibility into both exact values and for gcd one with the exact support
  lcm. Composite replay uses the original inclusion-exclusion formula. Its
  two factorials are invertible because every prime factor of the residual is
  above `2s+1`.
- Lane B maintains one exact first-kind row through degree `2H`. The map
  `(s,h) -> n=s+2h+1` and the inverse `s=n-2h-1` cover the registered rectangle
  once in increasing `n`, then increasing `h`. The tested entries are the two
  literal coefficients from the algebra. Each distinct word candidate is
  cached after one deterministic FLINT call. Joint zeros receive an original
  second-kind inclusion-exclusion replay.
- Both lanes bound witness output and stop after their first witness. The
  telemetry fixed-divisor calculation runs only when the stored row is
  complete. It cannot change status. The `s=73` false divisibility boolean is
  mandatory in the self-test.
- All twelve registered self-test records are present: the two small rows,
  homogeneous identity, last-variable recurrence, complement, norm,
  endpoints and reflection, discarded-target negative control, both F277
  individual saturations, noncentral adjacent positive control, fixed-divisor
  refutation, and synthetic `13^2` residual detector.
- Pilot tuples and all six production rungs match the preregistration. Worker
  inputs are restricted to one or two, with a hard rejection above eight.
  The two-thread path owns disjoint lane results and output directories. The
  scientific source contains no fork, exec, shell, subprocess, random, or
  probable-prime path.
- The modular addition, subtraction, factorial, and unsigned descending-loop
  logic is exact on every registered range. GMP in-place operations are used
  in permitted aliasing forms. Serialized source schemas have matching field
  counts. Exceptions prevent `DONE` closure.

## Runner properties that did survive static audit

- Frozen-input and hostile-audit authentication occurs before target
  creation. Existing targets and the explicitly broad targets are refused.
- The scientific launch uses a subshell followed by direct `exec`; its PID is
  the binary PID. The watchdog signals that PID directly, then waits. No
  pipeline or `timeout` process is inserted between the runner and scientific
  process.
- The scientific process receives exact soft and hard 4 GiB `RLIMIT_AS`, core
  zero, and the registered bounded file, descriptor, and process limits. The
  source reads them back before allocating large rows. One process with
  internal threads makes `RLIMIT_AS` an aggregate address-space limit. The
  packet does not misstate it as RSS or swap accounting.
- Optional cgroup-v2 values are classified conservatively: absent, `max`, or
  larger limits do not become a claim of cgroup containment.
- The six pilot tuples, work and limb proxies, 2.5 multiplier, rung arrays,
  highest-rung selection, and one-versus-two-worker memory aggregation match
  the frozen formulas. The same binary and lane kernels serve pilots and
  production. Rung values are not interpolated.
- Ordinary scientific failures leave staging data and a non-PASS runner
  manifest. Witness status requires independent replay. A finite null is
  labeled `FINITE_NULL_EVIDENCE`, not proof, and prior `s<=3000` provenance is
  never imported as packet output.

These surviving properties do not cure the decisive runner blockers above.
