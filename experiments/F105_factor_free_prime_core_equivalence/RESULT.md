# F105 — public gcd refinement exposes the exact hidden-prime parity core

**Status:** corrected candidate exact theorem. The first hostile audit required
two explicit definition boundaries. Promotion requires a fresh pin of this
wording and the completed proof-blind reconstruction.

Let the input to parity gcd refinement be integer-mask pairs

\[
(a_i,m_i),\qquad a_i>1,\quad m_i\in\mathbb F_2^s.
\]

For each prime \(p\), define its hidden parity row

\[
r_p=\sum_i (v_p(a_i)\bmod2)m_i.
\]

The public refinement repeatedly takes two entries \((x,s)\), \((y,t)\) with
\(d=\gcd(x,y)>1\), and replaces them by the nontrivial, nonzero-mask entries

\[
(d,s+t),\qquad(x/d,s),\qquad(y/d,t).
\]

For \(\alpha=v_p(x)\), \(\beta=v_p(y)\), and
\(\gamma=v_p(d)=\min(\alpha,\beta)\), the contribution after the split is

\[
\gamma(s+t)+(\alpha-\gamma)s+(\beta-\gamma)t
=\alpha s+\beta t
\quad\text{in }\mathbb F_2^s.
\]

Thus every hidden row \(r_p\) is invariant through every refinement step.
Dropping an entry with mask zero or integer value one also preserves it.

For the proof, let \(\Omega(x)\) count prime factors with multiplicity. One
eligible split decreases the sum of \(\Omega\) over the active entries by at
least \(\Omega(d)>0\). Thus every schedule terminates. Continue until no
eligible pair remains; the terminal integers are then pairwise coprime.

At termination, the public integers \(g_j\) are pairwise coprime. A prime
\(p\) divides at most one \(g_j\). If its exponent in that block is \(e\),
then

\[
r_p=(e\bmod2)m_j.
\]

Consequently every nonzero hidden prime row is exactly the mask of one public
nonsquare block. Conversely, every public nonsquare block has a prime divisor
of odd exponent, so its mask occurs as a nonzero hidden prime row. Therefore
the public factor-free matrix and the unavailable prime-factor matrix have
the same set of nonzero row masks. After zero rows are omitted, they can
differ only by duplicate nonzero rows. An implementation that retains hidden
zero rows can also differ by those zero rows.

The following consequences are exact for every explicit batch:

1. The two matrices have the same kernel and rank.
2. Repeated degree-one peeling leaves the same relation-column core. Duplicate
   equal rows cannot change whether their common active degree is one.
3. The column graph that joins columns sharing a nonzero row has the same
   connected components in both presentations.
4. Degree-one peeling and column-component decomposition can be computed
   without factoring the relation values.

This explains the matching full and prefix core-column hashes in F102 and
F103 as a theorem, not a fixed-input coincidence.

The theorem is only a decoder equivalence. It does not make the core
nonempty, make its columns rank deficient, make its normalized-root image
non-global, or give a source that succeeds on every composite input.
