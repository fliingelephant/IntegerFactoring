# F216-D01 preregistration — dyadic trace saturation

## Frozen question

For odd `N` and `t >= 5`, define the public dyadic trace image

\[
W_t(N)=\{u+Nu^{-1}\pmod {2^t}:u\in U(2^t)\}.
\]

Test the exact conjecture that this image has constant density. It must not
shrink by one bit per dyadic lift. Let `d` be the element of `{1,3,5,7}`
congruent to `N` modulo `8`. Since `N/d` is a square in `U(2^t)`, let `a`
be the public bit-lifted square root with `a^2 d = N (mod 2^t)`.

The frozen predictions are

\[
a^{-1}W_t(N)=W_t(d),
\]

and, for representative square classes,

\[
W_t(3)=\{s:s=4\pmod 8\},\qquad
W_t(7)=\{s:s=0\pmod 8\},
\]

\[
W_t(5)=\{s:s=6\text{ or }26\pmod {32}\}.
\]

For `d=1`, the predicted cardinality is

\[
|W_t(1)|=
\begin{cases}
(2^{t-4}+8)/3,&t\text{ even},\\
(2^{t-4}+10)/3,&t\text{ odd}.
\end{cases}
\]

The formula is tested only in its stated range `t >= 5`; the even formula
starts at `t=6`.

## Train and holdout

- Training rows: the four representatives `d in {1,3,5,7}` for
  `5 <= t <= 14` (with the stated range restriction for `d=1`).
- Formula holdout: the same representatives for `15 <= t <= 18`.
- Square-class holdout: 32 deterministic seeded odd 40-bit integers at
  `t in {8,12,16}`. Only `N` and `t` are used to form the image and the
  normalizing root.
- Factor-trace holdout: 16 deterministic seeded balanced semiprimes with
  16-bit prime factors. Their hidden factor traces are used only as labels
  to check membership, never as construction features.

## Acceptance and rejection

Accept the exact conjecture only if every set equality, cardinality formula,
square-class normalization, and factor-trace membership check passes.

Also test the weaker saturation claim

\[
|W_t(N)|/2^t\ge 1/64
\]

on every row with `t >= 8`. Reject saturation if any such row violates it.

This is finite evidence only. The intended mathematical output is an exact
proof or a counterexample. The experiment cannot prove a complexity lower
bound for a decoder that retains the reciprocal parameter `u`.

## Resources

Run one Python process. Expected wall time is below 60 seconds. Expected
peak memory is below 128 MiB. The remote host was inspected first: it has 32
logical CPUs, 503 GiB RAM, 367 GiB available memory, and 22 GiB free disk.
Its load average exceeded the logical CPU count, so this run stays single
process and uses only `t <= 18`.

