# F166 hostile audit — PASS

## Verdict

**PASS.** The frozen statement proves exactly its narrow claim:

\[
\text{proper factor of }N
\quad\lor\quad
\text{one public element of exact common order }Me.
\]

The proof covers any number of unknown odd prime-power CRT components. It
does not need hidden-log alignment for this output. It correctly keeps
alignment for stronger global-subgroup and integer-relation outputs.

I found no theorem-level defect. I did not change a frozen input or a
durable ledger. I did not perform the blind reconstruction.

## Frozen-input integrity

The frozen files matched `MANIFEST.md` before this audit:

- `STATEMENT.md`:
  `5b245ddc902f300b89dab11c61d06dfffb2deef09d01182f4f8e6f7cce608615`
- `PROOF.md`:
  `bba045350ed11b8756d11c233d909f4f14a0225b19b5d7bab74296ced04ec4a6`
- `MANIFEST.md` itself:
  `dcf533a603c5d94124f33bfb4d1dbeb62e45b023ccd423e9c6f316e4b1b8b116`

The exact F161 inputs also match the hashes promoted as P148:

- F161 `STATEMENT.md`:
  `c999958e6b1cce04b7aa4fbf03e7b233a57c4461da66a4ba68c46cf2aaba4a32`
- F161 `PROOF.md`:
  `409bdd11bdff1dc0b571b6169f669186e16b3aac04ad7566a009f14ddeb41a27`

The needed P148 interface is exact. A first common return gives one common
local quotient order `e`, the factorization of `e`, `gcd(e,N)=1`, and
`d^(eM)=1 mod N`. The old state gives exact local order `M`, its complete
factorization, and `gcd(M,N)=1`.

## 1. Factor-first determination of `m`

Put `Q=eM`. The order of `d` modulo `N` divides `Q`. Standard divisor
stripping from the known factorization of `Q` returns the exact global
order

\[
m=\operatorname{ord}_N(d).
\]

At termination, `d^(m/ell)` is not one modulo `N` for each prime
`ell | m`. If the retained value were larger than the exact order, one
prime could still be removed. Thus the stripping proof is complete.

Let `m_j=ord_(R_j)(d)`. Then each `m_j` divides `m`. If `m_j<m`, choose a
prime `ell` with

\[
v_\ell(m_j)<v_\ell(m).
\]

Now `m_j | m/ell`, so the full prime-power component `R_j` divides
`d^(m/ell)-1`. Exactness of `m` prevents all components from doing so.
Therefore

\[
1<\gcd(d^{m/\ell}-1,N)<N
\]

for at least one screen. This is a valid factor, including when the gcd
contains only part of another prime-power component.

On the no-factor branch, every `m_j` is therefore equal to `m`. This
argument uses no squarefreeness assumption. It works for arbitrary odd
prime powers and for any number of CRT components.

The `gcd(m,N)` screen is also sound. In the stated F161 branch it is
automatically one because `m | eM`. In the more general proof it can only
be one or a proper factor because `m <= phi(N) < N`.

## 2. The lcm identity

Fix one hidden component. Its unit group is cyclic because the component
is an odd prime power. The subgroup `H_j=<g_j>` has order `M`. The coset
`d_j H_j` has exact order `e`. Hence

\[
|\langle g_j,d_j\rangle|=Me.
\]

On the no-factor branch, `g_j` and `d_j` have orders `M` and `m`. Two
elements of a cyclic group generate the unique subgroup of order

\[
\operatorname{lcm}(M,m).
\]

The two expressions describe the same local subgroup. Therefore

\[
\boxed{\operatorname{lcm}(M,m)=Me}.
\]

No coprimality between `M` and `m` is used. Prime by prime, the identity is

\[
\max(v_\ell(M),v_\ell(m))=v_\ell(M)+v_\ell(e).
\]

This closes the shared-prime case.

## 3. The public prime-primary word

For each prime `ell | L`, where `L=lcm(M,m)`, the selected word `y_ell`
has exact order `ell^v_ell(L)` in every hidden component. This follows
directly from the exact common orders of `g` and `d`.

The words commute. Their orders are pairwise coprime. Therefore their
product

\[
h=\prod_{\ell\mid L}y_\ell
\]

has exact order `L=Me` in every hidden component and modulo `N`. The
construction uses only public positive exponents.

The public certificate is also exact. Since `gcd(Me,N)=1`, every prime
`ell | L` differs from every hidden residue prime `p_j`. The reduction
kernel from units modulo `p_j^alpha_j` to units modulo `p_j` is a
`p_j`-group. It cannot kill the order-`ell` element `h^(L/ell)`. Hence

\[
\gcd(h^{L/\ell}-1,N)=1
\]

for every prime `ell | L`.

## 4. Separators and edge cases

The `N=91` separator is correct. For `(g,M,d,e)=(-1,2,30,3)`, the exact
global order of `d` is six and

\[
\gcd(30^3-1,91)=7.
\]

Thus this mismatch factors during the new order screen. It does not reach
the lcm word.

The `N=341` separator is also correct. For `(g,M,d,e)=(202,5,277,2)`, the
element `d` has common local order ten. Both order screens pass. The word

\[
h=g d^5=139\pmod {341}
\]

has exact common order ten. However,

\[
|\langle g,d\rangle|=50,
\qquad
|\langle h\rangle|=10,
\qquad
\gcd(d^2-g,341)=11.
\]

This proves the stated local-versus-global boundary.

The `e=1` edge case is correct. With the same `N,g,M` and `d=4`, the local
logarithms are one and three. The lcm remains five, but

\[
\gcd(d-g,341)=11.
\]

Thus no growth does not certify global membership. The theorem does not
claim otherwise. The cases `M=1` and `L=1` also cause no defect. The empty
prime-primary product is the identity.

## 5. Global subgroup and F164 boundary

The proof uses only local equality

\[
\langle h_j\rangle=\langle g_j,d_j\rangle.
\]

It does not infer global equality. Different component relations can make
`<g,d>` a noncyclic subdirect product. The `N=341` example proves that this
strict inclusion occurs.

This distinction preserves the F164 interface. An F164 collision word
`x` already satisfies `x^M=1`. Its relative order is one, so an lcm update
cannot add order. More importantly, the lcm word does not give the exact
global row `x=g^a`. Adding the definition of a new word does not recover
the missing relation among the old coordinates. F164 still needs
factor-first alignment for relation rank, lattice index, and rank-volume
closure.

It is safe to keep every old word and its provenance while using `(h,L)`
only as the next local common-order state. Old coordinates cannot be
discarded without later alignment or another proof of global powers.

## 6. Cost audit

Divisor stripping uses at most the prime-factor multiplicity of `Q` plus
one failed test per distinct prime. This is `O(log Q)` modular
exponentiations. The order screens and the lcm word use one operation per
distinct known prime.

All exponents have `O(log N + log e)` bits. In F161, `e` is below the
quasipolynomial cap, and the factorizations of `M` and `e` are available in
quasipolynomial time. The factorization of `m` is obtained by decrementing
known exponents of `eM`. No unknown group order is factored.

Therefore the update has deterministic quasipolynomial bit cost. If
`e>=2`, each successful update at least doubles the common order, which is
less than `N`. There are fewer than `log_2 N` strict enlargements. The proof
correctly gives no bound on `e=1` calls, source misses, or above-cap calls.

## 7. Hostile checks

I attacked these cases directly:

- shared prime factors of `M`, `m`, and `e`;
- different local orders whose lcm is the global order;
- partial prime-power gcds;
- more than two CRT components;
- ties in the prime-primary selection rule;
- `e=1`, `M=1`, and `L=1`;
- local cyclic generation with a noncyclic global subdirect product;
- reduction modulo the hidden residue primes;
- attempted use of the shortcut as an F164 lattice row;
- cost hidden in order finding or factorization.

None refuted the stated result.

As corroboration only, I exhaustively checked all qualified public inputs
for odd `3 <= N <= 175`. The run covered 343,256 inputs. It reached 496
factor-screen branches and 342,760 no-factor branches. Every no-factor
branch satisfied the common-local-order conclusion, the lcm identity, the
prime-primary word order, and every public certificate screen. It found no
failure. I also checked the three displayed `N=91` and `N=341` certificates
exactly.

This finite check is not part of the proof.

## Final classification

- Frozen hashes: **PASS**.
- Exact F161/P148 interface: **PASS**.
- Arbitrary odd prime-power CRT scope: **PASS**.
- Factor-first common local order: **PASS**.
- `lcm(M,m)=Me`, including shared primes: **PASS**.
- Prime-primary public word and order certificate: **PASS**.
- `e=1`, `N=91`, and `N=341` separators: **PASS**.
- Global-versus-local subgroup boundary: **PASS**.
- F164 implications: **PASS**.
- Deterministic quasipolynomial cost: **PASS**.
- Source theorem or complete factoring algorithm: **not claimed**.

**Overall verdict: PASS.** A separate statement-only blind reconstruction
is still required before promotion.
