# F136 corrected hostile re-audit — FAIL

## Verdict

**FAIL, for one narrow proof sentence.** The corrected definitions make
Theorems 1--3 self-contained, and the new Theorem 4 is a valid explicit
conditional corollary. I found no change to the arithmetic theorem or its
constants. However, Section 6 of the frozen proof contains a false
monotonicity claim.

Audited frozen hashes:

- `STATEMENT.md`:
  `7f751c757ce61b341e1845abf04c7f1076b6417af827480520a9f77ebd6c9a3e`
- `PROOF.md`:
  `754f9c1d552b9a98fe59cda16233bc776119de2bf47bc06506fcdf702fab8473`

## Exact failure

Section 6 says that at \(n=21846\), \(L=15\), and \(E=2^{225}\), and then
states:

> For all larger \(n\), the gap only grows.

This is false. On every interval where

\[
L=\lceil\log_2(n+1)\rceil
\]

is constant, \(E=2^{L^2}\) is constant while
\(B=\lceil12n\rceil=12n\) increases. For example, \(n=21846\) and
\(n=21847\) both have \(L=15\), while \(B\) increases by \(12\).
Therefore both \(E-B\) and \(E/B\) decrease at this step.

The required conclusion \(B<E\) is still true. A direct uniform proof is

\[
n\le2^L-1,
\qquad
B=12n<12\mathbin{\cdot}2^L<2^{L^2}=E
\quad(L\ge15).
\]

Replacing the false sentence by this inequality repairs the proof without
changing the theorem.

## Checks that passed

The blind failure requested five missing conventions. The new Definitions
section now supplies all five.

1. It defines a unit block and the least positive inverse.
2. It defines \(P_N(c)\) and stored endpoint presentations.
3. It states both endpoint gcd screens.
4. It defines first-occurrence exact-value retention and parity-row degree.
5. It defines complete gcd-free refinement and the residual-block meaning
   used by Theorem 3.

With these definitions, the canonical anchored values in Theorem 2 and the
release statements in Theorem 3 are truth-valued and reconstructible from
the statement. The original elementary proof of Theorems 1--3 is unchanged
apart from the added algorithmic scope, and its constants remain correct:

\[
x\ge2^{18},
\qquad
n\ge21846,
\qquad
B=12n,
\qquad
d>\frac{37n}{50\log(13n)}.
\]

Theorem 4 no longer asks the reader to derive the all-block transcript and
decoder cost from undefined external objects. It assumes that entire source
and cost guarantee explicitly. Conditional on that hypothesis, the F136
prime-anchor scan is a subbank once \(B<E\), so it adds no source position.
The only failed step is the quoted monotonicity sentence used to justify
\(B<E\).

## Scope

This failed re-audit does not refute the linear-cutoff theorem. It records a
false proof claim that has a one-line exact repair. No durable ledger should
promote this frozen proof hash.
