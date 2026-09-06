# F217 frozen manifest

## Family

F217: moving-level trace compression and exact ring, Eisenstein, eta, and
Ramanujan coefficient targets on the balanced beta-two branch.

## Status

Frozen, self-audited, proof-only candidate. No hostile audit, blind
statement reconstruction, cross-family audit, or human audit has run. It
is not an unconditional factoring algorithm and is not a general lower
bound against compressed coefficient evaluation.

## Namespace check

Before the directory was created, a repository-wide search found no F217
entry in the durable ledgers, notes, or experiment tree.

## Frozen candidate files and SHA-256 hashes

- STATEMENT.md
  - f6bada7e65dc7c6617760cb1ce1e7b87618953cea6f46d11dc0d1fd8416e384d
- PROOF.md
  - 16946a7a8d2c6adc869524b9e27d15b2317bfb4336688a5bc5e960dafce82e5a
- SELF_AUDIT.md
  - b9eb6001d741da1905efae8b363a27306fe25d7da6c0b4732a4fbed5c102ff99
- PROVENANCE.md
  - e266737a3860eff054202d5834836526d3340898ac1200841081c3f0044f7709

## Evidence class

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, or numerical fit was performed. The result is
proof-only. Targeted retrieval was limited to local predecessor packets.
Hashing was used only to freeze the packet.

No durable registry, proved ledger, failed ledger, progress ledger,
statement ledger, inspiration file, or process-lessons file was changed.

## Claims frozen for audit

1. Under an explicitly supplied certified cyclic decomposition, inverse
   coordinate map, succinct coordinate characters, and certified
   divisor-coefficient evaluator, at most \(2r-1\le2n-1\) traces recover
   the factor orbit.
2. The cyclic decomposition and character evaluator are premises.
   Factorization of \(K\) alone is not claimed to provide them.
3. The tautological ring character sends the universal group-algebra
   divisor coefficient to
   \(\sigma_1(N)\equiv2+p+q\pmod K\).
4. The least-residue decoder recovers the integer \(p+q\) for every
   allowed input except \(N=15\), which is handled by trial division.
5. For \(k=\varphi(K)+2\), the arithmetic-normalized level-one
   Eisenstein coefficient
   \(\sigma_{k-1}(N)\) has the same residue modulo \(K\).
6. The Eisenstein target output has \(O(n)\) bits, while its unrestricted
   exact value and standard dense numeric state are exponential. The
   binary weight encoding remains \(O(n)\).
7. For prime \(K=r\ge7\), the holomorphic eta quotient
   \(\eta(\tau)^r/\eta(r\tau)\) has a coefficient modulo \(r^2\) that
   yields the same additive residue modulo \(r\).
8. The eta modularity statement is restricted to prime level \(r>3\);
   both transformation congruences and both cusps are audited.
9. The twisted Ramanujan expansion is absolutely valid for
   \(\Re(s)>0\), and its first factor-sensitive multiplier is exactly
   \(p\). Its \(s=0\) nonprincipal reading is only an Abel limit or
   analytic continuation.
10. Direct Hecke representatives, standard Manin-symbol state, standard
    moving-weight state, and direct Ramanujan summation are exponential
    named models. No arbitrary compressed model is ruled out.
11. Abelian matrix representations factoring through
    \((\mathbb Z/K\mathbb Z)^\times\) repackage character coefficients.
    Genuinely nonabelian extensions remain outside the claim.
12. A one-child recurrence
    \(T(n)\le T(n-1)+\operatorname{QP}(n)\) remains QP. The packet does
    not demand fixed-ratio contraction for a single recursive chain.

## Highest-risk points

1. Recheck that the coordinate decoder uses a supplied inverse coordinate
   map and never derives discrete logarithms from
   \(\operatorname{factor}(K)\).
2. Reconstruct both trigonometric separation bounds and the adaptive
   \(2r-1\) query count.
3. Verify that \(p+q<K\) fails only for \(N=15\).
4. Check the exact Eisenstein normalization, the exponent
   \(k-1=\varphi(K)+1\), and coprimality of every divisor with \(K\).
5. Recheck the odd-\(K\) bound \(\varphi(K)\ge\sqrt K\) and the
   distinction between residue output and standard numeric state.
6. Verify eta-quotient modularity at cusp zero and the formal-product
   congruence modulo \(r^2\), including the meaning of division by \(r\).
7. Check the \(L\)-factor direction and convergence domain in the twisted
   Ramanujan identity.
8. Reject any reading of the named-model state counts as a general lower
   bound or of any target identity as a constructed evaluator.

## Required fresh reviews

1. Recompute the four frozen content hashes before reading the packet.
2. Run a hostile audit against the statement and proof.
3. If it passes, run a strict statement-only reconstruction by a fresh
   agent.
4. Promote only after both reviews pass and all frozen hashes are
   rechecked.
