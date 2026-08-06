# F24 — balanced-promise Boolean subset norm: exact amortization and corrected evaluators

**Family:** F02/P21-adjacent structured-product evaluator. The optional mixed-Hurwitz prefix comes from F14/P30, but it is dispensable and P31 is not used by the terminal mechanism.

**Status:** substantively revised self-audited candidate after the first hostile audit rejected the earlier evaluator obstruction; pending a fresh hostile re-audit. It is not verifier-backed and is not an all-input factoring algorithm.

**Outcome:** For independent uniform residues \(a_1,\ldots,a_K\bmod N\), the Boolean subset norm

\[
  Q_K(a_1,\ldots,a_K)
  =\prod_{\varnothing\ne S\subseteq[K]}\sum_{i\in S}a_i\pmod N
\]

is an exact cancellation-free OR of \(2^K-1\) local subset-sum tickets. On every promised input

\[
  N=pq,\qquad 53\le p<q<2p,
\]

with distinct odd primes, the terminal gcd is proper with a fixed positive one-trial probability. Thus a uniform exact polynomial-bit evaluator for \(Q_K\) would give a classical Las Vegas polynomial-time factorer for this balanced-semiprime promise.

No such evaluator is supplied. The corrected best explicit general evaluator in this report uses a balanced meet-in-the-middle product and monic multipoint evaluation in \(N^{1/4+o(1)}\) bit time and space. Gray-code enumeration gives \(N^{1/2+o(1)}\) time and polynomial space. The full Boolean diagonal, the formal minimal polynomial, and the characteristic-zero union polynomial give only representation-specific rank or degree statements; they do not lower-bound general arithmetic circuits, branching modular algorithms, or characteristic-sensitive formulas.

## 1. Scope, closest prior route, and material difference

The closest terminal route is X15/P21, not F14. P21 studies an exponentially long structured product with the desired local zero predicate and proves that fixed positive-binomial lists, a literal two-child recurrence, and several materialization shortcuts do not yield a polylogarithmic evaluator. It explicitly does not prove a circuit lower bound.

F24 differs materially from P21 in its ticket family and probability theorem. Here \(K=\Theta(\log N)\) independent random residues generate \(2^K-1=\Theta(\sqrt N)\) subset-sum tickets. Pairwise independence and a second-moment calculation prove that their union has constant probability at each unknown balanced prime. The product \(Q_K\) represents that union without cancellation.

X24/P30 and X25/P31 are relevant only as provenance for the original mixed-trace idea. They close polynomial menus of independent quaternion comparisons and fixed span-dimension pools, while leaving nonlinear joint decoders open. Once each retained mixed trace is multiplied by an independent uniform residue, however, every Hurwitz-specific distributional feature disappears. Direct sampling gives exactly the same \(a_i\) law and is therefore the clean theorem.

The promise is deliberately narrow. Nothing below supplies the all-input success theorem required by `PROMPT.md`.

## 2. Corrected theorem

Let

\[
  n=\lceil\log_2(N+1)\rceil,
  \qquad h=\lfloor\sqrt N\rfloor,
  \qquad b=\lfloor\log_2h\rfloor,
  \qquad K=b-3.
\]

Under the promise \(53\le p<q<2p\), one has \(K\ge2\). Put

\[
  T=2^K,\qquad m=T-1.
\]

In one trial, draw \(a_1,\ldots,a_K\) independently and exactly uniformly from \(\mathbb Z/N\mathbb Z\). For every nonempty \(S\subseteq[K]\), put

\[
  L_S=\sum_{i\in S}a_i\pmod N
\]

and evaluate

\[
  Q_K=\prod_{\varnothing\ne S\subseteq[K]}L_S\pmod N.
\]

Finally compute \(d=\gcd(Q_K,N)\). Return \(d\) if \(1<d<N\), and otherwise restart with fresh independent residues.

> **Corrected F24 theorem.** If \(N=pq\) with distinct odd primes \(53\le p<q<2p\), then
>
> \[
>   \Pr\bigl(1<\gcd(Q_K,N)<N\bigr)
>   \ge
>   \delta:=
>   \frac{2}{32\sqrt2+1}
>   \left(1-\frac{\sqrt2}{8}\right)>0.
> \]
>
> Hence, conditional on a uniform exact evaluator for \(Q_K\bmod N\) with bit complexity polynomial in \(\log N\) and \(K\), the repeated procedure above is a classical Las Vegas polynomial-time factorer for this balanced distinct-odd-semiprime promise. The explicit evaluators actually supplied here are exponential in \(n\), so the theorem is not a polynomial-time factoring result even on the promise.

Sections 3 and 4 prove the probability and Las Vegas assertions with all floor losses retained.

## 3. Exact local OR and local ticket probability

For \(r\in\{p,q\}\), define

\[
  E_r=
  \{\text{some nonempty }S\subseteq[K]
      \text{ has }L_S=0\pmod r\},
\]

and let

\[
  Z_r=
  #\{\varnothing\ne S\subseteq[K]:L_S=0\pmod r\},
  \qquad
  \mu_r=\frac mr.
\]

Because \(\mathbb F_r\) is an integral domain,

\[
  Q_K\equiv0\pmod r
  \quad\Longleftrightarrow\quad
  E_r.                                                   \tag{3.1}
\]

Since \(N=pq\) is squarefree with exactly two prime factors,

\[
  1<\gcd(Q_K,N)<N
  \quad\Longleftrightarrow\quad
  E_p\mathbin\triangle E_q.                              \tag{3.2}
\]

Thus \(Q_K\) is a cancellation-free local OR: no sum of ticket values is being treated as an existence predicate.

For a fixed nonempty \(S\), the incidence vector of \(S\) is nonzero, so \(L_S\) is uniform in \(\mathbb F_r\). If \(S\ne T\), their two nonzero \(0/1\) incidence vectors are linearly independent. Indeed, scalar multiples would have the same support, and any occupied coordinate would force the scalar to be \(1\), hence the vectors to be equal. Therefore \((L_S,L_T)\) is uniform in \(\mathbb F_r^2\), and the two zero indicators are independent.

Consequently,

\[
  \mathbb E Z_r=\mu_r,
  \qquad
  \operatorname{Var}(Z_r)
  =\mu_r\left(1-\frac1r\right).
\]

The union bound and the second-moment inequality give

\[
  \frac{\mu_r}{\mu_r+1-1/r}
  \le \Pr(E_r)
  \le \mu_r.                                           \tag{3.3}
\]

The lower bound follows from

\[
  \Pr(Z_r>0)
  \ge\frac{(\mathbb E Z_r)^2}{\mathbb E Z_r^2}
  =\frac{\mu_r}{\mu_r+1-1/r}.
\]

This is the point at which exponentially many tickets are genuinely amortized: the lower bound is not inferred from a union bound.

## 4. Floors, constants, CRT independence, and the promise Las Vegas reduction

From \(2^b\le h<2^{b+1}\), exactly

\[
  \frac h{16}<T\le\frac h8.                            \tag{4.1}
\]

Since \(h>\sqrt N-1\),

\[
  m=T-1>
  \frac{\sqrt N}{16}-\frac{17}{16}
  =\frac{\sqrt N-17}{16}.                              \tag{4.2}
\]

The balanced promise gives

\[
  p<\sqrt N<q,
  \qquad
  p>\frac{\sqrt N}{\sqrt2},
  \qquad
  q<\sqrt{2N}.                                        \tag{4.3}
\]

For either \(r\in\{p,q\}\), equations (4.1)--(4.3) imply

\[
  a:=\frac1{32\sqrt2}<\mu_r
  <U:=\frac{\sqrt2}{8}.                               \tag{4.4}
\]

For the lower bound, \(r\le q<\sqrt{2N}\) and (4.2) give

\[
  \mu_r>
  \frac{\sqrt N-17}{16\sqrt{2N}}
  =\frac{1-17/\sqrt N}{16\sqrt2}
  >\frac1{32\sqrt2},
\]

because \(\sqrt N>p\ge53>34\). For the upper bound, \(m<T\le h/8\le\sqrt N/8\), so

\[
  \mu_p<\frac{\sqrt N}{8p}
       =\frac18\sqrt{\frac qp}
       <\frac{\sqrt2}{8},
  \qquad
  \mu_q<\frac{\sqrt N}{8q}<\frac18.
\]

Let \(\alpha_r=\Pr(E_r)\). From (3.3)--(4.4),

\[
  \frac1{32\sqrt2+1}<\alpha_r<U.
\]

Exact uniform sampling modulo \(N\), followed by CRT, makes the entire vectors

\[
  (a_1\bmod p,\ldots,a_K\bmod p)
  \quad\text{and}\quad
  (a_1\bmod q,\ldots,a_K\bmod q)
\]

independent and individually uniform. Hence \(E_p\) and \(E_q\) are independent. Therefore

\[
\begin{aligned}
  \Pr(E_p\mathbin\triangle E_q)
  &=\alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p)\\
  &\ge
  \frac{2}{32\sqrt2+1}
  \left(1-\frac{\sqrt2}{8}\right)
  =\delta.
\end{aligned}                                         \tag{4.5}
\]

Every returned \(d\) is checked by the inequalities \(1<d<N\), the gcd identity, and exact division. Independent retries have probability at most \((1-\delta)^j\) of surviving \(j\) trials, so nontermination has probability zero and the expected number of trials is at most \(1/\delta\).

If \(Q_K\) had a uniform polynomial-bit evaluator, exact rejection sampling for the \(K=O(n)\) residues would use \(O(n^2)\) expected random bits per trial, and all modular arithmetic and the terminal gcd would have polynomial bit complexity. This proves only the conditional balanced-promise Las Vegas reduction stated in Section 2.

## 5. Exact meet-in-the-middle evaluator

Partition

\[
  [K]=A\mathbin{\dot\cup}B,
  \qquad
  |A|=\lfloor K/2\rfloor,
  \qquad
  |B|=\lceil K/2\rceil.
\]

For \(U\subseteq A\) and \(V\subseteq B\), including the empty subsets, define

\[
  x_U=\sum_{i\in U}a_i,
  \qquad
  y_V=\sum_{i\in V}a_i.
\]

Let

\[
  F_A(X)=\prod_{U\subseteq A}(X+x_U),
  \qquad
  Q_A=\prod_{\varnothing\ne U\subseteq A}x_U.
\]

Every nonempty subset of \([K]\) is uniquely \(U\mathbin{\dot\cup}V\). Separating the case \(V=\varnothing\) gives the sign-free identity

\[
  \boxed{
  Q_K
  =Q_A
   \prod_{\varnothing\ne V\subseteq B}F_A(y_V).
  }                                                     \tag{5.1}
\]

No division, field operation, or knowledge of \(p,q\) is used.

For an equivalent resultant form, put

\[
  P_A(X)=\prod_{\varnothing\ne U\subseteq A}(X+x_U),
  \qquad
  R_B(X)=\prod_{\varnothing\ne V\subseteq B}(X-y_V),
\]

and \(m_B=2^{|B|}-1\). With the convention that for monic \(f\),

\[
  \operatorname{Res}(f,g)=\prod_{f(\rho)=0}g(\rho),
\]

the same identity is

\[
  Q_K
  =(-1)^{m_B}P_A(0)R_B(0)
    \operatorname{Res}(R_B,P_A).                      \tag{5.2}
\]

Indeed, \(R_B(0)=(-1)^{m_B}\prod_{V\ne\varnothing}y_V\), so both displayed signs cancel. Formula (5.1) avoids relying on any sign convention.

Let

\[
  s=2^{\lceil K/2\rceil}.
\]

An exact algorithm over \(R=\mathbb Z/N\mathbb Z\) is:

1. enumerate both half-sum lists in Gray-code order using \(O(s)\) modular additions;
2. build the monic polynomial \(F_A\) with a balanced product tree;
3. build the monic subproduct tree for the points \(y_V\), whose leaves are \(X-y_V\);
4. evaluate \(F_A\) at every nonempty \(y_V\) by the usual remainder tree;
5. multiply those values and \(Q_A\) modulo \(N\).

Every divisor polynomial in the remainder tree is monic. Polynomial remainder therefore needs no inversion of a possibly nonunit leading coefficient, so the construction is valid over the composite coefficient ring. Repeated evaluation points also cause no problem. Fast polynomial products and monic remainders can be implemented uniformly over \(R\), for example by coefficient reduction modulo \(N\) together with Kronecker-substitution multiplication.

The resulting bounds are

\[
  \widetilde O\bigl(s\,\operatorname{poly}(n,K)\bigr)
  \quad\text{bit operations}
\]

and

\[
  \widetilde O(sn)
  \quad\text{stored coefficient bits},
\]

where the first display means \(\widetilde O(s\operatorname{poly}(n,K))\). Since \(T=2^K=\Theta(\sqrt N)\) on the promise and \(s=\Theta(\sqrt T)\),

\[
  \text{time}=N^{1/4+o(1)},
  \qquad
  \text{space}=N^{1/4+o(1)}.                         \tag{5.3}
\]

The Sylvester matrix associated with (5.2) has dimension \(O(s)\), not \(T\). Its naive determinant is not the claimed algorithm; product and multipoint trees give the sharper bound (5.3).

## 6. Polynomial-space evaluator

A Gray-code traversal of all \(T\) subsets updates the current subset sum by one modular addition or subtraction whenever a bit toggles. Multiplying every nonempty sum into an accumulator evaluates \(Q_K\) with

\[
  T-1=\Theta(\sqrt N)=N^{1/2+o(1)}
\]

modular additions and multiplications. All residues are reduced modulo \(N\). Beyond the \(O(Kn)\)-bit input list, the traversal uses \(O(n+K)\) working bits for the current sum, accumulator, and Gray-code state. Thus it gives

\[
  \text{time}=N^{1/2+o(1)},
  \qquad
  \text{space}=\operatorname{poly}(n).               \tag{6.1}
\]

Forming the full product over the integers could create \(O(Tn)\)-bit intermediates, but neither explicit evaluator does that.

## 7. Exact structural interpretations

### 7.1 Full Boolean diagonal

Let \(P=\operatorname{diag}(0,1)\), let \(P_i\) act as \(P\) on Boolean tensor factor \(i\), and let

\[
  P_0=(I-P)^{\otimes K},
  \qquad
  H_K=P_0+\sum_{i=1}^Ka_iP_i.
\]

On the Boolean basis state indexed by \(S\subseteq[K]\), \(H_K\) has eigenvalue \(1\) for \(S=\varnothing\) and \(L_S\) otherwise. Hence

\[
  \det H_K=Q_K.
\]

This is a polynomial-bit description of a \(T\)-dimensional diagonal matrix, not a polynomial-time determinant algorithm.

### 7.2 Weighted hypercube spanning trees

Give every edge in direction \(i\) of the \(K\)-dimensional undirected hypercube weight \(a_i\), and let \(\tau_K(a)\) be its weighted spanning-tree polynomial. The weighted Laplacian is a Kronecker sum with eigenvalues

\[
  2L_S
  \qquad(S\subseteq[K]).
\]

The matrix-tree theorem, with \(T=2^K\), gives the exact polynomial identity

\[
  \boxed{
  \tau_K(a)
  =\frac1T\prod_{S\ne\varnothing}2L_S
  =2^{2^K-K-1}Q_K.
  }                                                     \tag{7.1}
\]

Over the odd moduli in the theorem, the power of \(2\) is a unit, so evaluating either scalar evaluates the other. The cofactor determinant still has dimension \(T-1\); (7.1) is a normalization and interpretation, not a faster general evaluator.

### 7.3 Binary-weight factorial specialization

For the structured choice

\[
  a_i=u2^{i-1}
  \qquad(1\le i\le K),
\]

the nonempty subset sums, as integer polynomials in \(u\), are exactly

\[
  u,2u,\ldots,(T-1)u.
\]

Therefore

\[
  \boxed{
  Q_K=u^{T-1}(T-1)!\pmod N.
  }                                                     \tag{7.2}
\]

This specialization does not have the independent-uniform distribution used in Sections 3--4. It shows that F24 contains an ordinary batch-factorial product and reinforces its F02/P21-adjacent classification; it does not supply an arbitrary-weight evaluator.

## 8. Exact scope of the formal rank and degree statements

Several narrow facts remain correct, but none is a general evaluation lower bound.

First, over \(\mathbb Q(a_1,\ldots,a_K)\), the unmodified diagonal subset-sum operator has the \(T\) distinct formal eigenvalues

\[
  \sum_{i\in S}a_i
  \qquad(S\subseteq[K]),
\]

and therefore has minimal polynomial of degree \(T\). Any linear representation required to retain that entire formal spectrum has dimension at least \(T\). Computing the one symmetric scalar \(Q_K\) need not retain the spectrum; formula (5.1) already improves on full diagonal traversal.

Second, in characteristic zero, the linear forms

\[
  L_S=\sum_{i\in S}a_i
  \qquad(\varnothing\ne S\subseteq[K])
\]

are distinct nonassociate irreducibles. If a nonzero polynomial \(G\in\mathbb Q[a_1,\ldots,a_K]\) vanishes identically on every hyperplane \(L_S=0\), then every \(L_S\) divides \(G\), so

\[
  Q_K\mid G,
  \qquad
  \deg G\ge T-1.                                      \tag{8.1}
\]

Consequently, a \(d\times d\) determinant with entry degrees at most \(e\), if its nonzero characteristic-zero determinant has this universal hyperplane-vanishing property, must satisfy \(de\ge T-1\). This statement does not cover high-degree entries computed by short circuits, characteristic- or modulus-dependent functions, branching algorithms, or other modular evaluators. Repeated squaring alone shows why large formal degree is not a circuit lower bound.

Third, the symmetry can create small formulas at fixed \(K\). For \(K=3\), writing \(e_1,e_2,e_3\) for the elementary symmetric polynomials,

\[
  Q_3=e_1e_3(e_1e_2-e_3).
\]

No polynomial-size formula for arbitrary \(K\) follows, but neither formal roots nor (8.1) proves one absent.

Finally, if \(D_r\) is the number of distinct local subset sums including the empty sum, then pairwise collision counting gives

\[
  \mathbb E D_r
  \ge
  T-\binom T2\frac1r
  =T\left(1-\frac{T-1}{2r}\right).                   \tag{8.2}
\]

This says that a literal support table has exponential expected size at the chosen threshold. It is neither a concentration theorem nor a lower bound on compressed state, circuit size, or modular evaluation time.

The only rigorous evaluator conclusion is therefore:

- the named full diagonal, full Boolean-quotient multiplication matrix, dense literal recursion, raw support table, and Gray-code traversal are exponential;
- the exact meet-in-the-middle evaluator is a stronger \(N^{1/4+o(1)}\) upper bound;
- no uniform polynomial-bit evaluator for arbitrary weights is supplied; and
- no result here excludes such an evaluator.

## 9. Optional and dispensable mixed-Hurwitz provenance

For completeness, the original prefix can manufacture residues before uniformization. Let \(\beta,\gamma\) be two fresh independent primitive **raw residual** Lipschitz quaternions from P30, so that \(N\mid\operatorname{nrd}(\beta)\) and \(N\mid\operatorname{nrd}(\gamma)\), and put

\[
  c=\operatorname{trd}(\beta\gamma)\pmod N.
\]

Locally write the two nonzero rank-one split matrices as

\[
  B=uv^{\mathsf T},
  \qquad
  C=xy^{\mathsf T}.
\]

Then

\[
  \operatorname{tr}(BC)
  =(v^{\mathsf T}x)(y^{\mathsf T}u).
\]

Conditional on the accepted residual and completion randomness of the two fresh calls, P30 makes each required row or image marginal uniform on \(\mathcal S_r\), where

\[
  s_r=|\mathcal S_r|
  =r-\left(\frac{-1}{r}\right).
\]

Independence of the calls and a union bound give

\[
  \Pr(r\mid c)\le\frac2{s_r}.                         \tag{9.1}
\]

This is a conditional upper bound, not an exact divisibility law and not a uniformity claim after conditioning on the entire current call transcript, which fixes the output.

Retain \(c\) only when \(\gcd(c,N)=1\); a proper gcd already factors the promised input, and a gcd of \(N\) is discarded. For \(p,q\ge53\), \(s_p,s_q\ge52\), so, conditional on all earlier calls, the discard probability is at most

\[
  \eta=\frac2{s_p}+\frac2{s_q}\le\frac1{13}.
\]

Ignoring early proper-gcd termination, the expected number of fresh-pair attempts required for \(K\) retained units is therefore at most

\[
  \frac K{1-\eta}\le\frac{13K}{12}.
\]

For any adaptively obtained unit residues \(c_1,\ldots,c_K\), fresh independent uniform \(\lambda_i\bmod N\) make

\[
  a_i=\lambda_i c_i\pmod N
\]

independent uniform residues conditional on all preceding data. Multiplication by each unit \(c_i\) is a bijection. Thus the terminal distribution is exactly the direct distribution of Section 2, and the entire prefix may be deleted without changing the theorem. P31's mixed-hand graph, menu bounds, and pooled-space results play no role after this uniformization.

## 10. Bit-complexity and all-input audit

Exact direct sampling draws \(n\)-bit strings until the value is below \(N\). The acceptance probability is at least \(1/2\), so one uniform residue uses \(O(n)\) expected random bits and a full trial uses \(O(Kn)=O(n^2)\). All sampled residues, running sums, modular products, and gcd inputs have \(O(n)\) bits.

The meet-in-the-middle coefficient arrays have \(N^{1/4+o(1)}\) total bits and the Gray-code evaluator has polynomial working space. Both have exponential bit time. The optional Hurwitz prefix has expected polynomial bit and random-bit complexity under P30 and the retention bound (9.1), but it is unnecessary.

There is no accidental access to \(p\) or \(q\) in either evaluator. The monic remainder tree performs no division by an unknown nonunit. CRT is used only in the proof of probability, not by the algorithm. The only terminal extraction is the verified gcd.

The result does not handle prime inputs, prime powers, repeated factors, even composites, unbalanced semiprimes, or integers with three or more prime factors. On a prime input the displayed restart loop need not terminate. No reduction to complete recursive factorization is proved. Fixed trial division or deterministic primality testing would not repair the missing evaluator or supply the absent all-input separation theorem.

Accordingly, this report does not meet any completion criterion in `PROMPT.md`.

## 11. Classification and materially new reopen condition

**Classification:** method failure for the explicit general evaluators supplied here. The probability theorem proves that amortizing many lucky relations can create a constant-mass joint local event; the unresolved step is exact fast evaluation of its structured product. This is not evidence that a polynomial-time evaluator is impossible, and it is not evidence against other nonlinear joint decoders.

The route is grouped with F02/P21 because its terminal missing lemma is a uniform fast evaluator for an exponentially long structured modular product. The optional F14 trace construction is only dispensable provenance.

A materially new reopening requires at least one of:

1. a uniform exact algorithm evaluating arbitrary-weight \(Q_K\bmod N\) for \(K=\Theta(\log N)\) in \(\operatorname{poly}(\log N)\) bit time, including every intermediate bit length;
2. a different cancellation-free aggregate with a proved inverse-polynomial local-XOR probability and a proved polynomial-size evaluator;
3. a characteristic- or modulus-sensitive identity, branching algorithm, or symmetric formula that genuinely beats (5.3), rather than re-materializing the full Boolean algebra;
4. an all-input threshold and recursion theorem extending beyond the balanced distinct-semiprime promise; or
5. a structural law for unrandomized algebraic relations that yields a provably small exact state space while retaining asymmetric local zero events.

A succinct \(2^K\)-dimensional determinant, the degree statement (8.1), the hypercube normalization (7.1), the binary factorial specialization (7.2), or a literal support table is not by itself such a reopening.
