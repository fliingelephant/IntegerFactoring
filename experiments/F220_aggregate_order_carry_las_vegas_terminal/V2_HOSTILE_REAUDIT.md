# F220 V2 hostile reaudit

## Verdict

**PASS, with the exact scope readings stated below.** V2 repairs both
mathematical failures in the frozen V1 packet. I found no remaining defect in
the primary certificate, generalized CRT, selected-prime GFHP invocation,
exact-target drift argument, four-case CRT-uniform law, repeated-prime-power
handling, common-predecessor ceiling, bounded-gap bound, or corrected cyclic
source model.

The result remains a conditional balanced-semiprime terminal. It assumes a
certified dyadic factor residue and a witness process with the stated
history-by-history progress law. It neither supplies those premises nor
proves an all-input factoring algorithm.

Two implementation readings must remain explicit.

1. The fixed function `S(n)` is the public threshold schedule. An
   implementation must be able to evaluate or compare against its target.
   As usual for an algorithmic schedule, it cannot be a noncomputable
   numerical-QP-valued function.
2. “Every stage has numerical-QP bit cost” means one uniform bound for all
   histories. It includes witness generation, the encoded factored
   annihilator, every primary test, and retained state. A pointwise family
   of unrelated bounds would not justify multiplying by the expected stage
   count.

These are the standard readings of the frozen algorithmic statement, not
new mathematical premises. Under them, the cost conclusion is valid.

There is one nonmathematical typo in `V2_PROOF.md`: proof display (35) writes
`)mid` where `\mid` was intended. The corresponding statement (E2), the
surrounding prose, and every later use have the correct divisibility sign.

## 1. Authentication and audit method

The five expected V2 hashes were supplied before I opened any V2 file. I
recomputed them first, and all matched exactly.

| Artifact | Expected and observed SHA-256 | Result |
|---|---|---|
| `V2_STATEMENT.md` | `935ef9a28dff6bfade891ca069eb5d544236977c4c8c20c6d4208ff582b5fe45` | match |
| `V2_PROOF.md` | `99ae21becd47b17a288af31670ba5a6df96529164a93c2b39e5704ef520af99d` | match |
| `V2_SELF_AUDIT.md` | `4151c2d72201d7c026c432e4543433c98494a56e89979e37b5a0096893bace05` | match |
| `V2_PROVENANCE.md` | `91b425bbb7d06f09ebfd83f5accde57bf305fbd173e4f4b33d8475bbc69e6f1d` | match |
| `V2_MANIFEST.md` | `1874c16d58f8cfc1828b85975ecd2e96ede67792f05d0455d3b92f7504157635` | match |

I also rechecked every V1 identity preserved in the V2 manifest. The V1
statement, proof, self-audit, provenance, manifest, and hostile FAIL all
match their declared hashes. The four cited local source identities also
match: `PROMPT.md`, P160's statement, P165's statement, and P175's
statement.

I read the complete V2 packet and the preserved V1 hostile FAIL. I checked
the authenticated P175 statement and its promoted hostile-audit interface
where the general GFHP modulus mattered. I used no mathematical script,
finite search, random sampling, remote run, web search, or numerical fit.
Hashing and textual comparison were the only machine operations. I did not
edit a frozen input or a durable ledger. I wrote only this reaudit.

## 2. Theorem A: primary certification passes

Fix a rational prime `r | N` and write

\[
o_r=\operatorname{ord}_r(a).
\]

The global identity gives `o_r | A`. For
`ell^e || A`, the condition

\[
\gcd(a^{A/\ell}-1,N)=1
\]

makes `a^(A/ell)` nonidentity modulo every rational prime divisor `r`.
Thus `o_r` does not divide `A/ell`. All primary valuations of `o_r` are
bounded by those of `A`, so the only possible obstruction to division by
`A/ell` is

\[
v_\ell(o_r)=e.
\]

Lagrange gives

\[
\ell^e\mid o_r\mid r-1.
\]

This proof is directly in the residue field. It does not use equality of
complete local orders, reduction from a prime-power unit group, or
`gcd(A,N)=1`. In particular, if `ell=r`, the gcd-one branch is simply
impossible, as the conclusion requires.

A gcd strictly between one and `N` is a verified factor. A gcd equal to
`N` contributes no block. The certified primary powers are pairwise
coprime, so their product divides every `r-1`. An lcm of several such
products retains the same universal predecessor property. The quantifiers
in Theorem A are sound for arbitrary odd `N`, including repeated prime
powers.

## 3. Theorem B: generalized CRT and the GFHP interface pass

Let

\[
g=\gcd(2^t,M).
\]

The hidden true factor `p` satisfies both public congruences. Hence
`b=1 mod g`, which is exactly generalized-CRT compatibility. Substitution
`x=b+2^t z` gives

\[
\frac{2^t}{g}z=\frac{1-b}{g}\pmod{M/g}.
\]

The coefficient is a unit modulo `M/g`, and the solution modulus is

\[
2^t(M/g)=\operatorname{lcm}(2^t,M)=L.
\]

This correctly handles every overlap with the dyadic modulus. It never
uses the product modulus when powers of two overlap.

The proof that `L` is a unit modulo `N` is exact. If a rational prime
`rho` divided both `M` and `N`, universality would imply
`M | rho-1`, while `rho | M`; this is impossible. Oddness handles the
dyadic part.

For canonical `s=p mod L`, unitness makes `s` nonzero. If `p<L`, then
`s=p` and the preliminary gcd returns the factor. Equality `L=p` is
excluded by `gcd(L,N)=1`. On the remaining branch,

\[
1\le s<L<p<N,
\qquad
\gcd(L,N)=1,
\qquad
p=s\pmod L.
\]

These are the hypotheses of Gao--Feng--Hu--Pan Theorem 3.1 with `r=1`.
The imported theorem accepts an arbitrary unit modulus `m`; it is not
restricted to a power of two. It locates a selected prime in one residue
class, so F220 does not need the stronger Corollary 3.2 hypothesis that all
prime divisors occupy the same class. With `m=L`, its deterministic cost is

\[
O\!\left(
\left\lceil\frac{N^{1/4}}L\right\rceil
\log^{7+3\epsilon}N
\right).
\]

Thus `L >= N^(1/4)/S(n)` makes the cost numerical QP. Since `L` is an
integer, this chosen sufficient target is exactly

\[
J_{\rm G}=\left\lceil\frac{N^{1/4}}{S(n)}\right\rceil.
\]

Finally, `M | p-1 < N` and `t<=n` give `O(n)`-bit CRT operands. The lcm
growth formula (B8) is the exact valuation identity and counts growth of
`L`, not merely growth of `M`.

## 4. V1 threshold defect is repaired

V2 separates

\[
T_{\rm G}=N^{1/4}/S(n),
\qquad
J_{\rm G}=\lceil T_{\rm G}\rceil,
\qquad
R_*=2^{\lceil\log_2J_{\rm G}\rceil}.
\]

Only `J_G` is the stopping target. The dyadic value satisfies

\[
J_{\rm G}\le R_*<2J_{\rm G}
\]

and is used only as an upper envelope. The universal obstruction (E3) and
the cyclic-source obstruction (E12) both compare their ceilings with
`J_G`. V2 explicitly refuses to infer a terminal obstruction from a ceiling
in `[J_G,R_*)`.

The V1 hostile certificate therefore no longer attacks V2. For
`N=67*73`, `S=2`, and `t=1`, the old ceiling is six, the exact integer
target is five, and the envelope is eight. It lies in the explicitly
non-obstructive interval

\[
J_{\rm G}\le C_N(t)<R_*.
\]

No V2 premise labels this case obstructed.

## 5. Theorem C: exact-target drift passes

For a nonterminal state,

\[
\Phi(L)=
\left\lceil\log_2\frac{J_{\rm G}}L\right\rceil
\]

is a positive integer. It is zero after applying the outer maximum exactly
when `L>=J_G`. If `L'` is a strict lcm update, divisibility gives
`L'/L>=2`. While the update remains below the target,

\[
\left\lceil\log_2\frac{J_{\rm G}}{L'}\right\rceil
\le
\left\lceil\log_2\frac{J_{\rm G}}L-1\right\rceil
=\Phi(L)-1.
\]

If it crosses the target, the new potential is zero and the old potential
was at least one. A verified factor has the same decrement property. Thus
every useful event decreases the potential by at least one, including a
non-dyadic step that crosses `J_G`.

Before stopping,

\[
1\le\Phi(L)\le\lceil\log_2J_{\rm G}\rceil=O(n).
\]

The `J_G=1` case has no nonterminal state. For the stopped time `tau`, the
conditional drift hypothesis telescopes to

\[
Q(n)^{-1}\mathbb E[m\wedge\tau]\le\Phi_0.
\]

Monotone convergence gives

\[
\mathbb E\tau\le\Phi_0Q(n)=O(nQ(n)),
\]

so `tau` is finite almost surely. A uniform numerical-QP stage bound and
the deterministic terminal cost then give numerical-QP expected total bit
complexity.

Let `E_k` be factor return or `c` not dividing the current `L`. Outside
`E_k`, the state and potential do not change. On `E_k`, the decrement is
between one and `O(n)`. Therefore

\[
\Pr(E_k\mid\mathcal F_k)\ge1/Q(n)
\]

implies the same drift lower bound, while drift `1/Q(n)` implies useful
mass at least `1/(O(n)Q(n))`. This proves both directions of the claimed
numerical-QP-scale equivalence. It uses no stage independence.

For iid witnesses, a no-progress outcome leaves `L` fixed and a fresh draw
has the same law. The waiting time until the next useful outcome is
therefore geometric. Independence is used only in this final iid
restatement.

## 6. Theorem D: initial root probabilities pass

For `R_j=r_j^f_j`, the odd-prime-power unit group is cyclic of order

\[
h_j=r_j^{f_j-1}(r_j-1).
\]

The explicit premise `gcd(A,N)=1` removes the `r_j`-part and gives

\[
d_j=\gcd(A,h_j)=\gcd(A,r_j-1).
\]

The full local `A`-root subgroup has `d_j` elements among `h_j` units.
Thus full return modulo every prime power has probability

\[
\Gamma=\prod_j\frac{d_j}{h_j}.
\]

In contrast, `G_0=1` means nonreturn already after reduction modulo every
rational prime. Exactly `d_j` of the `r_j-1` field units are roots, so

\[
B=\prod_j\left(1-\frac{d_j}{r_j-1}\right).
\]

This explains and validates the different denominators. Every outcome
strictly between `1` and `N`, including a partial repeated-prime power, is a
proper factor. Conditioning on `G_0=N` independently restricts each CRT
coordinate to a uniform element of its cyclic root subgroup `C_{d_j}`.

## 7. Theorem D: every primary case and the product law pass

Fix `ell^e || A`. In local root group `C_{d_j}`:

- if `v_ell(d_j)<e`, then `d_j | A/ell`, so
  `a_j^(A/ell)=1` deterministically;
- if `v_ell(d_j)=e`, exponentiation by `A/ell` maps the uniform
  `ell`-Sylow coordinate uniformly onto a group of order `ell`, so the
  identity probability is exactly `1/ell`.

Because `ell | A` and `gcd(A,N)=1`, one has `ell != r_j`. The reduction
kernel is an `r_j`-group, so an active nonidentity of order `ell` remains
nonidentity modulo `r_j`. A conditioned primary gcd therefore contains the
whole component `R_j` when the local value is the identity and no
`r_j`-support otherwise. There is no hidden partial-power outcome.

Let `c_ell` be the number of active components. The four factors in (D8)
follow.

1. If `c_ell=0`, every component is the identity and the gcd is `N`.
   No-progress factor: `1`.
2. If `0<c_ell<nu`, inactive components force nonempty gcd support.
   Any active nonidentity makes the gcd proper. Avoiding a factor requires
   all active identities. No-progress factor: `ell^(-c_ell)`.
3. If `c_ell=nu` and `e>v_ell(L)`, all identities give gcd `N`, all
   nonidentities give gcd one and a new certificate, and a mixture gives a
   proper factor. Only the all-identity endpoint is no progress. Factor:
   `ell^(-nu)`.
4. If `c_ell=nu` and `e<=v_ell(L)`, the gcd-one certificate is already
   contained in `L`. Both synchronized endpoints are no progress, while
   mixtures factor. Factor:
   `ell^(-nu)+(1-ell^(-1))^nu`.

Within each local cyclic root group, distinct Sylow coordinates of a
uniform element are independent. CRT coordinates are also independent.
Thus the conditional joint no-progress probability is exactly the product
of the `f_ell(L)`, not a union bound.

Unconditionally there are exactly two disjoint no-progress routes:

1. `G_0=1`, of probability `B`, after which the processor returns no
   block; or
2. `G_0=N`, of probability `Gamma`, followed by no progress in every
   primary coordinate.

Hence

\[
P_{\rm np}(L)
=B+\Gamma\prod_{\ell\mid A}f_\ell(L)
\]

is exact for arbitrary odd prime-power decompositions under
`gcd(A,N)=1`. No conditioning or independence assumption is transferred
to independent small integer witnesses.

## 8. Universal capacity and bounded gaps pass

Every certified block divides every rational-prime predecessor. Therefore

\[
M\mid D_N:=\gcd_{r\mid N}(r-1),
\qquad
L\mid C_N(t):=\operatorname{lcm}(2^t,D_N).
\]

This ceiling is distribution-free and survives adaptive witness choices.
If `C_N(t)<J_G`, no Theorem-A aggregate update can reach the fixed target;
a proper gcd can still terminate.

For `N=pq`,

\[
D_N=\gcd(p-1,q-1)\mid q-p.
\]

In the CRT-uniform `A=N-1` model, either local prime field has exactly
`d=D_N` roots. Every initial factor route or later primary-certificate route
requires at least one local root. The union bound therefore gives, at every
state,

\[
\Pr(\text{factor or strict }L\text{-growth})
\le\frac d{p-1}+\frac d{q-1}.
\]

Already-covered certificates only reduce the useful event. On a fixed
bounded-gap family, `d` and `M` are bounded, while balance gives
`p=2^(n/2+O(1))`. The right side is `2^(-Omega(n))`. The standard
bounded-prime-gap theorem supplies infinitely many such prime pairs, and
all sufficiently large pairs satisfy `q<2p`. The probability estimate is
specific to CRT-uniform units; the deterministic capacity bound is not.

## 9. V1 prime-power injection defect is repaired

V2 assumes the synchronized common order `c` is completely factored and

\[
\gcd(c,N)=1.
\]

For each `R_j=r_j^f_j`, the kernel of reduction from local units to
`F_(r_j)^*` is an `r_j`-group. The cyclic subgroup generated by `g_j` has
order `c`, prime to `r_j`, so its intersection with the kernel is trivial.
Reduction is injective on the whole synchronized direction.

For every exponent `u` used in stripping,

\[
g_j^{zu}=1\pmod{R_j}
\quad\Longleftrightarrow\quad
c\mid zu,
\]

independently of `j`. If the condition holds, the gcd contains every full
component and is `N`. If it fails, injection makes every component
nonidentity already modulo its rational prime, and the gcd is one. Thus no
stripping gcd is a proper factor or a partial repeated-prime power.

The V1 certificate `N=63,c=3` is now outside the theorem because
`gcd(c,N)=3`. It does not refute V2.

Every synchronized witness has exact local order

\[
m_z=\frac c{\gcd(c,z)},
\]

so all returned orders and primary blocks divide `c`. For
`ell^e || c`, the full `ell^e` part occurs exactly when `ell` does not
divide `z`. With independent uniform exponents modulo `c`, absence after
`k` witnesses means that every exponent is divisible by `ell`, an event of
exact probability

\[
\ell^{-k}.
\]

No independence between different primes `ell` is claimed or needed.
Every reachable modulus divides `lcm(2^t,c)`, so comparison with `J_G`
proves the corrected cyclic-source capacity statement.

## 10. Complexity and exact boundary

The universal predecessor property keeps `M<N` and the retained aggregate
at `O(n)` bits. Generalized CRT, gcd, lcm, and candidate verification are
polynomial in those bit lengths. Modular exponentiation is polynomial in
the encoded exponent length. The theorem explicitly charges the factored
annihilator encoding, its number of distinct prime tests, witness
generation, and retained state to the uniform per-stage numerical-QP bound.
The expected-stage proof therefore does not hide an exponential-size
annihilator or transcript.

P160 can supply an admissible block only on its exact-common-order exit; its
hard branch gives neither the required factored annihilator nor a source
law. P165 supplies the uniform-root model, but bounded-gap inputs defeat an
all-input inverse-QP progress lower bound for that source. Neither theorem
evaluates the dyadic carry.

Accordingly, V2 proves the advertised conditional terminal and exact source
kernel. It does not handle arbitrary-composite terminals, unbalanced
factors, carry evaluation, construction of an adaptive source, or complete
factorization recursion. Those omissions are stated scope boundaries, not
hidden proof steps.

## Disposition

F220 V2 is ready for the required strict statement-only reconstruction. It
must not be promoted before that independent reconstruction passes and all
frozen V2 hashes are checked again.
