# F213 self-audit

## Verdict

Self-audit passes for the frozen proof-only statement. The result is an
exact obstruction to the declared rational-prime parity matrix, not a
general lower bound. No mathematical computation or randomized evidence was
used.

## Hostile quantifier audit

1. The theorem says “for every \(M\geq2\), there exists.” It does not say
   that every input \(N\) or every bank has the obstruction.
2. The constructed \(N=s^2+1\) is proved odd and composite because
   \(d\parallel N\) and \(1<d<N\). It is not proved semiprime, squarefree,
   or balanced, and none of those words appears in the positive claim.
3. The public bank is exactly \(a=1,\ldots,M\). The private-row theorem is
   not claimed for added indices.
4. The count \(2M=n^{1/2+o(1)}\) is polynomial and therefore numerical QP.
   This refutes an inference from membership in the QP cardinality class;
   it does not refute a theorem requiring a particular larger QP schedule.
5. The fixed public subbank \(a\leq\lfloor n^{1/3}\rfloor\) is eventually
   contained in \(a\leq M\), so selecting the bank need not reveal the CRT
   construction parameter.
6. The result grants complete factorizations of the displayed children. It
   only classifies the ordinary valuation-parity consequences of those
   factorizations.

## Prime-existence and CRT audit

1. The proof does not assume \(M\) primes in one short interval. It uses
   Bertrand's postulate once per private prime, in disjoint growing
   intervals.
2. A prime divisor \(d\mid R^2+1\) exists because \(R^2+1>1\). Since \(R\)
   is even, every such \(d\) is odd. The congruence
   \(R^2\equiv-1\pmod d\) proves \(d\equiv1\pmod4\).
3. The bound \(d\leq R^2+1\) is enough for the bit estimate. No claim about
   the least prime in an arithmetic progression is used.
4. Taking \(H\geq R^2+1\) makes every \(\ell_a\) larger than every prime
   divisor of \(R\) and larger than \(d\). Thus
   \(R,d^2,\ell_1^2,\ldots,\ell_M^2\) are pairwise coprime.
5. For the linear polynomial \(g_a\), exactly one lift of its root modulo
   \(\ell_a\) is a root modulo \(\ell_a^2\). Since \(\ell_a>2\), another
   lift exists and has valuation exactly one.
6. For \(v\), the derivative \(2R\) is nonzero modulo \(d\). Exactly one
   lift is a root modulo \(d^2\), so a nonroot lift exists and gives
   \(d\parallel s^2+1\).
7. Choosing \(s=x_0+\mathcal L\), rather than the least CRT representative,
   guarantees \(s\geq\mathcal L>d\) and makes \(d\) a proper divisor of
   \(N\).

## Bit-length audit

1. The crude radical bound
   \(R\leq(2M^3)^M\) gives
   \(\log R=O(M\log M)\).
2. Repeated Bertrand intervals give
   \(\ell_a<2H4^{a-1}\), hence
   \(\sum_a\log\ell_a=O(M^2\log M)\).
3. Their forced doubling gives
   \(\sum_a\log\ell_a=\Omega(M^2)\). This supplies the lower bound on
   \(n\); it does not depend on an unproved estimate for \(R\).
4. Since \(\mathcal L\leq s<2\mathcal L\) and \(N=s^2+1\),
   \(n=\Theta(\log\mathcal L)\). The proof states the safe bounds
   \(\Omega(M^2)\leq n\leq O(M^2\log M)\), not the earlier unsupported
   \(\Theta(M\log M)\) claim.
5. These two bounds imply \(M=n^{1/2+o(1)}\). They are sufficient to call
   the bank polynomial-sized.

## Arithmetic audit

1. The no-carry condition is exact because
   \(a(\sqrt{s^2+1}-s)=a/(\sqrt{s^2+1}+s)<1\).
2. The identities \(E_a=a^2\) and
   \(F_a=2as+1-a^2\) follow by direct expansion.
3. Positivity of \(F_a\) uses \(a<s\). Strict descent uses
   \(N-F_a=(s-a)^2>0\).
4. If a prime divides \(a\) and \(N\), it divides \(R\), while
   \(s\equiv0\pmod R\) forces \(N\equiv1\). Thus every normalization
   denominator is a unit.
5. If a prime divides \(F_a,N\), identity
   \((as+1)^2-F_a=a^2N\) makes it divide \(as+1\). It then divides
   \(a^2+1\), hence \(R\), giving the same contradiction.
6. The private-row identity
   \(bF_a-aF_b=(b-a)(1+ab)\) is exact. Its nonzero right side has magnitude
   less than \(M(M^2+1)<\ell_a\), so \(\ell_a\) cannot occur in another
   adjacent column.
7. Every \(\ell_a\) exceeds \(M\), so it occurs in no square
   \(E_b=b^2\).

## Parity and root-image audit

1. The sign row is explicit. Each \(-E_a=-a^2\) column is exactly the sign
   vector, not the zero vector.
2. A private row forces every \(F_a\) coefficient to zero in a binary
   dependency. The sign row then forces an even number of \(E_a\) columns.
3. Conversely, any even subset of \(E_a\) columns has a positive square
   product. This proves the whole kernel, not only a subspace of it.
4. For such a subset, division by \(Y=\prod a\) is legal modulo \(N\), and
   the normalized root is exactly \(s^k=(-1)^{k/2}\).
5. Because \(N\) is odd and \(Y\) is a unit, the two gcd outputs associated
   with a global root are exactly \(1,N\).
6. Ignoring the sign row does not create a useful root: an odd subset gives
   the already public root \(s\) of \(-1\), and
   \(\gcd(s\pm1,N)=1\).

## Recursion audit

1. The \(E_a\)'s have only \(O(\log M)\) bits.
2. The \(F_a\)'s lie between \(s\) and \(2Ms+1\), so their bit lengths are
   \(n/2+O(\log M)=(1/2+o(1))n\).
3. Therefore all calls are fixed-ratio calls for sufficiently large inputs.
   There are polynomially many.
4. P183 expressly permits QP-weighted fixed-ratio side calls and one
   separate one-bit spine. The self-audit does not reject this route on
   contraction grounds.
5. Recursive factoring is conditional on an all-input routine for arbitrary
   smaller children. No promise is silently inherited by \(F_a\).

## Scope and overclaim audit

1. The construction may be easy to recognize because \(N-1=s^2\). That
   does not affect the exact parity-kernel counterexample. No hardness claim
   is made for the constructed inputs.
2. Factoring the \(F_a\)'s may enable a decoder outside ordinary parity.
   Nonlinear, Archimedean, adaptive, class-group, and other joint uses remain
   open.
3. The private primes are existential construction witnesses. The theorem
   does not claim a polynomial-time generator for the counterexample family.
4. The result does not touch P175's reciprocal-prefix selector: the parity
   image is global and supplies no such bit.
5. The correct conclusion is “the listed data do not force usefulness by
   the declared parity mechanism,” not “near-square norm banks can never
   factor.”

## Required fresh hostile checks

1. Reconstruct the \(d\parallel N\) construction and all CRT coprimalities.
2. Re-derive the upper and lower bit-length bounds from repeated Bertrand
   intervals.
3. Recheck the cross identity and its strict magnitude bound.
4. Reconstruct the entire kernel, including the sign row.
5. Verify the normalized root and both gcd outcomes.
6. Reject any reading that assumes semiprimality, balanced factors, efficient
   counterexample generation, or impossibility of non-parity postprocessing.
