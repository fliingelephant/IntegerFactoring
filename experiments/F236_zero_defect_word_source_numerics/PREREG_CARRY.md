# F236 follow-up preregistration: centered quotient carry

Use the same complete finite domain as `PREREG.md`.

For each pair choose `K=1` when `q<2B`, and `K=2` otherwise.  Put

\[
x=|p-KB|,\qquad y=|q-KB|.
\]

Both are in `(0,B)`.  If the factors are on the same side of `KB`, define
`c=(xy-1)/B`; if they are on opposite sides, define `c=(xy+1)/B`.
Check the division exactly and abort if `0<=c<B` fails.

Freeze the following outputs before computation:

- the maximum of `c/B`, with every record-setting pair;
- the maximum carry bit length by input bit length;
- the counts with `c<=n`, `c<=n^2`, `c<=n^3`, and `c<=n^4`;
- the ten largest carries, ordered by `c/B` and then by `N`;
- a direct check that the candidate trace formula
  `K(p+q)=K^2 B+H-c` on the same-side branch and
  `K(p+q)=K^2 B+H+c` on the opposite-side branch holds.

This follow-up tests whether the new carry parameter is uniformly small.
It does not change any word menu from the first scan.

