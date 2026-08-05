# Proof-blind reconstruction: the canonical-isogeny-neighbor boundary

## 0. Scope, conventions, and verdicts

This note is an independent reconstruction from the bare statement.  It proves a
factoring equivalence only for **distinct odd semiprimes**.  It does not claim a
complete factoring algorithm.

The classical modular polynomial \(\Phi_\ell(X,Y)\in\mathbb Z[X,Y]\) is the
symmetric polynomial, monic in each variable, characterized in characteristic
zero by

\[
 \Phi_\ell(j(\tau),j(\ell\tau))=0.
\]

An *odd ring* below means a commutative ring in which \(2\) is a unit.  For
\(N=pq\), all congruences and schemes are over
\(R=\mathbb Z/N\mathbb Z\cong\mathbb F_p\times\mathbb F_q\).  The notation
\(u\ne0\pmod N\) means only that \(u\) is not the zero element of \(R\); it does
not mean that \(u\) is a unit.  In fact, the useful \(u\) will be a zero divisor.

Here are the verdicts proved below.

| Claim | Verdict | Exact scope |
|---|---|---|
| The three displayed specializations of \(\Phi_2,\Phi_3\) are exact | **true** | With the classical symmetric normalization above |
| Their listed exceptional collision primes are exact | **true** | Algebraically in every characteristic; the usual separable-isogeny reading also requires characteristic prime to \(\ell\) |
| The public and nonpublic two-torsion quotients of \(E_A\) have \(j=1728\) and \(j=287496\) | **true** | Any odd base on which the stated section exists; for the mixed case, componentwise over \(\mathbb Z/N\mathbb Z\) |
| A rational double coarse root implies a descended nonpublic isogeny from a fixed twist | **false** | It already fails over finite fields when \(-A\) is a nonsquare |
| The fine rank-2 subgroup task is exactly the equation \(u(u^2+A)=0\), \(u\ne0\) | **true** | \(N=pq\), distinct odd primes, \(A\in R^\times\), and Jacobi symbol \(\left(\frac{-A}{N}\right)=-1\) |
| Every valid fine output factors \(N\) | **true** | Under that same promise; both complementary gcds are identified |
| Known factors construct a fine output | **true** | Las Vegas polynomial bit complexity, using a verified square root in the residue component |
| Random \(A\) reduces arbitrary distinct-odd-semiprime factoring to the fine promise | **true** | Exact raw promise probability \((p-1)(q-1)/(2pq)\ge4/15\) |
| Returning an arbitrary coarse root or an opaque isogeny certificate suffices | **false** | A selective kernel, or a representation from which its nonidentity section can be recovered, is required |
| Irreducibility of \(\Phi_\ell\) gives a general selector lower bound | **false** | It rules out only a root in \(\mathbb Q(X)\), i.e. a universal rational-function coarse selector |
| For fixed \(\ell\), a uniform \(j\) has a discriminant collision with probability \(O_\ell(1/r)\) | **true** | Outside a finite set of primes; it says nothing about fixed special \(j\)'s |
| A fixed characteristic-zero CM ideal label automatically orients the two unknown factors | **not established, and not automatic** | The label must first be tied to compatible local endomorphism embeddings |

## 1. Exact modular-polynomial specializations

For reference, the normalized level-2 polynomial is

\[
\begin{aligned}
\Phi_2(X,Y)={}&X^3+Y^3-X^2Y^2+1488XY(X+Y)
 -162000(X^2+Y^2)\\
&+40773375XY+8748000000(X+Y)-157464000000000.
\end{aligned}
\]

Setting \(X=0\) gives

\[
\begin{aligned}
\Phi_2(0,Y)
 &=Y^3-162000Y^2+8748000000Y-157464000000000\\
 &=(Y-54000)^3.
\end{aligned}
\]

Setting \(X=1728\) and collecting coefficients gives exactly

\[
 \Phi_2(1728,Y)=(Y-1728)(Y-287496)^2.
\]

For level 3, the terms of the normalized polynomial which survive at \(X=0\)
are

\[
\begin{aligned}
\Phi_3(0,Y)={}&Y^4+36864000Y^3+452984832000000Y^2\\
 &+1855425871872000000000000Y,
\end{aligned}
\]

and hence

\[
 \Phi_3(0,Y)=Y(Y+12288000)^3.
\]

These are identities in \(\mathbb Z[Y]\), so their reductions remain identities
in every characteristic.  The exact collision sets follow by factoring the
differences of the displayed roots:

\[
\begin{aligned}
287496-1728&=285768=2^3 3^6 7^2,\\
54000-0&=54000=2^4 3^3 5^3,\\
12288000-0&=12288000=2^{15}3\,5^3.
\end{aligned}
\]

Consequently:

* in \(\Phi_2(1728,Y)\), the simple root \(1728\) and double root \(287496\)
  remain distinct exactly outside \(2,3,7\); at each of \(2,3,7\) they merge
  to one triple root;
* in \(\Phi_2(0,Y)\), the target \(54000\) equals the source \(0\) exactly in
  characteristics \(2,3,5\); and
* in \(\Phi_3(0,Y)\), the simple root \(0\) and triple root \(-12288000\)
  remain distinct exactly outside \(2,3,5\), and merge to \(Y^4\) at those
  primes.

More explicitly, \(\Phi_2(1728,Y)\) becomes \(Y^3\) in characteristics 2 and
3 and \((Y-6)^3\) in characteristic 7.  The other two collision
specializations become \(Y^3\) for \(\Phi_2(0,Y)\) and \(Y^4\) for
\(\Phi_3(0,Y)\) in each of their listed characteristics.

The algebraic identities do not fail at an exceptional prime.  What fails is
the distinction between the coarse roots (and, when the characteristic equals
the isogeny degree, the naive separable-isogeny interpretation also needs the
usual qualification).

## 2. The fine degree-2 geometry at \(j=1728\)

Let

\[
 E_A: y^2=x^3+Ax
\]

over an odd ring \(R\), with \(A\in R^\times\).  Its discriminant is
\(\Delta=-64A^3\), so it is an elliptic curve, and its \(j\)-invariant is
\(1728\).  Because the differential of \([2]\) is multiplication by the unit
\(2\), \(E_A[2]\) is finite etale of rank \(4\).  Away from the identity its
two-torsion equation is

\[
 y=0,\qquad x(x^2+A)=0.
\]

### 2.1 The public kernel

The point \(P_0=(0,0)\) exists over every such base.  For a model

\[
 y^2=x^3+a x^2+b x
\]

with kernel generated by \((0,0)\), the standard degree-2 quotient model is

\[
 y^2=x^3-2a x^2+(a^2-4b)x. \tag{2.1}
\]

Applying (2.1) with \(a=0,b=A\) gives

\[
 E_A/\langle P_0\rangle:\quad y^2=x^3-4Ax.
\]

It is again a \(j=1728\) curve.  Thus the public kernel accounts for the simple
factor \(Y-1728\) in \(\Phi_2(1728,Y)\).

### 2.2 Either nonpublic kernel

Suppose \(s\in R\) satisfies \(s^2=-A\).  Then \(P_s=(s,0)\) is a nonpublic
two-torsion point.  Translate \(x=X+s\).  Since \(s^2=-A\), the curve becomes

\[
 y^2=X^3+3sX^2+2s^2X.
\]

Formula (2.1) gives the quotient

\[
 y^2=X^3-6sX^2+s^2X. \tag{2.2}
\]

For (2.2), the standard Weierstrass quantities are

\[
 b_2=-24s,\quad b_4=2s^2,\quad b_6=0,\quad b_8=-s^4,
\]
\[
 c_4=528s^2,qquad \Delta=512s^6.
\]

Here \(s\) is a unit because \(s^2=-A\) is a unit.  Therefore the quotient is
smooth and

\[
 j=\frac{(528s^2)^3}{512s^6}
   =\frac{(16\cdot33)^3}{2^9}=8\cdot33^3=287496.
\]

The other nonpublic point \((-s,0)\) gives the same coarse \(j\).  These two
fine kernels account for the double factor \((Y-287496)^2\).

### 2.3 Why the double root need not descend from a fixed twist

Let \(R=\mathbb F_r\), with \(r\) odd, and suppose \(-A\) is a nonsquare.
Frobenius exchanges the two geometric points \((s,0)\) and \((-s,0)\).
Neither order-2 subgroup \(\{O,(s,0)\}\) or \(\{O,(-s,0)\}\) is Frobenius
stable.  Equivalently, a finite etale group of order 2 has only one geometric
nonidentity point, so a descended order-2 subgroup would force that point to be
\(\mathbb F_r\)-rational.  Hence neither nonpublic degree-2 isogeny descends
from this fixed \(\mathbb F_r\)-twist.

Nevertheless, \(287496\in\mathbb F_r\) is a root of the specialized modular
polynomial.  For \(r\notin\{2,3,7\}\) it is still a distinct double root.  This
is the precise failure of the inference

\[
 \text{rational coarse target }j'\quad\Longrightarrow\quad
 \text{isogeny from the specified source twist over the base field}.
\]

## 3. Exact formulation of the fine task

Let \(N=pq\), where \(p\ne q\) are odd primes, and let
\(A\in(\mathbb Z/N\mathbb Z)^\times\) satisfy

\[
 \left(\frac{-A}{N}\right)=-1. \tag{3.1}
\]

Write \(C_0=\{O,(0,0)\}\) for the public subgroup.  The **fine selective-kernel
task** is:

> Return a finite etale rank-2 subgroup scheme
> \(C\subset E_A[2]\) whose reduction differs from \(C_0\) in at least one CRT
> component, in a representation that explicitly returns—or permits
> deterministic polynomial-time recovery of—the unique nonidentity section
> \(P=(u,0)\).

For this task, the complete and exactly verifiable output format is simply the
canonical residue \(u\in\{0,\ldots,N-1\}\) satisfying

\[
 u(u^2+A)\equiv0\pmod N,qquad u\not\equiv0\pmod N. \tag{3.2}
\]

### 3.1 Subgroup schemes are exactly the sections in (3.2)

First let \(C\subset E_A[2]\) be finite etale of rank 2.  Its identity section
is an open-and-closed copy of the base.  Its complement is finite etale of rank
1, hence is another copy of the base and supplies a unique nonidentity section
\(P\).  Since \(P\) is nonidentity two-torsion and \(2\) is invertible, it is
affine, has \(y=0\), and has a unique coordinate \(u\) satisfying the first
part of (3.2).  The subgroup equals \(C_0\) in both CRT components exactly when
\(u=0\) in \(R\), so selectivity is exactly the second part of (3.2).

Conversely, a residue \(u\) satisfying (3.2) gives the section
\(P=(u,0)\in E_A[2]\).  It is disjoint from the identity because it lies in the
affine chart.  The map from the constant group scheme
\((\mathbb Z/2\mathbb Z)_R\) sending its nonzero section to \(P\) is a finite
etale closed subgroup of rank 2.  Thus (3.2) is not merely a necessary
coordinate test: it is exactly the desired subgroup-scheme certificate.

For completeness, translating by an arbitrary such \(u\) over the CRT ring
gives

\[
 y^2=X^3+3uX^2+(3u^2+A)X,
\]

and the componentwise quotient is represented by

\[
 y^2=X^3-6uX^2+(-3u^2-4A)X. \tag{3.3}
\]

On a component with \(u=0\), (3.3) is the public \(j=1728\) quotient.  On a
component with \(u^2=-A\), it is (2.2), with \(j=287496\).

### 3.2 Every fine output factors \(N\)

Let \(\chi_p=\left(\frac{-A}{p}\right)\) and similarly for \(q\).  Since \(A\)
is a unit, each symbol is \(\pm1\), and (3.1) says
\(\chi_p\chi_q=-1\).  Exactly one component is therefore split.  Suppose, with
no loss of generality, that \(\chi_p=-1\) and \(\chi_q=1\).

Reducing (3.2) modulo \(p\), the alternative \(u_p^2=-A\) is impossible, so
\(u_p=0\).  Modulo \(q\), either \(u_q=0\) or \(u_q^2=-A\).  The first choice
together with \(u_p=0\) would make \(u=0\pmod N\), which is excluded.  Hence
\(u_q^2=-A\), and \(u_q\ne0\) because \(A\) is a unit.  It follows exactly that

\[
 \gcd(u,N)=p,qquad \gcd(u^2+A,N)=q. \tag{3.4}
\]

The roles reverse when \(\chi_p=1,\chi_q=-1\).  Thus every valid fine output
reveals both complementary factors.  In particular, a valid selective \(u\)
can never give a trivial gcd under the promise.

### 3.3 Known factors construct the fine object

Conversely, suppose the factors are known.  Determine the two Legendre symbols.
On the unique residue component, compute and verify a square root
\(s^2=-A\); on the nonresidue component set \(u=0\).  CRT gives a unique
\(u\pmod N\).  For example, if \(-A\) is a nonresidue modulo \(p\) and a
residue modulo \(q\), then

\[
 u\equiv p\,(p^{-1}\bmod q)\,s\pmod N. \tag{3.5}
\]

This satisfies (3.2).  A standard finite-field square-root algorithm such as
Cipolla's is Las Vegas: every proposed root is checked by squaring, a suitable
auxiliary nonsquare is found with constant expected trials, and exponentiation
uses \(O(n)\) modular multiplications.  With schoolbook arithmetic, (3.5) and
the square root therefore use expected \(O(n^3)\) bit operations and
\(O(n)\) random bits; faster multiplication only improves this.  Thus the
construction is algorithmic, not just existential.

## 4. Reduction from distinct odd semiprimes

Assume a fine-task solver has uniform expected bit complexity \(Q(n)\) on every
promised input, terminates almost surely, and returns its kernel in the exposed
format above (or in a format from which \(u\) is recovered within \(Q(n)\)).

Given an arbitrary unknown \(N=pq\) with distinct odd primes:

1. Draw \(A\) uniformly from \(\{0,\ldots,N-1\}\).
2. Compute \(g=\gcd(A,N)\).  If \(1<g<N\), return \(g,N/g\); if \(g=N\),
   restart.
3. Compute the Jacobi symbol \(\left(\frac{-A}{N}\right)\).  Unless it is
   \(-1\), restart.
4. Invoke the fine solver.  Reduce its claimed \(u\) canonically, check
   \(u\ne0\), check \(u(u^2+A)\equiv0\pmod N\), and compute
   \(d=\gcd(u,N)\).  Accept only if \(1<d<N\) and \(d\mid N\), then return
   \(d,N/d\).

The verification in step 4 is exact.  Under the checked promise, Section 3.2
proves that every passing \(u\) yields a nontrivial factor.  Multiplication
checks the factorization; if desired, the two outputs can also be certified
prime by any deterministic polynomial-time primality test.  Thus no erroneous
factorization can be returned.

### 4.1 Exact raw probability

For a uniform residue \(A\pmod N\), the number of units for which the Jacobi
symbol in step 3 is \(-1\) is

\[
 2\cdot\frac{p-1}{2}\cdot\frac{q-1}{2}
   =\frac{(p-1)(q-1)}2.
\]

Therefore the exact raw probability of reaching a promised fine instance is

\[
 \alpha=\frac{(p-1)(q-1)}{2pq}. \tag{4.1}
\]

The function \((1-1/p)(1-1/q)/2\) increases with each prime.  The smallest
distinct odd primes are \(3,5\), so

\[
 \alpha\ge\frac12\cdot\frac23\cdot\frac45=\frac4{15}. \tag{4.2}
\]

Discovering a nontrivial gcd in step 2 only makes actual termination faster.
Even if those easy successes are ignored, the number of uniform residues until
a promised one is geometric with expectation \(1/\alpha\le15/4\), and the
probability of never finding one is zero.

### 4.2 Random bits and bit operations

With the prompt's \(n=\lceil\log_2(N+1)\rceil\), generate a uniform residue
exactly by drawing an \(n\)-bit integer \(W\) and rejecting \(W\ge N\).  One
uniform residue uses exactly

\[
 n\frac{2^n}{N}<2n
\]

expected random bits.  If one deliberately ignores early gcd factorizations
and waits for the promise event, the expected sampling cost is exactly

\[
 n\frac{2^n}{N}\frac1\alpha
\]

random bits, and by (4.2) it is less than \((15/2)n\).  Thus the reduction adds
\(O(n)\) expected random bits beyond those used by the fine solver.

Euclid's algorithm, the binary/Jacobi algorithm, comparisons, and the two
modular products in the verifier all have polynomial bit cost; with elementary
arithmetic they fit in \(O(n^2)\) bit operations per trial.  Modular reduction
keeps operands at \(O(n)\) bits (even an unreduced \(u^2+A\) has only \(2n+O(1)\)
bits).  Since the expected trial count is at most \(15/4\), the total expected
bit complexity is

\[
 Q(n)+O(n^2),
\]

and termination is almost sure.  If instead the fine producer is merely a
restartable bounded-error producer, exact verification converts it to Las
Vegas only when a uniform inverse-polynomial lower bound on producing a valid
\(u\) is supplied; without such a bound, no expected-polynomial conclusion is
available.

This reduction is deliberately no broader than its hypothesis: it handles
distinct odd semiprimes.  It contains no recursion or reduction for even
inputs, prime powers, repeated primes, or composites with three or more prime
factors.

## 5. Why coarse neighbors and opaque certificates are weaker

The coarse equation at the source \(j=1728\) is

\[
 \Phi_2(1728,Y)=(Y-1728)(Y-287496)^2.
\]

A task that asks for *any* root has two input-independent answers:
\(Y=1728\) and \(Y=287496\).  The first is public.  The second remains a base
field element even on a component on which neither nonpublic isogeny descends
from the fixed twist.  Neither answer reveals the selective zero divisor
\(u\).

Over a CRT ring there are also mixed coarse roots obtained by independently
choosing one displayed root in each component (when the two roots remain
distinct there).  The modular equation alone
does not say which component admits a descended nonpublic kernel.  In
particular, it permits the *wrongly oriented* mixed root that chooses
\(287496\) on the nonsplit component and \(1728\) on the split component; this
root is not the target of a degree-2 isogeny from the specified \(E_A\) over the
base ring.  Requiring a specially oriented mixed root would be an additional
fine condition, not a consequence of being a coarse root.

Likewise, a target curve, a target \(j\), or an unspecified/opaque assertion
that an isogeny exists is insufficient for the gcd reduction.  A concrete
separable degree-2 rational map does qualify if its representation lets one
recover its kernel: its kernel polynomial is linear and exposes \(u\).  More
generally, any representation is acceptable exactly when it recovers the
unique nonidentity section in polynomial time.  This is why the correct task is
the exposed selective kernel, not merely a coarse neighbor or an opaque
certificate.

The kernel proof itself remains valid when an odd factor is 3, 5, or 7: it
uses only that \(2\) and \(A\) are units.  By contrast, at factors 3 or 7 the
two \(j\)-labels in \(\Phi_2(1728,Y)\) collide, so a purported extraction based
on their difference is not uniform even on distinct odd semiprimes.  A factor
2 is excluded both by the input scope and by the etaleness argument.

## 6. Complete good-prime certificate: \(N=143\), \(A=1\)

Here \(143=11\cdot13\), and

\[
 \left(\frac{-1}{11}\right)=-1,qquad
 \left(\frac{-1}{13}\right)=1,qquad
 \left(\frac{-1}{143}\right)=-1.
\]

Take

\[
 u=44.
\]

Then \(u\equiv0\pmod{11}\) and \(u\equiv5\pmod{13}\), while
\(5^2\equiv-1\pmod{13}\).  In integers,

\[
 u^2+1=1937=13\cdot149,qquad
 u(u^2+1)=85228=143\cdot596.
\]

Thus the two kernel gcds are

\[
 \gcd(44,143)=11,qquad \gcd(1937,143)=13. \tag{6.1}
\]

The kernel is public modulo \(11\) and nonpublic modulo \(13\).  Its quotient
therefore has

\[
 j_C\equiv1728\equiv1\pmod{11},qquad
 j_C\equiv287496\equiv1\pmod{13}.
\]

The mixed target is consequently

\[
 j_C=1\pmod{143}.
\]

As a certificate-specific check,

\[
 \Phi_2(1728,1)=(-1727)(-287495)^2\equiv0\pmod{143},
\]

and the two coarse differences also happen here to expose the factors:

\[
 \gcd(1-1728,143)=11,qquad
 \gcd(1-287496,143)=13. \tag{6.2}
\]

Equation (6.2) verifies this particular mixed coarse root; it does not turn the
task “return any coarse root” into a selective-kernel task.

### 6.1 The complete power identities in \(\mathbb F_r[T]/(T^2+1)\)

Let \(B_r=\mathbb F_r[T]/(T^2+1)\), and write \(t\) for the residue class of
\(T\).  For every positive odd integer \(m\), the defining relation gives

\[
 t^m=(-1)^{(m-1)/2}t. \tag{6.3}
\]

Since \(143\equiv3\pmod4\), for every \(i\ge1\), in **both** \(B_{11}\) and
\(B_{13}\),

\[
 t^{143^i}-t=
 \begin{cases}
  -2t,&i\text{ odd},\\
  0,&i\text{ even}.
 \end{cases} \tag{6.4}
\]

The true one-step local Frobenius identities are different:

\[
 \begin{array}{c|c|c|c}
 r & T^2+1\text{ over }\mathbb F_r & t^r & t^r-t\\ \hline
 11 & \text{irreducible} & -t & -2t\ne0\\
 13 & (T-5)(T+5) & t & 0.
 \end{array} \tag{6.5}
\]

Indeed, \((-1/r)=(-1)^{(r-1)/2}\); hence \(-1\) is a nonsquare modulo 11 and
a square modulo 13, with \(5^2=-1\pmod{13}\).  The element \(-2t\) is nonzero
in either quotient because \(-2\ne0\) and the degree-one representative is not
in the ideal generated by the monic quadratic.

Thus odd \(i\) in (6.4) gives the same answer on both CRT components, and even
\(i\) gives the other same answer on both.  No \(143^i\)-power identity
reproduces the selective local pair \((-2t,0)\) from (6.5).  Raising to an
\(N\)-power over \(\mathbb Z/N\mathbb Z\) is not a substitute for the two true
prime-characteristic Frobenius maps.

## 7. What generic irreducibility and discriminants do—and do not—prove

### 7.1 Irreducibility excludes only a rational-function selector

For prime \(\ell\), the modular curve \(X_0(\ell)\) is connected, and the map
to the \(j\)-line which forgets the cyclic subgroup has generic degree
\(\ell+1\).  Equivalently, the coset action on the \(\ell+1\) cyclic subgroups
is transitive.  Its function-field equation is
\(\Phi_\ell(X,Y)=0\).  Hence \(\Phi_\ell\) is irreducible over
\(\mathbb Q(X)\) (and, with the chosen primitive integral normalization, over
\(\mathbb Q[X,Y]\)).

If a universal rational function \(f(X)\in\mathbb Q(X)\) selected a coarse
neighbor, then

\[
 \Phi_\ell(X,f(X))=0.
\]

The polynomial \(Y-f(X)\) would then be a degree-one factor of
\(\Phi_\ell(X,Y)\) in \(\mathbb Q(X)[Y]\), contradicting irreducibility because
\(\deg_Y\Phi_\ell=\ell+1>1\).

That is the entire conclusion.  It does not exclude selectors using extra
level structure, a chosen curve model or twist, endomorphism embeddings,
algebraic extensions, characteristic-dependent information, the modulus
\(N\), or non-rational algorithms.  It also says nothing against selectors at
special \(j\)-values, as the explicit factorizations at \(0\) and \(1728\)
already demonstrate.  It is not a computational lower bound and not a general
selector impossibility theorem.

### 7.2 Fixed-\(\ell\), uniform-\(j\) collision bound

Fix \(\ell\), and let

\[
 D_\ell(X)=\operatorname{disc}_Y\Phi_\ell(X,Y)\in\mathbb Z[X].
\]

Characteristic-zero irreducibility implies separability, so
\(D_\ell\ne0\).  Write \(D_\ell=cD_\ell^{\rm prim}\), where
\(D_\ell^{\rm prim}\) is primitive, and put
\(d_\ell=\deg D_\ell^{\rm prim}\).  Outside the finite set of prime divisors
of \(c\), its reduction is a nonzero polynomial.  Because \(\Phi_\ell\) is
monic in \(Y\), two geometric roots of \(\Phi_\ell(j,Y)\) collide only if
\(D_\ell(j)=0\).  Therefore, for uniform \(J\in\mathbb F_r\),

\[
 \Pr\bigl[\Phi_\ell(J,Y)\text{ has a repeated geometric root}\bigr]
 \le \min\!\left(1,\frac{d_\ell}{r}\right). \tag{7.1}
\]

This is a fixed-\(\ell\) uniform-input statement.  It gives no small bound for
an adversarial or fixed CM value such as \(0\) or \(1728\), where the
characteristic-zero specialization itself already has repeated roots.

## 8. The narrow CM boundary and surviving scope

A characteristic-zero CM ideal \(\mathfrak a\) labels an isogeny only relative
to an embedding

\[
 \iota:\mathcal O\hookrightarrow\operatorname{End}(E):
 \qquad E[\mathfrak a]=\bigcap_{\alpha\in\mathfrak a}\ker\iota(\alpha).
\]

After CRT reduction, one needs local embeddings \(\iota_p\) and \(\iota_q\).
An abstract fixed ideal label alone neither supplies those embeddings nor proves
that their orientations are compatible.  Composing one local embedding with
complex conjugation can replace \(\mathfrak a\) by \(\bar{\mathfrak a}\) while
leaving the underlying coarse \(j\)-invariant unchanged.  Thus a fixed
characteristic-zero label is **not automatically** an orientation of the two
unknown factors.  This is a missing-data/compatibility observation, not an
impossibility theorem.

In particular, nothing here closes routes based on higher-class-number CM,
explicitly supplied or recoverable endomorphism embeddings, vertical
isogenies, supersingular structure, or selectors that depend essentially on
\(N\).  Nor does this note prove a general selector lower bound.

The precise surviving positive result is only this:

> On distinct odd semiprimes and under the checkable Jacobi promise, producing
> an exposed selective rank-2 kernel is equivalent to producing the mixed
> solution \(u\) in (3.2), and that solution factors \(N\) immediately.  Random
> \(A\) reaches the promise with the exact constant probability (4.1).

Explicitly excluded are even inputs, repeated primes, prime powers,
multifactor inputs, a complete recursive factorization argument, extraction
from an arbitrary coarse \(j\)-root, extraction from an opaque certificate, a
general selector lower bound, and any claimed closure of the
embedding-sensitive, higher-class-number, vertical, supersingular, or
\(N\)-dependent CM possibilities.
