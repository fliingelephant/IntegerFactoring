# F11 structured-CVP reconstruction

Status: **self-audited proof-blind reconstruction**.

## Verdict

Every assertion in the corrected bare statement is true with the standard
embedded-lattice definition of exact search Euclidean CVP.  The affine system,
distance gap, normalization to an integer target, incidence minor,
codimension bound, and the narrow lifted-convolution counterexample are proved
below.  This is a polynomial-time Turing reduction from factoring to exact
CVP on this family; it is not a polynomial-time factoring algorithm unless
exact CVP on the family can itself be solved in polynomial time.

## 1. The exact affine multiplication system

Fix an odd `n`-bit integer `N` and a pair `2<=a<=b` with
`L=a+b` in `{n,n+1}`.  Bits are little-endian, and `N_k=0` for `k>=n`.
Use these ambient integer variables:

* factor bits `x_i` for `0<=i<a` and `y_j` for `0<=j<b`;
* four tuple variables `t_(ij)^(uv)` for every `(i,j)` and
  `(u,v) in {0,1}^2`;
* carry digits `c_(k,h)` for `1<=k<L` and `0<=h<H`, where
  `H=ceil(log_2 a)`, representing
  `C_k=sum_h 2^h c_(k,h)`.  Set `C_0=C_L=0` as constants.

Let `z` collect all variables and let

`M=a+b+4ab+(L-1)H`.

The integer equations `Az=d` are:

1. For every `(i,j)`,
   `sum_(u,v) t_(ij)^(uv)=1`.
2. For every `(i,j)`,
   `x_i=t_(ij)^(10)+t_(ij)^(11)` and
   `y_j=t_(ij)^(01)+t_(ij)^(11)`.
3. `x_(a-1)=y_(b-1)=1` and, since `N` is odd, `x_0=y_0=1`.
4. For every `0<=k<L`,

   `C_k + sum_(i+j=k) t_(ij)^(11) = N_k + 2 C_(k+1)`.

The final equation is essential.  If `a+b=n`, it says
`C_(n-1)=N_(n-1)=1`; if `a+b=n+1`, it says `C_n=N_n=0`.
Prematurely forcing `C_(L-1)=0` would incorrectly delete the first case.

### Binary solutions are exactly factor witnesses

In a binary solution, the one-hot and marginal equations force the unique
selected tuple at `(i,j)` to be `(x_i,y_j)`.  Hence
`t_(ij)^(11)=x_i y_j`.  Multiplying the column equations by `2^k` and summing
telescopes the carries:

`sum_(i,j) x_i y_j 2^(i+j) - sum_k N_k 2^k = 2^L C_L-C_0=0`.

Thus the decoded positive integers `x,y` satisfy `xy=N`.  The leading-bit
equations give exact bit lengths `a,b`; in particular both factors are at
least two.

Conversely, let length-`(a,b)` integers `x,y` satisfy `xy=N`.  Choose at each
pair the unique tuple `(x_i,y_j)` and use the ordinary multiplication carries.
If `S_k=sum_(i+j=k)x_i y_j`, induction gives the exact bound

`0<=C_k<=a-1`.

Indeed it starts at zero, `S_k<=a`, and
`C_(k+1)=(C_k+S_k-N_k)/2` is a nonnegative integer with
`C_(k+1)<a`.  Therefore `H=ceil(log_2 a)` binary digits suffice.  Their
available range may extend to `2^H-1`, but the column recurrence uniquely
determines the carry, so that harmless slack creates no binary solutions.
The tuple and carry assignment is a binary solution of `Az=d`.

## 2. Why the length enumeration is complete

For a nontrivial factorization `N=xy`, reorder the factors so `x<=y` and let
their bit lengths be `a,b`.  Odd nontrivial factors give `2<=a<=b`.  The bounds

`2^(a+b-2) <= N < 2^(a+b)` and
`2^(n-1) <= N < 2^n`

imply `n<=a+b<=n+1`.  Thus enumerating the stated pairs includes a witness for
every odd composite.  There are only `O(n)` pairs.

## 3. Polynomial encoding and integer normal forms

There are `M=O(n^2)` variables and `O(n^2)` equations.  Matrix coefficients
are `0`, `+/-1`, or carry coefficients `2^h,2^(h+1)` of magnitude `O(a)`;
the right-hand side contains only bits and constants.  Even a dense encoding
therefore has polynomial length, and the natural sparse encoding is smaller.

Integer feasibility and the affine integer solution set are computable in
polynomial bit complexity by HNF or SNF.  Concretely, compute

`U A V = D`

with `U,V` unimodular and `D` diagonal.  The equations are integrally feasible
exactly when the nonzero diagonal entries divide the corresponding entries of
`Ud` and all remaining entries of `Ud` vanish.  Setting the free transformed
coordinates to zero gives one integer solution `z_0`; the corresponding free
columns of `V` give a basis `B` of `ker_Z(A)`.  Hence every integer solution is
uniquely of the form `z_0+B w`, `w in Z^r`.

This is a bit-complexity statement, not unit-cost elimination.  If `rho` is
the rank and the entries are bounded by `C`, Hadamard bounds every nonzero
`rho`-minor by `(sqrt(rho) C)^rho`, whose bit length is
`O(rho(log rho+log C))`.  Polynomial-bit HNF/SNF algorithms keep reduced
remainders and transformation data within polynomially many bits; the same
minor bounds apply to the augmented matrix `[A|d]`.  Consequently `z_0`, `B`,
and their computation have polynomial encoding length and polynomial bit
cost.  Uncontrolled textbook elimination would not by itself justify this
claim; a polynomial-bit normal-form algorithm is required.

If `Az=d` is infeasible, that length pair is skipped.  It cannot contain a
binary factor witness.

## 4. The exact CVP gap

Let `t=(1/2,...,1/2) in Q^M`.  Every integer coordinate `q` satisfies

`(q-1/2)^2 >= 1/4`,

with equality exactly for `q in {0,1}`.  A nonbinary integer coordinate has
distance at least `3/2`, so its squared contribution is at least `9/4`, an
increase of exactly `2` over baseline.

Therefore, on a feasible affine coset:

* a binary factor witness gives squared optimum exactly `M/4`;
* if no binary witness exists, every integer point has squared distance at
  least `M/4+2`;
* every minimizer at baseline is binary, hence the affine-system proof above
  decodes it to `xy=N`.  The multiplication is checked directly before a
  factor is returned.

This proves both the gap and the stronger assertion about every baseline
minimizer; uniqueness is neither claimed nor needed.

## 5. Standard CVP conventions and integer-target normalization

Under the standard embedded-lattice convention, an exact search-CVP instance
is a full-column-rank integer matrix `B in Z^(M x r)` and a rational target in
`Q^M`; the lattice need not have full rank in the ambient space.  Translate
the affine coset by asking for the closest `Bw` to `t-z_0`.

No rational target is necessary.  Give CVP the basis `2B` and integer target

`T=1-2z_0`.

The returned vector `2Bw` minimizes

`||2Bw-T||^2 = 4 ||z_0+Bw-t||^2`.

Thus the scaled binary baseline is `M` and the scaled gap is `8`; division by
two recovers `Bw` exactly.

The zero lattice vector bounds the returned distance by `||T||`, so the
closest vector has polynomial-bit coordinates.  Coefficients in the basis also
have polynomial bit length: select a nonsingular maximal square row minor of
`B` and apply Cramer's rule plus the same Hadamard bound.  Exact squared
distance comparison and decoding therefore remain polynomial-bit operations.

If the integer kernel has rank zero, the affine system has at most the single
point `z_0`; evaluate its distance directly instead of submitting a degenerate
zero-column basis.

Some formulations require a full-rank lattice in its ambient dimension.  That
convention is also covered with polynomial overhead.  The integer kernel is
primitive, and the SNF transformation supplies columns `C` such that, after a
column reordering, `D_0=[B C]` is unimodular.  Let

`S=(M max(1,|D_0|_max))^(M-1)` and
`R_T=M max(1,|T|_max)`,

and choose the polynomial-bit integer `Q=2 S R_T+1`.  Use the square basis

`[2B, Q C]`

with target `T`.  Since `det D_0=+/-1`, its least singular value is at least
`1/S`.  Any lattice vector using a nonzero `C` coefficient has norm greater
than `2||T||`, hence is farther from `T` than the zero vector.  Every closest
vector therefore has zero `C` coefficient and is exactly a vector of `2B`.
The logarithm of `Q` is polynomial in the original input length.

## 6. Factoring reduction and all input classes

This gives a deterministic polynomial-time Turing reduction to exact search
CVP:

1. For an even input, remove all powers of two and recurse on the odd part.
2. A polynomial-time deterministic primality test terminates prime leaves.
3. For an odd composite node, enumerate the `O(n)` length pairs.  Use SNF/HNF
   to skip integrally infeasible systems; call exact CVP on every feasible
   affine kernel until a baseline point is returned.  The length lemma ensures
   one exists.  Decode, verify `1<x,y<N` and `xy=N`, and recurse on `x,y`.

Prime powers and repeated factors need no promise or special step: a divisor
and its cofactor still form a witness, and recursion retains multiplicities.
Arbitrary composites are handled identically.  The recursion tree has at most
`O(n)` nontrivial nodes because the number of prime factors with multiplicity
is at most `log_2 N`; with `O(n)` CVP calls of polynomial-size instances per
node, the total oracle reduction, normal-form work, arithmetic, and output
verification have polynomial bit complexity.

## 7. Incidence minor and codimension of this presentation

Use the standard bipartite constraint-incidence graph, with a vertex for every
variable and equation and an edge for incidence.  For every `(i,j)` it contains
the path

`x_i -- X_(ij) -- t_(ij)^(11) -- Y_(ij) -- y_j`,

where `X_(ij)` and `Y_(ij)` are the two marginal equations.  These paths have
pairwise disjoint internal vertices and share only their appropriate factor-bit
endpoints.  Deleting all other vertices and edges leaves a subdivision of
`K_(a,b)`.  Contracting the paths gives a `K_(a,b)` minor, so treewidth is at
least `tw(K_(a,b))=a` because `a<=b`.

The `ab` one-hot rows are linearly independent: each has nonzero entries in
its own disjoint block of four tuple columns.  Hence

`rank(A)>=ab`.

Equivalently, `ker_R(A)` has codimension at least `ab`; whenever the affine
system is feasible, its real affine hull has the same codimension.  This is a
claim about this exact one-hot presentation, not every possible multiplication
encoding.

## 8. The narrow lifted-convolution counterexample

Consider instead the relaxation whose binary lifted variables are only a
matrix `W=(w_ij)` and the carry digits, with the `L` anti-diagonal equations

`C_k + sum_(i+j=k) w_ij = N_k + 2C_(k+1)`.

Its constraint rank is at most `L=a+b`, rather than the one-hot system's lower
bound `ab` (the ambient presentations differ, so this is only the displayed
linear-constraint comparison).

For `N=25`, `a=b=3`, the true factor bits for `5*5` are `(1,0,1)`, and the true
outer product is

```
W_true = [1 0 1]
         [0 0 0]
         [1 0 1].
```

Its anti-diagonal sums for `k=0,...,5` are

`(1,0,2,0,1,0)`.

The binary matrix

```
W_spurious = [1 0 1]
             [0 1 0]
             [0 0 1]
```

has the same anti-diagonal sums, while its determinant is one, so its ordinary
rank over `Q` or `R` is three, not one.  Its Boolean rectangle rank is also
three: the three diagonal ones cannot share an all-one rectangle because each
pair has at least one zero cross-entry, and three singleton-row rectangles
give the matching upper bound.  With the padded bits of 25,
`(N_0,...,N_5)=(1,0,0,1,1,0)`, both matrices use the same carries

`(C_0,...,C_6)=(0,0,0,1,0,0,0)`.

Thus `W_spurious` is a binary feasible point of the half-target relaxation and
therefore itself attains the coordinatewise baseline distance.  It is not a
factor outer product, so not every closest vector of this relaxation is
certified as a factor matrix.

Nothing here concerns all possible ways of restoring rank one, proves a width
lower bound for such restorations, or says that entries of this particular
spurious matrix cannot incidentally expose the number 5.  The counterexample
refutes only Boolean rank-one enforcement by the displayed anti-diagonal
relaxation.
