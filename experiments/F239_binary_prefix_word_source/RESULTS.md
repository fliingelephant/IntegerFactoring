# F239 finite numerical results

These are exact finite scan facts.  They are not asymptotic claims.

## Named rows

### F236 combined-word worst row

For

\[
 (p,q)=(4190987,4243619),\qquad n=45,
\]

the residuals are the two primes

\[
 s_p=2095493,\qquad s_q=2121809.
\]

Neither prime divides a quotient, positive suffix, or centered suffix.
Every one of the seven menus therefore leaves

\[
 (r_p,r_q)=(2095493,2121809).
\]

The new source does not improve the frozen F236 combined-word residual on
its exact worst row.

### F236 cubic-carry worst row

For

\[
 (p,q)=(3565721,6646697),\qquad n=45,
\]

one has

\[
 s_p=5\cdot97\cdot919,\qquad s_q=7\cdot118691.
\]

The lists hit `5` and `7`, but miss `97`, `919`, and `118691`.  Every menu
leaves

\[
 (r_p,r_q)=(89143,118691).
\]

F236 found a centered carry of magnitude `14` on this row.  That carry
route and the present word route are different; the comparison supplies no
implication in either direction.

### F237 certified row

For the 129-bit certified F237 semiprime,

\[
 s_p=7593622735504604171,
\]

\[
 s_q=37\cdot359045826645918359.
\]

All three lists miss `s_p` and the large prime factor of `s_q`.  Each list
hits `37`.  Every menu leaves

\[
 (r_p,r_q)=
 (7593622735504604171,359045826645918359).
\]

Thus

\[
 \min(r_p,r_q)=359045826645918359>2^{58}.
\]

This exactly matches the large-factor obstruction in F237.  It is one
finite certified input, not an asymptotic counterfamily.

## Complete F236 zero-defect domain

The rerun contains all 34,463 frozen F236 rows.  The count by bit length is
identical to F236.  The exact menu summaries are:

| Menu | Maximum `min(r_p,r_q)` | `=1` | `<=n` | `<=n^2` | `<=n^3` |
|---|---:|---:|---:|---:|---:|
| `K` | 2,096,765 | 593 | 1,338 | 7,942 | 25,410 |
| `R` | 2,095,493 | 805 | 1,590 | 8,763 | 25,861 |
| `C` | 2,095,493 | 942 | 1,849 | 9,592 | 26,732 |
| `KR` | 2,095,493 | 1,691 | 2,553 | 11,773 | 28,154 |
| `KC` | 2,095,493 | 1,806 | 2,690 | 12,168 | 28,467 |
| `RC` | 2,095,493 | 1,597 | 2,497 | 11,656 | 28,080 |
| `KRC` | 2,095,493 | 2,427 | 3,223 | 13,503 | 29,100 |

For the full combined menu, the exact fractions are

\[
 \Pr_{\rm finite}(r_{\min}=1)={2427\over34463}=7.042335\%,
\]

\[
 \Pr_{\rm finite}(r_{\min}\le n)={3223\over34463}=9.352059\%,
\]

\[
 \Pr_{\rm finite}(r_{\min}\le n^2)
 ={13503\over34463}=39.181151\%,
\]

\[
 \Pr_{\rm finite}(r_{\min}\le n^3)
 ={29100\over34463}=84.438383\%.
\]

These are domain fractions, not probabilities for an input distribution.

There are 161,570 residual-prime occurrences across the two sides.  Of
these, 85,913, or `53.173857%`, miss all three lists.  The combined maximum
occurs at the published F236 word-worst row above.

## Broad balanced-semiprime domain

The exact domain contains all 18,474,958 pairs of distinct odd primes with

\[
 3\le p<2^{16},\qquad p<q<2p.
\]

There is no zero-defect filter.  Input lengths run from 4 through 33 bits.
The exact menu summaries are:

| Menu | Maximum `min(r_p,r_q)` | `=1` | `<=n` | `<=n^2` | `<=n^3` |
|---|---:|---:|---:|---:|---:|
| `K` | 32,759 | 2,778,685 | 4,132,080 | 13,167,346 | 18,474,958 |
| `R` | 32,759 | 1,493,000 | 3,511,053 | 11,748,724 | 18,474,958 |
| `C` | 32,759 | 1,584,289 | 3,609,591 | 11,892,961 | 18,474,958 |
| `KR` | 32,759 | 5,017,463 | 5,796,612 | 14,580,906 | 18,474,958 |
| `KC` | 32,759 | 5,072,104 | 5,834,933 | 14,618,271 | 18,474,958 |
| `RC` | 32,759 | 2,376,077 | 4,670,465 | 12,930,999 | 18,474,958 |
| `KRC` | 32,759 | 5,967,904 | 6,494,106 | 14,962,785 | 18,474,958 |

For the full combined menu, the exact fractions are `32.302666%`,
`35.150857%`, `80.989548%`, and `100%`, respectively.  The `n^3` result is
a cutoff effect.  For `n<=32`, balance and `d>=2` give
`s_p<p/2<2^(n/2-1)<=n^3`.  At `n=33`, the scan cap gives
`s_p<=p/2<2^15<33^3`.  It is not evidence for an all-input cubic theorem.

The selected combined maxima by bit length are

| `n` | 20 | 24 | 28 | 32 | 33 |
|---|---:|---:|---:|---:|---:|
| maximum | 491 | 2,003 | 8,111 | 32,723 | 32,759 |

This finite sequence follows the available `2^(n/2)` scale.  No asymptotic
fit is claimed.

There are 87,891,505 residual-prime occurrences.  Of these, 32,710,874, or
`37.217333%`, miss every factor list.

For the full combined menu, one exact worst row is

\[
 p=65519,\qquad q=79979,\qquad N=5240144101,\qquad n=33,
\]

with

\[
 d=2,\qquad
 s_p=32759=17\cdot41\cdot47,\qquad
 s_q=39989.
\]

Every displayed residual prime misses every quotient, positive suffix, and
centered suffix.  Hence

\[
 (r_p,r_q)=(32759,39989).
\]

## Interpretation

The quotient, positive-suffix, and centered-suffix lists are useful on many
finite inputs.  Combining them increases the full-saturation count.
However, none supplies a forced hit for a large exclusive residual prime.
The F236 and F237 exact examples survive unchanged at their large-factor
scale.

The evidence supports only this conclusion:

\[
 \boxed{\text{The binary-spine menus do not supply the required all-input word.}}
\]

An asymptotic rejection would require an infinite semiprime family.  The
power-of-two-neighbor criteria in `STATEMENT.md` reduce two structured
families to multiplicative-order conditions, but this packet proves no
required prime distribution.

## Output hashes

- named rows: `2f60d0a8a49bf5cedf252bef12126160b2aec113dccad4848159d8a39cd45b4c`;
- corrected F236-domain scan:
  `e31176462ba5617b3555249df6b6ea5149aff3fbd6a367fb34d550a5f6fdbc6f`;
- corrected broad scan:
  `b1914784d6babc2b3026260bcc0de82c7277c914aa94de2d17fe052bab0f75dd`.
