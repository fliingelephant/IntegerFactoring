# F116 Sage/Pari retry

The first mathematical run timed out in the pure-Python endpoint factorizer
after it completed the registered selection. This retry changes only the
factor-assisted discovery backend.

It independently repeats the exact F116 selection rule. It then runs the
same frozen layer, global residue deduplication, direct screens, online binary
decoder, and lexicographic all-unordered-seed-pair menu. The batch classes are
imported from the pinned independent F115 verifier, which uses Sage/Pari for
endpoint factorization.

The run is sequential. It has a 1,800-second hard timeout and writes a
checkpoint after selection and after each completed case. A null case is a
valid mathematical result and gives output status `FAIL`; an execution error
or timeout is preserved separately.

This remains factor-assisted finite stress evidence. Any positive certificate
still needs an N-only replay. It proves no all-input law or runtime bound.
