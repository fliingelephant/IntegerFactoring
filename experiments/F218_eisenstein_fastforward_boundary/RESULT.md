# F218 result

## Status

F218 is a frozen proof-only, self-audited candidate.  It contains no
empirical mathematical claim.  It does not factor the input and does not
construct the missing remote coefficient evaluator.

## Proved candidate statements

1. Modulo every prime power `ell^e || K`, a moving Eisenstein exponent
   congruent to one modulo `lambda(K)` collapses coefficientwise to the
   `ell`-depleted weight-two coefficient

   \[
   \sigma_1(m/\ell^{v_\ell(m)}).
   \]

   At the target `m=N`, this is exactly `sigma_1(N) mod ell^e`.
2. For prime `K=r`, the first `r`-adic eta quotient lift returns the same
   depleted coefficient, with the explicit normalization

   \[
   -[q^m]F_r/r=u^{-1}\sigma_1(u)\pmod r,
   \qquad m=r^v u.
   \]
3. A big-Witt circuit using only `K`-supported Frobenius and
   Verschiebung preserves the prime-to-`K` rough part of every ghost index.
   It cannot turn the affine target `N=2K+1` into a smaller seed index.
4. The Frobenius-compressed theta attempt has an exact cusp obstruction.
   At `r=17, N=35`, the full theta coefficient is `15 mod 17`, its
   Eisenstein target is `10 mod 17`, and the cusp difference is `5`.
5. For every prime `r`, the affine Cartier section

   \[
   b_r(j)=\sigma_1(rj+1)\bmod r
   \]

   is not eventually periodic.  It has no constant-coefficient affine or
   homogeneous linear recurrence of any finite order, and its generating
   series over `F_r` is not rational.

## Failed remote launch

F218-D01 was preregistered and the remote source hashes matched the frozen
local files.  The first launch used the required timeout and the planned
single-core low-priority command.  It exited with status `127` before
Python started because the remote image has no `/usr/bin/time`:

```text
nice: ‘/usr/bin/time’: No such file or directory
```

No remote `RESULT.json` was produced.  The exact empty stdout, stderr,
exit status, resource check, source, and preregistration are preserved.
The runner was not changed and the experiment was not rerun.  Therefore
F218 makes no finite-search claim.

## Sharp live interface

The remaining live interface is not another moving-weight packaging.  It
is a nonlinear or growing-state exact evaluator for

\[
\sigma_1(N)\bmod K,
\]

or an equivalent cusp/Cartier projection that computes this residue from
`factor(K)` without materializing numeric-exponential coefficient state.
Any solution must use operations that mix the affine index `2K+1` in a way
that standard `K`-supported Witt operations and fixed linear Cartier state
do not.
