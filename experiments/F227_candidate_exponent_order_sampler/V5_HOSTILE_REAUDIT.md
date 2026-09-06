# F227 V5 hostile re-audit

## Authentication

I read `V5_MANIFEST.md` before reading any V5 content file. Its observed
SHA-256 identity is

`d7b189cb569858112a32c751c10eb9b7a3855615701a5ea0f9e1e14730f17411`.

I then recomputed the four frozen V5 content identities. All matched the
manifest.

| File | Expected and observed SHA-256 | Result |
|---|---|---:|
| `V5_STATEMENT.md` | `b4f1ad6826f867105cd4cafaaeaa02ea6914a92ff1986be1698f10a136a457c1` | PASS |
| `V5_PROOF.md` | `92c1869539e78b247823d89ff29d2194c63368296b13bd10ca18b6b26810ee6f` | PASS |
| `V5_SELF_AUDIT.md` | `c462efeed83d1ac9e05b152bdbcda938bd9aed5dbeaed05a4906453b2a395ddb` | PASS |
| `V5_PROVENANCE.md` | `eed58eca89d0d6ac97b04d4c6fb18d054b49025d3d1da5d755cae0bf340c081b` | PASS |

I also recomputed all twenty-four V1--V4 identities recorded in the V5
manifest. Every statement, proof, self-audit, provenance, manifest, and
hostile-audit hash matched. I read the preserved V4 hostile failure in full.

## Verdict

**PASS at hostile-re-audit status.** I found no counterexample or missing
premise in the frozen V5 material claims. V5 makes the one repair required by
the V4 audit: (B6) is now an upper bound, in both prose and mathematics. The
proof already established exactly that bound.

This PASS does not promote F227. A fresh strict statement-only reconstruction
is still required. The source gap and the all-input dispatch gap remain open.

## Hostile reconstruction

### The V4 defect is exactly repaired

A textual comparison confirms that the only mathematical change from V4 is

\[
\Pr(\text{at least one useful trial})
\le Q(n)2^{-c_0n}=2^{-\Omega(n)}.
\]

The proof conditions on every reachable no-progress history and bounds the
next useful-trial probability by `2^(-c_0 n)`. Summing over at most `Q(n)`
trial positions proves the displayed inequality. The bank may use fewer
trials, different conditional laws, or dependent histories; none of these
turns the upper bound into an equality. Cross-trial independence is not used.

### AP gcd mean

For each `d|m`, the congruence `c+jL=0 mod d` is either insoluble or one index
class modulo `d/gcd(d,L)`. In `H` consecutive indices its size is at most

\[
\frac{H\gcd(d,L)}d+1\le \frac{HL}d+1.
\]

Multiplication by the largest atom and
`gcd(A,m)=sum_(d|gcd(A,m)) phi(d)` gives (A3). The identities
`sum_(d|m) phi(d)=m` and `phi(d)/d<=1` give exactly the two terms stated.
Setting the largest atom to `1/H` gives (A4). No unmentioned coprimality of
`L` and `m` is needed.

### Fresh-base obstruction and its quantifiers

For a fixed candidate exponent `A`, CRT makes a uniform unit independent and
uniform in the two field groups. Its exact local return probabilities are

\[
\frac{\gcd(A,p-1)}{p-1},\qquad
\frac{\gcd(A,q-1)}{q-1}.
\]

Outside `x=p`, every declared factor or common-order exit requires at least
one local return. The direct atom plus the two endpoint terms from (A3)
produce the constant `3` in (B1). Unit rejection contributes the separately
stated proper-nonunit mass.

The factor cell has length `Theta(p)`. Because it contains `p` in the named
residue class and preterminal `L=O(p^(1/2))`, its population satisfies
`H=Theta(p/L)` with absolute constants for all sufficiently large inputs.
The fixed numerical-QP envelope is `p^(o(1))`, as is the uniform divisor
bound. Therefore `eta H<=Q(n)` and (B1) give

\[
p^{-1/2+o(1)}=2^{-\Omega(n)}.
\]

One fixed envelope permits fixed constants `c_0,n_0` uniform over all inputs,
stages, and reachable histories. Thus (B5) and the repaired (B6) have the
required asymptotic quantifiers. The theorem explicitly excludes heavy
atoms, candidate/base coupling, integer-biased bases, and joint processing
of nonreturns.

### Fixed-base residual-order law

The candidate `p` proves solubility of `o_p|(x_j-1)`. After division by
`gcd(o_p,L)`, the AP step is invertible modulo

\[
u_p=o_p/\gcd(o_p,L).
\]

The returning indices are therefore exactly one class modulo `u_p`, giving
at least `floor(H/u_p)` representatives. If `u_p<=Q(n)` and `H>=2Q(n)`, the
claimed `1/(2Q(n))` lower bound follows. If the cell is smaller, exhaustive
direct gcd testing uses fewer than `2Q(n)` tests.

For a candidate returning in both fields, prime-copy stripping has three
exhaustive outcomes. A proper intermediate gcd factors. A removable prime
copy is unnecessary in both local orders. A retained copy is necessary in
both local orders. If no factor occurs, the final exponent is consequently
`o_p=o_q`. It certifies a common order and strictly grows `L` unless that
common order already divides `L`. Hence the only order-channel no-progress
case is exactly `o_p=o_q|L`. The direct candidate can still factor in that
case; V5 uses nonstaleness only as a sufficient condition for all local
returns to be useful.

### Conditional cost and the oracle boundary

At a fixed state, every fresh uniform candidate has useful probability at
least `1/(2Q(n))`. Trial `j` is reached based only on earlier trials, so its
reach probability is at most `(1-1/(2Q(n)))^(j-1)`. Conditional on reach and
the complete public history, the explicit oracle premise bounds the new
child call by `F_all(n/2+C_0)`. Summing reached-trial costs proves (C8)
without assuming that the current trial's runtime and success are
independent.

Every strict lcm update is an integer multiple at least twice as large. The
potential `ceil(log_2(J_N/L))` is positive at every running state and drops
by at least one if the update remains nonterminal. It also counts the final
factor-or-threshold-crossing state when its value is one. This proves the
state count and every multiplicity in (C9).

The child `A_x` is an arbitrary even integer. V5 consistently charges its
factorization to a separately supplied all-input `FactorAll`. It neither
substitutes the balanced-node bound for `F_all`, nor unrolls (C9), nor states
an all-input numerical-QP recurrence. The V3 promise-closure defect is not
present.

### Rough residual corollary

Every prime divisor of `u_p` is a prime divisor of `o_p`. Under the stated
rough-branch hypothesis, `u_p` is therefore one or greater than `T(n)`. As
`T(n)>Q(n)`, a residual at most `Q(n)` must equal one. Then `o_p|L`, and the
two congruences `x=p mod L` and `o_p|p-1` make every factor-cell exponent
return modulo `p`. The corollary does not manufacture either the required
nonstale base or the child factorer.

## Exact surviving limitations

1. V5 does not supply suitable nonstale fixed bases with inverse-QP
   probability at every state.
2. V5 does not construct or bound the external all-input factorer.
3. A randomized base source would still need a capped or otherwise
   recognizable-success schedule.
4. The fresh-base negative result applies only to its explicitly declared
   diffuse, conditionally uniform channel.

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, web search, or numerical fit was used. Hashing,
textual comparison, and proof reconstruction were the only machine-assisted
operations. I changed no frozen input and no durable ledger. I wrote only
this hostile re-audit.
