# Proof-blind reconstruction report

## Verdict: FAIL as written

The concrete \(N=4033\) construction does prove the narrow existential result:
gcd refinement exposes \(5\notin\langle2\rangle\), and the enlarged subgroup
contains \(630\), for which \(\gcd(630-1,4033)=37\). Nevertheless, the
statement asks for PASS only if *all* of its claims follow from the statement
alone. They do not, for these exact reasons.

1. The “direct sign,” “inverse-pair,” “difference,” and especially
   “discriminant” screens are not defined. There is no formula or success
   predicate for them. “Discriminant” is not unambiguous here: for example,
   \((g+w)^2-4gw=(g-w)^2\) is always a square, whereas
   \((g+w)^2-4\) and \((g-w)^2+4\) are different tests. Thus the requested
   screen claims cannot be proved from this source alone. The elementary gcd
   checks that are natural for an inverse pair are verified below.
2. The assertion that the “sole old/new overlap” is
   \(\gcd(1985,3905)=5\) is literally false: \(2\) is an old block, \(2048\)
   is a new endpoint, and
   \[
   \gcd(2,2048)=2.
   \]
   The intended statement “the sole **proper, refinement-causing** old/new
   overlap is \(\gcd(1985,3905)=5\)” is true.
3. The fixed-transcript bound is stated for “endpoint integers,” but its proof
   needs positive, nonzero endpoints. For negative \(x\), the displayed real
   logarithm need not be defined; if \(x=0\), blocks can divide \(x\) while
   its contribution to \(L\) is zero. Under the usual positive-endpoint
   convention, the bound is correct.
4. “Authorize” and “exact positive whole-block occurrence box” are not
   defined in the statement. Under their evident intended meanings (multiply
   the selected relation-side values, and take bounded products with
   nonnegative whole-block exponents), the corresponding conclusions are
   correct, as shown below.

These are specification defects, not defects in the central \(4033\)
construction.

## Refinement accounting

Let \(d(q)\) be the number of nontrivial descendants of an old block \(q\).
Descendants of distinct old blocks cannot coincide: a common nontrivial
descendant would divide two coprime old blocks. Hence the number of
old-derived types after refinement is

\[
\sum_{q\in Q}d(q)=\sum_{q\in Q}(1+(d(q)-1))=r+\sigma.
\]

Every remaining new type divides no old block, and there are \(\nu\) such
types. Therefore

\[
r'=r+\sigma+\nu.
\]

For the transcript bound, assume every endpoint \(x\geq1\), every final block
occurs in an endpoint, and the final blocks are pairwise coprime. Assign each
of the \(R\) blocks to one endpoint containing it. If \(m_x\) blocks are
assigned to \(x\), their product divides \(x\) and is at least \(2^{m_x}\).
Thus

\[
m_x\leq \lfloor\log_2x\rfloor
   \leq \left\lceil\log_2(x+1)\right\rceil.
\]

Summing over endpoints gives \(R\leq L\). Applying the one-step identity at
each refinement and telescoping gives

\[
\sum_t(\sigma_t+\nu_t)
=\sum_t(r_{t+1}-r_t)
=R-r_0\leq L-r_0.
\]

This does not give a polynomial stopping bound for an adaptive run. The
number and sizes of future endpoints, hence final \(L\), are not bounded in
advance by the input length. Moreover, a step can have
\(\sigma_t+\nu_t=0\), so block gain need not count iterations.

## The old subgroup for \(N=4033\)

The cyclotomic polynomial is

\[
\Phi_{36}(X)=X^{12}-X^6+1,
\]

so

\[
\Phi_{36}(2)=4096-64+1=4033=37\cdot109.
\]

The number \(37\) has no prime divisor at most \(\sqrt{37}<7\), and \(109\)
has no divisor among \(2,3,5,7\), the primes at most
\(\sqrt{109}<11\). Thus both are prime. The supplied congruences are
numerically correct:

\[
2^{18}=262144=37\cdot7085-1=109\cdot2405-1,
\]

\[
2^{12}=4096=37\cdot110+26=109\cdot37+63.
\]

Thus \(2^{36}=1\) modulo either prime, while \(2^{18}\ne1\), and the order
divides \(36\) but not \(18\). The only divisors of \(36\) not dividing
\(18\) are \(4,12,36\). Since \(2^{12}\ne1\) in both components, the order
is \(36\) in both.

For \(h=2^k\in H_0\), \(h=1\) in either component exactly when
\(k\equiv0\pmod {36}\), and \(h=-1\) in either component exactly when
\(k\equiv18\pmod {36}\). The same exponent condition holds in both CRT
components. Hence no element has sign \(+1\), or sign \(-1\), in exactly one
component. Since \(N\) has the two prime factors \(37,109\), neither
\(\gcd(h-1,N)\) nor \(\gcd(h+1,N)\) can be a proper factor.

## Immediate-square family

Put

\[
a=2s-1,\qquad b=\frac{2s+1}{3}.
\]

The congruence \(s\equiv1\pmod3\) makes \(b\) integral. The hypotheses force
\(s\geq7\), so both \(a,b\) are odd and greater than one. If \(d\mid a,b\),
then \(d\mid a,3b\), hence
\(d\mid(3b-a)=2\). Since \(d\) is odd, \(d=1\). Therefore

\[
N_s=ab
\]

is the claimed coprime factorization. Also

\[
N_s+1=\frac{4s^2+2}{3}
=2\frac{2s^2+1}{3}.
\]

The second factor is integral and odd. Consequently \(v_2(N_s+1)=1\), so
the square class of \(N_s+1\) is nonzero. Two indexed identical copies have
equal nonzero parity vectors; the kernel on those two indices is exactly
\(\{(0,0),(1,1)\}\). The nonempty dependency is the duplicate pair, and its
positive integer root is \(N_s+1\equiv1\pmod {N_s}\).

Interpreting each copy as the relation

\[
2\frac{2s^2+1}{3}=1+N_s,
\]

selecting both multiplies the two left multipliers and gives \(g=4\). Since

\[
4s^2=1+3N_s
\]

and \(1\leq s^2<N_s\) (the strict inequality is equivalent to
\(s^2>1\)), the canonical inverse is \(w=s^2\). Moreover

\[
gw=(2s)^2.
\]

The square root splits \(N_s\):

\[
\gcd(2s-1,N_s)=a,
\qquad
\gcd(2s+1,N_s)=b.
\]

For the second equality, use \(2s+1=3b\), \(\gcd(a,b)=1\), and
\(a\equiv1\pmod3\). Both gcds are proper and nontrivial.

Now let \(s\equiv55\pmod {1530}\). Then

\[
s\equiv1\pmod9,\qquad s\equiv0\pmod5,
\qquad s\equiv4\pmod {17},
\]

which gives

\[
N_s\equiv1\pmod3,\qquad N_s\equiv3\pmod5,
\qquad N_s\equiv4\pmod {17}.
\]

Thus \(\gcd(N_s,3\cdot5\cdot17)=1\). For \(g=4,w=s^2\), the natural
sign and inverse-pair gcds are all trivial. Indeed, \(g-1=3\), \(g+1=5\),
and \(4w\equiv1\pmod {N_s}\), so the \(w\pm1\) gcds reduce to the same
small primes. Also

\[
4(g-w)=15-3N_s,
\qquad
4(g+w)=17+3N_s.
\]

Since \(N_s\) is odd and coprime to \(15\cdot17\),

\[
\gcd(g-w,N_s)=\gcd(g+w,N_s)=1.
\]

Finally \(gw=(2s)^2\), so the exact-square test succeeds. These calculations
verify all obvious sign/sum/difference gcd screens, but an undefined
“discriminant screen” cannot receive a formal verdict.

For \(s=55\),

\[
s^2=3025,\quad N_s=\frac{12100-1}{3}=4033,\quad
g=4,\quad w=3025,\quad gw=12100=110^2.
\]

The old relation is \(2\cdot2017=4034\), so its distinct old blocks are
\(2,2017\). Appending \(4,3025\) does not split an old block because

\[
\gcd(2017,3025)=1
\quad(2017-2(3025-2017)=1),
\]

and \(4\) only uses the whole old block \(2\). Hence \(\sigma=0\). The new
block \(3025\) divides no old block, so under plain gcd refinement
\(\nu=1\) and total gain is one, not zero. The root is non-global:

\[
110\equiv1\pmod {109},\qquad110\equiv-1\pmod {37},
\]

and it exposes both factors via

\[
\gcd(110-1,4033)=109,\qquad
\gcd(110+1,4033)=37.
\]

Therefore old-block splitting is not necessary for immediately useful
feedback. This example does not have zero total block gain.

## Strict refinement-created expansion for \(N=4033\)

The three relations check exactly:

\[
2\cdot2017=4034=1+4033,
\]

\[
64\cdot3970=254080=1+63\cdot4033,
\]

\[
8\cdot3529=28232=1+7\cdot4033.
\]

Here \(64=2^6\), \(3970=2\cdot1985\), and \(8=2^3\). The odd blocks are
pairwise coprime:

\[
\gcd(2017,1985)=\gcd(2017,3529)
=\gcd(1985,3529)=1.
\]

Thus complete gcd refinement gives

\[
Q_0=\{2,2017,1985,3529\}.
\]

Modulo \(N\), the relations give

\[
2017=2^{-1}=2^{35},\qquad
1985=2^{-7}=2^{29},\qquad
3529=2^{-3}=2^{33},
\]

where exponents are reduced modulo the order \(36\). Since \(2\in Q_0\),

\[
H(Q_0)=\langle2\rangle=H_0.
\]

For the authorized product,

\[
g=2^{11}=2048<4033,\qquad w=3905,
\]

and

\[
2048\cdot3905=7{,}997{,}440
=1+1983\cdot4033.
\]

Thus \(w\) is the canonical inverse and, in particular,
\(w=2^{-11}=2^{25}\in H_0\). Both feedback endpoint residues lie in the old
subgroup.

For the unambiguous elementary screens, the CRT residues are

| quantity | modulo \(37\) | modulo \(109\) |
|---|---:|---:|
| \(g\) | \(13\) | \(86\) |
| \(w\) | \(20\) | \(90\) |
| \(g-1\) | \(12\) | \(85\) |
| \(g+1\) | \(14\) | \(87\) |
| \(w-1\) | \(19\) | \(89\) |
| \(w+1\) | \(21\) | \(91\) |
| \(g-w\) | \(-7\) | \(-4\) |
| \(g+w\) | \(33\) | \(67\) |

No listed residue is zero in either component, so every corresponding gcd
with \(N\) is \(1\). The exact product is not a square:

\[
2827^2=7{,}991{,}929
<7{,}997{,}440
<7{,}997{,}584=2828^2.
\]

This proves failure of the sign, sum, difference, and exact-square checks. It
does not define the requested discriminant check.

For refinement,

\[
\gcd(1985,3905)=5,\qquad
1985=5\cdot397,\qquad3905=5\cdot781.
\]

All other *proper partial* old/new gcds are \(1\). The full containment
\(\gcd(2,2048)=2\) is the additional literal overlap noted in the verdict.
The refined basis is

\[
Q_1=\{2,2017,5,397,3529,781\}.
\]

Only the old block \(1985\) splits, into two descendants, so
\(\sigma=(2-1)=1\). Of the new refined types, \(5\) divides the old block
\(1985\), while \(781\) divides no old block. Hence \(\nu=1\), consistently
with \(6=4+1+1\).

In the appended relation, \(781\) occurs to odd exponent one, and no old
relation contains it. Its parity coordinate therefore forces the coefficient
of the appended relation to be zero in every square-class dependency. No new
dependency involving this relation is created at this step.

The equality of subgroups is

\[
H(Q_1)=\langle H_0,5\rangle.
\]

Indeed, \(397=1985\cdot5^{-1}\) and
\(781=3905\cdot5^{-1}\) modulo \(N\), while \(1985,3905\in H_0\); all other
generators were already in \(H_0\). Strictness follows from

\[
2^{23}=2^{18}2^5\equiv-32\equiv5\pmod {37},
\]

but

\[
2^{23}\equiv-32\equiv77\ne5\pmod {109}.
\]

If \(5=2^k\pmod N\), the order-\(36\) result modulo \(37\) would force
\(k\equiv23\pmod {36}\), contradicting the residue modulo \(109\). Thus
\(5\notin H_0\).

Finally,

\[
x=5\cdot2^{-23}=5\cdot2^{13}\pmod N.
\]

Since \(2^{13}=8192\equiv126\pmod {4033}\),

\[
x\equiv630\pmod {4033},
\qquad
630-1=629=17\cdot37,
\]

and therefore

\[
\gcd(x-1,4033)=37.
\]

The exact positive monoid generated by \(Q_1\), and hence any occurrence-
bounded box inside it, cannot contain the integer \(630\). The blocks
\(2017,3529,781\) exceed \(630\). The remaining block \(397\) does not divide
\(630\), so it also cannot occur in an exact positive product equal to \(630\).
Only \(2\) and \(5\) remain, and their products cannot supply the prime factors
\(3\) and \(7\) in

\[
630=2\cdot3^2\cdot5\cdot7.
\]

By contrast,

\[
5\cdot2^{13}=40960=10\cdot4033+630.
\]

The subgroup statement uses reduction modulo \(4033\); it is not an exact
whole-block product representation of \(630\).

## Classification and limits

Subject to the standard meanings of gcd refinement and generated subgroup,
the concrete example proves:

> Endpoint gcd refinement can expose a generator outside a separator-free old
> subgroup and enlarge it to a subgroup containing a factor-bearing element,
> even though both feedback endpoint residues lie in the old subgroup.

It is one existential example. It proves no uniform selector or sampler,
no polynomial stopping bound, no all-input success theorem, no claim that
\(\sigma\) alone ranks candidates, and no factoring algorithm. The immediate-
square example with \(\sigma=0\) also directly shows that old-block splitting
is not necessary for immediate usefulness.
