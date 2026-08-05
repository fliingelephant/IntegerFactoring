# F16 — affine stabilizer-chain kill test

**Status:** self-audited.

**Family:** B7, a nonabelian/affine lift of Shor's hidden period.

**Classification:** method failure for explicit faithful permutation actions, and
for nonfaithful local affine actions that must retain any nonzero translation.
This is not a lower bound against all succinct actions, all nonabelian lifts, or
all quotient actions that discard translations but retain some other sufficient
factor certificate.

**Computation:** none. Every statement below is symbolic, so there is no run
manifest.

## Closest prior route and material difference

The closest prior route is F07/P12, which studies standard trace and point probes
for Shor's modular-multiplication spectrum. The present route does not reconstruct
that spectrum or use dense moments. It lifts a hidden subgroup into an affine or
semidirect-product action and asks whether a Schreier--Sims/Luks stabilizer chain
can run on only polynomially many test objects. The new decisive invariant is
faithful permutation degree, explicitly separated from base size. P17 is a
secondary analogy because it also warns that a small base does not make an
automorphism search small, but P17 concerns descent in fixed-degree algebras, not
an affine lift of a hidden cyclic period.

Throughout, the degree of an action is the cardinality of its permutation domain.
For a family of actions, total degree means the sum of the individual degrees,
equivalently the degree of their disjoint union.

## 1. A prime-order element forces prime-sized degree

### Lemma 1 (prime-cycle obstruction)

Let \(G\) contain an element \(\tau\) of prime order \(p\).

1. Every faithful action \(\rho:G\to\operatorname{Sym}(\Omega)\) has
   \(|\Omega|\ge p\).
2. More generally, if actions
   \(\rho_i:G\to\operatorname{Sym}(\Omega_i)\) have faithful diagonal product,
   then
   \[
   \sum_i |\Omega_i|\ge p.
   \]
   In fact, at least one individual degree is at least \(p\).

**Proof.** Faithfulness makes \(\rho(\tau)\) have order \(p\). A permutation of
prime order has only cycles of lengths \(1\) and \(p\), and a nonidentity such
permutation has a \(p\)-cycle. This proves (1). For (2), faithfulness of the
diagonal product means that some \(\rho_i(\tau)\) is nonidentity. Its order is
then \(p\), so the same cycle argument gives \(|\Omega_i|\ge p\). \(\square\)

The same proof gives the precise nonfaithful boundary needed for a stabilizer
construction. Suppose a target subgroup \(H\le G\) is represented exactly as the
common stabilizer of test objects in a family of actions. Then the intersection
of the action kernels lies in \(H\). If \(\tau\notin H\), some action must see
\(\tau\), and its degree is at least \(p\). Thus global faithfulness is not needed
for the lower bound: it is enough that the test objects distinguish \(\tau\) from
the claimed hidden stabilizer.

## 2. The local affine group

Write

\[
G_p=\operatorname{AGL}_1(\mathbb F_p)
=\{x\mapsto ax+b:a\in\mathbb F_p^\times, b\in\mathbb F_p\}
=T_p\rtimes\mathbb F_p^\times,
\]

where \(T_p=\{t_b:x\mapsto x+b\}\cong C_p\).

### Proposition 2 (minimum degree and base size)

The minimum faithful permutation degree of \(G_p\) is exactly \(p\). Its natural
action on \(\mathbb F_p\) attains this degree. For \(p>2\), that natural action
has base size exactly two; \((0,1)\) is a base.

**Proof.** The translation \(t_1\) has order \(p\), so Lemma 1 gives the lower
bound. The natural degree-\(p\) action is faithful: an affine map fixing every
point has \(b=0\) from the point 0 and then \(a=1\) from the point 1. The same
calculation shows that \((0,1)\) is a base. A one-point stabilizer has order
\(p-1>1\) when \(p>2\), so the base size is not one. \(\square\)

The natural stabilizer chain displays why the base does not control the work:

\[
G_p > (G_p)_0=\{x\mapsto ax:a\ne0\} > (G_p)_{0,1}=1.
\]

Its two orbit indices are \(p\) and \(p-1\). A standard explicit
Schreier--Sims implementation must represent a degree-\(p\) permutation and
construct an orbit/transversal of size \(p\) at the first level. Chain depth two
does not remove that cost.

### Proposition 3 (nonfaithful local actions erase every translation)

Every nontrivial normal subgroup of \(G_p\) contains \(T_p\). Consequently every
nonfaithful action of \(G_p\) kills all translations. In particular:

* any action nontrivial on even one nonzero translation is automatically faithful
  and has degree at least \(p\);
* no family consisting entirely of nonfaithful \(G_p\)-actions can have faithful
  diagonal product, because every kernel contains \(T_p\);
* a hidden subgroup not containing \(T_p\) cannot be the exact stabilizer of test
  objects in a nonfaithful \(G_p\)-action.

**Proof.** Let \(K\triangleleft G_p\) be nontrivial and choose
\(g=(a,b)\in K\setminus\{1\}\). If \(a=1\), then \(b\ne0\), and the powers of
\(t_b\) are all of \(T_p\). If \(a\ne1\), conjugating a translation gives
\(g t_c g^{-1}=t_{ac}\), so the commutator is the nonzero translation
\(t_{(a-1)c}\) for any \(c\ne0\). Normality puts that commutator in \(K\), and
again it generates \(T_p\). Apply this to the kernel of an action. \(\square\)

This is stronger than merely saying that actions of degree below \(p\) kill
translations. It closes the proposed local escape through a nonfaithful affine
action whenever the translation coordinate is supposed to carry the hidden
distinction.

There is one exact nonfaithful quotient that remains relevant:

\[
G_p\longrightarrow G_p/T_p\cong\mathbb F_p^\times,
\qquad (a,b)\longmapsto a.
\]

It discards every translation but retains multiplicative-order information. If
Shor's period is placed entirely in this quotient, Proposition 3 does not kill
the construction. The nonabelian lift has then contributed no extra information,
however; the explicit-action question reduces to the cyclic minimum-degree
calculation in Section 4, and the succinct-action question reduces to the matrix
order/stabilizer identity in Section 5.

## 3. The affine group over a balanced semiprime

Let \(N=pq\) for distinct primes. CRT gives

\[
\operatorname{AGL}_1(\mathbb Z/N\mathbb Z)
\cong G_p\times G_q.
\]

The natural action on \(\mathbb Z/N\mathbb Z\) is faithful of degree \(N\), and
\((0,1)\) is a base. Its first base orbit has \(N\) points; after fixing 0, the
orbit of 1 is \((\mathbb Z/N\mathbb Z)^\times\), of size \(\varphi(N)\). Thus
even this depth-two chain has orbit indices \(N\) and \(\varphi(N)\).

### Proposition 4 (exact minimum degree for the semiprime affine group)

For distinct primes \(p,q\),

\[
\mu\bigl(\operatorname{AGL}_1(\mathbb Z/pq\mathbb Z)\bigr)=p+q,
\]

where \(\mu\) denotes minimum faithful permutation degree.

**Proof.** Translation by 1 has order \(pq\). A permutation of order \(pq\) must
either contain a \(pq\)-cycle or contain both a \(p\)-cycle and a disjoint
\(q\)-cycle. Hence its degree is at least
\(\min(pq,p+q)=p+q\). Conversely, under the CRT product decomposition, let the
first local affine group act naturally on a set of size \(p\), the second act
naturally on a disjoint set of size \(q\), and let each factor act trivially on
the other set. The disjoint-union action is faithful and has degree \(p+q\).
\(\square\)

The upper-bound construction consists of two nonfaithful actions of the product
group whose diagonal product is faithful. It therefore also shows that the total
degree lower bound is the correct measure; distributing the action among many
test families does not make the aggregate representation small. Constructing
these two local actions from \(N\) requires identifying the CRT components; as an
abstract upper bound it is not a factor-free algorithm.

If the semiprime is balanced, for example \(p<q<2p\), and
\(n=\lceil\log_2(N+1)\rceil\), then

\[
p>\sqrt{N/2}\ge 2^{(n-2)/2}.
\]

Thus the local natural degree \(p\), the optimal global faithful degree \(p+q\),
and the natural global degree \(N\) are all exponential in the input bit length.
An explicit permutation is itself an exponential-size input, and the usual
Schreier--Sims orbit operations are polynomial in this degree, not in its
logarithm. The local and natural global affine actions have base size two; the
displayed optimal disjoint-union action has the still-constant base size four.
This proves the requested separation between small base and small degree.

## 4. Cyclic multiplicative subgroups

The translation obstruction should not be silently transferred to a hidden
period that lies only in a multiplicative complement. The exact cyclic analogue
is as follows.

### Lemma 5 (minimum faithful degree of a cyclic group)

If

\[
r=\prod_{i=1}^s \ell_i^{e_i}\ge2,
\]

then

\[
\mu(C_r)=\sum_{i=1}^s \ell_i^{e_i}.
\]

**Proof.** Disjoint cycles of the displayed prime-power lengths give a faithful
action, proving the upper bound. Conversely, the image of a generator in any
faithful action has order \(r\). For every maximal prime power
\(\ell_i^{e_i}\), some cycle length is divisible by it. Assign each maximal
prime power to one such cycle. A cycle assigned pairwise coprime prime powers has
length at least their product, and that product is at least their sum (repeatedly
use \(xy\ge x+y\) for \(x,y\ge2\)). Summing over cycles gives the lower bound.
\(\square\)

Hence a large prime divisor \(L\mid r\) forces degree at least \(L\). P12 already
provides an unconditional fixed-pair family with \(r=\ell=2^{\Theta(n)}\), so no
uniform poly\((n)\) degree bound exists for faithful explicit actions of the
hidden cyclic subgroup on every \((N,a)\). This uses no claim about the order of
a random residue. Accordingly it does not refute a factoring algorithm that
resamples \(a\) and proves an inverse-polynomial mass of favorable orders.

The formula also marks a genuine surviving case: if every prime-power divisor of
\(r\) collectively has polynomial sum, then \(C_r\) has a polynomial-degree
faithful action even when \(r\) itself is large. A universal factoring route would
need a proved way to reach such orders or a quotient action that retains enough
information; no unproved order-distribution premise may substitute for that
proof.

## 5. Succinct and linear actions: what survives

Affine maps do have a factor-free succinct representation:

\[
(a,b)\longmapsto
\begin{pmatrix}a&b\\0&1\end{pmatrix}
\in GL_2(\mathbb Z/N\mathbb Z).
\]

Composition, inversion of the known unit \(a\), action on a vector, and equality
are polynomial-time in \(\log N\). This shows that the permutation-degree
obstruction is not a representation-size lower bound for circuit or matrix
actions.

For the whole affine group, the stabilizers of 0 and of \((0,1)\) are indeed
available factor-free from the formulas above: they are respectively the scaling
subgroup and the identity. Those easy stabilizers contain no hidden-period
information. The difficulty returns when the acting group is the cyclic subgroup
generated by modular multiplication.

It does not, however, supply an applicable stabilizer algorithm. For a unit
\(u\pmod N\), put

\[
M_u=\begin{pmatrix}u&0\\0&1\end{pmatrix},
\qquad e_1=(1,0)^T.
\]

Then

\[
M_u^k e_1=e_1
\quad\Longleftrightarrow\quad
u^k=1\pmod N.
\]

Therefore the stabilizer of \(e_1\) in the exponent-domain action
\(\mathbb Z\curvearrowright(\mathbb Z/N\mathbb Z)^2\) is exactly
\(\operatorname{ord}_N(u)\mathbb Z\). Equivalently, the orbit of \(e_1\) under
\(\langle M_u\rangle\) has size \(\operatorname{ord}_N(u)\), even though one
vector is a base for that cyclic matrix group. Computing the least positive
stabilizer exponent or the orbit size is precisely modular order finding.

Thus the two-dimensional representation is a clean surviving formulation, but
not a new algorithm: invoking an unspecified ``matrix stabilizer'' routine here
would assume the target subproblem. Standard explicit-permutation
Schreier--Sims does not apply to the circuit encoding with a runtime polynomial in
\(\log |\Omega|\); if expanded, the relevant orbit can be exponential.

## 6. Exact retry boundary

The explicit-permutation affine route may be reopened only with at least one of
the following materially new ingredients:

1. **A quotient sufficient for factoring.** Give a factor-free nonfaithful action
   and prove that its kernel lies inside the target hidden subgroup (or otherwise
   prove that the quotient certificate alone always yields a proper factor). For
   a local \(G_p\), any such action that must distinguish a nonzero translation
   is impossible by Proposition 3; a viable quotient must deliberately discard
   \(T_p\) and prove that the remaining multiplicative data suffices.
2. **A justified succinct-action algorithm.** State an algorithm whose input is
   the affine/circuit representation, prove a runtime polynomial in circuit size
   and \(\log N\) rather than permutation degree, and prove that its stabilizer or
   orbit output recovers the hidden subgroup. Citing ordinary Schreier--Sims or
   Luks, whose explicit action work is polynomial in degree, is insufficient.
3. **A factor-free linear stabilizer beyond order finding.** Use the small matrix
   representation with a special module, tensor, or family of test vectors for
   which the stabilizer is computable over \(\mathbb Z/N\mathbb Z\) in polynomial
   bit complexity and prove that the result separates CRT components. Computing
   the stabilizer of \(e_1\) for \(\langle M_u\rangle\) is exactly the original
   order-finding problem and is not new.
4. **A distribution theorem for a cyclic quotient.** If relying on small
   \(\mu(C_r)\), prove an inverse-polynomial probability, for the algorithm's
   actual factor-free choice of bases, that
   \(\sum_{\ell^e\parallel r}\ell^e=\operatorname{poly}(n)\). Fixed favorable
   examples or heuristic smoothness of orders do not meet the boundary.

No conclusion here rules out all nonabelian lifts or all succinct actions. It
closes the specific inference ``small affine base implies a stabilizer chain on
poly\((\log N)\) explicit test objects.''
