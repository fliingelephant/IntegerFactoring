# F230 hostile audit

## Verdict

**PASS.** I found no false theorem within the frozen candidate's stated
distinct-balanced-semiprime and conditional-recursion scope. The zero-defect
repair is exact. The odd projection, local-return laws, redundant-power
stripping, favorable-bank dichotomy, constants, and conditional drift all
reconstruct from first principles.

Three scope qualifications must remain attached to the result:

1. Equations (17)--(19) are upper laws for a uniform **unit** odd
   projection, or equivalently conditional on the base gcd screen not
   factoring. If the public implementation samples `x` uniformly from
   `1,...,N-1`, an unconditional upper bound must add its direct nonunit
   atom. That atom is exponentially small here, so the stated sparse-source
   conclusion survives.
2. "Arbitrary prime powers" in Theorem B means arbitrary primary powers in
   the odd integers `P`, `Q`, `D`, `s_p`, and `s_q`. The frozen theorem does
   not claim formulas for inputs containing repeated factors such as
   `p^e q^f`.
3. The factorer in Theorem C is conditional on a correct all-input
   dispatcher for the arbitrary half-size integer `H`. F230 proves the size
   and incremental cost of that call, not the missing dispatcher or a
   top-level factoring algorithm.

These are boundaries already recoverable from the frozen definitions and
status paragraph; they are not promotion blockers. In particular, the
first point must not be dropped when (19) is cited outside its conditional
unit-source context.

I used no numerical experiment, web search, or unlisted artifact. I edited
no frozen file or durable ledger and wrote only this audit.

## Frozen-input authentication

I hashed `MANIFEST.md` before reading any proof content. Its observed
SHA-256 is

```text
111e954ea921b6424d6fc5664cc740acaa2c346f49e553597e9465accb360285
```

No separate expected digest for the manifest was supplied, so this records
its exact identity rather than asserting an external signature. Every
digest frozen inside it matched before I read the corresponding file:

| Frozen file | Expected and observed SHA-256 |
|---|---|
| `STATEMENT.md` | `96edf9b0eb183364ce9178385e289e8e7c5dc967d32f74912aaff7548ba5999f` |
| `PROOF.md` | `2a07b604ac59d3090ed6cc7e46c8c4aed197665ce79db84068b802031a82d407` |
| `SELF_AUDIT.md` | `902ee4dd3c9a5528c3fcbcc2a2e5860aee1feb51ed0400d7ea77581185c8f8ba` |
| `PROVENANCE.md` | `290cc0b5a0e670bcd05ea0739feedad1a1c79d54080ee4da9611e72a0ec987ec` |

I then read all four frozen files in full. I also read the full F228 hostile
failure and the complete promoted P175, P197, and P198 statements on which
F230 relies.

## 1. Exact zero-defect branch

For odd `1<=u<B`, both `u` and the Euclidean remainder `R_u` lie in
`(0,B)`. The remainder is nonzero because `uN` is odd while `B` is a power
of two. If

\[
E_{u,c}=u-R_u+cB=0,
\]

then `R_u-u=cB`. Its absolute value is less than `B`, so `c=0` and
`R_u=u`. The division identity modulo `B` then gives

\[
uN\equiv R_u=u\pmod B,
\qquad
u(N-1)\equiv0\pmod B.
\]

Odd `u` is invertible modulo the power of two `B`; hence `B|(N-1)`.

Conversely, if `N=BH+1`, then

\[
uN=uHB+u.
\]

The range `0<u<B` makes this the Euclidean division, so `R_u=u`,
`Q_u=uH`, and `E_{u,0}=0`. This proves (1)--(3), including uniqueness of
the zero shift.

For the advertised extension, write a positive odd multiplier as
`u=v+kB`, with `0<v<B`. From `E=0`, reduction modulo `B` again gives
`B|(N-1)`. In that branch `R_u=v`, so

\[
E_{u,c}=(k+c)B.
\]

It vanishes exactly at `c=-k`. Moreover,

\[
BA_{u,c}=uN-R_u+cB=u(N-1)=uBH,
\]

so `A_{u,c}=uH`. No zero integer is used as a recursive child. This is the
exact repair of the first F228 hostile failure.

Finally, `N<2^n` implies

\[
H={N-1\over2^{\lfloor n/2\rfloor}}
<2^{\lceil n/2\rceil}.
\]

Thus `H` has at most `ceil(n/2)` bits. Factoring every public multiplier up
to a numerical-QP **value** `U` by a sieve and merging its factors with the
one factorization of `H` has numerical-QP cost. A QP bound only on
`log U` would not suffice, but that is not the frozen hypothesis.

## 2. Odd common part and cancellation

Set

\[
P=(p-1)_{\rm odd},\quad Q=(q-1)_{\rm odd},\quad D=\gcd(P,Q).
\]

The exact identity

\[
N-1=q(p-1)+(q-1)
\]

gives

\[
\gcd(N-1,p-1)=\gcd(q-1,p-1).
\]

Division of `N-1` by the power of two `B` changes no odd valuation. Taking
odd parts therefore proves

\[
\gcd(H,P)=D.
\]

The symmetric identity gives `gcd(H,Q)=D`. This remains exact when an odd
prime has cancellation-enhanced valuation in `N-1`: the gcd identity caps
its intersection with `P` or `Q` at the corresponding minimum valuation.

For each odd prime `ell`, division by the full gcd subtracts the smaller of
`v_ell(P)` and `v_ell(Q)` from both. At least one residual valuation is
zero. Hence

\[
s_p=P/D,\qquad s_q=Q/D,
\qquad \gcd(s_p,s_q)=1,
\qquad S=s_ps_q.
\]

Neither residual is asserted coprime to `D`; that stronger assertion would
be false and is not used. Since `D|H`, one has `P|s_pH|SH` and similarly
`Q|SH`. The hidden `S` is only an analysis annihilator and is never
enumerated.

## 3. Exact odd projection and local returns

CRT sends a uniform unit modulo `N=pq` to independent uniform units modulo
`p` and `q`. Write

\[
p-1=2^{e_p}P,
\qquad
q-1=2^{e_q}Q.
\]

Because `p-1,q-1<N<2^n`, both `e_p,e_q<n`. In either cyclic local unit
group, raising to `2^n` kills the full two-primary component. It is an
automorphism on every odd primary component because `2^n` is coprime to
the odd group order. The image is therefore uniform in the odd subgroup,
and the two images remain independent. No squarefreeness assumption on the
integers `P` and `Q` occurs here.

For a prime `ell`, put

\[
e=v_\ell(P),\quad h=v_\ell(H),\quad d=v_\ell(D).
\]

The identity `gcd(H,P)=D` says `min(e,h)=d`. If `e>d`, then `h=d`; if
`e=d`, `H` already saturates the local exponent. In both cases,

\[
v_\ell(\gcd(uH,P))
=d+\min(v_\ell(u),e-d).
\]

Thus, including all primary powers,

\[
\gcd(uH,P)=D\gcd(u,s_p).
\]

The analogous identity holds at `q`. A cyclic group of order `P` has
exactly `gcd(uH,P)` solutions to `y^(uH)=1`. Therefore

\[
\alpha_p(u)={\gcd(u,s_p)\over s_p},
\qquad
\alpha_q(u)={\gcd(u,s_q)\over s_q}.
\]

Independence of the CRT coordinates makes the probability of exactly one
local return

\[
\alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p)
=\alpha_p+\alpha_q-2\alpha_p\alpha_q,
\]

and the global-return probability is `alpha_p alpha_q`. Equations (7)--(9)
are exact.

This audit does not enlarge the input scope. For an input with a repeated
factor, the local unit group and the information exposed by a gcd modulo a
prime power require a different statement. F230 assumes distinct primes.

## 4. Redundant-power stripping

Let the current factored exponent `E` annihilate both local coordinates.
For a prime `ell|E`, puncture one copy and compute

\[
g=\gcd(a^{E/\ell}-1,N).
\]

There are exactly three cases for the squarefree semiprime `N`:

- `g=N`: both local orders divide `E/ell`; replacing `E` by `E/ell`
  preserves the annihilator invariant.
- `1<g<N`: exactly one local order divides `E/ell`, so `g` is a factor.
- `g=1`: neither local order divides `E/ell`, although both divide `E`.
  Their `ell`-adic order valuations therefore both equal `v_ell(E)`, which
  certifies that full common primary block.

Repeating the first case strips all redundant copies before either an
unequal local valuation factors or an equal valuation is certified. A
reduction at another prime changes no already proved valuation. Hence the
loop is valid for arbitrary exponent powers and in any prime-processing
order.

The bank must not stop at an earlier global return that produces only a
block already contained in `M`. Step 5 explicitly continues in that case.
An earlier proper gcd or new block is already success, while an earlier
stale return leaves the same base available for later multipliers. Thus an
early return cannot mask the favorable hidden bank entry.

## 5. Favorable bank and the constants

Assume `min(s_p,s_q)<=U` and `(s_p,s_q)!=(1,1)`. Since both residuals are
odd and coprime, the complete odd bank contains a value `w` such that one
residual equals `w` and the other, call it `z`, exceeds one:

- if both residuals exceed one, take one that is at most `U`;
- if one residual is one, take `w=1`.

No hidden choice is performed by the algorithm; it tests every odd
`u<=U`. A nontrivial `gcd(w,N)` would itself be success. After the direct
screen, (7) gives, up to orientation,

\[
\alpha_p(w)=1,
\qquad
\alpha_q(w)={\gcd(w,z)\over z}={1\over z}.
\]

Since odd `z>1` implies `z>=3`, the exact proper-factor probability at that
entry is

\[
1-{1\over z}\ge {2\over3}.
\]

This proves the stronger branch of (12) without knowing which residual is
small.

Now let `s_p=s_q=1`. Then `P=Q=D`, and `D|H`, so the entry `u=1` is a
global return for every projected unit. Because `M|D`, the conjunction

\[
\operatorname{lcm}(2^t,M)<J
\le\operatorname{lcm}(2^t,D)
\]

forces a prime `ell` with

\[
k=v_\ell(M)+1\le v_\ell(D).
\]

This `ell` is odd. It divides the fully factored public `H`, so the
stripping loop processes it without being told which primary is missing.

For a uniform element in a cyclic group whose `ell`-primary order is
`ell^e`, the probability that the element order is divisible by `ell^k`
is exactly

\[
1-\ell^{k-1-e}
=1-\ell^{-(e-k+1)}.
\]

The two coordinates are independent. On the event that both local order
valuations reach `k`, unequal valuations produce a proper gcd at the first
unequal puncture, while equal valuations certify their common value, which
strictly exceeds `v_ell(M)`. Its probability is (13), and

\[
\left(1-\ell^{-(v_\ell(P)-k+1)}\right)
\left(1-\ell^{-(v_\ell(Q)-k+1)}\right)
\ge(1-1/\ell)^2\ge4/9.
\]

Thus both residual cases prove (12). The hidden residual and hidden missing
primary are proof witnesses only. Enumeration of all multipliers and all
prime divisors of their factored exponents removes both selectors.

## 6. Sampling `x`, one multiplier, and one shift

The implementable stage samples `x` uniformly from `1,...,N-1`. Every
nonunit in this range is divisible by exactly one of `p,q`, so its gcd is a
factor. Conditional on the absence of that immediate success, `x` is
exactly uniform in the unit group. If `r` is either lower bound above and
`delta` is the nonunit probability, the unconditional success probability
is at least

\[
\delta+(1-\delta)r\ge r.
\]

The averaging in (15) is also sound. There are
`O_U=ceil(U/2)` odd multipliers in `[1,U]`. At least one fixed member has
conditional success probability at least `4/9`, so a uniform member gives

\[
\Pr(\text{factor or growth})
\ge {4\over9O_U}\ge {4\over9U}.
\]

The algorithm need not name that member.

For every bank multiplier, `u<B`; Theorem A therefore gives exactly one
zero-defect shift, namely `c=0`. An independent uniform choice from `W`
consecutive integers containing zero hits it with exact probability `1/W`.
Multiplication gives (16). This is an exact accounting of the certified
zero-shift contribution, not an assertion that the total success
probability at all shifts equals (16). Other shifts can only contribute
additional successes if they are processed.

## 7. Sparse-source upper law and the nonunit atom

Fix a screened multiplier and a unit odd projection. If neither local
coordinate returns at exponent `uH`, no divisor of `uH` can return locally:
an order dividing a punctured exponent would also divide `uH`. Hence every
factor or common certificate produced by that exponent and its punctures is
contained in the union of the two initial local-return events. Its exact
union probability is

\[
\alpha_p+\alpha_q-\alpha_p\alpha_q,
\]

which proves (17). Since `u<=U`,

\[
\alpha_p\le U/s_p,
\qquad
\alpha_q\le U/s_q.
\]

Dropping the negative intersection proves (18). With a fresh projected unit
at each adaptive test, the statement holds conditionally at every history;
a union bound proves (19). For a fixed bank on one projection, the same
union bound needs no independence between its entries.

There is an important conditioning boundary. In the public sampler of
Theorem C, the exact probability that the preliminary `x` is a nonunit is

\[
\delta={p+q-2\over N-1}.
\]

Indeed, the interval contains `q-1` positive multiples of `p` and `p-1`
positive multiples of `q`, with no overlap. Equations (17)--(19) do not
upper-bound this direct-factor atom; they concern the subsequently formed
uniform unit projection. For `K` fresh public samples, a safe unconditional
bound is

\[
K\left[
\delta+U\left({1\over s_p}+{1\over s_q}\right)
\right].
\]

For one `x` followed by a fixed `K`-multiplier bank, a sharper form is

\[
\delta+(1-\delta)
KU\left({1\over s_p}+{1\over s_q}\right).
\]

Balance gives `p=2^(n/2+O(1))` and therefore
`delta=2^(-n/2+O(1))`. If both residuals are `2^Omega(n)` and `K,U` are
numerical-QP values, either full bound remains `2^-Omega(n)`. Thus the
sparse conclusion survives, but an unconditional citation must include
this atom.

The upper law does not address an adaptive multiplier chosen from results
on the **same** projection unless it is covered by a predetermined bank
union. It also does not address biased projections, carry-correlated
integer witnesses, or a use of the factorization of `H` outside the
declared return-and-puncture decoder. The frozen boundary states these
exclusions.

## 8. Lcm terminal and conditional drift

Every certified block divides both `p-1` and `q-1`; because the projection
has odd order, the accumulated `M` is odd and satisfies `M|D`. Therefore

\[
p\equiv1\pmod M.
\]

This combines with the beta-two residue `p mod 2^t` by CRT because `M` is
odd. The public combined modulus is exactly

\[
L=\operatorname{lcm}(2^t,M).
\]

It is coprime to `N`: `2^t` is coprime to odd `N`, and
`M|D|P<p`, so neither hidden prime divides `M`. The promoted P175/P197
known-residue terminal therefore applies when `L>=J` (with the standard
fixed numerical-QP terminal schedule embodied in `S_0`).

Strict growth of the odd `M` multiplies `L` by an odd integer at least
three. Hence every factor-or-growth event at a preterminal history decreases

\[
\Phi(L)=\max\{0,\lceil\log_2(J/L)\rceil\}
\]

by at least one, taking a returned factor as terminal potential zero. The
conditional probability bound gives conditional expected decrease at least
`4/9`. The P197 telescoping argument yields at most `9n/4` expected stages
under the usual `Phi<=n` terminal schedule, with no interstage independence
assumption. It also gives almost-sure termination.

One stage has numerical-QP bit cost. The bank has numerical-QP cardinality;
`uH` has `n/2+polylog(n)` bits; modular exponentiation is polynomial in
that bit length and in `n`; and the number of stripping punctures is at most
the total number of prime occurrences in the factored exponent. Multiplying
this cost by `O(n)` expected stages remains numerical-QP.

The factorization of `H` is a single prior half-size call. If an all-input
Las Vegas dispatcher with the required bound is granted, its cost at
`ceil(n/2)` bits plus the F230 stage cost remains numerical-QP, exactly as
in the P198 recursion boundary. F230 neither constructs that dispatcher nor
shows that `H` is itself in the favorable state. Arbitrary composites,
prime powers, and the complete recursive factorization problem therefore
remain outside this candidate.

## Final assessment

The F228 witness is genuinely repaired rather than hidden: zero defect
forces the public child `H`, and the odd projection turns its shared odd
support into exact local-return probabilities. The favorable theorem then
removes both hidden selectors by full public enumeration. The complementary
upper law is also correct when kept conditional on a unit projection, with
the explicit exponentially small nonunit term added for the public sampler.

No blocker remains in the frozen mathematical content at its declared
scope. The result is a favorable-state source theorem and source boundary,
not the all-input factoring theorem required by the project prompt.
