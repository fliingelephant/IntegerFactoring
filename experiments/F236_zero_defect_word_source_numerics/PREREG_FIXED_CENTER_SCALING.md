# F236 follow-up preregistration: fixed-center multiplier scaling

Use the same complete finite domain as `PREREG.md`.  For each integer
`1<=u<=n^3`, set the one public center

\[
K_u=\left\lfloor {uH\over B}+{1\over2}\right\rfloor,
\]

where `H=(N-1)/B`, and put

\[
c_u={(up-K_uB)(uq-K_uB)-u^2\over B}.
\]

Check exact divisibility.  Freeze the same caps `n,n^2,n^3` and report the
maximum of `min |c_u|` for each cap, by bit length, all records, and the ten
worst cubic-cap inputs.

This tests whether a fully public single center retains the favorable
multiplier effect.  It is evidence only.

