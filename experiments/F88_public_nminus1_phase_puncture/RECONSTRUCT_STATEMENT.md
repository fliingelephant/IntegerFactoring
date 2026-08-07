# F88 proof-blind reconstruction statement

Reconstruct or refute the claims below without reading the F88 candidate,
audit, later F88 artifacts, or later durable-state entries.

Let \(N=pq\) for distinct odd primes. Let \(H\) be a diagonal graph subgroup
of \((\mathbb Z/N\mathbb Z)^\times\), with order \(h\). Let \(K\ge H\) be a
strict pure-phase extension:

\[
K_p=H_p,
\qquad
K_q=H_q,
\qquad
c=[K:H]>1.
\]

Public generators for \(K\) are supplied. Prove or refute that \(c\mid h\)
and

\[
\boxed{h\mid N-1.}
\]

Choose a prime \(\ell\mid c\), and write

\[
e=v_\ell(N-1),
\qquad
H_\ell=v_\ell(h),
\qquad
C_\ell=v_\ell(c).
\]

For

\[
j=e-C_\ell+1,
\qquad
E=(N-1)/\ell^j,
\]

prove or refute that

\[
c_E=\ell,
\qquad
h_E=\ell^{H_\ell-C_\ell+1},
\qquad
|K^E|=\ell^{H_\ell-C_\ell+2}.
\]

Here \(h_E=|H^E|\) and \(c_E=[K^E:H^E]\). Prove or refute that \(K^E\)
contains exactly \(2\ell-2\) positive separators and has separator density

\[
\frac{2(\ell-1)}{\ell^{H_\ell-C_\ell+2}}.
\]

Check excess public valuation \(e>H_\ell\), the case
\(C_\ell<H_\ell\), \(\ell=2\), and unscanned large prime components of
\(h\).

Prove or refute the public deterministic algorithm. For public bounds
\(L,S\), enumerate each prime \(\ell\le L\) dividing \(N-1\), every
\(1\le j\le v_\ell(N-1)\), and the exponent
\(E=(N-1)/\ell^j\). Power all public generators of \(K\), enumerate the
powered subgroup by breadth-first multiplication, stop after more than
\(S\) distinct residues, and gcd-test each residue minus one. Prove or
refute that the algorithm succeeds when some \(\ell\mid c\) satisfies

\[
\ell\le L,
\qquad
\ell^{H_\ell-C_\ell+2}\le S.
\]

Check completeness, wrong-exponent caps, inverse-free enumeration,
deterministic lookup, storage, and uniform bit complexity when \(L,S\), the
generator count, and generator encodings are polynomial in \(\log N\). The
executable algorithm must not use \(p,q,h,c\), hidden valuations, a branch
selector, or a cancellation word.

Verify the fixed specialization

\[
N=2047,
\qquad
H=\langle11\rangle,
\qquad
K=\langle11,2\rangle,
\qquad
h=22,
\qquad
c=11.
\]

For \(\ell=11\), verify that \(E=(N-1)/11=186\), that
\(|K^E|=121\), and that the image contains 20 positive separators.

State the exact scope. This is a conditional deterministic decoder for a
supplied strict pure-phase state. It does not create that state, prove that
feedback supplies a scanned phase prime or a polynomial residual image,
handle general order/phase mixtures or arbitrary composites, or give an
all-input factoring algorithm. The polynomial promise concerns the full
residual size \(\ell^{H_\ell-C_\ell+2}\), not only the raw valuation gap.
