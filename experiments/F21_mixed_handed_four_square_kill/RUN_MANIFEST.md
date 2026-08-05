# Run manifests

## F14-M01 — excluded

- Family: `F14`, Hurwitz one-sided gcds.
- Disposition: **non-authoritative/excluded**. The run occurred before its
  canonical computation-ledger row existed. Its source, output, and diagnostic
  log are preserved as provenance, but no claim relies on it.
- Purpose: finite discovery for same-source mixed-handed tests after an explicit lexicographic normalization of the right- and left-gcd generators.
- Source: `scripts/F14_M01_exact_sections.py`.
- Runner: CPython 3, standard library only.
- Inputs: distinct odd semiprimes `15 21 33 35 39 55 77 91 143 187 221 323 391 437`.
- Hard timeout: 120 seconds.
- Log: `logs/F14_M01.log`.
- Structured output: `output/F14_M01.json`.
- Interpretation: finite discovery/counterexample evidence only; it cannot prove an asymptotic probability claim.

## F14-M02 — completed

- Family: `F14`, Hurwitz one-sided gcds.
- Purpose: authoritative finite certificate for the residual-compatible
  `N=91, R=1` failure of the 12-element mixed-handed unit menu, plus finite
  consistency checks of the projective/coefficient dictionary.
- Driver: `scripts/F14_M02_exact_sections.py`.
- Enumeration dependency: `scripts/F14_M01_exact_sections.py`; the driver
  records both source hashes.
- Runner: CPython 3, standard library only.
- Inputs: distinct odd semiprimes `15 21 33 35 39 55 77 91 143 187 221 323 391 437`.
- Hard timeout: 120 seconds.
- Working directory: `/Users/zhou/autoresearch/IntegerFactoring`.
- Exact command:

      /opt/homebrew/bin/timeout 120s python3 experiments/F21_mixed_handed_four_square_kill/scripts/F14_M02_exact_sections.py --output experiments/F21_mixed_handed_four_square_kill/output/F14_M02.json --inputs 15 21 33 35 39 55 77 91 143 187 221 323 391 437 > experiments/F21_mixed_handed_four_square_kill/logs/F14_M02.log 2>&1

- Log: `logs/F14_M02.log`.
- Structured output: `output/F14_M02.json`.
- Driver SHA-256: `c37e8a5d461dfa79c14a89e99b655f13613aec665333bb0481bf1c43a71ad03c`.
- Enumeration-dependency SHA-256: `4002517d33241a8ebe3dddb2ed7e99dfe965ad8b83e8d79aad08d85d443ab9ef`.
- Output SHA-256: `b4b44bb61eeaae72a4e4fc50b66d4139f13f9220956a525dd2abfe0342eba211`.
- Exit status: 0.
- Observed wall duration: approximately 30.0 seconds, below the 120-second
  hard timeout.
- Interpretation: finite certificate only; it cannot prove an asymptotic
  probability claim.
