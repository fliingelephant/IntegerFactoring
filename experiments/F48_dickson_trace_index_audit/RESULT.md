# F48 hostile audit — ordinary Dickson trace index

**Artifact audited:**
`experiments/F48_dickson_trace_index_kill/RESULT.md`

**Candidate SHA-256:**
`801f86d6acb3c5278ba5f5e1d0ba4db6349b4e9be3878727d29602991c5d6d61`
(matches the assigned digest).

**Audit mode:** proof-only. I used no web search and ran no finite or
symbolic mathematical experiment.

**Verdict: PASS.** I found no false theorem, missing case inside a stated
theorem, sign error, quantifier slip, or scope inflation requiring a
mathematical amendment. The result is only a narrow interface/method
failure on distinct odd semiprimes. It is not an all-input factoring
algorithm and not a hardness theorem for arithmetic over
\(\mathbb Z/N\mathbb Z\).

Two readings need care, but neither is a defect in the stated result:

1. The public derivative \(D_{N-1}'(X)\) is efficiently computable. What is
   missing is the derivative of a hidden short alias, or an independent
   comparator that orients the public derivative. The public derivative is
   already the scaled difference of the two known shifted roots.
2. The Euler quotient in the modulo-\(N^2\) discussion depends on the
   chosen lift. Formula (7.1) is valid for every fixed lift and does not
   assert lift invariance.

The detailed hostile checks follow.

## 1. Scope and comparison with durable results

The candidate's closest-route declaration is accurate.

* P12 rules out dense consecutive-moment reconstruction on a synchronized
  family with exponentially many frequencies. It expressly leaves open
  binary-indexed recurrences and explicit arithmetic. F48 uses exactly
  those omitted features, so it is not an illicit consequence of P12.
* P55 proves an exact signed gap relation in discriminant-dependent Lucas
  tori and a lower bound only in independently random-encoded tagged groups
  of common prime order. F48 instead uses the ordinary unit group, its
  quotient by inversion, unequal composite local orders, and one explicit
  CRT ring. The candidate repeats rather than suppresses all reasons the
  P55 generic theorem does not transfer.
* X49 closes only opaque tagged common-prime-order pooling. F48's generic
  theorem is another deliberately opaque boundary, while explicit
  coordinate algorithms remain open.
* P56/X50 concern the canonical exponent-\(N\) high digit modulo \(N^2\)
  and genuine multiplicative linear-cocycle consistency. F48's
  exponent-\(N-1\) Euler-quotient discrepancy is a different lift
  observable. The candidate neither contradicts P56 nor claims that P56
  closes it.

The registry's F28 test asked for the ordinary identity, complete aliases,
both decoders, structured-relation analysis, a quotient-by-inversion generic
boundary, and attacks on roots, derivatives, lifts, and intervals. The
candidate supplies those items while preserving coordinate root selection,
useful gcd distributions, lifts, and all inputs outside the semiprime
promise as open. This is the correct classification under the prompt.

## 2. Universal Dickson identities

Let \(D_0=2,D_1=X,D_{j+1}=XD_j-D_{j-1}\), with \(D_{-j}=D_j\).
For a unit \(a\) in any commutative ring, the Laurent expressions

\[
L_j=a^j+a^{-j}
\]

have the same initial values and recurrence. Hence

\[
D_j(a+a^{-1})=a^j+a^{-j}
\]

for every integer \(j\). No division by \(2\), field hypothesis, or
reducedness is used.

The later composition and addition laws are also genuine polynomial
identities:

\[
D_j(D_k(X))=D_{jk}(X),
\qquad
D_{u+v}(X)+D_{u-v}(X)=D_u(X)D_v(X).
\]

Substitution \(X=z+z^{-1}\) proves them in
\(\mathbb Z[z,z^{-1}]\); this proves them in \(\mathbb Z[X]\) because
the substitution is injective (the highest Laurent exponent of a nonzero
polynomial cannot cancel). Thus their use over \(\mathbb Z/N\mathbb Z\)
and over the local fields is valid.

For \(N=pq\), \(3\le p<q\), put

\[
e=pq-1,\quad t=p+q-2,\quad g=q-p.
\]

The exact differences are

\[
e-t=(p-1)(q-1),
\]

\[
e-g=(p-1)(q+1),\qquad
e+g=(q-1)(p+1).
\]

Therefore every unit satisfies \(a^e=a^t\) globally, while locally

\[
a^e=a^g\pmod p,\qquad a^e=a^{-g}\pmod q.
\]

Taking traces gives \(F_e=F_t=F_g\). All signs in the candidate are
correct, and no generator assumption is present.

## 3. One-prime trace classification, including self-inverse classes

Let \(r\) be odd and index the characters of
\(\mathbb F_r^\times\) by \(j\in\mathbb Z/(r-1)\). If
\(\sum_j c_jz^j=0\) for every nonzero \(z\), multiplication by \(z^{-k}\)
and summation gives

\[
(r-1)c_k=0\quad\text{in }\mathbb F_r.
\]

Since \(r-1=-1\ne0\) in that field, all \(c_k\) vanish. Thus the
characters form a basis of the functions on \(\mathbb F_r^\times\).

It follows that

\[
z^u+z^{-u}=z^v+z^{-v}\quad\text{for all }z
\]

exactly when the inversion orbits of \(u\) and \(v\) modulo \(r-1\)
are equal. If \(2u=0\), its coefficient is \(2\), not zero, because
\(r\) is odd. This covers both self-inverse classes \(0\) and
\((r-1)/2\), when distinct. At \(r=3\), both exponent classes are
self-inverse, and the two functions are \(2\chi_0\) and \(2\chi_1\),
still distinct. Hence Lemma 2.1 has no small-characteristic exception.

## 4. Complete global alias class and all coincidence risks

CRT lets the \(p\)- and \(q\)-coordinates of a unit vary independently.
Consequently

\[
F_u=F_v\text{ on all units}
\]

if and only if

\[
u\equiv\epsilon_pv\pmod{p-1},\qquad
u\equiv\epsilon_qv\pmod{q-1}
\]

for independently chosen signs. With
\(L=\operatorname{lcm}(p-1,q-1)\) and \(v=e\), the four compatible
systems have representatives

\[
t,\quad g,\quad-g,\quad-t\pmod L.
\]

Every solution of each local system is one residue class modulo \(L\), so
the union is complete; shared divisors of \(p-1\) and \(q-1\) do not
create additional classes.

Possible coincidences only merge entries of this union. For example, with
\(A=p-1\), \(B=q-1\), and \(d=\gcd(A,B)\),

\[
t-g=2A,\qquad t+g=2B.
\]

Thus \(t\equiv g\pmod L\) exactly when \(L\mid2A\). Since \(B>A\),
this forces \(B=2A\), namely \(q=2p-1\). Also
\(t\equiv-g\pmod L\) exactly when \(A/d\mid2\), so other pairwise
mergers can occur without creating a fifth class. A representative is
self-inverse only if both local divisibility conditions hold; in the
present ordering that again forces \(B=2A\). In the exceptional
\(q=2p-1\) case all four representatives coincide modulo \(L=2(p-1)\).
The candidate's union formulation is therefore robust under every
coincidence.

For the unsymmetrized power map, equality on all units is instead

\[
a^m=a^e\text{ for every }a
\iff m\equiv e\pmod L,
\]

because \(L\) is the exponent of
\(\mathbb F_p^\times\times\mathbb F_q^\times\). Since
\(e\equiv t\pmod L\), this is the single same-sign class. The gap \(g\)
is in it exactly when

\[
q-1\mid e-g\iff q-1\mid2(p-1).
\]

Again \(q-1>p-1\), so the only possibility is
\(q-1=2(p-1)\), or \(q=2p-1\). The stated exception is exact.

## 5. Exact integer decoders and verification

For an exact nonnegative gap \(h=q-p\),

\[
h^2+4N=(p+q)^2.
\]

An exact square root \(S\), parity, positivity, and
\(((S-h)/2)((S+h)/2)=N\) verify the candidate completely.

For an exact nonnegative trace index \(u=p+q-2\), put \(S=u+2\). Then

\[
S^2-4N=(q-p)^2,
\]

and the same parity, positivity, and product checks verify the factors.
Taking the absolute value handles the two negative alias representatives.
Trying both decoders is safe: acceptance always includes an exact product
test, so a wrong index can only be accepted by producing a genuine
factorization. Integer square root and the checks are polynomial in the
input and candidate bitlengths; requiring polynomial-bit output is
necessary and is stated.

## 6. Powers, products, repeated bases, and adaptive trace expressions

The identities

\[
T(a^k)=D_k(T(a)),\qquad
F_e(a^k)=D_k(F_e(a))
\]

show that a power-related query is a deterministic image of the original
pair. Likewise

\[
T(a)T(b)=T(ab)+T(ab^{-1})
\]

and

\[
F_e(a)F_e(b)=F_e(ab)+F_e(ab^{-1})
\]

are just the trace addition law, while \(a\mapsto a^e\) is a
homomorphism. Repetition cannot add an equation.

The adaptive transcript claim has the right quantifier. Inductively, if
the previously returned trace values are identical after replacing \(e\)
by any member of its full alias class, then the procedure makes the same
next choice and receives the same next trace value. Every subsequent ring
expression is therefore identical. This proves non-identifiability only in
the specified trace-function interface.

It does not cover inspection of explicit numerical coordinates, gcds,
additive constructions not generated by the displayed identities, lifts,
or a separate invariant of the chosen bases. The candidate states these
exclusions. Its discussion of the unsymmetrized value also does not claim
that the power-map congruence class is efficiently recoverable, since
computing \(L\) or an order would be a hidden factoring-strength call.

## 7. Shifted-trace quadratic and coherent CRT roots

For

\[
X=T(a),\quad Y=D_e(X),\quad K=D_k(X),
\]

set

\[
A=D_{e+k}(X),\qquad B=D_{e-k}(X).
\]

The addition law and direct Laurent multiplication give

\[
A+B=YK,
\]

\[
AB=D_{2e}(X)+D_{2k}(X)=Y^2+K^2-4.
\]

Thus \(A,B\) are the two displayed roots of the stated quadratic. For

\[
C=D_{g+k}(X),\qquad D=D_{g-k}(X),
\]

the same coefficients follow from \(D_g(X)=Y\). The local ordering is
exactly:

\[
(C,D)=(A,B)\pmod p,
\qquad
(C,D)=(B,A)\pmod q.
\]

The second equality uses
\(e\equiv-g\pmod{q-1}\) and \(D_{-j}=D_j\); no root-ordering sign was
lost.

There are exactly three gcd cases.

* If \(1<\gcd(A-B,N)<N\), a factor is already found.
* If \(A-B\) is a unit, the local roots are distinct in both fields. A
  coherent mixed root satisfies, for example,
  \(C=A\pmod p\) and \(C=B\pmod q\), so
  \(\gcd(C-A,N)=p\). The other mixed root returns \(q\).
* If \(A=B\pmod N\), both local roots are double and no orientation is
  present.

These cases also cover a double root in exactly one component: that is the
proper-gcd branch. The factorization

\[
A-B=(a^e-a^{-e})(a^k-a^{-k})
\]

is correct. Hence \(Y^2-4\), \(K^2-4\), and \(A-B\) are legitimate
early-gcd tickets, not events that may be conditioned away. The candidate
claims no uniform lower bound for them. Multiple quadratics do share the
same hidden CRT orientation, but producing the coherent mixed roots is
left open rather than assumed.

## 8. Derivatives: identities and exact nonconsequence

Writing \(X=z+z^{-1}\), differentiation gives

\[
D_m'(X)=m\frac{z^m-z^{-m}}{z-z^{-1}}.
\]

Multiplying by \(X^2-4=(z-z^{-1})^2\) proves

\[
(X^2-4)D_m'(X)
=m(D_{m+1}(X)-D_{m-1}(X)),
\]

and squaring proves

\[
(X^2-4)D_m'(X)^2=m^2(D_m(X)^2-4).
\]

As in Section 2, injectivity of the Laurent substitution makes these
identities valid in \(\mathbb Z[X]\), including the degenerate trace
points after polynomial specialization.

Equality of \(D_e\) and \(D_g\) merely as functions on the finite trace
set does not imply equality of formal derivatives. A polynomial can be
changed by a nonzero polynomial vanishing on that set, changing its
derivative. Thus interpolation of values alone supplies no hidden-alias
derivative.

There is one important public-object check. The polynomial derivative
\(D_e'(X)\) is computable by a differentiated doubling recurrence because
\(e=N-1\) is public. Let

\[
H_m=D_{m+1}(X)-D_{m-1}(X).
\]

Then \(H_e\) is also public and is the \(k=1\) instance \(A-B\) of the
shifted-root construction. Locally,

\[
H_e=H_g\pmod p,
\qquad
H_e=-H_g\pmod q.
\]

Moreover \(H_e^2=H_g^2=(X^2-4)(Y^2-4)\). Thus the public derivative
provides one CRT orientation of a known square-root pair; the unavailable
short-alias derivative \(H_g\) is the coherently remixed root whose
comparison would factor. If \(X^2-4\) is a unit, \(D_e'\) is just a unit
rescaling of this public root difference; if it is a zero divisor, its gcd
is already a ticket. This confirms the candidate's precise narrow
nonconsequence. Its final derivative paragraph must be read as referring
to manufacture of the hidden-alias derivative or another independent
orientation, not to \(D_e'\), which is public.

Finally, \(p,q\nmid g\), while \(p\mid t\) exactly when
\(q\equiv2\pmod p\), and \(q\nmid t\). Therefore division by an unknown
candidate index is not uniformly legitimate. This caveat is correct.

## 9. Modulo-\(N^2\) discrepancy and lift dependence

Let \(\varphi=(p-1)(q-1)=e-t\) and fix a unit lift
\(\widetilde a\pmod{N^2}\). Euler's theorem modulo \(N\) makes

\[
Q_{\widetilde a}
=\frac{\widetilde a^\varphi-1}{N}\pmod N
\]

well defined. Since
\(\widetilde a^\varphi\equiv1+NQ_{\widetilde a}\pmod{N^2}\),

\[
\widetilde a^e
\equiv\widetilde a^t(1+NQ_{\widetilde a})\pmod{N^2}
\]

and inversion changes the sign of the first-order term. Consequently

\[
T(\widetilde a^e)-T(\widetilde a^t)
\equiv NQ_{\widetilde a}
(\widetilde a^t-\widetilde a^{-t})\pmod{N^2},
\]

with the candidate's sign.

This quotient is lift-dependent, as it must be. If
\(\widetilde a'=\widetilde a+kN\), binomial expansion gives

\[
Q_{\widetilde a'}
\equiv Q_{\widetilde a}
+k\varphi\widetilde a^{\varphi-1}
\equiv Q_{\widetilde a}+k\varphi\widetilde a^{-1}
\pmod N.
\]

Formula (7.1) remains valid for each chosen lift; the trace terms themselves
also vary coherently. Thus it gives neither a lift-independent leaked
\(\varphi\) nor an obstruction to deliberately pooling several chosen
lifts. The candidate correctly leaves that mechanism open. Recovering
\(\varphi\) would recover \(p+q=N+1-\varphi\), so it cannot be treated as
free preprocessing.

## 10. Interval and representation-cost accounting

For balanced semiprimes \(t=\Theta(\sqrt N)\), while \(g\) can occupy a
range of that scale. If one prime is fixed, both can be \(\Theta(N)\).
These ranges have exponentially many points as a function of
\(n=\Theta(\log N)\). A size-\(H\) BSGS search costs
\(\Theta(\sqrt H)\) group operations, still exponential for
\(H=2^{\Theta(n)}\).

Binary-index evaluation of \(D_m\) can be polynomial in \(\log m\), but
expanding it has \(\Theta(m)\) potential support and cannot be charged as a
constant-size object. Conversely, an independently proved polynomial-size
candidate set would be enough because the exact decoders verify every
member. The candidate identifies, rather than assumes, this missing metric
or non-enumerative step.

## 11. Quotient-by-inversion generic theorem

The orbit operation in the model is well defined: changing the sign of
either representative of \([u]\) or \([v]\) merely swaps or negates the
two outputs

\[
\{[u+v],[u-v]\}.
\]

In a symbolic run, every handle is an inversion orbit of an affine form
\(\alpha+\beta Z\), canonicalized modulo global sign. A scalar call adds
at most one formal handle and an addition-pair call at most two. Therefore
tag \(i\), after \(q_i\) calls, contains at most \(2q_i+3\) formal
handles, including \([0],[1],[Z]\).

Two formally different orbit handles collide at a secret \(E\) only if

\[
f(E)=g(E)\quad\text{or}\quad f(E)=-g(E).
\]

Canonicalization ensures neither affine equation is an identity, and each
has at most one root in the prime field. Hence the bad-secret set has size
at most

\[
B=2\sum_i\binom{2q_i+3}{2}.
\]

This count includes initial accidents such as \(E=0,1,-1\), output-output
collisions from one unordered-pair call, and collisions with old handles.
Concentrating the \(Q=\sum_iq_i\) calls in one tag maximizes the convex
sum, giving

\[
B\le2\binom{2Q+3}{2}+6(K-1).
\]

Adaptivity does not invalidate the count. Condition on the algorithm's
coins and on a collision-free lazy symbolic transcript. All public scalars
and subsequent choices are then fixed functions of random labels whose law
is independent of \(E\). Inductively, the real random injection couples to
this transcript until the first surprise collision. Outside the union of
the at most \(B\) bad field values, no such collision occurs.

For a fixed output list of \(M\) residues, success up to inversion covers
at most \(2M\) secrets. Averaging over the label transcript therefore gives

\[
\Pr[\exists h:h=\pm E]
\le\min\left\{1,\frac{2M+B}{\ell}\right\}.
\]

For a uniform public \(H\)-element subset, intersecting both the collision
set and output coverage with that subset replaces \(\ell\) by \(H\). For
a prior of maximum point mass \(\mu_*\), the same union bound gives
\((2M+B)\mu_*\), truncated at one. If both secret and outputs are defined
on inversion orbits rather than field representatives, one output covers
one prior atom, explaining the stated replacement of \(2M\) by \(M\).

The stronger ordinary generic-group variant is also sound. Handles remain
affine, now equality is not quotiented by sign, so each distinct pair has at
most one bad secret. With at most \(q_i+3\) handles in tag \(i\),

\[
C=\sum_i\binom{q_i+3}{2}
\le\binom{Q+3}{2}+3(K-1).
\]

A list of \(M\) integer representatives still covers \(2M\) secrets when
success is accepted up to inversion, yielding the candidate's bound.

For composite order \(d\), an affine congruence can have
\(\gcd(\text{slope},d)\) roots, and non-generators reveal only a quotient
order. The prime-order theorem therefore cannot simply be substituted for
the actual F28 units. The candidate explicitly lists unequal composite
orders, correlated bases, explicit numerical labels, CRT gcds, and the
nonuniform arithmetic secret as transfer blockers. There is no unjustified
generic-model lower bound for the real ring.

## 12. Edge cases, hidden calls, and all-input boundary

All inversions are preceded by \(\gcd(a,N)\). A proper gcd is success, a
full gcd rejects the base, and only a unit is inverted. The same trichotomy
is needed for differences, derivative scales, discriminants, and
resultants. The candidate preserves rather than conditions away these
branches.

The divisibility statements are exact:

* neither hidden prime divides \(0<g=q-p<q\);
* \(q\nmid t\);
* \(p\mid t\) can occur and threatens derivative division, not the integer
  decoder.

No promise case was silently extended.

* At \(p=q\), the CRT proof is unavailable and the difference of the two
  proposed power exponents is \((p-1)^2\), not a multiple of the exponent
  \(p(p-1)\) of \((\mathbb Z/p^2\mathbb Z)^\times\); the universal power
  identity fails.
* Higher prime powers have principal-unit exponent factors absent from the
  field proof.
* Three or more distinct primes give one local exponent condition per
  factor and no two-variable sum/gap decoder.
* Characteristic two changes the trace quotient.
* For prime \(N\), the public trace is constantly \(2\).

Thus even a semiprime index decoder would still need prime-power and even
handling, arbitrary multifactor splitting, recursion, primality testing,
and a total expected bit bound. The candidate says so explicitly.

On the promised family, gcd screening, inversion, binary powering, and a
polynomial number of binary-indexed Dickson evaluations operate on
\(O(n)\)-bit residues in polynomial bit complexity. The candidate does not
hide expansion of an exponential-degree polynomial. It also disallows
selecting local generators, learning \(p-1\) or \(q-1\), computing \(L\),
or using order/discrete-log oracles without cost. Knowing a suitable group
exponent multiple would already be factoring-strength information.

## 13. Final hostile classification

I tried the following possible refutations and none lands:

* self-inverse character classes do not invalidate Lemma 2.1, even at
  \(r=3\);
* common divisors of \(p-1\) and \(q-1\) merge but do not enlarge the four
  global alias classes;
* the exceptional unsymmetrized gap class is exactly \(q=2p-1\);
* the shifted-root ordering reverses in the \(q\)-component with the signs
  stated;
* all double-root cases are caught by the gcd trichotomy;
* public derivatives reduce to known shifted-root data unless a new
  orientation is supplied;
* the modulo-\(N^2\) equation remains correct after exposing its lift
  dependence;
* adaptive oracle choices do not evade the generic bad-secret union; and
* no generic statement is transferred to explicit composite-ring
  coordinates.

Accordingly, no mathematical repair is required. The candidate may advance
to the required fresh proof-blind reconstruction. Any later promotion must
retain its exact narrow classification and all six reopen conditions; it
does not satisfy the top-level all-input factoring statement.
