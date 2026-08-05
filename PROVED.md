# Promoted Results

Only verifier-backed results may be promoted here. Each result must include its exact status label and its proof or certificate.

## P01 — no rank reduction by universally sound linear square-class sketches

**Status:** promoted.

**Verification record:** initial proof, focused hostile audit, and proof-blind end-to-end reconstruction all completed. No cross-family audit has run.

**Statement.** Let \(a_1,\ldots,a_m\) be positive integers with classes \(v_i=[a_i]\) in the \(\mathbb F_2\)-vector space \(\mathbb Q^\times/(\mathbb Q^\times)^2\). Let a homogeneous linear sketch choose \(e_i\in\mathbb F_2^d\). Suppose it is universally sound in the exact sense that

\[
\sum_i c_i e_i=0
\quad\Longrightarrow\quad
\prod_i a_i^{c_i}\text{ is an integer square}
\]

for every \(c\in\mathbb F_2^m\). Then

\[
\operatorname{rank}(e_1,\ldots,e_m)
\ge
\operatorname{rank}(v_1,\ldots,v_m).
\]

In particular, if the \(a_i\) are distinct primes, then \(d\ge m\) and the sketch has no nonzero dependence.

**Proof.** Define \(E(c)=\sum_i c_i e_i\) and \(V(c)=\sum_i c_i v_i\). Positivity and unique factorization imply that \(V(c)=0\) exactly when \(\prod_i a_i^{c_i}\) is an integer square. Universal soundness is therefore \(\ker E\subseteq\ker V\). The map \(V\) factors through \(E\): define \(L(E(c))=V(c)\), which is well-defined by the kernel inclusion. Hence \(V=L\circ E\) and \(\operatorname{rank}V\le\operatorname{rank}E\). For distinct primes \(a_i=p_i\), taking the \(p_j\)-adic valuation modulo 2 in a relation shows each coefficient \(c_j=0\); thus \(\operatorname{rank}V=m\), forcing \(\operatorname{rank}E=m\), \(d\ge m\), and \(\ker E=0\). \(\square\)

**Scope.** This does not address lossy sketches followed by exact verification, randomized rejection, nonlinear or adaptive encodings, or special generators whose true square-class span is structurally small.

## P02 — factoring from a root of a hidden random unit square

**Status:** promoted.

**Verification record:** initial proof, focused hostile audit, and proof-blind end-to-end reconstruction all completed. No cross-family audit has run.

**Statement.** Let

\[
N=\prod_{j=1}^r p_j^{\alpha_j}
\]

be odd, with distinct primes \(p_j\). Choose hidden \(X\) uniformly in \((\mathbb Z/N\mathbb Z)^\times\), set \(A=X^2\), and give only \((N,A)\) to a routine whose private randomness is independent of \(X\). Conditional on the routine returning any valid root \(Y^2=A\),

\[
\Pr\bigl(1<\gcd(X-Y,N)<N\bigr)=1-2^{1-r}.
\]

Thus the probability is exactly \(1/2\) for a product of two distinct odd prime powers, at least \(1/2\) whenever \(r\ge2\), and zero for an odd prime power.

**Proof.** A unit square modulo an odd prime power has exactly two roots, since \(u^2=1\pmod {p^\alpha}\) implies \(p^\alpha\) divides one of the coprime-up-to-2 factors \(u-1,u+1\), hence \(u=\pm1\). CRT gives exactly \(2^r\) roots of \(A\), indexed by independent signs on the prime-power components. Conditional on \(A\) and on any returned \(Y\), the hidden \(X\) remains uniform among these roots because the routine sees no information about \(X\) beyond \(A\). If \(S\) is the set of components on which \(X=Y\), then

\[
\gcd(X-Y,N)=\prod_{j\in S}p_j^{\alpha_j};
\]

on every other component \(X-Y=-2Y\) is a unit. The gcd is proper and nontrivial for all sign subsets except the empty and full subsets. Exactly \(2^r-2\) of the \(2^r\) equiprobable choices succeed. \(\square\)

**Scope.** The unit, odd-modulus, root-validity, and hidden-root independence conditions are essential. This is a reduction, not a construction of an efficient square-root routine.
