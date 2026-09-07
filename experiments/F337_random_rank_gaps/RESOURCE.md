# F337 resource control

**Family:** route:F31

The 2026-09-07 preflight reported 59 percent system-wide free memory, zero
swap I/O in the preceding shared check, and load averages 2.19, 2.00, and
1.89. The process listing was restricted. The other Sol worker announced
only a bounded fair-branch rerun of about 0.6 seconds and 28 MiB in the second
authorized slot. F337 uses one Python process and one thread.

The pilot starts with `N=209` and two attempts per each of seven source laws.
Only that input uses the direct quadratic energy validation. The full plan
runs one modulus per process with eight attempts per law. The largest offline
array has 5,404 ranks; grouped residue sums replace quadratic enumeration for
`N=1333` and `N=10807`. Estimated runtime is below 10 seconds and peak RSS
below 256 MiB per process.

The source enforces a 28-second internal alarm, a 30-second external timeout,
and a 256 MiB peak-RSS ceiling. Large sorted arrays are offline diagnostics.
Offline factors never select a public parameter or rank law.

The `N=209` pilot passed in 0.031 seconds at 33,587,200 bytes peak RSS.
The full `N=209`, `N=1333`, and `N=10807` jobs passed in 0.139, 0.197,
and 1.721 seconds, respectively; the largest peak RSS was 41,172,992 bytes.
The aggregate pass took 0.046 seconds and peaked at 71,909,376 bytes. Every
job stayed within its resource bounds, and no numerical process remains.
