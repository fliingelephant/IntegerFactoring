# F198 hostile audit

## Verdict

**STRICT PASS.** I tried to refute each algebraic identity, parameter
conversion, oracle reduction, terminal algorithm, and complexity claim. No
counterexample or scope error survived. The result is a reduction from a
truncated carry value to factoring. It is not an algorithm that evaluates the
carry, and it is not a lower bound below the stated precision.

## Frozen packet

All required hashes matched before review.

| File | Expected SHA-256 | Observed SHA-256 | Result |
|---|---|---|---:|
| `STATEMENT.md` | `244e44b2d93fe6f62ef2ceb161b67132a12d3741a54a6ff80a2930e438dce0bb` | `244e44b2d93fe6f62ef2ceb161b67132a12d3741a54a6ff80a2930e438dce0bb` | PASS |
| `PROOF.md` | `7bde29f9c62ab8fa357f7103615a8c5a45db5a38ddb4e94a9bc576bde5bba12a` | `7bde29f9c62ab8fa357f7103615a8c5a45db5a38ddb4e94a9bc576bde5bba12a` | PASS |
| `SELF_AUDIT.md` | `3b5403d564b2e10565cab184c753fa6a956cdcdc609872bad4d0026cb77669d4` | `3b5403d564b2e10565cab184c753fa6a956cdcdc609872bad4d0026cb77669d4` | PASS |
| `PROVENANCE.md` | `9b22d615ea4cca619b8ae5085800eefb1194ddde976b745bf564a0cf9ef0b32e` | `9b22d615ea4cca619b8ae5085800eefb1194ddde976b745bf564a0cf9ef0b32e` | PASS |

The manifest is intentionally not self-hashed. Its observed SHA-256 is
`c174304e0c5d96d9399a65baf86237f0d0076fb5d2a187a661696a027d5b3f0b`.

I read all five frozen files in the directory. I did not modify them or any
ledger.

## Primary-source verification

I inspected these primary sources directly:

- Mugurel Ionut Andreica, [“A Fast Algorithm for Computing Binomial
  Coefficients Modulo Powers of Two”](https://pmc.ncbi.nlm.nih.gov/articles/PMC3856163/),
  *The Scientific World Journal* (2013), Article 751358.
- Yiming Gao, Yansong Feng, Honggang Hu, and Yanbin Pan, [“On Factoring and
  Power Divisor Problems via Rank-3 Lattices and the Second
  Vector”](https://eprint.iacr.org/2025/1004.pdf), ePrint 2025/1004. The
  ePrint landing page identifies the current revision as 2025-11-11.
- Don Coppersmith, [“Small Solutions to Polynomial Equations, and Low
  Exponent RSA Vulnerabilities”](https://link.springer.com/content/pdf/10.1007/s001459900030.pdf),
  *Journal of Cryptology* 10 (1997), 233–260.

The Andreica dependency uses a corrected reading of four evident printed
defects. The other two terminals use the theorem statements in the cited
primary papers without changing their hypotheses.

## 1. Balanced-prime congruence and integrality

From (p<q) and (N=pq),

\[
p<\sqrt N<q,
\]

so (p\le B<q). The promise (q<2p) also gives

\[
B\le\sqrt{pq}<\sqrt2p<2p.
\]

Thus write

\[
B=p+r,\quad 0\le r<p,
\qquad
q=p+d,\quad 1\le d<p.
\]

Modulo (q), all denominators (1,\ldots,B) are units. Therefore

\[
C=\prod_{j=1}^{B}\frac{N-j}{j}\equiv(-1)^B\pmod q,
\]

and (A=(-1)^BC\equiv1\equiv1-q\pmod q).

The base-(p) digits are exactly

\[
N-1=p^2+(d-1)p+(p-1),
\qquad B=p+r.
\]

Lucas' theorem gives

\[
C\equiv
\binom10\binom{d-1}{1}\binom{p-1}{r}
\equiv(d-1)(-1)^r\pmod p.
\]

Since (p) is odd,

\[
(-1)^B=(-1)^{p+r}=-(-1)^r.
\]

Hence

\[
A\equiv1-d\equiv1-q\pmod p.
\]

The mod-(p) and mod-(q) congruences combine because the primes are
distinct. Thus (N\mid A-(1-q)), and (h) is an integer. This argument
does not divide by a multiple of (p); Lucas' theorem handles that modulus.

**Attack result: PASS.** The sign, base-(p) digits, and both CRT
coordinates are correct.

## 2. Andreica dependency and public offset

The primary paper states the following main-range interface at precision
(T):

- preprocessing costs
  (O(T^3\mathsf M(T)+T^4));
- one query (inom P Q\bmod2^T), for
  (0\le Q\le P\le2^T-1), costs
  (O(T^2\log T\,\mathsf M(T))).

F198 substitutes

\[
T=n,\qquad P=N-1,\qquad Q=B.
\]

The definition of (n) gives (N+1\le2^n), so

\[
N-1\le2^n-2<2^n.
\]

Also (0\le B\le N-1). The query is therefore in the source's main
range. F198 does not use the source's large-index extension. Computing at
precision (n), then reducing to (t\le n), is valid. Calling the
main-range theorem directly at precision (t) would not be valid in
general, and the frozen proof does not do that.

The four inherited source corrections are forced:

| Printed location | Printed defect | Forced reading | Why it is forced |
|---|---|---|---|
| Equation (25) | Adds the `FFODD` blocks. | Multiply the blocks modulo (2^T). | The blocks partition a product of odd integers. Addition cannot equal the defined product. |
| Equation (29) | Adds `FODD(P)` and `F_2(P/2)`. | Multiply `FODD(P)` by (F_2(\lfloor P/2\rfloor)). | Removing one factor of two from every even term of (P!) leaves the odd part of (lfloor P/2\rfloor!). Both the operation and integer argument are forced. |
| Section 3 valuation recurrence | Uses the current `Exp_2(...,Q)` on both sides. | Use `Exp_2(...,Q-1)` on the right. | The binomial update advances from (Q-1) to (Q); the printed self-reference cannot define the next value. |
| Equation (17) | Omits floors in Legendre's formula. | Use (sum_{j\ge1}\lfloor Q/2^j\rfloor). | A 2-adic valuation is an integer and the standard valuation identity requires floors. |

These repairs do not hide an asymptotic change. The source already budgets
the block work as multiplications. The extra recursive multiplication is
dominated by its stated multiplication count. Floors and the corrected
index have polynomial cost. The corrected factorial identity, Legendre
valuation, and odd-part inversions give the source's displayed binomial
formula modulo (2^T).

After obtaining (C\bmod2^n), F198 applies the known parity of (B),
reduces to (2^t), and multiplies by (N^{-1}\bmod2^t). The inverse exists
because (N) is odd. Negative (A) when (B) is odd causes no problem;
canonical modular reduction covers both signs.

**Attack result: PASS.** The source is genuinely typo-dependent, but F198
states that dependency and uses only the forced corrected main-range
interface.

## 3. Hidden inverse identity and oracle reductions

The definition of (h) is equivalent to

\[
Nh=A-1+q.
\]

Modulo (2^t), multiplication by (N^{-1}) gives

\[
h\equiv N^{-1}(A-1)+N^{-1}q
\equiv z_t+(pq)^{-1}q
\equiv z_t+p^{-1}\pmod{2^t}.
\]

Thus

\[
h-z_t\equiv p^{-1}\pmod{2^t}.
\]

This is modular multiplication by (N^{-1}). It does not require
((A-1)/N) to be an integer.

Given the canonical oracle value (H=h\bmod2^t), the residue

\[
u=(H-z_t)\bmod2^t
\]

is the odd unit (p^{-1}\bmod2^t). Inverting (u) returns exactly
(p\bmod2^t). Conversely, (p\bmod2^t) is odd, so its inverse exists and
adding (z_t) returns (h\bmod2^t). This remains true at (t=1), where
the unit group has one element. Each direction uses one query and
polynomial-time modular arithmetic.

The public-computability condition on (t=t(N)) is necessary for a uniform
promise reduction and is stated in Theorem 2. At the terminal precision,
the factorer also knows (t), so it can compute (L=k-t) without any
hidden advice.

**Attack result: PASS.** There is no quotient convention, sign ambiguity,
or unavailable inverse in the reduction.

## 4. Exact input-length conversions

From (n=\lceil\log_2(N+1)\rceil),

\[
2^{n-1}<N+1\le2^n.
\]

Hence (N\ge2^{n-1}). Equality would make the odd composite (N) a power
of two, which is impossible. Therefore

\[
2^{n-1}<N<2^n,
\qquad
\lfloor\log_2N\rfloor=n-1.
\]

Let (a=n-1). Since (log_2N\in(a,a+1)), division by four gives an
interval of width (1/4). If (a\equiv3\pmod4), its right endpoint is an
integer but is not included; in all other cases it crosses no integer.
Consequently,

\[
\left\lfloor\frac{\log_2N}{4}\right\rfloor
=\left\lfloor\frac{n-1}{4}\right\rfloor.
\]

**Attack result: PASS.** The threshold is not the approximate
(lfloor n/4\rfloor); the frozen equality is exact.

## 5. Half-precision exact recovery

The strict ordering (p<q) implies (p^2<N), so (p<\sqrt N). Also
(N<2^n). For (t_0=\lceil n/2\rceil),

\[
0<p<\sqrt N<2^{n/2}\le2^{t_0}.
\]

Therefore the canonical value (p\bmod2^{t_0}) is the integer (p), not
one of several lifts. Checking (1<p<N) and (p\mid N) makes recovery
sound. Exact division returns (q). In the reverse direction, a
factorization supplies the smaller factor and formula (10) computes the
carry residue without materializing (A) or (h).

**Attack result: PASS.** Ceiling parity and strict inequalities cover both
even and odd (n).

## 6. Gao--Feng--Hu--Pan Theorem 3.1

The current primary source states in Theorem 3.1 that, given natural
numbers (N,s) and (m\in(\mathbb Z/N\mathbb Z)^*) with (s,m<N), it
deterministically finds all prime divisors satisfying

\[
p\equiv s\pmod m,
\qquad p^r\mid N,
\]

within

\[
O\!\left(
\left\lceil\frac{N^{1/(4r)}}m\right\rceil
\frac{\log^{7+3\epsilon}N}{r^{2+\epsilon}}
\right)
\]

bit operations. Its introduction states the deterministic multitape Turing
model used by the paper.

F198 sets

\[
r=1,qquad m=2^t,qquad s=p\bmod2^t,qquad t\ge1.
\]

Every hypothesis checks:

1. (N) and (s) are natural integers. The source's Appendix A reduces
   (s) to (0\le s<m). Its own Theorem 6.1 explicitly invokes Theorem
   3.1 with (s=0,m=1), so zero is within the source's intended range.
   F198's actual (s) is nonzero because an odd prime cannot be zero
   modulo (2^t) for (t\ge1). Thus (1\le s<m).
2. (N) is odd, so (gcd(2^t,N)=1), and (m) represents a unit modulo
   (N).
3. Since (t\le k\),
   (m=2^t\le2^k\le N^{1/4}<N).
4. By construction (p\equiv s\pmod m).
5. The selected (p) is prime and (p^1\mid N).

The proof correctly invokes Theorem 3.1, which finds primes in one selected
class. It does not invoke Corollary 3.2, whose additional premise requires
every prime divisor of (N) to occupy the same class.

Let (alpha=(\log_2N)/4). With (k=\lfloor\alpha\rfloor) and
(t=k-L),

\[
\frac{N^{1/4}}{2^t}
=2^{\alpha-k+L}
<2^{L+1}.
\]

Because (L) is an integer, the ceiling is at most (2^{L+1}). For
(L=(\log n)^{O(1)}), this factor is numerical QP. The remaining
(log^{7+3\epsilon}N) factor is polynomial in (n). Checking each
returned value for nontriviality and exact divisibility has polynomial
cost.

**Attack result: PASS.** The residue range, zero convention, unit modulus,
(m<N), exponent parameter (r=1), theorem number, and bit-model cost all
match the primary source.

## 7. Coppersmith Theorem 5

The primary paper's Theorem 5 states deterministic polynomial-time
factorization from the low-order

\[
k=\left\lfloor\frac14\log_2N\right\rfloor
\]

bits of one factor (P). Its proof writes

\[
P=2^kx+P_0,
\qquad
Q=2^ky+Q_0,
\]

iterates over the possible value of (lceil\log_2P\rceil), and uses

\[
\frac{(2^kx+P_0)(2^ky+Q_0)-N}{2^k}.
\]

Thus the source itself supplies the exact floor and does not require the
factor bit length as advice.

For (t=k-L\ge1), the values

\[
p_{0,j}=p_t+j2^t,
\qquad0\le j<2^L,
\]

are distinct, lie in ([0,2^k)), and exhaust every residue modulo (2^k)
that reduces to (p_t) modulo (2^t). The count is exactly
(2^{k-t}=2^L), including the (L=0) case. One value is
(p\bmod2^k).

Every extension is odd. Hence it has an inverse modulo (2^k), and

\[
q_{0,j}=Np_{0,j}^{-1}\bmod2^k
\]

is defined. For the correct extension,

\[
q_{0,j}=N p^{-1}\equiv q\pmod{2^k}.
\]

For every extension, not only the correct one,
(p_{0,j}q_{0,j}\equiv N\pmod{2^k}). Therefore the constant term of
Coppersmith's divided polynomial is an integer. In this odd-semiprime
application (p_{0,j}) and (q_{0,j}) are odd, so the divided polynomial
is primitive. For the correct extension, its small integer root is exactly
the root covered by Theorem 5.

An incorrect extension has no correctness promise, but the deterministic
polynomial-time routine still terminates. F198 accepts a result only after
checking (1<d<N) and (d\mid N). Thus false candidates cannot corrupt
soundness, while the correct extension guarantees completeness. The total
post-oracle cost is

\[
2^L\operatorname{poly}(n)
=2^{(\log n)^{O(1)}}.
\]

**Attack result: PASS.** The frozen proof uses the low-order Theorem 5, not
the high-order Theorem 4, supplies the other factor's low bits exactly, and
verifies all candidates.

## 8. QP slack, composition, and small inputs

For each fixed polylogarithmic (L), both terminal costs are bounded by
(2^{(\log n)^{O(1)}}). Multiplying by a polynomial, adding one
numerical-QP oracle call, or running (O(n)) sequential numerical-QP
stages preserves that class.

Since (k=\Theta(n)) while (L=(\log n)^{O(1)}=o(n)), the condition
(k-L<1) holds for only finitely many inputs. Direct deterministic
factoring on that fixed finite set changes only the constant part of the
uniform asymptotic bound. For inputs covered by the theorem, (t\ge1)
also guarantees (k\ge1), so every power-of-two inverse and every
Coppersmith modulus used above is nondegenerate.

The earlier public-computability scope for (t) is important. If one
allowed an unspecified noncomputable (L), a uniform promise-function
claim would not be meaningful. F198 does not need such an interpretation:
the terminal receives the declared precision (t), and computes the
integer slack as (L=k-t).

**Attack result: PASS.** No exponential factor is hidden in a ceiling,
polynomial logarithm, oracle composition, candidate loop, or finite-input
exception.

## 9. Claim-boundary audit

| Targeted claim | Result | Hostile conclusion |
|---|---:|---|
| Balanced congruence and (h\in\mathbb Z) | PASS | Both prime moduli and the sign were reconstructed. |
| Public computation of (z_t) | PASS | Andreica is called at precision (n), inside its main range, before reduction. |
| Andreica errata | PASS | All four defects are visible in the primary source and have unique definition-preserving corrections. |
| (h-z_t=p^{-1}\bmod2^t) | PASS | It follows directly after multiplying (Nh=A-1+q) by (N^{-1}). |
| One-query oracle reductions | PASS | All inverted residues are odd units, including at (t=1). |
| Half-precision exact recovery | PASS | The strict bound places (p) inside the canonical residue interval. |
| (lfloor\log_2N\rfloor=n-1) | PASS | Odd compositeness excludes the only equality obstruction. |
| (k=\lfloor(\log_2N)/4\rfloor=\lfloor(n-1)/4\rfloor) | PASS | The open right endpoint removes the only possible floor crossing. |
| GFHP Theorem 3.1 application | PASS | (s,m,r), the unit condition, ranges, selected-prime premise, and model all match. |
| (s=0) scope | PASS | The source itself later applies Theorem 3.1 with (s=0); F198 actually has (s\ge1). |
| GFHP QP bound | PASS | The ceiling is at most (2^{L+1}); all logarithmic factors are polynomial in (n). |
| Coppersmith Theorem 5 application | PASS | The exact low-bit floor, other-factor residue, size iteration, and primitive polynomial match the source. |
| Extension enumeration | PASS | Exactly (2^L) residues are covered without omission or duplication. |
| Candidate verification | PASS | Exact divisibility prevents false acceptance on incorrect extensions. |
| Small inputs | PASS | Only finitely many fixed inputs fall outside (t\ge1). |
| Claimed boundary | PASS | The proof establishes sufficiency and equivalence at the named precision, not carry evaluation or a lower bound. |

## Final conclusion

The frozen packet withstands the hostile audit. Its literature dependence
is explicit and correctly scoped. The Andreica source must not be read
literally at its four defective formulas, but the stated repairs are forced
by the source's own definitions and do not change the claimed complexity.
The two factoring terminals match their primary theorems exactly. The
quarter-minus-polylog carry residue is therefore a valid deterministic
numerical-QP factoring terminal on the balanced-semiprime promise.
