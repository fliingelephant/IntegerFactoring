# F149 V2 statement-only blind reconstruction

## Protocol and verdict

**Verdict: PASS.**

I read only `V2_STATEMENT.md` within the F149 directory. Its SHA-256 is

```text
8e116d027dd5ecfe14f789fd301e9a6f4cf3b62e402fa2575cfc34406aa4d4dd
```

This is the requested hash. The algebraic invariance, singleton criteria,
root and gcd formulas, semiprime counts, density bounds, union bound, collision
claim, and finite arithmetic certificate all reconstruct correctly.

The verdict uses the following meanings that are implicit in the statement:

- `[x]_N` is the canonical positive residue of a unit, in
  `1,...,N-1`.
- `iota_N(c)` is a positive representative of the inverse of `c` modulo
  `N`.
- A useful square root of one is neither `+1` nor `-1` modulo `N`.
- In the asymptotic statement, `n` is the bit length of `N`.
- For the union bound, each center is fixed independently of its sampled
  anchor, or the anchor is uniform conditional on that center.

The P71, P114, P128--P131 labels and their notions of legality are external
to this statement. I therefore verify the displayed arithmetic, but I do not
independently certify those historical classifications.

## 1. Raw-anchor canonicalization

Let

\[
\alpha=[a]_N,\qquad c=[q\alpha^2]_N,\qquad cw\equiv1\pmod N.
\]

The two exact values are

\[
C=cw,\qquad L_a=qa^2w.
\]

They are both `1 mod N`, since `c` is also the residue of `qa^2`.
In the positive rational square-class group,

\[
[L_a]=[qa^2w]=[qw],
\]

because `a^2` is a square. Thus the exact exponents and size of `a` do not
affect the square class once its residue `alpha` is fixed. They can still
affect the compact presentation. They do not affect this parity calculation.

For

\[
L_\alpha=q\alpha^2w,
\]

one has the exact identity

\[
L_aL_\alpha=q^2a^2\alpha^2w^2=(qa\alpha w)^2.
\]

Its positive root is global modulo `N`:

\[
qa\alpha w\equiv q\alpha^2w\equiv cw\equiv1\pmod N.
\]

Hence replacing `a` by `alpha` creates only a root-`+1` duplicate. This does
not show that `alpha` has an allowed source presentation. The statement
correctly keeps that distinction.

The containment claim is an equality claim, not only a congruence claim:

\[
[qa^2]_N=[q\alpha^2]_N=c.
\]

For every fixed named integer block `r`, divisibility of these two canonical
integers is identical. If divisible, the quotient is the same. Therefore raw
magnitude alone cannot alter any containment predicate of the displayed
form.

## 2. Exact singleton square criterion and factor extraction

The product of the two actual columns is

\[
CL_a=(cw)(qa^2w)=a^2w^2(qc).
\]

The first two factors form an exact square. Therefore `CL_a` is a square if
and only if `qc` is a square. Writing

\[
qc=s^2,\qquad s>0,
\]

gives the exact positive root

\[
R=aws.
\]

Modulo `N`,

\[
R\equiv \alpha c^{-1}s
 \equiv \alpha(q\alpha^2)^{-1}s
 \equiv s(q\alpha)^{-1}.
\]

This proves the normalized-root formula. Since `q alpha` is a unit,
multiplying a gcd argument by it does not change the gcd with `N`. Also,

\[
q\alpha(R\pm1)\equiv s\pm q\alpha\pmod N.
\]

Consequently,

\[
\gcd(R\pm1,N)=\gcd(s\pm q\alpha,N).
\]

Finally,

\[
s^2=qc\equiv q^2\alpha^2=(q\alpha)^2\pmod N.
\]

Both sides are units. For odd `N`, a square root of one is `+1` or `-1` at
each prime-power component. Global equal signs give a global root. Mixed
signs give nontrivial proper sign gcds. Thus the statement's usefulness
criterion is exact. For an odd prime power there are no mixed signs, which is
also consistent with the claim.

## 3. Exact positive self-containment criterion

Put `z=[alpha^2]_N`. Then

\[
c=[qz]_N=qz-kN,
\]

where `0 <= k <= q-1`, because `0<z<N` implies `0<qz<qN`.

If `qz<N`, then `k=0`, so `c=qz`. This gives the self-edge with residual
`T=z`.

Conversely, suppose `c=qT`. Then `q` divides both `qz` and `c`, so it divides
`kN`. Since `gcd(q,N)=1`, it divides `k`. The range of `k` forces `k=0`.
Thus `qz<N`, and again `T=z`. This proves the iff in (7).

Under this condition, the general singleton criterion becomes

\[
qc=q^2z.
\]

It is a square exactly when `z` is a square. Since `z<N/q`, this is exactly

\[
z=S^2<N/q.
\]

Here `s=qS`, so the normalized singleton root reduces to

\[
s(q\alpha)^{-1}=S\alpha^{-1}.
\]

Its two sign gcds are therefore

\[
\gcd(S-\alpha,N)=\gcd(\alpha-S,N),\qquad
\gcd(S+\alpha,N).
\]

Because `S^2` is the canonical residue of `alpha^2`, there is an integer
`h>=0` with

\[
\alpha^2-S^2=hN.
\]

If `h=0`, positivity gives `alpha=S`, hence the normalized root is `+1`.
Therefore usefulness requires `h>=1`. The statement does not claim that
`h>=1` is sufficient; a global `-1` root can still occur. The
difference-of-squares interpretation for a positive multiple of `N` is
correct.

## 4. Exact count for an odd semiprime

Now let `N=p ell`, where `p` and `ell` are distinct odd primes. Write

\[
q=du^2
\]

with `d` squarefree. Since `q` is a unit modulo `N`, so are `d` and `u`.

### Ordinary singleton count

The condition `qc=s^2` is equivalent to

\[
du^2c=s^2.
\]

Prime valuations and squarefreeness of `d` show that this holds exactly when

\[
c=dv^2,\qquad s=duv
\]

for one positive integer `v`. The canonical bound on `c` gives `dv^2<N`.
The fact that `c` is a unit gives `gcd(v,N)=1`. Thus the possible exact
values of `c` are indexed exactly by the `V_d` values in the statement.

For a fixed such `v`, the condition on `alpha` is

\[
du^2\alpha^2\equiv dv^2\pmod N,
\]

or

\[
(u\alpha v^{-1})^2\equiv1\pmod N.
\]

There are exactly four roots of one modulo a product of two distinct odd
primes. Two have equal CRT signs and two have mixed CRT signs. The normalized
root is

\[
\rho={s\over q\alpha}
     ={v\over u\alpha}
     =(u\alpha v^{-1})^{-1}.
\]

It has the same local signs. Hence exactly two of the four `alpha` values are
useful. Distinct positive `v` values cannot overlap: they would give two
equal canonical integers `dv^2<N`, hence the same `v`. The exact useful
count is therefore

\[
2V_d.
\]

The elementary bound is

\[
V_d\le \sqrt{N/d}.
\]

Also,

\[
{\varphi(N)\over N}
=\left(1-{1\over p}\right)\left(1-{1\over\ell}\right)
\ge {2\over3}{4\over5}={8\over15}>{1\over2},
\]

where distinctness makes the smallest pair `3,5`. It follows that

\[
{2V_d\over\varphi(N)}
\le {2\sqrt{N/d}\over\varphi(N)}
< {4\over\sqrt{dN}}.
\]

### Self-containment count

For each admissible `S`, the congruence

\[
\alpha^2\equiv S^2\pmod N
\]

again has four unit solutions. Exactly two give mixed signs for
`S alpha^{-1}`. The exact bound `qS^2<N` makes `S^2` the canonical residue,
and distinct positive `S` values cannot collide. The exact useful count is
therefore

\[
2W_q.
\]

Since `W_q<sqrt(N/q)` and `phi(N)>N/2`,

\[
{2W_q\over\varphi(N)}<{4\over\sqrt{qN}}.
\]

I also exhaustively checked both exact counts for every distinct odd-prime
pair below `50` and every unit center `2<=q<N`. No counterexample occurred.
This computation is supplementary; the bijections above prove the claims.

### Quasipolynomial union bound

Both per-trial bounds are at most a constant times `N^{-1/2}`. If `N` has
`n` bits, then

\[
N^{-1/2}\le 2^{-(n-1)/2}=2^{-n/2+O(1)}.
\]

For `M=2^{polylog(n)}=2^{o(n)}` trials, the union bound gives

\[
\Pr(\text{some useful singleton})
\le M\,2^{-n/2+O(1)}
=2^{-n/2+o(n)}.
\]

No independence between trials is used. However, fixed-center uniformity is
material. If a center can be selected after seeing its anchor, uniformity of
the anchor's unconditional marginal alone does not justify the fixed-`q`
count. The statement begins this section with a fixed `q`, so its bound is
valid in that stated scope. Equivalently, the bound remains valid for random
centers when the anchor is uniform conditional on each center.

## 5. Squared-residue collisions and cycle closure

If unit residues satisfy

\[
\alpha^2\equiv\beta^2\pmod N,
\]

then

\[
x=\alpha\beta^{-1}\pmod N
\]

satisfies `x^2=1`. For odd `N`, `x` is a sign on each prime-power CRT
component. If all signs agree, `x` is global `+1` or `-1`. Otherwise,
`gcd(x-1,N)` and `gcd(x+1,N)` separate nonempty component sets, so each is a
proper nontrivial divisor. The collision claim is correct.

Calling a collision of two public bounded presentations a P71
"half-relation" depends on the external P71 definition. The arithmetic
content needed for that classification is present and correct.

The more general cycle formula can be checked conditionally from its stated
aggregate data. Cycle cancellation must supply

\[
A_0^2\equiv S^2\pmod N.
\]

Then `S` is a unit and

\[
(A_0S^{-1})^2\equiv1\pmod N.
\]

Thus `A_0 S^{-1}` is the claimed root. Whether a declaration of `S` meets a
specific bounded-word grammar, and whether a given collection is a legal
containment-cycle collection, are not defined inside V2. Those semantic
labels cannot be reconstructed in a statement-only audit. This does not
create an algebraic defect in the displayed root formula.

## 6. Strict finite certificate

For `N=77`, `q=2`, and `a=alpha=25`, direct calculation gives

\[
25^2=625=8\cdot77+9,
\]

so `z=9=3^2` and `a^2` is not `1 mod 77`. Also,

\[
c=[2\cdot625]_{77}=18=2\cdot3^2.
\]

The inverse representative `w=30` is correct because

\[
18\cdot30=540=7\cdot77+1.
\]

The displayed direct screens are both null:

\[
\gcd(18-30,77)=\gcd(12,77)=1,
\]

\[
\gcd(18+30,77)=\gcd(48,77)=1.
\]

The exact columns are

\[
C=18\cdot30=540,
\]

\[
L_a=2\cdot25^2\cdot30=37500.
\]

Here `qc=36=6^2`, so

\[
CL_a=540\cdot37500=20{,}250{,}000=4500^2.
\]

The root and its sign gcds are

\[
4500=58\cdot77+34,
\]

\[
\gcd(34-1,77)=11,\qquad \gcd(34+1,77)=7.
\]

The self-edge view agrees: `2z=18<77`, `S=3`, and

\[
S\alpha^{-1}=3\cdot25^{-1}\equiv34\pmod{77}.
\]

Since `25=5^2`, the same root is

\[
25/3\equiv34\pmod{77}.
\]

The same-residue identity is also exact:

\[
2\cdot3^2=18,
\qquad
2\cdot5^4=1250=16\cdot77+18.
\]

Thus all numerical claims in the certificate pass. The certificate proves a
local congruence-of-squares capability and the failure of the two displayed
endpoint screens. The further claim that it is a legal P131/P128
"source-semantic" edge is not self-contained. The statement itself properly
does not claim survival under unspecified full preprocessing.

## 7. Hostile scope check

No displayed result supplies a method that finds a closing residue. The
uniform count is a density statement for a fixed center, not a theorem about
a compact-word distribution. A nonuniform source can concentrate on the
exceptional residues. Multi-relation closure is not bounded by the singleton
count. The raw-anchor argument removes only the exact squared mass of an
anchor after its residue is fixed. It does not remove the source's ability to
reach a new residue.

The assumptions are used sharply:

- `gcd(q alpha,N)=1` is needed for every inverse and for the gcd formulas.
- Oddness makes local roots of one equal to signs on prime powers.
- The product of two distinct primes gives exactly four roots of one and
  exactly two mixed roots.
- The semiprime hypothesis is needed for the exact `2V_d` and `2W_q`
  counts as written.
- Fixed or conditional uniformity is needed for the probability statement.
- A bit-length definition of `n` is needed for the final exponent.

The proposed remaining work is consistent with these limits. It must obtain
a nonuniform source advantage or combine several nonclosing relations. Raw
numerical magnitude alone cannot alter the endpoint, parity column, or
containment quotient already proved invariant above.

**Final result: PASS, with the explicit semantic and uniformity scope noted
above.**
