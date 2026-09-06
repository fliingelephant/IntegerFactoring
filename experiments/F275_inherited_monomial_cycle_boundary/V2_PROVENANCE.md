# F275 V2 provenance

## Immutable V1 base

| V1 artifact | SHA-256 |
|---|---|
| `STATEMENT.md` | `4fa048b441cbb9e6177e3577ebbdd910d5e6555b5ee904ff7a184a2eecbbaa34` |
| `PROOF.md` | `d5d1990b1e3fa4cf5e4d4e6efa1cfc02690576e761aa136e8f59afb6df836447` |
| `SELF_AUDIT.md` | `727c9019fc1349f210613ae6c162a06b6be0db0e966c8bde291de2fa794ce830` |
| `PROVENANCE.md` | `91ebdffb0bbabe66cc8a8cc0c69f4c2ab633a9e5fdc88cd44ec490e2224fcb9c` |
| `MANIFEST.md` | `913e16c59a589a2f24e07429a1371a64635c5656d488b3314f9010b32f31e2b7` |
| `FROZEN.sha256` | `6c3cebe4f34bdb439dabb9cc50990bb68d0250ae552ea5087dd4e57dc057aa9d` |

Every V1 byte remains unchanged.

## Triggering hostile audit

The fresh V1 hostile audit is preserved at SHA-256

`a839f1bd62ca2671882c6dba0270de9f901aad9f0d52e2de888f38ca196743a2`.

Its verdict was `FAIL` because V1 claimed `dT_y(d)<N^2` while construction
(8) allowed an arbitrary positive unit carrier `d`. Its exact counterexample
was `N=3`, `d=10`, `y=1`, for which `T_y(d)=1` and `A=10>9`.

The audit passed Theorem A, Theorem B, and the reduced-complement/F270 scope
boundary. It stated that requiring `1<=d<N` in construction (8) repairs the
sole blocker.

## V2 delta

V2 adds exactly that canonical-carrier hypothesis to construction (8) and
proves the corrected bound `(N-1)^2<N^2`. The general graph carriers remain
arbitrary positive units. No theorem, formula, or exclusion changes.

V2 has no author self-audit. Fresh hostile and statement-only audits are
required before promotion.

