# Frozen small Pell-orbit circuit search

Purpose: determine whether the fixed `D=2` fundamental Pell trajectory can
contain a retained exact-square dependency after canonical reduction.

Enumerate odd primes `3 <= p < q < 2p` with `p <= 500`, ordered by `(p,q)`.
For `N=pq`, put `n=N.bit_length()` and generate
`(3+2*sqrt(2))^j = S_j+T_j*sqrt(2)` for `0 <= j <= 4n`.
Set `y_j=T_j mod N`, `x_j=S_j mod N`, and `A_j=1+2*y_j^2`.

Apply the F250 cleanup exactly: discard `j=0`; discard and record a factor
when `gcd(x_j,N)` is proper; discard exact-square `A_j` after testing both
root gcds; discard repeated `y_j` after testing both supplied-root sign gcds.

For retained rows, factor `A_j` by exact trial division and perform binary
square-class elimination in increasing `j`.  At the first dependent column,
reconstruct and verify its exact square subset and both normalized-root gcds.
Report the lexicographically first witness by `(N,j)` and stop.  If no witness
exists, report null over the frozen range.  Also report source counts.

The run is local, single-process, and deterministic.  Estimated runtime is
under 10 seconds and peak memory under 50 MiB.  Abort after 60 seconds.  This
is finite discovery evidence only.
