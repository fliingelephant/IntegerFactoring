# HOSTILE AUDIT — F283

## Verdict

**PASS.** I found no false theorem, missing endpoint, invalid divisibility step, or illicit lower-bound inference. No repair is required.

## Frozen-set authentication

I authenticated the frozen set before reading `STATEMENT.md` or `PROOF.md`.

- `FROZEN.sha256`: `4e71c1866f2fc8badfa063f3e08aee43531de12a7fde49452254d04fec681e5e`
- `STATEMENT.md`: `97711c57667f13d4a86daa5b0533ecdb3165818f92544016fb38ee8673b3e006`
- `PROOF.md`: `b14153c052c20e5059dbd1a0881cd71dc846a439c712f1a871ec80cabc6520e1`
- `SELF_AUDIT.md`: `5d8c5c9f291f2cc7f85bda8cddb4b1626db858fd921026413359bfccaaedd57e`
- `PROVENANCE.md`: `7dc6f672342a9f1cdb59b4eb1c7f95b21bc916b87b852035f4bcd620d2f6c16a`
- `MANIFEST.md`: `23ca73054178346d73ebbf2e9a89232e4cbe52c216c55e829202c567e8bb7b5a`

Every manifest entry returned `OK`. I then read `STATEMENT.md` and `PROOF.md` in full. I did not use the self-audit as evidence.

## Hostile reconstruction

1. **Generalized Stirling endpoint.** Unit-spaced divided differences give
   \(\Delta^B X^{2B}/B!=h_B(a,\ldots,a+B)=G_a(2B,B)\). Newton interpolation gives the stated recurrence. Both generating functions have the correct indices. For nonnegative \(r\), the exponential generating function is exactly that of the stated \(r\)-Stirling number. Arbitrary shifts use the polynomial identity and need no combinatorial interpretation.

2. **Distinct poles and exact scope.** Over \(\mathbb Q(a)\), the denominator has exactly \(B+1\) distinct uncancelled factors. This proves order and dimension \(B+1\) only for the full scalar sequence and its standard linear constant-matrix realizations. After fixed-radix decimation, the modes \((a+j)^r\) remain pairwise distinct and their coefficients remain nonzero. The displayed bidiagonal matrix has the correct orientation and endpoint. The packet does not transfer this result to the isolated diagonal value \(u_B\), modular specializations, nonlinear or adaptive state, or hard-wired entries.

3. **Shifts and block laws.** Translating the complete-homogeneous generating function gives the coefficient \(\binom{2B}{B-j}\) in every term. Reflection reverses and negates the node multiset. One forward shift raises the difference order and gives the stated \((B+1)h_{B-1}\) law. The interval split is a full coefficient convolution. The parity formulas have the correct child lengths and affine shifts, including the empty child at \(m=0\). Their linear leaf count and width claims concern only the displayed direct recursion. They do not assert a general lower bound.

4. **Divided-power crossing.** Composition contributes \(\binom{m+n}{m}\). At the first crossing, all inputs are below \(p\) and
   \(p\le k\le B<q<2p\). Hence the numerator factorial contains one \(p\) and no \(q\), while the input factorials contain neither. Thus the gcd with \(N\) is exactly \(p\). The same valuation proves the finite-arity endpoint. Postponed normalization gives \(B!F_B(a)\), which contains \(p\) through \(B!\) and \(q\) through \(F_B\), so it is zero modulo \(N\). Addition-subtraction chains and custom quotient decoders are expressly outside the claim.

5. **Universal interval content.** Expanding the shifted monomial gives the stated Stirling coefficient formula and leading coefficient \(\binom{2B}{B}\). For \(B+1<r<2B\), the complement of the \(B+1\) nodes in \(\mathbb F_r\) has degree below \(B\), while the next term from \((1-t^{r-1})^{-1}\) occurs above degree \(B\). This proves universal vanishing and coefficientwise divisibility. The branch inequalities put \(q\), but not \(p\), in this interval. Legendre valuations give \(v_p\binom{2B}{B}=0\) and \(v_q\binom{2B}{B}=1\), including all higher-factorial endpoints. Therefore both gcd statements are exact. Dividing by \(P_B\) or the full content leaves a degree-\(B<q\) polynomial with nonzero leading coefficient modulo \(q\); it removes universal \(q\)-vanishing but proves neither efficient quotient evaluation nor a reduction from arbitrary evaluation to content extraction.

6. **The \(N^2\) quotient boundary.** Writing \(B!=pU\) and \(F_B=qV_B\) gives \(D_B/N\equiv UV_B\pmod N\), with \(U\) a unit. Independently of the cited earlier result, modulo \(p\) the full-field block plus the repeated nodes gives
   \[
   F_B(a)=2h_{s+1}(a,a+1,\ldots,a+s).
   \]
   Its degree is \(s+1<p\), and its leading coefficient is
   \(2\binom{2s+1}{s+1}\ne0\pmod p\). Modulo \(q\), the leading coefficient of \(V_B\) is a unit and \(B<q\). Nonroots can therefore be chosen in both fields and combined by CRT, producing shifts for which \(UV_B(a)\) is a unit modulo \(N\). Thus the immediate quotient is not an all-shift splitter. The faithful modulus \(NB!\) does recover \(F_B\bmod N\), but has \(\Theta(B\log B)\) bits and materializes the factor-bearing value \(B!\).

7. **Search disposition and exclusions.** Each rejected search family is tied to a displayed full-width state, convolution, two-child recursion, nonunit normalization, raw zero, explicit factor gate, immediate quotient, or already-super-target endpoint. The integer-output item is also sound: \(F_B(0)=\left\{\begin{smallmatrix}2B\\B\end{smallmatrix}\right\}\) contains all pair partitions, already giving \(\Theta(B\log B)\) output bits. The baby-step/giant-step item is explicitly an endpoint cost, not a lower bound. The no-search conclusion is a scoped research disposition, not a proof of nonexistence.

The eight exact exclusions are honored: the packet supplies no evaluator, general circuit lower bound, nonlinear-state lower bound, Mahler nonexistence theorem, evaluator-to-content reduction, impossibility result for custom exact division, all-input factoring theorem, empirical result, or new literature claim. In particular, no generic fixed-\(B\) pole argument is applied to a diagonal or nonlinear algorithm.

## Final disposition

**PASS — frozen manifest SHA-256:** `4e71c1866f2fc8badfa063f3e08aee43531de12a7fde49452254d04fec681e5e`
