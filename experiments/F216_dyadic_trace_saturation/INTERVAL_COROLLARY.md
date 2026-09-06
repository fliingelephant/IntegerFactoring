# F216 interval corollary — arbitrarily deep dyadic traces leave a dense Archimedean frontier

This corollary uses the frozen F216 theorem without modifying it.

Let `N` be odd and `t >= 7`. Every dyadic trace image `W_t(N)` contains a
complete ordinary arithmetic progression of modulus `128`. More precisely,
use the public normalization

\[
N\equiv da^2\pmod {2^t},
\qquad d\in\{1,3,5,7\}.
\]

Then:

- if `d=1`, `W_t(N)` contains both classes `82a` and `-82a modulo 128`;
- if `d=3`, it contains every integer `4 modulo 8`;
- if `d=5`, it contains both classes `6a` and `-6a modulo 32`;
- if `d=7`, it contains every integer `0 modulo 8`.

The first claim is the `b=2` stratum in the exact F216 description:

\[
2+2^4w\equiv82\pmod {128}
\qquad(w\equiv5\pmod8),
\]

together with its negative. Multiplication by the odd unit `a` permutes the
lifts of a class modulo `128`. The other three claims follow directly from
the representative images and the normalization identity.

Consequently, for every interval `I` of `L` consecutive ordinary integers,

\[
\boxed{
|\{s\in I:s\bmod2^t\in W_t(N)\}|
\ge \lfloor L/128\rfloor.}
\]

This bound is independent of `t`. In particular, on the public balanced
trace interval

\[
2\sqrt N < s < \frac{3}{\sqrt2}\sqrt N,
\]

whose length is

\[
\left(\frac3{\sqrt2}-2\right)\sqrt N+O(1),
\]

an arbitrarily deep power-of-two trace condition leaves `Omega(sqrt(N))`
ordinary candidates.

Thus dyadic trace lifting does not merely fail to produce a QP-size global
residue list. It also fails to thin the balanced Archimedean trace interval
by more than a constant factor. This remains a pruning theorem only. It is
not a lower bound against an implicit exact-square finder on the surviving
progression.

