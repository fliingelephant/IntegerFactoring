# F236 numerical results

These scans are finite evidence.  They are not asymptotic proofs.

## Domain and environment

The frozen domain contains all 34,463 balanced zero-defect prime pairs with
`p<2^22`.  The maximum input length is 45 bits.  Runs used one low-priority
core on `seetacloud`.  The container reported 503 GiB RAM, 367 GiB
available, and 22 GiB free disk before the first run.  Each scan used about
35 MB.  The host load was high, so no parallel scan was used.

## Public word obstruction

The first scan combined:

- `product_{k<=n}(N^k-1)`;
- `product_{k<=n}(H^k-1)`;
- every `(uH+c)^n` with `u<=n` and `|c|<=n`;
- `n!`.

The maximum smaller P204 residual was 2,095,493.  The exact worst row was

\[
p=4190987,\quad q=4243619,\quad N=17784952061953,
\]

\[
n=45,\quad B=4194304,\quad H=4240263,
\quad s_p=2095493,\quad s_q=2121809.
\]

Both residuals are prime.  Their `N`-orders are 2,095,492 and 2,121,808.
The complete combined word is coprime to both residuals.

## Centered carry identities

For a multiplier `u`, write

\[
up=K_pB+x,\qquad uq=K_qB+y,
\qquad -B/2\le x,y<B/2,
\]

and define

\[
c={xy-u^2\over B}\in\mathbb Z.
\]

The exact public recovery identity is

\[
T:=K_pq+K_qp={u^2H+K_pK_qB-c\over u}.
\]

For a guessed tuple `(u,K_p,K_q,c)`, the hidden factor is a root of

\[
K_qX^2-TX+K_pN=0.
\]

Equivalently, the discriminant

\[
\Delta=T^2-4K_pK_qN=(K_pq-K_qp)^2
\]

must be a square.  A square root gives

\[
p={T\mathbin\mp\sqrt\Delta\over2K_q},
\qquad
q={T\mathbin\pm\sqrt\Delta\over2K_p},
\]

and exact division verifies the result.  Thus false tuples are harmless.

When `K_p=K_q=K`, this reduces to the ordinary trace
`p+q=T/K`.  Thus a short public carry list gives a deterministic verified
factor search.  The two center indices must also be enumerated.

Use round-half-up at a dyadic tie.  Balance gives `p>B/2`, so the centered
indices are positive.  For a fixed `u`, both lie in `[1,3u]`.  Testing every tuple with `|c|<=C` costs
`O(Cu^2)` arithmetic operations.  Testing all `u<=U` costs `O(CU^3)`.
Thus numerical-QP caps give a valid deterministic search bank.  A Las Vegas
version may sample `u`; it then needs an inverse-QP lower bound on the event
`|c_u|<=C` at every input.

For `u=1`, the maximum centered carry was 522,514.  It retained 19 bits at
45-bit input size.  The maximum of `min(c,s_p,s_q)` was also 522,514, so
neither a small carry nor a small residual is forced.

The carry residue itself has no forced short meta-order.  On the first worst
word row, the correct carry is `-39`, but 39 is a primitive root modulo both
large residual primes.  The word `product_{j<=n}(39^j-1)` misses both.

## Multiplier scaling

With the two hidden nearest centers, the exact maxima of the best carry were

| multiplier cap | maximum `min |c_u|` |
|---|---:|
| `u<=n` | 27,483 |
| `u<=n^2` | 414 |
| `u<=n^3` | 14 |

This finite improvement matches the generic simultaneous-approximation
scale `B/U`; it does not prove a numerical-QP carry for asymptotic inputs.
The exact worst cubic-cap row was

\[
p=3565721,\quad q=6646697,\quad n=45,
\]

with minimum 14 at `u=5218`.

A uniform `u` in `[1,n^3]` hit `|c_u|<=n` with minimum observed probability

\[
{15\over91125}=0.000164609.
\]

This is finite evidence only.  The generic heuristic is `CU/B`, which is
exponentially small for polynomial `C,U` as `n` grows.

The fully public one-center choice

\[
K_u=\operatorname{round}(uH/B)
\]

did not improve with the multiplier cap.  Its worst minimum was 1,322,450
for each of `n,n^2,n^3`, always at `u=1`.  The favorable approximation
therefore depends on the two hidden centers.

## Exact obstruction suggested by the data

Zero defect makes every `c_u` integral.  It does not, by itself, improve the
standard two-dimensional approximation bound.  Standard simultaneous
Dirichlet gives a multiplier `u<=U` with

\[
|c_u|=O(B/U+U^2/B).
\]

For every numerical-polynomial `U`, this remains exponential.  The scans
found no separate one-dimensional collision law with better scale.  A
complete positive route still needs one of:

- a special approximation theorem using `pq=1+BH` that beats `B/U`;
- a public way to infer the two center indices;
- a different integer word whose P204 residual is numerical QP.

## Remote output hashes

- first word scan output: `38603fdc32a5a9f20cd396fbfa7ac41f2569d43a6760d7b34d996d30362ae1b7`;
- multiplier scaling output: `63268e6260bf178b0a6426660a182e90eeb83e0b376a15ec7c65a537fad5fd1b`;
- public fixed-center output: `389964b6367d3bd1ea5538175497a7e52d911cdff3a85109b4827a3a7a490ba3`;
- first-hit output: `6b72f5b762b797404b87a745f9aa46d881ff62fd737cd6d0ad46312deefb9348`.
