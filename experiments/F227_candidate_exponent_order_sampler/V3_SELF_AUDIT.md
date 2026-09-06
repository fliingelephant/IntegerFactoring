# F227 V3 self-audit

## Verdict

**PASS at self-audited V3 status. Do not promote.** V3 repairs only the
recursive-cost defect in the V2 hostile re-audit. The validated probability
and local-order statements are unchanged.

No computation, remote run, public-web search, or numerical fit was used.

## Version integrity

1. V1 and its hostile FAIL are unchanged.
2. V2 and its hostile re-audit FAIL are unchanged.
3. V3 uses new `V3_*` files.
4. The V3 repair is confined to the conditional cost statement, its proof,
   and the version metadata needed to expose the repair.

## Exact work partition

V3 defines four disjoint cost classes.

1. `F(n/2+C_0)` is one complete recursive factorization of the candidate
   exponent `A_x`. It occurs at most once per candidate trial.
2. `P_tr(n)` is the nonrecursive public work of one candidate trial. It
   excludes the recursive factorization.
3. `P_st(n)` is the one-time work of one same-size state. It includes
   production and verification of that state's supplied base.
4. `G(n)` is the final congruence terminal and output verification.

All three public bounds are at most the same fixed `Q(n)`. Nothing in
`P_st` is multiplied by the trial count, and nothing in `P_tr` is charged
only once per state.

## One-state audit

For a supplied nonstale base with `u_p<=Q(n)`:

1. If `H>=2Q(n)`, the per-trial progress probability is at least
   `1/(2Q(n))`.
2. Fresh uniform candidate draws give a geometric trial count of mean at
   most `2Q(n)` and almost-sure finite stopping.
3. Conditional on reaching any trial, the expected recursive plus public
   trial cost is at most `F(n/2+C_0)+P_tr(n)`.
4. Summing the geometric reach tail gives
   \[
   2Q(n)(F(n/2+C_0)+P_{\rm tr}(n))+P_{\rm st}(n).
   \]
5. This argument does not assume that success and runtime are independent.
6. If `H<2Q(n)`, direct enumeration uses no recursive candidate
   factorization and fits the same upper bound.

## Same-size-state audit

Define the exact integer terminal `J_N` and potential

\[
\Phi_N(L)=
\max\{0,\lceil\log_2(J_N/L)\rceil\}.
\]

1. A strict lcm update is a strict integer multiple, so it at least doubles
   `L`.
2. Such an update lowers `Phi_N` by at least one while nonterminal.
3. A factor or threshold crossing sets the potential to zero.
4. The number of same-size progress states is at most
   `Phi_N(L_0)<=ceil(log_2 J_N)=O(n)`.
5. The conditional base premise is imposed again at every later same-size
   state. It is not silently inherited from the first base.
6. Multiplying the one-state bound by this deterministic state count gives
   exactly (C9).

## Corrected recurrence audit

With `P_tr,P_st,G<=Q` and `R_N(L_0)=O(n)`, (C9) gives

\[
F(n)
\le C_2nQ(n)F(n/2+C_0)+C_2nQ(n)^2.
\]

The recursive coefficient counts `O(n)Q(n)` candidate exponent
factorizations. The additive term counts `O(n)Q(n)` trials at public cost
`Q(n)`, plus lower-order state and terminal work. There is no missing
same-size continuation and no double counting.

At the halved size sequence, the logarithm of each branching or additive
envelope is `O((log(m+1))^K)`. Summing over `O(log n)` levels is
`O((log(n+1))^(K+1))`. Unrolling therefore gives a fixed numerical-QP
bound. Geometric stage termination, finitely many same-size states, and
finite recursive depth also give almost-sure termination of the conditional
routine.

## Regression checks

1. The fixed input-length and adaptive-envelope repair from V2 remains.
2. The AP gcd mean is unchanged.
3. The exact local-return union bound and unit rejection mass are unchanged.
4. The uniform adaptive obstruction remains `2^(-Omega(n))` with fixed
   constants.
5. Returning fixed-base indices remain one class modulo `u_p`.
6. Only equal local orders already dividing `L` are stale.
7. P161 roughness still gives residual order one or above the roughness cap.

## Scope

V3 remains conditional on a missing source that supplies a nonstale base of
residual order at most `Q(n)` at every same-size state and recursive node.
It treats the declared balanced-semiprime channel. It does not prove such a
source, cover joint nonreturn processing, or give the complete all-input
factoring algorithm.

A fresh hostile re-audit and then a statement-only reconstruction remain
required before promotion.
