# F87 proof-blind reconstruction statement

Reconstruct or refute the claims below without reading the F87 candidate,
audit, later F87 artifacts, or later durable-state entries.

Let \(N=pq\) for distinct odd primes. Let

\[
K\le(\mathbb Z/N\mathbb Z)^\times
\]

be given by a public polynomial-size generator list, and put

\[
\lambda=\exp(K).
\]

Assume \(K\) contains a positive separator: an element with exactly one CRT
coordinate equal to one. For

\[
\sigma(a)=\max_{\ell^e\mid a}\ell^e,
\qquad
M_B=\operatorname{lcm}(1,\ldots,B),
\]

define

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

Prove or refute the following theorem. If

\[
\sigma(\lambda)\le B,
\]

then some \(E\in\mathcal E_B\) satisfies

\[
|K^E|\le B^2
\]

and \(K^E\) still contains a positive separator.

Verify the proposed witness exponent. Choose a separator \(x\), a prime
\(\ell\mid\operatorname{ord}(x)\), and put

\[
C=v_\ell(\operatorname{ord}(x)),
\qquad
H=v_\ell(\lambda),
\qquad
e=v_\ell(M_B).
\]

Then take

\[
E=M_B/\ell^{e-C+1}.
\]

Prove or refute that \(x^E\) is a positive separator of exact order
\(\ell\), that \(K^E\) is an \(\ell\)-group of exponent at most
\(\ell^{H-C+1}\le B\), and that the two-field CRT bounds its order by
\(B^2\). Check noncyclic \(K\), mixed-order separators, \(C<H\),
\(\ell=2\), \(B=1\), and redundant generators.

Prove or refute the public deterministic algorithm. For every bank exponent,
power all public generators, enumerate their subgroup by breadth-first
multiplication, stop after more than \(B^2\) distinct residues, and gcd-test
each residue minus one. Check completeness, wrong-exponent caps, inverse-free
enumeration, deterministic lookup, storage, and uniform bit complexity for
\(B=\operatorname{poly}(\log N)\). The executable algorithm must not use
\(\lambda\), an element order, hidden factors, or local projections.

Verify the fixed specialization

\[
N=2047,
\qquad
K=\langle11,2\rangle,
\qquad
\lambda=22,
\qquad
B=11,
\qquad
E=2520,
\]

where \(|K^E|=121\) and the image contains 20 positive separators.

State the scope. This is a deterministic decoder under the unverified
promises that a supplied subgroup already contains a separator and that
\(\sigma(\exp K)\le B\). It does not create the subgroup, prove the promise,
handle arbitrary many CRT components, or give an all-input factoring
algorithm. The smooth-exponent condition is sufficient for this bank, not
necessary for all possible decoders.
