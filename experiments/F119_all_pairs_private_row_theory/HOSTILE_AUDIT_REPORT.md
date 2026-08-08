# F119 hostile mathematical audit

## Verdict

**PASS_WITH_CORRECTIONS.** The exact carry laws and the infinite selected
cross-pair submatrix construction are sound. The CRT, prime-selection,
bit-length, trial-hardness, menu-eligibility, valuation, and linear-independence
arguments all close.

One scope correction is necessary. The endpoint sign-screen proof applies to
each named residue `c=a^2 b` and its canonical inverse `w_c`. If that canonical
residue appeared earlier, the earlier occurrence has the same endpoints and is
covered. If a different earlier residue `d` has the same exact value
`P_N(d)=P_N(c)`, exact-value deduplication preserves the protected value and
private row, but the proof does not show
`gcd(d-w_d,N)=gcd(d+w_d,N)=1`.

Therefore `RESULT.md` must not use “every selected endpoint sign screen” to
mean the endpoint pair attached to whichever raw residue first represented the
exact value. The correct claim is the named-residue identity

```text
gcd(c-w_c,N) = gcd(c+w_c,N) = 1  for each c in C_t.
```

`RECONSTRUCT_STATEMENT.md` states this distinction correctly. With that
correction, the strongest theorem remains an unconditional
`Theta(n/log n)` independent selected submatrix theorem. It is not a
complete-source obstruction and not an operational no-earlier-factor theorem.

## Audit scope and pins

The following five files were read in full:

| File | SHA-256 |
|:---|:---|
| `QUESTION.md` | `7dba1e0092302380bd9989d218cc144aa6026c44214ee215145285424f5e9c7f` |
| `RESULT.md` | `990952a8175733959ef8d7f67429a330c27378ba897426a81c11f536dbd8a500` |
| `FAILED_ROUTES.md` | `ff1e124d9a06a9f126876d21e06200e947084c461c4cd433c99e1319b3bebb83` |
| `MANIFEST.md` | `c465e6d76326ef2cd44003ab9150e19e71fba4f203f0fc66ddb611bb84937960` |
| `RECONSTRUCT_STATEMENT.md` | `4a4aaf43119609e7745b5f88623a3ea9fb3c72aac7d15b16062d1aef0e692986` |

The three local hashes listed by the original manifest for `QUESTION.md`,
`RESULT.md`, and `FAILED_ROUTES.md` match the exact bytes. The original
manifest also lists two files outside F119. They were not part of the assigned
audit set, so this audit does not claim to have verified their contents or
hashes.

No finite computation, external search, or empirical evidence was used. This
audit has no program run or timeout claim.

## Claim-by-claim result

| Claim | Audit result | Reason |
|:---|:---|:---|
| Carry range and unit deletion | PASS | Exact bounds follow from `1<=c,w<N`. |
| Exact-value/carry equivalence | PASS | `P_N(c)=1+kN` is injective in `k` for fixed `N`. |
| Three-way carry gcd identity | PASS | Subtraction and `gcd(1+kN,N)=1` give equality. |
| One carry class per prime row | PASS | `k=-N^{-1} mod r` for every `r` not dividing `N`. |
| Row-degree bound | PASS | One residue class has at most `1+floor(D/r)` points in diameter `D`. |
| Private-row necessary divisibility | PASS | Every odd prime must divide one carry difference. |
| PNT choices of bases and protectors | PASS | Both required prime intervals contain more than the requested counts. |
| CRT class and reducedness | PASS | All moduli are coprime and every prescribed residue is a unit. |
| Bertrand/Dirichlet/Linnik chain | PASS | It produces distinct primes and polynomial size in `Q_t`. |
| `N_t=R_t mod Q_t` | PASS | It follows from the chosen progression for `ell_t`. |
| `log Q_t` and `n_t` asymptotics | PASS | Both are `Theta(t^2 log t)`. |
| Trial-hard distinct semiprime | PASS | Both prime factors exceed `n_t^2`; their exponents in `N_t` are one. |
| F116 menu eligibility | PASS | Bases are at most `n_t`, exponent two is allowed, and each word is below `N_t`. |
| Canonical inverse and exact carry | PASS | `N_t=1 mod c` gives `w_c=N_t-(N_t-1)/c` and carry `c-1`. |
| Valuation-one protector | PASS | `P_c=q_c mod q_c^2`. |
| Privacy inside selected values | PASS | For `d!=c`, `P_d=(c-d)(c-1)^{-1} mod q_c` is nonzero. |
| Selected-column independence | PASS | The `q_c` rows contain an identity submatrix. |
| Value-level deduplication | PASS WITH WORDING CORRECTION | Every protected exact value remains, but its named raw occurrence need not be the retained representative. |
| Endpoint sign screens for named `c` | PASS | Reduction modulo each factor would force `c^2=+1` or `-1`, impossible by size. |
| Endpoint sign screens for another representative | NOT PROVED | Exact-value equality does not identify endpoint residues modulo the factors of `N_t`. |
| Complete-source obstruction | NOT CLAIMED / OPEN | Unselected source columns can reuse every protected row. |
| Operational survival to selected attempts | NOT CLAIMED / OPEN | An earlier unselected sign screen can expose a factor. |

## Exact carry identities

For `1<=c,w<N`,

```text
1 <= cw <= (N-1)^2 = 1+(N-2)N.
```

Thus the carry is in `0..N-2`. Carry zero means `cw=1`, hence `c=w=1`.
For fixed `N`, equality of `1+kN` and `1+lN` is equivalent to `k=l`.
Therefore unit deletion and exact-value/carry deduplication are exact.

Let

```text
P_k = 1+kN,  P_l = 1+lN,  k!=l.
```

First, `gcd(P_k,N)=1` because `P_k=1 mod N`. Therefore

```text
gcd(P_k,P_l)
= gcd(P_k,P_l-P_k)
= gcd(P_k,(l-k)N)
= gcd(P_k,l-k).
```

Taking an absolute difference gives `gcd(P_k,|k-l|)`. Interchanging `k,l`
gives the third expression. All three gcds are equal. No direction is merely a
divisibility claim.

If a prime `r` divides `P_k`, then it cannot divide `N`. Thus `N` is invertible
modulo `r`, and

```text
r divides 1+kN  iff  k=-N^{-1} mod r.
```

All incidences of row `r` lie in one carry residue class. Odd valuation can
remove positions from this class, but cannot add a position outside it.

If a finite carry set lies in an interval of diameter `D`, one residue class
modulo `r` contains at most `1+floor(D/r)` integers. This proves the row-degree
bound. In particular, an odd-valuation prime `r>D` is private in that carry
set.

Now fix `k` and assume its column has no private odd-valuation row. For every
prime `r` in

```text
sf(P_k) = product of primes with odd valuation in P_k,
```

there is an `l!=k` whose column also has odd `r`-valuation. In particular,
`r` divides both exact values. The gcd identity then gives `r | |k-l|`.
Every distinct prime in `sf(P_k)` therefore divides at least one factor of
`product_{l!=k}|k-l|`. Since `sf(P_k)` is squarefree,

```text
sf(P_k) divides product_{l!=k}|k-l|.
```

The stated implication is correct. Its converse is not claimed and does not
follow.

The intermediate shared-part identity is also sound. Prime by prime,

```text
v_r(gcd(P_k, product_{l!=k} P_l))
<= sum_{l!=k} v_r(gcd(P_k,P_l)).
```

Hence `gcd(P_k,product_{l!=k} P_l)` divides
`product_{l!=k} gcd(P_k,P_l)`, which in turn divides
`product_{l!=k}|k-l|` by the three-way gcd identity.

## Audit of the CRT construction

### Base words

For sufficiently large `t`, the prime number theorem supplies `t` primes in
`(t^2,2t^2)`. Let their set be `A_t`. The words

```text
C_t = {a^2 b : a,b in A_t, a!=b}
```

are distinct. Their prime-exponent patterns identify the squared base and the
other base. There are exactly `M_t=t(t-1)` words. For each unordered pair,
the two exponent-two orientations give the two ordered words. Also
`c<8t^6` and `c` divides `L_t=product_{a in A_t}a^2`.

The prime number theorem also supplies `M_t` distinct primes `q_c` in
`(t^10,2t^10)`. This interval has `Theta(t^10/log t)` primes, which is more
than `Theta(t^2)`. Each `q_c` exceeds every word and every nonzero difference
of two words.

### CRT class

Let `d_c=c-1` and

```text
Q_t = L_t * product_c q_c^2.
```

The prime supports of `L_t` and the `q_c` are disjoint. The displayed moduli
are pairwise coprime. Since `q_c>c`, `d_c` is invertible modulo `q_c^2`.
The CRT system

```text
R_t = 1                         mod L_t,
R_t = (q_c-1)d_c^{-1}           mod q_c^2
```

has one class modulo `Q_t`. It is reduced: it is 1 modulo every prime of
`L_t`, and it is nonzero modulo every `q_c`.

### Two distinct prime factors

Bertrand gives a prime `p_t` with `Q_t<p_t<2Q_t`. Thus `p_t` is a unit modulo
`Q_t`. Put

```text
a_t = R_t p_t^{-1} mod Q_t,  1<=a_t<Q_t.
```

For large `t`, 5 divides neither `L_t` nor any `q_c`. Hence `Q_t` is a unit
modulo 5. Among `j=2,3,4`, at most one value makes `a_t+jQ_t` zero modulo 5.
Choose another and set `b_t=a_t+jQ_t`. Then

```text
2Q_t < b_t < 5Q_t,
gcd(b_t,5Q_t)=1.
```

Dirichlet gives primes in this class modulo `5Q_t`. Let `ell_t` be the least.
Linnik gives `ell_t<=C(5Q_t)^L` for absolute constants. Since `b_t` is the
least positive representative of its class, `ell_t>=b_t>2Q_t>p_t`. Thus the
two primes are distinct. Finally,

```text
ell_t ≡ b_t ≡ a_t ≡ R_t p_t^{-1}  (mod Q_t),
N_t=p_t ell_t ≡ R_t               (mod Q_t).
```

This completes the CRT/Dirichlet/Linnik chain.

## Size, trial-hardness, and menu eligibility

The base modulus contributes `log L_t=Theta(t log t)`. The protecting moduli
contribute

```text
sum_c 2 log q_c = Theta(t^2 log t).
```

Therefore `log Q_t=Theta(t^2 log t)`. The lower bounds
`p_t>Q_t`, `ell_t>2Q_t` and the Linnik upper bound give

```text
log p_t = Theta(log Q_t),
log ell_t = Theta(log Q_t),
n_t = bit_length(N_t) = Theta(t^2 log t).
```

It follows that

```text
t(t-1) = Theta(n_t/log n_t).
```

The bases satisfy `a<2t^2<=n_t` for sufficiently large `t`. Exponent two is
within `0..n_t^2`. Every word is below `8t^6`, whereas
`N_t>2Q_t^2`, so `c<N_t`. The complete F116 unordered-pair menu therefore
contains canonical residue `c` at the named exponent-two orientation.

Both factors exceed `Q_t`, while `n_t=O(log Q_t)`. Hence
`p_t,ell_t>n_t^2` for large `t`. Trial division through `B=n_t^2` cannot find
either factor. Since `p_t` and `ell_t` are distinct primes with exponent one,
`N_t` is an odd distinct semiprime and not a perfect power. The lower bound on
`Q_t` grows without bound, so an infinite pairwise-distinct subsequence can be
chosen.

## Valuation and selected privacy

Since every `c` divides `L_t` and `N_t=1 mod L_t`,

```text
N_t=1 mod c.
```

Thus

```text
w_c = N_t-(N_t-1)/c
```

lies in `1..N_t-1` and satisfies

```text
c w_c = 1+(c-1)N_t.
```

It is the least positive inverse, and the carry is exactly `c-1`.

For the assigned protector,

```text
1+(c-1)N_t = q_c mod q_c^2.
```

Therefore its `q_c`-valuation is exactly one. For another selected word
`d!=c`, reduction modulo `q_c` gives

```text
P_d = (c-d)(c-1)^{-1} mod q_c.
```

The numerator is nonzero and has absolute value below `q_c`. Hence `q_c` does
not divide `P_d`. The protected rows form an identity submatrix, so the
selected square-class columns are linearly independent.

## Deduplication and the endpoint-screen correction

The words `c` are distinct, so their carries `c-1` and exact values
`1+(c-1)N_t` are distinct. They are all nonunit. Complete exact-value
deduplication therefore leaves one column for every protected value.

This is a value-level statement. It does not say that the raw occurrence at
the named exponent-two position becomes the column's first provenance.
There are two earlier-occurrence cases:

1. The same canonical residue `c` appeared earlier. Its least positive inverse
   is still `w_c`. The endpoint pair is unchanged.
2. A different canonical residue `d` appeared earlier with
   `P_N(d)=P_N(c)`. The protected exact value and `q_c` row are unchanged, but
   the endpoint pair is `(d,w_d)`, not `(c,w_c)`.

For a prime factor `s` of `N_t`, a nontrivial named-residue sign screen would
give

```text
s | c-w_c  => c^2=1 mod s,
s | c+w_c  => c^2=-1 mod s.
```

For sufficiently large `t`,

```text
0 < c^2-1 < c^2+1 < Q_t < s.
```

Neither congruence is possible. This proves
`gcd(c-w_c,N_t)=gcd(c+w_c,N_t)=1` for the named residue. It also covers an
earlier occurrence of that same residue.

Nothing in the CRT system constrains a different representative `d` modulo
`p_t` or `ell_t` in the same way. Equality of the products
`d w_d=c w_c` does not imply `d^2=c^2` modulo either factor. Therefore the
sign-screen conclusion cannot be transferred to `d` from the proof given.

The private-row theorem survives this provenance change because valuations
belong to the exact integer value. The endpoint-screen theorem does not,
because sign gcds belong to the endpoint representation.

## Full-source and operational boundaries

The protected `q_c` row is private only among the selected values. An
unselected seed, frozen, or all-pairs column can have carry congruent to `c-1`
modulo `q_c` and reuse it. The construction does not prove stable privacy in
the final complete matrix.

It also does not prove that an operational source reaches the named residues
without first finding a factor. Trial division is null, and the named-residue
screens are null, but an unselected earlier residue can have a proper sign gcd.
The theorem is therefore about the selected submatrix inside the mathematical
complete no-stop source.

The logical gaps are correctly separated:

- Stable complete-source privacy needs `(FSP)` for the final deduplicated carry
  set.
- A nonzero exact square dependency needs `(CLOSE)`, or an explicit nonempty
  kernel vector. Absence of private rows is insufficient.
- Factoring from a dependency also needs `(ROOT)`, a positive exact root whose
  residue is neither `+1` nor `-1` modulo `N`.

The direct CRT route uses one `q_c^2` constraint per selected column. Its
modulus therefore costs `Theta(M_t log M_t)` bits and protects only
`Theta(n_t/log n_t)` columns. This is a limitation of this construction, not
an impossibility result for a coupled construction.

## Strongest sound theorem

For every sufficiently large integer `t`, there is an odd, non-perfect-power
semiprime `N_t=p_t ell_t` with distinct prime factors, bit length `n_t`, and a
set

```text
C_t={a^2 b : a,b in A_t, a!=b},
|C_t|=t(t-1)=Theta(n_t/log n_t),
```

such that:

1. `p_t,ell_t>n_t^2`.
2. Every `c in C_t` is a valid exponent-two word in the complete F116
   unordered-pair menu and is below `N_t`.
3. Its canonical inverse is
   `w_c=N_t-(N_t-1)/c`, and its exact value is
   `P_c=1+(c-1)N_t`.
4. The values `P_c` are distinct nonunits. For each `c`, a distinct prime
   `q_c` has valuation one in `P_c` and valuation zero in every other selected
   `P_d`. Hence the selected columns are linearly independent.
5. `gcd(c-w_c,N_t)=gcd(c+w_c,N_t)=1` for every named residue `c`. This also
   covers an earlier occurrence of the same residue.
6. Final exact-value deduplication contains every `P_c`, even if a different
   earlier residue is its first representative. No sign-screen conclusion is
   asserted for such a different representative.

The inputs can be chosen pairwise distinct along an infinite subsequence. No
claim is made about stable rows in the complete source, absence of earlier
direct factors, existence of any square dependency, a non-global root,
publication novelty, success density, or arbitrary-input factorization.
