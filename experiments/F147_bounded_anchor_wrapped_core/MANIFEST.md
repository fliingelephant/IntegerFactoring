# F147 manifest — bounded-anchor wrapped-core candidate

## Preserved V1 history

- `STATEMENT.md`: frozen V1 candidate.  SHA-256
  `2fc9e36eac6754ffe0405d017d9a58829f95965fbdde94b7ce0f060e4309c204`.
- `PROOF.md`: frozen proof.  SHA-256
  `6868737e521dcaa64473bc105d9fa85e1458947b5aa312bc98f3771e141577ad`.
- `HOSTILE_AUDIT.md`: V1 hostile audit with verdict PASS.  SHA-256
  `ba28d4ceee58a7262d83137328dceeeb8c0dd868a87a142cbda26d444968c122`.
- `BLIND_RECONSTRUCTION.md`: fresh statement-only reconstruction with
  verdict FAIL.  SHA-256
  `250f65f99b61d5c3ab822aa1049cc53c266c888872f05c77a3d582b59a86ee0b`.

The failed reconstruction found one false sentence around V1 equation (12).
An upper bound `a_e <= H` makes

\[
L>\frac{\log N}{2\log H}
\]

a necessary condition for a wrapped length-`L` cycle.  It does not make the
condition sufficient and does not show that the P131 scale can be reached.
The reconstruction's `N=81`, `H=3` example refutes the V1 wording.

## V2 repair

- `V2_STATEMENT.md`: corrected statement.  SHA-256
  `a65034746ef11b0165ee4c0591c68107997e14d7234df1a4c1a45482b905d87b`.
- `PROOF.md`: reused unchanged with SHA-256
  `6868737e521dcaa64473bc105d9fa85e1458947b5aa312bc98f3771e141577ad`.

V2 replaces the false reachability sentence with the strict necessary
implication

\[
\sqrt N<\prod_{e=1}^{L}a_e\le H^L
\quad\Longrightarrow\quad
L>\frac{\log N}{2\log H}.
\]

It also restores the missing closing display delimiter after equation (11).
No `V2_PROOF.md` is needed: the frozen proof never used the false converse,
and its final scope already says that reaching the magnitude condition does
not supply any missing arithmetic condition.

## Current status

V2 passed a fresh hostile re-audit and a fresh statement-only blind
reconstruction.  It is promoted as P136.

- `V2_HOSTILE_REAUDIT.md`: SHA-256
  `e5deb09c9b3e8874658a999fbb4f7e86204c59dc4eeb3e22c6f01e19495bdf69`.
- `V2_BLIND_RECONSTRUCTION.md`: SHA-256
  `e61406b24486ff77e4b5a3f5ec7394c5a6ec9c1c1b2eb5869bc7b55ab8a6e296`.

F147 has no computation, cross-family audit, human audit, or literature
review.  It does not claim an all-input cycle, dependency, non-global root,
or factoring algorithm.  Its claimed increment remains the exact large-core
reduction and quasipolynomial complete decoder for bounded raw anchors.
