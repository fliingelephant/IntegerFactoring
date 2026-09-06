# F215 candidate — abelian higher reciprocity preserves the beta-two inversion torsor

## Status

This is a frozen, self-audited, proof-only candidate. It is an exact
information boundary for scalar abelian reciprocity data and an exact
factor-extraction boundary for a coherent non-diagonal cyclotomic lift. It
is not a lower bound against arbitrary ring-valued, nonabelian,
Archimedean, or divisor-coefficient computations, and it is not a factoring
algorithm.

## Setup

Assume

\[
N=pq,
\qquad p<q<2p,
\qquad N\equiv3\pmod4,
\]

where $p,q$ are distinct odd primes, and put

\[
K=\frac{N-1}{2}.
\]

The complete prime factorization of $K$ is granted. Since
$N\equiv3\pmod4$, $K$ is odd. A *$K$-supported cyclotomic modulus* below
means an integer $d\mid K$. A *scalar reciprocity transcript* means a transcript
whose factor-dependent entries are only:

1. products of one-dimensional Artin or ray-character values over all
   hidden prime components;
2. fully symmetric cyclotomic residue symbols or Jacobi symbols;
3. local Hilbert-symbol products obtained by bilinearity or global
   reciprocity; and
4. public algebraic combinations and adaptive choices based only on earlier
   entries of these kinds.

The definition does not include a selected hidden prime ideal, an element
whose two rational CRT components carry different symbol values, a sum of
the two hidden local character values, or an exact divisor coefficient.

## Theorem A — Frobenius inversion and scalar reciprocity boundary

For every $d\mid K$, all of the following hold.

### A1. Exact inversion torsor

The factors are units modulo $d$ and

\[
\boxed{q\equiv p^{-1}\pmod d.}
\]

Also $p,q<K$. Thus knowing the inversion orbit

\[
\{p\bmod K,p^{-1}\bmod K\}
\]

is enough to recover the unordered integer factor pair.

### A2. Cyclotomic Frobenius inversion

In $L_d=\mathbb Q(\zeta_d)$, the rational primes $p,q$ are unramified
and

\[
\boxed{
\operatorname{Frob}_q
=\operatorname{Frob}_p^{-1}.}
\]

Consequently their decomposition subgroups and residue degrees agree:

\[
\langle\operatorname{Frob}_p\rangle
=\langle\operatorname{Frob}_q\rangle,
\qquad
\operatorname{ord}_d(p)=\operatorname{ord}_d(q).
\]

Unlabelled cyclotomic splitting data therefore do not orient the two
factors.

### A3. Ray and genus characters

For every one-dimensional character $\chi$ of the cyclotomic or rational
ray quotient modulo $d$, writing

\[
z=\chi(\operatorname{Frob}_p),
\]

gives

\[
\boxed{
\bigl(\chi(\operatorname{Frob}_p),
      \chi(\operatorname{Frob}_q)\bigr)
=(z,z^{-1}).}
\]

The computable character of the composite ideal is only

\[
\chi(N)=zz^{-1}=1.
\]

For a genus character, $z\in\{1,-1\}$, so the two individual values are
equal even if they are granted separately. More generally, if a public ray
conductor coprime to $N$ has a $2$-part and
$\alpha=\chi(N)$ need not be one, the exact
swap involution is

\[
\boxed{z\longmapsto\alpha z^{-1}.}
\]

The product $\alpha$ does not label its two factors.

The same statement applies to an inverse class pair $C,C^{-1}$ in an
abelian ray or ideal class group: genus characters agree on the pair and a
higher character gives inverse values.

### A4. Local Hilbert symbols

Let a local or global field contain $\mu_m$, and let $a$ be public. At
every place $v$ at which the symbols are defined, bimultiplicativity gives

\[
\boxed{
(p,a)_{m,v}(q,a)_{m,v}=(N,a)_{m,v}.}
\]

Global Hilbert reciprocity supplies products of this form, not an ordered
pair of hidden local values. If $r\mid K$ and $r\nmid m$, then $N$ is
an $m$-th power in $\mathbb Q_r$. Hence every $m$-th Hilbert symbol at
$r$ having $N$ in one slot is trivial. When $r\mid m$, the wild local
correction may be nontrivial, but it is public and still gives only the
affine inversion product above.

### A5. Transcript closure

Every scalar reciprocity transcript as defined in the setup is invariant
under factor swap. For a conductor $d\mid K$, its hidden character data
factor through products which are identically one for every candidate pair

\[
(u,u^{-1}),
\qquad u\in(\mathbb Z/d\mathbb Z)^\times.
\]

Thus these products eliminate no candidate in the inversion torsor.
Adaptivity based only on earlier such products does not change this fact.

## Theorem B — exact cubic, quartic, octic, and common-order witness

Take

\[
\boxed{N=527=17\cdot31,
\qquad K=263.}
\]

Then $17<31<2\cdot17$, $N\equiv3\pmod4$, and $263$ is prime.

### B1. Fixed-order rational ray characters

The unit group is cyclic of order

\[
\left|(\mathbb Z/263\mathbb Z)^\times\right|=262=2\cdot131.
\]

Moreover,

\[
65^2\equiv17\pmod{263},
\qquad
174^2\equiv31\pmod{263}.
\]

Therefore every homomorphism from this unit group to $\mu_3$ is trivial,
and every homomorphism to $\mu_4$ or $\mu_8$ has image of order at most
two and takes value one on both hidden factors. Thus cubic, quartic, octic,
and genus ray labels modulo $K$ fail to distinguish this factor pair even
if their two individual values are granted for free.

### B2. Fixed-order cyclotomic residue symbols at the known prime

For $m\in\{3,4,8\}$, every prime $\mathfrak R\mid263$ in
$\mathbb Q(\zeta_m)$ has residue degree two. For every rational integer
$a$ with $263\nmid a$,

\[
\boxed{
\left(\frac a{\mathfrak R}\right)_m=1.}
\]

Thus the known prime factor of $K$ supplies no nontrivial rational cubic,
quartic, or octic residue label on this input. A symbol of a nonrational
primary factor of $17$ or $31$ is outside the claim: constructing that
primary factor already chooses data above a hidden rational factor.

### B3. Rational common-order obstruction

For every unit $a\bmod N$ satisfying

\[
a^{N-1}=1\pmod N,
\]

the exact orders of $a\bmod17$ and $a\bmod31$ are at most two. If the
two local signs of $a$ differ, $\gcd(a^K-1,N)$ or
$\gcd(a^K+1,N)$ factors $N$. If they agree, factor-first stripping
returns only the already public exact common order one or two. No rational
base returning under $N-1$ can give larger common-order progress on this
input.

## Theorem C — a coherent non-diagonal lift is a factor transition

Let $N=pq$ be squarefree, let $m\geq2$ satisfy

\[
\gcd(m,N)=1,
\]

and put

\[
A_m=\mathbb Z[Z]/(\Phi_m(Z))=\mathbb Z[\zeta_m].
\]

Assume $a,b\in\mathbb Z/m\mathbb Z$, and assume $m$ and $\varphi(m)$ are
numerical QP in the input bit length. Let an explicit element
$Y\in A_m/NA_m$ be given with

\[
Y\equiv\zeta_m^a\pmod{pA_m},
\qquad
Y\equiv\zeta_m^b\pmod{qA_m},
\qquad
a\not\equiv b\pmod m.
\tag{C1}
\]

Here the two congruences are congruences in the complete rational
components $A_m/pA_m$ and $A_m/qA_m$, not only at one selected prime
ideal above each rational prime.

For $0\leq e<m$, write $Y-\zeta_m^e$ in the standard power basis with
coefficients $c_{e,j}\bmod N$, and put

\[
g_e=\gcd\bigl(N,c_{e,0},\ldots,c_{e,\varphi(m)-1}\bigr).
\]

For the representatives of $a,b$, the corresponding values satisfy

\[
\boxed{g_a=p,
\qquad g_b=q.}
\]

This is a deterministic numerical-QP factor extraction.

There is a weaker selected-prime-ideal variant. The algebraic norm

\[
\operatorname{N}_{A_m/\mathbb Z}(Y-\zeta_m^e)
\]

can replace coefficient content whenever it is zero modulo exactly one of
$p,q$. A value at one selected prime ideal above $p$ proves divisibility
by $p$, but an additional no-collision condition at every prime above
$q$ is required. Merely knowing two different labels at two selected
prime ideals does not by itself imply this norm condition.

## Theorem D — trace/divisor-coefficient positive boundary

Let $G=(\mathbb Z/K\mathbb Z)^\times$. For a character
$\chi\in\widehat G$, define

\[
t_\chi(u)=\chi(u)+\chi(u)^{-1}.
\]

The full family $\{t_\chi\}_{\chi\in\widehat G}$ separates inversion
orbits in $G$: if

\[
t_\chi(u)=t_\chi(v)
\quad\hbox{for every }\chi,
\]

then $v=u$ or $v=u^{-1}$.

For the hidden factor residue $u=p\bmod K$, the trace is the exact divisor
coefficient

\[
\boxed{
\sum_{d\mid N}\chi(d)
=2+\chi(p)+\chi(p)^{-1}.}
\]

Consequently, a uniformly computable numerical-QP character bank whose
traces separate the live candidates, together with numerical-QP exact
evaluators for these divisor coefficients and a numerical-QP decoder,
would deterministically recover the inversion orbit and factor $N$.

This is a positive transition, not an evaluator. Ordinary reciprocity
computes the product $\chi(p)\chi(q)=1$; it does not compute the displayed
sum. The number, representation size, construction cost, coefficient
evaluation cost, and decoding cost of the character bank must all be
charged. The theorem does not assert that such a numerical-QP bank exists
for every $K$.

## Scope

F215 closes only the declared scalar abelian frameworks:

1. cubic, quartic, octic, or general one-dimensional residue-symbol
   products;
2. fully symmetric cyclotomic Artin and splitting data;
3. genus and ray character products; and
4. local Hilbert-symbol information used only through bilinear or global
   products.

It does not close:

1. a factor-free construction of a coherent non-diagonal lift satisfying
   (C1);
2. an exact, compressed evaluator of the trace/divisor coefficient;
3. selected-prime-ideal data accompanied by a proved norm separator;
4. nonabelian representations or nonlinear ring-valued carriers;
5. Archimedean size, exact division, or reciprocal-prefix selectors; or
6. a cyclotomic factoring method supplied with an independently proved
   multiple of a hidden group order such as $\Phi_j(p)$.

No claim is made that higher reciprocity in all possible forms cannot
factor integers.
