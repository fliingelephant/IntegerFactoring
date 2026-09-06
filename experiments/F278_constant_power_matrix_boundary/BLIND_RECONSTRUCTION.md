# F278 blind reconstruction

## Blind boundary and verdict

This reconstruction used only `STATEMENT.md`, authenticated before reading as

```text
4232a1007700802b25acafed944f7b5adc227a913af26aec8ab6b17a7bdba0fa  STATEMENT.md
```

I did not read the proof, audits, provenance, manifest, hostile audit, or related commentary before sealing this file.

**Verdict: PASS, with two interpretation qualifications.** The five positive theorems, the endpoint bounds, and the exclusions follow from elementary matrix algebra over the two CRT fields. The statement does not prove a lower bound or a complete classification. In Theorem C, “rank losses” cannot mean loss of rank of the invertible matrix `C^B`; it can only mean loss of rank in a collision-sensitive construction such as a Vandermonde or spectral-separation observable. In Theorem E, the recurrence-to-matrix direction is the standard public state-space representation, with a public initial vector and public coordinate functional; a recurrence term need not literally be an unaugmented entry of the companion-matrix power.

## 1. Balanced endpoint arithmetic

Let `N=pq` with distinct odd primes `p<q<2p`, and let `B=floor(sqrt(N))`. Since

\[
 p^2<pq<q^2,
\]

we have `p<=B<q`. The balance condition also gives `B<q<2p`. Hence there is a unique integer `s` with

\[
 B=p+s,\qquad 0\le s<p.
\]

No prime divisor of `N` other than `p` or `q` exists. The bounds `p<=B<q` show that `q` never divides `B`, while `p` divides `B` exactly when `B=p`, equivalently `s=0`. Therefore

\[
 \gcd(B,N)=p\quad\Longleftrightarrow\quad s=0,
\]

and the gcd is one otherwise. After this screen, `1<=s<p`, and `B` is a unit modulo both hidden primes.

The hypotheses `h<=d<=B` and `d<p` are explicit restrictions, not conclusions for every input. If `d(N)<=exp((log n)^{O(1)})` and `n=ceil(log_2 N)`, then `d=exp(o(n))`, whereas a balanced hidden prime has `log p=Theta(n)`. Thus `d<p` eventually. This leaves exactly the exceptional small inputs excluded by the statement.

## 2. The numerical-quasipolynomial endpoint

Binary powering computes `C_N^B` with `O(log B)=O(n)` matrix products. Naive multiplication of two `d by d` matrices takes `O(d^3)` additions and multiplications in `Z/NZ`. Each such ring operation has bit cost polynomial in `n`. Thus the total cost is

\[
 O\!\left(n d^3\operatorname{poly}(n)\right)
 =\exp((\log n)^{O(1)}).
\]

Storing a constant number of matrices takes `O(d^2)` residues, or `O(d^2 n)` bits, which is also numerical quasipolynomial. Construction of the explicit input matrix has the stipulated bound; its full output already has `d^2` entries. Consequently both fixed dimension and the allowed quasipolynomial dimension satisfy the state and endpoint bounds. This argument evaluates the complete power. It does not identify any coordinate, determinant, minor, discriminant, or other factor-bearing observable.

## 3. Jordan blocks are direct falling-window tests

For the nilpotent shift `J_h`, we have `J_h^h=0`. Since `alpha I` commutes with `J_h`, the binomial theorem over `Z/NZ` gives

\[
 (\alpha I+J_h)^B
 =\sum_{j=0}^{h-1}\binom Bj\alpha^{B-j}J_h^j.
\]

Fix `1<=j<h`. The assumptions give `j<h<=d<p<q`, so `j!` is a unit modulo `N`. With

\[
 D_j=B(B-1)\cdots(B-j+1),
\]

the identities `D_j=j! binom(B,j)` and `gcd(alpha,N)=1` show that the three quantities `D_j`, `binom(B,j)`, and `binom(B,j)alpha^{B-j}` have the same gcd with `N`.

Every factor in `D_j` is positive and at most `B<q`, so none is divisible by `q`. The interval of its factors is

\[
 [B-j+1,B]=[p+s-j+1,p+s].
\]

It contains `p` exactly when `p+s-j+1<=p`, namely exactly when `j>s`. Its length is `j<p`, so it cannot contain two multiples of `p`. Therefore

\[
 \gcd\!\left(\binom Bj\alpha^{B-j},N\right)=p
 \iff j>s
 \iff \gcd(D_j,N)=p,
\]

and all these gcds are one when `j<=s`. Some nonconstant Jordan diagonal signals a factor precisely when an index `j` in `1,...,h-1` exceeds `s`, equivalently `s<h-1`.

Taking all `j<=h-1` tests whether `p` occurs in

\[
 B,B-1,\ldots,B-h+2.
\]

Thus the Jordan block is exactly a direct scan of `h-1` consecutive integers. A quasipolynomial-width block gives only a quasipolynomial-width near-square window.

There is no second signal hidden in the local Jordan structure. After the boundary screen, for either `r` in `{p,q}` and nonzero local eigenvalue `lambda`, the coefficient of `J_h` in

\[
 (\lambda I+J_h)^B-\lambda^B I
\]

is `B lambda^{B-1}`, which is nonzero modulo `r`. Therefore composition by `X^B` preserves that block's nilpotent index. A zero-eigenvalue block is killed because `J_h^B=0` when `h<=B`, and this happens in both CRT components. A represented change of basis preserves these conclusions only when its determinant and every denominator are units modulo `N`; the argument does not construct a hidden local Jordan basis.

## 4. Semisimple collisions are ratio-torsion events

Over an algebraic closure of `F_r`, an invertible semisimple `C` is diagonalizable with distinct eigenvalues `alpha_1,...,alpha_m`, and `C^B` has eigenvalues `alpha_1^B,...,alpha_m^B`. Hence, for `i!=j`,

\[
 \alpha_i^B=\alpha_j^B
 \iff (\alpha_i/\alpha_j)^B=1,
\]

because every eigenvalue is nonzero. This is exactly a finite-extension multiplicative-order condition.

If `chi_C` is separable modulo `r`, each input eigenvalue has multiplicity one. The discriminant of `chi_{C^B}` is zero precisely when two roots of that polynomial coincide. By spectral mapping, this is precisely the ratio-torsion event above. If `det(C)` or `Disc(chi_C)` has a proper gcd with `N`, the factor is visible before exponentiation; requiring both to be CRT units isolates the clean powering event.

This proves the collision and discriminant claims. It does not reduce a general coordinate sum of three or more powered eigenmodes to a collision. Also, since an invertible `C^B` itself has full rank, any “rank loss” in this paragraph must refer to an auxiliary collision-sensitive matrix or observable, not to `rank(C^B)`.

## 5. Quadratic companions reduce to split-group or torus residuals

For

\[
 C=\begin{pmatrix}t&-\delta\\1&0\end{pmatrix},
\]

the characteristic equation is `C^2=tC-delta I`. Starting with `U_0=0`, `U_1=1`, induction using `U_{k+1}=tU_k-delta U_{k-1}` gives

\[
 C^k=U_kC-\delta U_{k-1}I.
\]

In particular, `(C^B)_{2,1}=U_B`.

Fix a hidden prime `r`. The unit condition on `delta Delta` makes the two roots `alpha,beta` distinct and nonzero in the quadratic etale algebra. The usual Binet identity is therefore valid:

\[
 U_B=\frac{\alpha^B-\beta^B}{\alpha-\beta}.
\]

Since `alpha-beta` and `beta` are units,

\[
 U_B=0\pmod r
 \iff (\alpha/\beta)^B=1.
\]

Set `z_r=alpha/beta`. If the polynomial splits, then `z_r` lies in `F_r^*`, so `z_r^{r-1}=1`. If it is irreducible, Frobenius exchanges the roots. Thus

\[
 z_r^r=\alpha^r/\beta^r=\beta/\alpha=z_r^{-1},
\]

so `z_r^{r+1}=1`; this is the norm-one torus.

At the smaller prime, `B=p+s`. In the split case,

\[
 z_p^B=z_p^{p-1}z_p^{s+1}=z_p^{s+1}.
\]

In the irreducible case,

\[
 z_p^B=z_p^{p+1}z_p^{s-1}=z_p^{s-1}.
\]

These give exactly the two displayed residual laws, including their literal group interpretation when an exponent is zero or negative. Finally,

\[
 \gcd(U_B,N)=p
\]

holds exactly when the applicable law holds modulo `p` and `z_q^B!=1`; exchanging the primes gives the symmetric statement. Nothing in the hypotheses forces the two local truth values to differ. The quadratic mechanism is therefore an ordinary unit-group or norm-one-torus order test, not an all-input factor law.

## 6. Matrix powers and `N`-dependent recurrences have the same endpoint

For a fixed `N`, Cayley-Hamilton is valid over the commutative ring `Z/NZ`:

\[
 C_N^d+c_{d-1}(N)C_N^{d-1}+\cdots+c_0(N)I=0.
\]

Multiplication by `C_N^k` gives the stated matrix recurrence for every `k>=0`. Applying any fixed coordinate functional shows that every entry sequence satisfies a homogeneous scalar recurrence of order at most `d`. Its coefficients may depend on `N`, but for that input they do not depend on `k`.

Conversely, put the `d` current values of a public order-`d` homogeneous recurrence into a state vector. The standard public companion transition advances this vector by one index. A requested term is a public coordinate functional applied to a power of that companion matrix and the public initial state. Computing the full power, followed by this public matrix-vector and coordinate operation, remains within the same endpoint bound. This is the precise state-space sense in which the two models are endpoint-equivalent; it is not a claim that every recurrence term is literally one fixed entry of the bare companion power.

Because the recurrence coefficients may be arbitrary numerical-quasipolynomial functions of `N`, this equivalence supplies no recurrence lower bound. Such coefficient construction may itself encode unrelated public work. Only the three named mechanisms have been classified.

## 7. Frobenius and additive exclusions

In characteristic `r`, spectral mapping sends an eigenvalue `alpha` of `C` to `alpha^r` under the ordinary matrix power `C^r`. This local identity does not provide one public CRT-glued Frobenius operator: the relevant characteristic and local algebra differ across the hidden CRT components. At the smaller prime, the available public exponent satisfies

\[
 C^B=C^{p+s}=C^pC^s,
\]

and the unknown residual `C^s` remains. The ratio-torsion and quadratic residual formulas are exact reductions in their stated cases; they do not remove this residual in general or construct the hidden local operator.

For dimension at least three, a coordinate may instead be an additive exponential sum

\[
 \sum_{i=1}^m a_i(N)\alpha_i^B,\qquad m\ge3.
\]

Such a sum can vanish through additive cancellation while all powered eigenvalues remain distinct. The collision proof therefore does not classify it. Allowing the public coefficients to depend on `N` makes a universal negative conclusion even less justified. The statement correctly leaves this class open and supplies neither an impossibility theorem nor an exact all-input factor law for it.

## 8. Search disposition, scope, and nonclaims

The proposed named searches have already reduced to exact familiar tests:

- Jordan coefficients are the direct consecutive-integer scan.
- Semisimple collisions are finite-field ratio-order tests.
- Quadratic companions are split-group or norm-one-torus residual tests.

Thus no new numerical or C++ search follows from those mechanisms alone. This is a scoped research disposition, not an impossibility result. A higher-dimensional additive search would first need an exact all-input local law and an explicit public coefficient construction. Finite samples cannot prove such a law.

The proofs above establish none of the following: a universal lower bound for matrix-power entries or recurrences; a classification of arbitrary additive sums with at least three modes; an impossibility result for `N`-dependent coefficients; an impossibility result for nonlinear, semilinear, adaptive, digit, or implicit-state algorithms; a public CRT-glued local Frobenius operator; an all-input factoring algorithm; or any computational or empirical result. These seven nonclaims are necessary and consistent with the proved boundary.

## Final assessment

All displayed identities and endpoint bounds check. The Jordan and quadratic conditions are equivalences, not heuristics. The semisimple result is exactly a multiplicative ratio-torsion statement. The recurrence result is an endpoint equivalence, not a lower bound. The Frobenius and additive paragraphs correctly delimit what the named proofs do not establish. Subject to the two interpretation qualifications stated at the start, the packet is mathematically sound.
