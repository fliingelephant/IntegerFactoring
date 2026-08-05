# F09 computation manifest

## F09-R01

- Family: `F09_phasekill`
- Purpose: exhaustively enumerate local cubic-character pairs and global-product fibers for `N=7*13`, and verify that all factor-symmetric scalar homomorphisms span a one-dimensional subspace.
- Source: `enumerate_cubic_diagonal.sage`
- Command: `timeout 60s sage enumerate_cubic_diagonal.sage output/F09-R01.json`
- Timeout: 60 seconds
- Log: `logs/F09-R01.log`
- Output: `output/F09-R01.json`
- Status: failed before script execution because Sage attempted to write its cache under the sandboxed home directory; retained in `logs/F09-R01.log`.

## F09-R02

- Family: `F09_phasekill`
- Purpose: repeat R01 with Sage's writable state redirected to `/tmp/F09_phasekill_sage`.
- Source: `enumerate_cubic_diagonal.sage`
- Command: `DOT_SAGE=/tmp/F09_phasekill_sage timeout 60s sage enumerate_cubic_diagonal.sage output/F09-R02.json`
- Timeout: 60 seconds
- Log: `logs/F09-R02.log`
- Output: `output/F09-R02.json`
- Status: failed after exhaustive enumeration at JSON serialization because Sage integers were not converted to Python integers; retained in `logs/F09-R02.log`.

## F09-R03

- Family: `F09_phasekill`
- Purpose: repeat R02 after converting top-level Sage integer fields to JSON-safe Python integers.
- Source: `enumerate_cubic_diagonal.sage`
- Command: `DOT_SAGE=/tmp/F09_phasekill_sage timeout 60s sage enumerate_cubic_diagonal.sage output/F09-R03.json`
- Timeout: 60 seconds
- Log: `logs/F09-R03.log`
- Output: `output/F09-R03.json`
- Status: passed. All nine local phase pairs occur; each global-product fiber has 24 units; `a=15` has pair `(0,1)` and `a=18` has `(1,0)` but both expose global exponent `1`; the span of all swap-invariant scalar homomorphisms has rank one.

## F09-R04

- Family: `F09_phasekill`
- Purpose: repeat R03 while also enumerating every root of `Phi_3(X)=X^2+X+1` modulo 91, its two CRT components, its global conjugate, and gcds of differences between distinct roots.
- Source: `enumerate_cubic_diagonal.sage`
- Command: `DOT_SAGE=/tmp/F09_phasekill_sage timeout 60s sage enumerate_cubic_diagonal.sage output/F09-R04.json`
- Timeout: 60 seconds
- Log: `logs/F09-R04.log`
- Output: `output/F09-R04.json`
- Status: passed. There are four roots, with CRT choices `(2,9)`, `(2,3)`, `(4,9)`, `(4,3)`. The two globally conjugate pairs have gcd-one differences, while each mixed-orientation pair has difference gcd 7 or 13 with 91.
