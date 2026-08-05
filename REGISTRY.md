# Approach Registry

Each family is grouped by its mathematical mechanism and terminal missing lemma. Before opening a route, compare it with `FAILED.md`. A stalled route must be classified as either **method failure** or **evidence against the exact auxiliary claim/mechanism**.

| ID | Mechanism / family | Exact claim attempted | Exact remaining gap | Smallest known obstruction | Next decisive test | Status |
| --- | --- | --- | --- | --- | --- | --- |
| F01 | Square-class compression / power-sum reconstruction (A1, A8) | From \(\operatorname{poly}(n)\) efficiently generated residues, recover a nontrivial congruence of squares with inverse-polynomial success probability, without smoothness or hidden factoring | Universally sound exact linear sketches cannot reduce square-class rank; lossy verified sketches, nonlinear/adaptive encodings, and special low-rank generators remain open; a useful second modular square root remains equivalent to splitting | Promoted rank-nullity obstruction; promoted hidden-root reduction; one-moment collision remains candidate | Test verified lossy sketches and higher-moment special generators, explicitly accounting for rejection probability | narrow generic-sketch failure promoted; broader family open |
| F02 | Succinct collision products in algebraic dynamics (B3) | Compute a Pollard-rho collision discriminant for exponentially many iterates by a circuit of size \(\operatorname{poly}(n)\), with inverse-polynomial probability of separating CRT components | Compression alone does not ensure asymmetric local collision times; arbitrary-x seeds and dynamics with provably separated local periods remain open | Candidate \(N=15\) duplication-Lattès witness: both local groups have order 7, so every affine seed collides simultaneously | Hostilely audit the curve enumeration, map, denominator units, and claimed minimality | initial kill result: candidate method failure for standard duplication-Lattès point seeds |
| F03 | Galois cycle-type / resolvent CRT separation (B2) | Use low-degree random polynomials and a computable subresultant/rank certificate whose reduction vanishes in exactly one unknown prime component with inverse-polynomial probability | Unequal local gcd degrees are efficiently extractable, but a cycle-type mismatch alone yields only a Jacobi-sign promise equivalent to factoring; componentwise Frobenius construction is circular | Candidate \(N=15,f=X^2+1\) DDF witness and conditional principal-subresultant lemma; verification cadence pending | Hostilely audit all probability, subresultant, DDF, and equivalence claims; search for certificates richer than cycle type but cheaper than local Frobenius | initial kill result: candidate method failure for standard DDF/resolvent instantiation |

## Computation ledger

Every computation must list its source file, family ID, timeout, log, and output location. Finite computation is discovery or counterexample evidence only.

| Run | Family | Source | Timeout | Log | Output / certificate | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
