# F204 hostile audit

## Verdict

**PASS.** I found no blocking mathematical defect in the frozen statement or
proof. The result supports only the four named fast-forward boundaries. It
does not support a general nonmodularity theorem, a nonlinear Mahler
obstruction, a factoring lower bound, or an objection to one-child bitwise
recursion.

I verified the frozen hashes before reading any packet content:

- `STATEMENT.md`: `020717143764c86138c4ac0d211924884330385c2d7a578c1e1c4a540c2f5929`
- `PROOF.md`: `705dff58fcda88f8d7906e9019289f7d8ba73e0d85e56ab7a3e5dcefa3e87c91`
- `SELF_AUDIT.md`: `599242dbd73060d9da399905ff5f5883fdd62f2495057034c21446d8bd8bcd3f`
- `PROVENANCE.md`: `37c45bc636a8609231143e0318a2581c5805701386100e193da148f76185c8e0`
- `MANIFEST.md`: `faa789fb6bfece814c40a974f2c30346b724b0424099f8ca885392462493e483`

I did not read `BLIND_RECONSTRUCTION.md`. I ran no mathematical computation.

## Refutation attempts

### 1. Exact product identities and formal freedom

The sign and chain rule are correct. Coefficientwise logarithmic
differentiation gives `L(q)=-q d(log P(q))/dq`, and the support of `chi` is
odd, so every nontrivial factor in `P(q)P(-q)` becomes
`1-q^(2a)`. This gives `P(q^2)` with the same character exponent. Applying
`-q d/dq` contributes the required factor two on `P(q^2)`.

For an arbitrary commutative rational algebra, formal logarithm and
exponential are inverse in the `q`-adic rings in question. Comparing the
logarithms gives exactly `2g_(2n)=g_n`; odd powers impose no condition. Every
positive index has a unique odd part, so assigning the odd `g_r` and setting
`g_(2^v r)=2^(-v)g_r` gives all solutions. Thus the claimed freedom concerns
the norm equation alone and is complete.

### 2. Scalar cusp argument

The q-gamma rearrangement is correct:

`P(e^(-t))=(1-e^(-4t))^(1/2) Gamma_Q(3/4)/Gamma_Q(1/4)`.

Hence its leading term is
`2 Gamma(3/4)/Gamma(1/4) * sqrt(t)`, with a finite nonzero constant. The
binary norm then gives `P(-e^(-t)) -> sqrt(2)`. Negative values of `a` or `b`
only reverse the corresponding polynomial power; they do not invalidate
either asymptotic.

Both `0` and `1/2` are cusps for every finite-index subgroup of
`SL_2(Z)`. For a scaling matrix of either finite cusp, the inverse image of a
vertical approach has imaginary part comparable to `1/y`, while the weight
factor has magnitude a nonzero constant times `y^(-k)`. A nonzero leading
local Fourier exponent gives exponential growth or decay in `1/y`. Under the
stated ordinary meromorphic cusp-expansion hypothesis, it cannot imitate a
nonzero polynomial asymptotic. A zero leading exponent therefore gives the
unique polynomial power `y^(-k)`; cusp width changes only constants.

At cusp `0`, the direct product asymptotic has power `y^(a/2)`. At cusp
`1/2`, the factors exchange and the power is `y^(b/2)`. The factor
`exp(2 pi i alpha tau)` tends to a finite nonzero value at each finite cusp.
Consequently `a/2=-k=b/2`, so `a=b`. This argument neither assumes that the
two cusps are inequivalent nor asserts a converse. It applies under exactly
the scalar, fixed-weight, meromorphic cusp hypotheses in the statement.

Finally, logarithmic differentiation of `P(q)^a P(-q)^b` gives
`aL(q)+bL(-q)`. Its odd coefficient is `(a-b)A(N)`, so the same necessary
condition deletes the named odd coefficient.

### 3. Infinite two-kernel

Modulo two, every odd divisor contributes one and every even divisor
contributes zero. Thus `b(n)=1` exactly when `oddpart(n)` is a square.

For the proposed witness, `2^e k_e+1=(2^e+1)^2`. If `f>=e+2`, then

`v_2(2^f k_e)=f+v_2(2^e+2)=f+1`,

because `e>=2`. If `M=x^2`, the adjacent even integers `x-1,x+1` have gcd
two. One has valuation one and the other valuation `f`, so
`x=plus or minus 1 mod 2^f`. The strict comparison is also correct:

`(2^f-1)^2-M=2^f(2^f-2^e-4)>0`.

It forces `1<x<2^f-1`, which is incompatible with either congruence class.
Taking even indices `e` ensures that every later even `f` is at least
`e+2`. The value at `k_e` distinguishes `s_e` from every later `s_f`, so the
two-kernel is infinite. The finite-kernel criterion then rules out
two-automaticity.

### 4. Primitive reduction of an inhomogeneous Mahler relation

Clearing the finitely many rational-function denominators produces polynomial
multipliers. Clearing numerical denominators and dividing the common integer
content preserves the identity and leaves a primitive family in
`Z[q]`. Since `L` has integer coefficients, coefficientwise reduction modulo
two is legitimate.

Primitivity ensures that some reduced polynomial is nonzero. If every
Mahler multiplier vanished modulo two, the reduced identity would assert
that a nonzero inhomogeneous polynomial is the zero formal series. Hence at
least one multiplier survives. Frobenius gives
`B(q^(2^i))=B(q)^(2^i)`. The monomials `1,X,X^2,X^4,...` have distinct
degrees, so the surviving coefficient family defines a nonzero polynomial
in `X`. It follows that `B` is algebraic over `F_2(q)`. Christol's theorem
would make `b` two-automatic, contradicting the infinite-kernel witness.

This excludes exactly fixed finite linear, possibly inhomogeneous,
base-two Mahler identities over `Q(q)`. It does not reach nonlinear equations
or systems whose state grows with the input.

### 5. Odd-prime root norm

For `ell` not dividing `a`, multiplication over the roots gives
`1-q^(ell a)`. For `a=ell d`, it gives `(1-q^(ell d))^ell`, and
`chi(ell d)=epsilon chi(d)`. The nondivisible indices therefore contribute
`P(q^ell)/P(q^(ell^2))^epsilon`; the divisible indices contribute
`P(q^ell)^(ell epsilon)`. Their product has exactly the two exponents stated
in the theorem.

After logarithmic differentiation, the two right-hand dilations contribute
factors `ell` and `ell^2`. The root filter on the left contributes `ell` at
multiples of `ell`. Comparing `q^(ell k)` gives

`A(ell k)=(1+ell epsilon)A(k)-epsilon ell 1_(ell divides k)A(k/ell)`.

Thus the correction term and its divisibility condition are necessary and
correct. For a fixed public prime, a smaller-index term appears at a target
only when that public prime divides the target; otherwise the displayed
relation moves from `A(N)` to `A(ell N)`.

### 6. Scope and recursion

No section supplies an evaluator for `A(N)`, and no truncation through degree
`N` is counted as quasipolynomial work. The scalar proof covers only orbit
monomials under its explicit cusp hypotheses. The Mahler proof is linear and
fixed-state. The root-norm claim is for one fixed public odd prime. None of
these statements extends to arbitrary orbit expressions, vector-valued or
nonholomorphic objects, nonlinear relations, adaptive root banks, or general
factoring algorithms.

The recursion correction is also sound. A single child of bit length at most
`n-1` gives a sum of at most `n` quasipolynomial local costs. The extra factor
`n` is absorbed by increasing the fixed constants in the quasipolynomial
bound. F204 therefore identifies same-node information loss only; it does not
reject a valid one-child recursion.

## Final assessment

All four high-risk claims survive hostile checking. The statement's
qualifiers are essential and are preserved by the proof. This frozen version
passes the hostile-audit step.
