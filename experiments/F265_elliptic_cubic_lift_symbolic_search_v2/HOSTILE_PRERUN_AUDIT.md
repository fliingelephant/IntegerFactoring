# F265-D02 hostile pre-run audit

## Verdict

**PASS.** The frozen F265-D02 packet is internally consistent and implements
the registered V2 repairs. This PASS authorizes only the exact frozen target
validation sequence after F258-D01 and every incompatible process have ended.
It does not authorize a corpus after a failed authentication, host, compile,
self-test, preflight, resource, selection, or output-set gate.

This was a static hostile audit. I did not compile or execute `search.cpp`,
invoke `remote_run.sh`, access the target host, generate an input, or inspect a
discovery, preflight, or held-out corpus.

## Frozen-chain authentication

The externally supplied SHA-256 of `FROZEN.sha256` is exact:

```text
PASS  FROZEN.sha256  26f7940244242edc549a2612fc08120372e0f8fab64a2dca154b69ed02d55d6a
```

Every entry authenticated from that root matches its live bytes:

```text
PASS  ALGEBRA.md             d20b5271bb4441fe7d280e35e09a73ff5b0142abf2ed6d3e9839fe22ff4914c4
PASS  PREREGISTRATION.md     8e3c90420014939ba3ae58490bac2e85fc0a7a45523e12d332cadb5e1f6b384f
PASS  search.cpp             eeceba4db014346cc78dae3cbae29a65fb32946163becc5d9f5617fc465a7957
PASS  remote_run.sh          7d2e214d4fda2b6cc9ca15c4c30c34962f9865b356451fd0aee0e0c23be525b7
PASS  VALIDATION_PENDING.md  a6d88c8c8422c0cd46d55a98d157c239e9b7150a07e83cc3e14bd8467f6f689a
PASS  AUDIT_REQUEST.md       d53747fa102ef27405a0ae629a94667de6cf4b9f700a0cecd3c2aee86ad89aee
PASS  PRELAUNCH_MANIFEST.md  d3d1a74f50ad54b8217e65f8a0492d277b407fe237190d3189d91a522130818a
```

The declared parent provenance is also exact. The immutable F265-D01
`FROZEN.sha256` hash is
`9de9af4b9da746b8732913cf1cc4495ffb4b612d556cfd5e0ca8d7089cdcbb13`,
all five of its entries still authenticate, and its unchanged FAIL audit hash
is `7219be54b5a82ff4c043f86562118a23578f369e9e5869a51f61dbe5e8e9a67b`.

## Exact algebra reconstruction

For each accepted public seed, the source sets

```text
B = (y0^2 - x0^3 - A*x0) mod N
delta = 4*A^3 + 27*B^2.
```

After the discriminant and affine-denominator exits, each admitted affine
point `(u_k,v_k)` gives the positive integer row

```text
a_k = u_k^3 + A*u_k + B
a_k - v_k^2 = carry_k*N.
```

Thus `a_k=v_k^2 mod N`, and the stored carry is an exact signed integer. The
source checks the congruence and divisibility before it stores the row. It
also enforces the 361-bit row bound and 384-row bank bound.

For a decoder vector `I`, the source forms the exact integer product

```text
A_I = product(a_i : i in I) = R_I^2
V_I = product(v_i : i in I) mod N.
```

Every admitted `v_i` is a unit. Hence
`z_I=R_I*V_I^(-1) mod N` satisfies `z_I^2=1 mod N`. The implementation
independently verifies the integer square, then classifies
`gcd(R_I-V_I,N)` and `gcd(R_I+V_I,N)`. On the frozen distinct-prime
semiprimes, a non-global root supplies a proper factor. No private factor is
part of this calculation.

The tangent/chord law is also exact:

```text
F(u)-F(w) = (u-w)*(u^2+u*w+w^2+A).
```

The direct chord screen, opaque-block refinement, and third-root tests use
this same expression. There is no algebraic sign or modulus drift.

## Source grammar and complete-bank rule

The twelve family rows in `search.cpp` exactly match the frozen IDs, modes,
schedules, multipliers, and domains. The scalar limit is
`min(multiplier*ceil(log2(N+1)),192)`; for the odd frozen moduli this is
exactly `min(multiplier*bitlen(N),192)`. The `ALL`, `ODD`, `PRIME`, and
`LOWHAM` schedules match the preregistration.

The `POWER` repair is exact. The source samples `s` uniformly from
`1,...,N-1`, computes `A=(s+1) mod N`, and does not rewrite zero. At
`s=N-1`, it therefore computes `A=0`. That boundary also gives `B=0`, so the
already-frozen universal `B=0` screen retries the curve. The source does not
replace this outcome by a different curve.

Each bank attempts exactly two curves. A proper discriminant, denominator,
signed-coordinate, or row-root gcd is a direct factor and stops the partial
orbit. A full discriminant gcd retries the public curve. A globally resolved
point at infinity follows the affine group law. A full row root, unresolved
global affine exception, or other incomplete orbit sets `BANK_SKIP`. A
registered cap sets `RESOURCE_REJECT`. The analyzer checks completion and
`curves.size()==2` before any direct controls or P66 decoding. It clears all
partial rows and cannot mark a partial bank eligible or strict.

The ordinary, safe-prime, case, curve, residue, row, block, split, total-row,
and pattern loops all have finite source-level caps. In particular,
`random_below` has exactly 4,096 rejection attempts and raises the registered
resource rejection on exhaustion.

## Direct controls and exact decoder

For a complete bank, the source executes the registered controls:

- singleton integer squares and both signed root gcds;
- every pairwise `x` difference and both signed `y` gcds;
- equal-row and same-curve inverse counters;
- exact square-multiple divisibility, integer-square, and signed-root tests;
- every same-curve chord-expression gcd with `N`; and
- tangent, chord, and discriminant support counters.

A direct factor remains attached to the bank. It suppresses every later
strict relation count.

The gcd-free decoder retains an exponent vector for each block. It iterates
until all final blocks are pairwise coprime, enforces the split and block caps,
and reconstructs every row exactly. It omits exact-square blocks from the
parity matrix. Each nonsquare pairwise-coprime block contributes its exact
exponent-parity equation. The source reduces the complete binary matrix,
constructs a basis for its kernel, and independently verifies every kernel
vector against every reduced equation before relation evaluation.

Every final block is copied into the output record with:

- its exact integer value;
- its exact sparse `row:exponent` vector;
- its independently recomputed exact-square bit; and
- the literal status `UNKNOWN_NOT_NEEDED`.

No primality assertion, hidden-prime basis, or Pollard--Rho path exists. The
block records are serialized even when the later exhaustive pattern cap makes
the bank a resource rejection.

## Chord and index-pattern miner

For every final block, the miner enumerates all incident same-curve row pairs.
It computes

```text
b_chord = gcd(b, u^2+u*w+w^2+A)
b_tan   = gcd(b, u-w)
b_disc  = gcd(b, delta).
```

For every pair with `b_chord>1`, it enumerates every other incident row on the
same curve and tests `u+w+t=0 mod b_chord`. Indices are canonicalized as
`i<=j`, and the source records exactly:

```text
i+j=k, j-i=k, 2i=j, 3i=j, i*j=k, v2(i)=v2(j).
```

Pair inspections and third-root tests share the exact 200,000-work cap. A
crossing makes the bank a resource rejection. The chord-pair, third-test,
third-match, and six index counters continue independently of the deterministic
64-witness serialization cap. Each retained witness includes its block and
support values, curve coefficients, discriminant, row IDs, scalar indices,
and coordinates. Thus every eligible bank exhausted the frozen pattern menu.

## Factor-label and discovery firewall

`Case` contains only `split`, `factor_bits`, `shape`, `index`, and `N`.
`FactorLabel` is a separate parallel store. Curve choice, orbit generation,
controls, decoding, counters, and worker closures receive public cases only.
The worker closure captures only the public cases, public jobs, result slots,
and an atomic cursor.

The pre-evaluation cohort writer ends at `N`. It cannot serialize `p` or `q`.
Evaluation proceeds in deterministic batches of at most 64 banks. Public
bank, block, and pattern outputs are written in job order. Only capped pending
relation certificates survive across batches. After every public batch has
joined and all public streams have closed, certificates can receive their
post-evaluation labels. The separate `labels.tsv` is written after
`run_cases` returns.

Discovery evaluates all twelve families. Selection uses the exact registered
cross-product comparison and remaining integer tie-break fields. The selection
bytes contain the version, discovery-cohort SHA-256, rank-field declaration,
the four IDs, and their rank values. The runner hashes those exact bytes before
heldout, verifies them immediately, and verifies them again after heldout.
Heldout reads only the four authenticated IDs. It has no discovery-certificate
input.

## Preflight and resource firewall

Preflight times corpus generation separately from analysis and output. It
reports generation, evaluation, and total wall/CPU time; peak RSS; rows; pair
controls; gcd-free splits; pattern work; the frozen generation and work
ratios; projected generation and evaluation time; projected output; and all
three decision gates. Its generation ratio accounts for both complete
production corpus constructions. Its planned work includes discovery over all
twelve families and a conservative four-family held-out envelope. A shortfall,
projection above 12,600 seconds, peak RSS above 3.5 GiB, or projected output
above 768 MiB rejects the packet before discovery.

The runner creates one common deadline before authentication and compilation,
then reserves five minutes for finalization. Authentication, compilation,
self-test, preflight, discovery, selection, heldout, and summary all use
`run_phase`, which applies the remaining common timeout and `nice 15`. The
shell and all children inherit the 4 GiB virtual-memory and 1 GiB per-file
limits. At most eight worker threads are accepted.

Before every phase, the runner checks incompatible processes, one-minute load,
available memory, available disk, and remaining time. After every phase, it
checks the aggregate binary, output, preflight, and log bytes against 1 GiB.
It refuses to overwrite a prior binary or any prior output directory. Exact
preflight, discovery, and complete output-set gates reject missing or extra
files. The exit trap preserves phase statuses, resource state, byte count, and
hashes on both success and failure.

## Selection, held-out labels, and scope

The family ranking and held-out decision code match the frozen integer rules.
A positive label requires at least two strict-hit banks across at least two
factor-size cells. A null requires zero strict banks, 90 percent aggregate
eligibility, and the per-cell 12-eligible gate. Every other result is mixed or
inconclusive.

The P20 case is confined to `self_test`. It reconstructs the displayed curve,
checks affine multiples through 101, verifies the two local gcds 101 and 103,
and checks the pooled zero. It does not enter source generation, selection, or
heldout.

This packet can produce finite exact factor certificates and finite pattern
evidence. It does not prove an all-input probability law, an asymptotic
success rate, or a complete factoring algorithm. Dynamic compilation,
self-test, and preflight evidence are still pending.
