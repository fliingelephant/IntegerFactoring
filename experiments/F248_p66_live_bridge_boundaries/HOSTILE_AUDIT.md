# Hostile audit of F248

## Verdict

**PASS.** I found no false probability, counting identity, missing hypothesis,
asymptotic transfer, or route-wide overclaim in the authenticated packet. The
fixed-past result is genuinely history-wise for one product fixed before the
fresh lift coordinate. The torus results use only one row, an exact duplicate,
or the named inverse point. Nothing in the packet bounds an unrelated
nonduplicate two-row relation or the full multirow P66 parity kernel.

No numerical exploration was used. I edited no frozen input and no durable
ledger.

## Authentication

I computed the four assigned SHA-256 digests before reading any packet
content. All four matched exactly.

| File | SHA-256 |
|---|---|
| STATEMENT.md | 3f45f82829715678e2950dc07c80296e4c3f8230baf9d34bc84d5e2381bd3621 |
| PROOF.md | d7c2a349784046cd3b3cb8a285c173db06409bfde69894c061244f2d9db1c263 |
| SELF_AUDIT.md | 13f5dfe0213cba44f5242467b1e4ebc3966a34546bbe8212783dbb79a8987240 |
| PROVENANCE.md | e4eac22617cf6e56cdd1ef90d65a1fc0337059eacfeb7ae3cc3e904eaff0259b |

I then read the full five-file packet and the promoted P208/P209 statements
used for the marker transfer.

## 1. Uniform full lifts and the conditional root law

The unit group modulo \(N^2\) has local cyclic orders \(p(p-1)\) and
\(q(q-1)\). Since \(\gcd(E,N)=1\), the \(E\)-power kernel has exactly

\[
K=\gcd(E,p-1)\gcd(E,q-1)
\]

elements. A uniform input is therefore uniform on an image of size
\(N\varphi(N)/K\).

There are exactly \(\varphi(N)\) positive unit squares below \(N^2\): each is
\(s^2\) for one unit \(1\le s<N\). Intersecting this set with the power-map
image can only decrease it. This proves the upper bound \(K/N\); it does not
silently assume that every such square is reached.

For a fixed reached square, the input fibre is one kernel coset. On a local
kernel of order \(g_r=\gcd(E,r-1)\), the \(E/2\)-power image has size

\[
\frac{g_r}{\gcd(g_r,E/2)}\in\{1,2\}.
\]

It has size two exactly when \(v_2(E)\le v_2(r-1)\). Its elements are then
\(\{1,-1\}\). If one or both local images are active, translation by this
sign subgroup leaves exactly half of the normalized roots mixed. Thus the
conditional half law has the claimed direction and conditioning.

On the P209 family, the exact shifted-gcd table gives \(K=4\) for
\(E=N-1\). The construction has \(v_2(p-1)=2\), \(v_2(q-1)=1\), and
\(v_2(N-1)=1\), so both sides are active. For \(E=N^2-1\), the same table
and its prime-power support give local kernel sizes \(12\) and \(2\), hence
\(K=24\). Here \(v_2(E)\ge4\), so both local root images are trivial. The
packet correctly withholds the half law in this case.

## 2. Principal lifts and the fixed-past squarefree-kernel lemma

The binomial expansion modulo \(N^2\) gives

\[
h_t=h_0+Ea^{E-1}t\pmod N.
\]

The slope is a unit because \(a\) and \(E\) are units modulo \(N\). Thus the
lift digit visits every residue exactly once. The congruence
\(s^2\equiv x^2\pmod N\) has exactly four canonical positive roots below
\(N\), whose integer squares are distinct and below \(N^2\). Exactly two
roots have mixed signs relative to \(x\). This proves the exact \(4/N\) and
\(2/N\) laws, not merely upper bounds.

The second-root equivalence also has both directions. A successful square
gives a mixed root and a gcd factor. Given \(p,q\), CRT constructs the two
mixed roots, their square digits, and the corresponding lift parameters.
Nothing in this fibre argument distributes the fixed section \(t=0\), and
the packet explicitly leaves that section open.

For the fixed-past extension, write \(P=du^2\) with \(d\) squarefree. If
\(PB_t\) is a square, valuation parity forces \(B_t=dv^2\). The strict bound
\(B_t<N^2\) gives \(0<v<N/\sqrt d\le N\). Since

\[
X^2\equiv du^2\pmod N,
\]

\(d\) is a quadratic residue on both hidden prime sides. Therefore
\(dv^2\equiv x^2\pmod N\) has exactly four CRT classes, and the interval
\(0<v<N\) contains at most one integer from each class. Multiplication by
\(du(Xx)^{-1}\) bijects those four classes with the four roots of one. At
most two are mixed. Each surviving \(v\) fixes one digit and hence one
\(t\). The \(2/N\) conditional bound is exact as an upper bound.

This proof still works when \(d>N\) or \(P\) is very large: then the interval
only shrinks, and it can be empty. It does require \(P\) to be fixed before
the fresh \(t\) and to be a unit modulo \(N\), exactly as stated. It cannot
be union-bounded over all subsets selected after the fresh row is visible.

## 3. Scalar duplicate and reciprocal-output bounds

If two canonical outputs are equal modulo \(N^2\), their base ratio lies in
the \(E\)-power kernel modulo \(N\). For each second base, at most \(K\)
first bases pass this necessary condition. Hence the duplicate probability
is at most \(K/\varphi(N)\). Equality of outputs makes the supplied-root
ratio a root of one, and only its mixed cases factor. The pair union bound is
valid for a numerical-quasipolynomial bank because \(K\) is constant on the
two P209 specializations and \(\varphi(N)=2^{n-O(1)}\).

For the reciprocal-output pair, \(uv\equiv1\pmod {N^2}\). If \(uv=R^2\)
as integers, then \(0<R<N^2\) and \(R\) is one of the four canonical roots
of one modulo \(N^2\). For each such \(R\), a successful \(u\) divides
\(R^2\), so the number of candidate outputs is at most the stated sum of
four divisor counts. A fixed output has at most \(K\) canonical base
preimages. This gives \(2^{-n+o(n)}\) on P209.

This argument uses the least positive reciprocal of the output modulo
\(N^2\). It does not transfer to first taking the canonical inverse base
modulo \(N\). The packet repeats this exclusion in the theorem, proof, and
scope statement.

## 4. Raw torus fibres, Pell count, and duplicates

The local norm-one torus has order
\(m_r=r-\left(\frac Dr\right)\). Its points with \(x=0\) are exactly the
zero or two solutions of \(-Dy^2=1\), so their number is
\(z_r=1+\left(\frac{-D}{r}\right)\). Conditioning on \(x\) being a unit
leaves exactly

\[
H=(m_p-z_p)(m_q-z_q)
\]

clean global points. Every admitted global \(y\) has two nonzero choices of
\(x\) on each side and therefore exactly four clean points.

An exact-square row solves \(R^2-D_0y^2=1\). If \(D_0\) is an integer
square, positive factorization forces \(y=0\). Otherwise every nonnegative
solution is a power of the fundamental positive Pell unit. That unit is
strictly larger than \(2\sqrt{D_0}\), while \(y<N\) gives

\[
R+y\sqrt{D_0}<2N\sqrt{D_0}+1.
\]

The displayed \(B_D(N)\) is therefore a valid upper count including
\(y=0\), and it is \(O(n)\) uniformly for \(1\le D_0<N\).

Because \(D_0>0\) and \(y\) is canonical, equality of two integer rows is
equivalent to equality of their \(y\)-coordinates. Counting ordered samples
inside four-point fibres gives exactly \(4/H\) for a duplicate and \(2/H\)
for a duplicate whose root ratio changes sign on exactly one hidden side.

## 5. Powered fibres and the P209 marker transfer

In a local image subgroup, the second point with the same \(y\) as
\(U=(x,y)\) is \(-U^{-1}=(-x,y)\). It lies in the subgroup exactly when
\(-1\) does, equivalently when the subgroup order is even. Removing \(x=0\)
removes the only fixed points of this involution. Thus a clean local
\(y\)-fibre has size two for even image order and one for odd image order.

When the two local image orders are coprime, at most one is even. Every
global fibre consequently has size at most two, proving the powered Pell
bound \(2B_D(N)/H'\). If both orders are odd, a repeated \(y\) is the same
point and supplies no second root. If exactly one is even, every admitted
global fibre has two points, and the distinct ordered pair changes one local
sign. The exact useful-duplicate probability is therefore \(1/H'\).

The P209 transfer preserves all required hypotheses. For exponent
\(N^2-1=(N-J)(N+J)\), the local image orders are the exact square-word
residuals \(t_{p,a}\) and \(t_{q,b}\); P209 proves that all four such
residuals are pairwise coprime. In each orientation the two residuals retain
the corresponding distinct exponential marker primes. For a P208 exponent
\((N-J)W\) with \(W\) in P209's numerical-QP signed-power grammar, the local
orders are divisors of the coprime private parts and the same two markers
survive \(W\). Subtracting at most two \(x=0\) points on either side does not
change the exponential scale. Hence \(H'=2^{\Omega(n)}\) in exactly the
cases claimed. No transfer is made to an arbitrary public exponent that can
absorb a marker.

## 6. Torus inverse pair and divisor asymptotics

For \(1\le y<N\), direct expansion verifies

\[
(1+D_0y^2)(1+D_0(N-y)^2)
=(1-D_0y(N-y))^2+D_0N^2.
\]

If the left side is \(R^2\), then \(R>|C|\), so both \(R-C\) and \(R+C\)
are positive and form a divisor pair of \(D_0N^2\). There are at most
\(\tau(D_0N^2)\) resulting values of \(C\), and the quadratic equation for
\(y\) has at most two integer roots. This proves the \(2\tau(D_0N^2)\)
count. Multiplying by the exact raw fibre size four or the powered fibre
bound two gives the stated \(8\tau/H\) and \(4\tau/H'\) bounds.

The restriction \(1\le y<N\) is material. At \(y=0\), the inverse point is
the same point and the row product is \(1\); its normalized root is global,
so it is only the already-counted duplicate decoy and not a nontrivial
inverse-pair bridge.

Since \(D_0<N\), one has \(D_0N^2<N^3\). Thus the standard uniform divisor
bound gives \(\tau(D_0N^2)=2^{o(n)}\). The reciprocal-output divisor
arguments likewise involve only integers with \(O(n)\) bits. The packet uses
these bounds only for cardinality and probability; it does not claim a
quasipolynomial divisor-enumeration algorithm.

Finally, \(C\equiv x^2\pmod N\), so \(C\) is a unit on the clean set. The
exact product root normalizes to \(R/C\), a root of one. Only a mixed root
factors, as claimed.

## 7. Exact scope boundary

Every negative estimate in the packet relies on one rigid event:

1. one row is an exact square;
2. two rows are exactly equal;
3. scalar outputs are exact reciprocals modulo \(N^2\); or
4. torus points are an exact inverse pair.

P209's private markers control the orders and sizes of specified hidden
source groups. They do not control the ordinary integer-prime parity vectors
of distinct values \([a^E]_{N^2}\) or \(1+D_0y^2\). Therefore none of the
proved union bounds applies to an unrelated nonduplicate pair, a mixed-arm
relation, or a general multirow P66 dependency. The statement and proof say
this explicitly. No general P66 obstruction is overclaimed.
