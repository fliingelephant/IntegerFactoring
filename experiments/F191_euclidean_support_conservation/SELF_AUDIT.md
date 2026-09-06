# F191 self-audit

## Verdict

The exact congruence law, canonical counterexample, and permutation-bank
count are internally consistent. This is a proof-only candidate for a narrow
normalization obstruction. It is not a factoring lower bound and not a
closure of the P164 wide-action branch.

No mathematical computation was run. The candidate still requires a fresh
hostile audit and, if that passes, a statement-only blind reconstruction.

## Attacks checked

1. **Division convention.** The support law does not require Euclidean size
   bounds or a canonical quotient. It holds for every integer identity
   \(X=QD+R\). Ordinary and centered division are special cases.

2. **Nonunit divisor.** The equivalence fails when \(\ell\mid D\), but then
   \(D\) itself is already an \(\ell\)-supported public auxiliary. The
   statement separates this branch explicitly.

3. **Negative centered remainder.** Prime support is read from \(|R|\).
   Divisibility by \(\ell\) is unchanged by sign.

4. **Zero remainder.** A zero is not a valid P163 recursive child. In the
   bank theorem, every selected parameter outside the exceptional union has
   \(R_i\ne0\). If \(R_i=0\), support conservation would put that parameter
   inside the exceptional set.

5. **Canonical counterexample.** The balanced residue \(c\) is nonzero
   because \(\ell\nmid N\). Its magnitude is less than \(N/4\), so the
   nearest quotient of \(N+c\) by \(N\) is exactly one. Both one and
   \(|c|\) are below \(N/2\) and miss \(\ell\), while \(N+c\) is exactly
   divisible by \(\ell\).

6. **Representation independence.** The first theorem concerns the final
   division identity only. It is valid even if \(X\) has exponential
   numerical size but a short circuit. It does not claim that such an
   \(X\) can be evaluated or divided in QP time.

7. **Nearest-integer ties.** In the bank theorem, \(N\) and \(\ell\) are
   odd. The equality \(\ell b/N=t+1/2\) would make an even integer equal an
   odd integer after cross multiplication. Thus no tie convention changes
   the count.

8. **Exceptional endpoint count.** Since the nearest quotient lies between
   zero and \(\ell\), it is divisible by \(\ell\) only at those two
   endpoints. Each endpoint interval has length \(N/(2\ell)\) and contains
   at most that length plus one integer. The total bound
   \(N/\ell+2\) is valid without an asymptotic error term.

9. **Permutation use.** A permutation preserves the exceptional-set
   cardinality. No independence among the \(B\) selectors is assumed; the
   proof uses only a union bound. The theorem does not extend to arbitrary
   nonpermutation maps, which may concentrate on endpoint intervals.

10. **Bank constants.** The inequalities \(\ell\ge4B\) and \(N\ge8B\)
    bound the union by \(N/4+N/4=N/2\). Thus at least one of the \(N\)
    parameters is outside it. Strict inequalities are available in the
    P161 application because surviving \(\ell>T>4B\).

11. **Valid smaller children.** Outside the union,
    \(1\le Q_i\le\ell-1<N/2\) and
    \(0<|R_i|<N/2\). Hence the obstruction is not caused by an oversized or
    zero output.

12. **Local-order size.** P161 gives local orders coprime to the hidden
    rational prime. Reduction modulo that prime is therefore injective on
    the generated subgroup, so each order divides \(p-1\). On an odd
    composite, every such \(p<N/2\). Thus every surviving order prime
    satisfies the bank theorem's \(\ell<N/2\) premise.

13. **QP quantifier.** The theorem is finite and exact for every \(B\).
    QP enters only when choosing the P161 roughness cap \(T>4B\). A fixed
    multiple of a fixed numerical-QP bound remains numerical QP.

14. **One-child recursion.** F191 does not object to a single child losing
    only one bit. It shows that a centered child can omit the target prime
    entirely. The obstruction is support coverage, not recursion depth.

15. **Surviving route.** A special formula might force the quotient or carry
    to be divisible by \(\ell\). Such a theorem would evade F191 and would
    directly supply the support auxiliary required by P163. No such formula
    is assumed or refuted here.
