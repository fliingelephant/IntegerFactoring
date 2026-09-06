# F194 V2 self-audit

## Verdict

PASS for the exact balanced-semiprime identities and the narrowly defined
Boolean-incidence and modular-carry statements. No QP evaluator or general
lower bound is claimed.

## Repair of V1

V1 failed hostile audit. It used the false intermediate inequality
\(2p\le q+1\), used undefined provenance language, omitted the numerical-QP
bound on \(R\), and described the carry as a standalone primitive although
recovery also needs the remote coefficient residue.

V2:

1. proves \(2m<q\) from \(2m\le B+1\le q\) and parity;
2. states only full Boolean source incidence in each cyclic bucket;
3. explicitly requires numerical-QP \(R\);
4. requires the joint residue pair \((C,h)\bmod2^t\);
5. removes unsupported claims about standard holonomic algorithms.

## Checks

1. Every balance inequality is valid for odd \(p\ge3\).
2. The hidden \(p\) is canceled only in \(\mathbb Z\), never inverted modulo
   \(N\).
3. The exceptional AKS coefficient is \(+q\); its alternating sign is
   negative because \(p\) is odd.
4. Both central-binomial valuation counts include all multiples below their
   endpoints.
5. Polynomial moments are an identity, not an evaluator claim.
6. Local Frobenius powers and exact \(X\)-adic orders use nonzero linear
   coefficients.
7. The cyclic claim says nothing about cancellation or rich provenance.
8. The carry claim is conditional on both modular residues and says nothing
   about computing them.
9. The three listed sufficient primitives are conditional algorithmic
   interfaces, not supplied algorithms.

## Scope exclusions

- unbalanced or repeated-prime inputs;
- QP evaluation of a remote binomial coefficient;
- QP evaluation of its signed quotient carry;
- coefficient-sensitive cyclic sketches;
- circuit or information lower bounds;
- an all-input factoring theorem.
