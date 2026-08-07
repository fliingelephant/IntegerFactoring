# F70 refinement-gain selector kill: hostile reaudit v3

## Verdict

**PASS.** I found no blocking mathematical defect.

The audited source was exactly
`experiments/F70_refinement_gain_selector_kill/RESULT.md`. Its observed
SHA-256 was

```text
baa75d5935ca576dcea16bd5ebc675bbb76fad2ded26bbe3baff7c3e1a3decfe
```

which matches the required hash. I did not consult an earlier F70 audit or
reconstruction, `PROVED.md`, `Progress.md`, a registry, `FAILED`, or git
history.

## 1. Definitions, count identity, and screens

The model is internally consistent. Since every old block is a unit modulo
the odd integer \(N\), every allowed product \(g\) is a unit. It therefore
has one canonical inverse \(w\in\{1,\ldots,N-1\}\). Adding endpoints can split an
old coprime block but cannot merge two old coprime blocks. Consequently, if
an old block contributes \(d_i\geq 1\) descendants, its contribution to the
count increase is \(d_i-1\). Adding the private new types gives

\[
r'-r=\sum_i(d_i-1)+\nu=\sigma+\nu.
\]

The screen identities are also correct. From \(gw\equiv1\pmod N\), and from
the fact that \(g\) is a unit,

\[
\gcd(w-1,N)=\gcd(g-1,N),\qquad
\gcd(w+1,N)=\gcd(g+1,N).
\]

Moreover,

\[
g(g-w)\equiv(g-1)(g+1)\pmod N
\]

and

\[
g^2\bigl((g-w)^2+4\bigr)\equiv(g^2+1)^2\pmod N.
\]

Thus the stated difference and discriminant gcds are legitimate public
screens. The exact-square test on \(gw\) is logically separate and is also
public.

## 2. Finite-transcript potential

The positivity hypothesis is explicit and sufficient. Let the endpoint
integers be \(x>0\), and let the final distinct blocks be
\(q_1,\ldots,q_R\). They are pairwise coprime, each is at least \(2\), and
each occurs in an endpoint. Hence

\[
2^R\leq\prod_{j=1}^R q_j\mid\prod_x x.
\]

Therefore

\[
R\leq\sum_x\log_2 x
 \leq\sum_x\lceil\log_2(x+1)\rceil=L.
\]

The monotone refinement count then telescopes exactly to

\[
\sum_t(\sigma_t+\nu_t)=R-r_0,
\qquad
\sum_t\sigma_t\leq L-r_0.
\]

Positivity matters: a zero endpoint would destroy the product-divisibility
argument, and signed endpoints would require absolute values. The source does
not claim either extension. All feedback endpoints in its model are positive
and below \(N\). Its adaptive-process caveat is correct because each round
also increases \(L\) by \(O(\log N)\); the inequality alone does not bound the
number of rounds by a polynomial in \(\log N\).

## 3. The \(N_s\) family and the square-closure witness

For odd \(s>1\) with \(s\equiv1\pmod3\),

\[
N_s=(2s-1)(2s+1)/3.
\]

Both factors are odd and greater than one. If a number divides both, it
divides \(2\), so their gcd is one. Thus \(N_s\) is composite. Also

\[
4s^2=1+3N_s,
\]

so the inverse of \(g=4\) is \(w=s^2\). The inequality \(1<s^2<N_s\) is
equivalent on the upper side to \(s^2>1\), so \(w\) is canonical. The product
\(gw=(2s)^2\) is an exact square, and

\[
\gcd(2s-1,N_s)=2s-1,
\qquad
\gcd(2s+1,N_s)=(2s+1)/3.
\]

Both gcds are proper. The two duplicate old columns have exactly one nonzero
dependency, and its positive root is \(N_s+1\equiv1\pmod{N_s}\). The two
separately charged occurrences of the block \(2\) make \(g=4\) legal.

For \(s\equiv55\pmod{1530}\), direct reduction gives

\[
\gcd(N_s,3\cdot5\cdot17)=1.
\]

This proves the two sign screens and the discriminant screen are trivial. It
also proves the difference screen, which the source does not spell out:

\[
\gcd(4-s^2,N_s)=\gcd(15,N_s)=1,
\]

because \(4(s^2-4)=3N_s-15\) and \(N_s\) is odd. Finally,

\[
16\bigl((4-s^2)^2+4\bigr)\equiv17^2\pmod{N_s},
\]

and both \(4\) and \(17\) are units. Thus the useful square closure genuinely
comes after all four gcd screens on this infinite subfamily.

At \(s=55\), \(N_s=4033\), \(w=3025=55^2\), and

\[
\gcd(4-3025,4033)=1,
\qquad
\gcd((4-3025)^2+4,4033)=1.
\]

The old block \(2\) is wholly contained in \(g=2^2\); it is not split. Also
\(\gcd(2017,3025)=1\). Hence \(\sigma=0\) is correct. The private square
endpoint does not obstruct the exact-square closure. Its root \(110\) has
signs \((-1,+1)\) modulo \((37,109)\), yielding gcds \(37\) and \(109\).

## 4. Separator-free old subgroup

The arithmetic certificates at \(N=4033=37\cdot109\) are correct:

\[
2^{18}\equiv-1\pmod{37},\quad 2^{12}\equiv26\pmod{37},
\]

\[
2^{18}\equiv-1\pmod{109},\quad 2^{12}\equiv63\pmod{109}.
\]

The first congruence at each prime makes the order divide \(36\) and not
divide \(18\). Every proper divisor of \(36\) that does not divide \(18\)
divides \(12\), and the second congruence excludes those cases. Therefore
both orders are exactly \(36\). An exponent gives \(+1\) at either prime
exactly when it is \(0\pmod{36}\), and gives \(-1\) exactly when it is
\(18\pmod{36}\). Thus every element of \(H_0=\langle2\rangle\) has the same
sign status at both primes. The no-direct-separator claim follows.

## 5. Strict-refinement witness

All three retained relations are exact:

\[
2\cdot2017=1+4033,
\]

\[
64\cdot3970=1+63\cdot4033,
\]

\[
8\cdot3529=1+7\cdot4033.
\]

Their complete old block set is

\[
Q_0=\{2,2017,1985,3529\},
\]

and its elements are pairwise coprime. The displayed relations imply
\(2017\equiv2^{-1}\), \(1985\equiv2^{-7}\), and
\(3529\equiv2^{-3}\), so \(H(Q_0)=H_0\). The available exponent of \(2\) is
indeed \(1+7+3=11\).

For \(g=2^{11}=2048\), the canonical inverse is \(w=3905\), and

\[
2048\cdot3905=7{,}997{,}440=1+1983\cdot4033.
\]

Independent gcd checks give

\[
\gcd(2048\pm1,4033)=
\gcd(3905\pm1,4033)=1,
\]

\[
\gcd(2048-3905,4033)=1,
\]

and

\[
\gcd((2048-3905)^2+4,4033)=1.
\]

The product is not a square because its \(2\)-adic exponent is \(11\).

The overlap classification is exact:

- \(\gcd(2,2048)=2\) is whole-block containment. It leaves the old
  block \(2\) intact and contributes zero to \(\sigma\).
- \(\gcd(1985,3905)=5\) is a proper overlap. It splits the one old
  type \(1985\) into \(5\) and \(397\), and therefore contributes exactly one
  to \(\sigma\).
- The other old blocks have gcd one with the new material.

The complete refined set is therefore

\[
Q_1=\{2,2017,5,397,3529,781\},
\]

whose members are pairwise coprime. Hence \(\sigma=1\) and \(\nu=1\). The
private block \(781\) occurs to odd multiplicity only in the new column. It is
nonsquare. No combination with old columns can cancel that private square
class, so no new decoder dependency or useful closure exists.

## 6. Subgroup enlargement and finite occurrence box

Each block of \(Q_1\) lies in \(H_1=\langle H_0,5\rangle\): this is immediate
for \(2,2017,3529,5\), while

\[
397=1985/5,
\qquad
781=w/5

\]

as identities in the unit group. Conversely \(2\) and \(5\) are members of
\(Q_1\), so \(H(Q_1)=H_1\).

Modulo \(37\), \(5=2^{23}\). Since \(2\) has order \(36\), any hypothetical
membership \(5\in H_0\) would force exponent \(23\pmod{36}\). But modulo
\(109\), \(2^{23}=77\ne5\). Thus \(5\notin H_0\), and the enlargement is
strict.

The separator certificate is also exact:

\[
x=5\cdot2^{13}=40960\equiv630\pmod{4033},
\]

\[
630\equiv1\pmod{37},
\qquad
630\equiv85\pmod{109},
\]

so \(\gcd(629,4033)=37\).

The source correctly stops at a subgroup-level statement. A legal positive
representative below \(N\) for this residue would have to equal the unique
canonical integer \(630=2\cdot3^2\cdot5\cdot7\). Of the available whole
blocks, only \(2\) and \(5\) can occur in an exact product equal to \(630\),
and their products cannot supply \(3\) or \(7\). The modular representation
\(5\cdot2^{13}=40960\) is above \(N\). It is not an allowed exact source
product below \(N\). Thus the finite-box caveat is valid and does not claim
that every factor-bearing element, or even this one, is efficiently
reachable.

## 7. Scope conclusion

The two histories establish only the stated one-way separations:

- \(\sigma=0\) can accompany immediate non-global square closure, so positive
  old-block splitting is not necessary.
- \(\sigma=1\) can accompany failure of every immediate screen and failure of
  square-class closure, so positive old-block splitting is not sufficient.

They do not form a same-menu ranking counterexample, and the source explicitly
disclaims that stronger conclusion. The transcript potential is accounting,
not a polynomial trajectory theorem. The subgroup witness is structural,
not a bounded-representative sampler. The final classification stays within
those proved boundaries.
