# F281-D01 prelaunch manifest

Status: **STATIC FROZEN; FRESH HOSTILE AUDIT AND TARGET VALIDATION PENDING**

## Identity

- Experiment: `F281-D01`
- Question: large-prime joint saturation of the central second-kind Stirling
  pair
- Local packet root:
  `experiments/F281_central_stirling_joint_saturation`
- Search result at freeze: none
- Proof status at freeze: open

## Frozen inputs before this manifest

| File | SHA-256 |
|---|---|
| `ALGEBRA.md` | `77ec1762b5afdaa5cc7a3f15dfe5b5249d423595b31fefdf88697a4614707557` |
| `PREREGISTRATION.md` | `5be742e5e6a05f0566f4cd4944252c5bdfc0589539a79f5d01a0eb9ff15eccda` |
| `PROVENANCE.md` | `46ad8be1c1a26eca5d3f9cb7a3702ff069158307ef15a5454bbdca416a3f455f` |
| `search.cpp` | `b3f9df35d576124e875d67b0a38d6ba42786bc0cb9610f2a4ffba3fb60877c8c` |
| `remote_run.sh` | `e15cc08767105f1bf97d5433ca8bf02e1552278243b89ca9a492d71ff4ecbd96` |
| `VALIDATION_PENDING.md` | `1444c84d2ac7123ff0da1b1bad0474120cf158813f2f4c01b2190d4bd37bb12a` |
| `AUDIT_REQUEST.md` | `9d77c1a2a88197319d8d6f68c9c1b126dd788adabc64fb8e839f8ee8190557a7` |

`FROZEN.sha256` is the machine-readable authentication boundary. It also
authenticates this manifest. The requested hostile audit is a post-freeze
artifact and is not listed in `FROZEN.sha256`.

## Frozen theory seam

For `p=2s+1+2h>2s+1`, the exact target is

```text
p | S(2s+1,s), S(2s+1,s-1)
```

and its exact first-kind complement is

```text
c(s+2h+1,2h) = c(s+2h+1,2h-1) = 0 mod p.
```

The proposed replacement by complete homogeneous degrees `2h-2,2h-1` is
false. It is preserved only as a negative self-test. No proof, counterexample,
or prefix-to-tail fixed-divisor theorem is claimed.

## Frozen execution boundary

The packet has two exact lanes:

- all-`s` GMP second-kind recurrence with exhaustive small-prime stripping;
  and
- deterministic near-offset GMP first-kind recurrence with FLINT primality
  and independent second-kind replay.

The only production targets are the six rungs in `PREREGISTRATION.md`. The
same binary must first complete six geometric one-worker pilots. A measured
2.5-times projection chooses the highest safe rung. Failure of rung 0 stops
production.

Production is one scientific PID. One or two internal threads run the two
independent lanes. Soft and hard `RLIMIT_AS` bind their aggregate address
space to 4 GiB. This is not represented as a swap or RSS theorem. The runner
also enforces the four-hour packet deadline, fixed output caps, resource
snapshots, deterministic staging, witness replay, and final byte hashes.

The dependency boundary is exact C++17, GMP/GMPXX, and FLINT on a 64-bit
`unsigned long` target. A missing FLINT or GMP gate stops. No fallback is
registered.

## Qualification state

No F281-D01 byte was compiled or executed before freeze. No local pilot,
remote pilot, self-test, cohort, benchmark, or replay ran. The packet was not
transferred, and no `ssh seetacloud` command was issued for it. The existing
`s<=3000` observation is prior provenance only.

The next allowed action is the exact fresh static audit in
`AUDIT_REQUEST.md`. Any frozen-byte change invalidates that request and
requires a new version or complete refreeze.
