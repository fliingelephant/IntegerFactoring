# F227 V2 self-audit

## Verdict

**PASS at self-audited V2 status. Do not promote.** V2 repairs the exact
formal defect in the V1 hostile audit. The mathematical AP estimate and
fixed-base classification are unchanged.

## Version integrity

1. The five V1 candidate files were not edited.
2. `HOSTILE_AUDIT.md` remains the frozen V1 FAIL.
3. V2 uses new `V2_*` files.
4. No computation, remote run, public-web search, or numerical fit was used.

## Repaired definitions and quantifiers

1. V2 defines `n=ceil(log_2(N+1))` before any use of `n`.
2. It defines numerical QP with fixed constants independent of inputs,
   hidden factors, histories, and stages.
3. It fixes one function
   `Q(n)=2^(C_*(log_2(n+1))^(k_*))` once and for all.
4. The same `Q` bounds `eta H` after every reachable history and bounds the
   total number of adaptive trials.
5. Every base is fresh, conditionally independent, and uniform only after
   the candidate and its preprocessing are fixed.
6. The constants `C_*` and `k_*` cannot change from one history to another.
7. The per-stage exponential constant `c_0` consequently depends only on
   this fixed envelope, not on an input or history.
8. The conditional union bound uses at most the same `Q(n)` stages.

## Mathematical regression checks

1. `p` is the unique nonunit in the factor cell.
2. Even `L` makes every `A_x=x-1` even and coprime to `N`.
3. The AP congruence count is at most `HL/d+1`, including endpoints and
   insoluble cases.
4. The divisor identity gives the exact max-atom estimate (A3).
5. A declared F220-style factor or primary-support exit requires a local
   return in at least one field, apart from the direct candidate `x=p`.
6. The three max-atom contributions are exactly the direct event and the
   two additive terms from the AP gcd means.
7. In the preterminal range, `H=Theta(p/L)` with absolute constants and
   `L=O(sqrt(p))`.
8. The divisor bound is uniform, while the fixed envelope is `p^(o(1))`.
   Their product is uniformly `2^(-Omega(n))`.
9. Exact rejection sampling of a uniform unit adds proper-factor mass
   `(p+q-2)/(N-1)=O(1/p)`, which is smaller than the main upper bound.
10. The fixed-base return indices form one residue class modulo
   `u_p=o_p/gcd(o_p,L)`.
11. Unequal local orders split during stripping. Equal orders outside `L`
    grow the aggregate. Only equal orders already dividing `L` are stale.
12. P161 roughness gives `u_p=1` or `u_p>T(n)`; it does not give an
    intermediate QP residual order.

## Cost and scope checks

1. The negative theorem grants every factorization of `x-1` for free.
2. The positive recursion is explicitly conditional on receiving a
   nonstale base with residual order at most `Q(n)` at every node.
3. Each recursive child has at most `n/2+O(1)` bits.
4. The logarithm of the product of QP branching factors over `O(log n)`
   halvings is `O((log n)^(k_*+1))`, hence numerical QP.
5. V2 covers distinct odd balanced semiprimes and the declared per-trial
   channel only. It does not cover arbitrary composites, joint processing
   of nonreturns, heavy candidate atoms, or candidate/base coupling.
6. V2 is not an all-input factoring algorithm because it does not produce
   the required nonstale base.

Fresh hostile re-audit and then a statement-only reconstruction remain
required before promotion.
