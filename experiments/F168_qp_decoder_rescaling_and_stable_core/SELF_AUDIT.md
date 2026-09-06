# F168 self-audit

## Status

This is an author self-audit only. It does not raise the candidate above
proof-only status.

## Checks performed

1. **QP closure.** The proof counts the binary length of
   \(M_B\), not its numerical value. The safe bound
   \(\operatorname{bitlen}(M_B)=O(B\log B)\) is QP for QP \(B\).
   Bank size, prime sieving, generator count, enumeration cap, equality
   lookup, random bits, and repetition are all explicitly capped.

2. **Uniformity.** Every QP exponent uses fixed constants independent of
   \(N\). A finite collection of different QP bounds can be dominated by one
   fixed QP bound. P94/P96 do not assume a complete factorization of
   \(N-1\).

3. **Non-promised inputs.** The P97/P99 localizers are required to have QP
   work on every supplied list because the source does not recognize the
   generation event. Returned factors are verified before repetition stops.

4. **Recursion.** P99, not P97, supplies the all-composite conditional
   splitter. A complete factorization tree has at most \(n-1\) proper split
   nodes, so recursion adds only a polynomial factor.

5. **First Linnik class.** For odd prime \(r\), the residue
   \(1+2r\bmod4r\) is reduced, is \(3\bmod4\), and has least positive
   representative \(1+2r\). Thus the selected prime \(p\) is larger than
   \(2r\), and \(A=(p-1)/2\) is odd and divisible by \(r\).

6. **Second CRT class.** Since \(s>p>A\) and \(A\) is odd,
   \(\gcd(4s,\operatorname{rad}(A))=1\). Both prescribed residues are
   reduced. Every positive integer satisfying
   \(q\equiv1+2s\pmod{4s}\) is at least \(1+2s>p\). Therefore the Linnik
   prime is distinct from and larger than \(p\).

7. **Coprimality and stability.** The congruence
   \(q\equiv2\pmod{\operatorname{rad}(A)}\) gives
   \(2B\equiv1\) modulo every prime divisor of \(A\), so
   \(\gcd(A,B)=1\). Both are odd, hence \(g=2\). The identity
   \((N-1)/2=2AB+A+B\) then gives \(\gcd(AB,N-1)=1\).

8. **Length link.** Two Linnik upper bounds give \(N\le C_1r^D\) for fixed
   constants, while \(N>4r^2\). Hence \(n=\Theta(\log r)\), so the named
   prime divisors \(r\mid A\) and \(s\mid B\) are each
   \(2^{\Omega(n)}\).

9. **Claim boundary.** The family proves exponentially small uniform
   separator density and failure of the displayed bounded-component
   hypotheses. It does not prove that a deterministic capped enumeration
   cannot hit an axis early. It gives no lower bound against adaptive words,
   canonical integer data, or relation decoding.

## Correction made during self-audit

The first statement draft said that every QP punctured-lcm hypothesis fails.
That wording was too broad for arbitrary supplied elements whose local orders
can be proper divisors of \(A,B\). The final statement now says only that the
bounded-prime-component hypotheses fail for the two full powered local
orders. This is exactly what the construction proves.

## Result

No mathematical counterexample was found after the correction above. The
highest-risk external premise is the quantitative, uniform form of Linnik's
theorem. A hostile audit should check its use and the P95 near-uniform error
parameter first.
