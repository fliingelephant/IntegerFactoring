# Proof-blind reconstruction of the hidden-modulus relation-lattice theorem

## Independence and conventions

This report was derived from the supplied theorem statement. I did not inspect the candidate proof, either audit, or any prior reconstruction, and I used no computation. The permitted statements P19 and P30 were consulted only to fix surrounding terminology and scope; neither supplies any lemma used below.

Write

\[
K_m(A)=\{x\in\mathbb Z^d:Ax\in m\mathbb Z^t\},\qquad
s_r=\operatorname{rank}_{\mathbb F_r}(A\bmod r),
\]

where \(r\in\{p,q\}\), and put \(\rho=\operatorname{rank}_{\mathbb Q}A\). A determinant of a lower-dimensional lattice always means covolume in its real span. The determinant of the rank-zero lattice is \(1\).

Three qualifications are needed to make the bare statement literal.

1. A rank-\(\rho\) determinant root is defined only when \(\rho>0\). If \(A=0\), then \(\rho=0\), all the determinant identities still hold with the rank-zero determinant convention, but the expressions \(r^{u/\rho}\) are undefined and must be omitted.
2. In the graph lattice, \(a,b\ne0\); for the displayed unsigned formula one normally assumes \(a,b>0\). With signed weights the determinant is \( |a|^d|bN|^t\). Algorithmic claims require rational weights and all dimensions and encodings to be of polynomial size.
3. “Open” below means “not excluded by this obstruction.” It is a scope statement, not a claim of a literature-wide impossibility result.

With these qualifications, every algebraic claim reconstructs.

## 1. Congruence kernels, indices, and rank mismatch

Reduction modulo \(r\) gives a homomorphism

\[
\phi_r:\mathbb Z^d\longrightarrow\mathbb F_r^t,
\qquad x\longmapsto Ax\bmod r.
\]

Its kernel is \(K_r(A)\), and its image has cardinality \(r^{s_r}\). The first isomorphism theorem therefore gives

\[
[\mathbb Z^d:K_r]=r^{s_r}.
\]

As \(K_r\) is a full-rank sublattice of the unimodular lattice \(\mathbb Z^d\),

\[
\det K_r=r^{s_r}.
\]

Because \(p\) and \(q\) are coprime,

\[
Ax\in pq\mathbb Z^t
\quad\Longleftrightarrow\quad
Ax\in p\mathbb Z^t\text{ and }Ax\in q\mathbb Z^t,
\]

so

\[
K_N=K_p\cap K_q.
\]

The Chinese remainder isomorphisms on source and target identify the image of \(A\bmod N\) with the product of the two local images. Consequently

\[
[\mathbb Z^d:K_N]
=|\operatorname{im}(A\bmod N)|
=p^{s_p}q^{s_q},
\]

and hence

\[
\det K_N=p^{s_p}q^{s_q}.
\]

For the factor extraction, let \(D_k(A)\) be the \(k\)-th integer determinantal divisor, the positive gcd of all \(k\times k\) minors. Suppose, without loss of generality, that \(s_p<s_q\), and take \(k=s_p+1\). Every \(k\times k\) minor vanishes modulo \(p\), while at least one such minor is nonzero modulo \(q\). Thus

\[
p\mid D_k(A),\qquad q\nmid D_k(A),
\]

and

\[
\gcd(N,D_k(A))=p.
\]

The argument also covers \(s_p=0\). The chosen nonzero minor modulo \(q\) guarantees \(k\le\rho\) and that \(D_k\ne0\). If the direction of the inequality is unknown, compute the Smith normal form, hence all nonzero \(D_k\), and test their gcds with \(N\); some test returns the proper factor. Enumerating all minors is unnecessary.

Finally, \(0\in K_p\cap K_q\), so \(0\notin K_p\mathbin\triangle K_q\). Hence the symmetric difference cannot be an additive subgroup, and therefore cannot be an additive lattice. This remains true when the symmetric difference is empty (which here can happen when both local ranks are zero), since the empty set is not a group.

## 2. The exact quotient determinant

Let

\[
K_0=\ker_{\mathbb Z}A,
\qquad V=\operatorname{span}_{\mathbb R}K_0=\ker_{\mathbb R}A.
\]

The equality of real spans follows because \(A\) is rational, so its rational nullspace has dimension \(d-\rho\) and contains an integral basis after clearing denominators. The quotient

\[
\mathbb Z^d/K_0\cong A\mathbb Z^d
\]

is torsion-free, since \(A\mathbb Z^d\) is a subgroup of the free abelian group \(\mathbb Z^t\). Thus \(K_0\) is primitive in \(\mathbb Z^d\).

Let \(\pi:\mathbb R^d\to V^\perp\) be orthogonal projection, and set \(\Delta_0=\det K_0\). More generally, for any full-rank lattice \(L\) with

\[
K_0\subseteq L\subseteq\mathbb Z^d,
\]

\(K_0\) is primitive in \(L\): if \(m x\in K_0\) for \(x\in L\) and nonzero integer \(m\), then \(mAx=0\), hence \(Ax=0\), so \(x\in K_0\). Extend a basis of \(K_0\) to a basis of \(L\). The volume of the resulting fundamental parallelepiped factors into the volume along \(V\) and the volume of the projected complementary vectors. Those projected vectors form a basis of \(\pi(L)\). Therefore

\[
\det L=\Delta_0\det\pi(L). \tag{2.1}
\]

For \(L=\mathbb Z^d\), (2.1) gives

\[
\det\pi(\mathbb Z^d)=\Delta_0^{-1}.
\]

For \(L=K_r\) and \(L=K_N\), it gives

\[
\det\pi(K_r)=\frac{r^{s_r}}{\Delta_0},
\qquad
\det\pi(K_N)=\frac{p^{s_p}q^{s_q}}{\Delta_0}. \tag{2.2}
\]

In particular, when \(s_p=s_q=u\) and \(\rho>0\), the determinant roots in the actual positive-definite quotient dimension \(\rho\) are

\[
\det\pi(K_p)^{1/\rho}
=p^{u/\rho}\Delta_0^{-1/\rho},
\]

\[
\det\pi(K_q)^{1/\rho}
=q^{u/\rho}\Delta_0^{-1/\rho},
\]

and

\[
\det\pi(K_N)^{1/\rho}
=N^{u/\rho}\Delta_0^{-1/\rho}.
\]

At any resulting coefficient dimension \(d\), exactly \(d-\rho\) coefficient directions are null directions, and at most four are positive metric directions; once the output rank saturates, further coefficient dimensions cannot become positive metric dimensions. After quotienting the nullspace, the determinant root is taken in dimension \(\rho\le4\), not in dimension \(d\). This rules out an alleged gain based only on replacing the exponent \(u/\rho\) by \(u/d\). It does not rule out an algorithm that faithfully transfers the problem to the fixed-rank quotient and uses its metric geometry; the factor \(\Delta_0^{-1/\rho}\) can also vary when the map itself changes with the samples.

If \(\rho=0\), then \(A=0\), \(K_0=K_p=K_q=K_N=\mathbb Z^d\), \(\Delta_0=1\), and \(\pi(\mathbb Z^d)\) is the rank-zero lattice of determinant \(1\). There is no determinant root to take.

## 3. Translation cannot create a one-local zero syndrome

To avoid confusing the target vector with the row count \(t\), call the target \(\tau\in\mathbb Z^d\). For any \(v\in K_N\), put \(e=\tau-v\). Since \(Av\equiv0\pmod p\) and modulo \(q\), pointwise

\[
Ae\equiv A\tau\pmod r\qquad(r=p,q).
\]

Therefore

\[
e\in K_r\quad\Longleftrightarrow\quad\tau\in K_r
\qquad(r=p,q). \tag{3.1}
\]

This remains true if \(v\) was selected as a function of \(\tau\), provided only that its output lies in \(K_N\).

Now take \(\tau\) uniformly modulo \(N\). Its reductions modulo \(p\) and modulo \(q\) are independent and uniform. Since the kernel of \(A:\mathbb F_r^d\to\mathbb F_r^t\) has relative size \(r^{-s_r}\),

\[
\Pr(\tau\in K_p)=p^{-s_p},
\qquad
\Pr(\tau\in K_q)=q^{-s_q}.
\]

The probability of exactly one local zero syndrome is consequently

\[
\boxed{
p^{-s_p}+q^{-s_q}-2p^{-s_p}q^{-s_q}
}. \tag{3.2}
\]

The degenerate cases are:

\[
\begin{array}{c|c}
(s_p,s_q)&\Pr(\text{exactly one})\\ \hline
(0,0)&0\\
(0,s_q),\ s_q>0&1-q^{-s_q}\\
(s_p,0),\ s_p>0&1-p^{-s_p}\\
s_p,s_q>0&p^{-s_p}+q^{-s_q}-2p^{-s_p}q^{-s_q}.
\end{array}
\]

No equality of the positive ranks is used in (3.2). If the ranks mismatch, the formula is still exact, although Section 1 already exposes a factor through a determinantal divisor.

## 4. Output and scaled-dual lattices

Define

\[
\Lambda_{\rm out}=A\mathbb Z^d+N\mathbb Z^t\subseteq\mathbb Z^t.
\]

Modulo \(N\), this lattice maps to \(\operatorname{im}(A\bmod N)\). Therefore

\[
[\mathbb Z^t:\Lambda_{\rm out}]
=\frac{N^t}{|\operatorname{im}(A\bmod N)|}
=p^{t-s_p}q^{t-s_q},
\]

so

\[
\det\Lambda_{\rm out}=p^{t-s_p}q^{t-s_q}. \tag{4.1}
\]

Use the standard dot-product dual

\[
K_N^*=\{y\in\mathbb R^d:\langle y,x\rangle\in\mathbb Z
\text{ for every }x\in K_N\}.
\]

For \(x\in K_N\), \(z\in\mathbb Z^d\), and \(w\in\mathbb Z^t\),

\[
\langle Nz+A^Tw,x\rangle
=N\langle z,x\rangle+\langle w,Ax\rangle\in N\mathbb Z.
\]

Hence

\[
N\mathbb Z^d+A^T\mathbb Z^t\subseteq NK_N^*. \tag{4.2}
\]

Both sides are full-rank integral lattices. The right side has determinant

\[
\det(NK_N^*)
=\frac{N^d}{\det K_N}
=p^{d-s_p}q^{d-s_q}. \tag{4.3}
\]

The left side, reduced modulo \(N\), is the image of \(A^T\bmod N\). By CRT that image has size \(p^{s_p}q^{s_q}\), because a matrix and its transpose have the same rank over each field. Thus the left side also has index, and determinant,

\[
\frac{N^d}{p^{s_p}q^{s_q}}
=p^{d-s_p}q^{d-s_q}. \tag{4.4}
\]

The inclusion (4.2) between lattices of equal determinant is equality:

\[
\boxed{NK_N^*=N\mathbb Z^d+A^T\mathbb Z^t}. \tag{4.5}
\]

This determinant-and-inclusion proof is valid for composite \(N\); it does not incorrectly invoke field orthogonal-complement identities over \(\mathbb Z/N\mathbb Z\).

Neither \(\Lambda_{\rm out}\) nor the scaled dual is a symmetric difference of local kernels. Likewise, a faithful metric decoder on the exact quotient of Section 2 is not the linear translation operation in (3.1). Hence the intersection/translation obstruction proves nothing against those approaches.

## 5. Hurwitz multiplication: SNF, handedness, principality, and minima

Let

\[
\mathcal H
=\mathbb Z^4\ \cup\ (\mathbb Z+\tfrac12)^4
\]

in the standard coordinates \(1,i,j,k\), with its usual multiplication. Its reduced norm is

\[
\operatorname{nrd}(x)=x\bar x
=x_0^2+x_1^2+x_2^2+x_3^2,
\]

and the Hurwitz length is \(\|x\|_{\mathcal H}=\sqrt{\operatorname{nrd}(x)}\). Fix any integral basis of \(\mathcal H\) when matrices and relative determinants are mentioned.

Let \(\alpha\in\mathcal H\) have reduced norm \(N=pq\), and let \(M_\alpha\) be the integral matrix of left multiplication \(L_\alpha:x\mapsto\alpha x\). Multiplicativity of the norm says that \(L_\alpha\) scales squared Euclidean length by \(N\), so

\[
|\det M_\alpha|=N^2. \tag{5.1}
\]

Conjugation preserves \(\mathcal H\), and

\[
L_\alpha L_{\bar\alpha}
=L_{\bar\alpha}L_\alpha
=N I.
\]

It follows that every Smith invariant factor of \(M_\alpha\) divides \(N\). For each prime \(r\mid N\), the sum of the \(r\)-adic valuations of the four invariant factors is \(2\), by (5.1), while each valuation is \(0\) or \(1\). Smith divisibility orders those valuations nondecreasingly, so for both \(p\) and \(q\) the valuation pattern is

\[
(0,0,1,1).
\]

As \(N\) is squarefree, there are no other prime valuations. Therefore

\[
\operatorname{SNF}(M_\alpha)=\operatorname{diag}(1,1,N,N). \tag{5.2}
\]

For \(r\in\{p,q\}\), put

\[
J_r=\{x\in\mathcal H:\alpha x\in r\mathcal H\}.
\]

This is a **right** ideal: if \(x\in J_r\) and \(h\in\mathcal H\), then

\[
\alpha(xh)=(\alpha x)h\in r\mathcal H.
\]

The reduction of (5.2) modulo \(r\) has rank \(2\), so

\[
[\mathcal H:J_r]=r^2. \tag{5.3}
\]

Here is a handed proof that this right ideal is principal. First, \(\mathcal H\) is norm-Euclidean in the needed sense. Given any real quaternion \(y\), round its four standard coordinates to nearest integers. The squared rounding error is at most \(1\). Equality can occur only when all four coordinate errors have absolute value \(1/2\); in that case \(y\) itself lies in the all-half-integral coset of \(\mathcal H\), so a Hurwitz integer has distance zero. Thus in every case there is \(q\in\mathcal H\) such that

\[
\operatorname{nrd}(y-q)<1. \tag{5.4}
\]

Choose a nonzero \(\delta\in J_r\) of least positive norm. For any \(x\in J_r\), apply (5.4) to \(\delta^{-1}x\), obtaining \(q\in\mathcal H\), and set

\[
w=x-\delta q
=\delta(\delta^{-1}x-q).
\]

Because \(J_r\) is a right ideal, \(w\in J_r\). If \(w\ne0\), multiplicativity and (5.4) give

\[
\operatorname{nrd}(w)
<\operatorname{nrd}(\delta),
\]

contradicting minimality. Hence \(x=\delta q\), for every \(x\in J_r\), and

\[
J_r=\delta\mathcal H. \tag{5.5}
\]

The placement of \(\delta\) on the left is essential: \(\delta\mathcal H\) is a principal right ideal. Since left multiplication by \(\delta\) has determinant \(\operatorname{nrd}(\delta)^2\), (5.3)--(5.5) imply

\[
\operatorname{nrd}(\delta)=r.
\]

Every nonzero Hurwitz integer has positive integral norm at least \(1\). Therefore every nonzero element \(\delta h\in J_r\) has norm at least \(r\), with equality for a unit \(h\). Thus

\[
\det_{\mathcal H}J_r=r^2,
\qquad
\lambda_1(J_r)=\sqrt r. \tag{5.6}
\]

For the global kernel,

\[
J_N=\{x\in\mathcal H:\alpha x\in N\mathcal H\}.
\]

Certainly \(\bar\alpha\mathcal H\subseteq J_N\), since \(\alpha\bar\alpha=N\). Conversely, if \(\alpha x=Nz\), multiplication on the left by \(\bar\alpha\) gives

\[
Nx=N\bar\alpha z,
\]

and torsion-freeness gives \(x=\bar\alpha z\). Hence

\[
J_N=\bar\alpha\mathcal H. \tag{5.7}
\]

Also \(p\mathcal H\cap q\mathcal H=N\mathcal H\) coordinatewise, so

\[
J_N=J_p\cap J_q. \tag{5.8}
\]

Equation (5.7) and \(\operatorname{nrd}(\bar\alpha)=N\) yield

\[
\det_{\mathcal H}J_N=N^2,
\qquad
\lambda_1(J_N)=\sqrt N. \tag{5.9}
\]

For an \(m\)-fold orthogonal direct sum, the determinants are \(r^{2m}\) and \(N^{2m}\) in ranks \(4m\). Their determinant roots are still

\[
(r^{2m})^{1/(4m)}=\sqrt r,
\qquad
(N^{2m})^{1/(4m)}=\sqrt N.
\]

Thus direct summation supplies no determinant-root amortization.

## 6. The graph lattice and the exact residual threshold

For \(x\in\mathbb Z^d\), \(z\in\mathbb Z^t\), and nonzero weights \(a,b\), define

\[
\Gamma_{a,b}
=\{(ax,\ b(Ax-Nz)):x\in\mathbb Z^d,z\in\mathbb Z^t\}.
\]

A basis matrix, with the \(x\)-columns first and the \(z\)-columns second, is

\[
B_{a,b}=
\begin{pmatrix}
aI_d&0\\
bA&-bNI_t
\end{pmatrix}.
\]

It is block triangular, so

\[
\det\Gamma_{a,b}
=|\det B_{a,b}|
=|a|^d|bN|^t.
\]

For positive weights this is exactly \(a^d(bN)^t\), independently of \(A\).

Now specialize to one Hurwitz block, \(A=M_\alpha\), and interpret the two four-dimensional blocks with the Hurwitz norm metric. For \(x,z\in\mathcal H\), the unwrapped residual is

\[
s=\alpha x-Nz
=\alpha(x-\bar\alpha z),
\]

so multiplicativity gives the exact identity

\[
\boxed{
\|s\|_{\mathcal H}^2
=N\|x-\bar\alpha z\|_{\mathcal H}^2
}. \tag{6.1}
\]

Consequently the squared product-metric norm of a graph vector is

\[
a^2\|x\|_{\mathcal H}^2
+b^2N\|x-\bar\alpha z\|_{\mathcal H}^2. \tag{6.2}
\]

Suppose \(x\in J_r\), where \(r=p\) or \(q\). Both \(\alpha x\) and \(Nz\) lie in \(r\mathcal H\), hence \(s\in r\mathcal H\). If \(s\ne0\), then

\[
\|s\|_{\mathcal H}
=r\|h\|_{\mathcal H}\ge r
\qquad(s=rh,\ h\in\mathcal H\setminus\{0\}).
\]

Therefore

\[
x\in J_r\text{ and }\|s\|_{\mathcal H}<r
\quad\Longrightarrow\quad
s=0
\quad\Longrightarrow\quad
x\in J_N. \tag{6.3}
\]

The strict inequality and the unshifted residual are essential. At residual length at least \(r\), or for an affine target that destroys membership of the residual in \(r\mathcal H\), (6.3) gives no conclusion. Nor does it optimize the weights in (6.2). Those metric and target choices remain outside this obstruction.

The relative lattice determinant in a fixed integral Hurwitz basis and the Hurwitz norm are distinct notions: the latter is represented by a fixed rational positive-definite Gram matrix in that basis. Equations (6.1)--(6.3) use the Hurwitz metric, while the block-triangular determinant calculation uses coordinate covolume (or, equivalently, covolume normalized relative to the fixed product lattice).

## 7. Exact Gram quotient, bit complexity, and scope

Let a fixed-output coefficient map be represented in a fixed basis by \(C\in\mathbb Q^{m\times d}\), and let \(Q\in\mathbb Q^{m\times m}\) be the positive-definite Gram matrix of the output metric. Its pullback Gram matrix is

\[
G=C^TQC.
\]

For every real coefficient vector \(y\),

\[
y^TGy=(Cy)^TQ(Cy).
\]

Positive definiteness of \(Q\) therefore gives

\[
\ker_{\mathbb Q}G=\ker_{\mathbb Q}C,
\qquad
\operatorname{rank}_{\mathbb Q}G
=\operatorname{rank}_{\mathbb Q}C.
\]

For one quaternion output, this rank is at most \(4\). The coefficient space thus has an exact rational nullspace; quotienting it out leaves a positive-definite space of dimension \(\rho\le4\), regardless of how many coefficient samples were introduced. This is the Gram-matrix version of Section 2.

All purely algebraic operations invoked above are polynomial in the total binary encoding of their inputs. In particular:

- ranks modulo a supplied prime, CRT reductions, and gcds have polynomial bit complexity;
- integer HNF and SNF, including recovery of determinantal divisors from Smith factors, have polynomial bit complexity;
- a Hurwitz multiplication matrix has constant dimension and \(O(\log N)\)-bit entries, since a norm-\(N\) quaternion has \(O(\log N)\)-bit coordinates in any fixed basis;
- graph matrices have polynomial encoding when \(d,t\), the entries of \(A\), and rational \(a,b\) have polynomial encoding;
- exact rational kernels, quotient Gram matrices, and LLL reductions have polynomial bit complexity in matrix dimension and input bit length.

These statements do not make \(p\) or \(q\) available to an algorithm; local objects indexed by an unknown factor are analytical objects unless the factor has already been recovered. Nor does polynomial-time LLL imply polynomial-time exact CVP. No polynomial bound for exact CVP in a dimension growing with the input is used here. If a construction keeps the faithful quotient dimension fixed, its possible metric decoder is expressly not refuted.

The proved obstruction has exactly two operative parts:

1. exact null directions cannot legitimately be counted as positive metric dimensions to dilute a determinant root; and
2. subtracting an element of \(K_N\) preserves, rather than separates, both local zero-syndrome events.

It does not obstruct \(\Lambda_{\rm out}\), \(NK_N^*\), a faithful fixed-rank quotient decoder, targets or weights beyond (6.3), or nonlinear invariants. It proves neither a factoring lower bound nor a factoring algorithm.

## Adversarial checklist and verdict

- **Projection index:** verified by the primitive-basis volume factorization (2.1), including the rank-zero determinant convention.
- **Composite scaled dual:** verified by inclusion plus equal determinant; no field argument over \(\mathbb Z/N\mathbb Z\) was used.
- **Handedness:** \(J_r\) is a right ideal and is generated as \(\delta\mathcal H\); the Euclidean division approximates \(\delta^{-1}x\), not \(x\delta^{-1}\).
- **Smith valuations:** each invariant divides squarefree \(N\), and each of \(p,q\) has the forced pattern \((0,0,1,1)\).
- **Minima:** principality plus the index forces generator norm \(r\); the global generator is \(\bar\alpha\) on the left.
- **Graph quantifiers:** the determinant needs nonzero weights, the unsigned display needs positive weights, and the residual conclusion needs an unshifted residual with strict length \(<r\).
- **Bit complexity:** polynomiality is in total explicit input size and assumes polynomial-size rational encodings; it neither reveals the local primes nor solves growing-dimensional exact CVP.

**Final status: RECONSTRUCTED WITH CORRECTIONS.** The corrected theorem above is independently reconstruction-backed. The theorem exactly as written is not yet verifier-backed because its \(\rho=0\) determinant-root expression is undefined and its graph/complexity hypotheses on \(a,b\) and their encodings are omitted. This report supplies only the proof-blind reconstruction half of the required verification cadence; the corrected same version is verifier-backed only if a separate hostile audit has also passed it.
