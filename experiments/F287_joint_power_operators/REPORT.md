# F287: Joint power operators and a structured triple-product witness

**Family:** route:F30

Status: author-derived exact claims and a finite certificate. Independent
statement-only reconstruction is pending. No novelty or all-input factoring
claim is made. No external mathematical theorem is needed below except the
explicit P232 dependency stated here.

## Question and nearest record

The initial question was whether sums or products of public power derivatives
retain CRT information when all individual ranks synchronize. The initial
object was a sum of two rank-two derivatives on traceless two-by-two matrices.
That calculation suggested that a sum can retain relative scalar weights.
The selected construction below instead uses a three-factor composition with
an intentionally deficient adjacent product. It gives an exact distinction
between derivatives, commutators, and centralizer projections.

The Rust reader located and loaded P232. That record concerns individual
derivative ranks only and explicitly excludes combined operators. It proves
that for squarefree characteristic polynomial and collision-free N-th powers,
ker L_A = Cent(A) and im L_A = im ad_A. The new operation is L_A L_B L_A;
its rank depends on a weighted pairing that those two subspaces do not fix.
No F288 work was consulted. The local paper cache was absent; this packet
does not make a literature-comparison or novelty claim.

## Field setting and two-factor boundary

Let k be a field of odd characteristic dividing N. Let E=M_d(k), with
nondegenerate pairing <X,Y>=tr(XY). Assume every matrix under consideration
has squarefree characteristic polynomial and that N-th powering is injective
on its distinct eigenvalues. Put C_A=Cent(A), U_A=C_A^perp=im ad_A.
The derivative L_A has kernel C_A and image U_A, and is self-adjoint for
the trace pairing. Its restriction to U_A is invertible.

Consequently:

- A vertical stack of derivative maps has kernel the intersection of their
  centralizers, so its rank depends only on the unpowered geometry.
- A horizontal concatenation has image the sum of the U_A, with the same
  conclusion.
- rank(L_A L_B) = dim U_B - dim(U_B intersect C_A). This equals the rank
  of ad_A ad_B and of P_A P_B, where P_A projects onto U_A along C_A.
- If all three maps have rank r and both adjacent products have rank r,
  their restrictions between the corresponding r-dimensional image spaces
  are isomorphisms, and the triple product has rank r. A weight-dependent
  loss in such a triple requires an adjacent deficiency.

These statements concern ranks, not selected entries or intermediate gcds.

Sums do retain weights even in dimension two. On traceless matrices, if
A^2=aI with a nonzero and N odd, then L_A=a^((N-1)/2) P_A. For two
such matrices let s=a^((N-1)/2), v=b^((N-1)/2), and
rho=tr(AB)^2/[tr(A^2)tr(B^2)]. The rank-two projection formula and the
determinant lemma give

    det(s P_A + v P_B) = s v (s+v) (1-rho).

After screening the geometry and the nonzero weights, the only extra
rank loss is precisely the scalar Euler-residue equation s+v=0. This is
why the selected experiment moved to the structured triple above.

## Triple compression lemma

Specialize to d=3 and diagonal B with distinct eigenvalues. Write V for the
off-diagonal matrices. Suppose C_A intersect V is one-dimensional, spanned
by a nonzero K. Then

    rank(L_A L_B) = rank(L_B L_A) = 5,
    rank(L_A L_B L_A) = 4 if tr(K (L_B|V)^(-1) K)=0,
                              5 otherwise.

Here (L_B|V)^(-1) K denotes the inverse linear operator applied to K;
there is no matrix inverse of K.

Proof. Diagonal projection pi_V maps U_A onto the hyperplane in V
annihilated by K. Indeed its annihilator in V is U_A^perp intersect V
= C_A intersect V. Hence L_B(U_A) is the five-dimensional hyperplane

    {Y in V : tr(K (L_B|V)^(-1) Y)=0}.

Its intersection with ker L_A=C_A can only be the line kK or zero.
The line occurs exactly when the displayed weighted pairing vanishes.
Rank-nullity proves the formula. The adjacent rank formulas follow from
the same dimension computation. This proof works over k itself; no split
eigenbasis for A is needed.

## Explicit public family

Take the fixed matrix and the one-parameter diagonal matrix

    A = [[0,1,1],[1,0,1],[1,2,0]],    B_t=diag(0,1,t).

The characteristic polynomial of A is x^3-4x-3 and has discriminant 13.
For primes other than 13 it is squarefree. Its centralizer is
span(I,A,A^2). The diagonal of A is zero and diag(A^2)=(2,3,3).
Thus C_A intersect V=kA over every field: the diagonal equations for
alpha I+beta A+gamma A^2 force alpha=gamma=0.

Assume an odd prime ell divides N, ell!=13, A has collision-free N-th
powers modulo ell, and t, t-1, t^N-1 are nonzero modulo ell. Then B also
has collision-free N-th powers. Set u=t^(N-1). The three pair weights of
L_B are

    w12=1,  w13=u,  w23=(tu-1)/(t-1).

The opposite-entry products of A are 1, 1, 2. Therefore

    tr(A (L_B|V)^(-1) A)
       = 2[1 + 1/u + 2(t-1)/(tu-1)]
       = 2 F_N(t) / [u(tu-1)],

    F_N(t) = t u^2 + 3(t-1)u - 1
           = t^(2N-1) + 3t^N - 3t^(N-1) - 1.

The triple derivative has rank 4 exactly when F_N(t)=0, and otherwise
rank 5. This is an exact scalar reduction, not a requirement to materialize
a 9-by-9 operator in a factoring algorithm.

## Unpowered comparisons

For P_A P_B P_A the pairing is tr(A^2)=8, so its rank is 5 at every odd
prime in the stated squarefree branch. For ad_A ad_B ad_A, the pairing is
tr(A (ad_B|V)^(-1) A)=0: the (i,j) and (j,i) terms have opposite
denominators and equal numerators. Thus that triple has rank 4 throughout
the branch. Neither unpowered triple distinguishes the two primes in the
certificate below.

The derivative construction is nevertheless a scalar power-residue test.
It introduces a quadratic relation in u rather than the usual u=1 test.
For units satisfying u=1, F_N(t)=4(t-1), which cannot vanish on the
admissible odd-prime branch. In particular this fixed family supplies no
new admissible split on Carmichael inputs, where u=1 for every unit at
every prime divisor. That is a scoped failure of this family, not of joint
operators in general.

## Exact finite witness

The retained Python source builds each derivative directly from the
upper-right block of [[A,H],[0,A]]^N for each matrix unit H. It computes
field ranks independently of the scalar formula. Factors are offline
labels, not inputs used to select the public family or exponent.

For N=77 and t=3, u=25 modulo 77 and F_N(t)=22 modulo 77:

| Field | rank L_A | rank L_B | rank L_A L_B | rank L_B L_A | rank L_A L_B L_A |
| --- | ---: | ---: | ---: | ---: | ---: |
| F_7 | 6 | 6 | 5 | 5 | 5 |
| F_11 | 6 | 6 | 5 | 5 | 4 |

Thus gcd(F_N(3),77)=11. This witness also has gcd(u-1,77)=1 and
t^((N-1)/2)=9 modulo 77, with both gcd(9-1,77)=gcd(9+1,77)=1.
It is not an ordinary single-step Fermat/Euler plus-or-minus gcd on this
base. This comparison does not claim that standard factoring methods fail
on 77 or that this congruence has a favorable asymptotic success law.

## Public test, cost, and missing success law

For each publicly chosen t, first compute gcd(t(t-1),N), then
u=t^(N-1) mod N and gcd(tu-1,N). Any proper gcd is already a verified
divisor. On the unit-screened branch compute gcd(F_N(t),N). This needs
O(log N) modular multiplications, O(1) n-bit residues, and gcd work
polynomial in n=ceil(log2(N+1)). The fixed A is explanatory; the scalar
implementation need not test its collision condition to obtain a correct
divisor. That condition is required only for the rank interpretation.

For a uniform independent sampler, the missing statement is a uniform
inverse-quasipolynomial lower bound on the fraction of t modulo each
input N producing a proper gcd, or an explicit quasipolynomial-size
structured list with such a hit. The Carmichael observation prevents this
particular screened F_N family from serving as the only all-input unit
test. No such lower bound or covering list is established even on distinct
prime semiprimes. The finite witness does not supply one.

## Resource and verification record

The root supplied a fresh machine snapshot: load about 2, memory available
72%, no swap, and no numerical job running. The pilot budget was <60 s
and <512 MB; the source enforces a 50-second loop deadline. Matrices have
dimension at most 9, and the completed run took about 0.01 s. Source:
`pilot.py`; exact output: `pilot.json`. No shared records, catalogs, or Git
history were changed by this worker.
