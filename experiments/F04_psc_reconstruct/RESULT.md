# Proof-blind reconstruction of C13

## Verdict

The stated arithmetic is **confirmed under the determinant convention in the prompt**:

- The global representative has `n = 268`.
- `gcd(D_j, 79403) = 1` for every `0 <= j <= 46`.
- `D_47 = 30352 (mod 79403)` and `gcd(30352, 79403) = 271`.
- After the global gcd has revealed `271`, the complementary factor is `293`; the independently recomputed local representatives have degrees `46` and `268`, and the two reductions of `D_47` are `0` and `173`.

There is one material overclaim to avoid: a PSC is not needed to expose the factor. The constant coefficient of the already-computed global `H` is

`h_0 = 36585`, with `gcd(36585, 79403) = 271`.

Thus an increasing-degree raw-coefficient scan separates at degree `0`, before any determinant scan. In fact, 246 of the 269 displayed coefficients are separators.

## Exact determinant and dimension

For fixed `j`, there are `n-j` columns for `X^s P` and `r-j` columns for `X^t H`. The output interval

`j, j+1, ..., r+n-j-1`

has `r+n-2j` entries. Hence the matrix is square of dimension

`m_j = r+n-2j = 537-2j`.

At `j=47`, it has `221+222=443` columns and rows indexed by degrees `47,...,489`, also 443 rows. R01 constructed exactly this integer matrix using the representatives `0,...,N-1`, with rows increasing, increasing shifts inside each block, and all `P`-shift columns before all `H`-shift columns. It computed exact integer determinants and only then reduced modulo `N`. The scan started at `j=0`, used no factor and no preselected stopping index, and first obtained a proper gcd at `j=47`. The complete exact determinants and all 48 residues are in `output/R01_global.json`; R03 checks each exact determinant against its stored residue and gcd.

Changing conventions can change the displayed residue. At `j=47`, reversing the 443 rows contributes `(-1)^(443*442/2)=-1`, changing `30352` to `49051`. Replacing `P=X^269-1` by its negative also changes the sign because there are 221 `P` columns. Swapping the two column blocks does not change the sign here because `221*222` is even.

## Global discovery versus local certificate

R01 uses only `(N,r,a)=(79403,269,1)`. It computes `H` by binary powering with cyclic convolution modulo `(N,X^269-1)`, determines its global degree, and scans increasing `j`. Neither `271`, `293`, `47`, nor `30352` is an input to that source.

Only afterward, R02 takes the returned gcd dynamically. It verifies

`79403 = 271 * 293`,

with both factors prime, independently recomputes `H` in each finite-field quotient, and directly recomputes every local determinant through `j=47`. The local results reduce coefficientwise from the global result and give

`deg(H mod 271)=46`, `deg(H mod 293)=268`, and

`D_47 mod 271=0`, `D_47 mod 293=173`.

CRT then gives the unique residue `30352`: it is `271*112`, and `30352 mod 293=173`.

The local degrees also admit a short check. Since `N=271*293`, Frobenius and `X^269=1` give

`H mod 271 = (1+X^4)(1+X^2)^22-X^48-1`,

whose leading term is `22 X^46`. Modulo 293,

`H = (1+X^24)^271-X^48-1`.

The coefficient of `X^268` comes only from exponent index `t=56` (`24t=268 mod 269`) and equals `binomial(271,56)=41 mod 293`, so it is nonzero.

## Reduction and formal-degree padding

Reduction commutes because both quotient formation and determinant evaluation are polynomial operations under the ring maps `Z/NZ -> F_271,F_293`. Therefore reducing the global matrix entrywise gives the local matrix and reducing its determinant gives the local determinant.

This statement requires retaining the **global formal degree `n=268`** when forming both local matrices. Modulo 271 the actual degree drops to 46, but changing `n` to 46 changes the column bounds and matrix dimension; `D_47` would not even be defined in that altered family. Zero-padding through formal degree 268 is therefore essential, not cosmetic.

## Ordering scope and cost

With “standard shifts” ordered `a=1,2,...` and `j` increasing inside each shift, `(a,j)=(1,47)` is the first determinant separator in that lexicographic scope, because `a=1` is the first shift and R01 proves all earlier `j` are units. This does not make it the first separator among other statistics: `h_0` already separates.

The construction has uniform polynomial bit cost under the stated parameter regime. Cyclic binary powering costs `O(r^2 log N)` ring operations with naive multiplication. Each matrix has size at most `2r-1`; Berkowitz computes its determinant over the arbitrary commutative ring `Z/NZ` without division in `O(r^4)` ring operations. For `S` shifts and at most `r` values of `j`, the bound is `O(S r^5)` ring operations, each on `O(log N)`-bit residues. Thus it is polynomial in `log N` when `r` and `S` are. The final integer gcd is also polynomial-time and requires no inversion in `Z/NZ`.

## Reproducibility

All three authoritative runs completed before their hard timeouts. Commands, timings, log hashes, sources, outputs, and dispositions are listed in `RUN_MANIFEST.md`. R03 passed every cross-check. A preselected-`j=47` development probe had incomplete provenance and supports no claim; its restored controlled replay is disclosed in the manifest. No canonical result/progress file and neither forbidden PSC experiment directory was read or edited.
