# F152 hostile audit — decorated squareclass split-or-section law

## Verdict

**PASS.** The frozen statement and proof are correct within their stated
proof-only scope. The decorated set is an abelian exponent-two group, the
projection gives the claimed short exact sequence, and an explicit relation
list satisfies the exact split-or-section dichotomy. The two-layer formula,
the P134 same-fibre specialization, and the `N=2773` illustration also check.

This is not a relation-source theorem and not a factoring algorithm. An
abstract section always exists. Progress needs a public source to produce two
incompatible lifts, or to make a common public section impossible for an
additional reason.

## Frozen inputs

- `STATEMENT.md`:
  `db35d6381867052c876b69111c7b5409030e117501cccec2be12c45c8642a4e4`
- `PROOF.md`:
  `6f7c113eaca89455a22ce3b5d791bc56b7fb98d3520564dbf0b412d56d0f4beb`

I read both files in full. I did not modify either frozen file or a durable
ledger.

## 1. Group law and exact sequence

For each coordinate and bits `a,b`,

\[
q^a q^b=q^{a\mathbin{\mathsf{xor}}b}q^{2ab}.
\]

Multiplying coordinates gives

\[
Q(v)Q(w)=Q(v+w)C(v,w)^2.
\]

Thus the product in (1) is closed. The coordinate identity

\[
ab+(a\mathbin{\mathsf{xor}}b)c
=bc+a(b\mathbin{\mathsf{xor}}c)
\]

proves the cocycle law and hence associativity. Symmetry gives
commutativity. Also `C(v,v)=Q(v)`, so every element squares to `(0,1)`.
The identity and inverse claims follow.

The projection image is closed under binary addition, so it is an
`F_2`-subspace. Its kernel is exactly `(0,r)` with `r^2=1 mod N`. This proves
the exact sequence. Because every group in the sequence has exponent two,
the sequence is also a short exact sequence of finite-dimensional
`F_2`-vector spaces.

For odd `N`, a non-global root `r` cannot make either sign gcd equal to `N`.
Since `N` divides `(r-1)(r+1)`, its two CRT sign sets are both nonempty.
Both sign gcds are therefore proper nontrivial divisors. The weaker claim
that one of them factors is certainly correct.

I also exhaustively checked closure, commutativity, associativity,
exponent two, and the gcd assertion for odd `3 <= N < 80` and all tested
two-block unit systems. No counterexample occurred.

## 2. Relation lifts and the P66 root

From `T_i=s_i^2 Q(v_i)` and `alpha_i^2=T_i mod N`, the second coordinate
`alpha_i/s_i` squares to `Q(v_i)`. Hence every displayed lift belongs to
the group.

For a parity dependency `c`, let

\[
d_j=\sum_i c_i(v_i)_j.
\]

Each `d_j` is even, and the exact positive root of the selected integer
product is

\[
R(c)=\prod_i s_i^{c_i}\prod_jq_j^{d_j/2}.
\]

The cocycle corrections in the decorated product divide by precisely the
second product. Its kernel coordinate is therefore

\[
\frac{\prod_i\alpha_i^{c_i}}{R(c)}.
\]

P66 uses the inverse convention `R(c)/(prod alpha_i^c_i)`. The two values
are equal because either one is a square root of one. Thus `G(ker A)` is
exactly the complete normalized-root image, not only a subset of it.

## 3. Split or section, including the online form

Assume every kernel lift is global. The formula

\[
h(Ac)=\overline{G(c)}
\]

is well-defined: two representations differ by a kernel word, whose lift is
in `Delta`. It is a homomorphism, projects to `Ac`, and has the prescribed
values on every generator. Those generators span `W`, so the section is
unique.

Conversely, a section with the prescribed generator values sends every
kernel word to the identity in the quotient. Its unquotiented root is then
global. Hence failure of the prescribed section is equivalent to a
non-global normalized root. The two alternatives are exhaustive and
disjoint.

The online procedure is ordinary binary elimination with one decorated
representative per basis vector. An independent parity vector extends the
basis. A dependent vector gives a lift quotient in `R_N`; equality up to
global sign is a modular comparison, and any other quotient factors `N`.
The procedure is polynomial in the explicit transcript size. A polynomial
amount of work on a quasipolynomial-size explicit transcript remains
quasipolynomial.

The abstract splitting claim is also correct. Choose a basis of `V_Q`, pick
one lift of each basis vector, and extend by the group operation. Exponent
two makes this an `F_2`-linear section. In fact, any no-factor section on a
subspace also extends abstractly after choosing a complement. Therefore
parity-space structure alone cannot contradict the existence of a lift.

## 4. Two layers and the same-fibre cross ratio

For `u` in `W_F intersect W_A`, choose one representation from each layer.
Their union is a parity dependency. Modulo global roots its lift is

\[
h_F(u)h_A(u).
\]

Changing a representation multiplies its lift by a pure-layer kernel root,
which is global by hypothesis. The map is therefore well-defined. Every
union dependency maps to an intersection vector, and every intersection
vector supplies such a dependency. This recovers the P108 cross quotient
and its induced normalized-root image.

For two relations with the same parity vector and
`T_i=d*s_i^2`, `T_j=d*s_j^2`, the cocycle factor is `d`. Their quotient lift
is

\[
\frac{\alpha_i\alpha_j}{d s_i s_j}.
\]

Using either root congruence converts it to

\[
\frac{\alpha_i s_j}{\alpha_j s_i}.
\]

This is exactly the P134 residual-core cross ratio.

### Deduplication application warning

The theorem is correct for the explicit list that survives into it. In a
general supplied-root source, exact integer equality alone is not a safe
deduplication rule: two equal integers can carry roots that differ by a
non-global root. Deleting one would delete a valid section disagreement.
P108's canonical inverse values all use the same supplied root, so its
first-occurrence rule is safe there. A broader application of F152 must
retain root-labelled occurrences, or first prove that discarded root labels
agree up to global sign. The frozen candidate does not claim a general
deduplication-preservation theorem, so this is an application condition, not
a counterexample to its statements.

## 5. Independent check of the finite illustration

The exact identities are

\[
5547=3\cdot43^2=1+2\cdot2773,
\]

\[
2126892=3\cdot842^2=1+767\cdot2773.
\]

All displayed roots and denominators are units modulo `2773`. Their
same-fibre decorated product is the inverse of

\[
R=3\cdot43\cdot842=108618.
\]

Now `R=471 mod 2773`, and

\[
471^2-1=80\cdot2773.
\]

Because a square root of one is self-inverse, this is the same decorated
kernel coordinate. Finally,

\[
\gcd(470,2773)=47,
\qquad
\gcd(472,2773)=59.
\]

The certificate is exact. The word "smallest" is best read as the minimal
two-lift same-fibre disagreement pattern, not as a numerical minimality
claim; no numerical minimality is proved or needed.

## Scope retained after audit

F152 changes the description of the remaining source problem. It does not
solve it. It proves no density of incompatible lifts, no canonical-inverse
collision law, no feedback-cycle source theorem, no PFR lift theorem, and no
all-input factorization result. Its precise positive content is the public
win-or-structure invariant: each new decorated relation extends the observed
section, agrees with it, or exposes a factor.
