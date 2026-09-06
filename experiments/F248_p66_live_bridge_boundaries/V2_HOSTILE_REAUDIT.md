# F248 V2 hostile re-audit

## Verdict

**PASS.** I found no false identity, incorrect count, probability-space
mismatch, missing operative hypothesis, invalid asymptotic transfer, or
undeclared P208/P209 dependency in the authenticated V2 packet.

The conclusions are narrow. They apply only to the stated rigid events and
probability spaces. The bank corollary is conditional on its displayed size
hypotheses. It does not construct a family that satisfies those hypotheses.

I did not edit a frozen input or a durable ledger. This report is the only
file created by the re-audit.

## Authentication

I first computed all five assigned V2 digests without opening their contents.
All five matched.

| File | SHA-256 |
|---|---|
| `V2_STATEMENT.md` | `57ea62c39ce0e04b4a271135e613eabdcf79a32dd5df85dc692effb6dc8d8504` |
| `V2_PROOF.md` | `0d292831f42bb515d298c26846c7c912cddbf07682b7b63564e9ff2fce3c46f8` |
| `V2_SELF_AUDIT.md` | `8e35ea5f0ea84ba8c02b848acc4fb1a1dbb53dd5c404c9929ae78975b0795297` |
| `V2_PROVENANCE.md` | `302e9ffa432c73cda9ced650e2cc3e6ab309e4f5846777b0880fa5903e48ef6a` |
| `V2_MANIFEST.md` | `52961d5d130590dbd4d858544fc1ffa29e9ea8aafebc6cb39ccf20bebb56bff0` |

I then opened only the authenticated V2 manifest. I extracted its preserved
V1/audit digest list and authenticated all seven listed files before opening
any of them. All seven matched.

| Preserved file | SHA-256 |
|---|---|
| `STATEMENT.md` | `3f45f82829715678e2950dc07c80296e4c3f8230baf9d34bc84d5e2381bd3621` |
| `PROOF.md` | `d7c2a349784046cd3b3cb8a285c173db06409bfde69894c061244f2d9db1c263` |
| `SELF_AUDIT.md` | `13f5dfe0213cba44f5242467b1e4ebc3966a34546bbe8212783dbb79a8987240` |
| `PROVENANCE.md` | `e4eac22617cf6e56cdd1ef90d65a1fc0337059eacfeb7ae3cc3e904eaff0259b` |
| `MANIFEST.md` | `4a100390362d1f446142c149329f4f4be7a07ad4f215501c69afcb41954fa1f5` |
| `HOSTILE_AUDIT.md` | `9321ec03a26e1d0ddc5f29dee2874b6498b9a0d0b0bb542c58b4d0f8b2e7c142` |
| `BLIND_RECONSTRUCTION.md` | `0a4ec2ec1627026dd01c4936a8f3cc71831dd3cd043fbdb8d5c87dc0f8a5ef22` |

## Common reconstruction

CRT gives

\[
(\mathbb Z/N^2\mathbb Z)^\times
\cong
(\mathbb Z/p^2\mathbb Z)^\times
\times
(\mathbb Z/q^2\mathbb Z)^\times.
\]

The two local groups are cyclic of orders (p(p-1)) and (q(q-1)).
Because (E) is coprime to (N), the local (E)-power kernels have sizes

\[
g_p=\gcd(E,p-1),\qquad g_q=\gcd(E,q-1).
\]

The global kernel size is (K=g_pg_q). A unit square modulo (N=pq) has
four roots. Relative to one root, two have global CRT signs and two have
mixed signs. For an exact square (s^2) with supplied root (x), the
signed gcds factor (N) exactly when (sx^{-1}\bmod N) is mixed.

The size parameter satisfies

\[
N,\varphi(N)=2^{n+O(1)}.
\]

The Euler factors are bounded below by an absolute positive constant because
(p,q) are distinct odd primes. Every integer used in a divisor bound has
(O(n)) bits. The standard uniform divisor estimate therefore gives
(\tau(m)=2^{o(n)}) for each such integer.

These facts also settle the basic edge cases. There are exactly four roots
of one modulo both (N) and (N^2). All supplied roots in the packet are
units. The raw and powered clean torus spaces are nonempty because they
contain the identity.

## Theorem A: uniform full lifts

The (E)-power image modulo (N^2) has size

\[
\frac{\varphi(N^2)}K=\frac{N\varphi(N)}K.
\]

A uniform input is uniform on that image. There are exactly
(\varphi(N)) positive unit squares below (N^2): each has the unique form
(s^2), where (1\le s<N) and (s) is a unit modulo (N). Intersecting
these squares with the power image gives

\[
\Pr([A^E]_{N^2}\text{ is an exact square})
\le
\frac{\varphi(N)}{N\varphi(N)/K}
=\frac KN.
\]

For one reached square output, its input fibre is one kernel coset. Uniform
input conditioning makes the kernel element uniform. On a local side (r),
reduction modulo (r) is injective on the local (E)-kernel: that kernel
has order dividing (r-1), while the kernel of reduction has order (r).
The local supplied-root variation has size

\[
\frac{g_r}{\gcd(g_r,E/2)}.
\]

If (e=v_2(E)) and (t=v_2(r-1)), the odd part cancels and this quotient is
two exactly when (e\le t). Its elements square to one, so it is
(\{1,-1\}). Otherwise the quotient is one and the image is (\{1\}).

If at least one side is active, translation by its sign pairs a global root
with a mixed root. Every resulting coset is half global and half mixed.
Thus exactly half of the preimages of the fixed reached square factor (N).
If neither side is active, V2 makes no half-law claim.

## Theorem B: a complete principal-lift fibre

For a fixed residue (a\bmod N), binomial expansion gives

\[
(a_0+tN)^E
\equiv
a_0^E+Ea_0^{E-1}tN
\pmod {N^2}.
\]

Therefore

\[
h_t=h_0+Ea^{E-1}t\pmod N.
\]

The slope is a unit. Hence (t\mapsto h_t) is a bijection on the (N)
lift digits.

Put (x=[a^{E/2}]_N). The unit square (r=x^2\bmod N) has four canonical
roots (1\le s<N). Their four integer squares are distinct, lie below
(N^2), and are all exact squares in the principal fibre. Conversely, every
exact square in the fibre has one of these roots. Exactly two normalized
roots (s/x\bmod N) are mixed. This proves the exact laws

\[
\Pr(\text{square})=\frac4N,
\qquad
\Pr(\text{useful square})=\frac2N.
\]

A useful digit gives its positive integer root (s), hence a mixed second
root of (r\bmod N). In the other direction, a mixed root (s) gives

\[
h_s=\frac{s^2-r}{N},
\qquad
t=(h_s-h_0)(Ea^{E-1})^{-1}\pmod N.
\]

Factoring (N) constructs both mixed roots by CRT. Thus the asserted
polynomial-time equivalence has both directions.

### Fixed-past squarefree-kernel bound

Fix (P>0) and its supplied unit root (X) before sampling the fresh
uniform (t). Write

\[
P=du^2
\]

with (d) positive and squarefree. If (PB_t) is an exact square, parity
of every ordinary prime valuation forces

\[
B_t=dv^2.
\]

Since (B_t<N^2),

\[
0<v<\frac N{\sqrt d}\le N.
\]

The event makes (d,u,v) units modulo (N). From
(X^2\equiv du^2\pmod N), (d) is a square on both prime sides. The
congruence (dv^2\equiv x^2\pmod N) therefore has exactly four CRT
classes. The strict interval (0<v<N) contains at most one representative
of each class.

The positive exact root is (S=duv). Multiplication by the fixed unit
(du(Xx)^{-1}) maps the four possible (v)-classes injectively onto the
four roots of one. At most two images are mixed. Each surviving integer
(v) fixes (B_t), its lift digit, and one (t). Hence at most two of the
(N) fresh coordinates are useful.

The proof remains valid when (P) or (d) is large; the interval then only
shrinks. It needs one product and root fixed before the fresh coordinate.
It gives no post-hoc bound over many past subsets and no result for the fixed
section (t=0).

## Theorem C: canonical scalar duplicates

For a fixed canonical unit (b), the equality

\[
[a^E]_{N^2}=[b^E]_{N^2}
\]

places (a) in one full (E)-power fibre modulo (N^2). The full fibre
has (K) elements. Its intersection with the canonical set has at most
(K) elements. Averaging over independent uniform (b) gives

\[
\Pr[u(a)=u(b)]\le\frac K{\varphi(N)}.
\]

For a duplicate, the two supplied roots square to the same residue. Their
ratio is a root of one and factors (N) exactly when mixed. The probability
space includes the diagonal (a=b); the upper bound remains valid.

## Theorem D: reciprocal outputs

Let (v=[u^{-1}]_{N^2}). If (uv=R^2) as positive integers, then

\[
R^2\equiv1\pmod {N^2},
\qquad 0<R<N^2.
\]

Thus (R) is one of the four members of (\mathcal R_M). For fixed (R),
the exact identity forces (u\mid R^2) and (v=R^2/u). There are at most
(\tau(R^2)) candidate outputs. Each output has at most (K) canonical
base preimages. Summing over the four roots gives

\[
\Pr(uv\text{ is an exact square})
\le
\frac{K}{\varphi(N)}
\sum_{R\in\mathcal R_M}\tau(R^2)
=\frac{KS_M}{\varphi(N)}.
\]

Because (R^2<N^4), (S_M=2^{o(n)}). The supplied product root is
(x x^{-1}=1). Therefore the exact root (R\bmod N) factors exactly in
the two mixed cases. The theorem uses the reciprocal of the output modulo
(N^2). A canonically lifted inverse base modulo (N) need not produce
that output and is correctly excluded.

## Raw torus space and Theorem E

Over (\mathbb F_r), the norm-one torus has order

\[
m_r=r-\left(\frac Dr\right).
\]

The points with (x=0) solve (-Dy^2=1), so their number is

\[
z_r=1+\left(\frac{-D}{r}\right)\in\{0,2\}.
\]

CRT therefore gives exactly

\[
H=(m_p-z_p)(m_q-z_q)
\]

clean global points. For each admitted global (y\bmod N), each prime side
has two nonzero (x)-roots. Every raw clean global (y)-fibre consequently
has exactly four points. Uniform clean-point sampling is uniform over these
(H) points.

An exact-square row has

\[
R^2-D_0y^2=1.
\]

If (D_0=d^2) is an integer square, then

\[
(R-dy)(R+dy)=1,
\]

so (R=1) and (y=0). This is the only square row in that branch.

If (D_0) is not an integer square, let
(\epsilon=R_1+y_1\sqrt{D_0}) be the least positive Pell unit above one.
All positive solutions are powers of (\epsilon). Moreover,

\[
\epsilon>2y_1\sqrt{D_0}\ge2\sqrt{D_0},
\]

while (0<y<N) gives

\[
R+y\sqrt{D_0}<2N\sqrt{D_0}+1.
\]

The number of positive-(y) solutions is at most the logarithmic floor in
the definition of (B_D(N)). Adding (y=0) proves the stated count. The
denominator has a positive absolute lower bound in the nonsquare branch,
and the numerator is (O(\log N)). Hence (B_D(N)=O(n)) uniformly.

At most (B_D(N)) admitted (y)-values yield an exact square. Multiplying
by the four-point fibre size proves

\[
\Pr[A_y\text{ is an exact square}]\le\frac{4B_D(N)}H.
\]

Since (D_0>0) and canonical (y)'s are nonnegative,
(A_{y_1}=A_{y_2}) exactly when (y_1=y_2). There are (H/4) fibres of
size four. Ordered independent sampling gives

\[
\Pr(\text{duplicate})=\frac4H.
\]

For each first point, exactly two points in its fibre change one local sign.
Thus

\[
\Pr(\text{useful duplicate})=\frac2H.
\]

## Theorem F: powered torus images

On the local cyclic torus of order (m_r), the (W)-power image has order

\[
\rho_r=\frac{m_r}{\gcd(m_r,W)}.
\]

A uniform input maps uniformly onto this image. CRT gives the product of
the two local images. Conditioning the output on (x) being a unit gives
the uniform distribution on the clean image of size

\[
H'=(\rho_p-z'_p)(\rho_q-z'_q).
\]

An image subgroup contains either both (x=0) points or neither, so
(z'_r\in\{0,2\}). The identity is clean, so this conditional space is
nonempty.

For a clean local point (U=(x,y)), the only other point with the same
(y) is

\[
(-x,y)=-U^{-1}.
\]

It lies in the image subgroup exactly when (-1) lies there. In a cyclic
group, this happens exactly when the image order is even. The fixed points
of this involution have (x=0) and were removed. Thus a clean local
(y)-fibre has size two for even image order and size one for odd image
order.

The condition (\gcd(\rho_p,\rho_q)=1) permits at most one even side.
Every clean global fibre has size at most two. The Pell count therefore
gives

\[
\Pr[A_y\text{ is an exact square}]\le\frac{2B_D(N)}{H'}.
\]

If both image orders are odd, every global fibre is a singleton. Equal
(y)-coordinates then identify the same point, so no useful duplicate
exists. If exactly one image order is even, every global clean fibre has two
points. The distinct pair changes the (x)-sign on exactly one prime side.
There are (H'/2) fibres and two ordered distinct pairs per fibre. Hence

\[
\Pr(\text{useful duplicate})
=\frac{(H'/2)\,2}{(H')^2}
=\frac1{H'}.
\]

These two parity cases are exhaustive under the coprimality hypothesis.
V2 correctly asserts no general lower bound for (H').

## Theorem G: inverse-point identity and count

For (1\le y<N), the group inverse has canonical coefficient (N-y).
Direct expansion gives

\[
\begin{aligned}
A_yA_{N-y}
&=(1+D_0y^2)(1+D_0(N-y)^2)\\
&=(1-D_0y(N-y))^2+D_0N^2\\
&=C^2+D_0N^2.
\end{aligned}
\]

Also (C\equiv1+D_0y^2\equiv x^2\pmod N), so (C) is a unit modulo
(N) on the clean set.

If the product is (R^2), then (R>|C|) and

\[
(R-C)(R+C)=D_0N^2.
\]

Both factors are positive. A positive divisor (R-C) determines (R+C)
and then (C). There are at most (\tau(D_0N^2)) candidate values of
(C). For each one, the quadratic equation

\[
C=1-D_0y(N-y)
\]

has at most two integer roots. Thus at most
(2\tau(D_0N^2)) nonzero canonical (y)-values work.

Every raw (y)-fibre has four points. Under the powered coprime-image
hypothesis, every fibre has at most two. Therefore

\[
\Pr_{\rm raw}(y\ne0\text{ and square inverse product})
\le\frac{8\tau(D_0N^2)}H,
\]

and

\[
\Pr_{\rm powered}(y\ne0\text{ and square inverse product})
\le\frac{4\tau(D_0N^2)}{H'}.
\]

Since (D_0N^2<N^3), the divisor factor is (2^{o(n)}). The supplied
product root is (x^2\equiv C\pmod N). Hence (R/C\bmod N) is a root of
one and factors exactly when mixed. The excluded (y=0) point is
self-inverse and has row product one. It is a global decoy, not a useful
inverse bridge.

## Conditional bank corollary

Each displayed bank estimate is the union bound for the corresponding
one- or two-sample theorem.

- Full lifts contribute at most (TK/N).
- At each adaptive principal-lift stage, condition on the full past. The
  fixed-past theorem gives at most (2/N) for every past in which the
  product and its supplied root are fixed before the fresh uniform
  coordinate. Taking expectations and summing gives (2T/N). Independence
  between stages is not needed.
- Canonical scalar pairs contribute at most
  (\binom T2K/\varphi(N)). The (T) reciprocal-output pairs contribute at
  most (TKS_M/\varphi(N)).
- Raw torus points contribute at most (4TB_D/H) for one-row squares,
  (2\binom T2/H) for useful duplicates, and
  (8T\tau(D_0N^2)/H) for the stated nonzero inverse event.
- Under Theorem F, powered points contribute at most (2TB_D/H'), zero or
  (\binom T2/H') for useful duplicates, and
  (4T\tau(D_0N^2)/H') for the stated nonzero inverse event.

If

\[
T=2^{(\log n)^{O(1)}},
\]

then both (T) and (T^2) are (2^{o(n)}). The factors (B_D), (S_M),
and (\tau(D_0N^2)) are also subexponential. Thus (K=2^{o(n)}) makes
each scalar numerator subexponential against (N) or (\varphi(N)).
The premises (H=2^{\Omega(n)}) and (H'=2^{\Omega(n)}) do the same for
the applicable raw and powered torus estimates. Every applicable displayed
bank probability is consequently (2^{-\Omega(n)}).

This transfer is conditional. No step derives (K=2^{o(n)}),
(H=2^{\Omega(n)}), or (H'=2^{\Omega(n)}) from a named family.

## P208/P209 dependency audit

The V2 statement and proof contain no operative reference to P208, P209, a
specific private marker, an orientation, a residual-order construction, or
a signed-power grammar. Generic mentions of removed family machinery occur
only in scope disclaimers. The quantities needed by A--G are defined in V2:

- (K) is the exact scalar power-kernel size;
- (H) is the exact clean raw torus size;
- (W), (\rho_r), (z'_r), and (H') define the powered image;
- powered fibre coprimality is an explicit premise;
- all exponential size claims are explicit premises of the conditional
  corollary.

The proof uses only CRT, cyclic prime-square unit groups, elementary finite
field torus orders, Pell growth, and the divisor bound. No P208/P209 fact is
needed to prove an A--G statement or the conditional corollary. The V1
statement-only failure is therefore repaired by removal, not by an implicit
transfer.

## Corroborating edge-case enumeration

As a check, I exhaustively tested small distinct primes from
(\{3,5,7,11\}), admissible even exponents (2\le E\le14), all canonical
unit bases, all unit (D_0), and (1\le W\le8). The checks covered:

- 30 full-lift families and every reached square fibre;
- 900 principal fibres;
- 3,600 fixed-past instances;
- 30 canonical duplicate and reciprocal-output instances;
- 164 raw torus and inverse-count instances;
- 481 powered images with coprime local image orders.

All exact laws and upper bounds held. These finite checks are corroboration
only. The verdict rests on the reconstructions above.

## Exact scope

V2 controls only one exact-square row, one exact duplicate, one scalar
output with its reciprocal output, one torus point with its inverse, and one
fresh principal lift against one product fixed in advance. It does not
control an unrelated nonduplicate relation, a mixed scalar-torus relation,
post-hoc subset selection, the fixed canonical lift section, a canonical
inverse-base pair, or a general multirow integer-prime parity dependency.
It gives no all-input factoring algorithm and no unconditional
quasipolynomial success or failure result.

Within that exact boundary, the authenticated V2 packet passes.
