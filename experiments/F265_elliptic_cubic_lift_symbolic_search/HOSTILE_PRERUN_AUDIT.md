# F265-D01 hostile pre-run audit

## Verdict

**FAIL. Do not compile, self-test, preflight, or launch either cohort from this
frozen packet.**

The central cubic-row identity and factor-free square-class decoder are
mathematically sound. The executable is not the complete preregistered
experiment. It changes one frozen source family, mishandles a registered
full-row-root branch, omits mandatory chord/index mining and opaque-block
reporting, serializes hidden factors before public analysis, and does not
implement the registered preflight and complete-packet resource gates.

This was a static hostile audit. I did not compile or execute `search.cpp`,
invoke `remote_run.sh`, access the target host, generate a corpus, or inspect a
discovery or held-out cohort. `F258-D01` can continue without interference.

## Frozen-artifact authentication

All five entries in `FROZEN.sha256` match the local bytes.

```text
PASS  ALGEBRA.md             be4a2d5b74656a0a34ee11da7972d92c78123386258e20eb28c726179fac42ca
PASS  PREREGISTRATION.md     f24e878f5d2080faa1a297969e638f4f15b1adba7c993c731861fc1408f1361b
PASS  search.cpp             96ba06af46e274836975c7e79f2bd2a5096e83c0ea4b35e770b12a701ac4a835
PASS  remote_run.sh          35465d726b42b52d07c821c9d26cac0e2cdd4647ed1c7fdf2060f1a9d0312f65
PASS  PRELAUNCH_MANIFEST.md  3cd2437da71bda44e07cb4a28f2e5a322e2e15b0d1ee7f94a960c411e8624a9f
```

The observed SHA-256 of `FROZEN.sha256` is
`9de9af4b9da746b8732913cf1cc4495ffb4b612d556cfd5e0ca8d7089cdcbb13`.

## Exact algebra reconstruction

For each public seed, the source sets

```text
B = (y0^2 - x0^3 - A*x0) mod N
delta = 4*A^3 + 27*B^2.
```

After the discriminant and affine-denominator exits, an admitted affine point
`(u_k,v_k)` gives the positive integer row

```text
a_k = u_k^3 + A*u_k + B,
a_k - v_k^2 = c_k*N.
```

Thus `a_k = v_k^2 (mod N)`. The row-root screen makes every admitted `v_k`
a unit. For a binary decoder relation `I`, the source forms

```text
A_I = product(a_i : i in I) = R_I^2 over the integers,
V_I = product(v_i : i in I) mod N,
z_I = R_I * V_I^(-1) mod N.
```

It follows that `z_I^2=1 mod N`. The implementation verifies the exact
integer square and computes `gcd(R_I-V_I,N)` and `gcd(R_I+V_I,N)`. On the
frozen distinct-prime semiprimes, `z_I` is either global `+1`, global `-1`, or
the two signed gcds expose the hidden factors. The production classification
in `search.cpp:708-741` implements this law correctly.

The tangent/chord identity is also correct:

```text
F(u)-F(w) = (u-w)*(u^2+u*w+w^2+A).
```

The source uses this identity for pair counters and coarse relation labels.
It does not implement the complete registered support miner, as described
below.

## Decisive blockers

### 1. The `POWER` family is not the frozen family

The preregistration defines `A=s+1 mod N` for every uniform nonzero `s`
(`PREREGISTRATION.md:58-59`). For `s=N-1`, the frozen value is `A=0`.
The source instead replaces that value by `A=1`
(`search.cpp:436-441`). This changes families 8 and 9 on a legitimate source
outcome. The general algebra permits `A=0`; only the `U` mode requires a
nonzero `A`.

This is a source-distribution change, not a harmless rejection or a direct
factor screen.

### 2. A full row-root is not skipped as registered

The algebra says that `gcd(v_k,N)=N` makes the current row inadmissible and
that the row is skipped. The source instead returns from the whole curve at
`search.cpp:488-496`. `analyze_bank` then breaks its two-curve construction
and can decode any earlier rows because this branch is neither `direct` nor
`resource_reject` (`search.cpp:744-755`).

Consequences:

- the sequential orbit is truncated instead of skipping the row;
- the second frozen curve might never be attempted;
- a partial one-curve bank can be called eligible; and
- a relation in that partial bank can be counted as strict.

This conflicts with both “each family uses two curves” and the declared
full-row-root behavior. Proper row-root gcds correctly stop the bank as direct
factors. The `gcd=N` branch is different and needs an explicit frozen policy.

### 3. Mandatory chord-block and index-pattern mining is absent

The freeze requires every chord-supported block to test a third incident
coordinate for `u+v+w=0 mod block` and to record the six frozen index patterns
(`PREREGISTRATION.md:172-176`). No such test, third-coordinate search, binary
valuation test, or index-formula output exists in `search.cpp`.

`relation_label` only computes pairwise

```text
shared = gcd(a_i,a_j),
gcd(shared,u_i-u_j),
gcd(shared,u_i^2+u_i*u_j+u_j^2+A),
gcd(shared,delta)
```

and reduces the result to one string label (`search.cpp:671-705`). The bank
counters at `search.cpp:792-800` have the same pairwise scope. They do not
identify the supporting opaque block or execute the frozen third-root and
index menu. Therefore the packet cannot answer its preregistered symbolic
pattern question.

### 4. Opaque-block reporting is missing

The internal gcd-free refinement does retain exact exponent vectors, checks
final pairwise coprimality, reconstructs every row, builds exact parity
equations, verifies the reduced binary kernel, and calls an exact integer
square test (`search.cpp:548-662`). Treating one pairwise-coprime nonsquare
opaque base as one parity equation is valid: an odd power of that base is
nonsquare and an even power is square. No Pollard--Rho or primality inference
appears in the decoder.

However, the freeze also requires every opaque block to be reported as
`UNKNOWN_NOT_NEEDED` (`PREREGISTRATION.md:145-147`; `ALGEBRA.md:265-268`).
That string does not occur in the executable. No block value, exponent vector,
square/nonsquare status, or factorization-status field is written to the bank,
metric, or certificate output. The internal `Decoder::blocks` are discarded
after `analyze_bank`. The advertised block-level authentication therefore
cannot be reconstructed from an output certificate.

### 5. Hidden factors are serialized before public computation

The freeze says `p` and `q` are used only to construct `N` and to label a
final certificate after all public computation is complete
(`PREREGISTRATION.md:28-30`). `write_cohort` writes both hidden factors
(`search.cpp:1027-1035`), and `main` calls it before `run_cases`
(`search.cpp:1366-1379`).

Static inspection confirms that `choose_curve`, orbit generation, controls,
and decoding do not read `Case::p` or `Case::q`; the arithmetic itself is
factor-free. Nevertheless, the frozen timing and output firewall are false as
written. The factors exist in a public output file before the analysis starts,
not only in final verification certificates.

### 6. The preregistered preflight report and projection are not implemented

The freeze requires the scaled preflight to report wall time, CPU time, peak
RSS, rows, pair controls, gcd-free splits, and projected complete runtime
(`PREREGISTRATION.md:241-245`). `RunOutput` contains only wall seconds and
peak RSS. The preflight JSON reports only those measurements plus a modeled
work ratio (`search.cpp:1298-1319`). Rows and pair counts exist only in side
tables. CPU time and gcd-free split counts are never retained or emitted.

The projection also times only `run_cases`. It excludes deterministic cohort
generation, including bounded safe-prime searches, because `make_corpus` runs
later inside discovery and heldout. It also excludes cohort serialization,
selection, held-out summary construction, and final manifests. Thus the
12,600-second gate is not a measurement-based projection of the registered
complete packet.

### 7. The complete runner is not under the frozen resource envelope

The 4 GiB virtual-memory and output-file limits apply to preflight, discovery,
and heldout only (`remote_run.sh:84-89,102-111,135-145`). Compilation,
self-test, selection, and summarization run outside those limits
(`remote_run.sh:38-42,120-124,151-156`). Compilation has no timeout. The
deadline is checked before the three large phases, but compilation can itself
run past it, and summarization can run after the held-out timeout has consumed
the remaining budget.

The runner records load, memory, disk, and active processes, but it has no
availability threshold that rejects an unsafe launch. Its aggregate 1 GiB
check occurs only after all output has already been written and excludes the
log directory (`remote_run.sh:162-173`). These facts do not satisfy the frozen
claim that the complete packet uses the four-hour, 4 GiB, and 1 GiB envelope.

### 8. Residue sampling has an unbounded retry loop

Prime requests, case retries, curve attempts, and gcd-free splitting have the
declared finite caps. `random_below`, however, uses an unconditional
`for (;;)` rejection loop (`search.cpp:219-227`). Every curve family calls it.
The loop is expected to terminate quickly, but the source-level resource
contract is not deterministic and bounded on this path.

## Controls that are implemented correctly

Subject to the blockers above, the following static paths match the intended
mathematics:

- proper discriminant gcds are direct, full discriminant gcds retry, and seed
  exhaustion is a resource rejection (`search.cpp:458-472`);
- affine addition checks every proposed denominator before inversion, exposes
  mixed CRT signs at equal `x`, and handles a global inverse or a doubled
  `y=0` point as infinity (`search.cpp:305-341`); there is no projective branch;
- admitted rows check the 361-bit cap, row congruence, carry divisibility, row
  count, and proper row-root gcd (`search.cpp:475-520`);
- singleton integer squares use both signed gcds
  (`search.cpp:757-763`);
- every admitted pair receives `x`-difference and both signed-`y` gcds
  (`search.cpp:764-771`);
- equal rows and same-curve inverse rows are identified, while their signed
  root gcds are already covered by the pair controls
  (`search.cpp:772-775`);
- every exact square-multiple pair verifies integer divisibility and an exact
  square multiplier, then tests both normalized-root signs
  (`search.cpp:776-789`);
- every same-curve pair tests the public chord expression against `N`, and
  pairwise tangent/chord/discriminant support counters are exact
  (`search.cpp:792-800`);
- a proper result from any direct control suppresses all later strict relation
  counts in that bank (`search.cpp:812-825`);
- discovery ranking uses exact cross-products for the strict-bank rate and the
  remaining frozen integer tie-breaks (`search.cpp:1065-1080`);
- the runner hashes the exact deterministic selection bytes before heldout and
  rechecks them before and after that phase (`remote_run.sh:118-150`); heldout
  code reads only the four selected IDs, not discovery certificates;
- discovery and heldout use disjoint seed domains and each corpus construction
  enforces modulus distinctness across both splits (`search.cpp:243-291`); and
- the finite positive, null, and inconclusive summary thresholds implement the
  registered integer rules (`search.cpp:1160-1207`).

## P20 control scope

The P20 synchronization case is confined to `self_test`. It reconstructs the
displayed curve and seed for `N=10403`, checks the discriminant, computes all
affine multiples through index 101, verifies the two declared local gcds
`101` and `103`, and checks that the pooled product is zero modulo `N`
(`search.cpp:1209-1239`). It does not enter corpus construction, family
selection, or heldout scoring. This is the correct static scope. Dynamic
execution remains pending and is not authorized by this FAIL verdict.

## Required disposition

Preserve F265-D01 and this audit as an immutable failed packet. Any repair must
use a new version and new hashes. At minimum it must:

1. implement the exact `POWER` source and define the full-row-root transition;
2. implement and serialize the frozen opaque-block, third-root, and index
   pattern evidence;
3. keep `p,q` inaccessible until post-analysis labeling;
4. add CPU and gcd-free-split accounting and project all complete-packet work;
5. bound every sampling loop; and
6. place every packet phase under the declared wall, memory, output, and host
   availability gates.

Only a fresh hostile audit of that new immutable packet can authorize target
validation or a cohort launch.
