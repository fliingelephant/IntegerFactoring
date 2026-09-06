# F198 self-audit

## Scope and algebra

1. The promise is exactly a balanced squarefree semiprime with distinct odd
   primes \(p<q<2p\). The function \(\mathcal P_t\) always uses the smaller
   factor \(p\).
2. The proof reconstructs the balanced congruence modulo both \(p\) and
   \(q\). It does not assume the integrality of \(h\) without explanation.
3. The expression \(z_t=N^{-1}(A-1)\bmod2^t\) is modular multiplication by
   an inverse. It does not claim that \(N\mid A-1\) in \(\mathbb Z\).
4. Equation (7) follows from \(Nh=A-1+q\) and
   \((pq)^{-1}q=p^{-1}\) modulo \(2^t\). No signed Euclidean quotient
   convention enters this identity.
5. Every inverse modulo \(2^t\) exists because \(N,p,q\) and every extension
   of the odd residue \(p_t\) are odd.

## Andreica interface

6. The algorithm computes \(C\bmod2^n\) at precision \(n\) and only then
   reduces to precision \(t\). It never applies the source's main-range
   theorem with \(T=t<n\) and upper index \(N-1\).
7. The direct source substitution is \(T=n,P=N-1,Q=B\), with
   \(N-1<2^n\). Uniform preprocessing is included in the polynomial cost.
8. F198 inherits the source scope and four forced errata from the audited
   P173/F196 package: both factorial-block additions become products, the
   valuation recurrence uses the preceding index, and Legendre's valuation
   uses floors. It does not silently read the false printed formulas
   literally.
9. The public sign \((-1)^B\) is applied before reduction. Both parities of
   \(B\) are covered by modular arithmetic.

## One-query reductions and canonical residues

10. Given \(h\bmod2^t\), subtraction of the public \(z_t\), followed by
    modular inversion, returns the canonical residue \(p\bmod2^t\).
11. Given \(p\bmod2^t\), inversion and addition of \(z_t\) return the
    canonical residue \(h\bmod2^t\). Each direction makes one query to the
    named promise function and otherwise uses polynomial work.
12. At \(t_0=\lceil n/2\rceil\), the strict bound
    \(p<\sqrt N<2^{n/2}\le2^{t_0}\) makes the canonical residue equal to
    the exact factor. The returned divisor is still checked by exact
    division.

## Direct arithmetic-progression terminal

13. Oddness gives \(2^{n-1}<N<2^n\), hence
    \(\lfloor\log_2N\rfloor=n-1\). The primary threshold
    \(k=\lfloor(\log_2N)/4\rfloor\) is therefore exactly
    \(\lfloor(n-1)/4\rfloor\), not \(\lfloor n/4\rfloor\) by
    approximation.
14. The main QP terminal uses Gao--Feng--Hu--Pan 2025, Theorem 3.1, with
    \(m=2^t\), \(s=p\bmod2^t\), and \(r=1\). Oddness gives
    \(\gcd(m,N)=1\); canonicalization gives \(1\le s<m\); and
    \(t\le k\) gives \(m<N\).
15. The proof invokes Theorem 3.1, which locates a selected prime divisor in
    one residue class. It does not incorrectly invoke Corollary 3.2, which
    assumes that every rational prime divisor lies in the same class.
16. Since \(k=\lfloor(\log_2N)/4\rfloor\), the direct published cost obeys
    \(N^{1/4}/2^t<2^{L+1}\). No enumeration is needed for this terminal.

## Independent Coppersmith threshold

17. The independent cited result is Coppersmith 1997, Theorem 5,
    specifically the low-order-bit theorem. The high-order-bit Theorem 4 is
    not substituted.
18. The actual smaller factor \(p\) is the source theorem's \(P\). The
    source iterates over possible bit lengths, so no hidden value
    \(\lceil\log_2p\rceil\) is supplied as advice.
19. From \(t=k-L\), the list in (21) has exactly \(2^{k-t}=2^L\) entries
    and exhausts, without duplication, every compatible canonical residue
    modulo \(2^k\).
20. The low bits of the other factor are computed as
    \(q_0=Np_0^{-1}\bmod2^k\). For the correct extension this is exactly
    \(q\bmod2^k\).
21. A wrong extension is never trusted. Every candidate is checked for
    nontriviality and exact divisibility. The correct extension guarantees
    that one iteration succeeds.
22. Each independent iteration is polynomial by the Coppersmith theorem.
    With a fixed \(L(n)=(\log n)^{O(1)}\), the complete enumeration costs
    numerical QP.
    The direct Gao--Feng--Hu--Pan route has the same QP bound without this
    enumeration. Composing either route with one numerical-QP carry call
    remains numerical QP.
23. The theorem assumes \(t\ge1\). The finitely many smaller inputs are
    handled directly, so they do not change the asymptotic uniform bound.

## Nonclaims

24. F198 does not compute \(h\), \(p^{-1}\), or any new carry bit. It only
    identifies an exact sufficient statistic and its precision threshold.
25. The result is a reduction, not a lower bound below quarter precision and
    not a lower bound against factorial, binomial, gamma, middle-product, or
    product-tree algorithms.
26. A one-bit selector chain is not rejected for lacking fixed-ratio
    contraction. Only \(O(n)\) sequential QP stages would still have QP
    total cost.
27. No experimental mathematical computation, randomized evidence, or
    durable-ledger edit supports this packet.
