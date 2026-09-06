# F151 V2 blind reconstruction

## Evidence boundary and hash

This reconstruction used only `V2_STATEMENT.md` and independent arithmetic.
It did not read a proof, a V1 file, an audit, a manifest, a ledger, or another
F151 artifact.

The SHA-256 digest of the statement is

```text
325c1f8facf40e114586a5e7c1759129d7a422479102f9798da6a5fa42f7dec6
```

It matches the required digest.

## Verdict

**Conditional pass for the mathematical core. Not a literal
self-contained pass.**

The elementary implications in Theorems 1, 2, and 4 reconstruct. The
dimension and ball-counting implication in Theorem 3 also reconstruct. This
uses the two external theorem statements exactly as black-box assumptions.
No reconstructed implication produces a factoring algorithm on every input.

There are two self-containment qualifications.

1. The statement does not define `iota_N`. Theorem 2 reconstructs under the
   evidently intended definition
   \(\iota_N(c)=[c^{-1}]_N\), with both brackets denoting canonical integer
   representatives.
2. The phrases "canonical exact-value decoder" and "factor-free
   refinement" are not defined. Their algorithmic claim cannot be audited
   from the statement. The modular claims and the two concrete integer-effect
   claims do not need those phrases.

The references to P55, P85, P132, and P133 are comparative scope statements,
not self-contained mathematical premises. They are outside this blind
reconstruction.

## External assumptions

I use the following statements without trying to reconstruct their cited
sources.

### Harvey--Hittmeir black box

For an admissible integer target \(B\), a deterministic quasipolynomial-time
call returns either a proper factor of \(N\), or a unit
\(\alpha\in(\mathbb Z/N\mathbb Z)^\times\) with

\[
\operatorname{ord}_N(\alpha)>B.
\]

The statement does not give the theorem's parameter range or its exact
runtime dependence. Those facts are external assumptions. Also, the
procedure is formally stated most cleanly for integer \(B\). If \(B\) is a
real asymptotic bound, all scan limits can instead use \(\lfloor B\rfloor\).

### Pilatte black box

With high probability over the stated random small-prime generators, the
full relation lattice in dimension
\(d=\lceil\sqrt{\log N}\rceil\) has a basis whose vectors have Euclidean norm
at most \(\exp(Cd)\) for a fixed positive constant \(C\).

The distribution, success probability, effective value of \(C\), and any
algorithm that obtains the basis are not present in the statement. I assume
only the displayed existence and norm claim.

## 1. Factor or large order in every prime component

Let

\[
o_r=\operatorname{ord}_r(\alpha)
\]

for a rational prime \(r\mid N\). Suppose the black box did not factor
\(N\), so \(\operatorname{ord}_N(\alpha)>B\).

Assume for contradiction that \(o_r\le B\). At scan exponent \(e=o_r\),

\[
r\mid \alpha^e-1,
\]

so \(D=\gcd(\alpha^e-1,N)>1\). There are two possibilities.

- If \(D<N\), the scan returns a proper factor.
- If \(D=N\), then \(\alpha^e=1\pmod N\). Hence
  \(\operatorname{ord}_N(\alpha)\mid e\le B\), contrary to the black-box
  guarantee.

Therefore a no-factor scan implies

\[
\operatorname{ord}_r(\alpha)>B
\quad\text{for every rational prime }r\mid N.
\]

This argument also covers repeated prime factors of \(N\). It uses only one
prime divisor \(r\), while the case in which the gcd absorbs all of \(N\) is
excluded by the large global order.

There are \(B\) modular-power/gcd tests. They can also be implemented with
successive multiplication. Since
\(B=2^{(\log n)^{O(1)}}\), this extra work is quasipolynomial in the
\(n\)-bit input. Thus Theorem 1 reconstructs, conditional on the external
black box.

This proves no correlation claim beyond the tested congruences
\(\alpha^e=1\pmod r\) for \(e\le B\).

## 2. The short power bank

Set \(L=\lfloor B/4\rfloor\). Use the intended definitions

\[
c_e=[\alpha^e]_N,
\qquad
w_e=[c_e^{-1}]_N=[\alpha^{-e}]_N.
\]

If one of the listed gcds exceeds one, some prime \(r\mid N\) divides its
argument. Reduction modulo \(r\) then gives the following consequences.

| Divisibility modulo \(r\) | Consequence | Positive exponent bounded by |
|---|---|---:|
| \(c_e-c_f=0\) | \(\alpha^{e-f}=1\) | \(|e-f|\le L-1<B\) |
| \(c_e+c_f=0\) | \(\alpha^{e-f}=-1\), hence \(\alpha^{2(e-f)}=1\) | \(2|e-f|\le 2(L-1)<B\) |
| \(c_ec_f-1=0\) | \(\alpha^{e+f}=1\) | \(e+f\le 2L\le B/2\) |
| \(c_ec_f+1=0\) | \(\alpha^{e+f}=-1\), hence \(\alpha^{2(e+f)}=1\) | \(2(e+f)\le4L\le B\) |
| \(c_e-w_e=0\) | \(\alpha^{2e}=1\) | \(2e\le2L\le B/2\) |
| \(c_e+w_e=0\) | \(\alpha^{2e}=-1\), hence \(\alpha^{4e}=1\) | \(4e\le4L\le B\) |

For the first four rows, \(e\ne f\). Thus the exponent in the first two
rows is nonzero. Every row contradicts
\(o_r=\operatorname{ord}_r(\alpha)>B\). Consequently every gcd in (5) and
(6) is one. The floor and equality cases are safe because the order bound is
strict and \(4\lfloor B/4\rfloor\le B\).

This proves, in every prime component, the stated pairwise distinctions,
noninverse relations, and their signed variants. It also proves the two
self-inverse sign screens are null. The result follows from the scan; it
does not require separately computing all \(O(B^2)\) pairwise gcds. Even
that many tests would remain quasipolynomial.

### Exact integer products

By the definition of \(w_e\),

\[
c_ew_e\equiv1\pmod N.
\]

For canonical positive representatives this gives an integer
\(\kappa_e\) with

\[
P_e=c_ew_e=1+\kappa_eN.
\]

The modular screens do not control ordinary factorization or equality of
the integers \(P_e\). Both stated possibilities occur even for a composite
\(N\) on a certified window.

- Let \(N=143=11\cdot13\), \(B=8\), and \(\alpha=2\). The component orders
  are \(10\) and \(12\). For \(e=1,2\), the endpoint pairs are
  \((2,72)\) and \((4,36)\), yet both exact products equal \(144\).
- Let \(N=143\), \(B=8\), and \(\alpha=7\). The component orders are again
  \(10\) and \(12\). The products are
  \(P_1=7\cdot41=287\) and \(P_2=49\cdot108=5292\), and
  \(\gcd(P_1,P_2)=7\), although all listed modular screens are null.

Thus equal exact values through different endpoint pairs and shared integer
factors are genuine residual effects. Whether either effect gives
"progress" in a particular decoder, and what it means to close after
"factor-free refinement", cannot be decided without definitions of that
decoder and refinement.

The theorem says nothing about exponents outside the stated window, order
finding beyond \(B\), or other functions of the exact representatives.

## 3. Dimension, norm, and catalogue size

Since

\[
n=\Theta(\log N),
\]

the stated dimension satisfies

\[
d=\lceil\sqrt{\log N}\rceil=\Theta(\sqrt n).
\]

A vector of Euclidean norm at most \(R=\exp(Cd)\) has each coordinate of
magnitude at most \(R\). One coordinate therefore needs \(O(d)\) bits, and
all \(d\) coordinates need \(O(d^2)=O(n)\) bits. The description of one
vector is compact.

Compact descriptions do not make the complete catalogue small. For the
integer Euclidean ball

\[
\mathcal B_d(R)=\{v\in\mathbb Z^d:\lVert v\rVert_2\le R\},
\]

the containing cube gives

\[
|\mathcal B_d(R)|\le(2R+1)^d=\exp(O(d^2)).
\]

The cube with coordinate radius \(R/\sqrt d\) is contained in the ball, so

\[
|\mathcal B_d(R)|
\ge
\left(2\left\lfloor\frac R{\sqrt d}\right\rfloor+1\right)^d
=\exp(\Theta(d^2)).
\]

Together these give

\[
|\mathcal B_d(\exp(Cd))|=\exp(\Theta(d^2))=\exp(\Theta(n)).
\]

This is exponential in the input length, not quasipolynomial in it. The
\(\Theta\) count refers to enumerating the full radius-\(\exp(Cd)\) ball.
From the notation \(\exp(O(d))\) alone, without fixing an effective
constant, one should state only that a chosen theorem-level upper ball has
this count.

A Euclidean norm bound gives no support bound. For example, a vector can
have all \(d\) coordinates nonzero while having norm far below
\(\exp(Cd)\). Therefore the external existence theorem alone does not
place a promised basis vector in a polylogarithmic-support catalogue.

This is only a limitation of what follows from the cited norm theorem. It is
not a lower bound against a structured sampler, and it does not prove that
the promised basis vectors are actually dense.

## 4. The scalar-order/Jacobi-torus splice

Now let \(N=pq\) for distinct odd primes, and write \(\chi_r\) for the
Legendre symbol modulo \(r\). Because

\[
\left(\frac\Delta N\right)=\chi_p(\Delta)\chi_q(\Delta)=-1,
\]

exactly one component is split
\((\chi_r(\Delta)=1)\), and the other is nonsplit.

In either component, direct expansion of
\(x=(\alpha+\alpha^{-1})/2\) gives

\[
x^2-1
=\left(\frac{\alpha-\alpha^{-1}}2\right)^2.
\]

The squared factor is nonzero. Otherwise \(\alpha^2=1\pmod r\), which
would give \(\operatorname{ord}_r(\alpha)\le2\), contrary to
\(\operatorname{ord}_r(\alpha)>B\ge4\). Hence

\[
\begin{aligned}
\chi_r(b)
&=\chi_r(\Delta^{-1})
  \chi_r\!\left(\left(\frac{\alpha-\alpha^{-1}}2\right)^2\right)\\
&=\chi_r(\Delta).
\end{aligned}
\]

This proves (13).

The fixed-\(x\) norm equation is equivalent locally to

\[
y^2=\Delta^{-1}(x^2-1)=b.
\]

It therefore has a solution in exactly the split component. A solution
modulo \(N=pq\) would, by reduction or CRT, require a solution in both
components. None exists. In the split component, a choice
\(s^2=\Delta\) gives the familiar lift

\[
y=\frac{\alpha-\alpha^{-1}}{2s},
\qquad
x+sy=\alpha.
\]

There is no global square root \(s\) and, more decisively, no global \(y\)
for this fixed \(x\). Thus the direct scalar-to-global-torus lift fails.

### Chebyshev projection, including \(m=0\)

Let

\[
S_m=\frac{\alpha^m+\alpha^{-m}}2.
\]

Since \(N\) is odd, division by two is valid. Direct multiplication gives

\[
S_0=1,\qquad S_1=x,\qquad
S_{m+1}=2xS_m-S_{m-1}.
\]

These are the initial values and recurrence for the first-kind Chebyshev
polynomials. Therefore

\[
T_m(x)=S_m=\frac{\alpha^m+\alpha^{-m}}2
\]

for every integer \(m\ge0\). The \(m=0\) case is exactly \(1=1\).

The displayed Kummer orbit has no \(\Delta\) in its formula. Thus the
direct Chebyshev relations of this fixed scalar source do not retain the
split/nonsplit label forced by \(\Delta\). This does not prove that an
arbitrary choice rule for \(\alpha\) cannot correlate \(x\) with a factor,
nor does it rule out factor information in larger exponents, extra
coordinates, or formulas that also use \(\Delta\).

## Exact scope and exclusions

The reconstruction supports exactly the following boundary.

1. Subject to the Harvey--Hittmeir black box, the extra scan gives a
   deterministic quasipolynomial source whose every prime-component order
   exceeds \(B\).
2. That order bound removes precisely the listed signed collision and
   inverse screens for \(1\le e,f\le\lfloor B/4\rfloor\). It does not
   control the exact integers \(c_e w_e\).
3. Subject to the Pilatte black box, a short basis exists with high
   probability and each vector has a polynomial-size description. Exhaustive
   enumeration of the full promised ball is exponential. No classical
   sampling lower bound follows.
4. The direct scalar construction gives a local torus point in only one
   component, while its Kummer recurrence forgets the explicit Jacobi
   orientation. This does not exclude other torus points, multi-coordinate
   decoders, or a separate torus win--win theorem.

In particular, none of the reconstructed results excludes component-order
mismatches after \(B\), larger exponents, exact-representative arithmetic,
structured relation samplers, or non-Kummer torus coordinates. The four
"live options" at the end of the statement are research directions, not
deductions that can be proved or refuted from the statement alone.
