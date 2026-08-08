# Proof-blind reconstruction task: fixed cross-layer certificate

## Isolation rule

Read only this statement and RECONSTRUCT_INPUT.json. Do not read any other
F111 file. Do not read F98, F109, F110, their outputs, or their source code.
Do not use a factorization or primality routine. Reconstruct the result from
the public arithmetic specification below.

Write new files whose names start with RECONSTRUCT_BLIND_. Preserve every
failed attempt. Use a named hard timeout. Report every source file, command,
log, output, elapsed time, and SHA-256 pin.

## Public input

RECONSTRUCT_INPUT.json supplies:

- an odd integer \(N\);
- \(n=N.\mathrm{bit\_length}()\);
- \(B=n^2\);
- a retained-record stop count;
- one strictly increasing list of zero-based retained-record indices.

The index list is external advice. The task is to verify its fixed-instance
effect. It is not to discover the list.

## Ordered source

Maintain an ordered record list, an endpoint list, and a set of seen
canonical residues. To attempt a residue \(c\):

1. Count the attempt.
2. If \(c\) was seen, count one duplicate and do nothing else.
3. Otherwise, mark \(c\) as seen.
4. Compute the canonical inverse \(w\), with \(1\le w<N\) and
   \(cw\equiv1\pmod N\).
5. Record \(P=cw\), the pair \((c,w)\), and the supplied provenance.
6. Test both \(\gcd(c-w,N)\) and \(\gcd(c+w,N)\).
7. Append \(c,w\) to the endpoint list.

First attempt the seeds \(c=2,3,\ldots,n\), in that order.

### Deterministic gcd basis

Give endpoint \(i\) the signature \(\{i:1\}\). Put every endpoint greater
than one into a work stack in endpoint order. The last item is popped first.
Maintain an ordered basis list.

For each popped pair \((x,s)\):

1. If \(x=1\), discard it.
2. If \(x=a^e\) for some \(e>1\), choose the largest such \(e\), replace
   \(x\) by \(a\), and multiply every signature multiplicity by \(e\).
3. Scan the current basis from its first item. For the first
   \((y,t)\) with \(d=\gcd(x,y)>1\), remove \((y,t)\).
4. If \(x=y\), merge the two signatures and push \((x,s+t)\).
5. Otherwise push, in this order,
   \[
   (d,s),\quad(x/d,s),\quad(d,t),\quad(y/d,t).
   \]
6. If no basis item overlaps \(x\), append \((x,s)\) to the basis.

Continue until the stack is empty. Sort the final basis by its integer block
value. Check that the blocks are pairwise coprime, are not perfect powers,
and reconstruct all endpoints exactly from their signatures.

For each seed relation, add the signatures of its two endpoints to get one
integer exponent column on the final basis. Sort the block values in the
nonzero support. If the support has one value \(u\), select \((u,1)\).
Otherwise select its two smallest values \((u,v)\). Keep the seed-relation
order. This gives the ordered frozen-pair list.

### Frozen and appended trajectories

For each frozen pair \((u,v)\), in order, and each
\(e=0,1,\ldots,B\), attempt these two residues in this order:

\[
[u^e v]_N,\qquad [u v^e]_N,
\]

where brackets mean the canonical residue in \(0,\ldots,N-1\).
Use provenance frozen_seed_basis_pair, the zero-based pair index, \(u,v,e\),
and the orientation.

After all frozen pairs, process the appended pairs \((2,3)\), then \((2,4)\),
with the same exponent and orientation order. Use provenance
nonadaptive_seed_pair and a zero-based appended-pair index. Stop immediately
when the retained-record count equals the public stop count.

## Reconstruction claims

Independently determine and verify all of the following:

1. Every trial gcd \(\gcd(t,N)\), for \(2\le t\le B\), is one.
2. The basis block list, basis operation counts, frozen-pair list, frozen
   record count, total attempt count, duplicate count, and exact stop.
3. Every direct sign screen on every retained record. State whether any is a
   proper factor. Explain every nonunit but improper screen.
4. The public index list is in range, distinct, increasing, and ends at the
   final retained record.
5. The provenance split of the selected records. State whether both frozen
   and appended layers occur and identify every selected appended pair.
6. The exact selected product is a square. Compute its positive integer root
   without factoring the selected relation values.
7. Compute the root modulo \(N\), check that its square is one, test whether
   it is globally \(\pm1\), and compute both terminal gcds.
8. State the exact factor-free boundary. Gcd splitting and exact perfect-power
   extraction are allowed. General integer factorization, endpoint prime
   factorization, primality tests, and known factors of \(N\) are not.
9. State the advice boundary: the fixed indices verify existence only. They
   do not give a selector, probability law, or all-input factoring algorithm.

Use canonical byte encodings or another explicit bounded representation when
hashing very large integers. Do not rely on decimal conversion limits.
