# F292 continuation: conductor descent with the cap retained

Status: author-derived exact identities and finite verification; no fast
low-row contractor or independently verified new theorem is claimed.

## Source mechanism inspected

The local full text of Milicevic--Zhang, *Sums of products of Kloosterman sums
to prime power moduli*, arXiv:2608.21346, was inspected after the initial F292
mechanism was formulated. The actual statements used as inspiration are:

- Lemma2.1: stationary cancellation is on translation-invariant domains.
- Proposition5.3: the allowed weight is invariant under a specified additive
  subgroup. An ordinary short cap does not automatically satisfy this.
- Lemma5.4: a bounded initial list of inverse-half-power sums controls the
  later Taylor coefficients, through symmetric-polynomial recurrences.

The displayed equations were checked in the extracted formula images,
including (5.1)--(5.3) and Proposition5.3. The paper assumes an odd prime.
No modulus-two theorem is imported. The elementary dyadic identities below
are derived separately. The recurrence idea, rather than a cancellation bound
for a completed domain, is the part investigated here.

Source: [arXiv:2608.21346](https://arxiv.org/abs/2608.21346), citation key
`milicevic_2026_sums`; cached full text and provenance are listed in
`reference_arxiv_2608_21346/SOURCE_MANIFEST.json`.

## A closed twisted-window lift

Fix M=2^R and the primitive even character psi on its units with
psi(5)=exp(2*pi*i/2^(R-2)). For m<=R define

    F[m,e;W] = sum_{u odd<2^m} psi(u*v/N)^e W(u,v),
    v=N/u mod2^m, with the canonical representative 0<=v<2^m.

Here character arguments use inverses modulo M, including N inverse. The
weight may be complex. Put L=2^(m-1), K=M/L, and W_ij(u,v)=W(u+iL,v+jL).
For a lower-level graph pair, define

    A_ij(u,v)=psi(1+iL/u)^e psi(1+jL/v)^e.

Then, for m>=3,

    F[m,e;W]
      = 1/2 sum_{i,j in{0,1}}
          (F[m-1,e; A_ij W_ij]
            +(-1)^(i+j) F[m-1,e+2^(R-m); A_ij W_ij]).

Proof: the permissible lift parity is i+j=c mod2, with
c=(N-uv)/L mod2. Its indicator is(1+(-1)^(i+j)chi)/2. The lower-pair
carry character is exactly chi=psi(uv/N)^(2^(R-m)). Multiplication by the
lift ratios gives the displayed identity. In particular the second exponent
increment does not alter A_ij: that multiplier still uses the original e.

When L^2 is divisible by M, the lift multiplier is an additive linear phase.
Define odd beta modulo K by psi(1+L)=exp(2*pi*i*beta/K). Then

    A_ij(u,v)=exp(2*pi*i*e*beta*N^(-1)*(i*v+j*u)/K).

Indeed (1+La)(1+Lb)=1+L(a+b) mod M, and 1/u=v/N mod K since K divides L.
Thus the class consisting of a translated geometric window times an additive
linear phase stays closed under the lift. No new inverse or square-root phase
has to be represented at these levels. Constants from translating a preexisting
linear phase can be carried as scalars.

## Jump directly to the geometric scale

Choose q=2^s with q^2 divisible by M and write H=M/q. For each odd u<q let
v=N/u mod q. Keep the actual high blocks X,Y and define

    D_XY(u)=(uv-N)/q+X*v+Y*u mod H,
    W_XY(u,v)=W(u+qX,v+qY).

The exact count on the full graph is

    C_W = (1/H) sum_{e=0}^{H-1} sum_{X,Y}
               sum_{u odd<q} W_XY(u,v)
                 exp(2*pi*i*e*N^(-1)*D_XY(u)/H).

The q*X*Y term in the product quotient vanishes modulo H. The unit multiplying
e can be chosen as written because multiplication by that unit permutes the
complete character list. Each block term is a base character twist multiplied
by a linear phase in u,v. All real inequalities in W are kept exactly.

This jump groups the recursively generated terms into H times the number of
geometric high blocks; it avoids separately retaining eight formal children
per lift. For a balanced short cap and q approximately sqrt(M), there are
O(1) blocks and H=O(sqrt(M)) character states. Alternatively take q strictly
larger than both possible cap coordinates. There is then only block(0,0).
This gives an explicit quantified recurrence, but it is not a quasipolynomial
state bound. Direct construction still scans the admissible low residues.

## Exact pilot and the two separating caps

`conductor_descent.py` uses integer cyclotomic coefficient vectors, not
floating-point equality. It verified132 complete twisted-window recurrences
and120576 linear-multiplier identities. It also verified62 public short caps:
the two retained F290 inputs plus a seeded random family with R=10,12,14,16,18,
N uniform among odd integers in[8M,16M), seed2922608. The normal is always the
public menu member(a,b)=(64+N mod8,65), with
T=floor(1.01*sqrt(4abN)). No factor label selects a query.

At N=12827 versus12851, M=1024, q=256, H=4, the carry polynomials are2 and0.
The exact projection returns the respective cap counts2 and0. At
N=2563051, M=262144, q=2048, H=128, the retained carry polynomial is2*z^7.
All128 twisted values are distinct while the exact projected count is0.
This refutes equality-based merging of those states, not recurrence-based
compression: the latter example in fact has a first-order recurrence.

## A constructive formal compression of the twist sequence

With one high block define the nonnegative carry histogram n_c and

    G_e=sum_c n_c*zeta^(e*c), zeta=exp(2*pi*i/H).

If K distinct carries occur, the polynomial

    A(t)=product_{c:n_c!=0}(t-zeta^c)

gives an exact order-K linear recurrence for G_e. This follows by multiplying
each geometric sequence by its annihilating factor and summing. It is the
finite power-sum recurrence mechanism suggested by the paper. Distinct twist
values therefore do not alone measure the necessary representation size.

There is an integer version avoiding root-of-unity field assumptions:

    mu_j=sum_c n_c*c^j, P(t)=product_{c:n_c!=0}(t-c).

If P(t)=sum_{i=0}^K p_i*t^i, then
sum_i p_i*mu_(j+i)=0 for every j>=0. Once the support is known, the polynomial
product over nonzero c of(1-t/c) gives the weight n_0 by a linear combination
of these moments. Constructing the support or the requisite moments without
scanning low rows remains unresolved. The formal recurrence is not being
treated as an evaluation oracle. Cyclotomic coefficients also require a bit
representation; their degree can be H/2, so a short list of algebraic scalars
does not by itself imply a short bit representation.

`carry_support_scaling.py` tests this integer recurrence exactly for16 seeded
public caps, seed2922609. It verifies four consecutive recurrence identities
per case. The observed occupied-carry counts were:

| R | H range | Four observed recurrence degrees |
|---:|---:|---:|
|18|64--128|1,0,1,2|
|22|256|2,2,2,3|
|26|1024--2048|23,27,9,23|
|30|4096--8192|78,65,101,72|

The largest integer recurrence coefficient in the pilot had915 bits. The
support is much smaller than H here, but visibly grows in this finite family.
No asymptotic law, all-input degree bound, or lower bound against another
representation follows. The public cap range gives only the unconditional
bound K<=1+floor((T^2/(4ab)-N)/q), which is O(sqrt(M)) at this scale.

## Outcome

The new useful identity is the exact conductor descent with linear additive
lift phases and intact windows. It gives a direct H-by-block contraction
instead of an ungrouped lift tree. A second formal compression replaces H
twists by an order-K moment recurrence. The remaining constructive question
is to obtain that recurrence or its needed moments from the public cap without
forming its low rows. Neither a complete-sum cancellation theorem nor equality
of a few twists supplies this step.

Resource check before these pilots: load1.99/2.07/2.07, memory_pressure73% free,
no swap. Same read-only process inspection succeeded with approval; one Apple
process occupied a core. Each script has a30-second timeout, estimated peak
memory below64MiB. Recorded runtimes were0.094s and0.036s. Sources, exact JSON
outputs, and logs are retained beside this note.
