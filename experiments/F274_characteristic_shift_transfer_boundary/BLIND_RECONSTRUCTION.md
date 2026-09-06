# F274 blind reconstruction

## Seal metadata

- Authenticated input: `experiments/F274_characteristic_shift_transfer_boundary/STATEMENT.md`
- Input SHA-256: `22674281efe2fc593ef8b657bc4782f1892e118a2a193c6f5028d514a245ce47`
- Pre-seal source boundary: only the authenticated statement was read. No proof, audit, provenance, manifest, ledger, history, or conversation artifact was read.
- Canonical output-payload SHA-256: `386ba5d655e9fa5955704fc73993f74b9e7253d75ed768e2bccef50366f923f0`
- Hash domain: the UTF-8 bytes strictly between the two payload marker lines below, including their terminating newlines and excluding the marker lines.
- The whole-file SHA-256 is reported externally after sealing. A file cannot embed its own ordinary whole-file digest without changing the hashed byte stream.

<!-- BEGIN SEALED PAYLOAD -->
## Verdict

**VERIFIED WITH A SEARCH-SCOPE QUALIFICATION.** The balanced endpoint, Theorems 1--4, Corollary 4.1, the telescoping formulas, and the modular-operation warnings are correct as stated. They establish exact boundaries for the named models, not evaluator or circuit lower bounds.

The sentence that no C++ search is justified is defensible as a research disposition for attempts whose only goal is to evade one of these exact classifications. It is not a theorem that all searches over the loosely described objects are futile. In particular, Theorem 3 classifies every integer-polynomial difference as `B!` times an integer, but does not rule out discovering special structure that evaluates that integer or the unnormalized difference efficiently. Likewise, the four listed future seams are not proved exhaustive of all mechanisms already declared outside scope, such as integer-valued-polynomial or adaptive algorithms. Read literally as exhaustive impossibility claims, those search sentences do not follow. Read as gates for this named characteristic-shift/rational-gauge program, they are sound.

## 1. Balanced endpoint

From `p<q`,

\[
p^2<pq=N,
\]

so `p<sqrt(N)`. Since `p` is an integer, `p<=floor(sqrt(N))=B`. Also `pq<q^2`, hence `sqrt(N)<q` and therefore `B<q`. Thus

\[
p\le B<q.
\]

No primality or balance assumption beyond `p<q` is needed for this particular inequality; primality is used later for characteristic and factorial conclusions, and balance is used for the input-length comparison.

## 2. Full characteristic shift

Let `e_y` be the indicator of `y` in `F_r`. The vectors `e_y` form a basis of `V_r`, and `T_r` permutes them in one cycle of length `r`. Consequently `T_r^r=I`. No nonzero polynomial of degree below `r` annihilates `e_0`, because its application to `e_0` is a linear combination of distinct basis vectors. Hence

\[
\mu_{T_r}(Z)=Z^r-1.
\]

In characteristic `r`, the freshman's-dream identity gives

\[
Z^r-1=(Z-1)^r.
\]

Replacing `T_r` by `I+Delta_r` gives

\[
\mu_{\Delta_r}(Z)=Z^r.
\]

Thus `Delta_r` is one nilpotent Jordan block of size `r`; equivalently, `Delta_r^r=0` and `Delta_r^{r-1}` is nonzero. One direct check is

\[
\Delta_r^{r-1}=\sum_{j=0}^{r-1}T_r^j
\]

in characteristic `r`, which maps a point indicator to the nonzero constant function. Therefore, for every nonnegative integer `k`,

\[
\Delta_r^k=0\iff k\ge r.
\]

Using `p<=B<q` gives `Delta_p^B=0` and `Delta_q^B!=0`. More precisely, the ranks are `0` and `q-B`, respectively. This is an operator statement. A chosen probe can lie in the kernel of the nonzero operator, so the rank difference alone does not give a public nonzero value modulo `q`.

## 3. Linear subquotient dimension barrier

A `T_r`-stable subspace is also `Delta_r`-stable, and `Delta_r^r=0` descends through invariant subspaces and quotients. Thus the induced operator on every stated subquotient is nilpotent. Any nilpotent endomorphism of a `d_r`-dimensional vector space has nilpotency index at most `d_r`, so

\[
\overline\Delta_r^{d_r}=0.
\]

If `d_r<=B`, every power at least `d_r`, including the `B`th power, is zero. Applying this independently at `p` and `q` proves the claimed loss of asymmetry. A reduction that lowers dimension can only lower the possible nilpotency index.

For the asymptotic statement, balance gives

\[
\sqrt{N/2}<p<\sqrt N.
\]

With `n=ceil(log_2(N+1))`, this yields `log_2 p=n/2+O(1)`, hence `p=2^{Theta(n)}`. For fixed `k`,

\[
O((\log n)^k)=o(n),
\]

so every fixed numerical quasipolynomial `Q(n)=2^{O((log n)^k)}` eventually satisfies `Q(n)<p<=B`. The conclusion concerns explicitly represented linear shift subquotients. It says nothing about a succinct representation that does not enumerate the state basis, or about matrices with no shift-subquotient intertwining.

## 4. Integer-polynomial forward differences

For every function on the integers,

\[
\delta^kF(a)=\sum_{j=0}^k(-1)^{k-j}\binom{k}{j}F(a+j).
\]

For `F(X)=X^m`, expand `(a+j)^m` and use

\[
\sum_{j=0}^k(-1)^{k-j}\binom{k}{j}j^t=k!S(t,k).
\]

This gives

\[
\frac{\delta^kX^m(a)}{k!}
=\sum_{t=k}^m\binom mt a^{m-t}S(t,k),
\]

with value zero when `m<k`. Integer linearity over the coefficients `c_m` proves both the displayed formula in the statement and

\[
\delta^kF(a)\in k!\mathbb Z.
\]

For `m=k`, only `t=k` remains, so `delta^k X^k=k!` identically; in particular its value at zero is `k!`. This proves sharpness.

At `k=B`, entrywise application gives a common factor `B!` for every integer-coefficient vector or matrix polynomial. Since `p<=B<q` and `p,q` are prime,

\[
\gcd(B!,N)=p.
\]

Thus `B!` is a nonunit and a zero divisor modulo `N`, so modular division by it is undefined. Computing the integer quotient from the Stirling-number formula is legitimate, but removes the universal factorial factor; the quotient can still have instance-specific divisibility, which the theorem neither promises nor excludes.

The coefficient boundary is real. The integer-valued polynomial

\[
\binom XB
\]

has rational monomial coefficients and satisfies

\[
\delta^B\binom XB=1,
\]

so the `B!` divisibility does not extend to all integer-valued polynomials. Treating such a value as a primitive oracle is additional computational power, not a consequence of Theorem 3.

## 5. Exact scalar rational-coboundary criterion

First suppose `R=tau(h)/h`. A nonzero rational function has the same leading asymptotic after an additive unit shift, so `h(X+1)/h(X)` tends to `1` at infinity.

Fix a translation orbit and index it as `P_j(X)=P_0(X+j)`. If `b_j=v_{P_j}(h)`, then

\[
v_{P_j}(\tau h/h)=b_{j-1}-b_j.
\]

Only finitely many `b_j` are nonzero, so summing over `j` telescopes to zero. This proves necessity of every orbit sum.

Conversely, factor `R` into a rational constant and monic irreducibles. On one orbit put `a_j=v_{P_j}(R)`. The support is finite and the stated condition gives `sum_j a_j=0`. Define

\[
b_j=\sum_{t>j}a_t.
\]

These integers also have finite support, and `b_{j-1}-b_j=a_j`. Multiplying `P_j^{b_j}` over all relevant indices and orbits constructs a rational `h` whose shift quotient has all the nonconstant valuations of `R`. Orbit balance also makes the total numerator and denominator degrees equal. Because all irreducibles are monic, the remaining factor is the limit of `R` at infinity, and condition 1 makes it `1`. Hence `R=tau(h)/h`.

Multiplication immediately telescopes:

\[
\prod_{j=0}^{m-1}R(X+j)=\frac{h(X+m)}{h(X)}
\]

for nonnegative integers `m`. Taking `h=X` gives `(X+1)/X`. The function `R=X` fails the infinity condition (and also has an unbalanced divisor orbit), so it has no rational gauge. Every nonconstant polynomial, and every affine product of positive net degree, similarly fails at infinity.

The identity lives in `Q(X)`. To use a displayed rational evaluation modulo `N`, each denominator actually inverted at the selected endpoints must be a unit. A denominator with gcd strictly between `1` and `N` reveals a proper factor. A denominator with gcd `N` is still noninvertible but reveals no proper factor. Algebraic cancellation may be performed before specialization; cancellation through an inverse that does not exist modulo `N` is invalid.

## 6. Matrix determinant obstruction and endpoint product

Taking determinants in

\[
G(X+1)=A(X)G(X)
\]

gives

\[
\det A(X)=\frac{\det G(X+1)}{\det G(X)},
\]

so the scalar criterion is necessary. Rational shift coboundaries form a multiplicative group. If `det A=X^eR_0`, with `R_0` a coboundary and `e!=0`, existence of `G` would make `X^e` a coboundary. But `X^e` tends to infinity for positive `e` and to zero for negative `e`, contradicting the necessary limit `1`. This proves Corollary 4.1.

The determinant test is not sufficient for a matrix gauge. In particular `det A=1` always passes the scalar test and supplies no information about projective or off-diagonal dynamics.

When a rational `G` does exist, substituting

\[
A(X+j)=G(X+j+1)G(X+j)^{-1}
\]

into the correctly ordered product cancels all adjacent factors and yields

\[
A(X+m-1)\cdots A(X)=G(X+m)G(X)^{-1}.
\]

This is an algebraic endpoint identity, not yet a quasipolynomial modular algorithm. Such an algorithm also needs unit denominators at every inversion and quasipolynomial descriptions, coefficient sizes, and endpoint-evaluation cost.

## 7. Search disposition

The exact negative filters are:

1. An explicit shift subquotient of dimension at most `B` cannot retain the `p/q` nilpotency asymmetry. Searching its matrices cannot change this.
2. An integer-coefficient polynomial probe of `delta^B` always contains the common integer factor `B!`. Searching coefficients cannot remove that factor while remaining in the theorem's coefficient class.
3. A rational matrix gauge whose determinant has `X^e`, `e!=0`, modulo a scalar coboundary cannot exist.
4. A scalar rational candidate is completely decided by its limit and finite divisor-orbit sums; if it passes, its full interval product is an endpoint telescope, and if it fails, no rational gauge exists.

These facts justify replacing blind numerical search for exceptions to those classifications with exact symbolic tests. They do not establish that no useful structured evaluator can exist inside a broader reading of “polynomial probe,” nor that every mathematically new route belongs to the four-item survivor list. The theorem itself leaves integer-valued-polynomial oracles, adaptive algorithms, characteristic-dependent constructions, implicit states, and nonlinear states outside scope. Accordingly, the word “only” in the future-search sentence is a program restriction, not a derived exhaustive theorem.

The proposed theory gates are valid when applicable to a claimed rational-gauge/shift-state quasipolynomial algorithm: define the state and intertwiner; apply the determinant-orbit test; prove every used denominator is a unit or handle its gcd; account for numerical coefficient and endpoint costs; forbid hidden local-characteristic or factor advice; and prove an exact `p/q` asymmetry rather than infer it from samples. Determinant and denominator audits are inapplicable, rather than failed, for models that contain no rational matrix gauge or rational inversions.

## 8. Exact controls

- Full-state control: established above, `mu_{Delta_r}=Z^r`.
- Factorial control: `delta^B X^B(0)=B!`.
- Scalar telescope: `(X+1)/X=tau(X)/X`.
- Scalar nongauge: `X` fails both the infinity and orbit tests.
- Determinant-one decoy: for

\[
G(X)=\begin{pmatrix}1&X\\0&1\end{pmatrix},
\]

direct multiplication gives

\[
G(X+1)G(X)^{-1}=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]

Its `m`-step product is `[[1,m],[0,1]]`, exactly the endpoint telescope. It records interval length, not a rising interval product. Counting it as a factor-sensitive lead would be a false positive.

## 9. Exclusions audit

All nine exclusions are necessary and consistent with the proofs:

1. The arguments classify named linear representations and rational gauges, not arbitrary arithmetic, algebraic, or Boolean circuits.
2. No uniform interval-product evaluator is constructed or ruled out.
3. Nonlinear, semilinear, characteristic-specific, adaptive, and implicit-state algorithms violate or evade the hypotheses used here.
4. The dimension theorem needs an induced regular-shift action; arbitrary finite matrix sequences need not have one.
5. Factorial divisibility is an algebraic identity and gives no cost lower bound for evaluating either the difference or its integer quotient.
6. Determinant-one systems pass the determinant test automatically, so no obstruction for them is proved.
7. No numerical quasipolynomial endpoint evaluator is supplied.
8. No complete factoring algorithm is supplied.
9. Every result is deductive; no computational or empirical result is used.

## Final classification

F274 correctly closes the explicit low-dimensional regular-shift mechanism, the attempt to erase its factorial through integral polynomial normalization, and rational gauges with a scalar/determinant obstruction. Its surviving seams and operational audits are useful research guidance. They must not be promoted to an exhaustive lower bound or a literal ban on searching outside the exactly classified grammar.
<!-- END SEALED PAYLOAD -->
