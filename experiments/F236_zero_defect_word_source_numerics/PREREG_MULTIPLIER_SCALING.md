# F236 follow-up preregistration: multiplier-menu scaling

Use the same complete finite domain as `PREREG.md` and the centered
multiplier carry from `PREREG_MULTIPLIER_CARRY.md`.

Freeze the caps

\[
U\in\{n,n^2,n^3\}.
\]

For each input and cap compute `min_{1<=u<=U}|c_u|`.  Freeze these outputs:

- the maximum of that minimum for each cap;
- each maximum by input bit length;
- every record-setting pair for each cap;
- the ten worst pairs for the `n^3` cap.

The loop uses direct integer arithmetic.  This is evidence only.

