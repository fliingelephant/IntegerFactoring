# F227 V3 hostile re-audit

## Authentication

I authenticated the five frozen V3 inputs before reading their contents.

| File | Expected SHA-256 | Observed SHA-256 | Result |
|---|---|---|---:|
| `V3_STATEMENT.md` | `2030573691879933e7819d6d34278dfa1b4d0aa3d2378ae3dd29845c6da5ec29` | `2030573691879933e7819d6d34278dfa1b4d0aa3d2378ae3dd29845c6da5ec29` | PASS |
| `V3_PROOF.md` | `758296a586c1b6e24eab1e25a455e12947f91ff1d099d6421995caf8497247e3` | `758296a586c1b6e24eab1e25a455e12947f91ff1d099d6421995caf8497247e3` | PASS |
| `V3_SELF_AUDIT.md` | `c31e8a7b85d74c10935a7a7db0cc4c3323dff5defb0aba076805aecf9a696d76` | `c31e8a7b85d74c10935a7a7db0cc4c3323dff5defb0aba076805aecf9a696d76` | PASS |
| `V3_PROVENANCE.md` | `97ce5e4224c48ee844fd30c5ad2961f77bf5ba26be218e550ac505737c092ad5` | `97ce5e4224c48ee844fd30c5ad2961f77bf5ba26be218e550ac505737c092ad5` | PASS |
| `V3_MANIFEST.md` | `8a9daa113a30ba730f428393ab9fc3f6fddf9cd002d77f9e25395035abb5eb35` | `8a9daa113a30ba730f428393ab9fc3f6fddf9cd002d77f9e25395035abb5eb35` | PASS |

I then read both preserved hostile failures in full. I also authenticated all
six V1 files and all six V2 files against the identities in the V3 manifest.
Every predecessor hash matched.

## Verdict

**FAIL.** V3 correctly repairs the particular V2 accounting defect. Its
same-size potential, geometric waiting-time calculation, and multiplicities
for public work are sound under the stated supplied-base premise. The AP
mean, fresh-uniform-base obstruction, fixed-base progression, stale
classification, and P161 rough-order dichotomy also survive fresh review.

The claimed complete recursive cost in (C9)--(C11) does not survive. F227
proves its current-node transition only for a distinct odd balanced
semiprime. Every recursively factored candidate exponent is

\[
A_x=x-1,
\]

which is even and otherwise unrestricted. V3 supplies no correct all-input
dispatch for these children and no recurrence for such a dispatch. Thus the
half-size inequality is a valid local bound relative to an external child
factorer, but it is not a closed recurrence for that factorer's complete
cost. The numerical-QP conclusion does not follow.

This is a promise-closure defect. It is separate from both preserved
failures: V3 fixes V1's missing uniform envelope and V2's omitted same-size
and public-work factors.

## Promotion blocker: the recursive children leave the theorem's domain

The setup proves a transition for

\[
N=pq,\qquad p<q<2p,
\]

with distinct odd primes and a certified factor-cell state. A trial then asks
for a **complete** factorization of `A_x`. The size fact

\[
\operatorname{bits}(A_x)\le n/2+C_0
\]

is correct, but size contraction is not recursive correctness.

The domain is not hereditary:

1. Since `L` is even and `x` is odd, every `A_x` is even. It is therefore
   never itself a distinct odd balanced semiprime.
2. Removing the public factor two does not repair closure. The odd part of
   `(x-1)/2` can be prime, a prime power, an unbalanced semiprime, or a product
   of many primes. F227 imposes no condition on it.
3. The imported F220 terminal is also a balanced-semiprime terminal. P161 is
   a rough-order postprocessor and explicitly is not an all-input factorer.
   Neither import supplies the missing dispatch.

The definition of `F` has no reading that closes the proof:

- If `F(m)` ranges only over eligible F227 balanced-semiprime states, then
  `F(n/2+C_0)` does not bound the cost of factoring `A_x`.
- If `F(m)` is the worst-case cost on all integers of at most `m` bits, then
  Sections 5--8 bound only the balanced-semiprime current node. They do not
  prove the same recurrence for the other inputs that can determine this
  all-input worst case.

The justified local statement has the form

\[
\begin{aligned}
\mathbb E[\operatorname{cost}(N,L_0)]
\le R_N(L_0)\bigl[&2Q(n)F_{\rm all}(n/2+C_0)\\
&+2Q(n)P_{\rm tr}(n)+P_{\rm st}(n)\bigr]+G(n),
\end{aligned}
\]

where `F_all` is an external complete-factorization cost. Nothing in V3
bounds `F_all` by the left side. Replacing the instance cost by `F(n)` in
(C9), then recursively unrolling it, silently assumes exactly this missing
closure.

The manifest's statement that V3 does not handle arbitrary composites is
consistent with the local result, but inconsistent with using (C9) as a
complete self-recursive cost theorem. A fixed numerical-QP envelope can
absorb known QP factors. It cannot absorb an unproved child algorithm or its
runtime.

A repair must do one of the following:

1. state only the oracle-relative current-node bound and remove (C10)--(C11);
   or
2. separately assume a correct all-input recursive dispatch and prove that
   every reachable input has the declared fixed-ratio call count and public
   cost bounds.

Supplying a nonstale base at every “recursive node” is not that assumption.
It neither defines the non-balanced branches nor proves that they satisfy the
F227 setup.

## Attacks on the V3 recurrence repair

### Same-size stages: PASS

Put

\[
J_N=\left\lceil N^{1/4}/S(n)\right\rceil.
\]

For integer `L`, the state is nonterminal exactly when `L<J_N`. Therefore
`Phi_N(L)>=1` at every state that actually runs a candidate loop. A useful
nonfactor update has `L|L'` and `L'>L`, hence `L'>=2L`. Consequently

\[
\Phi_N(L')\le\Phi_N(L)-1
\]

when the new state remains nonterminal. A threshold crossing or a factor
ends the node. This counts the final factor-or-crossing state: when the
potential is one, one last state is allowed. Thus

\[
R_N(L_0)=\Phi_N(L_0)\le \lceil\log_2J_N\rceil=O(n)
\]

is correct. There is no remaining V2-style same-size omission or off-by-one
error.

### Geometric reach tail without success-cost independence: PASS

At one fixed state and fixed base, the successful candidates form a fixed
subset of `C`. Independent uniform candidate draws therefore have conditional
success probability at least

\[
\delta=1/(2Q(n))
\]

at every reached trial. Hence

\[
\Pr(\text{trial }j\text{ is reached})
\le(1-\delta)^{j-1}.
\]

The cost of trial `j` may be correlated with whether that same trial
succeeds. That does not affect the calculation: the event that trial `j` is
reached depends only on earlier trials. A uniform per-input conditional cost
bound for the fresh child call gives

\[
\sum_{j\ge1}\Pr(j\text{ reached})
\left(F_{\rm all}(n/2+C_0)+P_{\rm tr}(n)\right)
\le
2Q(n)\left(F_{\rm all}(n/2+C_0)+P_{\rm tr}(n)\right).
\]

Thus the correlation defense is valid. It does not repair the missing
all-input bound on `F_all`.

### Recursive calls per trial: local PASS, global FAIL

One candidate needs at most one invocation that returns the complete
factorization of `A_x`; its internal factor tree is part of that invocation.
The bit-size bound is also correct. V3 therefore charges the local call once
per trial.

The failure is not a missing multiplicity. It is the unsupported
self-application of the balanced-semiprime recurrence to that arbitrary
child invocation.

### Public-work charging: PASS under the stated strong premise

The V3 partition has the right multiplicities:

- `P_tr` is multiplied by the expected trial count at each state;
- `P_st` is charged once per same-size state;
- the whole state bound is multiplied by `R_N(L_0)`; and
- `G` is charged once after the current node ends.

The small-cell enumeration branch is safely overbounded by the same formula.
With `P_tr,P_st,G<=Q`, the local algebra gives

\[
O(nQ(n))F_{\rm all}(n/2+C_0)+O(nQ(n)^2).
\]

This repairs V2's public-work error. It does not turn `F_all` into the F227
current-node cost.

The cost theorem uses the stronger premise that a qualifying base is supplied
at every state with its full acquisition cost already included in `P_st`.
The final “inverse-QP probability” source criterion would still need an
explicit capped batching or recognizable-success argument before it can be
substituted for that premise. Such an outer QP factor could be absorbed by a
new fixed envelope, but that conversion is not the recursion proof given in
V3.

### QP unrolling: algebraic PASS, applicability FAIL

If one independently grants the recurrence

\[
F(n)\le C_2nQ(n)F(n/2+C_0)+C_2nQ(n)^2
\]

for every reachable input, its solution is numerical QP. There are
`O(log n)` size levels, and the sum of the logarithms of the branching
envelopes is

\[
O((\log(n+1))^{K+1}).
\]

The fixed constants in (Q1)--(Q2) are adequate, and the additive `C_0`
causes no issue after a fixed base range. The defect is the derivation of the
recurrence, not its algebraic solution.

## Regression checks on the unchanged claims

### Factor cell and divisor average: PASS

Balance gives

\[
\sqrt{N/2}<p<\sqrt N<q<2p.
\]

Thus `p` is the sole direct gcd target in `I_N`. Every `A_x` is positive,
even, below `q` and below `2p`, so `gcd(A_x,N)=1`.

For each `d|m`, a soluble AP congruence occupies one residue class modulo
`d/gcd(d,L)`. Its count is at most

\[
H\gcd(d,L)/d+1\le HL/d+1.
\]

Multiplying by the largest atom and using

\[
\gcd(A,m)=\sum_{d\mid\gcd(A,m)}\varphi(d),
\qquad
\sum_{d\mid m}\varphi(d)=m
\]

proves (A3). Endpoints, insoluble classes, and nonuniform laws are all safely
overcounted.

### Fresh-base probability obstruction: PASS

For fixed `x`, a uniform unit has independent uniform reductions, and

\[
\Pr(a^{A_x}=1\bmod r)=\frac{\gcd(A_x,r-1)}{r-1}.
\]

Apart from `x=p`, every declared useful exit needs a return in at least one
field. The direct atom and the two AP applications give the exact constant
three in (B1). Exact unit rejection adds

\[
\frac{p+q-2}{N-1}=O(1/p),
\]

which is smaller than the preterminal scale.

In a nonterminal state, `H=Theta(p/L)` uniformly. The standard uniform bound
`tau(m)=m^{o(1)}`, the fixed condition `eta H<=Q(n)`, and
`L=O(p^{1/2})` give

\[
\Pr(\text{useful}\mid\text{history})
\le p^{-1/2+o(1)}=2^{-\Omega(n)}.
\]

The fixed envelope makes the exponent uniform. A conditional union bound
over at most `Q(n)` histories proves (B6); cross-trial independence is not
needed for this negative assertion.

### Fixed-base progression and stale classification: PASS

The index of `p` solves `o_p|(x_j-1)`. Dividing by `gcd(o_p,L)` makes the
step invertible modulo `u_p`, so the returning indices are exactly one class
modulo `u_p` and number at least `floor(H/u_p)`.

For a returning candidate, a missing `q`-return gives a proper factor.
Global return plus complete factor-first stripping either splits unequal
local-order valuations or leaves the exact equality `o_p=o_q`. In the equal
case the certified common order grows `L` unless it already divides `L`.
Thus the only no-progress order case is exactly

\[
o_p=o_q\quad\text{and}\quad o_p\mid L.
\]

This proves (C3), including its endpoint floor term. The direct-enumeration
branch for `H<2Q(n)` is also valid.

### P161 rough residual dichotomy: PASS

On P161's named rough-descendant branch, reduction from the hidden prime
power to its prime field preserves the local order because that order is
coprime to the hidden rational prime. Hence every prime divisor of `o_p`
exceeds the chosen cap `T(n)`.

Every prime divisor of

\[
u_p=o_p/\gcd(o_p,L)
\]

is then greater than `T(n)`. Therefore `u_p` is either one or greater than
`T(n)`. Under `u_p<=Q(n)<T(n)`, only `u_p=1` remains, equivalently
`o_p|L`. Since `x` is congruent to `p` modulo `L`, every factor-cell exponent
then returns modulo `p`. The factor-or-growth conclusion follows unless the
base is stale.

The claim is correctly restricted to P161's rough descendant. P161 does not
supply the missing nonstale base and does not supply the missing all-input
recursive factorer.

## Final assessment

V3 closes the exact V2 defect: it counts every later same-size state and
charges public trial work at the trial multiplicity. Its probability and
local-order boundary remains valid. Promotion is nevertheless blocked.
Equations (C9)--(C11) turn an oracle-relative balanced-node estimate into a
self-recursive complete-factorization bound without an all-input dispatch.
The packet must either add that separate premise or retract the complete QP
recurrence claim.
