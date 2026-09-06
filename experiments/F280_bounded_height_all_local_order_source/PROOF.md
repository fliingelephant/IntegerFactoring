# Proof of F280

## 1. The local gcd postprocessor

Let \(a\in\mathbb Z_N^*\) satisfy

\[
 \operatorname{ord}_N(a)>D.
\tag{30}
\]

For \(1\leq e\leq D\), compute

\[
 g_e=\gcd(a^e-1,N).
\tag{31}
\]

If \(1<g_e<N\), then \(g_e\) is a verified nontrivial factor. The other
two possibilities are \(g_e=1\) and \(g_e=N\). The second is impossible:
it would imply

\[
 a^e\equiv1\pmod N,
\]

and hence \(\operatorname{ord}_N(a)\mid e\leq D\), contrary to (30).

Suppose no proper factor occurs. Then every \(g_e=1\). Fix a rational prime
\(p\mid N\). If \(r=\operatorname{ord}_p(a)\leq D\), then

\[
 p\mid a^r-1,
\]

so \(p\mid g_r\). This contradicts \(g_r=1\). Therefore

\[
 \operatorname{ord}_p(a)>D
\]

for every rational prime \(p\mid N\). This proves the mathematical
postprocessor.

The argument also covers nonsquarefree \(N\). If a prime but not its full
prime-power component divides \(a^e-1\), the gcd is still a proper factor.
The conclusion concerns the rational-prime reductions, exactly as stated.

To evaluate the scan, maintain

\[
 x_0=1,\qquad x_e=ax_{e-1}\bmod N.
\tag{32}
\]

There are \(D\) modular multiplications and \(D\) gcd computations on
\(O(n)\)-bit integers. This gives the bound (3). The proof does not invoke a
batched or sublinear scan.

## 2. Proof of Theorem 1

Apply Nir Proposition 1.2 to \((N,D)\). Its hypotheses are precisely that
\(D,N\) are positive and \(D<N\). It returns one of:

1. a nontrivial factor;
2. the report that \(N\) is prime; or
3. a unit \(a\) of global order greater than \(D\).

The proof of Nir's proposition scans the ordinary integers

\[
 2,3,\ldots,D^2+D.
\]

Therefore the third outcome satisfies the height bound in (12). Apply the
postprocessor of Section 1. It returns a factor or proves
\(\mathsf{Local}_D(a;N)\). This proves every output claim in Theorem 1.

Nir's source construction costs

\[
 O(D^{5/2+o(1)}\operatorname{polylog}N).
\]

The added scan costs (3), which is absorbed by the displayed bound under
the same standard fast-integer-arithmetic convention. This proves (13).

The equalities (14) are exactly the surviving scan transcript. They can be
verified by recomputation. No claim of a shorter certificate is needed.

## 3. Proof of Theorem 2

Apply Harvey--Hittmeir Theorem 1.1. Its hypotheses are (4). If it returns a
factor, stop. Otherwise it returns a unit \(\alpha\) satisfying (5).

Apply Section 1 with \(a=\alpha\). A proper gcd factors \(N\). If no proper
gcd occurs, the section proves (15). Adding the source cost (6) and scan
cost (3) gives (16).

The Harvey--Hittmeir theorem returns a residue class. Its canonical
representative is below \(N\). Its theorem statement gives no bound by a
fixed power of \(D\). This proves the stated height distinction.

The distinction is also visible inside Algorithm 3.1. Its direct
high-order escape returns a scanned integer
\(\beta\leq\lceil D^{1/3}\rceil\). A different branch uses Lemma 2.2 to
combine primary order parts into a residue of lcm order. Since the theorem
does not promise which branch occurs, the small bound from the first branch
cannot be promoted to a theorem-wide output bound.

## 4. Proof of Corollary 3

Let

\[
 D\leq\exp((\log n)^C)
\tag{33}
\]

for one fixed \(C\). Every fixed positive power of \(D\), every polynomial
in \(n\), and every fixed product of these quantities remains
\(\exp((\log n)^{O(1)})\). Therefore (13), (16), and the height
\(D^2+D\) are numerical quasipolynomial. Since \(N=2^{\Theta(n)}\), every
such \(D\) is smaller than \(N-1\) for all sufficiently large inputs.

For Nir's main theorem, (8) gives

\[
 \log D>\sqrt{2\log N\log\log N}
       =\Theta(\sqrt{n\log n}).
\tag{34}
\]

For every fixed \(C\),

\[
 {\sqrt{n\log n}\over(\log n)^C}\longrightarrow\infty.
\]

Thus its admissible \(D\) eventually exceeds every fixed numerical-QP
bound. Proposition 1.2, not Theorem 1.1, is the Nir interface that applies
to the QP range.

If \(D=N^\delta\), substitution into (6) gives

\[
 T_{\rm HH}(N,D)=N^{\delta/2+o(1)}.
\]

Substitution into (3) gives \(N^{\delta+o(1)}\). These are only the costs of
the named constructions.

## 5. Proof of Proposition 4

For each accepted low-order base \(b_i\), let

\[
 m_i=\operatorname{ord}_N(b_i).
\]

The prime-divisor gcd screens in Harvey--Hittmeir Lemma 2.3, also restated
as Nir Lemma 2.3, certify

\[
 \operatorname{ord}_p(b_i)=m_i
 \quad\text{for every rational prime }p\mid N.
\tag{35}
\]

Every multiplicative order modulo \(p\) divides \(p-1\). Hence

\[
 m_i\mid p-1
 \quad\text{for every }i\text{ and every }p\mid N.
\]

Taking the least common multiple proves (21).

Now let \(N=pq\). Equation (21) gives

\[
 M\mid\gcd(p-1,q-1)=d.
\]

Also

\[
 N-1=pq-1=q(p-1)+(q-1),
\]

so every common divisor of \(p-1\) and \(q-1\) divides \(N-1\). This
proves (23).

It remains to check the saturated-baseline claim. Let \(\ell\mid N-1\) be
prime. For any rational prime \(p\mid N\),

\[
 \ell^{v_\ell(p-1)}\leq p-1<N<2^n.
\]

Thus \(v_\ell(p-1)<n\). Since \(v_\ell(N-1)\geq1\),

\[
 v_\ell((N-1)^n)\geq n>v_\ell(p-1).
\tag{36}
\]

Every prime divisor of \(M\) divides \(N-1\). Equation (36) shows that the
baseline already contains its complete primary contribution to every
\(p-1\). Consequently

\[
 \gcd((N-1)^nM,p-1)
 =\gcd((N-1)^n,p-1).
\tag{37}
\]

The same holds for every other hidden prime. This proves the exact baseline
statement.

## 6. Proof of Proposition 5

For \(N=77\), the order of \(2\) modulo \(7\) is \(3\), because

\[
 2^3\equiv1\pmod7
\]

and neither exponent \(1\) nor \(2\) returns. Modulo \(11\), the powers

\[
 2,4,8,5,10,-2,-4,-8,-5,1
\]

show that the order is \(10\). The Chinese remainder theorem gives

\[
 \operatorname{ord}_{77}(2)=\operatorname{lcm}(3,10)=30.
\]

For \(D=10\), the global order exceeds \(D\), while both local orders are
at most \(D\) and are unequal. The prime divisors of \(30\) are
\(2,3,5\), all at most \(D\). This proves the first three
non-implications.

For the P205 notation,

\[
 d=\gcd(7-1,11-1)=2,
 \qquad
 {7-1\over d}=3,
 \qquad
 {11-1\over d}=5.
\]

The ordinary returned base \(a=2\) is coprime to both residuals. Thus the
assignment \(W=a\) absorbs neither residual on this valid high-global-order
instance. This refutes the bare-base implication.

The source theorems return a residue and an order inequality. They do not
define any other integer map \(W=W(N,a,\text{transcript})\), and they prove
no divisibility property for such a map. Therefore a direct call from their
declared output interface into P205 is not specified. This is an interface
fact, not a theorem that every future map must fail.

## 7. Lane and search boundaries

The comparisons in Statement Section 8 follow by matching declared output
fields.

Theorem 1 outputs \(N,D,a\) and the local nonreturn transcript (14). It does
not output the factorization of any local order, a list of its prime
support, a recursive modulus, an ACD cluster, a Jacobi segment value, a
Paley coefficient, a coherent representation, or a P205 word. Proposition
4 describes the separate low-order synchronized transcript. It contains
only common divisibility data.

The bounded integer \(a\) is deterministic and biased. Hence a theorem whose
hypotheses require fresh uniform units cannot be applied to it. The failure
of those hypotheses gives no positive distribution law for \(a\), its
inverse quotient, or any carry derived from it.

A numerical experiment can test candidate transfers, but it cannot supply
the all-input or inverse-QP law required for a factoring transition. The
order theorem by itself does not identify a candidate transfer with such a
law. The theory gate in (29) is therefore a search-admission rule, not an
impossibility theorem.
