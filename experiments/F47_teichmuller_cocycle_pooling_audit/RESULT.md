# F47 focused hostile audit

**Artifact audited:**
`experiments/F47_teichmuller_cocycle_pooling_kill/RESULT.md`

**Candidate SHA-256:**
`2a667261e61979aca3b0ba11b7605b750bb18bff9cb8274c318782cadc9adce2`

**Audit mode:** proof-only. I ran no finite number-theoretic experiment and
used no web source. I read the candidate in full together with `PROMPT.md`,
the preregistered F12/F47 row of `REGISTRY.md`, and P22/X16. I reconstructed
the claims independently and tried to falsify their strongest quantifiers,
especially at repeated odd primes and at \(2^e\).

## Verdict

**PASS.** I found no false identity, sign error, representative ambiguity,
prime-power exception, quantifier leak, hidden factoring call, or unsupported
all-input conclusion in the candidate as written. No mathematical repair is
required before the prescribed fresh proof-blind reconstruction.

The pass is deliberately narrow. It certifies that a genuine finite network of
multiplicative relations has one public global solution to its normalized
carry equations, and therefore cannot reveal a factor through a local linear
consistency failure. It does not synchronize the ranks of the coefficient
matrix in different CRT fields and says nothing decisive about its minors or
Smith data, nonlinear processing, higher integer quotients, additive
relations, engineered bases used outside this decoder, power-map inversion,
or all-input factorization.

## 1. The exponent-\(N\) lift is well defined for every \(N\ge2\)

Let \(G_N=(\mathbb Z/N\mathbb Z)^\times\). If integers \(r\) and \(r+kN\)
represent the same element of \(G_N\), then

\[
(r+kN)^N-r^N
=N r^{N-1}kN+
  \sum_{j=2}^{N}\binom Nj r^{N-j}(kN)^j
\equiv0\pmod {N^2}.
\]

The first term already contains \(N^2\), and every later term contains at
least \(N^2\). This argument has no parity or squarefreeness premise and also
covers \(N=2\). Thus

\[
A([r]_N)=[r^N]_{N^2}
\]

is independent of the representative. Since a unit modulo \(N\) is also a
unit modulo \(N^2\), the codomain is the unit group.

For base classes \(a,b\), the integer product of representatives is a
representative of \(ab\). Therefore

\[
A(ab)=[(rs)^N]_{N^2}=A(a)A(b)
\quad\text{in }(\mathbb Z/N^2\mathbb Z)^\times.
\]

This proves the homomorphism claim. It also checks the candidate's important
distinction: canonical integer representatives need a final reduction, while
the residue classes multiply exactly. Reduction gives the homomorphism

\[
x(a)=A(a)\bmod N,
\qquad x(ab)=x(a)x(b)\pmod N.
\]

Writing the canonical representatives as

\[
A(a)=x(a)+Nh(a),
\quad 0\le x,h<N,
\]

defines \(h\) uniquely as a function of the base class. It does not by itself
make \(h\) a function of the possibly colliding value \(x(a)\), exactly as the
candidate warns.

## 2. Carry law, normalization, inverses, and cocycle signs

Put \(x=x(a)\), \(y=x(b)\),

\[
z=\langle xy\rangle_N=x(ab),
\qquad c(x,y)=\frac{xy-z}{N}.
\]

Because \(x,y,z\) are canonical integers, \(c\) is an exact public integer.
Expanding modulo \(N^2\) gives

\[
\begin{aligned}
A(a)A(b)
&=(x+Nh(a))(y+Nh(b))\\
&\equiv z+N\{c+xh(b)+yh(a)\}\pmod {N^2}.
\end{aligned}
\]

Comparison with \(A(ab)=z+Nh(ab)\) proves

\[
h(ab)\equiv c+xh(b)+yh(a)\pmod N.
\]

There is no missing minus sign: the convention is \(xy=z+Nc\). Since \(z\)
is a unit, define

\[
\lambda(a)=h(a)x(a)^{-1},
\qquad \kappa(x,y)=c(x,y)z^{-1}\pmod N.
\]

Now \(z^{-1}x=y^{-1}\) and \(z^{-1}y=x^{-1}\) modulo \(N\), so the normalized
identity is exactly

\[
\lambda(ab)=\lambda(a)+\lambda(b)+\kappa(x(a),x(b))
\pmod N.
\tag{2.1}
\]

The inverse specialization is a useful independent sign check. Let
\(\bar x=\langle x^{-1}\rangle_N\) and
\(c_x=(x\bar x-1)/N\). Since \(A(1)=1\) and \(\lambda(1)=0\), (2.1) gives

\[
\lambda(a^{-1})=-\lambda(a)-c_x\pmod N,
\]

because the product residue is \(1\). The same formula follows directly from

\[
0\equiv c_x+xh(a^{-1})+\bar x h(a)\pmod N.
\]

Thus both normalization and inverse conventions agree.

For a structural cocycle check, let \(s(u)\) be the canonical integer section
from \(G_N\) into \((\mathbb Z/N^2\mathbb Z)^\times\). Then

\[
s(x)s(y)=s(xy)\{1+N\kappa(x,y)\}\pmod {N^2}.
\]

The kernel elements \(1+Nt\) form a central copy of the additive group
\(\mathbb Z/N\mathbb Z\). Comparing the two parenthesizations of \(s(x)s(y)s(w)\)
therefore yields

\[
\kappa(x,y)+\kappa(xy,w)
=\kappa(y,w)+\kappa(x,yw)\pmod N.
\]

This is exactly the central \(2\)-cocycle identity under the candidate's
convention. Equation (2.1) says that its pullback along the homomorphism \(x\)
is the coboundary

\[
\delta\lambda(a,b)=\lambda(ab)-\lambda(a)-\lambda(b).
\]

Changing the section coherently would change both the digit and the factor set
by a coboundary; it would not create an inconsistency. Extra noncanonical lift
data, however, is correctly left outside the theorem.

## 3. Occurrence-labelled relation graphs

For an edge \(e\) with exact base-class relation

\[
a_{t(e)}=a_{s(e)}a_{m(e)},
\]

equation (2.1) reads

\[
\lambda_{t(e)}-\lambda_{s(e)}-\lambda_{m(e)}=\kappa_e.
\]

If two or all three roles use the same occurrence, collecting their
coefficients gives the candidate's row of \(B\); no special case is lost.
Consequently the entire finite multigraph satisfies the literal identity

\[
B\lambda=\kappa
\quad\text{over }R=\mathbb Z/N\mathbb Z.
\tag{3.1}
\]

This proves, rather than assumes, global compatibility. In particular:

1. every edge residual and every \(R\)-linear combination of residuals is
   zero, even when the combining matrix is chosen adaptively after seeing the
   public transcript;
2. every left syzygy \(\alpha^TB=0\) gives
   \(\alpha^T\kappa=0\), including path, triangle, and cycle eliminations;
3. reducing the displayed global solution modulo any \(d\mid N\) supplies a
   solution in that component; and
4. for every prime \(p\mid N\),
   \(\kappa_p=B_p\lambda_p\), hence
   \(\operatorname{rank}_{\mathbb F_p}[B_p\mid\kappa_p]
    =\operatorname{rank}_{\mathbb F_p}B_p\).

The corresponding unnormalized residual is an integer multiple of \(N\).
Its residue modulo \(N\) is zero, so a direct gcd returns \(N\), not a proper
factor. Dividing the integer residual by \(N\) and studying the next digit is a
different operation and is properly retained as open.

Equation (3.1) does **not** imply

\[
\operatorname{rank}(B\bmod p)=\operatorname{rank}(B\bmod q).
\]

It also does not synchronize arbitrary minors or Smith invariants of \(B\),
the ranks of an unnormalized matrix whose entries include \(x\)-values,
nonlinear eliminants, or graph statistics. The candidate consistently excludes
those stronger claims. In particular it kills augmented-versus-coefficient
inconsistency, not every possible use of the coefficient matrix.

Occurrence labels are essential to (3.1): \(\lambda_v\) is computed from the
actual base occurrence. Repeated roles, loops, repeated products, and multiple
paths cause no problem. Quotienting distinct occurrences merely because their
\(x\)-labels collide requires a separate descent theorem, checked next.

## 4. Squarefree descent, including the factor \(2\)

First suppose \(p\mid N\) is odd and occurs to exponent one. Write \(N=pm\)
with \(p\nmid m\). A unit lift modulo \(p^2\) has the unique form

\[
a=\omega(1+pt),
\]

where \(\omega\) is the Teichmüller lift of \(a\bmod p\). Since

\[
(1+pt)^{pm}\equiv1\pmod {p^2},
\qquad \omega^{pm}=\omega^m,
\]

we get

\[
A(a)\equiv\omega^m\pmod {p^2}.
\]

Meanwhile \(x(a)\bmod p=a^{pm}=a^m\bmod p\), so \(\omega^m\) is precisely the
Teichmüller lift of \(x(a)\bmod p\). Hence

\[
A(a)\equiv[x(a)\bmod p]_p\pmod {p^2}.
\tag{4.1}
\]

For squarefree \(N\), (4.1) at every odd prime and CRT over the pairwise
coprime moduli \(p^2\) prove that \(A\) is determined by \(x\).

The even squarefree component is also correct. If \(2\parallel N\), then \(N\)
is even and every unit representative is odd, so \(a^N\equiv1\pmod4\). This is
the unique lift of the sole element of \(\mathbb F_2^\times\). Thus an even
squarefree \(N\) has the same descent property.

The local digit formula has the claimed scale and sign. For canonical global
\(x\), define

\[
q_p(x)=\frac{[x\bmod p]_p-x}{p}\pmod p.
\]

Reducing \(A=x+pmh\) modulo \(p^2\) and using (4.1) gives

\[
h\equiv m^{-1}q_p(x),
\qquad
\lambda\equiv m^{-1}x^{-1}q_p(x)\pmod p.
\]

If \(z=\langle xy\rangle_N\) and \(xy=z+pmc\), multiplication of the two local
Teichmüller lifts gives

\[
q_p(z)\equiv mc+xq_p(y)+yq_p(x)\pmod p,
\]

which normalizes to the reduction of (2.1). Therefore equal \(x\)-values imply
equal \(A,h,\lambda\) on squarefree inputs, even though the power map
\(a\mapsto x(a)\) itself need not be injective.

## 5. Repeated odd primes: the retained coordinate is exact

Let \(p^e\parallel N\) for odd \(p\), write \(N=p^e m\), and \(p\nmid m\).
At precision \(p^{2e}\), decompose the unit lift uniquely as

\[
a=\omega\eta,
\qquad \omega^{p}=\omega,
\qquad \eta\in1+p\mathbb Z_p.
\]

Then

\[
A(a)=a^{p^e m}
\equiv\omega^m\eta^{p^e m}\pmod {p^{2e}}.
\tag{5.1}
\]

For \(\eta\in1+p\mathbb Z_p\), the principal factor satisfies

\[
\eta^{p^e m}\equiv1\pmod {p^{e+1}},
\]

so in particular

\[
x(a)\equiv\omega^m\pmod {p^e}.
\tag{5.2}
\]

The candidate's isomorphism follows exactly from the odd \(p\)-adic logarithm.
It identifies

\[
\frac{1+p\mathbb Z_p}{1+p^e\mathbb Z_p}
\quad\text{with}\quad
\frac{p\mathbb Z_p}{p^e\mathbb Z_p}
\]

and

\[
\frac{1+p^{e+1}\mathbb Z_p}{1+p^{2e}\mathbb Z_p}
\quad\text{with}\quad
\frac{p^{e+1}\mathbb Z_p}{p^{2e}\mathbb Z_p}.
\]

Under these identifications, raising to \(p^e m\) is multiplication by
\(p^e m\). Its kernel on the first quotient is trivial, because

\[
p^e m t\in p^{2e}\mathbb Z_p
\Longleftrightarrow t\in p^e\mathbb Z_p,
\]

and it is surjective because \(m\) is a \(p\)-adic unit. Both quotients have
order \(p^{e-1}\). This includes the trivial \(e=1\) case; for every \(e\ge2\)
it proves that \(x\bmod p^e\) erases the input principal coordinate while
\(A\bmod p^{2e}\) retains that coordinate bijectively.

The symbolic counterexample is also correct for every odd \(p\). For \(N=p^2\)
take \(a=1\), \(b=1+p\pmod {p^2}\). Both have \(x=1\), while

\[
(1+p)^{p^2}\equiv1+p^3\pmod {p^4}.
\]

For the last congruence, the \(j=2\) binomial term has valuation at least four;
the \(j=3\) term has valuation at least five when \(p>3\) and at least four
when \(p=3\); all \(j\ge4\) terms visibly contain \(p^4\). Thus
\(A(a)\ne A(b)\), and \(h(a)=0\), \(h(b)=p\pmod {p^2}\). This directly
refutes any unlabelled same-\(x\) merge at a repeated odd prime.

## 6. The \(2\)-adic cases and the global iff criterion

Let \(2^e\parallel N\) and \(m=N/2^e\), so \(m\) is odd.

- If \(e=1\), an odd \(a\) satisfies \(a^N\equiv1\pmod4\).
- If \(e=2\), the exponent is divisible by four and every odd \(a\) satisfies
  \(a^4\equiv1\pmod {16}\), so \(A(a)\equiv1\pmod {16}\).
- If \(e\ge3\), every \(2\)-adic unit decomposes uniquely as
  \(a=(-1)^\epsilon\eta\), \(\eta\in1+4\mathbb Z_2\). The even exponent kills
  the sign and

  \[
  A(a)\equiv\eta^{2^e m}\pmod {2^{2e}},
  \qquad x(a)\equiv1\pmod {2^e}.
  \]

For \(e\ge3\), the \(2\)-adic logarithm is an isomorphism on
\(1+4\mathbb Z_2\). It changes the candidate's map into multiplication by
\(2^e m\) from

\[
4\mathbb Z_2/2^e\mathbb Z_2
\quad\text{to}\quad
2^{e+2}\mathbb Z_2/2^{2e}\mathbb Z_2.
\]

The kernel is trivial, the map is onto because \(m\) is odd, and both groups
have order \(2^{e-2}\). Thus the exact isomorphism and the count of \(e-2\)
retained signless principal bits are correct, including the boundary case
\(e=3\).

These local results prove both directions of the global criterion.

- If every odd prime occurs once and \(8\nmid N\), each odd component satisfies
  (4.1), while the possible \(2\)-part of order \(2\) or \(4\) has constant
  local \(A\). Hence the CRT tuple \(A\bmod N^2\) is determined by
  \(x\bmod N\).
- If an odd \(p^e\), \(e\ge2\), divides \(N\), vary its principal input
  coordinate through the isomorphism of Section 5 while fixing its
  Teichmüller coordinate and every other local base. Then global CRT gives two
  unit base classes with equal \(x\) and unequal \(A\).
- If \(2^e\parallel N\), \(e\ge3\), do the same with the signless principal
  coordinate from the (2)-adic isomorphism.

Therefore \(A\), and equivalently \(h\), is determined by \(x\) on all unit
inputs if and only if the odd part of \(N\) is squarefree and \(8\nmid N\).
There is no omitted \(4\parallel N\) exception.

## 7. Boundaries, collision handling, and bit complexity

The normalized theorem is correctly restricted to units. If a sampled base is
not a unit, its gcd with \(N\) either supplies a proper factor or is a trivial
outcome to reject. No conclusion about a separate nonunit decoder is inferred.

The canonical section is used consistently in every carry. The product base is
an equality of classes modulo \(N\), so replacing a representative before
exponentiating does not alter \(A\). Equal base classes can always share a
vertex value. Equal \(x\)-values can share one only under the proven descent
criterion; occurrence labels prevent precisely the false identification on
general inputs. These observations also cover repeated products and multiple
paths without assuming injectivity of \(x\).

Let \(n=\lceil\log_2(N+1)\rceil\). Binary exponentiation uses \(O(n)\) modular
multiplications modulo \(N^2\); with schoolbook arithmetic each acts on
\(O(n)\)-bit values and costs \(O(n^2)\) bit operations. Thus the stated
\(O(n^3)\) cost per vertex is valid. Exact division by \(N\) and extended gcd
for inverses fit within that bound. An edge needs only a constant number of
\(O(n)\)-bit products, reductions, an exact carry division, and (if not already
stored at its target) one inverse, all in \(O(n^2)\) classical bit operations.
Reduction after every ring operation controls intermediate lengths.

Consequently the advertised

\[
O(Vn^3+En^2)
\]

bound for constructing the vertex transcript and all edge residuals is sound.
It is conditional, as stated, on a factor-free relation generator and
\(V,E=\operatorname{poly}(n)\). It does not price an exponentially large graph
or an exponentially large pooling matrix as polynomial.

## 8. Material scope relative to P22/X16

P22/X16 closes direct gcds of a fixed polynomial-size list of canonical high
digits from a uniform base on an infinite balanced semiprime family, plus the
specified consecutive and additive carriers. It expressly leaves cross-base
relations and engineered bases open.

F47 is a different deterministic statement. It allows arbitrarily selected
unit bases and any finite genuine multiplicative relation graph, but closes
only the proposed linear carry-cocycle inconsistency signal. It proves no
rarity or distribution theorem for the digits. The candidate correctly leaves
all of the following outside its conclusion:

- additive and other nonmultiplicative relations;
- ranks of \(B\) across different CRT fields, arbitrary minors, Smith data,
  resultants, and nonlinear eliminants;
- nonlinear functions of the transcript, graph, or collision fibres;
- engineered bases used by a decoder not equivalent to the killed linear
  consistency test;
- inversion or partial inversion of \(a\mapsto x(a)\);
- integer quotients after a modular residual vanishes, higher levels, and
  noncanonical extra lift data; and
- inverse-polynomial separation, arbitrary composite recursion, and complete
  all-input factorization.

Thus this PASS cannot be promoted as a broad hardness theorem for
\(N^2\)-adic mechanisms. It supports only the candidate's exact disposition:
method failure for genuine multiplicative linear-cocycle inconsistency
pooling.

## 9. Evidence and presentation checks

The candidate hash above was taken from the exact bytes audited. A byte-level
check found valid UTF-8, no disallowed ASCII control character, no carriage
return, and a final newline. Its displayed equations, section boundaries, and
minus signs are intact. The proof-only declaration is accurate: this audit ran
no finite mathematical computation, so it needs no computation-ledger entry.

An audit file cannot contain its own whole-file cryptographic hash without a
self-reference convention. The exact finalized SHA-256 of this audit artifact
is therefore reported to the root agent alongside this disposition rather than
embedded here.

The hostile-audit disposition is **PASS**, with no mathematical repair request.
The next required step is a fresh context-free end-to-end reconstruction from
the statement and key ideas only.
