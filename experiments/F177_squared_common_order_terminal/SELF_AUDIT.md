# F177 self-audit

## Verdict

The two congruences and candidate counts are exact under the stated balanced
squarefree-semiprime promise. This is a terminal decoder theorem only.

## Checks

1. The ordinary modulus is \(M^2\), not \(M\), because the public identity
   is \(N+1-(p+q)=(p-1)(q-1)\).
2. The torus signs are fixed by
   \((p-\epsilon)(q+\epsilon)=N-1-\epsilon(q-p)\).
3. The balanced sum constant is \(3/\sqrt2-2\). The balanced difference
   constant is \(1/\sqrt2\).
4. Every accepted candidate is verified by exact multiplication. False
   square candidates cannot corrupt the output.
5. The theorem does not replace F170's useful combined-channel CRT theorem.
   It improves the threshold when one individual ordinary or oriented torus
   common order is already large.
6. Constant common-order obstruction families remain outside the terminal
   range.
7. No computation, hidden-factor-assisted search, or durable-ledger edit was
   used.
