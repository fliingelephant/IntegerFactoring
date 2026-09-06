# Hostile audit of F193

## Verdict

**FAIL.** The frozen candidate is not promotable as written.

Section 3 contains a direct counterexample under the standard definition of
an imprimitive Dirichlet character. Sections 1 and 2 pass within their named
models. The conjugacy and order claims in Section 4 pass, but the minimal-
polynomial wording for composite `m` is not canonical and the CM
characteristic-polynomial sentence needs a stronger justification.

No mathematical computation was run. No durable ledger was edited.

## Frozen-input verification

Before reading the candidate, I recomputed the hashes. They agree with the
frozen hashes in `MANIFEST.md`:

- `STATEMENT.md`:
  `55968763e179387ff0db2bcb90a3740ffa36d982ab5f23e81b67d0fc6bae0f46`;
- `PROOF.md`:
  `b9ce3e75679b8bc6e04d38236d3d57e7bb15de7d968b7183575c1c0a6c821f1f`;
- `SELF_AUDIT.md`:
  `6644ad9d81ac31ea9052786ff0b37529176127c0e04a8c6d7830d38fd3f7f905`.

I attacked `STATEMENT.md` and `PROOF.md` before consulting
`SELF_AUDIT.md`.

## 1. Squarefree cusp and sparse-boundary claim

This part passes with its explicit-boundary scope.

For each prime `r | N`, the proof checks cancellation in both directions.
If `r | c`, the transformed numerator is nonzero modulo `r`, so reduction
cannot remove `r` from the denominator. If `r` does not divide `c`, the
transformed denominator is nonzero modulo `r`. The usual cusp classification
then gives one orbit for each `d | N`, because
`gcd(d,N/d)=1` at squarefree level.

The boundary conclusion is only a support conclusion. It does not control
the coefficient of `[c_N]-[c_1]`, a boundary-zero class, a period, or a
compressed dense presentation. The candidate states these non-implications.

For `gcd(m,N)=1`, every diagonal entry in an upper-triangular Hecke branch is
a unit at every level prime. The branch therefore preserves denominator
type. This does not cover bad-prime operators.

The Fricke formula `d -> N/d` is correct. For `N=pq`, it swaps `1` with `N`
and also swaps `p` with `q`. The sentence that it "only swaps the two global
types" must be read as a statement about an input in the global pair. A
revision should say explicitly that Fricke preserves the partition
`{1,N} union {p,q}`.

For a squarefree exact divisor `Q`, the toggle formula

`d -> dQ/gcd(d,Q)^2`

is correct. An integral Atkin--Lehner representative can be chosen with
determinant `Q`. The normalized analytic matrix need not have determinant
`Q`, so the determinant observation is valid only for the explicitly named
integral convention. The public exact-divisor label already supplies the
same information. The candidate does not extend this to an opaque circuit.

One input-size detail should be repaired. The statement bounds the endpoint
integers but not the coefficients `u_i`. The structural support theorem does
not need a coefficient bound, and the endpoint gcd scan can ignore the
coefficients. However, calling the whole explicitly encoded chain a QP-size
input requires the bit lengths of the `u_i` to be QP too. A revision should
either bound the total chain encoding or say that only the separately
accessible endpoint list is scanned.

## 2. Small-modulus CRT claim

This part passes.

The bound

`0 < b_N < 2(N+1) <= 2^(n+1)`

is correct. Taking `n+2` distinct auxiliary primes gives a product strictly
larger than the coefficient bound. There are enough such primes below
`C n log(n+2)`, and each has `O(log n)` bits. Thus the bank has `O(n)`
members and is constructible in polynomial time.

For outputs `24 b_N mod ell`, omitting `2` and `3` makes `24` invertible.
CRT then recovers the exact integer `b_N`. The discriminant computation
recovers `p` and `q`. Polynomially many uniform numerical-QP calls remain
numerical QP. The proof does not incorrectly amplify one fixed modulus.

## 3. Dirichlet-twist claim

This part fails as written.

For a Dirichlet character presented modulo `M`, its conductor can be coprime
to `N` while its defining modulus is not. The principal character modulo
`N` is the simplest counterexample. Its conductor is `1`, hence coprime to
`N`, but

`chi(N)=0`.

Therefore the frozen assertions that every multiplier is nonzero, that any
one twist value recovers `a_f(N)`, and that every such bank has rank exactly
one are false. A bank containing only this character has rank zero at the
index `N`.

The coefficient identity itself remains correct:

`a_(f tensor chi)(N) = chi(N) a_f(N)`.

Hence the valid general conclusion is **rank at most one**. Recovery of the
base coefficient is possible from a row only when `chi(N)` is a unit in the
chosen coefficient ring.

There are two clean repairs:

1. require primitive characters presented at their conductors, with those
   conductors coprime to `N`; or
2. allow arbitrary characters, state rank at most one, and require at least
   one explicitly evaluable character with `chi(N) != 0` for the converse.

If arbitrary defining moduli are used, a proper gcd of a modulus with `N`
already factors `N`; a modulus divisible by all of `N` can instead give the
public zero above. A gcd statement about the conductor does not cover this
case.

Across different coefficient fields, the identity is mathematical after
placing the values in compatible composita. An algorithmic recovery claim
also needs explicit compatible embeddings and QP exact field arithmetic.
This does not create new information, but it is part of the precise
interface.

## 4. Global elliptic-torsion endomorphism claim

The central conjugacy claim passes under the stated finite-etale premise.

When `m` is invertible, `E[m]` is a rank-two lisse
`Z/mZ`-module. A global endomorphism is a morphism of this local system.
Etale path transport is natural in all such morphisms, so it intertwines the
two fiber actions. On a connected base, their matrices are therefore
conjugate after choices of bases. This proves equality of characteristic
polynomials and, when the action is invertible, equality of exact orders.
There is no order-invariance failure here.

For composite `m`, however, "the minimal polynomial" of a matrix over
`Z/mZ` is not generally a unique canonical polynomial. For example, over
`Z/4Z`, the matrix

`A = [[0,2],[0,0]]`

has no monic linear annihilator, while both `X^2` and `X^2+2X` are monic
quadratic annihilators. Conjugacy preserves the full annihilator ideal and
the minimum possible degree, but the frozen singular wording is ambiguous.
A revision should use the annihilator ideal, define a convention, or
restrict `m` to a prime.

The CM characteristic-polynomial formula is standard and true, but equation
`alpha^2-Tr(alpha)alpha+[Nm(alpha)]=0` alone does not prove that this
annihilating quadratic equals the matrix characteristic polynomial over a
non-field ring. A complete proof should invoke the characteristic polynomial
on the prime-to-characteristic Tate module, or separately identify trace and
determinant and then reduce modulo every prime power dividing `m`.

The result does not apply to local Frobenius, endomorphisms created only
after reduction, characteristic-primary torsion, a disconnected CRT base,
or local maps that do not descend from one global map. The candidate states
these exclusions and makes no lower-bound inference about them.

## Required disposition

Do not promote the frozen candidate. Revise Section 3 at minimum. Also make
the composite-`m` invariant and the sparse-input convention precise. Freeze
new hashes and send the revised candidate through a fresh audit.
