# F277 blind reconstruction — PASS

## Verdict and authenticated boundary

**PASS.** Every displayed identity, endpoint, local congruence, saturated
example, evaluator qualification, scope statement, and nonclaim in the
authenticated statement follows independently.

I authenticated and read only:

| Artifact | SHA-256 |
|---|---|
| `STATEMENT.md` | `1f4c3226ddabfc231f37f4da4b6f9ac410e225f646e82a54cbc29b845bed381a` |

Before sealing this reconstruction, I did not read any F277 proof, audit,
provenance, manifest, or hostile-review artifact. I used the conventions

\[
\binom nk=0,\qquad
\left\{\begin{matrix}n\\k\end{matrix}\right\}=0
\]

when (k<0) or (k>n). Binomial polynomials at negative integers have their
usual polynomial meaning.

## 1. Balanced endpoint inequalities

Write (q=p+d) and (B=p+s). Since (p<\sqrt{pq}<q),

\[
p\le B<q.
\]

Also (q<2p) gives

\[
B<\sqrt2p,qquad 0\le s<(\sqrt2-1)p.
\]

Assume (s>0). From (B^2\le pq),

\[
(p+s)^2\le p(p+d),qquad d\ge2s+\frac{s^2}{p}>2s.
\]

The difference (d=q-p) is even because (p,q) are odd. Hence

\[
d\ge2s+2,qquad q-B=d-s\ge s+2.
\]

Finally (q<2p) gives (d<p). Combining it with (d\ge2s+2) gives

\[
2s+1<p.
\]

This proves all assertions in (3)--(4). If (s=0), then (B=p), so

\(\gcd(B,N)=p\) exactly as stated.

## 2. Newton expansion and high differences

For every (j\ge1), Pascal's identity gives the polynomial identity

\[
\Delta\binom Xj=\binom X{j-1}.
\]

Let (f\) be integer-valued of degree at most (D). Each

\(a_j=\Delta^jf(0)\) is an integer because it is an integral linear
combination of the integer values (f(0),\ldots,f(j)). Newton interpolation
on (0,1,\ldots,D) gives

\[
f(X)=\sum_{j=0}^{D}a_j\binom Xj.
\]

The triangular evaluation matrix has diagonal one, so the expansion is
unique. Applying the difference identity (k) times and evaluating at an
arbitrary integer (a) gives

\[
\Delta^kf(a)=\sum_{j=k}^{D}a_j\binom a{j-k}.
\]

This proves (5)--(6), including negative integer evaluation points.

For a nonnegative monomial exponent (m), the standard surjection count is

\[
\Delta^B X^m(0)
=\sum_{j=0}^{B}(-1)^{B-j}\binom Bj j^m
=B!\left\{\begin{matrix}m\\B\end{matrix}\right\}.
\]

Division as an exact integer identity proves (7). It also shows why
integer-valued normalization removes the formal (B!) while leaving the
remote Stirling coefficient.

## 3. Shifted-binomial phase transition

Apply Pascal's identity to the upper argument of

\(F(c)=\binom{N+c-1}{B}\). Iteration gives

\[
\Delta_c^kF(c)=\binom{N+c-1}{B-k},
\]

which proves (9).

Now fix (1\le c<p) and put (r=B-k). For (0\le k\le s), write

\[
r=p+t,qquad t=s-k.
\]

Here (0\le t<p) and (r<q). Lucas reduction modulo (p) gives

\[
\binom{pq+c-1}{p+t}
\equiv q\binom{c-1}{t}\pmod p.
\]

Lucas reduction modulo (q) gives zero because the lower units digit

\(r\ge p>c-1\). The integer (q\binom{c-1}{t}\) has exactly these two
components, so the first line of (10) follows by the Chinese remainder
theorem.

For (s<k\le B), one has (0\le r<p<q). Lucas reduction modulo each hidden
prime gives the same residue

\[
\binom{c-1}{r}.
\]

This proves the second line of (10). At (c=1), a binomial with upper
argument zero is nonzero only when its lower argument is zero. The first
branch therefore survives only at (k=s), with value (q), and the second
only at (k=B), with value one. This is exactly (11). It also verifies the
claimed loss of (p/q) asymmetry after the hidden threshold.

## 4. Short binomials and the central-binomial control

By binomial symmetry,

\[
\binom UV=\binom Uw
=\frac{\prod_{i=1}^{w}(U-w+i)}{w!},
\qquad w=\min(V,U-V).
\]

If (w<p<q), neither hidden prime divides (w!). The denominator is therefore
a unit modulo (N). For (r=p) or (q), the numerator valuation is positive
exactly when at least one displayed numerator factor is divisible by (r).
This proves (12)--(13) and the factor-first interpretation. If (w) is
numerical quasipolynomial, the displayed product and its individual gcds use
that many public operations. Nothing in this argument applies when both
binomial sides are long.

The difference identity from Section 2 gives

\[
\Delta^B\binom X{2B}\bigg|_{X=2B}=\binom{2B}{B},
\]

proving (14). For the base-(p) Kummer count, (B=p+s) has digits

\((1,s)_p\). Since (2s<p), adding (B+B) makes no base-(p) carry. For
base (q), (B<q<2B<2q), so adding (B+B) makes exactly one carry. Thus

\[
v_p\binom{2B}{B}=0,qquad
v_q\binom{2B}{B}=1,
\]

and (15) follows.

## 5. Prime-cycle lemma for the Stirling laws

The needed local identity follows from one orbit count. Let (r) be prime,
cycle (r) distinguished elements, and fix (n) other elements. In a set
partition fixed by that cycle, exactly one of these cases occurs:

1. all (r) distinguished elements lie in one invariant block; collapsing
   them to one element gives
   \(\left\{\begin{smallmatrix}n+1\\k\end{smallmatrix}\right\}\)
   fixed partitions; or
2. their blocks form an orbit of length (r). Each such block contains one
   distinguished element and no fixed element, so the distinguished elements
   are (r) singleton blocks. This gives
   \(\left\{\begin{smallmatrix}n\\k-r\end{smallmatrix}\right\}\)
   fixed partitions.

Every nonfixed orbit has size (r). Therefore

\[
\boxed{
\left\{\begin{matrix}n+r\\k\end{matrix}\right\}
\equiv
\left\{\begin{matrix}n+1\\k\end{matrix}\right\}
+\left\{\begin{matrix}n\\k-r\end{matrix}\right\}
\pmod r.}
\tag{A}
\]

This lemma is sufficient for all of (17)--(19).

### The (q)-components

Because (B\ge p) and (q<2p), one has (q<2B). Also (B<q). Apply (A)
with (r=q). For (T_0),

\[
T_0\equiv
\left\{\begin{matrix}2B-q+1\\B\end{matrix}\right\}
\pmod q.
\]

The second term in (A) has negative lower index. Since

\(q-B\ge s+2\ge3\), the displayed upper index is less than (B), so it is
zero. Similarly,

\[
T_1\equiv
\left\{\begin{matrix}2B-q+2\\B\end{matrix}\right\}=0\pmod q.
\]

This proves (17).

### The (p)-components

Apply (A) twice and use (B=p+s). First,

\[
\begin{aligned}
T_0
&=\left\{\begin{matrix}2p+2s\\p+s\end{matrix}\right\}\\
&\equiv
\left\{\begin{matrix}p+2s+1\\p+s\end{matrix}\right\}
+\left\{\begin{matrix}p+2s\\s\end{matrix}\right\}\\
&\equiv
\left\{\begin{matrix}2s+1\\s\end{matrix}\right\}
+\left\{\begin{matrix}2s+1\\s\end{matrix}\right\}
\pmod p.
\end{aligned}
\]

The discarded term

\(\left\{\begin{smallmatrix}2s+2\\p+s\end{smallmatrix}\right\}\)
is zero because (2s+1<p\). Hence (18) follows.

Likewise,

\[
\begin{aligned}
T_1
&=\left\{\begin{matrix}2p+2s+1\\p+s\end{matrix}\right\}\\
&\equiv
\left\{\begin{matrix}p+2s+2\\p+s\end{matrix}\right\}
+\left\{\begin{matrix}p+2s+1\\s\end{matrix}\right\}\\
&\equiv
2\left\{\begin{matrix}2s+2\\s\end{matrix}\right\}
\pmod p.
\end{aligned}
\]

Here

\(\left\{\begin{smallmatrix}2s+3\\p+s\end{smallmatrix}\right\}=0\)
because (p>s+3\), which follows from (2s+1<p) and (s>0). This proves
(19).

Since (q\mid T_i\) and (N=pq) is squarefree, the gcd is (q) when

\(p\nmid T_i\) and (N) when (p\mid T_i\). This proves (20).

## 6. Saturated examples and the pair condition

For (p=37,q=47),

\[
B=\lfloor\sqrt{1739}\rfloor=41,qquad s=4,qquad
\left\{\begin{matrix}9\\4\end{matrix}\right\}=7770.
\]

Thus (2\cdot7770=15540=37\cdot420\), verifying (21) and saturation of

\(T_0\).

For (p=19,q=29),

\[
B=\lfloor\sqrt{551}\rfloor=23,qquad s=4,qquad
\left\{\begin{matrix}10\\4\end{matrix}\right\}=34105.
\]

Thus (2\cdot34105=68210=19\cdot3590\), verifying (22) and saturation of

\(T_1\). The complementary residues are nonzero: (2\cdot34105\equiv19
\pmod {37}\) and (2\cdot7770\equiv17\pmod {19}\).

Because (p) is odd, the factor two in (18)--(19) is a unit modulo (p).
Both gcds saturate exactly when (p) divides both Stirling numbers, which is
(23). The recurrence gives

\[
\left\{\begin{matrix}2s+2\\s\end{matrix}\right\}
=s\left\{\begin{matrix}2s+1\\s\end{matrix}\right\}
+\left\{\begin{matrix}2s+1\\s-1\end{matrix}\right\}.
\]

After imposing divisibility of the first term in (23), divisibility of the
left side is equivalent to divisibility of the final term. This proves the
equivalence of (23) and (24) without any unproved inversion.

## 7. Evaluator and representation boundary

Inclusion-exclusion gives (25) by counting surjections onto (B) labeled
blocks. It has exactly (B+1) displayed terms. On the unresolved branch,

\[
p\le B<q,
\]

so (p\mid B!\), (q\nmid B!\), and

\(\gcd(B!,N)=p\). Modular division by (B!\) is invalid; checking that
denominator already factors (N).

The recurrence (26) is the usual operation of either inserting the new
element into one of (k) existing blocks or making it a singleton. It is
division-free, but the literal dynamic program must traverse indices of order

\(B\). These observations are costs of the displayed representations. They
are not lower bounds for other circuit or algorithm models.

For the exact-size assertion, the partitions of (2B) into (B) pairs give

\[
T_0\ge\frac{(2B)!}{2^B B!}\ge\left(\frac B2\right)^B.
\]

Also (T_0\le B^{2B}\). Hence

\[
\log_2 T_0=\Theta(B\log(B+1)).
\]

Adding the extra element of a (2B+1)-set to the block containing a fixed old
element injects the counted pair partitions into partitions counted by

\(T_1\), while (T_1\le B^{2B+1}\). Therefore the same bit bound holds for

\(T_1\). Balancedness gives (B=\Theta(\sqrt N)\), so exact materialization
uses exponentially many bits in the input length \(\Theta(\log N)\).

Thus the statement correctly stops at exact identities. It supplies neither a
numerical-quasipolynomial modular evaluator nor a lower bound excluding one.

## 8. Scope, search decision, and nonclaims

The shifted-binomial residues are exhausted by the two Lucas regimes in (10).
The short binomial regime is exhausted by the unit denominator and direct
numerator gcds in Theorem 3. The Stirling congruences reduce the remaining
factor question to two separate open requirements: operational evaluation of
the remote coefficient and, for the pair, exclusion or handling of (23).
Consequently the stated refusal to run a larger search on the same exact
families is consistent with the proved boundary.

Nothing reconstructed above supplies:

1. a numerical-QP evaluator for a remote binomial or Stirling coefficient;
2. an all-input factor oracle from either scalar or their pair;
3. a proof that simultaneous saturation in (23) is impossible;
4. a lower bound for integer-valued-polynomial, canonical-division,
   arithmetic, algebraic, or Boolean circuits;
5. a general Lucas or Kummer classification;
6. an all-input factoring algorithm; or
7. an empirical result.

The individual saturated examples explicitly rule out treating either scalar
alone as an all-input oracle. No statement argument establishes a probability
law or joint nonvanishing theorem. The exclusions are therefore precise.

## Qualification

The bit-size statement is asymptotic as the balanced input family grows. The
remote-evaluator discussion is a representation analysis, not a complexity
lower bound. These are already the statement's claimed meanings and do not
weaken the PASS verdict.

## Blind-review boundary

This reconstruction used the authenticated statement and independent
derivation only. I did not compile or run project code, use a remote host,
inspect private data, or read any forbidden F277 companion artifact before
sealing this file.
