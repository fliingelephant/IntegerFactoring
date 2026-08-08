# F111 — one cross-layer dependency now has a factor-free public certificate

**Status:** completed candidate replay.  Hostile audit and proof-blind
reconstruction are required before promotion.

For

\[
N=3{,}241{,}632{,}473,
\]

the executable regenerates 15,383 retained relation values from the public
frozen source.  It applies 30,766 direct endpoint gcd screens.  Every screen
is nonproper.

The explicit certificate selects 363 relation values:

- 327 from the frozen seed-basis layer;
- 36 from the appended fixed-pair layer.

Their exact integer product is a 21,620-bit square.  Its positive square root
has residue

\[
1{,}058{,}780{,}986\pmod N,
\]

and gives

\[
\gcd(R-1,N)=79{,}043,
\qquad
\gcd(R+1,N)=41{,}011.
\]

The replay uses modular inversion, gcd, exact division, exact integer roots,
multiplication, and square testing.  It does not factor an endpoint, test a
prime, or read the hidden factors.

This is an explicit factor-free cross-layer relation.  The 363 relation
indices are advice found by the factor-assisted discovery.  They verify that
the public batch contains a useful dependency; they do not provide an
all-input selector or prove that another batch must contain one.
