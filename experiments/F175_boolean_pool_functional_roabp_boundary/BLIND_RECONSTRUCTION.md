# Blind reconstruction of F175

**Statement SHA-256:** `5119a4ba746b40b17f4b1a886fb660ef0463803298c281b36c529b7e55116bfe` (verified before reading).

**Verdict:** proved as stated. The singleton-cut function rank is exactly
\(2^{K-1}\). Each listed model consequence follows from that flattening
rank. None of the listed exclusions is ruled out by the argument.

## 1. Canonical finite-field representative

Put \(d=2^{K-1}\). Each variable \(X_i\) occurs in exactly the \(d\)
linear factors indexed by subsets that contain \(i\). Hence

\[
\deg_{X_i} Q_K=d<r
\qquad (1\leq i\leq K).
\]

The evaluation map from polynomials with degree less than \(r\) in every
variable to functions on \(\mathbb F_r^K\) is injective. Indeed, in one
variable a polynomial of degree less than \(r\) that vanishes at all \(r\)
field elements is zero. Induction on the number of variables gives the
multivariate assertion by viewing a polynomial as a univariate polynomial
in its last variable.

Thus \(Q_K\) is already its unique canonical reduced representative. Its
large total degree is irrelevant: no relation \(X_i^r-X_i\) can identify
any of its monomials in an individual variable. The same observation will
let us turn formal independence of coefficient polynomials into independence
of the corresponding functions.

## 2. Every cut coefficient is nonzero

Fix \(j\), write \(x=X_j\), let \(I=[K]\setminus\{j\}\), and put
\(m=K-1\), so \(d=2^m\). For \(T\subseteq I\), define

\[
L_T(y)=\sum_{i\in T}y_i,
\qquad L_\varnothing=0,
\]

and set

\[
A(y)=\prod_{\varnothing\ne U\subseteq I}L_U(y).
\]

Splitting the factors of \(Q_K\) according to whether they contain \(j\)
gives

\[
Q_K(x,y)
=A(y)\prod_{T\subseteq I}(x+L_T(y))
=A(y)x\prod_{\varnothing\ne T\subseteq I}(x+L_T(y)).
\]

Let \(E_{m,s}\) be the elementary symmetric polynomial of degree \(s\)
in the \(d-1\) linear forms \(L_T\) with \(T\ne\varnothing\). Then

\[
Q_K(x,y)=\sum_{a=1}^{d}x^a c_a(y),
\qquad
c_a(y)=A(y)E_{m,d-a}(y).
\tag{1}
\]

We first prove that \(E_{m,s}\ne0\) over \(\mathbb F_r\) for every
\(0\leq s\leq d-1\). There are \(d/2\) subsets of \(I\) that contain a
fixed first index. If \(s\leq d/2\), set all other variables to zero. This
specializes

\[
E_{m,s}\longmapsto {d/2\choose s}y_1^s.
\]

The binomial coefficient is nonzero modulo \(r\), because its factorials
have arguments at most \(d/2<r\). If \(s>d/2\), the largest possible power
of \(y_1\) is \(d/2\). To obtain it, one must select all \(d/2\) forms whose
index sets contain \(1\), and select the \(y_1\) term from each. Therefore

\[
[y_1^{d/2}]E_{m,s}
=E_{m-1,s-d/2}(y_2,\ldots,y_m).
\]

Induction on \(m\) makes this coefficient nonzero. The base case consists
of \(E_{1,0}=1\) and \(E_{1,1}=y_1\). This proves the claim for every
\(s\).

Every \(L_U\) is a nonzero polynomial, so \(A\ne0\) in the integral domain
\(\mathbb F_r[y]\). Equation (1) now shows that every \(c_a\) is nonzero.
Moreover, \(A\) is homogeneous of degree \(d-1\), and \(E_{m,d-a}\) is
homogeneous of degree \(d-a\). Hence

\[
\deg c_a=2d-1-a.
\]

These total degrees are different for different \(a\). The polynomials
\(c_1,\ldots,c_d\) are therefore formally linearly independent, since a
linear relation cannot cancel distinct homogeneous components.

Each \(c_a\) has degree at most \(d<r\) in every \(y_i\), as it is an
\(x\)-coefficient of \(Q_K\). By the canonical-representative argument in
Section 1, the functions on \(\mathbb F_r^{K-1}\) represented by the
\(c_a\)'s are also linearly independent.

## 3. Exact singleton-cut rank

Let

\[
V[x,a]=x^a
\quad (x\in\mathbb F_r,\ 1\leq a\leq d),
\qquad
C[a,y]=c_a(y).
\]

Equation (1) gives the matrix factorization \(\mathcal M_j=VC\). The
columns of \(V\) are independent: a relation among them would be a
univariate polynomial of degree at most \(d<r\) with all \(r\) field
elements as roots. The rows of \(C\) are independent by Section 2. Thus
\(V\) has column rank \(d\), \(C\) has row rank \(d\), and

\[
\operatorname{rank}_{\mathbb F_r}\mathcal M_j=d=2^{K-1}.
\]

The choice of \(j\) was arbitrary, so this holds across every singleton
cut.

## 4. Consequences for the stated exact models

For any exact separated representation across \(X_j\mid X_{-j}\),

\[
Q_K(x,y)=\sum_{t=1}^{w} f_t(x)g_t(y),
\]

the function matrix is a sum of \(w\) rank-one matrices. Therefore its rank
is at most \(w\), and Section 3 forces \(w\geq d\). No algebraic restriction
on the functions \(f_t,g_t\) is needed.

Apply this observation after the first variable of a functional ROABP. If
\(j=\pi(1)\) and that bond has width \(w\), then

\[
u^TM_1(x)=\bigl(f_1(x),\ldots,f_w(x)\bigr),
\]

while the coordinates of \(M_2(y_{\pi(2)})\cdots M_K(y_{\pi(K)})v\) are
functions \(g_t(y)\). Their contraction is the separated representation
above. Hence the width immediately after the first variable is at least
\(d\), and so is the maximum width. Allowing arbitrary, nonuniform
single-variable matrix entries, including entries selected using public or
surrounding-modulus parameters, does not alter this rank factorization.

The other consequences are the same cut argument in equivalent notation:

1. A one-pass linear-state recurrence has a variable-dependent linear map
   at each read and a linear final contraction. Its state coordinates after
   the first read give the separated summands, so that state dimension is at
   least \(d\).
2. A tensor train is the same matrix product written as tensor cores. The
   first bond in any variable ordering has dimension at least \(d\).
3. In a tree tensor network, cut the sole bond incident to the designated
   leaf for \(X_j\). Summing over that bond gives at most one separated term
   per bond index. Its bond dimension is therefore at least \(d\). The
   assumptions that \(X_j\) occurs only at that leaf and that the leaf has
   one incident bond are exactly what makes this the singleton cut.
4. Every exact sum of \(w\) character products is a separated expansion
   across each singleton cut: the character involving \(X_j\) is the first
   factor, and the product of all remaining characters is the second.
   Therefore such a sum needs at least \(d\) terms.

If \(K=\Theta(n)\), then \(d=2^{K-1}=2^{\Theta(n)}\). For fixed constants
\(C\) and \(k\), one has \((\log_2(n+1))^k=o(n)\), so eventually

\[
K-1>C(\log_2(n+1))^k.
\]

Thus \(2^{K-1}\) eventually exceeds every fixed
\(2^{C(\log_2(n+1))^k}\). The assumptions \(p,q>2^K>d\) let the rank theorem
be applied separately over either hidden prime field whenever the exact
model in question computes \(Q_K\) on the full field cube.

## 5. Why the stated exclusions remain exclusions

The proof establishes only a flattening-rank obstruction to an exact,
explicitly separated read-once representation of this particular function
on the full input cube.

- A general arithmetic circuit can read and reuse variables. A large
  flattening rank does not imply a lower bound for unrestricted circuit
  size.
- An exponential-dimensional state can have an implicit structured
  description and a special fast update. The rank result bounds its
  mathematical dimension, not the cost of manipulating such a description.
- A determinant, Pfaffian, permanent, or other global circuit need not expose
  a small bond across the singleton cut. Its expansion may have exponential
  read-once width even when its global description is small.
- A composite-modulus branching computation can stop when a nonunit or a
  failed denominator exposes a gcd. Such a partial, branching computation
  is not a fixed exact field-valued representation on all of
  \(\mathbb F_r^K\).
- The proof is specific to exact computation of \(Q_K\). It says nothing
  about a different observable that has a useful local zero set.
- Equality only on a random subset of inputs does not give equality of the
  full function matrix used in the rank argument.
- Characteristic-dependent Moore or Frobenius operations, or other
  finite-field functions outside the stated read-once separation, are not
  constrained merely because \(Q_K\) has this rank.
- A gcd-only detector that never represents \(Q_K\) does not supply a
  separated representation of \(Q_K\), so the premise of the lower bound is
  absent.

Finally, for \(K=2\), direct expansion gives

\[
\det\!\begin{pmatrix}x&y\\x^2&y^2\end{pmatrix}
=xy(y-x),
\qquad
Q_2(x,y)=xy(x+y).
\]

In every odd characteristic, \((x,y)=(1,1)\) is a zero of the determinant
but not of \(Q_2\), while \((1,-1)\) is a zero of \(Q_2\) but not of the
determinant. Hence their zero sets differ. This refutes only that direct
characteristic-two Moore lift; it gives no obstruction to a different
determinant or a different pooled observable.
