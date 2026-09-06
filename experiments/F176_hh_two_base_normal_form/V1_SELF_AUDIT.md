# F176 candidate self-audit

## Central claim

F176 does not replace F174. It fixes \(D=n\), preserves every F174 screen,
and adds one collision bank only when the line-13 prime is at least five.
The bank forces every no-factor escape to be two or three. The base-three
case is then exactly a composite Mersenne input with prime exponent.

## Collision audit

- The proof uses \(n<64\) only as a fixed finite preprocessing range.
- For \(n\ge64\), \(t=\lceil\sqrt n\rceil\le n/4\).
- Every \(2^u3^v\) in the bank is below \(N\).
- Unique factorization makes all bank integers distinct.
- The bank has more than \(n\), hence more than \(M\), members.
- If \(\beta\ge5\), both generators occur in the completed HH prefix and
  are annihilated by the current \(M\).
- Root counting is over \(\mathbf F_p\), not over the composite ring.
- A colliding difference is nonzero and smaller than \(N\), so its gcd is
  proper.

The proof needs no balancedness and no squarefreeness.

## Prime-power audit

For \(p^a\parallel N\), a collision modulo \(p\) already makes the gcd
nontrivial. If the difference were divisible by all of \(N\), its absolute
value would be at least \(N\), contrary to the bank bound. Thus the gcd is
proper even when \(N\) is a power of one rational prime.

The imported F174 order screens certify exact orders modulo every hidden
prime power, so the hard certificates also retain their original
prime-power scope.

## Mersenne audit

- Before an escape at three, the only nontrivial processed integer is two.
- The no-factor HH prime-divisor screens make its exact global order exact
  in every hidden component.
- \(N\mid2^M-1\) and \(M\le n\) force \(M=n\).
- The interval \(2^{n-1}<N<2^n\) then forces \(N=2^n-1\).
- A composite exponent gives the explicit cyclotomic factor
  \(2^{n/\ell}-1\). Thus only prime exponent remains.
- The input is promised composite. F176 does not confuse a Mersenne prime
  with a factoring target.

## Complexity audit

The collision list has \(O(n)\) entries, not exponentially many entries.
The pair scan has \(O(n^2)\) gcds. Its exact integers have
\(O(\sqrt n)\) bits. The finite preprocessing, exponent trial division,
and complete-factor recursion add only polynomial overhead to F174's QP
bound.

## Scope risks retained

1. The proof imports the full F174 transcript theorem and all its external
   Harvey--Hittmeir premises.
2. It does not localize unequal hidden orders of base two.
3. It does not factor prime-exponent composite Mersenne numbers.
4. It does not convert capacity into exact common order.
5. It is not an all-input QP factoring theorem.

These exclusions are part of the candidate, not deferred corrections.
