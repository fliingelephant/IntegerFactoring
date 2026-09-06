# F179 self-audit

## Verdict

The two-return closure is internally consistent. Independent hostile audit
and statement-only reconstruction are required before promotion.

## Kill-first checks

1. The shift is \(3\), not \(2\). The unit circles centered at \(0\) and
   \(-3\) are disjoint, so the resultant is never zero. A shift of \(2\)
   would have a tangency at \(-1\).
2. The resultant is an integer Bezout combination of the two monic
   polynomials. Hence divisibility after evaluation at \(N\) is exact.
3. The large integers \(N^a-1\) and \((N+3)^b-1\) are never factored. Only
   the small-height resultant is factored.
4. The cap \(K\) is polylogarithmic, not an arbitrary numerical QP cap.
   Trial division of an \(O(K^2)\)-bit resultant is QP only in that stated
   range.
5. The \(N\)-action is always invertible modulo every \(f_j\) by F178. The
   \(N+3\)-action need not be; the final statement keeps that nonunit branch
   explicit.
6. A global return only gives an annihilator. Exact common order still uses
   factor-first stripping, which factors on unequal local orders.
7. No short-period existence theorem is claimed.

## Computation

No mathematical computation was run. No durable result ledger was edited by
this candidate artifact.
