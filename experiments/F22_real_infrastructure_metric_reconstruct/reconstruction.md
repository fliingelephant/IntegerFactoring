# Proof-blind reconstruction: the real-infrastructure/SQUFOF boundary

## Scope and verdict

This reconstruction was made from the bare statement, first principles, and the primary sources listed at the end. I did **not** inspect either `experiments/F22_real_infrastructure_metric_kill/` or `experiments/F22_real_infrastructure_metric_audit/`, and I did not read an F22 passage in `PROVED.md` or `FAILED.md`. No mathematical computation was run.

Here and below

\[
t\ge 1,\qquad a=6t+1,\qquad N=a^2+2,\qquad \Delta=4N.
\]

The symbol \(D\) is reserved for the working integer/discriminant used in the Gower--Wagstaff pseudocode. It is not silently identified with \(\Delta\).

| Claim | Verdict |
|---|---|
| \(N\) is odd, nonsquare, composite, and has the public nontrivial divisor \(3\) | **Proved exactly** |
| \(\sqrt N=[a;\overline{a,2a}]\) | **Proved exactly** |
| In the Gower--Wagstaff proper-form \(\rho\) convention, the complete reduced proper principal cycle is \((1,2a,-2)\leftrightarrow(-2,2a,1)\) | **Proved exactly** |
| The only oriented positive right square coefficient is \(1\), and it is an improper/period-completion square under the queue/list test | **Proved, with the literal parity/indexing qualification in Section 3** |
| Every coefficient of either reduced endpoint is coprime to \(N\) | **Proved exactly** |
| The family is not uniformly squarefree; the \(3\)-adic cases and other possible repeated factors are accounted for | **Proved exactly** |
| Full traversal, or a jump that reveals only a reduced endpoint, followed only by single-form coefficient gcds/proper-square localization, fails to reveal a factor | **Proved for precisely that restricted observation model** |
| The two endpoints are at distances \(0,R/2\); distance is injective on reduced principal ideals; reduction-corrected addition, gap/precision facts, compact encodings, and the Terr bounds stated below | **Proved for the family / reconstructed with exact source qualifications in general** |
| The fundamental unit of the order of discriminant \(4N\) is \((N-1)+a\sqrt N\), and \(R=\Theta(\log N)\) | **Proved exactly** |
| A general infrastructure or factoring lower bound follows | **Not claimed; explicitly excluded** |

## 1. Elementary arithmetic and the continued fraction

Since \(a=6t+1\) is odd, \(a^2\) and \(N=a^2+2\) are odd. Also

\[
a\equiv 1\pmod 3 \quad\Longrightarrow\quad N\equiv 1+2\equiv0\pmod3.
\]

For \(t\ge1\), \(a\ge7\), so \(N\ge51>3\). Thus \(3\) is a public, nontrivial divisor and \(N\) is composite.

Moreover

\[
a^2<N=a^2+2<(a+1)^2=a^2+2a+1,
\]

because \(2<2a+1\). Hence \(N\) is not a square and \(\lfloor\sqrt N\rfloor=a\).

For the continued fraction, let \(x_0=\sqrt N\). Then

\[
x_1=\frac1{\sqrt N-a}=\frac{\sqrt N+a}{2}.
\]

As \(a<\sqrt N<a+1\), one has \(a<x_1<a+\tfrac12\), so the first periodic partial quotient is \(a\). Next,

\[
x_2=\frac1{x_1-a}=\frac2{\sqrt N-a}=\sqrt N+a.
\]

Thus \(2a<x_2<2a+1\), so the next partial quotient is \(2a\). Finally

\[
\frac1{x_2-2a}=\frac1{\sqrt N-a}=x_1.
\]

Therefore, with minimal period two,

\[
\boxed{\sqrt N=[a;\overline{a,2a}].}
\]

The period is genuinely two: \(a\ne2a\) for \(a>0\).

## 2. Exact proper-form cycle

Gower--Wagstaff write a form as \((A,B,C)\), with discriminant

\[
B^2-4AC=\Delta,
\]

and define

\[
\rho(A,B,C)=\left(C,r(-B,C),\frac{r(-B,C)^2-\Delta}{4C}\right),
\]

where \(r=r(-B,C)\) is the unique integer satisfying \(r+B\equiv0\pmod{2C}\) in their stated reduction interval. A form is reduced when

\[
\left|\sqrt\Delta-2|A|\right|<B<\sqrt\Delta.
\]

Set

\[
f_0=(1,2a,-2),\qquad f_1=(-2,2a,1).
\]

Both have discriminant \(4a^2+8=4N=\Delta\), and both are primitive. Since \(\sqrt\Delta=2\sqrt N\), the inequalities

\[
2\sqrt N-2<2a<2\sqrt N,
\qquad
2\sqrt N-4<2a<2\sqrt N
\]

show that \(f_0\) and \(f_1\), respectively, are reduced. (The left inequalities follow from \(\sqrt N<a+1\).)

For \(f_0\), the integer \(r=2a\) satisfies

\[
r+2a=4a\equiv0\pmod{-4}
\]

and lies in \((2\sqrt N-4,2\sqrt N)\). Hence

\[
\rho(f_0)
=\left(-2,2a,\frac{4a^2-4N}{-8}\right)
=(-2,2a,1)=f_1.
\]

For \(f_1\), the same \(r=2a\) satisfies the congruence modulo \(2\) and lies in \((2\sqrt N-2,2\sqrt N)\). Therefore

\[
\rho(f_1)
=\left(1,2a,\frac{4a^2-4N}{4}\right)
=(1,2a,-2)=f_0.
\]

Gower--Wagstaff's principal form is the unique reduced form with first coefficient \(1\), so it is \(f_0\). Their \(\rho\) permutes the reduced forms in one proper equivalence class cyclically. Since the orbit of \(f_0\) returns after the two distinct reduced forms above, it is the complete reduced proper principal cycle:

\[
\boxed{(1,2a,-2)\ \xleftrightarrow{\ \rho\ }\ (-2,2a,1).}
\]

No fundamentality or squarefreeness of \(\Delta\) was used in this calculation.

Every displayed coefficient is coprime to \(N\). This is immediate for \(\pm1,\pm2\) because \(N\) is odd. For the middle coefficient,

\[
\gcd(2a,N)=1,
\]

since \(\gcd(2,N)=1\) and

\[
\gcd(a,a^2+2)=\gcd(a,2)=1
\]

for odd \(a\). In particular, every left- or right-end coefficient has gcd \(1\) with \(N\).

## 3. The square-form test, including its parity convention

### 3.1 The only oriented positive right square

The right coefficients in the oriented proper cycle are \(-2\) and \(1\). Thus the only positive square right coefficient is

\[
C=1=1^2
\]

at \(f_1=(-2,2a,1)\). There is no other reduced endpoint and hence no other possible right square coefficient.

It is essential not to replace a negative right coefficient by its absolute value: \(-2\) is not a positive square-form coefficient in the Gower--Wagstaff definition.

### 3.2 Exact list/queue classification

Because \(a\) is odd, \(a^2\equiv1\pmod8\) and hence \(N\equiv3\pmod8\), in particular \(N\equiv3\pmod4\). In the binary-quadratic-form version of Gower--Wagstaff, initialization gives

\[
D=4N,\quad m_{\rm GW}=2,\quad
d=\lfloor\sqrt D\rfloor=2a,\quad b=2\lfloor d/2\rfloor=2a,
\]

and hence the initialized form is \(f_0\). The equality \(d=2a\) follows from

\[
2a<2\sqrt N<2a+1;
\]

the right inequality follows from \((a+\tfrac12)^2>a^2+2\) for \(a\ge7\).

The sufficient-list initialization inserts

\[
g=\frac{|{-2}|}{\gcd(2,m_{\rm GW})}=\frac2{2}=1,
\]

and \(1\le L=\lfloor\sqrt d\rfloor\). Thus the root \(c=1\) of the only square endpoint is already in the list. The exact Step 2b control flow is:

1. a square whose root is absent from the list proceeds to inverse-square-root extraction;
2. a listed root greater than \(1\) is skipped (the paper warns that this sufficient list can skip some proper squares, so list membership alone is not an exact impropriety certificate);
3. a listed root equal to \(1\) triggers the explicit stop because the entire principal period has been traversed without a proper square.

Therefore the lone square is classified as improper/period completion, not as a factor-producing square.

The queue version gives the same answer. In the continued-fraction initialization, \(Q_1=2\) is eligible and inserts

\[
(Q_1/2,P_1\bmod(Q_1/2))=(1,0).
\]

At the positive square endpoint the candidate root is \(c=1\), whose search key is likewise \((c,2a\bmod c)=(1,0)\). Gower--Wagstaff Proposition 3.2 identifies such a match with an inverse square root equivalent to one of the trivial ambiguous forms \(\pm\mathbf1,\pm\mathbf2\). It is therefore improper; in the \(c=1\) case the algorithm declares completion of the principal period.

### 3.3 Parity/indexing qualification

There are three labels that must not be conflated:

- position in the proper \(\rho\)-cycle;
- the continued-fraction form index \(n\), for which Gower--Wagstaff test only the parity giving a positive right end;
- the local pseudocode counter `i`, whose starting value differs between their continued-fraction and binary-form presentations.

In the continued-fraction form sequence, a positive right square can occur only at an even mathematical form index. The typeset binary-form pseudocode instead initializes its local counter at `i = 2`, applies \(\rho\), and then says to skip the square test when `i` is even. On the present cycle the first post-\(\rho\) form is exactly \((-2,2a,1)\), so that printed local counter skips it; all printed odd-counter positions see \((1,2a,-2)\), whose right coefficient is negative. Read completely literally, that branch reaches its cap without executing the explicit `c = 1` branch.

The mathematical parity normalization is to test the positive-right-end positions (equivalently here, test \(C>0\), or reverse/rebase the printed counter parity). Under that normalization \((-2,2a,1)\) is tested, and the preloaded list entry \(1\) rejects it as period completion. The discrepancy is a local indexing mismatch in the presentation, not a new proper square.

The invariant conclusion is exact in either presentation:

- on the parity-normalized, positive-right-end presentation, the only root is \(1\), already in the list/queue, and it is period completion;
- if the literal local counter suppresses that occurrence, then no square is extracted at all.

Thus the unmultiplied cycle contains **no proper SQUFOF square**. Treating the skipped occurrence as a factor-producing square, or treating \(|-2|\) as a square candidate, would be a parity/sign error.

## 4. Squarefree and repeated-factor audit

The first member is

\[
t=1:\qquad a=7,\qquad N=51=3\cdot17,
\]

which is squarefree. It satisfies the paper's squarefreeness hypothesis, though this one small example is not by itself in the asymptotic setting of its "large odd prime divisor" assumption.

The \(3\)-adic behavior is controlled by \(t\bmod3\). Write \(t=3k+r\).

- If \(r=0\), then
  \[
  N=(18k+1)^2+2=3(108k^2+12k+1),
  \]
  and the parenthesis is \(1\bmod3\). Hence \(v_3(N)=1\).

- If \(r=1\), then
  \[
  N=(18k+7)^2+2=3(108k^2+84k+17),
  \]
  and the parenthesis is \(2\bmod3\). Hence \(v_3(N)=1\).

- If \(r=2\), then
  \[
  N=(18k+13)^2+2=9(36k^2+52k+19),
  \]
  so \(v_3(N)\ge2\). Higher \(3\)-adic valuation can occur; the last parenthesis is \(k+1\bmod3\).

These congruences audit only the prime \(3\); they do not prove squarefreeness in either of the first two residue classes. For example,

\[
t=3:\qquad a=19,\qquad N=363=3\cdot11^2.
\]

Indeed repeated factors other than \(3\) occur in every residue class of \(t\bmod3\). Since

\[
19^2\equiv-2\pmod{11^2},
\]

the congruence \(6t+1\equiv19\pmod{121}\), equivalently \(t\equiv3\pmod{121}\), forces \(11^2\mid N\). As \(121\equiv1\pmod3\), choosing the free multiple of \(121\) realizes each prescribed class of \(t\bmod3\).

When \(N\) is squarefree, \(N\equiv3\pmod4\) and \(4N\) is the field discriminant. When \(N\) is not squarefree, \(\Delta=4N\) is still the discriminant of the quadratic order

\[
\mathcal O_\Delta=\mathbf Z[\sqrt N],
\]

but it is not a fundamental discriminant. The explicit continued fraction, proper-form cycle, coefficient gcds, and Pell-unit argument here remain valid. What does not automatically extend is the squarefree/fundamental-discriminant **average-case analysis** in Gower--Wagstaff; they explicitly say their experience suggests similar behavior for nonsquarefree inputs but that their analysis does not cover it.

## 5. Exact endpoint-only obstruction and its boundary

Consider the following deliberately restricted observation model at the fixed discriminant \(\Delta=4N\):

1. traverse the reduced proper principal cycle completely, or use arbitrary jumps within that principal infrastructure;
2. after every operation discard the composition/reduction transcript and retain only the final reduced endpoint;
3. attempt extraction only by a gcd of \(N\) with one coefficient of that single endpoint, or by the standard proper-square localization from that endpoint.

Every observed endpoint is either \(f_0\) or \(f_1\). Every coefficient gcd is \(1\), and the only positive right square is the improper root \(1\). Therefore this observation model never returns a nontrivial divisor.

This is the strongest conclusion reconstructed from the family. It says nothing against richer algorithms. In particular it explicitly excludes:

- the public-factor driver (trial division already returns \(3\));
- multipliers and all different discriminants;
- intermediate composition and reduction transcripts;
- relative generators/reduction multipliers;
- distance power products and other compact generator encodings;
- failure-event decoders or decoders that combine several observations;
- joint endpoint/transcript/distance decoders;
- any general lower bound for SQUFOF, infrastructure methods, or classical factoring.

Because \(3\mid N\) is visible from the input formula, this family cannot itself be a hard factoring family.

## 6. Qualified infrastructure facts

All facts in this section concern the real quadratic order of discriminant \(\Delta\); they are not claims that endpoint-only data factors \(N\).

### 6.1 Injective distance on reduced principal ideals

Buchmann--Vollmer define the distance of equivalent ideals modulo the numeric regulator \(R\). Their Section 3 states that restriction to the reduced principal ideals is injective:

\[
d(\mathcal O,\cdot):\mathcal R_\Delta\cap\mathcal P
\hookrightarrow \mathbf R/R\mathbf Z.
\]

Thus distinct reduced principal ideals occupy distinct points of the infrastructure circle. This injectivity is specifically a statement about normalized reduced ideals. On all principal ideals before normalization, rational scalings (and the corresponding kernel discussed by Buchmann--Vollmer) prevent the naive unrestricted statement.

Injectivity is only uniqueness of the endpoint label. It does not assert that inversion of the distance map is cheap, nor that the labelled endpoint contains a factor of \(N\).

### 6.2 Addition requires the reduction multiplier

Distance is additive on exact principal-ideal products. But the product of two reduced ideals is generally not reduced. Write \(\delta(I)=d(\mathcal O,I)\). If

\[
\rho(IJ)=\gamma\,IJ,
\]

then, in a distance sign convention where principal multiplication adds,

\[
\delta(\rho(IJ))
\equiv \delta(I)+\delta(J)+\operatorname{Log}\gamma\pmod R.
\]

(The last sign reverses if ideals are represented by inverse generators; the requirement to retain it does not.) Gower--Wagstaff likewise warn immediately after their distance-composition formula that composed forms need not be reduced and a correction is required. Buchmann--Vollmer's giant steps explicitly retain the reducing number \(\delta_i\)/relative generator.

Therefore one may double or add distances through composition and reduction only if the reduction multipliers, or an exactly equivalent correction record, are tracked. The reduced endpoint by itself does not justify replacing its distance by the uncorrected sum.

### 6.3 Exact metric on the two-point family

Gower--Wagstaff use the one-step distance

\[
d(f,\rho(f))=\frac12\log\left|\frac{B+\sqrt\Delta}{B-\sqrt\Delta}\right|.
\]

Both forms in this cycle have \(B=2a\). Hence each oriented step has length

\[
\ell
=\frac12\log\frac{\sqrt N+a}{\sqrt N-a}
=\log\frac{\sqrt N+a}{\sqrt2},
\]

where \((\sqrt N-a)(\sqrt N+a)=2\). Moreover

\[
2\ell
=\log\frac{(\sqrt N+a)^2}{2}
=\log\bigl((N-1)+a\sqrt N\bigr)
=R,
\]

where the last equality is proved in Section 7. Thus the two reduced principal endpoints lie exactly at \(0\) and \(R/2\) modulo \(R\). This computes the metric geometry of this family; it does not turn either endpoint into a factor-bearing form.

### 6.4 Neighbor gaps and numerical precision

In the Buchmann--Vollmer normalization, if \(\gamma_i\) is the relative generator from one reduced neighbor to the next, Lemma 3.2 gives

\[
\frac1{\sqrt\Delta}<\operatorname{Log}\gamma_i
<\frac12\log\Delta,
\qquad
\operatorname{Log}\gamma_i+\operatorname{Log}\gamma_{i+1}>\log2.
\]

Thus every one-neighbor gap is strictly larger than \(\Delta^{-1/2}\), and every two consecutive gaps have the stronger total lower bound \(\log2\). If a target is promised to be an exact reduced endpoint, circular absolute error below \(1/(2\sqrt\Delta)\) is sufficient to distinguish it from every other endpoint. This requires \(\tfrac12\log_2\Delta+O(1)\) fractional bits, not constant precision.

For an approximate doubling chain, write a lifted exact recurrence as

\[
x_{j+1}=2x_j+\kappa_j,
\]

where \(\kappa_j\) is the tracked reduction correction. If the input error is \(e_0\) and the correction error at step \(j\) is \(\eta_j\), then

\[
|e_K|\le 2^K|e_0|+
\sum_{j=0}^{K-1}2^{K-1-j}|\eta_j|.
\]

This follows by induction from \(|e_{j+1}|\le2|e_j|+|\eta_j|\). If all of \(|e_0|,|\eta_j|\) are at most \(2^{-p}\), then

\[
|e_K|<(2^{K+1})2^{-p}.
\]

Hence the safe sufficient precision

\[
p\ge K+\left\lceil\tfrac12\log_2\Delta\right\rceil+3
\]

keeps the final error below half the minimum neighbor gap. One must not claim that a fixed initial approximation remains endpoint-resolving through arbitrarily many doublings. Buchmann--Vollmer's Terr algorithms avoid this issue by arranging exact arithmetic; the recurrence above qualifies approximate jumping schemes.

### 6.5 Sizes and compact encodings

A reduced ideal in standard representation has integral parameters bounded on the scale \(\sqrt\Delta\); Buchmann--Vollmer explicitly use size \(O(\log\Delta)\) bits for a reduced ideal. Thus a reduced endpoint is polynomial-size even if a generator relating it to the origin is enormous.

Large generators need not be expanded. Buchmann--Vollmer Equation (12) outputs the relative generator/fundamental unit as a power product of reducing numbers and giant-step corrections, while retaining the reduced ideals needed to construct those bases. More generally, a power product

\[
\prod_{j=1}^s \alpha_j^{e_j}
\]

has encoding length polynomial in the base encodings, \(s\), and the binary lengths of the \(e_j\); an equivalent straight-line program has size proportional to its number of arithmetic gates. Buchmann--Thiel--Williams prove polynomial-size compact representations (polynomial in \(\log\log H(\alpha)\), \(\log|N(\alpha)|\), and \(\log\Delta\)) and polynomial-time norm, sign, product, inverse, principal-ideal, and comparison operations on them.

These are representation upper bounds. They neither make an expanded generator small in general nor prove that a compact generator reveals a factor.

### 6.6 TerrUnit/TerrEquivalent bit complexity

Buchmann--Vollmer Proposition 7.1 gives, for reduced inputs where applicable,

\[
\boxed{
T_{\rm TerrUnit},\ S_{\rm TerrUnit},\
T_{\rm TerrEquivalent},\ S_{\rm TerrEquivalent}
=O\!\left((\log\Delta+\sqrt R)(\log\Delta)^2\right).
}
\]

Here \(R=\log\varepsilon\) is the **numeric regulator**. The term is \(\sqrt R\), not \(\sqrt{\log R}\). Their proof counts \(O(\log\Delta+\sqrt R)\) stored reduced ideals/corrections, each reduction in \(O((\log\Delta)^2)\) bit time, reduced-ideal size \(O(\log\Delta)\), and correction storage \(O((\log\Delta)^2)\).

This is an upper bound for the named regulator/equivalence algorithms. It is not an \(\Omega(\sqrt R)\) lower bound for those algorithms, for infrastructure arithmetic, or for factoring.

## 7. Fundamental unit and regulator of the explicit family

The order of discriminant \(4N\) is \(\mathcal O_\Delta=\mathbf Z[\sqrt N]\). The period-two continued fraction gives the convergent

\[
[a;a]=\frac{a^2+1}{a}=\frac{N-1}{a}.
\]

The standard continued-fraction theorem for Pell's equation says that an even period of length two yields the fundamental positive solution of \(x^2-Ny^2=1\) at this convergent. Directly,

\[
(N-1)^2-Na^2
=(a^2+1)^2-(a^2+2)a^2
=1.
\]

Therefore the fundamental unit of this order is

\[
\boxed{\varepsilon=(N-1)+a\sqrt N.}
\]

The even period also rules out a norm-\(-1\) Pell solution, so no smaller negative-norm unit changes the regulator convention.

Since \(a<\sqrt N\),

\[
N-1<\varepsilon=(N-1)+a\sqrt N<2N-1.
\]

For \(N\ge51\), this proves

\[
\boxed{R=\log\varepsilon=\Theta(\log N).}
\]

The coefficient pair \((N-1,a)\) itself has \(O(\log N)\) bits, so this family does not even require a compact power product to store its fundamental unit.

Consequently the Terr upper bound on this particular family is

\[
O\!\left((\log N+\sqrt{\log N})(\log N)^2\right)
=O((\log N)^3)
\]

in both bit time and bit space. This reinforces, rather than weakens, the scope boundary: the two-endpoint example is not an infrastructure-computation lower bound.

## 8. Exact Gower--Wagstaff caps and the scope of their complexity analysis

### 8.1 Unmultiplied continued-fraction presentation

Gower--Wagstaff Section 3.3 sets

\[
D=\begin{cases}
2N,&N\equiv1\pmod4,\\
N,&N\equiv2,3\pmod4,
\end{cases}
\]

and then, with every floor in its published position,

\[
S=\lfloor\sqrt D\rfloor,
\qquad
L_{\rm CF}=\left\lfloor2\sqrt{2\sqrt D}\right\rfloor,
\qquad
B=2L_{\rm CF}.
\]

For this family,

\[
D=N=a^2+2,\qquad
L_{\rm CF}=\left\lfloor2\sqrt{2\sqrt{a^2+2}}\right\rfloor,\qquad
B=2L_{\rm CF}.
\]

The bound parameter is unambiguous, but the typeset counter convention has a one-step inconsistency: initialization assigns `i = 0`, the prose says Steps 2a--2e are repeated for \(i=1,2,\ldots\), and the only explicit increment occurs at Step 2e. Under the prose indexing there are \(B\) forward updates and \(B/2=L_{\rm CF}\) even-counter square-test positions. Under a completely literal execution beginning with the assigned value `i = 0`, there are \(B+1\) body passes and \(B/2+1\) even-counter positions before the incremented counter exceeds \(B\). The latter reading tests this family's \(c=1\) square on its first pass and terminates there. Thus the published cap formula is exact, but any claimed exact body-pass count must state which published indexing convention it resolves. The cap, all body passes, and parity-eligible square tests are not interchangeable.

### 8.2 Binary-quadratic-form presentation

Gower--Wagstaff Section 3.6 sets

\[
D=\begin{cases}
N,&N\equiv1\pmod4,\\
4N,&N\equiv2,3\pmod4,
\end{cases}
\qquad
d=\lfloor\sqrt D\rfloor,
\]

then

\[
L_{\rm BQF}=\left\lfloor\sqrt d\right\rfloor,
\qquad
\mathrm{Bound}=4L_{\rm BQF}.
\]

For this family,

\[
D=4N,\qquad d=2a,\qquad
L_{\rm BQF}=\lfloor\sqrt{2a}\rfloor,\qquad
\mathrm{Bound}=4\lfloor\sqrt{2a}\rfloor.
\]

One must not replace \(\lfloor\sqrt{\lfloor\sqrt D\rfloor}\rfloor\) by an unfloored fourth root when claiming the exact pseudocode. Here `i` starts at \(2\); each pass applies one \(\rho\), and the algorithm gives up after incrementing beyond `Bound`. If nothing stops earlier, the printed loop executes `Bound - 1` reductions. Its printed "skip even" branch exposes \(2L_{\rm BQF}-1\) odd-counter square-test positions; on a reduced cycle those have negative right coefficient. The positive-right-end parity normalization described in Section 3.3 instead tests the \(2L_{\rm BQF}\) even-counter positions from \(2\) through `Bound`. On this family the first such normalized test already encounters the listed root \(1\) and stops. Again, the exact bound parameter and the parity convention are separate facts.

### 8.3 Multiplier presentation is separate

Section 5 does not authorize silently reusing the preceding symbols. For an odd squarefree multiplier \(m\), their continued-fraction modification uses

\[
D=\begin{cases}
2mN,&mN\equiv1\pmod4,\\
mN,&\text{otherwise},
\end{cases}
\quad
L=\left\lfloor\sqrt{2\sqrt D}\right\rfloor,
\quad B=2L,
\]

as typeset in the corrected author copy. Their binary-form multiplier modification instead chooses \(D=mN\) or \(4mN\) according to the congruence, then retains \(d=\lfloor\sqrt D\rfloor\), \(L=\lfloor\sqrt d\rfloor\), and `Bound = 4L`, with the multiplier-aware list/queue gcd normalization. These are different discriminants and different initialization rules from the unmultiplied family proved above.

### 8.4 Why the paper does not give a worst-case polylog theorem

The proper/improper queue criterion is exact in its stated setting, but the published running-time conclusions have a much narrower scope:

- Section 3 says the analysis assumes \(N\) squarefree and explicitly says it does not extend the analysis to nonsquarefree \(N\).
- Assumption 4.5 takes \(N\) to be squarefree with \(k\) distinct large odd prime divisors. The later asymptotics also use Assumptions 4.8, 4.11--4.13, 4.15, 4.17, and 4.19; these cover discriminant averaging, distribution among cycles, square-form spacing, and random ambiguous-cycle landing. Assumption 4.23 separately models queue density. The authors explicitly describe the process as a random walk.
- Theorem 4.22 is an **asymptotic average** count of order \(N^{1/4}\) under that model, averaged over inputs/discriminants rather than internal randomness for each fixed input; it is not a uniform worst-case bound polynomial in \(\log N\).
- The multiplier results assume distinct small odd primes \(p_i\nmid N\), a squarefree input with \(k\) distinct large odd prime factors, and the squarefree multiplier \(m=\prod_i p_i\). With \(\Delta=mN\) when \(mN\equiv1\pmod4\) and \(\Delta=4mN\) otherwise, they set \(\mu=m\) in the first case and \(\mu=2m\) in the second, and require respectively \(\mu^{3/4}<N^{1/4}\) or \(2\mu^{3/4}<N^{1/4}\). Theorems 5.4 and 5.8 remain asymptotic average statements under the preceding heuristic assumptions.
- The paper reports that some principal periods contain no proper square form. Trying or racing selected multipliers is an algorithmic remedy, not a proof that a fixed finite list succeeds for every integer.
- A hard cap of order \(D^{1/4}\) is a termination rule, not a lower bound, and neither that cap nor an average count is a worst-case polylogarithmic guarantee.

Thus the correct negative conclusion is only:

> The Gower--Wagstaff analysis, including its multiplier analysis, does not establish a classical worst-case or Las Vegas \(\operatorname{poly}(\log N)\) factoring theorem.

It would be invalid to strengthen that sentence into a general impossibility or lower-bound claim.

## 9. What was and was not reconstructed

Reconstructed exactly:

- the arithmetic family, its public divisor, nonsquareness, and continued fraction;
- the complete two-form reduced proper principal cycle in the cited \(\rho\) convention;
- the lack of a proper unmultiplied SQUFOF square, with exact list/queue and parity qualifications;
- coefficient coprimality and the squarefree/repeated-factor audit;
- failure of the explicitly defined endpoint-only observation model;
- the family unit and logarithmic regulator;
- the exact two-point metric and the cited infrastructure injectivity, corrected distance addition, gap/precision, compact-representation, Terr complexity, cap, and heuristic-scope facts.

Not reconstructed or asserted:

- failure of trial division (it succeeds immediately);
- failure with multipliers or another discriminant;
- failure of any method using a reduction transcript, a relative generator, a power product, or a distance straight-line program;
- failure of failure-event or joint decoders;
- a lower bound for cycle traversal, SQUFOF, infrastructure arithmetic, or integer factoring;
- any resolution of worst-case classical polynomial-time factoring.

## Primary sources

1. Jason E. Gower and Samuel S. Wagstaff, Jr., *Square Form Factorization*, Mathematics of Computation **77** (2008), 551--588, corrected author copy: <https://homes.cerias.purdue.edu/~ssw/squfof.pdf>. Relevant parts: reduction and reduced forms in Section 2.1.2; continued fractions and the form sequence in Sections 2.2 and 2.4; proper-square queue/list and both algorithms in Sections 3.1--3.6; explicit random-walk assumptions in Section 4; multiplier hypotheses and modified pseudocode in Section 5.
2. Johannes Buchmann and Ulrich Vollmer, *A Terr algorithm for computations in the infrastructure of real-quadratic number fields*, Journal de Théorie des Nombres de Bordeaux **18** (2006), 559--572: <https://www.numdam.org/item/10.5802/jtnb.558.pdf>. Relevant parts: distance in Section 2; injectivity, neighbor gaps, and reduction generators in Section 3; power-product output in Sections 4--6; bit time and space in Proposition 7.1.
3. Johannes Buchmann, Christoph Thiel, and Hugh C. Williams, *Short Representation of Quadratic Integers*, in *Computational Algebra and Number Theory*, Mathematics and Its Applications **325** (1995), 159--185, DOI <https://doi.org/10.1007/978-94-017-1108-1_12>; author-uploaded copy/abstract: <https://www.researchgate.net/publication/2606872_Short_Representation_of_Quadratic_Integers>.
4. H. W. Lenstra, Jr., *Solving the Pell Equation*, Notices of the AMS **49** (2002), 182--192, author reprint: <https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/2002a/art.pdf>.
5. H. W. Lenstra, Jr., *On the Calculation of Regulators and Class Numbers of Quadratic Fields*, in *Journees Arithmetiques 1980*, LMS Lecture Note Series **56** (1982), 123--150: <https://public.csusm.edu/ssharif/crypto/Lenstra82-QuadraticRegulators.pdf>.
