# F244 hostile audit

## Verdict

**PASS.** I found no false claim, missing hypothesis, reversed inequality, or
hidden conjectural input in the authenticated packet.  The positive result is
an exact consequence of prime-by-prime valuations and the verified F242 clean
powered law.  The negative result is an unconditional existential construction
inside its stated signed-power-word and common-order scope.

No numerical evidence was needed.

## Authenticated frozen inputs

I computed the hashes before reading any packet content.  All five observed
SHA-256 digests matched the supplied values exactly.

```text
ace1c3ec745c64b4ac9383b8620720791a3c87b065307a2702baa63f1607a70a  STATEMENT.md
9a5030717a6611ad56dc8f013f6dc59e81bd93cf63e9a825e60a01e4688979be  PROOF.md
fe6d85b9e64f80aee4fbc9379ea6b353b79da8042af7bd3566460a40a5db95ee  SELF_AUDIT.md
7e43e5614e223dfd9caaa95da14f087a89df7287921ba2398cb7c10289b67bbd  PROVENANCE.md
ca15aee041692755293a652efb9c6e58c11a2f72009a9377cf92f95bd9700a81  MANIFEST.md
```

I did not edit any frozen input or durable ledger.

## 1. Lcm and residual conservation laws

The odd-prime argument is exact.  An odd prime divides at most one of
`p-1,p+1` and at most one of `q-1,q+1`.  Its valuation in the unique relevant
shifted gcd is therefore `min(v_ell(A),v_ell(B))`.  This gives the complete odd
part of `G` in the lcm.  The same prime has residual valuation

```text
max(v_ell(A)-v_ell(B),0) + max(v_ell(B)-v_ell(A),0),
```

and only one summand can be positive.  This proves both odd-prime pairwise
coprimality and the odd part of the product formula.

At two, the shifted valuations are `{1,U-1}` and `{1,V-1}`.  Hence the lcm
valuation is

```text
max_{a,b} min(v2(p-a),v2(q-b)) = min(U,V)-1 = v2(G)-1.
```

The total residual valuation is

```text
max(U-1-V,0) + max(V-1-U,0)
  = |U-V| - 1_{U != V}.
```

Again only one term can be positive.  Thus the four residuals are pairwise
coprime also at two, and equations (4) and (6) have the claimed powers of two.
The strict inequality in (7) is valid because `AB<N^2`; no quarter-power
conclusion is inferred.

## 2. F242 bridge and four-orientation averaging

For orientation `(a,b)`, put `m=p-a`, `r=q-b`, and `J=ab`.  Direct reduction
gives

```text
gcd(m,N-J) = gcd(p-a,q-b)
```

and the symmetric identity on the `q` side.  Choosing the public
Jacobi-dependent word `W_J=N+J` gives `E=N^2-1`.  Therefore the complete local
residual is

```text
(p-a)/gcd(p-a,N^2-1)
  = (p-a)/gcd(p-a,q^2-1)
  = t_{p,a},
```

with the symmetric formula for `t_{q,b}`.  This also verifies that no common
factor is lost or counted twice between F242's base and word residuals.

The fact that `W_J` changes with the public Jacobi sign causes no averaging
gap.  Conditional on each retained unit discriminant, F242 applies to that
public word; all four sign pairs remain equiprobable because the discriminant
is chosen first and only coefficient pairs are resampled.  Thus

```text
(1/4) sum_{a,b} S_{a,b}
 >= (1/8) sum_{a,b} max(1/t_{p,a},1/t_{q,b})
 >= (1/8) (sum_a 1/t_{p,a} + sum_b 1/t_{q,b}).
```

AM--GM gives (9), and substitution of (6) with `AB<N^2` gives the strict
constant in (10).  The conditioning, factor `1/2`, orientation factor `1/4`,
and final AM--GM factor all have the stated directions.

## 3. Signed-power valuation laws

Equations (11) and (12) are the standard odd-prime LTE cases with all needed
conditions present.  If `h=ord_ell(N)`, a minus word has support exactly when
`h|k`.  A plus word has support exactly when `h` is even and
`k=(h/2)u` for odd `u`.  In the latter case LTE applies to
`(N^(h/2))^u+1`.  The exclusion `ell|N` and the restriction to odd `ell`
remove all exceptional cases.

## 4. Sequential CRT--Linnik family

The construction is genuinely sequential.

1. Bertrand first supplies four fixed, distinct primes in disjoint intervals.
2. The first CRT class is reduced modulo
   `24 lambda_+ lambda_- rho_+ rho_-`.  Linnik then supplies `p`.
3. Only after `p` is fixed, every prime power in `p^2-1` is included in the
   second CRT system.  The `rho` primes are absent from this support because
   the imposed order of `p` modulo each is greater than two.
4. Every second-stage residue is a unit.  The moduli are pairwise coprime, so
   Linnik supplies `q` in one reduced arithmetic progression.

Primitive roots are chosen as residues modulo already selected primes.  The
proof never asks a fixed integer to be primitive for infinitely many primes.
It therefore uses neither Artin's conjecture nor a simultaneous-prime
conjecture.  Linnik is invoked only after each complete reduced residue class
is fixed.

The two Linnik size estimates also close correctly.  The first modulus is
`O(X^4)`, so `p<X^C` for an absolute `C`.  The second modulus is at most

```text
3(p^2-1) rho_+ rho_- = O(p^2 X^2),
```

so `q<X^C'` for another absolute constant.  The congruences
`p=1 mod lambda_+` and `q=1 mod rho_+`, together with primality, force
`p,q>X`.  Hence `n=Theta(log X)`.  A fixed positive `c` then makes all four
selected primes exceed `2^(cn)` on the tail.  Since `N>X^2`, an unbounded
sequence of `X` gives infinitely many distinct semiprimes.

## 5. Exact shifted gcd table

The local congruences determine every common prime.

- `p=13 mod 24` gives `v2(p-1)=2`, `v2(p+1)=1`, and `3|(p-1)`.
- `q=3 mod 8` gives `v2(q-1)=1` and `v2(q+1)=2`.
- `q=2 mod 3^max(e,2)` gives `v3(q+1)=1` and `3` does not divide `q-1`.
- For each prime `s>=5` dividing `p^2-1`, the second CRT residue is neither
  sign modulo `s`.  Hence `s` does not divide `q^2-1`.

These cases exhaust the support of `p^2-1`.  Thus `G=2^3*3=24`, and locating
the two- and three-primary parts among the signs gives exactly

```text
(d_{+,+}, d_{+,-}, d_{-,+}, d_{-,-}) = (2,12,2,2).
```

There is no unhandled future divisor of `q^2-1`; a common divisor must already
divide the fully handled integer `p^2-1`.

## 6. Primitive order after multiplication by a sign

Let `g` have order `ell-1`.  Multiplication by `-1` replaces `g` by
`g^(1+(ell-1)/2)`.  Since

```text
gcd(ell-1, 1+(ell-1)/2) is 1 or 2,
```

the new order is exactly `ell-1` or `(ell-1)/2`.  Multiplication by `+1`
does nothing.  Equations (31) and (32) are therefore valid for every one of
the four signs.  This also shows that the F242 base misses the selected prime:
a primitive root modulo a prime greater than five is neither sign.

## 7. Quantifier over adaptive signed-power words

If a selected prime divides `N^k-1`, its order is at most `k`.  If it divides
`N^k+1`, its order is at most `2k`.  The lower order bound from the preceding
section therefore proves the no-hit condition (33).

Every factor `|N^k-sigma|` is greater than one and has binary length at least
`k`; the positive product has length at least that of each factor.  Hence the
largest exponent `K` is at most the numerical bit length of the final word.
For every fixed numerical-quasipolynomial `Q`, `Q(n)=2^{o(n)}`.  The selected
primes are `2^{Omega(n)}`, so condition (33) holds eventually for every factor
in every word of length at most `Q(n)`.

This argument is pointwise in the final exponents and signs.  It does not
assume that they were selected nonadaptively.  Positive multiplication gives
no cancellation mechanism, so adaptivity cannot evade the bit-length bound
inside grammar (17).  Exponents `e_j` also cannot introduce a missed prime.
Equation (18) follows with the stated quantifier order.

## 8. Powered and incidental success probabilities

For orientation `(a,b)`, `lambda_a` survives both the base and word on the
`p` side, and `rho_b` survives on the `q` side.  Thus the two F242 residuals
are multiples of these primes.  Its exact clean law is at most the sum of the
two local return probabilities, giving (19).

The incidental exits have the claimed scale.  A random discriminant is a
proper zero divisor with probability `O(1/p+1/q)`.  For a coefficient pair,
the coefficient screen costs `O(1/p^2+1/q^2)`.  A split local norm vanishes on
`2r-1` of `r^2` pairs, while a nonsplit norm vanishes only at zero, so norm-gcd
exits cost `O(1/p+1/q)`.  Clean acceptance is at least `16/81`; therefore the
expected number of coefficient samples before acceptance or an earlier factor
exit is bounded by `81/16`.  The complete incidental probability per outer
trial is consequently `O(1/p+1/q)=2^{-Omega(n)}`.  Multiplication by a
numerical-quasipolynomial number of trials preserves an exponential bound.

## 9. Common-order and scope boundary

Every exact common element order in orientation `(a,b)` divides
`gcd(p-a,q-b)=d_{a,b}`.  Taking any number of such orders across all four
orientations therefore gives lcm dividing `lcm(2,12,2,2)=12`.  For `t>=2`,
`lcm(2^t,12)=3*2^t`, so (20) is exact.

The obstruction does not extend beyond the stated model.  In particular, the
proof does not rule out difference, quotient, carry, discriminant-dependent,
or retained-relation sources, and it does not establish a general factoring
lower bound.  The packet states each of these exclusions.  The sentence about
a numerical-quasipolynomial number of trials is valid for the specified F242
signed-word trials and their enumerated sampler exits; it must not be read as a
claim about algorithms that retain or exploit additional transcript data.

## Final result

**PASS.** All frozen mathematical claims survive hostile audit within the
packet's explicit boundary.  No correction is required.
