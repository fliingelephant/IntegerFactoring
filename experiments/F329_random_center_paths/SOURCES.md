# F329 retained sources

- `experiments/F327_random_pairing_paths/EXPERIMENT_DESIGN.md`, SHA-256
  `65f7e71a753881719059a992555af019b94770a443813e87a2599ffb1c0093af`.
- Research record `P247`, read through the repository `research show` command.
  It supplies the exact lazy-uniform-matching survival, capped-mean, endpoint,
  and static symmetric-screen laws.
- `experiments/F326_direct_gauss_pairing/direct_gauss_pairing.py`, frozen
  SHA-256
  `7829cc45822021c64c42842a2c938b15c52df85e30ae694efcdd4171c5012f73`.
  F329 imports `GaussPairing`, `brute_domain`, and `jacobi` unchanged.
- `experiments/F328_capped_rabin_paths/moduli.json`, frozen SHA-256
  `acf09b285c57c39cfcb93d3cd77addce909498e224955fd0ec9d2e4d86ee0428`.
  F329 reuses only its 20-, 28-, and 36-bit modulus rows and offline labels.

No network source, Sage computation, or large-graph enumeration is used in
F329. Offline factors enter exact controls and output validation only. They do
not enter an arithmetic trajectory.
