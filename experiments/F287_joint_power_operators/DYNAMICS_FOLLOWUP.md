# F287 third cycle: larger counts, asymmetric h=2, and three-base batching

Status: new author-derived claims and exact finite certificates. Independent
reconstruction is pending. Earlier reports and data were not modified.

## The root-count-four pattern is false

`extended_counts.py` enumerated all 12,395 balanced prime pairs p<q<2p
with 5<=p<q<=1500. Pairs with gcd(p-1,q-1)=2 were processed first.
All 24,790 local root sets were checked for reciprocal closure and for
absence of local Fermat roots. Runtime was 6.72 seconds, under the
30-second/128-MB budget. The local count histogram for the original h=3
was:

| Count | Number of local fields |
| ---: | ---: |
| 0 | 15327 |
| 2 | 7422 |
| 4 | 1755 |
| 6 | 256 |
| 8 | 29 |
| 10 | 1 |

The first count above four occurs at (p,q)=(43,47), in F_43:
roots {2,10,13,22,25,31}, with orders {14,21,21,14,21,21}.
Here gcd(42,46)=2.

The maximum occurs at (383,643), in F_643, also with shared gcd 2:

    roots: 30,54,96,131,355,390,407,455,493,582
    orders:214,107,107,107,107,321,321,321,214,321
    inverse pairs: (30,493),(54,131),(96,355),(390,582),(407,455).

The other largest sets and exact orders are retained in
`extended_counts.json`. This is a finite maximum, not a universal bound.
Neither this data nor the earlier twin-prime formulas support a speed
claim over Fermat's difference-of-squares method on close factors.

## Which rational maps are monomial maps?

Over characteristic zero, consider

    R_h(v)=v(h-v)/(hv-1).

For h=1 the map cancels to -v; for h=-1 it cancels to v. For other h
it has degree two, fixed points 0,1,infinity, and fixed-point multipliers
(-h,-h,2/(1-h)). Comparison with the fixed-point multipliers of v^2
and v^(-2) shows that a member can be Möbius-conjugate to either of
these two degree-two monomials only at h=0 or h=2. Both occur.
This classification is only for conjugacy to degree-two monomials; it
is not a classification of all possible algebraic-group constructions.
Special finite characteristics can require separate treatment.

R_0(v)=v^2. At h=2, assume characteristic is neither 2 nor 3, and
let alpha,beta be the distinct roots of x^2-x+1. They satisfy
alpha+beta=alpha*beta=1. Put M(v)=(v-alpha)/(v-beta). Then

    M(R_2(v))=M(v)^(-2).

One proof is that R_2 swaps its two critical points alpha,beta, so its
conjugate has the form c/z^2; evaluation at v=infinity gives c=1.
The identity can also be checked directly using alpha^2=alpha-1.
It holds over the quadratic splitting extension, including nonsplit
finite-field cases.

This does NOT turn the F_2 test into an ordinary group power test.
Its actual transformed equation is

    M(t)=M(t^N)^(-2),

not M(t)=M(t)^(-2N). The original exponentiation remains in the
original coordinate. Conjugating both operations would deliberately
replace the test by an ordinary monomial condition. That would lose
the present noncommutation, not prove it irrelevant. For example in
F_17 at N=187,t=3, (1-t)^N=9 while 1-t^N=11.

One recognized order component remains: if t^r=t^(-1), clearing the
F_2 equation gives (1-t)(t^2-t+1)=0. At characteristic different from
2 and3 the admissible roots here have order6. This small-order part
should not be mistaken for a new large root source.

## h=2 has a regular asymmetric matrix realization

The symmetric A_2 construction is degenerate, but that is not a barrier
to the scalar h=2 correspondence. Take

    A=[[0,1,1],[1,0,1],[1,2,0]],
    C=[[0,1,1],[1,0,1],[1,0,0]],
    B=diag(0,1,t).

A and C have characteristic discriminants 13 and 5. Away from these
primes their centralizers intersect the off-diagonal subspace V in
span(A) and span(C), respectively. Suppose their N-th-power spectra
are collision-free and t(t-1)(t^N-1) is nonzero.

The original hyperplane argument now says L_B(im L_C) is the
five-dimensional subspace of V annihilated by the functional
Y -> tr(C (L_B|V)^(-1)Y). Its intersection with ker L_A is the line
span(A) exactly when tr(C (L_B|V)^(-1)A)=0. Therefore

    rank(L_A L_B L_C)=4 iff F_2(t)=0, otherwise5.

Both adjacent products have rank5 and all individual ranks are6.
Indeed the opposite-entry cross sums C_ij A_ji+C_ji A_ij are all2,
so the pairing is

    2[1+1/u+(t-1)/(tu-1)] = 2 F_2(t)/[u(tu-1)].

This is an asymmetric compression, not a repair to the singular A_2.
It changes the two outer centralizers while preserving a one-dimensional
intersection for each.

The full derivative certificate in `asymmetric_h2.json` has N=187,t=5,
u=60,F_2=153,gcd(F_2,N)=17. The individual ranks are6 and adjacent
ranks5 on both fields; the triple ranks are5 at11 and4 at17. The mutual
orders remain10 and16, outside both order-at-most-three exceptions.

## A structural three-base batch

R_2 commutes with v -> 1-v as well as v -> 1/v. These transformations
generate the six Möbius permutations of {0,1,infinity}. For a public
t with t(t-1) invertible, the orbit is

    t, 1/t, 1-t, 1/(1-t), t/(t-1), (t-1)/t.

Exponentiation by odd N commutes with inversion, and each F_2 root is
accompanied by its inverse. Thus the six orbit tests reduce exactly
to the following three bases:

    t, 1-t, t/(t-1).

This is a concrete batching operation suggested by the map symmetry.
The third power can be computed from the first two: if a=t^N and
b=(1-t)^N, then (t/(t-1))^N=-a/b. The batch therefore uses only two
modular exponentiations, plus modular inversions, arithmetic, and gcds.
Nonunit inversion denominators already give a factor when their gcd is
proper. Each batch remains polynomial in log N.

For a fair small comparison, `s3_batch.py` conditions on all three bases
passing the collision screens and all three Fermat gcds being1. At a
local prime each t gets a three-bit mask recording which F_2 equations
vanish. A global batch splits exactly when the two local masks differ.
The exact conditional probability is

    1 - sum_mask c_p(mask)c_q(mask)/(H_p H_q),

where H_ell counts the local screened values. This formula includes all
correlations between the three tests.

| p,q | Single-base splits / denominator | Three-base splits / same denominator |
| --- | --- | --- |
| 11,17 | 12/72 | 36/72 |
| 43,47 | 168/1596 | 336/1596 |
| 101,149 | 180/12420 | 540/12420 |
| 383,643 | 2268/241164 | 5292/241164 |
| 613,887 | 3528/536256 | 7056/536256 |
| 1259,1783 | 8556/2229612 | 20640/2229612 |

These are exact finite gains under a shared conditioning event. A
constant-size orbit cannot by itself establish a quasipolynomial success
law, and the results are not presented as such. The batch's savings is
three related tests from two powers, not a claim of dense local roots.

## Remaining structural question

The h=2 map is a monomial only after a coordinate change, while the
public N-th-power map stays in the original coordinate. That leaves a
specific noncommuting pair of inexpensive rational operations. Can a
publicly specified longer composition or orbit of this pair produce
many CRT-asymmetric fixed points with a provable success law, while
avoiding degree growth proportional to the enumerated orbit? The
three-base batch is the first exact finite operation in that direction.

This question remains open. The sparse fixed-parameter sampler does not
close the coupled source family, and no all-input claim is made.

## Resource record

Fresh local load was about2.1; the root reported74% memory available and
no swap I/O. The extended sweep used6.72 seconds; the asymmetric witness
used0.01 seconds. All new source and output names are separate from the
files being checkpointed by the record keeper. No shared catalogs,
records, or Git commits were changed by this worker.
