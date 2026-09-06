# F227 V4 hostile re-audit

## Authentication

I authenticated the frozen V4 manifest before reading the packet. The
task-supplied external SHA-256 identity and the observed identity were both

`8ba0c42fc0f9d836063eaebd3c16188da5441eefbdbc87599e9fd61391e2d559`.

I then authenticated all four V4 content files against that manifest before
reading them.

| File | Expected and observed SHA-256 | Result |
|---|---|---:|
| `V4_STATEMENT.md` | `5a7b0aa093af31417ff6db68a77bd5938d6675a7f583a7c4940c9b8e9a9ab1ff` | PASS |
| `V4_PROOF.md` | `02086d1f796594594fe378f045478cfc7b230aef052fdb38338e361fdecd7f23` | PASS |
| `V4_SELF_AUDIT.md` | `1d7be7c40f9bedc3d1c90838acffec822e357ce9233c37ffb0a956a60210989d` | PASS |
| `V4_PROVENANCE.md` | `c16a796a2aa275cd366d47b126361ef968faf0526cb02be4f22726ec9f7d00ce` | PASS |

I also recomputed all eighteen V1, V2, and V3 identities listed in the V4
manifest. Every statement, proof, self-audit, provenance, manifest, and
hostile-audit hash matched. I read all three preserved hostile failures in
full. For the imported interfaces, I checked the promoted P197/F220 V2
primary-certificate and generalized-CRT terminal statements and the
promoted P161/F181 rough-descendant statement. Their frozen source hashes
match their manifests and promoted-ledger identities.

## Verdict

**FAIL, for one narrow formal defect in (B6).** The substantive AP,
fresh-base, fixed-base, cost, and roughness arguments survive hostile
review. V4 also correctly retracts V3's unsupported all-input recurrence.
However, the frozen statement no longer puts an upper-bound relation in
(B6). It asserts an equality that is false for the class of adaptive banks
that it defines.

This is a statement regression, not a failure of the union-bound proof. The
intended inequality follows from (B5), but a hostile audit cannot insert the
missing words into a frozen theorem.

## Promotion blocker: (B6) states equality instead of an upper bound

The V4 statement says that every qualifying bank “has total useful
probability”

\[
Q(n)2^{-c_0n}=2^{-\Omega(n)}.
\tag{B6}
\]

There is no “at most” in the prose and no inequality in the display. Read as
written, this assigns the same exact useful probability to every
`Q`-diffuse bank. That is false. The definition permits a bank to make at
most `Q(n)` trials, so a zero-trial bank is already a counterexample: its
useful probability is zero, while `Q(n)2^{-c_0n}` is positive. More
generally, a conditional union bound cannot turn different trial laws and
different trial counts into one exact probability.

The proof establishes only

\[
\Pr(\text{at least one useful trial})
\le Q(n)2^{-c_0n}=2^{-\Omega(n)}.
\]

Restoring “at most,” or putting the displayed inequality into (B6), is the
complete repair. No change to the proof or to the exponent is needed.

## Hostile checks that survived

### Factor cell and AP endpoints

Balance gives

\[
\sqrt{N/2}<p<\sqrt N<q<2p.
\]

Thus `p` is in the cell and is its only integer with a nontrivial gcd with
`N`. Every candidate is odd, while `0<A_x=x-1<sqrt(N)<q,2p`; parity excludes
the only possible positive multiple `p`. Hence `gcd(A_x,N)=1`.

For `d|m`, a soluble congruence `c+jL=0 mod d` is one index class modulo
`d/gcd(d,L)`. Its count in any `H` consecutive indices is at most

\[
\frac{H\gcd(d,L)}d+1\le\frac{HL}d+1.
\]

Multiplication by the largest atom and the identity

\[
\gcd(A,m)=\sum_{d\mid\gcd(A,m)}\varphi(d)
\]

give (A3), including insoluble classes and both endpoint errors. Setting
`eta=1/H` gives (A4). No coprimality assumption between `L` and `m` is
missing.

### Fresh uniform bases

For fixed `x`, CRT makes the reductions of a uniform unit independent and
uniform. The exact local return probability is

\[
\frac{\gcd(A_x,r-1)}{r-1}\qquad(r=p,q).
\]

Outside the direct candidate `x=p`, every useful exit in the declared
channel needs at least one local return. The direct atom and the two AP
means give exactly the three additive atom terms in (B1).

If `W=|I_N|`, then `W=Theta(p)`. In the nonterminal range,
`L=O(p^(1/2))`, so the residue class containing `p` has
`H=Theta(p/L)` with absolute constants, uniformly for all sufficiently
large inputs. Since `eta H<=Q(n)`, `Q(n)=p^{o(1)}`, and the uniform divisor
bound is `tau(m)=m^{o(1)}`, (B1) gives

\[
\Pr(\text{useful}\mid\text{history})
\le p^{-1/2+o(1)}=2^{-\Omega(n)}.
\]

One fixed envelope supplies fixed `c_0,n_0` over all inputs, stages, and
reachable histories. Exact unit rejection contributes only `O(1/p)`.
After the missing inequality is restored, conditional union bounding over
at most `Q(n)` trials proves the intended (B6). No cross-trial independence
is needed for that upper bound.

### Fixed-base progression and exact stale branch

The index of `p` solves `o_p|(x_j-1)`. Dividing by
`gcd(o_p,L)` makes the AP step invertible modulo

\[
u_p=\frac{o_p}{\gcd(o_p,L)}.
\]

The returning indices are therefore exactly one class modulo `u_p`, and
there are at least `floor(H/u_p)` of them. This proves the floor term and
its endpoint-safe lower bound in (C3).

A `p`-return with no `q`-return factors. On a global return, repeated
prime-copy stripping preserves a common annihilator. A proper intermediate
gcd factors; otherwise every retained primary valuation is necessary in
both fields, so the final exponent is exactly `o_p=o_q`. The promoted
P197/F220 certificate makes it a common primary block. It grows `L` unless
the common order already divides `L`. Thus the only order-channel
no-progress case is exactly

\[
o_p=o_q\mid L.
\]

The direct candidate `x=p` can still factor in that stale case; V4 uses
nonstaleness only as a sufficient condition for every `p`-return to be
useful. If `u_p<=Q(n)` and `H>=2Q(n)`, the success probability is at least
`1/(2Q(n))`. If the cell is smaller, direct enumeration finds `p` in fewer
than `2Q(n)` gcds.

### Geometric cost without success-cost independence

At one fixed state, fresh uniform candidate draws see a fixed useful subset
of density at least `1/(2Q(n))`. The event that trial `j` is reached depends
only on earlier trials, so

\[
\Pr(R_j)\le\left(1-\frac1{2Q(n)}\right)^{j-1}.
\]

Conditional on reach and on the complete public history, the external
oracle premise bounds the fresh child call by
`F_all(n/2+C_0)`. Thus summing reached-trial costs proves (C8) even if the
current trial's success and cost are correlated. One oracle call and one
copy of `P_tr` are charged per reached trial; `P_st` is charged once per
same-size state.

### Exact same-size potential

For integer `L`, the real nonterminal condition is exactly `L<J_N`, where
`J_N=ceil(N^(1/4)/S(n))`. Hence the potential is positive at every running
state. A strict lcm update is an integer multiple with ratio at least two.
It lowers the potential by at least one if the new state remains
nonterminal. A factor or a threshold crossing ends the node. The potential
therefore counts the last factor-or-crossing state, including the case in
which its value is one. Equations (C6) and (C9) have no V2-style off-by-one
or missing same-size multiplier.

### P161 roughness transfer

On the named P161 rough-descendant branch, every prime divisor of `o_p`
exceeds `T(n)`. Every prime divisor of `u_p` is still a prime divisor of
`o_p`. Therefore `u_p` is one or exceeds `T(n)`. Since `T(n)>Q(n)`, the
condition `u_p<=Q(n)` forces `u_p=1`, equivalently `o_p|L`. The congruences
`x=p mod L` and `o_p|p-1,L` then make every factor-cell exponent return
modulo `p`. The corollary is correctly restricted to the rough-descendant
branch and supplies neither a nonstale base nor a child factorer.

### Oracle boundary and multiplicities

Every child `A_x` is even and otherwise unrestricted. V4 consistently uses
the separately supplied all-input `FactorAll` cost `F_all` for those
children. It never substitutes the balanced-semiprime node cost for that
quantity, never unrolls (C9), and states no numerical-QP all-input factoring
conclusion. The cost bound is only an oracle-relative estimate for the
current balanced node. The V3 promise-closure failure is repaired.

## Qualifications and exact scope

Apart from the false equality in (B6), I found no counterexample to the
frozen material arguments. Any revised packet must retain these scope
conditions:

1. The negative theorem covers only diffuse candidate laws followed by a
   conditionally independent uniform unit and only the declared per-trial
   exits. It does not cover heavy atoms, candidate/base coupling,
   integer-biased bases, or joint processing of nonreturns.
2. The positive cost bound assumes that every reached same-size state is
   supplied a verified nonstale base with `u_p<=Q(n)` and that its full
   acquisition cost is within `P_st(n)`. V4 does not construct this source.
3. `FactorAll` is an external correct all-input Las Vegas factorer with the
   stated uniform conditional expected-cost bound. V4 neither constructs
   it nor bounds `F_all` by a numerical-QP function.
4. Corollary D applies only on P161's named rough-descendant branch.
5. No all-input recursion or complete factoring theorem follows from V4.

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, web search, or numerical fit was used. Hashing and
textual inspection were the only machine operations. I changed no frozen
input and no durable ledger. I wrote only this hostile re-audit.
