# F207 hostile audit

## Verdict

**PASS at the narrow scope stated by the packet.** The abstract recurrence,
the local balanced-node size accounting, the CRT root, the inverse-torsor
bijection and count, the discriminant and swap identities, the support-prime
Jacobi formula, and the genus-character conclusion are correct.

This verdict has three strict scope guards.

1. A balanced root does not imply that its `K` descendant is balanced. The
   recurrence theorem applies to a whole recursion only when every reachable
   node has at most one near-size child, or when nonconforming descendants
   have an independent QP bound. The packet's explicit exclusion of an
   unbalanced two-near-child branch is therefore essential.
2. The usual factoring convention `N >= 3` is needed. For a perfect square,
   `E=0` and `gcd(E,N)=N`; the proper factor is `B=sqrt(N)`, not that gcd.
   The later coprime branch is unaffected.
3. The quadratic-character argument covers a character evaluated directly
   on the multiplicative torsor coordinate. It does not cover a character
   evaluated on an arbitrary shifted or nonlinear expression in that
   coordinate. The packet does not prove a lower bound against such a
   postprocessor.

Under those readings, I found no false mathematical claim in the frozen
theorems. I did not edit a frozen input.

## Frozen-input integrity

I read `MANIFEST.md`, hashed the three declared frozen inputs, and did not
read their mathematical contents until all three hashes matched.

| File | Expected and observed SHA-256 | Result |
|---|---|---|
| `STATEMENT.md` | `d3ca187a62f3706749cbe3f0083c25dccf7b82b21edf3c514377b2cc839c0774` | match |
| `PROOF.md` | `692c011c170e81251faa4ae590c2b927ed2ecd0b21c4c5d2d4f715aeee101484` | match |
| `SELF_AUDIT.md` | `7e86ad7e9174180912ee7cf6510a6d212c95961cf2f5655bb7ebaaea2b263a57` | match |

The manifest itself has SHA-256
`a476109cea1cfc3c0267331b02d188c190cd49a548e99df1541b49f060b52476`.

## 1. The recurrence is QP

Let

\[
S(n)=1+\max_{1\le m\le n}T(m).
\]

Choose a fixed cutoff above which `r(j)<j`. Unrolling only the coefficient-one
decrement edge gives, after absorbing the fixed base range,

\[
S(n)\le A nQ(n)S(\lceil\rho n\rceil+c).
\tag{1}
\]

For fixed `rho<sigma<1`, the last argument is at most `sigma*n` above a fixed
cutoff. Iterating (1) therefore uses `O(log n)` geometric scales. At each
scale,

\[
\log_2(An_jQ(n_j))=O((\log(n+1))^k),
\]

so

\[
\log_2 S(n)=O((\log(n+1))^{k+1}).
\]

This proves the stated numerical-QP upper bound. The proof does not require
`T` itself to be monotone because `S` is the monotone envelope.

A fixed number of side children changes only the QP coefficient. If there
are at most `Q(n)` side children and each already carries a `Q(n)`
coefficient, the coefficient can become `Q(n)^2`; this is still of the
stated QP form after doubling its fixed exponent constant. Thus the last
sentence of the recurrence proof is valid as a class statement.

If `T` denotes an expectation, the same derivation applies after the
displayed recurrence for that expectation has been justified. The theorem
does not itself justify an expected-time recurrence or independence between
recursive calls.

## 2. Exact application and the nonhereditary balanced promise

If `N` has `n` bits, then

\[
K=(N-1)/2<2^{n-1},
\]

so `K` has at most `n-1` bits. Also

\[
1\le E\le 2B<2\sqrt N
\]

on the nonsquare branch. For `N=pq` with `p<q<2p`,

\[
p<\sqrt N<q,
\qquad
q^2<2pq=2N.
\]

Hence `E`, `p`, and `q` have `n/2+O(1)` bits. At one balanced node, the
recursive calls therefore have exactly the shape required by Theorem 1:
one decrement child `K` and a fixed number of fixed-ratio side children.

The condition is not inherited by the decrement child. For example,

\[
247=13\cdot19
\]

is balanced, but its decrement child is

\[
K=123=3\cdot41.
\]

At the `123` node, the next decrement child is `61`; both `61` and the
output cofactor `41` have six bits, while `123` has seven. Thus a balanced
top-level promise alone does not establish the scalar recurrence for the
complete descendant tree.

The packet explicitly says that a branch with the decrement child and an
independent `n-O(1)`-bit output cofactor is not covered. That exclusion is
correct and is necessary for this PASS. The balanced application must be
read as local accounting, or as a conditional statement about a recursion
tree that satisfies the one-near-child invariant at every reachable node.
It is not an all-input or top-level-balanced factoring algorithm.

## 3. Early gcd branch and small inputs

For odd `N>=3`, there are two cases.

- If `E>0`, then `E<N`. Hence `1<gcd(E,N)<=E<N` is a proper factor.
- If `E=0`, then `N=B^2` and `1<B<N`. The available proper factor is `B`;
  `gcd(E,N)=N` is not proper.

Thus the early branch is factor-bearing, but the square case needs this
case split. On the surviving `gcd(E,N)=1` branch, `E>0`, `K>=1`, and all
moduli used later are valid.

The literal input `N=1` would give `K=E=M=0`, so the modular statements are
undefined. This is excluded by the standard factoring domain `N>1`; an
explicit `N>=3` hypothesis would remove the endpoint.

## 4. CRT root construction

The public identities are

\[
N=2K+1,
\qquad
N=B^2+E.
\]

For `ell^a || M`, if `v_ell(K)>=v_ell(E)`, then the full prime power
`ell^a` divides `K`, and root `1` is valid. If
`v_ell(E)>v_ell(K)`, the full prime power divides `E`, and root `B` is
valid. This remains true when a prime divides both children with equal
valuation; no congruence between `1` and `B` is required. It also includes
the 2-primary component.

The local prime powers are coprime to one another, so CRT constructs `R`
with `R^2=N mod M`. Further,

\[
\gcd(N,K)=1,
\qquad
\gcd(N,E)=1,
\qquad
\gcd(N,M)=1.
\]

If a prime divided both `R` and `M`, the congruence `R^2=N mod M` would
make it divide `N`, a contradiction. Thus `R` is a unit.

On this branch,

\[
M\le KE<N^{3/2}.
\]

All CRT moduli and residues have `O(n)` bits. The complete child
factorizations have at most `O(n)` prime-power entries, so forming `M` and
performing sequential or product-tree CRT has deterministic polynomial bit
complexity in `n`.

## 5. Exact inverse torsor and its size

For each unit `u mod M`, set

\[
(x,y)=(Ru,Ru^{-1}).
\]

Then `xy=R^2=N mod M`. Conversely, from a unit pair with `xy=N mod M`,
the unique coordinate

\[
u=xR^{-1}
\]

gives `x=Ru` and `y=Ru^{-1}`. This is a bijection, so the exact ordered
candidate count is `phi(M)`.

For a prime power,

\[
\frac{\varphi(p^a)^2}{p^a}=p^{a-2}(p-1)^2.
\]

Every odd-prime factor is greater than one. The 2-primary factor is at
least `1/2`, with equality only for `2^1`. Multiplication gives

\[
\varphi(M)^2\ge M/2.
\]

Since `M>=K=(N-1)/2`,

\[
\varphi(M)\ge\sqrt{M/2}\ge\frac{\sqrt{N-1}}2.
\]

This is an exponential local residue count. It is not an information,
running-time, or post-Archimedean candidate lower bound, and the packet does
not promote it to one.

## 6. Discriminant, swap, and character scope

For every torsor point,

\[
(x+y)^2-4N
\equiv R^2(u-u^{-1})^2\pmod M.
\]

Equivalently, because `xy=N mod M`, the discriminant is simply
`(x-y)^2 mod M`. Thus every product-consistent unit pair passes the stated
square-discriminant test.

Swapping the ordered factors sends `u` to `u^{-1}`. For a group character
of order at most two,

\[
\chi(u^{-1})=\chi(u)^{-1}=\chi(u),
\]

and every symmetric ring expression is invariant by definition. These
interfaces cannot distinguish the two orderings.

This does not make every use of a quadratic character inversion-invariant.
For a concrete boundary witness,

\[
589=19\cdot31,
\quad B=24,
\quad K=294,
\quad E=13,
\quad M=3822.
\]

Modulo the child-supported prime `7`, the chosen root is `R=1`. The two
normalized factor residues are `3` and `5=3^{-1}`. Their Legendre symbols
are equal, but

\[
\left(\frac{3+1}{7}\right)=+1,
\qquad
\left(\frac{5+1}{7}\right)=-1.
\]

A shifted-character probe can therefore distinguish the swap. This does
not supply a uniform rule that identifies the smaller integer factor, but
it shows why the theorem's exact direct-character scope must be preserved.

## 7. Support-prime Jacobi signs

Let `N=3 mod 4`. If an odd prime `ell` divides `K`, then

\[
N=1\pmod\ell,
\qquad
\left(\frac N\ell\right)=1.
\]

If `ell` divides `E`, then `N=B^2 mod ell`. The coprimality screen implies
`ell` does not divide `B`, so the same Legendre symbol is again `+1`.
Quadratic reciprocity for the coprime positive odd integers `ell,N` gives

\[
\left(\frac\ell N\right)
\left(\frac N\ell\right)
=(-1)^{((\ell-1)/2)((N-1)/2)}.
\]

Since `(N-1)/2` is odd,

\[
\left(\frac\ell N\right)
=(-1)^{(\ell-1)/2}=\chi_4(\ell).
\]

This proof is valid for composite `N`; Jacobi reciprocity is the applicable
identity. The prime `2` is explicitly excluded. Shared child support and
repeated prime powers cause no exception.

## 8. Genus characters

The frozen F202 statement and proof still match their manifest hashes. In
that formulation, the two mixed orientations have classes `C^2` and
`C^{-2}` in the proper ideal class group. A genus character is a
homomorphism to `{+1,-1}`, so

\[
\gamma(C^2)=\gamma(C^{-2})=1.
\]

For any auxiliary class `D` fixed independently of the orientation,

\[
\gamma(DC^2)=\gamma(D)=\gamma(DC^{-2}).
\]

The genus vectors are therefore identical. This proves the stated boundary
for genus characters. It does not exclude orientation-dependent auxiliary
constructions, square-root navigation inside the class group, or other
nonquadratic full-class-group operations.

## 9. Finite adversarial checks

As a sanity check, not as proof, I exhaustively checked the CRT root,
unit condition, and elementary totient bound on 798 coprime nonsquare odd
inputs through `N=1999`. I enumerated the complete torsor on 162 small
instances and checked 971 support-prime Jacobi identities for odd
`N<=1999` with `N=3 mod 4`. No counterexample occurred.

The finite scan did expose the expected square endpoint:
`N=9,25,49,81` all have `E=0` and `gcd(E,N)=N`. This is exactly the
case split in Section 3, not a defect in the surviving coprime theorem.

## Conclusion

The frozen mathematical core passes. The result must remain a conditional
recursion/accounting theorem and a boundary for the named direct local
interfaces. It does not prove that a top-level balanced promise survives
recursive factorization, and it does not prove that all quadratic or
integer-specific postprocessors are inversion-blind.
