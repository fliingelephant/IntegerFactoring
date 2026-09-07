# F332 retained sources

- Frozen F326 arithmetic implementation:
  `experiments/F326_direct_gauss_pairing/direct_gauss_pairing.py`, SHA-256
  `7829cc45822021c64c42842a2c938b15c52df85e30ae694efcdd4171c5012f73`.
- F330 exact statement and guards:
  `experiments/F330_short_path_conditions/STATEMENT_ONLY.md`, SHA-256
  `a1b1b87a5b3d4ea524a24ec6bcfb3c24b666fdaace6ab115830d912a1ebd67bc`.
- F330 author proof: `experiments/F330_short_path_conditions/PROOF.md`,
  SHA-256
  `f7f6519ec90c7c5ce4ebf9d9916ab721194ada55f2ef6ba9edf3533da717a8df`.
- F330 positive-block derivation:
  `experiments/F330_short_path_conditions/RATIONAL_PATHS.md`, SHA-256
  `b0d59c6344e4761572eb187d923cddb94c0f624432e08ff89ac6f9a53de021d7`.
- Retained F328 public moduli:
  `experiments/F328_capped_rabin_paths/moduli.json`, SHA-256
  `acf09b285c57c39cfcb93d3cd77addce909498e224955fd0ec9d2e4d86ee0428`.

The F330 author supplied the kernel's intermediate guards and clarified that
the block cap and fine F-call cap are different work measures. No external
source or new prime generation was used. Offline factors classify whether a
square root of `-1` is impossible; they do not enter either public solver.
