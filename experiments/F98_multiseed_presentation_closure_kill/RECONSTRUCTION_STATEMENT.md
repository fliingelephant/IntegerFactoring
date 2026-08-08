# F98 proof-blind reconstruction statement

Reconstruct and verify the following finite claim without reading any other
file in this experiment directory.

## Public one-round rule

The only arithmetic input is

\[
N=202{,}537{,}109.
\]

Put \(n=\operatorname{bitlength}(N)\) and \(B=n^2\).

1. Test \(\gcd(t,N)\) for every \(2\le t\le B\).
2. For every seed \(s=2,\ldots,n\), retain the first occurrence of the
   canonical-inverse presentation
   \((s,w_s)\), where \(1\le w_s<N\) and \(s w_s\equiv1\pmod N\).
   Test both endpoint sign gcds before retention.
3. Refine all seed endpoints into a pairwise-coprime,
   perfect-power-free integer basis. Use only exact integer roots and gcds.
   Keep the full exponent of every endpoint on that basis.
4. For each seed relation whose basis exponent column is nonzero modulo two,
   in seed order, take the two smallest supported basis blocks \(u\le v\).
   If the support has one block, put \(v=1\). Keep at most the first \(n\)
   such pairs.
5. For each retained pair, in that order, and each \(0\le e\le B\), process
   first \([u^e v]_N\) and then \([u v^e]_N\), where brackets mean the least
   nonnegative residue. Skip a residue only if it was processed before.
   For a new residue \(c\), compute its least positive inverse \(w\), test
   \(\gcd(c-w,N)\) and \(\gcd(c+w,N)\), and retain the exact relation
   \(P=cw\) if neither gcd is proper.
6. Remove \(P=1\) and all but the first occurrence of each repeated exact
   value \(P\) from the binary decoder. Jointly refine all remaining
   endpoints by exact gcd operations while tracking each relation's exponent
   parity. A final pairwise-coprime block which is an integer square adds no
   row; every other final block adds its incidence row modulo two.
7. Compute a full basis of the binary column kernel. For every basis vector,
   take the exact positive square root \(R\) of the selected relation-value
   product and test \(\gcd(R-1,N)\) and \(\gcd(R+1,N)\).

The implementation must not use integer factorization, primality testing,
orders, discrete logarithms, a target residue, a target relation class, or a
preselected kernel vector. It can use these only in a separate audit after
the public replay is frozen.

## Claim to reconstruct

The public rule has \(n=28\), \(B=784\), and the trial screen is null. It
retains 27 seed relations and 12,522 new first-occurrence trajectory
relations. Both direct sign gcds are nonproper for every one of the resulting
12,549 residues.

After removing one value \(P=1\) and 3,134 repeated exact values, the decoder
has 9,414 distinct nonzero relation values. Its factor-free parity matrix has
11,015 nonsquare rows, rank 8,926, and kernel dimension 488. One public kernel
basis vector uses 166 distinct relation values. Its exact positive root obeys

\[
R\equiv132{,}013{,}085\pmod N,
\]

\[
\gcd(R-1,N)=19{,}727,
\qquad
\gcd(R+1,N)=10{,}267.
\]

Thus this fixed execution factors \(N\) only after a joint retained-relation
decode; no individual canonical-inverse sign screen factors it.

As a separate diagnostic, regenerate the first 5,616 retained relations in
the same public order. Prove that no useful square-class dependency has
support one, two, or three. Independent online binary elimination first finds
a useful dependency at ordinal 5,616; that dependency has 166 distinct exact
relation values and gives root residue 70,524,024 with the two proper gcds
10,267 and 19,727. This does not claim that support 166 is globally minimal;
a useful dependency of support 4 through 165 may exist.

## Required scope

Reconstruct the factor-free correctness argument and a bit-complexity proof
for the declared bounded rule. The rule has polynomial bit complexity in
\(n\). The claim is one finite mechanism witness. It gives no all-input
success law, no inverse-polynomial density theorem, no abstract-subgroup
expansion theorem, no publication novelty claim, and no polynomial-time
factoring algorithm for arbitrary inputs.
