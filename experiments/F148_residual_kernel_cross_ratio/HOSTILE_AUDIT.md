# F148 hostile audit — residual-kernel cross-ratio closure

## Verdict

**PASS.** The frozen statement and proof are correct within their stated
conditional scope. The residual-kernel pairing identity, the two cleared
gcd formulas, the strict metric condition, and the quasipolynomial accounting
all survive hostile review. The registered V3 replay returns the pinned
`N=745` certificate.

This is not a source theorem. It does not construct the required cycles,
bound their residuals, or force slope diversity. The finite witness also has
an extra direct congruence of squares between its two public centers. That
weakens the witness as isolation evidence, but the frozen candidate does not
claim that every possible cross-center screen is null.

## Frozen inputs

- `STATEMENT.md`:
  `8d790d05d8161444684d109ad16c3cc1f2be453dcc04638a8d8a10406b78cc35`
- `PROOF.md`:
  `92542fe2f91fbdb26311112bef799f0f0f7d02d22ca161b34d1ca2fcf082e405`
- `MANIFEST.md`:
  `ea856e36c6034629386fd4db3f7b66bc9747c10917c3e9e2dca4dc6a37a115dd`
- `V3_PREREGISTRATION.md`:
  `b4763cb8971062fe11536f5c43242b93ab565bfb10f4838003a3876121e3fc78`
- `search_v3.py`:
  `8ab73be57082ff5f0bedf47cb23d41991f120987d01a1af79776fff5a0ac3f0a`
- `V3_OUTPUT.json`:
  `e00b51b16aadd378abe33b4f6c3a57e49e9983e0a1c6a9086b8e6c856571e379`

The preserved V1 and V2 preregistrations, searches, and rejection reports
also match the hashes recorded in the manifest.

## 1. Cycle boundary and actual-column semantics

For one edge,

\[
U_e=q_ea_e^2,
\qquad
c_e=r_eT_e,
\qquad
A_e=c_ew_e,
\qquad
B_e=U_ew_e.
\]

The matched actual-column product is

\[
A_eB_e=U_ec_ew_e^2.
\]

Around a directed cycle, `r_e=q_(e+1)`, so the center factors occur twice.
Thus

\[
\prod_e A_eB_e
=
\left(\prod_eq_ea_ew_e\right)^2\prod_eT_e.
\]

The exact square-class boundary is therefore `T_i`, as claimed. This
calculation does not require the displayed integer factors to be rational
primes or pairwise coprime.

Global first-occurrence exact-value deduplication is compatible with this
claim. All actual P128 values here are congruent to `1 mod N` and have the
same supplied root label. Removing two occurrences of one duplicate removes
an exact square and changes the positive root by a unit congruent to `1`.
The theorem additionally assumes that the two retained cycle supports are
disjoint, so their union is their binary sum without a cross-cycle
cancellation.

## 2. Pair root and signs

For cycle `i`, write

\[
Q_i=\prod_eq_e,
\qquad
W_i=\prod_ew_e.
\]

Since `c_e*w_e=1 mod N` and
`prod(c_e)=Q_i*T_i`,

\[
Q_iW_iT_i\equiv1\pmod N.
\]

If

\[
T_i=ds_i^2,
\qquad
T_j=ds_j^2,
\]

the exact positive root of the combined actual-column product reduces to

\[
\rho_{ij}
\equiv
\frac{\alpha_i\alpha_j}{ds_is_j}
\pmod N.
\]

Using `alpha_j^2=d*s_j^2 mod N` gives

\[
\rho_{ij}
\equiv
\frac{\alpha_is_j}{\alpha_js_i}
\pmod N.
\]

All denominators are units because each residual product is a unit. Clearing
the unit denominator preserves gcd with `N`. Therefore both displayed gcd
equalities in the statement are exact. There is no missing inverse or sign.

## 3. Metric theorem

Put

\[
X=\alpha_is_j-\alpha_js_i,
\qquad
Y=\alpha_is_j+\alpha_js_i.
\]

The cycle congruences imply `N | X*Y`. Under unequal slopes and `Y<N`,

\[
0<|X|<Y<N.
\]

Hence neither `X` nor `Y` is divisible by `N`. If either were coprime to
`N`, divisibility of their product would make the other divisible by `N`, a
contradiction. Both gcds are therefore strictly between `1` and `N`. This
argument also works for odd nonsquarefree composites.

For one common residual core, `z_i=alpha_i/s_i mod N` satisfies
`z_i^2=d mod N`, and the pair root is `z_i/z_j`. Thus the root is global
exactly when the two `z` values differ by a global sign. Under `Y<N`, the
minus sign is impossible. The plus sign forces `X=0`, which is exact equality
of the two positive rational slopes. The stated failure characterization is
correct.

## 4. Factor-free core and quasipolynomial cost

P66 refinement gives a common pairwise-coprime block basis for all supplied
`T_i`. Equal parity vectors are exactly equal rational square classes. For a
shared parity vector `epsilon`, the construction

\[
d=\prod_hh^{\epsilon_h},
\qquad
s_i=\prod_hh^{(e_{hi}-\epsilon_h)/2}
\]

is exact and needs no rational-prime factorization. The computed `d` need not
itself be the rational squarefree kernel; it is a common factor-free
representative, which is sufficient for every formula. Also `d<=T_i<=R`, so
there are at most `R` possible bucket labels. More than `R` explicit cycles
force a repeated bucket.

For the repeated pair, `s_i,s_j<=sqrt(R)`. The bounds `alpha_i,alpha_j<=H`
and `2*H*sqrt(R)<N` imply the strict metric inequality. Exact slope
deduplication then supplies unequal slopes.

The cost claim is conditional on an explicit quasipolynomial-size cycle
list and quasipolynomial total presentation length, as stated. Pairwise
gcd-free refinement, parity grouping, rational slope comparison, and even
all pair tests remain quasipolynomial. The metric inequality itself implies
`H<N`, so each anchor product has `O(n)` bits. No exponential integer is
hidden behind the compact notation in this corollary.

This accounting does not give an algorithm for finding the cycles. It only
decodes and compares a supplied explicit family.

## 5. Registered V3 replay and independent arithmetic checks

Running the frozen command

```text
python3 experiments/F148_residual_kernel_cross_ratio/search_v3.py
```

returns the pinned tuple

```text
N=745, d=6, a=119, b=179, u=57, v=92.
```

The certificate arithmetic is exact:

\[
119^2=19\cdot745+6,
\qquad
179^2=43\cdot745+6,
\]

\[
342\cdot403=185\cdot745+1,
\qquad
552\cdot193=143\cdot745+1.
\]

The four actual values are the four distinct integers recorded in the
statement. Direct exact-square testing of all `15` nonempty subsets finds
only the full four-value set. Its positive root is
`52128626351256`, which is `446 mod 745`. Therefore

\[
\gcd(446-1,745)=5,
\qquad
\gcd(446+1,745)=149.
\]

The smaller cross-products give the same factors:

\[
\gcd(179-119,745)=5,
\qquad
\gcd(179+119,745)=149.
\]

All four claimed canonical inverse-pair sign screens are null:
the minus gcds are `1`, and both plus arguments equal `745`.

### Finite-witness limitation

The two public centers also satisfy

\[
57^2\equiv92^2\pmod{745},
\]

so

\[
\gcd(92-57,745)=5,
\qquad
\gcd(92+57,745)=149.
\]

The same holds for several derived endpoint pairs. The V3 preregistration
did not exclude these cross-center tests, and the frozen statement claims
only that the four within-pair endpoint sign screens are null. This does not
falsify the theorem or the listed certificate. It does mean that `N=745`
does not isolate F148 from every simpler public congruence-of-squares channel.
A stronger future certificate should exclude all predeclared pairwise
center and endpoint sign screens.

## 6. Preserved rejected rounds

The V1 rejection is correct: it duplicates one canonical exact value, and
its reported normalized root divides by the supplied root a second time.
The V2 rejection is also correct: `c1=w1=24 mod 115`, so its first canonical
value is the exact square `24^2` and already gives a non-global root.

## Final scope

F148 gives a correct conditional cross-cycle decoder and a correct
conditional amortization target. It is a standard congruence-of-squares
identity expressed in the P128 retained-column language. It proves no
all-input cycle source, no success frequency, and no integer factoring
algorithm.
