# F196 strict statement-only blind reconstruction

## Input discipline

Before reading `STATEMENT.md`, its SHA-256 digest was computed as

```text
07d2bccb9f508248a44f39faba3bd13a87cc0b2a1bc3dafa1464c348ae871c5c
```

This exactly matches the required digest. This reconstruction read no F196
proof, self-audit, provenance, manifest, hostile audit, durable ledger, or
other mathematical file. Andreica's binomial-modulo-(2^T) result is used
only as the explicitly stated external premise, with precisely the parameter
range and costs quoted in the statement.

## Exact verdict

**PASS, conditional on the stated Andreica premise and on the balanced
distinct-odd-semiprime promise.**

Every reduction, sign case, residue bound, output-size statement, and
complexity conclusion reconstructs. The equivalence is for the promised
function problems only. It does not supply a factoring algorithm or a lower
bound against one.

## 1. Basic numerical facts

The input length

\[
n=\left\lceil\log_2(N+1)\right\rceil
\]

gives

\[
2^{n-1}<N+1\le2^n.
\tag{R1}
\]

In particular,

\[
N\le2^n-1,
\qquad
0<q<N<2^n.
\tag{R2}
\]

The integers (B=\lfloor\sqrt N\rfloor), its parity, and the sign
((-1)^B) are computable in deterministic polynomial time by exact integer
square root and elementary arithmetic.

The balanced-prime identity is supplied as the existing elementary premise

\[
A=(-1)^B\binom{N-1}{B}\equiv1-q\pmod N.
\tag{R3}
\]

It implies that

\[
h=\frac{A-(1-q)}N
\]

is an integer and, by exact rearrangement,

\[
q=1+hN-A.
\tag{R4}
\]

No division modulo (N) occurs in this definition.

## 2. Polynomial-time computation of (C\bmod2^n)

Apply the stated external algorithm with

\[
T=n,
\qquad
P=N-1,
\qquad
Q=B.
\]

Its range conditions hold directly. From (R1),

\[
0\le P=N-1\le2^n-2<2^n-1.
\]

Also (0\le B\le N-1=P) for every input in the promised range. Thus

\[
0\le Q\le P\le2^T-1,
\]

and no extension for indices larger than the modulus range is needed.

The quoted preprocessing cost becomes

\[
O\!\left(n^3\mathsf M(n)+n^4\right),
\]

and the one-query evaluation cost becomes

\[
O\!\left(n^2\log n\,\mathsf M(n)\right).
\]

Deterministic multiplication of two (n)-bit integers has polynomial bit
cost, even using a basic quadratic algorithm. Both displayed costs are
therefore polynomial in (n). Computing (P,Q), performing preprocessing,
and returning the canonical (n)-bit residue add only polynomial work. This
proves Theorem 1 from the granted premise.

Define for later use

\[
A_n=A\bmod2^n=
\begin{cases}
C_n,&B\text{ even},\\
-C_n\bmod2^n,&B\text{ odd}.
\end{cases}
\tag{R5}
\]

Thus the signed coefficient residue is also available in deterministic
polynomial time. The negative case uses the canonical modular negative; it
does not require materializing the negative exact integer (A).

## 3. One-query reduction from the carry to factoring

Assume one oracle query returns

\[
h_n=h\bmod2^n.
\]

Compute (A_n) by Theorem 1 and (R5), and form

\[
q_n=(1+h_nN-A_n)\bmod2^n.
\tag{R6}
\]

Reducing the exact identity (R4) modulo (2^n) proves

\[
q_n=q\bmod2^n.
\]

But (R2) places (q) in the canonical interval
([0,2^n)). Therefore

\[
q_n=q
\]

as an ordinary integer, not only as a congruence class. Multiplication by
(N), addition, subtraction, and reduction of (O(n))-bit integers take
polynomial bit time. One can verify the answer by checking that
(1<q<N) and (q\mid N), then return the complementary factor (p=N/q).

This is a deterministic polynomial-time one-query reduction

\[
\mathcal F\le_T^{1,\mathrm{poly}}\mathcal H.
\]

It handles both parities of (B) through (R5).

## 4. One-query reduction from factoring to the carry

Assume one oracle query returns (q), the larger promised factor. Theorem 1
again supplies (A_n). Reducing (R4) modulo (2^n) gives

\[
hN\equiv q-1+A_n\pmod{2^n}.
\tag{R7}
\]

The input (N=pq) is odd. Hence

\[
\gcd(N,2^n)=1,
\]

and the extended Euclidean algorithm computes (N^{-1}\bmod2^n) in
polynomial time. Therefore

\[
h_n=
N^{-1}(q-1+A_n)\bmod2^n
\tag{R8}
\]

is exactly the canonical output of (mathcal H). This uses one factoring
query and polynomial additional work:

\[
\mathcal H\le_T^{1,\mathrm{poly}}\mathcal F.
\]

If a conventional factoring oracle returns the two factors without an
order, comparison identifies the larger one. Thus defining
(mathcal F(N)=q) introduces no extra computational issue.

The two directions prove deterministic polynomial-time one-query
interreducibility. Replacing either oracle by a numerical-QP algorithm leaves
the composed algorithm numerical-QP, because adding polynomial overhead to
a QP bound preserves the QP class. Hence a QP carry evaluator exists on the
promise if and only if a QP factorer exists on the same promise.

## 5. The joint residue problem

The joint problem returns

\[
(C_n,h_n).
\]

It trivially projects to (h_n), so Section 3 reduces factoring to the joint
problem. Conversely, a factoring query gives (h_n) by (R8), while Theorem
1 independently gives (C_n). Thus factoring reduces to the joint problem
with one oracle query and polynomial overhead. Its first coordinate adds no
computational power under the quoted external premise.

## 6. Signed Euclidean division

Let

\[
r=N+1-q.
\tag{R9}
\]

Because (1<q<N),

\[
0<r<N.
\tag{R10}
\]

The definition of (h) gives

\[
A=hN+1-q=(h-1)N+(N+1-q)=(h-1)N+r.
\tag{R11}
\]

Equation (R10) shows that (R11) is already Euclidean division with the
canonical nonnegative remainder. Uniqueness of Euclidean division therefore
gives

\[
\left\lfloor\frac AN\right\rfloor=h-1,
\qquad
A\bmod N=N+1-q.
\]

This derivation remains valid when (A<0). In particular, it uses the floor
quotient rather than truncation toward zero.

The two parity cases provide a direct sign check:

- If (B) is even, (A=C>0). Writing
  (C=uN+(N+1-q)) with (u\ge0) gives (h=u+1), so
  (lfloor A/N\rfloor=u=h-1).
- If (B) is odd, (A=-C<0). The congruence for (C) is
  (C\equiv q-1\pmod N), so write (C=uN+q-1), with (u\ge0). Then
  (A=(-u-1)N+(N+1-q)) and (h=-u), again giving
  (lfloor A/N\rfloor=h-1).

Thus no sign or off-by-one error is hidden in (11).

## 7. Exact mixed-radix conversion

Fix (t\ge1), and set

\[
Q=h-1,
\qquad
u=Q\bmod2^t,
\quad0\le u<2^t.
\]

Equation (R11) gives (A=NQ+r). Since (Q-u) is divisible by (2^t),

\[
A\equiv Nu+r\pmod{N2^t}.
\]

Moreover,

\[
0\le Nu+r<N(2^t-1)+N=N2^t,
\]

where strictness uses (r<N). Hence the canonical mixed-modulus residue is
exactly

\[
a_t=Nu+r.
\tag{R12}
\]

Taking its base-(N) quotient and remainder yields

\[
\left\lfloor\frac{a_t}{N}\right\rfloor=u
=(h-1)\bmod2^t,
\]

and

\[
a_t\bmod N=r=N+1-q.
\]

Consequently,

\[
h\equiv1+\left\lfloor\frac{a_t}{N}\right\rfloor
\pmod{2^t}
\]

and

\[
q=N+1-(a_t\bmod N).
\]

If (u=2^t-1), the first displayed sum is (2^t) and correctly represents
zero modulo (2^t); thus the edge carry also has the right sign and wrap.

## 8. Mixed-modulus residue is factoring-equivalent

Let the mixed-residue problem return

\[
a_n=A\bmod(N2^n).
\]

One query gives the exact factor immediately through

\[
q=N+1-(a_n\bmod N).
\]

All operands have at most (2n+O(1)) bits, so the postprocessing is
polynomial.

For the reverse reduction, query the factor function for (q). Then compute

\[
A\bmod N=N+1-q
\]

from Section 6, and compute (A\bmod2^n=A_n) by Theorem 1. Because (N)
is odd,

\[
\gcd(N,2^n)=1.
\]

The Chinese remainder theorem combines these two residues into the unique
canonical residue modulo (N2^n) in polynomial time. The modulus has

\[
\log_2(N2^n)=\log_2N+n=O(n)
\]

bits. Thus this is a deterministic polynomial-time one-query reduction in
the reverse direction as well.

Equivalently, the factor query can first produce (h_n) through (R8), after
which (R12) constructs (a_n). Both derivations confirm the same result.

## 9. Exact output-length boundary

The exact coefficient is

\[
C=\binom{N-1}{B},
\qquad B=\lfloor\sqrt N\rfloor.
\]

For the promised inputs, (B=\Theta(\sqrt N)). The elementary bounds

\[
\left(\frac{N-1}{B}\right)^B
\le \binom{N-1}{B}
\le \left(\frac{e(N-1)}B\right)^B
\tag{R13}
\]

give

\[
\log_2 C=\Theta(B\log N).
\tag{R14}
\]

Indeed, ((N-1)/B=\Theta(\sqrt N)), so its logarithm is
(Theta(\log N)). From (R1), (N=2^{\Theta(n)}), and hence

\[
B=2^{\Theta(n)},
\qquad
\log_2 C=2^{\Theta(n)}.
\]

The exact binary output for (C) therefore has exponentially many bits in
the input length. A bit-complexity algorithm cannot explicitly return all of
it in polynomial or numerical-QP time.

This output-size argument does not apply to the requested residues:
(C\bmod2^n) and (h\bmod2^n) each have only (n) bits, and
(A\bmod(N2^n)) has (O(n)) bits. The reductions show that the latter two
tasks are factoring-equivalent on the promise; they do not prove that every
succinct modular representation is hard.

## 10. Scope disposition

The exact content that survives reconstruction is:

- the remote coefficient modulo (2^n) is deterministically
  polynomial-time computable under the stated external algorithm;
- its signed quotient carry modulo (2^n) and promised balanced-semiprime
  factoring are deterministic polynomial-time one-query equivalent;
- adjoining the already-easy coefficient residue does not change that
  equivalence;
- signed Euclidean division gives the quotient digit and factor formulas for
  every (t\ge1);
- the mixed residue modulo (N2^n) is likewise factoring-equivalent;
- exact coefficient materialization has exponential output length, while no
  lower bound follows for succinct residue computation.

All statements depend on (N) being an odd balanced product of two distinct
primes and on identity (R3). They do not cover arbitrary composites, prime
powers, even inputs, or unbalanced semiprimes. They establish a precise
reduction boundary, not a general factoring result. Within that scope, F196
passes strict statement-only reconstruction.
