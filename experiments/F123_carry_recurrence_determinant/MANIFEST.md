# F123 Manifest

## Status

**Self-audited candidate.**

This is a retrospective registration. It has not passed the project’s
hostile-audit and proof-blind-reconstruction cadence. It is not promoted to
PROVED.md.

## Registered run

~~~text
python3 experiments/F123_carry_recurrence_determinant/run_verifier.py
~~~

The runner gives each source a 60-second timeout. It verifies the preserved
source hash, writes RUN.log, and writes OUTPUT.json.

## Outcome

- The byte-preserved supplied verifier passed.
- The independent 3,571-case identity sweep passed.
- The sweep found exactly one proper carry-residual gcd for seeds 2 through
  92 on the certificate modulus: seed 68, factor 2,621.
- No failed registered run occurred.

## SHA-256 pins

| File | SHA-256 |
|:---|:---|
| FAILED_RUNS.md | adda50898bc35adf321a879fce4c8728e09868f60bc7ef99cc624e543005d139 |
| OUTPUT.json | e158983c172b148a2c2ba7a61e438d04d42f38a9c1f8d2c7c399889d3b7c77d3 |
| QUESTION.md | 4d81d805875b7db4fc87cccb2c9c8aecdc628d843dc10f8d1060e18dc7c8b569 |
| RESULT.md | 670c5c4560c818ce28dd11be4a22257f3a666f490ec9b01e853882600d7118b5 |
| RUN.log | 77e76896d880d26285a541807554edbc056b8699480c1af109a627d960d4a5e9 |
| SOURCE_PROVENANCE.md | d4a0c6b05f4c2a631765e11314128c5c67bffe0d2cd5658a5301b4ecd7d03c7a |
| run_verifier.py | 21efb783700d9e594f5bb6b753a4ca330522e6b4e9b3e43cb64c473ab50c2a3a |
| verify_gct_carry_obstruction.py | eb18408931a02891b3b7cb27a7e80379f487efc3756fcdff2cc291fc63b9d594 |
| verify_identity_sweep.py | 6ced9203ae8395afeffd5af081c2556b7879ccfa8b9287e14ec8641f5cd43ec4 |

This manifest has no self-hash.

## Exact boundary

- The determinant identity and finite arithmetic are exact candidate claims.
- The 364-position source separation is finite and retrospective.
- No all-input success probability or asymptotic factor correlation is
  claimed.
- The construction is a static scalar-plus-gcd screen.
- No feedback-created block, source transition, or recursive closure is used.
- “GCT-inspired” describes the determinantal analogy only.
