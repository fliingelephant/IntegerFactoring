# F203 hostile audit

## Verdict

**PASS.** I found no false identity, missing case, reversed sign, invalid
factor extraction, hidden positivity failure, or scope overclaim in the frozen
candidate. The twisted coefficient is an exact promise-specific factoring
equivalent. The quotient identities are exact, including their coalescence.
The recursion statement is only conditional accounting and does not claim a
decoder.

I did not edit a frozen input or a durable ledger. I did not run a
mathematical computation or an experimental search. The edge-case checks
below are algebraic.

## Frozen-input integrity

I checked the hashes before reading the candidate. They matched the supplied
values:

- `STATEMENT.md`:
  `10481fa918cffefe71eee3dee08ad23b7b837d685c899a23e5c03a2a74aa9b4f`
- `PROOF.md`:
  `415b2079baed3b0d01ffa1b82d2d537dbf5288c2dce0640a0175f4bb1515c174`
- `SELF_AUDIT.md`:
  `4883be9a2bb0738fa83c527cfa00bb79e7fb4886a66492959fb8cb6f43e9e44f`
- `PROVENANCE.md`:
  `897e48c467222e4ebb58b5e11971bcbb3cf7962fcd2ee26285d7b23f8a5137de`
- `MANIFEST.md`:
  `bc2918d851be0a36202cfc605a7d0b019b54f9de5ae9a27a3599d329c9af824f`

The supplied manifest hash referred to `MANIFEST.md`; no `MANIFEST.json`
exists in the frozen directory.

## 1. Divisor location and the lift character

From (p<q),

\[
 p<\sqrt{pq}<q,
\]

so (p\leq B<q). Balance gives

\[
 \sqrt N<\sqrt2\,p.
\]

For the possible lower endpoint, (p\geq3) implies

\[
 B+1\leq\sqrt N+1<\sqrt2\,p+1<2p.
\]

Since (2\lceil B/2\rceil\leq B+1), this proves

\[
 \lceil B/2\rceil<p\leq B<q.
\]

Thus the strict endpoint in the definitions of (J_+) and (J_-) does not
lose (p). The factor (q) is outside both children.

The granted prefix gives (r\equiv p\pmod m). Because (p) is odd and
(m) is even, exactly one bit (a\in\{0,1\}) satisfies

\[
 p\equiv r+am\pmod{2m}.
\]

The definition of the weight therefore gives the exact character

\[
 \epsilon=w_{m,r}(p)=(-1)^a.
\]

This proves both child exhaustiveness and the orientation convention. There
is no unhandled zero-weight case for (p).

## 2. Inverse lift and the public sibling relation

Let (v\equiv r^{-1}\pmod{2m}). Both (r) and (v) are odd. For a bit
(a),

\[
 (r+am)(v+am)
 =rv+am(r+v)+a^2m^2.
\]

The first term is one modulo (2m). The second correction is divisible by
(2m) because (r+v) is even. The third correction is divisible by (2m)
because (m) is even. Hence

\[
 \boxed{(r+am)^{-1}\equiv v+am\pmod{2m}}.
\]

This confirms that the inverse lift uses the same bit. It is not the
opposite lift.

Since (N) is odd,

\[
 q\equiv Np^{-1}\equiv Nv+aNm\equiv c_0+am\pmod{2m}.
\]

Also (c_0\equiv c\pmod m). If (c\ne r), then (q) is outside the
support of (w_{m,r}), so (w_{m,r}(q)=0). If (c=r), then (c_0) is
exactly one of (r,r+m) modulo (2m). Adding (am) flips its sign exactly
when (a=1). Thus

\[
 w_{m,r}(q)=w_{m,r}(c_0)(-1)^a
 =\lambda\epsilon.
\]

The quantities (v,c_0,lambda) are public. The relation has no hidden use
of (p) after the prefix (r) is granted.

## 3. All cases for the corrected coefficient

The distinct-semiprime promise gives exactly four positive divisors:

\[
 1,p,q,N.
\]

Subtracting the two public endpoint terms leaves

\[
 T=pw_{m,r}(p)+qw_{m,r}(q).
\]

The sibling relation gives the exhaustive cases

\[
 T=
 \begin{cases}
 \epsilon p,&c\ne r,\\
 \epsilon(p+q),&c=r,\ \lambda=+1,\\
 \epsilon(p-q),&c=r,\ \lambda=-1.
 \end{cases}
\]

No value is zero. In the first case (p>0). In the second case (p+q>0).
In the third case (p-q<0) because the primes are distinct and ordered.
Therefore

\[
 \epsilon=
 \begin{cases}
 \operatorname{sgn}(T),&c\ne r\text{ or }\lambda=+1,\\
 -\operatorname{sgn}(T),&c=r\text{ and }\lambda=-1.
 \end{cases}
\]

The negative sign in the opposite-orientation branch is necessary and is
present in both the statement and proof.

## 4. Factor extraction and the converse

Each branch gives a deterministic polynomial-time factor extraction.

1. If (c\ne r), then (p=|T|).
2. If (c=r) and (lambda=+1), put (s=|T|=p+q). The two factors are
   the roots of (X^2-sX+N).
3. If (c=r) and (lambda=-1), put (d=|T|=q-p). Then
   
   \[
   T^2+4N=d^2+4pq=(p+q)^2.
   \]
   
   Thus (s=\sqrt{T^2+4N}=p+q), followed by
   
   \[
   p=\frac{s-d}{2},\qquad q=\frac{s+d}{2}.
   \]

All integers used here have (O(\log N)) bits. Exact square root,
discriminant evaluation, parity checks, multiplication checks, and exact
division have polynomial bit cost.

Conversely, a factorization lists (1,p,q,N). Direct evaluation of the four
public weights gives (S_{m,r}(N)) in polynomial time. The equivalence is
therefore exact on the stated promise. It does not claim an evaluator for
the coefficient and does not extend the theorem to arbitrary composites.

## 5. Formal Lambert coefficient

As a formal power series,

\[
 \sum_{a\geq1}\frac{a w_{m,r}(a)X^a}{1-X^a}
 =\sum_{a\geq1}\sum_{k\geq1}a w_{m,r}(a)X^{ak}.
\]

For a fixed exponent (N), only the finitely many pairs with (ak=N)
contribute. These pairs are in one-to-one correspondence with (a\mid N).
Hence

\[
 [X^N]\sum_{a\geq1}\frac{a w_{m,r}(a)X^a}{1-X^a}
 =\sum_{a\mid N}a w_{m,r}(a)=S_{m,r}(N).
\]

This is only a coefficient identity. It does not imply an efficient
truncation or a modular-form evaluator.

## 6. The (m=2) specialization and sign edge cases

For (m=2,r=1), the supported classes modulo four are (1) and (3),
with signs (+1) and (-1). Even classes have weight zero. Thus

\[
 w_{2,1}=\chi_4.
\]

Here (v=1), (c=r=1), and

\[
 \lambda=w_{2,1}(N)=\chi_4(N).
\]

The four residue orientations give this complete algebraic table:

\[
\begin{array}{c|c|c|c|c}
p\bmod4&q\bmod4&\epsilon&\lambda&T\\ \hline
1&1&+1&+1&p+q\\
1&3&+1&-1&p-q<0\\
3&1&-1&-1&q-p>0\\
3&3&-1&+1&-(p+q)
\end{array}
\]

The selector formula returns the smaller factor's character in every row.
The fixed coefficient

\[
 \sum_{d\mid N}d\chi_4(d)
\]

therefore factors every semiprime in the stated promise. The only balanced
odd case with (p=3) is outside the quotient hypothesis (2m<p), but the
coefficient algebra itself still works: it uses neither quotient positivity
nor (2m<p). Thus no small selector exception is hidden by the quotient
assumption.

The unweighted sum (sum_{d\mid N}\chi_4(d)) discards the divisor
magnitudes and can be constant or zero across many inputs. The statement
correctly does not identify it with the weighted selector.

## 7. The contracted quotient (K)

The residue congruences give (N\equiv rc\pmod m), so (K) is integral.
The strict hypothesis (2m<p), together with (0<r,c<m), gives

\[
 0<rc<m^2<p^2<N.
\]

Therefore

\[
 0<K=\frac{N-rc}{m}<\frac N2.
\]

Since (N) is odd, (gcd(m,N)=1). Also (r,c<p), so neither can have
the prime factor (p) or (q). Consequently

\[
 \gcd(K,N)
 =\gcd(mK,N)
 =\gcd(N-rc,N)
 =\gcd(rc,N)=1.
\]

This does not cancel an unknown divisor. It uses the fact that (p) is the
least prime divisor of (N).

## 8. Lift parity and both formulas for (K'_a)

Write exact integer lifts

\[
 p=r+mP,\qquad q=c+mQ,
\]

and let (a=P\bmod2), (b=Q\bmod2). Expanding gives

\[
 K=rQ+cP+mPQ.
\]

Because (r,c) are odd and (m) is even,

\[
 \delta=K\bmod2\equiv P+Q\equiv a+b\pmod2.
\]

For bits, this is exactly

\[
 \boxed{b=a\mathbin{\mathsf{xor}}\delta}.
\]

For either candidate (a), use this public relation to choose (b). Then

\[
 (r+am)(c+bm)=rc+m(ac+br)+abm^2,
\]

so

\[
 \boxed{
 K'_a=\frac{K-ac-br-abm}{2}
 =\frac{N-(r+am)(c+bm)}{2m}.}
\]

The numerator in the first expression is even because it is congruent to
(delta-a-b) modulo two. Thus both candidates are integers, not only the
true candidate.

Every lifted residue is positive and strictly below (2m<p). Hence its
product with the other lifted residue is below (p^2<N). This proves

\[
 0<K'_a<\frac{N}{2m}
\]

for both candidates. It also proves coprimality:

\[
 \gcd(K'_a,N)
 =\gcd(2mK'_a,N)
 =\gcd((r+am)(c+bm),N)=1.
\]

For the true (a), the lifted residues are the actual residues of (p) and
(q) modulo (2m). Thus the displayed value is exactly the next quotient
state.

## 9. Separation, parity, and coalescence

If (delta=0), then (b=a), giving

\[
 K'_0=\frac K2,\qquad
 K'_1=\frac{K-r-c-m}{2}.
\]

Their difference is

\[
 K'_0-K'_1=\frac{r+c+m}{2}>0,
\]

so this branch never coalesces.

If (delta=1), then (b=1-a), giving

\[
 K'_0=\frac{K-r}{2},\qquad
 K'_1=\frac{K-c}{2}.
\]

These values agree exactly when (r=c). Therefore

\[
 \boxed{K'_0=K'_1\iff \delta=1\text{ and }r=c.}
\]

In that case the factor lift bits are opposite. The two candidate residue
products are (r(r+m)) and ((r+m)r). They are literally equal. This is
why the quotient forgets which residue lift belongs to the smaller factor.
It does not show that every statistic or every adaptive decoder forgets the
orientation.

At (m=2), one has (r=c=1) for every odd input and

\[
 K=\frac{N-1}{2}.
\]

If (N\equiv3\pmod4), then (K) is odd, so (delta=1), and

\[
 K'_0=K'_1=\frac{K-1}{2}=\frac{N-3}{4}.
\]

The two middle rows of the preceding (chi_4) table are exactly the two
possible smaller-factor orientations on this coalescing branch.

## 10. Bit size and recursive accounting

Let (n) be the binary input length. Since (0<K<N/2),

\[
 \operatorname{bitlen}(K)\leq n-1.
\]

The stronger bound (K'_a<N/(2m)\leq N/4) also gives at least the required
strict descent for either candidate child. Thus a construction that makes
at most one recursive factoring call on one such child, with a
nondecreasing numerical-QP local bound (Q), satisfies

\[
 \mathcal T(n)\leq\mathcal T(n-1)+Q(n).
\]

Iteration along the single chain gives

\[
 \mathcal T(n)\leq \mathcal T(1)+nQ(n),
\]

and multiplication by (n) preserves numerical quasipolynomial time. A
fixed-ratio contraction is not required for this accounting.

This statement is conditional in two important ways. F203 gives neither a
coefficient evaluator nor a rule that selects the true (a). It also does
not assert that an available promise factorer automatically applies to the
generally composite recursive child. No recursive factoring algorithm is
silently obtained from the size bound.

## 11. P165 scope

The promoted P165 text studies complete recursive factorization of
((N-1)/2), followed by Pocklington/Lucas-style processing of independent
uniform bases. It proves exact return and stripping laws and an infinite
balanced family on which a numerical-QP bank of such bases has exponentially
small success probability. It explicitly leaves deterministic bases,
adaptive bases, other exponent families, and complete factorization open.

At (m=2), the F203 child is exactly

\[
 K=\frac{N-1}{2}.
\]

Thus the P165 citation is accurate. F203 uses it only to identify prior
one-child preprocessing and its narrow uniform-base boundary. It does not
turn P165 into a lower bound against adaptive deterministic use of the
factored child.

## Hostile attacks that did not refute the candidate

I checked:

- the strict lower endpoint (lceil B/2\rceil);
- both lifts of the inverse modulo (2m);
- support loss when (c\ne r);
- all three (T) branches and both sign orientations in the last branch;
- exact square-root and parity recovery in factor extraction;
- formal-power-series finiteness at coefficient (X^N);
- all four modulo-four orientations at (m=2);
- the smallest-modulus boundary and the separate role of (2m<p);
- positivity and coprimality of the false candidate (K'_a), not only the
  true one;
- both values of (delta) and the exact coalescence criterion;
- bit-length loss without a fixed-ratio contraction;
- the distinction between recursion accounting and a recursive decoder; and
- the cited P165 restriction to independent uniform-base processing.
