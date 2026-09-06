# F194 self-audit

## Verdict

PASS for the stated balanced-semiprime identities and named-model
boundaries. No QP evaluator or factoring algorithm is claimed.

## Checks

1. The balance promise gives \(p\le B<\sqrt2p<2p\) and \(B<q\). Hence the
   denominator prefix contains exactly the one hidden nonunit \(p\).
2. The proof of the post-jump value cross-multiplies and cancels an ordinary
   integer factor \(p\). It does not divide by \(p\) in \(\mathbb Z/N\).
3. The AKS coefficient at \(k=p\) is \(q\), while every other coefficient in
   the declared prefix is zero. The sign in the alternating prefix is
   negative because \(p\) is odd.
4. Equation (3) returns \(q\), not merely a nontrivial unspecified factor.
5. The central-binomial valuation arguments count the denominator
   cancellation at \(p\) and the surviving numerator occurrence of \(q\).
6. The polynomial-moment theorem uses integer divisibility
   \(W(k)-W(0)\in k\mathbb Z\); it does not assume a degree bound.
7. The Frobenius formulas are local field identities. The local leading
   coefficients are nonzero under \(p<q<2p\).
8. The cyclic statement is explicitly only about source support. It does not
   claim that arithmetic cancellation cannot factor.
9. The quotient-carry corollary uses the signed quotient. It is not
   \(\lfloor C/N\rfloor\) in both parity cases.
10. Standard truncation and baby-step/giant-step costs are context, not
    lower bounds. A new succinct threshold or Hasse-derivative extractor is
    left open.

## Scope exclusions

- unbalanced semiprimes;
- repeated prime powers;
- a QP evaluator for the remote coefficient or its quotient carry;
- a general circuit lower bound;
- cancellation-sensitive cyclic sketches;
- an all-input factoring theorem.
