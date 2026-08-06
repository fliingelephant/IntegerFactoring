# Metric ACD decoding by ordinary LLL

## Setting and conventions

Let
\[
N=pq,\qquad n=\lceil \log _2N\rceil,
\]
where (p\ne q) are balanced odd primes. Thus, in the asymptotic statements,
\(log _2p= n/2+O(1)\) and \(\log _2q=n/2+O(1)\). Let (m\geq1), put
\(d=m+1\), and suppose
\[
z_i=pt_i+r_i\in[0,N),\qquad t_i\mathrel{\mathop\sim}^{\mathrm{iid}}
\operatorname{Unif}(\mathbb Z/q\mathbb Z),
\]
with (1\leq B<p/8), \(|r_i|\leq B\), and
\(\epsilon=B/p<1/8\). For every possible quotient vector
\(t=(t_1,\ldots,t_m)\), the whole vector (r=(r_1,\ldots,r_m)) may be an
arbitrary function of (t); in particular, neither coordinatewise nor
probabilistic independence of the errors is assumed. All logarithms in the
asymptotic calculations below are base two. We use \(\|x\|\) for distance to
the nearest integer.

The algorithm may first compute \(\gcd(z_i,N)\) and
\(\gcd(z_i-z_j,N)\) for all relevant (i,j), returning any proper divisor.
These checks can only increase its success probability. Importantly, the
probability proofs below are unconditional: we never condition the independent
quotients on those checks having failed.

## A. Approximation denominators

### Simultaneous Dirichlet lemma

For arbitrary real \(\alpha_1,\ldots,\alpha_m\) and real (A\geq2^m), there
is an integer (a) with
\[
1\leq a\leq A,\qquad \max_i\|a\alpha_i\|\leq2A^{-1/m}.
\]

Indeed, set (K=\lfloor A^{1/m}\rfloor). Since (A^{1/m}\geq2),
\[
K\geq \tfrac12 A^{1/m},\qquad K^m\leq A.
\]
Partition \([0,1)^m\) into (K^m) half-open cubes of side (1/K), and place
the (K^m+1) points
\[
(\{j\alpha_1\},\ldots,\{j\alpha_m\}),\qquad 0\leq j\leq K^m,
\]
in those cubes. Two points lie in the same cube. Subtracting their indices
gives (1\leq a\leq K^m\leq A), and subtraction in every coordinate gives
\(\|a\alpha_i\|\leq1/K\leq2A^{-1/m}\).

### A shorter non-(q)-denominator vector

Consider the relation lattice
\[
L=\{(aB,az_1-Nk_1,\ldots,az_m-Nk_m):a,k_1,\ldots,k_m\in\mathbb Z\}.
\]
Suppose
\[
\left(\frac{2\sqrt d}{\epsilon}\right)^m<\frac q{2\sqrt d}.
\tag{A1}
\]
Apply the lemma to \(\alpha_i=z_i/N\) with
\(A_0=q/(2\sqrt d)\). This (A_0) is at least (2^m): its lower bound in
(A1) is already greater than (2^m), since \(\epsilon<1/8\). Taking each
\(k_i\) to be a nearest integer to \(az_i/N\), the resulting lattice vector
satisfies
\[
1\leq a\leq \frac q{2\sqrt d}<q,
\]
and
\[
|az_i-Nk_i|\leq2N A_0^{-1/m}
  <\frac{\epsilon N}{\sqrt d}=\frac{qB}{\sqrt d}.
\]
Also (aB\leq qB/(2\sqrt d)\). Hence
\[
\begin{split}
\|(aB,az_1-Nk_1,\ldots,az_m-Nk_m)\|_2^2
&<q^2B^2\left(\frac1{4d}+\frac m d\right)\\
&<q^2B^2.
\end{split}
\]
Thus its norm is strictly less than (qB), and (q\nmid a).

The designated factor vector is obtained by taking (a=q) and (k_i=t_i):
\[
v_q=(qB,qz_1-Nt_1,\ldots,qz_m-Nt_m)
    =(qB,qr_1,\ldots,qr_m).
\]
Its norm is at least (qB), so (v_q) is not a shortest vector.

There is a stronger coprimality conclusion under the separately stated
hypothesis that some (A) obeys
\[
\left(\frac{2\sqrt d}{\epsilon}\right)^m<A<min\left(p,\frac q{\sqrt d}\right).
\tag{A2}
\]
The same lemma now gives (1\leq a\leq A), residual coordinates strictly
smaller than (qB/\sqrt d), and (aB<qB/\sqrt d). The vector therefore again
has norm less than (qB). Moreover (a<p) and (a<q), so neither prime can
divide (a), and \(\gcd(a,N)=1\).

These observations do **not** prove that an SVP-plus-gcd decoder fails. They
only show that the particular vector (v_q) is not shortest. A still shorter
vector whose first coefficient is divisible by the other prime (p), for
example, is not excluded.

### Uniform probability bound for small denominators

Fix (a) with (1\leq a<q). If
\[
\max_i\left\|\frac{az_i}{N}\right\|\leq\epsilon,
\]
then for every (i), irrespective of how all errors were jointly selected,
\[
\left\|\frac{at_i}{q}\right\|
\leq \left\|\frac{az_i}{N}\right\|+\frac{a|r_i|}{N}
\leq\epsilon+\frac{(q-1)B}{pq}<2\epsilon.
\tag{A3}
\]
Multiplication by (a) permutes \(\mathbb Z/q\mathbb Z\). The number of
residues (u) satisfying \(\|u/q\|\leq2\epsilon\) is at most
\(4\epsilon q+1\). Since the (t_i) are independent, the probability for a
fixed (a) is at most
\[
\left(4\epsilon+\frac1q\right)^m.
\]
A union bound over (a=1,\ldots,q-1) consequently gives
\[
\Pr\!\left[\exists,1\leq a<q:
  \max_i\left\|\frac{az_i}{N}\right\|\leq\epsilon\right]
\leq q\left(4\epsilon+\frac1q\right)^m.
\tag{A4}
\]
The implication (A3) removed the errors before probability was evaluated, so
(A4) is uniform over every admissible joint error function.

All the conclusions in this part concern simultaneous approximation and its
denominator. They are not, by themselves, decoder-success or decoder-failure
theorems. For example, writing (Q=\log q\), the exact deterministic condition
is
\[
m\left(\log(1/\epsilon)+1+\tfrac12\log d\right)
 < Q-1-\tfrac12\log d.
\]
At \(\epsilon=n^{-c}\), both this transition and the transition in (A4) occur
only coarsely at (m=\Theta(n/\log n)). In particular, the
\(\tfrac12\log d\) term coming from the \(\sqrt m\) loss has not been erased;
it changes the leading constant when (m\asymp n/\log n).

## B. The ordinary-LLL decoder

Use the row basis
\[
M=\begin{pmatrix}
B&z_1&z_2&\cdots&z_m\\
0&N&0&\cdots&0\\
0&0&N&\cdots&0\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
0&0&0&\cdots&N
\end{pmatrix}.
\]
It is triangular, so
\[
\det L=BN^m.
\]
Every lattice vector has the form
\[
(aB,az_1-Nk_1,\ldots,az_m-Nk_m)
\tag{B1}
\]
for integers (a,k_i). This form is unique: the first coordinate uniquely
determines (a), and then every other coordinate uniquely determines its
integer multiple of (N).

Run ordinary LLL with \(\delta=3/4\), and let
\[
b_1=(aB,w_1,\ldots,w_m)
\]
be its first vector. The standard first-vector guarantee in dimension
\(d=m+1\) is
\[
\|b_1\|_2\leq2^{(d-1)/2}\lambda_1(L)=2^{m/2}\lambda_1(L).
\]
Put
\[
\Gamma=2^{m/2},\qquad
R=\Gamma qB\sqrt d,\qquad
A=R/B=\Gamma q\sqrt d,
\]
and
\[
\rho=R/N=\Gamma\epsilon\sqrt d,
\qquad
\theta=\min\left(1,4\Gamma\epsilon\sqrt d+\frac1q\right)
       =\min\left(1,4\rho+\frac1q\right).
\]
Because (v_q\in L) and \(\|v_q\|_2\leq qB\sqrt d\),
\[
\|b_1\|_2\leq R.
\tag{B2}
\]

Assume now that (R<N) and (A<N). If (a=0), (B1) says that every
nonzero coordinate of (b_1) is a nonzero multiple of (N), whence
\(\|b_1\|_2\geq N\), contradicting (B2). Thus (a\ne0). Further,
\[
1\leq |a|\leq R/B=A<N.
\tag{B3}
\]
The decoder computes \(\gcd(|a|,N)\). If this gcd is not proper, it is either
1 or (N). The second case is impossible under (B3), so decoder failure
implies \(\gcd(a,N)=1\). This also deals with all factor-bearing multiples,
not merely (a=\pm q): if (q\mid a) (or (p\mid a)) and (a\ne0), then
\(|a|<N\) makes the gcd a proper factor.

Fix any signed integer (a) in (B3) that is coprime to (N). If this (a)
can occur in a vector satisfying (B2), then (B1) gives, for every (i),
\[
\left\|\frac{az_i}{N}\right\|\leq\frac{|w_i|}{N}\leq\rho.
\]
Since \(|a|\leq A\),
\[
\left\|\frac{at_i}{q}\right\|
\leq\rho+\frac{|a|B}{N}
\leq\rho+\frac{AB}{N}=2\rho.
\tag{B4}
\]
Here (q\nmid a), including for negative (a), so multiplication by (a)
again permutes \(\mathbb Z/q\mathbb Z\). At most
\(\min(q,4\rho q+1)\) residues obey (B4). Independence of the quotients
therefore bounds the probability for this fixed signed (a) by
\(\theta^m\), uniformly over the joint error function.

There are at most (2\lfloor A\rfloor\leq2A) possible nonzero signed
integers. A union bound proves
\[
\Pr[\text{all public checks and the LLL gcd step fail}]
 \leq 2A\theta^m,
\]
or equivalently
\[
\Pr[\text{success}]\geq1-2A\theta^m.
\tag{B5}
\]
No union over the integers (k_i) is needed. For a fixed (a), existence of
any choices of (k_i) with bounded residuals is exactly the torus-distance
condition used in (B4); all possible nearest multiples of (N) have already
been collapsed into that one condition.

This probability statement holds for every deterministic map
\(t\mapsto r(t)\) satisfying the stated range and magnitude constraints. It
also holds for randomized errors by conditioning on their extra randomness.
Prepending the public gcd checks does not require conditioning on their
failure: total algorithmic failure is simply a subset of the bad event just
bounded.

## C. Consequences and optimization of the certificate

### Fixed slack

Fix \(\eta>0\), and suppose
\[
\epsilon\leq2^{-(1+\eta)\sqrt n},\qquad
m=\left\lfloor(1+\eta/2)\sqrt n\right\rfloor.
\]
Write \(\kappa=1+\eta/2\). Then
\[
\log A=\log q+\frac m2+\frac12\log d
      =\frac n2+O(\sqrt n)<\log N
\]
for all sufficiently large (n), so (A<N). Also
\[
\frac RN=\Gamma\epsilon\sqrt d,
\qquad
\log(R/N)\leq
\frac m2-(1+\eta)\sqrt n+\frac12\log d
=-\left(\frac12+\frac{3\eta}{4}\right)\sqrt n+O(\log n)<0,
\]
so (R<N).

Let
\(\bar\rho=2^{m/2-(1+\eta)\sqrt n}\sqrt d\). Since
\(q^{-1}=2^{-n/2+O(1)}=o(\bar\rho)\), for large (n)
\[
\theta\leq5\bar\rho.
\]
Using \(\log q=n/2+O(1)\), (B5) gives
\[
\begin{split}
\log(2A\theta^m)
&\leq \log q+\frac{m^2}{2}-m(1+\eta)\sqrt n
      +\frac m2\log d+O(m)\\
&=\left(\frac12+\frac{\kappa^2}{2}
        -\kappa(1+\eta)\right)n+o(n)\\
&=-\left(\eta+\frac{3\eta^2}{8}\right)n+o(n).
\end{split}
\]
Consequently the failure probability is (2^{-\Omega_\eta(n)}\).

### Vanishing relative slack

The same certificate reaches an exponent
\(\log(1/\epsilon)=(1+o(1))\sqrt n\), but its lower-order terms matter. Let
\[
L_n=\sqrt n+\frac14\log n+s_n,
\qquad s_n\longrightarrow\infty,
\qquad s_n=o(\sqrt n),
\]
assume \(\epsilon\leq2^{-L_n}\), and choose
\[
m=\left\lfloor L_n-\frac12\log L_n\right\rfloor.
\]
Then (m\sim\sqrt n). As above, the (q^{-1}) term is negligible compared
with the displayed upper bound on \(\Gamma\epsilon\sqrt d\), so
\[
\begin{split}
\log(2A\theta^m)
&\leq \log q+\frac{m^2}{2}-mL_n+\frac m2\log d
 +(\log 5+\tfrac12)m+O(\log d)\\
&\leq \log q-\frac{L_n^2}{2}
       +\frac{L_n}{2}\log L_n+O(L_n)\\
&=-(1-o(1))s_n\sqrt n.
\end{split}
\tag{C1}
\]
The cancellation producing the \(\tfrac14\log n\) correction is explicit:
the term \(-L_n^2/2\) contributes
\(-\tfrac14\sqrt n\log n\), while
\((L_n/2)\log L_n\) contributes
\(+\tfrac14\sqrt n\log n\). Thus, for example,
\[
\epsilon\leq
2^{-\sqrt n-(1/4)\log n-s_n}
=2^{-(1+o(1))\sqrt n}
\]
gives a vanishing bound, with (C1) quantifying it. For a sufficiently large
fixed additive constant in place of (s_n), the same calculation gives
\(2^{-\Omega(\sqrt n)}\); taking (s_n\to\infty) avoids hiding the absolute
constant in the (O(L_n)) term. The choices also satisfy (A<N) and (R<N):
\(\log A=n/2+O(\sqrt n)<\log N\), while
\(\log(R/N)\leq m/2-L_n+(1/2)\log d<0\) for large (n).

### What the certificate says for polynomial relative error

Now take \(\epsilon=n^{-c}\) for a fixed (c>0), and put
\(L=c\log n\). Let
\(F_m=2A\theta^m\), the proved upper bound on failure. If \(\theta=1\), then
plainly (F_m=2A>1). If \(\theta<1\), then
\[
4\Gamma\epsilon\sqrt d<1,
\]
which implies (m<2L) for all sufficiently large (n). Moreover
\(A\geq q\) and \(\theta\geq4\Gamma\epsilon\sqrt d\geq4\epsilon\). Hence
\[
\log F_m\geq1+\log q+m(2-L)
>1+\log q+2L(2-L)
=\frac n2-O((\log n)^2)>0.
\]
Thus no choice of (m) makes this particular worst-case ordinary-LLL failure
certificate nontrivial at \(\epsilon=n^{-c}\). This is only a limitation of
the proved bound. It is not an LLL hardness result, an ACD hardness result, or
a lower bound for any more general decoder.

## D. Complexity and the precise algorithmic scope

The public gcd computations are polynomial-time. The basis has dimension
\(m+1\), determinant (BN^m), and entries of (O(n)) bits (with the usual
integer input parameter (B); a rational (B) of polynomial encoding length
can equivalently be cleared by a common scale). Exact ordinary LLL with
\(\delta=3/4\) runs in time polynomial in the dimension and input bit length.
Reading (a) from the first coordinate and computing \(\gcd(|a|,N)\) are also
polynomial-time. Thus the decoder is polynomial in its full batch input size;
in the corollaries (m=O(\sqrt n)\), so it is polynomial in (n).

There is a conditional Las Vegas conversion. Suppose a separate
polynomial-time source supplies fresh batches whose quotient vectors are
independent and uniform as stipulated. On each batch, run the public checks
and LLL decoder, verify any returned proper divisor, and retry on failure. If
\(\delta=2A\theta^m<1\), the conditional success probability of every fresh
attempt is at least (1-\delta), even if that batch's joint errors are selected
adversarially after its quotient vector is known. The expected number of
batches is at most (1/(1-\delta)); in the fixed-slack regime it is
\(1+2^{-\Omega_\eta(n)}\). Verification makes the procedure zero-error.

No method for producing even one such batch from bare (N) is constructed
here. The theorem is only for the balanced-semiprime, granted-source model. It
is therefore not an all-input factoring algorithm, nor the requested bare-
(N) factoring algorithm. No Coppersmith benchmark is used or needed as a
premise.

## Verdict and reconstruction attestation

With the standard exact/rational encoding assumption for the public scale
(B), the supplied statement is correct. Every constant in the deterministic
and probabilistic bounds above follows from the stated hypotheses; in
particular, the \(\sqrt m\) loss, signed values of (a), (a=0), and arbitrary
nonzero multiples of a factor have all been retained.

This was a proof-blind reconstruction. Before writing this file, I did not
read or list any filesystem file. In particular, I did not inspect any
pre-existing candidate solution or candidate `RESULT.md`, any audit or
re-audit, any canonical research file, any other experiment artifact, any
repository source or documentation file, or any git status, diff, log,
commit, branch, or other history object. I used only the statement supplied in
the task. The only repository artifact I touched was this target file, which I
created without reading a prior version.
