# F65-D02 preregistration

- Family: F26/F62.
- Run: F65-D02.
- Status: preregistered and not yet launched.
- Source: `scripts/F65_D02_larger.py`.
- Shared implementation dependency: `scripts/F65_D01_scan.py`.
- Runner: `run_F65_D02.sh`.
- Timeout: 300 seconds.
- Log: `logs/F65-D02.log`.
- Output: `output/F65-D02.json`.

## Exact finite question

Use one larger deterministic input. Let (p) be the first prime at least
(2^{30}), let (q) be the first prime at least both (p+2) and
(\lceil4p/3\rceil), and put (N=pq). Replay the same deterministic-offset
source and exact quotient-unique block refinement as F65-D01.

Scan the same four menus: blocks, legal block pairs, available single-block
powers, and signed block pairs. Record every count and the first exact hit.
The factors are ground-truth labels only and are not used by the source or
selector.

The purpose is to move beyond the finite crossover where an
(O(n^4))-scale pair menu is comparable to (\sqrt N). A hit is a discovery
trigger. A miss kills only this exact 61-bit input, transcript, and menu. It
does not prove an asymptotic obstruction.

Preregistered source SHA-256:
`c8153e3a8ab10349c97f1e0fd724fbc17bb36a6013e4416b7cc5150b97cca2bd`.

Preregistered shared dependency SHA-256:
`c7810ba32ce5d359530bf865252ee4446d4b95c29047e6e43ecbe03581c385ba`.

Preregistered runner SHA-256:
`b39ac2b1c7403f06eaebc4a8c5677d54d974a610bd87a05e18684d562b663ebe`.

## Outcome

- Exit status: 0.
- Source elapsed time: 211.9324433340007 seconds.
- Input: `N=1537228689631084579=1073741827*1431655777`, 61 bits.
- Raw relations: 2,662; quotient-unique relations: 2,247.
- Gcd-free blocks: 4,485.
- Direct source events: zero.
- Current-block candidates: 4,485; hits: zero.
- Available single-block powers: 6,237; hits: zero.
- Legal block-pair candidates: 2,942,006; hits: zero.
- Signed block-pair residues: 39,956,681; hits: zero.
- Log SHA-256:
  `2e51413bc2b5c3365d88e22193793cd20abe5e2974b3e55d2108d97f3f398844`.
- Output SHA-256:
  `9fb849478a76928dc317ef87000d709f937c84c2b79ba1fc662e188a282a8a91`.

This is a finite counterexample to the exact source and four menus on the
declared input, subject to the pending hostile source-proof audit. It does not
refute support above two, mixed higher exponents, a different transcript, or
later feedback rounds.
