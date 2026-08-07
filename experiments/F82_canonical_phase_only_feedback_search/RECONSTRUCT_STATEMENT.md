# F82 proof-blind reconstruction statement

Reconstruct or refute the claims below without reading the F82 candidate,
audit, search programs, logs, outputs, manifests, progress notes, or later
F82 artifacts.

Let

\[
N=2047=23\cdot89,
\qquad
a=11.
\]

First verify that 23 and 89 are prime and that the following are exact
integer or modular identities:

\[
11\cdot1861=1+10N,
\qquad
312\cdot269=1+41N,
\]

\[
11^4\equiv312\pmod N,
\qquad
11^{-4}\equiv269\pmod N.
\]

Prove or refute all of the following old-state claims.

1. The four positive endpoints
   \(11,1861,312,269\) are distinct, greater than one, and pairwise
   coprime.
2. None is a nontrivial integer perfect power.
3. Their residues generate exactly \(H_0=\langle11\rangle\).
4. The element 11 has exact order 22 modulo both 23 and 89.
5. Every element of \(H_0\) has synchronized \(+1\) and \(-1\) status in
   the two prime fields. Thus no direct sign gcd from \(H_0\) is proper.

Now take the canonical-residue word and inverse

\[
g=[11^7]_N=1778,
\qquad
w=1735.
\]

Verify

\[
1778\cdot1735=1+1507N,
\]

and prove or refute:

1. Both feedback residues lie in \(H_0\), so this relation adds no new
   modular subgroup element.
2. All immediate tests

   \[
   \gcd(1778\pm1,N),
   \quad
   \gcd(1735\pm1,N),
   \quad
   \gcd(1778-1735,N)
   \]

   equal 1.
3. Neither 1778 nor 1735 is an integer perfect power.
4. Integer refinement gives

   \[
   \gcd(312,1778)=2.
   \]

5. The residue 2 is not in \(H_0\), so the available block-generated
   subgroup strictly expands even though the selected feedback residue was
   already in \(H_0\).

Finally, prove or refute the phase-only claim. Verify that 2 has exact order
11 modulo both 23 and 89, using

\[
2^{11}=2048=1+N.
\]

Conclude that every pure power of 2 has synchronized identity status and,
because the common order is odd, never reaches local \(-1\). Thus for every
integer \(e\ge0\),

\[
\gcd(2^e-1,N)\in\{1,N\},
\qquad
\gcd(2^e+1,N)=1.
\]

Check that the mixed word succeeds:

\[
2\cdot11=22,
\qquad
22\equiv-1\pmod{23},
\qquad
22\not\equiv-1\pmod{89},
\]

and hence

\[
\gcd(22+1,2047)=23.
\]

State the exact scope. This is a fixed canonical-integer realization of a
phase-only subgroup expansion. It proves that pure-power contraction cannot
replace mixed-word processing after every feedback split. It does not give
an all-input selector, branch detector, frequency theorem, hard family, or
factoring algorithm. Also, 2 is visible by trial division of the old
endpoint 312 and is an ordinary public base, so feedback is not necessary
for this fixed integer under stronger preprocessing or unrestricted
factoring.
