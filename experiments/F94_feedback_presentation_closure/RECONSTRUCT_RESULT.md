# Independent proof-blind reconstruction

## Verdict

**PASS**, with the following two scope constraints made explicit.

1. A closing column exposes one *normalized candidate root coset* \(yH\).
   The coset need not be distinct from the old root image \(H\). Thus closure
   alone does not give a new residue root or a factor.
2. A materialized decoder menu of size \(\ell\) costs \(O(\ell)\) operations.
   This is polynomial in the size of the explicit menu, but not in the binary
   length \(\log \ell\). A polynomial-in-\(\log N\) claim therefore needs a
   numerical cap on every promoted \(\ell\), or an equivalent explicit cap on
   total menu size.

With these meanings, all six claims are correct. No algebraic correction is
needed.

## Notation

All kernels, images, ranks, spans, and dimensions below are over
\(\mathbb F_\ell\). Write

\[
A=E\bmod\ell,\qquad D=\Delta_\alpha\bmod\ell,\qquad A'=DA.
\]

Thus \(A:\mathbb F_\ell^m\to\mathbb F_\ell^s\),
\(D:\mathbb F_\ell^s\to\mathbb F_\ell^t\), and
\(A':\mathbb F_\ell^m\to\mathbb F_\ell^t\).

## 1. Exact multiplicity-refinement gate

Composition gives

\[
\ker A'=\{c\in\mathbb F_\ell^m:D(Ac)=0\}
       =\{c:Ac\in\ker D\}.
\]

Restrict \(A\) to \(\ker A'\). Its image is exactly
\(\operatorname{im}A\cap\ker D\): if \(c\in\ker A'\), then
\(Ac\) belongs to the intersection; conversely, if \(z=Ac\) belongs to the
intersection, then \(DAc=0\), so \(c\in\ker A'\). The kernel of this
restriction is \(\ker A\). Hence

\[
0\longrightarrow\ker A\longrightarrow\ker A'
 \overset{A}{\longrightarrow}\operatorname{im}A\cap\ker D
 \longrightarrow0
\]

is exact, and

\[
\dim\ker A'-\dim\ker A
=\dim(\operatorname{im}A\cap\ker D).
\]

For \(x=(x_1,\ldots,x_s)\) and \(r\in D_j\), disjointness of the supports
gives

\[
(Dx)_r=\overline{\alpha}_{rj}x_j.
\]

Rows outside all \(D_j\) impose no condition. Since every \(D_j\) is
nonempty, \(x_j\) is free exactly when every \(\alpha_{rj}\), \(r\in D_j\),
is divisible by \(\ell\). Otherwise one nonzero coefficient forces
\(x_j=0\). Therefore

\[
\ker D=\operatorname{span}\{e_j:\ell\mid\alpha_{rj}
                  \text{ for all }r\in D_j\}.
\]

The old kernel is contained in the refined kernel. It grows exactly when
\(\operatorname{im}A\cap\ker D\ne0\). If each old block has at least one
descendant exponent not divisible by \(\ell\), then \(\ker D=0\), so the
kernel is unchanged. This condition is sufficient, not necessary: equality
also holds whenever the displayed intersection is zero.

For the example, over \(\mathbb F_2\), \(A=[1]\) has zero-dimensional
kernel. The exponent map for \(4=2^2\) is \(D=[2]=[0]\), so \(A'=[0]\)
and \(\ker A'=\mathbb F_2\). The kernel grows by one dimension.

## 2. Exact appended-column gate

Let \(u\in\mathbb F_\ell^t\). A vector \((x,a)\) is in the augmented kernel
exactly when

\[
A'x+au=0.
\]

If \(u\notin\operatorname{colspan}(A')\), then \(a\ne0\) would imply
\(u=-a^{-1}A'x\), a contradiction. Thus \(a=0\) and

\[
\ker[A'\mid u]=\ker A'\times\{0\}.
\]

The new column raises the rank by one, so its addition leaves the nullity
\(m-\operatorname{rank}A'\) unchanged.

If \(A'c+u=0\), then \(A'x+au=A'(x-ac)\). Every kernel vector has the
unique form

\[
(x,a)=(v,0)+a(c,1),\qquad v\in\ker A',
\]

and the sum is direct because \((c,1)\) has nonzero last coordinate. Thus

\[
\ker[A'\mid u]
=(\ker A'\times\{0\})\oplus\langle(c,1)\rangle,
\]

and the nullity grows by one. Together with Claim 1, this proves the stated
two-gate accounting for a process whose presentation changes by exact
refinement and column appending. Deletion is a different operation.

### Root-coset consequence under the P91 hypotheses

Let \(C_0=\Delta_\alpha E\) be the integer lifted old matrix, so
\(C_0\bmod\ell=A'\). Let \(\widetilde u\) be the integer new relation
column whose reduction is \(u\), and put \(C_+=[C_0\mid\widetilde u]\).
More generally, let \(C\) be any integer relation matrix on unit blocks
\(B_1,\ldots,B_t\). For \(z\in\ker(C\bmod\ell)\), choose an integer lift
\(\widetilde z\) and define

\[
\rho_C(z)=\prod_{r=1}^t
B_r^{(C\widetilde z)_r/\ell}\pmod N.
\]

This is well-defined. Replacing \(\widetilde z\) by
\(\widetilde z+\ell h\) multiplies the result by \(B^{Ch}\), a product of
known relations, hence by \(1\pmod N\). The same argument makes \(\rho_C\)
a homomorphism, and

\[
\rho_C(z)^\ell=B^{C\widetilde z}=1\pmod N.
\]

Let \(H=\rho_{C_0}(\ker A')\) be the explicit old root image. In the closing
case, let \(g=(c,1)\) and \(y=\rho_{C_+}(g)\). Every new kernel direction
has nonzero last coordinate. Scaling that coordinate to one puts it in the
single affine coset

\[
g+(\ker A'\times\{0\}).
\]

Its root image is \(yH\). A nonzero scalar in \(\mathbb F_\ell\) raises an
\(\ell\)-th root to a power coprime to \(\ell\), which preserves at each
prime divisor of \(N\) whether the root is \(1\). Thus one normalized coset
is sufficient for the decoder. This does not prove \(y\notin H\); \(yH\)
can equal \(H\).

Assume now \(N=pq\) for distinct odd primes. By CRT,

\[
\mu_\ell(N)\cong\mu_\ell(\mathbb F_p^\times)
                 \times\mu_\ell(\mathbb F_q^\times).
\]

Each component has size \(\gcd(\ell,p-1)\) or \(\gcd(\ell,q-1)\), hence
size \(1\) or \(\ell\). Failure of the complete old pairwise-gcd decoder on
\(H\) makes both CRT projections injective on \(H\). Two distinct old roots
with the same residue modulo \(p\) would give
\(\gcd(x-y,N)=p\), and similarly for \(q\). Therefore

\[
|H|\le\ell.
\]

Old-old comparisons were already made. Comparisons within \(yH\) reduce to
old-old comparisons because \(y\) is a unit. Every cross comparison reduces
to

\[
\gcd(yh_1-h_2,N)
=\gcd(yh_1h_2^{-1}-1,N),\qquad h_1,h_2\in H.
\]

As \(h_1h_2^{-1}\) ranges over \(H\), only \(|H|\le\ell\) distinct gcd
tests are needed. If \(\ell\) is numerically polynomial in \(\log N\), this
update is polynomial-time. The proof uses the semiprime CRT structure and
does not extend to arbitrary \(N\).

## 3. Fresh-row obstruction

If \(r\in F\), then exactness gives \(\alpha_{rj}=0\) for every old
\(q_j\). Row \(r\) of \(D\), hence row \(r\) of \(A'=DA\), is zero.
Every vector in \(\operatorname{colspan}(A')\) is therefore zero on \(F\).
A new column with a nonzero residue on a fresh row is nonclosing. An integer
entry equal to one stays nonzero for every prime \(\ell\).

For canonical-inverse feedback, \(gw=1+kN\) is a known relation modulo
\(N\). If refinement exposes a cofactor block of \(w\) that is absent from
all old rows and occurs in this relation with exponent one, its row is fresh
and the column is nonclosing for every \(\ell\) on that step. This is only a
span obstruction. It says nothing about a direct gcd, a power or mixed-word
decoder, multiplicity loss elsewhere, or closure after later block reuse.

## 4. Private columns do not amortize

Let \(M=[M_0\mid u_1\mid\cdots\mid u_M]\), and suppose
\(M(x,a_1,\ldots,a_M)=0\). If some \(a_i\ne0\), choose the largest such
index \(i\). At row \(r_i\), the contribution from \(M_0x\) is zero. The
contributions from \(u_j\), \(j<i\), are zero at that row, and those from
\(j>i\) vanish because \(a_j=0\). The row equation becomes

\[
a_i(u_i)_{r_i}=0,
\]

contradicting both factors being nonzero. Hence every \(a_i=0\), after
which \(M_0x=0\). The reverse inclusion is immediate, so

\[
\ker M=\ker(M_0)\times\{0\}^M.
\]

An exponent-one private block supplies this witness for every prime. Under
later exact refinement, its descendant rows remain absent from \(M_0\) and
the earlier columns. The witness survives if at least one descendant
exponent is nonzero modulo \(\ell\). It can disappear only if all those
exponents vanish modulo \(\ell\), exactly Claim 1's multiplicity gate.
Appending a later column that reuses the block is instead a new
column-closure question.

## 5. Full-group source event

Let \(\langle B\rangle\) be the residue subgroup generated by the current
unit blocks. Exact representations of the retained raw units give

\[
\langle a_1,\ldots,a_d\rangle\subseteq\langle B\rangle.
\]

On the source event, the left side is \(G_N\). Since every member of \(B\)
is a unit modulo \(N\), the reverse containment is automatic. Thus

\[
G_N\subseteq\langle B\rangle\subseteq G_N,\qquad
\langle B\rangle=G_N.
\]

Any no-factor exact refinement that retains the representations preserves
this equality. Feedback cannot enlarge a subgroup that is already the full
unit group. It can name new integer blocks and record relations. The
existential equality \(\langle B\rangle=G_N\) does not provide the complete
relation lattice or compute an exponent word for a new block.

## 6. Bit complexity and deletion scope

Let \(S\) be the total binary size of the explicit maintained state,
including dimensions, integer exponent entries, block values, relation
columns, scanned-prime encodings, and any materialized decoder menu.

Matrix lifting uses polynomially many integer operations on operands whose
bit lengths are in \(S\). Output entry lengths grow by the operand lengths
and a logarithmic dimension term. Reduction modulo \(\ell\), Gaussian
elimination, kernel-basis updates, rank updates, and span tests use
polynomially many field operations in the matrix dimensions. Each field
operation has bit cost polynomial in \(\log\ell\). Root construction uses
integer exponent arithmetic, modular exponentiation, and gcd, all
polynomial in the explicit exponent lengths and \(\log N\).

A materialized menu of \(P\) candidates costs
\(P\,\operatorname{poly}(S+\log N)\) to process. This is polynomial in
explicit state size when the menu is counted in \(S\), or when promotion
enforces \(P\le\operatorname{poly}(S+\log N)\). Binary input of \(\ell\)
has length \(O(\log\ell)\), but enumerating an \(\ell\)-element coset takes
\(\Omega(\ell)\) time. Therefore an \(O(\ell)\) decoder is not polynomial
in \(\log\ell\) for unrestricted \(\ell\).

To obtain runtime polynomial in \(\log N\), one needs explicit polynomial
bounds on total retained presentation size, relation count and bit lengths,
the count and numerical sizes of promoted primes, total menu size, and
feedback steps. Per-state polynomiality does not itself prove a polynomial
state cap. A kernel basis has polynomial size and is computable by
elimination. The algorithm must retain such a basis, or an explicitly
capped promoted menu. Enumerating all \(\ell^{\dim\ker A}\) vectors is not
polynomial in the presentation size in general.

For the deletion example, use one row over \(\mathbb F_2\). Against the
empty one-row matrix, the first column \([1]\) is nonclosing, and \([1]\)
has zero kernel. A second \([1]\) lies in the first column's span, and

\[
\ker[1\mid1]=\langle(1,1)\rangle.
\]

Deleting the first column leaves \([1]\) and destroys that dependency. This
shows only that deletion can discard information needed for later closure.
It does not show that the dependency gives a non-global root or factors
\(N\).

## Exact algorithmic scope

The proved result is exact accounting for an explicit known presentation.
It determines when refinement or one appended relation enlarges a modular
kernel, when fresh or private rows obstruct closure, what subgroup equality
holds on the conditional full-generator event, and which explicit state
parameters control the work.

It proves no all-input source law, polynomial state cap, unconditional bound
on feedback or prime scanning, distinct or non-global root, factoring
algorithm, successful gcd, or computational lower bound.

Subject to this exact scope, the strict verdict is **PASS**.
