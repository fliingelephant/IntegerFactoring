# F10-autkill run manifest

## Setup probe (not evidence)

Before this family directory existed, the agent ran `command -v timeout; command -v gtimeout; python3 -c 'import sympy; print(sympy.__version__)'` to check tool availability. The timeout executables were present and the SymPy import failed. This was an environment check, used for no mathematical claim. It is disclosed because the task requires every computational attempt to be recorded; it was not a compliant named-source run and is disqualified as evidence.

The separate command `sage --version` confirmed SageMath 10.9. It was also only an environment check and supports no mathematical claim.

## R01 — symbolic equations and exhaustive N=15 cubic audit

- Family ID: `F10-autkill`
- Named source: `experiments/F10_autkill/cubic_automorphism_analysis.sage`
- Command: `/opt/homebrew/bin/timeout 60s sage experiments/F10_autkill/cubic_automorphism_analysis.sage > experiments/F10_autkill/logs/R01.log 2>&1`
- Timeout: 60 seconds
- Log: `experiments/F10_autkill/logs/R01.log`
- Output: `experiments/F10_autkill/output/R01.json`
- Purpose: derive the coefficient equations symbolically, find the first squarefree cubic over `Z/15Z` with local types `(12)` modulo 3 and `(3)` modulo 5, and exhaustively enumerate all `15^3` possible images of `x` to verify the local/global automorphism groups and gcd certificates.
- Result: failed before source execution because Sage attempted to create cache files below the sandbox-inaccessible `~/.sage`; no output artifact was produced and this run supports no claim.

## R02 — sandbox-compatible rerun

- Family ID: `F10-autkill`
- Named source: `experiments/F10_autkill/cubic_automorphism_analysis.sage`
- Command: `DOT_SAGE=/private/tmp/f10_autkill_sage /opt/homebrew/bin/timeout 60s sage experiments/F10_autkill/cubic_automorphism_analysis.sage > experiments/F10_autkill/logs/R02.log 2>&1`
- Timeout: 60 seconds
- Log: `experiments/F10_autkill/logs/R02.log`
- Output: `experiments/F10_autkill/output/R02.json`
- Purpose: identical to R01, with Sage's cache redirected to a sandbox-writable task-specific directory.
- Result: the exhaustive search and symbolic derivation completed, but JSON serialization failed on Sage integers. No output artifact was produced and this run supports no claim.

## R03 — JSON-safe rerun

- Family ID: `F10-autkill`
- Named source: `experiments/F10_autkill/cubic_automorphism_analysis.sage`
- Command: `DOT_SAGE=/private/tmp/f10_autkill_sage /opt/homebrew/bin/timeout 60s sage experiments/F10_autkill/cubic_automorphism_analysis.sage > experiments/F10_autkill/logs/R03.log 2>&1`
- Timeout: 60 seconds
- Log: `experiments/F10_autkill/logs/R03.log`
- Output: `experiments/F10_autkill/output/R03.json`
- Purpose: identical to R02, adding JSON conversion for Sage integers.
- Result: passed. It found `f=x^3+x+1` over `Z/15Z`, with local types `(12)` modulo 3 and `(3)` modulo 5, and exhaustively found exactly `2*3=6` global automorphisms among `15^3=3375` image tuples. The order-2 and order-3 selective maps each expose a proper gcd.

## R04 — characteristic-greater-than-3 example

- Family ID: `F10-autkill`
- Named source: `experiments/F10_autkill/cubic_automorphism_analysis.sage`
- Command: `DOT_SAGE=/private/tmp/f10_autkill_sage /opt/homebrew/bin/timeout 60s sage experiments/F10_autkill/cubic_automorphism_analysis.sage > experiments/F10_autkill/logs/R04.log 2>&1`
- Timeout: 60 seconds
- Log: `experiments/F10_autkill/logs/R04.log`
- Output: `experiments/F10_autkill/output/R04.json`
- Purpose: repeat the exhaustive audit for the first `(12)/(3)` cubic over `Z/35Z`, so the order-2 and order-3 group schemes are away from characteristics 2 and 3.
- Result: passed. It found `f=x^3+2` over `Z/35Z`; the local groups have orders 2 and 3, exactly six global automorphisms occur among `35^3=42875` possible image tuples, and the two selective order-3 maps are `x -> 11x` and `x -> 16x`, with `gcd(11-1,35)=gcd(16-1,35)=5`.

## R05 — parameterized reproduction of the N=15 example

- Family ID: `F10-autkill`
- Named source: `experiments/F10_autkill/cubic_automorphism_analysis.sage`
- Command: `DOT_SAGE=/private/tmp/f10_autkill_sage /opt/homebrew/bin/timeout 60s sage experiments/F10_autkill/cubic_automorphism_analysis.sage --run-id R05 --modulus 15 --p 3 --q 5 > experiments/F10_autkill/logs/R05.log 2>&1`
- Timeout: 60 seconds
- Log: `experiments/F10_autkill/logs/R05.log`
- Output: `experiments/F10_autkill/output/R05.json`
- Purpose: make the N=15 audit exactly reproducible from the final parameterized source.
- Result: passed and reproduced the R03 coefficients, local types, six automorphisms, orders, and gcd certificates.

## R06 — parameterized reproduction of the N=35 example

- Family ID: `F10-autkill`
- Named source: `experiments/F10_autkill/cubic_automorphism_analysis.sage`
- Command: `DOT_SAGE=/private/tmp/f10_autkill_sage /opt/homebrew/bin/timeout 60s sage experiments/F10_autkill/cubic_automorphism_analysis.sage --run-id R06 --modulus 35 --p 5 --q 7 > experiments/F10_autkill/logs/R06.log 2>&1`
- Timeout: 60 seconds
- Log: `experiments/F10_autkill/logs/R06.log`
- Output: `experiments/F10_autkill/output/R06.json`
- Purpose: make the characteristic-greater-than-3 audit exactly reproducible from the final parameterized source.
- Result: passed and reproduced the R04 coefficients, local types, six automorphisms, orders, and gcd certificates.

## Post-run artifact inspection

The read-only command `cat experiments/F10_autkill/logs/R05.log; cat experiments/F10_autkill/logs/R06.log; shasum -a 256 experiments/F10_autkill/output/R05.json experiments/F10_autkill/output/R06.json` checked that both final runs reported success and recorded artifact hashes. It was not a mathematical search. The hashes were `bd22d06705a965f7e812d7322ec34e6961501f5ac6a202fff3881734330652b1` for R05 and `eb75cfe0e0f2327476d35508eaa09ba652a4215e926dbff75d5311683469ce6c` for R06.
