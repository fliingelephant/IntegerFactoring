# F239 preregistration corrigendum: word-size output

This correction is frozen before any F239 scan runs.  It does not change a
word menu, domain, rank, or stopping rule.

`PREREG.md` calls

\[
 n\sum_j\operatorname{bitlen}(K_j)
\]

the bit length of the quotient word.  This sum is an upper bound, not the
exact bit length of a product.  The scan will not materialize a word.
Instead, for each base word with nonzero absolute factors `A_j`, it will
report the rigorous interval

\[
 1+n\sum_j(\operatorname{bitlen}(A_j)-1)
 \ \le\ \operatorname{bitlen}\!\left(\prod_j A_j^n\right)
 \ \le\ n\sum_j\operatorname{bitlen}(A_j).
\]

For a combined word, add the logarithmic lower sums and upper sums before
applying the same `+1` lower endpoint.  These bounds are sufficient for the
`O(n^3)` public-word cost claim.  No exact word bit length will be asserted.
