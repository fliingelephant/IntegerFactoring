# Proof of F272 V2

## 1. Prime mass, sets, and binary length

For every prime \(p\leq X\), the \(X\)-divisor property supplies a
\(d\in D\) divisible by \(p\). Therefore every such prime divides

\[
 P_D=\prod_{d\in D}d.
\]

Distinct primes are pairwise coprime, so

\[
 \prod_{p\leq X\atop p\ {\operatorname{prime}}}p
 \mid P_D.
\tag{27}
\]

Taking base-two logarithms gives

\[
 \vartheta_2(X)
 \leq\sum_{d\in D}\log_2d.
\tag{28}
\]

Every \(d\in D\) has at most \(L\) bits, hence \(d<2^L\). Thus

\[
 \sum_{d\in D}\log_2d<ML,
\tag{29}
\]

which proves (7).

Passing from ordered pair differences to the set \(D\) collapses only
duplicates. Consequently

\[
 M\leq K\leq|S|\,|T|,
\]

and (8) follows. The same argument applies to multiset inputs after replacing
them by their supports. Signs have already been removed by absolute value.
Zero pairs are absent by definition, while \(d=1\) is harmless because it
has logarithmic mass zero and bit length one.

If \(|s|,|t|<2^B\), then

\[
 0<|s-t|\leq|s|+|t|<2^{B+1}.
\]

Every nonzero difference has at most \(B+1\) bits, proving (9).

Let \(Q(n_X)=2^{C(\log_2(n_X+1))^k}\) be any fixed
quasipolynomial. Since \(n_X=\Theta(\log X)\),

\[
 \log_XQ(n_X)
 =O\!\left(
 \frac{(\log\log X)^k}{\log X}
 \right)=o(1).
\tag{30}
\]

A fixed product of quasipolynomial bounds in \(n_X\) is therefore
\(X^{o(1)}\). If \(|S|,|T|,L\) all had such bounds, (8) would contradict
the standard lower bound \(\vartheta_2(X)\geq cX\) on every unbounded
sequence. Rank and grammar never entered the proof.

## 2. Explicit factor output and fixed-machine time

Conceptually invoke the declared procedure on all \(K\) nonzero ordered
pairs. For every prime \(p\leq X\), at least one output is the complete
factorization of a difference divisible by \(p\). That output explicitly
writes the binary name of \(p\). Across all calls, the prime-name bits alone
therefore total at least

\[
 \sum_{p\leq X}
 \bigl(\lfloor\log_2p\rfloor+1\bigr)
 \geq\vartheta_2(X).
\tag{31}
\]

If each call writes at most \(F_{\rm out}\) bits, the aggregate output has
at most \(KF_{\rm out}\) bits. This proves (11). Equal differences,
duplicate pair presentations, and repeated prime names can only increase
the actual aggregate output. Factoring \(|s-t|\) handles either sign, and
no zero factorization is requested.

Fix a sequential bit machine and a constant \(C_0\) such that one step
writes at most \(C_0\) output bits. A call of at most
\(F_{\rm time}\) steps writes at most \(C_0F_{\rm time}\) bits. Hence

\[
 C_0KF_{\rm time}\geq\vartheta_2(X),
\tag{32}
\]

which proves (12). The constant is fixed independently of \(X,S,T\), so it
does not affect any exponent or quasipolynomial conclusion.

If a different output contract permits references to a shared dictionary,
then (11) is no longer a literal per-call statement. However, every covered
prime name must occur at least once in the charged dictionary plus outputs.
Their aggregate materialized length remains at least \(\vartheta_2(X)\).
An uncharged nonuniform dictionary is outside the uniform bit model.

## 3. Prime-pair incidence

For \(d\in D\), define

\[
 r(d)=|\{p\in\mathcal P:p\mid d\}|.
\]

The counted primes are distinct and each is at least \(a\sqrt X\). Their
product divides \(d\), so

\[
 (a\sqrt X)^{r(d)}
 \leq\prod_{p\in\mathcal P\atop p\mid d}p
 \leq d\leq H.
\tag{33}
\]

Thus \(r(d)\leq h\).

For every unordered pair of distinct \(p,q\in\mathcal P\),

\[
 pq\leq b^2X\leq X.
\]

The divisor property supplies a \(d\in D\) divisible by \(pq\). One fixed
\(d\) contains exactly \(\binom{r(d)}2\) such pairs. Counting incidences,
allowing a pair to be covered more than once, gives

\[
 \binom v2
 \leq\sum_{d\in D}\binom{r(d)}2
 \leq M\binom h2.
\tag{34}
\]

This proves (15), including the vacuous case \(v<2\), without an
intersection hypothesis or a rank assumption.

## 4. Exponent consequences

Under (16), positivity gives

\[
 H<\max_{u\in S\cup T}u,
 \qquad
 \log H\leq X^{\alpha+o(1)},
 \qquad
 M,K\leq X^{2\beta+o(1)}.
\tag{35}
\]

Equations (7), (6), and (35) imply

\[
 X^{1+o(1)}
 \leq X^{\alpha+2\beta+o(1)},
\]

so \(\alpha+2\beta\geq1\).

For fixed \(0<a<b\leq1\), the prime number theorem in the fixed band gives

\[
 v=\pi(b\sqrt X)-\pi(a\sqrt X)=X^{1/2+o(1)}.
\tag{36}
\]

Also

\[
 h\leq
 \frac{X^{\alpha+o(1)}}{(1/2+o(1))\log X}
 =X^{\alpha+o(1)}.
\tag{37}
\]

If \(h<2\) infinitely often, (15) fails once \(v\geq2\). Otherwise
(15), (35)--(37) imply

\[
 X^{1+o(1)}
 \leq X^{2\alpha+2\beta+o(1)},
\]

and \(\alpha+\beta\geq1/2\).

If every factor-output call takes at most
\(X^{\gamma+o(1)}\) steps on the fixed machine, (12), (6), and
\(K\leq X^{2\beta+o(1)}\) give

\[
 X^{1+o(1)}
 \leq X^{\gamma+2\beta+o(1)},
\]

which proves (19). The fixed constant \(C_0\) disappears into the
\(X^{o(1)}\) factor.

At \((1/3,1/3)\),

\[
 \alpha+2\beta=1,
 \qquad
 \alpha+\beta=2/3>1/2.
\]

Thus only (17) is saturated. Neither inequality settles existence at this
point.

The He--Sahai AP lower bound and the Umans--Wang factoring reduction are
external literature claims recorded in the statement and provenance. F272
V2 does not derive either. Conditional on the latter reduction, substituting
\(\alpha=\beta=1/3\) into (21) gives \(N^{1/6+o(1)}\), which is exponential
in \(\log N\).

## 5. Prime separation

For distinct primes \(p,q\leq X\), a separating integer exists exactly when
\(c(p)\ne c(q)\). Thus all \(\pi(X)\) codewords are distinct. Since the
binary cube has \(2^m\) words,

\[
 m\geq\lceil\log_2\pi(X)\rceil.
\]

At most one prime has the all-zero codeword. Every other prime divides at
least one \(A_i\), so its binary name appears in at least one complete
factorization. The aggregate output length is at least

\[
 \vartheta_2(X)-\log_2X.
\tag{38}
\]

The upper bound \(mF_{\rm out}\) proves (24). Applying the same fixed
write-rate constant \(C_0\) proves (25). This is a static statement only.

## 6. A sufficient interval-product interface

Assume a uniform evaluator returns

\[
 E(a,b,d)=\prod_{j=a}^{b}j\pmod d
\]

in time quasipolynomial in \(\log b+\log d\). First apply a deterministic
polynomial-time primality test. For composite \(N\), put
\(X=\lfloor\sqrt N\rfloor\) and compute

\[
 g=\gcd(E(1,X,N),N).
\]

A least prime factor of \(N\) is at most \(X\), so \(g>1\). If \(g<N\),
return it.

Suppose \(g=N\). Maintain a nonempty interval \(I\subseteq[1,X]\) whose
exact product is divisible by \(N\). Split it into two nonempty consecutive
subintervals \(I=I_0\sqcup I_1\) and compute

\[
 g_0=
 \gcd\!\left(
 \prod_{j\in I_0}j\bmod N,
 N
 \right).
\tag{39}
\]

If \(1<g_0<N\), return it. If \(g_0=N\), continue with \(I_0\). If
\(g_0=1\), then coprimality and divisibility of the parent product imply
that the product over \(I_1\) is divisible by \(N\), so continue with
\(I_1\).

This is one path of depth \(O(\log X)\). It cannot reach a singleton
\(I=\{j\}\), because its invariant would give \(N\mid j\leq X<N\).
Therefore a proper divisor appears earlier. Recursively applying the
procedure to the two proper factors gives complete factorization. There are
at most \(O(\log N)\) nontrivial factor nodes, and every call has input bit
length at most that of \(N\), so the total remains quasipolynomial.

This proves a reduction from the evaluator to deterministic
quasipolynomial integer factoring. It makes the evaluator factoring-hard.
No reverse reduction is proved.

The mass theorem charges expanded cover values. The output theorem charges
complete explicit prime lists. A modular evaluator that produces neither is
outside both theorems. This proves only that (26) is one precise sufficient
escape from those hypotheses. It does not prove uniqueness and gives no
circuit lower bound for any other succinct mechanism.

