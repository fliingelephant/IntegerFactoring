# F265-D07 draft algebra amendment: peeled elliptic cubic-row kernel

## Status and authenticated composition

This is an unfrozen theory-only amendment. It has not received a hostile
audit. There is no D07 source, runner, manifest, compilation, preflight,
freeze, local execution, remote execution, or cohort result.

D07 imports exactly these immutable draft bytes:

| imported artifact | SHA-256 |
|---|---|
| `D05_DRAFT_ALGEBRA.md` | `e3cbefeb597f263501d327f15f9dd4c7b78ee37d37178135ab1c0a5ff73e9fd3` |
| `D06_DRAFT_ALGEBRA.md` | `e79ea109a9cd8141dd27c4fc99cc7ec2957c454619b0e015802ab4eff5c45f74` |

The transitive implementation origin is also authenticated directly:

| D02 artifact | SHA-256 |
|---|---|
| `../F265_elliptic_cubic_lift_symbolic_search_v2/FROZEN.sha256` | `26f7940244242edc549a2612fc08120372e0f8fab64a2dca154b69ed02d55d6a` |
| `../F265_elliptic_cubic_lift_symbolic_search_v2/ALGEBRA.md` | `d20b5271bb4441fe7d280e35e09a73ff5b0142abf2ed6d3e9839fe22ff4914c4` |
| `../F265_elliptic_cubic_lift_symbolic_search_v2/PREREGISTRATION.md` | `8e3c90420014939ba3ae58490bac2e85fc0a7a45523e12d332cadb5e1f6b384f` |
| `../F265_elliptic_cubic_lift_symbolic_search_v2/search.cpp` | `eeceba4db014346cc78dae3cbae29a65fb32946163becc5d9f5617fc465a7957` |

The normative D07 algebra is the exact D05 algebra, followed by every
explicit D06 replacement, followed by the two replacements below. There is
no token rebinding, version-name substitution, or unnamed import. A later
standalone packet must materialize that resolved text and authenticate all
three inputs before source is written.

## 1. Closed public-factor boundary

Replace D06 Algebra Section 2's informal list of public factor events by the
closed production enumeration and byte schema in D07 Preregistration
Sections 2 and 3. In particular, the signed-`x` exceptional branch of affine
addition is reachable production behavior. Its proper gcd has class
`FACTOR_X_SIGN`; it is not absorbed into `AFFINE_DENOMINATOR` and cannot be
omitted from the factor journal, fixtures, packet cap, or null quantifier.

Every public factor event is still only a verified `g` with

\[
 1<g<N,\qquad g\mid N.
\]

The factor class describes the production call site. It does not change the
factor certificate or feed `g` back into any later computation.

## 2. Exact mathematical scope

The D05 saturated private-primary theorem, simultaneous fixed-point peel,
kernel isomorphism, support-at-most-two criterion, and normalized-root
homomorphism are unchanged. D07 makes no source theorem. It does not prove
that an elliptic bank has a private pivot, that the residual core is small,
that a useful relation occurs, or that any finite frequency extends to
unbounded inputs.

The peel is only a source-agnostic decoder optimization and a finite-source
opening. D07 closes experiment semantics and resource accounting. It adds no
all-input factoring claim.

## 3. Authorization boundary

A fresh no-context hostile theory audit must reconstruct the imported D05
and D06 bytes and the D07 replacements. A pass authorizes only preparation
of a standalone resolved draft. It does not authorize source, freezing,
compilation, preflight, or execution.
