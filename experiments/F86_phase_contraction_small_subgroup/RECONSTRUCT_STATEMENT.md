# F86 proof-blind reconstruction statement

Reconstruct or refute the claims below without reading the F86 candidate,
audit, later F86 artifacts, or later durable-state entries.

Let \(N=pq\) for distinct odd primes. Let \(H\) be a diagonal graph subgroup
of order \(h\):

\[
H=\{(x,\varphi(x)):x\in H_p\}
\]

for an isomorphism \(\varphi:H_p\to H_q\). Let \(K\ge H\) be a strict pure
phase extension:

\[
K_p=H_p,
\qquad
K_q=H_q,
\qquad
K\ne H.
\]

Put \(c=[K:H]\). Prove or refute that \(K/H\) is cyclic, \(c\mid h\), and
there is a cyclic \(D\le H_q\) of order \(c\) such that

\[
K=H\cdot(\{1\}\times D)
\]

with trivial intersection.

For \(M\ge1\), put

\[
h_M=\frac h{\gcd(h,M)},
\qquad
c_M=\frac c{\gcd(c,M)}.
\]

Prove or refute:

\[
K^M=H^M\cdot(\{1\}\times D^M),
\qquad
|K^M|=h_Mc_M.
\]

The local images must both have order \(h_M\). When \(c_M>1\), check that
the exact positive-separator count and density are

\[
2c_M-2,
\qquad
\frac{2(c_M-1)}{c_Mh_M}.
\]

Note that the extension can become trivial when \(c_M=1\).

For

\[
\sigma(a)=\max_{\ell^e\mid a}\ell^e,
\qquad
M_B=\operatorname{lcm}(1,\ldots,B),
\]

define the punctured bank

\[
\mathcal E_B
=
\{M_B\}
\cup
\left\{
M_B/\ell^j:
\ell\le B\text{ prime},\
1\le j\le\lfloor\log_\ell B\rfloor
\right\}.
\]

Assume \(K\ne H\) and \(\sigma(h)\le B\). Prove or refute that some bank
exponent \(E\) and prime \(\ell\mid c\) satisfy

\[
c_E=\ell,
\qquad
h_E\le B,
\qquad
|K^E|\le B^2,
\]

and that \(K^E\) contains exactly \(2\ell-2\) positive separators with
density at least \(1/B\). Verify the proposed choice: if

\[
H_\ell=v_\ell(h),
\quad
C_\ell=v_\ell(c),
\quad
e=v_\ell(M_B),
\]

then

\[
E=M_B/\ell^{e-C_\ell+1}.
\]

Prove or refute the public deterministic algorithm. For every bank exponent,
power all public generators of \(K\), enumerate their subgroup by breadth-
first multiplication, stop after more than \(B^2\) distinct residues, and
gcd-test every residue minus one. Check completeness, wrong-exponent caps,
redundant generators, \(\ell=2\), prime-power valuations, \(h=1\), storage,
and uniform bit complexity for \(B=\operatorname{poly}(\log N)\).

Finally verify the fixed specialization

\[
N=2047,
\qquad
H=\langle11\rangle,
\qquad
K=\langle11,2\rangle,
\]

with

\[
h=22,
\qquad
c=11,
\qquad
B=11,
\qquad
E=M_{11}/11=2520.
\]

Check \(h_E=c_E=11\), \(|K^E|=121\), and the count of 20 positive
separators.

State the scope: this is a deterministic post-feedback factorer only for a
pure phase extension whose old graph order has bounded full prime-power
components. It gives no all-input phase source, smoothness law, or factoring
algorithm.
