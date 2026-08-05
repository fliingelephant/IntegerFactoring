# F11 structured-CVP factoring: exact reduction, structural kill

**Approach-family ID:** `F11_structured_cvp_kill`  
**Status:** self-audited; no hostile verification or independent reconstruction yet.  
**Closest prior route:** F06/P10. This route does not quotient multiplication histories by a scalar carry. It encodes the complete multiplication CSP as an affine integer lattice and asks for an exact closest vector.

## Verdict

There is a clean polynomial-bit reduction from arbitrary integer factoring to exact Euclidean CVP on a natural family of multiplication-gadget affine lattices. It has an exact additive distance gap and does not assume a factor.

The hoped-for structural tractability fails at the encoding boundary:

- the exact constraint-incidence graph contains a subdivision of `K_(a,b)` and has treewidth at least `min(a,b)`;
- the affine lattice has codimension at least `ab`;
- the Toeplitz/circulant low-codimension relaxation forgets that the lifted multiplication matrix has Boolean rank one and has spurious exact closest vectors already for `N=25`;
- restoring that rank-one condition requires non-linear constraints or the full consistency gadgets that create the `K_(a,b)` core;
- converting the constraint kernel to an ordinary basis can densify it, so bounded width of some unrelated presentation cannot be assumed;
- “circulant,” “ideal,” or “low displacement rank” alone is not a proved polynomial-bit exact-CVP algorithm.

Thus F11 does not currently land in a class with a justified polynomial-time exact CVP algorithm. The exact missing lemma is stated at the end.

## Strongest natural exact encoding

First handle even `N` by returning 2 and prime `N` by deterministic primality testing. Let odd composite `N` have bit length `n`. Enumerate factor bit lengths

`2 <= a <= b`, with `a+b in {n,n+1}`.

There are only `O(n)` pairs, and some pair contains a nontrivial divisor `x<=sqrt(N)` and `y=N/x`.

For one pair introduce integer coordinates:

- factor bits `x_i` (`0<=i<a`) and `y_j` (`0<=j<b`);
- four tuple indicators `lambda_(i,j)^(u,v)` for every pair `(i,j)` and `(u,v) in {0,1}^2`;
- binary carry digits `c_(k,l)`, using `L=ceil(log_2 a)` digits for every carry `c_k`.

This many carry digits suffice: every column sum is at most `a`, and the recurrence below inductively gives `0<=c_k<=a-1` (an integral numerator greater than `-2` cannot yield a negative integer, while the upper bound is `floor((2a-1)/2)=a-1`).

Impose the following affine integer equations.

1. One tuple per bit pair:

   `sum_(u,v) lambda_(i,j)^(u,v)=1`.

2. Consistent factor-bit marginals:

   `x_i=lambda_(i,j)^(1,0)+lambda_(i,j)^(1,1)`,

   `y_j=lambda_(i,j)^(0,1)+lambda_(i,j)^(1,1)`.

3. For columns `0<=k<=a+b-1`, with absent partial products interpreted as zero,

   `sum_(i+j=k) lambda_(i,j)^(1,1) + c_k - 2c_(k+1)=N_k`,

   where `c_k=sum_l 2^l c_(k,l)`, `c_0=c_(a+b)=0`, and `N_k` is the `k`th bit of `N`.

4. Since `N` is odd and the lengths are exact,

   `x_0=y_0=x_(a-1)=y_(b-1)=1`.

Let this system be `Az=d` in `M` integer coordinates. Its binary solutions are exactly the schoolbook multiplication witnesses `xy=N` of lengths `(a,b)`: a binary one-hot tuple makes `lambda^(1,1)=x_i y_j`, and the carry equations telescope to the product identity. Conversely, every such factor pair supplies a binary solution with the ordinary carries.

The size is polynomial:

`M=4ab+a+b+(a+b+1)ceil(log_2 a)=O(n^2)`.

There are `O(n^2)` equations. Every matrix coefficient has magnitude `O(n)` and hence `O(log n)` bits; the right side uses only bits of `N`. Integer solvability, a particular solution `z_0`, and a basis of `ker_Z(A)` can be obtained by Smith/Hermite reduction. Hadamard's bound gives polynomial bit length for every relevant minor and hence for the retained basis data. This construction uses only `N`, its bits, and `(a,b)`; it contains no unknown factor or factor-dependent target.

If `Az=d` is integrally infeasible, skip this length pair. Otherwise its integer solutions form the affine lattice

`C=z_0+ker_Z(A)`.

Set the target to the all-`1/2` vector. Every integer coordinate contributes at least `1/4` to squared distance, with equality exactly at 0 or 1. Therefore:

- if a factor witness exists, the exact optimum is `M/4` and every closest vector is binary;
- if no binary witness exists, the squared optimum is at least `M/4+2`.

An exact CVP answer can therefore be accepted precisely at the baseline, decoded to `x`, and checked by multiplication. Uniqueness is unnecessary: swapped equal-length factors or several divisors may tie, but every baseline closest vector is a valid nontrivial factor witness.

The relative gap is only

`sqrt(1+8/M)=1+Theta(1/M)`.

Consequently, a constant-factor approximate CVP algorithm does not suffice; exact CVP (or comparably fine approximation) is essential.

## Bounded-treewidth obstruction

Consider the bipartite incidence graph between variables and affine equations. For every `(i,j)`, the two marginal equations and `lambda_(i,j)^(1,1)` give the path

`x_i -- E^x_(i,j) -- lambda_(i,j)^(1,1) -- E^y_(i,j) -- y_j`.

The internal vertices of these paths are distinct for distinct `(i,j)`. Hence the incidence graph contains a subdivision of `K_(a,b)`. Contracting those paths gives `K_(a,b)` as a minor, so

`treewidth >= treewidth(K_(a,b))=min(a,b)`.

For balanced factors this is `Theta(n)`, not bounded or logarithmic. Any exact-CVP dynamic program exponential in width is therefore exponential on the required arbitrary-input family. Moreover, an HNF/SNF kernel basis need not preserve even this constraint sparsity and is typically dense; an algorithm defined on basis-graph width needs a separate structural proof.

## Fixed/low-codimension obstruction

The `ab` one-hot equations have disjoint `lambda^(0,0)` coordinates and are linearly independent. Thus

`rank(A) >= ab`.

For balanced factors the affine lattice has codimension `Omega(n^2)`, a constant fraction of its ambient dimension. The reduction therefore does not enter a fixed- or low-codimension exact-CVP regime.

## Why the Toeplitz/circulant relaxation is unsound

Introduce only a lifted matrix `Z=(z_(i,j))` and require its anti-diagonal sums, together with carries, to equal the product bits. This linear convolution map is Toeplitz-like and has only `O(n)` column equations. But multiplication also requires

`Z=x y^T`, with binary `x,y`.

That rank-one Boolean set is not additive and is not a lattice or ideal. Dropping it produces spurious closest points.

A compact explicit certificate is `N=25`, `a=b=3`. The true factors have bits `x=y=(1,0,1)` and lifted matrix

```text
Z = 1 0 1
    0 0 0
    1 0 1.
```

The binary matrix

```text
Z' = 1 0 1
     0 1 0
     0 0 1
```

has the same anti-diagonal sums `(1,0,2,0,1)` and the same carry sequence `(0,0,0,1,0,0)`, so it satisfies exactly the same linear product/carry equations for the bits `(1,0,0,1,1)` of 25. Yet `det(Z')=1`, so `Z'` has rank 3 and cannot equal `xy^T`. Both matrices are binary and therefore tie at the absolute `1/2`-target minimum. An exact CVP solver for the relaxed Toeplitz system may return `Z'`, from which no factor can be decoded.

Adding equations that enforce rank one requires bilinear `2x2`-minor constraints. Linearizing them with truth-table/consistency gadgets returns to a dense interaction structure at least as strong as the construction above. Alternatively, building a convolution-by-one-factor basis would make multiplication linear, but it requires the unknown factor and is circular.

## Input-class audit

- **Primes:** primality testing must precede the CVP calls. Without a binary witness the baseline guarantee is absent.
- **Even inputs:** return 2 directly.
- **Prime powers and repeated factors:** a divisor `x` and cofactor `N/x` give a valid enumerated length pair; uniqueness is not needed.
- **Unbalanced composites:** the exact reduction still works. Width may be small when the least factor has few bits, but those cases do not cover arbitrary balanced inputs (and very small factors are already easy by trial division).
- **General composites:** choose any nontrivial divisor at most `sqrt(N)`; its bit lengths satisfy the enumerated conditions. After each verified split, recursive application has only polynomially many calls if the missing CVP algorithm is polynomial.
- **Coefficient leakage:** neither `A` nor the half-integral target contains a factor. Computing the affine kernel is ordinary integer linear algebra, not modular inversion or hidden factoring.
- **Gap/uniqueness:** the additive squared gap is exactly at least 2, but the relative gap tends to 1 and the closest vector need not be unique. Exact recovery remains correct because every baseline minimizer is a factor witness.

## Exact surviving reduction and missing lemma

The surviving statement is only:

> Factoring reduces in polynomial bit complexity to exact Euclidean CVP on the affine kernel lattices of the one-hot schoolbook-multiplication systems above.

To turn F11 into an algorithm one must prove:

> **Missing F11 lemma.** Given one of these multiplication-gadget affine lattices (or a polynomial-bit basis of its integer kernel) and its half-integral target, exact Euclidean CVP is solvable in time polynomial in `n`, despite incidence treewidth `Omega(n)`, codimension `Omega(n^2)`, and possible basis densification.

This lemma already implies arbitrary integer factoring through the explicit reduction, so calling the lattices “structured” is not progress. A materially new retry must either find an exact factor encoding that provably avoids the `K_(a,b)`/rank-one obstruction and lands in a class with a proved polynomial-bit exact-CVP algorithm, or prove the missing lemma by a mechanism not equivalent to enumerating factor-bit histories.

## Scope

This is a rigorous obstruction to the precise natural exact encoding and its low-codimension Toeplitz relaxation. It is not a lower bound against every possible lattice encoding of factoring, every low-displacement-rank basis, or every future structured-CVP algorithm.
