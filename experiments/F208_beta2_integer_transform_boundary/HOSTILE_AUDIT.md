# F208 hostile audit

## Verdict

**PASS.** I found no false identity, sign error, endpoint error, parity
exception, HNF multiplicity error, form-class error, or scope overclaim in
the frozen candidate. The result is valid only as the named-model boundary
that it states. It does not evaluate the hidden divisor event and does not
prove a factoring algorithm or an integer-model lower bound.

**Defects found: none.**

I did not edit a frozen input or a durable ledger. I ran small exact checks
after reconstructing the proofs. Those checks are supporting regression
evidence, not substitutes for the arguments below.

## 1. Frozen-input integrity

I read MANIFEST.md first. Before reading the four declared content files, I
recomputed their SHA-256 hashes. All four matched exactly:

- **STATEMENT.md**:
  e036b99dd345aacad134e716929e410a3ed083d601d7a5d50cf013957522f330;
- **PROOF.md**:
  a19f04c5c705f22bcf37d8b2a1eeac9bae3da5880121e7a986e133ec9f2c2bc9;
- **SELF_AUDIT.md**:
  69a56874669294d02c73c5531bdc876320cc0fcaa123533ae85c14822896434b;
- **PROVENANCE.md**:
  b5e5e867b44892b65cb7f7e0bdc1b60b87d6e00a31c278cab53830564f56f226.

The observed SHA-256 of MANIFEST.md itself is
0bc6946868aab0855b2fad36a919a309fc913d693abbac8a25ee8998af5593bb.
The manifest does not declare a self-hash.

## 2. Divisor pairing and both sign orientations

The jump is exact:

\[
J_d(N)=\left\lfloor\frac Nd\right\rfloor
-\left\lfloor\frac{N-1}{d}\right\rfloor
=\mathbf 1_{d\mid N}.
\]

The semiprime is nonsquare, so each divisor pair has exactly one member at
most $B=\lfloor\sqrt N\rfloor$. For an odd divisor $d$,

\[
\chi(N/d)=\chi(N)\chi(d)=\eta\chi(d),
\]

because $\chi(d)^2=1$. Pairing $d$ with $N/d$ therefore gives

\[
A(N)=\sum_{d\leq B}\chi(d)
\left(d+\eta\left\lfloor\frac Nd\right\rfloor\right)J_d(N).
\]

Only $d=1,p$ are supported. Removing the $d=1$ contribution gives

\[
T=A(N)-(1+\eta N)=\chi(p)(p+\eta q).
\]

Both branches have the claimed orientation:

\[
\begin{array}{c|c|c}
\eta&T&\operatorname{sgn}T\\ \hline
+1&\chi(p)(p+q)&\chi(p)\\
-1&\chi(p)(p-q)&-\chi(p)
\end{array}
\]

Since $\eta=\chi(p)\chi(q)$, both rows equal
$\eta\chi(p)=\chi(q)$. In particular, the negative parenthesis on the
$\eta=-1$ branch is necessary and is handled correctly. The remaining
sum over $2\leq d\leq B$ has the single supported term $d=p$, so it
equals $\chi(p)$, not $\chi(q)$.

## 3. Totalized floor reciprocity and the unique interval spike

For odd positive $N,d$, each floor sum counts one closed side of the line
$jN=id$ in the declared half-rectangle. The index bounds ensure that the
floors never count points outside that rectangle. Every off-line point is
counted once and every on-line point twice.

Writing $g=\gcd(N,d)$, all positive on-line points have the form

\[
i=tN/g,\qquad j=td/g.
\]

Because $g$ is odd, the two half-range bounds hold exactly for
$1\leq t\leq(g-1)/2$. Thus the double-count correction is $(g-1)/2$, and

\[
\Delta_N(d)=\frac{\gcd(N,d)-1}{2}.
\]

There is no missing endpoint or factor of two.

Balance gives

\[
p<\sqrt N<q,\qquad p\leq B<q,
\qquad B<\sqrt{2}\,p<2p.
\]

Hence $B/2<p\leq B$. A number $d\in(B/2,B]$ cannot be a multiple of
$q$, since $d\leq B<q$. If it is a multiple $kp$, then $d<2p$
forces $k=1$. Therefore $p$ is the unique nonunit-gcd location in the
interval. Restricting to odd $d$ retains it, and

\[
2\sum_{\substack{B/2<d\leq B\\d\ {\rm odd}}}
\chi(d)\Delta_N(d)=\chi(p)(p-1).
\]

Thus the intended recovery is “take the absolute value, then add one”:

\[
\left|2\sum_{\substack{B/2<d\leq B\\d\ {\rm odd}}}
\chi(d)\Delta_N(d)\right|+1=p.
\]

The direct interval has $\Theta(B)=\Theta(\sqrt N)$ entries on the
balanced promise. A gcd-based term evaluation has polynomial cost per
entry, but the number of entries is $2^{\Theta(\log N)}$. This is a
correct statement about that literal scan. It is not a lower bound against
a compressed aggregate.

## 4. Noncoprime Dedekind reduction and cotangent poles

Let $h=gh_0$, $k=gk_0$, and write each residue uniquely as
$r=u+jk_0$, with $0\leq u<k_0$ and $0\leq j<g$. The second sawtooth is
independent of $j$:

\[
\left(\left(\frac{hr}{k}\right)\right)
=\left(\left(\frac{h_0u}{k_0}\right)\right).
\]

For $u>0$, none of the first-factor arguments is integral and direct
summation gives

\[
\sum_{j=0}^{g-1}
\left(\left(\frac{u+jk_0}{gk_0}\right)\right)
=\frac{u}{k_0}-\frac12
=\left(\left(\frac{u}{k_0}\right)\right).
\]

For $u=0$, the $j=0$ term is the defined zero sawtooth value, while the
other $g-1$ terms sum to zero. Therefore no factor $g$ remains:

\[
s(h,k)=s(h/g,k/g).
\]

In the standard cotangent sum, the second cotangent is singular exactly
when $k\mid hr$. Coprimality of $h/g$ and $k/g$ makes this equivalent
to $k/g\mid r$. For $1\leq r<k$, the complete pole set is

\[
r=j\,k/g,\qquad 1\leq j<g,
\]

so it has exactly $g-1$ elements. The first cotangent is finite because
none of these residues is $0\pmod k$. It can be zero in an even-$g$ case,
but the ordinary pointwise cotangent summand still contains an undefined
second factor. The standard formula is therefore nonsingular as written
exactly on the coprime branch. In the application $g=p$ is odd.

For $(h,k)=(p,pq)$, the reduced arguments are $(1,q)$. The packet uses
this only as an exact relocation after the gcd normalization. It correctly
does not rule out another aggregate evaluation strategy.

## 5. Triangular HNF multiplicity and shell weight

The declared matrix is the upper-triangular row-HNF convention

\[
\begin{pmatrix}d&b\\0&a\end{pmatrix},
\qquad 0\leq b<a.
\]

For fixed $a,d$, there are exactly $a$ values of $b$. Each has weight
$\chi(a)$, so the total weight is $a\chi(a)$, not $d\chi(a)$ and not
merely $\chi(a)$. Consequently,

\[
\sum_{\substack{ad=N\\0\leq b<a}}\chi(a)
=\sum_{a\mid N}a\chi(a)=A(N).
\]

The statement's triple-sum definition of $\mathcal C(X)$ is equivalent to
the flattened proof definition

\[
\mathcal C(X)=\sum_{ad\leq X}a\chi(a).
\]

Taking $\mathcal C(N)-\mathcal C(N-1)$ selects exactly $ad=N$, or
equivalently the jump $J_a(N)$. The HNF claim is an exact weighted count
for this declared convention. It makes no claim that listing or summing the
shell is efficient.

## 6. The literal diagonal reduced form and its class

The form $[p,0,q]$ is primitive because $\gcd(p,q)=1$. It has
discriminant $-4pq=-4N$, and

\[
|0|\leq p<q
\]

puts it strictly inside the positive-definite reduced inequalities. Its
inverse form is $[p,-0,q]$, which is identical, so its proper class is
ambiguous.

A literal diagonal form of this discriminant has $ac=N$. Positivity and
reduction give $a\leq c$. For a distinct semiprime, the only choices are

\[
[1,0,N]\quad\text{and}\quad[p,0,q].
\]

The second form is not principal. It represents $p$ at $(1,0)$, while the
principal form would require

\[
x^2+Ny^2=p.
\]

If $y\ne0$, the left side is at least $N>p$. If $y=0$, it would make the
prime $p$ a square. Proper equivalence preserves represented integers, so
this contradiction is conclusive.

This proves uniqueness only among the literal diagonal reduced forms and
the stated nonprincipal-class fact. It does not constrain arbitrary
reduced forms, class-group statistics, or implicit class navigation. The
packet keeps those scopes separate.

## 7. Pair symmetry and the two-square identity

For $\eta=-1$, complementary divisors satisfy
$\chi(N/d)=-\chi(d)$. If $W_N(d)=W_N(N/d)$, each complete pair contributes

\[
\chi(d)W_N(d)+\chi(N/d)W_N(N/d)=0.
\]

There is no midpoint because $N$ is nonsquare. The cancellation therefore
holds for exactly the complete, pair-symmetric total stated. It does not
extend to asymmetric weights, truncated divisor sets, or incomplete
representation totals.

The standard formula gives

\[
r_2(N)=4\sum_{d\mid N}\chi(d)
=4(1+\chi(p))(1+\chi(q)).
\]

If $\eta=1$, the characters agree and

\[
4(1+\chi(p))^2=8(1+\chi(p)).
\]

If $\eta=-1$, exactly one local factor is zero, so $r_2(N)=0$ in both
orientations. Thus the comparison has the claimed information on the
same-character branch and loses the orientation on the opposite-character
branch.

## 8. Exact magnitude, parity, and small cases

The corrected value gives

\[
|T|=p+q\quad(\eta=1),
\qquad
|T|=q-p\quad(\eta=-1).
\]

Direct expansion yields

\[
|T|^2-4N=(q-p)^2\quad(\eta=1),
\]

and

\[
|T|^2+4N=(p+q)^2\quad(\eta=-1).
\]

There is no parity obstruction. Since $p,q$ are odd, both $p+q$ and
$q-p$ are even. The usual half-sum and half-difference formulas therefore
return integers in both branches. Exact magnitude is factoring-equivalent;
the sign alone is only the stated character bit.

The smallest promised input is $N=15=3\cdot5$. Here $B=3$, the hidden
interval is $(3/2,3]$, $T=2$, and $T^2+4N=64=(3+5)^2$. Thus neither the
strict balance condition nor the half-open interval introduces a
small-prime exception. The balanced examples
$(p,q)=(5,7),(7,11),(13,17)$, together with $(3,5)$, cover all four
residue orientations modulo four and confirm the sign table.

As an independent finite check, I tested:

- all 2,601 odd pairs $1\leq N,d\leq101$ in the totalized floor identity;
- 6,480 pairs $0\leq h\leq80$, $1\leq k\leq80$ in the Dedekind
  reduction and cotangent pole count; and
- all 423 balanced odd-prime pairs with $p,q\leq199$ in the divisor,
  interval, HNF, two-square, and magnitude identities.

Every check passed. These bounded checks do not enlarge the proof scope.

## 9. Scope audit

The conclusions remain exact relocations, not evaluators:

1. The reciprocal-floor sum still hides the divisor jump at $p$.
2. The totalized reciprocity aggregate is factoring-equivalent only if its
   exact signed value is supplied.
3. Dedekind reduction exposes a smaller modulus only with the proper gcd
   normalization; no claim covers nonlinear aggregates of unit slopes.
4. The HNF result is a weighted adjacent-shell identity, not a compressed
   shell algorithm.
5. The form result concerns the literal diagonal route, not arbitrary
   class-group computation.
6. Pair cancellation requires complete exact symmetry.
7. Difference-of-squares recovery requires the exact magnitude. It does
   not follow from the sign bit.

The packet also expressly leaves nonlinear integer selectors, adaptive
aggregates, compressed signed divisor-OR evaluation, smaller recursive
children, and globally nested one-child recursion open. I found no sentence
that converts a literal-scan cost into a generic lower bound or a named
identity into a top-level factoring theorem.
