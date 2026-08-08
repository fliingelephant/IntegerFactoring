# F116 full-source success corollary reconstruction

## Result and claim boundary

**PASS.** The reconstruction executed the supplied retained-record prefix. It
used the supplied raw support only to verify one useful dependency on this
fixed input. The run passed under the named 900-second hard timeout. The runner
elapsed time was 4.071624 seconds. The verifier elapsed time was 3.915429209
seconds.

The reconstruction did **not** execute the complete 8,348,507-position source.
It did **not** execute the complete factor-free decoder. Instead, the verified
prefix dependency proves an existence corollary for that complete algorithm.
The complete algorithm receives only `N`. It receives neither the prefix length
nor the dependency support.

The result applies only to the supplied `N`. It does not claim success on
another input. It does not claim a success density or a probability law. It
does not give a factoring algorithm for arbitrary integers.

## Isolation

Only these supplied project files were read:

- `FULL_SOURCE_COROLLARY_RECONSTRUCT_STATEMENT.md`, SHA-256
  `dacb0f606313045ce3f0e7b6ff75433bad437ac2b372056f71a021cfce5dce1b`.
- `RECONSTRUCT_INPUT.json`, SHA-256
  `5194ee596916810edb78fa802c3179341746423c6fb65f2548a600c598b05015`.

After this reconstruction began, no other F116 file and no F111 file was read.
`PROVED.md` and candidate implementations were not read. The computation did
not use a supplied factor, integer factorization, or a primality test.

The public values were:

```text
N = 12800004879996637
n = 54
B = 2916 = n^2
retained-record prefix = 771082
advised raw support size = 6486
```

The sorted support-index sequence has SHA-256
`080851d4e856eaec12d20b9e5609b824bd3aa03180cb2b4de13868c70fbd8cdb`.

## Executed advised-prefix verification

The trial screen tested all 2,915 integers from 2 through 2,916. Every gcd was
1. All 53 seeds were first residues and were retained.

The deterministic seed gcd basis used a last-in, first-out work list and the
first ordered basis overlap. It extracted maximal exact perfect powers. It
merged equal values. For unequal values `x,y`, it used `d=gcd(x,y)` and pushed
`(d,s)`, `(x/d,s)`, `(d,t)`, `(y/d,t)` in that order. It then sorted the final
blocks and verified exact reconstruction of all 106 endpoints.

The basis had 39 final blocks:

```text
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
12144217153697, 31013607193423, 52747272857129, 67085979454909,
148027267319689, 293620183627163, 341333463466577,
366666806458237, 821621934864649, 864000329399773,
1098039634313437, 1170732153658229, 1267633333526237,
1288312179480181, 2492632529262503, 2725926965184469,
2868966611033729, 3125582586975923, 4480001707998823,
4758976173332083, 5236365632725897, 7757578715149477,
10893621174465223
```

The basis stage made 795 work pops, 9,883 perfect-power exponent tests, 27
perfect-power extractions, 18,035 gcd tests, 193 equal merges, and 124 unequal
splits. The final signatures had 214 entries. Pairwise coprimality and exact
endpoint reconstruction passed.

The 53 frozen pairs produced 309,202 attempted positions. They retained 75,784
new residues and rejected 233,418 duplicates. Including the seeds, the
unordered-pair layer began with 75,837 retained records.

The prefix entered 177 lexicographic unordered seed pairs. It completed 176 of
them. The stop occurred in pair index 176, pair `(5,29)`, at exponent 89 and
orientation `[u^e v]_N`. The last raw index was 771,081. Its canonical residue
was 9,376,877,912,284,379 and its least positive inverse was
6,461,503,751,599,984.

The complete prefix accounting was:

```text
attempted positions    1,336,218
retained first residues  771,082
duplicate residues       565,136
```

The maximum endpoint bit length was 54. The maximum exact relation-value bit
length was 108. The retained-record trace SHA-256 was
`5978faf5abdbb44f7d67956ae6430c7f206b316dd145357bef7028d4320aac98`.

Every retained residue was invertible. Every retained residue received both
direct sign screens. No direct screen gave a proper divisor. The minus screens
gave 771,081 unit gcds and one improper gcd equal to `N`. The plus screens gave
771,082 unit gcds. The improper case was `c=w=1` at raw index 70,008, so it was
the identity case `gcd(c-w,N)=N`.

The raw dependency support did not alter source order or residue retention. The
supplied prefix length was the only stop condition. The support only selected
already-generated raw records for the proof. All 6,486 advised indices were
regenerated. Their complete selected-record trace SHA-256 was
`ce461ce04cf2ffa8891a2cc299e6ca389c8c2851b2c6f8e8676fd5cce13b12e1`.

## Advised raw dependency

The verifier multiplied all 6,486 selected exact values. It did not use modular
parity as a substitute for exact multiplication. The product had 672,808 bits
and SHA-256
`3dd659d9881e940191b6a9e40bf0ce7539a5032effeb116ee2f340ee466d83f7`.
It was an exact square.

The positive root had 336,404 bits and SHA-256
`014bbc5972a53228db75169355fb6c7bc15b4bd23aef68af0011c4d8bc4015c9`.
Its residue was

```text
5266287723884331 modulo N.
```

Its square was 1 modulo `N`. It was neither `+1` nor `-1`. The terminal tests
were

```text
gcd(root-1,N) = 159999943
gcd(root+1,N) = 80000059
```

Both values are proper divisors. They were computed at the terminal step. They
were not supplied as input.

## Exact-value projection

Let the raw vector space have one binary coordinate per retained raw record.
Let the exact vector space have one coordinate for the first occurrence of each
distinct nonunit exact value. Define `pi` as follows:

- Map a raw `P=1` coordinate to zero.
- Map every other raw coordinate to the coordinate of its exact value.

There was one raw unit column. There were 148,930 later occurrences of earlier
exact values. The projection retained 622,151 distinct nonunit exact columns.
Their value-sequence SHA-256 was
`a99a25d65a68665ee5c27085448ce221a432a0df232f8117617e7e8d45043bba`.
Their first-raw-index sequence SHA-256 was
`1b7f1f4f6d41d988765dc9fd002ca694584d9851d6828c76ee864be1bc33f0b3`.

A raw unit direction has selected product 1. Its positive root is the global
root `+1`. For a later raw column `j` with the same exact value `P` as its first
column `f`, the direction `e_j+e_f` has exact product `P^2`. Its positive root
is `P`, and `P=1 (mod N)`. Thus this direction also has global root `+1`.

These directions generate `ker(pi)`. To see this, take any raw vector in the
kernel. For each later duplicate coordinate, add its direction with the first
representative. This removes every later coordinate. The remaining nonunit
coordinates are first representatives. Since their images are distinct basis
coordinates and the projected vector is zero, all of them are zero. Only unit
coordinates remain, and the unit directions generate those coordinates.

Therefore projecting any raw square dependency removes only square products
whose positive roots are 1 modulo `N`. The projected exact product remains a
square and has the same root residue, hence the same normalized root class.

For this advised dependency, every selected value was a distinct nonunit. All
6,486 selected raw records were their global first occurrences. Thus the raw
and projected products were exactly identical. The projected support had 6,486
columns and SHA-256
`bda44b6d08bfc25f23a3773a628b70f70c6c6f1d070594cc0f8584c0db3d555f`.
Its product hash, root hash, root residue, and both terminal gcds matched the
raw dependency exactly. The projected dependency was nonzero.

## Factor-free exact square-class decoder theorem

For exact column `j` with endpoints `c_j,w_j`, start with entries
`(c_j,e_j)` and `(w_j,e_j)`. An entry `(x,A)` means that the integer `x` occurs
in the columns selected by mask `A`.

When two entries overlap, let `d=gcd(x,y)>1`. Replace

```text
(x,A), (y,B)
```

with

```text
(d,A xor B), (x/d,A), (y/d,B).
```

Fix one column. Let its two mask bits be `a,b`. The old contribution is
`x^a y^b`. The new contribution is
`d^(a xor b)(x/d)^a(y/d)^b`. The quotient of old by new is 1 for `00`, `10`,
and `01`. It is `d^2` for `11`. Each refinement therefore preserves every
column product modulo exact integer squares.

The deterministic refinement stops with pairwise-coprime terminal values. A
square terminal value gives no parity constraint. A nonsquare terminal value
has at least one prime with odd exponent. Pairwise coprimality makes that prime
unique to this terminal value. Hence a selected product is a square exactly
when every nonsquare terminal mask has even intersection with the selected
columns. These masks give the same kernel as hidden prime parity. The algorithm
does not compute a prime factor.

Binary elimination returns one kernel vector for every free column. It checks
each returned vector against every row. Rank plus nullity equals the column
count. Thus those vectors form a complete binary kernel basis.

## Append monotonicity and complete-basis detection

The verified retained records are an initial prefix of the fixed complete
source. First-occurrence exact-value deduplication preserves all old distinct
values in their old order. A later record equal to an old exact value is
discarded. Every new distinct value follows the old coordinate block.

Extend the projected prefix dependency by zero on every new exact coordinate.
Its selected exact product and positive root do not change. It remains a
nonzero normalized dependency in the complete-source kernel.

For kernel vectors `x,y`, let `C` be their common selected coordinates. Binary
addition selects the symmetric difference. Exact positivity gives

```text
R(x)R(y) = R(x+y) * product(P_i for i in C).
```

Every exact value `P_i` is 1 modulo `N`. Hence
`R(x+y)=R(x)R(y) (mod N)`. The root map is a homomorphism. Quotienting by the
global subgroup `{+1,-1}` gives the normalized root-class homomorphism.

If every vector in a complete kernel basis had global class, the homomorphism
would be zero on their span. Their span is the full kernel. This contradicts
the extended useful dependency. Therefore every complete basis contains at
least one useful vector. This statement does not claim that one particular
basis vector persists.

Finally, let `r^2=1 (mod N)` with `r` non-global. Since `N` divides
`(r-1)(r+1)`, `gcd(r-1,N)` cannot be 1 or `N`: either case would force `r` to
be `-1` or `+1`. The same argument applies to `gcd(r+1,N)`. Both terminal gcds
are proper.

## Complete no-advice algorithm corollary

The certified algorithm derives `n` from `N` and sets `B=n^2`. It then runs:

1. the complete trial screen from 2 through `B`, returning any proper divisor;
2. all seeds and all 53 frozen pairs;
3. all 1,378 unordered seed pairs in lexicographic order;
4. one global first-residue rule and complete first-exact-value deduplication;
5. the factor-free exact square-class decoder above;
6. both terminal gcds for every vector in a complete binary kernel basis.

It has 1,431 total pairs. Its full source contains exactly

```text
(n-1) + 2(B+1)[(n-1) + binomial(n-1,2)]
= (n-1) + (B+1)n(n-1)
= 8,348,507 positions.
```

The verified projected dependency persists into that complete source. Every
complete decoder basis must contain a useful class. Testing all basis roots
must expose proper terminal divisors. This certifies success for the supplied
`N` without giving the complete algorithm the prefix length or support.

This section is a proof of what the complete algorithm will find. It is not a
claim that the 8,348,507 positions or the complete decoder were run here.

## Uniform polynomial bit-cost

Let `n` be the bit length and `B=n^2`. The complete source has
`T=(n-1)+(n^2+1)n(n-1)=O(n^4)` positions. Each modular value has at most `n`
bits. Each exact relation value `P=cw` has at most `2n` bits. Global residue
retention and exact-value deduplication handle at most `T` values and therefore
take polynomial bit time and space.

Invertibility is uniform after the trial screen. If that screen continues,
every integer from 2 through `B` is a unit modulo `N`. This includes every seed
and unordered-pair entry. Seed inverses are units. Each final seed-basis block
divides a seed endpoint, so each frozen-pair entry is a unit. Powers and
products of these entries stay units. Thus every inverse requested by the
source exists after the trial branch.

The seed basis starts with `2(n-1)` endpoints. For a termination bound, use
prime factors only as abstract proof tokens. The algorithm never computes
them. The number of tokens with multiplicity is `O(n^2)`. For an item `(x,s)`,
define its cohabitation potential as

```text
sum_j s_j * binomial(Omega(x),2).
```

The initial potential is `O(n^3)`. Exact perfect-power extraction cannot
increase it. Equal merges preserve it. Every unequal gcd split strictly lowers
it because at least one value separates into two nonunit factors. Thus there
are `O(n^3)` unequal splits. Item counting also bounds equal merges and work
pops by `O(n^3)`. Even an ordered scan gives `O(n^6)` seed-basis gcd tests on
`O(n)`-bit integers. Exact perfect-power tests are also polynomial bit time.

Let `m<=T=O(n^4)` be the number of distinct nonunit exact columns. Gcd
refinement starts with `2m=O(n^4)` endpoint entries. The total numeric input
length is

```text
L <= 2mn = O(n^5).
```

One overlap replaces numeric product `xy` by `xy/d` with `d>=2`. Thus the
active numeric product loses at least one bit per refinement. There are at most
`L` refinements and `O(m+L)=O(n^5)` work or stable slots. A direct ordered scan
uses at most `O((m+L)^2)=O(n^10)` gcd queries on `O(n)`-bit values. Each mask
has `m=O(n^4)` bits. The complete mask storage is at most `O(n^9)` bits.

There are at most `O(n^5)` terminal rows and `O(n^4)` columns. Coarse bitset
Gaussian elimination costs `O(rm^2)=O(n^13)` bit operations for `r` rows.
Constructing a complete basis adds at most `O(m^3)=O(n^12)` bit operations.
The basis contains at most `m=O(n^4)` vectors.

One dependency selects at most `m` values. Its exact product has at most
`2nm=O(n^5)` bits. The algorithm performs at most `m` exact products, integer
square roots, modular reductions, and pairs of terminal gcd tests on
polynomial-bit integers. Thus the complete source, complete factor-free
decoder, and all basis-root tests form one uniform polynomial-bit-time
algorithm.

The advised prefix replay is also polynomial, but it is not a step of the
certified complete algorithm. It is used only to prove existence for this
fixed `N`.
