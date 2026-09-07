# Independent reconstruction of the two-source partial-FacRoot reduction

## Reconstruction boundary

- Input: `STATEMENT_ONLY.md`
- Input SHA-256: `0cc27150004a4d59380cdf50f5a413751ca997c473595268df0d0e43ec706239`
- Candidate proofs, other packet files, shared ledgers, and code were not read.

Throughout, write

\[
N=\prod_{i=1}^s p_i^{e_i},\qquad s\geq 2,
\]

where the \(p_i\) are distinct odd primes. Probabilities involving \(A\) also
average over its private random tape. A verified-factor outcome and a
verified-root outcome are disjoint under the priority rule in the statement.

## 1. Group facts and the hidden-root experiment

CRT gives

\[
U=(\mathbb Z/N\mathbb Z)^\times
  \cong \prod_{i=1}^s (\mathbb Z/p_i^{e_i}\mathbb Z)^\times.
\]

For an odd prime power, the kernel of squaring on the unit group is
\(\{+1,-1\}\). Hence the squaring map \(U\to S\) is onto with fibers of
constant size \(2^s\), and

\[
[U:S]=2^s.
\]

Every square has Jacobi symbol \(+1\), so \(S\subseteq J\). The Jacobi
character on \(U\) is either trivial or has image \(\{+1,-1\}\). Therefore
\([U:J]\) is respectively \(1\) or \(2\), and

\[
q:=\Pr_{a\leftarrow J}[a\in S]=\frac{|S|}{|J|}
   \in\{2^{-s},2^{1-s}\}\subseteq (0,1/2].                 \tag{1}
\]

In particular, conditioning a uniform element of \(J\) on membership in
\(S\) gives the uniform distribution on \(S\).

If \(r\) is uniform in \(U\) and \(a=r^2\), then constant fiber size makes
\(a\) uniform in \(S\). Conditional on a fixed \(a\), the hidden \(r\) is
uniform among the \(2^s\) square roots of \(a\).

Fix such an \(a\) and any verified root \(y\) returned by \(A\). The procedure
\(A\) receives neither the mode nor \(r\), and its random tape is independent
of the sampling tape. Thus, conditional on \(a\) and on everything that fixes
\(y\), the root \(r\) remains uniform in that fiber. Relative to \(y\), its
CRT components are independent uniform signs. The value
\(\gcd(y-r,N)\) is:

- \(N\) when all signs are \(+\);
- \(1\) when all signs are \(-\); and
- a proper nontrivial divisor for every mixed sign vector.

Consequently, for every fixed verified \(y\),

\[
\Pr\bigl(1<\gcd(y-r,N)<N\mid a,y\bigr)
 =1-\frac{2}{2^s}=1-2^{1-s}\geq \frac12.                 \tag{2}
\]

This pointwise conditioning needs the hidden root to remain private and the
coins to remain independent. Merely telling \(A\) that this is S mode would
not change (2): conditional on \(a\), it would still have no information about
which root \(r\) was sampled. Mode invisibility is used separately below. It
makes the conditional behavior of \(A\) on a fixed \(a\in S\) identical in
the J and S experiments, which is needed for (3).

## 2. Bounded two-source success

For the capped machine, let \(f_S,r_S\) be its verified-factor and
verified-root probabilities on uniform \(a\in S\), using the same outcome
priority as for \(f_J,r_J\). A verified root cannot occur when \(a\notin S\).
The input law and the law of \(A\)'s coins are identical after fixing \(a\) in
the two modes. Therefore

\[
r_J=q r_S.                                                  \tag{3}
\]

Let \(c_s=1-2^{1-s}\). The ideal two-mode attempt has factor probability

\[
\begin{aligned}
p_{\rm mix}
 &=\frac12 f_J+\frac12(f_S+c_s r_S)\\
 &\geq \frac12f_J+\frac{c_s}{2q}r_J\\
 &\geq \frac12f_J+\frac12r_J
  =\frac{\delta_J}{2}.                                    \tag{4}
\end{aligned}
\]

The penultimate inequality uses both \(c_s\geq 1/2\) and \(q\leq 1/2\).
No pointwise success assumption on \(A\) is present in this argument.

## 3. Sampling with no knowledge of the factors

An exact uniform nonzero residue can be generated from fair bits as follows.
Let \(n\) be the bit length of \(N\). Draw an \(n\)-bit integer \(X\) and
repeat until \(1\leq X\leq N-1\). Every accepted value is uniform in that
interval. Since \(N\) is an odd \(n\)-bit integer, \(N-1\geq 2^{n-1}\), so
each batch is accepted with probability at least \(1/2\). This step uses at
most \(2n\) fair bits in expectation.

For each accepted residue, compute \(d=\gcd(X,N)\). If \(d>1\), then
\(d<N\) because \(1\leq X<N\), so generation has already found a verified
proper factor.

In S mode, the first accepted residue is used. Conditional on \(d=1\), it is
a uniform element \(r\in U\), and the procedure supplies \(a=r^2\) to \(A\).

In J mode, after a unit is found, compute its Jacobi symbol. Accept it as
\(a\) if the symbol is \(+1\), and repeat only when the symbol is \(-1\).
If the Jacobi character is nontrivial, exactly half of the units have each
sign; if it is trivial, no unit is rejected. Thus the probability that a
nonzero-residue draw causes another J-generation iteration is at most
\(1/2\). The expected number of nonzero-residue draws is at most two, and the
accepted unit is exactly uniform in \(J\).

GCD, Jacobi, multiplication modulo \(N\), and the final decoder all have
polynomial bit cost. Including the independent fair mode bit, generation has
expected \(O(n)\) fair-bit cost and polynomial expected bit cost. It uses no
factorization of \(N\).

It remains to check that early generation factors do not dilute (4). In
either mode, let \(\rho\) be the probability of reaching the call to \(A\),
and let \(u\) be the ideal success probability conditional on reaching it.
All other terminating generation outcomes are verified factors, so the
implemented mode succeeds with probability

\[
(1-\rho)+\rho u\geq u.                                    \tag{5}
\]

The event of an infinite J-generation loop has probability zero. Hence the
implemented mixture preserves the lower bound \(\delta_J/2\), while all
generation successes and all rejected draws remain part of the same attempt.

## 4. Truncating an expected-cost procedure

Fix \(N\), and let \(C\) be the bit cost of one uncapped call on uniform
\(a\in J\), including complete output verification. Thus
\(\mathbb E C=\tau_J\). Let \(V\) be the event that the uncapped call gives a
valid prioritized output, so \(\Pr(V)=\delta_J\). Set

\[
B=\lceil 2Q(n)\rceil.
\]

The capped call retains every valid output on \(V\cap\{C\leq B\}\). Markov's
inequality and the pointwise contract \(\tau_J\leq \delta_J Q(n)\) give

\[
\begin{aligned}
\Pr(V\text{ under the cap})
 &\geq \delta_J-\Pr(C>B)\\
 &\geq \delta_J-\frac{\tau_J}{B}\\
 &\geq \frac{\delta_J}{2}.                               \tag{6}
\end{aligned}
\]

This argument does not condition the cost on success. Therefore arbitrary
correlation between a call's cost and its output is allowed. Applying the
bounded result (4) to the capped probabilities yields factor success at least
\(\delta_J/4\) per implemented attempt.

Let \(P(n)\) bound the expected generation cost and the deterministic outer
arithmetic for one attempt. Its expected cost is at most \(B+P(n)\). For
independent retries, write \((C_i,Z_i)\) for the cost and success indicator of
attempt \(i\), and \(K=\min\{i:Z_i=1\}\). Even when \(C_i\) and \(Z_i\) are
correlated within an attempt,

\[
\begin{aligned}
\mathbb E\!\left[\sum_{i=1}^K C_i\right]
 &=\sum_{i\geq1}\mathbb E[C_i\mathbf 1_{\{K\geq i\}}]\\
 &=\sum_{i\geq1}\mathbb E[C_1](1-p)^{i-1}
  =\frac{\mathbb E C_1}{p},                              \tag{7}
\end{aligned}
\]

because \(\{K\geq i\}\) depends only on earlier attempts. With
\(p\geq\delta_J/4\), this is

\[
O\!\left(\frac{Q(n)+P(n)}{\delta_J}\right).
\]

The assumptions \(\tau_J\geq1\) and
\(\tau_J/\delta_J\leq Q(n)\) imply \(1/\delta_J\leq Q(n)\). Hence the
expected restart cost is

\[
O\bigl(Q(n)^2+P(n)Q(n)\bigr),                             \tag{8}
\]

with no input averaging and no hypothesis about the mean cost conditional on
\(a\in S\).

Equation (8) accounts for executing the capped attempts after the integer
\(B\) is available. There is a uniformity qualification in the wording of the
statement. A function can have quasipolynomially bounded values and be
computable, while its particular evaluation algorithm takes more than
quasipolynomial time. Thus, if the reduction itself must calculate the literal
value \(Q(n)\), let \(E_Q(n)\) be that one-time evaluation cost. The literal
capped construction has total expected cost

\[
E_Q(n)+O\bigl(Q(n)^2+P(n)Q(n)\bigr).                    \tag{8a}
\]

The claimed quasipolynomial bound follows as written if “explicit computable
quasipolynomial” includes quasipolynomial-time evaluation, or if \(B\) is
supplied as part of the contract. A standard uniform alternative is to supply
an efficiently computable integer-valued quasipolynomial majorant
\(R(n)\geq Q(n)\), for example from explicit constants witnessing the stated
quasipolynomial growth bound, and use \(B'=\lceil2R(n)\rceil\). The Markov
argument only needs \(B'\geq2Q(n)\), so all success bounds remain unchanged,
while the expected cost becomes

\[
O\bigl(R(n)^2+P(n)R(n)\bigr).                           \tag{8b}
\]

Mere computability of \(Q\), without an efficient evaluator, a supplied cap,
or effective growth constants from which to build \(R\), is insufficient by
itself to establish a uniform quasipolynomial running time for the capped
implementation. This qualification does not affect the uncapped construction
below, which never evaluates \(Q\).

## 5. The uncapped two-engine dovetail

Continue to use the uncapped probabilities \(f_J,r_J\), so
\(f_J+r_J=\delta_J\). Let

\[
\tau_S=\mathbb E[C\mid a\leftarrow S].
\]

The nonnegativity of cost and the uniform-mixture identity for \(J\) imply

\[
q\tau_S\leq\tau_J.                                       \tag{9}
\]

Thus \(\tau_S\) can be as large as \(\tau_J/q\); it need not have a separate
uniform bound. Equation (3), now for the uncapped machine, gives
\(r_S=r_J/q\).

Let \(g(n)\) be the stated polynomial bound on expected generation and outer
verification cost. Early generation factors can only increase success, as in
(5), and can only avoid an \(A\) call. Therefore one J-engine attempt has
mean cost at most \(g+\tau_J\) and success probability at least \(f_J\). If
\(f_J>0\), (7) gives

\[
\mathbb E T_J\leq\frac{g+\tau_J}{f_J}.                    \tag{10}
\]

For the S engine, hidden-root decoding alone gives attempt success at least

\[
c_s r_S\geq\frac{r_J}{2q}.
\]

Its mean attempt cost is at most \(g+\tau_S\). If \(r_J>0\), then

\[
\begin{aligned}
\mathbb E T_S
 &\leq\frac{g+\tau_S}{r_J/(2q)}\\
 &\leq\frac{2(qg+\tau_J)}{r_J}\\
 &\leq\frac{2(g+\tau_J)}{r_J}.                            \tag{11}
\end{aligned}
\]

This is the required cancellation for rare square inputs: conditioning on
\(S\) can increase mean runtime by \(1/q\), but it increases the relevant
root rate by the same \(1/q\). No conditional-square runtime bound was used.

Regard a zero denominator in (10) or (11) as \(+\infty\). Let
\(h=g+\tau_J\). If \(f_J\geq\delta_J/3\), (10) is at most
\(3h/\delta_J\). Otherwise \(r_J>2\delta_J/3\), and (11) is less than
\(3h/\delta_J\). Thus, including the cases \(f_J=0\) or \(r_J=0\),

\[
\min\{\mathbb E T_J,\mathbb E T_S\}
 \leq\frac{3(g+\tau_J)}{\delta_J}.                        \tag{12}
\]

Give the two engines independent random tapes and store their complete machine
configurations. Alternate one bit-machine step of the J engine and one of the
S engine. Pathwise, the number of simulated engine steps before the first
factor is at most \(2\min(T_J,T_S)\). Therefore

\[
\mathbb E T_{\rm dovetail}
 \leq 2\min\{\mathbb E T_J,\mathbb E T_S\}
 \leq\frac{6(g(n)+\tau_J(N))}{\delta_J(N)},               \tag{13}
\]

up to the stated constant cost of simulating a bit-machine step. Random-bit
requests are machine steps supplied from the corresponding independent tape,
so a long or nonterminating call in one engine cannot block the other. One
engine may have zero success probability; \(\delta_J>0\) and (12) ensure that
the other then has finite expected time. The construction uses none of
\(Q,\tau_J,\delta_J\); these quantities occur only in its analysis.

Under the quasipolynomial contract, (13) is quasipolynomial because

\[
\frac{g+\tau_J}{\delta_J}
 =\frac{g}{\delta_J}+\frac{\tau_J}{\delta_J}
 \leq gQ+Q.                                                \tag{14}
\]

## 6. All-input preprocessing and recursive splitting

For a positive integer input \(M\), first remove its power of \(2\). On every
remaining cofactor \(x>1\), use exact polynomial-bit algorithms in this order:

1. Test whether \(x\) is prime. If so, record it.
2. Test whether \(x=b^k\) for integers \(b>1,k>1\). If so, factor \(b\)
   recursively and multiply all resulting exponents by \(k\).
3. Otherwise \(x\) is odd, composite, and not a perfect power. It must have at
   least two distinct prime divisors: a composite with only one distinct prime
   divisor is \(p^e\) with \(e>1\). Apply either splitter above, verify
   \(1<d<x\) and \(d\mid x\), and recursively factor \(d\) and \(x/d\).

Every reported split and every terminal primality claim is verified, so this
is Las Vegas: it never returns an incorrect factorization. Positive success
probability and finite expected split time imply almost-sure termination.
Inputs \(0,1\), signs, and the extracted factor \(2\) are handled by the usual
constant or polynomial-time conventions and do not invoke the reduction.

For the analytic complexity bound, define the monotone value envelope

\[
\widehat Q(n)=\max_{1\leq m\leq n}Q(m).
\]

It is still quasipolynomial as a value bound; this observation alone makes no
claim that evaluating it is efficient. A factor tree for an \(n\)-bit integer
has only polynomially many relevant nodes (there are at most \(n\) prime
factors with multiplicity, and perfect-power reductions strictly reduce bit
length). At a splitter node whose value and bit length are fixed by the
preceding history, the hypothesis applies pointwise to that value. Its
conditional expected capped-splitter cost is bounded by (8), or its uncapped
expected cost is bounded by (14), with its own bit length \(m\leq n\).

For the uncapped algorithm, this is a uniform quasipolynomial expression in
\(\widehat Q(n)\), which the algorithm never evaluates. For the capped
algorithm, the complete running-time conclusion additionally needs one of the
cap-uniformity conditions after (8a). Under the efficiently computable
majorant alternative, replace \(\widehat Q\) by an efficiently computable
monotone quasipolynomial majorant of \(R\) and use (8b). Summing the applicable
conditional bounds over the polynomially many nodes, together with
polynomial-time primality, integer-root, arithmetic, and verification work,
remains quasipolynomial. This uses a uniform bound for each actual recursive
input; it does not replace that requirement by an average over inputs.

## 7. Exact comparison with the statement

| Statement item | Independently derived result |
|---|---|
| Bounded ideal attempt | Factor probability at least exactly \(\delta_J/2\), equation (4). |
| Factor-free implementation | Exact uniform laws, expected polynomial bit cost, expected \(O(n)\) fair bits, and no loss in success, equation (5). |
| Capped J valid-output probability | At least exactly \(\delta_J(N)/2\), equation (6). |
| Capped factor probability per attempt | At least exactly \(\delta_J(N)/4\). |
| Expected capped-retry cost | After the cap is available, \(O(Q(n)^2+\operatorname{poly}(n)Q(n))\), equation (8), without assuming cost-success independence. Computing the literal cap adds \(E_Q(n)\), equation (8a). An efficiently computable quasipolynomial majorant gives the uniform bound (8b). |
| Uncapped dovetail | Upper bound exactly \(6(g(n)+\tau_J(N))/\delta_J(N)\) before constant machine-simulation overhead, equation (13). It does not evaluate \(Q\). |
| Zero-success engine | Allowed explicitly through the extended-value case in (12). |
| Conditional-square mean cost | No separate bound used; the \(q\)-cancellation is explicit in (9)--(11). |
| All-input result | Verified preprocessing and recursion give expected quasipolynomial bit complexity. For the capped implementation this includes the cap-uniformity qualification after (8a); the uncapped implementation needs no such qualification. |

There is no mathematical gap in the probability reduction under its
machine-model and permitted group/CRT assumptions. There are two substantive
scope qualifications. First, the capped uniform running-time conclusion needs
efficient access to a suitable cap, as detailed after (8a); bare computability
of \(Q\) does not supply that cost bound. The uncapped dovetail is unaffected.
Second, this reconstruction does not construct a procedure \(A\) with
\(\tau_J/\delta_J\leq Q\), does not claim that such a procedure exists, and
makes no novelty claim.

## Output integrity

The output-payload checksum is defined over all UTF-8 bytes above this
`## Output integrity` heading, including the newline immediately before the
heading. It permits an embedded, non-self-referential checksum of the proof.

- Output-payload SHA-256: `f16ee240af9b5958cf61e4f31b0f94f79d6bdc4d00d6e538f37cb999568c6458`
