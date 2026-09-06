# F279 draft algebra — canonical biased Rédei power-coset sources

## Status and exact scope

F279 is an unfrozen theory and search-design draft. It studies the clean
two-mode lane left open by P228/F278. It does not contain source code, a
runner, a frozen packet, a computation, or empirical evidence.

The exact endpoint is

\[
 N=pq,\qquad p<q<2p,\qquad B=\lfloor\sqrt N\rfloor=p+s,
\tag{1}
\]

where `p` and `q` are distinct odd primes. Put

\[
 h=q-B.
\tag{2}
\]

The branch `s=0` is already factored by `gcd(B,N)`. The unresolved branch
has `s>0`, `h>0`, and `B` is a unit modulo both hidden primes.

The draft has two purposes.

1. It gives a complete clean three-parameter normal form for every scalar
   two-mode observable of a public `2 by 2` constant matrix power.
2. It isolates one search-worthy source class: a canonical biased public
   source-target pair that is not a known orbit target, a bounded-torsion
   phase, a direct input gcd, or a near-square ticket.

The matrix representation is not itself the new mechanism. The only open
mechanism is correlation in the public target coset.

## 1. General scalar two-mode normal form

Let

\[
 C\in M_2(\mathbb Z/N\mathbb Z)
\]

be public, and let `L` be a public scalar linear functional on matrices.
Define

\[
 t=\operatorname{tr}C,\qquad
 \delta=\det C,\qquad
 \eta=t^2-4\delta,
\tag{3}
\]

and

\[
 A=L(C),\qquad e=L(I),\qquad
 H=A^2-Aet+e^2\delta.
\tag{4}
\]

The last scalar is the public invariant

\[
 H=\det(AI-eC).
\tag{5}
\]

Before a clean two-mode interpretation, the algorithm must gcd-screen
`delta`, `eta`, `e`, and `H`. A proper gcd is already a factor. A zero value
in both CRT components is a degenerate branch and is not a clean
power-coset candidate. The case `e=0 mod N` is retained separately below;
it is the ordinary powered-collision target.

Work in the quadratic étale algebra

\[
 E_N=(\mathbb Z/N\mathbb Z)[w]/(w^2-\eta).
\tag{6}
\]

When `2 delta eta` is a unit, the two roots of the characteristic
polynomial are

\[
 \alpha={t+w\over2},\qquad \beta={t-w\over2}.
\tag{7}
\]

For every `k>=0`, define `P_k,Q_k` without division by

\[
 (t+w)^k=P_k+Q_kw.
\tag{8}
\]

Equivalently,

\[
 \begin{pmatrix}P_{k+1}\\Q_{k+1}\end{pmatrix}
 =
 \begin{pmatrix}t&\eta\\1&t\end{pmatrix}
 \begin{pmatrix}P_k\\Q_k\end{pmatrix},
 \qquad (P_0,Q_0)=(1,0).
\tag{9}
\]

Binary powering evaluates `(P_B,Q_B)` in `O(log B)` multiplications in
`Z/NZ`.

Introduce the homogeneous public target

\[
 V=et-2A,\qquad W=e.
\tag{10}
\]

It obeys the exact identity

\[
 V^2-\eta W^2=4H.
\tag{11}
\]

The target is therefore disjoint from both local eigenlines exactly on the
clean `H`-unit branch.

### Theorem 1 — exact endpoint identity

Under the clean unit hypotheses,

\[
 \boxed{
 L(C^B)=2^{-B}(WP_B-VQ_B).
 }
\tag{12}
\]

This identity also covers `e=0`. In that case `W=0`, `V=-2A`, and

\[
 L(C^B)=A\,2^{1-B}Q_B.
\tag{13}
\]

Thus the `e=0` branch is exactly the `Q_B=0` powered-collision branch of
P228.

To prove (12), the standard two-root formula gives

\[
 L(C^B)=
 { (A-e\beta)\alpha^B-(A-e\alpha)\beta^B\over\alpha-\beta}.
\tag{14}
\]

Substitute (7), (8), and (10). The numerator simplifies to

\[
 2^{-B}w(WP_B-VQ_B),
\]

and `alpha-beta=w`. No local division by a possible zero divisor is used
in the executable form (12).

## 2. Rédei power-coset form

On a clean local field `F_r`, where `r` is `p` or `q`, define

\[
 z_r={t+w\over t-w}.
\tag{15}
\]

For a clean homogeneous target `[V:W]`, define

\[
 \lambda_r={V+Ww\over V-Ww}.
\tag{16}
\]

Both denominators are units because their norms are respectively
`t^2-eta=4 delta` and `V^2-eta W^2=4H`.

Equations (8), (15), and (16) give

\[
 z_r^B={P_B+Q_Bw\over P_B-Q_Bw}.
\tag{17}
\]

Cross multiplication in (16)-(17) gives the exact equivalence

\[
 \boxed{
 WP_B-VQ_B=0\pmod r
 \iff z_r^B=\lambda_r.
 }
\tag{18}
\]

The conjugation `w -> -w` sends both `z_r` and `lambda_r` to their
inverses. Therefore

\[
 y_r=z_r^B\lambda_r^{-1}
\tag{19}
\]

is one explicit norm-one-torus word, and a scalar two-mode cancellation is
exactly the local identity `y_r=1`.

This is a power-coset condition. It is not necessarily the powered
collision `z_r^B=1`.

## 3. Local residual exponents

Let

\[
 \chi_r=\left({\eta\over r}\right)\in\{1,-1\}.
\tag{20}
\]

The local norm-one torus is cyclic of order

\[
 m_r=r-\chi_r.
\tag{21}
\]

The Frobenius law is

\[
 z_r^r=z_r^{\chi_r}.
\tag{22}
\]

At the smaller prime, `B=p+s`, so

\[
 \boxed{z_p^B=\lambda_p
 \iff z_p^{s+\chi_p}=\lambda_p.}
\tag{23}
\]

At the larger prime, `B=q-h`, so

\[
 \boxed{z_q^B=\lambda_q
 \iff z_q^{\chi_q-h}=\lambda_q.}
\tag{24}
\]

Thus a proper endpoint gcd is an exclusive hit in two hidden cyclic
groups. P228 removes the target `1`; F279 asks whether a canonical biased
public target can orient another coset.

## 4. Complete literal diagonal chart

Assume first that `e` is a unit. Scale `[V:W]` to the affine chart
`[v:1]`, where

\[
 v=V/W=t-2A/e.
\tag{25}
\]

Every clean triple `(t,eta,v)` is realized by the public matrix

\[
 C(t,\eta,v)=
 \begin{pmatrix}
 (t-v)/2 & 1\\
 (\eta-v^2)/4 & (t+v)/2
 \end{pmatrix}.
\tag{26}
\]

Indeed,

\[
 \operatorname{tr}C=t,\qquad
 \det C={t^2-\eta\over4},\qquad
 \operatorname{Disc}(\chi_C)=\eta.
\tag{27}
\]

For the upper-left coordinate `L(X)=X_11`, one has

\[
 A=(t-v)/2,\qquad e=1,
\]

and hence

\[
 \boxed{
 (C(t,\eta,v)^B)_{11}=2^{-B}(P_B-vQ_B).
 }
\tag{28}
\]

The coefficient invariant is

\[
 H={v^2-\eta\over4}=-bc.
\tag{29}
\]

Conversely, for an arbitrary matrix

\[
 C=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]

the upper-left coordinate has

\[
 t=a+d,\qquad v=d-a,\qquad
 \eta=(a-d)^2+4bc,qquad H=-bc.
\tag{30}
\]

Therefore (26) is not a special example. It is a complete clean chart for
every literal diagonal two-mode coordinate. The other diagonal coordinate
uses `v=a-d`. An off-diagonal coordinate has `e=0` and returns to (13).

Projectively, `(C^B)_11=0` says that `C^B` sends the first coordinate line
to the second coordinate line. Equation (18) is the same orbit-hitting
condition in eigenline coordinates.

## 5. Exact orbit and phase decoys

For one fixed `eta`, use the pair law

\[
 (R,S)\star(R',S')
 = (RR'+\eta SS',\ RS'+SR').
\tag{31}
\]

The pair `(R,S)` represents

\[
 \Phi(R,S)={R+Sw\over R-Sw}.
\tag{32}
\]

Conjugation sends `(R,S)` to `(R,-S)`. Equality of two clean represented
elements is the division-free determinant condition

\[
 \Phi(R,S)=\Phi(R',S')
 \iff RS'-SR'=0.
\tag{33}
\]

The source power `z^k` is represented by `(P_k(t,eta),Q_k(t,eta))`.
The affine target `lambda(v)` is represented by `(v,1)`.

### Known orbit targets

If

\[
 P_e(t,\eta)-vQ_e(t,\eta)=0,
\tag{34}
\]

then `lambda=z^e`, and (18) reduces to

\[
 z^{B-e}=1.
\tag{35}
\]

For negative `e`, equation (34) becomes

\[
 P_{|e|}(t,\eta)+vQ_{|e|}(t,\eta)=0.
\tag{36}
\]

A one-prime equality in (34) or (36) is already exposed by its gcd. A
global equality is an ordinary or torus order ticket. It is not a new
power-coset source.

### Bounded target torsion

Let

\[
 (R_m,S_m)=(P_m(v,\eta),Q_m(v,\eta)).
\]

Then

\[
 \lambda(v)^m=1\iff S_m=0.
\tag{37}
\]

If this relation holds at only one prime, `gcd(S_m,N)` already factors. If
it holds globally, an endpoint hit is a phase inside a public group of
known bounded exponent. It belongs to a factor-first finite-torsion or
Miller-style phase check.

### Power times bounded torsion

More generally, suppose

\[
 \lambda=z^e\mu,\qquad \mu^m=1.
\tag{38}
\]

This is equivalent to

\[
 \lambda^m=z^{em}.
\tag{39}

Both sides of (39) have explicit pairs from (31). Their determinant in
(33) is a public direct screen. A one-prime zero factors before the remote
endpoint. A global zero turns an endpoint hit into

\[
 z^{B-e}=\mu,
\qquad
 z^{m(B-e)}=1.
\tag{40}

The first equality is a known finite phase of the verified return in the
second equality. It is not counted as a new free-coset hit.

The hostile F278 example has equal diagonal entries. In (30), this gives
`v=0`, hence `lambda=-1`. Its cancellation is exactly the order-two phase
`z^B=-1`, followed by `z^{2B}=1`. It proves that target `1` is not the only
two-mode cancellation. It does not witness a free target coset.

## 6. Exact unbiased-target boundary

Fix a clean local source `(t,eta)`. The Cayley map

\[
 [V:W]\longmapsto {V+Ww\over V-Ww}
\tag{41}
\]

is a bijection from clean projective target lines to the local norm-one
torus.

- If `eta` is nonsquare, every line of `P^1(F_r)` is clean, and both sets
  have `r+1` elements.
- If `eta` is square, the two eigenlines are removed by
  `V^2-eta W^2=0`. The remaining `r-1` lines map bijectively to the split
  torus of order `r-1`.

Consequently an independent uniform clean target has the exact hit law

\[
 \boxed{
 \Pr(z_r^B=\lambda_r)={1\over r-\chi_r}.
 }
\tag{42}

For CRT-independent accepted targets, the proper-gcd probability is

\[
 {1\over m_p}+{1\over m_q}-{2\over m_pm_q}.
\tag{43}

On balanced inputs, a numerical-quasipolynomial number of such independent
targets has exponentially small total hit probability. This exact boundary
is consistent with P212. It does not cover a canonical biased target.

## 7. Frozen draft source grammar

The proposed search does not enumerate arbitrary matrices. It uses the
complete chart (26) and one small public integer grammar.

Let

\[
 \mathcal C=\{-4,-3,-2,-1,0,1,2,3,4\}.
\tag{44}
\]

For each `c` in `C`, define the positive shifted center

\[
 x_c=B+c,
\tag{45}
\]

the Euclidean quotient and remainder

\[
 d_c=\lfloor N/x_c\rfloor,\qquad
 r_c=N-x_cd_c,
\tag{46}
\]

and, after the direct screen `gcd(x_c,N)=1`, the least positive inverse and
its exact inverse quotient

\[
 1\le u_c<N,qquad x_cu_c=1+k_cN.
\tag{47}
\]

Every one of `x_c,d_c,r_c,u_c,k_c` is gcd-screened with `N` before it is
used. A proper gcd is a direct factor and removes the row from source
discovery.

Define the ten signed residue expressions

\[
 \mathcal E_c=
 \{[\pm x_c]_N,[\pm d_c]_N,[\pm r_c]_N,
   [\pm u_c]_N,[\pm k_c]_N\}.
\tag{48}
\]

For one source anchor `c`, choose

\[
 t,\eta\in\mathcal E_c.
\tag{49}
\]

Choose a target anchor `c'` with

\[
 c'\in\mathcal C,\qquad |c'-c|\le1,
\tag{50}
\]

and choose

\[
 v\in\mathcal E_{c'}.
\tag{51}
\]

There are exactly

\[
 10^2\bigl(2\cdot20+7\cdot30\bigr)=25{,}000
\tag{52}
\]

named candidates and exactly `9*10^2=900` named source pairs. Candidate
names include every anchor, atom type, and sign. No coefficient, shift,
target, or expression is learned from a factor label or from discovery
outcomes.

The quotient, remainder, inverse, and inverse quotient in (46)-(47) are
formed as canonical integers before reduction modulo `N`. This is the
intended biased source. The grammar contains no Rédei power operation, no
hidden prime, no local character, and no endpoint value in a target
expression.

Equations (34)-(40) are mandatory decoy checks. A numerical coincidence
with a bounded orbit or phase is not promoted merely because its syntax did
not state that relation.

## 8. Separate high-order diagnostic source

The ranked grammar does not use a large-order constructor. One small
diagnostic subset may use this elementary bounded scan.

Put

\[
 D_0=n=\lceil\log_2(N+1)\rceil,
 \qquad A_0=D_0^2+D_0.
\tag{53}
\]

For `2<=a<=A_0`, gcd-screen `a`, then compute the incremental powers
`a^e mod N` for `1<=e<=D_0` and screen every `gcd(a^e-1,N)`.

- A proper gcd is a direct diagnostic factor exit.
- A saturated gcd rejects that base.
- If every gcd is one, retain the first such `z=a`. Its local orders are
  both greater than `D_0` by construction.
- If the cap is exhausted, record `shortfall`. Do not substitute another
  constructor.

On a retained base, screen `gcd(z-1,N)` and define the globally split chart

\[
 \eta=1,qquad t={z+1\over z-1}\pmod N.
\tag{54}
\]

Then

\[
 {t+1\over t-1}=z.
\tag{55}

This diagnostic excludes local source order at most `n`. It does not claim
that a high-order source is correlated with any canonical target. It is not
ranked, and it cannot enlarge or replace the 25,000-candidate grammar.

## 9. Evidence boundary and exact nonclaims

The proposed finite search can do only these jobs.

1. Find a repeated nondirect exclusive hit in a frozen canonical biased
   grammar.
2. Find an algebraic pattern that can be stated and proved separately.
3. Falsify a proposed identity or show that the frozen grammar has no
   held-out lead.

It cannot prove an inverse-quasipolynomial hit law, an all-input dispatcher,
or an integer-factoring theorem from finite rates.

F279 proves no:

1. lower bound for arbitrary matrices, recurrences, or torus words;
2. sparsity theorem for a deterministic canonical biased target;
3. classification of three-or-more-mode cancellation;
4. construction of a characteristic-dependent Frobenius operator;
5. claim that every target relation is an order relation; or
6. all-input factoring algorithm.

No experiment may run from this draft. The preregistration must be audited,
the C++ source and runner must be written later, a new immutable packet must
be frozen, and the containment workflow still requires the user's explicit
decision.
