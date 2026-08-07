# F62 proof-blind reconstruction

## Protocol and verdict

This reconstruction uses only `STATEMENT.md`. I did not read a candidate proof,
an audit, or any P69 source. No computer algebra, numerical search, or
probabilistic computation was used. All arithmetic used as evidence is displayed
below.

The exact quotient law and all four witnesses are correct. The ancillary claims
are also correct with two scope qualifications:

1. The statement about P69 can be checked here only at the level stated: an
   argument that requires closure in the old one-block universe cannot be applied
   when the complementary endpoint adds a block. This reconstruction does not
   assess any broader P69 result.
2. “Exponential” exponent-vector enumeration is exponential in the number of
   block coordinates (and can be superpolynomial in the full bit encoding). The
   exact arithmetic for any polynomially sized, explicitly supplied list of
   selections is polynomial. This does not make exhaustive search polynomial.

## 1. Exact feedback law

Write every retained endpoint in the complete gcd-free basis as

\[
z=\prod_{j=1}^r q_j^{e_j(z)},\qquad e_j(z)\geq 0.
\]

By the definition of the total exponents,

\[
P_S=\prod_{i\in S}A_i=\prod_jq_j^{E_j(S)}.
\]

Consequently, the coordinate bounds on \(c_j\) imply

\[
g=\prod_jq_j^{c_j}\mid P_S.
\]

Since \(P_S=1+K_SN\), one has \(\gcd(P_S,N)=1\), and hence
\(\gcd(g,N)=1\). The inverse \(w\) therefore exists and is unique in
\(\{1,\ldots,N-1\}\).

Reduce both exact identities modulo \(g\):

\[
1+K_SN\equiv0\pmod g,
\qquad
1+k(g)N=gw\equiv0\pmod g.
\]

Because \(N\) is invertible modulo \(g\), subtraction gives

\[
k(g)\equiv K_S\pmod g. \tag{1}
\]

It remains to identify the representative. Since \(g>1\), the positive integer
\(gw\) cannot equal 1. It is congruent to 1 modulo \(N\), so \(gw\geq N+1\)
and \(k(g)\geq1\). Also \(w<N\), so \(gw<gN\), whence \(k(g)<g\). Thus

\[
1\leq k(g)\leq g-1.
\]

Equation (1) is therefore exactly the least nonzero residue law

\[
\boxed{k(g)=K_S\bmod g\in\{1,\ldots,g-1\}.}
\]

In particular, \(K_S\not\equiv0\pmod g\). Notice that the proof of the residue
law actually works for every divisor \(g>1\) of \(P_S\); the extra condition
\(g<N\) is what makes \(g\) itself a canonical endpoint.

### Boundary cases

The argument uses exact block exponents but not primality of the \(q_j\).
Coordinates with \(c_j=0\) simply do not contribute, and coordinates with
\(c_j=E_j(S)\) cause no change to the divisibility argument. If \(S\) is
empty, or if its product is 1, every exponent is zero and the only possible
product is \(g=1\); the hypothesis \(g>1\) correctly excludes this case. At
\(g=1\), the quotient would be zero and there is no nonzero residue class of
the stated kind.

The lower modulus boundary also works. For \(N=3\), the relation
\(2\cdot2=4=1+3\) permits \(g=2\), with \(w=2\) and \(k=1\). At the other
endpoint, for every \(N\geq3\), the relation
\((N-1)^2=1+(N-2)N\) permits \(g=N-1\); then \(w=N-1\) and
\(k=N-2=g-1\). Thus both inequalities in \(1\leq k\leq g-1\) are sharp.
The value \(g=N\) cannot be selected from a divisor of \(P_S\), because
\(\gcd(P_S,N)=1\).

### Certificate independence

For fixed \((N,g)\), the least positive inverse \(w\), and hence
\((gw-1)/N\), is unique. If two subsets \(S,T\) both certify the same selected
\(g\), the proof above gives

\[
K_S\equiv k(g)\equiv K_T\pmod g.
\]

There can nevertheless be several certificates. For example, at \(N=21\),
retain the two relations

\[
2\cdot11=22=1+21,
\qquad
8\cdot8=64=1+3\cdot21.
\]

Either singleton subset supplies a factor 2, so each certifies the same state
\(g=2\). Their quotients are \(K=1\) and \(K=3\), respectively, and both are
1 modulo 2. The unique complementary endpoint is \(w=11\), and
\(2\cdot11=1+1\cdot21\).

## 2. Witness 1: \(N=21\), cross-relation selection

For the two seed relations,

\[
P_S=22\cdot85=1870=1+89\cdot21,
\qquad K_S=89.
\]

The selected divisor is \(g=2\cdot5=10\). Its least positive inverse modulo
21 is 19, and

\[
10\cdot19=190=1+9\cdot21,
\qquad 89\bmod10=9.
\]

After adding this relation, use rows \((2,5,11,17,19)\) and columns
\((22,85,190)\). The square-class parity matrix over \(\mathbf F_2\) is

\[
M=
\begin{pmatrix}
1&0&1\\
0&1&1\\
1&0&0\\
0&1&0\\
0&0&1
\end{pmatrix}.
\]

The rows for 11, 17, and 19 force the three column coefficients to be zero.
Thus \(\ker M=0\), as claimed. The direct endpoint screen still succeeds:

\[
\gcd(g-1,N)=\gcd(9,21)=3,
\]

with complementary factor 7.

This witness also proves the new-block claim. The old endpoint blocks are
\(2,5,11,17\), while the new complementary endpoint \(w=19\) contributes a
new coprime block. Hence closure in the old fixed block set is false. Any
one-block fixed-point argument that assumes that closure has an unmet premise.

## 3. Witness 2: \(N=55\), a new non-global root

The old products have square classes

\[
56=2^3\cdot7,
\qquad
111=3\cdot37.
\]

With rows \((2,7,3,37)\), their two parity columns are

\[
\begin{pmatrix}1\\1\\0\\0\end{pmatrix},
\qquad
\begin{pmatrix}0\\0\\1\\1\end{pmatrix}.
\]

They are linearly independent, so the old square-class kernel is zero. For the
subset containing both relations,

\[
P_S=56\cdot111=6216=1+113\cdot55.
\]

The selected \(g=3\cdot7=21\) divides this product. It is self-inverse modulo
55 because

\[
21^2=441=1+8\cdot55,
\qquad 113\bmod21=8.
\]

It is a non-global square root of 1, and both gcd screens are proper:

\[
\gcd(21-1,55)=5,
\qquad
\gcd(21+1,55)=11.
\]

## 4. Witness 3: three authorized copies at \(N=21\)

For three explicitly authorized indexed copies of \(22=2\cdot11\),

\[
P_S=22^3=10648=1+507\cdot21.
\]

The total exponent budget contains three copies of the block 2, so it permits
\(g=2^3=8\). This element is self-inverse modulo 21:

\[
8^2=64=1+3\cdot21,
\qquad 507\bmod8=3.
\]

Thus it splits 21:

\[
\gcd(8-1,21)=7,
\qquad
\gcd(8+1,21)=3.
\]

The three old parity columns are all the same vector, namely \((1,1)^T\) in
the block rows \((2,11)\). Their kernel consists of the even-cardinality
indexed subsets. Every nonempty such subset uses two copies, whose product is
\(22^2\); its positive square root is \(22\equiv1\pmod{21}\). A negative
choice gives \(-1\). Hence the old decoder produces only global roots.

The copies increase the available exponents but not the rank or the observed
square class. Therefore they are an exponent budget, not independent
observations. One may use the relation three times here only because the three
uses were explicitly authorized; a single retained relation does not license
unbounded reuse.

## 5. The infinite family

Let \(t\geq3\) be odd and set

\[
g=2^t,
\qquad
N=\frac{g^2-1}{3}=\frac{4^t-1}{3}
  =\sum_{i=0}^{t-1}4^i.
\]

The smallest allowed value \(t=3\) gives \((g,N)=(8,21)\), so the boundary
member is exactly witness 3.

### Integrality and endpoint checks

The geometric-sum identity proves that \(N\) is an integer. It also gives
\(N\equiv1\pmod4\), so \(N\) is odd. In particular, \(N\geq21\). Put

\[
y=\frac{N+1}{2}=\frac{2^{2t-1}+1}{3}.
\]

Then \(y\) is an odd integer and

\[
2y=N+1=1+1\cdot N.
\]

Moreover, \(2<N\) and \(1<y<N\). Thus this is a canonical quotient-one
inverse relation. Directly,
\(\gcd(2,N)=1\) and \(\gcd(y,N)=\gcd(y,2y-1)=1\).

Each copy contains exactly one factor 2 because \(y\) is odd. Therefore \(t\)
authorized copies give the exact exponent budget needed to select \(2^t=g\).
For \(g\geq8\),

\[
N-g=\frac{g^2-3g-1}{3}>0,
\]

so \(1<g<N\); also \(\gcd(g,N)=1\).

### Old decoder and feedback

Every old parity column is identical and has a 1 in the block-2 row. A subset
is in the square-class kernel exactly when it uses an even number \(m\) of
copies. Its product and positive square root are

\[
(N+1)^m,
\qquad
(N+1)^{m/2}\equiv1\pmod N.
\]

Thus every old decoded root is global (up to sign).

On the other hand,

\[
g^2=1+3N.
\]

Since \(g<N\), the least positive inverse of \(g\) is \(w=g\), and the new
quotient is 3. It agrees with the general law. Indeed, for

\[
K_S=\frac{(N+1)^t-1}{N},
\]

the facts \(g\mid(N+1)^t\), \(K_SN\equiv-1\pmod g\), and
\(3N=g^2-1\equiv-1\pmod g\) give \(K_S\equiv3\pmod g\).

The root is non-global because

\[
N-(g+1)=\frac{(g-4)(g+1)}{3}>0.
\]

### Factors and coprimality

Odd \(t\) gives \(g=2^t\equiv-1\pmod3\), so

\[
h=\frac{g+1}{3}\in\mathbb Z,
\qquad
N=(g-1)h.
\]

Both \(g-1\) and \(h\) are odd. If a number divides both, it divides
\(3h-(g-1)=2\), so

\[
\gcd(g-1,h)=1.
\]

Also \(3\nmid g-1\). It follows that

\[
\gcd(g-1,N)=g-1,
\qquad
\gcd(g+1,N)=\gcd(3h,(g-1)h)=h=\frac{g+1}{3}.
\]

For \(g\geq8\), the two coprime factors are at least 7 and 3, respectively,
so both are proper factors of \(N\).

### Exact bit sizes

Let \(\ell(a)=\lfloor\log_2 a\rfloor+1\) for \(a\geq1\). The displayed
forms and elementary bounds give

\[
\ell(g)=t+1,
\quad
\ell(N)=2t-1,
\quad
\ell(y)=2t-2,
\quad
\ell(g-1)=t,
\quad
\ell\!\left(\frac{g+1}{3}\right)=t-1.
\]

For example, \(2^{2t-2}\leq N<2^{2t-1}\), and
\(2^{t-2}<(g+1)/3<2^{t-1}\). The explicitly formed product
\((N+1)^t\), and hence its quotient \(K_S\), has \(\Theta(t^2)\) bits.
Since \(\ell(N)=2t-1\), this is polynomial in the input bit length. Listing
all \(t\) copies explicitly also costs \(O(t^2)\) bits (or less with an
explicit multiplicity encoding).

## 6. Reducing a divisor modulo \(N\) is not the same operation

Use witness 1, for which \(P_S=1870=1+89\cdot21\). The divisor

\[
G=2\cdot17=34>21
\]

satisfies \(G\mid P_S\). Reduce it modulo \(N\): \(h=34\bmod21=13\). The
least positive inverse of \(h\) is 13, and

\[
13^2=169=1+8\cdot21.
\]

But

\[
89\bmod13=11\ne8.
\]

Thus the quotient formula does not survive the replacement \(G\mapsto
G\bmod N\). The reason is structural: \(G\mid P_S\), but generally
\(G\bmod N\nmid P_S\). In this example, the unreduced divisor itself still
obeys the law:

\[
34\cdot13=442=1+21\cdot21,
\qquad 89\bmod34=21.
\]

The failure comes from changing the selected integer, not from the congruence
class used to compute its inverse.

## 7. Arithmetic cost versus search cost

Suppose the input explicitly contains \(m\) relations, with every endpoint
less than \(N\). For any subset certificate,

\[
P_S<N^{2m},
\]

so \(P_S\), \(K_S\), and every selected divisor of \(P_S\) have
\(O(m\log N)\) bits. Multiplication, exact division, modular inversion, and
gcd computation on a polynomial number of explicitly selected products
therefore have polynomial bit cost. The same conclusion holds when \(m\) and
the number of selections are polynomial in the encoded input length.

This arithmetic bound is not a search bound. There are \(2^m\) indexed
subsets. For fixed total block exponents, the rectangular exponent-vector
search space has

\[
\prod_{j=1}^r(E_j(S)+1)
\]

members; it already has \(2^r\) members when every \(E_j(S)=1\). Hence
coordinate-wise exhaustive enumeration is exponential in \(r\), and under
ordinary integer encodings can be superpolynomial in the total input length.
Magnitude filters and collisions can reduce a particular instance, but no such
reduction follows from the exact law. Polynomially many checked candidates do
not imply a polynomial-time method for finding a useful candidate.

## 8. Even inputs, perfect powers, and odd prime powers

An all-input factoring specification based on non-global square roots needs
explicit special-case handling:

- If \(N\) is even, 2 is already a factor (and powers of 2 can be removed).
- If \(N=a^e\) with \(e>1\), perfect-power detection reduces the problem to
  factoring \(a\) and restoring multiplicities.

The second branch is essential for the square-root target because an odd prime
power has no non-global square root of 1. Let \(N=p^e\) with odd prime \(p\).
If \(z^2\equiv1\pmod{p^e}\), then

\[
p^e\mid(z-1)(z+1).
\]

But \(\gcd(z-1,z+1)\mid2\), so the odd prime \(p\) divides at most one of
the two factors. Its entire exponent \(e\) must therefore divide that one
factor. Hence

\[
z\equiv1\pmod{p^e}
\quad\text{or}\quad
z\equiv-1\pmod{p^e}.
\]

Thus a correct reduction to a non-global-root search must preprocess perfect
powers or provide equivalent separate handling. If “all input” includes
primes rather than promised composites, primality detection is an additional
required outcome; the two preprocessing clauses alone are not a complete
factoring specification.

## 9. Scope of the result

What has been proved is an exact feedback operation: an explicitly selected
divisor of a certified product determines a new canonical inverse relation,
and its quotient is recovered by a residue of the certificate quotient. The
examples show that this operation can expose factors even when the old
square-class decoder is empty or produces only global roots. The family gives
infinitely many such explicit instances.

Nothing here supplies a useful selector for arbitrary inputs, a success
probability, a polynomial bound on candidate search, a classical
polynomial-time factoring algorithm, or a novelty claim.

## Computation register

No proof-relevant external computation was performed. The complete concrete
arithmetic register is:

| case | \(P_S=1+K_SN\) | selected endpoint equation | residue | gcd screens |
|---|---|---|---|---|
| 1 | \(22\cdot85=1870=1+89\cdot21\) | \(10\cdot19=190=1+9\cdot21\) | \(89\bmod10=9\) | \(\gcd(9,21)=3\) |
| 2 | \(56\cdot111=6216=1+113\cdot55\) | \(21^2=441=1+8\cdot55\) | \(113\bmod21=8\) | \(\gcd(20,55)=5,\ \gcd(22,55)=11\) |
| 3 | \(22^3=10648=1+507\cdot21\) | \(8^2=64=1+3\cdot21\) | \(507\bmod8=3\) | \(\gcd(7,21)=7,\ \gcd(9,21)=3\) |
| reduction counterexample | \(1870=1+89\cdot21\) | \(13^2=169=1+8\cdot21\) | \(89\bmod13=11\) | not applicable |

All infinite-family checks are symbolic identities and inequalities displayed
in Section 5.
