# F242 V2 focused hostile re-audit

## Verdict

**PASS.** V2 removes the only self-containment defect identified in the V1
strict reconstruction. The replacement boundary claim follows directly from
the four-orientation theorem. The exact shifted-gcd, sampler, torus-arithmetic,
Miller, orientation, and conditional-complexity core has no mathematical
change and survives fresh hostile checks.

This verdict is limited to the claimed V2 repair and absence of regression in
that exact core. It does not promote F242 into an all-input factoring result or
supply the missing word source.

## Authenticated frozen inputs

All five supplied files were hashed before they were read. The observed
SHA-256 digests matched the supplied values exactly:

```text
4ec456a0aa8794e36497a663b14747eba15dcaebd7984a923b53169969c1bfbd  V2_STATEMENT.md
8012cc4899226fec123a9f86d150e3dbe8fa199df88c4ee95651c3e0557f2090  V2_PROOF.md
5365e011209e0d1a9137f14a49918df4b4ff297df1b944c2ecaac6a52542a9f5  V2_SELF_AUDIT.md
640204bfc0b464c315c949a7508478c25dd9787cea230bf0abd2a4688e9dbc2a  V2_PROVENANCE.md
36da9286189a696cd17a849e411de387f573a4c509367b8064caa6d092a36ce4  V2_MANIFEST.md
```

## 1. The claimed repair is complete

A direct V1-to-V2 diff shows that the mathematical core of the statement is
byte-for-byte unchanged. Apart from the title, the only statement change is
the deletion of the P158/F172 paragraph and its replacement by a generic
scope boundary. The proof has the corresponding title change and replaces
only the P158/F172 subsection. No formula, algorithmic step, hypothesis, or
complexity assertion in the exact core changed.

The deleted V1 claim needed facts that V1 did not state: the definition of the
named family and a size relation forcing its smaller prime to be exponential
in the input length. V2 makes neither claim.

The replacement is self-contained. For fixed \(W\), the definitions

\[
 m_i=i-\epsilon_i,
 \quad d=\gcd(m_p,m_q),
 \quad r_i=\frac{m_i/d}{\gcd(m_i/d,W)}
\]

show that the residual pair is determined by
\((\epsilon_p,\epsilon_q)\). There are exactly four sign pairs. Therefore
varying \(D\) while keeping \(W\) fixed supplies only those four residual
laws. Equations (6)--(9) are conditional bounds in terms of the resulting
\(r_i\); they contain no argument that bounds any \(r_i\) above on every
input. Thus the replacement claim introduces no external premise.

The phrase “ordinary P205 pair” is only a provenance label. Its complete
mathematical content is stated locally: the \((+,+)\) orders are
\((p-1,q-1)\). No P205 theorem is used as a premise.

## 2. Shifted-gcd and exact return law

For either local index \(i\), the core congruence remains valid in all four
orientations. Explicitly,

\[
 N-J=q(p-\epsilon_p)+\epsilon_p(q-\epsilon_q)
\]

and its symmetric counterpart give

\[
 \gcd(N-J,m_p)=\gcd(m_p,m_q)=d,
 \qquad
 \gcd(N-J,m_q)=d.
\]

Writing \(N-J=dA_i\) gives \(\gcd(A_i,s_i)=1\), so

\[
 \gcd(E,m_i)=d\gcd(W,s_i).
\]

The kernel of exponentiation by \(E\) in the cyclic group of order
\(m_i=ds_i\) therefore has relative size

\[
 \frac{d\gcd(W,s_i)}{ds_i}=rac1{r_i}=\alpha_i.
\]

This uses no factorization of \(W\). No hidden local sign is needed by the
algorithm: it uses only the public Jacobi product \(J=(D/N)\).

Hostile edge checks found no parity exception. Both \(m_i\) and \(N-J\) are
even for odd \(N\) and \(J\in\{\pm1\}\), hence \(e_i,v,h_i\ge1\).

## 3. Exact full-torus sampler

For a hidden odd prime \(r\), the local algebra is either
\(\mathbb F_r\times\mathbb F_r\) or \(\mathbb F_{r^2}\). In the split case,
the map \(z\mapsto z/\bar z\) has fibres

\[
 (ty,y),\qquad y\in\mathbb F_r^\times,
\]

over \((t,t^{-1})\). In the nonsplit case its kernel is
\(\mathbb F_r^\times\). Thus every local fibre has exactly \(r-1\) elements,
and the image is the full cyclic norm-one torus of order
\(r-\epsilon_r\). Both \(+1\) and \(-1\) occur. There is no omitted
Cayley-chart point.

CRT makes the two raw local algebra elements independent. Conditioning on
the product event that both are units preserves independence and uniformity.
The local unit density is

\[
 \left(1-\frac1r\right)
 \left(1-\frac{\epsilon_r}{r}\right),
\]

which is at least \(4/9\). The global clean probability is therefore at
least \(16/81\), and the stated expected sampling bound follows.

The hostile denominator check also passes. The coefficient gcd detects a
local zero. The norm gcd detects every nonunit, including a nonzero zero
divisor in a split algebra. Formula (2) takes its only inverse after this
norm is certified as a unit. Formula (3) is the quotient-ring product and
uses no later division or square root.

Early sampler exits do not bias the clean law. If one raw draw is classified
as factor, clean point, or rejection, summing over any number of preceding
rejections multiplies every clean-point atom by the same geometric factor.
A proper gcd is already success. It can therefore only improve the complete
procedure relative to the clean powered probability.

## 4. Identity screens and unequal-kernel Miller law

The use of both coordinates in

\[
 G_\pm(Y)=\gcd(N,y_0\mp1,y_1)
\]

is exact: a hidden prime divides the gcd if and only if its local point is
the indicated signed identity. Thus every proper result is a verified
factor, and neither a nonscalar point nor a one-coordinate coincidence can
cause a false return.

Conditional on \(U_i^E=1\), the local point is uniform in the power-map
kernel. After raising by the odd part \(u\), its odd component is killed and
its two-primary component is uniform in \(C_{2^{h_i}}\). If \(K_i\) is the
base-two exponent of its exact order, including \(K_i=0\) for the identity,
then

\[
 \Pr(K_i=0)=2^{-h_i},
 \qquad
 \Pr(K_i=j)=2^{j-1-h_i}\quad(1\le j\le h_i).
\]

Repeated squaring exposes a factor exactly when \(K_p\ne K_q\). This remains
true when one exponent is zero and when \(h_p\ne h_q\). If the exponents are
equal, both components meet \(-1\) and then \(+1\) simultaneously; before
that neither is a signed identity. If they differ, the smaller-order
component reaches \(+1\) first, so \(G_+\) is proper at that stage.

With \(a=\min(h_p,h_q)\) and \(b=\max(h_p,h_q)\), the exact mismatch law is

\[
\begin{aligned}
 \mu_{a,b}
 &=1-\sum_{j=0}^{a}\Pr(K_a=j)\Pr(K_b=j)\\
 &=1-\frac{1+\sum_{j=1}^{a}4^{j-1}}{2^{a+b}}\\
 &=1-\frac{4^a+2}{3\,2^{a+b}}.
\end{aligned}
\]

Its failure probability is largest at \(b=a\), where it is at most
\(1/2\) for \(a\ge1\). Hence \(\mu_{a,b}\ge1/2\). No equal-kernel
specialization has been smuggled into the unequal-kernel case.

## 5. Exact powered probability and lower bound

The three disjoint return cases give

\[
\begin{aligned}
 S
 &=\alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p)
   +\mu_{a,b}\alpha_p\alpha_q\\
 &=\alpha_p+\alpha_q-(2-\mu_{a,b})\alpha_p\alpha_q.
\end{aligned}
\]

This is exact for the clean powered phase as claimed. If
\(x=\max(\alpha_p,\alpha_q)\), the two sign cases for
\(1-(2-\mu)x\) give

\[
 S\ge\mu x.
\]

Consequently

\[
 S\ge\frac1{2\min(r_p,r_q)}.
\]

Independent fresh clean points therefore give an almost-sure geometric
stopping time with expectation at most \(2R\) when
\(\min(r_p,r_q)\le R\). This claim is local to the fixed orientation; the
four-orientation average below has its separately stated constant loss.

## 6. Four orientations and rejection order

A uniform unit \(D\bmod N\) has independent uniform Legendre signs by CRT,
so all four orientations have probability \(1/4\). The clean densities in
the split and nonsplit algebras are unequal. Keeping \(D\) while resampling
only \((A,B)\) is therefore necessary and sufficient to preserve the
uniform orientation law. Rejecting the full triple would bias it, exactly as
V2 warns.

For \(R_\epsilon=\min(r_p,r_q)\) in orientation \(\epsilon\),

\[
 \frac14\sum_\epsilon S_\epsilon
 \ge\frac18\sum_\epsilon\frac1{R_\epsilon}
 \ge\frac1{8\min_\epsilon R_\epsilon}.
\]

The direction of the final inequality is correct: the sum contains the
reciprocal of the smallest \(R_\epsilon\). Fixed \(W\) makes every quantity
in this law depend on \(D\) only through its two signs. Allowing a
materially \(D\)-dependent word is correctly excluded as a new source
problem.

## 7. Complexity and scope

The exponent has \(O(\log N+\log W)\) bits. Binary powering and the square
chain use a polynomial number of operations in that length. All stored ring
coefficients are reduced modulo \(N\), and the constant-expected sampler,
gcds, inverses after certification, Jacobi symbols, and verification have
polynomial bit cost. Multiplying this per-trial bound by \(2R\) proves the
claimed conditional numerical-quasipolynomial bound when both \(\log W\)
and \(R\) have the stated size.

V2 still expressly does not construct \(W\), prove that one of the four
residuals is small, cover inputs beyond distinct odd semiprimes, or reduce
recursively to complete factorization. The repaired scope is therefore
accurate and does not claim the root all-input result.

## Final hostile conclusion

No surviving objection was found within the requested scope. The V1
self-containment failure has been removed, and the exact core has no
regression. **PASS.**
