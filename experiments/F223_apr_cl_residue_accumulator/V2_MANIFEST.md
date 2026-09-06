# F223 V2 manifest

## Frozen self-audited V2 candidate

- `V2_STATEMENT.md`:
  `a5d38c57213a9c237723e2ea916ee2865f81cc8b086287728d493a07ebf2334c`
- `V2_PROOF.md`:
  `290af2762069471b625442a851fd56b9e65d2db8964ee50ae3ab4a3832ea0e5a`
- `V2_SELF_AUDIT.md`:
  `44e9d36889b7ac58c3cf2ff95ec560bd84b16b7daa1bc21df63536582a1dcdbb`
- `V2_PROVENANCE.md`:
  `3b6dc93067e5f8a53ec641e686a210c9586fa0cba40367c310381ad28557a790`

## Reused post-hoc exact witness reconstruction

- `verify_witness.py`:
  `d5eb0a272319d1d1dbd9314277464f39368f4e3d634d4de66b8ef82a17947c3f`
- `POSTHOC_OUTPUT.json`:
  `8a352422599c9fb24d6344bcd0e28c77e8697fbb94197d5d8e368b30080de5fa`

These two V1 witness artifacts are unchanged. The reconstruction was not
preregistered. No remote scan artifact is present or hashed.

## Preserved failed audit

- `HOSTILE_AUDIT.md`:
  `ace81606d7d93a6f400431a9fb35094567cb730055f241541ab8bb40cdbc42cd`

V1 and its hostile FAIL remain frozen. Their complete identities are in
`V2_PROVENANCE.md`.

## Status

The V2 packet is self-audited only. No hostile re-audit, blind
reconstruction, independent numerical replay, human audit, or
durable-ledger promotion has run.
