# F236 follow-up preregistration: first small-carry hit density

Use the same complete finite domain and two hidden nearest centers from
`PREREG_MULTIPLIER_CARRY.md`.  Freeze thresholds

\[
C\in\{1,n,n^2,n^3\}
\]

and the multiplier horizon `1<=u<=n^3`.  For each threshold record the first
`u` with `|c_u|<=C`, or no hit.  Freeze these outputs:

- hit counts and maximum first-hit index;
- maximum first-hit index by input bit length;
- the ten latest hits for each threshold;
- counts of `u` hits for the worst input at each threshold.

This tests inverse-polynomial hit density after the hidden center pair is
enumerated.  It is evidence only.

