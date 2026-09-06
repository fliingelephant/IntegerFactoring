# F160 manifest

- Date: 2026-08-11
- Type: proof-only source/decoder candidate
- Computation: none
- Durable ledgers: not edited
- Closest results: P140, P144, F159, with P138/P143 as the section source
- Material difference: a public sign choice eliminates the inert branch for
  every primitive quadratic lift; a P138 square-class hit is therefore
  sufficient for factor-or-double progress
- Jacobi boundary: at even common order, the Jacobi bit detects unequal
  local lift capacity but cannot distinguish both-capable from neither-
  capable; the natural pair of negative-Jacobi discriminants is publicly
  root-equivalent to the original lift problem
- Complexity: deterministic polynomial decoding for one hit; deterministic
  quasipolynomial decoding for a quasipolynomial candidate list
- Missing theorem: a uniform factor-or-section-hit law at every surviving
  even common-order state
- Explicit nonclaim: no all-input hit, hit density, or factoring algorithm
  is proved
- Frozen statement SHA-256:
  `fd232fabd54a66ed03090a3ce4a03905dc1d3e3667b6ba712acee80751751ecc`
- Frozen proof SHA-256:
  `cc18b16e96f8363c0eb71bdb85e840bef9d5d9c7c954d5ec1f0b15875d9b17c7`
- Hostile audit: PASS
- `HOSTILE_AUDIT.md` SHA-256:
  `75b1f930eef9db366bbf8db97c765860673a2b5a6aecd8fe04984c63035d058f`
- Independent statement-only reconstruction: PASS
- `BLIND_RECONSTRUCTION.md` SHA-256:
  `6d709720c97c89c7c3a7176ca0007c407682400bb2ed368418af597f98f85bc5`
- Review qualification: the P138 triple already constructs the missing
  scalar root. Sign normalization removes the externality test; it does not
  manufacture the root or prove a source hit.
