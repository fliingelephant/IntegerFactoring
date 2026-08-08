# F104 result — bounded negative scan; universal question open

## Verdict

No scanned completed survivor had an empty or independent peeled core.
Every completed survivor had positive core nullity.

This is a bounded negative result. It is not a theorem for all inputs. The
scan found no counterexample, and it does not prove that rank defect is
necessary.

## First-principles reductions

Degree-one peeling preserves nullity. If row `r` has the unique active
column `c`, then `r,c` is a pivot. Deleting `r` and `c` reduces both rank and
column count by one. Repeating this step preserves `columns - rank`.
Therefore an empty or independent core exists exactly when the full frozen
batch has nullity zero.

The accelerated rows are also exact for this question. Give each endpoint
its one-hot relation mask. For each prime `l`, XOR the masks of endpoints in
which `l` has odd valuation. A P66 refinement

```text
(a,M),(b,N) -> (gcd(a,b),M xor N),(a/gcd(a,b),M),(b/gcd(a,b),N)
```

preserves this prime-parity mask. At termination, pairwise-coprime blocks
put each prime in one block. A terminal block is a nonsquare exactly when
one of its primes has odd valuation. Hence the set of distinct nonzero P66
nonsquare-block masks equals the set of distinct nonzero hidden
prime-parity masks. Duplicate rows change neither binary rank nor which
columns degree-one peeling removes.

## Exact factor-free P66 scans

The exact scan used the pinned N-only F98 replay for generation, all direct
screens, exact-value deduplication, P66 rows, rank, and peeling. Prime factors
were used only to enumerate and certify the input family.

| Run | Prime interval | Pairs | Stable | Completed | Min core columns | Min nullity |
|---|---:|---:|---:|---:|---:|---:|
| `PRESCAN_300_1200` | 300–1,200 | 200 | 57 | 0 | — | — |
| `SCAN_1K_5K` | 1,009–5,000 | 250 | 74 | 0 | — | — |
| `SCAN_10K_20K` | 10,007–20,000 | 500 | 162 | 5 | 1,395 | 288 |
| `SCAN_10K_20K_WIDE` | 10,007–20,000 | 1,000 | 291 | 6 | 1,781 | 488 |
| `SCAN_20K_40K` | 20,011–40,000 | 100 | 25 | 4 | 1,105 | 142 |
| `SCAN_40K_80K_P66` | 40,009–80,000 | 100 | 24 | 4 | 436 | 7 |

The two 10K–20K runs overlap. Together, the exact runs contain 17 distinct
completed moduli. All 17 have nonempty, rank-deficient cores.

## Accelerated candidate scans

These runs changed only the terminal row construction. They used the
theorem-equivalent distinct hidden prime-parity masks. No accelerated result
was eligible for acceptance without an exact P66 replay.

| Prime interval | Pairs | Stable | Completed | Min core columns | Min nullity |
|---|---:|---:|---:|---:|---:|
| 40,009–80,000 | 100 | 24 | 4 | 436 | 7 |
| 80,021–160,000 | 100 | 33 | 9 | 36 | 6 |
| 160,001–320,000 | 100 | 25 | 15 | 74 | 12 |
| 320,009–640,000 | 100 | 33 | 27 | 24 | 4 |
| 640,007–1,280,000 | 100 | 37 | 28 | 114 | 17 |
| 1,280,003–2,560,000 | 40 | 6 | 6 | 33 | 6 |
| 5,000,011–10,000,000 | 30 | 8 | 7 | 151 | 21 |
| 20,000,003–40,000,000 | 20 | 7 | 7 | 567 | 78 |

These eight disjoint-band runs contain 103 completed observations and no
candidate. A structured scan tested 100 prime pairs of the forms
`p=g*A+1`, `q=g*B+1`; 6 completed, with minimum nullity 126. A rectangular
scan paired primes in 100,003–200,000 with primes in 5,000,003–10,000,000;
5 of 50 pairs completed, with minimum nullity 30. Neither scan found a
candidate.

The exact and accelerated paths were calibrated on five completed moduli.
For each, column count, rank, nullity, core columns, core rank, core nullity,
and the core-column hash matched. For example, at `N=803101753`, exact P66
used 12,621 rows and the distinct hidden-prime representation used 10,865
rows. Both gave 10,538 columns, rank 10,232, core size 1,730, core rank
1,424, nullity 306, and core hash
`f0cb0217059ec6ff22547b551fe0256f5d5edd24bf5372150ce022735b981ebc`.

## The three outcomes are different

The exact P66 input

```text
N = 3241632473 = 41011 * 79043
```

had a nonempty core with 436 columns, core rank 429, and nullity 7. All seven
public kernel-basis roots were `+1 mod N`. Thus a nonempty core did not imply
a non-global root, even though this core was rank-deficient.

The smallest accelerated core occurred at

```text
N = 204816942773 = 320107 * 639839.
```

It had 24 core columns, core rank 20, and nullity 4. All four basis roots
were `+1 mod N`. Its four dependencies each had support six. This near miss
still did not give an independent core or a non-global root.

## Audit boundary

The 400-pair wide scan over 320,009–640,000 hit its 300-second hard timeout.
Its partial output is excluded. `FAILED_RUNS.md` records the last checkpoint.

Pinned source hashes:

- F98 public replay: `5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b`
- Exact F104 replay: `41c8ddee5d51d85349af2b61e239f81f9c6e12fb13d1eca92f0440f5d5eece50`
- Accelerated candidate scan: `2b38a3920524a434988ab4fa105d5770a2ef755e5d519c4248b0d2d6bebda79f`

The narrow conclusion is: this bounded search supplies evidence for rank
defect but no all-input proof. The existence of a stable trial-hard complete
survivor with an empty or independent core remains unresolved.
