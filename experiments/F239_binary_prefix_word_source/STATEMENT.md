# F239 candidate — exact binary-spine incidence and finite source obstruction

## Status and scope

This packet separates an exact theorem from finite evidence.

1. The endpoint, incidence, saturation, size, and power-of-two-neighbor
   statements below are proofs.
2. The F236-domain and broad balanced-semiprime scans are finite evidence.

The proposed literal quotient word is invalid.  The corrected quotient,
positive-suffix, and centered-suffix words are valid public polynomial-bit
integers, but this packet proves no all-input quasipolynomial residual bound.
It proves no asymptotic counterfamily either.

## Literal endpoint and corrected words

Let `N=pq` be an odd semiprime and put

\[
 n=\lceil\log_2(N+1)\rceil,
 \qquad K_j=\left\lfloor\frac{N}{2^j}\right\rfloor.
\]

Then `N<2^n`, so

\[
 K_n=0.
\]

Consequently, the literal word `prod_(j=1)^n K_j^n` is zero.  It is outside
the F238 premise `W>=1`, and `v_2((N-1)W)` is undefined.

The corrected nonzero quotient word is

\[
 W_K=\prod_{j=1}^{n-1}K_j^n.                         \tag{1}
\]

Define the positive and round-half-up centered binary suffixes by

\[
 R_j=N-2^jK_j=N\bmod2^j,
\]

\[
 C_j=N-2^j\left\lfloor\frac{N+2^{j-1}}{2^j}\right\rfloor,
 \qquad -2^{j-1}\le C_j<2^{j-1}.
\]

Since `N` is odd, every `R_j` and `C_j` is nonzero.  Put

\[
 W_R=\prod_{j=1}^{n}R_j^n,
 \qquad
 W_C=\prod_{j=1}^{n}|C_j|^n.                         \tag{2}
\]

All seven nonempty products of `W_K,W_R,W_C` are public positive integers.
Each has `O(n^3)` bit length.

## Exact residual-prime incidence

Let

\[
 d=\gcd(p-1,q-1),\qquad
 s_p=(p-1)/d,\qquad s_q=(q-1)/d.
\]

For every prime `ell` and `1<=j<n`,

\[
 \boxed{
 \ell\mid K_j
 \quad\Longleftrightarrow\quad
 N\bmod(\ell2^j)<2^j.
 }                                                     \tag{3}
\]

If `ell` is an odd divisor of `s_p`, then also

\[
 \boxed{
 \ell\mid K_j
 \quad\Longleftrightarrow\quad
 R_j\equiv q\pmod\ell.
 }                                                     \tag{4}
\]

Exchange `p` and `q` for a divisor of `s_q`.  Formula (4) is not valid at
`ell=2`; formula (3) remains valid there.

For an odd `ell` and fixed `j`, exactly a fraction `1/ell` of the odd
residue classes modulo `ell 2^j` satisfy (3).  After lifting all quotient
events to the common modulus `ell 2^(n-1)`, a union bound gives

\[
 \Pr_{\rm classes}(\ell\mid K_j\text{ for some }j<n)
 \le {n-1\over\ell}.                                 \tag{5}
\]

Thus `ell>n-1` leaves at least one odd residue class whose complete quotient
spine misses `ell`.  This is a residue-class statement.  It does not prove
that such a class contains a semiprime with `ell` in a hidden residual.

The other two incidence laws are direct:

\[
 \ell\mid R_j
 \quad\Longleftrightarrow\quad
 (N\bmod2^j)\bmod\ell=0,                              \tag{6}
\]

and, writing `r=R_j`,

\[
 \ell\mid C_j
 \quad\Longleftrightarrow\quad
 \begin{cases}
  r\equiv0\pmod\ell,&r<2^{j-1},\\
  r\equiv2^j\pmod\ell,&r\ge2^{j-1}.
 \end{cases}                                         \tag{7}
\]

If `ell^a || s_i`, then `a<n`.  Therefore one hit by a factor in a menu
saturates the full prime power through the exponent `n`.  For any one of
the seven menus `M`, the exact F238 residual is

\[
 \boxed{
 r_i(M)=
 \prod_{\substack{\ell^a\parallel s_i\\
       \ell\text{ hits no factor list in }M}}
 \ell^a.
 }                                                     \tag{8}
\]

In particular, the construction depends only on prime support incidence.
It does not require a factorization to construct the public word.

The first quotient has one limited deterministic effect.  Since

\[
 K_1=(N-1)/2,
\]

every odd residual prime that also divides `d` divides `K_1`.  The word
therefore removes valuation-overlap primes.  It need not hit a genuinely
exclusive residual prime.

## Exact power-of-two-neighbor criteria

These criteria give structured counterfamily templates.  They do not prove
that the required semiprimes exist infinitely often.

If

\[
 N=2^m-1=pq,
\]

then `n=m` and

\[
 K_j=2^{m-j}-1,\qquad R_j=2^j-1,\qquad C_j=-1.
\]

For any odd prime `ell` with `ell` not dividing `N`, the full combined word
hits `ell` exactly when

\[
 \operatorname{ord}_{\ell}(2)<m.                     \tag{9}
\]

If

\[
 N=2^m+1=pq,
\]

then `n=m+1`.  The quotient factors are powers of two, the positive
suffixes are `1` except for `R_n=N`, and the centered suffixes are units
except for

\[
 C_n=1-2^m.
\]

For any odd prime `ell` with `ell` not dividing `N`, the full combined word
hits `ell` exactly when

\[
 \operatorname{ord}_{\ell}(2)\mid m.                \tag{10}
\]

Thus a Mersenne or Fermat-neighbor semiprime with large residual primes
outside the order conditions would be an exact obstruction.  No infinite
prime family of this type is asserted.

## Frozen finite evidence

The exact named rows give the following facts.

1. On the F236 combined-word worst row, every factor list misses both prime
   residuals.  Every menu leaves
   `(r_p,r_q)=(2095493,2121809)`.
2. On the F236 cubic-carry worst row, every menu leaves
   `(r_p,r_q)=(89143,118691)`.
3. On the certified F237 row, the small factor `37` is hit, but the two
   large certified residual primes are not.  Every menu leaves

\[
 (r_p,r_q)=
 (7593622735504604171,359045826645918359),
\]

so the minimum remains larger than `2^58`.

The complete F236 zero-defect domain contains 34,463 rows.  The largest
combined-menu residual minimum is exactly `2095493`, at the published F236
worst row.  Only 2,427 rows have combined residual minimum one.

The broad domain contains all 18,474,958 pairs

\[
 3\le p<2^{16},\qquad p<q<2p
\]

of distinct odd primes.  The largest residual minimum is `32759` for every
menu.  For the full combined menu, one worst row is

\[
 (p,q)=(65519,79979),
\]

where every residual prime misses all three lists and

\[
 (r_p,r_q)=(32759,39989).
\]

These results rule out full saturation and small fixed polynomial bounds on
the named finite rows.  They do not rule out an unspecified
quasipolynomial function of `n` on all inputs.
