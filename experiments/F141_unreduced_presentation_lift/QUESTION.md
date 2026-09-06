# F141 question — unreduced word presentations as retained relations

## Source change

At one frozen F130 word position, keep the declared integer monomial

\[
U=\prod_j q_j^{e_j},\qquad c=[U]_N,\qquad
w=\iota_N(c).
\]

F130 keeps only the canonical exact value \(cw\).  F141 asks what changes if
the decoder also keeps the lifted congruence

\[
L(U)=Uw\equiv1\pmod N.
\]

Different word positions with the same residue must not be deleted before
their lifted columns are formed.  The endpoint \(U\) is not a new named
block: its presentation on the frozen named basis is already known.

## Kill-first questions

1. Is the lifted column decoder-equivalent to the canonical F130 column, so
   that it cannot enlarge the normalized-root image?
2. If it is a real expansion, is it only the standard square-congruence or
   bounded order-relation source in different notation?
3. Can the lifted relation be kept as an exponent vector, without expanding
   the possibly large integer \(U\)?
4. Does the resulting source and complete factor-free decode keep the F130
   quasipolynomial cost bound?
5. Is there an exact direct-screen-null certificate for which the matched
   canonical relations have global normalized-root image but the lifted
   relations have a non-global image?
6. In finite discovery, does the first useful lifted dependency come only
   from two presentations of the same residue, or can one find a useful
   dependency of at least two columns whose residues are all distinct?

## Required scope

A finite certificate can prove a real source expansion.  It cannot prove
that the complete F130 source fails, that lifted relations succeed on every
input, or that order collisions occur within a quasipolynomial menu on every
input.
