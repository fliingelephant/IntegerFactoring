# F65-D01 preregistration

- Family: F26/F62, cross-relation block selection.
- Run: F65-D01.
- Status: preregistered and not yet launched.
- Source: `scripts/F65_D01_scan.py`.
- Runner: `run_F65_D01.sh`.
- Command from the workspace root:
  `zsh experiments/F65_sparse_block_selector_scan/run_F65_D01.sh`.
- Declared timeout: 300 seconds, enforced by
  `/opt/homebrew/bin/timeout 300s`.
- Runtime: `/opt/homebrew/bin/python3`.
- Log: `logs/F65-D01.log`.
- Output: `output/F65-D01.json`.

## Exact finite question

Replay the exact deterministic-offset source schedule used by F59-D02. For
each target factor bit count in `10, 14, 18, 22`, let (p) be the first prime
at least (2^b). For each ratio `21/20`, `4/3`, and `7/4`, let (q) be the
first prime at least both (p+2) and the ceiling of the ratio times (p).
Set (N=pq). The retained factors are finite ground-truth labels only.

For (n=N.\mathrm{bit\_length}()), use starts (N-c) for
(c=1,\ldots,n), and follow at most (n) canonical inverse-quotient steps.
Record every direct nonunit event. Analyze both the full raw relation
multiset and the list that retains only the first nonzero relation for each
quotient.

Refine all public endpoints into pairwise-coprime gcd-free blocks using only
integer gcd and exact division. Reconstruct each endpoint from these blocks
and retain its full exponent budget. Do not prime-factor a block.

For each transcript variant, scan four polynomial explicit menus:

1. every current block;
2. every legal product of two distinct blocks below (N), plus (q_i^2<N)
   when two occurrences are available;
3. every legal power (q_i^e<N) within the retained exponent budget; and
4. every signed product (q_i^{\pm1}q_j^{\pm1}\bmod N) on two distinct
   blocks, including signed single blocks.

For every unique residue, test both `gcd(r-1,N)` and `gcd(r+1,N)`, and record
whether it is a non-global square root of one. The signed menu is a public
residue selector, not legal divisor feedback, and does not use F62's quotient
formula.

## Decision rule and scope

- A first hit is a discovery trigger. Preserve its exact block/exponent
  certificate and determine whether the source had already factored directly.
- A hit on an input with no direct source event shows finite selector gain.
- A miss kills only the exact menu and transcript on that exact input. It
  does not kill larger exponents, support above two, different sources, or
  more feedback rounds.
- Every result is finite evidence. It cannot prove an all-input probability,
  an asymptotic obstruction, or polynomial-time factoring.

Preregistered source SHA-256:
`c7810ba32ce5d359530bf865252ee4446d4b95c29047e6e43ecbe03581c385ba`.

Preregistered runner SHA-256:
`82d204d8d2c69b43011aa020a843feefdec081d02cfd3e2ab141c0dcbf58bd15`.

## Outcome

- Exit status: 0.
- Source elapsed time: 216.68114329200034 seconds.
- Source and runner hashes matched the preregistration.
- Log SHA-256:
  `5cf9dcb382afa5ca186ccd45103467d47d1585aedb72c9b4a6ba890c5b5c058c`.
- Output SHA-256:
  `0d41c802e316689ea0617820535616dec55d5f331155ffbb55dcdb5599f71309`.

The raw and quotient-unique variants gave the same input-level result. A
single block and every available power of one block gave no hit. Legal
positive block pairs hit 10 of 12 inputs, including eight of the ten inputs
with no direct source event. Signed block pairs hit all 12 inputs, including
all ten with no direct source event. F65-A01 validated every stored positive
certificate.

The menus were large relative to these finite inputs. The signed raw menu
tested 40,456,689 distinct residues across the 12 inputs. At 45 input bits,
the pair-menu size is already comparable to the square-root scale. These hits
therefore do not establish factor bias or predict asymptotic success.
