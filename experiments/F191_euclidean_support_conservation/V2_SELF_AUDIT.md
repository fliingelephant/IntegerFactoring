# F191 V2 self-audit

## Verdict

V2 repairs the three defects identified by the fresh V1 hostile audit. The
exact congruence law, canonical counterexample, and finite permutation-bank
count are unchanged. This remains a proof-only candidate for a narrow
normalization obstruction. It is not a factoring lower bound and not a
closure of the P164 wide-action branch.

No mathematical computation was run. Hashing is used only to freeze the
text. V2 still requires a fresh hostile audit and, if that passes, a fresh
statement-only blind reconstruction.

## Audited repairs

1. **Direct P163 admissibility.** The live interface now requires public
   integers \(A_j\) with \(0<|A_j|<N/2\), as well as prime-support coverage
   and QP list/construction bounds. Their absolute values are positive and
   have at most \(n-1\) bits. An unrestricted quotient or carry is no longer
   claimed to be a direct P163 input.

2. **Separate localization alternative.** If a quotient or carry is zero or
   oversized, V2 requires a separate support-preserving size-localization
   theorem. It does not suggest that centering supplies such a theorem.

3. **Zero divisor.** The branch \(\ell\mid D\) calls \(D\) a support carrier
   only when \(D\ne0\). The degenerate value \(D=0\) supplies no usable
   auxiliary. The exact equivalence for \(\ell\nmid D\) is unchanged.

4. **Noncircular QP quantifier.** A numerical-QP budget \(B_\star(n)\) is
   fixed independently of \(T\), then \(T=4B_\star+1\) is chosen. If the
   budget depends on \(T\), V2 explicitly assumes a public numerical-QP
   choice satisfying \(4B_\star(n,T(n))<T(n)\). It does not infer such a
   fixed point.

## Rechecked unchanged core

1. **Division convention.** The support law holds for every integer identity
   \(X=QD+R\) in the unit-divisor branch. Ordinary and centered division are
   special cases.

2. **Canonical counterexample.** The balanced residue \(c\) is nonzero
   because \(\ell\nmid N\). Its magnitude is less than \(N/4\), so the
   nearest quotient of \(N+c\) by \(N\) is one. Both one and \(|c|\) are
   admissible smaller integers and miss \(\ell\).

3. **Nearest-integer ties.** Odd \(N\) prevents
   \(\ell b/N\in\mathbb Z+1/2\), so the quotient is unique.

4. **Endpoint count.** A centered quotient in
   \(\{0,\ldots,\ell\}\) is divisible by \(\ell\) only at the two endpoints.
   Each endpoint interval contributes at most \(N/(2\ell)+1\) integers.

5. **Union bound.** No independence is assumed. The two inequalities
   \(\ell\ge4B\) and \(N\ge8B\) give an exceptional union of size at most
   \(N/2<N\).

6. **Valid missed children.** Outside the exceptional union,
   \(1\le Q_i\le\ell-1<N/2\) and \(0<|R_i|<N/2\). The obstruction is genuine
   support loss, not a zero or size failure.

7. **Local-order size.** Conditional on the P161 contract, coprimality of a
   local order with the hidden rational prime makes reduction injective on
   its cyclic subgroup, so the order divides \(p-1\). Every order prime is
   therefore below \(N/2\) on an odd composite.

8. **Model boundary.** The bank theorem is only for permutation-based
   equidistribution. It does not cover arbitrary correlated nonpermutation
   maps, special floor concentration, or non-Euclidean selectors.

9. **One-child recursion.** F191 does not require fixed-ratio contraction.
   Its issue is whether a smaller child retains the target support. A single
   child below \(N/2\) is sufficient for P163's one-bit QP recursion.
