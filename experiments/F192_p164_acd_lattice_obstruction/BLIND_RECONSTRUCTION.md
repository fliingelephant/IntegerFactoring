# F192 blind reconstruction

## Verdict

**PASS.** Every mathematical claim in the frozen statement follows from its
stated hypotheses. The strict inequalities and endpoint restrictions are
sufficient. No mathematical experiment was run.

The SHA-256 digest was computed before reading the statement and then checked
against the expected frozen digest supplied by the coordinator:

```text
23834b7193ce2f3e8e32a3277832fab633c2b7a701bd74591087b3d30ab57cb8  STATEMENT.md
```

This reconstruction used only `STATEMENT.md`. It did not inspect the candidate
proof, either audit, the manifest, or any durable ledger.

## 1. Reconstruction of the locally distinct word

Equations (1)--(4) are hypotheses and definitions. Fix
\(S\in\{P,Q\}\), and suppose that \(0\le i<j<R=K+1\). If
\(x_i=x_j\pmod S\), then the definition of \(g_S\) gives

\[
g_S\mid a^j-a^i=a^i(a^{j-i}-1).
\]

Every prime divisor of \(g_S\) is excluded from \(a\) by (3), so
\(\gcd(a,g_S)=1\). Hence

\[
g_S\mid a^{j-i}-1.
\]

Choose any prime \(\ell\mid g_S\), which exists because \(g_S>1\).
Then \(\operatorname{ord}_\ell(a)\mid j-i\). But

\[
1\le j-i\le R-1=K<\operatorname{ord}_\ell(a),
\]

a contradiction. This proves (5), separately for both \(P\) and \(Q\).
In particular, the hypotheses imply \(R\le P,Q\).

Endpoint check: if \(2\mid g_Pg_Q\), condition (3) cannot hold because a
unit modulo 2 has order 1 while \(K\ge1\). Thus (3) implicitly restricts the
two local orders to be odd. This does not invalidate the conditional theorem.

## 2. Reconstruction of the hidden clusters

Fix \(S\in\{P,Q\}\). Put the \(R\) distinct residues \(x_j\bmod S\) in
oriented cyclic order. Let their positive integral cyclic gaps be
\(d_0,\ldots,d_{R-1}\), with indices read modulo \(R\). Then

\[
\sum_{k=0}^{R-1}d_k=S.
\]

For each starting point, sum the next \(m\) gaps. Each gap occurs in exactly
\(m\) of the \(R\) sums, so their average is \(mS/R\). Some start therefore
satisfies

\[
d_k+\cdots+d_{k+m-1}\le \left\lfloor\frac{mS}{R}\right\rfloor
\le \left\lceil\frac{mS}{R}\right\rceil.
\]

Take \(j_0\) to be that starting label and \(j_i\) to be its \(i\)-th
successor for \(1\le i\le m\). These labels are distinct because \(m<R\).
The positive forward residue

\[
r_i=d_k+\cdots+d_{k+i-1}
\]

is at most the displayed \(m\)-gap sum. Also \(r_i<S\), since
\(mS/R<S\). As
\(z_i=[x_{j_i}-x_{j_0}]_N\) has residue \(r_i\) modulo \(S\), there is an
integer \(t_i\) (in fact \(t_i\ge0\)) such that

\[
z_i=St_i+r_i,
\qquad
0<r_i\le\left\lceil\frac{mS}{R}\right\rceil.
\]

This proves (6)--(7). For either prime divisor \(T\in\{P,Q\}\), (5) gives
\(x_{j_i}\ne x_{j_0}\pmod T\). Thus \(T\nmid z_i\). Since \(N=PQ\),
every \(z_i\) is a unit modulo \(N\).

For the public-bound remark after (8), let a known constant \(C\ge1\)
satisfy \(P/Q\le C\), and set

\[
U=\left\lceil\sqrt{CN}\right\rceil,
\qquad
\widehat B=\left\lceil\frac{mU}{R}\right\rceil.
\]

Because \(P^2=N(P/Q)\le CN\), this public \(U\) is an upper bound for
\(P\), so \(\widehat B\ge\lceil mP/R\rceil\). Moreover \(U/P\) is bounded
by a constant depending only on \(C\), so this is a constant-factor version
of the natural rounded bound. Also \(Q\ge\sqrt{N/C}\). Consequently a
sufficiently small fixed \(m/R\) makes \(\widehat B<Q\), including the
rounding term because the odd prime \(Q\ge3\). This establishes the claimed
public choice. Equation (8) itself is an explicit grant to the lattice
theorem, not a conclusion from the bare transcript.

## 3. Reconstruction of the row-lattice obstruction

### Determinant and factor-bearing vector

The basis matrix in (9) is upper triangular with diagonal
\(\widehat B,N,\ldots,N\). It has full rank and

\[
\det L=\widehat B N^m,
\]

which proves (10).

Now use the cluster for \(S=P\). Multiplying the first basis row by \(Q\)
and subtracting \(t_i\) times the \(i\)-th \(N\)-row gives

\[
Q(\widehat B,z_1,\ldots,z_m)
-\sum_{i=1}^m t_i(0,\ldots,N,\ldots,0)
=(Q\widehat B,Qr_1,\ldots,Qr_m).
\]

This proves membership in (11). Since \(0<r_i\le\widehat B\), its first
coordinate gives the lower bound in (12), and all \(D=m+1\) coordinates
have absolute value at most \(Q\widehat B\), giving the upper bound.
Moreover \(\widehat B<Q\) and \(r_i<Q\), so every coordinate of this vector
has gcd exactly \(Q\) with \(N\); it really is factor-bearing.

For (13), raising the asserted ratio to the \(D=m+1\) power gives

\[
\frac{(Q\widehat B)^D}{\widehat B(PQ)^m}
=Q\left(\frac{\widehat B}{P}\right)^m
=Q\epsilon^m.
\]

Taking the positive \(D\)-th root proves the identity.

### Strictly shorter Dirichlet vector

Assume (14), and put \(h=\lfloor A^{1/m}\rfloor\). The condition
\(A\ge2^m\) gives

\[
h\ge\frac{A^{1/m}}2.
\]

Consider the \(A+1\) points

\[
([kz_1]_N,\ldots,[kz_m]_N),
\qquad 0\le k\le A,
\]

in \([0,N)^m\). Partition each coordinate interval into \(h\) equal
half-open intervals. There are \(h^m\le A\) boxes, so two points, with
indices \(0\le k<\ell\le A\), lie in the same box. Put
\(c=\ell-k\). For every \(i\), the difference of their \(i\)-th
coordinates is an integer \(\delta_i\) satisfying

\[
\delta_i\equiv cz_i\pmod N,
\qquad
|\delta_i|<\frac Nh\le\frac{2N}{A^{1/m}}.
\]

Thus

\[
u=(c\widehat B,\delta_1,\ldots,\delta_m)\in L,
\qquad 1\le c\le A.
\]

Both strict endpoints in (14) now enter. The upper endpoint gives

\[
0<c\widehat B\le A\widehat B
<\frac{Q\widehat B}{\sqrt D},
\]

while the lower endpoint gives, for every \(i\),

\[
|\delta_i|<\frac{2N}{A^{1/m}}
<\frac{N\epsilon}{\sqrt D}
=\frac{Q\widehat B}{\sqrt D}.
\]

All \(D\) coordinates are strictly below
\(Q\widehat B/\sqrt D\) in absolute value. Hence

\[
0<\|u\|_2<Q\widehat B,
\]

which proves (15).

### Every shortest vector is coordinate-wise coprime

Every lattice vector has the form

\[
y=(c\widehat B,cz_1+Nk_1,\ldots,cz_m+Nk_m)
\]

for integers \(c,k_1,\ldots,k_m\). Let \(y\) be any shortest nonzero
vector. The preceding construction gives \(\|y\|_2<Q\widehat B<N\), where
the last inequality follows from \(\widehat B<Q\le P\). If \(c=0\), any
nonzero such vector has norm at least \(N\), a contradiction. Therefore
\(c\ne0\), and its first coordinate gives

\[
0<|c|\widehat B\le\|y\|_2<Q\widehat B,
\qquad	ext{so}\qquad 0<|c|<Q\le P.
\]

Neither \(P\) nor \(Q\) divides \(c\). Also
\(0<\widehat B<Q\le P\), so the first coordinate is a unit modulo \(N\).
For every remaining coordinate,

\[
cz_i+Nk_i\equiv cz_i\pmod P
\quad\text{and}\quad
cz_i+Nk_i\equiv cz_i\pmod Q.
\]

Both \(c\) and \(z_i\) are units modulo both primes. Thus every output
coordinate is coprime to \(N\). The coefficient \(c\) is coprime as well.
This proves the stronger claim following (15) for every possible exact-SVP
tie, not only for the particular Dirichlet vector.

### Asymptotic feasibility of (14)

Interpret numerical-QP length in its standard sense
\(\log_2R=(\log n)^{O(1)}\), and let \(m=(\log n)^{O(1)}\). From (8),

\[
\epsilon=\frac{\widehat B}{P}\ge\frac mR.
\]

Therefore the logarithm of the lower endpoint of (14) is at most

\[
m\left(1+\frac12\log_2D+\log_2\frac Rm\right)
=(\log n)^{O(1)}=o(n).
\]

The constant-factor condition (16) records that this is also the natural
cluster-error scale. For fixed balance,

\[
Q^2\ge\frac NC,
\]

so, with \(n=\lceil\log_2N\rceil\),

\[
\log_2\frac Q{\sqrt D}=\frac n2-o(n).
\]

The logarithmic gap between the endpoints therefore tends to infinity.
Because \(\epsilon<1\), the lower endpoint is already greater than
\(2^m\). For all sufficiently large \(n\), an integer strictly between the
two endpoints exists and automatically satisfies \(A\ge2^m\). This proves
the final claim of Section 3, including the integer and strict-endpoint
requirements.

## 4. Reconstruction of the subset-bank lower bound

There are \((R-1)!\) oriented cyclic orders of \(R\) distinct labels, where
rotations are identified and reversal is not. Fix one \(s\)-subset \(F\).
For \(F\) to be consecutive, order its \(s\) elements internally in \(s!\)
ways, contract it to one block, and cyclically order that block with the
remaining \(R-s\) labels in \((R-s)!\) ways. Thus a fixed \(F\) is a block
in exactly

\[
s!(R-s)!
\]

oriented cyclic orders. A family that covers every order must consequently
satisfy the union-bound incidence inequality

\[
|\mathcal F|\,s!(R-s)!\ge(R-1)!.
\]

Rearranging gives

\[
|\mathcal F|\ge
\frac{(R-1)!}{s!(R-s)!}
=\frac1R{R\choose s},
\]

which proves (17). Since cardinality is integral, the slightly stronger
written form is
\(|\mathcal F|\ge\lceil {R\choose s}/R\rceil\). The restrictions
\(2\le s<R\) ensure a proper nontrivial cyclic block; with \(s=m+1\), they
follow from \(1\le m<R-1\) in the intended use. If \(m=R-1\), then
\(s=R\) lies outside Section 4's stated range and no invocation of (17) is
licensed.

The word “exact” here can mean that the incidence count is exact. The proof
does not claim that this covering lower bound is always attained. Its
universal quantifier is over all oriented cyclic orders. It therefore does
not apply after restricting to the cyclic orders realizable by a particular
recurrence, nor to an adaptive or recurrence-aware selector. These are
exactly the limitations stated after (17).

## 5. Quantifier and scope audit

- The hidden-cluster result is existential. It does not expose the indices
  without knowing the order modulo a hidden prime.
- The strict bound \(\widehat B<Q\) is essential. It makes \(\widehat B\)
  a unit modulo \(N\), gives \(Q\widehat B<N\), and supports the
  coordinate-wise coprimality proof.
- Both inequalities in (14) are strict, and the reconstruction preserves
  strictness in (15).
- The SVP obstruction concerns only the row lattice (9) at the granted
  cluster scale. It says nothing about other lattices, source-aware
  recurrence methods, robust approximate-common-divisor decoders, or
  factoring in general.
- Shortness alone supplies no local-order prime-support statement. The
  surviving interface in Section 5 is therefore a correct statement of what
  remains open, not an additional factoring claim.

