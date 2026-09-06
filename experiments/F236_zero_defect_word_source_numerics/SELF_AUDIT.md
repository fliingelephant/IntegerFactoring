# F236 self-audit

## Exact theorem checks

1. The theorem uses the zero-defect identity `N=1+BH`.  Without it, carry
   integrality fails.
2. The two nearest quotient indices are hidden.  The procedure enumerates
   them; it does not call them public or infer them from `H`.
3. The recovery statistic is the weighted trace `K_pq+K_qp`.  It is not the
   ordinary trace unless `K_p=K_q`.
4. The corrected formula is
   `(u^2H+K_pK_qB-c)/u`.  There is no extra factor `B` or `B^2`.
5. The quadratic is `K_qX^2-TX+K_pN`.  Its roots are `p` and
   `(K_p/K_q)q`; only exact integral divisors are accepted.
6. The square discriminant is necessary for the true tuple but not accepted
   alone.  Exact division into `N` is mandatory.
7. Dyadic half-ties are possible.  The theorem and every scan use the same
   round-half-up convention, giving residues in `[-B/2,B/2)`.
8. Center indices are positive because balance gives `p>B/2`.  Their public
   range `1<=K_p,K_q<=3u` makes the declared bank cost `O(CU^3)`.
9. The Dirichlet bound is `O(B/U+U^2/B)`, not `O(B/U^2)`.  It is not an
   all-input positive result.

## Computational checks

1. Every scan had a separate preregistration before execution.
2. The finite prime-pair generator constructs candidates from
   `q=p^{-1} mod B` and then directly rechecks primality, balance, bit
   length, and `B | N-1`.
3. The code aborts if the expected equal two-adic valuations or carry
   divisibility fails.
4. Word gcds are computed modulo the residuals.  The enormous words are
   not materialized.
5. The first local smoke run was not used as separate evidence.  The frozen
   evidence is the remote exhaustive output.
6. Four early scans printed only summaries to the terminal.  They were
   reproduced after the fact from the unchanged preregistered sources, one
   low-priority process at a time, and their complete reproduction outputs
   are now frozen.  The provenance distinguishes original preserved output
   from reproduction output.
7. The computations are finite evidence.  No asymptotic law is inferred.

## Status

Self-audited candidate ready to freeze.  It still requires a fresh hostile audit and,
after a PASS, a strict statement-only reconstruction before promotion.
