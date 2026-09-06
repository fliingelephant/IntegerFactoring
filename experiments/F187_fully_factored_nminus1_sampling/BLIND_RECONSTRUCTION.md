# Blind reconstruction of F187

## Isolation and verdict

I read only **STATEMENT.md**. Its SHA-256 digest was
**9434188bf8c35cbd54d0f6f553b7e0698f19470745515bb1fe503fbe8b67f14e**.
I used no computation in this reconstruction.

**Verdict: pass.** All numbered claims follow. The arbitrary-prime-power
case is valid because the relevant local torsion has order coprime to the
local prime. The recursion claim is also correctly restricted. It proves
the cost of one descending preprocessing chain. It does not prove the cost
of recursively factoring every later split.

Two harmless conventions are implicit. The input has $N>1$. Also, the
quasipolynomial overhead $Q$ can be replaced by a nondecreasing
quasipolynomial majorant when (31) is summed.

## 1. Local torsion and deterministic stripping

Put

\[
U_i=(\mathbb Z/p_i^{e_i}\mathbb Z)^\times,
\qquad |U_i|=h_i=p_i^{e_i-1}(p_i-1).
\]

This group is cyclic because $p_i$ is odd. Also,

\[
p_i\nmid m,
\qquad
\gcd(m,h_i)=\gcd(m,p_i-1)=d_i,
\tag{A1}
\]

because $m=N-1\equiv-1\pmod {p_i}$. Therefore the $m$-torsion subgroup
$U_i[m]$ is cyclic of order $d_i$.

There is one useful prime-power lemma. Reduction

\[
\rho_i:U_i\longrightarrow(\mathbb Z/p_i\mathbb Z)^\times
\]

has a $p_i$-group kernel. Its restriction to $U_i[m]$ is injective.
Indeed, an element in the intersection of the kernel and $U_i[m]$ has
order dividing both a power of $p_i$ and $m$. Thus every element whose
order divides $m$ has the same order modulo $p_i^{e_i}$ and modulo $p_i$.
This fact rules out a partial $p_i$-power contribution during stripping.

Let $t_i=\operatorname{ord}_{p_i^{e_i}}(a)$. If $G_0=N$, then
$t_i\mid m$ for every $i$. If $G_0=1$, then no $p_i$ divides $a^m-1$.
For every $k\mid m$, divisibility $p_i\mid a^k-1$ would imply
$p_i\mid a^m-1$. Hence every gcd in (4) is one. A value strictly between
one and $N$ is already a proper divisor. This proves the initial trichotomy.

Now suppose $G_0=N$. During stripping, maintain

\[
t_i\mid R\quad\text{for all }i.
\tag{A2}
\]

This holds first for $R=m$. For a rational prime $q\mid R$, a hidden
component $p_i^{e_i}$ divides $a^{R/q}-1$ exactly when $t_i\mid R/q$.
Moreover, it contributes either the entire prime power or nothing. To see
this, put $y=a^{R/q}$. Then $y^q=1$, and $q\ne p_i$ because
$q\mid R\mid m$. If $y=1\pmod {p_i}$, its class lies in the $p_i$-group
kernel of reduction and has order dividing $q$. Hence it is already
$1\pmod {p_i^{e_i}}$.

It follows that:

- $G_q=N$ means every $t_i\mid R/q$. Replacing $R$ by $R/q$ preserves
  (A2).
- $1<G_q<N$ gives a proper factor.
- $G_q=1$ means no $t_i\mid R/q$. Since every $t_i\mid R$, this is
  equivalent to $v_q(t_i)=v_q(R)$ for every $i$.

After all removable copies of all primes have been tested, each prime
valuation in every $t_i$ equals the corresponding valuation in the final
$R$. Therefore $t_i=R$ for all $i$, which proves (6).

The same valuation argument proves the public certificate (7). From
$a^R=1\pmod N$, every local order divides $R$. If a local order were
smaller than $R$, it would divide $R/q$ for some prime $q\mid R$. This
would contradict $\gcd(a^{R/q}-1,N)=1$. Thus (8) is exact, including for
repeated hidden prime powers.

For every returned common order $R_j$,

\[
R_j\mid m,
\qquad R_j\mid h_i,
\qquad
R_j\mid\gcd(m,h_i)=d_i\mid p_i-1.
\tag{A3}
\]

Hence their lcm $C$ divides every $p_i-1$, which proves (9). If $N$ were
composite, it would have a prime divisor $p_i\le\sqrt N$. But (9) and
$C>\sqrt N$ would give $C\le p_i-1<\sqrt N$. This contradiction proves
(10).

## 2. Exact random law

The Chinese remainder theorem makes the local components of a uniform unit
independent and uniform in the groups $U_i$.

The event $G_0=1$ says that, for every $i$, the reduction of the local
component is not an $m$-th root in
$(\mathbb Z/p_i\mathbb Z)^\times$. That cyclic group has exactly $d_i$
such roots among $p_i-1$ elements. Its local probability is

\[
1-\frac{d_i}{p_i-1}=\beta_i.
\]

The event $G_0=N$ says that every local component belongs to $U_i[m]$.
This subgroup has $d_i$ elements among $h_i$, so its local probability is

\[
\frac{d_i}{h_i}=\gamma_i.
\]

Independence proves (13). The remaining disjoint event is a proper gcd,
which proves (14).

Conditioning on $G_0=N$ conditions each independent component to its
subgroup $U_i[m]$. The components remain independent and become uniform
in cyclic groups of orders $d_i$. A cyclic group has $\varphi(r)$ elements
of exact order $r$ when $r\mid d_i$, and none otherwise. Thus all local
orders are equal with conditional probability

\[
\frac{\sum_{r\mid D}\varphi(r)^s}{\prod_i d_i},
\qquad D=\gcd(d_1,\ldots,d_s),
\]

which is (15). The deterministic result above shows that equality of all
local orders is also exactly the event that stripping returns no factor.

Multiplying the probability of $G_0=N$ by the conditional mass of common
order $r$ gives

\[
\left(\prod_i\frac{d_i}{h_i}\right)
\frac{\varphi(r)^s}{\prod_i d_i}
=\frac{\varphi(r)^s}{\prod_i h_i},
\]

which proves (16). Given an accumulated lcm $C$, a returned common order
$r$ causes no strict growth exactly when $r\mid C$. The complete
nonreturn event and these synchronized-return events are disjoint. Their
sum is exactly (17). Every omitted event is either a proper gcd or a common
order not dividing $C$. This proves the final assertion of Section 2.

## 3. Squarefree semiprimes

Let $N=pq$, and abbreviate $P=p-1$ and $Q=q-1$. Reduction modulo $P$ and
$Q$ gives

\[
\gcd(pq-1,P)=\gcd(q-1,P)=d,
\qquad
\gcd(pq-1,Q)=\gcd(p-1,Q)=d,
\]

where $d=\gcd(P,Q)$. This proves (19).

At $C=1$, formula (17) leaves only two no-progress events. Neither local
component is an $m$-th root, or both root components have common order one.
The latter tuple is the identity tuple. Therefore

\[
\begin{aligned}
\Pr(\text{success})
&=1-\left(1-\frac dP\right)\left(1-\frac dQ\right)
  -\frac1{PQ}\\
&=\frac dP+\frac dQ-\frac{d^2+1}{PQ},
\end{aligned}
\]

which is (20). Among full-return tuples, the no-factor tuples are exactly
the tuples with a common order. Counting them gives

\[
\frac{\sum_{r\mid d}\varphi(r)^2}{PQ}.
\]

Subtracting both this mass and complete nonreturn from one proves (21).
Restricting the common-order count to $r>1$ proves (22). The two formulas
sum to (20), since the omitted $r=1$ term equals $1/(PQ)$.

## 4. Bounded-gap obstruction

Because $d$ divides both $p-1$ and $q-1$, it divides their difference
$q-p$. Thus $d\le H$ when $q-p\le H$. Every synchronized common order
divides $d$. The lcm of any collection of divisors of $d$ still divides
$d$. Such returns can never produce $C>H$.

A factor or strict growth is impossible when neither local component is an
$m$-th root. A union bound therefore gives, for every current $C$,

\[
\Pr(\text{factor or growth})
\le \frac d{p-1}+\frac d{q-1}=O_H(p^{-1}),
\]

which proves (24). Conversely, (20), together with $2\le d\le H$, shows
that the starting-state success probability is also $\Theta_H(p^{-1})$.
Since $q=p+O_H(1)$,

\[
\log_2 N=2\log_2p+O_H(1),
\]

and the definition of $n$ changes this by only $O(1)$. This proves (25).

For a sample uniform in all residues modulo $pq$, the number of residues
whose direct gcd is a proper nonunit factor is
$(q-1)+(p-1)=p+q-2$. Its probability is $O(p^{-1})$. Conditional on being
a unit, the preceding upper bound applies. The total success probability is
therefore still $O_H(p^{-1})$.

For numerical-QP $K(n)$, one has $K(n)=2^{o(n)}$. Applying the per-step
bound for each fresh uniform sample and taking a union bound gives

\[
K(n)\,2^{-n/2+O_H(1)}=2^{-\Omega(n)}.
\]

The bound is uniform in the current state. Thus it also covers state
changes caused by earlier synchronized returns. Independence ensures that
every fresh base retains the stated distribution. The bounded-prime-gap
theorem supplies infinitely many such balanced pairs for one fixed $H$.
Thus the claimed all-input inverse-QP lower bound for this sampling route is
indeed false.

## 5. Contrasts

### Prime input

For prime $N$, the unit group is cyclic of order $m$. Write a uniform
element as $g^z$ with $z$ uniform modulo $m$. If $q^v\Vert m$, its order
contains the full factor $q^v$ exactly when $q\nmid z$. One sample misses
that full factor with probability $1/q$. Hence $k$ independent samples all
miss it with probability $q^{-k}$. The lcm differs from $m$ only if at
least one prime-power part is missed. Therefore

\[
\Pr(C_k\ne m)\le\sum_{q\mid m}q^{-k}
\le\omega(m)2^{-k}<n2^{-k},
\]

which proves (27). Taking $k=O(\log n)$ makes the failure probability
polynomially small. Also, $C_k=m>\sqrt N$ gives the stated certificate.

### Squarefree Carmichael input

Korselt's criterion gives $p_i-1\mid m$ for every component. Thus every
unit fully returns. Starting at $C=1$, unequal local orders give a factor.
An equal common order greater than one gives growth. Common order one forces
every local component to be the identity. CRT gives exactly one such unit
among $\varphi(N)$, which proves (28).

### Odd prime power

For $N=p^e$,

\[
\gcd(p^e-1,p^{e-1}(p-1))=p-1.
\]

Thus $d_1=p-1$, $\gamma_1=d_1/h_1=p^{1-e}$, and
$\beta_1=1-d_1/(p-1)=0$. Equations (13)--(14) give exactly (29). In
particular, every unit is an $m$-th root modulo $p$. Thus a failure of full
return always gives a nontrivial power of $p$, never $G_0=1$. The general
derivation used no squarefreeness. It therefore continues to cover mixed
repeated prime-power components. Independent perfect-power detection is a
valid deterministic preprocessing terminal for the pure prime-power case.

## 6. Recursion scope

From $n=\lceil\log_2(N+1)\rceil$, one has $N+1\le2^n$, and hence

\[
A=\frac{N-1}{2}<\frac{N+1}{2}\le2^{n-1}.
\]

Therefore $A$ has at most $n-1$ bits. Its complete factorization gives that
of $m=2A$.

For one sample, the stripping loop performs at most the total number of
prime factors of $m$, counted with multiplicity, plus one terminal test per
distinct prime. This is $O(n)$. Modular exponentiation, gcd computation,
certificate verification, and lcm updates are polynomial in $n$. A
numerical-QP sample count therefore gives numerical-QP overhead $Q(n)$.

If this stage makes only the recursive call on $A$, iteration gives

\[
\mathcal T(n)
\le \mathcal T(n-1)+Q(n)
\le \mathcal T(1)+\sum_{j=2}^nQ(j)
\le \mathcal T(1)+n\widetilde Q(n),
\]

where $\widetilde Q$ is a nondecreasing numerical-QP majorant. This is
still $2^{(\log n)^{O(1)}}$. Thus a fixed-ratio decrease is unnecessary
for this unique chain.

This argument supplies no recurrence for a complete factoring algorithm by
itself. In particular, $A$ can have $n-1$ bits. After an unbalanced split,
the large cofactor can also have $n-O(1)$ bits. If both are recursively
factored, both children occur in the same recursion tree, as in (32). The
one-chain sum cannot be applied to that tree without an additional aggregate
bound. This confirms the precise limitation stated in Section 6.
