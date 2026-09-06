# F275 manifest — proof-only monomial and cycle boundary

## Status

F275 is a proof-only candidate with an author self-audit. Fresh hostile and
statement-only audits are pending. It is not promoted.

No source code, checker, compilation, numerical search, benchmark, corpus,
remote run, empirical claim, or durable-ledger edit belongs to this packet.

## Frozen mathematical artifacts

| File | SHA-256 | Role |
|---|---|---|
| `STATEMENT.md` | `4fa048b441cbb9e6177e3577ebbdd910d5e6555b5ee904ff7a184a2eecbbaa34` | Normative theorem and scope |
| `PROOF.md` | `d5d1990b1e3fa4cf5e4d4e6efa1cfc02690576e761aa136e8f59afb6df836447` | Self-contained proofs |
| `SELF_AUDIT.md` | `727c9019fc1349f210613ae6c162a06b6be0db0e966c8bde291de2fa794ce830` | Author claim and boundary audit |
| `PROVENANCE.md` | `91ebdffb0bbabe66cc8a8cc0c69f4c2ab633a9e5fdc88cd44ec490e2224fcb9c` | Prior boundaries and search disposition |

These four hashes freeze the mathematical content. `FROZEN.sha256` also
records the hash of this manifest.

## Exact claims

1. Every exact square relation among positive inherited monomial rows pulls
   back through the exponent-incidence matrix to an old exact square-class
   relation.
2. Its normalized root is the old normalized root times one global sign.
3. A structural incidence relation therefore has a global normalized root.
4. An independently supplied root either differs by a global sign or gives
   an immediate signed-root factor.
5. For a simple even inverse-square cycle, the normalized root equals the
   alternating edge-label ratio and its two relation gcds equal the two
   alternating-label gcds.
6. An unreduced complement product is inside the monomial theorem. Its
   canonical reduction modulo `N^2` is a deterministic correlated principal
   lift outside both that theorem and the F268/F270 `t=0` row grammar.

## Exact exclusions

F275 proves no general canonical-section obstruction, odd-cycle
classification, graph-carrier kernel classification, numerical
private-pivot theorem, event probability, runtime law, or factoring
algorithm. It does not evaluate F270 and does not authorize a new
reduced-complement search.

Any mathematical change requires a new packet version, new hashes, and fresh
audits.

