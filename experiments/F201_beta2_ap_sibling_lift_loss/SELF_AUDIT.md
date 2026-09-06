# Self-audit of F201

## Verdict

PASS as a narrow proof-only candidate.  It is not ready for promotion.  It
needs a fresh hostile audit and an independent statement-only
reconstruction.

## Checks performed

1. **Balanced range.**  From \(p<q<2p\) and
   \(B=\lfloor\sqrt{pq}\rfloor\), the proof obtains
   \(p\leq B<q\) and \(B\leq2p-2\).  Hence
   \(\lceil B/2\rceil<p\), and \(p\) is the only integer in the declared
   interval divisible by either hidden prime.
2. **Prefix-cell interface.**  Inversion is used only on odd residue
   classes modulo powers of two.  The two parity children of the parent AP
   are exactly the two lifts modulo \(2^{t+1}\).  Public endpoint cleanup
   leaves a consecutive AP, so the exact theorem can be iterated.  No next
   bit is assumed.
3. **Odd-cardinality cleanup.**  The extra term is a public endpoint.  Its
   gcd is \(p\) if it equals \(p\), and one otherwise.  When \(L=1\), this
   gcd must factor, so the unresolved paired case always has \(s\geq1\).
4. **Interlacing and quotient.**  The strict inequalities
   \(e_i<o_i<e_{i+1}\), together with
   \(e_0>B/2\) and \(o_{s-1}\leq B\), give \(1<O/E<2\), including the
   separate case \(s=1\).  Thus the quotient is exactly one and
   \(0<D<E\).
5. **Factor orientation.**  Exactly one sibling product contains \(p\).
   Reducing \(D=O-E\) modulo \(p\) proves \(p\nmid D\) in both
   orientations.  The proof makes no assertion about \(D\bmod q\).
   Therefore \(q\mid D\) and \(\gcd(D,N)=q\) remain possible accidents;
   \(\gcd(D,N)=1\) is not claimed.
6. **Reverse division.**  Since \(E<O\), its quotient is zero and its
   remainder is the unchanged integer \(E\).  Its explicit bit length is
   also \(2^{\Theta(n)}\) at the P175 schedule.  No small-input contraction
   is inferred.
7. **Explicit bit length.**  The positive product expansion supplies the
   single lower-bound term
   \(m\prod_{i=1}^{s-1}e_i\).  The full residue cell has
   \(s=B/(4m)+O(1)\), not \(B/(2m)+O(1)\).  At P175 precision this is
   \(2^{\Theta(n)}\), and both the lower and elementary upper bit-length
   bounds have that class.
8. **Linear axes.**  On \(E=0\), divisibility of
   \(\alpha E+\beta O\) is controlled by \(\beta\); on \(O=0\), it is
   controlled by \(\alpha\).  Public coefficient gcds are separated from
   the unit case.  Accidental \(q\)-support is left open.
9. **Same-node scope.**  The exponential statement concerns writing the
   exact remainder before a smaller child exists.  It is not based on a
   demand for fixed-ratio contraction.
10. **One-child correction.**  An adaptive QP selector still yields a valid
    \(O(n)\)-stage chain.  The recurrence
    \(T(n)\leq T(n-1)+\operatorname{QP}(n)\) is explicitly preserved.

## Highest-risk claims for hostile review

1. Recheck the strict upper bound \(O/E<2\) for both \(s=1\) and
   \(s\geq2\), including all interval endpoint conventions.
2. Recheck the odd-cardinality endpoint orientation and the \(L=1\)
   terminal.
3. Recheck the exact count \(s=B/(4m)+O(1)\) for the full parent cell and
   its persistence under repeated endpoint cleanup, then recheck the
   conversion from P175 precision to exponential explicit bit length.
4. Reject any inference that \(q\nmid D\), that \(\gcd(D,N)=1\), or that
   recursively factoring \(D\) is a useful smaller child.
5. Keep the axes conclusion limited to fixed linear combinations.  It is
   not a lower bound for nonlinear or target-correlated functions of the
   two products.
6. Keep the materialization conclusion separate from implicit modular AP
   products, gamma representations, and succinct quotient-bit algorithms.

## Computation and sources

No mathematical computation or benchmark was used.  One broad web search
about Jacobi and factorial algorithms ran during the preceding exploration,
but it supplied no premise, citation, or claim to this packet.  The only
imported premise is P175's balanced-semiprime reciprocal prefix and terminal
precision.  All sibling-product claims are proved from elementary integer
inequalities and divisibility.
