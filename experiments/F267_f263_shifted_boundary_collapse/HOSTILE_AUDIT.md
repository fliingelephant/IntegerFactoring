# F267 hostile proof audit

## Verdict

**PASS, with one scope qualification.** The frozen statement and proof are
correct under their stated hypotheses. The six candidate definitions match
the frozen F263 V2 implementation. The four boundary mechanisms account for
all authenticated held-out non-direct incidences. No checked implication
requires an unrecorded invertibility assumption.

The condition `s^2 < p` is a valid sufficient condition for the rigidity
conclusion. It is not the weakest sufficient condition and is not necessary.
Thus any use of the word "threshold" must mean the literal hypothesis of the
stated implication, not a sharp or biconditional threshold. The frozen
statement does not claim sharpness, so this qualification does not invalidate
the theorem.

## Authentication

Authentication preceded claim inspection.

```text
MANIFEST.md    8ff26680b73c10f1f3513428154719a30b3b027aab6b4127561f55eb05b71961
STATEMENT.md   feff0a8b5dfd254cba265c9378106520c4fed718bbff3d507112c59a367045ee
PROOF.md       f6e95ae5d8a27828cfd4802cdc587f2bba2b2e94d50f523d42b559ef14e4fac3
SELF_AUDIT.md  55ca0cc6fa901b62d63faec38256812e8e4fd0cb88a352ee59a5ce405e561893
```

The five F263 provenance artifacts named by the manifest also match their
recorded hashes, including source hash
`05c0b87a453eb3c2c40c01bf058b0559a6ff2e9b943d16ddcf68d147b1f4c827`
and held-out row hash
`58b1e1ebde26af9ccdca43449fafff6d1737c932ceb2c3f9849571919c0f10a1`.

## Source correspondence

The frozen source uses shifted factors `u=c` and `v=c-B`. Its update

```text
u2 <- u2*u + u1
u1 <- u1*u + u0
u0 <- u0*u
```

stores the coefficients of degrees zero, one, and two in
`R_L(a+X)`. Hence they are exactly `R_L(a)`, `R_L'(a)`, and
`R_L''(a)/2`. The same holds for `v` at `a-B`. The source determinant order
is `u0*v2-u2*v0`, exactly as in equation (4).

For the shifted family, source weights zero and one are exactly `1` and
`c+1`. Forward and reverse upper-right entries are the claimed `F_0,G_0`.
The source `transfer_det01` is
`R_L(a)F_1-F_0R_L(a)=R_L(a)(F_1-F_0)`. There is no convention or indexing
drift.

The shifted source domain has length `H-1` and actual base one. Query start
zero therefore gives `[1,L+1)`. Query start `H-1-L` gives
`[H-L,H)`. Both starts are inserted for every registered fitting length.
The source's shifted singular index is `s-1`, so the right block is
non-direct exactly when `s < H-L`.

## Exact algebra checks

The product-jet formulas follow coefficient by coefficient over the
integers. In particular, `R_L''/2` is integral; equation (4) does not hide a
division in the recurrence.

Both unit-weight transfer identities are valid without division. Replacing
the diagonal factors one at a time gives

```text
R_L(a)-R_L(a-B)=B F_0=B G_0.
```

For `Q_i=(product_{j<=i} A_j)(product_{j>i} C_j)`, the identity

```text
(B+1)Q_i=(A_i+1)Q_i-A_i Q_{i-1}
```

telescopes with the stated endpoints. This gives equation (6) exactly.

The reflection formula
`R_L(1-L-X)=(-1)^L R_L(X)` is correct. For even `L`, evaluating it and its
second derivative gives both equalities in (4.2). These equalities force the
three `s=L+1` left-edge zeros. The `s=L+2` substitution in equation (6)
forces `transfer_det01=0 mod p`. Division modulo `p` is legitimate only at
the last step: `B` is congruent to `s`, and `B+1` is congruent to `s+1`,
while balanced geometry gives `p>=s+2`.

The right-edge parity cases are also exact. For `u1`, both hypotheses give
`2(H-L)+L-1=p`. For `v1`, the two hypotheses together with
`q=p+2(s+1)` give `2(H-L-B)+L-1=-q`. Pairing the `L` roots therefore makes
the relevant polynomial even modulo the named hidden prime, so its linear
coefficient vanishes.

## Balanced geometry, rigidity, and Fermat collapse

The derivation `0<=s<H<p<q` and `B<q` is valid in both parities of `B`.
The odd-`B` equality case `s=H` would give `B=2p-1`, which contradicts
`B<sqrt(2)p` for every odd prime `p>=3`.

Writing `d=q-p`, the two floor-square inequalities are exactly

```text
p(d-2s) >= s^2,
p(d-2s-2) < (s+1)^2.
```

Since `d` is positive and even, the first inequality gives
`d>=2s+2`. Under `s^2<p`, integrality gives `p>=s^2+1`, hence
`2p>=(s+1)^2`. The second inequality then excludes `d>=2s+4` and forces
`d=2s+2`. It follows exactly that `B+1=(p+q)/2` and
`(B+1)^2-N=(s+1)^2`. Since `N` is nonsquare, the first Fermat trial starts
at `B+1` and returns the stated factors.

Scope qualification: the proof actually works under the weaker condition
`(s+1)^2<=2p`. For example, `(p,q)=(101,127)` has `B=113`, `s=12`, and
`s^2>p`, but still has `q-p=2(s+1)`. Conversely, `(101,137)` has `B=117`,
`s=16`, and `q-p=36`, not `2(s+1)=34`. Therefore `s^2<p` is sufficient
but not a necessary or sharp threshold. No frozen theorem states the
converse.

## Independent held-out reconstruction

A separate read-only parser rebuilt the 148-name catalog in source order and
decoded every held-out bitset. It found exactly six candidates with a
non-direct bit:

| Candidate | Incidences | Complete `s` set |
|---|---:|---|
| `shifted.u1` | 33 | `9,10,17,18` |
| `shifted.v1` | 34 | `7,8,15,16,31,32,63,64` |
| `shifted.jet_det02` | 18 | `9,17` |
| `shifted.transfer_f0` | 18 | `9,17` |
| `shifted.transfer_r0` | 18 | `9,17` |
| `shifted.transfer_det01` | 15 | `10,18` |

The total is 136 candidate-row incidences on a union of 67 rows. For each
incidence, an independent exact modular evaluator reconstructed the stated
left- or right-edge block, checked that its length is in that row's public
query bank, checked that its support excludes `s`, and recovered the claimed
proper factor. All 136 checks passed. No other candidate has a held-out
non-direct bit.

The row file independently gives 256 consecutive-prime rows, maximum
`s=95`, minimum `p=551426102609`, and eight cleanup rows. Every one satisfies
`s^2<p`, `q-p=2(s+1)`, `B+1=(p+q)/2`, and the first-trial square identity.

## Bounded counterexample search

As audit guidance, a bounded exact enumeration checked 36,678 balanced
odd-prime pairs with `p<2000` and `q<4000`. All geometry statements held.
All 2,387 pairs satisfying `s^2<p` satisfied the rigidity and Fermat
identities. A separate 2,000-case integer test over signed starts and even
lengths checked the jet, forward transfer, reverse transfer, determinant,
and reflection identities. No counterexample was found. These finite checks
support the algebra but are not used as proof.

## Evidence boundary

This audit validates the conditional theorem and its exact correspondence to
the authenticated F263 held-out result. It does not upgrade finite coverage
to a converse zero classification, an evaluator lower bound, or an all-input
factoring result.
