# ROOT_GAUSS_WINDOW: exact Gauss and retained-window validation

Status: exact finite validation of the formulas supplied by the root. No new
formula, proof, asymptotic claim, or repair was attempted.

## Coefficient-array Gauss check

For \(m=2^r\), \(q=m^2\), \(c=m/2\), and \(A=1+q/2\), the source compares

\[
 S=\sum_{w\bmod q}
 \zeta^{A(au_0-b\gamma)w+c(au_0+b\gamma)w^2}
\]

with the claimed zero or Gauss-sum value. Both sides are represented
coefficient by coefficient in

\[
 \mathbb Z[X]/(X^{q/2}+1).
\]

This is the exact cyclotomic relation for a primitive \(q\)-th root when
\(q\) is a power of two.

| \(r\) | \(q\) | Mode | Checks | Surviving condition | Mismatches |
|---:|---:|---|---:|---:|---:|
| 3 | 64 | all odd frequency pairs, \(u_0=\gamma=1\) | 1,024 | 128 | 0 |
| 4 | 256 | all odd frequency pairs, \(u_0=\gamma=1\) | 16,384 | 1,024 | 0 |
| 5 | 1,024 | random parameters plus 16 forced survivors | 272 | 26 | 0 |
| 6 | 4,096 | random parameters plus 16 forced survivors | 144 | 18 | 0 |
| 7 | 16,384 | random parameters plus 16 forced survivors | 48 | 16 | 0 |

All 17,872 comparisons matched. Of these, 1,212 satisfied
\(au_0\equiv b\gamma\pmod {2m}\) and tested the nonzero formula

\[
 S=mG_m(b\gamma)\eta^{-j^2/(b\gamma)}.
\]

The remaining cases tested exact vanishing.

## Exact retained-window count

Sage 10.9 evaluated the supplied Fourier expression in
\(\operatorname{CyclotomicField}(q)\). Every division was a field operation,
and all phases were retained exactly.

| \(q\) | \(u_0\) | \(\gamma\) | \(D\) | Direct count | Surviving \((a,b)\) | Match |
|---:|---:|---:|---:|---:|---:|:---:|
| 64 | 1 | 45 | 13 | 18 | 128 | yes |
| 64 | 3 | 15 | 25 | 18 | 128 | yes |
| 64 | 5 | 7 | 0 | 14 | 128 | yes |
| 256 | 1 | 109 | 230 | 67 | 1,024 | yes |
| 256 | 7 | 235 | 142 | 57 | 1,024 | yes |
| 256 | 13 | 241 | 31 | 60 | 1,024 | yes |

The required \(q=64,u_0=1,\gamma=45,D=13\) case retained count 18.
There were no mismatches.

## High-lift Cauchy identity

The exact field check evaluated both supplied sides for 76 cases:

- 64 structured \(q=64\) cases covering four \(d\)-sources, every odd
  \(b_0\bmod 8\), and every \(z\bmod 4\); and
- 12 seeded random \(q=256\) cases.

Every difference was exactly zero in the cyclotomic field. No denominator
vanished in these cases.

## Resources and setup record

The coefficient-array run took 0.612 seconds and used peak RSS 17,530,880
bytes. Its source alarm was 20 seconds. The successful Sage computation took
1.362 seconds and used peak RSS 260,734,976 bytes. Its source alarm was
30 seconds. Both remained within the stated limits.

Three setup attempts stopped before an output artifact was written:

1. the sandbox blocked Sage's lazy-import cache under the user directory;
2. the Sage preparser produced a non-built-in seed integer rejected by
   Python 3.14; and
3. exact computations completed, but Sage integers needed explicit JSON
   conversion.

The retained compatibility changes are \(int(\mathrm{SEED})\) and
JSON integer conversion. No mathematical formula changed.

## Artifacts

- ROOT_GAUSS_WINDOW.py and ROOT_GAUSS_WINDOW_output.json: coefficient arrays;
- ROOT_GAUSS_WINDOW.sage and ROOT_GAUSS_WINDOW_sage_output.json: exact field
  checks;
- ROOT_GAUSS_WINDOW_run.log and ROOT_GAUSS_WINDOW_sage_run.log: successful
  run summaries;
- ROOT_GAUSS_WINDOW_sage_setup.log: pre-check setup failures; and
- ROOT_GAUSS_WINDOW_RESOURCE.md: resource estimate and preflight.
