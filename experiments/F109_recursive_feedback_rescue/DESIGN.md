# F109 — recursive rescue versus a nonadaptive small-pair source

## Question

Can the declared multi-round C2T feedback rule rescue stable trial-hard inputs
whose complete first round has relations but only global roots?  If it can,
does the success require a block created by feedback, or does one pair of
small initial seeds already supply the decisive batch?

## Cases

Use seven completed F104 inputs.  Each first-round core is rank deficient and
its full kernel basis has only the global root `+1`.

For each input:

1. run the pinned full factor-assisted C2T rule for at most `n` rounds;
2. record the round, final active pair, and factor channel;
3. start again from the initial seeds `2..n` and expand only that final active
   pair through both declared trajectories and exponents `0..n^2`;
4. retain every distinct residue, apply every direct screen, and run the same
   complete parity decoder online.

Endpoint factorization is used only to accelerate discovery.  The generated
residues, direct screens, gcd-free block basis, parity kernel, and root tests
all have factor-free polynomial-time equivalents.  Any promoted fixed witness
requires a separate N-only replay.

## Falsifiers

The recursive-rescue observation fails if full C2T does not factor a pinned
case.  The feedback-necessity interpretation fails on a case if its final pair
uses only initial seed integers and the isolated pair replay already factors.

## Scope

This is a bounded mechanism comparison.  It gives no all-input theorem and no
frequency law.  A successful isolated pair does not prove that scanning all
small pairs works on every input; it only shows that the fixed recursive
witness did not require a feedback-created block.
