# F65-A01 preregistration

- Family: F26/F62.
- Run: F65-A01.
- Status: preregistered and not yet launched.
- Source: `scripts/F65_A01_audit.py`.
- Runner: `run_F65_A01.sh`.
- Timeout: 60 seconds.
- Log: `logs/F65-A01.log`.
- Output: `output/F65-A01.json`.

The audit pins the D01 source, runner, log, and output hashes. It parses all
12 records, checks block/budget shape and unit status, validates every stored
positive certificate from its declared block indices and exponents, recomputes
its gcd result, and produces cross-input totals. It does not re-enumerate a
menu. Therefore it independently certifies positive witnesses and artifact
consistency, but not stored null results.

Preregistered source SHA-256:
`9c5261efa88c394eda98644d504d2dacda0efe6efb8cf91140d8f32d55e5f602`.

Preregistered runner SHA-256:
`348f56323a8fd8f4414c6e2bd7900e178b38dea2a0fb1b7f744b33caf2cd156e`.

## Outcome

- Exit status: 0.
- Every assertion passed.
- Log SHA-256:
  `71f92dfdf74de19e07b1bc99319abae2ad0ed7a886beee8dbaa7c1718890bcbf`.
- Output SHA-256:
  `b0af62734d9dc447b9fe05ff52797023a386344a3e8a6cdaa38b160f064e1ff5`.

For both the raw and quotient-unique transcript variants, the audit confirmed
zero stored single-block and single-power first-hit certificates, ten
legal-pair input hits, and twelve signed-pair input hits. It independently
validated every stored first-hit certificate. D01 stores aggregate hit counts,
not every positive certificate. Those aggregate counts and all stored
null-menu claims were not independently re-enumerated.
