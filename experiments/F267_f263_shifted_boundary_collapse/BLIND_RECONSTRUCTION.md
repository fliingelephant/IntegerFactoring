# F267 blind reconstruction

## Audit status

- Frozen `MANIFEST.md`: authenticated before reading the statement.
  SHA-256 `8ff26680b73c10f1f3513428154719a30b3b027aab6b4127561f55eb05b71961`.
- Frozen `STATEMENT.md`: authenticated before reading it.
  SHA-256 `feff0a8b5dfd254cba265c9378106520c4fed718bbff3d507112c59a367045ee`.
- Blind mathematical verdict: **PASS**.
- Finite F263 artifact audit: pending at the time this section was sealed.
- Overall verdict: pending the finite artifact audit.

Everything through the end of **Blind proof seal** was reconstructed from
`STATEMENT.md` alone.  I had not read `PROOF.md`, `SELF_AUDIT.md`,
`HOSTILE_AUDIT.md`, the F263 source, or any F263 result artifact.

## Independent derivation

### 1. Basic inequalities and units

From (p<\sqrt{pq}<q), with all quantities integral where applicable,

\[
p\le B<q.
\]

Also (B<q<2p), so (B\le 2p-2).  Hence

\[
0\le s=B-p\le p-2,
\qquad
H-s=\left\lfloor {p-s\over2}\right\rfloor\ge1.
\]

This proves (0\le s<H<p<q) and (B<q).  If (s=0), then
‎(gcd(B,N)=gcd(p,pq)=p).  If (s\ge1), then (B\equiv s\not\equiv0
\pmod p), while (0<B<q).  Thus (B) is a unit modulo both hidden
primes on the unresolved branch.  The same bound (s\le p-2) also shows
that (B+1\equiv s+1\not\equiv0\pmod p).

### 2. Product jets

For (x_j=a+j), the coefficient of (z^k) in

\[
\prod_{j=0}^{L-1}(x_j+z)
\]

is the sum of the products obtained by omitting (k) distinct factors.
It is also (R_L^{(k)}(a)/k!).  Therefore the first three product-jet
coordinates are

\[
u_0=R_L(a),\quad u_1=R_L'(a),\quad
u_2={R_L''(a)\over2}.
\]

Replacing every (x_j) by (x_j-B) gives the three stated (v)
coordinates.  Consequently the (0,2) determinant is

\[
u_0v_2-u_2v_0
={R_L(a)R_L''(a-B)-R_L''(a)R_L(a-B)\over2}.
\]

This is an integer identity: each second derivative is divisible by two
coefficientwise in this evaluation formula.

### 3. Transfer identities

Order the block as (c_0=a,\ldots,c_{L-1}=a+L-1), and put

\[
A_j=\prod_{i<j}c_i\prod_{i>j}(c_i-B).
\]

The upper-right entry of the forward triangular-matrix product is
‎(F_w=\sum_j w_{c_j}A_j).  The elementary telescoping identity

\[
\prod_j c_j-\prod_j(c_j-B)
=\sum_j B A_j
\]

therefore proves

\[
BF_0=R_L(a)-R_L(a-B).
\]

Telescoping in the reverse order gives the same formula for (G_0).
No modular inverse has been used.

Linearity in the weights gives (F_1-F_0=F_c:=\sum_j c_jA_j).  For a
division-free derivation of its closed form, define

\[
T_j=\prod_{i<j}c_i\prod_{i\ge j}(c_i-B),
\qquad T_0=R_L(a-B),\quad T_L=R_L(a).
\]

Then (T_{j+1}-T_j=BA_j), and summation by parts gives

\[
BF_c=(a+L-1)T_L-aT_0-\sum_{j=1}^{L-1}T_j.
\]

Since (c_jA_j=T_j+BA_j), one also has
‎(sum_{j=1}^{L-1}T_j=F_c-T_L).  Substitution yields

\[
(B+1)F_c=(a+L)R_L(a)-aR_L(a-B).
\]

Multiplication by (R_L(a)) proves the displayed formula for
‎(D_{01}=R_L(a)(F_1-F_0)).  This too is an identity over the
integers and requires no recurrence factor to be invertible.

### 4. Left-edge reflection: (s=L+1)

The half-open block (E_L=[1,L+1)) contains exactly (1,\ldots,L).
Modulo (p), (B\equiv s=L+1), so its shifted factors are

\[
c-B\equiv c-(L+1)=-(L+1-c).
\]

They are the reversed negatives of the unshifted factors.  Because (L)
is even, the full shifted product has sign ((-1)^L=1), and every
product omitting two factors has sign ((-1)^{L-2}=1).  Thus

\[
v_0\equiv u_0,\qquad v_2\equiv u_2\pmod p.
\]

It follows that `jet_det02` is zero modulo (p).  The same equality of
full products, together with the two division-free transfer identities
and the fact that (B) is a unit modulo (p), forces both
`transfer_f0` and `transfer_r0` to be zero modulo (p).

The singular index is (s=L+1), immediately outside the right endpoint
of (E_L).

### 5. Left-edge one-step translation: (s=L+2)

Again on (E_L), the unshifted product is (L!).  Modulo (p), the
shifted factors are the reversed negatives of (2,\ldots,L+1).  Since
‎(L) is even,

\[
R_L(1-B)\equiv(L+1)!,
\]

and therefore

\[
(1+L)R_L(1)-R_L(1-B)\equiv0\pmod p.
\]

The transfer identity gives ((B+1)D_{01}\equiv0\pmod p).  Here
‎(B+1\equiv s+1\not\equiv0\pmod p), as proved in Section 1, so
`transfer_det01` is zero modulo (p).  The singular index (L+2) is
again outside the block.

### 6. Right-edge unshifted reflection

The right block (J_L=[H-L,H)) contains

\[
H-L,H-L+1,\ldots,H-1.
\]

Its endpoint sum is (2H-L-1).  If (s=L+1), then (s) is odd,
‎(B=p+s) is even, and (2H=p+L+1).  If (s=L+2), then (s)
is even, (B) is odd, and again (2H=B-1=p+L+1).  In both cases the
endpoint sum is (p), so the block is invariant under (c\mapsto p-c).

All its elements lie strictly between zero and (p).  Hence its full
product is a unit modulo (p), and

\[
R_L'(H-L)
=R_L(H-L)\sum_{c=H-L}^{H-1}c^{-1}\equiv0\pmod p,
\]

because each pair (c,p-c) has cancelling inverses.  There is no fixed
point because (p) is odd.  This proves the two `shifted.u1` cases,
including their parity and half-open endpoints.

### 7. Right-edge shifted reflection

Write (t=q-B).  Under the extra hypothesis

\[
q=p+2(s+1),
\]

one has (t=s+2).  The shifted factors on (J_L), represented as
positive residues modulo (q), therefore run from

\[
t+H-L\quad\hbox{through}\quad t+H-1.
\]

If (s=L-1), then (s) is odd and (2H=B=p+L-1).  If (s=L), then
‎(s) is even and (2H=B-1=p+L-1).  In either case the endpoint
sum is

\[
2H+2s+3-L=p+2s+2=q.
\]

The residue interval is thus invariant under (z\mapsto q-z).  Its
members are nonzero; the positive lower endpoint and the endpoint-sum
identity also put the upper endpoint below (q).  Pairwise inverse
cancellation proves (R_L'(H-L-B)\equiv0\pmod q), which is exactly the
`shifted.v1` claim.

Since (s<H) always, (J_L) excludes the singular index precisely when
‎(s<H-L).  This is the stated strict non-direct condition.  The two
left-edge cases exclude the singular index automatically.

### 8. Near-square rigidity

Keep (t=q-B\ge1), and put (d=t-s).  The floor-square inequalities give

\[
0\le N-B^2<2B+1.
\]

Using (p=B-s) and (q=B+t), this becomes

\[
0\le dp-s^2<2p+2s+1.
\tag{A}
\]

Because (q-p=2s+d) is even, (d) is even.  The lower inequality, with
‎(q>p), forces (d>0); hence (d\ge2).  If (d\ge4), the upper
inequality in (A) implies

\[
2p<(s+1)^2.
\]

But (s^2<p), with integral (p), gives
‎(2p\ge2s^2+2\ge(s+1)^2), the last inequality being
‎((s-1)^2\ge0).  This is a contradiction.  Therefore (d=2), so

\[
t=s+2,\qquad q-p=2(s+1),\qquad {p+q\over2}=p+s+1=B+1.
\]

This proof also covers (s=0).  Since distinct (p,q) make (N) a
nonsquare, the first Fermat trial uses (A=\lceil\sqrt N\rceil=B+1).
The midpoint identity gives

\[
A^2-N=\left({q-p\over2}\right)^2=(s+1)^2,
\]

and returns (A-(s+1)=B-s=p) and (A+(s+1)=B+s+2=q).

### 9. Public-descriptor collapse and exact scope

Every table hypothesis already sets

\[
p=B-s,
\qquad s\in\{L-1,L,L+1,L+2\}.
\]

For each public registered length (L), one can test these at most four
public integers directly, for example by computing
‎(gcd(B-s,N)).  If the query bank has polynomial size, this direct
offset list also has polynomial size.  Thus these mechanisms cannot
provide a nonconsecutive factoring advantage: even without the
small-offset condition or the extra equation in the `v1` row, their
hypotheses expose the hidden factor through a public offset.  Under
‎(s^2<p), all of them additionally collapse to one Fermat trial by
Section 8.

This derivation proves the displayed integer identities and the four
mechanisms: left reflection, left one-step translation, right unshifted
reflection, and right shifted reflection.  It does **not** prove that the
six polynomials have no zeros elsewhere, that another grammar cannot
evaluate a target block, or that general factoring is impossible.  Any
claim about the reported finite sets, incidence counts, row union, or
held-out numerical bounds still requires authentication against the
frozen F263 artifacts.

## Blind proof seal

This line terminates the statement-only reconstruction.  The exact byte
prefix through this line is to be hashed before any implementation,
result, or reference-proof inspection.  Later audit notes may only be
appended below it.

## Post-seal authentication and finite audit

The blind prefix above was sealed at 8,179 bytes with SHA-256
`04bbb7dc95fea1ff3f39ac81ee6464f014b5eedc7b716e5bae542215e7bee047`
before any of the files named below were read.

After the seal, I authenticated the F263 provenance named by the F267
manifest:

| Artifact | Authenticated SHA-256 |
|---|---|
| `V2_FROZEN.sha256` | `2a41fb0ca76955522843fdc0b15c69b1b2d811a3ac79021b0518bf6da9224271` |
| `V2_symbolic_search.cpp` | `05c0b87a453eb3c2c40c01bf058b0559a6ff2e9b943d16ddcf68d147b1f4c827` |
| `V2_RESULT_AUDIT.md` | `320427df65f9d45f63cfaf4ad93194fe7e09cc499b4bd6d86b9a5ad7fb92b976` |
| held-out rows TSV | `58b1e1ebde26af9ccdca43449fafff6d1737c932ceb2c3f9849571919c0f10a1` |
| held-out summary JSON | `95bb89d57c6a45cc964c70ec57db7c95f8fc5e0dfcd96d5e3df4c005559f46cb` |

All 17 entries in `V2_FROZEN.sha256` also pass `shasum -a 256 -c`.

### Source-semantics check

The source independently confirms the interpretation used in the blind
proof:

- the shifted scan uses actual indices (c=1+q.start+j), with factors
  (u_c=c) and (v_c=c-B);
- its three jet registers obey the product-omission recurrence, so they
  equal (R,R',R''/2);
- transfer weights zero and one are exactly (1) and (c+1), and the
  source accumulates both forward and reverse products;
- `transfer_det01` is the determinant of the two forward transfer rows,
  hence (R_L(a)(F_1-F_0));
- shifted domain size is (H-1) with base index one; and
- every registered length includes query starts zero and
  `domain-length`.  These are actual blocks (E_L=[1,L+1)) and
  (J_L=[H-L,H)).

The source's registered length set consists of powers of two up to the
‎(n^2) cap, plus at most (n) and (n^2) themselves.  It therefore
has (O(\log n)) lengths.  The at-most-four-offset public test in the
blind proof is polynomial, as the statement claims.

### Independent held-out reconstruction

I decoded the authenticated TSV bitsets directly in the 148-candidate
source order and checked every JSON candidate aggregate.  There are 1,152
held-out rows.  The only candidates with a non-direct bit are:

| Candidate | Incidences | Factor-bit counts 40/48/56/60 | Complete (s=B-p) set |
|---|---:|---|---|
| `shifted.u1` | 33 | 11/11/7/4 | `9,10,17,18` |
| `shifted.v1` | 34 | 11/10/5/8 | `7,8,15,16,31,32,63,64` |
| `shifted.jet_det02` | 18 | 7/3/4/4 | `9,17` |
| `shifted.transfer_f0` | 18 | 7/3/4/4 | `9,17` |
| `shifted.transfer_r0` | 18 | 7/3/4/4 | `9,17` |
| `shifted.transfer_det01` | 15 | 4/8/3/0 | `10,18` |

The sum is exactly 136 candidate-row incidences.  Their union is exactly
67 rows.  Every incidence is in the consecutive-prime cohort.  Each set
maps without exception to the statement's registered length:

- `u1`: (L=8,16);
- `v1`: (L=8,16,32,64);
- `jet_det02`, `transfer_f0`, and `transfer_r0`: (L=8,16); and
- `transfer_det01`: (L=8,16).

For each of all 136 incidences, I independently reevaluated the indicated
edge block with exact arbitrary-precision modular arithmetic.  Every
support excludes the source's shifted singular index.  The resulting gcd
is (p) for all five (p)-rows and (q) for every `v1` row.  There are
no replay failures and no unmapped incidences.

There are exactly 256 held-out consecutive-prime rows, including exactly
eight cleanup rows.  Direct reconstruction gives

\[
\min p=551426102609,
\qquad
\max s=95.
\]

All eight cleanup rows have (s=0).  Every one of the 256 rows satisfies
‎(B+1=(p+q)/2) and
‎((B+1)^2-N=(s+1)^2).  Thus the stated small-offset bound and the
one-Fermat-trial conclusion hold on the complete finite cohort, not only
on the 67-row union.

### Counterexample search

As bounded guidance, I enumerated odd-prime pairs with both primes at most
10,000 and (p<q<2p).  The search checked 17,952 instances of the
small-offset rigidity implication, 14,314 left-reflection instances,
14,565 left-translation instances, 28,645 right-`u1` instances, and
22,461 right-`v1` instances.  It found no counterexample.  A separate 500
case exact-integer check, including signed starts and signed (B), found
no failure of either transfer identity.  These checks are audit guidance,
not part of the proof.

## Reference-proof comparison

Only after the blind proof and finite audit were complete, I authenticated
and read `PROOF.md` at SHA-256
`f6e95ae5d8a27828cfd4802cdc587f2bba2b2e94d50f523d42b559ef14e4fac3`.
Its derivations agree with the reconstruction.  It uses an equivalent
rising-factorial reflection for the left edge, even-polynomial pairing for
both right edges, and the prime gap (q-p) instead of (t-s) in the
floor-square argument.  I found no mathematical omission or changed
hypothesis.

The reference proof delegates the finite set, 136-incidence, and
67-row-union claims to the authenticated F263 result audit instead of
retabulating them.  The independent reconstruction above closes that
provenance step.  I did not read `SELF_AUDIT.md` or `HOSTILE_AUDIT.md`.

## Final verdict

**PASS.**  Every mathematical claim in the frozen statement follows with
the stated parity, endpoint, invertibility, and support conditions.  The
authenticated F263 source has the asserted candidate semantics, and every
finite count, set, bound, and boundary attribution reconstructs exactly.
The conclusion remains conditional and finite in precisely the scope
stated: it does not classify other zeros or exclude other evaluator
grammars.
