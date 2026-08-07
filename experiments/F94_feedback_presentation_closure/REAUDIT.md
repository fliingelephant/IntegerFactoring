# F94 fresh hostile re-audit

## Verdict: FAIL

I audited the corrected `RESULT.md` at SHA-256

```text
7c4f9a4bcca5832c87988b80253d7e0622d4b53c6cf239cc1b60f1f2da21a9b5
```

The corrected candidate repairs all three failures in the first audit.  Its
central linear-algebra theorems are correct under the intended convention
that blocks are nontrivial, and I found no counterexample to the corrected
private-row theorem, the P91 and P99 consequences, or the deletion example.

Two new qualifications are nevertheless required before the candidate is
correct as written:

1. The setup permits `q_j=1`, although it asserts that every support `D_j`
   is nonempty and later says that every multiplicity-free refinement has a
   nonzero descendant coefficient.  That implication is false for a trivial
   old block.  Nontrivial old blocks must be required explicitly, or empty
   supports must be handled separately.
2. Section 8's polynomial-time claim is valid only in the bit size of the
   explicit maintained presentation and `log N`.  It becomes polynomial in
   `log N` only under an explicit polynomial state and iteration cap.  In
   addition, “every direction” cannot literally mean enumerating every
   vector-space direction when the new nullity is unbounded.

There is also a mechanical cross-reference error in the proof of Theorem 2:
its final references to equations (6) and (7) should refer to (9) and (10).

## 1. Fresh check of the exponent-refinement theorem

Fix a prime `ell` and work over `F_ell`.  The identity

\[
E'=\Delta_\alpha E
\]

immediately gives

\[
\ker E'=E^{-1}(\ker\Delta_\alpha),
\]

which is equation (4).  The restriction

\[
E:\ker E'\longrightarrow
\operatorname{im}E\cap\ker\Delta_\alpha
\]

is surjective and has kernel `ker E`.  Rank-nullity therefore gives (5),
and (6) follows exactly.

If the supports `D_j` are disjoint, the columns
`Delta_alpha e_j` have disjoint supports.  The nonzero columns are then
linearly independent.  A column is zero modulo `ell` exactly when every one
of its descendant multiplicities is divisible by `ell`.  This proves (7).
Thus multiplicities are handled correctly, including repeated prime factors
inside an old block.  The example `4=2^2` modulo 3 is also correct.

This fully repairs the first prior-audit objection.  The old candidate used
row duplication for a general refinement; the corrected candidate uses the
full multiplicity map and identifies its exact modular kernel.

### The trivial-block edge case

The hypotheses call the `q_j` positive integers, so they allow `q_j=1`.
Such a block has no descendants with positive exponent and hence

\[
D_j=\varnothing.
\]

This contradicts the setup's assertion that every `D_j` is nonempty.  It
also defeats the unqualified sentence that a multiplicity-free refinement
has a descendant coefficient nonzero modulo every prime.

For a literal example, take

\[
N=3,\qquad Q=(1),\qquad E=[1],\qquad B=(2),
\]

where 2 is supplied by a new endpoint.  The exact old-block factorization is

\[
1=2^0,
\]

so `Delta_alpha=[0]`.  All displayed multiplicities belong to `{0,1}`, but
modulo 2,

\[
\ker E=0,
\qquad
\ker(\Delta_\alpha E)=\mathbb F_2.
\]

Equations (4)-(7) themselves correctly predict this growth: the universal
condition in (7) is vacuous on the empty support.  The failure is the
nonempty-support assertion and the blanket multiplicity-free consequence.
The clean repair is to require

\[
q_j>1\quad\text{for every old block }j.
\]

The refined block convention should likewise state `b_r>1`; otherwise a
unit block `b_r=1` can be assigned arbitrary irrelevant exponents, destroying
the claimed disjointness of the supports.  Standard gcd-free presentations
normally discard 1, but the candidate must state that convention if it uses
it in the proof.

Alternatively, the candidate can allow `q_j=1`, call its support empty, and
exclude those redundant coordinates from the multiplicity-free corollary.

## 2. One-column closure theorem

Theorem 2 is correct.  A vector `(x,a)` is in the new kernel precisely when

\[
E'x+au=0.
\]

If `a` is nonzero, this equation implies that `u` lies in the old column
span.  Hence a nonclosing column forces `a=0` and leaves the old kernel
unchanged.  If `E'c+u=0`, subtracting `a(c,1)` leaves exactly an element of
`V_ell x {0}`.  The last coordinate makes the sum direct, so closure adds
one and only one kernel dimension.

The displayed conclusions (9) and (10) are right.  The proof text still
says “which gives (6)” and “so (7) follows”; those numbers refer to the
preceding theorem after the correction.  They must be changed to (9) and
(10).

## 3. Corrected private-row batch corollary

Corollary 4 now includes the condition missing from the failed version:

\[
(M_0)_{r_i,*}=0.
\]

It also states nonvanishing and vanishing modulo `ell`.  Suppose

\[
M_0x+\sum_i a_i u_i=0
\]

and choose the largest index `i` for which `a_i` is nonzero.  On row `r_i`,
the old span and all earlier appended columns vanish, while all later
coefficients vanish.  The remaining product
`a_i (u_i)_{r_i}` is nonzero, a contradiction.  Thus all `a_i` vanish and
`x` lies in `ker M_0`, proving (13).

This proves independence modulo the old column span, not merely mutual
independence of the appended columns, and fully repairs the second prior
objection.  The phrase “private fresh block in the final refined
presentation” must retain its precise meaning in (12): zero incidence in
`M_0` and in every earlier appended column.  Later columns may use that row;
the triangular proof does not require them to vanish there.

## 4. Canonical-inverse interpretation

If `g` is a unit and `w` is its least positive inverse, then

\[
gw=1+kN
\]

is an exact known multiplicative relation.  After lifting the old relation
matrix through the full refinement map, a residual block of `w` that

- divides no old block, and
- occurs in the new relation to exponent one

has a zero old row and a `1` in the new column.  Theorem 3 therefore makes
the column nonclosing for every prime.  This interpretation is correct.
“New cofactor ... that has not appeared before” must mean exactly this fresh
row condition; a newly assigned label for an old-supported factor would not
be enough.

The conclusion is only about the known modular column span.  It does not
exclude a direct gcd, a power or mixed-word decoder, a useful later reuse,
or an unknown relation.  The candidate preserves those distinctions.

## 5. P91 scope

The first audit objected that the old version invoked P91 under unrestricted
`N >= 2`.  The correction fully resolves this.  Both the decoder paragraph
and its later algorithmic use now require:

- `N=pq` for distinct odd primes;
- failure of the complete old decoder on the root image generated by the
  explicit known kernel; and
- a public prime `ell` numerically polynomial in `log N` for the short scan.

These are the needed P91 conditions.  In the closing case, the new
one-dimensional kernel quotient maps to one coset of the old root image.
After the complete old decoder fails, that image is trivial or a graph line,
so one test or the menu of at most `ell` tests is complete.  The statement
does not mistake the explicit known kernel for the complete relation lattice.

## 6. P99 sandwich

On the stated conditional event, the retained units generate `G_N` and are
all represented by products of current unit blocks `B`.  Therefore

\[
G_N=\langle a_1,\ldots,a_d\rangle
\leq\langle B\rangle\leq G_N,
\]

so equation (14) is exact.  A later factor-free refinement retains all those
representations and preserves the sandwich.  This proves only that abstract
subgroup enlargement is impossible on the P99 source event.  It does not
give public words for newly exposed blocks or complete the known relation
lattice.  The candidate states this scope correctly.

## 7. Complexity qualification

Matrix multiplication, modular kernel computation, span testing, and basis
updates are polynomial in

- the total bit size of the explicit block and exponent presentation;
- the bit sizes and count of the scanned primes; and
- `log N` for the modular arithmetic and gcd tests.

They are not unconditionally polynomial in `log N`.  After `T` retained
feedback relations the matrix already has at least `T` appended columns, so
even reading it costs `Omega(T)`.  If `T` or the number of retained blocks is
superpolynomial in `log N`, the bookkeeping is also superpolynomial in the
original input length.

Moreover, if a refinement increases the kernel dimension by `d`, the number
of nonzero one-dimensional directions is

\[
\frac{\ell^d-1}{\ell-1}.
\]

That is exponential in `d`.  Therefore “process every direction” cannot
literally prescribe enumeration of all directions while claiming polynomial
time.  The implementation must compute a kernel basis and invoke the
applicable complete decoder on a polynomial-size generating/test set.  The
P91 one-column coset scan remains polynomial when `ell` is numerically
polynomial in `log N`, but it does not itself justify arbitrary
multi-direction enumeration.

The precise repair is:

> The bookkeeping is polynomial in the explicit maintained presentation
> size and `log N`.  It is polynomial in `log N` when the number and bit size
> of retained blocks, relations, scanned primes, and feedback steps are
> polynomially capped.  Kernel updates operate on bases rather than all
> vector-space directions.

This qualification is consistent with the candidate's final statement that
it proves no all-input feedback law or factoring algorithm.

## 8. Ephemeral deletion example

The one-row example is exact.  Over `F_2`, the first column `[1]` is outside
the empty column span and creates no kernel.  Retaining it and appending a
second `[1]` gives

\[
[1\mid1]
\]

with kernel generated by `(1,1)`.  Deleting the first column makes the later
column nonclosing again.  The example proves only that deletion can erase a
future closure witness; it does not claim that this particular dependency
must reveal a factor.  No counterexample was found.

## Exact scope after repair

After excluding trivial blocks and qualifying complexity by explicit state
size, the corrected candidate gives exact accounting for the two ways the
known prime-saturation kernel can grow: multiplicity refinement and appended
column closure.  It gives no source law for either gate, no guarantee that a
new root leaves the synchronized image, no all-input polynomial state bound,
no factoring algorithm, and no computational lower bound.
