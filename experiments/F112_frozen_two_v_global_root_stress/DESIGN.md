# F112 — stress test of the frozen `(2,v)` source

## Question

Does the narrowed F110 source rescue only its seven discovery inputs, or does
it also rescue the complete set of larger first-round global-root cases found
by F104?

## Frozen source

For each input, use only this public source:

1. initial residues `2..n`;
2. the complete frozen first layer selected from the factor-free seed endpoint
   basis;
3. the fixed appended pairs `(2,v)` for `3 <= v <= n`, in increasing order;
4. both canonical exponent trajectories through `0..n^2`;
5. one joint decoder across both layers.

No generated relation changes the source menu.

## Corpus

Read every completed F104 scan output.  Select each distinct stable trial-hard
semiprime whose complete first round is rank deficient and whose entire
reported kernel basis has only the global root `+1`.  Exclude the interrupted
wide scan.  Sort by `N` and test every distinct selected input.

The endpoint decoder is factor-assisted for speed.  The source itself is
public and polynomial.  Fixed promotion requires a factor-free replay.

## Falsifier

One completed `(2,v)` menu with no factor refutes the empirical all-corpus
claim.  A parity success is counted as cross-layer only when its exact
dependency contains at least one frozen-layer relation and at least one
appended relation.

## Scope

This is a finite adversarial corpus test.  Even a perfect result supplies no
all-input theorem, success probability, or independence claim.
