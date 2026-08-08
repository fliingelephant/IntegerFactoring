# F104 — all-input degree-one peeling question

## Question

For the exact N-only F98 one-round rule, must lossless degree-one peeling
leave a rank-deficient core on every stable trial-hard distinct odd
semiprime that reaches the end of the round?

The rule is pinned to the public F98 source. It uses:

- `n = N.bit_length()` and `B = n^2`;
- trial gcds through `B`;
- initial seeds 2 through `n`;
- the first at most `n` public active pairs;
- both public trajectories for every exponent 0 through `B`;
- residue deduplication during generation;
- exact-value deduplication before decoding; and
- the factor-free P66 pairwise-coprime parity rows.

## Definitions

A scanned input is a distinct odd semiprime `N = p*q` with proven prime
factors. It is trial-hard when `p,q > n^2`. It is P98-stable when, for

```text
g = gcd(p-1,q-1), A = (p-1)/g, B = (q-1)/g,
```

we have `gcd(A*B,N-1) = 1`.

A completed input also survives the initial public decoder and every direct
`gcd(c-inv(c),N)` and `gcd(c+inv(c),N)` screen through the end of round one.

Degree-one peeling repeatedly deletes the unique column incident to an
active row of degree one. The core is the remaining column set.

The outcome labels are separate:

- `core_nonempty`: at least one column survives peeling;
- `core_rank_deficient`: core nullity is positive;
- `non_global_basis_root`: the public kernel basis contains a root other
  than `+1` or `-1` modulo `N`.

An empty core and a nonempty independent core both refute the proposed
universal rank-defect conclusion. A nonempty core alone does not imply a
dependency. A dependency alone does not imply a non-global root.

## Method

The scan enumerates a named, deterministic bounded family of prime pairs.
Factor data is used only to select and certify stable trial-hard inputs. The
one-round replay itself receives only `N` and calls the pinned public F98
arithmetic primitives.

There are two execution tiers.

1. The acceptance tier reconstructs the exact-value-deduplicated,
   factor-free P66 matrix. It computes full and core rank over `GF(2)`, peels
   in both forward and reverse degree-one orders, and checks that nullity is
   preserved.
2. The candidate tier keeps the pinned N-only generation and every public
   screen unchanged. It replaces only the terminal P66 rows with distinct
   nonzero hidden prime-parity masks. This tier can use the certified factors
   of endpoint values. It is faster, but it cannot accept a counterexample.

The candidate-tier replacement is exact for rank and peeling. For each
prime, refinement preserves its parity-incidence mask. In a terminal
pairwise-coprime P66 basis, each prime occurs in one block. A block is a
nonsquare exactly when at least one prime in it has a nonzero parity mask.
Thus the distinct nonzero terminal P66 row masks and hidden prime-parity row
masks are the same. Duplicate P66 rows do not change rank or the terminal
column set under degree-one peeling.

Each scan stops at the first empty or independent core. Any candidate from
the fast tier must then pass a separate factor-free P66 replay by the pinned
N-only routine.

## Falsifiers

The run fails if the pinned F98 source hash changes, if the fast source loses
its pin to the exact replay source, if a purported input is not
prime-factor-certified, stable, and trial-hard, if the public replay does
not complete, if the two peel orders disagree, or if peeling changes
nullity. A fast-tier candidate also fails unless the factor-free P66 replay
accepts it.

## Scope

One counterexample refutes only the universal claim that this one-round
peel must leave a rank-deficient core. It does not refute later rounds, give
a density law, or prove that a rank-deficient core yields a non-global root.
