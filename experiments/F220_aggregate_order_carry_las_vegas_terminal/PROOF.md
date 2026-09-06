# Proof of the F220 aggregate order/carry terminal

## 1. Primary-level certification

Let (r) be an arbitrary rational prime divisor of (N). The global
identity

\[
a^A\equiv1\pmod N
\]

reduces to the same identity modulo (r). Therefore

\[
o_r:=\operatorname{ord}_r(a)\mid A.
\tag{1}
\]

Fix \(\ell^{e_\ell}\parallel A\) and suppose

\[
g_\ell=\gcd(a^{A/\ell}-1,N)=1.
\]

Then

\[
a^{A/\ell}\not\equiv1\pmod r.
\]

If (v_\ell(o_r)\le e_\ell-1), every prime-power valuation in (o_r)
would be bounded by the corresponding valuation in (A/\ell), so

\[
o_r\mid A/\ell.
\]

This would give the excluded identity. Hence

\[
v_\ell(o_r)=e_\ell.
\]

Since (o_r\mid |\mathbb F_r^\times|=r-1),

\[
\ell^{e_\ell}\mid r-1.
\tag{2}
\]

This argument works directly in the prime field. Equivalently, one may note
that prime-to-(r) torsion reduces injectively from
\((\mathbb Z/r^f\mathbb Z)^\times\) to \(\mathbb F_r^\times\). The direct
argument does not require that reformulation.

If (1<g_\ell<N), the gcd is visibly a proper factor. If it is (N), no
conclusion about the full \(\ell\)-part follows and the construction simply
omits that primary block. Multiplying all certified, pairwise coprime
primary blocks gives (c(A,a)\), which divides every (r-1). An lcm of
several such divisors also divides every (r-1). This proves Theorem A.

Notice what was not used: the local orders of (a) need not agree outside
the certified primary coordinates, and no complete exact order is claimed.

## 2. Generalized CRT and the arithmetic-progression terminal

Let

\[
g=\gcd(2^t,M).
\]

Both supplied congruences are satisfied by the true integer (p), because

\[
p\equiv b\pmod{2^t}
\]

and (M\mid p-1). Thus

\[
b\equiv1\pmod g,
\tag{3}
\]

which is exactly the compatibility condition for generalized CRT.

For an explicit construction, write (x=b+2^tz). Dividing the second
congruence by (g) gives

\[
\frac{2^t}{g}z
\equiv\frac{1-b}{g}
\pmod{M/g}.
\tag{4}
\]

The coefficient (2^t/g) is a unit modulo (M/g), so one extended-Euclid
inversion finds (z\pmod{M/g}). Equation (4) yields one residue modulo

\[
2^t(M/g)=\operatorname{lcm}(2^t,M)=L.
\]

All integers involved have (O(n)) bits. Indeed, (M\mid p-1<N) and
(t\le n), so

\[
L\le 2^tM<2^nN<2^{2n}.
\]

Standard gcd, inversion, and multiplication therefore have polynomial bit
cost.

We next prove that (L) is a unit modulo (N). The dyadic part is coprime
to odd (N). If a rational prime \(\rho\) divided both (M) and (N),
then the universal predecessor property applied to (r=\rho) would give

\[
M\mid \rho-1,
\]

contradicting \(\rho\mid M\). Hence

\[
\gcd(L,N)=1.
\tag{5}
\]

The true factor satisfies

\[
p\equiv s\pmod L.
\tag{6}
\]

It is also coprime to (L), so the canonical residue (s) is nonzero.
Compute (d=\gcd(s,N)). If (p<L), (6) and
\(0<p,s<L\) force (s=p), and (d=p). Consequently, if the gcd is not a
factor, then

\[
L<p<N.
\tag{7}
\]

In this remaining case all exposed hypotheses of the imported
Gao--Feng--Hu--Pan arithmetic-progression terminal hold:

\[
1\le s<L<N,
\qquad
\gcd(L,N)=1,
\qquad
p\equiv s\pmod L.
\]

Its bit-cost bound is

\[
O\!\left(
\left\lceil\frac{N^{1/4}}L\right\rceil
\log^{7+3\epsilon}N
\right)
\tag{8}
\]

for any fixed \(\epsilon>0\). If

\[
L\ge N^{1/4}/S(n)
\]

with numerical-QP (S), (8) is numerical QP. Every candidate factor is
verified by exact division.

Finally, if a new certified block is (c), prime-power valuations of an lcm
give

\[
\begin{aligned}
\frac{\operatorname{lcm}(L,c)}L
&=\prod_\ell
\ell^{\max\{v_\ell(L),v_\ell(c)\}-v_\ell(L)}\\
&=\prod_\ell
\ell^{\max\{v_\ell(c)-v_\ell(L),0\}}.
\end{aligned}
\]

This proves Theorem B, including the overlap warning.

## 3. The Las Vegas potential

By definition,

\[
R_*=2^H\ge N^{1/4}/S(n).
\tag{9}
\]

Thus (Phi(L)=0) implies (L\ge R_*), and Theorem B applies. Before that
point,

\[
1\le\Phi(L)\le H=O(n).
\tag{10}
\]

Every aggregate update satisfies (L\mid L'). If it is strict, the integer
(L'/L) is at least two, and consequently

\[
\lfloor\log_2L'\rfloor
\ge\lfloor\log_2L\rfloor+1.
\tag{11}
\]

Therefore a strict update decreases (Phi) by at least one; a returned
factor decreases it to zero.

Let \(\tau\) be the first terminal stage. The drift hypothesis can be
written

\[
\mathbb E[\Phi_k-\Phi_{k+1}\mid\mathcal F_k]
\ge Q(n)^{-1}\mathbf1_{\{k<\tau\}}.
\tag{12}
\]

Sum (12) through stage \((m\wedge\tau)-1\), take expectations, and telescope:

\[
Q(n)^{-1}\mathbb E[m\wedge\tau]
\le \mathbb E[\Phi_0-\Phi_{m\wedge\tau}]
\le\Phi_0.
\tag{13}
\]

Monotone convergence gives

\[
\mathbb E[\tau]\le\Phi_0Q(n)=O(nQ(n)).
\tag{14}
\]

In particular, \(\tau<\infty\) almost surely. If each stage costs at most a
fixed numerical-QP amount (Q_0(n)), its expected total cost is bounded by

\[
O(nQ(n)Q_0(n)),
\]

which is numerical QP. The final CRT, GFHP invocation, and verification are
also numerical QP.

Let (E_k) be the event that stage (k) returns a factor or has
\(c\nmid L). On a nonterminal history, (E_k) decreases (Phi) by at
least one, so

\[
\Pr(E_k\mid\mathcal F_k)\ge Q(n)^{-1}
\]

implies (12). Conversely, the decrement is zero outside (E_k) and is at
most (H\le O(n)) on (E_k). Thus (12) implies

\[
\Pr(E_k\mid\mathcal F_k)
\ge\frac1{H Q(n)}.
\tag{15}
\]

The two criteria differ only by a polynomial factor and are equivalent at
the numerical-QP scale.

For iid witness pairs ((A,a)) with law \(\mu\), failures do not change
the current (L). Each new trial therefore has the same useful probability

\[
\pi_\mu(L)=\mu(E_k),
\]

until the state grows or a factor appears. The waiting time is geometric.
This proves Theorem C.

## 4. Uniform-root preliminaries

We now prove the exact law in Theorem D. Because (N) is odd, every local
unit group

\[
G_j=(\mathbb Z/R_j\mathbb Z)^\times
\]

is cyclic of order (h_j\). The condition (gcd(A,N)=1) gives

\[
d_j=\gcd(A,h_j)=\gcd(A,r_j-1).
\tag{16}
\]

The (A)-root subgroup in (G_j) is cyclic of order (d_j).

A uniform unit modulo (N) has independent uniform CRT components in the
(G_j). The event (G_0=N) says that every component belongs to its full
local (A)-root subgroup. Therefore

\[
\Pr(G_0=N)=\prod_j\frac{d_j}{h_j}=\Gamma.
\tag{17}
\]

The event (G_0=1) says that no rational prime (r_j) divides
(a^A-1). Reduction from (G_j) onto \(\mathbb F_{r_j}^\times\) is
uniform, and exactly (d_j) of the (r_j-1) field units are (A)-roots.
Independence gives

\[
\Pr(G_0=1)
=\prod_j\left(1-\frac{d_j}{r_j-1}\right)=B.
\tag{18}
\]

Every other gcd lies strictly between (1) and (N), possibly containing
only part of a repeated prime power, and is a proper factor.

Conditioned on (G_0=N), each local component is independent and uniform
in the cyclic root subgroup (C_{d_j}).

## 5. One primary test and the four (f_\ell) cases

Fix \(\ell^{e_\ell}\parallel A\), and abbreviate (e=e_\ell). Since
(d_j\mid A),

\[
v_\ell(d_j)\le e.
\]

Consider the local value

\[
y_j=a_j^{A/\ell}\in G_j.
\tag{19}
\]

There are exactly two local cases.

1. If (v_\ell(d_j)<e), then (d_j\mid A/\ell), so (y_j=1)
   deterministically.
2. If (v_\ell(d_j)=e), exponentiation by (A/\ell) kills every
   prime-primary coordinate except the last quotient of the
   \(\ell\)-primary coordinate. Its image has order \(\ell\). For a
   uniform member of (C_{d_j}),
   \[
   \Pr(y_j=1)=\ell^{-1},
   \qquad
   \Pr(y_j\ne1)=1-\ell^{-1}.
   \tag{20}
   \]

Because (ell\mid A) and (gcd(A,N)=1), one has \(\ell\ne r_j\). A
nonidentity (y_j) in (20) has order \(\ell\), so it remains nonidentity
after reduction modulo (r_j). It follows that the gcd

\[
g_\ell=\gcd(a^{A/\ell}-1,N)
\]

contains the complete component (R_j) when (y_j=1), and none of its
rational-prime support when (y_j\ne1). No partial (r_j)-adic case occurs
inside this conditioned primary test.

The indicators in (20) are independent across (j). They are also
independent for distinct rational primes (ell\mid A), because a uniform
element of a finite cyclic group has independent Sylow coordinates.

Let

\[
c_\ell=\#\{j:v_\ell(d_j)=e\}.
\]

We now derive every line of (D8).

### Case 1: (c_\ell=0)

Every (y_j) is the identity. Hence (g_\ell=N) deterministically. The
test neither factors nor certifies, so its no-progress factor is

\[
f_\ell(L)=1.
\]

### Case 2: (0<c_\ell<\nu)

The \(\nu-c_\ell\) inactive components are identities deterministically.
If any of the (c_\ell) active components is nonidentity, the gcd contains
the inactive components but omits at least one active component, and is a
proper factor. The only no-factor outcome is that every active component is
also the identity. Its probability is

\[
f_\ell(L)=\ell^{-c_\ell}.
\]

The gcd-one certificate is impossible because at least one inactive
component is always present in the gcd.

### Case 3: (c_\ell=\nu) and (e>v_\ell(L))

All components are active. There are three disjoint outcomes:

\[
\begin{array}{c|c|c}
\text{local pattern}&\text{gcd outcome}&\text{probability}\\ \hline
\text{all identities}&N&\ell^{-\nu}\\
\text{all nonidentities}&1&(1-\ell^{-1})^\nu\\
\text{mixed}&\text{proper factor}&
1-\ell^{-\nu}-(1-\ell^{-1})^\nu.
\end{array}
\tag{21}
\]

The all-nonidentity row certifies \(\ell^e\), and (e>v_\ell(L)) means
that it strictly enlarges (L). Thus only the all-identity row is
no-progress:

\[
f_\ell(L)=\ell^{-\nu}.
\]

### Case 4: (c_\ell=\nu) and (e\le v_\ell(L))

The same three rows (21) occur. Now the gcd-one row certifies only a primary
block already contained in (L), so both synchronized rows are no-progress.
The mixed row remains a factor. Therefore

\[
f_\ell(L)
=\ell^{-\nu}+(1-\ell^{-1})^\nu.
\]

This proves all four cases in (D8).

## 6. Multiplying the primary laws

Conditional on (G_0=N), distinct \(\ell\)-tests depend on independent
Sylow coordinates. Hence the probability that every test avoids both a
proper factor and strict (L)-growth is

\[
\prod_{\ell\mid A}f_\ell(L).
\tag{22}
\]

Unconditionally, there are exactly two no-progress routes:

1. (G_0=1), of probability (B), after which no divisor of (A) can
   give an identity gcd; or
2. (G_0=N), of probability \(\Gamma\), followed by (22).

All other paths contain a verified proper gcd or new certified primary
support. Thus

\[
P_{\rm np}(L)
=B+\Gamma\prod_{\ell\mid A}f_\ell(L),
\]

and \(\pi_A(L)=1-P_{\rm np}(L)\). This proves Theorem D.

## 7. The universal attainability ceiling

Every certified (c_i) divides every (r-1), so

\[
c_i\mid D_N:=\gcd_{r\mid N}(r-1).
\]

Taking lcms gives

\[
M\mid D_N.
\tag{23}
\]

Monotonicity of prime-power valuations under lcm then gives

\[
L=\operatorname{lcm}(2^t,M)
\mid\operatorname{lcm}(2^t,D_N).
\tag{24}
\]

If the right side is below (R_*), no sequence of certified-block updates
can reach the modulus threshold. This statement does not exclude a factor
gcd on the way.

For (N=pq),

\[
D_N=\gcd(p-1,q-1),
\]

and every common divisor of (p-1) and (q-1) divides their difference:

\[
D_N\mid q-p.
\tag{25}
\]

This proves the deterministic bounded-gap ceiling.

## 8. The bounded-gap probability obstruction

Specialize to (A=N-1=pq-1), as in P165, and put

\[
d=\gcd(p-1,q-1).
\]

Modulo either hidden prime, the number of (A)-roots is (d): for example,

\[
\gcd(A,p-1)
=\gcd(pq-1,p-1)
=\gcd(q-1,p-1)=d.
\tag{26}
\]

Any factor or primary certificate produced by the processor requires at
least one local component to be an (A)-root. A union bound therefore gives

\[
\Pr(\text{factor or strict aggregate growth})
\le\frac d{p-1}+\frac d{q-1}.
\tag{27}
\]

This upper bound is valid for every current state; declaring some
certificates already contained in (L) only reduces the useful event.

If (q-p\le C), (25) gives (d\le C). Balance gives

\[
p=2^{n/2+O_C(1)},
\]

so (27) is (2^{-n/2+O_C(1)}\). A numerical-QP bank of independent uniform
bases still has total useful probability (2^{-\Omega(n)}\). The standard
bounded-prime-gap theorem gives an absolute (C) for infinitely many prime
pairs, establishing the infinite-family statement. No unproved prime-tuple
conjecture is used.

The same order bound (M\le d\le C) holds for every witness distribution,
including adaptive choices. Only the probability estimate (27) is specific
to uniform bases.

## 9. The cyclic-direction obstruction

Suppose each hidden local group contains an element (g_j) of the same
exact order (c), and every witness has synchronized local tuple

\[
(g_1^z,\ldots,g_\nu^z).
\]

For every component,

\[
\operatorname{ord}(g_j^z)=\frac c{\gcd(c,z)}.
\tag{28}
\]

Thus the complete local orders agree, so exact factor-first stripping does
not split the components. Every returned order, and every primary block
within it, divides (c). Their aggregate can never exceed (c).

Let \(\ell^e\parallel c\), and sample (z) uniformly modulo (c). The
order in (28) contains the full \(\ell^e\)-part exactly when

\[
\ell\nmid z.
\]

The full primary part is absent from the lcm after (k) independent samples
exactly when every sampled exponent is divisible by \(\ell\). This has
probability

\[
\ell^{-k}.
\]

Therefore random sampling can rapidly fill the exponent of its one cyclic
direction, but no number of samples creates support outside that exponent.
If \(\operatorname{lcm}(2^t,c)<R_*\), the aggregate terminal is
unreachable in this model. This proves Theorem E.

## 10. Complexity and exact logical boundary

The primary certificates use modular exponentiation with exponents whose
binary encodings and certified factorizations are charged to the stage.
When those encodings, the number of tested prime divisors, witness
generation, and retained state are numerical QP, every stage is numerical
QP. The aggregate (M\) remains below every hidden rational prime and has
(O(n)) bits. Generalized CRT and all gcd verification are polynomial in
these bit lengths.

Theorem C is conditional on a progress law; it does not prove one. Theorem D
gives an exact law for full CRT-uniform units, not for numerically small
integer witnesses. Independence between successive draws from a small
integer distribution does not make the hidden CRT components uniform.

P160's exact-common-order exit supplies one admissible block after its
coprime-order normalization, but its hard-branch theorem allows unequal local
orders and does not supply the factored global annihilator required by
Theorem A. P165 supplies
the uniform-root model but, by Section 8, refutes a uniform all-input
inverse-QP progress lower bound. These are scope statements, not further
premises in the proofs above.

The dyadic residue is supplied rather than evaluated. The result applies to
the balanced semiprime terminal after that residue is available. It does not
handle primes, arbitrary composites, prime powers, unbalanced factors, or
the recursion needed for complete factorization. It is therefore a
conditional terminal and source boundary, not a solution of the task in
`PROMPT.md`.
