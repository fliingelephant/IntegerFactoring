# F236 follow-up preregistration: multiplier-centered carry

Use the same complete finite domain as `PREREG.md`.  For every integer
`1<=u<=n`, define the centered residues

\[
x_u=up-K_pB,\qquad y_u=uq-K_qB,
\]

where `K_p=floor(up/B+1/2)` and `K_q=floor(uq/B+1/2)`; ties cannot occur
because `p,q` are odd and `B` is a power of two.  Then

\[
c_u=(x_uy_u-u^2)/B
\]

is an integer.  Check exact divisibility and abort on failure.

Freeze these outputs:

- the maximum over inputs of `min_{1<=u<=n}|c_u|`;
- that maximum by bit length;
- every record-setting pair;
- the ten worst pairs, with the minimizing multiplier and the complete
  list `|c_u|`;
- the number of inputs for which the best carry is at most `n,n^2,n^3,n^4`.

This tests whether a polynomial numerical multiplier menu gives a short
true-carry list.  It is evidence only.

