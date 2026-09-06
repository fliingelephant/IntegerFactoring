# F225 provenance

The root agent assigned the large-gap fixed-shift complement after F224.
The requested channel was

\[
H_N(x)=(x+1)^N-x^N-1\pmod N
\]

with fixed shift `1`, a fresh uniform point, and an individual proper gcd.

The proof was derived from the hidden-prime identity

\[
q=2p-c.
\]

This identity yields the reciprocal polynomial modulo `p` and the
quadratic-character partition modulo `q`.  The hostile family reuses the
same Baker--Harman--Pintz prime-in-short-interval theorem already cited and
audited in F222/P193.

No numerical result is part of the candidate.  An optional small local
check was attempted only after inspecting load and memory pressure.  It
stopped immediately because `/opt/homebrew/bin/python3` did not contain
SymPy.  No alternate numerical workflow was substituted.

No durable ledger was edited.
