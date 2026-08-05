# F23 hostile audit: canonical small-degree isogeny neighbors

**Status:** hostile audit of `experiments/F23_canonical_isogeny_neighbor_kill/RESULT.md`.

**Protocol:** proof-only. No computation, benchmark, database query, or public-web search was used. Every numerical identity needed below is expanded or reduced explicitly.

**Verdict:** **the central narrow obstruction survives, but only after material scope corrections.** The fixed `j=1728`, degree-two construction gives a sound factoring-equivalent **fine-kernel** promise on distinct odd semiprimes, while the coarse modular-polynomial root problem is genuinely weaker. The original report must:

1. replace the phrase “an `R`-valued cyclic subgroup” by a finite étale rank-two subgroup scheme, or explicitly by its unique nonidentity section;
2. delete the unqualified claim about “the codomain `j` together with a verifiable descended isogeny” and state the exact exposed representation required;
3. list the exceptional characteristics and root-collision primes explicitly;
4. restrict the irreducibility argument to universal characteristic-zero rational selectors;
5. retract the claim that all descending CM edges form an automorphism/class-group orbit, and treat the CM discussion only as a boundary for the fixed public-orientation mechanism.

With those repairs, blind reconstruction is warranted for the strongest corrected theorem in Section 12 below. It is not warranted for the original broader prose.

## 1. Exact modular-polynomial normalizations

The report uses the standard symmetric classical modular polynomial, monic of degree \(\ell+1\) in each variable and satisfying

\[
\Phi_\ell(j(\tau),j(\ell\tau))=0.
\]

### 1.1 Degree two at `j=0`

Substitution of `X=0` into the displayed \(\Phi_2\) gives

\[
Y^3-162000Y^2+8748000000Y-157464000000000.
\]

Since

\[
3(54000)=162000,\qquad
3(54000)^2=8748000000,\qquad
(54000)^3=157464000000000,
\]

the exact identity is

\[
\boxed{\Phi_2(0,Y)=(Y-54000)^3.}
\]

There is no sign error.

### 1.2 Degree two at `j=1728`

Coefficient comparison after substituting `X=1728` gives

\[
\boxed{\Phi_2(1728,Y)=(Y-1728)(Y-287496)^2.}
\]

For example, the \(Y^2\)-coefficient on both sides is

\[
-1728^2+1488\cdot1728-162000=-576720
=-(1728+2\cdot287496).
\]

The two coarse roots collide modulo exactly the primes dividing

\[
287496-1728=285768=2^3 3^6 7^2.
\]

Thus they are distinct in characteristic \(r\) exactly when

\[
r\notin\{2,3,7\}.
\]

The level itself is non-étale in characteristic \(2\). In characteristics \(3\) and \(7\), the two integer branch values coincide even though the kernel-coordinate distinction may remain meaningful.

### 1.3 Degree three at `j=0`

In the same classical normalization, the `X=0` coefficients are

\[
Y^4+36864000Y^3+452984832000000Y^2
+1855425871872000000000Y.
\]

For \(a=12288000\),

\[
3a=36864000,\quad
3a^2=452984832000000,\quad
a^3=1855425871872000000000.
\]

Hence

\[
\boxed{\Phi_3(0,Y)=Y(Y+12288000)^3.}
\]

The nonzero root is \(-12288000\), not \(+12288000\). Its difference from the self-root factors as

\[
12288000=2^{15}\cdot3\cdot5^3.
\]

Therefore the two roots are distinct only outside \(\{2,3,5\}\); characteristic \(3\) is also the level characteristic. The usual characteristic-zero branch description—one ramified CM self-neighbor and three descending kernels with the common coarse value \(-12288000\)—should be asserted after excluding these reduction anomalies, not uniformly in every characteristic.

For \(\Phi_2(0,Y)\), the sole neighbor value collides with the source value `0` at the primes dividing

\[
54000=2^4 3^3 5^3.
\]

These primes also need exclusion from any claim that the source and target coarse values are distinct.

## 2. The degree-two quotient calculation is correct

Let \(R\) be a ring in which \(2A\) is a unit and

\[
E_A:y^2=x^3+Ax.
\]

The discriminant is \(-64A^3\), so this is an elliptic curve over \(R\). Its nonidentity two-torsion sections have \(y=0\) and

\[
x(x^2+A)=0.
\]

For the public point \(P_0=(0,0)\), the standard quotient formula

\[
y^2=x^3+a x^2+b x
\quad\longmapsto\quad
y^2=x^3-2a x^2+(a^2-4b)x
\tag{2.1}
\]

gives

\[
E_A/\langle P_0\rangle:
y^2=x^3-4Ax,
\]

whose \(j\)-invariant is \(1728\).

Now let \(s^2=-A\) and translate \(x=u+s\). The source becomes

\[
y^2=u^3+3su^2-2Au.
\]

Applying (2.1) gives coefficients

\[
a'=-6s,\qquad b'=9s^2+8A=-A=s^2.
\]

For a model \(y^2=x^3+a'x^2+b'x\), one has

\[
j=256\frac{(a'^2-3b')^3}{b'^2(a'^2-4b')}.
\]

Therefore, in every odd characteristic,

\[
j=256\frac{(33s^2)^3}{s^4(32s^2)}
=8\cdot33^3
=287496.
\]

The quotient discriminant is a unit because \(s\) and \(2\) are units. Replacing \(s\) by \(-s\) changes the quotient model but not its coarse \(j\)-invariant. This explains the double factor.

## 3. Coarse rationality does not imply descent

Let \(k=\mathbb F_r\) with \(r\) odd and \(A\ne0\). A separable degree-two isogeny from \(E_A\) over \(k\) is defined over \(k\) only if its kernel subgroup scheme is defined over \(k\). A rank-two subgroup of \(E_A[2]\) has a unique nonidentity geometric point, so Galois stability of the subgroup is equivalent to rationality of that point.

Consequently, the two nonpublic kernels descend over \(k\) exactly when

\[
\left(\frac{-A}{r}\right)=1.
\tag{3.1}
\]

If \((-A/r)=-1\), neither nonpublic isogeny descends from the fixed curve \(E_A\), even though \(287496\in k\) remains a literal double root of

\[
\Phi_2(1728,Y).
\]

This is a genuine stack/coarse-moduli effect. At the extra-automorphism point \(j=1728\), the automorphism of the source exchanges the two nonpublic geometric kernels. They form one coarse orbit, and its target \(j\)-value is rational even when no member of the orbit is a rational subgroup of the fixed twist \(E_A\). A rational point on the plane coarse correspondence is not automatically a lift to an isogeny object from that fixed source curve.

This also answers the audit's explicit question: **yes, the double coarse root \(287496\) can be \(\mathbb F_r\)-rational without any descended isogeny from \(E_A\)**. The \(N=143\) example supplies such a good-characteristic instance at \(r=11\).

## 4. Exact subgroup-scheme formulation

The original phrase “an \(R\)-valued cyclic subgroup” is not precise. The correct object is a finite locally free cyclic subgroup scheme \(C\subset E_A[2]\) of rank two over

\[
R=\mathbb Z/N\mathbb Z,\qquad N=pq
\]

for distinct odd primes \(p,q\).

There are no hidden non-étale or “mixed-scheme” exceptions:

1. Since \(2\) is a unit and \(E_A\) is smooth, \(E_A[2]\) is finite étale over \(R\).
2. Every closed rank-two subgroup \(C\) is therefore finite étale.
3. The identity section is an open-and-closed rank-one component of \(C\); its complement is finite étale of rank one and hence is a unique \(R\)-section \(P_C\).
4. Conversely, the subgroup generated by any everywhere nonidentity two-torsion section is finite étale of rank two.

Writing \(P_C=(u,0)\), this is exactly the congruence

\[
u(u^2+A)=0\pmod N.
\tag{4.1}
\]

The public subgroup \(C_0=\langle(0,0)\rangle\) corresponds to \(u=0\). Because \(R\cong\mathbb F_p\times\mathbb F_q\) is reduced, \(C\) differs from \(C_0\) in at least one CRT component exactly when

\[
u\not\equiv0\pmod N.
\tag{4.2}
\]

Thus (4.1)–(4.2) are genuinely equivalent to the **exposed-generator** version of the subgroup problem. They are not equivalent to returning only a coarse root of \(\Phi_2\).

## 5. Correct fine-neighbor promise theorem

### Theorem 5.1

Let

\[
N=pq
\]

be a product of distinct odd primes, and let \(A\in(\mathbb Z/N\mathbb Z)^\times\) satisfy

\[
\left(\frac{-A}{N}\right)=-1.
\tag{5.1}
\]

The task of returning \(u\) satisfying (4.1)–(4.2) is Las Vegas randomized-polynomial-time equivalent, under verified reductions, to factoring distinct odd semiprimes.

### Fine output gives a factor

Condition (5.1) says that the two local Legendre symbols are opposite. Relabel so that

\[
\left(\frac{-A}{p}\right)=-1,\qquad
\left(\frac{-A}{q}\right)=1.
\]

Modulo \(p\), the only root of \(T(T^2+A)\) is \(0\), so \(u\equiv0\pmod p\). If also \(u\equiv0\pmod q\), then \(u=0\) in \(R\), contradicting (4.2). Hence \(u\not\equiv0\pmod q\), and for any integer representative \(\tilde u\),

\[
\boxed{\gcd(\tilde u,N)=p.}
\]

The equations and nonzero condition are checked with a constant number of \(O(\log N)\)-bit modular operations before accepting the gcd.

### Factors construct the fine output

Given \(p,q\), compute the two Legendre symbols, find a square root \(s^2=-A\) on the split side, and CRT-combine \(s\) there with \(0\) on the nonsplit side. A finite-field square root can be found by a standard Las Vegas procedure: random search finds a quadratic nonresidue with expected constant trials, and modular exponentiation/Tonelli–Shanks then uses polynomially many bit operations. The resulting \(u\) satisfies (4.1)–(4.2).

### Reduction from arbitrary distinct odd semiprimes to the promise

For unknown \(N=pq\), sample \(A\) uniformly modulo \(N\). Compute \(g=\gcd(A,N)\):

- if \(1<g<N\), return \(g\);
- if \(g=N\), resample;
- if \(g=1\), compute the Jacobi symbol and invoke the promise solver only when (5.1) holds.

The probability per raw sample of reaching a valid promise input is exactly

\[
\frac{(p-1)(q-1)}{2pq}\ge \frac4{15},
\]

with equality at \(\{p,q\}=\{3,5\}\). Thus the expected number of raw trials is at most \(15/4\), even before crediting proper-gcd successes. Exact uniform sampling by \(n\)-bit rejection has acceptance probability at least \(1/2\), so random-bit generation also has polynomial expectation. Jacobi symbols, gcds, modular products, verification, and the single reached promise call preserve polynomial expected bit complexity. Almost-sure termination follows from the positive independent success probability and the Las Vegas premise for the solver.

This theorem is the exact \(2\)-isogeny form of P07's quadratic Jacobi bottleneck.

## 6. The codomain-`j` extension must be narrowed

The following original sentence is too broad:

> “If the oracle instead returns the codomain \(j\) together with a verifiable descended isogeny, ...”

An unspecified valid isogeny may be the public isogeny in every CRT component. More importantly, “verifiable” does not define an output representation from which the kernel or a branch-selective coefficient can be recovered. A coarse \(j'\) plus an opaque certificate is not equivalent to (4.1).

The valid corrected statement is:

> If the output explicitly exposes a selective kernel generator \(u\), a normalized degree-two kernel polynomial, or another representation from which that generator is deterministically recoverable in polynomial bit complexity, Theorem 5.1 applies. If, in addition, it supplies the quotient \(j_C\) of that same certified selective subgroup, then away from \(\{2,3,7\}\) its local values are \(1728\) and \(287496\), and one of
> \[
> \gcd(j_C-1728,N),\qquad \gcd(j_C-287496,N)
> \]
> is a proper factor.

For inputs divisible by \(3\) or \(7\), direct trial division by those fixed primes handles the exceptional semiprime cases. This does not justify extraction from an arbitrary coarse root, arbitrary valid isogeny, or unspecified proof object.

## 7. The \(N=143\) certificate is exact

For \(N=11\cdot13\), \(A=1\):

- \(T^2+1\) is irreducible modulo \(11\) and split modulo \(13\);
- both reductions of \(y^2=x^3+x\) are good;
- \(1728\equiv12\pmod{143}\) and \(287496\equiv66\pmod{143}\);
- the roots are distinct modulo both primes because neither prime is in \(\{2,3,7\}\).

The element \(u=44\) satisfies

\[
u\equiv0\pmod{11},\qquad u\equiv5\pmod{13},\qquad 5^2\equiv-1\pmod{13},
\]

and

\[
44(44^2+1)=85228=596\cdot143,\qquad
\gcd(44,143)=11.
\]

The mixed quotient value is \(j_C=1\pmod{143}\), since

\[
1728\equiv1\pmod{11},\qquad
287496\equiv1\pmod{13}.
\]

Therefore

\[
\gcd(1-12,143)=11,\qquad
\gcd(1-66,143)=13.
\]

The pure residue \(66\) is nevertheless a root of the coarse polynomial in both components. Modulo \(11\), where \(\left(\frac{-1}{11}\right)=-1\), it is not the target of a descended nonpublic two-isogeny from the fixed curve. This is the promised good-prime coarse/descent certificate.

## 8. Every public-exponent identity is correct

In

\[
S_r=\mathbb F_r[T]/(T^2+1),
\]

one has \(T^2=-1\) and \(T^4=1\). Since \(143\equiv3\pmod4\),

\[
143^i\equiv
\begin{cases}
3\pmod4,&i\text{ odd},\\
1\pmod4,&i\text{ even}.
\end{cases}
\]

Thus, for every \(i\ge1\), in both local algebras,

\[
T^{143^i}-T=
\begin{cases}
-2T,&i\text{ odd},\\
0,&i\text{ even}.
\end{cases}
\]

The true first local powers differ:

\[
T^{11}-T=-2T\quad\text{in }S_{11},\qquad
T^{13}-T=0\quad\text{in }S_{13}.
\]

No exponent or parity case was omitted. This is an exact instance of P06, not a new general obstruction to every \(N\)-dependent operation.

## 9. Precise scope of the no-section argument

For fixed prime \(\ell\), the classical \(\Phi_\ell(X,Y)\) is irreducible in

\[
\mathbb Q(X)[Y]
\]

and has degree \(\ell+1>1\) in \(Y\). Equivalently, the generic characteristic-zero cover \(X_0(\ell)\to X(1)\) is connected. Therefore no

\[
R(X)\in\mathbb Q(X)
\]

can satisfy \(\Phi_\ell(X,R(X))=0\): such a root would give a linear factor over \(\mathbb Q(X)\), or equivalently a rational section of the generic cover.

What this actually rules out is:

- one universal characteristic-zero rational function of the source \(j\);
- a fixed straight-line formula over \(\mathbb Q\) using only field operations, on the dense open set where its denominators are nonzero;
- similarly, a fixed finite algebraic branch scheme only if one branch must apply on a dense generic open and output such a rational function.

It does **not** rule out:

- algorithms whose operation sequence depends on \(N\) or on the characteristic;
- modular root algorithms using exponentiation or randomized branching;
- formulas involving additional curve, level, orientation, or metric data;
- a nonalgebraic bit algorithm.

Accordingly, “no rational section” is a precise selector-class obstruction, not a lower bound for polynomial-time isogeny selection.

## 10. Exact discriminant rare-event bound

Let

\[
D_\ell(X)=\operatorname{disc}_Y \Phi_\ell(X,Y).
\]

Characteristic-zero separability makes \(D_\ell\) a nonzero integer polynomial. Let \(d_\ell=\deg D_\ell\), and exclude the finite set of primes for which its reduction is the zero polynomial. Because \(\Phi_\ell\) is monic in \(Y\), a repeated geometric root at a specialization \(j\) is equivalent to \(D_\ell(j)=0\).

For uniform \(j\in\mathbb Z/pq\mathbb Z\), CRT independence and the elementary root bound give

\[
\Pr[D_\ell(j)\equiv0\pmod p
\text{ or }
D_\ell(j)\equiv0\pmod q]
\le \frac{d_\ell}{p}+\frac{d_\ell}{q}.
\tag{10.1}
\]

The event that \(\gcd(D_\ell(j),N)\) is proper is a subset of this union. For fixed \(\ell\) and balanced \(p,q\), (10.1) is exponentially small in \(\log N\).

This bound applies only to a uniform random source \(j\) and fixed \(\ell\). It does not prove that deliberately generated, nonuniform, or \(N\)-dependent sources cannot make asymmetric collisions frequent. A fixed integral discriminant root merely collides in both CRT components and is useless; constructing a CRT-asymmetric root would be a new localization mechanism.

## 11. CM claims that survive, and claims that do not

The sound standard statement is the following. Over characteristic zero, or for ordinary reductions of characteristic different from \(\ell\) with endomorphism ring exactly \(\mathcal O_D\), if \(\ell\) does not divide the conductor, the number of horizontal \(\ell\)-isogenies is

\[
1+\left(\frac D\ell\right)\in\{0,1,2\}.
\]

In the split case, the two horizontal directions are labeled by the conjugate primes of \(\mathcal O_D\) above \(\ell\). Given \(D,\ell\), choosing one of these characteristic-zero ideal labels is public. The label is Galois-equivariant and does not, by itself, name the unknown CRT factors \(p\) and \(q\).

Three qualifications are essential:

1. **Embedding data matter.** For class number greater than one, reducing a CM point and an ideal action requires a choice of prime/embedding in the ring class field. Two CRT components may realize different conjugates. The report correctly notes this as an open escape, and therefore may not conclude that the resulting coordinates are always synchronized.
2. **Vertical edges are not proved to be one orbit.** If \(\ell\) divides the conductor, the geometric volcano description distinguishes an ascending direction under the usual hypotheses. The remaining descending directions should not be asserted, without further hypotheses, to form “an automorphism/class-group orbit.” That phrase is unnecessary and is retracted.
3. **Quadratic splitting is only a shadow.** Ordinary versus supersingular behavior of a CM reduction has a quadratic splitting criterion away from finitely many ramified primes, but rational descent and orientation of a particular class action can depend on a fuller Frobenius class in a ring class field. It is not proved to reduce universally to one Jacobi symbol.

Thus the CM discussion supports only this narrow conclusion: a fixed characteristic-zero ideal label is not automatically a factor orientation, and the special \(j=0,1728\) coarse neighbors do not manufacture one. It does not close every higher-class-number, vertical, supersingular, or \(N\)-dependent CM construction.

## 12. Strongest corrected theorem and exact exclusions

### Corrected F23 theorem

For every distinct-odd-semiprime promise input

\[
(N,A),\qquad N=pq,\quad A\in(\mathbb Z/N\mathbb Z)^\times,\quad
\left(\frac{-A}{N}\right)=-1,
\]

returning a finite étale rank-two subgroup \(C\subset E_A[2]\) distinct from the public subgroup in at least one CRT component, **in a representation exposing its unique nonidentity section**, is Las Vegas randomized-polynomial-time equivalent to factoring distinct odd semiprimes. In coordinates, the exact output relation is

\[
u(u^2+A)=0\pmod N,\qquad u\not\equiv0\pmod N,
\]

and \(\gcd(u,N)\) is always a proper factor.

By contrast, returning an arbitrary root of

\[
\Phi_2(1728,Y)=0\pmod N
\]

is uninformative: the public integers \(1728\) and \(287496\) are roots in every CRT component, and \(287496\) can be rational even where no corresponding nonpublic isogeny descends from the fixed twist. The \(N=143,A=1\) certificate proves this without bad reduction or root collision. Replacing local Frobenius powers by \(N^i\) also fails on that certificate for every \(i\ge1\).

Finally, irreducibility of \(\Phi_\ell\) rules out only a universal rational-function selector from the generic source \(j\), and uniform random discriminant collisions occur with probability at most \(O_\ell(1/p+1/q)\) outside finitely many fixed characteristics.

### Explicit exclusions

The corrected theorem does **not** provide:

- a selector on prime powers, repeated factors, even inputs, products of more than two primes, or arbitrary composites;
- a complete factoring recursion;
- extraction from a coarse \(j\)-root or an unspecified isogeny certificate;
- a lower bound against nonalgebraic or \(N\)-dependent selectors;
- a closure of higher-class-number, vertical, supersingular, or embedding-sensitive CM routes.

For the coarse branch-value extraction, characteristics \(2,3,7\) are exceptional for \(\Phi_2(1728,Y)\). For \(\Phi_3(0,Y)\), the root-collision/level exceptions are \(2,3,5\). For \(\Phi_2(0,Y)\), the target value meets the source at \(2,3,5\). These are fixed public primes and can be trial-divided when a restricted semiprime reduction needs to remove them; that does not solve the omitted all-input cases.

## 13. Final audit disposition

**Survives:**

- all three integer modular-polynomial specializations, with the stated signs;
- the quotient formula and the \(1728/287496\) branch interpretation;
- rational coarse root without descended nonpublic isogeny;
- the exposed fine-kernel factoring equivalence and its constant-probability converse reduction;
- the complete \(N=143\) certificate and every \(N^i\) exponent identity;
- the narrow generic rational no-section obstruction;
- the fixed-\(\ell\), uniform-\(j\) discriminant rare-event bound.

**Retracted or narrowed:**

- “\(R\)-valued subgroup” terminology;
- extraction from “\(j\) plus a verifiable isogeny” without a specified exposed representation and selective condition;
- any universal synchronization claim for higher-class-number CM reductions;
- the descending-edge automorphism/class-group-orbit assertion;
- any implication that irreducibility or the discriminant bound excludes general polynomial-time selectors.

**Blind reconstruction:** warranted, but the reconstructor should receive only the corrected theorem and key ideas in Section 12, not the original proof or the retracted generalizations.
