# Second fresh hostile re-audit of F49 coherent Dickson-root selection

## Artifact and verdict

This audit checks
`experiments/F49_coherent_dickson_root_kill/RESULT.md` at SHA-256

`b34c2965b4be06ca59c9c27ba54814a76c1cac286bcfb13beee65917f9093aba`.

I read `PROMPT.md`, C54--C55, P57, X51, the complete candidate, and both
preserved failed audits. I then reconstructed the argument from the stated
definitions and tried to break each reduction at zero divisors, repeated
variables, every position of an eliminated constant, disconnected components,
degenerate shifted pairs, and endpoint quantifiers. I used no web search or
finite computation.

**Verdict: PASS AS WRITTEN.** The second correction repairs the exact defect
found by the preceding re-audit. The new constant-output calculation is correct
as an algebra calculation, not only as a calculation on ordinary points. The
candidate now proves precisely its narrow claim: a screened, linearly reduced,
explicit polynomial system on one already established common-orientation
component has only one idempotent variable. It does not construct a factor or
claim an all-input factoring algorithm.

## 1. Dependency and the four global sections

Let \(R=\mathbb Z/N\mathbb Z\), where \(N=pq\) and \(3\le p<q\) are distinct
odd primes. Put \(e=pq-1\), \(g=q-p\), \(E(z)=z^e\), and \(G(z)=z^g\).
The identities used from P57 are exact:

\[
 e-g=(p-1)(q+1),\qquad e+g=(q-1)(p+1).
\]

Consequently,

\[
 E=G\pmod p,\qquad E=G^{-1}\pmod q,
\]

and \(T(E(z))=T(G(z))\) in \(R\).

Theorem 2.1 also has the claimed quantifiers. Write a unit as
\((a,b)\in\mathbb F_p^\times\times\mathbb F_q^\times\). If
\(H:R^\times\to R^\times\) is a homomorphism satisfying
\(T(H(x))=T(E(x))\) for every unit \(x\), then at an input \((1,b)\),

\[
 H_p(1,b)+H_p(1,b)^{-1}=2.
\]

Over the field \(\mathbb F_p\), this is
\((H_p(1,b)-1)^2=0\), hence \(H_p(1,b)=1\). Thus the \(p\)-coordinate
of \(H\) kills the whole \(q\)-side subgroup. The symmetric argument kills
the \(p\)-side subgroup in the \(q\)-coordinate. Each remaining local map is
an endomorphism of a cyclic group and therefore a power map. P57's one-field
trace classification gives, independently at each prime, the exponent of
\(E\) or its negative. The four sign pairs are exactly

\[
 E,\quad E^{-1},\quad G,\quad G^{-1},
\]

with coincidences allowed when a local image is self-inverse. This theorem
classifies homomorphisms on all units. It does not classify arbitrary choices
from finitely many unrelated quadratic root pairs, and the candidate does not
make that quantifier jump.

## 2. The anchor probability is exact and factor-free

Let

\[
 d=\gcd(p-1,q-1),\qquad h_p=(p-1)/d,\qquad h_q=(q-1)/d.
\]

The image of \(z\mapsto z^e\) in \(\mathbb F_p^\times\) has size

\[
 \frac{p-1}{\gcd(p-1,e)}
 =\frac{p-1}{\gcd(p-1,q-1)}=h_p,
\]

and similarly the \(q\)-image has size \(h_q\). A uniform unit has
independent uniform CRT coordinates, so its two \(E\)-coordinates are uniform
in these image groups. Since the common divisor \(d\) is the same and \(p<q\),
\(h_p<h_q\).

For \(\Delta=E(a)-E(a)^{-1}\), a proper gcd with \(N\) is already a
factor, and gcd \(1\) gives the required unit root difference. If the gcd is
\(N\), both local image values are self-inverse. A cyclic group of order \(h\)
contains the value \(-1\) exactly when \(h\) is even. The subsequent gcds with
\(E(a)-1\) and \(E(a)+1\) factor when the two local signs differ. Therefore
the exact conditional no-factor/no-anchor probability is

\[
 \frac{1+\mathbf 1_{2\mid h_p,\,2\mid h_q}}{h_ph_q}.
\]

If both orders are even, strict inequality gives
\(h_ph_q\ge 2\cdot4=8\). Otherwise \(h_ph_q\ge1\cdot2=2\).
Thus the probability is at most \(1/2\). Equality requires
\((h_p,h_q)=(1,2)\), which is equivalent to
\(q-1=2(p-1)\), or \(q=2p-1\).

For a raw uniform residue, the unit probability is

\[
 (1-1/p)(1-1/q)\ge (1-1/3)(1-1/5)=8/15.
\]

Hence a factor or a unit-difference anchor occurs with probability at least
\(4/15\) per raw trial. Initial gcd, extended-Euclidean inversion, modular
exponentiation by the public exponent \(N-1\), and the comparison gcds all
have polynomial bit cost. No value \(g\), hidden order, or hidden factor is
used by this sampling procedure.

## 3. One nondegenerate triangle

Let \(A,B\in R^\times\), \(C=AB\), and suppose
\(A-A^{-1}\) and \(B-B^{-1}\) are units. Normalize

\[
 X=A^{-1}+f(A-A^{-1}),\qquad
 Y=B^{-1}+h(B-B^{-1}).
\]

The two root equations are exactly \(f^2=f\) and \(h^2=h\). Their
algebra is \(R^4\), with one copy of \(R\) at each Boolean corner. After
eliminating \(Z\) by \(Z=XY\), the remaining \(Z\)-root polynomial is

\[
 (XY-C)(XY-C^{-1}).
\]

It vanishes at \((f,h)=(0,0)\) and \((1,1)\). At \((1,0)\) it is

\[
 (AB^{-1}-AB)(AB^{-1}-A^{-1}B^{-1}).
\]

The first factor is \(A(B^{-1}-B)\), and the second is
\(B^{-1}(A-A^{-1})\), so both are units. The other unequal corner is
symmetric. Quotienting the product algebra therefore kills exactly the two
unequal factors and leaves

\[
 R\times R\cong R[f]/(f^2-f),\qquad h=f.
\]

This also covers \(C=C^{-1}\), globally or at only one prime. No inverse of
\(C-C^{-1}\) was taken. Although the isolated repeated-root algebra for \(Z\)
could contain a nilpotent, the linear equation \(Z=XY\) removes \(Z\), and the
two mixed corner values above are units. Thus Section 4 is an exact coordinate-
algebra proof.

## 4. Degenerate roots and every repeated-variable case

For each multiplicative root pair, the gcd screen is complete. If
\(A_v-A_v^{-1}\) has full gcd with \(N\), then each local value is in
\(\{1,-1\}\). Opposite local signs are exposed by the gcds of \(A_v-1\)
and \(A_v+1\). An unfactored survivor has the same sign at both primes, so
\(A_v=s\in\{1,-1\}\) in \(R\).

The raw algebra \(R[X_v]/((X_v-s)^2)\) does have a nilpotent. The candidate
does not identify it with a constant algebra. It explicitly adds the linear
equation \(X_v=s\), eliminates the variable, and limits its theorem to this
linearly reduced system. This preserves all \(R\)-valued root choices while
removing the scheme-theoretic thickening.

It remains to check every equality pattern in a genuine relation

\[
 a_w=a_ua_v,\qquad X_w=X_uX_v.
\]

There are no missing repeated-position cases:

1. If \(u,v,w\) are distinct and nondegenerate, Section 3 above identifies
   all three orientations.
2. If \(u=v\ne w\), write \(A=A_u\), so \(A_w=A^2\). On the two unequal
   orientation corners of \(X_w=X_u^2\), the residual is, up to sign,

   \[
   A_w-A_w^{-1}=A^2-A^{-2},
   \]

   which is a unit because \(w\) passed its screen. The equal corners vanish.
3. If \(w=u\ne v\), cancellation in the unit group gives \(a_v=1\).
   Thus \(A_v=1\) is eliminated and the reduced relation contains at most the
   one nondegenerate variable \(X_u\). The case \(w=v\ne u\) is symmetric.
4. If \(u=v=w\), then \(a_u=a_u^2\) in the unit group, so \(a_u=1\);
   there is no nondegenerate variable.

Cases 3 and 4 are exactly within the candidate's “at most one distinct
nondegenerate variable” case. More generally, after constant substitution,
any residual involving at most one Boolean orientation vanishes at both
orientations because the global homomorphisms \(E\) and \(E^{-1}\) satisfy
every genuine multiplicative relation. In \(R[f]/(f^2-f)\cong R\times R\),
vanishing at both endpoints means that the residual is zero. Hence such a
relation imposes no hidden one-variable constraint.

Now suppose one eliminated constant and two distinct nondegenerate variables
remain. The two possible constant positions are both correct in the repaired
candidate.

If an input is \(s\in\{1,-1\}\), the equation is
\(X_w=sX_u\). Public multiplicativity gives \(A_w=sA_u\), so the two equal
orientation corners vanish and each unequal residual is a unit multiple of
\(A_u-A_u^{-1}\).

If the output is the constant, the equation is

\[
 s=X_uX_v,
\]

not \(X_v=sX_u\). Put \(A=A_u\) and
\(\delta=A-A^{-1}\in R^\times\). Since \(A_uA_v=s\), one has
\(A_v=sA^{-1}\), and the normalized root variables are

\[
 X_u=A^{-1}+f\delta,\qquad
 X_v=sA-hs\delta,qquad f^2=f,\quad h^2=h.
\]

For the residual \(X_uX_v-s\), the exact four corner values are

\[
 \begin{array}{c|cccc}
 (f,h)&(0,0)&(1,1)&(1,0)&(0,1)\\ \hline
 X_uX_v-s&0&0&sA\delta&-sA^{-1}\delta.
 \end{array}
\]

Both unequal values are units. The quotient therefore kills exactly the
unequal factors and imposes \(h=f\). This is the required correction to the
counterexample in the preceding audit: its actual equation now appears, and
the calculation works for both \(s=1\) and \(s=-1\).

If two or three values in a relation are eliminated constants, public
multiplicativity forces any remaining public value also to be a constant,
unless a repeated occurrence leaves only one variable as already covered.
Thus the list above exhausts all constant and repetition patterns relevant to
the reduced system.

## 5. Exact connected-component algebra

For \(m\) distinct retained nondegenerate variables, every root difference is
a unit. Before the multiplicative equations are imposed, repeated use of the
Chinese remainder theorem gives the Boolean product algebra

\[
 \bigotimes_{i=1}^m
 R[X_i]/((X_i-A_i)(X_i-A_i^{-1}))
 \cong R^{2^m}.
\]

For a three-distinct-variable relation, if the two input orientations differ,
Section 3 shows that
\((X_uX_v-A_w)(X_uX_v-A_w^{-1})\) is a unit. Hence each factor, and thus
the residual for either possible \(X_w\), is a unit. If the input orientations
agree but the output orientation differs, the residual is
\(\pm(A_w-A_w^{-1})\), also a unit because \(w\) was retained. Thus the
direct equation \(X_w-X_uX_v=0\) has exactly the same all-equal Boolean
survivors as the eliminated-\(Z\) calculation.

The preceding case analysis is stronger than a point count. At every Boolean
factor, each reduced relation has residual either zero or a unit. It is zero
when the orientations agree on every edge supplied by that relation, and a
unit at every forbidden assignment. Therefore quotienting by all relation
residuals deletes exactly the Boolean factors whose assignments violate an
edge. It creates neither nilpotents nor partially retained CRT factors.

The surviving assignments are precisely those constant on each connected
component of the reduced orientation graph. If the graph has components
\(C_1,\ldots,C_c\), the full reduced algebra is consequently

\[
 R[f_1,\ldots,f_c]/(f_1^2-f_1,\ldots,f_c^2-f_c),
\]

with one \(f_j\) per component; equivalently it is the tensor product of the
component algebras. In particular, one nonempty component has exactly

\[
 R[f_j]/(f_j^2-f_j).
\]

A constant vertex has already been eliminated, so two relations that shared
only that vertex do not acquire a spurious edge. Additional proved edges within
one component merely repeat equality of its one orientation variable. This
establishes the candidate's coordinate-algebra claim, including its
disconnected-component qualification.

## 6. Shifted-root coherence is screened and conditional

For one shifted quadratic with public roots \(A_i,B_i\), the retained screen
is exactly that \(A_i-B_i\) is a unit. Its algebra is then separable, and

\[
 Z_i=B_i+f_i(A_i-B_i),\qquad f_i^2=f_i.
\]

Separate quadratics have separate \(f_i\). The candidate explicitly says that
the quadratics alone do not synchronize them. A shifted family is called
coherent only after explicit relations have been proved to identify its
normalized variables in the reduced orientation graph.

The stated global-\(H\) example has the advertised common coordinate. Label
\(A_i\) as the \(E\)-root and \(B_i\) as the \(E^{-1}\)-root. Then the \(E\)
and \(E^{-1}\) sections have \(f_i=1\) and \(f_i=0\), respectively. Locally,
\(G=E\) at \(p\) and \(G=E^{-1}\) at \(q\), so the \(G\)-section has
\(f_i=(1,0)\) under CRT for every retained pair. The \(G^{-1}\)-section has
\(f_i=(0,1)\). Screening makes the normalization legitimate at both primes.

The phrase in the candidate is now “for every retained screened shift.” Thus
\(k=0\), or any other shift with coincident roots, is not assigned an undefined
normalized idempotent. No unspecified Dickson identity, finite collection of
quadratics, or unrelated root choice is claimed to establish coherence.

## 7. Endpoint theorem and algorithmic interface

For

\[
 \mathcal A=R[f]/(f^2-f),
\]

the ideals \((f)\) and \((f-1)\) are comaximal. Evaluation at the two endpoints
is therefore an isomorphism \(\mathcal A\cong R\times R\), and every class has
the unique form

\[
 Q(f)=Q(0)(1-f)+Q(1)f.
\]

If both endpoint values vanish in \(R\), then \(Q=0\) in the algebra. Now let
\(e\) be a nontrivial idempotent. Under CRT it is either \((1,0)\) or \((0,1)\).
For \(e=(1,0)\), the equation \(Q(e)=0\) says

\[
 Q(1)=0\pmod p,\qquad Q(0)=0\pmod q.
\]

If \(Q(1)\ne0\) in \(R\), it is nonzero modulo \(q\), so
\(\gcd(Q(1),N)=p\). If \(Q(0)\ne0\), then
\(\gcd(Q(0),N)=q\). The other nontrivial idempotent swaps the primes. This
proves both parts of Theorem 6.1 without assuming access to the CRT
decomposition in the public procedure.

For a finite system \(Q_j(f)=0\), if one mixed idempotent solves all equations
but an endpoint fails the system, at least one explicit equation fails there;
applying the preceding argument to that equation gives a proper gcd. If both
endpoints solve every equation, each \(Q_j\) is zero in \(\mathcal A\), so the
whole system is tautological on this component.

The candidate now makes the algorithmic interface literal. An explicit
relation is a public, factor-free arithmetic expression of polynomial size.
Both endpoint assignments consist only of known public roots. Evaluating such
an expression modulo \(N\), reducing intermediate values modulo \(N\), and
taking the endpoint gcds therefore has polynomial bit cost and requires no
hidden factor, hidden idempotent, or mixed root. If a solver instead returns a
mixed solution, the candidate compares a returned screened coordinate in that
same mixed section with its two public roots. It no longer suggests that an
unrelated sampled anchor supplies the missing corresponding mixed value.

The system statement is deliberately one-component and equation-by-equation.
It does not quantify over arbitrary polynomials in independent
\(f_1,\ldots,f_c\), and it excludes auxiliary existential variables. Thus the
known counterexample \(f_1-f_2=0\) to an unreduced multicomponent endpoint
argument is outside the theorem exactly as required.

## 8. Extraction and exact scope

For a screened pair \(A,A^{-1}\), a nontrivial idempotent \(e\) gives

\[
 X=A^{-1}+e(A-A^{-1}).
\]

At one hidden prime \(X=A\), and at the other \(X=A^{-1}\). Since the root
difference is a unit, the two gcds

\[
 \gcd(X-A,N),\qquad \gcd(X-A^{-1},N)
\]

are exactly \(p\) and \(q\), in some order. Conversely, known factors construct
the two nontrivial CRT idempotents and hence all mixed coordinates. This proves
the stated deterministic polynomial-time equivalence on the screened distinct-
odd-semiprime promise. It does not produce the idempotent.

The final classification stays within that proof. It covers only finite
explicit polynomial relations on one screened, linearly reduced component
whose common orientation has already been proved. It explicitly excludes raw
double-root schemes, unproved shifted coherence, arbitrary cross-component
couplings, auxiliary witnesses, metric or ordered rules, opaque or stochastic
root samplers, derivatives, lifts modulo \(N^2\), and lucky-gcd distributions.
It also leaves prime powers, repeated prime factors, even inputs, products of
three or more primes, recursion, almost-sure termination, and a uniform
Las Vegas bit bound open. Hence it is a narrow method classification consistent
with P57 and X51, not a resolution or lower bound for integer factoring.

PASS AS WRITTEN
