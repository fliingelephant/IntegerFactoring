# F283 blind reconstruction

## Blind protocol

This reconstruction uses only `STATEMENT.md`, authenticated before reading as

```text
97711c57667f13d4a86daa5b0533ecdb3165818f92544016fb38ee8673b3e006
```

No other F283 artifact was read before this file was sealed. No numerical or
symbolic search was run. The arguments below are direct derivations from the
statement.

Let

\[
N=pq,\qquad p<q<2p,\qquad B=\lfloor\sqrt N\rfloor,
\]

and work on the branch left after testing \(\gcd(B,N)\). Write

\[
B=p+s,\qquad q=B+h.
\]

The inherited geometry is

\[
s\geq 1,\qquad h\geq s+2,\qquad p\geq 2s+3,
\qquad p<B<q<2p<2B. \tag{A}
\]

The object under audit is

\[
F_B(a)=\frac{\Delta^B X^{2B}|_{X=a}}{B!}
      =h_B(a,a+1,\ldots,a+B). \tag{B}
\]

The equality in (B) is an equality in \(\mathbb Z[a]\). In particular, the
division by \(B!\) is exact integer division, not inversion modulo \(N\).
This reconstruction proves boundaries for specific representations of (B).
It does not construct an evaluator or prove a general evaluator lower bound.

## 1. Generalized Stirling descriptions

For nodes \(x_0,\ldots,x_k\), the generating series of divided differences of
monomials is

\[
\sum_{n\geq 0}[x_0,\ldots,x_k]X^n z^n
 =[x_0,\ldots,x_k]\frac1{1-Xz}
 =\frac{z^k}{\prod_{i=0}^k(1-x_i z)}. \tag{1}
\]

The last equality follows successively from

\[
\frac{(1-x_1z)^{-1}-(1-x_0z)^{-1}}{x_1-x_0}
=\frac{z}{(1-x_0z)(1-x_1z)}.
\]

Taking the coefficient of \(z^n\) in (1) gives, for \(n\geq k\),

\[
[x_0,\ldots,x_k]X^n=h_{n-k}(x_0,\ldots,x_k). \tag{2}
\]

Set \(x_i=a+i\) and define

\[
G_a(n,k)=[a,a+1,\ldots,a+k]X^n.
\]

Then

\[
G_a(n,k)=h_{n-k}(a,a+1,\ldots,a+k),\qquad
F_B(a)=G_a(2B,B). \tag{3}
\]

Newton interpolation on the consecutive grid has basis

\[
(X-a)_{\underline{k}}=\prod_{i=0}^{k-1}(X-a-i),
\]

so its coefficients are precisely these divided differences:

\[
X^n=\sum_{k=0}^nG_a(n,k)(X-a)_{\underline{k}}. \tag{4}
\]

Multiplication of the basis by \(X\) gives

\[
X(X-a)_{\underline{k}}
=(X-a)_{\underline{k+1}}+(a+k)(X-a)_{\underline{k}}.
\]

Equating coefficients in (4) therefore proves

\[
G_a(n+1,k)=G_a(n,k-1)+(a+k)G_a(n,k), \tag{5}
\]

with \(G_a(0,0)=1\) and zero outside the usual triangular range. When
\(a=r\) is a nonnegative integer, (5) and its initial condition are those
of the \(r\)-Stirling number

\[
G_r(n,k)=\left\{\begin{matrix}n+r\\k+r\end{matrix}\right\}_r. \tag{6}
\]

The polynomial definition (3), rather than a combinatorial interpretation
requiring \(r\geq0\), applies to arbitrary shifts.

There are two useful generating forms. Formally expand

\[
e^{Xz}=e^{az}(e^z)^{X-a}
=e^{az}\sum_{k\geq0}\frac{(X-a)_{\underline{k}}}{k!}(e^z-1)^k.
\]

Comparison with (4) yields

\[
G_a(n,k)=\frac{n!}{k!}[z^n]e^{az}(e^z-1)^k. \tag{7}
\]

Equation (2) also gives, for a fixed \(B\),

\[
\sum_{d\geq0}G_a(B+d,B)t^d
=\prod_{j=0}^{B}(1-(a+j)t)^{-1}. \tag{8}
\]

Thus the divided-difference, complete-homogeneous, recurrence, exponential
generating function, and rational generating function descriptions are
the same exact object. Their displayed, literal evaluations still traverse
a range, coefficient, or state whose size grows with \(B\). This observation
alone is not a lower bound for a different arithmetic circuit.

## 2. The exact linear mode count

Work over \(K=\mathbb Q(a)\), put \(x_j=a+j\), and let

\[
u_d=h_d(x_0,\ldots,x_B).
\]

Then

\[
U_B(t)=\sum_{d\geq0}u_dt^d
=\frac1{Q_B(t)},\qquad
Q_B(t)=\prod_{j=0}^{B}(1-x_jt). \tag{9}
\]

Every \(x_j\) is nonzero in \(K\), and the \(x_j\)'s are pairwise distinct.
The numerator 1 cancels no denominator factor. Hence (9) is reduced and its
denominator has degree \(B+1\).

A homogeneous constant-coefficient recurrence of order \(m\) for the full
sequence makes its generating function \(P(t)/R(t)\), where
\(\deg R=m\) and \(R(0)=1\). Reduction then forces \(Q_B\mid R\), so
\(m\geq B+1\). Conversely, the coefficients of \(Q_B\) give a recurrence
of order \(B+1\). The exact minimum is therefore \(B+1\).

Likewise, if a constant-matrix realization has the form

\[
u_d=\lambda^{\mathsf T}A^d\rho
\]

with \(A\) of dimension \(m\), Cayley--Hamilton gives a recurrence of order
at most \(m\). Every such realization of the full sequence has
\(m\geq B+1\).

Fixed-radix decimation does not merge these modes. Partial fractions give

\[
u_d=\sum_{j=0}^{B}\lambda_jx_j^d,
\qquad
\lambda_j=\prod_{\ell\ne j}(1-x_\ell/x_j)^{-1}\ne0. \tag{10}
\]

For fixed integers \(r\geq1\) and \(c\geq0\),

\[
\sum_{d\geq0}u_{rd+c}z^d
=\sum_{j=0}^{B}\frac{\lambda_jx_j^c}{1-x_j^rz}. \tag{11}
\]

The bases \(x_j^r\) remain distinct. Indeed, for \(j\ne\ell\),

\[
(a+j)^r-(a+\ell)^r
=r(j-\ell)a^{r-1}+\text{terms of lower degree},
\]

which is nonzero in characteristic zero. Each residue in (11) is nonzero,
so no pole cancels. The decimated sequence therefore also has reduced
denominator degree \(B+1\), and hence minimal recurrence order \(B+1\).
Even, odd, and iterated fixed-radix subsequences do not reduce this canonical
linear state.

The Stirling recurrence itself has a matching constant matrix. Let
\(M_B(a)\) be lower bidiagonal with

\[
(M_B)_{k,k}=a+k,
\qquad (M_B)_{k,k-1}=1,
\]

for the admissible indices \(0\leq k\leq B\). If
\(g_n=(G_a(n,0),\ldots,G_a(n,B))^{\mathsf T}\), then (5) says
\(g_{n+1}=M_Bg_n\) and \(g_0=e_0\). Consequently,

\[
F_B(a)=e_B^{\mathsf T}M_B(a)^{2B}e_0. \tag{12}
\]

Binary powering reduces the number of matrix-power stages, not the matrix
width. More importantly, the mode proof concerns generation of every
\(u_d\). It does not constrain a device designed only for \(u_B\). For
example, one can place \(F_B(a)\) itself in a one-dimensional matrix entry;
that representation says nothing about the cost of obtaining the entry.
The argument also gives no bound for nonlinear state, data-dependent state,
branching, or noncanonical encodings.

## 3. Shift, reflection, block, and parity identities

Let \(x=(x_1,\ldots,x_n)\). The generating function after translating all
variables by \(c\) is

\[
\begin{aligned}
\prod_{i=1}^n(1-(x_i+c)t)^{-1}
&=(1-ct)^{-n}
  \prod_{i=1}^n\left(1-x_i\frac{t}{1-ct}\right)^{-1}\\
&=\sum_{j\geq0}h_j(x)t^j(1-ct)^{-n-j}.
\end{aligned} \tag{13}
\]

Taking degree \(d\) yields

\[
h_d(x_1+c,\ldots,x_n+c)
=\sum_{j=0}^d\binom{n+d-1}{d-j}c^{d-j}h_j(x). \tag{14}
\]

With \(n=B+1\), \(d=B\), and \(x=(a,a+1,\ldots,a+B)\), this is

\[
F_B(a+c)=\sum_{j=0}^{B}
\binom{2B}{B-j}c^{B-j}h_j(a,a+1,\ldots,a+B). \tag{15}
\]

All \(B+1\) scalar coefficients in this polynomial identity are nonzero in
characteristic zero. For the special substitution \(c=0\), powers of \(c\)
of course vanish. The correct boundary is that the displayed generic
translation law consumes the full homogeneous state; it is not a proof
that every translation algorithm must do so. In particular, knowing only
the final component \(h_B\) at one base shift does not supply (15) at a
generic new shift.

The nodes for \(F_B(-B-a)\), after reordering, are the negatives of the
nodes for \(F_B(a)\). Homogeneity gives the reflection

\[
F_B(-B-a)=(-1)^BF_B(a). \tag{16}
\]

For the one-step difference, cancel the common internal nodes in the two
generating functions:

\[
\begin{aligned}
H_{B,a+1}(t)-H_{B,a}(t)
&=\prod_{j=1}^{B}(1-(a+j)t)^{-1}
 \left(\frac1{1-(a+B+1)t}-\frac1{1-at}\right)\\
&=(B+1)tH_{B+1,a}(t).
\end{aligned}
\]

The coefficient of \(t^B\) gives

\[
F_B(a+1)-F_B(a)
=(B+1)h_{B-1}(a,a+1,\ldots,a+B+1). \tag{17}
\]

Reflection retains the same index \(B\). Equation (17) changes both degree
and node count and therefore starts a neighboring ladder rather than
closing on \(F_B\). Neither formula supplies an initial value.

If \(a\) is uniform modulo \(N\), then \(ua+c\) is uniform precisely when
\(u\) is a unit modulo \(N\). Thus public unit-affine changes, including
the reflection \(u=-1\), preserve the sampling distribution. Replacing
the sampled shift by one fixed shift does not.

For interval products, define

\[
H_{L,a}(t)=\prod_{j=0}^{L}(1-(a+j)t)^{-1}. \tag{18}
\]

Its denominator is

\[
\prod_{j=0}^{L}(1-(a+j)t)
=(-t)^{L+1}(a-t^{-1})^{\overline{L+1}}, \tag{19}
\]

an ordinary rising factorial. Splitting one consecutive interval into two
gives

\[
H_{L_1+L_2+1,a}(t)
=H_{L_1,a}(t)H_{L_2,a+L_1+1}(t). \tag{20}
\]

The degree-\(d\) coefficient is the complete convolution

\[
\sum_{i=0}^{d}[t^i]H_{L_1,a}(t)
                  [t^{d-i}]H_{L_2,a+L_1+1}(t). \tag{21}
\]

At \(d=B\), the displayed sum has \(B+1\) terms.

Separating even and odd nodes proves the two parity formulas directly:

\[
H_{2m,a}(t)
=H_{m,a/2}(2t)H_{m-1,(a+1)/2}(2t), \tag{22}
\]

where the second factor is 1 for \(m=0\), and

\[
H_{2m+1,a}(t)
=H_{m,a/2}(2t)H_{m,(a+1)/2}(2t). \tag{23}
\]

These are also what the ordinary Pochhammer duplication formula gives.
They are two-child identities: the children have different affine shifts.
They are not a one-child geometric product law that can be powered by
repeated squaring. Because \(N\) is odd, the halves in (22)--(23) are
unit-safe modulo \(N\). That fact does not remove the central convolution.
A direct recursive expansion has one leaf per original linear factor, so
its total leaf count is linear in \(L+1\).

These conclusions apply to the displayed coefficient state and its direct
recursion. A fast multiplication method, a compressed aggregate, or an
unknown invariant is not excluded merely because (21) has many summands.

## 4. Divided-power composition and its first crossing

Over \(\mathbb Q[X]\), define

\[
\mathcal D_k=\frac{\Delta^k}{k!}.
\]

Since \(\Delta^m\Delta^n=\Delta^{m+n}\),

\[
\mathcal D_m\mathcal D_n
=\frac{(m+n)!}{m!n!}\mathcal D_{m+n}
=\binom{m+n}{m}\mathcal D_{m+n}. \tag{24}
\]

Consider a monotone binary addition chain. It starts at index 1, adds two
positive earlier indices, never exceeds \(B\), and ends at \(B\). Because
\(p<B\), there is a first generated index \(k\geq p\). If \(k=m+n\), the
choice of the first crossing gives \(m,n<p\), while (A) gives

\[
p\leq k\leq B<q<2p. \tag{25}
\]

Legendre valuations are then immediate:

\[
v_p(k!)=1,\qquad v_p(m!)=v_p(n!)=0,
\]

and no factorial contains \(q\). Hence

\[
v_p\binom{k}{m}=1,\qquad
v_q\binom{k}{m}=0,
\qquad
\gcd\!\left(\binom{k}{m},N\right)=p. \tag{26}
\]

The endpoints in (25) matter. The valuation argument uses both
\(k<2p\), so the numerator contains exactly one \(p\), and \(k<q\), so it
contains no \(q\).

For a finite-arity first crossing with positive inputs
\(m_1,\ldots,m_r<p\) and sum \(k\), composition gives

\[
\mathcal D_{m_1}\cdots\mathcal D_{m_r}
=\frac{k!}{m_1!\cdots m_r!}\mathcal D_k. \tag{27}
\]

The same valuation calculation shows that this multinomial coefficient
contains \(p\) exactly once and no \(q\).

Solving (24) or (27) for the normalized operator at the new index requires
exact division by a structure constant that is a nonunit modulo \(N\).
Its gcd with \(N\) already returns \(p\). If all normalization is postponed,
the endpoint is instead

\[
\Delta^B X^{2B}|_{X=a}=B!F_B(a). \tag{28}
\]

Here \(p\mid B!\) because \(p<B\), and Section 5 proves
\(q\mid F_B(a)\) for every integer \(a\). Therefore

\[
B!F_B(a)\equiv0\pmod N. \tag{29}
\]

The normalized monotone chain thus crosses a factor-bearing division, while
the completely unnormalized chain ends in a symmetric zero. This proof does
not cover addition--subtraction chains, cancellations, a specialized
exact-quotient decoder, or an arithmetic circuit unrelated to this operator
composition.

## 5. Universal interval content and the leading coefficient

Apply (15) with base nodes \(0,1,\ldots,B\) and translation \(a\). The
coefficient of \(a^k\) comes from \(j=B-k\):

\[
[a^k]F_B(a)=\binom{2B}{k}h_{B-k}(0,1,\ldots,B). \tag{30}
\]

By (3) at shift zero,

\[
h_{B-k}(0,1,\ldots,B)
=G_0(2B-k,B)
=\left\{\begin{matrix}2B-k\\B\end{matrix}\right\}.
\]

Thus

\[
[a^k]F_B(a)=\binom{2B}{k}
\left\{\begin{matrix}2B-k\\B\end{matrix}\right\},
\qquad 0\leq k\leq B, \tag{31}
\]

and in particular

\[
[a^B]F_B(a)=\binom{2B}{B}. \tag{32}
\]

Now let \(r\) be prime with

\[
B+1<r<2B.
\]

For every \(x\in\mathbb F_r\), Fermat reduction gives

\[
x^{2B}=x^e,\qquad e=2B-(r-1)=2B-r+1.
\]

Both exponents are positive, so this also holds at \(x=0\). The interval
for \(r\) gives \(e<B\). Hence the \(B\)-th forward difference of \(X^e\)
is zero. Since \(B<r\), \(B!\) is invertible modulo \(r\), and (B) gives

\[
F_B(a)=0\quad\text{in }\mathbb F_r
\]

for every residue \(a\). The polynomial \(F_B\) has degree \(B<r\), so a
polynomial with all \(r\) residues as roots must have every coefficient
zero modulo \(r\). The strict lower endpoint is real: if \(r=B+1\) is
prime, the reduced exponent is \(B\), whose normalized \(B\)-th difference
is 1 rather than 0.

Define

\[
P_B=\prod_{\substack{r\ {m prime}\\B+1<r<2B}}r.
\]

Distinct primes are coprime, so the preceding coefficientwise divisibility
proves

\[
P_B\mid\operatorname{content}(F_B). \tag{33}
\]

The geometry (A) places \(q\) in this product: \(h\geq s+2\geq3\) gives
\(q>B+1\), and \(q<2p<2B\). It leaves \(p\) outside because \(p<B\).

The leading coefficient determines exactly which hidden prime can divide
the content. First, \(B=p+s<2p\), \(2s<p\), and
\(2B=2p+2s<3p\). Since \(p\geq5\), there are no higher-power corrections,
and

\[
v_p(B!)=1,\qquad v_p((2B)!)=2,
\qquad v_p\binom{2B}{B}=0. \tag{34}
\]

Second, \(B<q<2B<2q\), so

\[
v_q(B!)=0,\qquad v_q((2B)!)=1,
\qquad v_q\binom{2B}{B}=1. \tag{35}
\]

It follows from (32)--(35) that

\[
\gcd(P_B,N)=q,
\qquad
\gcd(\operatorname{content}(F_B),N)=q. \tag{36}
\]

Thus explicit computation of the interval primorial, the polynomial
content, or the central-binomial leading coefficient gives a deterministic
gcd gate for \(q\). This is a warning about those explicit endpoints, not a
reduction from arbitrary black-box evaluation to content extraction. A
black-box evaluator need not expose any coefficient or content multiplier.

Let \(C_B=\operatorname{content}(F_B)\). Since the leading coefficient has
exactly one factor \(q\), both \(P_B\) and \(C_B\) have \(q\)-valuation 1.
Consequently, the leading coefficients of

\[
F_B/P_B\quad\text{and}\quad F_B/C_B
\]

are units modulo \(q\). Both quotient polynomials are nonzero modulo \(q\).
Dividing out either the explicit interval content or the full content thus
removes the universal \(q\)-zero. Individual shifts can still be roots;
only the guarantee has disappeared. Recovering the original splitter then
requires a factor-bearing multiplier or some different asymmetric
observable. This does not prove that no such observable exists.

## 6. The immediate \(N^2\) quotient and the faithful \(NB!\) quotient

The same valuation bounds give

\[
B!=pU,
\]

where \(U\) is an integer coprime to \(N\). Coefficientwise divisibility in
Section 5 gives

\[
F_B(a)=qV_B(a),\qquad V_B\in\mathbb Z[a].
\]

Therefore the raw difference is

\[
D_B(a)=B!F_B(a)=NUV_B(a). \tag{37}
\]

Suppose one computes the canonical residue
\(R=D_B(a)\bmod N^2\). It is divisible by \(N\), and exact integer division
gives

\[
R/N\equiv UV_B(a)\pmod N. \tag{38}
\]

The two guaranteed prime factors in (37) have both been divided away. The
right side of (38) is not identically zero modulo either hidden prime:

* Modulo \(p\), multiplication by \(Uq^{-1}\) is by a unit, so its zero set
  is the zero set of \(F_B\). The inherited P230 sampling statement supplies
  shifts outside that zero set.
* Modulo \(q\), (35) says the leading coefficient of \(V_B=F_B/q\) is a
  unit. Since \(\deg V_B=B<q\), there is a residue at which it is nonzero.

Choose one nonroot modulo each prime and combine them by the Chinese
remainder theorem. There are therefore shifts for which the value in (38)
is a unit modulo \(N\). The recipe “raw difference modulo \(N^2\), divide
by \(N\), take a gcd” is not a guaranteed splitter. This is only a failure
of that immediate quotient. A higher lift with a different decoder is not
excluded, but it must explain how a factor-asymmetric multiplier or
observable reappears without assuming a hidden prime or inverting a
nonunit.

There is a literal faithful quotient at a much larger modulus. Let
\(M=NB!\), and let \(S=D_B(a)\bmod M\) be the canonical residue. Both
\(D_B(a)\) and \(M\) are multiples of \(B!\), so \(S\) is a multiple of
\(B!\), and

\[
S/B!\equiv F_B(a)\pmod N. \tag{39}
\]

However,

\[
\log(NB!)=\Theta(B\log B), \tag{40}
\]

so the literal modulus has characteristic-size bit length. Moreover,

\[
\gcd(B!\bmod N,N)=\gcd(B!,N)=p. \tag{41}
\]

Materializing the normalizer or even its residue is itself factor-bearing.
Equations (39)--(41) reject the literal \(NB!\) route as a numerical
quasi-polynomial normalization. They do not reject a compressed exact
decoder that never materializes \(B!\), its residue, or the modulus.

## 7. Endpoint audit and search disposition

The identities give a complete disposition of the named grammars. They do
not supply a reason to perform a finite numerical or symbolic search within
those grammars.

1. A literal divided-difference or Stirling endpoint has \(B+1\) displayed
   terms or a triangular range of characteristic extent.
2. The complete-homogeneous coefficient vector has \(B+1\) entries.
3. Interval and parity decompositions retain a full central convolution;
   direct parity recursion has two affine children and linearly many leaves.
4. A positive monotone normalized divided-power chain encounters the
   factor-bearing structure constant at its first crossing of \(p\).
5. The fully unnormalized difference is zero modulo \(N\), so it has lost
   the required asymmetry.
6. Explicit primorial, content, factorial, and central-binomial endpoints
   expose a hidden prime by gcd.
7. The canonical constant-recurrence and constant-matrix descriptions have
   exact full-sequence state dimension \(B+1\), even after fixed-radix
   decimation.
8. The immediate \(N^2\) quotient can be a unit modulo \(N\), so it has no
   guaranteed factor.
9. A proposed generic baby-step/giant-step or holonomic endpoint whose own
   stated work is \(B^{1/2+o(1)}\) misses the requested numerical
   quasi-polynomial scale. This is a cost assessment of that endpoint, not
   a lower bound for every holonomic algorithm.
10. Exact integer materialization already has characteristic output at
    \(a=0\), because
    \(F_B(0)=\left\{\begin{smallmatrix}2B\\B\end{smallmatrix}\right\}\).
    Pair partitions alone give
    \[
    F_B(0)\geq\frac{(2B)!}{2^BB!}
             =\prod_{i=B+1}^{2B}\frac{i}{2}
             \geq(B/2)^B,
    \]
    while the elementary bound by assignments to \(B\) labeled boxes gives
    \(F_B(0)\leq B^{2B}\). Its bit length is therefore
    \(\Theta(B\log B)\). This output-size point applies to exact integer
    materialization, not modular evaluation.
11. A full-field or Frobenius collapse performed in characteristic \(p\) or
    \(q\) assumes the hidden characteristic and hence assumes a factor. It
    is not a public-modulus evaluator.

A pattern search restricted to literal rewrites of these forms can only
return another form with the stated state, convolution, product, division,
or factor-bearing endpoint unless it discovers a genuinely new aggregate.
Discovery of such an aggregate would leave the audited grammar and is not
ruled out.

In particular, none of the following inferences is valid:

* \(B+1\) nonzero translation coefficients imply an arithmetic-circuit
  lower bound.
* \(B+1\) distinct rational poles imply a lower bound for one requested
  coefficient, nonlinear state, or adaptive computation.
* A \(B+1\)-term convolution rules out fast or implicit aggregation.
* Universal content divisibility forces an evaluator to expose the content.
* Failure of the immediate \(N^2\) quotient rules out all higher-lift or
  exact-quotient decoders.
* The first-crossing proof applies to subtraction chains, branching chains,
  or unrelated circuits.

Any future synthesis proposal must therefore identify its new operation
explicitly. Before computation, it must show an exact route to
\(\exp(\operatorname{polylog}\log B)\) work and state, accept an arbitrary
public sampled shift, use only public unit-safe operations (or return a
verified factor when inversion fails), and end at a factor-asymmetric
observable rather than (29). A one-child nonlinear or adaptive law could
meet these conditions in principle; no such law is constructed here.

## 8. Exact nonclaims

This reconstruction proves none of the following:

1. a numerical quasi-polynomial evaluator for \(F_B(a)\bmod N\);
2. a lower bound for general modular evaluators or arithmetic circuits;
3. a lower bound for nonlinear, adaptive, branching, tailored, or
   noncanonical state;
4. a general nonexistence theorem for Mahler-type functional equations;
5. a reduction from arbitrary black-box evaluation to content extraction;
6. impossibility of a custom exact-division decoder on a restricted domain;
7. a factoring theorem for all inputs; or
8. an empirical result or a new literature result.

The proved result is narrower: each named literal evaluator endpoint either
retains characteristic-size structure, crosses an explicitly factor-bearing
quantity, or loses the guaranteed asymmetric factor. That classification
does not close the space of nonlinear, adaptive, or otherwise new circuits.
