# F62 hostile audit — exact order and HSP boundary

**Candidate audited:**
`experiments/F62_cross_relation_order_boundary/RESULT.md`

**Verified candidate SHA-256:**
`bc5419bb224cb95eb26e9b42bb786b0b193c2782552a835aa5cf72065abedf18`

**Verdict:** **FAIL as stated.**

The three numbered algebraic theorems are correct in their stated local
settings. The old-decoder image equality also survives negative lattice
coefficients. The arithmetic in the \(N=65\) witness is correct. The
multiplicity family has exact order \(2t\). The Smith-normal-form conclusion
for the unbounded subgroup target is correct after one wording repair.

The artifact nevertheless fails as an *exact F62 boundary*. It repeatedly
identifies all direct F62 screening with global 2-torsion search. F62 also
screens non-self-inverse CRT separators. This makes the opening claim, the
\(N=21\) bounded-source separation, two summary bullets, and the final theorem
target false for the full F62 operation. Two further strictness claims are
overstated: the \(N=65\) transcript has other individual blocks on which
ordinary order halving succeeds, and the stated odd-\(t\) family does not give
the claimed lower bound against unrestricted direct gcd screening.

No research computation was run for this audit. All checks below are symbolic
calculations or read-only inspection of existing proof-only artifacts.

## 1. The 2-torsion model — PASS only for the self-inverse subtarget

For an admissible vector \(v\), put

\[
g=q^v,
\qquad h=q^{E-v}.
\]

The candidate correctly proves

\[
h\equiv g^{-1}\pmod N
\]

and

\[
g\equiv h\pmod N
\quad\Longleftrightarrow\quad
g^2\equiv1\pmod N
\quad\Longleftrightarrow\quad
2v\in\Lambda_N.
\]

For odd \(N\), a self-inverse residue gives a factor through the two displayed
gcds exactly when it is not the global residue \(1\) or \(-1\). This part is
correct. In fact, in the non-global case both gcds are nontrivial and proper.

The opening assertion that the **direct splitting target** is exactly this
2-torsion problem is false for the F62 selector used elsewhere in the project.
For every selected state, F62 permits the direct tests

\[
\gcd(g-1,N),\qquad \gcd(g+1,N).
\]

One of these can be proper when \(g^2\not\equiv1\pmod N\). The existing F62
witness \(N=21,g=10\) is one example:

\[
10^2\not\equiv1\pmod {21},
\qquad
\gcd(10-1,21)=3.
\]

There is an even shorter counterexample inside the candidate's later
one-relation transcript:

\[
N=21,\qquad g=2,\qquad
2^2\not\equiv1\pmod {21},qquad
\gcd(2+1,21)=3.
\]

Thus non-global 2-torsion is sufficient for a direct split. It is not
necessary. General direct screening looks for a residue that equals one of
the signs modulo a nontrivial proper divisor of \(N\). For squarefree \(N\),
this is a strict nonempty collection of CRT components. For nonsquarefree
\(N\), a positive but possibly partial \(p\)-adic valuation can suffice.
Other components need not have either sign.

**Required correction.** Replace “direct splitting target” by “direct
self-inverse square-root subtarget” throughout. If the intended target is the
full F62 direct screen, state it using the two proper-gcd conditions, not
\(2v\in\Lambda_N\). The sentence that the final gcd is not the missing
operation remains reasonable, but the missing vector need not have its double
in \(\Lambda_N\).

## 2. Source multiplicities and integer magnitudes — FAIL as formalized

The block homomorphism and the bounded divisor model are otherwise sound.
For nonnegative \(v\le E\), the integer product \(q^v\) is a legal whole-block
divisor. The condition \(q^v<N\) is an integer condition. Modular reduction
does not preserve the legal-divisor provenance.

The multiplicity notation is inconsistent. Lines 65–72 say that repeated
presentations are repeated indexed rows, but then allow

\[
c_i\in\mathbb Z_{\ge0}
\]

with no capacity. An indexed submultiset of a finite occurrence list instead
has \(c_i\in\{0,1\}\). If \(i\) indexes row types with supplied capacities
\(\mu_i\), the correct condition is

\[
0\le c_i\le\mu_i.
\]

Unlimited \(c_i\) silently authorizes arbitrary reuse. It conflicts with the
later phrase “one-copy exponent box” and with the old decoder's finite
\(\{0,1\}\) occurrence vectors.

**Required correction.** Choose one source model and use it everywhere.
The clean model is a finite indexed occurrence list and \(c_i\in\{0,1\}\).
Deliberate amplification can first add explicit occurrences. Its transcript
length and runtime must then be charged. An equivalent capacity model is also
valid.

The claim that \(r/2\le M\) is required for a multiplicity scan is only a
necessary condition. Legal divisor feedback also requires the integer
magnitude condition

\[
q^{r/2}<N.
\]

Residue-power screening does not require this condition, but it is a different
operation. The order section should state this distinction at the point where
it discusses success under a multiplicity cap.

## 3. Old-decoder image equality — PASS

The equality

\[
R_{\rm old}
=
\{\Phi_N(v):v\in\mathbb Z^s,\ 2v\in L_0\}
\]

is correct as an equality of **modular residue images**.

Negative relation coefficients do not break the converse. Given

\[
2v=\sum_i z_i\lambda_i,
\]

choose \(c_i\in\{0,1\}\) with \(c_i\equiv z_i\pmod2\), including when
\(z_i<0\). Then \(z=c+2w\) for \(w\in\mathbb Z^m\), and

\[
v=
\frac12\sum_i c_i\lambda_i+
\sum_iw_i\lambda_i.
\]

The first summand is integral. The second can contain negative block
exponents, but this is harmless under \(\Phi_N\): every block is a unit and
every row maps to \(1\). Hence it changes no residue.

This is not an equality of positive integer roots or legal bounded divisors.
A vector with negative coordinates need not define an integer block product.
It also need not obey \(0\le v\le E\) or \(q^v<N\). The candidate mostly
protects itself by saying “image,” but the later quotient-group paragraph
drops these restrictions.

The quotient description

\[
Q_0=\mathbb Z^s/L_0,
\qquad K=\Lambda_N/L_0
\]

correctly identifies the old visible image with the image of \(Q_0[2]\) in
\(Q_0/K\). However, the displayed conditions

\[
x\notin K,
\qquad 2x\in K
\]

only describe a nonidentity involution in the abstract quotient. They do not
make it an F62 candidate.

**Required correction.** Add that the class must have a representative
\(v\) in the current source box with \(q^v<N\). Add the non-global condition
if “root” means a useful root. Without these additions, “equivalently” is too
strong.

## 4. Exact cyclic order boundary — theorem PASS, equivalence scope FAIL

For \(r=\operatorname{ord}_N(a)\), the candidate correctly solves

\[
r\mid2e,
\qquad r\nmid e.
\]

Solutions exist exactly when \(r\) is even, and they are exactly

\[
e=\frac r2(2j+1).
\]

The least solution is \(r/2\), and every solution gives the same involution.
The useful/non-global dichotomy is also correct. The modulo-21 comparison of
the order-6 base \(2\) and order-2 base \(8\) correctly shows why an arbitrary
successful exponent does not determine the order.

Two qualifications are required.

First, doubling the least answer recovers \(r\) only on the even-order
promise. For odd \(r\), the requested exponent does not exist. A total oracle
that returns `NONE` can be made equivalent to general order finding only
after an explicit reduction. For example, after `NONE` on \(a\), \(r\) is
odd and \(-a\) has order \(2r\); its least nonidentity involutory exponent is
\(r\). This reduction is an abstract modular-residue operation. It need not
respect an F62 legal-divisor box.

Second, a **least factoring-useful** exponent is weaker still. It is absent
when \(r\) is odd and also when the half-order involution is the global
\(-1\). Such an oracle alone is not exact order finding.

**Required correction.** Replace the summary bullet “least-power selection
for one block is exactly order finding” by one of these precise statements:

- on the even-order promise, the least nonidentity involutory exponent is
  \(r/2\); or
- a total least-nonidentity-involutory-power oracle, with `NONE` and the
  explicit \(-a\) reduction, is Turing-equivalent to modular order finding.

Do not substitute “least useful power” for “least nonidentity involutory
power.”

The one-generator lattice statement

\[
\Lambda_N=r\mathbb Z
\]

is exact. Therefore full relation-lattice recovery genuinely contains exact
order finding.

## 5. The \(N=65\) witness — arithmetic PASS, claimed comparator FAIL

All stated witness arithmetic is correct:

\[
66=2\cdot3\cdot11,
\qquad
651=3\cdot7\cdot31,
\]

the two parity rows are independent, and

\[
g=2\cdot7=14,
\qquad
14^2=1+3\cdot65.
\]

The two selected factors also each have order \(12\), with half-order residue
\(-1\):

\[
2^6\equiv7^6\equiv-1\pmod {65}.
\]

Thus the example strictly separates cross mixing from order halving applied
**only to the two selected constituent blocks \(2\) and \(7\)**. It also
strictly separates the cross root from the old two-row parity decoder.

It does not show that all separate one-block tests on the complete block list
miss. The same list contains \(3\), and

\[
\operatorname{ord}_{65}(3)=12,
\qquad
3^6\equiv14\pmod {65}.
\]

This is already the same useful non-global involution. Blocks \(11\) and
\(31\) also have useful half-order residues. Therefore the unqualified final
claim that the witness beats “separate one-block order-halving tests” is
false if those tests range over the complete public list.

The sentence about “one manufactured block” is also backwards. Every chosen
cross product is itself one manufactured group element. Here that element is
\(14\), of order \(2\), so order halving on that manufactured element is
trivial. The new operation is the public selection of \(14\) from two
original block directions. It is not a new postprocessing rule after \(14\)
has been selected.

**Required correction.** State the comparator as “the two selected original
blocks tested separately.” Remove the claim about every one-block test on the
complete list. Describe the novelty as multi-block candidate construction,
not as a separation from order halving on the resulting candidate.

The pair-enumeration cost statement passes under the candidate's explicit
polynomial-size block-list premise. Seed endpoint blocks are smaller than
\(N\), so their total encoding is polynomial under this premise.

## 6. The multiplicity family — square-root hierarchy PASS, broad arity claim FAIL

Let odd \(t\ge3\), \(G=2^t\), and

\[
N=\frac{G^2-1}{3},
\qquad
B=\frac{N+1}{2}.
\]

The candidate correctly classifies the legal divisors below \(N\) from
\(c<t\) copies as \(B\) and \(2^a\) for \(1\le a\le c\). It correctly proves
that none is self-inverse. With \(t\) copies, \(G\) is legal, non-global, and
satisfies \(G^2=1+3N\). The old parity decoder has only global roots.

The exact order proof also passes. Since \(2^{2t}\equiv1\pmod N\), the order
divides \(2t\). Reduction modulo \(2^t-1\) gives exact order \(t\): no smaller
positive exponent can produce a multiple of \(2^t-1\). Hence the order modulo
\(N\) is a multiple of \(t\). Since \(2^t\not\equiv1\pmod N\), it is exactly
\(2t\).

This proves an exact lower bound for the number of source occurrences needed
to reach a **self-inverse** divisor in this family. It does not prove the
unqualified direct-screening or “arity” claims.

First, “arity” here is the number of selected relation occurrences. For the
powers \(2^a\) in this family, it is also an exponent-budget bound. It is not
support size. The successful vector \(2^t\) has support one. A
constant-support residue selector with exponent cap
\(E\ge t=\Theta(\log N)\) finds it. Therefore this family does not rule out
constant-support sparse selection.

Second, for arbitrary odd \(t\), lower multiplicities can factor through an
ordinary direct gcd without being self-inverse. Take \(t=9\) and \(c=3\).
Then \(g=2^3=8\) is legal and

\[
g-1=7\mid 2^9-1\mid N.
\]

Thus

\[
1<\gcd(g-1,N)<N
\]

at multiplicity \(3<t\). The sentence that every fixed arity below \(t\)
misses is false for the full F62 direct screen.

**Required correction.** Rename the result an exact
“self-inverse total-multiplicity hierarchy.” Explicitly say that it does not
bound support. If a lower bound against all \(g\pm1\) screens is desired, use
a suitably restricted subfamily, such as odd prime \(t\ge5\), and supply the
additional order-on-each-factor proof. The current proof does not establish
that stronger result.

## 7. Smith normal form and HSP — core PASS with exact wording

Given a full-rank basis of \(\Lambda_N\), Smith normal form computes the
invariant factors of the finite quotient

\[
\mathbb Z^s/\Lambda_N
\cong
\langle q_1,\ldots,q_s\rangle.
\]

For an even invariant factor \(d_i\), the corresponding 2-torsion basis
element is \(d_i/2\) times an invariant-factor generator. It is not obtained
by literally “halving the generator.” This is the required wording repair.

There are at most \(s\) such independent elements. If the subgroup has a
non-global involution, at least one of these basis elements is non-global.
The reason given in the candidate is valid: the subgroup has at most one
nonidentity element equal to the global residue \(-1\), while distinct basis
elements of its elementary 2-subgroup are independent. Screening the at most
\(s\) elements therefore solves the unbounded subgroup 2-torsion target.

Negative coordinates in the transformed exponent representatives are valid
for this modular task. They use modular inverses. They do not automatically
give legal positive F62 divisors.

The bit-complexity statement must include the encoded sizes of \(N\), the
public generators, the supplied lattice basis, and the transformation data.
It proves no efficient way to recover that basis. The kernel formulation is
an abelian HSP in the mathematical coset-equality sense. This alone is not a
fully specified efficient quantum algorithm over the infinite domain
\(\mathbb Z^s\); a finite sampling/truncation and precision analysis would
still be needed. The candidate correctly refrains from claiming such a
solver.

## 8. The bounded-source HSP separation — FAIL for full F62, repair available

The candidate uses

\[
N=21,
\qquad
2\cdot11=22.
\]

Its one-copy box indeed contains no non-global self-inverse divisor, while the
generated subgroup contains \(2^3=8\). This separates the **bounded
self-inverse** target from the unbounded subgroup target.

It does not separate the full F62 factoring screen. The legal one-copy divisor
\(g=2\) already gives

\[
\gcd(2+1,21)=3.
\]

Hence the sentence “the HSP target has a solution while that F62 source
instance does not” is false without the self-inverse qualifier. The later
sentence “an F62 success gives one non-global involution” is false for the
same reason.

A strict replacement already exists in the proof-only F62 selector artifact.
Take

\[
N=187=11\cdot17,
\qquad
2\cdot94=188=2^2\cdot47.
\]

The one-copy block box has \(E=(2,1)\). Its proper legal divisors below \(N\)
are exactly

\[
2, 4, 47, 94.
\]

For all four, both gcd screens are trivial:

\[
\begin{array}{c|cc}
g & g-1 & g+1\\ \hline
2  & 1  & 3\\
4  & 3  & 5\\
47 & 46 & 48\\
94 & 93 & 95
\end{array}
\]

None of the numbers in the last two columns has a factor \(11\) or \(17\).
However, the subgroup generated by \(2\) has order

\[
\operatorname{lcm}
\bigl(\operatorname{ord}_{11}(2),
      \operatorname{ord}_{17}(2)\bigr)
=\operatorname{lcm}(10,8)=40.
\]

Its half-order power has opposite CRT signs:

\[
2^{20}\equiv1\pmod {11},
\qquad
2^{20}\equiv-1\pmod {17}.
\]

Thus the unbounded subgroup has a non-global involution, while the one-copy
box has neither a direct CRT separator nor a non-global involution. This gives
the claimed strict divisor-and-magnitude separation even under the full F62
screen.

**Required correction.** Either qualify the \(N=21\) example as a
self-inverse-only separation or replace it by \(N=187\).

## 9. Prime powers and the remaining theorem target — FAIL by omission

For an odd prime power \(p^k\), the only square roots of one are the two global
roots. Therefore no non-global 2-torsion selector can meet the final target on
that input class. This does not affect Theorem 1. It affects the all-input
scope of the disposition.

The phrase “for every required input class” is undefined. The sibling F62
result correctly handles even inputs and perfect powers first. This artifact
must preserve that scope. It must also distinguish primality testing from the
composite factoring target.

The final complexity statement counts only the number of vectors. A
polynomial-time claim also requires a seed transcript with
\(m,s\), total relation encoding, exponent capacities, and all candidate
exponent bit lengths bounded by \(\operatorname{poly}(\log N)\).

**Required correction.** State the target as one of the following:

- after polynomial-time handling of even inputs and perfect powers, find a
  direct CRT separator on every remaining odd composite input; or
- after the same preprocessing, find a bounded non-global involution if the
  research target is intentionally restricted to the square-root route.

The first target is the full F62 direct-screen problem. The second is the
lattice subproblem studied by this candidate. They are not equivalent.

## 10. Required disposition

The artifact can pass after these changes:

1. Restrict every exact 2-torsion claim to self-inverse square-root
   screening, or enlarge the target to all direct CRT separators.
2. Make occurrence capacities finite and consistent with the old decoder.
3. Preserve Theorem 2 as a residue-image theorem. Do not turn negative
   lattice representatives into legal integer divisors.
4. Add source-box and magnitude feasibility to the quotient-group novelty
   statement.
5. State the even-order promise for the least-exponent theorem. Do not equate
   a least *useful* exponent oracle with unrestricted exact order finding.
6. Restrict the \(N=65\) comparison to blocks \(2\) and \(7\). Do not claim
   that every blockwise order-halving test on the full list fails.
7. Rename the odd-\(t\) result as a self-inverse total-multiplicity hierarchy.
   It is not a support-arity lower bound or, for arbitrary odd \(t\), a lower
   bound against all direct gcd screens.
8. In the SNF paragraph, multiply an invariant generator by \(d_i/2\). Do not
   say that the generator itself is halved.
9. Qualify the \(N=21\) HSP example or replace it by the strict \(N=187\)
   witness above.
10. Restore even-input, prime, and perfect-power scope. Charge all transcript
    and exponent encodings in every polynomial-time statement.

After these corrections, the valid conclusion is narrower and useful. Full
relation-lattice recovery contains exact modular order finding. A supplied
full lattice solves the unbounded subgroup 2-torsion task by Smith normal
form. The old decoder already contains the modular image of the 2-saturation
of its known integer row lattice. F62's legal self-inverse search adds a box
and an integer-magnitude constraint. The broader F62 selector can also win on
non-self-inverse CRT separators, so it is not exactly the hidden-lattice
2-torsion problem described in the candidate.
