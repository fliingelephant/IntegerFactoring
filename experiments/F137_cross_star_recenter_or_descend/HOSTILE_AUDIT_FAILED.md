# F137 hostile audit — failed on canonical-generation scope

## Verdict

**FAIL as written.** The divisor-carry identity, recentering equality, overlap
bound, descent inequality, two-step contraction, path bound, and the
(N=143) arithmetic certificate are correct. However, the setup does not
imply the advertised application to one complete adaptive generation.

In particular, it does not require the parent value to have a canonical
anchored endpoint presentation, and it does not require the released block
to be small enough for the next anchored star. Thus the displayed
(H'_b=t+bN) are formal congruence cofactors under the written hypotheses;
they need not be relations that the canonical source can emit. The exact
duplicate also needs the P120 endpoint-screen qualification.

Audited frozen hashes:

- `STATEMENT.md`:
  `d18726e36df19bfc3420854cda69f04c51ed862a92223acb93097bcb1ffb9e03`
- `PROOF.md`:
  `03decbc64d249b1ed5cab4e3085c97294fd99bfd3e4c0ecf24cc26d6c4e88609`

No `HOSTILE_AUDIT.md` pass report was created.

## 1. The exact arithmetic core passes

From

\[
r(qS)=1+KN
\]

and the division (qS=jN+t), one has (1\le t<N) and

\[
rt\equiv1\pmod N.
\]

All factors of (H=Sr) are units modulo (N), so inverse uniqueness gives

\[
t=\iota_N(r).
\]

Writing (rt=1+k_rN) gives

\[
K=jr+k_r,
\qquad
1\le k_r<r.
\]

Hence (j=\lfloor K/r\rfloor) and (k_r=K\bmod r). Also,

\[
qS=t+jN=H'_j.
\]

Because (qS) is a unit modulo (N), for (b\ne j),

\[
\gcd(qS,H'_b)
=\gcd(qS,N(b-j))
=\gcd(qS,b-j)
\le |b-j|.
\]

Thus the claimed equality, not only its upper bound, is correct. If
(j<C), this gives the strict bound below (C). If (j\ge C), then

\[
K=k+Aq<Cq,
\qquad
Cr\le jr<K,
\]

so (r<q). The unit assumptions used in these deductions are sufficient.

## 2. First scope failure: the parent need not be canonical

The setup calls (V=qSr) an old parent relation and the introduction says
that (r) was released from an anchored arm. The written hypotheses do not
state the anchor or require a canonical endpoint presentation.

Take

\[
N=9,
\quad C=3,
\quad q=4,
\quad w=7,
\quad k=3,
\quad A=2.
\]

Then

\[
qw=28=1+3N,
\qquad
H=w+AN=25=5\cdot5.
\]

Choose (r=5) and (S=5). Every displayed setup condition holds, but

\[
V=qSr=100>N^2=81.
\]

A canonical inverse value is a product of two integers in
({1,\ldots,N-1}), so it is strictly less than (N^2). Therefore this
(V) cannot be a retained canonical inverse value at all. The formal
identities remain true, but the advertised parent-arm interpretation does
not follow from the statement.

For the operational version, the statement must either assume an actual
anchor (ell) and a canonical presentation

\[
V=(\ell q)(H/\ell),
\qquad
\ell q<N,
\qquad
H/\ell<N,
\]

or remove the claims about an old anchored relation and state the result as
a formal divisor-carry lemma.

## 3. Second scope failure: the child star need not exist

The only size condition on the released block is (r<N). This is not enough
to apply the bounded-anchor source to (r).

Take

\[
N=15,
\quad C=2,
\quad q=2,
\quad w=8,
\quad k=1,
\quad A=0,
\quad H=8=1\cdot8.
\]

Thus (S=1,r=8) satisfies the full setup. But

\[
r=8>N/C=7.5.
\]

No nontrivial anchor (a\le C) has (ar<N): already (2r=16>N).
The formal child cofactor at (b=1) is

\[
H'_1=2+15=17,
\]

but (rH'_1=136\equiv1\pmod {15}) is not the canonical value of any
unwrapped bounded-anchor arm based at (r). Therefore the theorem does not,
under its current assumptions, analyze one complete generated child star.

For the full-star interpretation, add (r<N/C). More generally, state the
result only for each actually realized child anchor (a), with

\[
a\mid H'_b,
\qquad ar<N,
\qquad H'_b/a<N.
\]

Not every formal digit (b\in[0,C)) must occur in the source. The word
“virtual” correctly allows (b=j) to be absent, but the present
“one complete adaptive generation” claim does not make this distinction
precise.

## 4. Duplicate value does not mean an inert occurrence

The equality at (b=j) is correct:

\[
rH'_j=rqS=V.
\]

However, if an actual child anchor realizes this digit, it can give a new
canonical endpoint presentation of the old exact value. P120/X73 requires
both endpoint sign screens before exact-value deletion.

An exact example is

\[
N=15,
\quad C=2,
\quad q=w=r=4,
\quad A=0,
\quad S=1,
\quad j=0,
\quad t=4.
\]

The parent presentation ((4,4)) has exact value (16). The child anchor
(a=2) realizes the same digit and gives the distinct canonical
presentation

\[
(ar,H'_0/a)=(8,2),
\qquad
8\cdot2=16.
\]

It immediately factors:

\[
\gcd(8-2,15)=3,
\qquad
\gcd(8+2,15)=5.
\]

The statement says “old exact value,” not “inert,” so the equality itself is
safe. But the concluding sentence that the simplest one-generation hope is
closed needs an explicit no-factor branch and must preserve all new endpoint
presentations before exact-value deduplication.

## 5. Two-step contraction and path length pass

For a large-quotient transition (q_0\to q_1), let
(delta=q_0-q_1>0). The next carry satisfies

\[
k_1<C\delta.
\]

If (delta\ge q_0/(C+1)), then already
(q_1\le Cq_0/(C+1)), and the second large transition makes (q_2<q_1).
Otherwise, using its digit (A_1\le C-1),

\[
Cq_2\le j_1q_2<k_1+A_1q_1
<C\delta+(C-1)q_1.
\]

Substitution of (q_1=q_0-\delta) gives exactly

\[
q_2<\frac{C}{C+1}q_0.
\]

Pairing the transitions in an all-large path gives
(O(C\log N)) steps because

\[
\log(1+1/C)\ge1/(C+1).
\]

This is only pathwise, as stated. It does not bound a branching transcript
or a path in which small-quotient steps alternate with large ones.

As an additional finite check, exact enumeration over
(3\le N\le300), (2\le C\le9), all unit (q), all digits, and all
admissible divisors checked 4,022,645 one-step transitions and 12,444,682
consecutive large-quotient pairs. No arithmetic counterexample occurred.
The proof above, not this finite check, establishes the identities.

## 6. The (N=143) certificate passes

Direct calculation gives

\[
28\cdot46=1+9\cdot143.
\]

At (A=1),

\[
H=189=27\cdot7,
\quad K=37,
\quad 28\cdot27=5\cdot143+41,
\quad 7\cdot41=1+2\cdot143.
\]

At (A=3),

\[
H=475=25\cdot19,
\quad K=93,
\quad 28\cdot25=4\cdot143+128,
\quad 19\cdot128=1+17\cdot143.
\]

Thus all stated quotients, inverses, carry remainders, branch labels, and
the duplicate value (19\cdot700=1+93\cdot143) are correct. In fact, the
parent arms can be made canonical using anchors (3) and (5), and the
small-quotient duplicate can use child anchor (5). The certificate is
stronger than the general hypotheses, but it does not repair their missing
canonicality conditions.

## 7. Prior-result and novelty boundary

The formula

\[
k_r=K\bmod r

\]

is already the divisor-carry law of P70/P80. The recentering equation
(qS=t+jN) is the corresponding exact quotient decomposition. The material
increment in F137 is narrower: it compares the parent complement with the
other formal child cofactors and proves the two-consecutive-large-quotient
contraction.

The candidate cites P80, but describes it only as a bounded state-scan
boundary. A corrected novelty paragraph should say explicitly that
Theorem 1 specializes the promoted divisor-carry law. It may claim the
cross-star overlap interpretation and quantitative two-step contraction as
the new internal result. It must not claim a publication-level novelty
result without a literature review.

The consequence “for (C=n^3), this is (O(n^4))” also uses an undefined
(n). If it is retained in this self-contained statement, define, for
example,

\[
n=\lceil\log_2(N+1)\rceil.
\]

## Required repairs before a fresh hostile audit

Choose one of these two scopes.

1. **Formal lemma:** Keep the current broad algebraic hypotheses. Replace
   the parent-arm and complete-generation language by formal cofactor
   geometry. State that only actually generated child digits inherit the
   overlap result.
2. **Operational feedback theorem:** Add hypotheses that certify a retained
   canonical parent arm. Add (r<N/C), or explicitly quantify only child
   anchors whose two endpoints are canonical. Preserve endpoint
   presentations and run their sign screens before deleting duplicate exact
   values.

In both versions, attribute the (K\bmod r) law to P70/P80, restrict the
new claim to the recenter/overlap and contraction consequences, and define
(n). Freeze new hashes and run a fresh whole-proof hostile audit.

