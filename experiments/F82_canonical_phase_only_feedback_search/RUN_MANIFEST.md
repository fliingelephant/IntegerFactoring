# F82-D01 preregistration

- Family: F26, canonical feedback and integer refinement.
- Run: F82-D01.
- Status: completed with exit status 0.
- Source: scripts/F82_D01_search.py.
- Runner: run_F82_D01.sh.
- Command from the workspace root:
  zsh experiments/F82_canonical_phase_only_feedback_search/run_F82_D01.sh.
- Declared timeout: 120 seconds, enforced by
  /opt/homebrew/bin/timeout 120s.
- Runtime: /opt/homebrew/bin/python3.
- Log: logs/F82-D01.log.
- Output: output/F82-D01.json.

## Closest prior route and material difference

The closest results are P78/P81, which give an integer feedback refinement
whose new block has unequal hidden local orders, and F81's abstract
phase-only model, in which equal local orders make every pure power fail.
This run searches for the missing bridge: a literal canonical-integer
refinement witness in the equal-order phase branch.

## Exact finite question

Enumerate distinct odd primes \(5\le p<q\le149\), in increasing
\(N=pq\), and public bases \(2\le a\le64\). Retain only bases with one
common local order

\[
\operatorname{ord}_p(a)=\operatorname{ord}_q(a)\ge3.
\]

For each old exponent \(i\), form the two public canonical inverse relations
with endpoint list

\[
a,\ [a^{-1}]_N,\ [a^i]_N,\ [a^{-i}]_N.
\]

Retain only lists of four distinct integers greater than one that are
pairwise coprime. Their gcd-free block subgroup is then exactly
\(\langle a\rangle\), and it has no direct sign separator.

For each later public canonical-residue word

\[
g=[a^e]_N,
\qquad
w=[a^{-e}]_N,
\]

exclude old endpoints, equal endpoints, and any immediate direct-sign or
endpoint-difference factor. Append \(g,w\), and search for a proper integer
gcd overlap \(d\) between one old endpoint and one new endpoint. Require
that \(d\) remains one gcd-free block against every other endpoint, is a
unit modulo \(N\), lies outside \(\langle a\rangle\), and has equal local
orders:

\[
\operatorname{ord}_p(d)=\operatorname{ord}_q(d).
\]

Finally, exhaust the finite mixed subgroup

\[
d^s a^t\bmod N
\]

for a direct sign separator. Preserve the first witness in the declared
enumeration order.

## Decision rule and scope

- A witness proves only that literal canonical integer feedback can enter
  the phase branch: the new block enlarges the usable subgroup, every pure
  power of that block is synchronized, but a mixed old/new word factors.
- A null kills only the declared prime, base, and two-relation search box.
- Hidden factors and local orders are discovery labels. The preserved
  certificate must later be re-expressed as a public execution with a
  factor-based proof of why it works.
- The run cannot prove frequency, an all-input law, a complexity lower
  bound, or a factoring algorithm.

Preregistered source SHA-256:
9dadc2e68a364a2722fe972948dd4d6bf8af3ed3877e6f95b86588c4316b8bd4.

Preregistered runner SHA-256:
74306812914097b5e978b0fad70abf8474328d7f3484c4d6c80d214d84211c02.

## Outcome

The run completed before the timeout and preserved the first declared
witness:

\[
N=703=19\cdot37,\qquad a=41,\qquad d=3.
\]

The old canonical endpoint list is

\[
41,\ 583,\ 27,\ 677.
\]

The feedback word and inverse are \(363\) and \(428\). The overlap
\(\gcd(27,363)=3\) exposes the equal-local-order block. The mixed residue is

\[
3\cdot41^5\bmod703=482,
\qquad
\gcd(482-1,703)=37.
\]

This remains finite discovery evidence. Its old endpoint \(27=3^3\), so
exact perfect-power extraction can expose \(3\) before feedback. F82-D02
preserves this limitation and adds a predeclared filter that removes it.

- Source SHA-256:
  9dadc2e68a364a2722fe972948dd4d6bf8af3ed3877e6f95b86588c4316b8bd4.
- Runner SHA-256:
  74306812914097b5e978b0fad70abf8474328d7f3484c4d6c80d214d84211c02.
- Log SHA-256:
  3b204218f5e3b2a81bf11b14a98cd3f394212a96663dd736e57c8d2a3e5468a8.
- Output SHA-256:
  3b204218f5e3b2a81bf11b14a98cd3f394212a96663dd736e57c8d2a3e5468a8.
