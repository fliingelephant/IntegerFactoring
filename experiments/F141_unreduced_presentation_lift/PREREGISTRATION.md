# F141-D01 preregistration — unreduced-presentation lift discovery

## Closest prior and material difference

P118/F130 keeps one canonical value \(cw\) for each first residue
\(c=[U]_N\).  P120 and X73 show that changing an endpoint presentation can
change a direct screen or later named blocks, but a duplicate canonical
value is decoder-inert.  P123/X75 shows that feeding a complete reciprocal
endpoint returns the old exact value and that row width does not force a
kernel.

This experiment changes the retained parity column itself.  For every frozen
word position it keeps \(Uw\), represented by the known exponent vector of
\(U\) and the canonical endpoint \(w\).  It therefore does not apply
same-residue deletion to lifted positions.  It does not feed \(U\) as a new
named endpoint.

## Frozen verifier and timeout

- Source: `search.py`.
- Timeout: 300 seconds.
- Authoritative log: `RUN.log`.
- Machine-readable output: `OUTPUT.json`.
- Command:

```text
env DOT_SAGE=/private/tmp/f141_sage_state gtimeout 300 sage -python experiments/F141_unreduced_presentation_lift/search.py
```

The source SHA-256 is recorded in the output and manifest after the run.
Python/Sage proof arithmetic is used for all fixed-certificate primality
checks.  Hidden factors are used only to certify normalized roots and to
label the finite corpus.

The first registered attempt used Sage's default user cache and failed before
the source ran because the sandbox denied that cache write.  Its log is
preserved as `RUN_FAILED_SANDBOX.log`.  The corrected command changes only
the cache directory.  It does not change the source, corpus, or decision
rule.

## Fixed large order-collision certificate

The script must verify

```text
p = 1238926361552897
q = 5704689200685129054721
N = p*q
m = 256
U1 = 2
U2 = 2^(2*m+1) = 2^513
c1 = c2 = 2
w = (N+1)/2
```

It must check all of the following.

1. \(p,q\) are prime, \(p\mid 2^m+1\), and \(q\mid2^m-1\).
2. With the literal F130 parameters of this \(N\), both factors exceed the
   complete initial seed bound \(E+1\), the named block \(2\) is present if
   the first frozen stage is reached, and exponents \(1,513\) are allowed.
3. The two positions have residue \(2\), canonical inverse \(w\), and both
   endpoint sign screens are one.
4. Canonical residue deletion keeps only \(2w=N+1\), and this integer is not
   a square.  Hence the matched one-column canonical decoder has zero kernel.
5. The two lifted values have equal parity columns and their product is
   \((2^{m+1}w)^2\).
6. The normalized root is \(2^m\bmod N\), and its two terminal gcds are
   exactly \(p,q\).

This fixed item is a same-residue bounded-order collision.  It is a baseline
source-expansion certificate, not evidence for a new order-finding method.
The complete canonical F130 source is not claimed to fail on this input.

## Frozen small-corpus discovery

The script scans, in lexicographic order, every semiprime \(N=pq\) with
distinct primes

\[
7\le p<q\le199.
\]

For each input it uses the fixed base \(2\) and the word positions

\[
U_e=2^e,\qquad1\le e\le24.
\]

An input is called slice-direct-null only when every distinct residue in
this menu has both canonical endpoint sign gcds non-proper.  The canonical
ledger keeps the first exact value after residue deletion and then exact
value deletion.  The lifted ledger keeps the first exact lifted value at
every word position and does not delete positions only because their
residues agree.

For both ledgers, the script constructs the exact prime-parity matrix, a full
binary kernel basis, and the normalized root of every basis vector.  Trial
factorization is permitted only because this is a fixed small offline corpus;
the theorem candidate must use factor-free refinement instead.

For every slice-direct-null input the output records whether:

1. the canonical normalized-root image is global;
2. the lifted normalized-root image is non-global;
3. a useful equal-parity pair uses the same residue;
4. a useful dependency of weight one exists; or
5. a useful dependency of weight two or three exists and all selected
   residues are distinct.  For this last category, the selected columns must
   form a binary circuit: every selected column is nonsquare and no proper
   nonempty subset is a dependency.

The scan is exhaustive over the declared corpus and menu.  It does not stop
at the first witness.  It records the first lexicographic witness in each
category and aggregate counts.  A missing all-distinct witness is only a
finite null result for this corpus.

The first completed source version did not impose the circuit condition in
item 5.  Its first reported all-distinct pair at `N=4033` consisted of two
individually square columns, so it did not show cross-relation closure.  That
valid but weaker output and log are preserved as `OUTPUT_V1.json` and
`RUN_V1.log`.  The corrected source adds only the preregistered minimality
test and extra witness labels; it does not change the corpus, menu, or other
categories.

## Decision rule

A precise candidate survives if the algebra proves either a strict source
expansion or a decoder equivalence, and the registered computation verifies
the fixed certificate.  Any discovered all-distinct witness is reported
separately from same-residue/order collisions.  No all-input factoring or
success-density claim is permitted.
