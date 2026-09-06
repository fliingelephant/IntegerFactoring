# F220 hostile audit — failed

## Verdict

**FAIL as frozen.** The primary certificate, generalized-CRT transition,
GFHP invocation, stopped-drift theorem, and exact four-case CRT-uniform law
all survive hostile reconstruction. The universal predecessor ceiling and
the bounded-gap probability bound also survive.

Two claims in Theorem E do not.

1. Equations (E3) and (E9) compare the attainable modulus with the rounded
   power-of-two drift target `R_*`, then call this an obstruction to the GFHP
   terminal. GFHP already applies at the smaller threshold
   `N^(1/4)/S(n)`. The factor-of-less-than-two gap is realizable, so both
   terminal-obstruction claims are false as written.
2. The cyclic-direction claim says that equal complete local orders prevent
   factor-first stripping from splitting. This is false for repeated
   rational-prime powers unless the common order is coprime to `N` (or the
   theorem is restricted to squarefree `N`). An order-primary element can
   become the identity modulo the residue field while remaining nonidentity
   modulo the full prime power, producing a partial-power gcd.

Both defects have short exact certificates below. They do not damage
Theorems A--D or the bounded-gap conclusion, but a frozen theorem containing
false exact obstruction claims cannot pass.

## Audit method and computation declaration

I read `MANIFEST.md` before opening any frozen candidate file. I then
recomputed the four required content hashes. I used no mathematical script,
finite search, random sampling, remote run, web search, or numerical fit.
The two small certificates below are direct exact arithmetic checks, not
search output. I did not edit a frozen input or a durable ledger. I wrote
only this audit.

## 1. Frozen-input integrity

All four candidate hashes match the manifest exactly.

| Artifact | Expected and observed SHA-256 | Result |
|---|---|---|
| `STATEMENT.md` | `d13ee7bfcf291a581c25382f8fc35cea7824edfaa7b7f4d5a198643b18b46184` | match |
| `PROOF.md` | `e1561d3be5681500a109ebf568c5f34209e36588388e9723e652af11d35704e7` | match |
| `SELF_AUDIT.md` | `a4fd4eb2c5df778d58c65d0dee0728413ea0b8fcb231d0add90cd8747b160201` | match |
| `PROVENANCE.md` | `34687ee6e68f399d1f593a514c513a39cb16d05ec2b2f152f6c73c19e95b6472` | match |

The four cited local source identities also match their declared hashes:
`PROMPT.md`, P160's statement, P165's statement, and P175's statement. The
relevant `PROVED.md` entries agree with the interfaces imported by F220.

## 2. Fatal threshold defect in (E3) and (E9)

Put

\[
T=\frac{N^{1/4}}{S(n)}.
\]

Theorem B invokes GFHP as soon as `L >= T`. Since `L` is an integer, the
exact discrete target is `ceil(T)`. Theorem C deliberately chooses the
stronger convenient target

\[
R_*=2^{\max\{0,\lceil\log_2T\rceil\}},
\]

so that a strict divisibility update drops a floored binary-log potential.
In general,

\[
T\le R_*<2T,
\]

and `L >= R_*` is sufficient but not necessary for GFHP.

Therefore

\[
\operatorname{lcm}(2^t,D_N)<R_*
\]

only obstructs the chosen drift target. It does not imply that the
attainable ceiling is below the GFHP threshold. The same error occurs with
`c` in (E9).

This is not a merely formal gap. Take

\[
N=67\cdot73=4891,\qquad S(n)=2,\qquad t=1.
\]

The input satisfies the balanced-semiprime promise, and

\[
D_N=\gcd(66,72)=6,
\qquad
\operatorname{lcm}(2,D_N)=6.
\]

Moreover,

\[
8^4=4096<N<12^4=20736.
\]

Hence

\[
4<T=\frac{N^{1/4}}2<6,
\qquad H=3,
\qquad R_*=8.
\]

Thus (E3) holds because `6 < 8`, but the attainable value `L=6` already
satisfies `L > T`, so Theorem B's GFHP interface applies. The value `M=6`
is admissible and certifiable: both prime fields contain elements of exact
order six, and CRT combines them into a witness for `A=6` whose two primary
gcd tests are one.

The same example refutes (E9). Choose a synchronized cyclic direction of
order `c=6` in the two prime fields. Then

\[
\operatorname{lcm}(2,c)=6<R_*=8,
\]

but a sample with exponent coprime to six supplies full order six and
reaches the actual GFHP threshold.

The exact repairs are either:

- replace `R_*` in the obstruction hypotheses by `T` (equivalently, compare
  the integer ceiling with `ceil(T)`); or
- state only that these inequalities obstruct the deliberately rounded
  drift target `R_*`, not the GFHP terminal.

## 3. Fatal prime-power injection defect in the cyclic obstruction

Section 9 argues that synchronized equality of complete local orders makes
factor-first stripping unable to split the hidden components. Equality of
orders is not enough over repeated prime powers. Reduction

\[
(\mathbb Z/r^f\mathbb Z)^\times\longrightarrow\mathbb F_r^\times
\]

is injective only on prime-to-`r` torsion. If the common order contains
`r`, a nonidentity modulo `r^f` can reduce to the identity modulo `r`.
The resulting gcd can contain a proper part of `r^f`.

An exact certificate is

\[
N=63=3^2\cdot7,
\qquad c=3.
\]

In the two hidden local groups choose

\[
g_1=4\pmod9,
\qquad g_2=2\pmod7.
\]

Both have exact order three. Their CRT combination is

\[
a=58\pmod{63}.
\]

For the synchronized exponent `z=1`, both complete local orders are three,
and `a^3 = 1 mod 63`. Nevertheless the sole primary stripping test gives

\[
\gcd(a^{3/3}-1,N)
=\gcd(57,63)
=3,
\]

a proper factor. Thus the assumptions displayed in (E6) hold, but stripping
does split a repeated prime-power component and terminates by a factor.

The probability identity (E8) remains correct for the abstract lcm of the
orders `c/gcd(c,z)`: the full `ell`-part is missing after `k` independent
uniform exponents exactly when all `k` exponents are divisible by `ell`.
What fails is the inference that the public factor-first processor can only
accumulate those orders and never factor.

This claim becomes correct if (E6)--(E9) explicitly assume

\[
\gcd(c,N)=1,
\]

or if they are restricted to squarefree `N`. On squarefree `N`, the
existence of order `c` in every prime-field component already gives
`c | r-1` for every `r | N` and hence `gcd(c,N)=1`.

## 4. Theorem A survives: every primary certificate is universal

Fix a rational prime `r | N` and let `o_r` be the order of `a` modulo `r`.
The global identity gives `o_r | A`. If

\[
\gcd(a^{A/\ell}-1,N)=1,
\]

then `a^(A/ell)` is nonidentity modulo every such `r`, so
`o_r` does not divide `A/ell`. Since `ell^e || A`, this forces

\[
v_\ell(o_r)=e.
\]

Lagrange then gives `ell^e | r-1`. No equality of complete local orders and
no hypothesis `gcd(A,N)=1` is used. If `ell=r`, the gcd-one branch is simply
impossible, as it must be. Lcm aggregation preserves divisibility by every
`r-1`.

I found no hidden prime-power injection step in this proof: it works directly
in each prime field.

## 5. Theorem B survives: generalized CRT, unit modulus, and GFHP

The true factor `p` satisfies both congruences, so compatibility modulo

\[
g=\gcd(2^t,M)
\]

is automatic. Dividing the congruence by `g` leaves the invertible
coefficient `2^t/g` modulo `M/g`, and the solution modulus is exactly

\[
L=\operatorname{lcm}(2^t,M),
\]

not the product.

The proof of `gcd(L,N)=1` is sound. The dyadic part is coprime to odd `N`.
If a rational prime `rho` divided both `M` and `N`, universality would give
`M | rho-1`, contradicting `rho | M`.

For canonical `0 <= s < L`, the relation `p = s mod L` and
`gcd(p,L)=1` make `s` nonzero. If `p < L`, then `s=p`, so the preliminary
gcd returns `p`. Equality `L=p` is excluded by `gcd(L,N)=1`. Therefore a
nonfactor branch has

\[
1\le s<L<p<N.
\]

These are exactly the P175/GFHP interface hypotheses, now with a general
unit modulus. Its stated cost is numerical QP when `L >= T`. Formula (B7)
also correctly measures growth of `L`; it does not double-count a primary
power already supplied by `2^t`.

## 6. Theorem C survives: stopped drift and useful-event mass

On a nonterminal state, strict lcm growth has integral ratio at least two.
It therefore raises the floored binary logarithm by at least one and lowers
`Phi` by at least one. The potential is nonnegative and at most `H=O(n)`.

Stopping at `tau`, conditional drift at least `1/Q(n)` gives

\[
Q(n)^{-1}\mathbb E[m\wedge\tau]
\le \Phi_0.
\]

Monotone convergence yields

\[
\mathbb E\tau\le\Phi_0Q(n)=O(nQ(n)),
\]

so termination is almost sure and the expected total bit cost is numerical
QP under the stated uniform per-stage cost bound. No independence is used.

Let `E` be factor return or `c` not dividing the current `L`. Off `E`, the
decrement is zero; on `E`, it lies between one and `H` at a nonterminal
history. Consequently useful-event mass at least `1/Q` implies the drift,
while the drift implies useful-event mass at least `1/(HQ)`. The claimed
`O(n)` equivalence is correct. The `H=0` case has no nonterminal histories
and is vacuous.

For iid witnesses, a no-progress result leaves `L` fixed, so the geometric
waiting-time statement is also correct. Independence across stages is used
only there, not in the drift theorem.

## 7. Theorem D survives for arbitrary odd prime powers

Let `R_j=r_j^f_j`, `h_j=phi(R_j)`, and
`d_j=gcd(A,h_j)`. The explicit hypothesis `gcd(A,N)=1` removes the
`r_j`-primary part of `h_j`, so

\[
d_j=\gcd(A,r_j-1).
\]

For a uniform CRT unit:

- full return modulo `R_j` has probability `d_j/h_j`;
- nonreturn even modulo `r_j` has probability
  `1-d_j/(r_j-1)`.

This proves the different denominators in `Gamma` and `B`. Conditioning on
full return restricts each independent local coordinate to its cyclic
`A`-root subgroup, uniformly and independently.

For `ell^e || A`, an inactive coordinate
`v_ell(d_j)<e` gives identity deterministically after exponent `A/ell`.
An active coordinate `v_ell(d_j)=e` maps uniformly onto a subgroup of order
`ell`, so its identity probability is `1/ell`. Because `ell | A` and
`gcd(A,N)=1`, one has `ell != r_j`. Reduction modulo `r_j` is therefore
injective on this order-`ell` image. An active nonidentity contributes none
of the rational-prime support to the gcd; an identity contributes the whole
`R_j`. This excludes a hidden partial-power outcome inside the conditioned
primary test.

The four no-progress factors follow exactly.

1. `c_ell=0`: every coordinate is inactive, so the gcd is `N`; factor `1`.
2. `0<c_ell<nu`: inactive coordinates force nonempty gcd support. Any
   active nonidentity makes the gcd proper. No progress requires all active
   identities; factor `ell^(-c_ell)`.
3. `c_ell=nu` and `e>v_ell(L)`: all identities give `N`, all
   nonidentities give gcd one and strict growth, and a mixture factors. Only
   the first endpoint is no progress; factor `ell^(-nu)`.
4. `c_ell=nu` and `e<=v_ell(L)`: both synchronized endpoints are no
   progress and mixtures factor; factor
   `ell^(-nu)+(1-ell^(-1))^nu`.

Within each cyclic root group, distinct prime-primary coordinates are
independent. Together with CRT independence, this justifies multiplying the
`f_ell(L)`. The two unconditional no-progress routes are disjoint:
`G_0=1`, of probability `B`, and full return followed by all primary
no-progress events, of probability `Gamma product f_ell(L)`. I found no
conditioning or independence leak in (D9).

## 8. The surviving ceiling and bounded-gap claims

Every certified block divides every `r-1`, so its aggregate satisfies

\[
M\mid D_N,
\qquad
L\mid\operatorname{lcm}(2^t,D_N).
\]

This divisibility ceiling is exact and distribution-free. Only its
comparison with `R_*` is overstated, as Section 2 explains.

For `N=pq`, the identity `D_N | q-p` is immediate. In the uniform-unit
`A=N-1` model, each prime field has exactly `d=D_N` roots. Every initial
proper gcd or later primary certificate requires at least one local root,
so the union bound

\[
\Pr(\text{factor or strict }L\text{-growth})
\le \frac d{p-1}+\frac d{q-1}
\]

is valid at every state. A bounded gap makes `d` and `M` bounded, and on
balanced inputs the right side is `2^(-Omega(n))`. The standard
bounded-prime-gap theorem then supplies the claimed infinite family. No
source independence is used for the deterministic ceiling, and no
CRT-uniform conclusion is transferred to independent small integers.

## 9. Scope and provenance

The P160 and P165 scope descriptions match their authenticated statements:
P160's exact-common-order exit can supply one block, while its hard branch
does not provide a factored common annihilator; P165 supplies the uniform
root model but has the bounded-gap rare-return obstruction. P175 supplies
the exact GFHP interface used in Theorem B. This audit checked consistency
with that promoted local interface; it did not repeat the external
literature audit.

F220 remains explicitly conditional on a supplied dyadic factor residue
and on a witness-source progress law. It is not an all-input factoring
algorithm. Those scope limits are stated honestly and are not audit defects.

## Required disposition

Do not advance this frozen version to statement-only reconstruction. A new
version must, at minimum:

1. distinguish the actual GFHP threshold `N^(1/4)/S(n)` from the stronger
   rounded drift target `R_*` in (E3) and (E9); and
2. add `gcd(c,N)=1` or a squarefree-input restriction to the cyclic
   no-splitting claim.

The corrected version should receive a new manifest and a fresh hostile
audit because both changes alter mathematical statements, not only prose.
