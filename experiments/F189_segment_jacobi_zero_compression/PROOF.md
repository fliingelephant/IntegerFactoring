# Proof of the F189 segment-Jacobi candidate

## 1. The zero predicate for every odd modulus

Write the hidden prime-power factorization as

\[
 N=\prod_{j=1}^s r_j^{e_j}.
\]

By the definition of the Jacobi symbol,

\[
 \chi_N(x)=\prod_{j=1}^s
 \left(\frac{x}{r_j}\right)^{e_j}.
\]

If some \(r_j\mid x\), one factor is zero. If no \(r_j\mid x\), every factor
is \(1\) or \(-1\), so the square of the product is one. Therefore

\[
 \chi_N(x)^2=\mathbf 1_{\gcd(x,N)=1},
\]

which proves (2). Complete multiplicativity in the numerator gives

\[
 J_N(a,L)
 =\chi_N\!\left(\prod_{t=0}^{L-1}(a+t)\right).
\]

The product is zero exactly when at least one factor is a nonunit. This
proves (3) for arbitrary odd \(N\), including repeated prime factors.

## 2. Totalized Gauss-floor reciprocity

Fix positive odd \(x,N\), and put \(g=\gcd(x,N)\). Consider the rectangle

\[
 1\le i\le\frac{N-1}{2},
 \qquad
 1\le j\le\frac{x-1}{2}.
\]

For fixed \(i\), the number of \(j\) in this rectangle satisfying
\(jN\le ix\) is

\[
 \left\lfloor\frac{ix}{N}\right\rfloor.
\]

Thus \(F(x,N)\) counts the points on or below the line \(jN=ix\).
Similarly, \(F(N,x)\) counts the points on or above the same line. Every
point off the line is counted exactly once, and every point on the line is
counted twice.

The positive solutions on the line are

\[
 i=k\frac{N}{g},
 \qquad
 j=k\frac{x}{g}.
\]

Because \(g\) is odd, the rectangle contains exactly

\[
 k=1,\ldots,\frac{g-1}{2},
\]

so there are \((g-1)/2\) equality points. The rectangle itself has

\[
 \frac{(N-1)(x-1)}4
\]

points. This proves (5).

The two displayed terms in (5) are integers: each of \(x-1,N-1\) is even,
and \(g-1\) is even. When \(g=1\), Eisenstein's lemma for Jacobi symbols is
exactly (6). When \(g>1\), its parity expression remains in
\(\{1,-1\}\), while the Jacobi symbol is zero. The extra equality-line count
is therefore the exact correction missing from the coprime identity.

Multiplying (5) by two, subtracting the rectangular main term, and summing
over \(\mathcal A\) proves (8). Every summand in (7) is nonnegative and is
zero exactly for a unit. Hence \(G_N(\mathcal A)=0\) exactly when all
members of \(\mathcal A\) are units.

## 3. Even terms do not change the correction

Since \(N\) is odd,

\[
 \gcd(2^ju,N)=\gcd(u,N)
\]

for every \(j\ge0\). For a positive segment below \(2N\), group its nonzero
members according to their exact two-adic valuation. At valuation \(j\),
division by \(2^j\) leaves an arithmetic segment of odd integers with step
two. There are at most

\[
 1+\lfloor\log_2(2N-1)\rfloor=O(n)
\]

nonempty strata. Applying (8) pointwise on these odd values recovers the
same hidden-divisor hit count as the original segment. A zero integer, if
present, is publicly recognizable and has gcd \(N\).

This stratification changes neither the exact predicate nor the asymptotic
number of symbolic strata. It does not evaluate the bilinear and
varying-denominator floor sums in (8).

## 4. One-child binary isolation

Suppose \([a,a+L)\) is known to have zero segment product and contains no
multiple of \(N\). If \(L=1\), equation (3) gives

\[
 1<\gcd(a,N)<N.
\]

For \(L>1\), split it into a left interval of length
\(L_0=\lfloor L/2\rfloor\) and a right interval of length \(L-L_0\). Query
the oracle only on the left. If the answer is zero, retain the left. If the
answer is nonzero, every left member is a unit; since the parent contains a
nonunit, the right child must contain one, so retain the right without a
second query.

Each step at least halves the retained length. After
\(\lceil\log_2L\rceil\) calls, one nonunit \(x\) remains. The exclusion of
multiples of \(N\) makes its gcd proper. This proves the conditional
isolation theorem.

If one oracle call costs \(Q(n)\), the isolation costs
\(O(nQ(n))\). Multiplication by a polynomial in \(n\) preserves a fixed
quasipolynomial bound.

## 5. Affine normalization and the exact source law

Assume (13). Once the gcd screens certify that \(U,V\) are units, \(V^{-1}\)
exists and

\[
 U+tV\equiv V(a+t)\pmod N,
 \qquad a=UV^{-1}\pmod N.
\]

Multiplication by the unit \(V\) preserves all gcd-zero positions. If \(U\)
and \(V\) are independent uniform units, their quotient \(a\) is a uniform
unit.

Starting from uniform residues does not make the conditioning expensive.
One residue is a unit with probability

\[
 \frac{\varphi(N)}N
 =\left(1-\frac1p\right)\left(1-\frac1q\right)>\frac12.
\]

A gcd strictly between one and \(N\) already factors \(N\); the residue zero
is the only case with gcd \(N\) and can be resampled. Thus two unit samples,
or an earlier factor, are obtained in expected constant trials.

For a hidden prime \(r\in\{p,q\}\), the residue \(-a\pmod r\) is uniform in
\(\{1,\ldots,r-1\}\). Because \(T<r\), the segment contains an \(r\)-multiple
exactly when this root position lies in \(\{1,\ldots,T-1\}\). Its probability
is therefore

\[
 \alpha_r=\frac{T-1}{r-1}.
\]

The CRT identifies the global unit group with the product of the two local
unit groups, so the two root positions are independent. Inclusion-exclusion
proves (17).

There is at most one local root for each prime. A zero is unhelpful exactly
when the two local roots are the same \(t\in\{1,\ldots,T-1\}\). For every
such \(t\), the single unit class \(a\equiv-t\pmod N\) realizes it. The
unit group has \((p-1)(q-1)\) elements, so (18) follows. In every other zero
case, each zero position has gcd \(p\) or \(q\), and binary isolation returns
a proper factor. Subtracting (18) from (17) proves (19).

It remains to justify the scale and the stated constant. From (14),

\[
 \frac{\lfloor\sqrt N\rfloor}{16}<T
 \le\frac{\lfloor\sqrt N\rfloor}{8}.
 \tag{29}
\]

Since \(q<2p\), one has \(q<\sqrt{2N}\), while
\(T<\sqrt N/8<\sqrt2p/8<p\). Thus all probability formulas above use
distinct root positions as claimed. Also

\[
 \alpha_q
 >\frac{\sqrt N-17}{16\sqrt{2N}}
 >\frac{36}{848\sqrt2},
\]

because \(\sqrt N>p\ge53\). The event that the \(q\)-root occurs but is not
the global aligned root has probability

\[
 \alpha_q-\beta
 =\alpha_q\left(1-\frac1{p-1}\right)
 >\frac{36}{848\sqrt2}\frac{51}{52}
 >\frac1{40}.
\]

For the last inequality, use \(\sqrt2<3/2\):

\[
 \frac{36}{848\sqrt2}\frac{51}{52}
 >\frac{3}{106}\frac{51}{52}
 =\frac{153}{5512}
 >\frac1{40}.
\]

This event is contained in the useful event, proving the final assertion.

## 6. Fourier support and linear recurrences

Let \(m=\operatorname{rad}(N)\) and view all functions in this section on
\(\mathbb Z/m\mathbb Z\). Put

\[
 u_N(x)=\chi_N(x)^2=\mathbf 1_{\gcd(x,m)=1}.
\]

The Fourier transform of \(u_N\) is the Ramanujan sum. Because \(m\) is
squarefree, its CRT factorization is a product over primes \(\ell\mid m\)
of local sums

\[
 \sum_{y\in\mathbb F_\ell^\times}
 e^{-2\pi i ky/\ell}
 =
 \begin{cases}
 \ell-1,&\ell\mid k,\\
 -1,&\ell\nmid k.
 \end{cases}
 \tag{30}
\]

Every factor is nonzero. Hence every Fourier coefficient of \(u_N\) is
nonzero. Since \(z_N=1-u_N\), its zero-frequency coefficient is

\[
 m-\varphi(m)>0,
\]

and every nonzero-frequency coefficient is the negative of the corresponding
nonzero coefficient of \(u_N\). Thus \(z_N\) has all \(m\) Fourier modes.
In particular, a period of \(z_N\) must preserve every \(m\)-th Fourier
root, so its least period is \(m\).

For a periodic complex sequence, a polynomial in the shift operator
annihilates the sequence exactly when it vanishes on every Fourier root with
nonzero coefficient. All \(m\)-th roots occur here, so the minimal
annihilating polynomial is \(X^m-1\), of degree \(m\).

Now specialize to \(N=pq\). Let

\[
 \delta_p(x)=\mathbf1_{p\mid x},
 \qquad
 \delta_q(x)=\mathbf1_{q\mid x}
\]

on \(\mathbb Z/N\mathbb Z\). The Fourier transform of \(\delta_p\) is
supported exactly on the \(p\) frequencies divisible by \(q\), and that of
\(\delta_q\) exactly on the \(q\) frequencies divisible by \(p\). Their
supports meet only at zero and their nonzero values cannot cancel. Therefore
\(c_N=\delta_p+\delta_q\) has \(p+q-1\) Fourier modes. Its Fourier roots are
the union of the \(p\)-th and \(q\)-th roots of unity. The minimal
annihilator is consequently

\[
 \operatorname{lcm}(X^p-1,X^q-1)
 =\frac{(X^p-1)(X^q-1)}{X-1},
\]

of degree \(p+q-1\).

## 7. Exact finite-automaton state count

Again let \(m=\operatorname{rad}(N)\), and let

\[
 S=\{x\pmod m:\gcd(x,m)>1\}.
\]

Tracking the binary input value modulo \(m\) gives a DFA with \(m\) states,
so \(m\) is an upper bound.

The set \(S\) has no nonzero additive stabilizer. Indeed, fix
\(d\not\equiv0\pmod m\), and choose a prime \(r\mid m\) for which
\(d\not\equiv0\pmod r\). By CRT choose \(x\) with \(x\equiv0\pmod r\) and,
for every prime \(\ell\mid m\), choose its local residue so that
\(x\not\equiv-d\pmod\ell\). Such a choice exists because every \(\ell\) is
odd. Then \(x\in S\), while \(x+d\) is a unit modulo every prime dividing
\(m\). Thus \(S+d\ne S\).

Take two distinct residue states \(r_0,s_0\pmod m\). Choose \(k\) with
\(2^k>m\). Since \(m\) is odd,

\[
 d=2^k(r_0-s_0)\not\equiv0\pmod m.
\]

The trivial-stabilizer result supplies \(u\) whose membership in \(S\)
differs from that of \(u+d\). Choose the \(k\)-bit suffix value

\[
 y\equiv u-2^ks_0\pmod m,
 \qquad 0\le y<m<2^k.
\]

Appending this same suffix sends \(s_0\) to \(u\) and \(r_0\) to \(u+d\),
which have different acceptance values. All \(m\) residues are reachable,
so all state pairs are distinguishable. The minimal DFA therefore has
exactly \(m\) states.

## 8. Factorial identity and the hidden-base carry

The integer identity

\[
 R_{a,L}=L!\binom{a+L-1}{L}
\]

proves (25). If \(r\mid N\) is prime and \(L<r\), then \(r\nmid L!\), so
the two divisibility conditions in (26) are equivalent.

Kummer's theorem identifies the \(r\)-adic valuation of the binomial
coefficient with the number of carries when adding \(L\) and \(a-1\) in
base \(r\). Because \(L\) has one base-\(r\) digit, any carry must begin in
the low digit. Such a carry occurs exactly when

\[
 ((a-1)\bmod r)+L\ge r.
\]

This is also the direct condition that one of
\(a,a+1,\ldots,a+L-1\) is divisible by \(r\). The identity is exact for
every hidden prime, including primes below repeated prime-power components.

## 9. Scope of the obstructions

On a balanced squarefree semiprime, \(m=N=2^{\Theta(n)}\) and
\(p+q-1=2^{\Theta(n)}\). Sections 6 and 7 therefore exclude QP-size
explicit Fourier lists, constant-coefficient recurrence tables, and finite
automata.

These are representation lower bounds only. A single gcd computes one
value of \(z_N\) in polynomial time despite the DFA state bound. Nonlinear
arithmetic circuits, implicit determinants, algorithms that reuse variables,
and a new aggregate gcd method are not covered. The proof therefore stops at
the exact reduction (8) and the conditional oracle theorem rather than
claiming that segment zero evaluation is impossible.
