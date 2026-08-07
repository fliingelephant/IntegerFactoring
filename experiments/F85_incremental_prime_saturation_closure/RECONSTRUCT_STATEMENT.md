# F85 proof-blind reconstruction statement

Reconstruct or refute the claims below without reading the F85 candidate,
audit, later F85 artifacts, or later durable-state entries.

Let \(N=pq\) for distinct odd primes. Let \(q_1,\ldots,q_s\) be
pairwise-coprime positive units, and let

\[
A_i=\prod_jq_j^{e_{ji}}\equiv1\pmod N,
\qquad
1\le i\le m,
\]

be a fixed full integer relation presentation with nonnegative exponents and
matrix \(E\). Fix a public prime \(\ell\), and put

\[
V=\ker(E\bmod\ell).
\]

Append one relation

\[
A_*=\prod_jq_j^{b_j}\equiv1\pmod N
\]

with nonnegative exponents, after complete joint gcd-free refinement. Work in
the final refined coordinates and write the new matrix as \([E\mid b]\).

Prove or refute that row splitting preserves the old kernel and that:

- if \(b\notin\operatorname{colspan}(E)\), then
  \(\ker[E\mid b]=V\times\{0\}\);
- if \(Ec+b=0\) and \(z=(c,1)\), then

  \[
  \ker[E\mid b]=(V\times\{0\})\oplus\langle z\rangle.
  \]

For \(x\in V\), define the exact old root residue

\[
R(x)=
\left[
\prod_jq_j^{(\sum_i e_{ji}x_i)/\ell}
\right]_N
\]

using canonical coordinate representatives, and put \(H=R(V)\). In the
closing case define

\[
s_c=
\left[
\prod_jq_j^{(\sum_i e_{ji}c_i+b_j)/\ell}
\right]_N.
\]

Prove or refute:

1. all displayed exponents are nonnegative integers;
2. the old and new root maps are homomorphisms despite coordinate carries;
3. the full new root image is \(H'=\langle H,s_c\rangle\);
4. a different solution \(c'\) gives the same coset \(s_{c'}H=s_cH\).

State precisely that this coset is canonical relative to the fixed block
list and full integer exponent presentation, not to the reduced matrix alone.

Assume the complete old prime-saturation decoder has run and found no factor.
Let \(b_1,\ldots,b_D\) be a public basis of \(V\).

Prove or refute the complete incremental decoder:

- If every basis root equals 1 modulo \(N\), then \(H=1\), and the single
  test \(\gcd(s_c-1,N)\) is complete for all new roots.
- Otherwise choose any basis root \(h\ne1\). Then \(H=\langle h\rangle\),
  and the public coset scan

  \[
  \{s_ch^t:0\le t<\ell\}
  \]

  contains a proper-gcd root if and only if the full new image does. If
  \(s_c\notin H\), exactly two scan elements are separators; if
  \(s_c\in H\), none is.

Check every zero-functional, proportional-functional, \(V=0\),
\(\ell=2\), and \(\ell=p\) or \(q\) case. State why a public
\(\ell=p\) or \(q\) is already caught by \(\gcd(\ell,N)\).

Check public executability and deterministic polynomial bit complexity when
the numerical value of \(\ell\) is polynomial in the full presentation
length plus \(\log N\). The algorithm must not use the hidden factors,
local characters, or a hidden membership test.

State the scope: this is a complete incremental decoder after one
prime-saturation closure. It does not make the new column close, make the new
root coset leave the old graph, or choose a useful prime on every input.
