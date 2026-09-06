# F279-D06 fresh hostile theory audit

## Verdict

**STRICT PASS.**

The authenticated D06 pair is a coherent additive repair of the
authenticated D01--D05 chain. It closes both D05 source blockers: the
benchmark is one literal, independently reconstructible contract, and the
four certificate counters have one cache-independent logical ownership
model. I found no mathematical, benchmark-byte, accounting, determinism,
command-line, descriptor, status, firewall, replay, resource, output, or
authority blocker.

This is a theory/interface-only PASS. It authorizes replacing the incomplete
portable evaluator draft with only the one standalone C++17 source:

```text
f279_public.cpp
```

It authorizes no runner or private-role source, containment choice, source
freeze, compilation, preprocessing, self-test, benchmark, validation,
fixture or tape creation, scientific execution, private-label access,
remote access, ledger change, git staging, or commit. A later complete
source packet still needs an immutable precompile freeze and hostile static
PASS. Every later build, validation step, and scientific run still needs its
applicable explicit authorization.

## Authenticated inputs and additive composition

I authenticated the D06 files before I read them.

```text
D06_DRAFT_ALGEBRA.md
e8df9b30b94b64ba1d9f5f885db19763c2db407d58cc58262637f402eb35f097

D06_DRAFT_PREREGISTRATION.md
3b3f69ec1351a5e2529aa12d7e30441ed1bb23b04240a0ca71cfc5f640f37299
```

I also authenticated the immediate D05 hostile PASS before reading it.

```text
D05_HOSTILE_THEORY_AUDIT.md
b22d63037d47c670c9535135d34847c7895afc432b181e8190ec3386f416a64a
```

Every imported draft and the inherited D03 hostile PASS matched its recorded
hash before I read the additive chain.

```text
D05_DRAFT_ALGEBRA.md
5e27479a5298b2ed6758bc81ba6f1aabaca107b97a624887aa7d420eef114763

D05_DRAFT_PREREGISTRATION.md
2d76c815fe752d1bc7f50caac788ab8943a8ec2a46377e7773677590a416cdb5

D04_DRAFT_ALGEBRA.md
3f801eb810f6019c5c54e2879c3d6f88d8ae2d99d7891e96da96e8b8c9718133

D04_DRAFT_PREREGISTRATION.md
2a21322b509a16a85162d8f16654e092f965c09b704179b2501f9b8153c59cf5

D03_DRAFT_ALGEBRA.md
d9f2fa7c490b96214e976478740257b0e6cc675f20bf7f7219760e4ca450e159

D03_DRAFT_PREREGISTRATION.md
6b5f1633e2cf2654adb8ec8bb2f79bf84a242550ef57cb4dc6cf964013413a1b

D03_HOSTILE_THEORY_AUDIT.md
859a170e6ca26d19f696559df1e7b570fc7f06a55240226fdf46cdf19e51e676

D02_DRAFT_ALGEBRA.md
f87f787bad0943b7149d276e158d28a6350dc8ab72836e80112acf33240cf843

D02_DRAFT_PREREGISTRATION.md
93e207fb2e3e4c489eb009f56e16751b3df79d7ecc329b602a678761795533f9

DRAFT_ALGEBRA.md
328c8c26d5c06e3033300539fd5900f7ddcb55f253b75fae851c58db47eea424

DRAFT_PREREGISTRATION.md
4498a4f3e2404297d6eda58036fc45e097915a13d73077dc9511dea4e6cb7e7e
```

I read the complete authenticated D01--D06 composition. I applied every
supersession narrowly and in order. I did not treat D06 as a standalone
replacement. I did not inspect `f279_public.cpp`.

## Literal benchmark reconstruction

The fixed arithmetic vector reconstructs exactly.

- Both `rho0` and `rho1` pass the inherited seven-base deterministic
  Miller--Rabin test. They are distinct 56-bit primes.
- `rho0*rho1=N0`, `isqrt(N0)=B0`, and the two square-root inequalities
  hold.
- Euclidean division by `x0` gives exactly `d0,r0`. The least positive
  inverse is exactly `u0`, and `(x0*u0-1)/N0=k0`.
- Every displayed atom, invariant, source-power, endpoint, control, and
  large-order gcd is one where D06 says it is one.
- Canonical pair powering reproduces `P0,Q0,F0` and `PG,QG` exactly. All
  32 orbit, 15 target-torsion, and 495 mixed-screen actual gcds are one.
- `R0=N0^2-1` has the displayed 32-byte big-endian encoding. The quotient
  `floor(2^256/N0^2)`, rejection bound `L0`, reduction `U0,V0,W0`, both
  control gcds, `F_uniform`, and its gcd all reconstruct exactly.
- The displayed `inv2`, `inv4`, four literal matrix entries, four powered
  matrix entries, and normalized right side reconstruct exactly.
- The two local residual powers reproduce the displayed ten signed feed
  values, including exponents `500008` and `-500012` and both zero equality
  bits.
- `F161,F162` are consecutive and coprime, both are below `2^112`, and
  their successor is not below `2^112`. The fixed surrogate is therefore
  the declared largest consecutive worst-case Euclidean pair.

The six serializer templates also reconstruct byte-for-byte.

```text
record          fields  bytes  sha256
R_endpoint           8    157  bb011cf26654ebdf59ed90d770ea6a306e9e88edb9023c6a4c5f9508d287f9b9
R_control           12    182  a87e69e0ecd6b6c4c8b1ff36ad9212dafa1f0aae50bd22a152c0df56af79e2ca
R_scan               7    106  c010dc158dd962b1c72bfe9fab1f863cd72b78bf53d438fb35770281c0feac54
R_certificate       41   1250  859d89a35ebe484a12542fd29b76e563da70283eed8e78499ba1c98a1aefd560
R_label             12    126  0c2bc7c953e25f4c88e9545c03dcb3408f28273a5554bea7ee49005faee24711
R_diagnostic        27    590  94670d6c313a08cbea3a7a6ae68ac909afc36b5a1a2bc6833d2f6c6c2737f3a0
```

The inherited headers plus 4,096 separately serialized copies give these
exact preimages.

```text
stream       bytes    sha256
endpoint      643145  5a4be2abe995b7f7fb9cc35dbe3b1774445eea7fc7d014f313554c36565a52bb
control       745569  70cb3b4008af755192441d6ea78740adf61a8bc1d3742d416e0ae6137359cddd
scan          434221  903196bd252c60208fedfbea3c14822955c8c1bb4bdfa798a8243d46894754e6
diagnostic   2416857  d7e38f17f2aeddf5cb55ad248f4703705df0f7e76f4799884e435cccecf35ffe
```

I independently applied the stated modulo-`2^64` feed recurrence to every
declared feed in all 14 kernels and all seven trials. All 98 resulting sink
words match the D06 table. This includes the two invariant-gcd result feeds
at the start of `source_power`, all 1,084 registered-decoy residue/gcd feeds
per iteration, the four final digest words of each streaming kernel, and the
combined candidate, decoy, matrix, and digest feeds of `diagnostic_target`.

The I/O bytes are also closed.

```text
object                    bytes      sha256
one generated block       1048576    d53ee020a0d5a374096215c86c5f8e68f5e5961223607170bc47c29a935a96f3
64-copy payload           67108864   20af2a434b08c78344d2e54c9d3a608752e4ac856d0d86dd0c6a400a5013f735
benchmark checksum input      4712   b8b4aabf6307c1898ea3767f97ecb07cf0b815ecdb38173446c450edce4f63f9
```

The 4,712-byte checksum input has the exact header, 98 kernel records, then
three write and three read records. Its digest is the only successful
benchmark status checksum.

## Timing, cleanup, and noncircularity

- Every arithmetic operand, record preimage, hash preimage, payload byte,
  sink seed, sink feed, and expected checksum exists before compilation.
  None depends on a clock, address, environment value, UID, file content,
  fixture, tape, compiler result, or prior trial.
- Setup verification is outside each timing boundary. Kernel timing starts
  before sink or SHA-context initialization and ends after the final sink
  update. The seven-trial maximum and checked ceiling division are total.
- I/O timing has one exact 64 MiB payload. Write timing includes exclusive
  create, all writes, `fsync`, close, reopen, full hash verification, and
  close. Read timing includes open, full read and hash verification, and
  close.
- Successful cleanup is total: verified write files from trials 0 and 1 are
  unlinked outside timing; the verified trial-2 file is retained for all
  read trials; it is unlinked after read trial 2; final `fstatat` must report
  `ENOENT`. A preexisting name is never removed.
- Failure classes remain disjoint. Existing bytes are `output_exists`;
  valid bytes over the file cap are `output_cap`; OS I/O and hash failures
  are `output_io`; inability to remove a fully verified temporary file is
  `benchmark`; and no failure emits PASS.
- ABI-dependent `capacity_touched_bytes` is not a compile prerequisite. The
  source fixes the production regions and checked size formula. Exact build
  and postcompile attestation later bind the ABI and binary that produce the
  value. This preserves the D04 precompile/build/postcompile ordering.

There is no compile/run cycle. Static source bytes and the build recipe are
audited before compilation. Binary hashes, capacity bytes, elapsed times,
and the concrete containment manifest arise only afterward and are bound by
postcompile validation. No scientific mode is unlocked by compilation or
benchmark success alone.

## Primitive and certificate accounting

The primitive rules are complete and implementation-independent.

- A pair product owns one `pair_mul` and exactly five ordered modular
  products. A matrix product owns one `matrix_mul` and exactly eight ordered
  modular products.
- A displayed two-argument gcd owns one gcd. The control expression
  `gcd(V,W,N)` owns two. An inverse owns one inverse and no hidden gcds.
- Binary power has no unused final square. For positive `e`, both pair and
  scalar power own `popcount(e)+floor(log2(e))` products. Negative pair
  power adds only the inherited sign change.
- Named source powers 2 through 16 own 15 pair products. A raw proper target
  owns 15 target-cache products and 240 source-cache extensions through
  power 256. Each saturated mixed relation owns its own binary power at
  `m*(B-e)`. Equal values, sources, and exponents do not merge logical
  owners.

For one certificate, let `k` be its number of saturated mixed mask bits and
let `L_j=m_j*(B-e_j)` in registered order. Its counters are uniquely:

```text
global_order_checks = k

pair_muls
  = 15 + pow_pair_muls(B) + 15 + 240
    + sum_j pow_pair_muls(L_j)

mod_muls = 5*pair_muls + 1025
gcds     = 563 + k
```

The `1025` non-pair products are one source square, one target square, one
endpoint product, 32 orbit products, and 990 mixed-determinant products.
The `563` base gcds are 19 source gcds, `g_H,g_F`, and the 542 complete-box
gcds. Every large mixed-order check adds one further gcd. The complete box
runs after the first direct relation, so direct and global certificates use
the same identities and retain every saturation.

The isolated certificate view deliberately repeats its named-source cost.
It excludes row cleanup, controls, diagnostics, serializers, labels, and
literal matrix replay. It is therefore independently reconstructible and
is not falsely presented as a partition of the phase summary.

## Phase ownership, caches, controls, diagnostics, and aborts

The phase summary has one stable logical owner tree.

- Row cleanup owns only its reached displayed operations.
- Each of the 900 named source IDs owns its reached invariant, small-power,
  `B`-power, `g_Q`, and `g_P` work once. Numerically equal source IDs remain
  separate logical owners.
- Each reached ranked candidate owns `g_H`, then its endpoint when clean,
  then the lazy complete box only for a raw proper endpoint. `no_hit`,
  `saturated_hit`, and source- or target-ineligible slots own no lazy cache.
- Controls reuse the named source pair. A modulo rejection owns no gcd or
  modular product. Every nonmodulo attempt owns the two vector gcds, three
  target-invariant modular products, and its target gcd. An acceptance also
  owns two endpoint modular products and one endpoint gcd. Uninspected
  attempts own nothing.
- A diagnostic base record owns one gcd. A positive-exponent scan record
  additionally owns one incremental modular product and one gcd. A retained
  diagnostic source owns its source construction and source work once for
  all 90 targets. Each target then follows the ranked target and lazy-box
  rules without borrowing a ranked certificate counter.
- Every primary raw ranked certificate and raw diagnostic target owns the
  literal matrix check in the phase view. With
  `h=pow_pair_muls(B)`, it adds one inverse, `h` matrix products, and
  `5+8*h+pow_mod_muls(B)` modular products. It reuses the candidate's
  already charged `v^2`.

The D05 raw-hit event remains ranked-only. Its gate is after `g_F` and
before all lazy work. The global-order event covers both ranked and
diagnostic saturated mixed relations. Its atomic gate is before exponent
construction and before every pair, modular-product, or gcd charge. No
control owns either event.

On success, phase `global_order_checks` is exactly the sum of all ranked
certificate `k` values plus all diagnostic-target large checks. Discovery
starts both packet counters at zero. Held-out imports the authenticated
discovery totals. Both remain cumulative and bounded by 131,072.

Source and target terminal events create no endpoint or certificate. A cap,
control-shortfall, arithmetic, resource, replay, serialization, or output
abort creates no successful summary or certificate with accounting
authority. Partial roots are nonevidence. Four-worker execution charges by
immutable owner keys and uses the inherited stable merge. Cache hits,
thread schedules, and physical call counts cannot change logical evidence.

Both public replay phases rebuild the same primary owner tree and compare
the sealed phase counts. They report their physical replay totals through
the inherited replay interface but do not add replay work to the primary
phase summary. Label replay does not enter the four public certificate
fields.

## Replacement, interface, firewall, and resources

- D06 changes only the two declared seams. Endpoint signs, residual signs,
  source and candidate states, finite `K=16` relation box, ExactTape256 law,
  evidence class, cap scopes, and nonclaims remain closed.
- Every future artifact prefix and JSON version is `F279-D06`. No stale
  operational D01--D05 basename or version survives the mechanical
  replacement.
- The six D05 command lines, fixed argv order, exact descriptor sets,
  descriptor types and access directions, status-pipe grammar, exit mapping,
  and failure precedence remain mutually closed. Benchmark mode receives
  only descriptors `2,9,10`.
- `rho0,rho1` and the residual values are public synthetic benchmark
  constants. They are not fixture labels. Scientific modes receive no
  benchmark operand path, private fixture, cohort, local character, factor,
  prime generator, or Legendre-symbol path.
- Held-out and replay-heldout still authenticate discovery manifest and
  summary on descriptors 11 and 12. Selection supplies no counter. Both
  public replay PASS records and the same discovery-manifest hash remain
  prerequisites to private-label access.
- D06 adds no evidence file and no record field. Every stress record remains
  below its inherited cap. The successful-output arithmetic remains exactly
  `281186304` bytes; the 25-percent projection remains `351482880`; and the
  hard aggregate cap remains `536870912` bytes.
- The inherited tape-read, artifact-read, wall, memory, disk, lock, process,
  and live-host gates remain unchanged. The benchmark temporary file is
  outside every evidence root and is below the inherited per-file cap.
- The fixed kernel counts still include primary work plus the one exhaustive
  public replay where specified. Splitting replay across two invocations
  does not duplicate a projected workload.

The probability claim remains conditional only on the product of local
control-success events `A_ctrl`. D06 makes no probability claim conditional
on runtime completion, a cap, a checksum, replay, or packet success.

## Audit boundary

I did not inspect or edit `f279_public.cpp`. I did not compile or execute the
evaluator. I did not access a fixture, tape, private label, remote host, or
ledger. I did not edit a released draft, stage a file, or create a commit.
