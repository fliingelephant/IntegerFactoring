# F202 hostile audit

## Verdict

**PASS, as the narrow conditional boundary stated by the packet.**  I found
no false algebraic identity, range failure, mixed-root omission, congruence
exception, ideal-class sign error, improper use of a conductor-supported
ideal, or defect in the \(N=2627\) certificate.

There is one necessary recursion qualification.  The displayed recurrence
is valid cost accounting when the recursive call is a correct complete
factorization call on an arbitrary smaller integer.  A postprocessor whose
correctness is promised only for balanced squarefree semiprimes does not by
itself supply that all-input child routine, because \(E\) need not satisfy
the promise.  The frozen packet explicitly says that it is not a factoring
algorithm and that the recurrence proves only complexity safety.  Under
that stated reading, the claim passes.  It must not be promoted as saying
that the promised postprocessor alone closes an all-input recursion.

I did not edit a frozen input or a durable ledger.  I did not run a
mathematical computation, numerical search, computer-algebra calculation,
or experimental form reduction.  The finite checks below are exact hand
derivations from the displayed integers.

## Frozen-input integrity

Before reading the statement, proof, or self-audit, I hashed all files and
then read only `MANIFEST.md`.  The three declared frozen hashes matched:

- `STATEMENT.md`:
  `266e527434b5c6b9f3a680b0ea31498cd8f55411d1ec75a459f4d8bd21587719`
- `PROOF.md`:
  `7a7227718561de054330a1ae29c128e20e1bff477125370856376fcb7759e8cf`
- `SELF_AUDIT.md`:
  `9b0d0eb4db936359b15b6b4f8dc1502c44eb4c39679bed1597691ea61319f5cd`

The task supplied no independent digest for the manifest.  Its pre-read
SHA-256 was
`7936c53b96f7b5b256494f7eec0ca8ecff842afdc0450705e1e1eaef03967e2a`.

## 1. Square-gap coordinates

Since (p<q),

\[
 p<\sqrt{pq}<q.
\]

The first inequality and integrality of (p) give (p\leq B), while the
second gives (B<q).  Therefore

\[
 a=B-p\geq0,
 \qquad
 c=q-B>0.
\]

Using (p=B-a), (q=B+c), and (d=c-a), direct expansion gives

\[
 N=(B-a)(B+c)=B^2+B(c-a)-ac,
\]

so

\[
 \boxed{E=Bd-ac}.
\]

The two norm identities follow without division:

\[
 a^2+E
 =a^2+B(c-a)-ac
 =(B-a)(c-a)=pd,
\]

\[
 c^2+E
 =c^2+B(c-a)-ac
 =(B+c)(c-a)=qd.
\]

Also

\[
 d=c-a=p+q-2B.
\]

Strict AM--GM applies because (p\ne q):

\[
 p+q>2\sqrt{pq}\geq2B.
\]

Thus (d>0).  Both primes and (2B) are even after summation, so (d)
is even.  Since (B\geq p),

\[
 d=p+q-2B\leq q-p.
\]

Balance gives (q-p<p).  Hence the stated weaker lower bound and exact
upper bounds are sound:

\[
 1\leq d\leq q-p<p.
\]

The possible endpoint (a=0) causes no algebraic exception.  It falls on
the early-gcd branch because then (B=p), but all displayed coordinate
identities still hold.

Finally,

\[
\begin{aligned}
d^2+4Bd-4E
&=(p+q-2B)^2+4B(p+q-2B)-4(pq-B^2)\\
&=(p+q)^2-4pq\\
&=(q-p)^2.
\end{aligned}
\]

For a correct (d), let the nonnegative square root be (s=q-p).  The
trace is (p+q=2B+d), so

\[
 p=\frac{2B+d-s}{2},
 \qquad
 q=\frac{2B+d+s}{2}.
\]

The parities agree because this trace and (s) are both even.  Exact
multiplication verifies the recovered factors.  Thus finding the correct
(d) is an exact factoring primitive.

## 2. Gap range, gcd branch, and bit size

The floor definition gives

\[
 B^2<N<(B+1)^2=B^2+2B+1.
\]

Since (E=N-B^2) is an integer,

\[
 \boxed{1\leq E\leq2B}.
\]

The gcd identity is exact:

\[
 \gcd(E,N)
 =\gcd(N-B^2,N)
 =\gcd(B^2,N).
\]

Because (0<B^2<N), a gcd greater than one is strictly less than (N)
and is already a proper factor.  On the other branch,

\[
 \gcd(E,N)=1
 \iff \gcd(B^2,N)=1
 \iff \gcd(B,N)=1.
\]

The last equivalence does not actually need squarefreeness, so the proof is
stronger than required at that point.

The smallest promised input is (15), hence (n\geq4).  From (N<2^n),

\[
 E\leq2B<2\sqrt N<2^{n/2+1}\leq2^{n-1}.
\]

Therefore (E) has at most (n-1) binary digits.  In fact the displayed
bound is close to a half-size child, but the weaker one-bit descent used in
the recurrence is correct.

## 3. Exact scope of the recursive accounting

If one correct recursive complete-factorization call is made on (E), and
all work at the current node is bounded by a nondecreasing numerical-QP
function (Q), the bit bound proves

\[
 T(n)\leq T(n-1)+Q(n).
\]

Along one chain,

\[
 T(n)\leq T(3)+\sum_{j=4}^{n}Q(j)
 \leq T(3)+nQ(n).
\]

Multiplication by (n) preserves numerical quasipolynomial time.  No
fixed-ratio contraction is needed for this cost statement.

This does not prove recursive correctness from the frozen promise alone.
The integer (E) can be prime, a prime power, an unbalanced semiprime, or a
general composite.  It is not guaranteed to be a balanced squarefree
semiprime.  Thus (T(n-1)) must refer to a correct factorization routine on
arbitrary child integers, or a separate all-input dispatch must be supplied.
The frozen result disclaims an all-input algorithm, so its valid conclusion
is the recurrence accounting, not a closed factoring construction.

## 4. Four roots and mixed-root extraction

On the coprime branch, (B) is nonzero modulo both odd primes and

\[
 B^2\equiv-E\pmod p,
 \qquad
 B^2\equiv-E\pmod q.
\]

Each prime field therefore has exactly the two distinct roots (B,-B).
CRT gives exactly four roots modulo (N).  Equal signs give the public
roots (B,-B).  A mixed root takes the (B)-sign at one hidden prime and
the (-B)-sign at the other.  Consequently exactly one of (p,q) divides
(r-B), and the other divides (r+B).  Neither difference vanishes modulo
both primes, so

\[
 \{\gcd(r-B,N),\gcd(r+B,N)\}=\{p,q\}.
\]

Both gcds are proper.  Conversely, known (p,q) permit opposite sign
choices followed by CRT.  Construction of a mixed root and factorization
are therefore deterministically polynomial-time equivalent on the promise.

## 5. Principal norms and the unit denominator

Suppose

\[
 N=x^2+Ey^2.
\]

If (p\mid y), reduction modulo (p) gives (p\mid x).  Then (p^2)
divides both terms on the left and hence divides (N=pq), a contradiction.
The same argument applies to (q).  Therefore

\[
 \gcd(y,N)=1.
\]

The residue

\[
 r=xy^{-1}\pmod N
\]

is well-defined and satisfies (r^2\equiv-E\pmod N).  If it is mixed,
the two gcds above factor (N).  If it is (B) or (-B), it retains the
public orientation.  The public representation

\[
 N=B^2+E
\]

is of the latter type.  Thus a second factor-bearing representation is
sufficient, but its existence is a genuine extra condition.

## 6. Complete factor-supported congruence calculation

Let (m\mid E).  On the coprime branch,

\[
 \gcd(B,E)=\gcd(B,N-B^2)=\gcd(B,N)=1,
\]

so (B) is a unit modulo every such (m).  Also

\[
 N\equiv B^2\pmod m.
\]

For an arbitrary unit (x\pmod m), define

\[
 y=Nx^{-1},\qquad t_x=x+y,\qquad d_x=t_x-2B.
\]

Product consistency is built into (xy=N).  The elementary trace identity
gives

\[
 t_x^2-4N=(x-y)^2\pmod m.
\]

Using (N\equiv B^2\pmod m),

\[
 d_x=x+B^2x^{-1}-2B=\frac{(x-B)^2}{x}\pmod m,
\]

and

\[
 d_x+4B=\frac{(x+B)^2}{x}\pmod m.
\]

Multiplication, together with (E\equiv0\pmod m), gives

\[
 \boxed{
 d_x^2+4Bd_x-4E
 =\left(\frac{x^2-B^2}{x}\right)^2\pmod m.}
\]

This calculation includes every prime power in the complete factorization
of (E), because it also holds for (m=E).  The genuine factor residues
are units modulo (m) since (gcd(E,N)=1), but so is every candidate in
the stated domain.  Hence this literal product-plus-square test cannot
orient them.

The quantifiers are narrow and correct.  The theorem does not say that an
arbitrary residue in the (d)-coordinate passes, does not include range
conditions, and does not cover a modulus that is not a divisor of (E).
The degenerate divisor (m=1) creates no exception.

## 7. The quadratic order, including the nonmaximal case

Put

\[
 \omega=\sqrt{-E},
 \qquad
 \mathcal O=\mathbb Z[\omega].
\]

The basis (1,\omega) has discriminant

\[
 (2\omega)^2=-4E.
\]

This remains a valid quadratic order when (E) has square factors or is a
perfect square.  In those cases it can be nonmaximal.  If (f) is its
conductor in the maximal order of its quadratic field, then

\[
 -4E=f^2D_K.
\]

Every prime dividing (f) therefore divides (2E).  On the coprime
branch, (p,q) are odd and divide neither (E) nor (2E).  Thus both
hidden primes are coprime to the discriminant and the conductor.  Ideals of
norm \(p\), \(q\), or \(N\) used below are consequently invertible proper
\(\mathcal O\)-ideals.  No noninvertible conductor prime is silently placed
in the proper class group.

The nonzero square root \(B\bmod p\) shows that \(p\) splits in the order;
the same holds for \(q\).  With

\[
 \alpha=B+\omega,
\]

one has \(N_{K/\mathbb Q}(\alpha)=B^2+E=N\).  Let

\[
 \mathfrak p=(p,B+\omega),
 \qquad
 \mathfrak q=(q,B+\omega)
\]

be the primes selected by divisibility of \(\alpha\).  Unique factorization
of invertible ideals coprime to the conductor gives

\[
 (\alpha)=\mathfrak p\mathfrak q.
\]

Equivalently, both sides have norm (N), and the two selected prime factors
are the only possible factors of the principal ideal.  In the proper ideal
class group, if (C=[\mathfrak p]), then

\[
 [\mathfrak q]=C^{-1}.
\]

## 8. The (C^2/C^{-2}) convention

For a root (s^2\equiv-E\pmod N), define

\[
 I_s=(N,s+\omega).
\]

As a lattice, this ideal has basis (N,s+\omega), hence norm (N).  Its
prime factors are determined by the two CRT signs.  For (s=B),

\[
 I_B=(\alpha)=\mathfrak p\mathfrak q.
\]

Choose the mixed root that retains the (B)-sign modulo (p) and reverses
it modulo (q).  Then

\[
 I_s=\mathfrak p\overline{\mathfrak q}.
\]

Conjugation is inversion in the proper ideal class group, so

\[
 [I_s]
 =C[\mathfrak q]^{-1}
 =C(C^{-1})^{-1}
 =\boxed{C^2}.
\]

The other mixed sign gives (C^{-2}).  A convention that attaches
([a,b,c]) using the conjugate ideal swaps these two labels globally, but
does not alter the statement that the two mixed classes are (C^{\pm2}),
nor any genus or principality conclusion.  The proof's explicit ideal
convention has the displayed (C^2) orientation.

Every genus character is a homomorphism to ({\pm1\}).  Therefore

\[
 \chi(C^2)=\chi(C)^2=1.
\]

The mixed class is a square in the proper class group and lies in the
principal genus, including for a nonmaximal order.  This shows invisibility
to genus labels, not efficient computability of the full square subgroup.

## 9. Principality equivalence

The integral proper ideal \(I_s\) has norm \(N\).  If its class is
principal, then \(I_s=(\beta)\) for some \(\beta\in\mathcal O\).  Writing

\[
 \beta=x+y\omega
\]

and comparing ideal norms gives

\[
 x^2+Ey^2=N.
\]

Conversely, a representation of this norm has (y) invertible modulo
(N).  If its associated root is (s=xy^{-1}\pmod N), then

\[
 \beta=x+y\omega\in(N,s+\omega)=I_s.
\]

The ideals ((\beta)) and (I_s) both have norm (N), so they are equal.
Thus the mixed ideal is principal exactly when a factor-bearing principal
norm representation exists.  Since its class is (C^2) or (C^{-2}),
this is equivalent to

\[
 \boxed{C^2=1}.
\]

There is no gap between class principality and integral representation in
this setting.

## 10. Exact scope of ramified and ambiguous classes

For an invertible ideal class (A), ambiguity means that conjugation fixes
the class.  Since conjugation is inversion,

\[
 A=A^{-1}\quad\Longrightarrow\quad A^2=1.
\]

Likewise, an invertible prime ideal at a field-ramified prime satisfies a
principal square relation and has class of exponent at most two.  Products
of these classes remain in a two-torsion subgroup.

At primes dividing the conductor of a nonmaximal order, the obvious prime
ideals can be noninvertible.  They are not elements of the proper ideal
class group.  The frozen statement avoids this error by restricting its
claim to canonical **invertible** ambiguous or ramified classes.  It does
not claim that every prime dividing (-4E) contributes an invertible class,
or that factoring (E) constructs the full proper class group.

A square (C^2) need not belong to the factor-supported two-torsion
subgroup.  In particular, a nontrivial square can have odd order.  The
finite certificate exhibits exactly this separation.

## 11. Arithmetic of the (N=2627) certificate

The displayed products and neighboring squares give

\[
 37\cdot71=2627,
 \qquad
 51^2=2601<2627<2704=52^2.
\]

Thus (B=51), (E=26=2\cdot13), and (71<74=2\cdot37).  The offsets are

\[
 a=51-37=14,
 \qquad
 c=71-51=20,
 \qquad
 d=20-14=6.
\]

They satisfy all coordinate checks:

\[
 51\cdot6-14\cdot20=306-280=26,
\]

\[
 14^2+26=222=37\cdot6,
 \qquad
 20^2+26=426=71\cdot6,
\]

and

\[
 6^2+4\cdot51\cdot6-4\cdot26
 =36+1224-104
 =1156
 =34^2.
\]

For (r=162),

\[
 162^2+26=26244+26=26270=10\cdot2627.
\]

Moreover,

\[
 r-51=111=3\cdot37,
 \qquad
 r+51=213=3\cdot71.
\]

Since neither (3\) nor the opposite hidden prime divides the corresponding
difference, the two gcds are exactly (37) and (71).  Equivalently,
(r\equiv B\pmod {37}) and (r\equiv-B\pmod {71}), so (r) is mixed.

## 12. Exhaustion of principal norm representations

If

\[
 x^2+26y^2=2627,
\]

then (x) is odd.  Modulo (13),

\[
 x^2\equiv2627\equiv1\pmod {13}.
\]

The bound \(|x|\leq51\), the two residues \(\pm1\bmod 13\), and odd
parity leave exactly

\[
 |x|\in\{1,25,27,51\}.
\]

The omitted congruent values (12,14,38,40) are even.  Substitution gives

\[
 y^2\in\{101,77,73,1\}.
\]

The first three lie strictly between consecutive integer squares; only the
last is a square.  Hence the complete solution set is

\[
 (x,y)=(\pm51,\pm1).
\]

Their associated roots are only (B) and (-B).  No factor-bearing
principal representation exists, so the mixed class is nonprincipal.

## 13. Proper form reduction

The form attached to the chosen mixed sign convention is

\[
 [2627,324,10],
\]

and

\[
 324^2-4\cdot2627\cdot10=-104.
\]

It is primitive.  Each displayed equivalence is proper:

1. The determinant-one swap sends
   ([a,b,c]) to ([c,-b,a]), giving
   
   \[
   [2627,324,10]\sim[10,-324,2627].
   \]
2. The shear (x\mapsto x+16y) changes the latter form to
   
   \[
   [10,-4,3],
   \]
   
   because the new last coefficient is
   (10\cdot16^2-324\cdot16+2627=3).
3. Another determinant-one swap gives ([3,4,10]).
4. The shear (x\mapsto x-y) gives ([3,-2,9]).

The final form satisfies the strict reduced inequalities

\[
 |{-2}|<3<9.
\]

It is not principal.  Besides uniqueness of the strictly reduced
representative, this follows directly because

\[
 3x^2-2xy+9y^2
 =3\left(x-\frac y3\right)^2+\frac{26}{3}y^2
\]

cannot represent (1): if (y=0), its positive values are at least (3),
and if (y\ne0), they exceed (8).  A form properly equivalent to the
principal form would primitively represent (1).

The sign convention for mapping ideals to forms can instead attach
([2627,-324,10]), which reduces to the inverse reduced form
([3,2,9]).  Both are nonprincipal and outside the ramified subgroup.  This
is exactly the harmless (C^2/C^{-2}) convention swap already accounted
for.

## 14. Ramified subgroup for discriminant (-104)

Here (-104=(-8)\cdot13) is fundamental, so conductor complications do not
occur in the certificate.  The ramified prime forms are

\[
 [2,0,13]
 \quad\text{and}\quad
 [13,0,2].
\]

They are properly equivalent by the same determinant-one swap.  The form
([2,0,13]) is reduced and does not represent (1), so it is nonprincipal.
Because its middle coefficient is zero, its inverse is itself; its class
therefore has exact order two.  The subgroup generated by both ramified
prime forms is exactly

\[
 \{[1,0,26],[2,0,13]\}.
\]

The strictly reduced mixed form ([3,-2,9]) is neither member.  Thus the
certificate proves that direct composition of the factor-supported
ramified classes does not reach the mixed square class.

Finally,

\[
 d=6=2\cdot3,
 \qquad
 2E=52=2^2\cdot13.
\]

The prime (3) in (d) is absent from the prime support of (2E).  This
single exact example is enough to refute any universal claim that the
coordinate identities force (d)'s prime support to come from the known
factorization of (E).

## 15. P175 and the remaining-gate scope

Theorems 1--5 do not depend on P175.  The imported result is used only to
label a quarter-minus-polylogarithmic prefix of (p^{-1}) as a
numerical-QP factoring terminal.  F202 does not claim to compute that
prefix.

The four final openings are stated as alternatives, not as an exhaustive
lower bound against all algorithms.  The packet leaves open nonlocal
moduli, interval or Archimedean information, compressed computation in the
full proper class group, and a different statistic selecting the reciprocal
path.  Its genus and ramified-form result excludes only the named
two-torsion information, not arbitrary navigation inside the principal
genus.

## Hostile attacks that did not refute the frozen claims

I checked:

- the floor endpoint (p\leq B), including (a=0);
- every sign in the two norm identities and in the discriminant;
- positivity, parity, and both upper bounds for (d);
- the exact integer range and bit length of (E);
- the early-gcd branch and the unit consequences;
- the one-child recurrence and its promise-domain limitation;
- all four CRT roots and both mixed orientations;
- invertibility of the norm denominator (y);
- every unit candidate modulo every divisor and prime power of (E);
- square factors of (E) and the resulting nonmaximal quadratic order;
- conductor coprimality, properness, and invertibility of all hidden-prime
  ideals;
- the (C^2) versus (C^{-2}) convention;
- the equivalence between ideal principality and an integral norm-(N)
  representation;
- the exclusion of noninvertible conductor primes from ramified
  two-torsion;
- every product, gcd, congruence, and range in the (2627) certificate;
- the complete principal-norm solution set;
- every proper swap and shear in the form reduction;
- reducedness and nonprincipality of the mixed form; and
- proper equivalence, order, and generated subgroup of the two ramified
  forms.
