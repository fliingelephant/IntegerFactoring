# F218 hostile audit

## Verdict

**PASS.** All six requested frozen hashes match. I found no false
congruence, missing valuation case, invalid index invariant, incorrect theta
projection, or overstatement of the Dirichlet argument within the packet's
declared scope.

The remote run is failed evidence, not mathematical evidence. Its preserved
artifacts consistently show that Python never started. No theorem in the
packet uses that run.

I did not edit a frozen input or a durable ledger. I wrote only this audit.

## 1. Frozen-input authentication

| Artifact | Expected SHA-256 | Recomputed SHA-256 | Result |
|---|---|---|---|
| `STATEMENT.md` | `458924ffa7bf4554fd697e36bd45acf29930e414a0dd09bab10a7e388a95a481` | `458924ffa7bf4554fd697e36bd45acf29930e414a0dd09bab10a7e388a95a481` | match |
| `PROOF.md` | `cfd2319a72f087c2b1c63f64c5dfbba68e16bbe6da0950019af3f1874d712ea3` | `cfd2319a72f087c2b1c63f64c5dfbba68e16bbe6da0950019af3f1874d712ea3` | match |
| `SELF_AUDIT.md` | `3874db102f50a539e333ae85c9aa05d4366b396ad0b2a2f4ee79732d9a726172` | `3874db102f50a539e333ae85c9aa05d4366b396ad0b2a2f4ee79732d9a726172` | match |
| `PROVENANCE.md` | `752b09497a015e02ed96e77d1519468986d9362ffbd898a65c477260ba714ebf` | `752b09497a015e02ed96e77d1519468986d9362ffbd898a65c477260ba714ebf` | match |
| `RESULT.md` | `3374da2247a292f11682e43368b53d953bfab4904b07d0aaa0acfcd30e5b06ba` | `3374da2247a292f11682e43368b53d953bfab4904b07d0aaa0acfcd30e5b06ba` | match |
| `MANIFEST.md` | `838ff9ad3ab38d419f432cf9ebbaf357d19f5f338b40dc80aa77eba7041461c5` | `838ff9ad3ab38d419f432cf9ebbaf357d19f5f338b40dc80aa77eba7041461c5` | match |

The additional hashes declared by `MANIFEST.md` also match, including the
preregistration, source, resource check, and all four failed-run artifacts.

## 2. Prime-power-local Eisenstein reduction

Fix `ell^e || K`. Since `K` is odd,

\[
\lambda(\ell^e)=\varphi(\ell^e)=\ell^{e-1}(\ell-1)
\mid\lambda(K)\mid\Lambda.
\]

For odd `ell`, `phi(ell^e) >= e`. Thus `Lambda+1 >= e`. If a divisor
`d=ell^a c` of `m` has `a>=1`, then

\[
v_\ell(d^{\Lambda+1})=a(\Lambda+1)\ge e.
\]

If `a=0`, Carmichael reduction is legal and gives
`c^(Lambda+1)=c mod ell^e`. The surviving divisors are exactly the divisors
of `m_(ell)`. This proves (A1), including every valuation of `m` and every
prime-power exponent `e`.

The coefficient of

\[
\mathcal H_\ell=(\ell E_2(\ell\tau)-E_2(\tau))/24
\]

is

\[
\sigma_1(m)-\ell\mathbf 1_{\ell\mid m}\sigma_1(m/\ell).
\]

For `m=ell^v u`, the two geometric sums cancel to `sigma_1(u)`. This is
an integer identity, not a modular division. The standard `E_2` anomaly
cancels in this level-`ell` combination. The packet reduces only positive
coefficients, so its rational constant term causes no reduction problem.
Finally, `(N,K)=1` makes every local rough part of `N` equal to `N`; CRT
then proves (A3).

I found no hidden use of Euler or Carmichael reduction on a nonunit.

## 3. First eta quotient at an arbitrary `r`-adic valuation

For `1<=j<r`,

\[
\frac{(-1)^j}{r}\binom rj\equiv-j^{-1}\pmod r.
\]

Consequently each Euler factor satisfies

\[
\frac{(1-x)^r}{1-x^r}
\equiv 1-r\sum_{j=1}^{r-1}\sum_{h\ge0}j^{-1}x^{j+hr}
\pmod {r^2}.
\]

When the factors are multiplied, every product of two nonconstant
corrections is zero modulo `r^2`. At index `m=r^v u`, a contribution is
exactly a factorization `m=ab` whose cofactor `b` is not divisible by `r`.
Such cofactors are precisely `b=u/c` with `c|u`. Hence

\[
\sum_{c\mid u}b^{-1}
\equiv u^{-1}\sum_{c\mid u}c
=u^{-1}\sigma_1(u)\pmod r.
\]

This accounts for every `v>=0`; no factor `r^v` is dropped. The congruence
modulo `r^2` first proves that every positive coefficient is divisible by
`r`, so the displayed quotient by `r` is an integer residue and not an
illegal modular inverse. At `N=2r+1`, `v=0` and `N^(-1)=1 mod r`, which
gives (B2).

## 4. Big-Witt rough-part invariant

On ghost coordinates, ring addition and multiplication keep the index
fixed. Reading a Frobenius gate inward replaces `m` by `dm`. A nonzero
Verschiebung dependency replaces `m` by `m/d`, only when `d|m`. If every
allowed `d` has prime support inside `K`, both moves change only valuations
at primes dividing `K`. They preserve

\[
\rho_K(m)=m/\prod_{\ell\mid K}\ell^{v_\ell(m)}.
\]

Induction over the dependency graph proves (C1). A zero Verschiebung path
creates no dependency and cannot violate the invariant. Public constants,
fan-out, and ring gates do not mix indices.

Because `(N,K)=1`, `rho_K(N)=N`. If an output coordinate `s<N` depended on
input coordinate `N`, the invariant would require `rho_K(s)=N`, impossible
because `rho_K(s)<=s`. The conclusion is therefore exact for the declared
ghost circuit model. It does not cover coefficient convolution, Cartier
operators, arbitrary index-mixing gates, or an oracle-like constant that
already contains the unknown value; the statement excludes these cases.

## 5. Theta projection and the cusp witness

With `k=(r+1)/2`, characteristic-`r` Frobenius gives

\[
\vartheta^{4k}=\vartheta^{2r+2}
\equiv\vartheta(q^r)^2\vartheta(q)^2\pmod r.
\]

Only quotient exponents `0,1,2` can contribute at `N=2r+1`. Since
`R_2(0)=1`, `R_2(1)=R_2(2)=4`, convolution gives exactly

\[
R_2(N)+4R_2(r+1)+16.
\]

I independently checked the fragile Eisenstein projection. For weight
`w=2k`, the constants of `E_w(tau),E_w(2tau),E_w(4tau)` at the cusps
`infinity,0,1/2` are

\[
(1,1,1),\qquad(1,2^{-w},2^{-2w}),\qquad(1,1,2^{-w}).
\]

The corresponding theta constants are `1`, `(-1)^k 2^(-w)`, and `0`.
Solving the three equations makes the coefficient of `E_w(tau)`

\[
\frac{(-1)^k}{2^{2k}-1}.
\]

The other two degeneracy forms have no odd-index coefficient. This gives
(D3) with the stated sign and normalization.

For every prime `r>3`, `r+1` is congruent to `2 mod r-1`, while `r-1`
does not divide `r+1`. Kummer's congruence therefore applies with
`r`-integral Bernoulli value and gives

\[
B_{r+1}/(r+1)\equiv B_2/2=1/12\pmod r.
\]

Together with `2^(r+1)-1=3 mod r` and `4k=2 mod r`, this reduces the
projection scalar to `(-1)^(k+1)8`. Every divisor of `N` is an `r`-unit,
so `sigma_r(N)=sigma_1(N) mod r`.

At `r=17`, `N=35`, and `k=9`, the two-square formula gives
`R_2(35)=0` and `R_2(18)=4`. Thus the full theta coefficient is
`32=15 mod 17`. Also `sigma_1(35)=48=14 mod 17`, so the Eisenstein
coefficient is `8*14=10 mod 17`. Their difference is `5 mod 17`.
The smaller eligible primes give only the listed cases; `r=7, N=15` has
zero difference. The example and its minimality claim are correct.

## 6. Nonperiodicity of the affine Cartier section

Assume eventual period `T>0` for

\[
b_r(j)=\sigma_s(rj+1)\pmod r,
\]

where `r` is any prime and `s` is any positive integer. Dirichlet's theorem
provides a prime `ell=1 mod rT`. Put

\[
j_a=(\ell^a-1)/r.
\]

These are integers, tend to infinity, and satisfy

\[
j_{a+1}-j_a=\ell^a(\ell-1)/r=0\pmod T.
\]

The exact input on this subsequence is the prime power
`r j_a+1=ell^a`. Since `ell^s=1 mod r`,

\[
b_r(j_a)=1+\ell^s+\cdots+\ell^{as}=a+1\pmod r.
\]

Consecutive exponents give unequal values although their indices have the
same residue modulo `T`. Taking `a` beyond the eventual threshold is the
required contradiction.

This proof also covers `r=2`: Dirichlet applies to the reduced class
`1 mod 2T`, and consecutive values differ by `1 mod 2`. It covers every
prime-power input exponent `a`, every period even when `r|T`, and every
positive `s`. No density assumption is present.

An explicit constant-coefficient affine recurrence of finite order over
`F_r` becomes a deterministic finite-state linear update after one
constant coordinate is adjoined. Its state, and hence its output, is
eventually periodic. The same is immediate for a homogeneous recurrence.
A rational power series over `F_r` has a constant-coefficient recurrence
after a finite prefix, so its coefficients are eventually periodic over
the finite field. Therefore the proved nonperiodicity excludes all three
claimed classes: homogeneous recurrences, affine recurrences, and rational
sections. It does not exclude nonlinear, growing-state, or single-digit
identities as `r` varies.

## 7. Failed remote run and scope

The preserved failure hashes are:

| Artifact | SHA-256 |
|---|---|
| `failed_run_01/EXIT_STATUS` | `743c7850cccfba5e53a9002663ec1ddd1079315a98bdbfdde10e6044f56abefe` |
| `failed_run_01/RUN.stderr` | `4939cc77c948270938337ed67a692628a6bede06223806df52b0853a3553fd0b` |
| `failed_run_01/RUN.stdout` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `failed_run_01/MANIFEST.md` | `e0ac20bec9b7a2a653ffb8eb348b59c0a70c6bf16fc86801d3b9edfe2d974e6e` |

The exit status is `127`. Stderr is exactly
`nice: '/usr/bin/time': No such file or directory` apart from typographic
quote style, stdout is empty, and no `RESULT.json` exists. This is
consistent with failure before Python execution. The frozen source and
preregistration hashes in the failure manifest match the local files.

The exact witness in Theorem D is derived inside the proof. The other
theorems are symbolic. No proof step cites a search row, survivor count,
remote output, or empirical pattern. Thus the failed launch reduces no
mathematical evidence quality because F218 makes no empirical claim.

The packet remains a boundary result. It neither evaluates
`sigma_1(N) mod K` in quasipolynomial time nor proves a lower bound against
general coefficient algorithms. The duplicated phrase around the
odd-index sentence in `PROOF.md` is a harmless editing blemish and has no
semantic effect.
