# F210 V2 provenance

Status: frozen repair provenance.

## V1 identity

V1 consists of the original unversioned packet. It remains unchanged. Its
observed SHA-256 values after creation of V2 are:

- `STATEMENT.md`:
  `77fea55ce6600f149a636aed9d2bc2ce788deaba47bbcec95a03e24a39430cd9`
- `PROOF.md`:
  `c754a738c21ce89f0c43ecfa5b9a96554b4b64bc23991b3258ee7fe2a885c0ea`
- `SELF_AUDIT.md`:
  `a00f07120dcda12447e556fe4529a7c1b9d9766c5bef5188a8b9ccd05f7eda28`
- `MANIFEST.md`:
  `d9f3e38e4d9ad09b63487f8d503655638eca5b82cb6d347b0a66ef9a1c24debd`

These equal the hashes recorded when V1 was frozen.

## V1 hostile audit

The file `HOSTILE_AUDIT.md` is the fresh hostile audit of V1. Its observed
SHA-256 is

`0385546d865c4cbec55adec59fe33c92ac06c64749adf9a2de773b0557563a35`.

The audit verdict was **FAIL** on one precise theorem defect. V1 asserted
that the true chart was the only chart containing an integer point with

\[
X<\sqrt N<Y,
\qquad XY=N.
\]

That condition admits the trivial positive factor pair \((1,N)\).

The audit supplied the exact noncoalesced counterexample

\[
N=77=7\cdot11,
\qquad m=2,
\qquad r=c=1,
\qquad \delta=0.
\]

Here the false chart \((r_0,c_0,K_0)=(1,1,19)\) contains
\((P,Q)=(0,19)\), whose physical point is \((X,Y)=(1,77)\). It satisfies
the V1 inequalities.

The audit also supplied the coalesced counterexample

\[
N=91=7\cdot13,
\qquad m=2,
\qquad r=c=1,
\qquad \delta=1,
\qquad K_0=K_1=22.
\]

The other chart contains the swapped point \((13,7)\) and the trivial point
\((1,91)\). The swapped point reverses the orientation, but the trivial
point satisfies the V1 orientation. Thus the V1 sentence about the other
chart also failed.

The same audit independently passed the child formulas, coalescence and
common-support bounds, half-translation and matrix signs, odd-local scope,
scaled-root statement, finite \(2\)-adic count, conditional order-stripping
bridge, polynomial-gcd/resultant distinction, and late P183 recursion scope.
It also requested an explicit \(t\ge1\) domain statement.

## Exact V2 repair

V2 makes two scope corrections.

1. It states \(t\ge1\) explicitly wherever the dyadic domain is used.
2. It replaces the defective integer condition by

   \[
   1<X<\sqrt N<Y<N,
   \qquad XY=N.
   \]

   Under the promised semiprime factorization, this condition forces
   \((X,Y)=(p,q)\). V2 explicitly permits false charts to contain trivial
   endpoints or other integer points outside this balanced box.

V2 retains the exact limitations of V1. It does not claim a selector from
raw child-factor statistics, an efficient test for the balanced integer
point, an adaptive common-order success theorem, or an early two-child
recursion theorem.

No experimental mathematical computation or randomized evidence was used
to make this repair. Hashing and text inspection were used only to preserve
and freeze the proof packet. No durable registry, proved ledger, failed
ledger, or progress ledger was edited.

