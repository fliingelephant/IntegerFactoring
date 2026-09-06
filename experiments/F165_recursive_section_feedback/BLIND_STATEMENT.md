# F165-R01 blind reconstruction statement

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

Let

\[
n=\left\lceil\log_2(N+1)\right\rceil.
\]

For every unit \(c\) with \(2\le c\le n+1\), let \(w\) be its least positive
inverse modulo \(N\). Add the endpoint presentation \((c,w)\), exact positive
value \(A=cw\), and supplied modular root \(1\).

At every decode stage:

1. Process all endpoint presentations before exact-value deletion.
2. If two occurrences have the same exact \(A\), compare their supplied
   decorated roots. A non-global ratio is an immediate factor certificate.
   Otherwise keep the first exact-value occurrence and retain occurrence and
   layer metadata.
3. Remove exact square and odd-perfect-power redundancy.
4. Repeatedly use integer gcd refinement, with multiplicity, on every retained
   endpoint until the named integer blocks are pairwise coprime.
5. Extract maximal perfect powers so the final positive blocks are pairwise
   coprime nonsquares.
6. Express each retained exact value uniquely as

   \[
   A=s^2\prod_{j:v_j=1}q_j,
   \]

   where \(v\) is its parity column and \(s>0\).
7. Compute a complete binary kernel basis. For each square dependency, compute
   its exact positive square root and then its supplied-root-normalized root
   modulo \(N\). Test both signs by gcd. A root outside global
   \(\{+1,-1\}\) is useful.
8. Select a deterministic first-occurrence column basis by Gaussian
   elimination. Use the largest active row as pivot. Store with each selected
   column its actual decorated lift

   \[
   (v,s^{-1}\bmod N).
   \]

Run exactly two frozen feedback levels. At one level, freeze the selected
basis before scanning. Scan every support-one subset in basis order, followed
by every unordered support-two subset \((i,j)\), \(i<j\), in lexicographic
order.

For a selected subset, multiply the actual decorated lifts. For every block
whose parity appears twice, divide the integer product by that block once.
This gives the actual positive star product \(z\). If \(z\) is not a unit,
the gcd is a factor. Otherwise compute its least positive inverse \(w\)
modulo \(N\), test

\[
\gcd(z-w,N),\qquad \gcd(z+w,N),
\]

and offer the endpoint presentation \((z,w)\), exact value \(zw\), and
supplied root \(1\) to the retained union. Do not let a new record affect the
current frozen scan. Rebuild the complete union decoder only after the level
ends.

Record, for the base and both feedback levels:

- attempted subsets;
- strict new exact values and duplicates;
- proper direct screens;
- rows, columns, rank, nullity, and normalized-root status;
- strict refinements of old named blocks;
- deterministic hashes of the candidate, exact-value, block, and selected
  column sequences.

Every positive certificate must have an \(N\)-only replay.

## Claimed finite result to verify or refute

The corpus SHA-256 is

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

The first claimed level-one block refinements occur at \(N=100440259\):

\[
1291243=23\cdot56141,\qquad
32284369=13\cdot2483413.
\]

The first claimed level-two refinement occurs at \(N=100740469\):

\[
11992913=23\cdot521431.
\]

These are integer-block refinements. They are not factors of \(N\).

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

Return PASS only if the independent replay reproduces the finite counts and
certificates and the fixed-depth theorem is independently proved. Otherwise
return FAIL with the first exact mismatch.

This is finite evidence plus a cost theorem. It is not a density law,
minimum-depth law, all-input success law, or factoring algorithm.
