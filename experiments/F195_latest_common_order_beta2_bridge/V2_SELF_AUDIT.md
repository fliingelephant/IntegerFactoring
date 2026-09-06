# F195 V2 self-audit

## Verdict

PASS conditional on the complete published-premise list in V2_STATEMENT.
No all-input QP factoring theorem is claimed.

## Repair of V1

V1 failed hostile audit. V2 makes these exact repairs:

1. replaces the false requirement \(T\ge k\) by
   \(P(k)\le T\), then uses Bertrand to obtain \(T>k/2\);
2. calls Gao--Feng--Hu--Pan Corollary 3.2 directly in the all-low branch,
   instead of invoking a theorem that also required an unconstructed witness;
3. scopes the beta-two control flow to odd \(N\ge N_0\) and includes the
   line-3 return;
4. lists Algorithm 4.3, Proposition 4.5, and the smooth-number lemma among
   the published premises;
5. uses the current primary-paper title and corrects the typesetting of
   \(\varphi(m)\).

## Checks

1. Common-order reduction uses \(\gcd(M,N)=1\); repeated prime powers are
   allowed in Theorem 1.
2. The new terminal improves same-node cost and scope but not the QP
   threshold class.
3. The P159 beta-two branch exits before the smooth stage for every odd
   sufficiently large input, whether line 3 fires or the first loop fires.
4. A one-child \(n\mapsto n-1\) recurrence is QP. It does not absorb
   exponential work done at the parent.
5. The rank-three \(N^{1/8}\) floor and \(N^{1/5}\) balance use the published
   parameter range.
6. The roughness interface includes smoothness of \(m\) and the exact
   largest-prime condition for all \(i\le k\).
7. The low/high fork is restricted to balanced distinct semiprimes.
8. Its all-low branch establishes the congruence premise directly and does
   not need to construct a common-order element.
9. The mixed high-order branch remains open.
10. The carry statement is an interface observation, not a lower bound.
