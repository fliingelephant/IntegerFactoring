# Verdict: FAIL
frozen_manifest_sha256: 1ebfeff0b66cdec024a9612279675f435ad668059289865b581bf4d2b74a70e8

# F266-D01 hostile pre-run audit

**DO NOT COMPILE, SELF-TEST, PREFLIGHT, OR LAUNCH THIS FROZEN PACKET.**

This was a static hostile audit. I did not compile or execute `search.cpp`,
invoke `remote_run.sh`, access the remote host, generate a corpus, or inspect a
discovery or held-out cohort.

## Frozen-artifact authentication

The SHA-256 of `FROZEN.sha256` is the authenticated manifest root shown above.
All five entries in that manifest match the local bytes:

```text
PASS  ALGEBRA.md             909e20c4e90a74266e99e80d120b21fbe16414dd7a88e144a936032ce3669c24
PASS  PREREGISTRATION.md     8e3704f68b59286c1b8ef82d5da5bd2ed9d579802b1c8b2e840fc06ae38816c7
PASS  search.cpp             820d0989c3816f091f6ab1931b02c3ebee445970bd107ae858dd3093f2df477d
PASS  remote_run.sh          a83ad64e3bb396b4899080f522d695e8773b105c814c402b51557993b17465cf
PASS  PRELAUNCH_MANIFEST.md  05fcee1e86fd36e397580206af7eea8c91828a5e62fab4b23c62388d402250f2
```

## Decisive blockers

### 1. The `N^2` source changes with the matrix, so the asserted same-level
carry quotient is not an identity

At level two, `make_row` draws three lift gauges from the supplied RNG and
uses them to change `a,r,s` (`search.cpp:702-715`). `generate_rows` constructs
a new RNG for every word, with a seed that depends on the word length and
matrix (`search.cpp:775-780`). Thus two level-`N^2` rows with the same
`base_id` generally have different lifted source forms and different exact
base discriminants `delta0`.

Equation (7) in `ALGEBRA.md` applies only when both rows have the same exact
base discriminant. Nevertheless, `screen_carries` treats equality of
`base_id` and level as sufficient and requires

```text
(x.value - y.value) mod N^2 = 0
```

for every such pair (`search.cpp:976-987`). The source proves only congruence
modulo `N`, not modulo `N^2`, across the word-dependent gauges. There is no
mathematical basis for this assertion. A failed assertion is caught inside
`analyze_public` and converted to an ordinary ineligible bank, not a resource
rejection (`search.cpp:1081-1117`). The preflight gate tests only resource
rejections, so it can pass even if this defect invalidates all banks
(`search.cpp:1656-1685`). This alone forbids dynamic validation.

### 2. The frozen direct-screen chronology is not implemented

The preregistration requires all transformed coefficient/discriminant screens
before all projective-root screens, then all projective determinants before all
quadratic resultants. Instead, `make_row` performs coefficient and projective
screens row by row (`search.cpp:718-754`). The pair loop then performs four
projective cross-determinants and one resultant for each pair before advancing
to the next pair (`search.cpp:950-965`).

Therefore a projective event from an early row can be recorded before a
coefficient event from a later row, and a resultant from an early pair can be
recorded before a projective event from a later pair. The stored
`first_channel`, first-applicable label, and replay chronology are not the
frozen hierarchy. All these calculations are public, but public arithmetic
does not repair the preregistered ordering claim.

### 3. Equal-row and square-template labels and certificates are incomplete

The frozen label hierarchy distinguishes `EQUAL_ROW_DECOY` from
`SQUARE_MULTIPLE_TEMPLATE`. The source increments `equal_rows` for an equal
pair but then processes every equal pair as a square multiple, increments
`useful_square_multiples`, and can set `strict_square_multiple`
(`search.cpp:1018-1033`). An equal-row mixed-root comparison can therefore
affect discovery ranking and null classification as the wrong family.

The executable also does not serialize full singleton, equal-row, or
square-multiple replay certificates. `certificate_bytes` writes only a generic
`DIRECT_OR_CARRY` object containing the first channel, a candidate, and a
factor (`search.cpp:1323-1341`). For normalized-root comparisons, that
candidate is already `gcd(exact_root +/- supplied_root,N)`, because the code
passes `gm` or `gp` back through `record_factor` (`search.cpp:997-1032`). The
row, exact square root, supplied root, normalized root, and original signed
difference are absent. This cannot authenticate the exact comparison claimed
by the lead gate.

### 4. Required opaque-block authentication is absent

The internal gcd-free refinement does preserve exponent vectors, checks final
pairwise coprimality, reconstructs every row, builds a binary parity matrix,
and verifies each kernel-basis vector (`search.cpp:844-947`). It does not
factor an opaque block, which is correct.

However, the frozen contract also requires every nonsquare block to be
recorded as `UNKNOWN_OPAQUE_NOT_NEEDED`. That string does not occur in the
source. Block values, exponent vectors, square status, and the required
unknown label are discarded when `analyze_public` returns. The bank output
retains only a block count, and the relation certificate retains only selected
input rows (`search.cpp:1252-1280,1323-1367`). The advertised complete P66
audit trail cannot be reconstructed.

Moreover, strict relation counters cover every useful kernel-basis row, while
only two useful relations per bank and 64 certificates per family/split can be
written (`search.cpp:1100-1113,1323-1366`). The lead gate never checks that
each bank supporting a positive gate has a retained full certificate. It can
therefore declare a lead whose counted hit is absent from the capped evidence.

### 5. The uniform-principal-digit baseline uses the wrong banks and row count

The stated comparison is `2*k/N` for an eligible bank with `k` distinct tested
rows. The code freezes `tested_rows` before equal-row, exact-square, and
rational-square-class canonicalization (`search.cpp:1084-1099`). Distinct
coefficient triples can have equal positive rows, so this is not the number of
distinct retained observations used by the residual decoder.

`lead_gate_bytes` then adds `2*tested_rows/N` for every evaluated bank,
including ineligible and resource-rejected banks (`search.cpp:1486-1500`). Its
cell `banks` counter has the same problem. The reported exact fraction is
therefore not the preregistered eligible-bank comparison mass.

The finite-null rule has an independent error. `no_gain` excludes strict
multirow, carry, orbit-singleton, and square-multiple events, but omits
`strict_base_singleton` (`search.cpp:1512-1513`). A useful held-out base
singleton can coexist with `finite_null_signal=1`, contrary to “no strict
heldout gain.” The cell anomaly table also reports only useful singleton
counts, not the frozen observed base and orbit singleton counts.

### 6. The authenticated selection parser does not authenticate selection
semantics

The held-out process does read the selection bytes once and verify their
SHA-256 before parsing. It also authenticates the discovery corpus before
generating held-out inputs (`search.cpp:1599-1617`). Those byte checks are
sound.

The parser, however, ignores every numeric rank metric and does not require
the four selected IDs to equal the first four IDs in the eight ranked rows. It
only requires four unique IDs that appear somewhere in the packet
(`search.cpp:1426-1457`). The runner obtains the expected selection digest
from a mutable sidecar produced in the same output directory. A coupled change
to the selection and sidecar before digest extraction passes the shell check,
and the held-out parser accepts any four known families. The frozen “select
the first four families” firewall is therefore not independently enforced.

### 7. The complete resource and evidence gates are false

Several independent runner defects violate the frozen contract:

- Compilation has no timeout or memory/file-size limit. Self-test has a
  timeout but no 4 GiB or 1 GiB limit (`remote_run.sh:42-49`). Thus the
  complete packet is not under the four-hour and 4 GiB envelope.
- The aggregate byte check counts only `output` and `preflight`; it excludes
  all uncompressed logs (`remote_run.sh:103-105`). Compile, self-test, and
  resource logs are outside the executable file-size limits as well.
- The preflight reports one-worker RSS but no conservative eight-worker RSS
  projection. Its output projection extrapolates only `bank_bytes`, omitting
  corpus, family, certificate, selection, lead-gate, manifest, and log bytes
  (`search.cpp:1662-1680`).
- Preflight does not require any eligible bank or reject ordinary analysis
  errors. This makes blocker 1 compatible with a nominal `pass:true`.
- The archive is created before `resource_after.txt` and
  `F266-D01.run_manifest.tsv` are written (`remote_run.sh:107-136`). Those
  final records are not in the evidence archive, and compression does not in
  fact occur after all uncompressed manifests are closed.
- Discovery and held-out output manifests hash their data files, but there is
  no phase manifest for preflight or logs and no final manifest with byte,
  line, and SHA-256 records. This does not implement “every phase manifest.”
- The overlap regex expects `F266-D01` before `search` in the process command,
  while this runner invokes its own executable as `./search`
  (`remote_run.sh:18-24,57-91`). It does not reliably detect another F266
  validation or production process.

These are launch-gate defects, not presentation issues.

## Static checks that passed

Subject to the blockers above, these parts are correct by static inspection:

- The only arithmetic analysis entry point is `analyze_public(N,family)`.
  Hidden `p,q` are used after it returns to label an exact public divisor.
- The split form satisfies
  `Delta_0 = a^2(r-s)^2 (mod N)`, and admitted source units make the supplied
  discriminant root a unit.
- The displayed `SL_2(Z)` coefficient transform preserves the exact integer
  discriminant. Canonical reduction gives the documented carry identity.
- For canonical `0 <= A,B,C < m`, the positive branch satisfies
  `0 < R <= 4m^2`; the source checks the corresponding row-bit bound.
- The projective root formula and determinant identity have the correct sign.
  The quadratic resultant formula `u^2-v*w` matches the `4 by 4` Sylvester
  determinant.
- Individual invariant carries and admitted cross-level differences are
  divisible by their documented moduli. The defect is specifically the
  same-level `N^2` comparison after changing the source gauges.
- Exact squares and rational square-class pairs are screened before residual
  representatives are removed. A globally signed removed row is algebraically
  redundant for later root classification.
- The internal P66 parity-kernel construction is factor-free, finitely capped,
  and verifies exact product squares and both signed gcds for the basis rows it
  evaluates.
- Prime, safe-prime, neighbor, pair-retry, source-attempt, word, matrix, row,
  pair, decoder, certificate, and worker loops have explicit finite caps.
  Accepted production cases enforce exact factor bits, primality, balance,
  and modulus distinctness across both splits.
- Writers refuse overwrite, check close status, and enforce an in-process
  aggregate byte cap. These local checks do not cure the runner-wide omissions
  above.

## Required disposition

Preserve F266-D01 and this audit as an immutable failed packet. Any repair must
use a new version and new hashes. At minimum, it must freeze one `N^2` lifted
source per base (or remove the invalid same-level quotient), implement the
exact direct chronology and label hierarchy, serialize replayable decoy/P66
evidence including opaque-block status, correct the baseline and null gate,
enforce selection semantics, and place every packet phase and evidence file
under the declared resource and manifest gates.

Only a fresh hostile audit of that new immutable packet can authorize target
validation or cohort execution.
