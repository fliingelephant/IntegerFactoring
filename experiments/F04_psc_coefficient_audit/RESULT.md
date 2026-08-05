# Hostile audit of the F04/X12 coefficient-hard PSC obstruction

## Verdict

The field theorem and the finite P11 obstruction survive, with one proof-level correction and one implementation warning.

The theorem is valid for the fixed determinant itself. The earlier proof's informal assertion that a Euclidean step gives a unit multiple of a smaller determinant is unnecessary and was not independently justified here. The direct kernel proof below replaces it and covers abnormal degree gaps, positive-degree gcds, and the top index without any PRS normalization or sparse-list indexing.

The implementation warning is that Sage's `subresultants()` list is not generically safe to index as a dense list across arbitrary small inputs; A06 and A07 failed on that assumption and support no claim. This does not affect the P11 zero-pattern conclusion, which follows from the direct theorem and the exhaustive Euclidean degree chains. At the two P11 endpoints, A04 explicitly observed the required dense full-chain list length, materialized all exact residues, and matched the earlier endpoint vectors byte-for-byte by residue hash.

## Corrected theorem, exact index set, and proof

Let `K` be a field and let nonzero `F,G in K[X]` have degrees `m>n`. For `0<=j<=n`, use exactly the fixed matrix: increasing output degrees `j,...,m+n-j-1`; increasing shifts of `F` first, then increasing shifts of `G`; multiplier bounds `deg U<n-j`, `deg V<m-j`. Let

`R_0=F, R_1=G, R_{i+1}=R_{i-1} mod R_i`

and let the degrees of the nonzero remainders be

`d_0=m>d_1=n>d_2>...>d_s=g`.

The final zero remainder is excluded, and `d_0` is outside the determinant index range. Then

`D_j(F,G) != 0  iff  j in {d_1,...,d_s}`.

In particular, every `j<g` is zero, every strict gap between consecutive remainder degrees consists of zeros, and

`D_n=lc(G)^(m-n) != 0`.

Proof: the defining matrix is square of dimension `m+n-2j`. Since every `UF+VG` has degree at most `m+n-j-1`, its matrix has a kernel exactly when there is a nonzero bounded pair `(U,V)` with `deg(UF+VG)<j`.

Write extended Euclidean cofactors as `R_i=S_iF+T_iG`. Adjacent cofactor pairs are unimodular, so `gcd(S_i,T_i)=1`, and ordinary division gives

`deg T_i=m-d_(i-1)` for `i>=1`, and `deg S_i=n-d_(i-1)` for `i>=2` (with `S_1=0`).

- If `d_(i+1)<j<d_i`, the pair `(S_(i+1),T_(i+1))` obeys both multiplier bounds and produces `R_(i+1)` of degree below `j`; hence `D_j=0`.
- If `j<g`, `(G/gcd(F,G),-F/gcd(F,G))` obeys both bounds and produces zero; hence `D_j=0`.
- Let `j=d_i` and suppose bounded `(U,V)` produces `L=UF+VG` with `deg L<d_i`. Then

  `V R_i-T_i L=(V S_i-T_i U)F`.

  Both terms on the left have degree below `m`, so the multiple of `F` must be zero. Thus `VS_i=T_iU`; coprimality of `S_i,T_i` gives `(U,V)=C(S_i,T_i)`, whence `L=CR_i`. Its degree cannot be below `d_i` unless `C=0`. The matrix is injective and `D_(d_i)!=0`.

At `j=n`, there are no `F` columns. The remaining matrix is triangular in the fixed increasing order with diagonal `lc(G)`, proving the displayed top formula with its exact sign.

A03 independently checked 4,932 exhaustive monic pairs over `GF(2)` through first degree 5 and `GF(3)` through first degree 4: 17,556 direct defining determinants, 1,788 cases with an internal abnormal gap, 1,790 positive-gcd cases, and 182 constant-`G` cases. It found no counterexample and checked the top formula in every case. Monic normalization loses no zero-pattern cases because nonzero rescaling changes determinants only by nonzero field factors.

## Fresh P11 exhaustion

A04 independently reran all standard shifts `1<=a<=2942` for

`N=20000000499999937=100000007*199999991`, `r=2953`.

For each shift it first formed

`H_a=(X+a)^N-X^N-a mod (X^2953-1)`

over `Z/NZ`, materialized that global coefficient vector, checked all its coefficients by `gcd(coefficient,N)`, and only then reduced the same vector into the two fields. It used no reduced-exponent substitution to construct the local inputs.

Results:

- 2,942 shifts completed under the 900-second timeout in 202.354 seconds wall time.
- All global degrees were 2,952.
- All `2,942*2,953=8,687,726` global coefficients were units modulo `N`.
- Both local ordinary Euclidean chains were exactly `2953,2952,...,0` at every shift.
- Therefore all `8,687,726` canonical determinant statuses per field, `17,375,452` total, were nonzero.
- The fresh 2,942 global coefficient-vector hashes all match the earlier R08 rows. The fresh rows hash is `7b1d411243e808e199d8bdd9e89b63f48aecfd344f650d80cc1dcae3a4298cb7`.

The exact endpoint residue vectors contain all `D_0,...,D_2952` values. Their boundary values are:

| shift | value | mod 100000007 | mod 199999991 | CRT mod N |
|---:|---|---:|---:|---:|
| 1 | `D_0` | 11525863 | 147232491 | 18571362511521147 |
| 1 | `D_2952` | 38386070 | 49417508 | 14008969419013858 |
| 2942 | `D_0` | 84912487 | 192618608 | 3545270833081422 |
| 2942 | `D_2952` | 4292146 | 123011658 | 12336691767860509 |

For shifts 1 and 2942 respectively, the local residue-vector hash pairs are

- `96c5cd358a44da272ad2420a0aac033527abff5eb00a598600f2d2cafb2697c3`, `1def7324bd999e1030ff8b299de1742a3ca6ab0f06e46dcfefeb4d4ae4d91f23`;
- `f4423d6e4a8f256089b48859a321b348b15b5f896b3d9e1482e392825c861358`, `9a9b40b09a656bcf4885197e9c001f2cf0e4dbe405e9c82c2ec6c0e82068c57e`.

They exactly equal the retained R05/R09 hashes. A05 verified every fresh row, count, artifact hash, endpoint residue, CRT reduction, and gcd; `audit_passed=true`.

## Independence limits and narrow obstruction

The fresh source, row stream, and timeout record are independent artifacts, but they use the same Sage finite-field and polynomial arithmetic library as the earlier computation. The endpoint vector comparison is a reproducibility check across fresh runs, not an independent implementation of subresultants. A06/A07 show why no broader claim about generic Sage list indexing is warranted. The decisive zero-pattern result does not rely on that indexing: it uses the independently proved fixed-matrix theorem plus exact ordinary Euclidean chains.

The narrow finite conclusion is unchanged: for this one P11 input, this minimal `r=2953`, and exactly the standard shifts `1,...,2942`, every individual coefficient and every fixed canonical `D_j` is a unit modulo `N`, although the AKS identities fail in both local fields. This refutes only the universal localization claim for that finite standard scan. It supplies no asymptotic lower bound and says nothing about nonstandard shifts, other moduli, other minors, or other polynomial relationships.
