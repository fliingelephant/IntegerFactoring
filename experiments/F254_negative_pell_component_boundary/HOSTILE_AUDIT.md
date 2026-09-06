# F254 hostile audit

## Verdict

**PASS.** The five frozen files authenticate exactly. The tailored Pell
identity, affine component split, even-subset modular-root interface,
resultant localization, complete negative-Pell window for `N=143`, exact
factorizations, parity ranks, and all declared direct screens reconstruct
independently.

The certificate has the narrow scope stated in the packet. It refutes a
universal claim for this one tailored negative-Pell source. It gives no
probability bound, no general factoring obstruction, and no closure of the
retrospective multirow P66 channel.

Two harmless exposition points are recorded below. Neither affects the
result.

## Authentication

I computed every requested SHA-256 digest before reading the frozen files.
All expected and observed digests agree.

| Frozen file | SHA-256 | Result |
|---|---|---|
| `STATEMENT.md` | `25d20381188d0ffe5e7d9b87331c3921b0f78dd9344d73628ca33e1f1201e190` | match |
| `PROOF.md` | `ac78cae56d0063191e0eafa8cf37ad61358fb9246bf5cd94033413434e96625e` | match |
| `SELF_AUDIT.md` | `e89c819546e80c422796f6779ce8366f5f699de8733b70bfb84dd7963d718874` | match |
| `PROVENANCE.md` | `c829ec3661320439e20eeae96f062ebdd7b3bfc43f135ab0290404ef8c9d2679` | match |
| `MANIFEST.md` | `cead4a48b27284d8e005dce1bedc79e2ccee3b87558fe460e8fb47b54a9bdc90` | match |

The task's labels `SELF` and `MANIFEST` correspond to the on-disk files
`SELF_AUDIT.md` and `MANIFEST.md`.

## 1. Tailored Pell row and exact factorization

From

\[
b^2-2y^2=-1,
\]

`y` must be odd: if it were even, then `b^2` would be `3 mod 4`. It follows
that `b` is odd. Thus

\[
u={b-1\over2},\qquad v={b+1\over2}
\]

are integers. The norm equation gives the three exact identities

\[
2u^2=y^2-b,\qquad 2v^2=y^2+b,\qquad 2uv=y^2-1.
\]

Put `T=N+y`, `D=T^2-2`, and `S=T^2-1`. Direct expansion gives

\[
S^2-DT^2=1.
\]

For `T>=2`,

\[
(T-1)^2<T^2-2<T^2,
\]

so `D` is positive and nonsquare. Since `T` reduces to `y mod N`,

\[
S\equiv y^2-1\pmod N
\]

and

\[
S^2\equiv 1+Dy^2=A\pmod N.
\]

The asserted component split follows without a modular step:

\[
\begin{aligned}
A
&=1+(T^2-2)y^2\\
&=(Ty)^2-b^2\\
&=(Ty-b)(Ty+b)\\
&=(yN+2u^2)(yN+2v^2).
\end{aligned}
\]

Thus the displayed factors are exact positive integer factors of the row,
not only congruence classes.

## 2. Component-level P66 interface

For a component

\[
C_i=y_iN+2w_i^2,
\]

we have `C_i = 2w_i^2 mod N`. If a selected subset has `2h` components,
then

\[
\prod_i C_i
\equiv 2^{2h}\prod_iw_i^2
=\left(2^h\prod_iw_i\right)^2\pmod N.
\]

Hence a modular square root is public. If the same integer product is an
exact square, this is exactly a P66 congruence-of-squares certificate. The
parity restriction is essential within this interface: the construction
does not supply a square root of the residual factor `2` for an
odd-cardinality component subset.

For the two components from one row, the public root is

\[
2uv=y^2-1\equiv S\pmod N,
\]

so the component interface agrees with the supplied original-row root. On
the counterexample every component and every `w` is a unit modulo `N`, so no
hidden nonunit invalidates this root comparison.

## 3. Determinant and resultant localization

For

\[
F_i(X)=y_iX+2w_i^2,\qquad F_j(X)=y_jX+2w_j^2,
\]

direct elimination gives

\[
y_iF_j(X)-y_jF_i(X)
=2(y_iw_j^2-y_jw_i^2).
\]

This is the stated resultant sign convention. Therefore any rational prime
that divides both specialized values `F_i(N)` and `F_j(N)` divides that
public determinant. No coprimality assumption is needed for this
specialization implication.

The generic statement also survives scrutiny. If a divisor divides both
`y` and either `u` or `v`, then `b` is respectively `1` or `-1` modulo that
divisor. The norm equation then makes the divisor divide `2`; because `y`
is odd, the divisor is one. Each affine form is primitive. Distinct
nonassociate linear forms are distinct irreducibles in `Q[X]`; a product of
distinct such forms has valuation one at each selected irreducible and
cannot be a square in `Q(X)`. The statement correctly excludes associate
forms from this generic claim.

The localization is exact, not a claim that resultants forbid all
specialized reuse. In the certificate, the shared prime `3` in the second
and third components divides their resultant `3072`, as required.

## 4. Completeness of the admissible negative-Pell window

For a positive solution with `y>1`,

\[
{b\over y}=\sqrt{2-{1\over y^2}},
\]

so, already for `y>=3`,

\[
{4\over3}<{b\over y}<{3\over2}
\quad\text{and}\quad b>y.
\]

Consequently

\[
(b',y')=(3b-4y,\;3y-2b)
\]

has positive integer coordinates, satisfies the same norm `-1`, and has
`0<y'<y`. Repeated descent reaches `y=1`, where positivity forces `b=1`.
Its inverse is

\[
(b,y)\longmapsto(3b+4y,\;2b+3y).
\]

This proves that the recurrence lists all positive solutions, rather than
only one unverified orbit. Its consecutive start is

\[
(1,1),\quad(7,5),\quad(41,29),\quad(239,169).
\]

Since

\[
1<5<29<143<169,
\]

the strict window `1<y<143` contains exactly `y=5` and `y=29`.

## 5. Exact arithmetic and ranks

For `(b,y)=(7,5)`, reconstruction gives

\[
(u,v,T,D,S)=(3,4,148,21902,21903),
\]

\[
(F_-,F_+)=(733,747),
\]

and

\[
A=547551=733\cdot747=733\cdot3^2\cdot83.
\]

Here `S mod 143=24`, and

\[
24^2\equiv547551\equiv4\pmod{143}.
\]

For `(b,y)=(41,29)`, reconstruction gives

\[
(u,v,T,D,S)=(20,21,172,29582,29583),
\]

\[
(F_-,F_+)=(4947,5029),
\]

and

\[
A=24878463
=(3\cdot17\cdot97)(47\cdot107).
\]

Here `S mod 143=125`, and

\[
125^2\equiv24878463\equiv38\pmod{143}.
\]

Thus the four component factorizations are

\[
733,\quad3^2\cdot83,\quad3\cdot17\cdot97,\quad47\cdot107.
\]

All displayed terminal factors are prime. The parity rows at
`733,83,17,47` restrict to the identity matrix on the four component
columns. Therefore the component parity matrix has column rank four. No one
of its 15 nonempty subsets is an exact square. This is stronger than needed:
there is no dependency even before the known-root interface imposes even
cardinality.

The two original rows also have rank two. For example, prime `733` is an
odd-valuation row private to the first original row, while prime `17` is an
odd-valuation row private to the second. Hence the original-row bank has no
nonzero exact-square subset either.

## 6. Direct screens

In component order

\[
(5,3),(5,4),(29,20),(29,21),
\]

the six pairwise resultants reconstruct as

\[
70,\quad3478,\quad3888,\quad3072,\quad3482,\quad2378.
\]

Each has gcd one with `143=11*13`. The following complete declared screen
groups also have gcd one with `143`:

- components: `733, 747, 4947, 5029`;
- supplied root residues: `24, 125`;
- first-row data: `7, 5, 3, 4, 148, 21902`;
- second-row data: `41, 29, 20, 21, 172, 29582`.

The two exact `S` values reduce to the listed unit roots. Both row values
are units because their components are units. Thus all direct gcd screens
declared by the packet are inert. Full parity rank then rules out every
exact-square P66 dependency.

## 7. Exact boundary

The authenticated example proves only this statement: for the odd composite
input `N=143`, exposing every affine component from every positive
negative-Pell solution in the complete strict window `1<y<N` does not force
an exact-square dependency and does not trigger any of the declared direct
screens.

It does not establish any of the following:

1. a success or failure probability for randomized discriminants, indices,
   windows, or coordinate laws;
2. an obstruction for another Pell source, a larger or mixed bank, or an
   adaptive nonlinear decoder;
3. a lower bound for integer factoring;
4. closure of the general retrospective multirow P66 channel left open by
   P213 and P214.

The frozen statement and manifest respect all four limitations.

## Nonoperative exposition notes

The proof says that reduction modulo two shows both `b` and `y` are odd.
Modulo two directly forces `b` odd; parity of `y` needs the one-line modulo
four argument used above. The conclusion is correct.

The descent proof also states `y>1` implies `y>=5` without showing the only
smaller odd candidate `y=3` is impossible. One may check `b^2=17`, or avoid
the sentence entirely because the required ratio inequalities already hold
for every integer `y>=3`. The complete-window proof is unaffected.

## Hostile conclusion

Every operative identity, quantifier, factorization, parity claim, screen,
and scope boundary passes independent reconstruction. I found no
promotion-blocking mathematical or evidentiary defect. I wrote only this
audit and changed no frozen input or durable ledger.
