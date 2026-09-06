# F270-D01 static resource estimate

## Immutable workload

- Cases: 188 discovery moduli.
- Rows: 284 original rows per modulus, 53,392 total.
- Maximum singleton tests: 53,392.
- Maximum support-two tests after no peeling:

  ```text
  188 * C(284,2) = 7,554,968.
  ```

- Preferred clean cohort: 125 cases, with maximum

  ```text
  125 * C(284,2) = 5,023,250
  ```

  support-two tests.

Discovery factors have at most 32 bits. Thus every `N` has at most 64 bits,
every canonical row `U<N^2` has at most 128 bits, and one complete 284-row
case has at most 36,352 input bits. The frozen 100,000-bit case cap leaves a
factor greater than two.

## Time

The dominant operations are pairwise gcd refinement of at most 284 short
integers, degree-one peeling, at most 40,186 support-two tests per case, and
binary elimination on at most 284 columns. The exact workload is far below
the previous F268-D04 held-out run, which processed 1,184 larger banks and
1,294,704 pair tests in about 1,082 wall seconds.

No benchmark is used as mathematical evidence. The frozen runner performs a
fresh eight-case preflight on the target host. It multiplies the observed
wall extrapolation by four and refuses the target above 14,400 seconds.

## Memory

At the hard 65,536-block cap, a dense exponent array of 284 unsigned
32-bit entries uses about 71 MiB per active case before container overhead.
Eight simultaneous cap-saturating cases could therefore approach 568 MiB.
Actual 128-bit inputs cannot normally sustain that cap, but the runner still
uses a factor-four live-memory projection and a strict 4-GiB gate.

The program also caps estimated serialized relation payload at 256 MiB and
global output at 512 MiB. Any breach aborts without a mathematical result.

## Disk

The authenticated F268 discovery evidence is about 16 MiB. Row, block,
peeling, case, aggregate, and summary outputs are expected to be below
100 MiB if the cores are small. The hard output gate is 512 MiB. The runner
checks target-host free disk before launch and requires at least 4 GiB.
