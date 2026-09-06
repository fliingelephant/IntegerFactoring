# F176 V3 candidate self-audit

## Central claim

F176 V3 gives a factor, an exact common-order state above the input length,
or one normalized base-two block that defeats arbitrary pre-registered
numerical QP absolute and quotient caps.

## V3 change audit

V2 used \(\Lambda_n\). V3 replaces it with \(\Lambda_B\), where
\(B\ge n\) is any fixed numerical QP cap.

The only new case is

\[
n<m\le B.
\]

It is correctly Outcome B because the theorem requires common order above
\(n\), not above \(B\). The Mersenne/sign argument is used only for
\(m\le n\). On the gcd-one branch, the same lcm characterization now gives
the stronger local certificate \(\sigma(\operatorname{ord}(2))>B\).

## Prime-power and order audit

- Factor-first stripping detects mixed CRT returns and partial returns
  modulo a repeated prime power.
- On a no-factor branch, it forces exact equality of every prime-primary
  valuation of every local order.
- A final nontrivial \(\gcd(m,N)\) is a proper factor.
- The direct order proof for \(-2\) works for all odd prime powers and does
  not invoke a squarefree-only theorem.
- The squaring kernel modulo every odd prime power is exactly
  \(\{1,-1\}\).

## QP audit

The numerical scan through \(B\), the bit length \(O(B\log B)\) of
\(\Lambda_B\), the scan through \(C\), and trial division through
\(\sqrt C\) are all QP in \(n\). No displayed exponent has super-QP bit
length.

The full recursion tree has fewer than \(2n\) nodes. This handles branching
and repeated factors.

## Preserved history

V1 and its audit remain byte-for-byte under the V1 filenames. V2, its
passing hostile re-audit, and its passing statement-only reconstruction
remain byte-for-byte under the V2 filenames. Neither old review chain is
used as proof of V3.

## Scope risks retained

1. The hard base-two branch is not factored.
2. The theorem quantifies over each fixed QP choice of \(B,C\); it does not
   choose a cap whose QP exponent grows with the input.
3. Capacity is not an exact order.
4. No cross-order, torus-transfer, or full-subgroup closure theorem is
   assumed.
5. The theorem is not an all-input QP factoring algorithm.
