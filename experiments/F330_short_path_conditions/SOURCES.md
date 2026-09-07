# Source and prior-record scope

**Family:** route:F31

Question stated before consulting sources: can the exact Q(t) endpoint
identity at a*t=+/-1 be extended to small signed remainders, and can it
explain public families of short arithmetic reflection paths?

Local prior checks used the Rust reader, not numeric experiment prefixes:

- P246 supplies the ranked involution, decoder, and exact floor-sum
  interface. F328/SHORT_PATHS.md supplies the +/-1 endpoint identities and
  the three short retained seeds. This packet generalizes that elementary
  count identity to arbitrary remainders and examines the actual branch
  words. It does not replace the missing probability bound.
- P247 concerns uniform random matchings. Its exact endpoint and survival
  law is not transferred to the structured reflection used here.
- P166 has a different totalized floor reciprocity, involving an explicit
  gcd correction and a conditional interval-zero oracle. Our defect counts
  are ordinary public residue counts for a unit multiplier. They do not
  evaluate P166's interval-zero oracle or bypass its missing algorithm.
- The query "continued fraction" found P32 and P64 among other packets.
  Their head snippets concern real infrastructure and formal inverse-pair
  parity, respectively. No conclusion from those records is used here.

The cached primary source
[Jeřábek, Integer factoring and modular square roots](https://users.math.cas.cz/~jerabek/papers/factor.pdf)
was checked at Lemmas 4.3 and 4.5. Lemma 4.5 explicitly places the a=-1
instance on [0,(N-1)/2], and states that this special case restates
Buresh-Oppenheim's result. Therefore the a=-1 domain/involution is prior
art. Its constant-matrix traversal coordinates in PROOF.md are direct
algebra; no new factoring reduction is claimed.

Focused web searches on 2026-09-07 used:

    "factoring" "Gauss" "involution" "continued fractions"
    "integer factoring" "Lonely" Jeřábek path algorithm
    "Dedekind" "floor" "reciprocity" incomplete sums modular rotation
    Buresh Oppenheim factoring "PPA" 2006 paper
    "Buresh-Oppenheim" "factoring" "involution"

They located the author's Jeřábek manuscript and its references, but did
not establish priority for our count identity or traversal coordinates.
Other search hits on generalized floor sums were not used as mathematical
dependencies. No absence-of-prior-art inference follows from these searches.

The Jeřábek reference lists Joshua Buresh-Oppenheim, *On the TFNP complexity
of factoring*, unpublished note (2006), at
http://www.cs.toronto.edu/~bureshop/factor.pdf. That original note was not
independently inspected in this packet; the attribution above is explicitly
Jeřábek's. No new external paper was added to the shared knowledge base.

After deriving the even-representative positive block correspondence, a
second focused search used "factoring" "Stern-Brocot" inverse,
"modular inverse" "even" "Stern-Brocot", "factoring" "Farey" "parity"
algorithm, and "Buresh-Oppenheim" "continued fraction". It supplied no
primary mathematical dependency for that derivation or a first-exit
algorithm. The correspondence and its limitations are proved directly in
RATIONAL_PATHS.md; this search does not establish novelty.
