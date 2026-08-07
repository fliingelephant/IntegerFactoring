# F68 hostile audit — root-labelled feedback closure

## Verdict: PASS

The audited candidate has SHA-256
87738f81027c00ded3e4861550b0de8faffa8fbc5787751780a406773d631328.

Every mathematical claim in the candidate is correct under its stated
hypotheses. In particular, the inference from failed old basis screens is
valid for every odd \(N>1\), including nonsquarefree \(N\). The one-new-root
test is an if-and-only-if test only after the old basis has been screened and
only because every relation value is \(1\) modulo \(N\).

This verdict covers the theorem, proofs, scope claims, and finite witnesses.
It does not certify the historical descriptions of P66 and P73, the
provenance statement that no computation was run, or the project-status word
“unresolved.” Those claims are not derivable from the pinned candidate
alone, and none is used as evidence here.

The exact scope is:

- relation values are positive exact integers and satisfy
  \(A_i\equiv1\pmod N\);
- complete exact refinement represents their rational square classes;
- every appended relation gets a separate coordinate only if it is actually
  appended as a separate indexed value;
- roots are the unique positive roots of exact integer squares, not arbitrary
  modular square roots;
- “canonical quotient label” means a well-defined coset, not a preferred
  representative of that coset;
- “the decoder finds a factor” refers to the two sign gcd screens applied to
  these exact-root labels. It does not include unrelated factoring routes.

## 1. Exact square relations

Complete gcd-free refinement can be written as

\[
A_i=T_i^2\prod_{j=1}^r Q_j^{e_{ji}},
\]

where the retained \(Q_j\) are positive, pairwise coprime, and nonsquare.
Their rational square classes are independent. If a nonempty product of
distinct \(Q_j\)'s were a rational square, it would be an integer square.
Choose a selected \(Q_j\). It has a prime of odd valuation, and pairwise
coprimality prevents every other selected block from containing that prime.
The full product would therefore have an odd prime valuation, a
contradiction. This argument allows composite blocks and prime-power blocks.

It follows that for \(x\in\mathbb F_2^m\),

\[
Mx=0
\quad\Longleftrightarrow\quad
Q(x)=\prod_i A_i^{x_i}
\text{ is an exact rational square}.
\]

A positive integer that is a rational square is an integer square: after a
rational square root is put in lowest terms, its denominator must be one.
Thus \(R(x)=\sqrt{Q(x)}\) is a unique positive integer. Exact exponent data,
including data for omitted square blocks, determines this root. The matrix is
not merely certifying a modular square.

This proves that \(K=\ker M\) is exactly the indexed subset-square space.
Joint exact refinement changes the coordinates but not the values \(A_i\),
so it preserves this intrinsic kernel.

## 2. The positive-root map really is a homomorphism

For \(x,y\in K\), let

\[
I(x,y)=\{i:x_i=y_i=1\}.
\]

Binary addition cancels precisely these repeated indices, giving the exact
identity

\[
Q(x)Q(y)
=Q(x+y)\left(\prod_{i\in I(x,y)}A_i\right)^2.
\]

All quantities are positive. Taking the unique positive square root therefore
introduces no sign ambiguity:

\[
R(x)R(y)
=R(x+y)\prod_{i\in I(x,y)}A_i.
\]

Every overlap factor is \(1\) modulo \(N\), so reduction modulo \(N\) gives

\[
\psi(x)\psi(y)=\psi(x+y).
\]

Also \(\psi(x)^2\equiv Q(x)\equiv1\pmod N\), which makes \(\psi(x)\) a unit
in \(\mu_2(N)\). Hence \(\psi:K\to\mu_2(N)\) is a group homomorphism and
\(H=\psi(K)\) is a subgroup.

The congruence \(A_i\equiv1\pmod N\) is essential. For example, if \(N=5\)
and the sole indexed value is \(A_1=4\equiv-1\pmod5\), its column is zero
and \(e_1\in K\), but

\[
\psi(e_1)^2=2^2\equiv-1\not\equiv1=\psi(0).
\]

Thus the same positive-root construction would not be a homomorphism under a
weaker hypothesis that allowed arbitrary unit relation values. This does not
refute the candidate because the candidate explicitly requires residue one.

## 3. The new kernel is exactly the claimed direct sum

After joint refinement, a vector \((x,\epsilon)\) is in the new kernel
exactly when

\[
Mx+\epsilon b=0.
\]

When \(\epsilon=0\), this says \(x\in K\). When \(\epsilon=1\), it says
\(Mx=b\). Therefore, if \(b\notin\operatorname{colspan}(M)\), no kernel
vector uses the new index and

\[
K'=K\times\{0\}.
\]

This means there is no new dependency direction; it does not say that the
old kernel is zero.

If \(Mc=b\), every last-coordinate-one vector is uniquely of the form

\[
(c+k,1)=(c,1)+(k,0),\qquad k\in K.
\]

The vector \(z_c=(c,1)\) cannot lie in \(K\times\{0\}\), because its last
coordinate is one. Hence

\[
K'=(K\times\{0\})\oplus\langle z_c\rangle.
\]

Thus a closure adds exactly one indexed dependency dimension, even when old
dependencies already exist.

Applying the already-proved positive-root homomorphism to this direct-sum
basis gives

\[
H'=\langle H,s_c\rangle.
\]

No dependency root is omitted by this image formula.

## 4. Lift dependence is exactly modulo the old image

Let \(c'\) be another solution of \(Mc'=b\). Then
\(k=c'+c\in K\) and

\[
z_{c'}=z_c+(k,0).
\]

The new root homomorphism gives

\[
s_{c'}=s_c\,\psi(k).
\]

Therefore \(s_{c'}H=s_cH\). The literal residue \(s_c\) need not be
lift-independent.

A sharp boundary example is \(N=15\), old value \(A_1=16\), and appended
value \(A_2=1\). Both values are \(1\) modulo \(15\), and both parity columns
are zero. The old kernel is generated by \(e_1\), with

\[
\psi(e_1)=\sqrt{16}=4\pmod{15},
\qquad H=\{1,4\}.
\]

For the new zero column, \(c=0\) gives \(s_c=1\), while \(c'=e_1\) gives
\(s_{c'}=4\). These are different roots but the same coset modulo \(H\).
They are not the same coset modulo the global-sign group
\(G=\{1,14\}\). Thus before an unsuccessful old decode, invariance modulo
\(G\) would be false. The candidate correctly claims invariance only modulo
\(H\) at this stage.

## 5. Failed basis screens imply \(H\subseteq\{1,-1\}\)

This is the main possible nonsquarefree failure point, but the inference is
valid.

Let \(r\in\mu_2(N)\), and define

\[
d_-=\gcd(r-1,N),\qquad d_+=\gcd(r+1,N).
\]

Since \(N\) is odd,

\[
\gcd(d_-,d_+)=1,
\]

because a common divisor divides both \(r-1\) and \(r+1\), hence divides
\(2\). Now fix any full prime power \(p^a\mid N\). From
\(r^2\equiv1\pmod{p^a}\), the product \((r-1)(r+1)\) is divisible by
\(p^a\). The odd prime \(p\) cannot divide both adjacent factors. Therefore
the entire \(p^a\) divides one of them. This proves

\[
d_-d_+=N
\]

without assuming that \(N\) is squarefree.

If \(r\) is not congruent to either global sign, neither \(d_-\) nor \(d_+\)
equals \(N\). Their product is \(N>1\), so both are strictly between \(1\)
and \(N\). Both screens return proper factors. Conversely, if neither screen
returns a proper factor, the coprime product identity forces

\[
(d_-,d_+)=(N,1)\quad\text{or}\quad(1,N),
\]

which is equivalent to \(r\equiv1\pmod N\) or
\(r\equiv-1\pmod N\).

For example, the nonsquarefree modulus \(N=45\) and root \(r=19\) satisfy

\[
19^2=361\equiv1\pmod{45},\qquad
\gcd(18,45)=9,\qquad \gcd(20,45)=5.
\]

The repeated prime power \(3^2\) goes wholly to the first screen.

Let \(k_1,\ldots,k_d\) be the screened old basis. Failure of both screens on
each \(\psi(k_j)\) therefore implies

\[
\psi(k_j)\in G=\{1,-1\}.
\]

Since \(\psi\) is a homomorphism and \(G\) is a subgroup, every product of
basis images also lies in \(G\). Hence

\[
H=\psi(K)\subseteq G.
\]

Screening only basis roots is complete here. Products of global signs cannot
hide a non-global root.

## 6. The one-new-root test is an if-and-only-if test

Assume the old basis screens failed, so \(H\subseteq G\).

If the append does not close, \(K'=K\times\{0\}\). There is no new root
label to test, and the already-screened image remains \(H\).

If the append closes, choose any one solution \(Mc=b\). The image is

\[
H'=\langle H,s_c\rangle.
\]

There are two exhaustive cases.

- If \(s_c\in G\), then \(H'\subseteq G\). Every old or new dependency has a
  global root, so no sign screen from the enlarged kernel can return a
  proper factor.
- If \(s_c\notin G\), the closure vector itself has a non-global root. The
  product identity \(d_-d_+=N\) from the previous section shows that its two
  sign gcds are proper factors.

Changing the lift multiplies \(s_c\) by an element of
\(H\subseteq G\). Multiplication by \(-1\) only swaps the two sign screens,
and it does not change global versus non-global status. Consequently

\[
\text{the enlarged decoder has a factor-bearing root}
\quad\Longleftrightarrow\quad
s_c\notin G,
\]

and one newly induced root test is complete. The implication would not hold
without the failed-old-screen premise, as the \(N=15\) lift example shows:
there \(H\) already contains a non-global root.

## 7. Indexed semantics and the finite witnesses

The vector spaces use one coordinate per appended index, not one coordinate
per distinct integer value.

For \(N=21\), two separately appended copies of \(22\) have equal parity
columns. The vector selecting both indices is an exact dependency because

\[
22\cdot22=22^2.
\]

Its positive root is \(22\equiv1\pmod{21}\), so the closure is real but its
root is global. If the second \(22\) were deduplicated instead of appended,
there would be no second coordinate, no new column, and no new dependency
dimension.

For \(N=55\),

\[
21^2=441\equiv1\pmod{55}
\]

is an exact square, so its parity column is zero. The lift \(c=0\) gives the
singleton dependency with exact positive root \(21\), and

\[
\gcd(21-1,55)=5,\qquad \gcd(21+1,55)=11.
\]

This is a useful zero-column closure. A zero column adds one indexed
dependency even if the old kernel is nonzero.

The general \(N+1\) duplicate boundary is also valid. Two indexed copies
have a closure whose exact positive root is \(N+1\equiv1\pmod N\), whether
or not \(N+1\) itself already has zero square class. Thus square-class
closure alone does not imply usefulness.

## 8. Final scope assessment

The two gates are genuinely distinct:

1. \(b\in\operatorname{colspan}(M)\) decides whether a new indexed square
   dependency exists.
2. After failed old basis screens, \(s_c\notin G\) decides whether the one
   new dependency coset contains factor-bearing roots.

The proof gives exact incremental accounting. It does not give a selector,
a success probability, a runtime distribution, or a factoring algorithm
that produces useful feedback additions. The candidate states these
limitations correctly.
