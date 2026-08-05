# F04 PSC coefficient reconstruction

Status: **self-audited reconstruction**.

This directory is an isolated, proof-blind reconstruction of the bare F04
statement supplied to the agent.  It does not depend on, cite, or modify the
canonical research state or either pre-existing F04 experiment.

The reconstruction has two logically separate parts:

1. `THEOREM.md` proves the determinant/nonzero-degree-chain theorem from the
   definition of the displayed linear map.
2. A finite certificate first materializes every global coefficient vector in
   `(Z/NZ)[X]/(X^2953-1)` in `outputs/global_vectors.bin`.  A separate verifier
   then reads that file, reduces its already-materialized entries modulo each
   prime factor, checks every coefficient, and checks every ordinary Euclidean
   degree in both fields.

All mathematical executions use named source files, a recorded pre-run source
manifest, hard timeouts, separate logs and outputs, and explicit failure files.
See `RUNBOOK.md` and `AUDIT.md`.

The computation is a certificate for this one fixed integer and these 2,942
shifts.  It is not evidence of a uniform polynomial-time factoring algorithm.

