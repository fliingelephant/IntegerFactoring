# F116 Sparse-DAG First-Case Hostile Audit

## Verdict

**PASS_WITH_CLAIM_BOUNDARIES.** The fixed advised support is a valid useful
dependency. The independent verifier regenerates the source, replays the
support without factorization, and obtains the reported factor split.

Three stronger readings fail:

1. The sparse candidate does not perform exact-value deduplication.
2. Its discovery run is not a factor-free polynomial-time algorithm. It uses
   Sage endpoint factorization.
3. Its XOR DAG removes dense combination masks. It does not make total memory
   constant or linear.

The no-stop and no-support consequence is limited to useful-dependency
existence, called the P66 level here. This audit did not run the full 1,378-pair
source or a complete factor-free decoder.

## Claim ledger

| Claim | Verdict | Exact boundary |
| --- | --- | --- |
| Public source through the advised stop | PASS | Regenerated from `N`, `n`, and `B`; stop controls termination. |
| Residue first-occurrence dedup | PASS | Counts and source order match the candidate. |
| Trial, invertibility, and endpoint gcd screens | PASS | No proper divisor appears before the dependency. |
| Candidate exact-value dedup | FAIL | The candidate sends every retained residue relation to the prime-row decoder. |
| Independent exact-value projection | PASS | 148,930 duplicate columns and one unit are removed. |
| Sparse GF(2) elimination mechanics | PASS | Conditional on exact endpoint factorizations supplied by discovery. |
| Persistent XOR-DAG recovery | PASS | Algebraic audit and independent dense-model test pass. |
| Online modular half-root invariant | PASS | Algebraic audit, symbolic test, and terminal exact root agree. |
| Exact factor-free replay of the advised support | PASS | No factorization or primality call is used. |
| Terminal factor output | PASS | The computed gcds are 159,999,943 and 80,000,059. |
| Discovery is factor-free polynomial bit time | FAIL | Endpoint factorization has no proved polynomial bound. |
| DAG total memory is constant or linear | FAIL | Pivot parity sets and elimination nodes still grow with the stream. |
| Full-source no-stop/no-support run | NOT RUN | Only useful-dependency existence is proved by monotonicity. |
| All-input factoring theorem | FAIL | Success is established for one selected fixed input only. |

## Promoted evidence

The promoted command is:

```text
/opt/homebrew/bin/python3 experiments/F116_independent_54bit_all_pairs_stress/SPARSE_DAG_AUDIT_run_with_timeout.py
```

The runner imposed a 300-second hard timeout. It returned exit code zero in
4.833909 seconds. The verifier's internal time was 4.762973 seconds.

The decisive phase read only:

- `N = 12,800,004,879,996,637`;
- `n = 54`;
- `B = 2,916`;
- the retained-record stop `771,082`;
- 6,486 advised retained-record indices.

It did not call factorization or primality code. It did not import or execute
the candidate. It read the candidate output and its known factors only after
it computed the terminal gcds. The candidate and its Sage run are discovery
evidence only.

Two preliminary named passes took 4.403388 and 4.822484 seconds. They were not
promoted because the final verifier then added explicit first-occurrence and
coordinate-number checks and narrowed the no-stop statement to P66 existence.
They were successful, not failed runs.

After this decisive run, a separately isolated `RECONSTRUCT_*` replay became
available. It also regenerated the same source counts and obtained the same
root residue and terminal gcds without factorization. Its integer-hash format
is different, so its product and root digest strings are not directly
comparable. Its monotonicity discussion does not perform exact-value dedup;
the raw-to-exact projection proof in this report supplies that missing step.

## Source regeneration

The verifier independently implements the stated gcd and perfect-power seed
basis. It verifies pairwise coprimality, perfect-power freedom, and exact
endpoint reconstruction.

```text
seed endpoints                 = 106
public basis blocks            = 39
frozen pairs                   = 53
frozen attempted residues      = 309255
frozen duplicate residues      = 233418
frozen retained relations      = 75837
menu pairs attempted           = 177
stop pair                      = (5,29)
all attempted residues         = 1336218
duplicate residues             = 565136
retained relations             = 771082
```

The 53 frozen pairs equal the candidate list exactly. The complete retained
stream digest is
`63c9adfc73fff1ed982ce954c5e1651468fd7a258446db9936600950b515baf4`.
The output defines the bounded encoding used by this digest.

### Direct screens

All 2,915 trial gcds are one. All 771,082 retained residues are units. The
1,542,164 endpoint sign screens give:

```text
gcd 1                          = 1542163
gcd N                          = 1
proper gcd                     = 0
```

The gcd equal to `N` is the minus screen for the retained residue `c=w=1`.
No proper factor precedes the parity dependency.

## Exact-value coordinates

The candidate has residue first-occurrence deduplication. It does not have
exact-value first-occurrence deduplication. Its sparse decoder therefore has
771,082 raw relation columns.

The independent projection removes:

```text
unit P=1 columns               = 1
repeated exact P columns       = 148930
unique nonunit exact columns   = 622151
projection-kernel dimension    = 148931
```

Let `pi` map each nonunit raw column to the first column with the same exact
value `P`, and let it map a unit column to zero. The kernel of `pi` is generated
by unit columns and pairs of columns with the same `P`.

- A unit generator has root `+1`.
- A same-value pair has exact product `P^2` and positive root `P`.
- Every relation satisfies `P = c*w = 1 mod N`.

Thus every projection-kernel direction has global root `+1`. Projection
cannot change a useful root class.

For this support, the result is stronger than the general projection claim:

- all 6,486 selected values are distinct nonunits;
- each selected record is that value's first raw occurrence;
- zero selected values first occur outside the advised support;
- the value projection is one-to-one;
- the first-occurrence raw records are the selected raw records.

One-to-one value projection and raw-coordinate identity are different facts.
Both happen to hold for this support. The projected dedup-column indices differ
numerically from the raw retained-record indices because 148,931 earlier raw
columns are removed.

## Sparse elimination and persistent DAG

The candidate builds one parity set from the odd prime exponents of each raw
relation. It always eliminates the largest row label. A stored pivot with that
label has no larger label, so symmetric difference removes the pivot and
cannot add a larger one. Elimination terminates and is ordinary sparse GF(2)
row reduction.

The reported discovery accounting is internally exact:

```text
pivots                         = 615011
dependency events              = 156071
pivots + dependencies          = 771082
global dependencies            = 156070
non-global dependencies        = 1
eliminations                   = 581630
DAG nodes                      = 581630
maximum reduced parity width   = 290
```

These rank and dependency counts remain factor-assisted discovery data. The
decisive verifier does not reproduce 615,011 prime-labelled pivots.

Each negative expression reference is a relation leaf. Each nonnegative
reference is a node whose two children predate it. A new elimination stores
the XOR of the current expression and a prior pivot expression. Reverse
topological toggling therefore recovers the leaf XOR exactly. Shared leaves
cancel because both node activity and leaf membership are toggled modulo two.

The independent mechanics test compares the sparse state with dense exponent
sums. Its third relation reduces through a pivot that already contains a DAG
node. Two paths share one leaf. Recovery cancels that leaf and returns support
`[1,2]`. All six parity and half-root invariant checks pass.

### Online half-root invariant

For an expression `E`, let `a_p(E)` be the total exponent of label `p`, let
`S(E)` contain labels with odd exponent, and define

```text
h(E) = product p^floor(a_p(E)/2) mod N.
```

When two expressions combine, their parity sets use symmetric difference.
For each label odd in both expressions, the floor exponent gains one. This is
the candidate's multiplication by every label in the parity intersection.

XOR can also cancel a relation present in both expressions. That removes the
square of its exact relation value. The corresponding half-root division is
by `P`, but `P = 1 mod N`. The candidate can omit this division modulo `N`.

When parity becomes empty, `h(E)^2 = 1 mod N`. The recovered support's exact
positive square root gives the same residue as the online value. This checks
the terminal use of the invariant without accepting endpoint factorization as
decisive evidence.

## Exact factor-free certificate replay

The raw advised support gives:

```text
support size                   = 6486
first retained index           = 655
last retained index            = 771081
frozen support relations       = 1844
appended support relations     = 4642
distinct appended pairs        = 137
exact product bit length       = 672808
positive root bit length       = 336404
root modulo N                  = 5266287723884331
root squared modulo N          = 1
```

The raw and projected exact products are identical because no selected value
is a unit or duplicate. Their product and root hashes match the discovery
output:

```text
product SHA-256 = ca9861f8261bf075259fed84bcf54194b38264206d0f3d0438f2bcbc292a7fb3
root SHA-256    = 907bdd7a35f8bf93a5c91e15ff46860005babfce9d41013f3d9bdf09333c65d9
```

Terminal extraction gives:

```text
gcd(root-1,N) = 159999943
gcd(root+1,N) = 80000059
product       = 12800004879996637
```

Only after these values existed did the verifier compare them with the two
known factors in the discovery output.

## Stop, support, and monotone extension

The promoted factor-free replay is an advised certificate. It needs both the
stop and the 6,486 support indices.

Two different monotonicity statements hold.

1. **Raw residue-stream monotonicity.** Appending source attempts does not
   change an earlier first-retained residue or raw column. The advised raw
   dependency embeds with zero coefficients on later columns.
2. **Exact-value monotonicity.** First-occurrence exact-value dedup keeps all
   earlier unique columns in place. The projected useful dependency embeds in
   the extended exact-value matrix.

The second statement uses the projection proof above. It must not be
attributed to the candidate, which does not run that deduplication.

The precise full source for the P66 existence corollary is:

1. seeds `2..n`;
2. frozen pairs in seed-relation order;
3. all unordered pairs `2 <= u < v <= n` in lexicographic order;
4. exponents `0..n^2` for each pair;
5. orientation `u^e*v` followed by `u*v^e`;
6. residue first-occurrence retention with no stop.

The separate complete decoder is:

1. remove units and repeated exact values by first occurrence;
2. build a factor-free gcd basis for all retained endpoints;
3. build the complete GF(2) square-class kernel;
4. test every kernel-basis root modulo global sign.

The verified prefix proves that this full exact-value system contains a useful
dependency. A complete basis must contain a useful root if the root map modulo
global sign is nonzero. However, this audit did not generate all 8,348,507
scheduled full-source positions and did not run that decoder. The no-stop and
no-support result is therefore promoted only as useful-dependency existence,
not as an executed factorization.

## Complexity and memory

The full source has

```text
(n-1) + 2(n-1)(n^2+1) + (n-1)(n-2)(n^2+1) = O(n^4)
```

scheduled positions. Each exact relation value is less than `N^2` and has at
most `2n` bits. With `O(n^4)` columns, a dependency product has `O(n^5)` bits.
A gcd-free basis, complete binary elimination, exact square roots, and gcds
on these polynomial-size integers give a polynomial-bit-time and
polynomial-space complete decoder specification. This is an asymptotic
statement. It is not a completed full-source run.

The sparse candidate has a different boundary:

- Sage endpoint factorization is not known to run in polynomial bit time.
- The DAG stores two signed 64-bit references per elimination. The fixed run's
  581,630 nodes use 9,306,080 bytes of array payload, excluding array headers.
- Each pivot also stores a parity `frozenset`, one expression reference, and
  one modular half-root. The output gives only maximum parity width, not total
  parity incidence or peak resident memory.
- Sparse DAG expressions avoid one dense relation mask per pivot. Total memory
  still grows with retained residues, pivots, parity incidence, and
  eliminations.
- Signed 64-bit references are safe for this fixed run. They do not define an
  unbounded all-input representation.

Thus the DAG is an effective fixed-case memory improvement. No linear-memory,
constant-memory, factor-free-runtime, or all-input complexity claim follows.

## Failure accounting

All five recorded failed attempts remain preserved:

1. The first process-pool run exited after a sandbox `sysconf` denial. It
   produced no batch result.
2. The pure-Python endpoint-factorization retry timed out after 1,800 seconds.
   It produced no completed case.
3. The Sage batch was killed with exit 137 after one provisional case. It had
   no exported exact support and is discovery evidence only.
4. The first isolated Sage retry exited during a forbidden `.sage` cache
   write. It produced no candidate output.
5. The second isolated Sage retry was killed with exit 137 after 57.116710
   seconds. It produced no support.

The later sparse-DAG discovery passed. The independent audit had no failed
hard-timeout run. The manifest pins every source, output, log, and recorded
failure.

## Exact theorem boundary

The narrow conclusion is:

> For `N = 12,800,004,879,996,637`, the advised 6,486-record raw support is an
> exact square dependency with a non-global root. Its first-occurrence
> exact-value projection uses those same first-occurrence records and has the
> same root. The
> reported factor split is correct. Appending the remaining fixed source
> preserves useful-dependency existence in both raw and exact-value systems.
> The certificate replay uses stop and support advice. The full no-stop
> complete decoder was not run. No result for another input follows.
