# Rational nullspaces for the structured `9M+1` cases

**Status:** exact finite follow-up to F310. This report describes only the
specified right nullspaces in the fixed matrix order. It states no all-size
rank formula, obstruction, or optimality claim for the returned basis.

For `s=7,9,11,13`, the matrix is the F310 matrix

    A[a,b]=phase(a+2^r*b),  r=floor((s-1)/2),

for the structured input `N=9M+1`. Sage computed its right kernel over `QQ`.
Each returned basis vector was multiplied by the least common multiple of its
denominators, divided by the gcd of its integer entries, and negated when
necessary so that its first nonzero entry is positive. Direct exact matrix
multiplication checked every normalized vector.

## Results

| s | Matrix order R | Rank over QQ | Nullity | Support sizes | Maximum absolute entries |
|---:|---:|---:|---:|---|---|
| 7 | 8 | 5 | 3 | 4, 4, 4 | 1, 1, 1 |
| 9 | 16 | 13 | 3 | 11, 10, 8 | 7, 2, 1 |
| 11 | 32 | 29 | 3 | 18, 27, 18 | 20, 199, 10 |
| 13 | 64 | 61 | 3 | 60, 59, 59 | 45688504479043099, 1183837317606248, 323993101178168 |

Thus the previously observed `R-3` ranks persist over the rationals in all
four requested cases. The deficiency is not caused only by reduction modulo
65521.

The normalized echelon basis is sparse with entries in `{0,+1,-1}` at
`s=7`. Its supports and coefficients become progressively larger, and the
returned `s=13` vectors are nearly dense. This observation concerns this
specific Sage basis. Another basis of the same three-dimensional nullspace
could have a different shape, so no absence-of-structure conclusion follows.

The complete integer vectors and their support indices are retained in both
`walsh_phase_nullspace.json` and `walsh_phase_nullspace.log`.

## Resources and evidence

All four cases took 0.0354 seconds after Sage startup and used 257,556,480
bytes peak RSS. The run used a hard 30-second outer timeout, a 28-second
internal alarm, a 1 GiB RSS watchdog, and one Sage process.

Evidence:
`walsh_phase_nullspace.sage`, `walsh_phase_nullspace.json`,
`walsh_phase_nullspace.log`, and `NULLSPACE_RESOURCE.md`.
