# F95 run manifest

## Identity

- Experiment: F95_two_relation_canonical_inverse_cycle
- Purpose: discover or kill, within a fixed finite range, an actual
  two-relation canonical-inverse cycle whose second relation closes
  2-saturation and whose induced exact root factors \(N\).
- Closest prior route: F94 presentation closure. This run differs by asking
  for an explicit arithmetic witness, not another presentation theorem.
- Date: 2026-08-08.
- Durable ledgers edited: none.

## Named artifacts

- Discovery source: search_two_relation_cycle.py
- Timeout runner: run_with_timeout.py
- Captured log: RUN.log
- Machine-readable output: OUTPUT.json
- Human result: RESULT.md

## Command and timeout

The command issued from this directory was

    python3 run_with_timeout.py

The runner invoked the named discovery source as

    python3 search_two_relation_cycle.py --n 2773 --ell 2 \
      --g-min 2 --g-max 2772 --output OUTPUT.json

The runner imposed a hard wall-clock timeout of 120 seconds. The process
finished with exit code zero.

## Exact finite bounds and ordering

- Modulus: \(N=2773\).
- Saturation prime: \(\ell=2\).
- Candidate range: every integer \(g\) with \(2\le g\le N-1=2772\).
- A candidate is retained only when the public test \(\gcd(g,N)=1\) passes
  and its least positive inverse is greater than one.
- Inverse-paired endpoints and any other duplicate exact relation values are
  deduplicated by \(P=gw\). The retained endpoint pair is the
  lexicographically least \((g,w)\), with \(g\le w\).
- Unique relations are sorted by \((P,g,w)\).
- All eligible pairs \(i<j\) are tested in nested-loop order until the first
  witness.
- A pair is eligible only when neither \(P_i\) nor \(P_j\) is an exact
  square. It closes mod \(2\) exactly when \(P_iP_j\) is an exact square.
- A witness additionally requires
  \(1<\gcd(\sqrt{P_iP_j}-1,N)<N\).

The found pair is therefore the smallest witness under this declared
ordering for the complete nontrivial residue range of \(N=2773\). It is not
a claim of minimality across other moduli.

## Public-data discipline

Candidate generation and pair selection use only:

- the public integer \(N\);
- integer range enumeration;
- gcd;
- least positive modular inversion;
- exact multiplication and division;
- integer square root; and
- the final gcd of the induced root.

No hidden factor of \(N\) enters candidate selection. Public trial
factorization of the two witness values \(P_i\) runs only after discovery to
print a gcd-free prime-basis certificate. The final factors \(47\) and
\(59\) are recovered from the public induced-root gcd and then
trial-primality checked.

The full range includes nonunits. The source records and skips them after
their public gcd test so that the relation census can continue. A real
factorer would already stop on those gcds; this experiment deliberately
continues to test the saturation mechanism.

## Outcome counts

- Raw \(g\)-candidates: 2771.
- Units in the range: 2667.
- Nonunits skipped after public gcd: 104.
- Unique canonical relation values: 634.
- Nonsquare relation values: 631.
- Eligible relation pairs tested through the witness: 934.
- Square-product pairs seen through the witness: 1.
- Outcome: witness.
- No fallback modulus scan was needed.

## SHA-256

    f46dfc439a53ecc2a2ed2c7e29d1d96324a97935a88a2781012175d0e1ba4509  search_two_relation_cycle.py
    eeba4263d7793da3b623977d4b64088717660ef63d8c37d968f25a66f97996e0  run_with_timeout.py
    f9fb5bdf181a0abe74a0ee745e39c001456b43a2287117b9fb8955686db66145  RUN.log
    9df2c3d924bcbb5c94c59613758431c91368c6b88f6ca95e11039251a6cd67f0  OUTPUT.json

## Evidence limit

This is a fixed finite discovery computation. It proves the displayed
integer certificate once its arithmetic is checked. It does not prove a
frequency law, a polynomial-time source of the second relation, or an
all-input factoring algorithm.
