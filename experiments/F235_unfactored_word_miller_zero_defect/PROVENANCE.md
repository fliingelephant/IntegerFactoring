# F235 provenance

Closest prior route: P202/F231 requires a completely factored word and uses
factor-first stripping to turn global returns into factors or certified
common orders.  F235 differs materially because it uses an arbitrary
unfactored word only as a direct-return exponent and applies a verified
Miller square chain after a global return.  It therefore needs neither the
factorization of the word nor the recursive factorization of `H`.

P160--P164 discussed unfactored annihilators such as `N^k-1` but rejected
them as exact common-order certificates.  F235 does not treat them as
certificates.  It uses their divisibility only to saturate one residual and
returns solely gcd-verified factors.

No computation was used.
