# F227 V5 blind reconstruction

## Authentication and scope

Before reading the statement, I computed

```text
SHA-256(V5_STATEMENT.md) = b4f1ad6826f867105cd4cafaaeaa02ea6914a92ff1986be1698f10a136a457c1
```

This is exactly the required digest. I then read only the project `PROMPT.md`
and the authenticated `V5_STATEMENT.md`. I did not read a proof, audit,
provenance file, manifest, earlier version, durable ledger, or prior message.
The hash was the only computation.

## Verdict

**PASS on the mathematical claims (A3)--(D2), with the declared-screen scope
stated below.** The repaired claim (B6) is the proved upper bound, not an
equality. The argument is uniform over adaptive no-progress histories and does
not use independence between a trial's success and its cost.

This is only a conditional, oracle-relative result for the balanced
semiprime factor cell. It is not a solution of the project prompt. In
particular, it neither constructs the required fixed bases nor implements or
bounds `FactorAll`.

There is one standalone-specification caveat. The words “direct gcds,”
“factor-first stripping,” and “common primary block” are not formally defined
in the frozen statement. The proof below reconstructs the narrow protocol
forced by the formulas: candidate-associated direct gcds, the displayed return
gcd, and gcds obtained by stripping prime factors from the candidate exponent.
If “direct gcds” instead permitted arbitrary additional gcd queries or an
arbitrary factoring computation during preprocessing, (B1) would not be a
universal upper bound. Thus the PASS is for the declared candidate-exponent
screens, not for unrestricted preprocessing. Historical assertions about
V1--V4, and the global word “exact” in “Exact remaining gaps,” cannot be
independently checked under the required blind source restriction.

## 1. Setup checks

From (p<q<2p),

\[
p^2<N<2p^2,
\qquad
\sqrt{N/2}<p<\sqrt N.
\]

Hence the integer (p) lies in (I_N). Since (p\equiv s\pmod L), it
also lies in \(\mathcal C\), so (H\geq 1). The elements of \(\mathcal C\)
form (H) consecutive terms of an arithmetic progression of difference
(L), and their exponents (A_x=x-1) do too.

For later use, every (x\in\mathcal C) satisfies

\[
\gcd(x-1,N)=1.
\tag{1.1}
\]

Indeed, (0<x-1<q), so a common prime factor could only be (p), and then
(x=p+1). But (x\equiv p\pmod L) would give (L\mid1), contrary to the
even integer (L\geq2). Also, among the elements of (I_N), the only one
having a nontrivial gcd with (N=pq) is (p): every element is below (q),
and the interval's upper endpoint is below (2p).

## 2. Theorem A

Use the elementary divisor identity

\[
\gcd(t,m)=\sum_{d\mid m,\ d\mid t}\varphi(d).
\tag{2.1}
\]

For a fixed (d\mid m), the congruence

\[
c+jL\equiv0\pmod d
\]

has either no solutions or one residue class modulo
(d/\gcd(d,L)). Among (H) consecutive values of (j), it therefore has
at most

\[
\frac{H\gcd(d,L)}d+1
\]

solutions. Summing (2.1) over the progression gives

\[
\begin{aligned}
\sum_j\gcd(A_j,m)
&\leq
H\sum_{d\mid m}\varphi(d)\frac{\gcd(d,L)}d
  +\sum_{d\mid m}\varphi(d)\\
&\leq HL\tau(m)+m.
\end{aligned}
\tag{2.2}
\]

The last line uses \(\gcd(d,L)\leq L\), \(\varphi(d)/d\leq1\), and
\(\sum_{d\mid m}\varphi(d)=m\). Since every atom of \(\mu\) is at most
\(\eta\) and all summands are nonnegative,

\[
\mathbb E_\mu\frac{\gcd(A_j,m)}m
\leq \frac\eta m\sum_j\gcd(A_j,m)
\leq\eta\left(\frac{HL\tau(m)}m+1\right).
\]

This proves (A3). Substitution of \(\eta=1/H\) proves (A4).

## 3. Theorem B

### 3.1 One-trial bound

Fix a candidate exponent (A=A_x). A uniform unit modulo (N) corresponds
under the Chinese remainder theorem to uniform elements modulo (p) and
(q). In the cyclic group \(\mathbb F_r^\times\), the equation
(z^A=1) has exactly \(\gcd(A,r-1)\) solutions. Consequently,

\[
\Pr(a^A=1\bmod r\mid x)=\frac{\gcd(A,r-1)}{r-1}
\qquad(r=p,q).
\tag{3.1}
\]

For the declared screens, a useful trial is contained in the union of these
three events:

1. the direct candidate gcd hits (x=p);
2. (a^A=1\pmod p);
3. (a^A=1\pmod q).

Equation (1.1) rules out a factor obtained merely from (A) or one of its
prime factors. A proper return gcd requires exactly one of events 2 and 3.
Stripping after a full return, or certifying a common primary block, requires
both, so it is also in their union. Thus a union bound and
\(\mu(p)\leq\eta\) give

\[
\Pr(\mathrm{useful})
\leq\eta+
\mathbb E_\mu\frac{\gcd(A_x,p-1)}{p-1}+
\mathbb E_\mu\frac{\gcd(A_x,q-1)}{q-1}.
\tag{3.2}
\]

Apply (A3) twice to the progression (A_x=x-1). This proves

\[
\Pr(\mathrm{useful})\leq
\eta\left[3+HL\left(
\frac{\tau(p-1)}{p-1}+\frac{\tau(q-1)}{q-1}
\right)\right],
\]

which is (B1). Taking \(\eta=1/H\) gives (B2).

### 3.2 Rejection sampling

Among the (N-1) nonzero residues modulo (N), there are (q-1) nonzero
multiples of (p) and (p-1) nonzero multiples of (q), with no overlap.
Therefore a uniform nonzero-residue draw exposes a proper factor with
probability

\[
\frac{p+q-2}{N-1}.
\]

Since (q<2p) and (N=pq), this is (O(1/p)). This proves (B3). Conditional
on acceptance, the residue is exactly a uniform unit, so (B1) still applies
to the accepted base.

### 3.3 Exponential sparsity

Let

\[
W=|I_N|.
\]

With \(\delta=1-2^{-1/2}>0\), endpoint rounding gives

\[
W\geq\delta\sqrt N-1.
\tag{3.3}
\]

Every residue class modulo (L) occurs at least \(\lfloor W/L\rfloor\)
times in an interval of (W) consecutive integers. For all sufficiently
large (N), (B4) and (S(n)\geq1) therefore imply

\[
H\geq c_1 S(n)N^{1/4}
\tag{3.4}
\]

for an absolute (c_1>0).

We also need only the following elementary fixed-power divisor bound: for
every fixed \(\epsilon>0\), there is a constant (K_\epsilon) such that

\[
\tau(m)\leq K_\epsilon m^\epsilon
\qquad(m\geq1).
\tag{3.5}
\]

To prove it, write (m=\prod r^e). For every prime with
(r^\epsilon\geq2), one has (e+1\leq2^e\leq r^{\epsilon e}). There are
only finitely many remaining primes, and for each of them
((e+1)/r^{\epsilon e}) has a finite maximum over (e\geq0). The product
of these finitely many maxima is (K_\epsilon).

Now use \(\eta H\leq Q(n)\), (L<N^{1/4}/S(n)\), and (3.4). The atom term
in (B1) satisfies

\[
3\eta\leq \frac{3Q(n)}H
\leq C_1Q(n)N^{-1/4}.
\tag{3.6}
\]

Take \(\epsilon=1/8\) in (3.5). Since
(p>\sqrt{N/2}), (q>p), and hence (p-1,q-1\gg\sqrt N), the remaining
term in (B1) is at most

\[
\begin{aligned}
\eta HL\left(
\frac{\tau(p-1)}{p-1}+\frac{\tau(q-1)}{q-1}
\right)
&\leq Q(n)L\left(
K(p-1)^{-7/8}+K(q-1)^{-7/8}
\right)\\
&\leq C_2Q(n)N^{-3/16}.
\end{aligned}
\tag{3.7}
\]

The rejection mass in (B3) is (O(N^{-1/2})) and can be absorbed too.
Finally,

\[
\log_2 Q(n)=O((\log(n+1))^{k_*})=o(n),
\]

while the definition of (n) gives (N\geq2^{n-2}) for all relevant
(n). Equations (3.6)--(3.7) are therefore at most (2^{-c_0n}), after
decreasing a fixed (c_0>0) and increasing a fixed (n_0). These constants
depend only on the fixed envelope. They do not depend on the input, state,
history, candidate law, or (S). This proves (B5), including its conditional
history quantifier.

### 3.4 Adaptive bank

For trial (i), condition on every reachable history in which no earlier
trial made progress. The definition of a (Q)-diffuse bank supplies exactly
the hypotheses of (B5), so its conditional useful probability is at most
(2^{-c_0n}). Summing the disjoint events “trial (i) is the first useful
trial,” or simply applying the conditional union bound, gives

\[
\Pr(\text{at least one useful trial})
\leq Q(n)2^{-c_0n}.
\]

Because \(\log_2Q(n)=o(n)\), the right side is (2^{-\Omega(n)}). This
proves the inequality in (B6). It does not prove an equality, and it does
not apply after any of the exclusions listed after (B6) is removed.

## 4. Theorem C

### 4.1 The stripping dichotomy

Let (r=o_p) and (t=o_q). Suppose first that both divide a completely
factored exponent (A). For each prime \(\ell\mid A\), test

\[
D_h=\gcd(a^{A/\ell^h}-1,N),\qquad 1\leq h\leq v_\ell(A),
\]

until the first (D_h\neq N). Immediately before this test, both local
orders divide the exponent. At the first change there are only two
possibilities:

- exactly one local order still divides the exponent, and (D_h) is a
  proper factor;
- neither does, and the two orders have the same exact \(\ell\)-adic
  valuation. The last full return and this first empty return certify their
  common primary block.

If (r\neq t), some prime has unequal valuations, and stripping at that
prime produces a proper factor. If (r=t=d), stripping certifies all primary
blocks of (d). It strictly enlarges (L) exactly when (d\nmid L). If only
(r\mid A), the initial return gcd is already the factor (p). Thus, once
an exponent returns modulo (p), failure of the modular/stripping channel to
factor or enlarge (L) occurs exactly when

\[
o_p=o_q\quad\text{and}\quad o_p\mid L.
\]

This proves (C2) under the declared-channel meaning of “stale.” The qualifier
is essential: the exceptional direct candidate (x=p) can still reveal a
factor independently of the base.

### 4.2 Counting returning exponents

Every (x\in\mathcal C) has a unique representation

\[
x=p+kL
\]

where the allowed (k)'s form an interval of (H) consecutive integers.
Since (o_p\mid p-1),

\[
o_p\mid x-1
\iff o_p\mid kL
\iff \frac{o_p}{\gcd(o_p,L)}\mid k
\iff u_p\mid k.
\tag{4.1}
\]

Any (H) consecutive integers contain at least \(\lfloor H/u_p\rfloor\)
multiples of (u_p). When the base is nonstale, every associated exponent
is useful by the stripping dichotomy. Hence

\[
\Pr(\mathrm{useful})\geq
\frac{\lfloor H/u_p\rfloor}{H}
\geq\frac1{u_p}-\frac1H,
\]

which proves (C3). If (u_p\leq Q(n)) and (H\geq2Q(n)), this is at least
(1/(2Q(n))). If (H<2Q(n)), enumerating all (x\in\mathcal C) and testing
(\gcd(x,N)) reaches (x=p) in fewer than (2Q(n)) gcds.

### 4.3 Potential and number of states

Put (J=J_N). Since (L) is integral,

\[
L<N^{1/4}/S(n)\iff L<J.
\tag{4.2}
\]

A strict lcm update is an integral strict multiple, so (L'\geq2L). While
(L<J), this decreases

\[
\Phi_N(L)=\left\lceil\log_2(J/L)\right\rceil
\]

by at least one. It is nonnegative and is zero at and beyond the threshold.
Thus there are at most \(\Phi_N(L_0)=R_N(L_0)\) same-size progress states.
Also

\[
R_N(L_0)\leq\lceil\log_2J_N\rceil=O(\log N)=O(n),
\]

which proves (C6).

### 4.4 Expected current-node cost

Every child input is (A_x=x-1<\sqrt N), so its bit length is at most
(n/2+C_0) for one absolute rounding constant (C_0).

At a state with (H\geq2Q(n)), let \(\rho=1/(2Q(n))\). Conditional on every
history that reaches a new trial, its useful probability is at least
\(\rho\). Therefore the probability of reaching trial (i) is at most
((1-\rho)^{i-1}). By the uniform conditional-history hypothesis on
`FactorAll`, the conditional expected cost of a reached trial is at most

\[
B=F_{\rm all}(n/2+C_0)+P_{\rm tr}(n).
\]

Consequently,

\[
\mathbb E[\text{all trial costs at the state}]
\leq\sum_{i\geq1}(1-\rho)^{i-1}B
=\frac B\rho
=2Q(n)B.
\tag{4.3}
\]

This reach-tail calculation uses conditional expected costs, not
cost/success independence. It also proves almost-sure progress. When
(H<2Q(n)), direct enumeration costs less than (2Q(n)P_{\rm tr}(n)), so
the same displayed upper bound still applies. Adding the one-time state cost
proves (C8).

There are deterministically at most (R_N(L_0)) such states. Applying the
conditional bound (C8) at each reached state, summing, and adding (G(n))
gives exactly

\[
\begin{aligned}
\mathbb E[\operatorname{NodeCost}]
\leq R_N(L_0)\bigl[&2Q(n)F_{\rm all}(n/2+C_0)\\
&+2Q(n)P_{\rm tr}(n)+P_{\rm st}(n)\bigr]+G(n),
\end{aligned}
\]

which is (C9). This is an oracle-relative call-and-overhead bound. Nothing
in the derivation bounds (F_{\rm all}), and substituting the same
balanced-semiprime routine for `FactorAll` would be invalid because the
children (A_x) are arbitrary even integers.

## 5. Corollary D

The integer (u_p=o_p/\gcd(o_p,L)) divides (o_p). If (u_p>1), it has a
prime divisor, and every such prime is a prime divisor of (o_p). Under the
roughness hypothesis it is therefore greater than (T(n)), so

\[
u_p=1\quad\text{or}\quad u_p>T(n).
\]

This proves (D1). Since (T(n)>Q(n)), the conjunction (u_p\leq Q(n))
forces (u_p=1), which is equivalent to (o_p\mid L). For
(x=p+kL\in\mathcal C), both (o_p\mid p-1) and (o_p\mid L), hence
(o_p\mid x-1). Every cell exponent therefore returns modulo (p).
The stripping dichotomy then factors or enlarges (L) for a nonstale base.
This proves (D2) and its stated consequence.

## 6. Final scope audit

- All asymptotic constants in (B5) are uniform because the sole growing
  envelope has logarithm (o(n)). The proof does not hide dependence on
  (N,p,q,L,S), a candidate law, or an adaptive history.
- (B5) is restricted to the nonterminal range (B4). (B6) additionally needs
  at most (Q(n)) trials, the conditional atom bound at every reachable
  no-progress history, a fresh conditionally uniform unit, and no progress
  exit outside the declared screens.
- (C9) assumes, rather than produces, a nonstale base with
  (u_p\leq Q(n)) at every same-size state. Verifying or recognizably
  obtaining such a base is part of the source gap.
- (C9) also assumes an all-input Las Vegas factorer with a uniform
  conditional expected-cost bound. It is not a recurrence and supplies no
  quasipolynomial bound for that oracle.
- The balanced-semiprime promise, the certified factor-cell state, and the
  P161 rough-descendant hypothesis are assumptions. None can be silently
  promoted to the arbitrary-input theorem required by `PROMPT.md`.

Subject to the declared-screen interpretation identified at the start, I
found no false inequality, reversed quantifier, missing adaptive conditioning,
or hidden cost/success-independence assumption in the frozen V5 mathematical
claims.
