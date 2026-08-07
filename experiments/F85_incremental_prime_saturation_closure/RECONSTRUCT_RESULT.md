# PASS

The SHA-256 digest of the reconstruction statement is

~~~text
cd439393760f0e4d5ad88fbe8321cb8a752dab270cfc8353223d8c3eb040706d
~~~

It matches the pinned digest. Every stated claim is correct, with the
canonical new-root coset understood relative to the fixed refined block list
and the full integer relation presentation.

## 1. Row splitting and the new linear kernel

When an old integer block is split into gcd-free descendants, every
descendant inherits the same exponent in each old relation. Thus a row of
the old exponent matrix is replaced by one or more identical rows. The
original blocks are pairwise coprime, so descendants of different old blocks
do not merge.

For any coefficient vector \(x\), all duplicate descendant rows vanish on
\(x\) exactly when their original row vanishes. Therefore row splitting
does not change

\[
V=\ker(E\bmod\ell).
\]

Now work over \(\mathbb F_\ell\) in the final refined coordinates. An
element \((x,t)\in\mathbb F_\ell^m\times\mathbb F_\ell\) belongs to the new
kernel exactly when

\[
Ex+tb=0. \tag{1}
\]

If \(b\notin\operatorname{colspan}(E)\), equation (1) cannot hold with
\(t\ne0\), because then

\[
b=-t^{-1}Ex
\]

would lie in the column span. Hence \(t=0\) and \(x\in V\), giving

\[
\ker[E\mid b]=V\times\{0\}.
\]

Suppose instead that \(Ec+b=0\), and put \(z=(c,1)\). For a solution of
(1),

\[
E(x-tc)=Ex+t b=0.
\]

Thus \(v=x-tc\in V\), and

\[
(x,t)=(v,0)+t(c,1).
\]

The sum is direct because a nonzero multiple of \(z\) has nonzero last
coordinate. Therefore

\[
\ker[E\mid b]
=(V\times\{0\})\oplus\langle z\rangle.
\]

This includes \(V=0\), \(\ell=2\), and rank-zero matrices.

## 2. Integrality and homomorphisms

Use representatives in \(\{0,\ldots,\ell-1\}\). For \(x\in V\), every row
satisfies

\[
\sum_i e_{ji}x_i\equiv0\pmod\ell.
\]

The numerator is nonnegative, so every exponent in \(R(x)\) is a
nonnegative integer.

In the closing case, \(Ec+b=0\) gives

\[
\sum_i e_{ji}c_i+b_j\equiv0\pmod\ell
\]

for every row. These numerators are also nonnegative, so every exponent in
\(s_c\) is a nonnegative integer.

More generally, define the new root of a new-kernel vector \((x,t)\) by

\[
\mathcal R(x,t)
=
\left[
\prod_jq_j^{(\sum_i e_{ji}x_i+b_jt)/\ell}
\right]_N.
\]

All its displayed exponents are nonnegative integers by (1).

To check additivity, let \(w,w'\) be two kernel vectors and let
\(\overline w\) be the canonical representative of their sum. In each old
coordinate and in the final coordinate, write the carry as an integer
multiple of \(\ell\). If those carry digits are \(k_i\) and \(k_*\), then
rearranging the integer exponent sums gives

\[
\widetilde{\mathcal R}(w)
\widetilde{\mathcal R}(w')
=
\widetilde{\mathcal R}(\overline w)
\left(\prod_i A_i^{k_i}\right)A_*^{k_*}.
\]

Every old relation and the appended relation is \(1\) modulo \(N\).
Consequently,

\[
\mathcal R(w+w')=\mathcal R(w)\mathcal R(w')\pmod N.
\]

Thus the new root map is a homomorphism despite canonical-coordinate
wraparound. The old map \(R\) is the special case with no final coordinate,
so it is also a homomorphism.

Raising either root construction to the \(\ell\)-th power recombines the
corresponding integer relations. Hence every root lies in the product of
the two local \(\ell\)-th-root groups.

## 3. The new image and solution independence

In the closing case, every new-kernel vector has the unique form

\[
(v,0)+t z,
\qquad v\in V,\quad t\in\mathbb F_\ell.
\]

The homomorphism property gives

\[
\mathcal R((v,0)+tz)=R(v)s_c^t.
\]

Therefore the full new root image is exactly

\[
H'=\langle H,s_c\rangle.
\]

If \(c'\) is another solution of \(Ec'+b=0\), then

\[
c'-c\in V.
\]

Writing \(v=c'-c\) in \(\mathbb F_\ell^m\), the two kernel vectors satisfy

\[
(c',1)=(c,1)+(v,0).
\]

Canonical carries are already handled by the homomorphism proof, so

\[
s_{c'}=s_cR(v).
\]

Since \(R(v)\in H\),

\[
s_{c'}H=s_cH.
\]

Thus the coset is independent of the chosen linear solution.

## 4. Exact presentation relativity

The reduced matrix \([E\mid b]\bmod\ell\) determines the linear kernel and
the affine solution class, but it does not determine the divided integer
exponents. Those exponents use the actual nonnegative integer lifts
\(e_{ji},b_j\), the actual refined integer blocks \(q_j\), and the canonical
coordinate representatives.

Changing an integer exponent by a multiple of \(\ell\) leaves the reduced
matrix unchanged but changes a divided exponent by an integer and can
multiply a root by a block residue. Likewise, changing the refined block
presentation can change the integer root even when the reduced linear
system is isomorphic.

Accordingly, \(s_cH\) is canonical only relative to:

1. the fixed final refined block list;
2. the fixed full integer exponent columns; and
3. the stated canonical coordinate convention.

It is not an invariant of the reduced matrix alone.

## 5. Structure forced by complete old-decoder failure

Let the two local components of the old root map be

\[
f_p,f_q:V\longrightarrow\mu_\ell(\mathbb F_p),
\quad
\mu_\ell(\mathbb F_q).
\]

After identifying a nontrivial local root group with the additive group of
\(\mathbb F_\ell\), each component is a linear functional, possibly zero.
A root gives a proper positive-sign gcd exactly when it belongs to exactly
one of the two identity kernels.

Completeness of the old decoder therefore implies

\[
\ker f_p=\ker f_q. \tag{2}
\]

There are only two possibilities.

* Both functionals are zero. Then both local components of every root are
  \(1\), so \(H=\{1\}\).
* Both are nonzero. Equal kernels make them nonzero scalar multiples. Their
  joint image is a one-dimensional graph line of order \(\ell\). Hence
  \(H\) is cyclic of order \(\ell\).

If every public basis root \(R(b_i)\) equals \(1\) modulo \(N\), the
homomorphism property and basis generation show directly that \(R(x)=1\)
for all \(x\in V\), so \(H=1\). Conversely, if some basis root

\[
h=R(b_i)\ne1,
\]

then the second case applies. The element \(h\) has order \(\ell\) and
generates the whole old image:

\[
H=\langle h\rangle.
\]

This proves that any nonidentity basis root can be used; no special basis
choice is required.

## 6. Complete incremental decoder when \(H=1\)

If the new column does not close, the new kernel and image are unchanged,
so the old complete failure remains complete.

Assume it closes. When \(H=1\),

\[
H'=\langle s_c\rangle.
\]

Each local component of \(s_c\) has order either \(1\) or \(\ell\), because
\(\ell\) is prime. If exactly one component has order \(1\), then \(s_c\)
itself is a separator and

\[
1<\gcd(s_c-1,N)<N.
\]

If both components have order \(1\), the new image is trivial. If both have
order \(\ell\), every nonzero power remains nonidentity in both components,
while the zero power is identity in both. No power is a separator.

Thus a separator occurs anywhere in the full new image if and only if
\(s_c\) itself is one. The single public gcd test is complete.

This argument includes \(\ell=2\).

## 7. Complete incremental decoder when \(H\ne1\)

Now \(H=\langle h\rangle\) is a graph line of order \(\ell\). The new image
is

\[
H'=\langle H,s_c\rangle.
\]

If \(s_c\in H\), then \(H'=H\). The old graph contains no positive
separator, and the scan

\[
\{s_ch^t:0\le t<\ell\}
\]

is just \(H\). It contains none.

Suppose \(s_c\notin H\). Both local projections of \(H\) are nontrivial
order-\(\ell\) root groups. Choose hidden additive coordinates for these
two root groups. In those coordinates, write

\[
h=(\alpha,\beta),
\qquad
s_c=(a,b),
\]

where \(\alpha,\beta\ne0\). The scan is the affine line

\[
(a+t\alpha,\ b+t\beta),
\qquad t\in\mathbb F_\ell.
\]

There is one exponent

\[
t_p=-a/\alpha
\]

whose \(p\)-component is identity, and one exponent

\[
t_q=-b/\beta
\]

whose \(q\)-component is identity. They are distinct: equality would imply
\((a,b)\) is a scalar multiple of \((\alpha,\beta)\), or
\(s_c\in H\).

At \(t_p\), the \(q\)-component is nonidentity; at \(t_q\), the
\(p\)-component is nonidentity. Every other scan element has both
components nonidentity. Hence exactly two scan elements are positive
separators.

Also, \(s_c\notin H\) makes the two vectors linearly independent, so the
full new image is the two-dimensional root product. It contains separators.
Therefore the public coset scan contains a proper-gcd root if and only if
the full new image does.

The algorithm need not decide whether \(s_c\in H\). It runs the same
\(\ell\) public gcd tests in either case.

## 8. Edge cases

### Zero and proportional local functionals

If both old local functionals are zero, \(H=1\), and the single-test branch
is complete. If both are nonzero and proportional, \(H\) is the graph line
handled by the coset scan. A zero functional and a nonzero functional would
have different kernels and would already have produced a factor in the
complete old decoder, so this case cannot remain at the incremental stage.

### \(V=0\)

When \(V=\{0\}\), the public basis is empty and the statement that every
basis root is \(1\) is vacuously true. Thus \(H=1\). If the column does not
close, the new kernel remains zero. If it closes, the solution \(c\) is
unique because \(E\) is injective, the new kernel is generated by
\((c,1)\), and the single \(s_c\) test is complete. The unique solution need
not be zero.

### \(\ell=2\)

In the nontrivial-old-image branch, \(H\) has order \(2\). If \(s_c\notin
H\), its coset has two elements, and the two exponents \(t_p,t_q\) are the
two distinct elements of \(\mathbb F_2\). Both scan elements are
separators. The statement “exactly two” remains literal.

### \(\ell=p\) or \(\ell=q\)

In characteristic \(\ell\),

\[
X^\ell-1=(X-1)^\ell,
\]

so the local \(\ell\)-th-root group at that prime is trivial. If the old
complete decoder found no factor, kernel equality forces the other old local
functional to be zero as well, and \(H=1\). The single-test branch then
handles the new root exactly as above.

Operationally, this edge case is even simpler. Before saturation work, the
public computation

\[
d=\gcd(\ell,N)
\]

returns the hidden prime immediately if \(\ell=p\) or \(\ell=q\). Thus an
implementation should perform this boundary check first.

## 9. Public algorithm and deterministic bit complexity

Let \(L\) be the full presentation length and assume the numerical value of
\(\ell\) is polynomial in \(L+\log N\).

The public procedure is:

1. compute \(\gcd(\ell,N)\);
2. perform Gaussian elimination on \(E\bmod\ell\) and
   \([E\mid b]\bmod\ell\);
3. if \(b\) is not in the column span, report that the root image did not
   change;
4. otherwise obtain one public solution \(c\);
5. compute all basis roots \(R(b_i)\) and the public root \(s_c\);
6. if all basis roots are \(1\), test only \(\gcd(s_c-1,N)\);
7. otherwise choose any nonidentity basis root \(h\), enumerate
   \(s_c,s_ch,\ldots,s_ch^{\ell-1}\), and gcd-test each residue.

All decisions in this list are public equality, linear-algebra, modular
arithmetic, or gcd decisions. No local character, hidden factor, or
membership test \(s_c\in H\) is used.

The matrix dimensions and the bit lengths of all integer exponents and
blocks are bounded by the full presentation length. Gaussian elimination
uses polynomially many operations on \(O(\log\ell)\)-bit field elements.
The divided root exponents have polynomial bit length because they are sums
of polynomially many input exponents multiplied by representatives smaller
than \(\ell\). Repeated squaring computes every basis root and \(s_c\) in
polynomial bit complexity.

The final scan uses at most \(\ell\) modular multiplications and gcd tests.
The hypothesis that the numerical value of \(\ell\), rather than merely
its bit length, is polynomial makes this total deterministic polynomial.
Storage is also polynomial.

## 10. Scope

The theorem is a complete decoder for the change caused by one appended
relation column at one public prime after the old prime-saturation image has
already been decoded completely.

It does not guarantee that the new column belongs to the old column span.
If it does close, it does not guarantee that \(s_cH\) leaves the old graph
line. It does not select a useful prime \(\ell\), construct a useful
relation source on every input, prove an all-input success probability, or
give a general factoring algorithm.
