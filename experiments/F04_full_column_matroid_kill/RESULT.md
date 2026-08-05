# F04 full column-matroid kill result

**Approach-family ID:** `F04_full_column_matroid_kill`  
**Status:** self-audited finite discovery.

## Verdict

The omitted P11 full-column-matroid gap is killed positively: the two local
column matroids are **not equal**.  All 32,362 one-column exchange quotients
are nonzero in both fields, but an exhaustive scan of all 237,941,605
two-column exchange quotients finds exactly two local zero-pattern
mismatches.  Each gives a globally specified `2942`-by-`2942` minor whose
gcd with `N` is the factor `199999991`.

This is an exact result for the fixed P11 matrix.  It does not prove that such
a mismatch exists uniformly for other inputs or that a polynomial-size
minor family always factors an arbitrary integer.

## Matrix and provenance

The fixed parameters are

`N=20000000499999937=100000007*199999991`, `A=2942`, and `r=A+11=2953`.

For every shift `1<=a<=A`, run 001 formed

`H_a=(X+a)^N-X^N-a mod (X^r-1)`

directly in `(Z/NZ)[X]/(X^r-1)`, using binary powering and reduction by the
monic polynomial.  It materialized the global coefficient matrix before any
field reduction.  The retained global-file SHA-256 is

`95062c911641aa6b9c03c996a1e17434b1b9210516cd403dfb6f5ceaad3431cd`.

Write `M=[M_0|M_1]`, where `M_0` consists of global columns `0,...,2941` and
`M_1` of columns `2942,...,2952`.  Exact local determinants were recomputed:

`Delta_p=det(M_0)=56136614 mod 100000007`,

`Delta_q=det(M_0)=132391112 mod 199999991`.

Both are nonzero.  Their global CRT value is
`16315256998204520 mod N`, with gcd one.

After reducing the already-formed global rows, the computation solved and
fully checked

`M_0 C_l = M_1`

over each field.  The retained `C_p,C_q` hashes are respectively

`ab98cf3541e6183ad7deac4e0ee8cf732bd3bedd6aa95d2666ac3afa3a2b7fa0`

and

`7196439353de436447c5d146f3dde3e763f60372f4579194c84ce87206a41933`.

## Determinant-quotient identity

Let `B=M_0`, `D=M_1`, and `C=B^(-1)D` over either field.  For equal-size
index sets `I subset {0,...,A-1}` and `J subset {0,...,10}`, let `E_(I,J)` be
the matrix whose columns, in original global order, are the base columns not
in `I`, followed by extra columns `A+j` for `j in J`.

Since `[B|D]=B[I_A|C]`, write `E_(I,J)=B Q_(I,J)`.  Expanding
`det Q_(I,J)` along its identity columns gives

`det E_(I,J) = epsilon(I) det(B) det(C[I,J])`,

where, for zero-based `I` and `k=|I|`,

`epsilon(I)=(-1)^(sum_(i in I)(i+1) + sum_(t=A-k+1)^A t)`.

This is the required Cramer/Jacobi exchange identity, including the sign
caused by placing the extra columns at the end.  Zero/nonzero status is
therefore exactly the status of the corresponding minor of `C` because
`det(B)` is nonzero.

For both mismatches below, run 002 also constructed the full exchanged matrix
from the retained global rows and computed its local determinant directly.
All four direct determinants equal the quotient formula, so the identity was
not used merely as an unchecked implementation shortcut.

## Exhaustive zero patterns

The exact results are:

| Family | Total | Zeros mod `p` | Zeros mod `q` | Mismatches |
| --- | ---: | ---: | ---: | ---: |
| entries of `C` / one exchanges | 32,362 | 0 | 0 | 0 |
| all `2x2` minors of `C` | 237,941,605 | 0 | 2 | 2 |

The second total is
`binom(2942,2) binom(11,2)=237941605`.  Run 003 independently rescanned the
entire family with the loop order “extra-column pair, upper row, lower row”.
Its zero-pattern file is byte-for-byte identical to run 001's file.

Rows of `C` are base-column indices; columns of `C` are local extra-column
indices.  The two zero minors are

| Removed base columns `I` | Local extras `J` | `det C_p[I,J]` | `det C_q[I,J]` |
| --- | --- | ---: | ---: |
| `{423,2336}` | `{2,6}` | 67,899,852 | 0 |
| `{1618,1874}` | `{3,10}` | 60,407,725 | 0 |

Thus the corresponding `A`-column sets are bases modulo `p` and dependent
modulo `q`; this alone proves the full column matroids differ.

## Exact global gcd certificates

All indices below are zero-based and the selected exchange columns are in
original global order.

1. Remove base columns `423,2336` and add global columns `2944,2948`.
   The exchange sign is `+1`.  The direct determinant residues are
   `15564403 mod p` and `0 mod q`.  Hence

   `det(E)=2473353088699106 mod N`,

   `gcd(2473353088699106,N)=199999991`.

2. Remove base columns `1618,1874` and add global columns `2945,2952`.
   The exchange sign is `-1`.  The direct determinant residues are
   `96432800 mod p` and `0 mod q`.  Hence

   `det(E)=15683193494256261 mod N`,

   `gcd(15683193494256261,N)=199999991`.

The complete retained table is `outputs/all_exchange_certificates.csv`.

## Factor-assisted certificate versus factor-free algorithm

The discovery computation is **factor-assisted**: it used the supplied primes
to solve for `C_p,C_q`, compare local zero patterns efficiently, compute direct
local determinants, and combine them by CRT.  Those operations are an exact
certificate for this experiment, but they are not themselves a factoring
algorithm.

The corresponding **factor-free, division-free evaluation algorithm** is
different and needs neither `C` nor the factors:

1. form every row over `Z/NZ` exactly as above;
2. enumerate the globally specified one- and two-exchange column sets in a
   fixed order;
3. evaluate each square determinant over `Z/NZ` with Berkowitz's algorithm,
   which uses only ring addition and multiplication and therefore requires no
   pivot division or factor knowledge;
4. compute `gcd(det(E),N)` and return any nontrivial result.

On the first displayed exchange set, that algorithm evaluates the same global
residue `2473353088699106` and returns `199999991`.  The numerical experiment
did not execute a 2,942-dimensional Berkowitz evaluation; its retained value
was certified factor-assistively by two direct field determinants and CRT.
The division-free algorithm is the factor-free way to recompute the same
globally defined determinant.

The number of tested minors is polynomial in the matrix dimensions, and
Berkowitz has polynomial ring-operation cost per determinant.  That observation
does not close the factoring problem: this experiment supplies no uniform
theorem that an exchange mismatch must occur for every composite input, nor a
uniform construction with all parameters proved polynomial in `log N`.

## Narrow scope

This result closes only the previously omitted full-column-matroid question
for the fixed coefficient-hard P11 matrix: the matroids differ, witnessed
already among two-column exchanges from the common base `M_0`.  It does not
characterize the rest of either matroid, scan exchanges of order three or
higher, address nonstandard shifts/moduli, or establish a universal separator.

## Artifact disposition

Run 004 was an optional packaging run, not mathematical evidence.  It exited
1 because the malformed shell token `256>` left `shasum -a` to parse
`FAILURE_DISPOSITIONS.md` as its numeric option.  Its plan, combined log, and
`outputs/run_004.failure.txt` are preserved and excluded from the mathematical
evidence.  Runs 001--003 had already fixed all source, scan, and certificate
evidence.  A later packaging-only run created a self-excluding final artifact
manifest without modifying any earlier hashed artifact.
