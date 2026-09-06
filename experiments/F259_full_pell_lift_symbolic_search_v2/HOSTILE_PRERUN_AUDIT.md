# F259-D02 V2 hostile pre-run audit

Verdict: PASS

This is a static pre-run verdict on the frozen V2 packet. I did not compile or
execute `symbolic_search.cpp`, invoke `remote_run.sh`, access the target host,
generate inputs, or open a discovery or held-out cohort. Target compilation,
self-test, benchmark, and production remain pending. This verdict authorizes
only the frozen runner's validation sequence after every incompatible process
has ended.

## Artifact authentication

The observed SHA-256 of the supplied V2 `FROZEN.sha256` is
`74a290c1d4b9065c46a36946d8c5f73b6ab58f78d15eacac93ce4fcf1068bc33`.
Every entry authenticates against the local bytes:

```text
PASS  PREREGISTRATION.md      274d6a4ce520ffb4cffeedcc9b0d244f77eeff3ddf7bed26e380fa03fcec7b36
PASS  ALGEBRA.md               20f0ebcfdb201542e3fccb75152f9a9d11de0b6857d1d5e61878ee24ccc7473d
PASS  symbolic_search.cpp      6e3cde672b893c9df13018e4a630c04f6b413d0de7ba3e09a65f8b7667c2c930
PASS  remote_run.sh            7640d30c291286cab634655b51db8ce7e7d36d09146ef982105b9afeeb541bc9
PASS  PRELAUNCH_MANIFEST.md    a6e5b80e216c95bdfc2cf7c6d97bfd801fcbd097ffb7a7b17f7af3747367b033
PASS  VALIDATION_PENDING.md    78993e92a82012491d498a30064fcf521cb24d9bffec74dd1ca3b686bccfdbce
PASS  STATIC_VALIDATION.md     e0875f5444f1d8e4a2f7ee5e983622b2cf56952a969958f4bff2ff5f4ecf6db2
PASS  AUDIT_REQUEST.md         2ecd15b2dd9ca27f74aa51c5f9987f82db93184aef5f67405f5288b1b5b9aa99
```

The preserved V1 packet and its FAIL audit also authenticate exactly:

```text
PASS  PREREGISTRATION.md       0b162d3f0b8c653483a3b92e5106b2b60b7066fa464366e9654163182198a014
PASS  ALGEBRA.md                7f5c1679816eb57e9810ce112f93c97ed0edef136f710f22d91596287e0cefb8
PASS  symbolic_search.cpp       2b8c941782cfa10aeb3598a558c6a9008a9a98534933ca58c4e94d628be9a145
PASS  remote_run.sh             77be4b41f8d414819bc0137f723309804e63fc193556f0e5c1520b7b7fd83e45
PASS  FROZEN.sha256             f876baafab99508e900b3fea8d65a5416118e756eb9dd5987d79786f1d101ead
PASS  HOSTILE_PRERUN_AUDIT.md   ef242ae9fb611f7d47fd3fb599f6ce07c34171fc4bc07d96c362ae16a153cb75
```

The three additional artifacts named by the V1 freeze list also remain
unchanged: `SELF_TEST.md` is
`678999e8f58703a569da5d68df7a5fc12933a5aff15a213b80706ff2a078b434`,
`BENCHMARK.md` is
`f3b59bc0f1cc5c3f568a38517f390028f26c7575b728514fa84b0d74b6bcbc24`,
and `FAILED_SELF_TEST.md` is
`2d0325d849ea1c5915f78d653b57807b612f4af3d50e15e112f858b00e8a301e`.
V1 remains an immutable failed packet.

## V1 repair reconstruction

Each decisive V1 defect has a source-level V2 repair:

- Family 20 inserts `D*c*(2*z+c*N)` without a zero-to-unit substitution.
  A zero first carry therefore increments the family zero count.
- Families 21 and 22 evaluate every admitted second finite difference and
  the displayed cubic or quintic core directly. The identity
  `E=4*D*c^2*core` is checked without division by `c`. Both target-15 route
  atoms are inserted whenever the two target-15 scopes exist, including
  zero-carry cases.
- Identity mining has exactly 12 columns. The four V1 carry-product columns
  are absent. The source computes rank 10 and exhausts all `3^12` ternary
  coefficient vectors after zero rejection and sign normalization.
- All four source screens use one certificate recorder. A first proper
  cleanup gcd overwrites an earlier grammar certificate and retains the
  proper divisor and public `D`/index scope. On a cleanup-free input, the
  first grammar gcd retains its family, formula tag, divisor, residue modulo
  `N`, and atom bit length.
- Repeated exact division by the public composite `N` records the total
  number of removed powers per family. Zero and unit outcomes remain
  separately counted.
- `cleanup_free` and `strict` have separate meanings. A cleanup-free direct
  family hit retains a grammar certificate. A strict P205 row has neither a
  cleanup factor nor a grammar-atom factor.
- Cohort labels, family summaries, normalized word syntax, stream-close
  checks, retry bounds, firewalls, and runner resource/report gates are all
  present in V2.

## Algebra and exactness

The Pell quotient and norm-digit identity, both tangent defects, both
multiplication carries, the quadratic resultant, and its same-discriminant
factorization are correct. The source asserts exact divisibility for the
norm digit, both carry coordinates, and every second finite difference by
`N^2`. Its cubic and quintic core formulas expand to the two frozen curvature
identities, including `c=0`.

`primitive_n` takes an absolute value, treats zero separately, and divides by
the whole public integer `N` until exact division stops. It removes no other
content. Every family constructor passes through this same normalization and
proper-gcd path.

## Families, scopes, and static work

All 22 family constructors match the frozen table. This includes both old
`(y,k)` controls, lift and tangent atoms, ten vector determinants per edge,
eight signed carry-resultant factors per edge, both cross-discriminant full
resultants, five collision coordinates with both signs, nine triple atoms,
and all admitted carry compositions.

The row window is exactly `1 <= j <= 4*bitlength(N)`. Same-`D` edge and triple
sets use the frozen patterns, sum-window tests, set deduplication, independent
public SplitMix64 priorities, and caps of 256 and 64 per discriminant.
Cross-discriminant pairs use every retained same-index pair. Composition
routes use only multipliers 3 and 5 and require the product index to stay in
the window. No hidden factor enters a scope, priority, atom, or word.

The maximum-input insertion projection reconstructs exactly:

```text
row atoms       3,840 * 6             =  23,040
pair atoms      2,048 * 37            =  75,776
triple atoms      512 * 9             =   4,608
composition     3,840 * 12            =  46,080
cross-D           480 * C(8,2) * 2    =  26,880
total                                      176,384
```

The word-score count is exactly `7,040*255 = 1,795,200`.

## Cocycle search

The matrix columns are exactly the six signed real terms followed by the six
signed imaginary terms in the displayed associativity cocycle. Training uses
96 fixed public synthetic samples modulo `1000000007`. The source requires
rank 10, so the modular nullity is two. It enumerates the entire normalized
ternary universe and requires exactly four vectors: the real control, the
imaginary control, their sum, and their difference. The two disjoint-support
controls form the primitive basis.

Each of the four candidates is then evaluated as an exact integer identity on
64 disjoint holdouts with moduli `2000003+2*t` and source schedules `96+t`.
All four remain reported decoys and are never inserted into a family product.
This authenticates the declared bounded basis; it makes no claim about a
larger symbolic universe.

## Words, scores, cohorts, and reports

The word grammar is non-adaptive and has
`1+22+C(22,2)+1 = 255` shapes. Products are reduced exactly modulo `s_p` and
`s_q`, raised to `n=bitlength(N)`, and scored by the two exact residual gcds.
Discovery ranking cannot change the word set or any held-out computation.
Its description length is the byte length of the frozen normalized syntax,
not the display-name length.

Prime, safe-prime, next-prime, and outer cohort retry loops all have explicit
failure bounds. Accepted factors have the requested bit length, are distinct,
are ordered as `p<q<2p`, and safe-safe factors have prime half-factors. A
per-size set enforces pair/modulus distinctness across all three cohorts. The
frozen counts are 512 random, 256 consecutive, and 256 safe-safe at each size,
except 128 safe-safe at 16 bits. They total 7,040.

The TSV schema has `14+22*5+255*2 = 634` columns and retains each exact input
row. Family aggregation has `7*3*22 = 462` rows and includes zero, unit,
stripped-power, direct-event, direct-input, and cleanup-free direct-input
counts. Word aggregation has `7*3*255 = 5,355` rows and includes mean `H`,
interpolated median/90th/99th loss quantiles, improvement, saturation, and
strict counterparts. These summaries expose the preregistered direct-family
threshold and the safe-safe/random word criteria without adapting them.

## Runner and preservation gates

The runner requires an empty one-shot output/log area, this fresh audit, and
all frozen hashes before compilation. Its process firewall scans command
line, working directory, and executable path for every F258, F260, F261,
F263, or F264 process. It checks before, during, and after compilation,
self-test, benchmark, description, production, report validation,
compression, and compression validation. Scanner failure is conservative.

Every monitored command uses `nice 15`, a 4 GiB virtual-memory limit, and a
mode timeout. Resource gates require at least eight allowed CPUs, 8 GiB
available memory, 4 GiB free disk, and one-minute load no greater than three
times the allowed CPU count before compilation, benchmark, and production.
Production uses exactly eight threads. Its four-hour deadline is shared with
TSV/JSON validation and compression.

The runner requires three full-pipeline 120-bit benchmark repetitions and
rejects the conservative projection
`1.75*max_seconds*7040/8 > 14400`. The static output prediction is
494,927,872 bytes. Aggregate output and logs are monitored below 1 GiB with
1 MiB reserved for the final manifest. Successful completion requires 7,040
rows, 634 columns, every exact cohort count, parseable JSON, 255 rankings, 462
family summaries, 5,355 word summaries, successful stream closes, a valid
gzip stream, and nonempty final artifacts. The exit trap preserves hashes and
failure status on every post-gate exit.

No static blocker remains. `STATIC_VALIDATION.md` was treated only as a claim
and was independently reconstructed. A PASS from target compilation,
self-test, benchmark, and report validation is still mandatory and is not
implied by this audit.
