# F280 V2 — statement-only blind reconstruction

## Protocol and verdict

Before this document was sealed, the only packet files read were:

- `STATEMENT.md`, authenticated as
  `0d4a9ad469b961855cf77518b29926dfecaf958884a85b73e17f0ebf6f75016d`;
- `V2_STATEMENT.md`, authenticated as
  `36d2323aa63822f23b55b5daa5aa98032592a4c3112040ab6d4bb33427143083`.

I treated V2 as V1 with exactly the stated Section 5 replacement. No proof,
audit, provenance, manifest, PDF, ledger, code, or experiment was consulted.

**Verdict: PASS, with qualifications.** The mathematical deductions made from
the two declared primary interfaces are sound, and V2 correctly restricts the
polynomial comparison to fixed \(0<\delta<1\). The qualifications are:

1. The Harvey--Hittmeir and Nir results are external premises. A
   statement-only reconstruction can check what follows from the quoted
   interfaces, but cannot authenticate the quotations or their internal
   lemma descriptions.
2. P139, P161--P170, P187, P205, P212, F259, and F260 are not defined in the
   allowed files. Their comparisons are therefore auditable only as narrow
   non-implication and scope statements, not as independent reconstructions
   of those lanes.
3. The equality \(D=N^\delta\) is literal only when it is integral. The usual
   interpretation \(D=\lfloor N^\delta\rfloor\),
   \(D=\lceil N^\delta\rceil\), or \(D=\Theta(N^\delta)\) gives the same
   exponents and domain conclusion.
4. The isolated Harvey--Hittmeir display containing \(\log D\) is an
   asymptotic large-\(D\) bound. At the literal endpoint \(D=1\), its written
   leading expression is zero. This finite case must be absorbed separately
   or the logarithm must be regularized. Theorem 2's displayed total bound is
   not invalidated: its nonzero explicit-scan term covers a constant number
   of ordinary bit operations.
5. Numerical-QP conclusions use a standard polynomial (or faster)
   deterministic multiplication bound \(\mathsf M(n)=n^{O(1)}\). Merely
   calling an arbitrarily loose function a “valid bound” would not by itself
   prove a QP upper bound.

Subject to these qualifications, I found no false V2 claim.

## 1. Definitions and the local certificate

Let

\[
n=\lceil\log_2(N+1)\rceil,
\qquad N\ge 3.
\]

For a unit \(a\bmod N\), define

\[
\mathsf{Local}_D(a;N)
\iff
\operatorname{ord}_p(a)>D
\quad\text{for every prime }p\mid N.
\]

Suppose a source has already certified \(\operatorname{ord}_N(a)>D\).
Generate \(r_e=a^e\bmod N\) successively and set

\[
g_e=\gcd(r_e-1,N),\qquad 1\le e\le D.
\]

For every such \(e\), \(g_e\ne N\), because \(g_e=N\) would give
\(a^e\equiv1\pmod N\) and hence
\(\operatorname{ord}_N(a)\mid e\le D\). Thus each test has only two possible
outcomes:

- \(1<g_e<N\), in which case it is immediately a nontrivial factor; or
- \(g_e=1\).

If every test gives 1 and some prime \(p\mid N\) had
\(\operatorname{ord}_p(a)=m\le D\), then \(p\mid g_m\), a contradiction.
Consequently the completed transcript

\[
g_1=\cdots=g_D=1
\]

is a direct all-local certificate. It is a length-\(D\) computation, not a
succinct certificate.

There are exactly \(D\) successive modular multiplications and at most
\(D\) gcd calls on a completed scan. With the cost convention in the
statement, this is

\[
O(D\,\mathsf M(n)\log n)
\]

bit operations. An early proper gcd only decreases this count.

## 2. Elementary all-local source and exact counting

The all-local source shape also has a completely elementary, slower
construction. This explains why the ordinary height \(D^{O(1)}\) is
plausible independently of either cited preprint; the preprints supply the
better source costs.

For an integer \(K\ge1\), put

\[
R_K=\sum_{m=1}^{K}\varphi(m).
\]

For a prime \(p\), the exact number of elements of \(\mathbb F_p^*\) whose
order is at most \(K\) is

\[
R_{K,p}
=
\sum_{\substack{m\mid p-1\\1\le m\le K}}\varphi(m).
\]

This is exact because \(\mathbb F_p^*\) is cyclic and has exactly
\(\varphi(m)\) elements of order \(m\) when \(m\mid p-1\). In particular,
among residues other than 1 there are exactly

\[
B_{K,p}
=
\sum_{\substack{m\mid p-1\\2\le m\le K}}\varphi(m)
=R_{K,p}-1
\le R_K-1
\]

bad residues. The coarser polynomial-root union bound is
\(R_{K,p}\le\sum_{e=1}^K e=K(K+1)/2\), but the totient formula gives the
relevant exact count.

Now first run a deterministic primality test. Report prime if appropriate.
Otherwise try, in order, the exactly \(R_K\) ordinary integers

\[
a=2,3,\ldots,R_K+1.
\]

For each \(a\), first compute \(\gcd(a,N)\). Return any proper gcd before
doing an order test. If \(a\) is a unit, run the successive power-gcd tests
for \(1\le e\le K\). Return a proper gcd immediately. Reject \(a\) if a
test gives \(N\), and return \(a\) if all tests give 1.

To prove termination, assume the composite branch returns no factor. If a
prime divisor \(p\mid N\) satisfied \(p\le R_K+1\), the attempt \(a=p\)
would have returned the proper gcd \(p\) (a smaller prime divisor is reached
even earlier when necessary). Hence every \(p\mid N\) is larger than the
whole attempted interval. The \(R_K\) candidates are therefore distinct,
nonzero, non-1 residues modulo any fixed \(p\mid N\).

If a candidate fails the local condition and no proper gcd occurs, then for
some \(e\le K\) its power gcd contains \(p\); because the gcd is not proper,
it must be \(N\). In particular the candidate is one of the
\(B_{K,p}\le R_K-1\) bad residues modulo the fixed \(p\). There are
\(R_K\) candidates, so at least one must complete with every gcd equal to 1.
That candidate has local order greater than \(K\) at every prime divisor.

The exact worst-case counts for this sharp elementary scan are:

- candidate attempts: \(R_K\);
- bad non-1 roots at a fixed prime: \(B_{K,p}\le R_K-1\);
- power-gcd rounds: at most \(K R_K\);
- base gcd calls: at most \(R_K\).

Also,

\[
R_K+1
=2+\sum_{m=2}^K\varphi(m)
\le 2+\frac{K(K-1)}2
\le K^2+K.
\]

Thus this elementary scan already returns a factor, a correct prime report,
or an ordinary all-local integer in the V1 height window. If one enumerates
the whole displayed V1 window \(2\le a\le K^2+K\), it contains exactly
\(K^2+K-1\) candidates; that larger count is not needed for the pigeonhole
argument. Conversely, the allowed statement does not expose the exact
number of candidates actually examined inside Nir's proposition. It exposes
only its output interval. One must not identify the interval size with
Nir's internal attempt count.

The elementary construction uses

\[
O(KR_K\,\mathsf M(n)\log n)+n^{O(1)}
=O(K^3\mathsf M(n)\log n)+n^{O(1)}
\]

bit operations. The primality term handles the prime endpoint, where an
order greater than \(K\) need not exist. On a composite factor-free path,
the preceding argument also shows that every processed base is below a
prime factor and hence below \(N\), so the arithmetic stays at \(O(n)\)
bits.

## 3. Reconstruction of Theorem 1

Take Nir Proposition 1.2 exactly as quoted: for positive \(D<N\), it
deterministically returns a factor, a correct prime report, or a unit \(a\)
with

\[
\operatorname{ord}_N(a)>D,
\qquad 2\le a\le D^2+D,
\]

in

\[
O(D^{5/2+o(1)}\operatorname{polylog}N)
\]

time. Preserve the factor and prime outcomes. Only on the unit outcome run
the local certificate scan of Section 1.

The scan can never return \(N\), so it either returns a proper factor first
or completes and proves \(\mathsf{Local}_D(a;N)\). It does not change the
ordinary representative, so the bound \(2\le a\le D^2+D\) survives.
Choosing a standard polynomial multiplication algorithm, the added
\(O(D\mathsf M(n)\log n)\) work is absorbed by
\(O(D^{5/2+o(1)}\operatorname{polylog}N)\). This proves the exact trichotomy
and cost in V1 Theorem 1, conditional on the quoted proposition.

The chronology matters. A proper gcd is returned as soon as it appears.
The algorithm calls an integer an all-local witness only after all \(D\)
tests equal 1. It never discards a revealed factor in order to preserve a
preferred source outcome.

The elementary construction in Section 2 proves the same qualitative
trichotomy and at least the same height bound, but with cubic rather than
\(D^{5/2+o(1)}\) dependence. Therefore it does not independently establish
Nir's sharper quantitative claim.

## 4. Reconstruction of Theorem 2

Take Harvey--Hittmeir Theorem 1.1 exactly as quoted: for
\(N\ge3\) and \(1\le D<N-1\), it returns either a nontrivial factor or a
unit \(\alpha\bmod N\) with \(\operatorname{ord}_N(\alpha)>D\). Its stated
source time and space are

\[
T_{\rm HH}(N,D)
=O\!\left(
\frac{D^{1/2}\log D}{\sqrt{\log\log D}}\log N
\right)
\]

and

\[
O\!\left(
\frac{D^{1/2}}{\sqrt{\log\log D}}\log N
\right),
\]

with the statement's convention for \(\log\log D\) and the finite-\(D\)
qualification recorded above.

Preserve a factor outcome. On a unit outcome, run exactly the Section 1
scan. The same contradiction excludes \(g_e=N\), and completion proves
\(\mathsf{Local}_D(\alpha;N)\). Adding the source and postprocessor costs
gives

\[
O\!\left(
\frac{D^{1/2}\log D}{\sqrt{\log\log D}}\log N
+D\mathsf M(n)\log n
\right),
\]

which is V1 Theorem 2.

The local scan has linear dependence on \(D\), whereas the quoted global
source has square-root dependence up to logarithms. Thus the explicit scan
is the large-\(D\) bottleneck when bit-arithmetic factors are treated in the
usual way. The resulting \(D^{1+o(1)}\) dependence is asymptotically below
Nir Proposition 1.2's \(D^{5/2+o(1)}\) dependence and the elementary scan's
\(D^{3+o(1)}\) dependence. These are upper-bound comparisons, not lower
bounds, and the interfaces are not identical:

- Nir Proposition 1.2 covers positive \(D<N\), can report prime, and
  supplies the ordinary height \(D^2+D\).
- Harvey--Hittmeir covers \(1\le D<N-1\), has no prime-report outcome in the
  quoted interface, and supplies only a residue class. Its canonical
  representative is below \(N\), but the interface gives no uniform
  \(D^{O(1)}\) height theorem.

The quoted descriptions of small scanned bases, synchronized exact orders,
lcm combination, and an arithmetic-progression factor branch are compatible
with this distinction, but they cannot be independently proved without the
excluded paper.

## 5. Numerical-QP scale

From the definition of \(n\), \(\log N=\Theta(n)\) and
\(\log\log N=\Theta(\log n)\). Fix a numerical-QP function

\[
D(n)\le \exp((\log n)^c)
\]

for some fixed \(c\). Then \(\log D=o(n)\), so \(D<N-1\) for all
sufficiently large positive admissible inputs. Fixed powers of \(D\),
polynomials in \(n\), and their products are still numerical-QP. Therefore:

- Nir Proposition 1.2 plus the local scan is numerical-QP;
- Harvey--Hittmeir plus the local scan is numerical-QP;
- the elementary scan is also numerical-QP; and
- \(D^2+D\), the ordinary height in Theorem 1, is numerical-QP.

Nir Theorem 1.1 has the strict lower threshold

\[
D>\exp\!\sqrt{2\log N\log\log N}.
\]

At the threshold,

\[
\log D
=\Theta(\sqrt{n\log n}),
\]

which exceeds \((\log n)^c\) for every fixed \(c\). Hence no asymptotic
choice can be both numerical-QP in \(n\) and satisfy that threshold. The
statement's claim is about Nir's main-theorem parameter domain, not about
the arbitrary-\(D\) proposition. The threshold also makes every fixed
\(\operatorname{polylog}N\) factor equal to \(D^{o(1)}\), which explains
the quoted absorption into \(D^{1/2+o(1)}\).

## 6. Fixed polynomial-\(N\) scale and the V2 repair

Let \(D=N^\delta\) in the standard integer-rounded asymptotic sense, with
fixed \(0<\delta<1\). Then

\[
\frac{D}{N-1}=N^{\delta-1}(1+o(1))\longrightarrow0,
\]

so \(D<N-1\) for all sufficiently large \(N\). Substitution into the
Harvey--Hittmeir source bound gives

\[
D^{1/2}
\frac{\log D}{\sqrt{\log\log D}}
\log N
=N^{\delta/2+o(1)}.
\]

Using \(n=\Theta(\log N)\) and a polynomial multiplication bound, the
explicit local scan costs

\[
D\mathsf M(n)\log n=N^{\delta+o(1)}.
\]

These are precisely upper-bound accounting statements. They do not assert
necessity. For comparison, the arbitrary-\(D\) Nir route costs
\(N^{5\delta/2+o(1)}\), and the elementary route costs
\(N^{3\delta+o(1)}\). Nir's main-theorem threshold is eventually satisfied
for every fixed \(\delta>0\); its quoted global-source cost then becomes
\(N^{\delta/2+o(1)}\), but the allowed interface does not attach the
\(D^2+D\) ordinary-height promise to that main theorem. Applying the
explicit local scan would again add \(N^{\delta+o(1)}\).

At \(\delta=1\), the literal choice is \(D=N\), which violates
\(D<N-1\). Every \(\delta>1\) also violates it for large \(N\). Algebraic
substitution into the running-time formula cannot enlarge an algorithm's
input domain. Thus V1's unqualified phrase “fixed \(\delta>0\)” was too
broad, and V2's restriction \(0<\delta<1\) is the correct endpoint repair.
The excluded case \(\delta=0\) would be a constant-\(D\) regime, not the
positive polynomial regime being compared.

Numerical-QP and fixed polynomial-\(N\) scales are very different here.
Since \(N=2^{\Theta(n)}\), \(N^\delta=\exp(\Theta(n))\) is exponential in
the input bit length, while numerical-QP is only
\(\exp((\log n)^{O(1)})\).

## 7. Synchronized-order capacity

Assume an accepted exact order \(m_i\) is the same modulo every prime
divisor \(p\mid N\). Lagrange's theorem in \(\mathbb F_p^*\) gives
\(m_i\mid p-1\). Therefore

\[
M=\operatorname{lcm}(m_1,\ldots,m_t)
\quad\Longrightarrow\quad
M\mid p-1
\quad\text{for every }p\mid N.
\]

For \(N=pq\), this gives

\[
M\mid d:=\gcd(p-1,q-1).
\]

Because \(p\equiv q\equiv1\pmod d\), one also has
\(N=pq\equiv1\pmod d\), hence

\[
M\mid d\mid N-1.
\]

This is common order capacity, and every rational prime divisor of \(M\)
already divides \(N-1\). It does not create new rational-prime support.

The saturation claim can be checked valuation by valuation. If
\(\ell\mid N-1\) and \(p\mid N\), then \(p-1<N\). Writing
\(e=v_\ell(p-1)\),

\[
e<\log_\ell N\le\log_2N<n.
\]

Since \(v_\ell(N-1)\ge1\),

\[
v_\ell((N-1)^n)=n\,v_\ell(N-1)\ge e.
\]

Thus \((N-1)^n\) already contains the full \(\ell\)-primary part of every
\(p-1\) whenever \(\ell\mid N-1\). Multiplication by any \(M\mid N-1\)
cannot change \(\gcd((N-1)^n,p-1)\). This proves Proposition 4 and its
F259/F260 saturation comparison from the stated premises.

## 8. Bare global order does not supply the missing transfers

For the supplied example

\[
N=77=7\cdot11,\qquad D=10,\qquad a=2,
\]

one has \(2^3\equiv1\pmod7\) with no smaller positive exponent, and
\(2^5\equiv-1\pmod{11}\). Hence

\[
\operatorname{ord}_7(2)=3,
\qquad
\operatorname{ord}_{11}(2)=10,
\qquad
\operatorname{ord}_{77}(2)=\operatorname{lcm}(3,10)=30>10.
\]

This one example proves that the bare global predicate does not imply the
all-local predicate or equality of local orders. It also does not imply
\(D\)-rough order: every prime divisor of 30 is at most 10.

With the residual quantities displayed in the statement,

\[
d=\gcd(6,10)=2,
\qquad s_7=3,
\qquad s_{11}=5,
\]

the returned ordinary base satisfies

\[
\gcd(2,s_7)=\gcd(2,s_{11})=1.
\]

Therefore the base itself does not absorb either nontrivial residual in the
sense asserted by the statement. Because “P205 word” is not defined in the
allowed files, the strongest statement-only conclusion is the deliberately
narrow one: neither a high-order predicate nor the displayed base provides
the claimed residual divisibility without an additional construction and
transfer lemma. This does not prove that no derived word can work.

The other named-lane boundaries have the same logical form:

- **P161:** large order need not be rough order, as the example proves. A
  primary-support filter needs extra information.
- **P162--P164:** long local actions do not by themselves specify a support
  list, resultant certificate, recursive child, or independent direction.
- **P165 and P212:** a deterministic bounded-height output is a point source
  conditional on its input, not a fresh uniform sample. No uniform or
  inverse-QP hit probability follows. This grammar mismatch neither proves
  failure of the deterministic source nor refutes a theorem about fresh
  uniform samples.
- **P166--P170:** an order certificate contains no stated Jacobi-sum,
  decoder, hidden-support localization, ACD-cluster, or separating
  representation map.
- **P187:** the common divisibility \(M\mid p-1\) is symmetric in all hidden
  prime factors and supplies no stated orientation map.
- **P205:** common capacity and a residual-absorbing public word are
  different interfaces. Proposition 4 gives only the former.
- **F259/F260:** the synchronized \(M\) adds nothing to the stated saturated
  support, and no theorem maps the high-order base to a Pell value, carry,
  inverse quotient, collision, determinant, or P205 word.

These are failures of implication from the source interface alone. They are
not impossibility theorems and do not say that the named lanes exhaust all
future uses.

## 9. Why this is not a factoring theorem

Both source interfaces are disjunctive. They may return a factor, but they
may instead return a high-order unit; Nir may also certify primality. The
local postprocessor improves the unit branch as follows:

\[
\text{global high order}
\longrightarrow
\begin{cases}
\text{proper gcd and factor},&\text{if a local failure is exposed},\\
\text{all-local high-order witness},&\text{if every gcd is 1}.
\end{cases}
\]

Nothing in the second branch extracts a factor. An all-local witness is
compatible with a composite input whenever its prime factors have enough
multiplicative-order capacity. Likewise, Proposition 4 supplies a symmetric
common divisor of the hidden \(p-1\)'s, not a separation of the hidden
factors. Hence the packet proves a deterministic source interface that can
incidentally factor, not an algorithm guaranteed to factor every composite
\(N\).

The search-admission condition in the statement is consequently a policy
boundary: before changing a frozen grammar, one must add a proved map from
the biased source to an explicit carry, inverse quotient, or determinant,
together with an all-input or inverse-QP divisibility law. Neither such map
nor such law follows from order alone.

All remaining exclusions are consistent with the positive results. Every
displayed running time is an upper bound. No argument above proves a
deterministic lower bound, an order-search lower bound, a source
impossibility theorem, a P205-word impossibility theorem, or a carry
distribution theorem. It also does not exclude batch certificates, new
recursions, symbolic identities, nonlinear carries, or source-aware
decoders.

## Seal declaration

This reconstruction was finalized from the two authenticated statement
files only. It was sealed before any comparison with a proof or audit file.
