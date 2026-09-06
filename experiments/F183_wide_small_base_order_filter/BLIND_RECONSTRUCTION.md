# F183 blind reconstruction

## Audit basis

This reconstruction uses only `STATEMENT.md`.

Verified statement SHA-256:

`1505042cdb44c0ef000c70638e53be12f2a07b160c5f9c3adddac543f0e4c67d`

## Verdict

**PASS.** The stated trichotomy and the uniform deterministic
quasipolynomial cost follow from the stated hypotheses. This uses the
standard meaning of the hidden prime-power decomposition: the (R_j) are
the pairwise-coprime maximal prime powers in (N). It also uses the standard
complexity convention that the fixed constants (c,d,C) are effective
constants.

## 1. Exact support of the primary filter

Put (E=P^n). Fix a prime power ℓ^e parallel to (g_j). For any base
(a),

\[
ℓ\mid C_a
\quad\Longleftrightarrow\quad
ℓ\mid a
\ \text{or}\ 
\bigl(ℓ\nmid a\text{ and }\operatorname{ord}_{ℓ}(a)\le K\bigr).
\]

Indeed, the first alternative is detected by the leading factor (a).
When ℓ does not divide (a), it divides (a^k-1) exactly when
(\operatorname{ord}_{ℓ}(a)) divides (k). Thus a factor with
(1\le k\le K) exists exactly when that order is at most (K). Taking the
product over all bases gives

\[
ℓ\nmid P
\quad\Longleftrightarrow\quad
\forall a\in[2,L+1]:
ℓ\nmid a\ \text{and}\ \operatorname{ord}_{ℓ}(a)>K.
\tag{A}
\]

There is no undefined-order case in (A). The explicit “ℓ does not divide
(a)” condition handles it. In fact, roughness makes this condition
automatic here: ℓ divides (g_j), so
(ℓ>T\ge L+1\), while (a\le L+1).

The support test alone must also remove the full ℓ-adic valuation from
the local order. That is why the exponent is (P^n). Since

\[
g_j\le \varphi(R_j)<R_j\le N<2^n,
\]

the relation ℓ^e dividing (g_j) implies (e<n). If ℓ divides (P),
then

\[
v_{ℓ}(E)=n v_{ℓ}(P)\ge n>e.
\]

If ℓ does not divide (P), then (v_{ℓ}(E)=0). The standard order
identity

\[
\operatorname{ord}_{R_j}(w^E)
=\frac{g_j}{\gcd(g_j,E)}
\]

therefore deletes every ℓ^e whose prime ℓ divides (P), and preserves
every other ℓ^e in full. Combining this valuation calculation with (A)
gives exactly

\[
\operatorname{ord}_{R_j}(z)=h_j.
\]

No prime power is partly retained by this filter.

## 2. Repeated hidden prime factors and the three gcd branches

Write (R_j=p_j^{\alpha_j}). The argument above works in the unit group
modulo the full prime power (R_j); it does not replace (R_j) by its
underlying prime. This is essential when (N) is not squarefree.

A possible attack is that (z-1) can contain only part of (R_j):

\[
0<v_{p_j}(z-1)<\alpha_j.
\]

This does not break the trichotomy. It makes
(\gcd(z-1,N)) a nontrivial proper divisor and therefore enters the factor
branch. The proof does not need (H) to be a product of whole (R_j)'s.

The endpoint branches are exact:

- If (H=1), no (R_j) can satisfy (z\equiv1\pmod{R_j}). Hence no
  (h_j) is (1). Each (h_j) divides (g_j), so all of its prime factors
  exceed (T). Definition (A) then gives both small-base conditions for
  every prime dividing every (h_j).
- If (H=N), then (z\equiv1\pmod N). Hence (g_j\mid E) for every (j),
  equivalently all local orders were extinguished by the primary filter.
- If (1<H<N), (H) is already a proper factor. This includes mixtures of
  fully extinguished components, surviving components, and partial
  (p_j)-adic collisions.

Thus repeated prime powers create no missing fourth branch.

## 3. Factor-first synchronization when (H=N)

The complete factorization of (E=P^n) permits the following stripping
procedure. Start with (m=E). For every prime (q) in that factorization,
repeatedly form

\[
D_q=\gcd\bigl(w^{m/q}-1,N\bigr)
\]

while (q\mid m).

- If (D_q=N), replace (m) by (m/q).
- If (1<D_q<N), return (D_q).
- If (D_q=1), retain that copy of (q) and continue with the next prime.

The invariant is (g_j\mid m) for every (j). It holds initially because
(H=N). A step with (D_q=N) preserves it, because that equality is
equivalent to (g_j\mid m/q) for every (j).

Suppose the procedure does not return a factor. At a (D_q=1) step, no
local order divides (m/q). Since every local order divides (m), this
forces

\[
v_q(g_j)=v_q(m)\qquad\text{for every }j.
\tag{B}

Indeed, all non-(q) valuations already fit inside (m/q), so failure to
divide can only occur at (q). If different components first stopped at
different (q)-valuations, the components with the smaller valuation would
contribute their full (R_j) to (D_q), while a component with the larger
valuation would fail to contribute its full (R_j). Then
(1<D_q<N), including any partial (p_j)-adic contribution, and a factor
would be returned.

Primes absent from all (g_j)'s are stripped completely. For every prime
remaining in (m), (B) fixes the same exact valuation in every (g_j).
Consequently

\[
m=g_1=\cdots=g_s.

The factorization of (m) is known because the procedure only subtracts
valuations from the known factorization of (E). Also (m>T): it is a
nontrivial (g_j), and every prime dividing it is greater than (T).

Processing each prime once in this manner is sound. Later stripping at
other primes does not change the already established (q)-valuation.

## 4. Complete factorization and duplicate valuations

Trial division is applied to each small integer expression (C_a), not to
the much larger product (P). For each prime (q), the merged exponent must
be the sum

\[
v_q(P)
=\sum_{a=2}^{L+1}v_q(C_a)
=\sum_{a=2}^{L+1}
\left(v_q(a)+\sum_{k=1}^K v_q(a^k-1)\right).
\tag{C}

Thus repetitions within one (C_a), between different (k)'s, and between
different bases are all retained. The complete factorization of (E) is
then

\[
E=\prod_{q\mid P}q^{,n v_q(P)}.

\]

Collapsing duplicate primes without summing their valuations would not be a
factorization of the stated (P). Equation (C) is the exact merge needed by
the construction and by factor-first stripping.

## 5. Explicit size and uniform cost bounds

Let

\[
\lambda=\log_2(n+1).

\]

With (c,d,C) fixed,

\[
K=O(\lambda^c),\qquad
L=2^{O(\lambda^d)},\qquad
\log_2(L+1)=O(\lambda^d).

\]

For every (a\le L+1),

\[
\begin{aligned}
\log_2 C_a
&=\log_2 a+\sum_{k=1}^K\log_2(a^k-1)\\
&<\left(1+\frac{K(K+1)}2\right)\log_2 a\\
&=O(\lambda^{2c+d}).
\end{aligned}
\tag{D}

Hence trial division through √(C_a) uses at most
(2^{O(\lambda^{2c+d})}) candidate divisions for one base. Multiplying by
the (L) bases and by polynomial integer-arithmetic overhead keeps the
total at

\[
2^{O(\lambda^{2c+d})},

\]

which is quasipolynomial in the input bit length (n).

The product and exponent sizes are also within the claimed bound:

\[
\log_2 P
=\sum_{a=2}^{L+1}\log_2 C_a
=O\bigl(L\lambda^{2c+d}\bigr)
=2^{O(\lambda^d)},
\tag{E}

\]

and

\[
\log_2 E=n\log_2 P=2^{O(\lambda^d)}.
\tag{F}

\]

The last absorption uses (d\ge1). Construction of all powers and
products is polynomial in these displayed bit lengths. Repeated-squaring
modular exponentiation uses (O(\log E)) modular multiplications on
(O(n))-bit residues, and gcd has polynomial bit cost.

Finally, the number of prime-factor copies stripped from (E) is bounded
by

\[
\Omega(E)=n\Omega(P)\le n\log_2 P=\log_2 E.

\]

Even recomputing (w^{m/q}\bmod N) by repeated squaring at every stripping
step costs only a polynomial in (n) and (log E), hence remains
(2^{\operatorname{poly}(\log n)}). All loop bounds and arithmetic
operations are explicit. The algorithm is therefore uniform and
deterministic under the effective-fixed-constant convention stated above.

## 6. Boundary of the result

The hard descendant branch does not synchronize the (h_j). They may be
unequal. The result is conditional on the supplied rough local-order state,
so it does not claim a factoring algorithm for every odd composite. These
limitations agree with the exact boundary in the statement and do not
weaken the trichotomy.
