# F54-D01 preregistration and run manifest

- Family: F29, iterated low-degree polynomial root basins.
- Run: F54-D01.
- Status: completed successfully with exit status 0.
- Source: `scripts/F54_D01_exact_basins.py`.
- Runner: `run_F54_D01.sh`.
- Command from the workspace root:
  `sh experiments/F54_polynomial_root_basin_kill/run_F54_D01.sh`.
- Declared timeout: 60 seconds, enforced by
  `/opt/homebrew/bin/timeout 60s`.
- Log: `logs/F54-D01.log`.
- Output: `output/F54-D01.json`.
- Environment: the Python version is written to the log.

## Exact finite question

For every odd prime \(p\le509\) for which \(5\) is a quadratic nonresidue,
the run checks the exact claim

\[
H^{-1}(\{0,1\})=\{0,1\},\qquad H(x)=x(x-1).
\]

For every such \(p\) and every \(c\in\mathbb F_p^\times\), it also checks
the scaled family

\[
H_c(x)=cH(x/c)=x(x-c)/c,
\]

including both the conjugacy and
\(H_c^{-1}(\{0,c\})=\{0,c\}\).

For every distinct pair of the listed primes through 79, it enumerates all
starts modulo \(N=pq\), runs eight iterations, screens both public root
tickets, and checks the predicted exact success count

\[
2p+2q-6.
\]

This run can refute these candidate formulas. Passing cannot prove them for
unbounded primes or prove an asymptotic runtime statement. The result will
use a symbolic proof.

## Preregistered hashes

- Source SHA-256:
  `943ea2fd1cc28bc53998499f468f06a9ea43176e6819929fa1ff0853a80fca60`.
- Runner SHA-256:
  `2fa47db442b6b7c5a5d45c43af073d4f67f24ac68b36d81db13a92f6ad416f00`.

## Outcome

- Runner wall time: 0.613 seconds under the declared 60-second timeout.
- Python: 3.14.5.
- Log SHA-256:
  `3ce069be420d1a929996c1e88f2e7694a29818a4d42f54fe7fe4eaec05f68048`.
- Output SHA-256:
  `1c6c32f0b4e7dfbeffe2b171fb36ba02921b62a648fff7347f10c9fdd189b6f3`.
- Checked 49 primes, 10,954 nonzero scaling parameters, and 55 distinct
  semiprime pairs.
- No baseline, scaled-family, or semiprime-count counterexample occurred.

This finite result is only a cross-check. It supports no unbounded claim.
