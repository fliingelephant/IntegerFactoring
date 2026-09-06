# Hostile re-audit of F177 V2

## Verdict

**PASS.**

The V1 orientation defect is exactly repaired.  V2 enumerates both public
sign classes, one of which is the hidden correct orientation, and uses the
sum of their candidate-count bounds.  The ordinary square-modulus branch,
the repaired torus branch, both threshold constants, factor recovery, and
the deterministic quasipolynomial bit-cost claim are correct under the
stated balanced distinct-odd-semiprime promise.

The frozen V2 inputs have the requested SHA-256 hashes:

- `V2_STATEMENT.md`:
  `021925cf9eb6bd86df8851ab497a675025754b8061ed5d9816d851b9be938bf5`;
- `V2_PROOF.md`:
  `1c459deec3ec93924566e9bfa9e3f41a182fd8d1249ccc3f047924a21a409c25`.

I read both V2 files and the preserved V1 `HOSTILE_AUDIT.md` in full.  I did
not modify either frozen input or any durable ledger.

## 1. The V1 defect is repaired

For a Jacobi-minus-one torus state, the public data does not reveal

\[
\epsilon=(D_0/p)=-(D_0/q).
\]

V1 nevertheless scanned only the residue class indexed by that hidden sign.
V2 instead scans both public values

\[
\delta\in\{+1,-1\},
\qquad
D\equiv\delta(N-1)\pmod{B^2}.
\]

The true class is the branch with \(\delta=\epsilon\).  Thus no orientation
oracle is used.  The concrete V1 witness
\(N=1147=31\cdot37\), \(B=4\), and hidden \(\epsilon=-1\) is now handled:
the repaired scan includes the true gap \(D=6\), while its total three
candidates are below the new two-branch bound.

## 2. Ordinary square-modulus branch

Exact common order \(M\) implies

\[
M\mid p-1,
\qquad
M\mid q-1.
\]

Consequently,

\[
N+1-(p+q)=(p-1)(q-1)\equiv0\pmod{M^2}.
\]

No coprimality or generator assumption is missing.  Exactness is stronger
than needed for this divisibility argument.

With \(x=q/p\in(1,2)\),

\[
\frac{p+q}{\sqrt N}=\frac{1+x}{\sqrt x}
\]

is strictly increasing.  Its endpoint values are \(2\) and
\(3/\sqrt2\).  The search interval therefore has exact width

\[
c_0\sqrt N,
\qquad
c_0=\frac3{\sqrt2}-2.
\]

One residue class modulo \(M^2\) contributes at most

\[
1+\frac{c_0\sqrt N}{M^2}
\]

integers.  Under

\[
M^2\ge \frac{c_0\sqrt N}{Q(n)},
\]

this is at most \(Q(n)+1\).  Thus the constant and the
\(N^{1/4}/\sqrt{Q(n)}\) scale are correct.

For the true sum, \(S^2-4N=(q-p)^2\).  The exact-square and parity tests
make the two formulas in (7) integral, and direct multiplication or division
verifies the factorization.  No false candidate can cause an incorrect
output.

## 3. Repaired two-sign torus branch

For the hidden orientation \(\epsilon\), common order \(B\) gives

\[
B\mid p-\epsilon,
\qquad
B\mid q+\epsilon.
\]

Hence

\[
B^2\mid(p-\epsilon)(q+\epsilon)
      =N-1-\epsilon(q-p),
\]

and, for the true gap \(D=q-p\),

\[
D\equiv\epsilon(N-1)\pmod{B^2}.
\]

All signs are correct.  Also

\[
\frac{D}{\sqrt N}=\frac{x-1}{\sqrt x}
\]

is strictly increasing on \((1,2)\), with upper endpoint \(1/\sqrt2\).
Each sign class therefore contributes at most

\[
1+\frac{\sqrt N}{\sqrt2 B^2}
\]

candidates.  Adding the two lists, even if they overlap and duplicates are
retained, gives

\[
2+\frac{\sqrt{2N}}{B^2}.
\]

The V2 condition

\[
B^2\ge\frac{\sqrt N}{\sqrt2\,Q(n)}
\]

therefore bounds the combined count by \(2Q(n)+2\), exactly as claimed.

For every candidate gap, \(S^2=D^2+4N\) is a complete recovery test.  If
the right side is a square, parity is automatic for odd \(N\): an odd
\(D\) would make it \(5\pmod8\), which is not a square, while an even
\(D\) gives an even \(S\).  The stated parity check is harmless and direct
multiplication verifies the resulting roots.

## 4. Exact enumeration and bit cost

The irrational-looking interval endpoints need no approximation.  The
ordinary bounds are tested by

\[
4N<S^2,
\qquad
2S^2<9N,
\]

and the gap bound by \(0<2D^2<N\).  The first member of each residue class
is obtained with integer modular arithmetic, after which the algorithm adds
the public square modulus.

The supplied orders satisfy bounds of size \(O(N)\), so \(M^2\), \(B^2\),
all residues, and all candidates have \(O(n)\) bits.  Modular arithmetic,
exact integer square root, parity, multiplication, and division take
polynomial bit time per candidate.  A QP candidate count therefore gives
deterministic QP total bit cost.

As a non-proof sanity check, exhaustive enumeration over all balanced prime
pairs below 500, every divisor of \(\gcd(p-1,q-1)\), and every divisor of
both oriented torus group orders checked 5,916 ordinary cases and 12,678
torus cases.  Every congruence, inclusion, and candidate-count inequality
passed.

## 5. Scope relative to F170

F177 V2 is a genuine individual-channel terminal improvement.  It uses
\(M^2\) for an ordinary state or \(B^2\) for a torus state, whereas F170's
combined CRT state uses \(L=\operatorname{lcm}(A,B)\).  F170 remains
distinct and can combine two moderate channels; it also has an unbalanced
two-class factor search.  F177 requires balance and can be stronger when one
individual channel is large.

V2 does not supply either common order.  It does not convert local capacity
into a common order, handle the F172/F173 constant-common-order families,
cover other factor patterns, or prove all-input QP factoring.  Its boundary
claims are therefore accurate, and no conflict with F170 was found.
