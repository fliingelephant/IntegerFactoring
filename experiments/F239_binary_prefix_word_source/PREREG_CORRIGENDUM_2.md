# F239 preregistration corrigendum 2: two-primary incidence

The first broad-domain attempt aborted before producing a result.  The
scanner correctly rejected one preregistered cross-check at residual prime
`ell=2`.  This correction is frozen before the broad-domain rerun.  It does
not change a word, domain, bound, output rank, or stopping rule.

For every prime `ell`, including `ell=2`, the exact quotient incidence is

\[
 \ell\mid K_j
 \quad\Longleftrightarrow\quad
 N\bmod(\ell2^j)<2^j.
\]

If `ell` is an odd divisor of `s_p`, multiplication by `2^j` is invertible
modulo `ell`, so there is also the equivalent local condition

\[
 \ell\mid K_j
 \quad\Longleftrightarrow\quad
 q\equiv N\bmod2^j\pmod\ell.
\]

Exchange `p` and `q` on the `s_q` side.  This local equivalence is not used
for `ell=2`: both the other odd prime and the binary remainder are odd, so
their congruence modulo two is automatic and contains no quotient-incidence
information.

The repaired scanner will cross-check direct divisibility against the
interval predicate for every residual prime.  It will additionally
cross-check the local congruence only for odd residual primes.  The aborted
attempt is protocol-debugging information, not numerical evidence.
