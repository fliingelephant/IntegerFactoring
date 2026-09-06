# F279-D06 additive benchmark and accounting repair

## Status, ancestry, and exact scope

F279-D06 is an unfrozen theory/interface amendment. It authorizes no source
edit, runner, fixture, tape, source freeze, compilation, preprocessing,
self-test, benchmark, validation run, scientific run, private-label access,
remote access, ledger edit, staging, or commit.

Its authenticated immediate inputs are:

```text
D05_DRAFT_ALGEBRA.md
5e27479a5298b2ed6758bc81ba6f1aabaca107b97a624887aa7d420eef114763

D05_DRAFT_PREREGISTRATION.md
2d76c815fe752d1bc7f50caac788ab8943a8ec2a46377e7773677590a416cdb5

D05_HOSTILE_THEORY_AUDIT.md
b22d63037d47c670c9535135d34847c7895afc432b181e8190ec3386f416a64a
```

Read D06 additively with the complete authenticated D01--D05 chain. D06
repairs exactly two source blockers:

1. it replaces the underdetermined D02/D03 benchmark operands, record
   preimages, I/O payload, timing boundaries, and checksum with the literal
   contract below; and
2. it replaces implementation-dependent certificate operation counts with
   the logical ownership model in `D06_DRAFT_ALGEBRA.md` and Section 8.

All D05 modes, argv, descriptor sets, basenames, status schemas, error
tokens, precedence, packet caps, public/private role partition, manifests,
seals, replay chronology, output bounds, probability conditioning, and
unresolved deployment inputs remain unchanged. Mechanical artifact prefixes
and JSON versions advance to `F279-D06`.

The existing incomplete `f279_public.cpp` is not authenticated input. This
pair neither changes nor approves it.

## 1. One literal benchmark vector

The D02 phrase `112-bit odd moduli` is superseded by this one vector. The
decimal constants are exact:

```text
rho0 = 72057594036927911
rho1 = 72057594037927931
N0   = 5192296858462767872764747260382141 = rho0*rho1
B0   = 72057594037427920 = floor(sqrt(N0))

x0 = 72057594037427920
d0 = 72057594037427921
r0 = 72057344027427821
u0 = 4509779229051360486714317898580055
k0 = 62585759201298139

t0   = x0
eta0 = d0
v0   = r0
```

`rho0` and `rho1` are distinct 56-bit primes. Benchmark setup verifies each
with the inherited seven deterministic Miller--Rabin bases and verifies all
displayed products, divisions, inverse identities, gcds, and square-root
inequalities. In particular:

```text
gcd(x0,N0)=gcd(d0,N0)=gcd(r0,N0)=gcd(u0,N0)=gcd(k0,N0)=1
gcd(eta0,N0)=1
gcd(t0^2-eta0,N0)=1
gcd(v0^2-eta0,N0)=1
```

The registered names attached to this vector are exactly:

```text
source_id    s4-t00-e02
candidate_id s4-t00-e02-d4-v04
```

They denote anchor zero with `t=+x`, `eta=+d`, and `v=+r`. The benchmark
does not score these names and does not create scientific evidence.

The fixed source and matrix exponent and the fixed large-order exponent are:

```text
E0 = 72057594037927935 = 2^56-1
EG = 1152921504606847216 = 16*(2^56-1+16).
```

The fixed consecutive Fibonacci gcd operands are the largest consecutive
pair both below `2^112`:

```text
F161 = 1983924214061919432247806074196061
F162 = 3210056809456107725247980776292056
gcd(F161,F162)=1.
```

Benchmark setup computes the inherited gcd operands and verifies their
expected outcomes. Inside a timed kernel, however, every logical gcd slot
executes exactly `gcd(F162,F161)` and uses its result `1`. This is the one
fixed worst-case Euclidean surrogate for all timed gcd slots. A nested
`gcd(V,W,N)` therefore executes the surrogate twice. No kernel adds a bonus
gcd or times a data-dependent easier operand.

No kernel selects an operand from a clock, address, compiler, file content,
environment value, UID, random source, fixture, tape descriptor, or prior
trial.

### 1.1 Fixed source, endpoint, control, order, and matrix results

Using the inherited pair law modulo `N0`, benchmark setup must reproduce:

```text
(t0+w)^E0
P0 = 546235288075814104597900157766191
Q0 = 2050355986842150267503452025035379
gcd(P0,N0)=1
gcd(Q0,N0)=1

F0 = P0-v0*Q0 mod N0
   = 289765957888600935550152132631336
gcd(F0,N0)=1

gcd(Q_m(t0,eta0),N0)=1 for every m=2,...,16.
Every actual gcd in the 32 orbit, 15 target-torsion, and 495 mixed
registered screens is also one.
```

The one synthetic ExactTape256 block is:

```text
R0 = N0^2-1
   = 26959946666402328507693636050555806496420540967009894165513351743880

32-byte big-endian hex
00000000ffffffffe17b440000e8d8d131fdfff6e790c4ed340016bd0ea04988
```

The benchmark control reduction must reproduce:

```text
M0 = N0^2
   = 26959946666402328507693636050555806496420540967009894165513351743881

floor(2^256/M0)=4294967296

L0 = 4294967296*M0
   = 115792089234102222918792651224463791525030564515935710349301056791313463115776

U0=R0
V0=N0-1=5192296858462767872764747260382140
W0=N0-1=5192296858462767872764747260382140
g_vector=1
g_target=1

F_uniform=1504120698766336162905551867269188
gcd(F_uniform,N0)=1.
```

The large-order kernel must reproduce:

```text
(t0+w)^EG
PG = 3440831553615722869918064737449083
QG = 462075355879171003448010482325851
gcd(QG,N0)=1.
```

For the literal matrix at exponent `E0`, setup must reproduce:

```text
inv2 = 2596148429231383936382373630191071
inv4 = 3894222643847075904573560445286606

C00 = 2596148429231383936382498635191120
C01 = 1
C10 = 3894231651390995924107362428537111
C11 = 2596148429231384008439842662618941

(C^E0)00 = 4662747449486028399575507469426950
(C^E0)01 = 3368742099563065922611141661159379
(C^E0)10 = 242639670993409867463953164383354
(C^E0)11 = 3459505105645858071340362456319990

2^(-E0)*F0 mod N0 = 4662747449486028399575507469426950.
```

The two public synthetic residual operands are `rho0,rho1`; they are not
fixture factors and no scientific mode can access them. Here

```text
B0-rho0 = 500009
rho1-B0 = 500011
chi_rho0=chi_rho1=-1.
```

The label-residual benchmark feeds this exact signed result list:

```text
500008
66745776074730768
23744879761430206
25449488386170113
0
-500012
56645214409475462
12025180446520232
35468277657070566
0
```

Each five-field block is signed exponent, canonical pair `P,Q`, residual
endpoint, and equality bit. Benchmark-only constants add no `p`, `q`,
Legendre-symbol, trial-division, or label path to a scientific mode.

## 2. Exact maximum-width serialization templates

Define these benchmark-only ASCII constructors:

```text
TSV(f1,...,fk) = f1 || TAB || ... || TAB || fk || LF
U               = "5192296858462767872764747260382140"
H               = 64 lowercase "f" bytes
MASK            = 138 lowercase "f" bytes followed by "fe"
U64             = "18446744073709551615"
```

`repeat(X,n)` below splices `n` copies of field `X`; it emits no brackets,
commas, or spaces. These records are serializer stress vectors. Their field
grammar is canonical, but they are not candidate evidence and no cross-field
mathematical claim is made for them.

```text
R_endpoint = TSV(
  "discovery","d1023","s8-t09-e09-d8-v09","raw_proper_hit",
  U,U,"registered_global_powered_collision","-")

R_control = TSV(
  "discovery","d1023","s8-t09-e09","1","2","accept",
  U,U,"1","1",U,U)

R_scan = TSV(
  "discovery","d1023","12656","112",U,U,"saturated")

R_certificate = TSV(
  "d1023-s8-t09-e09-d8-v09","discovery","d1023","128",
  "s8-t09-e09-d8-v09","5192296858462767872764747260382141",
  "72057594037427920","-4","-4",
  repeat(U,5),repeat(U,5),repeat(U,14),MASK,"mx-16-16","131072",
  U64,U64,U64,"direct_registered_mixed_phase",
  "direct_registered_mixed_phase:mx-16-16")

R_label = TSV(
  "d1023-s8-t09-e09-d8-v09","d1023","72057594036927911",
  "72057594037927931","four_capacity_at_most_32",
  "72057594037927931","-1","-1","1","1","1","pass")

R_diagnostic = TSV(
  "discovery","d1023","5192296858462767872764747260382141",
  "72057594037427920","112","12656","retained","12656","112","-",
  U,"12655","1417360",H,"d8-v09","raw_proper_hit",
  repeat(U,9),"direct_registered_mixed_phase","mx-16-16")
```

The required field counts, byte lengths including LF, and SHA-256 hashes
are:

```text
record          fields  bytes  sha256
R_endpoint           8    157  bb011cf26654ebdf59ed90d770ea6a306e9e88edb9023c6a4c5f9508d287f9b9
R_control           12    182  a87e69e0ecd6b6c4c8b1ff36ad9212dafa1f0aae50bd22a152c0df56af79e2ca
R_scan               7    106  c010dc158dd962b1c72bfe9fab1f863cd72b78bf53d438fb35770281c0feac54
R_certificate       41   1250  859d89a35ebe484a12542fd29b76e563da70283eed8e78499ba1c98a1aefd560
R_label             12    126  0c2bc7c953e25f4c88e9545c03dcb3408f28273a5554bea7ee49005faee24711
R_diagnostic        27    590  94670d6c313a08cbea3a7a6ae68ac909afc36b5a1a2bc6833d2f6c6c2737f3a0
```

Each template remains below its inherited per-record cap. Benchmark setup
constructs and verifies all six byte strings before timing begins. A future
source cannot substitute an implementation-chosen record.

### 2.1 Exact streaming-hash preimages

The endpoint, control, scan, and diagnostic headers are the exact inherited
headers. For each hash benchmark trial, the preimage is its header followed
by exactly 4,096 copies of the named record:

```text
stream       record         preimage bytes  expected sha256
endpoint     R_endpoint             643145  5a4be2abe995b7f7fb9cc35dbe3b1774445eea7fc7d014f313554c36565a52bb
control      R_control              745569  70cb3b4008af755192441d6ea78740adf61a8bc1d3742d416e0ae6137359cddd
scan         R_scan                 434221  903196bd252c60208fedfbea3c14822955c8c1bb4bdfa798a8243d46894754e6
diagnostic   R_diagnostic          2416857  d7e38f17f2aeddf5cb55ad248f4703705df0f7e76f4799884e435cccecf35ffe
```

One context is initialized per trial. The header is one update. Every
record is separately serialized and supplied by one update. Finalization is
inside the timing boundary.

## 3. Exact fourteen benchmark kernels

The inherited kernel key order and projected counts remain:

```text
source_power          3686400
candidate_endpoint  102400000
control_attempt       22118400
control_endpoint       7372800
registered_decoy        262144
global_order             262144
matrix_replay            262144
label_residual           131072
certificate_serialize    131072
label_serialize          131072
endpoint_stream_hash  102400000
control_stream_hash    22118400
diagnostic_scan        91520960
diagnostic_target          5760
```

Each kernel runs seven trials of exactly 4,096 iterations. Each trial starts
from the Section 1 constants; no state crosses a trial. The timed work and
sink-feed order are:

1. `source_power`: compute `g_eta,g_delta`; construct source powers 2
   through 16 by recurrence and feed `(Q_m,gcd(Q_m,N0))` in numeric `m`
   order; binary-power `E0`; feed `P0,Q0,g_Q,g_P`.
2. `candidate_endpoint`: using setup `P0,Q0`, compute and feed
   `H4,g_H,F0,g_F,score_increment`.
3. `control_attempt`: decode `R0`, compute rejection bound and both target
   tests, and feed `R0,L0,U0,V0,W0,g_vector,target_residue,g_target,1`.
4. `control_endpoint`: compute and feed `F_uniform,g_F_uniform`.
5. `registered_decoy`: rebuild the power recurrences and execute all 32
   orbit, 15 target-torsion, and 495 mixed screens. Feed each
   `(canonical_residue,gcd)` in inherited chronology. It never runs a large
   order check.
6. `global_order`: binary-power `EG` and feed `EG,PG,QG,gcd(QG,N0)`.
7. `matrix_replay`: construct `inv2` and `inv4`, construct the literal
   matrix, binary-power it at `E0`, independently scalar-power `inv2` at
   `E0`, multiply that scale by `F0`, and feed `C00,C01,C10,C11`, the four
   powered entries in row-major order, `F0`, the computed normalized right
   side, and the equality bit.
8. `label_residual`: execute the two division-free synthetic residual
   powers and feed the ten signed values at the end of Section 1.1.
9. `certificate_serialize`: construct `R_certificate` anew and feed its
   byte length, first eight bytes, eight bytes starting at
   `floor(length/2)`, and last eight bytes, interpreting each byte group as
   unsigned big-endian.
10. `label_serialize`: apply the same four feeds to a newly constructed
    `R_label`.
11. `endpoint_stream_hash`: implement the endpoint preimage in Section 2.1
    and, after finalization, feed its four digest words in unsigned
    big-endian order.
12. `control_stream_hash`: do the same for the control preimage.
13. `diagnostic_scan`: in every iteration compute
    `(N0-1)^2 mod N0`, subtract one canonically, execute the fixed gcd
    surrogate in place of that logical gcd slot, serialize and update one
    `R_scan`; feed the modular power, the subtracted value, and surrogate
    result `1`.
    After the loop, feed the four scan digest words.
14. `diagnostic_target`: execute the candidate endpoint, the complete
    `registered_decoy` work, and `matrix_replay`; serialize and update one
    `R_diagnostic` per iteration; feed the candidate list, every registered
    `(residue,gcd)`, and the matrix list in the orders above. After the loop,
    feed the four diagnostic digest words.

Every displayed kernel gcd uses the fixed surrogate in Section 1. There is
no additional gcd feed: its result occupies the corresponding displayed gcd
field. Benchmark setup has already checked that every actual vector gcd
whose result is fed as a screen value is also one.

All setup constants, expected values, record templates, and the 1 MiB I/O
block are constructed and checked outside every timing boundary. The work
listed above, result formatting, record buffer copies, SHA updates, and sink
updates are inside. No trial is a warm-up and no result is discarded.

## 4. Volatile sink and fixed benchmark checksum

All sink arithmetic is unsigned modulo `2^64`. For kernel index `j=0,...,13`
in Section 3 order and trial `r=0,...,6`, initialize:

```text
S = 0xF279D0605A17C0DE xor (j<<32) xor r.
```

For every iteration `i=0,...,4095`, first feed `i`, then the kernel fields
in Section 3 order. Feeding signed or unsigned integer `x` means:

```text
u = x mod 2^64
S = ((S xor u)*0x9e3779b185ebca87
     + 0xd1b54a32d192ed03) mod 2^64.
```

`S` is a `volatile uint64_t`, and every displayed assignment is executed.
Digest and byte-group feeds use their unsigned big-endian 64-bit values.

The required final sinks, as exactly 16 lowercase hexadecimal digits, are:

```text
kernel                 trial0            trial1            trial2            trial3            trial4            trial5            trial6
source_power           d7a762e7447d80de  8258bbf2dac660df  d3c2322b208960dc  447922f6ff6e20dd  908196f7d82f00da  4129c3da3f2420db  9a23084904e0e0d8
candidate_endpoint     44896867d53760de  a7e9af323a9aa0df  4deec398b2d2c0dc  16565142f12380dd  b2f692fa9f1980da  90a6f509347aa0db  45d9216ece1a40d8
control_attempt        b824bb2354a280de  dbfa19768e3960df  e83c678f431e60dc  fa6d2c5557c660dd  83bc26a98c7a80da  0c60a5d8d2f7a0db  fdb00fa9c3cc20d8
control_endpoint       b14c95122085a0de  9659cf402a8600df  3b0646c64f4620dc  4d16ba74242f20dd  07cfc26f810a20da  de6616afa7b7a0db  1dfda66561e9c0d8
registered_decoy       fdd7a55df31ba0de  42362c07a997c0df  1c340f5179cb60dc  570b8a24a2fa00dd  96fa79efba57c0da  d407dac346b840db  2755d51ff09160d8
global_order           ac0bcbf0597420de  c585e5bccbc060df  e59e6d0831d440dc  dd5225ab0a1a40dd  49b5f926540600da  ce646d81fdcf60db  4a889cd5008bc0d8
matrix_replay          67d20b9b9c0400de  a9a2ddd951d500df  ab8409cc377aa0dc  a9b1b6fc2224c0dd  b2af13293f81c0da  5762909c5c99e0db  e59bfc0b7cf140d8
label_residual         729d8f6fefdde0de  2b43643a22d280df  717e12fbb186a0dc  a96021980bb8e0dd  44a6da51f79900da  4c2692e07b82e0db  7675ebb625c3a0d8
certificate_serialize c6f5f5ba2db160de  ee1922554d4660df  efd75eaa39b680dc  c0cadb96c7ec20dd  85188affbb8de0da  68493d18ebba80db  63e7dd1c97c900d8
label_serialize       c4a2caf2274c00de  ea703f4def2540df  24487bfeaeee20dc  82e8c0b4a27140dd  439adba1cf0100da  48e77e38f58a60db  b8d7cda24919c0d8
endpoint_stream_hash  b293c235438872f5  dd285a794260d674  b48ee6735c657d57  d4c6330c76983a56  625926175549c031  6a84f0be941c9550  1745f75fb0abce13
control_stream_hash   215f01d5b39ce65e  2f55c584a034cd5f  fdc8a0317756debc  a70ceb9a1a8f7e3d  5dd4b31392a9c1fa  4953889b97ea271b  ab20352424830658
diagnostic_scan       019b8e6869581799  c814b90235911ad8  26b3d7affcca207b  b5301901d35ba37a  cc4ed5a8e7587b7d  0a5b410cdcb94a1c  13dd9790faa8545f
diagnostic_target     34f5da163c6f3385  eb2b76c7178bc814  aa149aee1c7c1267  140405c14876bef6  d3f219b654114ce1  7925474340acb650  1f760129eee423c3
```

A sink mismatch is not a timing sample. It aborts benchmark mode.

The benchmark checksum preimage has exact header:

```text
kind	name	trial	value
```

It then has 98 `kernel` records in kernel order and trial order. Each is:

```text
kernel<TAB><kernel-name><TAB><trial><TAB><16-hex-sink><LF>
```

It next has three `write` and three `read` records, in that order, with
trial `0,1,2` and the payload hash from Section 6:

```text
write<TAB>payload<TAB><trial><TAB><payload-sha256><LF>
read<TAB>payload<TAB><trial><TAB><payload-sha256><LF>
```

The complete checksum preimage is exactly 4,712 bytes and has SHA-256:

```text
b8b4aabf6307c1898ea3767f97ecb07cf0b815ecdb38173446c450edce4f63f9
```

That literal is the only successful benchmark status `checksum` value.
Elapsed times and capacity bytes do not enter this digest.

## 5. Timing conversion

Each kernel trial uses `std::chrono::steady_clock`. Benchmark setup requires
`steady_clock::is_steady=true`. Timing starts immediately before trial-sink
initialization or, for a streaming kernel, before SHA-context
initialization. Timing ends immediately after the final sink update. Let
`elapsed_ns` be

```text
duration_cast<nanoseconds>(end-start).count().
```

It must be a positive representable unsigned 64-bit integer. For each
kernel, the status value is:

```text
kernel_ns[k] = max over seven trials of ceil(elapsed_ns/4096)
             = max ((elapsed_ns+4095)/4096),
```

with checked addition. Kernel setup, expected-value checks, and the
capacity allocation are outside these boundaries. Thread creation is
forbidden in benchmark mode.

The D04 benchmark PASS key order remains exact. `kernel_counts` uses the
Section 3 projected counts. `kernel_ns` uses the same key order and canonical
unsigned decimal values. No timing result changes a workload or checksum.

## 6. Exact 64 MiB I/O payload and trials

The only temporary basename advances mechanically to:

```text
.F279-D06.benchmark.io.tmp
```

Before any benchmark timing, require that this basename does not exist below
descriptor 9. Before exclusive creation, apply the inherited per-file
`RLIMIT_FSIZE` check to exactly 67,108,864 valid payload bytes; failure is
D05 `output_cap`. Construct one 1,048,576-byte memory block. For block index
`i=0,...,32767`, append:

```text
SHA256(ASCII "F279-D06-benchmark-io" || NUL || uint64_be(i)).
```

The block hash must be:

```text
d53ee020a0d5a374096215c86c5f8e68f5e5961223607170bc47c29a935a96f3
```

The 67,108,864-byte payload is exactly 64 consecutive copies of that block.
Its expected SHA-256 is:

```text
20af2a434b08c78344d2e54c9d3a608752e4ac856d0d86dd0c6a400a5013f735
```

There is no zero-fill, sparse-file operation, `mmap`, compression, random
payload, filesystem clone, `fallocate`, or substitute generator.

Run three write trials. For each trial, timing starts immediately before
`openat(9,name,O_CREAT|O_EXCL|O_WRONLY,0600)`. Write the 64 blocks in order
with the inherited positive-partial and `EINTR` rules, call `fsync`, close,
reopen read-only, hash exactly 67,108,864 bytes with a 1 MiB buffer, verify
size, EOF, and the expected digest, close, then stop timing. After trials 0
and 1, unlink the verified file outside timing. Leave the verified trial-2
file for the read trials.

Run three read trials on that file. Timing starts immediately before the
read-only `openat`, includes full read and SHA-256 verification and close,
and ends immediately after close. After read trial 2 succeeds, unlink the
file outside timing. Success requires that a final `fstatat` reports
`ENOENT`.

Define:

```text
write_ns_per_byte = max ceil(write_trial_ns/67108864)
read_ns_per_byte  = max ceil(read_trial_ns/67108864).
```

The expected digest from each of all six trials enters the checksum preimage
in Section 4. A preexisting basename is D05 `output_exists`. A create,
write, `fsync`, close, reopen, read, stat, EOF, or file-hash failure is D05
`output_io`. Failure to remove a fully verified temporary file is D05
`benchmark`. No failed benchmark emits PASS.

## 7. Capacity and benchmark status

The inherited D03 capacity exercise remains production-typed. A future
source must declare one fixed list of capacity regions in source order,
checked-multiply every element count by `sizeof(production_type)`, allocate
the exact maximum capacities, and initialize every element to a valid
maximum-width production state. Trivially copyable byte buffers are written
at every byte; nontrivial objects are touched only through valid field
assignments. It reports

```text
capacity_touched_bytes
```

as the checked sum of `count*sizeof(production_type)` plus every explicitly
owned dynamic backing span, not object addresses, allocator metadata, RSS,
virtual-memory peak, rounded pages, or an estimate.
This value can differ across bound C++17 ABIs; the postcompile attestation
binds the binary that produced it. The future source audit must verify that
the declared regions are exactly the four row buffers, 25,000-candidate
score table, fixed queues, replay state, 1 MiB I/O buffer, diagnostic row
buffer, three SHA contexts, manifest tables, and expanded operation counters
required by D02/D03. No optional or fallback capacity set exists.

The exact successful status remains the D05/D04 schema:

```text
version,role,mode,phase,kernel_counts,kernel_ns,read_ns_per_byte,
write_ns_per_byte,capacity_touched_bytes,checksum,status
```

with `version="F279-D06"`, `role="f279_public"`, `mode="benchmark"`,
`phase=null`, the fixed checksum in Section 4, and `status="pass"`.

Checked allocation overflow or allocation failure is `memory_cap`. A
serializer that cannot produce a Section 2 template is `serialization`.
An embedded-vector identity, primality, expected arithmetic result, payload
construction, clock, elapsed-time, sink, or final checksum mismatch is
`benchmark`. D05 failure precedence otherwise remains unchanged.

## 8. Executable counter ownership

The logical primitive definitions and certificate formulas in
`D06_DRAFT_ALGEBRA.md` are normative. A source implements two counter views:

1. a phase-owner accumulator for the D03 summary; and
2. a fresh isolated-certificate accumulator for each raw ranked endpoint.

The phase view charges row cleanup, each named source once, each reached
ranked candidate, each inspected control attempt, diagnostics, and canonical
serialization/SHA work. It never derives a count from wall time or from the
number of C++ calls after caching. Equal named IDs remain separately
charged. A numerical cache stores values only; its hit or miss does not
alter logical charges.

The certificate view starts at zero and deterministically charges one clean
source replay, one clean target endpoint, the complete lazy box, and its own
large mixed-order checks. It must satisfy before serialization:

```text
global_order_checks = number of saturated mixed mask bits for that candidate
gcds               = 563+global_order_checks
mod_muls           = 5*pair_muls+1025
```

`pair_muls` is the exact D06 power formula, including one separate binary
power for every saturated mixed relation. Failure of any equality is
`internal`, because the classification has not yet been serialized.

The packet-wide D05 global counter is an event counter, not a derived
primitive count. Immediately before each permitted large check, its atomic
reservation follows D05. Only after that reservation does the owning
candidate or diagnostic charge exponentiation, pair, modular-product, and
gcd primitives. The successful phase `global_order_checks` equals ranked
certificate global checks plus diagnostic-target global checks. Replay
reconstructs both terms. No control owns a global check.

The raw-hit packet counter remains ranked-only. Its permitted increment
occurs after endpoint gcd and before the candidate's lazy-box accumulator.
Source-direct, target-direct, saturated endpoints, controls, and diagnostic
targets do not increment it.

Controls allocate their charges to `(row_id,source_id,control_index,attempt)`.
The nested vector gcd charges two. A modulo rejection owns only tape decode
and comparisons. A target rejection owns both vector gcds and the target
gcd. An acceptance additionally owns two endpoint mod-products and one
endpoint gcd. A shortfall has no successful controls JSON or summary.

Diagnostics allocate scan charges by `(row_id,base,exponent)` and target
charges by `(row_id,target_id)`. A retained diagnostic source owns its
source work once across 90 targets. Diagnostic target records do not borrow
or modify ranked certificate counters.

Endpoint, control, and diagnostic checksum records allocate their exact
serialization and SHA bytes to the phase summary only. They allocate no
pair, modular multiplication, or gcd to a certificate. Matrix replay and
label residual work likewise never enter the four public certificate
fields. Each primary raw ranked certificate and primary raw diagnostic
target nevertheless performs the D06 literal matrix check and allocates its
inverse, matrix, scalar-power, and modular-product charges to the phase
summary exactly as specified in D06 algebra Section 4.

Public replay rebuilds the same primary owner tree and compares every
counter. It reports its inherited replay counts but does not add its own
physical operations to the sealed primary summary. No failed or partial
record has counter authority. These rules preserve D05 abort-before-next-
record semantics under four-worker execution.

## 9. Preserved boundary and next authority

D06 changes no scientific outcome definition. In particular, it preserves:

1. the explicit `D^{-1}CD` chart and endpoint signs;
2. total source and candidate status serialization;
3. authenticated promises, input manifests, containment anchor, and carry
   inputs;
4. the ExactTape256 sample space and control-local probability condition;
5. the complete finite decoy box and bounded claims;
6. high-order diagnostic evidence and replay;
7. phase close, manifest, seal, label, replay, and reveal chronology;
8. the exact six-mode D05 CLI, descriptor, status, and failure contracts;
9. four-worker no-fork scientific execution; and
10. every inherited wall, memory, output, raw-hit, and global-order cap.

Numeric UIDs, network denial, namespaces, cgroups, RLIMIT deployment,
process groups, locks, the runner, and the private role remain unresolved
deployment work requiring separate user authorization.

This exact D06 pair must be released unchanged for a fresh no-context
hostile theory audit. Its authors do not audit it and do not grant it a
PASS. Only a fresh strict PASS may authorize replacing the incomplete public
evaluator draft. It still cannot authorize runner or private-role source,
source freeze, compile, execution, private data, remote work, staging, or
commit.
