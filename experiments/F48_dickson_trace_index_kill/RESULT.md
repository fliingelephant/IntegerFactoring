# F48 — mandatory proof-only kill test for the ordinary Dickson trace index

**Status:** candidate proof-only kill result. No finite computation and no
web search were used.

**Family:** F28.

**Closest promoted routes.** P12/F07 shows that natural dense spectral
reconstruction can have exponential support, but does not address
binary-indexed recurrences or explicit arithmetic coordinates. P55/F27 gives
an exact signed gap in discriminant-dependent Lucas tori and a generic
shared-exponent obstruction. The present route is materially different: it
uses the ordinary unit group, has no random discriminant or hidden torus
orientation, and exposes two factor-determining integer representatives of
one globally valid trace-function alias class.

**Conclusion.** Polynomially many powers, products, repeated bases, and
Dickson addition/composition identities do not create independent equations:
they are exact functorial consequences of the same power map or trace
function. The full trace alias class of the public exponent \(N-1\) is

\[
 m\equiv \pm(p+q-2),\ \pm(q-p)
 \pmod{\operatorname{lcm}(p-1,q-1)}.
\]

Thus trace data do not distinguish the two positive factor-determining
representatives. This is a narrow method failure for “amortize the displayed
structured relations until the index localizes,” not a lower bound against
explicit arithmetic over \(\mathbb Z/N\mathbb Z\). In particular, coherent
mixed-root selection, numerical-coordinate resultants, useful gcd events,
non-generic interval algorithms, and lifts modulo \(N^2\) are not ruled out.

## 1. Exact Dickson identities

Let

\[
 N=pq,\qquad 3\le p<q
\]

with \(p,q\) distinct odd primes, let

\[
 R=\mathbb Z/N\mathbb Z,\qquad U=R^\times,
\]

and put

\[
 e=N-1,\qquad s=p+q,\qquad t=s-2,\qquad g=q-p.
\]

Define the monic Dickson polynomials

\[
 D_0(X)=2,\qquad D_1(X)=X,\qquad
 D_{j+1}(X)=XD_j(X)-D_{j-1}(X),
\]

and set \(D_{-j}=D_j\).

### Lemma 1.1 — universal trace formula

For every commutative ring \(A\), every unit \(a\in A^\times\), and every
integer \(j\),

\[
 D_j(a+a^{-1})=a^j+a^{-j}.
\tag{1.1}
\]

**Proof.** The right side has initial values \(2,a+a^{-1}\) and satisfies
the same recurrence, since

\[
 (a+a^{-1})(a^j+a^{-j})
 =(a^{j+1}+a^{-j-1})+(a^{j-1}+a^{-j+1}).
\]

The negative-index assertion is immediate. \(\square\)

For a unit \(a\), define

\[
 T(a)=a+a^{-1},\qquad F_j(a)=T(a^j)=D_j(T(a)).
\]

Fermat's theorem in the two CRT components gives

\[
 e\equiv q-1\pmod{p-1},\qquad
 e\equiv p-1\pmod{q-1}.
\tag{1.2}
\]

Also

\[
 e-t=(p-1)(q-1),
\tag{1.3}
\]

and

\[
 e-g=(p-1)(q+1),\qquad
 e+g=(q-1)(p+1).
\tag{1.4}
\]

Consequently, for every \(a\in U\),

\[
 a^e=a^t
\tag{1.5}
\]

in both CRT components, hence in \(R\), while

\[
 a^e\equiv a^g\pmod p,\qquad
 a^e\equiv a^{-g}\pmod q.
\tag{1.6}
\]

Taking inversion-invariant traces proves the two advertised identities:

\[
 \boxed{F_e(a)=D_e(T(a))=D_t(T(a))=D_g(T(a))=F_g(a).}
\tag{1.7}
\]

Thus the public pair

\[
 x=T(a),\qquad y=F_e(a)
\]

obeys

\[
 y=D_{q-p}(x)=D_{p+q-2}(x)\pmod N.
\]

The unsymmetrized value \(b=a^e\), which is just as publicly computable,
retains the stronger same-sign identity \(b=a^t\).

## 2. Full classification of trace-index aliases

### Lemma 2.1 — one-prime classification

Let \(r\) be an odd prime. For integers \(u,v\), the following are
equivalent:

1. \(z^u+z^{-u}=z^v+z^{-v}\) for every
   \(z\in\mathbb F_r^\times\);
2. \(u\equiv v\pmod{r-1}\) or
   \(u\equiv-v\pmod{r-1}\).

**Proof.** The functions

\[
 \chi_j(z)=z^j,\qquad j\in\mathbb Z/(r-1)\mathbb Z,
\]

are linearly independent over \(\mathbb F_r\). Indeed, multiplying a
linear relation by \(z^{-k}\) and summing over
\(\mathbb F_r^\times\) isolates the \(k\)-th coefficient because

\[
 \sum_{z\in\mathbb F_r^\times}z^h
 =
 \begin{cases}
 r-1,&r-1\mid h,\\
 0,&r-1\nmid h,
 \end{cases}
\]

and \(r-1\ne0\) in \(\mathbb F_r\). Equality of the two trace functions
therefore says that the coefficient multisets of
\(\chi_u+\chi_{-u}\) and \(\chi_v+\chi_{-v}\) agree. Because \(r\) is odd,
the possible coefficient \(2\) when \(u\equiv-u\) does not disappear.
Hence the two inversion orbits are equal. \(\square\)

### Theorem 2.2 — global alias relation

For any integers \(u,v\), the following are equivalent:

\[
 F_u(a)=F_v(a)\quad\text{for every }a\in U;
\tag{2.1}
\]

\[
 u\equiv\epsilon_pv\pmod{p-1},\qquad
 u\equiv\epsilon_qv\pmod{q-1}
\tag{2.2}
\]

for some independently chosen
\(\epsilon_p,\epsilon_q\in\{+1,-1\}\).

**Proof.** CRT lets the \(p\)- and \(q\)-coordinates of a unit vary
independently. Apply Lemma 2.1 in each coordinate. \(\square\)

Let

\[
 L=\operatorname{lcm}(p-1,q-1).
\]

Applying Theorem 2.2 to \(v=e\), the four sign patterns have the explicit
representatives

\[
 \begin{array}{c|c}
 (\epsilon_p,\epsilon_q)&\text{representative modulo }L\\ \hline
 (+,+)&t=p+q-2\\
 (+,-)&g=q-p\\
 (-,+)&-g\\
 (-,-)&-t.
 \end{array}
\]

Therefore

\[
 \boxed{
 F_m=F_e\text{ on }U
 \iff
 m\equiv t,-t,g,\text{ or }-g\pmod L.}
\tag{2.3}
\]

This includes all aliases, including coincidences among the four residue
classes when the local exponents have extra symmetry.

For comparison, equality of unsymmetrized power maps has only the
same-sign class:

\[
 a^m=a^e\text{ for every }a\in U
 \iff m\equiv e\equiv t\pmod L.
\tag{2.4}
\]

Thus retaining \(b=a^e\) removes the independent local sign ambiguity but
does not reveal the least positive representative \(t\). The mixed
representative \(g\) is also a power-map representative exactly when
\(q-1\mid2(p-1)\); because \(p<q\), this is exactly the exceptional relation
\(q=2p-1\).

### Consequence for coexistence of the two aliases

The coexistence is:

* helpful only in the weak sense that either exact positive representative
  \(g\) or \(t\) is an acceptable factoring witness;
* neutral for every identity that depends only on the function \(F_e\),
  because both representatives define exactly that same function;
* obstructive to any assertion that the values identify a unique integer
  index, because even the complete value table cannot choose between the
  two sign patterns.

An arbitrary member of the four residue classes, after adding an unknown
multiple of \(L\), is not automatically a short or factor-determining
integer. The useful target is an exact representative, not merely an
unverified congruence class.

## 3. Both small representatives factor, with exact verification

### Lemma 3.1 — gap decoder

Given \(N\) and the exact nonnegative integer \(h=q-p\), compute

\[
 S^2=h^2+4N.
\]

For the true \(h\), \(S=p+q\), and

\[
 p=\frac{S-h}{2},\qquad q=\frac{S+h}{2}.
\tag{3.1}
\]

A candidate is accepted only if \(h^2+4N\) is an exact square, the two
numerators are even, both factors exceed one, and their product is \(N\).

### Lemma 3.2 — trace decoder

Given the exact nonnegative integer \(u=p+q-2\), put \(S=u+2\) and compute

\[
 \Delta=S^2-4N.
\]

For the true \(u\), \(\Delta=(q-p)^2\), and

\[
 p=\frac{S-\sqrt\Delta}{2},\qquad
 q=\frac{S+\sqrt\Delta}{2}.
\tag{3.2}
\]

Again, exact squareness, parity, positivity, and product are complete
verification.

Integer square root, parity tests, multiplication, and comparison have
polynomial bit complexity in \(n+\operatorname{bitlength}(h)\) or
\(n+\operatorname{bitlength}(u)\). Therefore a polynomial-time decoder must
output a polynomial-bit candidate. Running both verified decoders on the
absolute value of a candidate is Las Vegas safe: a false candidate is never
accepted unless it nevertheless supplies a correct factorization.

These lemmas make index recovery the entire missing step; the final
discriminant is not a hidden cost.

## 4. Structured many-base relations are tautological

The Dickson identities

\[
 D_j(D_k(X))=D_{jk}(X),
\tag{4.1}
\]

\[
 D_{u+v}(X)+D_{u-v}(X)=D_u(X)D_v(X)
\tag{4.2}
\]

follow immediately from (1.1).

For all units \(a,b\) and every integer \(k\),

\[
 T(a^k)=D_k(T(a)),
\qquad
 F_e(a^k)=D_k(F_e(a)).
\tag{4.3}
\]

Thus the pair for the power-related base \(a^k\) is exactly

\[
 \bigl(D_k(x),D_k(y)\bigr).
\tag{4.4}
\]

It is a deterministic image of the original pair and supplies no new
constraint on the hidden representative.

Products obey

\[
 T(a)T(b)=T(ab)+T(ab^{-1}),
\tag{4.5}
\]

\[
 F_e(a)F_e(b)=F_e(ab)+F_e(ab^{-1}).
\tag{4.6}
\]

The unsymmetrized map \(B_e(a)=a^e\) is a homomorphism:

\[
 B_e(ab)=B_e(a)B_e(b),\qquad B_e(a^k)=B_e(a)^k.
\tag{4.7}
\]

Equations (4.3)--(4.7) hold for every exponent representative of the
appropriate power or trace alias class. Repeated bases only repeat them;
chosen products only instantiate them at another public unit.

More generally, suppose an adaptive procedure chooses each next unit using
the preceding public residues and then forms any ring expression from
\(T(a_i)\) and \(F_e(a_i)\). Replacing \(e\) by any \(m\) satisfying (2.3)
leaves every query answer unchanged, and induction leaves the whole
transcript unchanged. This is exact representative non-identifiability in
the trace-function interface.

It is not an information-theoretic or computational lower bound for
factoring: \(N\) and the residues are explicit, and a procedure can exploit
coordinate arithmetic outside this interface. It proves only that the
displayed structured identities themselves do not accumulate independent
index equations.

## 5. Shifted traces, resultants, and the missing mixed root

The addition law exposes the smallest exact obstruction behind a tempting
resultant attack. Fix one public unit \(a\), write

\[
 X=T(a),\qquad Y=D_e(X),
\]

and choose any public integer \(k\). Put

\[
 K=D_k(X),\qquad
 A=D_{e+k}(X),\qquad B=D_{e-k}(X).
\]

All these residues are public and evaluable by binary powering. Equations
(4.2) and its product analogue give

\[
 A+B=YK,
\tag{5.1}
\]

\[
 AB=D_{2e}(X)+D_{2k}(X)=Y^2+K^2-4.
\tag{5.2}
\]

Hence \(A,B\) are the two displayed global roots of

\[
 P_k(Z)=Z^2-YKZ+(Y^2+K^2-4).
\tag{5.3}
\]

For the mixed-sign representative \(g\), the two values

\[
 C=D_{g+k}(X),\qquad D=D_{g-k}(X)
\]

obey the same sum and product. Locally at \(p\), the pair \((C,D)\) has the
same ordering as \((A,B)\); locally at \(q\), it has the opposite ordering.
Thus \(C,D\) are precisely the CRT-mixed roots of the already split
quadratic (5.3).

Before using this observation, screen

\[
 \gcd(A-B,N).
\]

A proper gcd is already a factor. If \(A-B\) is a unit, any CRT-mixed root
\(C\) immediately factors:

\[
 \gcd(C-A,N)\in\{p,q\}.
\tag{5.4}
\]

If \(A-B\) vanishes in both components, this \(k,a\) is degenerate and gives
no root orientation.

Therefore the trace addition law supplies only the symmetric coefficients
of a quadratic whose two global roots are already known. Producing the
mixed root that would encode \(g\) is exactly a modular root-selection
problem sufficient to factor. A resultant or quadratic formula does not
select that root for free. Polynomially many such quadratics share a
coherent hidden CRT orientation, so a genuinely new amortized mixed-root
algorithm is still conceivable; none is proved here.

The obvious “lucky relation” gcds must not be discarded. For example,

\[
 A-B=(a^e-a^{-e})(a^k-a^{-k}),
\]

so gcds of \(Y^2-4\), \(K^2-4\), or \(A-B\) with \(N\) can split special
inputs or bases. There is no proved inverse-polynomial lower bound on their
proper-gcd probability for every semiprime: they are ordinary local-order
events. An all-input route must prove such a bound or add another mechanism.

## 6. Derivatives do not follow from value aliases

Over \(\mathbb Z[X]\), Dickson polynomials satisfy

\[
 (X^2-4)D_m'(X)
 =m\bigl(D_{m+1}(X)-D_{m-1}(X)\bigr),
\tag{6.1}
\]

\[
 (X^2-4)D_m'(X)^2
 =m^2\bigl(D_m(X)^2-4\bigr).
\tag{6.2}
\]

These follow after substituting \(X=z+z^{-1}\), and hence as polynomial
identities.

However, equality of \(D_m\) and \(D_e\) on the finite trace set
\(\{z+z^{-1}:z\in\mathbb F_r^\times\}\) is equality of functions, not
equality of formal polynomials. It gives no equality of their formal
derivatives. Interpolation of all values does not canonically choose a
polynomial representative or its derivative; an infinitesimal or
multiplicity datum would be additional information.

Moreover, the scale factor \(m\) in (6.1)--(6.2) can vanish in a local
characteristic. For the genuine gap \(g\), neither \(p\) nor \(q\) divides
\(g\), but \(p\mid t\) can occur when \(q\equiv2\pmod p\). Thus division by
the candidate index is not a uniform step even on the promised family.

A derivative-based route survives only if it constructs the derivative or
an equivalent oriented infinitesimal from public data in polynomial bit
complexity. Merely differentiating a guessed \(D_m\) presupposes the missing
index.

## 7. Lifting to \(N^2\) is new data, not the same identity

The equality \(a^e=a^t\) used only the local fields modulo \(p\) and \(q\).
It generally fails modulo \(N^2\). Let \(\widetilde a\) be a unit lift
modulo \(N^2\), let

\[
 \varphi=(p-1)(q-1)=e-t,
\]

and define its Euler quotient

\[
 Q_{\widetilde a}
 =\frac{\widetilde a^\varphi-1}{N}\pmod N.
\]

Then

\[
 \widetilde a^e
 \equiv \widetilde a^t(1+NQ_{\widetilde a})\pmod{N^2},
\]

and therefore

\[
 T(\widetilde a^e)-T(\widetilde a^t)
 \equiv
 NQ_{\widetilde a}
 \bigl(\widetilde a^t-\widetilde a^{-t}\bigr)
 \pmod{N^2}.
\tag{7.1}
\]

The unknown quotient uses the factor-determining exponent
\(\varphi=N-(p+q)+1\). Formula (7.1) shows why the mod-\(N\) alias does not
automatically lift. It neither supplies \(Q_{\widetilde a}\) nor rules out a
polynomial-time way to pool these discrepancies. A lift-modulo-\(N^2\)
decoder is a materially new F28 mechanism and remains open.

## 8. Interval and BSGS accounting

For balanced semiprimes, \(t=p+q-2=\Theta(\sqrt N)\), while \(g\) may range
from very small to \(\Theta(\sqrt N)\). For unbalanced semiprimes, such as
\(p\) fixed and \(q\) growing, both useful representatives can be
\(\Theta(N)\). Enumerating a candidate interval of exponential cardinality
is not polynomial in \(n\); ordinary baby-step--giant-step on an interval of
size \(H\) costs \(\Theta(\sqrt H)\) group operations and is still
exponential when \(H=2^{\Theta(n)}\).

If an independent metric argument shrinks the candidate set to
\(\operatorname{poly}(n)\), direct discriminant verification already gives
a polynomial algorithm. The missing theorem is exactly such a shrinkage or
a non-enumerative explicit-coordinate decoder. No complexity claim may
count a Dickson polynomial of degree \(m\) as a constant-size object merely
because \(m\) is binary encoded: evaluation by fast doubling is cheap, but
expansion, generic resultants, and coefficient output can have size
\(\Omega(m)\).

## 9. A generic quotient-by-inversion boundary

The following theorem tests only the claim that many opaque relations force
recovery by their number.

### Model

Let \(\ell\) be an odd prime and let \(E\) be uniform in
\(\mathbb F_\ell\). For each of \(K\) independent tags, an oracle randomly
and injectively encodes inversion orbits

\[
 [z]=\{z,-z\}\subset\mathbb F_\ell.
\]

Initially it gives labels for

\[
 [0],\qquad[1],\qquad[E].
\]

Within one tag, an adaptive algorithm may make either of two oracle calls:

1. from \([u]\) and public \(c\), obtain \([cu]\);
2. from \([u]\) and \([v]\), obtain the unordered pair
   \(\{[u+v],[u-v]\}\).

The second call grants the two branches behind the trace addition law,
rather than only their symmetric sum. No cross-tag call or inspection of
the random encodings is allowed. Unlimited ordinary computation and
adaptivity are allowed between at most \(Q\) total oracle calls.

### Theorem 9.1 — trace-orbit shared-index bound

If the algorithm outputs a list of at most \(M\) residues, then

\[
 \Pr\bigl[\exists h\text{ in the list}:h=\pm E\bigr]
 \le
 \min\left\{
 1,\frac{2M+B}{\ell}
 \right\},
\tag{9.1}
\]

where, writing \(q_i\) for the calls in tag \(i\),

\[
 B=2\sum_{i=1}^K\binom{2q_i+3}{2}
 \le
 2\binom{2Q+3}{2}+6(K-1).
\tag{9.2}
\]

In particular, polynomially many tags and calls have only
quadratic-generic success when \(\ell\) is exponential in the input length.

**Proof.** Run a symbolic execution with indeterminate \(Z\). Every orbit
handle is represented by an affine form

\[
 [\alpha+\beta Z],
\]

canonicalized up to multiplication by \(-1\). A scalar call creates at most
one new formal orbit, and an addition-pair call creates at most two. Thus tag
\(i\) sees at most \(2q_i+3\) formal handles.

Two formally distinct orbit handles can become equal at the secret \(E\)
only if

\[
 f(E)=g(E)\quad\text{or}\quad f(E)=-g(E).
\]

Each nonidentity affine equation has at most one root, so each pair
contributes at most two bad secret values. This proves the first expression
for \(B\). Convexity, with \(\sum q_i=Q\), gives the second.

Outside this union of bad values, the real execution couples exactly to a
lazy symbolic execution in which every new formal orbit receives a fresh
random label. That symbolic transcript, including all adaptive choices and
random coins, is independent of \(E\). A fixed output list covers at most
\(2M\) field values after allowing inversion, contributing \(2M/\ell\);
the bad set contributes at most \(B/\ell\). \(\square\)

The same proof gives the required prior variants. If \(E\) is uniform on a
public \(H\)-element subset, including a nonwrapping interval, then

\[
 \Pr[\text{list success}]
 \le\min\left\{1,\frac{2M+B}{H}\right\}.
\tag{9.3}
\]

For an arbitrary public prior of maximum point mass \(\mu_*\),

\[
 \Pr[\text{list success}]
 \le\min\{1,(2M+B)\mu_*\}.
\tag{9.4}
\]

If the prior and output are already distributions/lists of inversion
orbits, the factor \(2\) on \(M\) is replaced by \(1\).

There is also a stronger-access full generic-group variant. Give each tag
ordinary random encodings for exponents \(0,1,E\) in a cyclic group of prime
order \(\ell\), and allow \(Q\) full group operations and equality tests.
Every handle remains affine in \(E\). If \(q_i\) new handles are made in tag
\(i\), at most

\[
 C=\sum_i\binom{q_i+3}{2}
 \le\binom{Q+3}{2}+3(K-1)
\]

secret values cause a surprise collision. Therefore a list of \(M\)
representatives succeeds up to inversion with probability at most

\[
 \min\left\{1,\frac{2M+C}{\ell}\right\},
\tag{9.5}
\]

with the same subset and maximum-prior-mass substitutions. This is the
quotient-output analogue of the affine generic argument in P55.

### Non-generator and transfer caveats

Prime order makes every nonidentity input a generator. For a base of
composite order \(d\), the index is visible only modulo \(d\) up to sign,
and a nontrivial affine congruence can have
\(\gcd(\text{slope},d)\) roots rather than one. Bounds (9.1) and (9.5) then
require an explicit root-multiplicity parameter. Small-order bases can leak
short congruences; polynomially many bases can reconstruct an index only if
their order information and compatibility are themselves available. Those
orders must not be obtained by a hidden order-finding or factoring call.

Neither generic theorem transfers to F28's explicit residues:

* the local orders \(p-1\) and \(q-1\) are unequal and composite;
* sampled units can be non-generators;
* all bases inhabit one public group and products are explicitly correlated;
* one residue carries two CRT components and gcds can expose their
  disagreement;
* the encodings are numerical ring coordinates, so addition, multiplication,
  resultants, and lifts can inspect more than equality;
* \(g,t\) are worst-case arithmetic functions of \(N\), not uniform generic
  secrets.

The theorem closes only opaque shared-index pooling and gives no hardness
result for \(\mathbb Z/N\mathbb Z\).

## 10. Scope and edge cases

### Nonunits and gcd tickets

For every proposed base, compute \(\gcd(a,N)\) before inversion. A proper
gcd factors \(N\); gcd \(N\) rejects the base; gcd \(1\) permits the inverse.
Every denominator, difference, discriminant, derivative scale, or resultant
coefficient introduced later must receive the same treatment. A proof may
not condition these events away, because a proper gcd is a successful
branch and a zero value in both components can change the algebra.

### Candidate indices divisible by a hidden prime

For \(0<g=q-p<q\), neither \(p\) nor \(q\) divides \(g\): either divisibility
would force one distinct prime to divide the other. Also \(q\nmid t\), but
\(p\mid t\) can occur. The discriminant decoders remain correct in every
case; only derivative divisions or characteristic-sensitive manipulations
are endangered.

### Inputs outside the promise

* If \(p=q\), the CRT field proof disappears. Modulo \(p^2\),
  \(a^{p^2-1}=a^{2p-2}\) is not a universal identity, and the gap
  representative \(0\) is useless.
* For prime powers, local unit exponents contain powers of the prime; the
  reductions (1.2)--(1.4) no longer prove the stated identities.
* For three or more prime factors, \(N-1\) has a separate residue modulo
  each \(r_i-1\); there is no single two-variable sum/gap discriminant.
* The characteristic-two trace quotient degenerates, so even inputs are
  outside the theorem.
* For prime \(N\), \(a^{N-1}=1\) and the trace is the constant \(2\), giving
  no factor.

Thus even a complete promise decoder for \(g\) or \(t\) would still require
prime-power handling, arbitrary multifactor input handling, recursion,
primality testing, and a total expected bit-complexity proof.

### Bit complexity and hidden calls

On the promised family, unit sampling with gcd screening, inversion, the
values \(x,y,b\), and any polynomial number of binary-indexed Dickson
evaluations use polynomially many operations on \(O(n)\)-bit residues.
Candidate discriminants are verifiable in polynomial bit complexity when
the candidate itself has polynomial bitlength.

By contrast, expanding degree-\(m\) polynomials, enumerating
\(\Theta(m)\) coefficients, a \(\sqrt H\)-step BSGS over exponential \(H\),
or materializing an exponential trace table is not polynomial in \(n\).
Selecting a local generator, learning \(p-1\) or \(q-1\), computing
\(\lambda(N)=L\), or invoking an ordinary discrete-log/order-finding oracle
must be charged. In particular, knowing a suitable multiple of the group
exponent is already sufficient for standard randomized splitting on
distinct odd composites, so it cannot be treated as harmless preprocessing.

## 11. Classification and exact reopen conditions

**Classification:** narrow method failure for the auxiliary assertion that
polynomially many displayed ordinary-unit relations become independent and
localize one symmetric invariant. Powers, products, repeats, Dickson
composition, and trace addition remain inside one exactly classified alias
function. The generic prime-order quotient also stays at birthday scale.

This is not a failure of every explicit-coordinate F28 decoder and is not a
refutation of the top-level factoring statement.

A retry is materially new only if it supplies at least one of:

1. a uniform explicit-coordinate algorithm that selects a coherent
   CRT-mixed root from polynomially many quadratics such as (5.3), with a
   proved inverse-polynomial all-input success bound;
2. a derivative, resultant, determinant, or additive invariant actually
   computable from the public residues and not merely a reformulation of the
   missing index or modular root;
3. a modulo-\(N^2\) pooling law that controls the Euler-quotient discrepancy
   (7.1) without first recovering \(\varphi(N)\), an order, or a factor;
4. a factor-free interval/list mechanism shrinking the exact integer
   candidates to polynomial size, or a genuinely non-enumerative
   binary-index decoder with full bit-cost analysis;
5. a proved useful distribution of non-generator/order events, including
   every gcd branch, whose success is inverse-polynomial for every input;
6. after a promise decoder, a uniform extension covering prime powers,
   repeated factors, even inputs, multifactor composites, recursion, and
   complete Las Vegas expected bit complexity.

The smallest exact obstruction is therefore not “one gcd at the end.” It is
that every currently manufactured structured relation is invariant under
the same independent local inversion symmetry, while the first object that
breaks that symmetry—a mixed shifted trace, an oriented derivative, or a
nontrivial lift—is already additional factor-sensitive data whose
polynomial-time manufacture remains unproved.
