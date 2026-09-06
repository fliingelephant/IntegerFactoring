# F190 self-audit

## Verdict

The frozen statement and proof are internally consistent as a proof-only
candidate. The result is a collection of exact named-model boundaries and a
smaller live interface. It is not a factoring theorem and not a lower bound
against arbitrary processing of retained full words.

It still requires a fresh hostile audit and, if that passes, a statement-only
blind reconstruction. No mathematical computation was run.

## Attacks checked

1. **Squarefreeness.** The exact Fourier support and Hankel rank use
   \(N=pq\) with distinct odd primes. The Jacobi character is then the
   primitive product of the two local quadratic characters. These claims are
   not stated for repeated prime powers.

2. **Balance.** Exact Fourier and correlation identities do not need balance,
   but the estimates \(p,q=2^{n/2+O(1)}\),
   \(\varphi(N)=N-O(\sqrt N)\), and every
   \(2^{-n/2+o(n)}\) conclusion do. The statement places those claims under
   \(p<q<2p\).

3. **QP versus exponential.** A fixed QP envelope is \(2^{o(n)}\).
   Therefore QP products remain negligible compared with \(p\asymp2^{n/2}\).
   In contrast, \(N^{1/4}=2^{\Theta(n)}\),
   \(\varphi(N)=2^{\Theta(n)}\), and \(2^{cn}\) are exponential and are not
   QP.

4. **Public transcript.** Retaining \(X\) does not reveal a new oracle value.
   Every Jacobi entry and acceptance gcd is recomputable from \((N,X)\).
   This observation alone does not prove the transcript useless: a decoder
   may exploit many publicly computed values jointly. The equivalence theorem
   says only that a decoder promised to output a numerical prime is already a
   QP formulation of factoring.

5. **Acceptance overhead.** Trial division through \(B=4mk\) is QP. If it
   does not split the node, every hidden prime exceeds \(B\). With at most
   \(k\) distinct primes, rejection mass is below \(1/4\). A proper gcd during
   sampling is success, not rejection. Thus accepted batches have constant
   expected overhead.

6. **Odd-exponent target.** A non-perfect-power integer has hidden exponent
   gcd one. If every exponent were even, that gcd would be at least two.
   Hence at least one exponent is odd. Exact perfect-power preprocessing is
   necessary because the accepted Jacobi signs erase even-multiplicity
   components.

7. **Fourier zeros.** The CRT Gauss-sum factorization has a zero local Gauss
   sum exactly when the corresponding local frequency is zero. A global
   frequency is therefore supported exactly when it is a unit modulo \(N\),
   giving exactly \(\varphi(N)\) modes.

8. **Hankel rank.** Fourier inversion supplies \(\varphi(N)\) distinct
   exponentials with nonzero coefficients. Their Vandermonde columns and
   transposes have full rank, so the periodic \(N\)-by-\(N\) Hankel rank is
   exactly \(\varphi(N)\). The conclusion is limited to dense recurrence,
   Prony/Padé, explicit-mode, and materialized-rank models. A high-degree
   object can still have a short arithmetic description.

9. **Autocorrelation.** For a prime, the correlation is \(r-1\) at zero
   shift and \(-1\) otherwise. CRT multiplication gives all four cases.
   Every nonunit difference already exposes the same factor through Euclid,
   so the complete correlation adds no factor-sensitive screened case.

10. **Sampling lower bounds.** The claimed sample counts are exact variance
    calculations for the ordinary independent empirical average. They are
    not statistical-query lower bounds against all estimators or against an
    algorithm that uses other arithmetic data.

11. **QP explicit correlations.** P53's odd-support bound is
    \((u-1)^2/\sqrt N\). Its all-even informative deviation is
    \(u(p+q-u)/N\). A QP \(\ell_1\) expansion and QP total support multiply
    these only by \(2^{o(n)}\). The extension still discards each source and
    row after releasing one scalar; it does not touch the full-word channel.

12. **Accepted local sums.** Removing the \(m-t\) roots outside a selected
    subset adds at most \(m-t\) to the complete squarefree character-sum
    bound. This yields \((m-1)\sqrt r\) uniformly, including \(t=1\).

13. **Product-list normalization.** The \(2^{-m}\) expansion has
    \(2^m-1\) nonempty terms. Their total error is at most
    \((1-2^{-m})(m-1)^2\sqrt N\), so the simpler bound in the statement is
    valid. Under \(m\le(1/2-\delta)\log N\), its relative size is at most
    \(m^2N^{-\delta}=o(1)\), uniformly for every word.

14. **Retained-source caveat.** The list count treats only a product word.
    Each true local source pair corresponds to one global source by CRT, and
    the transcript explicitly retains that numerical source. Therefore the
    exponential row-only list is not asserted to be an ambiguity lower bound
    for the actual pair \((X,Y(X))\).

15. **Long-word distance.** The exact local disagreement count is
    \((r-1)/2\). Hypergeometric concentration plus a union bound over fewer
    than \(r^2/2\) source pairs proves that \(96\ln r\) random distinct
    columns give relative distance at least \(1/6\) with probability at least
    \(1-r^{-2}\). This is an existence/information theorem, not an efficient
    decoder and not a theorem for the fixed consecutive puncture.

16. **Accepted-row collisions.** Conditional accepted local sources are
    independent uniform elements of sets of size \(p-m\) and \(q-m\).
    A fixed cross-row equality has probability at most the reciprocal set
    size. Difference screening handles all within-row pairs. The QP union
    bound remains \(2^{-n/2+o(n)}\).

17. **Polynomial correlated sources.** Coefficient gcd screening ensures
    that a surviving nonzero polynomial has a unit coefficient and is
    nonzero in both local fields. The degree root bound then applies. The
    theorem requires QP degree and a fresh uniform source. It does not cover
    succinct exponential degree, a rational pole mechanism, or repeated
    high-order use of one source.

18. **Surviving interface.** Good long-word distance prevents an
    information-theoretic closure. The exact open operation is source-aware
    and modulus-blind: separate hidden local Paley components and produce a
    verifiable zero divisor without enumerating exponentially many candidates.
    No step of F190 supplies that operation.
