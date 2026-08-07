# Hostile audit of F74 — FAIL as written

## Verdict

**FAIL as written.** The three gcd forms, the valuation law, the
necessary-and-sufficient divisor test, the \(D_r>r\) construction under
\(N>r^2\), the polynomial bit-cost claim, and all displayed arithmetic
witnesses are correct. The failure is a scope failure in the claimed
algorithmic contribution.

When the seed quotients and target quotients are polynomially bounded, the
gate is already dominated by a polynomial scan of small canonical states.
The candidate proves the small-prime support law needed for this domination,
but does not draw the consequence. It therefore calls the construction a
new high-support replacement for subset search in a regime where it gives no
new relation value or provenance. The note also dismisses \(r=k_i\) for an
unsafe reason: a retained relation value can have a new endpoint presentation
that matters, even though this particular gcd gate gives no useful
localization when \(D_r=A_r\).

The audited file was pinned before reading. Its SHA-256 was the expected

```text
6cdb5cea5121d07972c2f84211d6cfd26d0a30088769355806b86eec0c26a217
```

I also checked the relevant promoted statements P69, P70, P71, and P78.

## 1. Blocking scope defect: bounded quotients reduce to a small-state scan

Assume

\[
1\le r,k_i\le B,
\qquad B=\operatorname{poly}(\log N),
\qquad r\ne k_i.
\]

Suppose \(D_r>r\). By the candidate's own valuation law, each prime divisor
of \(D_r\) divides some nonzero \(k_i-r\). Hence every such prime is at most
\(B\). The integers \(\lvert k_i-r\rvert\) are at most \(B\), so trial division factors
all of them in polynomial time. This also gives the prime factorization of
\(D_r\), because \(D_r\) is already known by one gcd.

Multiply prime occurrences of \(D_r\) until the product first exceeds \(r\).
Call the product \(g\). Then

\[
r<g\le rB\le B^2.
\]

If \(N>B^2\), then \(g<N\), and Theorem 2 gives

\[
g\,\iota_N(g)=1+rN=A_r.
\]

Thus a prior scan of all canonical states \(2\le g\le B^2\) already emits
the same relation value \(A_r\). Once \(A_r\) is present, the old transcript
computes the same

\[
D_r=\gcd(P,A_r)
\]

and the same gcd-free provenance. If \(N\le B^2\), trial division through
\(B\) handles \(N\) directly. Therefore the complete bounded-\(k_i\),
bounded-\(r\) gate is polynomially dominated by the small-state scan.

This does not make the algebra useless. The sieve can be a genuinely
different source operation when some difference \(\lvert k_i-r\rvert\) is not
polynomially bounded. A corrected note must state this boundary. It must not
claim an unqualified high-support algorithmic gain or an unqualified
replacement of exponential subset selection. In the bounded regime it is a
batch certificate for information that the small-state scan can already
generate.

This correction is especially important after P69 and P78. P69 already
identifies quotient-bounded state-scan domination. P78 shows that endpoint
presentation and provenance, not only the relation value, can matter. The
argument above preserves that provenance: after the small scan emits
\(A_r\), computing \(\gcd(P,A_r)\) gives exactly the same \(D_r\) for
refinement.

## 2. Required correction at \(r=k_i\)

The sentence that such a scan “only rediscovers a retained relation value”
is true only at the value level. It is not a sufficient reason to call the
case uninteresting. Different endpoint presentations of one value can have
different direct screens and different source capacity.

There is a small exact example. At \(N=55\), retain

\[
56=2\cdot28=1+1\cdot55.
\]

The retained endpoints pass both sign screens:

\[
\gcd(2\pm1,55)=1,
\qquad
\gcd(28\pm1,55)=1.
\]

After gcd-free refinement, the source contains powers of \(2\) and the block
\(7\). The alternative legal presentation

\[
56=14\cdot4
\]

has the same quotient \(r=k_i=1\), but

\[
\gcd(14+1,55)=5.
\]

For \(r=k_i\), the identity gives \(D_r=A_r\). It therefore supplies no
collision filter and does not select \(14\) from the divisors of \(56\).
That is the correct reason to exclude the case from the quotient-collision
gate. The corrected text must not imply that an old relation value makes all
new presentations redundant.

## 3. The exact algebra passes

From (P=1+KN),

\[
P-N(K-r)=1+rN=A_r.
\]

Since (gcd(P,N)=1), this proves

\[
\gcd(P,A_r)=\gcd(P,K-r).
\]

Modulo (A_r), each retained value satisfies

\[
A_i\equiv (k_i-r)N.
\]

Because (gcd(A_r,N)=1), multiplication by (N^m) does not affect the
gcd. Hence

\[
\gcd(P,A_r)
=\gcd\!\left(A_r,\prod_i(k_i-r)\right).
\]

The zero-factor convention when (r=k_i) is also correct. For
(r\ne k_i), taking prime valuations gives equation (3) exactly. The prime
support bound (4) follows.

## 4. The divisor gate and construction pass

Let (g) be an occurrence-certified divisor of (P), with (1<g<N).
Because (P) is coprime to (N), (g) is a unit. If its canonical inverse
has quotient (r), then (gmid A_r), so (gmid D_r), and the usual
canonical-inverse bound gives (r<g).

Conversely, if (gmid D_r) and (r<g<N), then

\[
w=\frac{1+rN}{g}
\]

is a positive integer and

\[
w\le\frac{1+rN}{r+1}<N.
\]

It is therefore the canonical inverse of (g), with exact quotient (r).
Theorem 2 is correct.

Under (N>r^2), complete gcd-free refinement represents (D_r) as a
polynomial-length list of retained block occurrences. If one occurrence is
larger than (r), it is a valid (g). Otherwise the first running product
larger than (r) is at most (r^2<N). This proves the (D_r>r)
if-and-only-if gate. The branch (N\le r^2) is also polynomial when
(r\le\operatorname{poly}(\log N)), because trial division only runs
through (r).

The proof needs the candidate's explicit assumptions: the endpoint
transcript is retained, block exponents and capacities are exact, and the
number of indexed occurrences is polynomial. Under those assumptions, the
gcd-free representation claim is sound. It does not factor an unrestricted
unknown integer.

## 5. Bit complexity and provenance pass with one qualification

Each (A_i<N^2). For polynomial (m), the explicit product (P) has
(O(m\log N)) bits. A polynomial number of products, gcds, exact divisions,
and gcd-free refinements therefore has polynomial bit cost. A polynomial
scan of (r) is polynomial in the full retained transcript size.

The subproduct identity (7) is correct at every tree node. A product tree can
mark all indexed occurrences that support a prime or composite gcd factor.
When the same prime power occurs in both children, the raw child gcds can
overlap. Exact non-overlapping capacity allocation then needs the stated
gcd-free refinement and valuation caps. The tree alone is not an arbitrary
subset selector. The candidate mostly states this limitation correctly.

## 6. Direct screens and multiplicity pass

Since (g) is a unit and (gw\equiv1\pmod N),

\[
\gcd(g-w,N)=\gcd(g^2-1,N).
\]

For a non-global involution, (g=w), so this gcd is (N). The two sign gcds
must remain. The (N=55, g=21) example is exact.

The duplicate relation example at (N=4033) is also exact. With one
quotient-one occurrence,

\[
D_3=\gcd(1+3N,-2)=2.
\]

With two indexed occurrences,

\[
D_3=\gcd(1+3N,4)=4.
\]

The duplicate does not enlarge a decoder row span, but it changes source
capacity and opens the gate. HNF or SNF compression must therefore preserve
multiplicity or an equivalent capacity ledger.

## 7. Witness audit

All five finite rows have the stated gcd:

\[
\begin{array}{c|c|c}
N & (k_i;r) & D_r\\ \hline
21 &(1,4;9)&10\\
55 &(1,2;8)&21\\
21 &(1,1,1;3)&8\\
4033 &(1,1;3)&4\\
4033 &(1,63,7;1983)&10240.
\end{array}
\]

In the last row,

\[
D_r=10240=2^{11}\cdot5,
\qquad
\gcd(D_r,1985)=5,
\]

and (g=2048) has (w=3905<N) and quotient (1983). Its two sign
screens and difference screen are all trivial, as P78 states. The source
exponent ledger contains the required eleven powers of (2).

The infinite power-family calculation is also exact:

\[
\gcd\left(2^{2t},(-2)^t\right)=2^t.
\]

For odd (t\ge3), (g=2^t<N=(2^{2t}-1)/3), and the displayed factor
identities follow.

The table proves that each listed useful (g) divides the corresponding
(D_r). It does not prove that the generic greedy rule selects that useful
(g) on other inputs. The final section correctly admits that opening the
gate need not make factor-bearing progress. The phrase “recovers all central
examples” should therefore mean “contains and certifies the listed
witness-specific choices,” not “selects a useful divisor in general.”

## 8. Dual (g\leftrightarrow r) interpretation

There is no hidden algebra error in the proposed dual view. For a supported
unit (g>1),

\[
\rho(g)=(-N^{-1})\bmod g
\]

in the range (1,\ldots,g-1) is exactly its canonical inverse quotient
(k(g)). Conversely, fixing (r), (D_r=gcd(P,1+rN)) is the largest
integer divisor common to the source product and the quotient-(r) relation
value.

Two limits must remain explicit. (D_r) can be at least (N), so it is not
itself necessarily a legal state. Also, (D_r) aggregates all supported
divisors in the fibre; it does not select a factor-bearing member of that
fibre.

## 9. Computation disclosure

No research search or family scan was run. I used exact Python integer
arithmetic only to verify the five displayed (D_r) values, the two
(N=4033) candidates (g=2048,2560), their canonical complements and
screens, and the small power-family instances (t=3,5,7). These checks only
verified formulas already present in the candidate or the audit; no empirical
claim depends on them.

## Required repair

Keep Theorems 1–3 and the polynomial bit-cost proof. Add the bounded-quotient
domination theorem from Section 1 of this audit. Restrict the claimed new
algorithmic role to regimes with unbounded seed-quotient differences, or
state the sieve only as a batch certificate. Correct the (r=k_i) rationale,
and distinguish “(D_r) contains a useful witness” from “the greedy rule
selects one.” The repaired version needs a fresh hostile audit.
