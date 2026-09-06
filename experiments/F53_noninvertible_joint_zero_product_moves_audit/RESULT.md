# Hostile whole-proof audit of F53

## Verdict

**FAIL AS WRITTEN.**

Pinned candidate:

```text
040407be820f014a7e2cae3a8c2b28af62fb1b1b8ee35ea16ad48f5875d575ed  experiments/F53_noninvertible_joint_zero_product_moves/RESULT.md
```

This equals the expected hash. I read that artifact and the closest promoted
result, F35/P45, in full.

The local low-degree lemma in Section 1 is correct. The failure is in the
claimed material consequence. Once F53 screens both coordinates after every
move, the path invariant and the factor-or-TV reduction no longer use the
low-degree lemma, polynomial maps, coefficient screens, or even a Markov
transition. They follow directly from the definition of the zero-product
set. Thus F53 does not, as written, close the noninvertible joint-move route.
It leaves the central new possibility -- factor-asymmetric roots of a
synchronized noninvertible restriction -- wholly unbounded and simply calls
such an occurrence a successful output gcd.

There is also a separate uniform-cost error: pointwise TV error
`delta_N < 1/2` does not by itself give an expected-polynomial repeated
splitter. A uniform inverse-polynomial success gap is required.

## 1. The exact point where the advertised consequence becomes universal

For `N=pq`, define

```text
A_N = (R^x x {0}) union ({0} x R^x) union {(0,0)}
B_N = Omega_N \ A_N.
```

For every `(k,x) in Omega_N`, the following are equivalent:

1. neither coordinate has a proper gcd with `N`;
2. each coordinate is either zero or a unit;
3. `(k,x) in A_N`.

The only non-immediate step is `2 => 3`: two units cannot have zero product,
and if one coordinate is a unit then the other must be zero. Consequently,

```text
B_N = {(k,x) in Omega_N :
       gcd(k,N) or gcd(x,N) is a proper factor}.
```

This identity has three consequences.

First, after an output-coordinate screen, every safe output of **any** map
into `Omega_N` lies in `A_N`. No assumption on the input or on the map is
needed. Section 2's low-degree synchronized-axis argument is therefore
logically redundant.

Second, the pathwise induction in Section 3 holds for arbitrary adaptive,
randomized, non-polynomial, high-degree, state-stitched, or opaque
`Omega_N`-valued transitions, provided their exposed output coordinates are
screened. It is not an obstruction specific to the F53 move class.

Third, screening only the terminal output already gives

```text
Pr(H) >= mu_N(B_N)
      >= pi_N(B_N) - ||mu_N-pi_N||_TV.
```

Thus Section 4 is numerically correct, but it is the direct zero-product
decoder. It is not evidence that low-degree noninvertible moves fail to
create a useful sampler.

## 2. Comparison with F35/P45

F35 used bijectivity in an essential way. Over each local field, bijectivity
made an active axis restriction send every nonzero input to a nonzero output.
That proved forward invariance of `A_N` after coefficient screens alone; F35
did not need to inspect every realized output coordinate.

F53 removes bijectivity, so an active one-variable polynomial can have roots.
It then adds output-coordinate gcd screens. Those screens directly recognize
every point outside `A_N`. This does not extend F35's coefficient-only
invariant. It replaces the lost invariant with the target decoder itself.

The part that does survive as a genuine extension is narrow:

- on each source axis, low degree forces at least one restricted output to be
  the zero polynomial in each CRT field;
- absent a proper coefficient gcd, the formal zero/nonzero pattern is the
  same in the two fields;
- unlike F35, both restrictions may be zero, and the active restriction may
  have roots.

This is a valid local restriction-classification lemma. Its root-counting
core was already present in F35 Section 2; dropping bijectivity adds the
collapse and root cases. It does not support F53's stronger claim that the
noninvertible joint-move reopen condition is closed.

## 3. Detailed proof audit

### 3.1 Local CRT lifting -- PASS

Given a point on one local axis over `F_r`, completing the other CRT component
with the origin gives a global point of `Omega_N`. Reducing its global image
shows that the chosen local image has zero product. No surjectivity or
injectivity is used.

### 3.2 Root counting -- PASS

On one source axis, `F_r(Z)G_r(Z)` has degree at most `2D < r` and vanishes
at all `r` field elements. It is therefore the zero polynomial. Since
`F_r[Z]` is an integral domain, at least one factor is formally zero. The
same argument applies to both source axes and both primes.

### 3.3 Coefficient-pattern synchronization -- PASS

If no restricted coefficient has a proper gcd with `N=pq`, each coefficient
is either zero modulo both primes or nonzero modulo both. Hence each whole
restriction is formally zero modulo `p` exactly when it is formally zero
modulo `q`. Combining this with root counting gives the same one of
`(nonzero,zero)`, `(zero,nonzero)`, or `(zero,zero)` in both fields.

This synchronizes only the **formal restriction pattern**. It does not make
the two evaluations at a given unit simultaneously zero or simultaneously
nonzero. The conclusion and framework discussion must preserve this
distinction.

### 3.4 Axis collapse -- PASS

Both restricted outputs can be the zero polynomial when bijectivity is
absent. This case is correctly included.

### 3.5 Pathwise induction -- TRUE BUT NOT A CONSEQUENCE OF SECTION 1

The stated induction is valid. However, each induction step follows from the
output's membership in `Omega_N` plus its two coordinate screens. The input
state, polynomial representation, degree bound, and coefficient screens are
irrelevant. It cannot be used as evidence for a low-degree barrier.

### 3.6 Factor-or-TV inequality and counts -- PASS, BUT UNIVERSAL

The counts

```text
|Omega_N| = (2p-1)(2q-1),
|B_N| = 2N-2,
rho_N = (2N-2)/((2p-1)(2q-1)) > 1/2
```

are correct, as is the TV inequality. As shown in Section 1 of this audit,
terminal-coordinate screening proves it for every law on `Omega_N`; the move
analysis is not used.

### 3.7 Circuit extraction -- PASS UNDER THE STATED PROMISES

Evaluation after the two substitutions in `R[Z]/(Z^(D_N+1))` recovers every
coefficient of the four restrictions when the exact formal output degrees
are at most `D_N`. Truncating high-degree intermediate values does not alter
the final low-degree coefficients because quotient evaluation is a ring
homomorphism. The `O(D_N^2)` ring-operation bound per multiplication gate is
valid with ordinary truncated convolution.

The global `Omega_N`-preservation and exact-degree properties remain semantic
promises supplied by the sampler, as F53 correctly states.

### 3.8 Small-factor scan -- PASS

If scanning `2,...,2D_N` gives no proper gcd, neither prime factor can be at
most `2D_N`; otherwise its own integer occurs in the scan. Hence
`2D_N < min(p,q)`. With `D_N` bounded by one public polynomial, this scan is
polynomial-time.

### 3.9 Monitoring cost -- PASS; repetition claim needs correction

Under one public polynomial degree bound and an expected-polynomial total
circuit encoding length, the coefficient-monitoring overhead is expected
polynomial. Gate count is bounded by encoded length, and every gate costs a
polynomial number of bit operations.

However, `delta_N < 1/2` for each input is insufficient for an
expected-polynomial Las Vegas splitter. On balanced semiprimes,
`rho_N-1/2` is exponentially small in the input bit length. Therefore a TV
error that approaches `1/2` can leave only exponentially small guaranteed
success probability. The required hypothesis is, for example,

```text
rho_N - delta_N >= 1/poly(n),
```

or the stronger uniform condition `delta_N <= 1/2-epsilon` for one fixed
`epsilon>0`. The expected number of independent runs is the reciprocal of
that gap.

### 3.10 Exclusions -- CONFLATED

The Section 1 coefficient-classification lemma does exclude high-degree,
rational, opaque, hidden-state, and non-global branches. The terminal
factor-or-TV reduction does not exclude them: it applies to any exposed
terminal point in `Omega_N`. F53 must give these two statements separate
scopes. The current single exclusion list incorrectly suggests that all
parts of the result stop at the polynomial-map boundary.

## 4. Explicit hostile examples

### 4.1 Roots defeat the F35 invariant without a coefficient factor

Take `N=77=7*11` and

```text
T(K,X) = (K(K-1), 0).
```

This degree-two, highly noninjective map sends all of `R^2`, hence all of
`Omega_77`, into `Omega_77`, and `2D=4<7`. Its axis-restriction coefficients
are only `0`, `1`, and `-1`, so no coefficient gcd is proper. Yet

```text
(8,0) in A_77,
T(8,0) = (56,0) in B_77,
gcd(56,77) = 7.
```

Modulo 7, the active polynomial evaluates to zero; modulo 11, it does not.
This is fully consistent with F53's formal-pattern lemma. It proves that
noninjective roots can desynchronize a realized value without any
coefficient factor. Only the newly added output gcd restores the claimed
safe path. Therefore this route remains open at the algorithmic question:
can a public bare-`N` process arrange such asymmetric root hits with
inverse-polynomial probability?

### 4.2 A genuinely mixed formal pattern is coefficient-visible

Again take `N=77` and

```text
T(K,X) = (22K, 56K).
```

Since `22*56` is divisible by 77, this degree-one noninjective map sends all
inputs into `Omega_77`. The two coefficients encode the complementary CRT
idempotent supports, and their gcds with 77 are 11 and 7. This confirms the
coefficient dichotomy rather than refuting it.

### 4.3 Adaptive random branches do not repair the claimed novelty

An adaptive selector may randomly alternate globally valid collapse/root
maps such as `(K(K-1),0)` and `(0,X(X-1))`, with its choice depending on the
full transcript. No pathwise counterexample survives the output monitors:
the first visit to `B_N` is itself a proper coordinate gcd. But this is true
for every adaptive branch family, not because the branches have low degree.
Randomness therefore does not break the stated inequality, while also not
making that inequality a new obstruction.

State-stitched branches that preserve `Omega_N` only at the current point do
fall outside the Section 1 lemma, as F53 says. They still fall inside the
universal terminal-coordinate reduction if the terminal point is exposed and
lies in `Omega_N`.

## 5. Mandatory corrections before another audit

1. Reframe the promoted mathematical content as the Section 1 local
   restriction-classification lemma. Do not present Sections 2--5 as a
   low-degree consequence.
2. State and prove explicitly that `B_N` is exactly the set detected by a
   proper coordinate gcd. Then separate the universal terminal decoder from
   the representation-dependent coefficient lemma.
3. Remove the claim that this closes the noninvertible joint-block-move
   reopen condition. The root/asymmetric-evaluation mechanism remains open;
   F53 gives no probability bound for it.
4. Say "formal zero/nonzero axis pattern" wherever synchronization is meant.
   Do not imply that evaluations at the two hidden primes vanish together.
5. Separate the exclusions for the coefficient lemma from the much wider
   scope of the terminal-coordinate reduction.
6. Replace the repeated-run cost claim by a uniform condition such as
   `rho_N-delta_N >= 1/poly(n)` (or fixed error at most
   `1/2-epsilon`) and state the reciprocal-gap expected run count.

## 6. What can survive

No counterexample was found to the exact low-degree coefficient lemma. The
CRT lifting, root count, formal-pattern synchronization, collapse case,
coefficient extraction, and small-factor scan are correct. A corrected
artifact can retain those facts and the universal decoder as two explicitly
separate observations.

It cannot honestly retain the current framework-level conclusion. The
candidate does not show that noninvertible joint moves fail. It shows that
when such a move reaches the useful part of the target, the ordinary output
gcd succeeds -- which is the original factoring decoder, not a new barrier.
