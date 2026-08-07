# F64 fixed-orientation uniformity: hostile re-audit

**Status: PASS**

**Audited file SHA-256:**
`b7a56e611d4f679237a9923204daa188b820f01bf869712a6636d91cc9065bc2`

This audit used only the corrected candidate. It did not use the earlier audit
as evidence. No mathematical or research computation was run.

## Refutation attempts

### 1. Fixed signed products

Theorem 1 is correct in its stated scope. For any nonzero
`epsilon` in `{-1,0,1}^m`, condition on all coordinates except one with
exponent `+1` or `-1`. Multiplication by the conditioned unit and either the
identity or inversion are bijections of the unit group. This proves exact
uniformity. It does not require the group to be cyclic.

I found no counterexample while retaining all three hypotheses: independent
uniform base units, a fixed signed pattern, and a nonzero net exponent vector.
Dropping any of these hypotheses can invalidate uniformity, but the result does
not claim otherwise.

### 2. Reuse across a fixed menu

Reuse does not refute the menu bound. Equal, inverse, or otherwise correlated
menu outputs can be highly dependent, but every nonzero fixed pattern still has
the uniform marginal law from Theorem 1. The union bound uses only those
marginal probabilities. It does not use independence between menu entries.

A zero pattern is also harmless for the stated success events: it outputs the
global root `1`, so neither a proper direct screen nor a useful non-global
involution results.

This does not justify adaptive reuse after an output has been observed. The
candidate correctly excludes that case unless a conditionally uniform unseen
pivot remains.

### 3. Exact direct-screen count

Under CRT, the relevant sample space has `(p-1)(q-1)` pairs. The union of the
two local sign strips has

`2(q-1) + 2(p-1) - 4`

pairs. The subtraction by four removes the double count of the four pairs in
`{+1,-1} x {+1,-1}`. Of the resulting union, `(1,1)` and `(-1,-1)` make only a
global gcd and must be removed. The useful count is therefore

`2p + 2q - 10`.

The only non-global square roots of one are `(1,-1)` and `(-1,1)`, so their
count is two. Both displayed exact probabilities are correct, including for
the smallest permitted odd-prime cases.

### 4. Menu asymptotics are upper bounds

The candidate states

`Pr(any direct-screen success) <= T(2p+2q-10)/((p-1)(q-1))`.

On a balanced semiprime family, the right-hand side is
`T N^(-1/2+o(1))`. This is an asymptotic description of the union-bound right
side, not an assertion that the actual success probability is asymptotically
equal to it. Repeated or equivalent entries can make the union probability much
smaller, and the candidate says so explicitly. The analogous useful-involution
statement is also correctly presented as the upper bound `O(T/N)`.

For `T = poly(log N)`, these bounds are exponentially small in the input bit
length. The balanced-family restriction is necessary and is stated.

### 5. Adaptive trials

The adaptive extension is valid under its exact condition. At trial `t`, fix
the complete prior history. If the rule chooses the signed pattern and unit
multiplier before seeing a pivot that is uniform conditional on that history,
and the pivot has net exponent `+1` or `-1`, the conditional candidate law is
uniform. Thus each reached trial has the same conditional direct-screen bound.
Summing over at most `T` reached trials gives the stated union bound. Adaptive
stopping and prior failures do not change this argument.

An unseen pivot that is only marginally uniform would not suffice if it were
correlated with the history. The candidate avoids that overclaim in its exact
scope by requiring a *conditionally uniform* unseen pivot and by requiring the
choice before observation.

### 6. Escape conditions

The conclusion no longer says that integer-presentation dependence is the only
escape. It explicitly leaves open observed-residue dependence, correlated base
states, nonuniform base states, and other data-dependent operations. A rule can
indeed bias an output after observing a residue without inspecting any integer
presentation. The named F62 integer-presentation mechanism is therefore one
out-of-scope mechanism, not a claimed exhaustive one.

The apparent contrast between permitted reuse and excluded block reuse is also
consistent: a fixed menu may reuse independent-uniform base units across its
entries, while source-side reuse that creates correlated base states or
observation-dependent choices falls outside the model.

## Required repair

None.

For maximal standalone formality, the phrase "pattern and multiplier selected
from any prior history" could say "pattern and **unit** multiplier." The proof
already treats the conditioned multiplier as a unit, and all stated products
live in the unit group, so this is not a mathematical defect in context.
