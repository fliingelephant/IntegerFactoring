# F09 hostile-audit computation manifest

## F09-PA-A01

- Family: `F09_phase_audit`
- Purpose: independently exhaust the cubic phase fibers, the explicit collision, all roots of `Phi_3` modulo 91 and their difference gcds, and the product of conjugate cubic residue symbols above 7 and 13.
- Source: `audit_cubic_carrier.sage`
- Command: `DOT_SAGE=/tmp/F09_phase_audit_sage timeout 60s sage audit_cubic_carrier.sage output/A01.json`
- Timeout: 60 seconds
- Log: `logs/A01.log`
- Output: `output/A01.json`
- Status: failed only at JSON serialization after all assertions passed because a nested dictionary retained Sage-integer keys. The traceback and partial invalid output are retained.

## F09-PA-A02

- Family: `F09_phase_audit`
- Purpose: repeat A01 after converting every nested JSON key to a string.
- Source: `audit_cubic_carrier.sage`
- Command: `DOT_SAGE=/tmp/F09_phase_audit_sage timeout 60s sage audit_cubic_carrier.sage output/A02.json`
- Timeout: 60 seconds
- Log: `logs/A02.log`
- Output: `output/A02.json`
- Status: passed. Every one of the nine phase pairs occurs eight times, each diagonal-sum fiber has 24 units, `15/18=16` has phases `(0,1)-(1,0)=(2,1)`, the four roots and six gcds match R04, and the conjugate-symbol exponent sums vanish for every nonzero numerator modulo 7 and 13.
