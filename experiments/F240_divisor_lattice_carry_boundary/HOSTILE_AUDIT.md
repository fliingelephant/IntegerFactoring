# F240 hostile audit

## Verdict

**FAIL.** All five supplied SHA-256 values match, and the centered-carry
identity, the `d=2` offsets, the divisor-only support optimum, the residual
window contrapositive, and the divisor-count warning are correct at their
stated scopes. However, the packet makes an unqualified direct-factor-bank
claim that is false for an allowed true tuple.

The exact defect is at `STATEMENT.md` lines 263--264, with the same missing
qualification already visible at lines 104--108. For every allowed
semiprime, the choice

\[
B=M=N-1,\qquad u=1
\]

gives the true tuple

\[
(B,u,a,b,c)=(M,1,0,0,1).
\]

Its discriminant is the square zero, but equation (3) is the zero
polynomial. It supplies no candidate factor. Thus constant banks containing
the two correct centers and the correct carry do **not** always give the
claimed direct factor bank. The proof notices the degenerate equation, but
its assertion that the statement makes no bank-success claim for it is
contradicted by the statement itself. The same contradiction appears in
`SELF_AUDIT.md` item 5.

The minimal repair is to restrict candidate recovery and the direct
factor-bank corollary to a true tuple with

\[
(a,b)\ne(0,0).
\]

Equivalently, when `b=0`, the packet must require `a>0`; otherwise equation
(3) must be declared degenerate and skipped. I found no further defect.

I did not edit a frozen input or a durable ledger. I ran no mathematical
search or numerical experiment. I wrote only this audit.

## 1. Frozen-input integrity

I listed filenames without opening the packet, then recomputed the five
supplied hashes before reading any frozen content. Every value matched.

| Artifact | Expected and observed SHA-256 | Result |
|---|---|---|
| `STATEMENT.md` | `a9e57ccf65bcc793bccf844fb74216742acaecabe77d4e34ec9946ffb98015b9` | match |
| `PROOF.md` | `d8a1df081ee5c8c52a4515c1f0370486a8546a3a4589dce3bd76732fa0a76015` | match |
| `SELF_AUDIT.md` | `a7ac335219c52fb61f881eddfbc26fde16f2f7bff32fa5cd2a968b46fa8e24c2` | match |
| `PROVENANCE.md` | `521b31b7e210516311427ada75b6a719997ca76df9c71d9f35a8d990bc097361` | match |
| `MANIFEST.md` | `99affe0665add866d18b15bf2583cca8cba2a45327645849cce06c96be446caa` | match |

## 2. General centered-carry algebra

Round-half-up gives

\[
a-\frac12\le \frac{up}{B}<a+\frac12,
\]

and hence

\[
-\frac B2\le x=up-aB<\frac B2.
\]

The same argument applies to `y`. Since `B | N-1`,

\[
xy\equiv (up)(uq)=u^2N\equiv u^2\pmod B.
\]

Therefore

\[
c=\frac{xy-u^2}{B}\in\mathbb Z.
\]

Expanding the product and using `N=1+BH_B` and `xy=u^2+cB` gives

\[
u^2H_B=abB+ay+bx+c. \tag{A1}
\]

Independently,

\[
u(aq+bp)=2abB+ay+bx.
\]

Subtracting (A1) gives the stated sign and trace formula:

\[
uT=u^2H_B+abB-c,
\qquad T=aq+bp.
\]

The true `T` is an integer. Substitution of `N=pq` then gives

\[
bp^2-Tp+aN=0
\]

and

\[
T^2-4abN=(aq+bp)^2-4abpq=(aq-bp)^2.
\]

Thus all displayed algebraic identities in Theorem A are correct.

The offset bounds are also correct. If `|x|<=X`, then `|y|<B/2`, so

\[
|c|\le \frac{|x||y|+u^2}{B}
\le \frac X2+\frac{u^2}{B}.
\]

If `|c|<=C`, then

\[
|xy|=|u^2+cB|\le u^2+CB.
\]

At least one of two real factors has absolute value at most the square root
of their absolute product. This proves

\[
\min(|x|,|y|)\le\sqrt{u^2+CB}.
\]

This bound is only at square-root scale. It does not identify a factor, its
sign, or which centered residue is smaller.

## 3. The missing nondegeneracy condition

For distinct odd primes `p<q`, one has `p>=3` and `q>=5`. With `B=M` and
`u=1`,

\[
2p<pq-1
\quad\Longleftrightarrow\quad
p(q-2)>1,
\]

and

\[
2q<pq-1
\quad\Longleftrightarrow\quad
q(p-2)>1.
\]

Both inequalities are strict. Consequently

\[
0<\frac pM,\frac qM<\frac12,
\]

so round-half-up gives

\[
a=b=0,
\qquad x=p,
\qquad y=q.
\]

Since `xy=N`,

\[
c=\frac{N-1}{M}=1,
\qquad H_B=1,
\qquad T=0.
\]

Equation (3) is therefore

\[
0X^2-0X+0=0.
\]

It is not a linear equation and it imposes no condition on `X`. The square
test also gives only `0`, so exact division has no candidate to test. The
correct values `a=0`, `b=0`, and `c=1` lie in constant-size banks, which is
a direct counterexample to the claim at `STATEMENT.md` lines 263--264.

The proof at lines 122--126 correctly says that equation (3) can degenerate.
It then incorrectly says that the statement makes no bank-success claim in
that case. `SELF_AUDIT.md` lines 41--44 repeats the same incorrect reading of
the statement.

The repair is exact. If `b!=0`, equation (3) is a genuine quadratic and one
root is `p`. If `b=0` but `a>0`, then

\[
T=aq>0,
\qquad -TX+aN=0,
\]

so the unique root is

\[
X=\frac{aN}{T}=p.
\]

If `a=0` and `b>0`, the quadratic has roots `0` and `p`, and exact division
selects the nontrivial factor. Hence `(a,b)!=(0,0)` is sufficient and is the
precise missing hypothesis.

## 4. The P205 common-divisor point

From

\[
p-1=ds_p,
\qquad q-1=ds_q,
\qquad \gcd(s_p,s_q)=1,
\]

direct expansion gives

\[
M=d(s_p+s_q+ds_ps_q). \tag{A2}
\]

Thus `d | M`. If

\[
A=M/d=s_p+s_q+ds_ps_q,
\]

then

\[
A\equiv s_q\pmod {s_p},
\qquad A\equiv s_p\pmod {s_q}.
\]

The residuals are coprime, so `A` is coprime to each one. Therefore, for
every prime `ell | s_i`,

\[
v_\ell(M)=v_\ell(d),
\]

and in particular `ell | M` exactly when `ell | d`. The packet does not
overstate this as equality of the valuations in `s_i` and `M`.

Both `p-1` and `q-1` are even, so `d` is even. At `B=d` and `u=1`, if
`d>=4`, then

\[
\frac pd=s_p+\frac1d,
\qquad 0<\frac1d<\frac12.
\]

Hence `a=s_p` and `x=1`; similarly `b=s_q` and `y=1`. Thus `c=0`.

If `d=2`, then

\[
\frac p2=s_p+\frac12.
\]

The declared half-up convention selects `a=s_p+1`, not `s_p`, and

\[
x=p-2(s_p+1)=-1.
\]

Likewise `b=s_q+1` and `y=-1`, so `c=0`. The packet handles the unique tie
correctly.

## 5. Residual-window direction

For every real public bound `R>=1`, the positive identity `p-1=ds_p` gives

\[
s_p\le R
\quad\Longleftrightarrow\quad
d\ge\frac{p-1}{R}.
\]

Also `d<=p-1` and `d | M`. Therefore `s_p<=R` places the particular divisor
`d` in

\[
\left[\frac{p-1}{R},p-1\right].
\]

Its contrapositive is exactly the stated implication: if that interval
contains no divisor of `M`, then `s_p>R`. An unrelated divisor in the
interval need not equal `d`, so its presence gives no converse. The same
argument applies to `q`. Nothing in this order argument controls prime
factors of the residual, so the refusal to infer smoothness is necessary.

## 6. Divisor-only support optimum

Every prime in a word

\[
W=\prod_j B_j^{e_j},
\qquad B_j\mid M,
\qquad e_j\ge0,
\]

divides `M`. Gcd, lcm, and integer exact division between such words cannot
introduce a prime outside that support. Hence every primary part
`ell^e || s_i` with `ell` not dividing `M` is coprime to `W` and survives
in

\[
\frac{s_i}{\gcd(s_i,W)}.
\]

Multiplying these surviving primary parts proves

\[
s_i^{\perp M}\mid\frac{s_i}{\gcd(s_i,W)}.
\]

Now `n=ceil(log_2(N+1))` implies

\[
s_i<N<2^n.
\]

Therefore `v_ell(s_i)<n` for every prime `ell`. If `ell | M`, then

\[
v_\ell(M^n)=n v_\ell(M)\ge n.
\]

Thus `M^n` absorbs every complete primary part of `s_i` supported on `M`,
simultaneously for `i=p,q`, while absorbing no exterior prime. This proves
the exact equality

\[
\frac{s_i}{\gcd(s_i,M^n)}=s_i^{\perp M}.
\]

The word is allowed by the declared grammar by taking the single divisor
`B_1=M` with exponent `n`. Its bit length is

\[
\lfloor n\log_2 M\rfloor+1=O(n^2),
\]

and ordinary exponentiation constructs it directly from `N`. No
factorization or divisor enumeration is needed. Therefore factoring `K`
cannot improve this residual within the support-only multiplicative
grammar. This conclusion does not extend to an additive construction.

The baseline extension is also valid as a support statement. If all allowed
primes divide `ML`, then `(ML)^n` has at least valuation `n` at every prime
in that support and so saturates every residual primary part. For integral
`R>=1`, `(R!)^n` absorbs all primary parts on primes at most `R`; an exterior
prime larger than `R` remains unless it divides `M`. A complexity claim for
this baseline additionally requires a suitably bounded bit length for `L`,
as the self-audit correctly notes.

## 7. Additive escape and enumeration complexity

The additive identities are immediate and correct:

\[
aB+x-u=up-u=u(p-1),
\]

\[
bB+y-u=uq-u=u(q-1).
\]

Each positive integer is divisible by the corresponding residual. Thus a
public correct pair `(a,x)` or `(b,y)`, for public `B,u`, gives a valid P205
word. This does not make the signed residue public.

The carry relation gives only

\[
xy=u^2+cB.
\]

Even a complete factorization of a nonzero right side does not label which
signed divisor is the true `x`. The packet uses divisor count only as an
enumeration warning. Choose `ell_j` to be the first `t` primes and put

\[
F_t=\prod_{j=1}^t\ell_j
\]

Then `tau(F_t)=2^t`. The standard primorial estimate gives bit length
`m=Theta(t log t)`, and therefore

\[
\tau(F_t)=2^{\Theta(m/\log m)},
\]

which is super-quasipolynomial in `m`. Bertrand alone gives
`m=O(t^2)` and hence the weaker sufficient bound

\[
\tau(F_t)=2^{\Omega(\sqrt m)}.
\]

Both complexity conclusions are correct. There is one harmless wording
imprecision: `PROOF.md` says only "a product of `t` distinct primes" before
invoking the primorial estimate. Arbitrary distinct primes need not give
`m=Theta(t log t)`; the estimate requires the first `t` primes, or another
controlled sequence of comparable size. Since the passage is an
existential example, making that choice repairs the sentence without
changing the conclusion. The example proves an output-size barrier for
exhaustive enumeration, not selector hardness and not a property of every
carry child. The packet states these qualifications.

The zero-product child is publicly recognizable and is properly excluded
from this divisor-selection warning. In the special case `u=a=1`,

\[
x=p-B.
\]

Scanning a short signed range for `x` directly tests `B+x` as a factor of
`N`; the packet correctly refuses to count this as a new carry advantage.

## 8. Scope conclusion

The proof supports the narrow substantive boundary: the complete divisor
lattice of `N-1` adds no prime support beyond the public polynomial-bit word
`(N-1)^n` when it is used only multiplicatively. Additive differences,
shifted divisors, modular rules, carry children, and a semiprime-specific
selector remain outside the theorem. The residual-window result is
one-way and says nothing about smoothness. The packet proves neither an
all-input factoring algorithm nor a lower bound against other algorithms.

Those scope limitations are accurate. They do not cure the explicit
unqualified factor-bank claim identified in Section 3, so the frozen packet
as written fails.
