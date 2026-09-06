# F127 V2 hostile audit — PASS

The fresh hostile audit found no mathematical error in the corrected V2
claim. It checked the following points independently.

- Divisibility compatibility of the canonical carries gives the unique
  digits \(A,B,T\), including when \(a\) and \(b\) are not coprime.
- Substitution gives
  \[
  \Omega_{\square}=u[(b-a)T+(ab-1)(A-B)]
  \]
  with the stated strict bound.
- The bound \(2R^4<h\) covers only the residual and eligibility factors.
  The stronger bound \(R^6+1<h\) also covers the endpoint sign screens.
- The menu result is the fraction of all \(Q^3\) ordered triples. It is not
  a conditional density among eligible triples.
- The two arithmetic-progression examples, the balanced-semiprime
  consequence, and the literal fixed-bank quantifiers are correct.

The audit explicitly retested the V1 counterexample. For \(R=4\), its least
factor \(577\) exceeds \(2R^4=512\), but it does not exceed
\(R^6+1=4097\). Thus V2 no longer makes the false endpoint claim there.

The result applies only to numerically small unreduced rectangles and fixed
integer banks. It does not control the large or wrapped source, an adaptive
selector, or P66.
