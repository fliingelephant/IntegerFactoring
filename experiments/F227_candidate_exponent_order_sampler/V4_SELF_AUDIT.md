# F227 V4 self-audit

## Verdict

**PASS at self-audited V4 status. Do not promote.** V4 retracts V3's
unsupported self-recursive conclusion. It retains only the claims that the
V3 hostile audit passed, plus their explicit oracle-relative cost form.

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, public-web search, or numerical fit was used.

## Predecessor integrity

Before writing V4, I recomputed the SHA-256 hashes of all six V1 files, all
six V2 files, and all six V3 files, including every hostile audit. Every hash
matched its frozen identity. No predecessor file was edited.

## Scope audit

V4 states only:

1. the AP gcd mean;
2. exponential sparsity for QP-diffuse candidates followed by fresh uniform
   bases;
3. inverse-QP progress density for a supplied fixed nonstale base of small
   residual local order, together with an all-input-oracle current-node
   cost;
4. the P161 rough residual dichotomy.

It states no self-recursive factoring recurrence and no numerical-QP
factoring conclusion.

## Probability audit

For fixed `x`, the two local return probabilities are the exact cyclic-group
fractions `gcd(A_x,r-1)/(r-1)`. Outside `x=p`, every declared useful exit
requires at least one local return. The AP mean therefore yields (B1).

In a nonterminal state, `H=Theta(p/L)`, `L=O(p^(1/2))`, and
`tau(r-1)=p^(o(1))`. The fixed adaptive condition `eta H<=Q(n)` gives a
uniform `p^(-1/2+o(1))` bound. The same fixed envelope makes this
`2^(-c_0 n)` for all large inputs and all histories. A conditional union
bound handles the adaptive bank.

## Fixed-base audit

The `p`-returning indices form one residue class modulo
`u_p=o_p/gcd(o_p,L)`. There are at least `floor(H/u_p)` such indices. A
return gives a direct factor, a one-sided factor, or a global return. Exact
factor-first stripping of a global return either finds a valuation mismatch
or certifies the common order `o_p=o_q`. The latter grows `L` unless it
already divides `L`. Therefore only `o_p=o_q|L` is stale.

## Geometric and same-size cost audit

At a large-cell state, progress probability is at least `1/(2Q(n))`.
Trial `j` is reached with probability at most
`(1-1/(2Q(n)))^(j-1)`. Conditioning on reach and using the oracle's uniform
per-input expected bound proves (C8). This does not assume success-cost
independence.

The exact potential is positive at every running state. A strict lcm update
is an integer multiple of ratio at least two, so it reduces the potential by
at least one unless it crosses the threshold. The potential therefore counts
all same-size states, including the final factor-or-crossing state. This
gives (C9).

## Promise-closure audit

`FactorAll` is explicitly external and all-input. Its cost is denoted
`F_all`, not by the cost of the F227 transition. Equation (C9) is not
unrolled. V4 explicitly notes that every child is even and otherwise
arbitrary. It makes no claim that the balanced-semiprime transition handles
such children.

## Remaining gaps

1. No certified inverse-QP source of suitable nonstale bases is known.
2. No correct all-input dispatcher with a proved uniform QP cost is known.
3. A randomized source would still need capped batching or recognizable
   success.

A fresh hostile re-audit and, only after a hostile PASS, a strict
statement-only reconstruction remain required before promotion.
