# F195 V2 hostile re-audit

## Frozen-input verification

I verified `V2_MANIFEST.md` before reading any V2 candidate file. Every
observed SHA-256 digest matches its frozen value byte for byte.

| Frozen input | Manifest SHA-256 | Observed SHA-256 | Result |
|---|---|---|---|
| `V2_STATEMENT.md` | `49df39f6311c00c9fa1fc2f54b7da715783f17da10eec302373fe0fe479e2c3a` | `49df39f6311c00c9fa1fc2f54b7da715783f17da10eec302373fe0fe479e2c3a` | match |
| `V2_PROOF.md` | `bdbcbcff93de0fb1cee7ecc2783d9edf1fb066f87f9c943bec4ce1d990205bb5` | `bdbcbcff93de0fb1cee7ecc2783d9edf1fb066f87f9c943bec4ce1d990205bb5` | match |
| `V2_SELF_AUDIT.md` | `8291a0a26cf6b94b71984cbccbf692d4c7785dc6e3ef56504e6504420386b1f8` | `8291a0a26cf6b94b71984cbccbf692d4c7785dc6e3ef56504e6504420386b1f8` | match |
| `V2_PROVENANCE.md` | `e2c89261a1c76c24fe894562093561a6ef8ee00eed760d2531c7ddc1df639460` | `e2c89261a1c76c24fe894562093561a6ef8ee00eed760d2531c7ddc1df639460` | match |

The observed SHA-256 digest of `V2_MANIFEST.md` itself is
`11895df9d28a7be567a12078cbedb520c2f20da36dc42baee2d1a8f80b9608a8`.
I then read all four frozen V2 inputs in full. I did not edit a frozen file,
V1 artifact, or durable ledger. I ran no mathematical search or research
computation.

## Exact verdict

**PASS, with the strict scope readings stated below.**

V2 repairs every promotion blocker identified in the V1 hostile audit. The
largest-prime smoothness condition is exact, Bertrand's postulate preserves
the exponential lower scale, the all-low branch now calls Gao--Feng--Hu--Pan
directly without an unconstructed witness, and the Harvey--Hittmeir claim is
properly restricted to odd inputs beyond the source's fixed lookup range.
The modern primary results, parameter ranges, and bit-complexity formulas
are accurately listed and used.

Two readings must remain explicit.

1. The sentence obtained by substituting `D=N^delta` into the
   Harvey--Hittmeir bound is a same-node cost observation. It is not an
   allowed choice in the preceding P159 run when `C` is numerical QP and
   `D<=C`, since a fixed positive power of `N` eventually exceeds every
   such `C`. For an actual published-algorithm input it also requires a
   fixed `0<delta<1`, or another condition ensuring `D<N-1`.
2. For `D<=2`, equation (7) inherits Harvey--Hittmeir's small-logarithm
   convention. The asymptotic expression must not be read literally with a
   zero or undefined logarithm.

Neither point changes a theorem conclusion in the stated P159 branch. The
first sentence is used only to measure a hypothetical exponential cap; the
second is the cited primary paper's explicit convention.

F195 V2 remains a literature-dependent boundary theorem. It does not factor
the mixed high-order branch and does not prove integer factoring is in QP.

## Primary-source recheck

### Gao--Feng--Hu--Pan

I inspected the current 2025-11-11 primary revision of ePrint 2025/1004:

<https://eprint.iacr.org/2025/1004.pdf>

The current title and authors match V2. The paper measures deterministic
Turing-machine bit operations.

Theorem 3.1 assumes natural numbers `N,s`, a residue
`m in (Z/NZ)^*`, and `s,m<N`. Corollary 3.2 additionally assumes

\[
p\equiv s\pmod m
\]

for every rational prime divisor `p` of `N`. It factors `N` in

\[
O\!\left(
 \left\lceil\frac{N^{1/4}}m\right\rceil
 \log^{7+3\epsilon}N
\right)
\]

bit operations for fixed positive `epsilon`. V2 states this premise and
cost correctly.

Algorithm 4.3 assumes

\[
N=pq,\qquad cN^\beta<p\le N^\beta,
\qquad 1/3\le\beta\le1/2,
\]

where `c<1` is fixed. It also assumes

\[
m,s\in(\mathbb Z/N\mathbb Z)^*,
\quad 72<m<N^{(1-\beta)/2}/2,
\quad ms=tN+1,
\]

and a unit `alpha` satisfying

\[
\gcd(\alpha^{m^2i}-1,N)=1\quad(1\le i\le k),
\]

where

\[
k=\left\lceil
\frac{2\,3^{5/4}N^{1/2}}{c m^{3/2}}
\right\rceil.
\]

Proposition 4.5 gives exactly

\[
O\!\left(
 \varphi(m)\log^3N+
 \frac{N^{1/2}}{m^{3/2}}\log^2N
\right).
\]

V2 explicitly lists Algorithm 4.3 and Proposition 4.5 and conditions their
use on the complete published hypotheses. This repairs the V1 premise-list
defect.

### Harvey--Hittmeir

I inspected the current arXiv:2601.11131v2 primary PDF, revised 2026-06-05:

<https://arxiv.org/pdf/2601.11131>

Its title is *Deterministic methods for finding elements of large
multiplicative order*, exactly as V2 now states.

Theorem 1.1 assumes

\[
N\ge3,\qquad D\ge1,\qquad D<N-1
\]

and returns a nontrivial divisor or a unit of order above `D` in

\[
O\!\left(
 \frac{D^{1/2}\log D}{\sqrt{\log\log D}}\log N
\right)
\]

bit operations. The paper explicitly replaces the small-`D`
`log log D` expression by its bounded convention.

Lemma 2.1 determines whether an input unit has order at most `D`, and
returns the exact order when it does. With
`r=min(ord_N(alpha),D)`, its precise cost is

\[
O\!\left(
 \frac{r^{1/2}}{\sqrt{\log\log r}}
 (\log r+\log\log N)\log N
\right).
\]

Lemma 2.2 is the exact lcm-order combination routine. Lemma 2.3 is the
prime-primary local-order screen. Lemma 2.4 states, for
`x>=y>=2` and `x>=4`,

\[
\Psi(x,y)\ge
\frac{x}{(\log x)^{\log x/\log y}}.
\]

V2 lists all four lemmas actually relevant to its order and smoothness
claims.

Algorithm 3.1 has the exact control flow used below:

- line 1 handles `N<N_0` by a finite lookup;
- line 2 returns `2` as a divisor when `N` is even;
- line 3 returns the unit `2` if `2^D<N`;
- lines 5--6 initialize `alpha=M=1` and start the loop at `beta=2`;
- lines 7--10 perform the divisibility, subgroup, and bounded-order tests;
- lines 11--16 process low orders;
- lines 17--19 form the later smooth-number stage.

V2's source list, version, title, theorem range, and line references are
correct.

## 1. Common-order injection and terminal

Fix a hidden prime power `p^a | N`. The reduction kernel

\[
(\mathbb Z/p^a\mathbb Z)^*\longrightarrow
(\mathbb Z/p\mathbb Z)^*
\]

is a `p`-group. The cyclic subgroup generated by `g` has order `M`, while
`gcd(M,N)=1` implies `p` does not divide `M`. Its intersection with the
kernel is therefore trivial. Reduction is injective on the subgroup, so

\[
\operatorname{ord}_p(g)=M.
\]

Fermat's theorem gives `M | p-1`. This also proves the source's omitted
range conditions rather than assuming them:

\[
M\le p-1<N,
\qquad
M\in(\mathbb Z/N\mathbb Z)^*.
\]

Thus Gao--Feng--Hu--Pan Corollary 3.2 applies with `s=1,m=M`. Repeated prime
powers cause no defect, because the published corollary needs congruences
only for rational prime divisors.

For the threshold comparison, put `A=N^(1/4)/M`. Then

\[
\frac{\sqrt N}{M^2}=A^2.
\]

Numerical-QP bounds are closed under squaring, and `A<=1+A^2` gives the
converse. Ceilings do not change the class. V2 correctly distinguishes a
smaller same-node cost and broader scope from an unchanged QP threshold.

## 2. Harvey--Hittmeir beta-two exit

The assumption `N>=N_0` excludes line 1. Oddness excludes line 2. The P159
certificate and `1<=D<=C` give

\[
\operatorname{ord}_N(2)>D.
\]

They also imply `D<N-1`. If `N` is composite, this follows from
`ord_N(2)<=phi(N)<N-1`; if `N` is prime, strictness of
`ord_N(2)>C>=D` and `ord_N(2)<=N-1` gives the same integer inequality.

If `2^D<N`, the powers `2^0,...,2^D` are distinct positive integers below
`N`, so line 3 correctly returns `2` with order above `D`.

Otherwise the loop is reached. Its first state has `M=1,beta=2`. Line 7
does not return because `N` is odd. Line 8 does not skip because
`2^1` is not `1 modulo N`. Lemma 2.1 reports order above `D`, and line 10
returns `2`. Therefore the algorithm exits no later than beta two and never
reaches lines 11--19 on this branch.

After line 3 fails, `D>=log_2 N`. Hence `log D` absorbs the `log log N`
term in Lemma 2.1, giving the displayed Theorem 1.1 scale. Numerical-QP
`D` makes the call numerical QP. Same-node work is done before an output and
cannot be charged to a smaller recursive child. The recurrence distinction
is correct.

As noted in the verdict, the `D=N^delta` sentence is only an evaluation of
this cost formula outside the preceding QP-capped P159 run. With fixed
`0<delta<1`, that evaluation is

\[
N^{\delta/2+o(1)}.
\]

It does not assert that a numerical-QP `C` certifies beta two above that
larger threshold.

## 3. Rank-three scale and exact smoothness repair

At `beta=1/2`, the published upper range is

\[
m<N^{1/4}/2.
\]

Therefore

\[
m^{3/2}<2^{-3/2}N^{3/8}.
\]

Substitution into the exact formula for `k` gives

\[
k\ge \frac{2^{5/2}3^{5/4}}c N^{1/8},
\]

so every legal choice has `k=Omega(N^(1/8))`. The constant depends only on
the fixed balance constant `c`.

The two costs quoted in V2 match Proposition 4.5. At exponent scale,
`phi(m)=m^{1+o(1)}`. If `m=N^a`, their exponents are

\[
a,
\qquad
\frac12-\frac{3a}{2},
\]

which meet at `a=1/5`. Logarithmic and `phi(m)/m` factors affect only the
`o(1)` term.

The order-bound interface is correctly identified as sufficient. If every
local order exceeds `C` and `m^2k<=C`, no tested positive exponent can be a
multiple of a local order. The ceiling in `k` is negligible throughout the
legal range, because its unrounded term is already `Omega(N^(1/8))`. Hence

\[
m^2k=\Theta(N^{1/2}m^{1/2}).
\]

This is exponential in the input bit length over the whole legal interval.

For the rough-order route, an integer is `T`-smooth exactly when all of its
prime factors are at most `T`. Thus every `i` in `1,...,k` is `T`-smooth if
and only if

\[
P(k)\le T,
\]

where `P(k)` is the largest prime at most `k`. If `m` is also `T`-smooth,
then every `m^2i` is `T`-smooth. A `T`-rough local order has no common prime
factor with such an exponent, so the exponent cannot annihilate the
nonidentity local element.

For even `k`, Bertrand's postulate applied to `k/2` gives a prime strictly
between `k/2` and `k`. For odd `k`, apply it to `floor(k/2)`; the resulting
integer prime is again greater than `k/2` and below `k`. Hence, for the large
values in scope,

\[
T\ge P(k)>k/2=\Omega(N^{1/8}).
\]

This is the exact repaired deduction. It proves the intended direct-interface
obstruction without the false V1 inequality `T>=k`.

## 4. All-low smooth-prime branch

The corollary is restricted to a balanced distinct semiprime `N=pq`.
For each rational prime `beta<=B`, the initial gcd either factors `N` or
certifies a unit. Lemma 2.1 then returns an exact global order `m<=D` or
reports order above `D`.

In the low case, factor `m` and compute

\[
G_r=\gcd(\beta^{m/r}-1,N)
\]

for every prime `r | m`. The value `N` is impossible because `m` is the
exact global order. A proper value factors. If every value is one, each
local order divides `m` but cannot divide `m/r` for any `r | m`. Its
valuation at every prime of `m` is therefore maximal, so both local orders
equal `m`. This is exactly Harvey--Hittmeir Lemma 2.3.

Assume every scanned prime is synchronized low, and let `M` be the public
lcm of their orders. Then

\[
M\mid p-1,
\qquad
M\mid q-1.
\]

It follows immediately that

\[
M<N,
\qquad
\gcd(M,N)=1,
\qquad
p,q\equiv1\pmod M.
\]

These are all hypotheses needed for a direct Gao--Feng--Hu--Pan Corollary
3.2 call with `s=1,m=M`. No single group element of order `M` is required,
and V2 no longer claims otherwise.

The scan also proves `p>B`; otherwise the rational prime `p` would have
exposed a factor. Thus every `B`-smooth positive integer `x<=p` is actually
below `p`, is nonzero modulo `p`, and is a product of scanned primes. Hence

\[
x^M=1\pmod p.
\]

The polynomial `X^M-1` has at most `M` roots in the field, so

\[
\Psi(p,B)\le M.
\]

For

\[
B=\exp((\log(n+2))^3),
\]

one has `log B=o(n)` and `log B/log n` tending to infinity. Since a balanced
hidden prime satisfies `log p=Theta(n)`, eventually `p>=B>=2`, and
Harvey--Hittmeir Lemma 2.4 applies. Taking logarithms gives

\[
\log\Psi(p,B)
\ge
\log p-
\frac{\log p}{\log B}\log\log p
=\log p-O\!\left(\frac{n}{(\log n)^2}\right).
\]

The loss is `o(n)`, so

\[
M\ge\Psi(p,B)=p^{1-o(1)}=N^{1/2-o(1)}.
\]

Consequently `N^(1/4)/M<1` for every sufficiently large input in scope,
and the direct Corollary 3.2 call has QP cost.

The scan itself is QP. There are at most `B` bases. Deterministic prime
enumeration through `B`, every Lemma 2.1 call, trial division of each
`m<=D`, lcm updates, modular powers, and gcd screens all use numerical-QP
bit time. The intermediate lcm in fact divides both `p-1` and `q-1`, so it
is below `N` throughout.

## Remaining boundary

The mixed branch supplies at least one small ordinary integer of global
order above `D`. V2 correctly proves no independence, exact high order, or
factor from several such witnesses. The carry recurrence reduces modulo
each hidden factor to the same orbit generated by `2`; the text makes only
a named-interface observation and no general impossibility claim.

The result is therefore exact within its declared scope. No further repair
is required before the separately mandated statement-only reconstruction.

