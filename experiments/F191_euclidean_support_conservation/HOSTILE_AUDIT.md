# F191 hostile audit

## Strict verdict

**FAIL.** The elementary support-conservation theorem, canonical
counterexample, and permutation-bank count are correct. However, the claimed
surviving P163 interface is not sufficient for P163 as described in the
statement. It omits the required nonzero and (<N/2) size conditions on the
quotients or carries. Thus the sentence that P163 can use those values
directly is false without an additional size theorem.

This defect does not invalidate Sections 1--3. It invalidates the final
handoff and the claim that Section 4 gives the exact surviving interface.

## Frozen-file integrity

All three manifest hashes match the frozen files exactly:

- `STATEMENT.md`:
  `6747d7c6b121565bb1cbabb0041f7f11cb1f2f3306eb27beb126f3e4714bb124`
- `PROOF.md`:
  `21dfd6a74efc318434f54f5c7575b10c9d299b8e315459d20fd9643410cef455`
- `SELF_AUDIT.md`:
  `1bd8c60477f4bb8ccba50923e129333c0b48c5bf23312a21ac7ea1457c7ab7a5`

Hashing was the only machine computation used.

## Blocking defect: the P163 handoff is underspecified

The opening scope says that P163 needs a public list of **positive integers
below (N/2)**. Section 4 instead asks only for a QP bank of “integer
quotients or carries” such that each surviving prime divides one of them. It
then says:

> Once that quotient/carry theorem is proved, P163 can use those values
> directly.

Divisibility alone does not imply admissibility for P163:

- a quotient or carry can be zero, which is divisible by every prime but is
  not a positive support auxiliary;
- it can be negative, in which case its absolute value must be used;
- it can have magnitude at least (N/2), in which case it is not a P163
  child.

The valid live interface must require public QP-computable integers (A_j)
such that

\[
0<|A_j|<N/2
\]

and every surviving local-order prime divides at least one (A_j). Then
P163 can use (|A_j|). Alternatively, a separate theorem must convert each
oversized quotient or carry into an admissible value while preserving the
target support. F191 itself shows why ordinary centering is not such a
theorem.

The concrete permutation-bank obstruction does prove the needed size and
nonzero bounds for its selected parameter. That fact does not supply those
bounds for the unrestricted quotient/carry interface in Section 4.

## Formula audit

### Exact conservation law

From (X=QD+R) and (ell\mid X), one gets
(R\equiv-QD\pmod\ell). If (ell\nmid D), multiplication by (D) is
invertible modulo (ell), so
(ell\mid R\Longleftrightarrow\ell\mid Q). This part is exact and needs no
size premise.

There is one minor formal domain hole. The statement initially allows every
(D\in\mathbb Z), but its nonunit branch says that (D) itself carries
prime support. This is not a usable support claim when (D=0). A division
modulus is presumably intended to be nonzero, but that premise should be
stated. This does not affect division by (N).

### Canonical counterexample

The balanced residue is nonzero because (ell\nmid N), and

\[
|c|\le (\ell-1)/2<\ell/2<N/4.
\]

Hence (N/2<N+c<3N/2), the unique centered quotient is (1), and the
remainder is (c). Both (1) and (|c|) lie below (N/2), and neither is
divisible by (ell). No defect was found.

### Endpoint count

For (b\in\{0,\ldots,N-1\}), nearest-integer division of
(ell b/N) gives (Q(b)\in\{0,\ldots,\ell\}). There is no half-integer tie
when (N) is odd, since (2\ell b=(2t+1)N) would equate an even integer
with an odd integer. Therefore (ell\mid Q(b)) occurs only at
(Q(b)=0) or (Q(b)=\ell), namely in

\[
0\le b<N/(2\ell)
\quad\text{or}\quad
N-N/(2\ell)<b<N.
\]

Each interval contains at most (N/(2\ell)+1) integers. Thus the stated
bound (N/\ell+2) is safe. Support conservation makes the (Q)-event and
the (R)-event identical. Pullback by a permutation preserves the count,
and the union bound requires no independence. With
(ell\ge4B) and (N\ge8B), the exceptional union is at most (N/2<N).
Outside it, (1\le Q_i\le\ell-1<N/2) and
(0<|R_i|<N/2). No endpoint, constant, or zero-remainder error was found.

## P161 applicability audit

The group-theoretic implication is correct under the stated P161 premise.
If (g) is the exact order of a cyclic subgroup modulo (p^e) and
(gcd(g,N)=1), then (p\nmid g). The reduction kernel is a (p)-group,
so it intersects that subgroup trivially. Consequently (g\mid p-1), and
every (ell\mid g) satisfies (ell\le p-1).

The size argument is also correct if “prime-power component” means the
maximal component of an odd composite (N). With a remaining cofactor, that
cofactor is at least (3), so (p\le N/3). If (N=p^e) with (e\ge2),
then (p\le\sqrt N<N/2). Hence (ell<N/2).

Two applicability conditions are not established inside the frozen record:

1. The text imports from P161 that an arbitrary numerical-QP roughness cap
   (T) may be chosen and that every surviving order prime exceeds (T).
   The algebra after that premise is correct, but this audit cannot verify
   the P161 contract from the four permitted files.
2. The choice (T>4B) is noncircular only when the bank bound (B) is fixed
   independently of that choice of (T), or when a uniform bound satisfying
   (T>4B(T,N)) is proved. If the proposed P164 bank size can depend on the
   P161 cap, the sentence “given (B), choose (T>4B)” does not by itself
   justify the composite application.

Subject to those two interface premises, the final inequalities are valid:
(ell>T>4B) and (ell<N/2) imply (N>2ell>8B).

## Scope conclusion

F191 successfully refutes automatic support transfer through Euclidean or
centered normalization, and it proves the stated obstruction for a
permutation bank. It does not yet state a valid direct handoff to P163. The
candidate must add the admissible-size and nonzero requirements to the live
quotient/carry interface before it can pass.
