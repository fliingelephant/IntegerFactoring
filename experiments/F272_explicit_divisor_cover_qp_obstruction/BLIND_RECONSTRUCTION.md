# F272 blind statement-only reconstruction

## Blind boundary and verdict

I used only the root `PROMPT.md`, the root `AGENTS.md`, and the statement under
audit. Before reading the statement, I authenticated its SHA-256 as

```text
103722d5cf46884678867fd093e1ce5bcef9d57a797275c0f0e3c262615d67d0
```

I did not inspect the proof, self-audit, provenance, manifest, history, any
other F272 file, or any sibling-agent message.

**Verdict: the principal rank-free lower bounds reconstruct, but the statement
is not correct in every literal claim.** The prime-mass inequality, the
explicit-output mass inequality, the prime-pair incidence inequality, the
three necessary exponent inequalities, and the prime-separating-family
inequalities are valid. The interval-product evaluator is sufficient for a
quasipolynomial factoring algorithm. The following qualifications are needed:

1. At \((\alpha,\beta)=(1/3,1/3)\), (15) is an equality but (16) has strict
   slack: \(2/3>1/2\). Thus the claim that both constraints are “tight” at
   that point is false under the usual meaning of tight.
2. Turning an output-length bound into a bit-time bound preserves the lower
   bound exactly only under the normalization that one time unit writes at
   most one bit. In a machine model stated only up to a fixed constant, the
   conclusion is \(KF=\Omega(\vartheta_2(X))\), which has the same exponent
   consequence.
3. The proved obstructions do not establish that a succinct product hierarchy
   is the unique surviving route. It is one sufficient interface. Adaptivity,
   compressed decoding, and unrelated factoring mechanisms are not reduced to
   that interface by anything in the statement.
4. The named He--Sahai and algorithmic-complexity claims are external claims,
   not consequences of the supplied definitions. Under this blind protocol I
   cannot authenticate them. The consequences stated conditionally on (18)
   are consistent.

## 1. Sets, signs, zero, and duplicates

For \(d>0\), divisibility is unchanged by sign, so replacing \(s-t\) by
\(|s-t|\) loses no valid positive divisor witness. A zero difference must be
discarded: every positive \(m\) divides zero, so one admitted zero would make
the cover condition vacuous, while \(\log 0\) is undefined.

Repeated occurrences of the same positive difference give no new coverage.
Passing from ordered pairs to the set \(D\) therefore only removes redundant
copies. If

\[
 K=|\{(s,t)\in S\times T:s\ne t\}|,
\]

then \(M=|D|\le K\le |S||T|\). If one starts with multisets instead of sets,
replacing them by their supports preserves every available difference and can
only reduce the displayed size bounds. Thus the obstruction is at least as
strong for multisets. The value \(d=1\) causes no problem: its logarithmic
mass is zero and its bit length is one.

Because \(X\ge2\), the divisor property forces \(D\ne\varnothing\), so \(H\)
and \(L\) are defined.

## 2. Prime-mass inequality

For each \(d\in D\), let

\[
 P_d=\{p\le X:p\text{ is prime and }p\mid d\}.
\]

Applying the divisor property to \(m=p\) shows that every prime \(p\le X\)
belongs to at least one \(P_d\). Hence

\[
 \vartheta_2(X)
 \le \sum_{d\in D}\sum_{p\in P_d}\log_2p.
\]

The product of the distinct primes in \(P_d\) divides \(d\), so the inner
sum is at most \(\log_2d\). Therefore

\[
 \vartheta_2(X)\le\sum_{d\in D}\log_2d.
\]

By the definition of bit length, every \(d\in D\) satisfies \(d<2^L\), so
\(\log_2d<L\). Summing gives the strict inequality

\[
 \vartheta_2(X)\le\sum_{d\in D}\log_2d<ML.
\]

Combining this with \(M\le |S||T|\) proves (7). No additive structure, rank,
or progression representation entered the proof.

If \(|u|<2^B\) for every \(u\in S\cup T\), then

\[
 |s-t|\le |s|+|t|<2^{B+1}.
\]

Thus each nonzero difference has at most \(B+1\) bits, and (8) follows from
(7).

For completeness, the linear lower bound on prime mass needed below is
elementary. The central binomial coefficient gives
\(\log {2r\choose r}=\Omega(r)\). Its exponent of any prime \(p\) is at most
\(\lfloor\log_p(2r)\rfloor\), so this logarithm is at most the Chebyshev
prime-power sum \(\psi(2r)\). Also
\(\psi(y)-\vartheta(y)=O(\sqrt y(\log y)^2)\) by summing the crude bound over
prime powers of exponent at least two. Hence
\(\vartheta_2(X)\ge cX\) for all sufficiently large \(X\) and an absolute
\(c>0\).

## 3. Why quasipolynomial in \(\log X\) is too small

With \(n_X=\lceil\log_2(X+1)\rceil\), one has
\(n_X=\Theta(\log X)\). A fixed quasipolynomial in \(n_X\) is

\[
 2^{O((\log(n_X+1))^k)}
 =\exp(O((\log\log X)^k))
 =X^{o(1)}.
\]

The product of any fixed number of such bounds is still \(X^{o(1)}\).
Therefore uniform quasipolynomial bounds for \(|S|\), \(|T|\), and \(L\)
would make \(|S||T|L=X^{o(1)}\), contradicting
\(|S||T|L>\vartheta_2(X)\ge cX\) on every unbounded sequence. The constants
and exponents in the quasipolynomial bounds must, as usual, be fixed across
the sequence.

## 4. Explicit-prefactor output mass

For each prime \(p\le X\), choose one witness difference divisible by \(p\)
and one ordered pair that produces that difference. The complete explicit
factorization output for that pair contains the binary name of \(p\). Across
all \(K\) calls, the actual prime-name bits therefore have total length at
least

\[
 \sum_{p\le X}(\lfloor\log_2p\rfloor+1)
 \ge\vartheta_2(X).
\]

If each call writes at most \(F\) bits, the total output length is at most
\(KF\), proving (10). Equal differences and repeated prime names only add
output; the proof needs only one occurrence of each prime.

If \(F\) denotes time rather than output length, a bit machine that writes at
most \(C_0\) output bits per time unit gives

\[
 KF\ge \vartheta_2(X)/C_0.
\]

Taking \(C_0=1\) yields the exact displayed version. With an unspecified
fixed machine constant, the invariant statement is
\(KF=\Omega(\vartheta_2(X))\).

A dictionary does not alter the information mass. If each call must output
binary prime/exponent pairs, dictionary references do not satisfy the
hypothesis. If references are allowed, the shared dictionary must contain
the binary name of every covered prime at least once; charging its creation
or materialized storage gives the same \(\Omega(\vartheta_2(X))\) total-bit
lower bound. It need not preserve the literal per-call formula \(KF\) unless
dictionary cost is included in \(F\) or charged separately.

Since \(K\le |S||T|\), quasipolynomial \(|S|\), \(|T|\), and uniform
per-call explicit-output time in \(n_X\) would again give only \(X^{o(1)}\)
total work. This contradicts the linear prime mass even when the integers
being factored are supplied by short circuits and have very large expanded
bit length.

## 5. Prime-pair incidence inequality

For \(d\in D\), let \(r_d\) be the number of primes in \(\mathcal P\) that
divide \(d\). Their product divides \(d\), and every one is at least
\(a\sqrt X>1\). Thus

\[
 (a\sqrt X)^{r_d}\le d\le H,
 \qquad r_d\le h.
\]

Every unordered pair of distinct primes \(p,q\in\mathcal P\) satisfies
\(pq\le b^2X\le X\). The divisor property supplies a \(d\in D\) divisible
by \(pq\). A fixed \(d\) covers exactly \({r_d\choose2}\) such pairs, so

\[
 {v\choose2}
 \le\sum_{d\in D}{r_d\choose2}
 \le M{h\choose2}.
\]

This proves (13), including the vacuous cases \(v<2\), without any rank
assumption.

## 6. The exponent consequences

Under (14), positivity gives

\[
 H<\max_{u\in S\cup T}u,
 \qquad L\le X^{\alpha+o(1)},
 \qquad M,K\le X^{2\beta+o(1)}.
\]

The prime-mass inequality then implies

\[
 X^{1+o(1)}\le X^{\alpha+2\beta+o(1)},
\]

and hence \(\alpha+2\beta\ge1\).

For a fixed square-root band, the prime number theorem gives
\(v=X^{1/2+o(1)}\). Also

\[
 h\le \frac{X^{\alpha+o(1)}}{\log(a\sqrt X)}
 =X^{\alpha+o(1)}.
\]

Equation (13), together with \(M\le X^{2\beta+o(1)}\), gives

\[
 X^{1+o(1)}
 \le X^{2\alpha+2\beta+o(1)},
\]

so \(\alpha+\beta\ge1/2\). If each explicit factorization takes
\(X^{\gamma+o(1)}\) bit time, the output-mass argument similarly gives
\(\gamma+2\beta\ge1\), with the harmless fixed-machine constant noted
above.

At \((\alpha,\beta)=(1/3,1/3)\), however,

\[
 \alpha+2\beta=1,
 \qquad
 \alpha+\beta=2/3>1/2.
\]

Only (15) is saturated. Equation (16) does not exclude the point, but it is
not tight there. Nor do necessary inequalities construct a rank-two or
higher-rank cover. If (18) is assumed, then
\(\log H=X^{1/3+o(1)}=o(\sqrt X)\), while its asserted one-dimensional
length lower bound is \(X^{3/4-o(1)}\), which rules out length
\(X^{1/3+o(1)}\) in that one-dimensional setting. No higher-rank conclusion
follows from the statement's description of that external theorem.

If the relevant cover scale for factoring \(N\) is \(X=\Theta(\sqrt N)\),
then a cost \(X^{1/3+o(1)}\) becomes \(N^{1/6+o(1)}\). This is exponential,
not quasipolynomial, in the bit length of \(N\). This verifies the exponent
translation, not the external publication claim.

## 7. Prime-separating families

Separation makes the codewords of distinct primes distinct. Hence
\(2^m\ge\pi(X)\), proving (20), and two primes cannot both have the all-zero
codeword.

Every prime except a possible all-zero prime divides at least one \(A_i\).
Consequently the explicit factorization outputs contain all those binary
prime names and have aggregate length at least

\[
 \vartheta_2(X)-\log_2X.
\]

If each of the \(m\) outputs has at most \(F\) bits, (21) follows. Thus \(m\)
and \(F\) cannot both be quasipolynomial in \(n_X\). The proof is static: it
does not apply to an adaptive choice of later \(A_i\), or to a decoder whose
contract never materializes these factorizations.

## 8. What the interval-product evaluator would prove

Assume a uniform evaluator returns

\[
 E(a,b,d)=\prod_{j=a}^{b}j\pmod d
\]

in time quasipolynomial in \(\log b+\log d\). It is sufficient for factoring,
as follows.

Given composite \(N\), let \(X=\lfloor\sqrt N\rfloor\). A least prime factor
of \(N\) is at most \(X\), so

\[
 g=\gcd(E(1,X,N),N)>1.
\]

If \(g<N\), return it. If \(g=N\), maintain an interval \(I=[a,b]\) whose
integer product is divisible by \(N\). Split it into nonempty halves
\(I_1,I_2\), evaluate the product of \(I_1\) modulo \(N\), and compute its
gcd \(g_1\) with \(N\). If \(1<g_1<N\), return it. If \(g_1=N\), descend to
\(I_1\). If \(g_1=1\), divisibility of the parent product implies that the
product over \(I_2\) is divisible by \(N\), so descend to \(I_2\).

The maintained interval cannot become a singleton: its sole integer would
be at most \(X<N\) yet divisible by \(N\). Thus a proper factor appears after
at most \(O(\log X)\) evaluator calls. All moduli and endpoints have
\(O(\log N)\) bits, so this is deterministic quasipolynomial time in the
input length. Polynomial-time primality testing plus recursive splitting
gives complete factorization: there are at most \(O(\log N)\) factor nodes,
all with no larger bit length, so the total remains quasipolynomial.

The evaluator therefore is a precise sufficient and factoring-hard
interface. For a semiprime \(N=pq\), \(p\le q\), the residue
\(\lfloor\sqrt N\rfloor!\bmod N\) already gives gcd \(p\): the factorial
contains \(p\), does not contain \(q\) when \(p<q\), and contains exactly one
factor \(p\) when \(p=q\). This establishes the reduction from such residue
evaluation to semiprime factoring. It does not establish the reverse
reduction, so “factoring-equivalent” is justified only if that word is being
used informally for factoring-hardness.

Finally, the lower bounds above show why explicit expansion or explicit
factor output cannot supply the desired quasipolynomial route. They do not
prove that every possible escape must be a product hierarchy, and they do
not verify the stated complexity of named existing evaluator methods. Those
are boundaries of this reconstruction, not consequences of (6), (10), or
(13).
