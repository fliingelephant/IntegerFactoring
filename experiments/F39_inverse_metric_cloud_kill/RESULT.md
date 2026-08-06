# F39 kill-first result: inverse-pair metric clouds are Fourier-flat at every factor-free public mode

**Family:** F24.

**Status:** candidate obstruction; not promoted pending hostile audit and the
required proof-blind reconstruction.

**Classification:** evidence against the exact auxiliary mechanism that takes
polynomially many independent uniform unit/inverse pairs, keeps only a public
polynomial list of Fourier coefficients, a bounded Fourier-sparse observable,
or a polynomial-size axis-parallel histogram, and tries to read a factor-scale
metric bias from empirical averages.

**Computation:** none.  This is a proof-only kill-first analysis of the
preregistered F39 source and statistic classes.

Let

\[
 N=pq,
\]

where \(p\ne q\) are odd primes.  The asymptotic statements below may be read
on any fixed balanced family \(p<q\leq Cp\), although the exact Fourier
identities do not need balance.  Write

\[
 e_m(t)=\exp(2\pi i t/m),\qquad
 \mathcal U_m=(\mathbb Z/m\mathbb Z)^\times .
\]

The source is the probability measure

\[
 \mu_N=\frac1{\varphi(N)}
 \sum_{u\in\mathcal U_N}\delta_{(u,u^{-1})}
 \quad\text{on }(\mathbb Z/N\mathbb Z)^2.
\tag{1}
\]

Thus its additive Fourier coefficient at \((a,b)\) is

\[
 \widehat\mu_N(a,b)
 =\frac{S_N(a,b)}{\varphi(N)},\qquad
 S_N(a,b)=\sum_{u\in\mathcal U_N}e_N(au+bu^{-1}).
\tag{2}
\]

This is a normalized Kloosterman sum.  Frequencies are always reduced modulo
\(N\).  The zero character has coefficient \(1\), as it must, and is not a
bias relative to the uniform measure on the discrete two-torus.

## 1. Exact CRT factorization, including the additive twists

Let

\[
 \bar q_p\,q\equiv1\pmod p,
 \qquad
 \bar p_q\,p\equiv1\pmod q.
\]

For a CRT pair \(x=(x_p,x_q)\),

\[
 x\equiv x_p\,q\bar q_p+x_q\,p\bar p_q\pmod N,
\]

and hence

\[
 e_N(x)=e_p(\bar q_px_p)e_q(\bar p_qx_q).
\tag{3}
\]

Inversion of a unit is coordinatewise under the CRT and recombination uses
the same idempotent basis.  Hence the same additive-character twist multiplies
both the linear and inverse frequency.  Consequently

\[
 \boxed{
 S_N(a,b)
 =S_p(\bar q_pa,\bar q_pb)
  S_q(\bar p_qa,\bar p_qb).}
\tag{4}
\]

Equivalently,

\[
 \widehat\mu_N(a,b)
 =\widehat\mu_p(\bar q_pa,\bar q_pb)
  \widehat\mu_q(\bar p_qa,\bar p_qb).
\tag{5}
\]

It would be wrong simply to delete the unit twists in (4): a common twist
changes the Kloosterman parameter by its square after one normalizes the
first coordinate.  The twists do not, however, change any of the zero/nonzero
classifications below.

## 2. Complete local and global degeneracy table

For a prime \(r\), put

\[
 S_r(A,B)=\sum_{x\in\mathbb F_r^\times}e_r(Ax+Bx^{-1}).
\]

There are exactly three local cases:

\[
 \begin{array}{c|c|c}
 \text{type}&(A,B)\pmod r&S_r(A,B)\\ \hline
 Z&(0,0)&r-1\\
 D&\text{exactly one coordinate is }0&-1\\
 K&A\ne0,\ B\ne0&|S_r(A,B)|\leq2\sqrt r.
 \end{array}
\tag{6}
\]

The \(D\) row follows by permuting \(\mathbb F_r^\times\), and the \(K\) row
is the classical Weil bound for a prime Kloosterman sum.  In terms of the
original integer frequency, \(Z_r\) means \(r\mid a\) and \(r\mid b\);
\(D_r\) means exactly one of these divisibilities; and \(K_r\) means neither.

Combining (4) and (6) gives the following exhaustive table.  Entries are
absolute normalized coefficients; entries containing a Weil bound are upper
bounds.

\[
\begin{array}{c|ccc}
 &Z_q&D_q&K_q\\ \hline
Z_p&1&\dfrac1{q-1}&\dfrac{2\sqrt q}{q-1}\\[6pt]
D_p&\dfrac1{p-1}&\dfrac1{(p-1)(q-1)}
   &\dfrac{2\sqrt q}{(p-1)(q-1)}\\[6pt]
K_p&\dfrac{2\sqrt p}{p-1}
   &\dfrac{2\sqrt p}{(p-1)(q-1)}
   &\dfrac{4\sqrt{pq}}{(p-1)(q-1)}.
\end{array}
\tag{7}
\]

This table includes all locally zero-coordinate cases.  Some useful special
cases are:

* if \(a=0\) and \(b\) is a unit modulo \(N\), both local types are \(D\) and

  \[
  \widehat\mu_N(0,b)=\frac1{\varphi(N)};
  \tag{8}
  \]

  the same holds with the two coordinates exchanged;
* if \(a=0\) and \(\gcd(b,N)=p\), the types are \(Z_p,D_q\) and

  \[
  \widehat\mu_N(0,b)=-\frac1{q-1};
  \tag{9}
  \]

  but the displayed frequency has already exposed \(p=\gcd(b,N)\);
* if both \(a,b\) share \(p\) but not \(q\), the types are \(Z_p,K_q\), so a
  coefficient as large as square-root scale over \(q\) is allowed, while
  \(\gcd(a,b,N)=p\) already splits \(N\);
* if \(p\mid a,q\mid b\) with neither opposite divisibility, both local types
  are \(D\), giving \(1/\varphi(N)\), and the separate coordinate gcds expose
  both factors.

Thus the large degenerate modes are not missing from (7); they are exactly
the modes that are locally the zero character in one CRT component.

### 2.1 The factor-free bound and its necessary exceptions

Let \((a,b)\ne(0,0)\) modulo \(N\), and set

\[
 d=\gcd(a,b,N).
\]

Call a mode **common-gcd-free** when \(d=1\).  Call it **publicly
factor-free** only when none of the three available screens
\(\gcd(a,b,N),\gcd(a,N),\gcd(b,N)\) is a nontrivial proper divisor of
\(N\).  The latter is a stronger condition: separate coordinate screens can
expose the two factors even when \(d=1\).

Because \(N=pq\), either \(d=1\), \(d=p\), or \(d=q\).  If \(d=p\) or
\(d=q\), the public frequency itself factors \(N\).  If \(d=1\), neither
local component can have type \(Z\); both local sums have magnitude at most
\(2\sqrt r\), including the smaller \(D\) case.  Therefore

\[
 \boxed{
 d=1\quad\Longrightarrow\quad
 |\widehat\mu_N(a,b)|
 \leq\delta_N:=\frac{4\sqrt N}{\varphi(N)}.}
\tag{10}
\]

On balanced odd semiprimes,

\[
 \delta_N=N^{-1/2+o(1)}.
\tag{11}
\]

There is hence no nontrivial common-gcd-free counterexample to the
preregistered single-mode claim, and in particular none among publicly
factor-free modes.  Two exceptions have to be stated rather than hidden:

1. The literal statement for *all* coefficients is false at the zero
   character, whose coefficient is \(1\).  It has the same expectation under
   the uniform discrete-torus baseline and carries no bias.
2. If the public-gcd restriction is removed, \(N^{-1/4}\)-scale coefficients
   really occur in the permitted square-root range.  Indeed

   \[
   \sum_{c\in\mathbb F_q}|S_q(1,c)|^2=q(q-1),
   \tag{12}
   \]

   by character orthogonality.  Since \(S_q(1,0)=-1\), some
   \(c\in\mathbb F_q^\times\) obeys

   \[
   |S_q(1,c)|^2\geq q-\frac1{q-1}.
   \tag{13}
   \]

   The factor-aware frequency \((a,b)=(p,pc)\) is \(Z_p,K_q\), because the
   \(q\)-twist in (4) turns it into \((1,c)\).  Hence

   \[
   |\widehat\mu_N(p,pc)|
   \geq\frac{\sqrt{q-1/(q-1)}}{q-1}
   =q^{-1/2+o(1)}=N^{-1/4+o(1)}
   \tag{14}
   \]

   on a balanced family.  This is a genuine counterexample to any
   *unrestricted* \(N^{-1/2}\) assertion, but \(p=\gcd(a,N)\) is already in
   its description.

The second-moment example proves that the public-gcd qualification is
structural, not merely an artifact of a loose Weil upper bound.

## 3. Polynomial Fourier lists and sparse trigonometric observables

Let \(\lambda_N\) be uniform measure on all of
\((\mathbb Z/N\mathbb Z)^2\).  Consider a public observable

\[
 F(x,y)=\sum_{j=1}^M c_j e_N(a_jx+b_jy),
 \qquad
 A=\sum_{j=1}^M|c_j|.
\tag{15}
\]

First combine duplicate frequencies and remove zero-character terms; the
latter have identical expectation under \(\mu_N\) and \(\lambda_N\).  For
every remaining mode compute

\[
 d_j=\gcd(a_j,b_j,N),
\]

and, if desired, the even stronger screens
\(\gcd(a_j,N),\gcd(b_j,N)\).  This gives a sharp dichotomy:

* if any screen is a nontrivial proper divisor \(1<d<N\), the frequency list
  has already factored \(N\);
* otherwise every remaining mode satisfies (10), and

  \[
  \boxed{
  |\mathbb E_{\mu_N}F-\mathbb E_{\lambda_N}F|
  \leq A\delta_N.}
  \tag{16}
  \]

In particular, \(M=\operatorname{poly}(\log N)\) modes with individually
polynomially bounded coefficients, or more generally any explicitly bounded
\(A=\operatorname{poly}(\log N)\), have total population bias

\[
 N^{-1/2+o(1)}.
\tag{17}
\]

The \(\ell^1\) coefficient bound in (16) is essential.  Sparsity alone does
not prevent an exponentially large numerical coefficient from amplifying an
exponentially small Fourier coefficient.

## 4. Axis-parallel rectangle discrepancy, with the hidden modes included

Embed the source in \([0,1)^2\) by

\[
 u\longmapsto (u/N,u^{-1}/N),
\]

using representatives in \(\{0,\ldots,N-1\}\).  Let \(D_N^*\) be its star
discrepancy from Lebesgue measure.

The two-dimensional Erdős--Turán--Koksma inequality says that for an
absolute constant \(C_2\) and every integer \(1\leq H<N\),

\[
 D_N^*\leq C_2\left(
 \frac1{H+1}+
 \sum_{\substack{|h_1|,|h_2|\leq H\\(h_1,h_2)\ne(0,0)}}
 \frac{|\widehat\mu_N(h_1,h_2)|}
 {\max(1,|h_1|)\max(1,|h_2|)}
 \right).
\tag{18}
\]

This is the standard tensor-product Erdős--Turán--Koksma construction from
the one-dimensional degree-\(H\) Selberg majorants and minorants: its
constant-term error is \(O((H+1)^{-1})\), and its nonzero Fourier weights are
\(O(1/\max(1,|h|))\) in each coordinate.  Thus (18) applies to this atomic
measure without a boundary-regularity assumption.

The modes sharing \(p\) or \(q\) cannot simply be discarded in (18), since
the discrepancy theorem sums all frequencies.  They can nevertheless be
counted exactly.  Define

\[
 \alpha_r=\frac{2\sqrt r}{r-1},\qquad
 L(H)=2\sum_{k=1}^H\frac1k,
\tag{19}
\]

and, with an empty sum interpreted as zero,

\[
 M_r(H)=\frac2r\sum_{k=1}^{\lfloor H/r\rfloor}\frac1k.
\tag{20}
\]

The local table implies the pointwise bound

\[
 \frac{|S_r(a,b)|}{r-1}
 \leq \alpha_r+\mathbf1_{r\mid a,\ r\mid b}.
\tag{21}
\]

The total Fourier weight in the square is

\[
 (1+L(H))^2-1,
\tag{22}
\]

whereas the weight of modes for which both coordinates are divisible by
\(r\) is

\[
 (1+M_r(H))^2-1.
\tag{23}
\]

Because \(H<N\), no nonzero frequency in the square has both coordinates
divisible by \(N\).  Expanding the product of the two bounds (21) in (18)
therefore gives the explicit inequality

\[
\boxed{
\begin{aligned}
D_N^*\leq C_2\Bigg[&\frac1{H+1}
+\alpha_p\alpha_q\big((1+L(H))^2-1\big)\\
&+\alpha_p\big((1+M_q(H))^2-1\big)\\
&+\alpha_q\big((1+M_p(H))^2-1\big)\Bigg].
\end{aligned}}
\tag{24}
\]

This is valid for every \(1\leq H<N\), with all cutoff dependence shown.
At \(H=N-1\),

\[
 M_p(N-1)=\frac2p\sum_{k=1}^{q-1}\frac1k,
 \qquad
 M_q(N-1)=\frac2q\sum_{k=1}^{p-1}\frac1k.
\tag{25}
\]

Using \(\sum_{k\leq t}1/k\leq1+\log t\) in (24) yields, on every fixed
balanced family,

\[
 \boxed{D_N^*=O_C\!\left(
 \frac{(1+\log N)^2}{\sqrt N}
 \right)=N^{-1/2+o(1)}.}
\tag{26}
\]

The generic \(K_p,K_q\) modes give the leading term.  The potentially larger
\(Z_p,K_q\) and \(K_p,Z_q\) coefficients only occur at frequencies divisible
by a hidden prime; the reciprocal-frequency weights in (18) contribute an
extra factor \(1/p\) or \(1/q\), so these modes are smaller than the leading
term after summation.  This is why the factor-aware \(N^{-1/4}\) example
(14) does not spoil coarse rectangular equidistribution.

For any half-open axis-parallel rectangle \(R\subset[0,1)^2\), inclusion and
exclusion of four anchored rectangles gives

\[
 |\mu_N(R)-\operatorname{area}(R)|\leq4D_N^*.
\tag{27}
\]

For any list of \(B\) axis-parallel rectangular bins, its population-mass
vector \(\theta\) and area vector \(a\) satisfy

\[
 \|\theta-a\|_\infty\leq4D_N^*,\qquad
 \|\theta-a\|_1\leq4B D_N^*.
\tag{28}
\]

If the bins form a disjoint exhaustive rectangular partition, as a
histogram will mean below, then both vectors are probability vectors and

\[
 d_{\rm TV}(\theta,a)=\tfrac12\|\theta-a\|_1\leq2B D_N^*.
\tag{28a}
\]

Thus every histogram with
\(B=\operatorname{poly}(\log N)\) rectangular bins has aggregate population
deviation \(N^{-1/2+o(1)}\).  Equation (28) concerns fixed axis-parallel
rectangles.  A diagonal magnitude bin, a curved region, or a sample-adaptive
partition is not silently included.

## 5. Exactly what the empirical sample bound does and does not prove

Fix one factor-free nonzero mode and let

\[
 X=e_N(au+bu^{-1}),\qquad \mu=\mathbb EX=\widehat\mu_N(a,b).
\]

For \(m\) independent unit samples and their raw empirical Fourier mean
\(\overline X_m\), there is an exact identity

\[
 \mathbb E|\overline X_m-\mu|^2
 =\frac{1-|\mu|^2}{m}.
\tag{29}
\]

Consequently, relative root-mean-square accuracy

\[
 \big(\mathbb E|\overline X_m-\mu|^2\big)^{1/2}
 \leq\eta|\mu|
\]

requires

\[
 m\geq\frac{1-|\mu|^2}{\eta^2|\mu|^2}.
\tag{30}
\]

If \(\mu\ne0\), (10) makes the right side at least

\[
 \frac{1-\delta_N^2}{\eta^2\delta_N^2}
 =N^{1-o(1)}
\tag{31}
\]

on balanced semiprimes.  If \(\mu=0\), there is no mean bias to read.

This is not merely a variance slogan.  When \(\delta_N\leq1/2\), the centered
summands in (29) are bounded by \(2\) and have variance at least \(3/4\).
An elementary fourth-moment expansion gives

\[
 \mathbb E|\overline X_m-\mu|^4\leq C/m^2
\]

for an absolute \(C\).  Paley--Zygmund applied to
\(|\overline X_m-\mu|^2\) therefore supplies absolute constants
\(c_0,c_1>0\) such that

\[
 \Pr\!\left(
 |\overline X_m-\mu|\geq c_1m^{-1/2}
 \right)\geq c_0.
\tag{32}
\]

More precisely, if

\[
 m<\frac{c_1^2}{\eta^2|\mu|^2},
\]

then relative error exceeds \(\eta|\mu|\) with probability at least \(c_0\).
Thus obtaining relative accuracy from the *raw empirical mean* with success
confidence greater than \(1-c_0\) needs
\(m=\Omega(|\mu|^{-2})\), and therefore \(N^{1-o(1)}\) samples under (10).

For one histogram bin with population mass \(\theta\), its empirical
frequency \(\widehat\theta_m\) obeys the equally exact identity

\[
 \mathbb E(\widehat\theta_m-\theta)^2
 =\frac{\theta(1-\theta)}m.
\tag{33}
\]

If the bin area and its complement are at least inverse-polynomial in
\(\log N\), then (27) makes \(\theta(1-\theta)\) inverse-polynomial for all
large \(N\).  Relative empirical estimation of a nonzero deviation
\(\theta-\operatorname{area}(R)\), whose magnitude is at most (26), again
requires \(N^{1-o(1)}\) samples by (33), up to polynomial and logarithmic
factors.  The same conclusion for a bounded sparse observable requires a
stated lower bound on its sample variance; cancellations can otherwise make
that variance zero.

No arbitrary-algorithm sample lower bound follows.  In particular:

* each pair satisfies the exact nonlinear relation \(uv\equiv1\pmod N\), so
  the source is not statistically close to uniform on all pairs;
* the samples are generated from the already known \(N\), and therefore do
  not supply external information about \(N\);
* a nonlinear statistic can use aspects of the sample distribution that its
  selected empirical Fourier mean or histogram discards; and
* an exact evaluator for an exponentially small population bias could, in
  principle, avoid Monte Carlo estimation altogether.

For a regular polynomial-resolution bin the centered Bernoulli fourth moment
gives the analogous conclusion at a sufficiently high absolute constant
confidence (quantified by its own Paley--Zygmund constant) after only an
inverse-polynomial burn-in; this is still a statement about that one raw bin
frequency, not a joint nonlinear use of the histogram.

Rejection sampling a uniform residue until it is a unit is expected-constant
time here.  A rejected residue whose gcd is \(p\) or \(q\) is a separate
local-zero ticket of probability

\[
 \frac{p+q-2}{N}=N^{-1/2+o(1)}
\]

per proposal on a balanced family; polynomially many proposals do not turn
that event into inverse-polynomial success.

## 6. Scope, candidate verdict, and exact retry condition

The proved conclusion is distributional and statistic-specific:

* every nonzero public additive Fourier mode either exposes a nontrivial
  proper gcd or has normalized bias at most \(4\sqrt N/\varphi(N)\);
* a polynomial-\(\ell^1\) bounded sparse trigonometric observable has only
  \(N^{-1/2+o(1)}\) population bias unless its frequency list already factors
  \(N\);
* every polynomial-size axis-parallel rectangular histogram has only
  \(N^{-1/2+o(1)}\) aggregate population deviation; and
* estimating such a nonzero bias by its ordinary empirical mean needs
  \(N^{1-o(1)}\) independent samples in the precise relative-RMSE sense
  above, with the stated sufficiently-high-absolute-confidence strengthening
  for one Fourier character or one regular bin.

It is **not** a factoring lower bound, a computational indistinguishability
claim, or an assertion that bare \(N\) cannot manufacture a metric hint.
It does not cover nonlinear or Fourier-dense/high-complexity statistics,
implicit searches for hidden high-bias frequencies, adaptive frequencies
chosen from the same sample transcript, correlated or nonuniform arithmetic
sources, noisy approximate-common-divisor/hidden-number/Coppersmith lattice
decoding, noninvertible or dissipative dynamics, curved or diagonal magnitude
bins, or exact symbolic evaluation of tiny biases.

**Candidate verdict:** the preregistered F39 obstruction survives, after the
necessary zero-character convention and public-gcd exception are made
explicit.  The simple inverse-pair cloud fails as a polynomial-sample metric
source for ordinary empirical means of public polynomial Fourier lists,
polynomial-\(\ell^1\) linear combinations of those means, and polynomial
rectangular histograms in the stated raw-frequency sense.  Arbitrary
nonlinear processing of a Fourier transcript is not covered, and the broader
F24 family remains open.

**Exact retry condition:** a retry must exhibit at least one of the following:

1. a factor-free, polynomial-time evaluable nonlinear or Fourier-dense
   observable whose factor-dependent population signal is proved
   inverse-polynomial on every target input;
2. an implicit hidden-frequency decoder that does not first materialize a
   frequency having a nontrivial proper gcd with \(N\), with a proved
   polynomial-time recovery law;
3. a correlated/adaptive or dissipative source whose full generation cost is
   polynomial and whose factor-dependent nonequilibrium bias is proved
   inverse-polynomial; or
4. a rigorous noisy ACD/HNP/Coppersmith-style reduction showing that the tiny
   inverse-cloud deviations satisfy the quantitative error and sample
   thresholds of a polynomial-time lattice decoder.

Merely pooling polynomially many more independent unit/inverse samples in
the same ordinary empirical means, taking polynomial-\(\ell^1\) linear
combinations of polynomially many public frequencies, or refining an
axis-parallel raw-frequency histogram by only polynomially many bins is
covered by the obstruction above.
