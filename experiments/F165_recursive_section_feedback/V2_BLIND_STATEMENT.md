# F165-R01 V2 blind reconstruction statement

## Required independence

Use this file as the only F165 mathematical source before the replay freezes.
Do not read any other file in this directory. Do not import an F165 program.
Implement the workflow independently. Before the mathematical run, freeze the
new source, runner, registration, timeout, log path, and output path. The root
agent must add the run to `REGISTRY.md`.

The reconstruction has two parts:

1. Independently replay the finite depth-two experiment.
2. Independently prove or refute the fixed-depth cost theorem in this file.

## Public finite workflow

Construct the first 64 lexicographic pairs of distinct rational primes
\((p,q)\) in \([10000,20000]\) with \(p<q<2p\). For each pair set \(N=pq\).
The public analysis function receives only \(N\). The factors can be used only
after the public result is complete, to classify a returned divisor.

For the corpus hash, flatten the ordered pairs as

\[
p_0,q_0,p_1,q_1,\ldots,p_{63},q_{63}.
\]

Encode each nonnegative integer in its shortest unsigned big-endian byte
string. Prefix it with its byte length as an eight-byte big-endian integer.
Hash the concatenation, followed by the element count \(128\) as one final
eight-byte big-endian integer.

Let

\[
n=\left\lceil\log_2(N+1)\right\rceil.
\]

For every unit \(c\) with \(2\le c\le n+1\), let \(w\) be its least positive
inverse modulo \(N\). Offer the exact positive value \(A=cw\) with supplied
modular root \(1\).

The retained relation ledger keeps only the first occurrence of each exact
integer \(A\). Before deleting an equal value, compare the two supplied
decorated roots. A non-global ratio is an immediate factor certificate.
Otherwise update only its occurrence count and layer metadata.

This experiment does **not** retain \((c,w)\) or later \((z,w)\) as two
separate refinement inputs. At every decode, pass each distinct exact value
\(A>1\) as one labelled positive integer to the factor-free parity decoder.

The decoder must:

1. remove exact square and odd-perfect-power redundancy;
2. repeatedly use multiplicity-aware integer gcd refinement on the distinct
   labelled exact values;
3. extract maximal perfect powers so the final positive blocks \(q_j\) are
   pairwise coprime nonsquares;
4. express every retained value uniquely as

   \[
   A=s^2\prod_{j:v_j=1}q_j;
   \]

5. compute a complete binary kernel basis;
6. for each square dependency, compute its exact positive square root and
   supplied-root-normalized residue, then test both signs by gcd;
7. select a deterministic first-occurrence column basis by Gaussian
   elimination, using the largest active row as pivot;
8. store with each selected column its actual decorated lift

   \[
   (v,s^{-1}\bmod N).
   \]

Run exactly two frozen feedback levels. At one level, freeze the selected
basis before scanning. Scan every support-one subset in basis order, followed
by every unordered support-two subset \((i,j)\), \(i<j\), in lexicographic
order.

For a selected subset, multiply the actual decorated lifts. For every parity
block present in both support-two columns, divide the modular product by that
block once. This gives one unit residue \(z\). Compute its least positive
inverse \(w\) modulo \(N\), test

\[
\gcd(z-w,N),\qquad \gcd(z+w,N),
\]

and offer only the exact positive value \(A=zw\), with supplied root \(1\),
to the retained relation ledger. Do not let a new record affect the current
frozen scan. Rebuild the complete union decoder only after the level ends.

Record, for the base and both feedback levels:

- attempted subsets;
- strict new exact values and duplicates;
- proper direct screens;
- rows, columns, rank, nullity, and normalized-root status;
- preservation or strict splitting of old exact-value parity blocks;
- deterministic hashes of candidate, exact-value, block, and selected-column
  sequences.

Every positive certificate must have an \(N\)-only replay.

## Claimed finite result to verify or refute

The corpus SHA-256 under the encoding above is

`bd1d2987d2eaa6d3cfda3fceea72fbd471592a659137df26ae05a3d86cec7fb3`.

The base decoder is null on 63 of the 64 inputs. All 63 remain null after
level one and level two. Neither feedback level has a proper direct screen.
There is no level-two-only factor certificate.

Aggregate feedback accounting:

| Quantity | Level 1 | Level 2 |
|---|---:|---:|
| attempted subsets | 5,020 | 8,896 |
| strict new exact values | 315 | 310 |
| duplicate exact values | 4,705 | 8,586 |
| inputs with positive rank gain | 63 | 57 |
| total rank gain | 251 | 310 |
| inputs with strict old-block splits | 42 | 38 |
| total strictly split old blocks | 67 | 69 |
| proper direct candidates | 0 | 0 |
| duplicate-root splits | 0 | 0 |

The only useful root is already present at the base for

\[
N=100160063=10007\cdot10009,
\qquad
N+1=10008^2.
\]

It gives

\[
\gcd(10008-1,N)=10007,\qquad
\gcd(10008+1,N)=10009.
\]

The first claimed level-one exact-value block refinements occur at
\(N=100440259\):

\[
1291243=23\cdot56141,\qquad
32284369=13\cdot2483413.
\]

The first claimed level-two refinement occurs at \(N=100740469\):

\[
11992913=23\cdot521431.
\]

These are factor-free blocks inside exact relation values. They are not
factors of \(N\).

## Fixed-depth cost theorem

Let \(L=\lceil\log_2(n+1)\rceil\). Suppose the explicit base transcript has
quasipolynomial total bit length and at most

\[
R_0\le 2^{C L^a}
\]

records. At layer \(h\), let the retained union have \(R_h\) records and
parity rank \(r_h\le R_h\). Enumerate every nonempty selected-basis subset of
support at most

\[
D\le L^b,
\]

and retain at most one canonical exact record per attempt.

Claim: for every fixed integer \(H\ge0\), generation, retention, complete
factor-free refinement, and full decoding through layer \(H\) use

\[
2^{L^{O_H(1)}}
\]

bit operations and space.

The claim does not give a uniform quasipolynomial bound when \(H\) grows with
\(n\). It gives no success theorem.

## Required verdict and scope

Return PASS only if the independent replay reproduces the finite counts,
sequence hashes, and certificates and the fixed-depth theorem is independently
proved. Otherwise return FAIL with the first exact mismatch.

This is finite evidence for an exact-value relation decoder plus a cost
theorem. It is not evidence for a presentation-complete endpoint grammar.
It is not a density law, minimum-depth law, all-input success law, or
factoring algorithm.
