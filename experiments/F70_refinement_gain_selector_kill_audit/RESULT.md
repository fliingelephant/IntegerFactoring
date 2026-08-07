# F70 hostile audit — refinement-gain selector boundary

## Verdict: FAIL as written

The audited candidate has SHA-256

cc62a2afa22352785ff3b3a0abcb8402687910c2c90a31afed6ab55f73a23f9c.

The two main \(N=4033\) mechanisms are mathematically correct:

1. canonical feedback creates a useful square root although the complete old
   block subgroup has no direct separator; and
2. endpoint gcd refinement strictly enlarges that separator-free subgroup to
   a subgroup that contains a direct separator.

The infinite family, the order-\(36\) certificates, the refinement, all named
screens, the subgroup separation, and the element \(x=630\) also check.

The candidate fails this audit because its final selector conclusion is
stronger than its evidence. It also uses “refinement gain” inconsistently.
These are scope errors, not failures of the two exact witnesses.

## Required corrections

### R1. Distinguish \(\sigma\) from total refinement gain

Section 5 proves \(\sigma=0\). It does not prove zero total refinement gain.
The new endpoint \(w=3025\) is coprime to the old blocks \(2,2017\), so it
introduces a private new gcd-free block. Under the candidate's own equation

\[
r'-r=\sigma+\nu,
\]

one has \(\nu>0\) and therefore \(r'-r>0\).

The sentence “positive refinement gain is not necessary” must say “positive
old-block splitting, \(\sigma>0\), is not necessary.” All later uses of
“refinement count” must state whether they mean \(\sigma\), \(\nu\), or
\(\sigma+\nu\).

### R2. Do not close refinement count as a universal selector

The two histories prove only these two statements:

- \(\sigma>0\) is not necessary for immediate success; and
- \(\sigma>0\) is not sufficient for immediate success.

They do not compare two candidates in one fixed menu and one fixed history.
They do not refute a rule that first runs all public screens and then uses
\(\sigma\) as one ranking feature. They also do not refute a rule that combines
\(\sigma\) with block identities, multiplicities, or later feedback.

The candidate correctly admits this at the end of Section 8. Therefore the
last sentence cannot “close raw refinement count as a universal selector or
progress metric.” Replace it with the narrower conclusion:

> Raw old-block split count is not a stand-alone certificate of immediate
> factoring success or useful square-class closure. Its value as one feature
> in a uniform selector remains open.

For the same reason, “not monotone with immediate factoring success” must be
replaced by “neither necessary nor sufficient for immediate success across
the two displayed histories.” No same-history monotonicity theorem is proved.

### R3. Correct the fixed-\(N\) “forever” statement

For fixed \(N\), all canonical endpoints lie in a finite set. A process cannot
introduce a new private block type literally forever. Equation (4) only fails
to give a polynomial bound because its right side grows with the transcript;
it is compatible with a superpolynomial or exponential number of rounds.

Replace “one private block per round forever” with “one private block per
round for a number of rounds not bounded polynomially by (4).”

### R4. State the finite-box limitation precisely

The current box does not merely lack a proved representative of the displayed
\(x\). It cannot contain that representative under the declared positive
whole-block rule. A residue in \(1,\ldots,N-1\) has a unique representative
in that interval, so a legal representative of \(x\) would have to equal

\[
630=2\cdot3^2\cdot5\cdot7.
\]

None of \(2017,397,3529,781\) is divisible by \(3\) or \(7\), and the other
blocks are \(2,5\). Thus no positive product of the available whole blocks can
equal \(630\). The larger representation \(5\cdot2^{13}=40960\) becomes \(630\)
only after modular reduction, which is outside the candidate's \(1<g<N\)
source operation.

Also replace “exactly the bounded hidden-lattice difficulty from P71” with
“an instance of the bounded-representative obstruction highlighted by P71.”
P71 does not prove an exact equivalence for this factor-bearing target. Since
\(N=4033\) is one fixed input, phrase the complexity limitation uniformly:
the witness supplies no uniform polynomial-time rule that finds such an
element on an input family.

### R5. Remove unsupported minimality wording

The heading “The first separator-free instance” has no minimality proof.
Use “A separator-free instance,” unless “first” is explicitly defined only as
the \(k=0\) member of the displayed congruence progression.

## 1. Exact refinement accounting

After complete gcd refinement, every new block is either a descendant of one
old block or is coprime to all old blocks. Existing blocks do not merge.
Therefore

\[
r'=r+\sigma+\nu
\]

is exact with the candidate's definitions.

For a fixed final transcript, let its distinct blocks be
\(q_1,\ldots,q_R\). They are pairwise coprime and at least \(2\), and

\[
\prod_{j=1}^R q_j
\mid
\prod_x x.
\]

Hence

\[
R\le \sum_x\log_2x\le
\sum_x\lceil\log_2(x+1)\rceil=L.
\]

The telescoping identities (3) and (4) follow. Their quantifiers are valid
only for a fixed finite final transcript. Since an adaptive run adds
\(O(\log N)\) bits per round, this is an accounting identity, not a stopping
bound.

## 2. The separator-free subgroup at \(N=4033\)

The factorization and cyclotomic identity are exact:

\[
4033=37\cdot109=2^{12}-2^6+1=\Phi_{36}(2).
\]

Modulo \(37\),

\[
2^{12}=26,
\qquad
2^{18}=26\cdot27=-1.
\]

Modulo \(109\),

\[
2^{12}=63,
\qquad
2^{18}=63\cdot64=-1.
\]

Thus the order divides \(36\), does not divide \(18\), and does not divide
\(12\). The only divisor of \(36\) with both properties is \(36\). Therefore

\[
\operatorname{ord}_{37}(2)=\operatorname{ord}_{109}(2)=36.
\]

For \(2^e\), the local value \(+1\) occurs at both factors exactly when
\(e=0\pmod {36}\). The local value \(-1\) occurs at both factors exactly when
\(e=18\pmod {36}\). No element of \(H_0=\langle2\rangle\) can have a selected
sign at only one factor. Equation (5) is correct.

This is a strict improvement over the scope of P76's \(N=209\) witness,
whose old subgroup already contained \(3^5=34\), a direct separator.

## 3. Infinite immediate-closure family

Let \(s>1\) be odd and \(s=1\pmod3\). Then

\[
N_s=(2s-1)\frac{2s+1}{3}.
\]

Both factors are odd and greater than one. If \(d\) divides both, then it
divides

\[
3\frac{2s+1}{3}-(2s-1)=2.
\]

Thus \(d=1\). The displayed factors are proper and coprime.

Also

\[
N_s+1=2\frac{2s^2+1}{3}.
\]

The second factor is odd, so \(v_2(N_s+1)=1\). Therefore this relation value
is not a square. Two identical nonzero parity columns have exactly the one
duplicate dependency, whose positive root is \(N_s+1=1\pmod {N_s}\).

Two charged copies supply two occurrences of the block \(2\), so \(g=4\) is
legal. Moreover,

\[
4s^2=1+3N_s,
\qquad
1<s^2<N_s.
\]

Thus \(w=s^2\) is the canonical inverse of \(4\), and the new relation has
the exact root \(2s\). Since

\[
\gcd(2s-1,N_s)=2s-1,
\qquad
\gcd(2s+1,N_s)=\frac{2s+1}{3},
\]

the root gives a proper coprime split of every member of the family.

For \(s=55\pmod {1530}\), one has

\[
s=1\pmod9,\qquad s=0\pmod5,\qquad s=4\pmod {17}.
\]

Direct reduction gives

\[
N_s=1\pmod3,\qquad N_s=3\pmod5,\qquad N_s=4\pmod {17}.
\]

Hence \(N_s\) is coprime to \(3\cdot5\cdot17\). The sign screens for \(g=4\)
and the equivalent \(g-w\) screen are trivial. For the discriminant,

\[
g^2((g-w)^2+4)
\equiv(g^2+1)^2
=17^2\pmod {N_s}.
\]

Both \(g\) and \(17\) are units, so this gcd is also one. The infinite
subfamily claim is correct. It is a manufactured special family, not an
all-input sampling law.

## 4. Immediate \(N=4033\) closure

For \(s=55\), \(N_s=4033\), and

\[
N+1=4034=2\cdot2017.
\]

The old blocks generate \(H_0\). The two identical columns decode only the
global root \(4034=1\pmod N\).

The exact feedback data are

\[
g=4,\qquad w=3025=55^2,\qquad
gw=12100=1+3N=110^2.
\]

The old blocks do not split because

\[
\gcd(3025,2)=\gcd(3025,2017)=1.
\]

The direct and discriminant screens for \(g\) fail, while

\[
110=-1\pmod {37},\qquad110=1\pmod {109},
\]

so

\[
\gcd(109,4033)=109,\qquad
\gcd(111,4033)=37.
\]

This proves the claimed non-global closure with \(\sigma=0\). It does not
prove zero total block gain; \(w\) supplies a private new block.

## 5. Three-relation refinement witness

All three source equations are exact:

\[
2\cdot2017=1+N,
\]

\[
64\cdot3970=254080=1+63N,
\]

\[
8\cdot3529=28232=1+7N.
\]

Since \(3970=2\cdot1985\), complete refinement gives

\[
Q_0=\{2,2017,1985,3529\}.
\]

The odd blocks are pairwise coprime. The source equations imply

\[
2017=2^{-1},\qquad1985=2^{-7},\qquad3529=2^{-3}\pmod N.
\]

Thus \(H(Q_0)=H_0\), and the old subgroup contains no direct separator.

The total available exponent of \(2\) is \(1+7+3=11\), so

\[
g=2^{11}=2048<N
\]

is legal. Its canonical inverse is \(w=3905\), because

\[
2048\cdot3905=7{,}997{,}440=1+1983\cdot4033.
\]

The sign screens are trivial at both prime factors. For the discriminant,
\(d=1857\) has

\[
d=7\pmod {37},\qquad d=4\pmod {109},
\]

and therefore

\[
d^2+4=16\pmod {37},\qquad d^2+4=20\pmod {109}.
\]

The discriminant gcd is one. The product is nonsquare because its exact
\(2\)-adic valuation is \(11\).

The only proper overlap with an old block is

\[
\gcd(1985,3905)=5.
\]

It gives

\[
1985=5\cdot397,\qquad3905=5\cdot781
\]

and therefore

\[
Q_1=\{2,2017,5,397,3529,781\}.
\]

Exactly one old block splits, and \(781\) is one private new block. Hence
\(\sigma=1,\nu=1\). The private block \(781\) is nonsquare, has odd exponent
in the appended column, and is absent from all old columns. P73 therefore
rules out square-class closure. The candidate's immediate-failure claim is
correct.

## 6. Strict subgroup enlargement and separator

The old congruence \(1985=2^{-7}\) and the split \(1985=5\cdot397\) put
\(397\) in \(\langle H_0,5\rangle\). Similarly,
\(3905=2^{-11}=5\cdot781\) puts \(781\) there. Thus

\[
H(Q_1)=\langle H_0,5\rangle=H_1.
\]

Modulo \(37\),

\[
2^{23}=2^{18}2^5=(-1)32=5.
\]

Modulo \(109\), the same power is \(77\), not \(5\). Since \(2\) has order
\(36\) at each factor, any exponent that gives \(5\) modulo \(37\) is
\(23\pmod {36}\). It cannot give \(5\) modulo \(109\). Therefore

\[
5\notin H_0,\qquad H_0\subsetneq H_1.
\]

Finally,

\[
x=5\cdot2^{-23}=5\cdot2^{13}=630\pmod {4033}.
\]

The CRT values are

\[
x=1\pmod {37},\qquad x=85\pmod {109},
\]

so

\[
\gcd(x-1,4033)=\gcd(629,4033)=37.
\]

This is a valid strict subgroup-level gain. Both feedback endpoint residues
were already in \(H_0\), but integer refinement exposed a generator outside
\(H_0\).

## 7. Exact relation to P70–P77

The candidate's valid new point is narrower than its title suggests.

- P70 already proves that cross-relation or repeated-occurrence feedback can
  create useful relations and special infinite families. The new infinite
  family is another manufactured-square family; it is not a sampler.
- P71 already states the finite occurrence-box obstruction. F70 supplies a
  sharper concrete instance but no new method to solve it.
- P73 and P74 already give the closure and root-label gates. The \(g=4\)
  witness is a strong new instance of those gates, not a new decoder theorem.
- P76 already proves strict subgroup enlargement from endpoint refinement.
  F70 strengthens its witness: here the old subgroup has no direct separator,
  while the enlarged subgroup contains one.
- P77 already closes raw balance, not endpoint-refinement scoring. F70 does
  not close refinement count as a ranking feature.

After R1–R5, the surviving result is nontrivial and exact: canonical integer
feedback can manufacture factor-bearing structure outside a separator-free
old subgroup. The missing uniform candidate rule remains completely open.
No publication-level novelty conclusion follows without a dedicated
literature review.
