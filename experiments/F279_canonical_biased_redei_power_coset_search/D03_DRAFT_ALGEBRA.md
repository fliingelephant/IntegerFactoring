# F279-D03 additive algebra repair — canonical biased Rédei power-coset sources

## Status, ancestry, and merge rule

F279-D03 is an unfrozen theory-only repair. It authorizes no source, runner,
fixture, tape, freeze, compile, benchmark, experiment, remote access,
private-label access, ledger change, git staging, or commit.

The immutable predecessors are:

```text
DRAFT_ALGEBRA.md
328c8c26d5c06e3033300539fd5900f7ddcb55f253b75fae851c58db47eea424

DRAFT_PREREGISTRATION.md
4498a4f3e2404297d6eda58036fc45e097915a13d73077dc9511dea4e6cb7e7e

D02_DRAFT_ALGEBRA.md
f87f787bad0943b7149d276e158d28a6350dc8ab72836e80112acf33240cf843

D02_DRAFT_PREREGISTRATION.md
93e207fb2e3e4c489eb009f56e16751b3df79d7ecc329b602a678761795533f9
```

Read this file with `D02_DRAFT_ALGEBRA.md`. This file supersedes only the
affine-chart conjugation sentence in D02 Section 5 and the probability
conditioning sentence in D02 Section 9. Every other D02 algebra statement,
constant, sign, residual exponent, finite-decoy boundary, and nonclaim is
unchanged.

## 1. Explicit affine-chart conjugation

Let

\[
C=\begin{pmatrix}a&b\\c&d\end{pmatrix}
\]

be on the clean upper-left-coordinate branch. D02 gives
`H=-bc`. Since `H` is a unit modulo the square-free modulus `N`, both `b`
and `c` are units. Put

\[
D=\operatorname{diag}(b,1).
\]

The intended direction and equality are exactly

\[
\boxed{
D^{-1}CD
=
\begin{pmatrix}a&1\\bc&d\end{pmatrix}
=
\begin{pmatrix}
(t-v)/2&1\\
(\eta-v^2)/4&(t+v)/2
\end{pmatrix}.}
\tag{D03.1}
\]

Here `t=a+d`, `v=d-a`, and
`eta=(a-d)^2+4bc`, so

\[
bc={\eta-v^2\over4}.
\]

For every integer `k>=0`,

\[
(D^{-1}CD)^k=D^{-1}C^kD.
\tag{D03.2}
\]

Because `D` is diagonal, equation (D03.2) gives

\[
\bigl((D^{-1}CD)^k\bigr)_{11}=(C^k)_{11}.
\tag{D03.3}
\]

Thus the normalized chart preserves the literal upper-left power
coordinate. No use of `DCD^{-1}` is intended.

## 2. Exact probability conditioning for ExactTape256

Fix all public fixture bytes, every modulus, the grammar, and the set `I`
of controls whose sources reach the D03 control-eligible state. Randomness
in this section is only the declared ExactTape256 product measure.

For one control `i` in `I`, let `X_i` be its three assigned 256-bit blocks.
The block triples `X_i` are mutually independent. Let `A_i` be the event
that at least one of the three attempts assigned to `i` passes the modulo,
vector, and clean-target tests. The accepted target is the first passing
attempt in attempt order.

Each accepted attempt is uniform on the clean vectors. Therefore, for each
fixed `i`, conditional on `A_i`, the first accepted target induces the
uniform clean projective target modulo each hidden prime. Its two CRT-local
projective targets are independent. The local endpoint hit law remains

\[
\Pr(z_r^B=\lambda_r\mid A_i)
={1\over r-\chi_r}.
\tag{D03.4}
\]

Let

\[
A_{\rm ctrl}=\bigcap_{i\in I}A_i.
\tag{D03.5}
\]

Because each `A_i` depends only on the disjoint block triple `X_i`,
conditioning on `A_ctrl` preserves the product of the control-local
conditional laws. Thus the accepted controls are mutually independent and
projective-uniform conditional on `A_ctrl`.

This is the full probability claim. D03 does not condition that claim on
`phase_success`, `packet_success`, a deadline, a resource gate, a replay
result, a checksum result, or any other runtime event. Such events can
depend on which attempts pass and on the resulting byte paths. D03 proves
no independence between them and the tape.

## 3. Preserved mathematical boundary

D03 changes no endpoint identity, Cayley sign, local residual exponent,
projective rejection law, finite relation box, target grammar, or
high-order statement from D02. In particular, the finite evidence label is
still only `box_unexplained_exclusive`. It is not an exhaustive relation or
Miller classification.

D03 proves no inverse-quasipolynomial hit law, all-input dispatcher,
all-input factoring theorem, deterministic-target sparsity theorem, or
physical-entropy claim. The operational repair is specified separately in
`D03_DRAFT_PREREGISTRATION.md`.
