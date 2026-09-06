# Hostile audit of F200

## Verdict

**FAIL.** The packet is not the frozen version declared by its manifest.
Moreover, the optional P159--P161 cyclotomic corollary overstates the
interface to the promoted results. The elementary Theorems 1--5 and the
earlier parts of Theorem 6 otherwise reconstruct correctly within their
named scopes.

## 1. Fatal frozen-hash mismatch

I computed all hashes before reading the packet. The observed values are

- `STATEMENT.md`:
  `e6516eb85462f577d899bb4bfe50fd62b6ceea58e5752bb2c806208b42440713`;
- `PROOF.md`:
  `0e6010f2a78e2867bb3ed37c0e4c5b0484acc698cedbd976436944fb38ef1b8b`;
- `SELF_AUDIT.md`:
  `a26c2a174a9278f9a8e51059869af04a24e9658fd6f080d69b230f7ea1a8d398`;
- observed `MANIFEST.md`:
  `329b3acdb7b78ad40966a4e6dc882524b4f1a4953fdb73d423322a85b98402df`.

The manifest instead declares

- `STATEMENT.md`:
  `9277582c6c39d48f4fd2555a1797e09bb84d1ad8411a8ac8fa1c5f5d8b5535a0`;
- `PROOF.md`:
  `cefcb6f82c5a74bfed67623eadb42eeb04f2309c3a577ccc3824ee50bbb48f5f`.

Only `SELF_AUDIT.md` matches. Therefore the statement and proof supplied
for review are not the frozen inputs authenticated by the manifest. This
alone requires failure under the verification cadence. A new version must
freeze the actual statement and proof hashes before another hostile audit.

## 2. One-denominator delta and gcd orientation

The underlying calculation is correct. From

\[
j(A_j-A_{j-1})=-NA_{j-1}
\]

one gets

\[
x_j=\frac{A_{j-1}}j=\frac{A_{j-1}-A_j}{N}.
\]

The range (p\le B<q) and (B<2p) makes (p) the only index in
\([1,B]\) that is not coprime to (N=pq). For (j\ne p), Euclid's lemma
gives (j\mid A_{j-1}). At (j=p), P171 gives

\[
A_{p-1}=1+Ng,
\qquad
x_p=qg+\frac1p.
\]

Thus the delta in \(\mathbb Q/\mathbb Z\) has value (1/p) at (p).
For an active subset,

\[
D_I=NS_I\equiv q\pmod N,
\]

so its endpoint-difference gcd is (q). The index-product gcd is (p).
The inactive orientations are (N) and (1), respectively. Telescoping on
an interval is exact.

## 3. Floor and sign

The root sum is

\[
\sum_{j=1}^Bx_j=\frac{1-A_B}{N}
=\frac1p-h.
\]

Since (0<1/p<1), its ordinary floor is (-h). An active subset has the
form integer plus (1/p), with the displayed positive fractional part.
The sign and the Archimedean-versus-2-adic distinction are correct.

## 4. Walsh, Fourier, Haar, and differences

After zero padding, the quotient-valued word is a single point mass.
Every unnormalized Walsh coefficient is \(\pm1/p\), nonzero in
\(\mathbb Q/\mathbb Z\).

Every Fourier coefficient is a root of unity times (1/p). Because a root
of unity is a unit of \(\mathcal O_K\), this element cannot be integral:
if \(\zeta/p\in\mathcal O_K\), multiplying by the unit \(\zeta^{-1}\)
would make (1/p) integral, impossible. Hence all coefficients are
nonzero in \(K/\mathcal O_K\).

The Haar conclusion is correct for the declared unnormalized dyadic
wavelet coefficients: exactly one parent at each wavelet scale contains
the point. The scaling/root coefficient is not called a wavelet and causes
no contradiction.

For cyclic differences, each Fourier coefficient acquires the stated
character multiplier. The assertion that an odd shift kills only zero
frequency correctly relies on the already declared dyadic (M). The
translation-averaged autocorrelation of the rational delta is independent
of its location. These are quotient-valued or rational transform facts,
not efficient evaluation claims.

## 5. Residue-cell inversion

On odd residues modulo (2^t), inversion is a permutation. Therefore

\[
j^{-1}\equiv a\pmod{2^t}
\iff
j\equiv a^{-1}\pmod{2^t}.
\]

Only (j=p) contributes in \(\mathbb Q/\mathbb Z\), so the cell vector is
a point mass at (p^{-1}\). Any Boolean labelling of the odd residue
classes is only a permutation of the cube, and its Walsh transform remains
full.

## 6. Finite 2-adic tree gauge and nonempty cells

The gauge identity is exact:

\[
s_v=s_{v_0}+s_{v_1},
\qquad
\mathbf1_{\ell\in v}
=\mathbf1_{\ell\in v_0}+\mathbf1_{\ell\in v_1}.
\]

Subtracting (u\mathbf1_{\ell\in v}) preserves every fork equation for
every proposed leaf. Surjectivity of \(\mathbb Z\to\mathbb Z/2^t\mathbb Z\)
does supply integer representatives. One can choose representatives at
leaves and define the internal integer labels by summation. False paths are
not asserted to reproduce the actual floors or their sizes.

For the two next reciprocal lifts, inversion modulo (2^{t+1}) yields two
odd index classes modulo (2^{t+1}). An interval of length greater than
the modulus contains a representative of each. The balanced candidate
interval has length \(\Theta(\sqrt N)\), while at or below quarter
precision the modulus is at most a constant multiple of (N^{1/4}).
Thus both cells are nonempty after a finite prefix. The proof's stronger
length (>2^{t+1}) is sufficient. It uses only plausible balanced
representatives, not primes or exact factor pairs.

The symmetry is additive. The statement correctly leaves ordinary floors,
exact rational integrality, and nonlinear integer-part distributions open.

## 7. Summation by parts, run count, and sampling

The discrete summation-by-parts formula is exact:

\[
N\sum_{j=1}^Bw_jx_j
=w_1A_0+\sum_{j=1}^{B-1}(w_{j+1}-w_j)A_j-w_BA_B.
\]

A weight with (R) nonzero adjacent differences uses at most (R+2)
endpoint terms. P173 evaluates a supplied QP collection of endpoints
modulo (2^t) in QP time. This yields only residues, not Archimedean
floors.

A residue cell has (B/2^t+O(1)) isolated singleton runs. With

\[
t=\left\lfloor\frac{\log_2N}{4}\right\rfloor-L(n),
\]

this count is

\[
N^{1/4}2^{L(n)+O(1)},
\]

up to the (B=\sqrt N+O(1)) factor. It is exponential in input length.
Uniform sampling from the correct cell hits (p) with reciprocal
probability \(\Theta(2^t/B)\). These claims are correctly scoped to literal
endpoint materialization and uniform coordinate sampling.

## 8. Auxiliary moduli, density, and Mahler scope

If \(\gcd(M,N)=1\), then (p,q,N) are units modulo (M), so the reduction
of \(\mathbb Z[1/N]\) is defined and sends (1/p) to (p^{-1}\). Every
such residue is also the reduction of an ordinary integer. The same holds
in any finite product. Therefore a value-local residue predicate cannot be
an integer-versus-integer-plus-(1/p) test.

The (N\mid M) case is explicitly excluded. The density statement is also
correct: ordinary integers are dense in \(\mathbb Z_2\), so a continuous
function constant on all ordinary integers is constant on all of
\(\mathbb Z_2\). Uniformly convergent Mahler expansions and finite-precision
characters lie in this value-local continuous class. The theorem does not
apply to the rational presentation together with (N), discontinuous
floors, or nonlocal correlations.

## 9. Phase magnitude and equality reduction

For bounded integer frequency (m),

\[
|e^{2\pi im/p}-1|\le 2\pi|m|/p.
\]

Numerical-QP (m) and (p=2^{\Theta(n)}) give exponentially small
separation. Uniform (m\bmod N\) maps uniformly modulo (p), so a constant
fraction of active phases have constant separation.

The exact equality reduction is also correct:

\[
e^{2\pi imS_I}=e^{2\pi imD_I/N}.
\]

For \(\gcd(m,N)=1\), this phase equals one iff (N\mid D_I), hence iff
the cell is inactive. Exact equality on successive children locates (p).
The statement carefully distinguishes exact equality from approximate
phase estimation.

## 10. Local cyclotomic degree: local fact correct, interface overstated

The local-field fact itself is correct. If a finite extension
\(K/\mathbb Q_2\) with residue degree (f) contains a primitive odd
(p)-th root of unity, prime-to-two torsion reduces injectively. Hence

\[
p\mid 2^f-1,
\qquad
\operatorname{ord}_p(2)\mid f,
\]

so \([K:\mathbb Q_2]\ge f\ge\operatorname{ord}_p(2)\).

However, the statement then says:

> on a normalized P161 branch obtained from the beta-two witness, the
> surviving element is a power of two and its order divides
> \(\operatorname{ord}_p(2)\). Its rough order above the chosen QP
> dimension cap therefore excludes a QP-degree extension containing the
> active phase.

This needs a missing condition. P160 constructs (y=4^{N^n}\), and P161
constructs (w=y^Q\), so (w) is indeed a public power of two. On P161's
surviving (H=1) branch, every local order, including
\(\operatorname{ord}_p(w)\), exceeds (T), and divisibility

\[
\operatorname{ord}_p(w)\mid\operatorname{ord}_p(2)
\]

then proves \(\operatorname{ord}_p(2)>T\). But P161 has a trichotomy: it
can instead return a factor or an exact common-order state. Its conclusion
is not an unconditional property of every beta-two instance, and F200's
statement does not explicitly condition the corollary on the P161
surviving (H=1) rough-local-order outcome at the same hidden prime (p).

There is a second precision issue in the phrase "above the chosen QP
dimension cap." P161 allows any fixed numerical-QP roughness cap (T),
but the corollary must explicitly choose (T\ge D(n)), where (D(n)) is
the proposed extension-degree cap. Merely saying that the order is rough
above "the chosen cap" is not a quantified exclusion until this coupling
is stated.

The repaired corollary would be:

> Fix a numerical-QP degree cap (D(n)), run P160--P161 with
> (T\ge D(n)), and condition on its surviving (H=1) branch. Then for
> each hidden rational prime (r\mid N),
> \(\operatorname{ord}_r(2)\ge\operatorname{ord}_r(w)>T\). Therefore no
> extension of \(\mathbb Q_2\) of degree at most (D(n)) contains a
> primitive (r)-th root of unity.

The factor and exact-common-order exits must remain separate algorithmic
outcomes. This repair is material enough to require a new frozen version,
although it does not affect Theorems 1--5 or the earlier parts of Theorem
6.

## 11. Recursion and nonclaims

The packet does not impose fixed-ratio contraction. Its remaining opening
allows adaptive dyadic localization. A one-child sequence of (O(n)) QP
steps would remain QP, in agreement with the user's correction.

All broader exclusions are stated. F200 proves no lower bound against:

- nonlocal canonical-integer or Euclidean-floor features;
- a QP aggregate cell evaluator;
- nonlinear statistics of the actual integer parts;
- implicit high-order phase algorithms;
- complex approximation;
- sparse high-degree circuits; or
- other factoring methods.

## Strict result

**FAIL.** The statement and proof hashes do not match the manifest. The
optional P159--P161 corollary also needs the explicit P161 surviving-branch
condition and a quantified choice (T\ge D(n)). Refreeze the repaired
packet before a fresh hostile audit.
