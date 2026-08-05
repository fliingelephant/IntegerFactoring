# Hostile audit of F16 affine stabilizer kill

Approach-family ID: F16_affine_stabilizer_audit.

**Verdict: PASS WITH REQUIRED LOCAL CORRECTIONS.** The prime-cycle
obstruction, exact local faithful degree, normal-subgroup obstruction,
semiprime CRT decomposition and minimum-degree formula, cyclic minimum-degree
formula, and exponent-stabilizer identity are correct. The result supports
exactly a method failure for ordinary explicit-permutation stabilizer chains.
It gives no lower bound for succinct, circuit, or matrix actions and no
obstruction to all nonabelian lifts.

The exact author version should not be promoted unchanged:

1. The natural action of
   $G_2=\operatorname{AGL}_1(\mathbb F_2)\cong C_2$ has base size $1$, not
   $2$. Correspondingly, the displayed disjoint CRT action for $N=2q$ has
   base size $1+2=3$, not $4$. For odd local primes the asserted values $2$
   and $4$ are exact.
2. In the matrix discussion, affine point $x$ should be written as the
   homogeneous column $\widehat x=(x,1)^T$. The literal zero vector is fixed
   by the whole matrix group. The later vector $e_1=(1,0)^T$ is a different
   vector; its stated exponent-stabilizer identity for the diagonal subgroup
   is nevertheless correct.
3. The degree-$p+q$ upper action explicitly uses $p,q$ and their CRT factors.
   It is an abstract upper bound. The proof does not show that every possible
   construction of a minimum-degree action must reveal the factors.

The first item is a smallest counterexample to the unqualified base-size
summary. It does not affect an asymptotic degree conclusion.

No computation was needed; all checks below are symbolic.

## 1. Prime-order obstruction

Let $\tau$ have prime order $p$ in $G$, and let
$\rho:G\to\operatorname{Sym}(\Omega)$ be faithful. Then $\rho(\tau)$ has
order $p$. Every cycle length of $\rho(\tau)$ divides $p$, and a nonidentity
permutation must therefore contain a $p$-cycle. Thus

\[
|\Omega|\ge p.                                                    \tag{A1}
\]

For a finite family $\rho_i$, faithfulness of the diagonal action means
$\bigcap_i\ker\rho_i=1$. Hence some $\rho_i(\tau)\ne1$, and that component
alone has degree at least $p$. For an arbitrary group, this does not say that
the component is faithful; it says only that the component sees $\tau$.

If $H$ is the exact common stabilizer of test objects, every element in
$\bigcap_i\ker\rho_i$ fixes all of them, so
$\bigcap_i\ker\rho_i\le H$. If $\tau\notin H$, at least one component must
see $\tau$ and have degree at least $p$. This needs neither global
faithfulness nor an assumption about base size.

## 2. The local affine group, including \(p=2,3\)

Write

\[
G_p=T_p\rtimes\mathbb F_p^\times,\qquad
T_p=\{t_b:x\mapsto x+b\}\cong C_p.
\]

Translation $t_1$ and (A1) give $\mu(G_p)\ge p$. The natural action on
$\mathbb F_p$ is faithful: if $x\mapsto ax+b$ fixes $0$ and $1$, then $b=0$
and $a=1$. Hence

\[
\boxed{\mu(G_p)=p\quad\text{for every prime }p.}                  \tag{A2}
\]

The stabilizer of any one point has exactly $p-1$ elements, one for each
$a\in\mathbb F_p^\times$. Therefore the exact base size is

\[
b(G_p,\mathbb F_p)=
\begin{cases}
1,&p=2,\\
2,&p>2.
\end{cases}                                                       \tag{A3}
\]

For $p>2$, no one-point base exists and two distinct points, for example
$(0,1)$, form a base. For $p=2$, $G_2=T_2\cong C_2$ acts regularly, so one
point is already a base. At $p=3$, $G_3\cong S_3$ and a point stabilizer has
order $2$, so the base size is exactly $2$.

Let $K\triangleleft G_p$ be nontrivial and choose
$g=(a,b)\in K\setminus\{1\}$. If $a=1$, then $g=t_b$ with $b\ne0$, and
$t_b$ generates the prime-order group $T_p$. If $a\ne1$, then for $c\ne0$

\[
g t_c g^{-1}=t_{ac},\qquad
[g,t_c]=t_{(a-1)c}\ne1.
\]

Normality puts the commutator in $K$, and it generates $T_p$. Thus

\[
K\ne1\quad\Longrightarrow\quad T_p\le K.                         \tag{A4}
\]

In fact the nontrivial normal subgroups are exactly $T_p\rtimes A$, where
$A\le\mathbb F_p^\times$. This disposes of the small-prime and complement
cases:

- For $p=2$, the complement is trivial and the only nontrivial normal
  subgroup is $T_2=G_2$.
- For $p=3$, the order-$2$ complements in $S_3$ are not normal, and the only
  nontrivial proper normal subgroup is $T_3=A_3$.
- For $p>2$, any complement subgroup containing a nonidentity scaling is
  moved out of the complement by conjugation with a translation.

The kernel of a nonfaithful action is nontrivial and normal, so (A4) proves
that every such action kills all of $T_p$. Conversely, an action that sees
one nonzero translation has trivial kernel and is faithful.

This gives the stronger local diagonal statement. If every component
$\rho_i$ were nonfaithful, then

\[
T_p\le\bigcap_i\ker\rho_i,
\]

so the diagonal action would be nonfaithful. Therefore every faithful
diagonal family of $G_p$-actions contains at least one individually faithful
component, which by (A2) has degree at least $p$.

That conclusion is special to the local affine group. It is false for
general groups and for the CRT product below: the two local quotient actions
of $G_p\times G_q$ are individually nonfaithful but have faithful diagonal
product.

## 3. Exact semiprime minimum degree

For distinct primes $p,q$, CRT respects the affine group law and gives

\[
\operatorname{AGL}_1(\mathbb Z/pq\mathbb Z)
\cong G_p\times G_q.                                               \tag{A5}
\]

Let $t_1:x\mapsto x+1$. It has order $pq$. In any faithful permutation
action its image $\sigma$ also has order $pq$. Every cycle length of
$\sigma$ divides $pq$. If $\sigma$ has a $pq$-cycle, its degree is at least
$pq\ge p+q$. Otherwise its cycle lengths belong to $\{1,p,q\}$, and their
least common multiple can be $pq$ only if there is both a $p$-cycle and a
distinct, hence disjoint, $q$-cycle. The degree is again at least $p+q$.

For the matching upper bound, take

\[
\Omega=\mathbb F_p\sqcup\mathbb F_q
\]

and let $(g_p,g_q)$ act naturally through $g_p$ on the first block and
through $g_q$ on the second. If this action is the identity, faithfulness of
the local natural actions gives $g_p=g_q=1$. Hence it is faithful and has
degree $p+q$. Therefore

\[
\boxed{\mu\!\left(\operatorname{AGL}_1(\mathbb Z/pq\mathbb Z)\right)=p+q.}
                                                                    \tag{A6}
\]

The natural degree-$pq$ action has base size exactly $2$: $(0,1)$ is a base,
while a one-point stabilizer has order $\varphi(pq)>1$. The displayed
degree-$p+q$ action has base size $4$ when $p,q$ are odd and $3$ when one
prime is $2$.

F16 states (A6) only for a squarefree product of two distinct primes, and no
factoring result for repeated factors follows from that statement. For
completeness, the same group theorem can be extended only after adding a
proof. If

\[
N=\prod_i\ell_i^{e_i},
\]

then translation by $1$ has order $N$, so the cyclic lower bound in the next
section gives degree at least $\sum_i\ell_i^{e_i}$. CRT and the disjoint
union of faithful natural actions on
$\mathbb Z/\ell_i^{e_i}\mathbb Z$ give the matching upper bound. Thus

\[
\mu\!\left(\operatorname{AGL}_1(\mathbb Z/N\mathbb Z)\right)
=\sum_{\ell^e\parallel N}\ell^e.                                  \tag{A7}
\]

The action proving this upper bound uses the prime-power CRT decomposition.
Equation (A7) is not a factor-free algorithm and says nothing about the
complexity of discovering the action from $N$.

## 4. Cyclic minimum degree

Let $r=\prod_i\ell_i^{e_i}\ge2$. Disjoint cycles of lengths
$\ell_i^{e_i}$ give a permutation of order $r$, hence a faithful action of
$C_r$ of degree $\sum_i\ell_i^{e_i}$.

Conversely, let the image of a generator in a faithful action have cycle
lengths $d_1,\ldots,d_m$. Its order is
$\operatorname{lcm}(d_1,\ldots,d_m)=r$. For each maximal prime power
$q_i=\ell_i^{e_i}$, choose a cycle $d_{j(i)}$ divisible by $q_i$. For one
fixed cycle, the assigned $q_i$ are pairwise coprime, so their product
divides the cycle length. The product of integers at least $2$ is at least
their sum. Therefore

\[
d_j\ge \sum_{i:j(i)=j}q_i.
\]

Summing over cycles proves

\[
\boxed{\mu(C_r)=\sum_{\ell^e\parallel r}\ell^e.}                  \tag{A8}
\]

The scope is finite permutation actions of the abstract cyclic group, with
$r\ge2$. It is not a lower bound on succinct encodings. The use of promoted
P12 in F16 is within scope: P12 supplies fixed pairs with
$r=\ell=2^{\Theta(n)}$, so a faithful **explicit permutation** action of
that cyclic subgroup has exponential degree. P12 supplies no distribution
theorem for a resampled base, and F16 correctly preserves that limitation.

## 5. Matrix conventions and the exact surviving problem

Use column vectors. The faithful affine representation is

\[
(a,b)\longmapsto
A_{a,b}=\begin{pmatrix}a&b\\0&1\end{pmatrix},\qquad
A_{a,b}\widehat x=\widehat{ax+b},\qquad
\widehat x=\binom{x}{1}.                                           \tag{A9}
\]

Thus the stabilizer of $\widehat0=(0,1)^T$ in the whole affine group is the
scaling subgroup $\{A_{a,0}\}$, and the common stabilizer of
$\widehat0,\widehat1$ is the identity. By contrast, the literal zero vector
has the whole group as stabilizer.

For a unit $u\pmod N$, let

\[
M_u=\operatorname{diag}(u,1),\qquad e_1=(1,0)^T.
\]

For every $k\in\mathbb Z$, with negative exponents defined because $u$ is a
unit,

\[
M_u^k e_1=(u^k,0)^T=e_1
\quad\Longleftrightarrow\quad
u^k\equiv1\pmod N.
\]

Consequently

\[
\operatorname{Stab}_{\mathbb Z}(e_1)
=\operatorname{ord}_N(u)\mathbb Z,                                \tag{A10}
\]

and the orbit has exactly $\operatorname{ord}_N(u)$ vectors. The vector
$e_1$ is a base for the finite cyclic matrix group $\langle M_u\rangle$, but
its orbit can be exponentially large.

There is no contradiction between (A9)--(A10) and the permutation-degree
lower bounds. A matrix or circuit description has $O(\log N)$-bit entries
and is succinct. Ordinary explicit-permutation Schreier--Sims takes a domain
of size $d$ as explicit data and performs orbit/transversal work polynomial
in $d$; it supplies no runtime polynomial in $\log d$ for (A9). Other
matrix- or circuit-group algorithms are outside that model and are not ruled
out. Equation (A10) proves only that an algorithm asked for the least positive
stabilizing exponent on this instance is being asked to compute the modular
order. It is an identity of problems, not a hardness theorem.

## 6. Accepted scope

After the local corrections, the proved obstruction is precisely:

- A faithful explicit action of $G_p$, or any local test family that must
  distinguish a nonzero translation, contains a component of degree at least
  $p$.
- The minimum faithful explicit degree for the semiprime affine group is
  $p+q$, despite constant base size.
- Quotienting $G_p$ by $T_p$ deliberately discards the translation
  obstruction and leaves cyclic multiplicative information.
- A succinct affine matrix encoding avoids the representation-size lower
  bound, but the displayed cyclic vector stabilizer asks for modular order.

This closes the inference “small affine base implies a
poly$(\log N)$-size ordinary Schreier--Sims computation.” It does not close
succinct stabilizer algorithms, quotient certificates, alternative matrix
modules or tensors, resampling arguments, or nonabelian lifts with a different
mechanism.
