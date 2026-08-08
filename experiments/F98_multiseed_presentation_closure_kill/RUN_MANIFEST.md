# F98 run manifest

## Identity

- Experiment: `F98_multiseed_presentation_closure_kill`.
- Final disposition: exact positive mechanism candidate.
- Date: 2026-08-08.
- Durable ledgers edited by this agent: none.
- Audit status: no hostile audit and no proof-blind reconstruction yet.

## Final public replay

Source: `public_factorization_free_replay.py`.

Runner: `run_public_replay_with_timeout.py`.

Command issued from this directory:

    python3 run_public_replay_with_timeout.py

The runner invoked:

    python3 public_factorization_free_replay.py \
      --modulus 202537109 \
      --output PUBLIC_REPLAY_OUTPUT.json

The runner imposed a 120-second wall-clock timeout. It finished with exit
code zero. The log is `PUBLIC_REPLAY_RUN.log`.

The executable receives only `N`. It derives `n`, `B=n^2`, seeds, canonical
inverses, initial gcd/perfect-power blocks, active pairs, trajectories,
direct gcd screens, retained relations, factor-free parity blocks, binary
kernel roots, and final gcds. It contains no displayed factors, target word,
target exponent, target relation value, or target square class.

The final decoder is a self-contained copy of the audited P66
`parity_coprime_basis` and `binary_kernel_basis` logic in
`F59_D01_scan.py`, with first-occurrence provenance added.

## Final small-support diagnosis

Source: `analyze_minimum_circuit.py`.

Runner: `run_minimum_circuit_with_timeout.py`.

Command issued from this directory:

    python3 run_minimum_circuit_with_timeout.py

The runner invoked:

    python3 analyze_minimum_circuit.py

The runner imposed a 120-second wall-clock timeout. It finished with exit
code zero. The output and log are `SMALL_SUPPORT_OUTPUT.json` and
`SMALL_SUPPORT_RUN.log`.

This diagnostic receives only `N` and the pinned public prefix length 5,616.
It uses factor-free gcd refinement and exact square tests. It checks every
support-one and support-two circuit. For support three, it checks the first
right endpoint for each matching left pair and separately certifies that
all alternative right endpoints differ by an identical-value global
support-two cycle. It also records one 166-column Gaussian witness. It does
not claim that 166 is minimum above support three.

## Input discovery and direct-null selection

The named diverse-band screen is `DIRECT_10K_OUTPUT.json`, produced by
`search_direct_trajectory.py` through `run_direct_10k_with_timeout.py` under
a 120-second timeout. It used 500 deterministic diverse prime pairs, with
162 stable pairs retained. Five were complete round-one direct nulls. The
first was the selected input.

Factor data was used in discovery to select and certify stable semiprimes.
It is absent from the final per-input public replay.

## Superseded and failed runs preserved

- `DISCOVERY_10K_OUTPUT.json` used a fixed first prime because of the old
  lexicographic pair cap. It is a sampling artifact and is not proof.
- `DISCOVERY_RUN.log` records a timed-out 5K--20K broad run.
- `DISCOVERY_100K_RUN.log` records a timed-out diverse 100K run. Its
  checkpoint output remains in `DISCOVERY_100K_OUTPUT.json`.
- `DISCOVERY_1M_RUN.log` records a timed-out full 1M run with no completed
  output.
- `MINIMUM_CIRCUIT_OUTPUT.json` and `MINIMUM_CIRCUIT_RUN.log` are the
  superseded factor-assisted version of the small-support diagnosis.
- `SINGLE_202537109_OUTPUT.json` and `DIRECT_NULLS_10K_FULL_OUTPUT.json` are
  factor-assisted discovery confirmations. They are not used as final proof.
- `DIRECT_1M_OUTPUT.json` is a later direct-only screen. It is not used in
  the final claim.

No conclusion is drawn from a timed-out run.

## Final SHA-256 pins

    6f4ff30185cef38effd1cc0954f1d30504a5ba216144c422446cf4da8a014273  DESIGN.md
    f2d28d074d53bc93c675553b28e083b93b0d6dd35d1a65edb430c69a6cd26fb0  RESULT.md
    5fded40920ca52827662ba536f14a49ec9e302b934f6d0967e66be2b18c9ba4b  public_factorization_free_replay.py
    7525f1eba47d154143e4df7706ed4c9150abd988927c999217dde01062a1438b  run_public_replay_with_timeout.py
    6cf67bb5928248ad139daa374a805d463859a67d2a398303c6153d2b4defd7c7  PUBLIC_REPLAY_RUN.log
    ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab  PUBLIC_REPLAY_OUTPUT.json
    749e4c2c43d78d895aa53de685b719b051c6115135df6a9b51cb8d3ac7b3ffb6  analyze_minimum_circuit.py
    90fde9c43fdb1797832ab2e97adddb442c7e692e852be0aaa324ecc41827cc76  run_minimum_circuit_with_timeout.py
    433d12eef1de0407f85f74f7e102a05e41a8d358da135e44a253d8c8aa7ba6bb  SMALL_SUPPORT_RUN.log
    3896034b332f55b0cd1b8302eecf117c26e9c3dcb934eb7b7912f332d49aa8c2  SMALL_SUPPORT_OUTPUT.json
    d1cdf08cb99a26d671484d7b566442620d73a7d6c8c1958a79100b83d66788e7  search_direct_trajectory.py
    3e611505a98e8fc8a54cfb6c707298fa150c277f6f6cd4bf84ca007fd20dec25  run_direct_10k_with_timeout.py
    1d6be67149c368f9ec7810b3baec5e3900b60754891b0c101271455c5534a73c  DIRECT_10K_RUN.log
    738a5738b6909ae3528d3eb9aea5194d510b56b0772bd476db742cd4ee902ea8  DIRECT_10K_OUTPUT.json
    b68a07945899395649a5373f6d321009bb42cf072dfad9342392d2c8fd7c8c0a  ../F59_completion_bias_generic_decoder_scan/scripts/F59_D01_scan.py

The manifest does not hash itself.
