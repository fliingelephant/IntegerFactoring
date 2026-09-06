# F155 hostile audit — PASS AS NARROWLY CLAIMED

## Verdict

**PASS AS NARROWLY CLAIMED.** The congruences, canonical representatives,
direct-screen equalities, forced gcd refinement, infinite-family argument,
Legendre-symbol calculations, endpoint subgroup membership, and strict
named-subgroup containment are all correct. The one-row transcript is a
legitimate instance of F154.

There is one material interpretation limit. The released block is the fixed
public integer `5`, and the old atom `a` is visibly divisible by both `3` and
`5`. Thus F155 proves strict growth only relative to the deliberately frozen
named state `H=<a>`. It does not prove that feedback reveals information that
a normal small-seed source, trial refinement of relation values, or the
existing F130 source did not already have. This does not contradict the
frozen statement, which claims only named-block subgroup growth and expressly
disclaims a separator or factoring theorem. Any promotion must preserve this
limit.

## Frozen inputs

I read the complete statement and proof. Their requested SHA-256 hashes match:

- `STATEMENT.md`:
  `b42079fcb9b0d09a16483fffd8ee41d24f3fc6c3ac6bddc4495af6fa09298998`;
- `PROOF.md`:
  `5fd7d453b96c67b6112b4a50d52d5ce877e317ac7029dc792da21dfd1e52c233`.

I also checked the construction against P76, P128, P129, P138, and F154.
I did not modify a frozen input or durable ledger. No research computation
was needed.

## 1. Congruences, ranges, units, and canonical representatives

The factorization

\[
23400=2^3\,3^2\,5^2\,13
\]

shows that `N=77 mod 23400` implies all five residue conditions used in the
proof. Since `N>13` in this residue class actually gives `N>=77`, the three
integers

\[
z=(N-3)/2,\qquad s=(N-2)/3,\qquad a=(3N+9)/4
\]

are positive and strictly below `N`.

If a divisor of `N` divides `z`, `s`, or `a`, it respectively divides `3`,
`2`, or `9`. The displayed residue conditions exclude these possibilities.
Thus all three integers are units modulo `N`.

Direct expansion gives

\[
zs=1+N(N-5)/6,
\qquad
z^2-a=N(N-9)/4.
\]

Both quotients are integral. The strict ranges therefore prove both
canonical claims: `a` is the least positive residue of `z^2`, and `s` is the
least positive inverse of `z`.

## 2. Direct screens

The exact identities

\[
z-s=(N-5)/6,
\qquad
z+s=(5N-13)/6
\]

are correct. Since `6` is a unit modulo `N`, they give

\[
\gcd(z-s,N)=\gcd(5,N)=1,
\qquad
\gcd(z+s,N)=\gcd(13,N)=1.
\]

Multiplication by the unit `z`, together with `zs=1` and `z^2=a` modulo
`N`, gives the two claimed equalities with `gcd(a-1,N)` and
`gcd(a+1,N)`. No sign was reversed.

The statement calls only these canonical endpoint screens null. It does not
claim that every scalar one could form from `a,z,s` is null. On the stated
large semiprime family, the obvious additional affine-difference screens are
also harmless because any local divisor they could expose is among fixed
small constants, while both hidden primes tend to infinity.

## 3. The forced integer refinement

Writing `N=77+23400t` gives exactly

\[
s=25+7800t=25(1+312t),
\]

\[
a=60+17550t=5(12+3510t).
\]

Hence both values are divisible by `5`, while the second factor of `a` is
`2 mod 5`; thus `v_5(a)=1`. Also `4a-9s=15`, so every common divisor divides
`15`. Since `s=1 mod 3`, the gcd is exactly `5`.

A perfect power with exponent at least two has every prime valuation
divisible by that exponent. The valuation `v_5(a)=1` therefore proves that
`a` is not a perfect power. Moreover, `gcd(a/5,s)=1`: any common divisor
would divide `gcd(a,s)=5`, but `a/5=2 mod 5`. Thus complete gcd-free
refinement really does replace the old atom by the pairwise-coprime
descendants `5` and `a/5`. Discarding `s` after recording this split does not
undo the exact presentation of `a`.

## 4. Infinite balanced trial-hard family

The classes `7` and `11` are reduced modulo `23400`. The prime number theorem
in a fixed arithmetic progression implies that, for all sufficiently large
`X`, each dyadic interval `[X,2X]` contains a prime in each class. Choosing
one of each gives distinct odd primes because their residue classes differ.
Their ratio is strictly between `1/2` and `2`; equality would require one
large odd prime to be twice another prime.

Taking disjoint increasing dyadic intervals gives infinitely many pairs. For
`N=PR`, one has `X^2 <= N <= 4X^2`, so

\[
n=\lceil\log_2(N+1)\rceil=2\log_2 X+O(1).
\]

Both factors are at least `X`, hence exceed `n^2` for all sufficiently large
`X`. In fact they are exponential in `n`, so the change from polynomial to
quasipolynomial target time does not make trial division reach them. Finally,
`PR=7*11=77 mod 23400`, as required.

This uses only a fixed-modulus dyadic interval consequence of PNT in
arithmetic progressions. It does not assume an unproved short-interval result.

## 5. Endpoint membership in the old subgroup

For either hidden prime `L`,

\[
z=-3/2\pmod L.
\]

Multiplication by the square `4` shows that its Legendre symbol is
`(-6/L)`. The standard formulas give

\[
(-1/P)=-1,\quad (2/P)=1,\quad (3/P)=-1
\]

for `P=7 mod 24`, and

\[
(-1/R)=-1,\quad (2/R)=-1,\quad (3/R)=1
\]

for `R=11 mod 24`. Thus `(-6/L)=1` in both components.

Both primes are `3 mod 4`. Their square subgroups have odd orders
`(L-1)/2`, so the local order of `z` is odd. Consequently squaring is an
automorphism of the cyclic group generated by `z`. This gives

\[
\langle z^2\rangle=\langle z\rangle
\]

in both components and, equivalently, modulo `N`. Since `a=z^2 mod N`, both
`z` and `s=z^{-1}` lie in `H=<a>`. The section-completion endpoint therefore
adds no new residue to the declared old subgroup.

## 6. Strict named-subgroup expansion

Because `5=1 mod 4`, quadratic reciprocity gives

\[
(5/P)=(P/5)=(2/5)=-1.
\]

Every element of `H=<z^2>` is a quadratic residue modulo `P`, so `5` cannot
belong to `H`. After refinement, the new named subgroup contains `5` and
`a/5`; their product is `a`. It therefore contains `H` and also an element
outside `H`. The containment

\[
H<\langle5,a/5\rangle
\]

is strict.

## 7. The one-row source is formally legitimate but algorithmically weak

Take the single F154 block `q_1=a`, the parity vector `v=1`, the exact value
`T=a=1^2Q(v)`, and the supplied modular root `alpha=z`. The block is a unit
and is an integer nonsquare because `v_5(a)=1`. A one-column nonzero parity
matrix has zero kernel, so this transcript is automatically on the no-factor
section branch. Its actual lift is `(1,z)`. F154 completion then computes
`s=iota_N(z)` and the exact record `s^2a=1 mod N`. Thus no hidden factor,
oracle, or factor-aware choice enters the source. It is uniform from bare
`N` on the publicly testable congruence class.

However, this example does not show that feedback is needed to obtain the
expanded group. The same public formulas give

\[
a=3(N+3)/4
\]

and, on the declared congruence class, `5` divides `a`. A routine can expose
`3` and `5` before section completion by fixed small-prime division. The
F130 initial seed bank already includes both constants for large inputs, so
F155 is not strict subgroup growth relative to F130's actual initial named
subgroup.

Therefore the exact result is an infinite-family certificate for this state
transition:

\[
\text{freeze the one-block state }\{a\}
\;\longrightarrow\;
\text{complete its section}
\;\longrightarrow\;
\text{gcd-refine with }s.
\]

It is not a certificate that feedback manufactures previously inaccessible
factor-correlated information. It gives no density law, no all-input
refinement theorem, no useful element of the enlarged subgroup, and no
factoring algorithm. The frozen statement explicitly disclaims the last
three claims; its phrase “named-block-generated subgroup” is essential to
the pass verdict.
