# F254 self-audit

## Identity checks

1. The tailored pair ((S,T)) satisfies the norm-one Pell equation by
   direct expansion. No modular inference is used for this identity.
2. (D=T^2-2) is strictly between consecutive squares, so the construction
   uses a valid positive nonsquare discriminant.
3. The component factorization follows from a difference of squares and
   the exact negative-Pell equation.
4. One component is only twice a square modulo (N). A known modular root
   is asserted only for an even number of components. The original row has
   the supplied root (2uv=y^2-1).
5. The resultant statement uses the displayed sign convention. Its prime-
   support consequence is independent of the sign convention.

## Completeness checks

1. The descent covers all positive solutions, not only the displayed
   recurrence orbit. The inequalities are valid for every nontrivial
   solution because the next possible odd (y) after one is at least five.
2. The consecutive coordinates are (1,5,29,169). Therefore no omitted
   solution lies in (1<y<143).
3. The excluded (y=1) is outside the proposed source definition. The
   proof does not silently remove any admitted row.

## Arithmetic checks

1. (143=11\cdot13).
2. (733) is prime; (747=3^2\cdot83);
   (4947=3\cdot17\cdot97); and (5029=47\cdot107).
3. Private parity pivots (733,83,17,47) prove full rank without relying
   on a heuristic independence claim.
4. The shared prime (3) has even valuation in (747), so it does not
   remove the private pivot in the second column.
5. All six pairwise resultants and all declared direct-screen quantities
   have gcd one with (143).
6. The supplied-root residues square to the exact row residues.

## Quantifier and scope checks

The certificate disproves only the assertion that this complete tailored
negative-Pell bank must create progress for every odd composite input. A
single counterexample cannot bound success under another randomized choice
of discriminant or source. It also cannot rule out larger mixed banks or the
general retrospective P66 mechanism.

## Evidence and next gate

- Numerical computation: none.
- External sources: none.
- Durable ledgers edited: none.
- Current label: self-audited candidate.
- Required before promotion: a fresh hostile audit and then a strict
  statement-only reconstruction.
