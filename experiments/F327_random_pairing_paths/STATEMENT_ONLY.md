# F327 statement for fresh independent reconstruction

## Combinatorial setup

Let F be an explicitly evaluable involution on V={0,...,d-1}, where d is odd. Let q be its number of fixed vertices. Choose j uniformly in V. Let A fix j and be a uniform perfect matching of V without j. Starting at j, evaluate F; stop on an F-fixed current vertex, and otherwise follow A and repeat. Let H count F evaluations, including the terminal one.

The matching is generated lazily: remove a uniform current rank from an unused pool; if its F partner is distinct, remove that partner, pair it under A with a fresh uniform rank from the pool, remove that rank and continue. The pool uses sparse forward/inverse Fisher–Yates maps with identity defaults and a decreasing active prefix. Balanced search trees implement the maps. Uniform positions use fair-bit rejection from the next power of two.

Claims:

1. The lazy procedure has the stated uniform-matching law and uses O(T) words through T evaluations, without sampling-rejection slowdown from pool depletion. Word size is O(log d). Including fair bits and balanced-tree costs, overhead per evaluation is polynomial in log d.
2. Put m=(d-q)/2. For 0<=k<=m, the stopping hazard after k failures is q/(d-2k). For 1<=T<=m+1,
   S_T=Pr(H>T)=product_{k=0}^{T-1}(d-q-2k)/(d-2k).
   Set S_0=1 and S_T=0 for T>m+1. Then Pr(H<=T)=1-S_T and E min(H,T)=sum_{k=0}^{T-1}S_k.
3. E H=(d+2)/(q+2). Conditional on H<=T, the endpoint is uniform among the q fixed ranks.
4. For fixed d,q, expected capped evaluations divided by Pr(H<=T) is nonincreasing in T. Adding any fixed nonnegative per-attempt setup cost preserves this monotonicity. This does not assert monotonicity after mixing different input-dependent d,q.

## Arithmetic application

Take F to be the ranked involution defined in F326/STATEMENT.md, for a fixed odd N with s>=2 distinct prime divisors and a fixed unit square a modulo N. The F326 rank/select/involution/decoder results and P02 are declared dependencies. Conditional on a, the outer hidden root r is uniform among the 2^s roots of a and is independent of all matching coins. Only N,a are passed to the inner procedure.

Claims:

5. F has exactly 2^s-1 unit fixed ranks: 2^(s-1)-1 in the first inverse branch, all yielding proper divisors through the specified decoder, and 2^(s-1) in the scaled inverse branch, yielding square roots. Nonunit fixed ranks yield proper divisors. Consequently the exact capped factor probability, averaged over the independent matching and conditional hidden-root coins, is (1-1/q)(1-S_T).
6. Let a public history-independent gcd screen inspect both endpoints of an F edge. Include every fixed rank in an absorbing set B and include both vertices of each nonfixed F pair on which the screen yields a verified proper divisor. Write b=|B|. Stop when an absorbing current rank is selected. Then claims 2–3 hold with b in place of q and with absorption in place of fixed-point output. The outer factor probability is at least (1-1/b)(1-S_T). Equality holds if the screen does not preempt any root-producing fixed rank under the stated decoder priority.

No statement is made about structured auxiliary matchings, cross-edge/history-dependent gcd screens, or compressed arithmetic jumps. The arithmetic claims require no algorithmic computation of q or b and no full graph enumeration.
