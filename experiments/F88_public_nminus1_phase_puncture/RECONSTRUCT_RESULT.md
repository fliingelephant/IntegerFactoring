# PASS

The SHA-256 of RECONSTRUCT_STATEMENT.md is
f6b264e4c7e45fbac65fe8071dc59b68332715f559102f09df3da076f384d054,
as required. Every structural, valuation, counting, algorithmic, complexity,
and fixed-specialization claim is correct.

## 1. Structure and the public divisibility \(h\mid N-1\)

Write the graph as

\[
H=\{(x,\varphi(x)):x\in H_p\},
\]

where \(\varphi:H_p\to H_q\) is an isomorphism. Since
\(\mathbb F_p^\times\) is cyclic, \(H_p\), and hence \(H\), is cyclic of
order \(h\).

For \((x,y)\in K\), define

\[
\psi(x,y)=y\varphi(x)^{-1}\in H_q.
\]

The pure-phase hypotheses ensure that \(x\in H_p\) and \(y\in H_q\).
The map \(\psi\) is a homomorphism, and

\[
\ker\psi=H.
\]

Let \(D=\psi(K)\). Then the first isomorphism theorem gives

\[
K/H\simeq D.
\]

The group \(D\) is a subgroup of the cyclic group \(H_q\) of order \(h\).
Therefore \(D\) is cyclic,

\[
|D|=[K:H]=c,
\]

and

\[
\boxed{c\mid h}.
\]

Moreover, if \(\psi(x,y)=d\), then

\[
(x,y)(x,\varphi(x))^{-1}=(1,d)\in K.
\]

It follows that

\[
K=H\cdot(\{1\}\times D)
\]

with trivial intersection.

The graph projections give

\[
|H_p|=|H_q|=h.
\]

Lagrange's theorem in the two local multiplicative groups gives

\[
h\mid p-1,\qquad h\mid q-1.
\]

Hence \(p\equiv q\equiv1\pmod h\), so

\[
N=pq\equiv1\pmod h.
\]

Thus

\[
\boxed{h\mid N-1}.
\]

This conclusion uses no claim that \(p-1\) or \(q-1\) is publicly known.
Only the multiple \(N-1\) is used by the executable algorithm.

## 2. General power contraction

Let \(M\geq1\), and put

\[
h_M=\frac h{\gcd(h,M)},\qquad
c_M=\frac c{\gcd(c,M)}.
\]

Because \(K\) is the internal direct product of \(H\) and
\(\{1\}\times D\), and the ambient group is abelian,

\[
K^M=H^M\cdot(\{1\}\times D^M)
\]

with trivial intersection. The power image of a cyclic group of order \(r\)
has order \(r/\gcd(r,M)\). Therefore

\[
|H^M|=h_M,\qquad |D^M|=c_M,
\]

and

\[
|K^M|=h_Mc_M,\qquad [K^M:H^M]=c_M.
\]

Projection commutes with powering. Since \(K_p=H_p\) and \(K_q=H_q\), both
local images of \(K^M\) have order \(h_M\). The kernel of either projection
from \(K^M\) consequently has size \(c_M\), and the two kernels intersect
only in the global identity. Positive separators form their symmetric
difference. Thus, whenever \(c_M>1\), their exact count and density are

\[
2c_M-2,
\qquad
\frac{2(c_M-1)}{c_Mh_M}.
\]

The same count is zero when \(c_M=1\), in which case the phase extension has
contracted to \(K^M=H^M\).

## 3. The public \(N-1\) puncture

Choose a prime \(\ell\mid c\), and write

\[
e=v_\ell(N-1),\qquad
H_\ell=v_\ell(h),\qquad
C_\ell=v_\ell(c).
\]

Since \(c\mid h\mid N-1\),

\[
1\leq C_\ell\leq H_\ell\leq e.
\]

Therefore

\[
j=e-C_\ell+1
\]

satisfies \(1\leq j\leq e\), and

\[
E=(N-1)/\ell^j
\]

is a positive integer. Its \(\ell\)-adic valuation is

\[
v_\ell(E)=e-j=C_\ell-1.
\]

For every prime \(r\ne\ell\),

\[
v_r(E)=v_r(N-1)\geq v_r(h)\geq v_r(c).
\]

It follows that every prime component of \(c\) except one copy of \(\ell\)
is absorbed by \(E\):

\[
\boxed{c_E=\frac c{\gcd(c,E)}=\ell}.
\]

Likewise, all prime components of \(h\) other than its \(\ell\)-component
are absorbed, and

\[
v_\ell(h_E)
=H_\ell-(C_\ell-1)
=H_\ell-C_\ell+1.
\]

Hence

\[
\boxed{h_E=\ell^{H_\ell-C_\ell+1}}.
\]

The powered group has exact size

\[
\boxed{|K^E|=h_Ec_E
=\ell^{H_\ell-C_\ell+2}}.
\]

Because \(c_E=\ell>1\), Section 2 gives exactly

\[
\boxed{2\ell-2}
\]

positive separators. Their exact density is

\[
\boxed{
\frac{2\ell-2}{\ell^{H_\ell-C_\ell+2}}
=\frac{2(\ell-1)}{\ell^{H_\ell-C_\ell+2}}
}.
\]

### Edge cases

- If \(e>H_\ell\), the larger puncture depth
  \(j=e-C_\ell+1\) removes the excess public \(\ell\)-valuation and still
  leaves exactly \(C_\ell-1\) copies of \(\ell\) in \(E\).
- If \(C_\ell<H_\ell\), the old graph is not fully contracted. Its exact
  residual order is \(\ell^{H_\ell-C_\ell+1}\), which is why the size
  promise must include the full residual exponent.
- If \(\ell=2\), then \(c_E=2\), the separator count is exactly two, and
  the same formulas hold without a parity exception.
- A prime \(r\ne\ell\) dividing \(h\) can be arbitrarily large and need not
  be scanned. The exponent \(E\) retains the full public valuation
  \(v_r(N-1)\geq v_r(h)\), so that component is killed automatically.

If \(h=1\), then \(c\mid h\) forces \(c=1\), contrary to the strict-extension
premise. Thus no hidden \(h=1\) exception exists.

## 4. Public deterministic algorithm

Let \(g_1,\ldots,g_s\) be the supplied public generators of \(K\). For each
prime \(\ell\leq L\) dividing \(N-1\), compute
\(e=v_\ell(N-1)\). For every \(1\leq j\leq e\), do the following:

1. Set \(E=(N-1)/\ell^j\).
2. Compute \(g_1^E,\ldots,g_s^E\bmod N\).
3. Starting from \(1\), enumerate their multiplicative closure by
   breadth-first search.
4. Store canonical residues already seen and gcd-test \(y-1\) for every
   newly discovered residue \(y\).
5. Return \(d\) only after checking \(1<d<N\) and \(d\mid N\).
6. Abandon the current exponent immediately after discovering more than
   \(S\) distinct residues.

All choices in this procedure are public. Trial division or a sieve through
\(L\), followed by repeated division of \(N-1\), lists precisely the scanned
primes and their public valuations.

### Completeness under the stated promise

Assume some \(\ell\mid c\) satisfies

\[
\ell\leq L,\qquad
\ell^{H_\ell-C_\ell+2}\leq S.
\]

The algorithm scans this \(\ell\) and every puncture depth through
\(e=v_\ell(N-1)\). In particular, it scans the hidden successful depth

\[
j=e-C_\ell+1.
\]

For that depth, Section 3 proves

\[
|K^E|=\ell^{H_\ell-C_\ell+2}\leq S
\]

and proves that \(K^E\) contains \(2\ell-2>0\) positive separators.

Powering is a homomorphism in the abelian unit group, so

\[
K^E=\langle g_1^E,\ldots,g_s^E\rangle.
\]

The breadth-first queue therefore empties only after every element of
\(K^E\) has been reached. Since the group has at most \(S\) elements, the
cap does not fire. A separator \(y\) is enumerated, and
\(\gcd(y-1,N)\) is one of \(p,q\). The algorithm succeeds.

### Wrong exponents, inverse-free enumeration, and redundancy

If a wrong exponent produces more than \(S\) residues, the search stops on
the \((S+1)\)-st discovery. Before that discovery, at most \(S\) residues
can be dequeued, each with at most \(s\) outgoing generator multiplications.
If the powered subgroup has at most \(S\) elements, it is fully enumerated.
The boundary case \(|K^E|=S\) is complete because stopping occurs only after
more than \(S\) discoveries.

Explicit inverse edges are unnecessary. In a finite group, the monoid
generated by an element contains its inverse as a positive power. Hence
repeated forward multiplication by the powered generators reaches the whole
subgroup. Redundant generators only add duplicate edges and do not affect
correctness.

### Deterministic lookup, storage, and bit complexity

Use a deterministic balanced search tree keyed by the canonical residue in
\(\{0,\ldots,N-1\}\). It gives polynomial lookup time without a randomized
hashing assumption. At most \(S+1\) residues are stored for any exponent,
using \(O(S\log N)\) bits, apart from polynomial queue and tree overhead.

Let \(n=\lceil\log_2N\rceil\). For a scanned prime,

\[
v_\ell(N-1)\leq\log_2(N-1)<n.
\]

There are at most \(L\) candidate integers through \(L\), so the number of
scanned exponents is \(O(Ln)\). Every exponent \(E\) is at most \(N-1\) and
has \(O(n)\) bits. Modular powering is therefore polynomial in \(n\) and
the generator encoding length.

Each capped breadth-first search uses \(O(sS)\) modular multiplications,
\(O(S)\) gcds, and deterministic dictionary operations polynomial in
\(n+\log S\). If the numerical values \(L,S\), the generator count \(s\),
and all generator encoding lengths are polynomial in \(n\), the entire
algorithm has uniform deterministic polynomial bit complexity.

The executable procedure never uses \(p,q,h,c\), any hidden valuation, a
successful-prime selector, a branch detector, or a precomputed cancellation
word. Those quantities occur only in the conditional proof that one of the
publicly enumerated cases succeeds.

## 5. The fixed \(N=2047\) specialization

First,

\[
2047=23\cdot89.
\]

The factors are prime: \(23\) has no prime divisor at most
\(\sqrt{23}<5\), and \(89\) has no prime divisor among \(2,3,5,7\), the
primes below \(\sqrt{89}<10\).

Modulo \(23\),

\[
11^2\equiv6,\quad
11^4\equiv13,\quad
11^5\equiv5,\quad
11^{10}\equiv2,\quad
11^{11}\equiv-1.
\]

Modulo \(89\),

\[
11^2\equiv32,\quad
11^4\equiv45,\quad
11^5\equiv50,\quad
11^{10}\equiv8,\quad
11^{11}\equiv-1.
\]

Thus \(11^{22}=1\) in both fields. Its order is not \(1\), \(2\), or \(11\),
so it is exactly \(22\) at both primes. Also,

\[
2^{11}=2048=1+2047.
\]

The local order of \(2\) divides the prime \(11\) and is not one, so it is
exactly \(11\) at both primes. Finally, if \(2=11^k\) modulo \(N\), the
modulo-\(23\) table and the order \(22\) force
\(k\equiv10\pmod{22}\). The modulo-\(89\) table would then give
\(2\equiv11^{10}\equiv8\pmod{89}\), a contradiction. Hence
\(2\notin H\).

The element \(11\) therefore has order \(22\) modulo both primes, so
\(|H|=h=22\) and \(H\) is a graph. The element \(2\) has order \(11\)
modulo both primes and is not in \(H\). Modulo \(23\), \(H_p\) already has
the full order \(22\). Modulo \(89\), the cyclic group \(H_q\) has order
\(22\) and contains the unique subgroup of order \(11\), so it contains
\(2\). Thus \(K\) is a strict pure-phase extension.

The coset \(2H\) has order dividing \(11\) and is nontrivial, hence

\[
c=[K:H]=11.
\]

Now

\[
N-1=2046=2\cdot3\cdot11\cdot31.
\]

For \(\ell=11\),

\[
e=H_{11}=C_{11}=1,\qquad
j=e-C_{11}+1=1.
\]

Therefore

\[
\boxed{E=(N-1)/11=2046/11=186}.
\]

The formulas give

\[
h_E=11^{1-1+1}=11,\qquad
c_E=11,
\]

and hence

\[
\boxed{|K^E|=11\cdot11=121}.
\]

The exact positive-separator count is

\[
\boxed{2\cdot11-2=20}.
\]

## 6. Scope

This is a conditional deterministic decoder for a supplied strict
pure-phase state. It does not create such a state, prove that feedback
produces a phase prime \(\ell\leq L\), or prove that the residual image fits
the public cap \(S\).

The required polynomial promise is

\[
\ell^{H_\ell-C_\ell+2}\leq S,
\]

the full powered-subgroup size. A small raw gap \(H_\ell-C_\ell\) alone is
not enough when \(\ell\) itself is large.

The proof does not cover feedback extensions that enlarge one or both local
projection images, general mixtures of order growth and phase growth,
arbitrary composite moduli, or all inputs. It therefore gives neither an
all-input phase source nor a general factoring algorithm.
