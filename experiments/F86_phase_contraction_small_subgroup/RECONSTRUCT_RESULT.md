# PASS

The SHA-256 of RECONSTRUCT_STATEMENT.md is
e864530fbf489c1af09aef0371fcb86857d9c502c8bca887c1767138d1c9af3c,
as required. All structural, counting, algorithmic, edge-case, and fixed
specialization claims are correct.

## 1. Structure of a pure phase extension

Because \(H_p\) is a subgroup of the cyclic group
\(\mathbb F_p^\times\), it is cyclic. The graph projection
\(H\to H_p\) is an isomorphism, so \(H\) is cyclic of order \(h\).

For \((x,y)\in K\), define

\[
\psi(x,y)=y\varphi(x)^{-1}.
\]

This is well-defined because \(K_p=H_p\), \(K_q=H_q\), and
\(\varphi:H_p\to H_q\). It is a homomorphism from \(K\) to \(H_q\).
Its kernel is exactly the graph \(H\):

\[
\psi(x,y)=1\iff y=\varphi(x)\iff(x,y)\in H.
\]

Let

\[
D=\psi(K)\leq H_q.
\]

The first isomorphism theorem gives

\[
K/H\simeq D.
\]

The group \(H_q\) is cyclic of order \(h\), so \(D\) is cyclic and

\[
|D|=|K/H|=c,\qquad c\mid h.
\]

There is also an internal realization of \(D\). If
\(\psi(x,y)=d\), then

\[
(x,y)(x,\varphi(x))^{-1}=(1,d)\in K.
\]

Thus \(\{1\}\times D\leq K\). Every \((x,y)\in K\) factors as

\[
(x,y)=(x,\varphi(x))(1,y\varphi(x)^{-1}),
\]

with the first factor in \(H\) and the second in \(\{1\}\times D\).
Their intersection is trivial, because the only graph element with first
coordinate \(1\) is \((1,1)\). Therefore

\[
\boxed{K=H\cdot(\{1\}\times D)}
\]

is an internal direct product, and \(K/H\) is cyclic of order \(c\).

## 2. Power contraction and separator density

Put \(D_0=\{1\}\times D\). Since \(K=H\times D_0\) internally and the
ambient group is abelian,

\[
(hd)^M=h^Md^M
\]

for \(h\in H,d\in D_0\). Conversely, every product \(h^Md^M\) is the
\(M\)-th power of \(hd\). Hence

\[
\boxed{K^M=H^M\cdot(\{1\}\times D^M)}.
\]

The intersection remains trivial. For a cyclic group of order \(r\), the
image of the \(M\)-th power map has order \(r/\gcd(r,M)\). Consequently,

\[
|H^M|=h_M,\qquad |D^M|=c_M,
\]

and

\[
\boxed{|K^M|=h_Mc_M}.
\]

Projection commutes with powering. Since \(K_p=H_p\) and \(K_q=H_q\), both
local images of \(K^M\) have order

\[
\frac h{\gcd(h,M)}=h_M.
\]

The subgroup \(H^M\) remains the graph of the restriction of \(\varphi\) to
\(H_p^M\), and it has order \(h_M\). Thus \(K^M/H^M\) has index \(c_M\),
while neither local image grows beyond that of \(H^M\).

The kernel of either projection from \(K^M\) has size

\[
\frac{|K^M|}{h_M}=c_M.
\]

The two kernels intersect only at the global identity. Positive separators
are their symmetric difference, so their exact count is

\[
\boxed{2c_M-2}.
\]

For \(c_M>1\), their exact density in \(K^M\) is

\[
\boxed{\frac{2c_M-2}{h_Mc_M}
=\frac{2(c_M-1)}{c_Mh_M}}.
\]

If \(c_M=1\), then \(D^M=1\) and \(K^M=H^M\). The phase extension has become
trivial and the separator count is zero.

## 3. What the smoothness hypothesis implies

Interpret

\[
\sigma(h)=\max_{\ell\mid h}\ell^{v_\ell(h)}
\]

as the largest full prime-power component of \(h\). The assumption
\(\sigma(h)\leq B\) means

\[
\ell^{v_\ell(h)}\leq B
\]

for every prime divisor \(\ell\) of \(h\). Therefore every such prime is at
most \(B\), and

\[
v_\ell(h)\leq\lfloor\log_\ell B\rfloor
=v_\ell(M_B).
\]

It follows that

\[
h\mid M_B.
\]

Since \(K\ne H\), one has \(c>1\). Choose any prime \(\ell\mid c\), and put

\[
H_\ell=v_\ell(h),\qquad
C_\ell=v_\ell(c),\qquad
e=v_\ell(M_B).
\]

The divisibility \(c\mid h\mid M_B\) gives

\[
1\leq C_\ell\leq H_\ell\leq e.
\]

Define

\[
j=e-C_\ell+1.
\]

Then \(1\leq j\leq e=\lfloor\log_\ell B\rfloor\), so

\[
E=M_B/\ell^j
=M_B/\ell^{e-C_\ell+1}
\]

is an element of the punctured bank \(\mathcal E_B\).

Its \(\ell\)-adic valuation is

\[
v_\ell(E)=C_\ell-1.
\]

For every other prime \(r\), the exponent \(E\) retains the full valuation
of \(M_B\), which is at least \(v_r(h)\) and hence at least \(v_r(c)\).
Therefore

\[
v_\ell(c_E)=1,\qquad v_r(c_E)=0\quad(r\ne\ell),
\]

and

\[
\boxed{c_E=\ell}.
\]

Similarly, every prime other than \(\ell\) is removed from \(h_E\), while

\[
v_\ell(h_E)
=H_\ell-(C_\ell-1)
=H_\ell-C_\ell+1.
\]

Thus

\[
\boxed{h_E=\ell^{H_\ell-C_\ell+1}}
\]

and

\[
h_E\leq\ell^{H_\ell}\leq B.
\]

It follows that

\[
\boxed{|K^E|=h_Ec_E=h_E\ell\leq B^2},
\]

because \(\ell\leq B\).

The separator count for this exponent is exactly

\[
\boxed{2\ell-2}.
\]

Its density is

\[
\frac{2(\ell-1)}{\ell h_E}.
\]

For every prime \(\ell\geq2\),

\[
\frac{2(\ell-1)}{\ell}\geq1.
\]

Since \(h_E\leq B\), the density satisfies

\[
\boxed{\frac{2(\ell-1)}{\ell h_E}\geq\frac1{h_E}\geq\frac1B}.
\]

This includes \(\ell=2\), where the first inequality is an equality and the
exact separator count is two.

## 4. Public deterministic algorithm

Let \(g_1,\ldots,g_s\) be the public generators of \(K\). Construct \(M_B\)
and the finite bank \(\mathcal E_B\). For every \(E\in\mathcal E_B\):

1. Compute \(g_i^E\bmod N\) for every \(i\).
2. Starting from \(1\), enumerate the multiplicative closure of these
   powered generators by breadth-first search.
3. Keep a set of canonical residues already seen. Test
   \(\gcd(y-1,N)\) for every newly discovered residue \(y\).
4. Return any gcd strictly between \(1\) and \(N\).
5. Abandon this exponent as soon as more than \(B^2\) distinct residues
   have been discovered.

### Completeness

Powering is a homomorphism because the unit group is abelian. Hence

\[
K^E=\langle g_1^E,\ldots,g_s^E\rangle.
\]

Repeated multiplication by the powered generators reaches their entire
finite subgroup. In a finite group, the monoid generated by group elements
already contains their inverses through positive powers, so explicit inverse
edges are not required.

Section 3 proves that at least one bank exponent \(E\) has
\(|K^E|\leq B^2\) and contains \(2\ell-2>0\) positive separators. For that
exponent, the cap never fires: the breadth-first queue empties only after
all of \(K^E\) has been enumerated. Testing every residue therefore finds a
proper factor.

### Wrong exponents and redundant generators

If a wrong exponent produces more than \(B^2\) elements, breadth-first
search discovers a \((B^2+1)\)-st residue and stops. At most \(B^2+1\)
residues are stored. Each discovered residue is processed once, with at most
\(s\) outgoing multiplications. If a wrong exponent produces at most
\(B^2\) elements, it is fully enumerated within the same cap. Redundant
generators add duplicate edges but cannot change the generated subgroup or
completeness.

### Prime-power valuations and \(\ell=2\)

The bank includes every puncture

\[
M_B/\ell^j,\qquad1\leq j\leq v_\ell(M_B).
\]

Thus it includes the exact depth \(j=e-C_\ell+1\), even when \(c\) contains
a high power of \(\ell\). The proof does not assume that \(c\) is squarefree.
For \(\ell=2\), the selected image has \(c_E=2\), exactly two positive
separators, and density \(1/h_E\geq1/B\). No parity exception occurs.

### The edge case \(h=1\)

The structural result gives \(c\mid h\). If \(h=1\), then \(c=1\), so no
strict pure phase extension \(K\ne H\) exists. The bank theorem's strict
extension premise is therefore empty in this case. One may set
\(\sigma(1)=1\) by convention, but no prime \(\ell\mid c\) must or can be
chosen.

### Storage and bit complexity

The elementary bound

\[
M_B\mid B!,\qquad
\log_2M_B\leq B\log_2B
\]

shows that every bank exponent has \(O(B\log B)\) bits. The bank contains at
most

\[
1+\sum_{\substack{\ell\leq B\\\ell\text{ prime}}}
\lfloor\log_\ell B\rfloor
\leq1+B\lfloor\log_2B\rfloor
\]

entries. It can be constructed deterministically by lcm updates and
elementary prime enumeration up to \(B\).

For each bank element, modular powering costs polynomial time in
\(B+\log N\) and the public generator count. The capped search performs
\(O(sB^2)\) modular multiplications and \(O(B^2)\) gcds, and stores
\(O(B^2)\) residues of \(O(\log N)\) bits. A deterministic dictionary or
balanced search tree gives polynomial membership-test cost.

If \(B=\operatorname{poly}(\log N)\), the number of bank elements, every
exponent bit length, every capped search, and the total storage are uniformly
polynomial in the public input length. The algorithm does not need \(h,c\),
their prime factorizations, the successful prime \(\ell\), or the successful
bank exponent.

## 5. The fixed \(N=2047\) specialization

Use

\[
N=2047=23\cdot89,\qquad
H=\langle11\rangle,\qquad
K=\langle11,2\rangle.
\]

The local order of \(11\) is \(22\) at both primes, so \(h=22\) and \(H\)
is a graph. The local order of \(2\) is \(11\) at both primes. Modulo \(23\),
\(H_p\) already has the full order \(22\). Modulo \(89\), the cyclic group
\(H_q\) has order \(22\) and contains the unique subgroup of order \(11\),
so it contains \(2\). Therefore

\[
K_p=H_p,\qquad K_q=H_q.
\]

Since \(2\notin H\), the extension is strict. The coset \(2H\) has order
dividing the global order \(11\) of \(2\), and it is nontrivial. Hence

\[
c=[K:H]=11.
\]

The lcm through \(11\) is

\[
M_{11}=2^3\cdot3^2\cdot5\cdot7\cdot11=27720,
\]

so

\[
E=M_{11}/11=2520.
\]

The exponent \(2520=2^3\cdot3^2\cdot5\cdot7\) is divisible by \(2\) but
not by \(11\). Consequently,

\[
h_E=\frac{22}{\gcd(22,2520)}
=\frac{22}{2}
=11
\]

and

\[
c_E=\frac{11}{\gcd(11,2520)}
=11.
\]

Thus

\[
\boxed{|K^E|=h_Ec_E=11\cdot11=121}.
\]

The exact positive-separator count is

\[
\boxed{2c_E-2=20}.
\]

Here \(B^2=11^2=121\), so the successful subgroup lies exactly at the
algorithm's enumeration cap and is still fully enumerated, because stopping
occurs only after more than \(B^2\) distinct residues.

## 6. Scope

This is a deterministic post-feedback factorer under two structural
promises: the feedback state is a strict pure phase extension, and every
full prime-power component of the old graph order is at most
\(B=\operatorname{poly}(\log N)\). The algorithm does not know the hidden
orders or indices, but its proof depends on those promises.

The result supplies no mechanism that creates a pure phase extension on
every input. It proves no all-input smoothness law for old graph orders, and
it does not extend to arbitrary feedback enlargements whose local projection
images also grow. Therefore it is not a general polynomial-time factoring
algorithm.
