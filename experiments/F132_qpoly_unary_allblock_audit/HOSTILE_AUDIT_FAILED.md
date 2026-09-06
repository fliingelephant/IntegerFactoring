# F132 first hostile audit — FAIL as written

The first independent hostile audit preserved the cost theorem and the main
row algebra. It found four statement defects.

1. An exact-value duplicate can still factor through a new endpoint sign
   screen. The exact certificate is \(N=63\), where the old value \(64\) has
   endpoint pair \((8,8)\), while feedback exposes the duplicate presentation
   \((2,32)\) and \(\gcd(2-32,63)=3\).
2. The \(N=77\) certificate proves that its current two-column prefix has an
   empty 2-core. It does not prove that later unary rounds cannot reuse its
   rows.
3. The standalone source needed an explicit input convention. The corrected
   form takes an ordered screened list of at most \(E\) canonical unit pairs.
   The uniform form starts on F130's no-factor branch.
4. The private-row splice needed one common union row space, and the
   global-root warning needed the exact P119/F131 citation.

The corrected branch order is: run the endpoint sign screens; retain a new
exact value; otherwise discard the decoder- and refinement-inert duplicate.

This file preserves the failed audit. A corrected candidate still needs a
fresh hostile audit and a blind reconstruction.
