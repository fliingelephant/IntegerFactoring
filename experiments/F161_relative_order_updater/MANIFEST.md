# F161 manifest

- Date: 2026-08-11
- Type: proof-only decoder/progress candidate
- Computation: none
- Durable ledgers: not edited
- Closest results: P144/F158 certified common-order lifting and F159 V2
  post-refinement membership screen
- Material difference: scan the relative order of a released unit up to a
  quasipolynomial cap, align all hidden logarithms factor-first, and
  compress every aligned extension to one certified common-order generator
- Exact positive result: a supplied released unit gives a factor, global
  membership, certified multiplicative common-order growth, or a certificate
  that every local relative order exceeds the cap
- Hidden flaw resolved: equal local relative indices do not suffice; hidden
  log mismatch must be tested and gives a factor
- Cyclicity result: after log alignment, the common two-generator
  presentation has order `Me` and is forced to be cyclic in every odd
  prime-power component and globally
- Generator method: an explicit two-by-two Smith word gives a deterministic
  common generator; optional public word sampling succeeds in expected at
  most `log_2(Me)+1` trials
- Discrete-log cost: digit-wise factor-first Pohlig--Hellman uses
  `O(sum v_ell(M)*ell)` tests and never scans `ell^v_ell(M)`
- Complexity: one updater and any sequence of at most `n` successful updates
  have deterministic quasipolynomial bit complexity
- Smoothness: if `M` is supplied `B`-smooth and the returned relative index
  is at most `B`, then `Me` remains supplied `B`-smooth
- Input scope of the decoder theorem: arbitrary odd CRT decompositions,
  including prime powers and more than two distinct primes; powers of two
  can be removed before the call
- Missing theorem: no source guarantees a useful released unit, a bounded
  relative order, or enough successful updates
- Explicit nonclaim: no all-input source law, complete-factorization
  reduction, or quasipolynomial factoring algorithm is proved
- Frozen statement SHA-256:
  `c999958e6b1cce04b7aa4fbf03e7b233a57c4461da66a4ba68c46cf2aaba4a32`
- Frozen proof SHA-256:
  `409bdd11bdff1dc0b571b6169f669186e16b3aac04ad7566a009f14ddeb41a27`
- Review status: candidate; fresh hostile audit and independent
  statement-only reconstruction are still required before promotion
