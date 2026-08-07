# F70 fresh hostile re-audit — refinement-gain selector boundary

## Verdict: PASS

This verdict applies only to the candidate with SHA-256

`a520b299086f1ff613e70003aee6e573f7548305921f287006a95fdbc8cefaf1`.

I read the exact candidate and the failed first hostile audit in full. I then
rechecked the definitions, quantifiers, arithmetic certificates, finite-box
claim, and relation to P70--P77. All five defects from the first audit are
repaired. I found no remaining mathematical or scope error that blocks
promotion to proof-blind reconstruction.

The passing claim is narrow. F70 gives exact special-family and finite
witnesses. It does not give an all-input selector, a polynomial-time factoring
algorithm, a stopping bound, or a publication-level novelty claim.

## 1. Check of the five required repairs

### R1. Old-block splitting is separate from total block gain

Repaired.

The candidate now defines

\[
r'-r=\sigma+\nu,
\]

where \(\sigma\) counts extra descendants of old block types and \(\nu\)
counts private new block types.

In the immediate-square history, \(w=3025\) is coprime to the old blocks.
Thus \(\sigma=0\), but the new endpoint contributes private exact block data
and the total block gain is positive. The conclusion is now only that
positive **old-block splitting** is not necessary for useful feedback.

In the three-relation history, \(1985\) splits into \(5\) and \(397\), while
\(781\) is private. Thus \(\sigma=1\) and \(\nu=1\). The candidate no longer
uses "refinement gain" as if it meant only \(\sigma\).

### R2. No unsupported universal-selector or monotonicity claim

Repaired.

Section 8 now states only that \(\sigma>0\) is neither necessary nor
sufficient for immediate success **across the two displayed histories**. It
explicitly says that this is not a same-history or same-menu ordering
counterexample. It leaves open a selector that combines \(\sigma\) with block
identities, multiplicities, public screens, or later feedback.

The final classification is also narrow: raw old-block split count is not a
stand-alone certificate of an immediate factor or useful closure. Its value
as one feature remains open.

### R3. No literal infinite stream of private blocks for fixed \(N\)

Repaired.

The candidate now says that the transcript accounting bound does not give a
polynomial round bound. It does not say that a fixed input can add a new
private block forever.

### R4. The finite-box obstruction is exact and correctly scoped

Repaired.

The displayed separator has canonical residue

\[
x=630=2\cdot3^2\cdot5\cdot7.
\]

A legal candidate for this residue must be the unique integer \(630\) in the
range \(1,\ldots,N-1\). The available refined blocks are

\[
2,\ 2017,\ 5,\ 397,\ 3529,\ 781.
\]

The four blocks larger than \(630\), or their products, cannot occur in an
exact positive product equal to \(630\). Powers of the remaining blocks
\(2\) and \(5\) cannot supply the prime factors \(3\) and \(7\). Therefore
the current positive whole-block occurrence box cannot contain this
representative.

The identity \(5\cdot2^{13}=40960\equiv630\pmod {4033}\) uses modular
reduction and is outside the declared source operation. The candidate now
calls this an instance of P71's bounded-representative obstruction. It does
not claim an exact equivalence theorem or a complexity lower bound from one
fixed input.

### R5. No unsupported minimality claim

Repaired.

The heading is now "A separator-free instance." The candidate does not call
\(4033\) the first or least such instance.

## 2. Refinement accounting

The exact count is valid. Old pairwise-coprime blocks cannot merge under the
declared joint refinement. Each old block stays intact or becomes two or more
pairwise-coprime descendants. A block of the new endpoint that divides no old
block is private. These cases give

\[
r'=r+\sigma+\nu.
\]

For a fixed final transcript, the product of its \(R\) distinct nontrivial
blocks divides the product of all endpoint integers. Since every block is at
least two,

\[
R\leq \log_2\!\left(\prod_x x\right)
 \leq \sum_x\lceil\log_2(x+1)\rceil=L.
\]

Telescoping gives

\[
\sum_t(\sigma_t+\nu_t)=R-r_0\leq L-r_0.
\]

The candidate correctly fixes the final transcript before applying this
bound. In an adaptive run, each round also increases \(L\). Thus this is an
accounting identity, not a polynomial stopping argument.

## 3. Separator-free old subgroup at \(N=4033\)

The factorization and order certificates are exact:

\[
4033=37\cdot109=\Phi_{36}(2),
\]

\[
2^{18}=-1\pmod {37},\qquad 2^{12}=26\ne1\pmod {37},
\]

and

\[
2^{18}=-1\pmod {109},\qquad 2^{12}=63\ne1\pmod {109}.
\]

The order divides \(36\), but it divides neither \(18\) nor \(12\). Every
proper divisor of \(36\) divides at least one of those two numbers. Hence the
order of \(2\) is \(36\) at both prime factors.

Therefore \(+1\) occurs in both CRT components at exponents
\(0\bmod36\), and \(-1\) occurs in both at exponents \(18\bmod36\). No
element of \(H_0=\langle2\rangle\) is a direct sign separator. This is
strictly stronger than the relevant feature of P76's \(N=209\) witness,
where the old subgroup already had a separator.

## 4. Infinite immediate-square family

Let \(s>1\) be odd with \(s=1\pmod3\). Then

\[
N_s=(2s-1)\frac{2s+1}{3}.
\]

Both factors are odd and greater than one. A common divisor divides

\[
3\frac{2s+1}{3}-(2s-1)=2,
\]

so the factors are coprime.

Also

\[
N_s+1=2\frac{2s^2+1}{3}.
\]

The second factor is odd. Thus each old relation has a nonzero parity column,
and two identical indexed copies have only the duplicate dependency. Its
positive root is \(N_s+1\equiv1\pmod {N_s}\).

The two charged copies supply \(g=4\). Its canonical inverse is \(w=s^2\),
because

\[
4s^2=1+3N_s=(2s)^2,
\qquad 1<s^2<N_s.
\]

The root \(2s\) gives

\[
\gcd(2s-1,N_s)=2s-1,
\qquad
\gcd(2s+1,N_s)=\frac{2s+1}{3}.
\]

For \(s=55\pmod {1530}\), direct reduction gives

\[
N_s=1\pmod3,\qquad N_s=3\pmod5,\qquad N_s=4\pmod {17}.
\]

Thus the sign, inverse-pair, and discriminant tickets are trivial before the
integer-square test succeeds. The discriminant calculation is valid because

\[
g^2\bigl((g-w)^2+4\bigr)\equiv(g^2+1)^2=17^2\pmod {N_s},
\]

and both \(g\) and \(17\) are units. This is an infinite manufactured family,
not an all-input law.

## 5. Immediate closure at \(N=4033\)

For \(s=55\),

\[
N=4033,
\qquad
N+1=4034=2\cdot2017.
\]

The old blocks generate \(H_0\). Two identical columns decode only the global
root. The feedback data are

\[
g=4,
\qquad
w=3025=55^2,
\qquad
gw=12100=1+3N=110^2.
\]

The old blocks do not split because \(3025\) is coprime to both \(2\) and
\(2017\). The root is non-global:

\[
110=-1\pmod {37},
\qquad
110=1\pmod {109}.
\]

Consequently

\[
\gcd(110-1,4033)=109,
\qquad
\gcd(110+1,4033)=37.
\]

This proves useful closure with \(\sigma=0\). Perfect-square blocks can be
omitted from parity rows under P66/P73, but their exact exponent data remain
available for the root. Thus the candidate's block and closure claims are
compatible.

The phrase "perfect-square endpoint passes the closure gate" is read as
shorthand for the appended relation \(gw\) having a zero square-class column.
The displayed equations make the tested object unambiguous.

## 6. Three-relation refinement witness

The three old equations are exact:

\[
2\cdot2017=1+N,
\]

\[
64\cdot3970=1+63N,
\]

\[
8\cdot3529=1+7N.
\]

Since \(3970=2\cdot1985\), complete refinement gives

\[
Q_0=\{2,2017,1985,3529\}.
\]

The blocks are pairwise coprime, and the old relations imply

\[
2017=2^{-1},
\qquad
1985=2^{-7},
\qquad
3529=2^{-3}\pmod N.
\]

Hence \(H(Q_0)=H_0\), which has no direct separator.

The available exponent of \(2\) is \(1+7+3=11\). The legal choice
\(g=2^{11}=2048<N\) has canonical inverse \(w=3905\), with

\[
2048\cdot3905=7{,}997{,}440=1+1983N.
\]

The sign gcds are trivial. For \(d=1857\),

\[
d=7\pmod {37},\qquad d=4\pmod {109},
\]

so \(d^2+4\) is a unit at both factors. The product is nonsquare because its
exact \(2\)-adic valuation is \(11\).

The only nontrivial old/new overlap is

\[
\gcd(1985,3905)=5.
\]

It gives

\[
1985=5\cdot397,
\qquad
3905=5\cdot781,
\]

and

\[
Q_1=\{2,2017,5,397,3529,781\}.
\]

The block \(781\) is nonsquare, private, and odd in the appended relation.
Its parity row is zero on all old columns and one on the new column. Therefore
the new column cannot close. The step gives neither an immediate factor nor a
new decoder dependency.

## 7. Strict subgroup enlargement

Both feedback endpoint residues are in \(H_0\):

\[
g=2^{11},
\qquad
w=2^{-11}=2^{25}\pmod N.
\]

Nevertheless, integer refinement exposes \(5\). Modulo \(37\),

\[
5=2^{23},
\]

while modulo \(109\),

\[
2^{23}=77\ne5.
\]

The order is \(36\) at both factors, so no other exponent can repair this
mismatch. Hence \(5\notin H_0\).

The refined set contains both \(2\) and \(5\), while every other refined
block lies in \(\langle H_0,5\rangle\). Therefore

\[
H(Q_1)=\langle H_0,5\rangle=:H_1,
\qquad
H_0\subsetneq H_1.
\]

The enlarged subgroup contains

\[
x=5\cdot2^{-23}=5\cdot2^{13}=630\pmod {4033}.
\]

Its CRT values are \(1\pmod {37}\) and \(85\pmod {109}\), so

\[
\gcd(x-1,4033)=\gcd(629,4033)=37.
\]

This proves the exact new point: endpoint gcd refinement can expose a
generator outside a separator-free old subgroup and can enlarge it to a
factor-bearing subgroup, even though the two endpoint residues themselves
were in the old subgroup.

## 8. Prior-result and novelty boundary

The candidate does not inflate its relation to the durable results.

- P70 already proves that cross-relation feedback can manufacture useful
  special relations. F70's infinite family is another exact special family,
  not a sampler theorem.
- P71 already identifies the finite occurrence-box problem. F70 supplies a
  concrete strict-enlargement instance and does not solve that problem.
- P73 and P74 already give the closure and root-coset gates. F70 supplies a
  stronger witness for the mechanism, not a new complete decoder.
- P76 already proves endpoint-refinement subgroup expansion. F70 strengthens
  the witness by starting from a subgroup with no direct separator and ending
  in a subgroup that has one.
- P77 closes raw balance only. F70 does not claim to close refinement scoring
  as a selector feature.

No dedicated literature audit has run. Therefore this re-audit confirms the
internal theorem and its scope only. It does not certify publication-level
novelty.

## Final classification

**PASS for the exact pinned hash.** The repaired candidate proves a genuine
representation-level feedback effect and states its finite-box obstruction
correctly. Its missing step remains unchanged: a uniform public rule must
find, on every input family and with inverse-polynomial probability, an
immediate separator, a non-global closure, or a reachable factor-bearing
representative after strict enlargement.
