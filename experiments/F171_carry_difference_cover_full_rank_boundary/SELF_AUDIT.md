# F171 self-audit

## Status

This is an author self-audit only. It does not raise the candidate above
proof-only status.

## Checks performed

1. **Difference cover versus row cover.** The proof does not use the invalid
   implication that a repeated residue class is the occupied class. It proves
   the stronger statement directly: for each \(r\le R\), two displayed
   carries have valuation exactly one at \(r\).

2. **Canonical endpoints.** The CRT makes \(g_k\mid1+kN\), and
   \(k<g_k\) gives \((1+kN)/g_k<N\). Both endpoints are positive and below
   \(N\), so the inverse is canonical.

3. **CRT compatibility.** All \(g_k\) are distinct primes larger than
   \(m\). The inverses of \(k\) exist modulo every declared square modulus.
   Each prescribed residue is \(-k^{-1}\) modulo \(g_k\), so the final CRT
   class is reduced.

4. **Second prime lower bound.** The progression representative satisfies
   \(2Q<b<5Q\). Choosing the least prime in that reduced class makes
   \(\ell\ge b>2Q\), not merely \(\ell>0\). This keeps both hidden factors
   above \(Q\).

5. **Use of Linnik.** Only the standard least-prime upper bound in a reduced
   residue class is used. It gives \(\log N=\Theta(\log Q)\). No short
   interval or bounded-ratio prime theorem is assumed.

6. **No balance overclaim.** The proof does not claim \(p<\ell<2p\). It
   claims only distinct trial-hard prime factors and the displayed length
   relation.

7. **Small-row valuation.** After writing
   \(1+(a+jr)N=r(h+jN)\), avoiding one residue of \(j\pmod r\) gives
   valuation exactly one. The four choices leave at least two good indices
   even for \(r=2\) and \(r=3\). No claim is made that only one carry in
   the entire interval can have valuation at least two.

8. **Private rows.** The congruence modulo \(g_k^2\) gives valuation one,
   not only divisibility. The inequality \(g_k>m>|k-j|\) proves absence from
   every other selected value. The same prime is the public canonical first
   endpoint, so no auxiliary private-prime bank is needed.

9. **Deduplication.** The exact values \(1+kN\) are distinct. Global
   exact-value deduplication cannot collapse two of these values into one.
   It can retain an earlier occurrence of one value, so the proof does not
   make an endpoint-screen claim about that earlier presentation.

10. **Direct screens.** The proof checks only the displayed canonical
    endpoint pairs. It does not claim that every screen in the complete
    source is null.

11. **Length link.** The prime bank contributes \(m\) squares, so
    \(\log Q=\Theta(m\log m)\). Bertrand and Linnik give
    both lower and upper bounds on \(\log N\), with no circular choice of
    \(m\) from \(n\).

12. **Public source range.** The explicit lower bound
    \(n>2\log_2Q>4m\log_2m\), together with
    \(g_k<4m\log m\), puts every \(g_k<n\) for large \(m\). The bank is a
    selected subset of the standard public seed range.

13. **Rank scope.** The identity rows prove full rank only for the selected
    columns. They can be reused by omitted static or adaptive columns. This
    is not a complete-source null and not an all-input obstruction.

14. **Root and quotient scope.** The selected kernel is zero, so it supplies
    no normalized root. Small rational-prime row reuse has no proved map to
    P154 quotient-fingerprint closure or state growth. A later full-source
    kernel would still have to violate the P138 section.

15. **QP relevance.** The displayed bank and cutoff are polynomial in
    \(n\), hence within the permitted QP budget. The theorem does not say
    that every QP carry cutoff has such a family, and it does not rule out a
    source theorem that covers and controls all larger fresh rows.

## Result

No internal counterexample was found. The highest-risk point for hostile
audit is the prime-bank and Linnik length bookkeeping, followed by the exact
claim that the public endpoints lie below \(n\). The intended classification
is a selected-source method failure: carry coverage, even in its strongest
targeted valuation-one form, is not a rank theorem.
