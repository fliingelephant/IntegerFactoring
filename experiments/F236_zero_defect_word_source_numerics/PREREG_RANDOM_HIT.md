# F236 follow-up preregistration: uniform-multiplier hit probability

Use the same finite domain and the hidden nearest-center carries `c_u`.
Freeze the horizon `U=n^3` and thresholds `C=n,n^2,n^3`.  For each input
compute the exact hit fraction

\[
U^{-1}\#\{1\le u\le U:|c_u|\le C\}.
\]

Freeze these outputs:

- the minimum hit fraction for each threshold;
- the minimum hit fraction by bit length;
- every record-setting input;
- the ten lowest fractions for `C=n`.

This directly tests an inverse-polynomial Las Vegas source after the hidden
center indices and carry are enumerated for the sampled multiplier.  It is
evidence only.

