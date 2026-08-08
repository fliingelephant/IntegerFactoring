# F119 — Carry Congruences Are the Exact Private-Row Gate

## Verdict

**The complete-source question remains open.** No unconditional proof here
constructs stable private rows for every column of the full F116 source, and
no unconditional proof shows that the cross-pair structure forces reuse or a
dependency.

There are two rigorous advances.

1. Prime-row incidence is exactly a congruence problem on canonical carries.
   This gives deterministic row-degree bounds and a necessary condition for
   the absence of private rows.
2. There is an infinite trial-hard family with
   `Theta(n / log n)` distinct genuine exponent-two cross-pair values whose
   selected square-class matrix has a private odd prime row in every column.
   These rows are mutually stable inside that cross-pair submatrix.

The second result extends the P104/X69 construction beyond one power
trajectory. It is not stable against the frozen layer or the other all-pairs
columns, so it is not a full-source obstruction.

No smoothness heuristic is used.

## 1. Canonical carries

Let `N > 1`, and let `c` be a unit represented in `1..N-1`. Let `w` be its
least positive inverse. Define

```text
kappa_N(c) = (c*w - 1) / N
P_N(c)     = c*w = 1 + kappa_N(c)*N.
```

The carry is an integer in `0..N-2`. It is zero exactly when `c=w=1`.
For nonunit exact values after unit removal, the carry lies in `1..N-2`.

For a fixed `N`, exact-value deduplication is exactly carry deduplication:

```text
P_N(c) = P_N(d)  if and only if  kappa_N(c) = kappa_N(d).
```

Thus provenance and pair structure matter only through the set of carries
that they produce.

## 2. Exact carry-difference theorem

Let `k != l` be two retained carries and put

```text
P_k = 1 + k*N,
P_l = 1 + l*N.
```

Then

```text
gcd(P_k, P_l) = gcd(P_k, |k-l|) = gcd(P_l, |k-l|).        (1)
```

Proof: every divisor of `P_k` is coprime to `N`. A common divisor of `P_k`
and `P_l` therefore divides `(k-l)N` and hence `k-l`. Conversely, a divisor
of `P_k` and `k-l` also divides `P_l = P_k + (l-k)N`.

For every prime `r` not dividing `N`,

```text
r divides P_k  if and only if  k = -N^(-1) mod r.         (2)
```

Therefore the support of the hidden prime row `r` is contained in one
residue class of the carry set modulo `r`. Valuation parity can delete entries
from that class, but it cannot add entries outside it.

### Row-degree bound

Let `K` be any finite carry set contained in an interval of diameter `D`.
The degree of row `r` is at most

```text
1 + floor(D / r).                                         (3)
```

In particular, if `r > D` divides one `P_k` to odd valuation, its row is
private in `K`.

For the full canonical range `K subset {1,...,N-2}`, row degree is at most
`1 + floor((N-3)/r)`. Every odd-valuation prime `r > N-3` is globally private
among all possible canonical carries, not only among source carries.

### Shared-part bound

For one `k in K`, equation (1) gives

```text
gcd(P_k, product_{l != k} P_l)
    divides product_{l != k} |k-l|.                       (4)
```

Let

```text
sf(P_k) = product of primes having odd valuation in P_k.
```

If column `k` has no private odd row in `K`, every prime in `sf(P_k)` occurs
in another `P_l`. Hence

```text
sf(P_k) divides product_{l != k} |k-l|.                   (5)
```

Consequently, failure of divisibility in (5) is a rigorous private-row
certificate. If the carry diameter is `D`, the right side is at most
`D^(|K|-1)`. This bound becomes weak for a large source, but it is exact and
uses no factor-size model.

## 3. A genuine cross-pair private-row family

### Theorem

For every sufficiently large integer `t`, there is an odd semiprime

```text
N_t = p_t * ell_t,
```

with distinct prime factors exceeding `n_t^2`, where `n_t` is the bit length
of `N_t`, and a set of

```text
M_t = t(t-1) = Theta(n_t / log n_t)
```

distinct exact values from exponent-two orientations of the F116 unordered
seed-pair menu such that:

1. every selected value has a private prime of valuation one;
2. the selected square-class columns are linearly independent;
3. for every named exponent-two residue `c`, both sign screens of `c` and its
   canonical inverse have gcd one;
4. `N_t` is not a perfect power.

The semiprimes can be chosen pairwise distinct along an infinite subsequence.

### Construction

By the prime number theorem, choose `t` primes in

```text
t^2 < a < 2t^2
```

and call their set `A_t`. Define the ordered cross-pair value set

```text
C_t = {a^2*b : a,b in A_t and a != b}.
```

Unique factorization shows that these `M_t=t(t-1)` integers are distinct.
They are exactly the two exponent-two orientations supplied by each unordered
pair from `A_t`.

Put

```text
L_t = product_{a in A_t} a^2.
```

Every `c in C_t` divides `L_t`. Also `c < 8t^6`.

Again by the prime number theorem, choose distinct primes `q_c`, one for each
`c in C_t`, in the interval

```text
t^10 < q_c < 2t^10.
```

There are more than `t(t-1)` such primes for all sufficiently large `t`.
In particular, every `q_c` exceeds every value and every nonzero difference
in `C_t`.

Let `d_c=c-1`. The moduli below are pairwise coprime. Use CRT to select the
reduced class `R_t modulo Q_t`, where

```text
Q_t = L_t * product_{c in C_t} q_c^2,
```

with

```text
R_t = 1                                      mod L_t,
R_t = (q_c - 1) * d_c^(-1)                  mod q_c^2.    (6)
```

The inverses exist because `q_c>c`. The class is reduced modulo `Q_t`.

Bertrand's postulate gives a prime `p_t` with

```text
Q_t < p_t < 2Q_t.
```

Let `a_t = R_t*p_t^(-1) mod Q_t`, with `1 <= a_t < Q_t`. Since `5` divides
neither `L_t` nor a `q_c`, choose `j in {2,3,4}` such that

```text
b_t = a_t + j*Q_t
```

is coprime to `5`. Then `2Q_t < b_t < 5Q_t` and
`gcd(b_t,5Q_t)=1`. Dirichlet supplies a prime in the class
`b_t mod 5Q_t`; choose the least and call it `ell_t`. Linnik gives

```text
ell_t <= C*(5Q_t)^L
```

for absolute constants `C,L`. Because `b_t` is the least positive
representative of its class and `b_t>2Q_t>p_t`, the two primes are distinct.
Set `N_t=p_t*ell_t`. Then

```text
N_t = R_t mod Q_t.                                         (7)
```

### Valid F116 source positions

The size of the CRT modulus is

```text
log Q_t = Theta(t^2 log t).
```

The lower bounds on `p_t,ell_t` and Linnik's upper bound give

```text
n_t = Theta(log Q_t) = Theta(t^2 log t).                  (8)
```

For sufficiently large `t`, every base in `A_t` is at most `n_t`, exponent
two is at most `n_t^2`, and every `c in C_t` is less than `N_t`. Thus all
these values occur in the declared F116 no-stop all-unordered-pair
enumeration, possibly earlier than their named provenance if residue
deduplication has already seen the same residue. This does not assert that an
operational run reaches them before some unselected direct factor is found.

Equation (8) also gives

```text
M_t = t(t-1) = Theta(n_t / log n_t).
```

Both factors exceed `Q_t`, while `n_t=O(log Q_t)`. Hence both factors exceed
`n_t^2` for large `t`; the family is trial-hard. Distinct prime factors make
`N_t` a non-perfect-power odd semiprime.

### Canonical inverses and private rows

Equations (6) and (7) give `N_t=1 mod c` for every `c in C_t`. Therefore

```text
w_c = N_t - (N_t-1)/c
```

is the canonical inverse of `c`, and

```text
P_c = c*w_c = 1 + (c-1)N_t.                               (9)
```

For its assigned prime `q_c`, equations (6) and (9) give

```text
P_c = q_c mod q_c^2,
```

so `v_{q_c}(P_c)=1`. If `d in C_t` and `d != c`, reduction modulo `q_c`
gives

```text
P_d = (c-d)*(c-1)^(-1) mod q_c.
```

The numerator is nonzero and has absolute value below `q_c`. Hence
`q_c` divides no other selected value. The `q_c` rows form an identity
submatrix of size `M_t`.

The exact values are distinct because their carries `c-1` are distinct.
Global exact-value deduplication therefore keeps all `M_t` values, although
their first residue provenance can precede the displayed exponent-two
attempt.

Finally, for either factor `s in {p_t,ell_t}`, a successful sign screen at a
named residue `c` would imply

```text
c^2 = 1 mod s  or  c^2 = -1 mod s.
```

But `0<c^2-1<c^2+1<Q_t<s` for large `t`. Neither congruence is possible.
Thus both sign screens have gcd one for every named residue `c`. If the same
canonical residue occurred earlier, it has the same endpoints and is also
covered.

A different earlier residue can have the same exact value. Exact-value
deduplication then preserves the protected value and its private row, but this
argument does not control the sign screens of that different representative.

## 4. Why this is not the requested full obstruction

The prime `q_c` is private among the values in `C_t`. This proof does not
exclude an earlier frozen value or another all-pairs value whose carry is
congruent to `c-1 mod q_c`. Equation (2) shows that such a carry would reuse
the row.

The construction therefore proves no statement about:

- the joint seed, frozen, and complete pair matrix;
- stability after all `O(n_t^4)` source positions;
- absence of an earlier direct factor outside `C_t`;
- null sign screens for a different earlier residue that represents the same
  exact value;
- absence of a dependency outside the selected submatrix.

This boundary is essential. A private row in a selected submatrix can be
reused by an unselected column.

The construction also exposes a scale barrier in this direct CRT method. It
uses one independent `q_c^2` congruence per protected column, so its bit
length is `Theta(M_t log M_t)`. It protects only
`Theta(n_t/log n_t)` columns, not a quadratic or quartic number of columns.
This is a limitation of the construction, not an impossibility theorem.

## 5. Exact missing lemmas

Let `K_N` be the set of distinct nonzero carries produced by the complete
F116 source after residue and exact-value first occurrence.

### Lemma needed for a full private-row obstruction

It would suffice to prove an infinite trial-hard distinct-semiprime family
such that, for every `k in K_N`, there is a prime `r_k` with

```text
v_{r_k}(1+kN) odd,
K_N intersect (k + r_k*Z) = {k}.                          (FSP)
```

By equation (2), `(FSP)` says exactly that every complete-source column has a
stable private odd row. It would make the full matrix have column rank
`|K_N|` and kernel zero.

The difficulty is that `K_N` is self-generated by canonical reduction of all
cross-pair words and has size up to `O(n^4)`. CRT, Dirichlet, and Linnik can
protect a predeclared finite carry set. They do not control this
`N`-dependent carry set at the required scale.

### Lemmas needed for a forced-progress theorem

A pure row-reuse theorem would have to show

```text
for every k in K_N and every prime r with odd valuation in 1+kN,
there is l != k in K_N with l = k mod r.                   (REUSE)
```

This removes degree-one rows, but it still does not force a dependency.
The actual closure lemma needed is

```text
rank_F2(M_N) < |K_N|,                                     (CLOSE)
```

where `M_N` is the complete hidden prime-parity matrix. Equivalently, there
must be a nonempty `X subset K_N` such that

```text
product_{k in X} (1+kN)
```

is an exact square.

For factoring, one further lemma is necessary:

```text
the positive square root for some such X is not +1 or -1 mod N.  (ROOT)
```

Neither `(REUSE)`, `(CLOSE)`, nor `(ROOT)` follows from the number of source
positions. The cross-pair word identities must be converted into carry
congruences or exact valuation cancellations.

## 6. Final boundary

The rigorous conclusion is:

> Cross-pair provenance alone does not yield a reuse law. Hidden prime rows
> are controlled exactly by congruence collisions among canonical carries.
> An unconditional CRT construction protects
> `Theta(n/log n)` genuine cross-pair exact values, but not the complete
> source. A full obstruction requires `(FSP)`. A positive source theorem
> requires `(CLOSE)` and then `(ROOT)`; absence of private rows alone is not
> enough.

No computation was run for F119. No empirical distribution is evidence for
any statement above.
