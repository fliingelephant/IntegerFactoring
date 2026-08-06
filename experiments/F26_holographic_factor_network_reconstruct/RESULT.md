# Proof-blind reconstruction: exact multiplication-network contraction and the common-basis obstruction

**Status: RECONSTRUCTED.**

This is a from-scratch reconstruction of exactly the two requested claims. Part A is a conditional reduction: it does **not** construct the assumed contraction algorithm. Part B is an unconditional obstruction to one precisely defined holographic route. Consequently this package is not, by itself, an unconditional solution of integer factoring.

No finite experiment or symbolic-computation run is used. The only external matchgate input is the standard arity-at-most-three characterization stated in Section 4; its low-arity specialization is also derived there.

## 1. The Boolean multiplication-witness network

Let \(N>1\), and put

\[
n=\lceil\log _2(N+1)\rceil,
\qquad
m=2^{\lceil\log _2 n\rceil}.
\]

Thus \(n\le m<2n\), and \(m\ge2\). Represent each factor by \(m\) little-endian bits,

\[
x=\sum_{i=0}^{m-1}x_i2^i,
\qquad
y=\sum_{j=0}^{m-1}y_j2^j,
\]

and pin every bit with index at least \(n\) to zero. Use the following \(0/1\)-valued tensors:

* the unary free tensor \(F=(1,1)\) and pins \(P_b(t)=\mathbf 1[t=b]\);
* the equality tensors
  \[
  \operatorname{COPY}_k(t_1,\ldots,t_k)
  =\mathbf 1[t_1=\cdots=t_k];
  \]
* the ternary multiplication-cell tensor
  \[
  \operatorname{AND}_3(u,v,w)=\mathbf 1[w=u\wedge v];
  \]
* the five-leg full-adder relation
  \[
  \operatorname{FA}(a,b,c;s,d)=\mathbf 1[a+b+c=s+2d].
  \]

All indices are Boolean.

### 1.1 Exact padded fanout

For each \(x_i\), make a complete rooted binary tree with \(m\) leaf edges. Every internal vertex is a ternary COPY tensor: one parent leg and two child legs. Since \(m\) is a power of two, the tree has exactly \(m-1\) COPY3 vertices and no uneven final level. Subdivide every edge between two COPY3 vertices by an arity-two identity tensor

\[
I_2(a,b)=\mathbf 1[a=b].
\]

Attach \(F\), \(P_0\), or a requested prefix pin to the root leg. Bijection the \(m\) leaf edges with \(j=0,\ldots,m-1\), and attach leaf \(j\) **directly** to the first input of \(\operatorname{AND}_{ij}\). Construct the analogous tree for each \(y_j\), with leaves indexed by \(i\), and attach them directly to the second inputs of the same AND tensors. Thus there are exactly \(m^2\) multiplication ANDs and there are no dummy fanout leaves. The padded factor bits merely make the corresponding genuine AND outputs zero.

For a fixed root value \(b\), contraction of one such tree is exactly

\[
\prod_{\ell=1}^{m}\mathbf 1[z_\ell=b].
\]

Indeed, if all leaves equal \(b\), every internal index has one forced value; otherwise no internal assignment survives. Hence the tree introduces neither lost assignments nor a multiplicity factor. Contracting a free root sums once over \(b=0,1\), while a pin selects exactly one value.

### 1.2 A polynomial-size exact product checker

Write the output of \(\operatorname{AND}_{ij}\) as \(p_{ij}\). A deterministic ripple network adds the \(m\) shifted rows. Let \(A^0_k=0\) for \(0\le k<2m\). At stage \(i\), define

\[
R^i_k=
\begin{cases}
p_{i,k-i},&0\le k-i<m,\\
0,&\text{otherwise},
\end{cases}
\]

and impose, for \(0\le k<2m\),

\[
A^i_k+R^i_k+c^i_k=A^{i+1}_k+2c^i_{k+1},
\qquad
c^i_0=c^i_{2m}=0.
\]

These are \(2m^2\) constant-size full-adder tensors. Finally pin \(A^m_0,\ldots,A^m_{2m-1}\) to the \(2m\)-bit expansion of \(N\). For genuine partial products, every prefix row sum is at most \(xy<2^{2m}\), so the terminal-carry pin is correct. The ripple equations have a unique assignment of all sum and carry bits for every fixed collection of partial products.

Every ordinary circuit wire is represented by a degree-two equality tensor. Constants and final checks are unary constraint tensors. The complete tensor graph can therefore be made genuinely bipartite as follows:

* the primal side contains all fanout COPY3 vertices and all ordinary degree-two wire-variable tensors;
* the constraint side contains AND3, FA, pins/free tensors, and the identity tensors that subdivide parent-child edges inside the fanout trees.

Every edge joins the two sides. In particular, every bottom-level COPY3 vertex has its parent leg adjacent to a constraint-side identity tensor and both child legs directly adjacent to AND inputs. This subdivision changes neither the contracted value nor the unique-extension property.

### 1.3 Exact count and uniform size

Given \(x,y\), all COPY-tree indices, AND outputs, accumulator bits, and carries are forced. Conversely, every nonzero summand satisfies the COPY equalities, \(p_{ij}=x_i y_j\), the exact additions, and the final product pins. Therefore the contraction of the unpinned network is exactly

\[
Z_N(\varnothing)
=\#\{(x,y):0\le x,y<2^n,\ xy=N\}.
\]

If \(p\) is a prefix in any fixed ordering of the \(n\) bits of \(x\) (take most-significant first below), replacing the corresponding root free tensors by pins gives exactly

\[
Z_N(p)
=\#\{(x,y):0\le x,y<2^n,\ xy=N,\ p\preceq\operatorname{bin}_n(x)\}.
\]

Since \(N>0\), no counted factor is zero. Since every positive divisor of \(N\) is at most \(N<2^n\), this counts every ordered factor witness and no truncated witness. For each admitted \(x\), \(y=N/x\) is unique.

The construction has \(m^2\) AND tensors, \(2m(m-1)\) fanout COPY3 tensors, \(O(m^2)\) identity/wire tensors, and \(2m^2\) full adders. Its number of constant-size tensor entries is \(O(m^2)=O(n^2)\); an explicit indexed wiring description uses \(O(n^2\log n)\) bits and is constructible in that many bit operations. Every contraction is at most the number \(2^n\) of possible \(x\)'s, so its exact output has \(O(n)\) bits.

## 2. Exact contraction implies complete deterministic factoring

Assume there is one uniform deterministic algorithm \(\mathcal C\) and one fixed polynomial \(P\) such that, for every network in Section 1 and every \(x\)-prefix-pinned version, \(\mathcal C\) returns its exact integer contraction in at most \(P(L)\) bit operations, where \(L\) is the explicit network-description length. This is the precise “uniform exact polynomial-bit contraction” hypothesis.

For a word \(p\), let \(p\preceq w\) mean that \(p\) is a prefix of \(w\), and define

\[
E_N(p)
=\mathbf 1[p\preceq\operatorname{bin}_n(1)]
 +\mathbf 1[p\preceq\operatorname{bin}_n(N)],
\qquad
R_N(p)=Z_N(p)-E_N(p).
\]

The two subtracted witnesses are distinct because \(N>1\). They are public and require no unknown arithmetic information. Since \(y\) is unique for each \(x\),

\[
R_N(p)
=\#\{x:1<x<N,\ x\mid N,\ p\preceq\operatorname{bin}_n(x)\}.
\tag{1}
\]

In particular, \(R_N(\varnothing)>0\) exactly when \(N\) is composite.

### 2.1 Exact count self-reduction

Use an unconditional deterministic polynomial-time primality test at every recursive node. A prime node is returned as a leaf. If a composite node \(M>2\) is even, split it directly as \(2\cdot(M/2)\). It remains to split an odd composite \(M\).

Start with the empty prefix \(p\), for which (1) is positive. At the next bit, compute

\[
R_M(p0)=Z_M(p0)-E_M(p0)
\]

using one exact contraction. If it is positive, replace \(p\) by \(p0\); otherwise replace \(p\) by \(p1\). The invariant \(R_M(p)>0\) is preserved because

\[
R_M(p)=R_M(p0)+R_M(p1).
\]

After \(k=\lceil\log_2(M+1)\rceil\) steps, the full word encodes an integer \(d\) with \(1<d<M\) and \(d\mid M\). Verify these inequalities and compute the exact remainder of \(M\) on division by \(d\); accept the split only when the remainder is zero, then set \(e=M/d\). Under the exact-contraction hypothesis the verification always succeeds. The extracted integer is already a divisor: there is no terminal factor-extracting gcd.

Recursively apply the same procedure to \(d\) and \(e\), merge equal prime leaves into exponents, deterministically recheck primality of the leaves, and verify that their powered product is the original input. This handles arbitrary unbalanced composites, prime powers, repeated prime factors, and even inputs.

### 2.2 Bit complexity of the complete recursion

At a \(k\)-bit odd composite node, self-reduction makes at most \(k\) contraction calls on descriptions of length

\[
L(k)=O(k^2\log k).
\]

All count subtractions involve \(O(k)\)-bit nonnegative integers. Exact division, remainder, split verification, and network construction have polynomial bit complexity.

If the complete factorization has \(r\) prime leaves counted with multiplicity, then \(2^r\le N\), so \(r\le\log_2N=O(n)\). The binary recursion tree has at most \(2r-1=O(n)\) nodes. Crude domination of every node size by \(n\) therefore gives at most \(O(n^2)\) contraction calls, each costing

\[
P(O(n^2\log n)),
\]

plus \(O(n)\) invocations of deterministic polynomial-bit primality testing and polynomially many ordinary arithmetic operations on at most \(n\)-bit node values. This is one fixed deterministic polynomial in \(n\). Thus the assumed contraction algorithm implies complete deterministic polynomial-time factorization of every \(N>1\).

## 3. Classification of common bases that make COPY3 a matchgate

All holographic algebra below is over \(\mathbb C\); proving impossibility over this permissive field also proves it over any subfield. Fix the convention that a primal tensor is acted on by \(T\) on each incident leg. On an adjacent tensor the contraction-preserving action is

\[
S=(T^{-1})^{\mathsf T},
\]

because contraction of \(T\) with \((T^{-1})^{\mathsf T}\) on their common index is the identity.

Write

\[
T=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]

The transformed COPY3 tensor is

\[
(T^{\otimes3})(|000\rangle+|111\rangle).
\]

Every coordinate of Hamming weight \(j\) equals

\[
a^{3-j}c^j+b^{3-j}d^j.
\tag{2}
\]

For arity three, matchgate-realizability is exactly parity-purity. Therefore an invertible \(T\) is admissible precisely in one of the following two cases.

### 3.1 Even transformed COPY

The weight-one and weight-three coordinates in (2) vanish:

\[
a^2c+b^2d=0,
\qquad
c^3+d^3=0.
\tag{3}
\]

If \(c=0\), the second equation gives \(d=0\), contradicting invertibility; if \(d=0\), it similarly gives \(c=0\). Thus \(c,d\ne0\). If \(b=0\), the first equation then gives \(a=0\); if \(a=0\), it gives \(b=0\). Both branches are singular, so \(a,b\ne0\). Set \(\zeta=d/c\). Then

\[
\zeta^3=-1,
\qquad
(a/b)^2=-\zeta.
\]

Because \((\zeta^{-1})^2=-\zeta\), one has \(a/b=\pm\zeta^{-1}\). The plus sign makes \(ad-bc=0\), while the minus sign gives a nonzero determinant. Hence all and only the invertible even solutions are

\[
T_E(\zeta;u,v)
=\begin{pmatrix}
-u\zeta^{-1}&u\\
v&v\zeta
\end{pmatrix},
\qquad
\zeta^3=-1,\quad u,v\in\mathbb C^*.
\tag{4}
\]

Their determinant is \(-2uv\).

### 3.2 Odd transformed COPY

Now the weight-zero and weight-two coordinates vanish:

\[
a^3+b^3=0,
\qquad
ac^2+bd^2=0.
\tag{5}
\]

The first equation and invertibility force \(a,b\ne0\); the second then forces \(c,d\ne0\). With \(\zeta=b/a\) and \(q=c/d\), equations (5) give

\[
\zeta^3=-1,
\qquad
q^2=-\zeta.
\]

Thus \(q=\pm\zeta^{-1}\). The plus sign is singular and the minus sign is invertible. All and only the odd solutions are

\[
T_O(\zeta;u,v)
=\begin{pmatrix}
u&u\zeta\\
-v\zeta^{-1}&v
\end{pmatrix},
\qquad
\zeta^3=-1,\quad u,v\in\mathbb C^*,
\tag{6}
\]

with determinant \(2uv\).

Equations (4) and (6) include all three cube-root choices and all independent nonzero row scalings. The zero-coordinate branches omitted by taking ratios were explicitly eliminated above as singular, so there is no additional invertible family.

The corresponding dual input actions have the useful common form

\[
(T_E^{-1})^{\mathsf T}
=D\,P(\zeta),
\qquad
(T_O^{-1})^{\mathsf T}
=D\,X P(\zeta),
\tag{7}
\]

where \(D\) is an invertible diagonal matrix,

\[
P(\zeta)=
\begin{pmatrix}-\zeta&1\\1&\zeta^{-1}\end{pmatrix},
\qquad
X=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Thus changing the COPY parity only swaps the two transformed coordinates, up to nonzero coordinate scalings.

## 4. The only matchgate fact used

Cai and Gorenstein prove that the matchgate identities characterize planar matchgate signatures and that those identities imply the parity condition; see [J.-Y. Cai and A. Gorenstein, *Matchgates Revisited*, Theory of Computing 10 (2014), Article 7](https://theoryofcomputing.org/articles/v010a007/) (especially Sections 2 and 5).

For completeness, when the arity \(k\le3\), parity is also sufficient. If a signature is supported on one parity and two MGI index words have opposite parity, every product in the identity contains a zero factor. If the index words have the same parity, their Hamming distance is at most two. Distance zero is vacuous; at distance two the two MGI products are the same two scalar factors in opposite order and cancel. Hence every parity-pure arity-at-most-three signature satisfies all MGI, and the cited characterization realizes it as a matchgate. Therefore, for the COPY3 and AND3 tensors used here,

\[
\text{matchgate}\quad\Longleftrightarrow\quad
\text{all nonzero coordinates have one Hamming parity}.
\tag{8}
\]

No higher-arity matchgate identity is used below.

## 5. The transformed AND pencil cannot have both parities

Permit independent common primal bases \(T_1,T_2\) for the \(x\)-role and \(y\)-role fanout COPY tensors. On the two directly adjacent AND input legs, contraction preservation forces

\[
S_1=(T_1^{-1})^{\mathsf T},
\qquad
S_2=(T_2^{-1})^{\mathsf T}.
\]

Permit an arbitrary invertible action \(U\in\operatorname{GL}_2(\mathbb C)\) on the AND output leg. This is at least as permissive as any action forced there by the rest of the network.

Use input bits as matrix row and column indices. The two output slices of AND are

\[
A_0=\begin{pmatrix}1&1\\1&0\end{pmatrix},
\qquad
A_1=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\tag{9}
\]

They are linearly independent. Hence, after invertible input transformations, every nonzero row \((\alpha,\beta)\) of \(U\) gives a nonzero member of the two-dimensional pencil generated by

\[
M(\alpha,\beta)=\alpha A_0+\beta A_1
=\begin{pmatrix}\alpha&\alpha\\\alpha&\beta\end{pmatrix}.
\tag{10}
\]

Nonzero diagonal coordinate scalings in (7) do not change which entries vanish. First suppress the possible row swaps \(X\), and write the two independent cube roots from \(T_1,T_2\) as \(r,s\), where

\[
r^3=s^3=-1.
\]

A direct multiplication gives

\[
P(r)M(\alpha,\beta)P(s)^{\mathsf T}
=\begin{pmatrix}
\alpha(rs-r-s)+\beta
&\dfrac{\alpha(s-r-rs)+\beta}{s}\\[6pt]
\dfrac{\alpha(r-s-rs)+\beta}{r}
&\dfrac{\alpha(rs+r+s)+\beta}{rs}
\end{pmatrix}.
\tag{11}
\]

All denominators are nonzero.

### 5.1 Every zero-coordinate case

If \(\alpha=0\), then \(\beta\ne0\) for a nonzero output row, and all four numerators in (11) equal \(\beta\). Such a pencil member is neither diagonal nor anti-diagonal.

Suppose \(\alpha\ne0\) and set \(\lambda=\beta/\alpha\).

For (11) to be diagonal, its off-diagonal entries must vanish:

\[
\lambda+s-r-rs=0,
\qquad
\lambda+r-s-rs=0.
\tag{12}
\]

Subtracting gives \(2(s-r)=0\), so \(s=r\), and then \(\lambda=r^2\). This does yield a nonzero diagonal pencil member; it cannot be the zero matrix because (10) is nonzero and all transformations are invertible.

For (11) to be anti-diagonal, its diagonal entries must vanish:

\[
\lambda+rs-r-s=0,
\qquad
\lambda+rs+r+s=0.
\tag{13}
\]

Subtracting gives \(2(r+s)=0\), so \(s=-r\). But then \(s^3=-r^3=1\), contradicting \(s^3=-1\). Thus there is no nonzero anti-diagonal member for any cube-root choices. The cases \(\beta=0\) are already included in \(\lambda=0\), and the case \(\alpha=\beta=0\) is not a row of an invertible output action.

Restoring the COPY parity choices applies a row swap on the first input and/or a column swap on the second. Zero or two swaps preserve the diagonal and anti-diagonal subspaces; exactly one swap exchanges them. Consequently the transformed AND pencil has the following complete alternatives:

* if \(r=s\), it intersects exactly one of the diagonal/anti-diagonal subspaces nontrivially, depending on the parity of the number of swaps;
* if \(r\ne s\), it intersects neither subspace nontrivially.

It never has one nonzero member of each kind.

### 5.2 Parity contradiction for the whole AND tensor

For a parity-even ternary tensor, output slice zero must be diagonal and output slice one anti-diagonal. For a parity-odd tensor the two requirements are reversed. Since \(U\) is invertible, its two rows form a basis of the AND pencil; since (9) and the input actions are independent/invertible, neither resulting slice can be zero. By Section 5.1, the required one-diagonal/one-anti-diagonal basis does not exist. By (8), the transformed AND3 tensor is not a matchgate.

We have allowed, simultaneously:

* independent common bases \(T_1,T_2\) for the two copied input roles;
* either parity for each transformed COPY3;
* every nonzero scaling and every cube root in the complete COPY classification;
* the required transpose-dual actions on the adjacent AND inputs; and
* an arbitrary invertible AND-output action.

Therefore no contraction-preserving common holographic basis of this form makes all displayed fanout COPY3 tensors and multiplication AND3 tensors matchgates. The contradiction is local to any multiplication AND together with its two directly adjacent leaf-COPY roles; tensors farther downstream cannot repair it through an output basis, because that basis was already arbitrary.

## 6. Topology and exact scope

The input-side subgraph is explicit. Deleting AND output legs, contracting each padded fanout tree to one vertex, and suppressing the degree-two AND vertices produces \(K_{m,m}\). Thus for \(m\ge3\) it is nonplanar. This is a separate topological issue: the algebraic obstruction above does not assume planarity, and making individual signatures into matchgates would not alone establish an FKT contraction for an arbitrary nonplanar assembly.

The negative result is deliberately narrower than a contraction lower bound. It does not exclude edge-dependent or leg-dependent bases, block encodings of several Boolean wires, heterogeneous gadget replacements, a different exact multiplication network, planarization/crossover constructions, global cancellations that do not make each local tensor a matchgate, or any non-matchgate contraction algorithm. It also does not prove that exact contraction of these networks is hard. Part A states the precise consequence if a uniform exact polynomial-bit contraction algorithm is nevertheless found.

Finally, the reduction does not identify scalar carry as a sufficient state, does not invoke a tractable exact-CVP class, and does not evaluate a divisor-sum/metric oracle. Its sole hypothesis is the exact contraction algorithm it explicitly names, and the divisor is recovered by count self-reduction rather than by a terminal gcd or discriminant oracle.

## 7. Reconstruction verdict

Every requested component follows:

1. the padded COPY-tree realization has exact fanout, direct leaf-COPY/AND adjacency, polynomial description size, and exact witness-count preservation;
2. exact contractions of all \(x\)-prefix-pinned networks give a deterministic polynomial-bit self-reduction after subtracting the two public witnesses \(x=1,N\);
3. verification, deterministic primality handling, even inputs, recursion, repetitions, prime powers, and total bit complexity are explicit, with no terminal factor-extracting gcd;
4. the COPY basis classification includes both parities, every invertible scaling and cube-root choice, and all singular zero-coordinate branches are excluded explicitly;
5. the AND parity equations include arbitrary output action and every zero-coordinate case, and prove the common-basis obstruction; and
6. the topological and open-case scope is stated without claiming a general contraction lower bound.

Accordingly the bare theorem package is **RECONSTRUCTED**.
