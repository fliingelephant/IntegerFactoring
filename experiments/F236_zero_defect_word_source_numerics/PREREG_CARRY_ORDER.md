# F236 follow-up preregistration: centered-carry meta-order

Use the same complete finite domain as `PREREG.md` and the correct `K` and
centered carry from `PREREG_CARRY.md`.  Define the public integer

\[
A_K=K(N+1)-K^2B-H>0.
\]

The trace identity predicts

\[
A_K\equiv-c\pmod{s_p,s_q}
\]

on the same-side branch and

\[
A_K\equiv c\pmod{s_p,s_q}
\]

on the opposite-side branch.  Check these congruences exactly and abort on
failure.

Remove from each residual every primary part supported on `A_K`.  On the
remaining coprime parts, compute the exact multiplicative orders of `A_K`.
Freeze these outputs:

- the maximum of the smaller carry meta-order;
- the maximum of the smaller residual left by
  `product_{1<=j<=n}(A_K^j-1)`;
- every record-setting pair for either value;
- the ten worst pairs under the carry meta-order word.

This tests a new word family.  It does not alter the earlier frozen menus.
