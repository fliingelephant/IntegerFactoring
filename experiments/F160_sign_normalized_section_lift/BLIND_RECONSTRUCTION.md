# F160 blind reconstruction

## Isolation and verdict

- Source read: `STATEMENT.md` only.
- Verified source SHA-256: `fd232fabd54a66ed03090a3ce4a03905dc1d3e3667b6ba712acee80751751ecc`.
- Overall verdict: **PASS**.

Every algebraic claim follows from the stated hypotheses. The complexity claim uses the standard meaning that a quasipolynomial output list has quasipolynomial total encoded size and that a public decorated section can be evaluated in time polynomial in its encoding. With that normal interpretation, there is no missing externality premise and no hidden enumeration of the cyclic group.

## 1. Local order lemma

Fix (r\in\{p,q\}), and write (h=g\bmod r). Since

\[
\operatorname{ord}_r(h)=M,\qquad \gcd(a,M)=1,
\]

the element (h^a) also has order (M). If (T=\operatorname{ord}_r(x)), then

\[
\operatorname{ord}_r(x^2)=\frac{T}{\gcd(T,2)}=M. \tag{A}
\]

This elementary identity controls both parity cases.

### Even (M)

If (T) were odd, (A) would give (T=M), contrary to evenness of (M). Hence (T) is even, and (A) gives (T/2=M), so (T=2M). This applies independently at (p) and (q). Therefore the supplied (x) already has common order (2M), and (y=x) proves the even branch.

### Odd (M)

The map (t\mapsto t^2) is an automorphism of the odd-order group \(\langle h\rangle\). Let (k) be the unique residue modulo (M) such that

\[
2k\equiv a\pmod M.
\]

Then (h^k) is the unique root of (h^a) inside \(\langle h\rangle\). Also \(\gcd(k,M)=1\), so (h^k) has order (M). Over the odd field \(\mathbf F_r\), the two roots of (X^2-h^a) are exactly

\[
h^k\quad\text{and}\quad-h^k.
\]

The first has order (M). The second has order (2M): (-1\notin\langle h\rangle), and the commuting factors (-1) and (h^k) have coprime orders (2) and (M).

Now set (d=\gcd(x-g^k,N)). A hidden prime (r) divides (d) exactly when (x\equiv g^k\pmod r). Thus:

- If the two local signs differ, (d\in\{p,q\}), so (d) is a proper factor.
- If both signs are positive, (d=N), and (y=-x) has order (2M) at both primes.
- If both signs are negative, (d=1), and (y=x) has order (2M) at both primes.

This exhausts all cases. Computing (k), a modular power, one gcd, and a sign is deterministic polynomial time. The factorization of (2M) follows immediately from the public factorization of (M). Hence the exact local-order assertion needed for the next certified common-order state is proved.

For the source-free consequence, take any (a) coprime to odd (M), in particular (a=1), and set

\[
x_0=g^{a(2^{-1}\bmod M)}.
\]

Then (x_0^2=g^a) modulo (N), and (-x_0) has common order (2M). Thus an odd state can be doubled publicly once. The new order is even, and every further doubling preserves evenness.

**Verdict for all sign-normalization claims: PASS.**

## 2. Decorated-section bridge

For a candidate satisfying (8), the publicly supplied section value gives

\[
(u z_v)^2\equiv u^2Q(v)\equiv g^a\pmod N.
\]

Thus (x=u z_v) satisfies the primitive-root hypothesis because \(\gcd(a,M)=1\). Section 1 therefore returns either a proper factor or a common-order generator of order (2M). No condition about which local sign (z_v) uses is necessary; the gcd/sign procedure resolves it.

The candidate conditions are public checks: membership in the public span (W), the unit test for (u), modular evaluation of (Q(v)), the displayed congruence, and \(\gcd(a,M)=1\). Evaluating (z_v) is part of having a public decorated section. Each check and the decoder use polynomially many bit operations in the candidate and public-input encodings.

If a source emits a list of quasipolynomial total encoded size, polynomial work per encoded candidate keeps the total work quasipolynomial. The procedure only evaluates the listed candidates. It never enumerates \(\langle g\rangle\).

The inverse-representative specialization is exact. If

\[
s_v^2\equiv Q(v)^{-1}\equiv g^a\pmod N,
\]

then (x=s_v) directly satisfies the primitive-root hypothesis. It can also be put literally into the decorated-section form by taking

\[
z_v=Q(v)s_v,\qquad u=Q(v)^{-1};
\]

then (z_v^2=Q(v)), (u^2Q(v)=Q(v)^{-1}), and (u z_v=s_v).

These are conditional decoding statements. None supplies a vector or proves that a qualifying candidate exists.

**Verdict for the section bridge and quasipolynomial decoding claim: PASS.**

## 3. Exact Jacobi boundary

Assume (M) is even. Since (M\mid r-1), (c_r=(r-1)/M) is an integer. Also \(\gcd(a,M)=1\) forces (a) to be odd. Euler's criterion and the fact that an element of even order (M) satisfies (g^{M/2}=-1\pmod r) give

\[
\left(\frac{g^a}{r}\right)
= (g^a)^{(r-1)/2}
= (g^{M/2})^{a c_r}
=(-1)^{a c_r}
=(-1)^{c_r}.
\]

Consequently,

\[
\left(\frac gN\right)=(-1)^{c_p+c_q}.
\]

If this Jacobi symbol is (-1), the parities of (c_p,c_q) differ. Exactly one local Legendre symbol of (g^a) is (+1), so exactly one hidden field has roots. A scalar root modulo (N) would give roots in both fields, hence none exists. Any total factor-or-root source must therefore take its factor branch.

If the Jacobi symbol is (+1), the parities agree. Even-even means roots in both fields; odd-odd means roots in neither. The single Jacobi bit cannot distinguish them.

The two examples check the sharpness. For (N=13\cdot17), the capacities for the state ((-1,2)) are (6) and (8), and

\[
174^2=30276=137\cdot221-1.
\]

For (N=7\cdot11), the capacities are (3) and (5), so (-1) is a nonsquare in both fields. Both semiprimes nevertheless have Jacobi symbol \(\left(\frac{-1}{N}\right)=+1\).

**Verdict for the Jacobi formula, dichotomy, and examples: PASS.**

## 4. Paired-discriminant equivalence

Let (D) be a unit with Jacobi symbol (-1), assume \(\left(\frac gN\right)=+1\), and set (E=Dg^a\pmod N). Multiplicativity gives

\[
\left(\frac EN\right)
=\left(\frac DN\right)\left(\frac gN\right)^a
=-1.
\]

Also (DE=D^2g^a\pmod N). Since (D) is a public unit, multiplication by (D) is invertible, and

\[
x^2=g^a
\quad\Longleftrightarrow\quad
(Dx)^2=DE
\pmod N.
\]

The inverse map is (z\mapsto D^{-1}z). These maps are public polynomial-time bijections between the two root sets. Therefore a root of one problem is exactly enough to obtain a root of the other, including the empty-root case. The two Jacobi-minus-one labels do not construct such a root; a section root for (DE) would do so through the inverse map.

**Verdict for paired-discriminant equivalence: PASS.**

## 5. Scope and remaining source problem

The logical reduction is now exact:

1. An odd common-order state has the unconditional public doubling proved in Section 1.
2. At a surviving even state, a proper factor ends the branch, while one verified hit of form (8) gives a root and then a certified doubling.
3. After the first doubling, the order remains even.

Thus externality is not a source obligation. The source only needs to return a factor or a qualifying square-class hit at each surviving even state.

This is a source specification, not a construction of the source. In particular, the hypotheses contain no existence or counting premise for hits. The state ((-1,2)) at (N=77) even shows that no scalar-root hit can exist there: such a hit would produce a square root of (-1), contradicting the local Legendre calculation. A total source would have to factor on that branch. Hence the reconstruction proves no uniform hit law, no inverse-quasipolynomial hit density, and no factoring algorithm.

**Verdict for the stated narrowing and all negative scope claims: PASS.**
