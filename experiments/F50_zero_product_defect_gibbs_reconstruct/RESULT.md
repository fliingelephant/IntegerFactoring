# Zero-product defect Gibbs: proof-blind reconstruction

## 1. Precise model and the necessary interpretation

Let (N\ge 2), let (R=\mathbb Z/N\mathbb Z), and let (\lambda>0). Define

\[
\mathcal S_N=\{(k,x,d)\in R^3:d=kx\},\qquad
w_\lambda(d)=
\begin{cases}
1,&d=0,\\
\lambda,&d\ne0.
\end{cases}
\]

The target law is

\[
\pi_{N,\lambda}(k,x,d)
=\frac{w_\lambda(d)}{Z_{N,\lambda}}\mathbf 1_{\{d=kx\}},
\qquad
Z_{N,\lambda}=M_N+\lambda(N^2-M_N),
\]

where

\[
\Omega_N=\{(k,x)\in R^2:kx=0\},\qquad M_N=|\Omega_N|.
\]

The only nondegenerate meaning of a single-coordinate refresh is a refresh of one
of the two free coordinates (k,x), followed by the deterministic assignment
(d\leftarrow kx). Thus (d) is a recorded defect, not an independently held
coordinate. Under this convention, conditioning the target on (d=0) gives

\[
\pi_{N,\lambda}((k,x)\mid d=0)=\operatorname{Unif}(\Omega_N),
\]

independently of (\lambda).

This interpretation matters. Literal Gibbs updates of one of the three displayed
coordinates while holding the other two fixed leave (d) invariant: a (d)-update
is deterministic, and a (k)- or (x)-update must preserve the fixed (d).
That literal chain is reducible, and the scalar activity is constant on each
communicating class. It cannot mix to the full target. The rest of this
reconstruction uses the free-coordinate convention above.

## 2. Exact random-scan Gibbs kernel

For (b\in R), use its representative in \(\{0,\ldots,N-1\}\), and put

\[
g_b=\gcd(b,N).
\]

The annihilator

\[
A_b=\{y\in R:yb=0\}
\]

has exactly (g_b) elements. Indeed, after writing (N=g_bm) and
(b=g_bb') with \(\gcd(b',m)=1\), the condition is (m\mid y), so

\[
A_b=\{0,m,2m,\ldots,(g_b-1)m\}.
\]

The exact conditional distribution for a refreshed coordinate is therefore

\[
Q_{b,\lambda}(y)
=\frac{\mathbf 1_{\{yb=0\}}+\lambda\mathbf 1_{\{yb\ne0\}}}
{g_b+(N-g_b)\lambda}.
\tag{2.1}
\]

One Gibbs step chooses (k) or (x) with probability (1/2), samples the
chosen coordinate from (2.1) conditional on the other coordinate (b), and
recomputes (d=kx). This is reversible with respect to
\(\pi_{N,\lambda}\). Because \(\lambda>0\), every conditional has full support
on (R); hence the chain on (R^2\) is irreducible and aperiodic and has the
unique stationary law \(\pi_{N,\lambda}\).

### Exact fair-bit implementation for \(\lambda=1/N\)

Let (g=g_b), (m=N/g), and

\[
D=gN+(N-g)=gN+N-g.
\]

After multiplying all conditional weights by (N), each member of (A_b)
has (N) tickets and each member of its complement has one ticket. Draw an
integer (J\) uniformly from \(\{0,\ldots,D-1\}\).

* If (J<gN), return
  \[
  y=m\left\lfloor\frac{J}{N}\right\rfloor.
  \]
  Each member of (A_b) has exactly (N) preimages.
* If (J\ge gN), put (r=J-gN). This branch is impossible when (g=N).
  Otherwise (m\ge2), write
  \[
  r=q(m-1)+s,\qquad 0\le s<m-1,
  \]
  and return
  \[
  y=qm+s+1.
  \]
  This is a bijection from \(\{0,\ldots,N-g-1\}\) to
  (R\setminus A_b).

To draw (J), take (L=\lceil\log_2D\rceil) fair bits and reject values at
least (D). The acceptance probability is greater than (1/2), and
(D\le N^2). Thus a refresh uses (O(\log N)) expected fair bits. If
(n=\lceil\log_2N\rceil) and (M(n)) is the bit cost of (n)-bit
multiplication, the gcd, divisions, and modular multiplication cost
(O(M(n)\log n)) bit operations. This is (O(n^2\log n)) with schoolbook
arithmetic and is polynomial in the input length. No prime factorization of
(N) is used. If the gcd itself is a proper divisor, the requested factor
has already been found.

For an arbitrary real activity, (2.1) defines an exact mathematical kernel.
An exact fair-bit implementation additionally needs an effective
representation or Bernoulli oracle for \(\lambda\). No such claim is made
here for an unspecified real scalar.

## 3. Screens, proper nonunits, and the one-step hazard

Define

\[
H_N=\{a\in R:1<\gcd(a,N)<N\},\qquad h_N=|H_N|,
\]

and define the safe set

\[
C_N=\{0\}\cup R^\times.
\]

The natural coordinate screens compute \(\gcd(a,N)\) for every newly observed
coordinate (a\in\{k,x,d\}) and stop when the result is strictly between
(1) and (N). Before that stopping time, every screened coordinate is in
(C_N): gcd (N) means the residue is (0), and gcd (1) means it is a
unit. Moreover, if (k,x\in C_N), then (d=kx) is also either (0) or a
unit.

Suppose the other free coordinate is (b\in C_N).

* If (b=0), then every product is zero and (Q_{b,\lambda}) is uniform on
  (R). The probability that the refreshed coordinate is in (H_N) is
  exactly (h_N/N).
* If (b) is a unit, then (yb=0) only for (y=0). Hence
  \[
  Q_{b,\lambda}(H_N)
  =\frac{h_N\lambda}{1+(N-1)\lambda}.
  \tag{3.1}
  \]

Consequently, for every pre-hit history and either random-scan choice,

\[
\Pr(\text{coordinate-gcd hit on the next refresh}\mid\text{history})
\le
\begin{cases}
h_N/N,&\lambda=1/N,\\[2mm]
h_N/(N-1),&\lambda>0.
\end{cases}
\tag{3.2}
\]

For the canonical activity, the unit-conditioned value in (3.1) is
(h_N/(2N-1)), while the zero-conditioned value is the raw density (h_N/N).
For general positive \(\lambda\), (3.1) is at most (h_N/(N-1)), and
(h_N/N\le h_N/(N-1)). These bounds do not assume independence between
successive steps.

## 4. Exact counts for the two requested families

All residues are partitioned into zero, units, and proper nonunits, so in
general

\[
h_N=N-\varphi(N)-1.
\tag{4.1}
\]

### Distinct semiprime \(N=pq\)

Let (p<q) be distinct primes. The nonzero multiples of (p) contribute
(q-1) residues, and the nonzero multiples of (q) contribute (p-1)
residues. The two sets are disjoint modulo (pq). Therefore

\[
\boxed{h_{pq}=p+q-2.}
\tag{4.2}
\]

By the Chinese remainder theorem, the number of zero-product pairs is

\[
\boxed{M_{pq}=(2p-1)(2q-1).}
\tag{4.3}
\]

### Prime square \(N=p^2\)

The proper nonunits are the nonzero multiples of (p), so

\[
\boxed{h_{p^2}=p-1.}
\tag{4.4}
\]

A zero product either has at least one zero coordinate, giving (2p^2-1)
pairs, or has two nonzero multiples of (p), giving ((p-1)^2) more pairs.
Thus

\[
\boxed{M_{p^2}=3p^2-2p=p(3p-2).}
\tag{4.5}
\]

The formulas (4.2) and (4.4) must not be conflated when (p=q).

## 5. Hitting-time lower bounds

Let the initial law be supported on (C_N^2), and let

\[
\tau=\inf\{t\ge1:K_t\in H_N\text{ or }X_t\in H_N\}.
\]

This is the first success time for the coordinate-gcd screens. If (r) is
either bound in (3.2), then for every integer (t\ge0),

\[
\Pr(\tau>t)\ge(1-r)^t,
\qquad
\Pr(\tau\le t)\le1-(1-r)^t\le tr,
\tag{5.1}
\]

and the tail-sum formula gives

\[
\mathbb E\tau\ge\frac1r.
\tag{5.2}
\]

For (h_N=0), the right interpretation is \(\mathbb E\tau=\infty\).

For distinct (pq),

\[
\mathbb E\tau\ge
\begin{cases}
\dfrac{pq}{p+q-2},&\lambda=1/N,\\[3mm]
\dfrac{pq-1}{p+q-2},&\lambda>0.
\end{cases}
\tag{5.3}
\]

Fix (C\ge1), and call the family (C)-balanced when
(p<q\le Cp). Then

\[
\frac{p+q-2}{\sqrt{pq}}
\le \sqrt C+\frac1{\sqrt C},
\]

so both bounds in (5.3) are \(\Omega_C(\sqrt N)\). Without balance, the
exact lower bound is only of order the smaller prime; no unconditional
\(\Omega(\sqrt N)\) claim is valid.

For (N=p^2),

\[
\mathbb E\tau\ge
\begin{cases}
\dfrac{p^2}{p-1}=p+1+\dfrac1{p-1},&\lambda=1/N,\\[3mm]
\dfrac{p^2-1}{p-1}=p+1,&\lambda>0,
\end{cases}
\tag{5.4}
\]

which is \(\Omega(\sqrt N)\).

These are lower bounds in Gibbs refreshes. Since one exact refresh has
polynomial expected bit cost and performs at least one elementary random-scan
operation, the canonical local mechanism also needs
\(\Omega(\sqrt N)\) elementary operations on these families. This is
exponential in the input length \(\lceil\log_2N\rceil\).

## 6. Finite-time total-variation lower bounds

Let

\[
B_N=\{(k,x,d)\in\mathcal S_N:k\in H_N\text{ or }x\in H_N\}.
\]

On the graph (d=kx), this is also the event that at least one of the three
coordinates is a proper nonunit. If the chain starts in (C_N^2), then

\[
\mu_t(B_N)\le\Pr(\tau\le t),
\tag{6.1}
\]

where \(\mu_t\) is its time-(t) law.

Put \(\phi=\varphi(N)\). The total target weight of the complement of (B_N)
is

\[
1+2\phi+\lambda\phi^2:
\]

there are (1+2\phi) safe zero-product pairs and \(\phi^2\) unit-unit
pairs. Hence the exact stationary mass of the factor-bearing event is

\[
\beta_{N,\lambda}
=\pi_{N,\lambda}(B_N)
=1-\frac{1+2\phi+\lambda\phi^2}
{M_N+\lambda(N^2-M_N)}.
\tag{6.2}
\]

Combining (5.1), (6.1), and the event characterization of total variation
gives, for every (t\ge0),

\[
\boxed{
\|\mu_t-\pi_{N,\lambda}\|_{\mathrm{TV}}
\ge
\left[\beta_{N,\lambda}
-1+(1-r)^t\right]_+
\ge[\beta_{N,\lambda}-tr]_+ .}
\tag{6.3}
\]

For the canonical activity, use (r=h_N/N). For distinct (pq), (6.2) is
the explicit expression

\[
1-
\frac{1+2(pq-p-q+1)+(pq-p-q+1)^2/(pq)}
{(2p-1)(2q-1)+\bigl(p^2q^2-(2p-1)(2q-1)\bigr)/(pq)}.
\tag{6.4}
\]

It tends to (2/5) along every fixed-balance family. More crudely but
uniformly, the zero-product part of (B_N) alone has weight (2(N-1)), and
the canonical normalizer is less than (5N). Thus, for every distinct
semiprime (N\ge6),

\[
\beta_{N,1/N}>\frac{2(N-1)}{5N}\ge\frac13.
\tag{6.5}
\]

For (N=p^2), (6.2) simplifies to

\[
\boxed{
\beta_{p^2,1/p^2}
=\frac{p^2+2p-5+2/p}{4p^2-2p-3+2/p}.}
\tag{6.6}
\]

It is greater than (1/4) for every prime (p\ge2) and tends to (1/4).
The zero-product contribution alone gives the convenient uniform bound

\[
\beta_{p^2,1/p^2}>\frac{N-1}{4N}\ge\frac3{16}.
\tag{6.7}
\]

For example, for every integer (t\) satisfying

\[
t\le\frac{N}{32h_N},
\tag{6.8}
\]

(6.3) gives

\[
\|\mu_t-\pi_{N,1/N}\|_{\mathrm{TV}}
>
\begin{cases}
29/96,&N=pq\text{ with }p<q,\\
5/32,&N=p^2.
\end{cases}
\tag{6.9}
\]

Thus the full canonical Gibbs chain has a fixed-threshold mixing obstruction
of order (N/h_N): in particular, tolerance (1/8) gives
\(\Omega_C(\sqrt N)\) on balanced distinct semiprimes and
\(\Omega(\sqrt N)\) on prime squares.

### The time-(t\) law conditioned on zero defect

Let

\[
\nu_N=\operatorname{Unif}(\Omega_N).
\]

Its exact mass on (B_N) is

\[
\beta_N^{(0)}
=1-\frac{1+2\varphi(N)}{M_N}
=
\begin{cases}
\dfrac{2(N-1)}{(2p-1)(2q-1)}>\dfrac12,&N=pq,\ p<q,\\[3mm]
\dfrac{N-1}{3p^2-2p}>\dfrac13,&N=p^2.
\end{cases}
\tag{6.10}
\]

There is also a direct finite-time bound for the actual canonical chain after
conditioning its time-(t) output on (d=0). For any other coordinate (b),
with (g=\gcd(b,N)\), one canonical refresh has

\[
\Pr(d_{\mathrm{new}}=0\mid b)
=\frac{gN}{gN+N-g}\ge\frac{N}{2N-1}.
\tag{6.11}
\]

Therefore \(\Pr(D_t=0)\ge N/(2N-1)\) for every (t\ge1). If

\[
\widehat\mu_t=\mathcal L((K_t,X_t)\mid D_t=0),
\]

then

\[
\boxed{
\|\widehat\mu_t-\nu_N\|_{\mathrm{TV}}
\ge
\left[
\beta_N^{(0)}-
\frac{2N-1}{N}\bigl(1-(1-h_N/N)^t\bigr)
\right]_+ .}
\tag{6.12}
\]

In particular, under (6.8) the error term in (6.12) is less than (1/16).
The conditional total-variation distance is then greater than (7/16) for
distinct semiprimes and greater than (13/48) for prime squares. Thus the
zero-defect output itself has an explicit \(\Omega(\sqrt N)\) finite-time
obstruction at the usual (1/4) threshold on the requested families.

## 7. Edge cases and exact scope

* **(p=2\), distinct product.** For (N=2q) with odd prime (q),
  (h_N=q), (M_N=3(2q-1)), and \(\beta_N^{(0)}=2/3\). The canonical
  hitting lower bound is only (N/h_N=2). This does not contradict the
  balanced result: for fixed balance constant (C), the condition
  (q\le2C) permits only finitely many such (q).
* **(p=2\), square.** For (N=4), (h_N=1), (M_N=8),
  \(\beta_N^{(0)}=3/8\), and \(\beta_{N,1/N}=2/5\). The expected hitting
  lower bounds are (4) canonical refreshes and (3) refreshes for the
  activity-uniform bound. The asymptotic finite-time windows can contain no
  positive integer time for this small (N); the exact formulas remain
  valid.
* **Prime modulus.** If (N) is prime, (h_N=0), there is no proper factor,
  and \(\tau=\infty\). This case is not part of either composite family.
* **(N=1\).** It is excluded. In particular, (h_N/(N-1)) is undefined and
  the usual proper-factor problem is absent.
* **Repeated primes.** The notation (pq) above always means distinct
  primes. The repeated case uses the (p^2) formulas.
* **Zero activity.** The theorem assumes \(\lambda>0\). At \(\lambda=0\),
  support and irreducibility change.
* **Initial state.** Hitting and TV bounds assume that the initial law is
  supported on (C_N^2). If it already places mass on a proper nonunit, the
  gcd screen succeeds at time zero.
* **Meaning of “factor found.”** The result concerns the coordinate gcd
  screens \(\gcd(k,N)\), \(\gcd(x,N)\), and \(\gcd(d,N)\). It is not a lower
  bound against arbitrary factoring computations or additional arithmetic
  tests.

The proof closes only the scalar-activity, one-derived-defect, local
single-free-coordinate Gibbs mechanism. It does not close joint block moves
in ((k,x)), multiple defects with cancellation, moves that amplify
(p)-adic valuations, non-scalar activities that depend on residue strata,
or nontrivial warm starts. Those mechanisms can change the entry density into
factor-bearing strata and remain open.

## Verdict

**RECONSTRUCTION SUCCEEDS.** The requested hazard, exact counts, expected
hitting lower bounds, fair-bit implementation, and finite-time total-variation
bounds all follow from the displayed target and its exact conditionals. The
only semantic mismatch is that “single-coordinate Gibbs on constrained
triples” is degenerate if read literally. The nondegenerate theorem requires
single-coordinate Gibbs on the free pair ((k,x)), with (d=kx) recomputed
as a derived coordinate. Under that explicit convention, there is no
mathematical mismatch.
