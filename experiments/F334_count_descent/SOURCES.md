# F334 sources and scope

**Family:** route:F31

No web source or external dataset was used.

## Mathematical and numerical inputs

| File | SHA256 | Use |
|---|---|---|
| experiments/F330_short_path_conditions/Q_DESCENT_DESIGN.md | 5453c6e1c4f43985158a2fd3db60d8c9acfd61e0fbedc72684de39fe1ed5858a | Frozen descent and dyadic-menu protocol |
| experiments/F330_short_path_conditions/DISCREPANCY_NOTE.md | ef1c19be8d814807b3132a508db0e39ac0fa9a2f0361b7e0d74ca99e72abdd50 | Simultaneous continued-fraction defect bound |
| experiments/F326_direct_gauss_pairing/direct_gauss_pairing.py | 7829cc45822021c64c42842a2c938b15c52df85e30ae694efcdd4171c5012f73 | Frozen GaussPairing.floor_sum, K, and Q method objects |
| experiments/F328_capped_rabin_paths/moduli.json | acf09b285c57c39cfcb93d3cd77addce909498e224955fd0ec9d2e4d86ee0428 | Two retained moduli at each requested bit scale |

CountOracle aliases the three frozen F326 method objects. It initializes only
the fields those count methods use. It does not construct a domain, rank map,
involution, or path. Its arithmetic accepts any unit multiplier. The F334
sampling driver separately restricts the compared initial and fresh parameters
to Jacobi-positive units.

The F328 values p_offline and q_offline are retained labels. The solver and
menu builders receive only public N, public a where applicable, and public
cutoff D. Offline factors are attached only after an output or menu gcd has
already been computed.

## Workflow inputs

| File | SHA256 |
|---|---|
| README.md | 2599c853b752bf416250fdfccf741ebbb8540150920b504dfdbec011a5efe968 |
| PROMPT.md | 66f29a71094fa88b6b00f110d477ff753240acf0aebba7d7e9d75c87077f37ab |
| research/STATE.md | 8bd27941667f8d4de63fc19d25976569e8502a1af334a16107cca3d47d4c4bcb |

The Rust reader was used to inspect the route:F31 head and P248 metadata. No
shared record body or historical ledger was used as an implementation
dependency.
