# F149 hostile audit — FAIL

## Verdict

**FAIL.**  The main canonicalization, singleton criterion, semiprime count,
uniform fixed-center union bound, and finite certificate are correct.  The
frozen statement nevertheless contains one false unqualified claim in its
self-containment section.  A corrected statement needs a fresh audit.

## Frozen inputs

- `STATEMENT.md` SHA-256:
  `25af29ad09343eef88d7652f988b4ebd2f982e0d17ec6a0de867982c7e660738`;
- `PROOF.md` SHA-256:
  `08cd204330f47429f20e747a1c8bad9a7084ec5de9249a8e5e755f55e305da0e`;
- pre-audit `MANIFEST.md` SHA-256:
  `aadc3231ebb95e41e5550345cabb2600198ebb944d9dc80787d89ca92795ae69`.

The manifest hashes of the frozen statement and proof agree with the files.
I read the full statement, proof, and manifest.  I also checked the stated
scope against P71, P114, and P128--P131.

## Fatal issue: the self-loop multiple can be zero

Statement Section 4 claims, without a usefulness condition, that the exact
self-loop square condition is equivalently

\[
\alpha^2-S^2=hN
\quad\text{for an integer }h\ge 1.
\]

This is false for a valid global-root self-loop.  Take

\[
N=77,\qquad q=2,\qquad a=\alpha=3.
\]

Then `gcd(qa,N)=1`,

\[
z=[\alpha^2]_{77}=9=3^2,
\qquad qz=18<77.
\]

Thus this is an exact positive self-containment singleton with `S=3`, but

\[
\alpha^2-S^2=0,
\]

so the only possible coefficient is `h=0`.  Its normalized root is `+1`,
as expected.  The proof itself derives the correct statement `h' >= 0` and
only then observes that **usefulness** excludes `h'=0`.  It therefore does
not prove the stronger sentence in the frozen statement.

The minimal repair is one of the following equivalent formulations:

- write `h >= 0`, and then state that a useful self-loop has `h >= 1`; or
- qualify the displayed equivalence with “for a useful self-loop.”

## Claims that survived the hostile check

### Raw-anchor canonicalization

Since `a = alpha (mod N)`, the canonical endpoint and inverse are unchanged.
The exact identity

\[
L_aL_\alpha=(qa\alpha w)^2
\]

has normalized root `+1`, because
`qa alpha w = q alpha^2 c^{-1} = 1 (mod N)`.  Also
`[L_a]=[qw]` in the positive rational square-class group.  Exact anchor
magnitude therefore adds only an even valuation vector to this binary
square-class source.

### Singleton square and normalized root

The product of the two displayed P128 values is

\[
CL_a=a^2w^2(qc).
\]

It is an integer square exactly when `qc=s^2`.  Its positive root is
`R=aws`, and

\[
R=s(q\alpha)^{-1}\pmod N.
\]

Multiplication by the unit `q alpha` proves both exact gcd identities in
the statement.  The self-containment test `q | c` is also equivalent to
`q[alpha^2]_N < N`; the proof correctly uses the canonical carry
`0 <= floor(qz/N) < q` and `gcd(q,N)=1`.

The P131 conventions `alpha/S` and `S/alpha` give the same residue whenever
`alpha^2 = S^2 (mod N)`: this residue is an involution.  Thus the apparent
orientation change causes no sign error.

### Exact semiprime count

For `N=p*l` with distinct odd primes and `q=du^2`, every eligible canonical
endpoint has the unique form `c=dv^2`.  For each such `v`,

\[
(u\alpha)^2=v^2\pmod N
\]

has four unit solutions.  Two have global signs and two have mixed CRT
signs.  Different positive `v` give different canonical endpoints.  Hence
the useful count is exactly `2V_d`.  The same four-sign argument gives the
exact self-containment count `2W_q`.

The bounds use `V_d < sqrt(N/d)` and
`phi(p*l)=(p-1)(l-1)>N/2`, which is valid for distinct odd primes.  Thus the
count is `O(sqrt(N/d))` and the density is less than
`4/sqrt(dN)`.  For one fixed center per trial, quasipolynomially many trials
whose anchor residues each have a uniform unit marginal have total success
probability `2^{-n/2+o(n)}` by a union bound; independence is unnecessary.

This probability sentence must continue to retain the section's fixed-center
scope.  Uniformity of the anchor alone would not justify it if an adaptively
chosen center were allowed to correlate with that same anchor.

### Exact-value deduplication

If `C=L_a`, the selected pair has normalized root `+1`; therefore a useful
singleton necessarily uses two distinct exact values.  Replacing either
value by an equal retained occurrence does not change the integer product
or its positive square root.  The useful singleton criterion is therefore
compatible with global exact-value deduplication.  The statement does not
claim that a duplicate root-`+1` pair survives as a nonzero binary kernel
column.

### The `N=77` certificate

All displayed arithmetic checks:

\[
[25^2]_{77}=9,
\quad [2\cdot25^2]_{77}=18,
\quad 18\cdot30=1+7\cdot77,
\]

\[
\gcd(18\pm30,77)=1,
\quad 540\cdot37500=4500^2,
\quad 4500=34\pmod{77},
\]

and

\[
\gcd(34-1,77)=11,
\qquad \gcd(34+1,77)=7
\]

are correct.  The text also correctly limits this to a source-semantic
certificate and identifies its public residual square root as a P71/P128
half-relation presentation.  It is not presented as a surviving complete
factorization run.

## Scope conclusion

Apart from the strict `h >= 1` error, the proposed boundary is materially
consistent with P71, P114, and P128--P131.  It proves no source-hitting law,
no forced multi-relation arithmetic closure, and no factoring algorithm.
Repair the one quantifier, freeze a new statement and proof pair, and run a
fresh hostile audit plus the required statement-only reconstruction.
