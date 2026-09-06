# F175 statement — the Boolean pool has exponential one-variable functional rank

**Status:** candidate. This is a proof-only boundary for P34. It is not a
factoring algorithm and it is not a lower bound for general arithmetic
circuits or general modular algorithms.

For an integer `K >= 2`, put

\[
 Q_K(X_1,\ldots,X_K)
 =\prod_{\varnothing\ne S\subseteq[K]}
   \left(\sum_{i\in S}X_i\right),
 \qquad d=2^{K-1}.
\]

Let `r` be a prime with `r>d`. For each index `j`, form the matrix of the
function `Q_K` across the singleton cut `X_j | X_{-j}`:

\[
 \mathcal M_j[x,y]
 =Q_K(y_1,\ldots,y_{j-1},x,y_{j+1},\ldots,y_K),
\]

where rows are indexed by `x in F_r` and columns by
`y in F_r^{K-1}`.

## Theorem

For every `j`,

\[
 \operatorname{rank}_{\mathbb F_r}\mathcal M_j=d=2^{K-1}.
\]

Consequently, suppose an exact functional read-once oblivious algebraic
branching program computes `Q_K` on all of `F_r^K` in any variable order:

\[
 Q_K(x_1,\ldots,x_K)
 =u^T M_1(x_{\pi(1)})M_2(x_{\pi(2)})\cdots
 M_K(x_{\pi(K)})v.
\]

The entries of each `M_i` may be arbitrary functions `F_r -> F_r`. They may
be nonuniform and may depend on `r`, on a surrounding composite modulus, and
on all public parameters. The width immediately after the first variable is
at least `d`. Thus the maximum width is at least `2^{K-1}`.

The same lower bound applies to these exact models:

1. a one-pass linear-state recurrence that reads each input residue once;
2. a tensor train with one input variable at each site;
3. a tree tensor network in which each variable occurs only at its designated
   leaf and that leaf is attached through one bond, for the dimension of that
   leaf bond;
4. an exact separated expansion across any singleton cut, including an
   exact sum of character products.

For P34, `K=Theta(n)` and both hidden primes satisfy `p,q>2^K>d`.
Therefore the required width is `2^{Theta(n)}`, which is larger than every
fixed quasipolynomial `2^{C(log_2(n+1))^k}`.

## Exact scope

The theorem does not exclude any of the following:

- a general arithmetic circuit that reads or reuses variables many times;
- an implicitly represented exponential-width state that might admit a
  special fast update;
- a small determinant, Pfaffian, permanent, or other global circuit whose
  expansion has exponential read-once width;
- a branching algorithm whose nonunit or denominator screens can themselves
  expose a factor;
- an algorithm that computes only a different function with a useful local
  zero set, rather than `Q_K` exactly;
- an algorithm that is correct only on a random subset of inputs;
- a characteristic-dependent Moore, Frobenius, or finite-field function
  outside the stated read-once model;
- a gcd-only detector that never computes `Q_K`.

The elementary integer Moore determinant does not supply the missing
positive construction. Already for `K=2`,

\[
 \det\!\begin{pmatrix}x&y\\x^2&y^2\end{pmatrix}
 =xy(y-x),
 \qquad
 Q_2(x,y)=xy(x+y).
\]

Their zero sets differ over every odd characteristic. This observation
rejects only that direct characteristic-two lift. It does not reject a
different determinant or a different pooled observable.
