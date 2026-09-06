# F219 self-audit

## Verdict

The proof-only candidate passes self-audit within its stated scope. It proves
a stronger certificate interface and two exact randomized boundaries. It
does not provide a biased integer carry sampler or a factoring algorithm.

## Certificate checks

1. The test uses `A/ell`, not `A/ell^e`. Failure of this exponent to return
   in every component forces the full valuation `e` in every local order.
2. The gcd-one conclusion is componentwise because every hidden prime power
   would otherwise divide the gcd.
3. Reduction to the rational prime preserves the certified primary part
   only under `gcd(ell,N)=1`. This premise is explicit.
4. Contributions from different bases and annihilators can be lcm-combined
   because each separately divides every `r-1`. No public element of the
   combined order is asserted.
5. The universal factor two is valid only for odd inputs, which is the
   declared branch.

## CRT and Las Vegas checks

1. Generalized CRT uses `lcm(M,2^s)`, not the product. This accounts for
   shared powers of two.
2. A residue class modulo `L_s` has exactly `L_t/L_s` refinements modulo
   `L_t`; no independence heuristic is used.
3. Wrong guesses are harmless only because every returned divisor is
   verified. The deterministic terminal is run for a fixed bounded cost on
   every class.
4. Sampling with replacement reaches the true refinement almost surely and
   its true-hit waiting time has exact mean `L_t/L_s`. The accepted-factor
   waiting time is only bounded above by this quantity, because a wrong
   refinement may also return a verified factor.
5. The ceiling in the terminal cost contributes one unit per trial. Choosing
   `L_t=Theta(N^(1/4))` keeps it within the same expected bound.
6. Uniform guessing is not called impossible. Only the route guaranteed by
   hitting the true refinement has the same expected exponent as the
   already known modulus. No lower bound is asserted against off-class
   factor events.

## Top-multiplier checks

1. Balance gives `p <= B < q < 2p`, so the base-`p` representation of `B`
   has exactly the two digits used by Lucas.
2. The Lucas calculation retains all higher digits of `r q-1` implicitly;
   the higher digits of `B` are zero and contribute binomial factors one.
3. The signed parity is `(-1)^(p+s)=-(-1)^s` because `p` is odd.
4. The CRT target `1-rq` is one modulo `q`, so the two local congruences are
   compatible.
5. Division by `r` occurs only for odd `r`.
6. The binomial computation uses precision `T >= log2(rN)`, so its upper
   index lies in the cited routine's main range. The statement does not
   incorrectly run it with `T=t` when `rN >= 2^t`.
7. A nonuniform predictor succeeds with the exact atom mass it assigns to
   the true integer carry. No unproved carry distribution is assumed.

## Probability and obstruction checks

1. The exact probability samples uniformly from the unit group. Raw residue
   sampling would add a separate gcd screen and is not claimed by the
   formula.
2. Conditional `A`-torsion coordinates are independent and uniform by CRT.
3. In a cyclic group of order `ell^e`, exactly the fraction `1-1/ell` has
   full `ell`-adic order.
4. For `A=N-1`, both torsion sizes equal `gcd(p-1,q-1)` by direct modular
   reduction.
5. The bounded-gap conclusion imports only P165's already promoted infinite
   family. It does not claim a new prime-distribution theorem.
6. The capacity obstruction concerns ordinary multiplicative primary
   certificates. Torus, higher-dimensional, nonabelian, and integer carry
   observables remain outside it.

## Computation provenance

F219-D01 was frozen before execution and completed under its exact command.
Its output is finite guidance only. F219-D02 failed at import time because
`sympy` was unavailable. No result from D02 is used, and no substitute run
was made.
