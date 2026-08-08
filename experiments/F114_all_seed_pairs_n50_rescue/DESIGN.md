# F114 — all-seed-pair control on the seven 50-bit nulls

Repeat the complete nonadaptive all-seed-pair source from F113 on the seven
remaining 50-bit F112 failures.  The exact source is the frozen initial-basis
layer followed by every unordered pair `2 <= u < v <= n`, with both exponent
trajectories through `n^2` and one retained joint decoder.

The menu is fixed and has `O(n^4)` positions.  The implementation is
factor-assisted.  A positive fixed witness still requires factor-free replay;
a null is evidence only against this exact bounded source.
