# F232-D01 V2 hostile pre-run audit

## Verdict

**FAIL before execution.**  Do not run the V2 packet.  No mathematical run
occurred.

## Freeze failure

The preregistered symbolic hashes did not match the bytes presented for V2:

```text
STATEMENT frozen 90265a37... actual 0af99315...
PROOF     frozen 981a0353... actual 7e096bc2...
```

## Additional implementation and registration objections

1. Direct rows overwrote the formula-(11) probability labels with `1`.
   The exact projected-stage probability and the separate deterministic
   direct-factor event need different fields.
2. The hostile rankings excluded all direct rows, but the registration
   specified rankings over each complete split.
3. Corpus generation and Pollard factorization shared one global random
   stream.  The claimed `N`-only public builder therefore had hidden global
   state advanced by the factor-assisted corpus construction.  A corrected
   source must use a separate deterministic factorization stream derived
   only from the public child value, or otherwise isolate and declare it.
4. The expression `p |= 1` did not sample uniformly from odd candidates in
   the declared closed interval: an endpoint could receive a different
   weight.

The audit did not refute the core shifted-child gcd identities or the exact
projected return formula.  V1 and V2 remain failed pre-run packets.  Any V3
must receive fresh hashes and a fresh hostile pre-run audit.

