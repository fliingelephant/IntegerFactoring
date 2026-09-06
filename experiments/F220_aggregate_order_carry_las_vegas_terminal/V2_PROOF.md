# Proof of the F220 V2 aggregate order/carry terminal

## 1. Primary-level certification

Let \(r\) be any rational prime divisor of \(N\). Reducing (A1) modulo
\(r\) gives

\[
o_r:=\operatorname{ord}_r(a)\mid A.
\tag{1}
\]

Fix \(\ell^{e_\ell}\parallel A\), and suppose \(g_\ell=1\). Then

\[
a^{A/\ell}\not\equiv1\pmod r.
\tag{2}
\]

If \(v_\ell(o_r)\le e_\ell-1\), every primary valuation of \(o_r\) is
bounded by the corresponding valuation of \(A/\ell\), so
\(o_r\mid A/\ell\). This contradicts (2). Therefore

\[
v_\ell(o_r)=e_\ell.
\tag{3}
\]

Lagrange's theorem in \(\mathbb F_r^\times\) now gives

\[
\ell^{e_\ell}\mid o_r\mid r-1.
\tag{4}
\]

This direct residue-field argument uses neither \(\gcd(A,N)=1\) nor
equality of complete local orders. If \(1<g_\ell<N\), exact division
verifies a proper factor. If \(g_\ell=N\), no primary contribution is
claimed. Products of the pairwise coprime certified primary powers give
\(c(A,a)\), and lcms of several such blocks remain divisors of every
\(r-1\). This proves Theorem A.

## 2. Generalized CRT and the exact GFHP target

Put

\[
g=\gcd(2^t,M).
\]

The true factor \(p\) satisfies both congruences in (B4), because
\(M\mid p-1\). Hence

\[
b\equiv1\pmod g,
\tag{5}
\]

which is the generalized-CRT compatibility condition. Writing
\(x=b+2^tz\), the second congruence becomes

\[
\frac{2^t}{g}z
\equiv\frac{1-b}{g}
\pmod{M/g}.
\tag{6}
\]

The coefficient \(2^t/g\) is invertible modulo \(M/g\). Extended Euclid
therefore computes \(z\pmod{M/g}\), and the solution modulus is

\[
2^t(M/g)=\operatorname{lcm}(2^t,M)=L.
\tag{7}
\]

All operands have \(O(n)\) bits. Indeed, \(M\mid p-1<N\) and \(t\le n\),
so

\[
L\le2^tM<2^nN<2^{2n}.
\tag{8}
\]

Thus the CRT work has polynomial bit complexity.

We next show \(\gcd(L,N)=1\). The dyadic part is coprime to odd \(N\).
If a rational prime \(\rho\) divided both \(M\) and \(N\), universality
applied to \(r=\rho\) would give \(M\mid\rho-1\), contradicting
\(\rho\mid M\). Hence

\[
\gcd(L,N)=1.
\tag{9}
\]

The canonical remainder \(s=p\bmod L\) is nonzero because \(p\) is a unit
modulo \(L\). It also satisfies \(0<s\le p<N\). Therefore
\(\gcd(s,N)\) is either \(1\) or the factor \(p\). If \(p<L\), the
canonical remainder is \(s=p\), and the gcd returns \(p\). Equality
\(L=p\) is excluded by (9). Thus the branch on which the gcd is one has

\[
1\le s<L<p<N,
\qquad
\gcd(L,N)=1,
\qquad
p\equiv s\pmod L.
\tag{10}
\]

These are the imported GFHP interface hypotheses. Its bit-cost bound is

\[
O\!\left(
\left\lceil\frac{N^{1/4}}L\right\rceil
\log^{7+3\epsilon}N
\right)
\tag{11}
\]

for fixed \(\epsilon>0\). If \(L\ge T_{\rm G}=N^{1/4}/S(n)\), this is
numerical QP. Since \(L\) is integral,

\[
L\ge T_{\rm G}
\quad\Longleftrightarrow\quad
L\ge\lceil T_{\rm G}\rceil=J_{\rm G}.
\tag{12}
\]

This is the actual discrete terminal threshold.

Finally, prime-power valuations of an lcm give

\[
\begin{aligned}
\frac{\operatorname{lcm}(L,c)}L
&=\prod_\ell
\ell^{\max\{v_\ell(L),v_\ell(c)\}-v_\ell(L)}\\
&=\prod_\ell
\ell^{\max\{v_\ell(c)-v_\ell(L),0\}}.
\end{aligned}
\tag{13}
\]

This proves Theorem B.

## 3. Exact-target potential and stopped drift

The dyadic envelope in (C1) obeys

\[
J_{\rm G}\le R_*<2J_{\rm G},
\tag{14}
\]

but V2 does not use \(R_*\) as its stopping target. For an unfactored
state, (C3) gives

\[
\Phi(L)=0
\quad\Longleftrightarrow\quad
L\ge J_{\rm G}.
\tag{15}
\]

Suppose the state is nonterminal and \(L'=\operatorname{lcm}(L,c)>L\).
Because \(L\mid L'\),

\[
L'\ge2L.
\tag{16}
\]

If \(L'<J_{\rm G}\), then

\[
\begin{aligned}
\Phi(L')
&=\left\lceil\log_2\frac{J_{\rm G}}{L'}\right\rceil\\
&\le
\left\lceil\log_2\frac{J_{\rm G}}L-1\right\rceil
=\Phi(L)-1.
\end{aligned}
\tag{17}
\]

If \(L'\ge J_{\rm G}\), the new potential is zero, while the old one was
at least one. A returned factor also sets it to zero. Hence every useful
event lowers \(\Phi\) by at least one.

For every nonterminal state,

\[
1\le\Phi(L)
\le\lceil\log_2J_{\rm G}\rceil=O(n).
\tag{18}
\]

The case \(J_{\rm G}=1\) has no nonterminal state and is vacuous.

Let \(\tau\) be the first factor or threshold stage. The drift hypothesis
is

\[
\mathbb E[\Phi_k-\Phi_{k+1}\mid\mathcal F_k]
\ge Q(n)^{-1}\mathbf1_{\{k<\tau\}}.
\tag{19}
\]

Summing through \((m\wedge\tau)-1\), taking expectations, and telescoping
gives

\[
Q(n)^{-1}\mathbb E[m\wedge\tau]
\le\mathbb E[\Phi_0-\Phi_{m\wedge\tau}]
\le\Phi_0.
\tag{20}
\]

Monotone convergence yields

\[
\mathbb E\tau\le\Phi_0Q(n)=O(nQ(n)).
\tag{21}
\]

Thus \(\tau\) is finite almost surely. Multiplying (21) by a uniform
numerical-QP per-stage cost preserves numerical QP. The final CRT, GFHP
call, and exact-division verification also have numerical-QP cost.

Let \(E_k\) be the event that stage \(k\) returns a factor or has
\(c\nmid L\). On a nonterminal history, \(E_k\) lowers the potential by
at least one. Outside \(E_k\), it does not change. The decrement on
\(E_k\) is at most the \(O(n)\) bound in (18). Therefore

\[
\Pr(E_k\mid\mathcal F_k)\ge Q(n)^{-1}
\quad\Longrightarrow\quad
\mathbb E[\Delta\Phi_k\mid\mathcal F_k]\ge Q(n)^{-1},
\tag{22}
\]

and conversely a drift lower bound \(Q(n)^{-1}\) implies useful-event mass
at least \(1/(O(n)Q(n))\). No independence is used.

For iid witnesses, a no-progress outcome leaves \(L\) unchanged. Fresh
trials therefore retain probability \(\pi_\mu(L)\) until the next useful
event, giving the stated geometric waiting time. This proves Theorem C.

## 4. CRT-uniform root probabilities

For odd \(r_j\), the local unit group

\[
G_j=(\mathbb Z/R_j\mathbb Z)^\times
\]

is cyclic of order \(h_j\). Since \(\gcd(A,N)=1\), the \(r_j\)-primary
part of \(h_j=r_j^{f_j-1}(r_j-1)\) contributes nothing to
\(\gcd(A,h_j)\), so

\[
d_j=\gcd(A,h_j)=\gcd(A,r_j-1).
\tag{23}
\]

The local \(A\)-root subgroup has order \(d_j\). A uniform unit modulo
\(N\) has independent uniform CRT components. Full return modulo every
\(R_j\) therefore has probability

\[
\Pr(G_0=N)=\prod_j\frac{d_j}{h_j}=\Gamma.
\tag{24}
\]

The event \(G_0=1\) says that no \(r_j\) divides \(a^A-1\). Reduction to
\(\mathbb F_{r_j}^\times\) is uniform, and exactly \(d_j\) of its
\(r_j-1\) elements are \(A\)-roots. Hence

\[
\Pr(G_0=1)
=\prod_j\left(1-\frac{d_j}{r_j-1}\right)=B.
\tag{25}
\]

Every other gcd is strictly between \(1\) and \(N\), including any partial
power of a repeated rational prime. Conditioned on \(G_0=N\), the local
components are independent uniform elements of the cyclic root subgroups
\(C_{d_j}\).

## 5. One primary test and all four cases

Fix \(\ell^{e_\ell}\parallel A\), abbreviate \(e=e_\ell\), and set

\[
y_j=a_j^{A/\ell}.
\tag{26}
\]

Because \(d_j\mid A\), there are two local cases.

1. If \(v_\ell(d_j)<e\), then \(d_j\mid A/\ell\), so \(y_j=1\)
   deterministically.
2. If \(v_\ell(d_j)=e\), exponentiation by \(A/\ell\) maps the uniform
   root-group element onto a group of order \(\ell\). Therefore
   \[
   \Pr(y_j=1)=\ell^{-1},
   \qquad
   \Pr(y_j\ne1)=1-\ell^{-1}.
   \tag{27}
   \]

The hypothesis \(\gcd(A,N)=1\) gives \(\ell\ne r_j\). A nonidentity
\(y_j\) in (27) has order \(\ell\), so reduction modulo \(r_j\) remains
nonidentity. Thus the primary gcd contains all of \(R_j\) when \(y_j=1\)
and none of its rational-prime support when \(y_j\ne1\). No partial local
power occurs in this conditioned test.

The indicators are independent across \(j\). For distinct \(\ell\), they
are independent because a uniform cyclic-group element has independent
Sylow coordinates. Put

\[
c_\ell=\#\{j:v_\ell(d_j)=e\}.
\]

We derive every line of (D8).

### Case 1: \(c_\ell=0\)

Every coordinate is inactive and hence every \(y_j=1\). The gcd is \(N\)
with probability one. The no-progress factor is

\[
f_\ell(L)=1.
\tag{28}
\]

### Case 2: \(0<c_\ell<\nu\)

The inactive coordinates guarantee nonempty gcd support. If any active
coordinate is nonidentity, the gcd is proper. The only no-factor outcome is
that all \(c_\ell\) active coordinates are identities, which gives gcd
\(N\). Therefore

\[
f_\ell(L)=\ell^{-c_\ell}.
\tag{29}
\]

The gcd-one certificate is impossible in this case.

### Case 3: \(c_\ell=\nu\) and \(e>v_\ell(L)\)

All coordinates are active. The three disjoint patterns are

\[
\begin{array}{c|c|c}
\text{pattern}&\text{gcd}&\text{probability}\\ \hline
\text{all identities}&N&\ell^{-\nu}\\
\text{all nonidentities}&1&(1-\ell^{-1})^\nu\\
\text{mixed}&\text{proper factor}&
1-\ell^{-\nu}-(1-\ell^{-1})^\nu.
\end{array}
\tag{30}
\]

The gcd-one row certifies \(\ell^e\), which strictly enlarges \(L\).
Only the all-identity row is no progress:

\[
f_\ell(L)=\ell^{-\nu}.
\tag{31}
\]

### Case 4: \(c_\ell=\nu\) and \(e\le v_\ell(L)\)

The same three patterns occur, but the gcd-one certificate is already
contained in \(L\). Both synchronized endpoints are now no progress, so

\[
f_\ell(L)=\ell^{-\nu}+(1-\ell^{-1})^\nu.
\tag{32}
\]

This proves all four cases.

## 6. Multiplying the primary laws

Conditional on \(G_0=N\), distinct primary tests use independent Sylow
coordinates. Their joint no-progress probability is

\[
\prod_{\ell\mid A}f_\ell(L).
\tag{33}
\]

There are exactly two unconditional no-progress routes:

1. \(G_0=1\), with probability \(B\); or
2. \(G_0=N\), with probability \(\Gamma\), followed by (33).

Every other route gives a verified proper gcd or a certified primary power
not yet contained in \(L\). Consequently

\[
P_{\rm np}(L)
=B+\Gamma\prod_{\ell\mid A}f_\ell(L),
\qquad
\pi_A(L)=1-P_{\rm np}(L).
\tag{34}
\]

This proves Theorem D.

## 7. Universal ceiling and the corrected threshold comparison

Each certified block divides every \(r-1\), so

\[
c_i\mid D_N:=\gcd_{r\mid N}(r-1).
\]

Taking lcms gives

\[
M\mid D_N,
\qquad
L=\operatorname{lcm}(2^t,M)mid
C_N(t)=\operatorname{lcm}(2^t,D_N).
\tag{35}
\]

If \(C_N(t)<J_{\rm G}\), every attainable aggregate modulus is below the
actual integer GFHP threshold. This proves (E3). A factor gcd is still
possible.

The distinction from V1 is exact. The relation

\[
J_{\rm G}\le C_N(t)<R_*
\tag{36}
\]

is compatible with GFHP termination because the left inequality already
meets the actual threshold. It says only that the optional dyadic envelope
cannot be reached. V2 makes no stronger inference from (36).

For \(N=pq\),

\[
D_N=\gcd(p-1,q-1)\mid q-p,
\tag{37}
\]

which proves the deterministic bounded-gap ceiling.

## 8. Bounded-gap probability obstruction

Take \(A=N-1=pq-1\), as in P165, and write

\[
d=\gcd(p-1,q-1)=D_N.
\]

Modulo either hidden prime, the number of \(A\)-roots is \(d\); for
example,

\[
\gcd(A,p-1)
=\gcd(pq-1,p-1)
=\gcd(q-1,p-1)=d.
\tag{38}
\]

Any initial factor or later primary certificate requires at least one local
component to be an \(A\)-root. A union bound gives, at every current state,

\[
\Pr(\text{factor or strict }L\text{-growth})
\le\frac d{p-1}+\frac d{q-1}.
\tag{39}
\]

Marking already accumulated primary blocks as no progress only decreases the
left side. If \(q-p\le C\), then \(d\le C\) and \(M\le C\). Balance gives

\[
p=2^{n/2+O_C(1)},
\]

so (39) is \(2^{-n/2+O_C(1)}\). A numerical-QP number of independent
uniform samples still has total useful probability \(2^{-\Omega(n)}\).
The standard bounded-prime-gap theorem supplies infinitely many such pairs;
for all sufficiently large pairs, \(q<2p\). This proves the bounded-gap part
of Theorem E.

The deterministic bound \(M\le d\) is source-independent. Only the
probability estimate is specific to CRT-uniform bases.

## 9. Corrected cyclic-direction obstruction

Assume (E7)--(E8). For each \(j\), reduction

\[
(\mathbb Z/R_j\mathbb Z)^\times
\longrightarrow\mathbb F_{r_j}^\times
\tag{40}
\]

has an \(r_j\)-group kernel. Because \(\gcd(c,N)=1\), the cyclic subgroup
\(\langle g_j\rangle\) has order prime to \(r_j\), so it intersects that
kernel trivially. Reduction is therefore injective on
\(\langle g_j\rangle\).

For a synchronized exponent \(z\), every local order is

\[
\operatorname{ord}_{R_j}(g_j^z)
=\frac c{\gcd(c,z)}=m_z.
\tag{41}
\]

More strongly, for every stripping exponent \(u\),

\[
g_j^{zu}=1\pmod{R_j}
\quad\Longleftrightarrow\quad
c\mid zu,
\tag{42}
\]

and the right side is independent of \(j\). If (42) holds, the gcd contains
every full component \(R_j\) and equals \(N\). If it fails, injectivity in
(40) makes \(g_j^{zu}\) nonidentity even modulo \(r_j\) for every \(j\),
so the gcd is \(1\). Thus no factor-first gcd can be a proper divisor,
including a partial power of a repeated rational prime.

Every returned exact common order is \(m_z\mid c\), and every certified
primary block obtained by stripping it also divides \(c\). Their lcm never
exceeds \(c\).

Let \(\ell^e\parallel c\), and sample \(z\) uniformly modulo \(c\). The
order in (41) contains the full \(\ell^e\)-part exactly when
\(\ell\nmid z\). After \(k\) independent samples, that full primary part
is absent from the lcm exactly when all \(k\) exponents are divisible by
\(\ell\). Hence

\[
\Pr(\text{full }\ell^e\text{ still absent})=\ell^{-k}.
\tag{43}
\]

Every modulus reachable through this source divides

\[
C_c(t)=\operatorname{lcm}(2^t,c).
\tag{44}
\]

If \(C_c(t)<J_{\rm G}\), it cannot meet the actual GFHP threshold. If only
\(C_c(t)<R_*\), no such conclusion follows unless it is also below
\(J_{\rm G}\). This proves the corrected cyclic part of Theorem E.

## 10. Regression checks and exact logical boundary

The hostile threshold certificate had an attainable ceiling strictly below
the old \(R_*\) but already above \(T_{\rm G}\). It therefore satisfies
\(J_{\rm G}\le C_N(t)<R_*\), the explicitly non-obstructive interval (E4),
and does not contradict V2.

The hostile repeated-prime-power certificate used \(N=63\) and \(c=3\).
It violates the new premise \(\gcd(c,N)=1\), so it is outside the corrected
cyclic theorem. Equation (40) identifies precisely the injection that failed
in that example.

The primary certificates use modular exponentiation with supplied factored
exponents. Their encodings, number of tested prime divisors, witness
generation, and retained state are charged to each stage. Under the stated
numerical-QP per-stage premise, all gcd, lcm, CRT, and verification work is
within the claimed cost.

Theorem C remains conditional on a source law. Theorem D is exact for
CRT-uniform units satisfying \(\gcd(A,N)=1\), not for independent small
integers. P160's exact-common-order exit can supply a block, but its
hard-branch theorem supplies no factored common annihilator. P165 supplies
the uniform-root model but fails the all-input inverse-QP drift condition on
the bounded-gap family.

The dyadic residue is supplied rather than evaluated. The aggregate terminal
is stated for balanced semiprimes. It does not handle primes, arbitrary
composites, unbalanced factors, carry evaluation, or complete recursion.
F220 V2 is therefore a conditional terminal and source boundary, not a
solution of `PROMPT.md`.
