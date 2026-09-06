# F195 hostile audit

## Frozen-input verification

I verified the manifest before reading the candidate. The three observed
SHA-256 digests match the frozen values byte for byte.

| Frozen input | Manifest SHA-256 | Observed SHA-256 | Result |
|---|---|---|---|
| `STATEMENT.md` | `c24ae917a6f8ee3d4de9b89c2b6c576e15c603241085b12a4a00af59e508f88e` | `c24ae917a6f8ee3d4de9b89c2b6c576e15c603241085b12a4a00af59e508f88e` | match |
| `PROOF.md` | `a33e742566b1f4024037ff227f2da138eb1398d5c15f410b2f1aa29df88fede2` | `a33e742566b1f4024037ff227f2da138eb1398d5c15f410b2f1aa29df88fede2` | match |
| `SELF_AUDIT.md` | `96726cf39f24071977d0122586f9f7f7e0e00d0bd39bbf6141c988d620609c2b` | `96726cf39f24071977d0122586f9f7f7e0e00d0bd39bbf6141c988d620609c2b` | match |

The observed SHA-256 digest of `MANIFEST.md` itself is
`216b1a3fe08d11365750188cedd455d92415df07fdb3aa8a1f3670519037b88e`.
I then read `STATEMENT.md`, `PROOF.md`, and `SELF_AUDIT.md` in full. I did
not edit a frozen input or a durable ledger. I ran no mathematical search or
research computation.

## Exact verdict

**FAIL — the frozen candidate is not promotion-ready.**

The common-order kernel argument, the Gao--Feng--Hu--Pan terminal, its QP
threshold comparison, the asymptotic beta-two return, the rank-three
`N^(1/8)` list floor, and the mathematical content of the smooth-prime fork
all survive reconstruction. However, the frozen proof contains one false
inequality and one formal missing-premise application:

1. `PROOF.md` says that making every `i <= k` smooth below the P161 cap
   requires `T >= k`. This is false. The exact requirement from these
   indices is

   \[
   T\ge P(k),
   \]

   where `P(k)` is the largest prime at most `k`. For example, every integer
   through `10` is `7`-smooth. Thus `T=7<10` covers that prefix. Bertrand's
   postulate gives `P(k)>k/2` for the relevant large `k`, so the intended
   exponential obstruction remains valid with `T=Omega(k)`. That repair is
   not the argument written in the frozen proof.
2. The all-low fork constructs the public integer `M`, proves
   `M | p-1` and `M | q-1`, and proves the numerical condition (6). It does
   not construct or name one public element `g` of exact local order `M`.
   Theorem 1, as stated, assumes such a `g`. Therefore the sentence
   "Theorem 1 applies" does not follow from the premises that the frozen
   proof explicitly established. The branch can be repaired either by
   invoking Gao--Feng--Hu--Pan Corollary 3.2 directly from the already-proved
   congruences, or by constructing `g` primary part by primary part. Neither
   repair appears in the frozen version.

There is also a smaller control-flow overstatement. Harvey--Hittmeir
Algorithm 3.1 has a finite lookup at line 1 and an even-input exit at line 2
before the `2^D < N` test at line 3. The exact claim is that an odd input
which passes lines 1--3 returns at beta two on the P159 branch. The frozen
conditional mentions only failure of line 3. The inherited P159 scope is odd
and already removes a fixed finite range, so this does not affect the
asymptotic conclusion. It is still not the literal control flow of the cited
algorithm unless the two absolute thresholds are explicitly aligned.

The first finding alone prevents an exact hostile-audit pass. The following
reconstructions classify the defects. They are not silent substitutions into
the frozen proof.

## Primary-source audit

### Gao--Feng--Hu--Pan 2025

I inspected the current primary ePrint revision, dated 2025-11-11:

<https://eprint.iacr.org/2025/1004.pdf>

The paper uses deterministic Turing-machine bit operations. Its Theorem 3.1
assumes natural numbers `N,s`, a residue `m in Z_N^*`, and `s,m<N`. Given
`s,m`, it finds the primes `p` with

\[
p\equiv s\pmod m,\qquad p^r\mid N
\]

in

\[
O\!\left(
 \left\lceil\frac{N^{1/(4r)}}m\right\rceil
 \frac{\log^{7+3\epsilon}N}{r^{2+\epsilon}}
\right)
\]

bit operations. Corollary 3.2 sets `r=1` and assumes the congruence for
every rational prime divisor of `N`. Its displayed complexity is exactly

\[
O\!\left(
 \left\lceil\frac{N^{1/4}}m\right\rceil
 \log^{7+3\epsilon}N
\right).
\]

Thus equation (1) in F195 is accurate under a fixed positive `epsilon` and
the paper's stated input conditions.

I also inspected Algorithm 4.3 and Proposition 4.5. For
`N=pq`, `cN^beta<p<=N^beta`, `1/3<=beta<=1/2`, and fixed `c<1`, the
algorithm assumes

\[
m,s\in Z_N^*,\qquad
72<m<\frac{N^{(1-\beta)/2}}2,\qquad ms=tN+1,
\]

and an `alpha in Z_N^*` satisfying

\[
\gcd(\alpha^{m^2i}-1,N)=1\quad(1\le i\le k),
\qquad
k=\left\lceil\frac{2\,3^{5/4}N^{1/2}}{c m^{3/2}}\right\rceil.
\]

Proposition 4.5 gives

\[
O\!\left(\varphi(m)\log^3N+
          \frac{N^{1/2}}{m^{3/2}}\log^2N\right).
\]

These are the parameter range and bit-complexity formula used by F195.
They are additional published inputs beyond Theorem 3.1 and Corollary 3.2,
although the opening list of external premises does not list them.

### Harvey--Hittmeir 2026

I inspected arXiv:2601.11131v2, revised 2026-06-05:

<https://arxiv.org/pdf/2601.11131>

The primary title is *Deterministic methods for finding elements of large
multiplicative order*. F195's bibliography gives a different title, although
the URL and version identify the correct paper.

Theorem 1.1 assumes

\[
N\ge3,\qquad D\ge1,\qquad D<N-1,
\]

and gives exactly

\[
O\!\left(
 \frac{D^{1/2}\log D}{\sqrt{\log\log D}}\log N
\right)
\]

bit operations, with the paper's convention that `log log D` is replaced
by `log log max(D,3)` for small `D`.

Lemma 2.1 is slightly more precise than F195 needs. If
`r=min(ord_N(alpha),D)`, its cost is

\[
O\!\left(
 \frac{r^{1/2}}{\sqrt{\log\log r}}
 (\log r+\log\log N)\log N
\right).
\]

Algorithm 3.1 has the following relevant lines.

- Line 1 handles `N<N_0` by a lookup.
- Line 2 returns the factor `2` for even `N`.
- Line 3 returns `alpha=2` if `2^D<N`.
- Lines 5--6 initialize `alpha=M=1` and start `beta=2`.
- Line 7 tests `beta | N`.
- Line 8 skips `beta` only if `beta^M=1 mod N`.
- Line 9 invokes Lemma 2.1.
- Line 10 returns `beta` if its order is above `D`.
- Lines 11--16 handle a found low order and maintain an lcm-order element.
- Lines 17--19 are the later smooth-number stage.

Lemma 2.3 is exactly the local-order synchronization screen used in F195.
Lemma 2.4 states, for `x>=y>=2` and `x>=4`,

\[
\Psi(x,y)\ge
\frac{x}{(\log x)^{\log x/\log y}}.
\]

These source statements support the reconstructed claims below.

## 1. Common-order kernel and arithmetic-progression terminal

Fix `p^a | N`. The kernel of

\[
(\mathbb Z/p^a\mathbb Z)^*\longrightarrow
(\mathbb Z/p\mathbb Z)^*
\]

is a `p`-group. If the local order of `g` is `M` and `p` does not divide
`M`, then the cyclic group generated by `g` intersects that kernel
trivially. Hence reduction is injective on that cyclic group and

\[
\operatorname{ord}_p(g)=M.
\]

It follows that `M | p-1`. This also verifies the source condition `M<N`,
which F195 leaves implicit: in fact `M<=p-1<N`. The assumption
`gcd(M,N)=1` says that `M` is a unit modulo `N`. Therefore the Gao--Feng--
Hu--Pan call with `s=1,m=M` satisfies every hypothesis:

- `s,m<N`;
- `m in Z_N^*`;
- every rational prime `p | N` obeys `p=1 mod M`.

The complexity (5) is correct. The deduction works for repeated prime
powers because only the rational-prime congruence enters Corollary 3.2.

The comparison with the prior balanced enumeration is also exact. Put

\[
A=\frac{N^{1/4}}M.
\]

Then

\[
\frac{\sqrt N}{M^2}=A^2.
\]

If `A` is numerical QP, then `A^2` is numerical QP. Conversely, if `A^2`
is numerical QP, then `A<=1+A^2` is numerical QP. Ceilings do not change
this equivalence. Thus the new terminal reduces the same-node search cost
and enlarges the input scope, but it does not change the QP threshold class.

## 2. Beta-two control flow and same-node cost

On the P159 hard branch, `N` is odd and

\[
\operatorname{ord}_N(2)>C\ge D.
\]

This inequality also ensures the theorem's upper input condition:
`D<N-1`, because the order of a unit modulo an odd composite is strictly
less than `N-1`. The algorithm still requires the implicit lower condition
`D>=1`.

If line 3 returns `2`, its order is indeed above `D`: the powers
`2^0,2^1,...,2^D` are distinct positive integers below `N`, so they cannot
collide modulo `N`.

Assume instead that an odd input has passed lines 1--3. At the first loop
iteration, `M=1` and `beta=2`. Line 7 does not return. Line 8 does not skip,
because `2^1` is not `1 modulo N`. Lemma 2.1 reports order above `D`, and
line 10 returns `2`. Lines 11--19 are not reached. This proves the intended
"no later than beta two" conclusion after adding the omitted line-1
condition.

When line 3 has failed, `D>=log_2 N`, so the `log log N` term in Lemma 2.1
is absorbed by `log D`. Theorem 1.1 therefore gives equation (2). For a
fixed `0<delta<1`, taking `D=N^delta` gives

\[
N^{\delta/2+o(1)}
\]

same-node work. No smaller recursive child is produced before that work is
done. The one-child recurrence observation in F195 is therefore correct.

## 3. Rank-three list floor, cost, and roughness defect

Set `beta=1/2` in the primary Algorithm 4.3. Its legal upper range is

\[
m<N^{1/4}/2.
\]

Consequently

\[
m^{3/2}<2^{-3/2}N^{3/8},
\]

and the exact formula for `k` gives

\[
k\ge \frac{2^{5/2}3^{5/4}}c N^{1/8}.
\]

Thus `k=Omega(N^(1/8))` is correct for fixed balance constant `c`.

The Proposition 4.5 cost is exactly equation (10). At exponential scale,
`phi(m)=m^{1+o(1)}`. Writing `m=N^a`, the two exponents are

\[
a,\qquad \frac12-\frac{3a}{2}.
\]

They meet at `a=1/5`. The `N^(1/5+o(1))` scale is therefore correct.

If every local order of `alpha` exceeds `C`, the inequality
`m^2 k<=C` is a sufficient direct consequence interface: every tested
exponent `m^2 i` is then below the local order and cannot annihilate a local
component. Since the unrounded term in `k` is already at least a constant
times `N^(1/8)`, the ceiling is harmless, and

\[
m^2k=\Theta(N^{1/2}m^{1/2}).
\]

This is exponential in `n` throughout the legal range.

For the P161 route, let each local order be `T`-rough. A `T`-smooth
exponent is coprime to that order and cannot annihilate the nonidentity
local element. To apply this to every `m^2i`, one needs both

\[
P^+(m)\le T
\]

and every `i<=k` to be `T`-smooth. The second condition is equivalent to

\[
P(k)\le T,
\]

not to `k<=T`. Bertrand's postulate gives `P(k)>k/2` for the large values in
scope. Hence any such cap still satisfies

\[
T=\Omega(k)=\Omega(N^{1/8}),
\]

which is outside numerical QP. The asymptotic gate survives. The frozen
exact inequality does not.

## 4. Low/high small-prime fork

The fork is scoped to a balanced distinct semiprime `N=pq`. Within this
scope, its order synchronization is correct.

For each rational prime `beta<=B`, first taking `gcd(beta,N)` either factors
or supplies a unit. Lemma 2.1 then either reports order above `D` or returns
the exact global order `m<=D`. Trial division factors `m` in numerical-QP
time. For each prime `r | m`, consider

\[
G_r=\gcd(\beta^{m/r}-1,N).
\]

The value `N` is impossible because `m` is the exact global order. A proper
value factors. If all values are one, let `d_p=ord_p(beta)`. Since
`d_p | m`, any strict loss in the `r`-primary valuation would imply
`d_p | m/r`, contrary to `G_r=1`. Thus `d_p=m` for every hidden rational
prime, primary part by primary part. This is also Harvey--Hittmeir Lemma
2.3.

The same screen itself remains valid with repeated prime powers. Once
`ord_p(beta)=m`, the order modulo `p^a` is a multiple of `m`; it also divides
the known global order `m`, so it equals `m`. The smooth-number corollary,
however, is stated only for the balanced distinct-semiprime core.

Assume every scanned rational prime is synchronized low, and let `M` be the
lcm of the exact orders. Then

\[
M\mid p-1,\qquad M\mid q-1.
\]

In particular, `M<N` and

\[
\gcd(M,N)=1.
\]

The latter conclusion uses both local divisibilities. It is valid in the
declared squarefree scope.

The scan also proves `p>B`; otherwise the rational prime `p` itself would
have produced a factor. Every `B`-smooth `x<=p` is therefore nonzero modulo
`p` and is a product of scanned primes. Hence

\[
x^M=1\pmod p.
\]

Distinct positive integers below `p` give distinct field elements, and a
nonzero polynomial of degree `M` has at most `M` roots. Therefore

\[
\Psi(p,B)\le M.
\]

For the displayed choice

\[
B=\exp((\log(n+2))^3),
\]

Harvey--Hittmeir Lemma 2.4 gives

\[
\log\Psi(p,B)
\ge
\log p-
\frac{\log p}{\log B}\log\log p.
\]

On balanced inputs, `log p=Theta(n)`. The subtracted term is
`O(n/(log n)^2)=o(n)`. Thus

\[
M\ge\Psi(p,B)=p^{1-o(1)}=N^{1/2-o(1)}.
\]

It follows that `N^(1/4)/M<1` for all sufficiently large inputs. The
numerical terminal condition is correct by an exponential margin.

The scan cost is numerical QP. There are at most `B` bases. Each bounded
order search costs numerical QP, each order factorization by trial division
costs at most `D^(1/2+o(1))`, and each primary screen uses only
polylogarithmically many modular powers and gcds.

### Missing witness in the frozen theorem application

The preceding argument proves all congruences needed by Gao--Feng--Hu--Pan
Corollary 3.2. Thus the branch's factoring conclusion is mathematically
recoverable by calling that published corollary directly with `s=1,m=M`.
The frozen text instead calls Theorem 1, whose stated premise includes one
public `g` of exact common local order `M`. No such `g` is constructed in
Section 4.

For classification only, a valid construction would be the following. For
each prime `ell | M`, choose a scanned base whose order `m_beta` has maximal
`ell`-adic valuation `e=v_ell(M)`, and set

\[
h_\ell=\beta^{m_\beta/\ell^e}.
\]

It has exact order `ell^e` in both hidden components. The product of all
`h_ell` has exact order `M` in both components because these primary orders
are pairwise coprime. This is also the content of the lcm-combination step
in Harvey--Hittmeir Lemma 2.2. The required factorizations are known, and
the construction is numerical QP. The frozen proof does not contain this
step and cannot receive it during an audit.

The mixed branch containing one or more high-order ordinary primes remains
open exactly as stated. The proof does not infer independent cyclic
directions, exact high orders, or a factor from those witnesses.

## 5. Carry paragraph and remaining scope

The integer identities

\[
x_e=[2^e]_N,\qquad x_{e+1}=2x_e-c_eN,
\qquad c_e\in\{0,1\}
\]

are exact. Reduction modulo either hidden prime leaves the same exponent
orbit generated by `2`. The displayed transcript does not by itself supply
the `p mod m` input to Algorithm 4.3 or a bank of independent small bases
for the smooth-number argument. F195 correctly stops at this interface
observation and states no lower bound against other carry-sensitive
constructions.

Two documentary points should also be fixed in a new version.

1. The opening assertion that all claims are conditional only on the
   enumerated published premises omits Gao--Feng--Hu--Pan Algorithm 4.3 and
   Proposition 4.5, and the smooth-number estimate used in Section 4.
2. The first term in equation (10) is printed as `varphi(m)log^3 N` rather
   than `varphi(m)\log^3 N`. Its intended meaning is clear and matches the
   primary source, but the mathematical typesetting is defective.

## Required disposition

Do not promote the frozen F195 candidate. Preserve it unchanged. A new
version should, at minimum:

1. replace the false `T>=k` necessity by the exact largest-prime condition
   and derive `T=Omega(k)`;
2. either call Gao--Feng--Hu--Pan Corollary 3.2 directly in the all-low
   branch or explicitly construct the common-order witness required by
   Theorem 1;
3. state the complete Harvey--Hittmeir pre-loop conditions; and
4. list every published result actually used and correct the primary title.
