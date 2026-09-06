# F195 self-audit

## Verdict

PASS conditional on the two explicitly named published algorithmic premises.
The elementary deductions and beta-two control-flow claims are exact. No
all-input QP factoring theorem is claimed.

## Checks

1. Reduction from \(p^a\) to \(p\) is injective on the common-order group
   only because \(\gcd(M,N)=1\). A raw order with hidden-prime primary support
   is outside Theorem 1.
2. The Gao--Feng--Hu--Pan call uses \(s=1,m=M\), and every rational prime
   divisor of \(N\) satisfies the needed congruence.
3. The new terminal does not move the asymptotic QP order threshold compared
   with \(\sqrt N/M^2\); it improves search cost and scope.
4. Harvey--Hittmeir's initial return is \(2\) when \(2^D<N\). Otherwise the
   first order search returns \(2\) on the P159 high-order branch. The
   smooth-number phase is therefore unreachable there.
5. The user's one-child recurrence correction is retained. The obstruction
   is exponential same-node work, not failure of \(n\mapsto n-1\) recursion.
6. The rank-three lower list scale follows from the published legal bound
   \(m<N^{1/4}/2\). It is a boundary for that direct interface, not a lower
   bound on other rank-three or lattice methods.
7. The low-order prime screen proves full equality of local orders primary
   part by primary part. It handles repeated hidden prime powers.
8. The smooth-number fork is stated on balanced inputs. It does not claim a
   large lower bound when a hidden prime has subexponential bit length.
9. The mixed high-order branch is explicitly left open.
10. The carry paragraph states lack of an input to the named papers, not a
    general carry lower bound.

## Required literature audit

A hostile reviewer must inspect the primary versions cited in STATEMENT.md,
not a secondary summary, and verify theorem hypotheses, parameter ranges,
line numbers, and bit-complexity conventions.
