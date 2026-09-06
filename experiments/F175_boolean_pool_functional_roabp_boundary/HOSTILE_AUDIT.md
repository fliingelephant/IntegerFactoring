# F175 hostile audit — PASS with precision repairs

## Verdict

**PASS for the theorem and proof.** The exact singleton-cut function rank is

\[
2^{K-1}
\]

over every prime field of characteristic greater than that number. The
functional ROABP consequence is valid for arbitrary variable order and
arbitrary, nonuniform univariate layer functions. I found no leading-term,
modular-cancellation, canonical-representative, or matrix-rank defect.

The named model consequences are valid when they have their standard
separated meaning over the same field (or a field extension): the inspected
variable occurs only at its one site or leaf, and cutting its first state or
leaf bond separates that variable from all others. They are representation
width statements. They are not time lower bounds for implicit state
representations or lower bounds for general determinant, norm, resultant,
branching, random-input, or gcd-only algorithms.

Two sentences in `SELF_AUDIT.md` need precision repairs before promotion.
They do not damage the theorem.

1. The standard direction-weighted cube Laplacian has nonzero eigenvalues
   `2 L_S`, not `L_S`. Its nonzero spectral product is
   `2^(2^K-1) Q_K`. Equivalently, `Q_K` is the reduced norm only after
   normalizing the group-algebra element by `1/2`, or it is the spectral
   product only for the half-Laplacian. The text must state this normalization
   or say "up to the displayed power of two."
2. "The proved `2^(K/2)` frontier" and the following multiblock sentence can
   sound like a lower bound for resultant or norm algorithms. P34 proves one
   two-block evaluator with that scale. F175 proves no optimality result for
   resultants, multiblock norms, modular composition, or global circuits. Say
   "the verified two-block construction has `2^(K/2+O(1))` scale" and limit
   the next sentence to the naive recursive construction.

I recommend two additional definition edits. State explicitly that the
coefficient functions have individual degree at most `d`, and state that a
tree variable occurs only at its designated leaf. Both facts are already
implicit in the proof, so neither is a mathematical repair.

## Frozen inputs

I read the three requested files in full and did not edit them or any durable
ledger. Their SHA-256 hashes at audit time were:

- `STATEMENT.md`:
  `310b554edfbc5b7cf641841648564d16a1bb979a1856ccd44bb6c1e71f550c4b`;
- `PROOF.md`:
  `83d860671104a3b4fd0255151a694e8e6ce158f124cf745a02d22fafb9c019b3`;
- `SELF_AUDIT.md`:
  `90e6909fc78f77555d5440acd99ff66686fc0b3dcc46a825f3ceb17aa0da3536`.

No computation was needed.

## 1. Exact leading coefficient

Put `m=K-1`. The nonzero subset forms split into groups

\[
G_i=\{L_S:\min S=i\},\qquad |G_i|=c_i=2^{m-i}.
\]

For a fixed `t`, write the greedy fill as

\[
t=\sum_{h<i}c_h+u,\qquad 0\le u\le c_i,
\]

with the evident endpoint convention. Lexicographic order first maximizes
the number of selected forms from `G_1`, then from `G_2`, and so on. Hence

\[
\operatorname{LM}(e_t)
=\left(\prod_{h<i}Y_h^{c_h}\right)Y_i^u,
\qquad
\operatorname{LC}(e_t)=\binom{c_i}{u}.
\]

If a selected form supplies a lower term, the exponent of the earliest
affected variable decreases. No later group contains that variable, so no
other choice restores the same monomial. If a selection omits a form from an
earlier not-yet-full group, its leading exponent vector is already smaller.
Thus the coefficient is exactly the binomial coefficient, not merely a
nonzero contribution that could cancel with others.

Every prime divisor of `binom(c_i,u)` is at most `c_i<d`. Therefore a prime
`r>d` cannot annihilate it. This includes `t=0` and the full-group endpoints,
where the coefficient is one. The zero form from the empty subset explains
why the expansion stops at `e_(d-1)` and has powers `x^d,...,x` only.

## 2. Coefficient and function independence

Each coefficient

\[
C_t=Q_{K-1}e_t
\]

is nonzero because the polynomial ring over `F_r` is an integral domain.
Its total degree is `(d-1)+t`, so the `C_t` are polynomially independent by
homogeneous degree.

There is no hidden finite-field cancellation. The whole polynomial `Q_K`
has individual degree exactly `d` in every variable. Coefficient extraction
in `x` gives

\[
\deg_{Y_i} C_t\le d<r.
\]

Thus every linear combination of the `C_t` is already its canonical
finite-field representative. A zero function would be the zero polynomial.
The functions `x,x^2,...,x^d` are likewise independent because a nonzero
univariate polynomial of degree at most `d<r` cannot vanish at every point
of `F_r`.

Let `A` have these `d` row functions as columns and let `B` have the `C_t`
column functions. Both matrices have column rank `d`, and
`mathcal M_1=A B^T`. Left and right inverses for the two full-column-rank
matrices show that the product has rank exactly `d`; this is not only an
upper-rank factorization. Symmetry gives the same result for every singleton
cut.

## 3. Arbitrary order and arbitrary layer functions

After the first variable in any ROABP order, a width-`w` state gives a sum
of `w` singleton-separated functions. This statement uses only pointwise
function values. It does not use a degree bound, uniformity, or a restriction
on how the univariate layer functions depend on public parameters. The
singleton matrix rank therefore forces `w>=d`.

Interpolation in the proof is optional but correct. Each arbitrary
univariate function has a representative of degree at most `r-1`; because a
variable occurs in only one layer, interpolation does not create an
individual-degree conflict across layers.

The same cut argument proves the stated tensor-train and separated-sum
bounds. For a tree tensor network it applies only when the selected variable
is confined to its physical leaf tensor. If the variable is reused in other
tensors, cutting the leaf bond no longer gives the asserted separation and
the model is outside the theorem. A one-pass linear recurrence is included
only when its state update is linear in the current state; an arbitrary
nonlinear or implicitly encoded state is not included.

If a composite-modulus ROABP is intended, reduction modulo a hidden prime
also causes no loophole: choose one fixed lift in `Z/NZ` for every element of
`F_r`, restrict all input variables to those lifts, and reduce the resulting
layer values modulo `r`. This produces arbitrary univariate functions on
`F_r` and preserves the same width. This observation does not cover
data-dependent branching or a path that finds a nonunit and returns a
factor.

## 4. Determinants, Moore identities, and characters

The displayed `K=2` Moore comparison is correct in every odd
characteristic: `xy(y-x)` and `xy(x+y)` have different third zero lines.
More generally, a determinant whose inspected variable is confined to one
column has singleton separation rank at most the matrix dimension by Laplace
expansion, so a small determinant of that special form cannot equal `Q_K`
under the theorem's hypotheses.

This does not extend to a general small determinant. Its entries can reuse
all variables, and determinant evaluation need not admit a small
one-variable ROABP. F175 also says nothing about a determinant or character
formula for a different function with the same useful local zero set. An
exact separated character expansion of `Q_K` over `F_r` (or an extension)
does inherit the rank bound. The additive-character zero-count formula in
the self-audit computes a different observable and uses `r` modes; the
packet correctly makes no sampling lower-bound claim from it.

## 5. P34 scale

Under the P34 promise `53<=p<q<2p`, put `h=floor(sqrt(N))` and
`T=2^K`, where `K=floor(log_2 h)-3`. Then

\[
T\le h/8<\sqrt N/8<\sqrt2\,p/8<p,
\]

so both hidden characteristics exceed `T>d=T/2`. If
`ell=floor(log_2 h)`, then `2^ell<=h<2^(ell+1)`, hence

\[
h/16<T\le h/8.
\]

Therefore `d=2^(Theta(n))` for
`n=ceil(log_2(N+1))`. For each fixed `C>0` and fixed `k`,

\[
2^{C(\log_2(n+1))^k}=2^{o(n)}.
\]

This proves an exponential-versus-QP **width** separation in the named
models. It does not prove that every exact P34 evaluator takes exponential
time, and it does not constrain the weaker random-input or gcd-only task.

