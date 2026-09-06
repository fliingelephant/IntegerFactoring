# F237 self-audit

1. The primality checks do not use probable-prime tests.  The verifier
   checks recursive Lucas certificates with complete factorizations of
   every predecessor `r-1`.
2. The exact-order checks include a return at the claimed order and a
   nonreturn after division by every distinct prime factor of that order.
3. The whole order modulo `s_q` is the lcm of the two primary orders, by
   the Chinese remainder theorem.
4. The power-word conclusion is uniform over every `K <= 2^57`; the
   verifier does not materialize `W_K`.
5. A prime divides `W_K` exactly when its local order divides some
   `k <= K`.  The strict comparison with both relevant primary orders is
   therefore sufficient.
6. The retained lower bound concerns `min(r_p,r_q)`, not only the two
   whole-modulus orders.
7. The example satisfies every P204 domain condition, including primality,
   balance, the bit-length definition of `B`, zero defect, equal two-adic
   valuations, and coprime exclusive residuals.
8. The statement is finite.  It does not disprove a numerical-QP theorem,
   and it does not rule out other integer-word sources.
9. The instance was post-selected.  This is disclosed in `PROVENANCE.md`.
   No statistical claim is made.

