# GCD-free square-relation decoder

## Result

The claim is true with the output-size-consistent meaning of part (iii): the algorithm outputs a polynomial-time evaluator for the exact positive root \(R(c)\) of every supplied kernel vector \(c\), and it evaluates that root for every vector in the tested kernel basis. It does not list all \(2^{\dim K}\) kernel vectors.

Let

\[
A(c)=\prod_{i=1}^m a_i^{c_i},\qquad
X(c)=\prod_{i=1}^m x_i^{c_i}\pmod N,
\]

for \(c\in\mathbb F_2^m\). The construction below produces:

1. pairwise-coprime nonsquare blocks \(b_1,\ldots,b_t>1\) and nonnegative integer coordinates \(e_{ji}\) such that
   \[
   a_i=\prod_{j=1}^t b_j^{e_{ji}};
   \]
2. the binary matrix \(M=(e_{ji}\bmod 2)\), whose kernel is exactly the set of \(c\) for which \(A(c)\) is an integer square;
3. for every \(c\in\ker M\), the exact formula
   \[
   R(c)=\prod_{j=1}^t b_j^{\frac12\sum_i e_{ji}c_i};
   \]
4. a factor test on an arbitrary basis of \(\ker M\) that is complete for all square subsets.

No prime factorization is used by the algorithm.

## Promised input and boundary checks

The theorem assumes that \(N\ge 3\) is odd, each \(a_i\ge 1\), and each supplied residue \(x_i\) is a unit modulo \(N\) with

\[
x_i^2\equiv a_i\pmod N.
\]

At a system boundary, the algorithm can check these promises. Reduce each \(x_i\) modulo \(N\), check the congruence, and compute \(d_i=\gcd(x_i,N)\). If \(1<d_i<N\), then \(d_i\) is already a proper divisor and the algorithm returns it. If \(d_i=N\), or if the congruence is false, the input is outside the promise and is rejected. On a promised input, every \(d_i\) is one.

The unit promise implies

\[
\gcd(a_i,N)=1
\]

for every \(i\). Consequently, whenever \(A(c)=R(c)^2\), both \(A(c)\) and \(R(c)\) are units modulo \(N\). This fact is essential for the normalized-root argument below.

## Step 1: deterministic GCD-free refinement

A record is a pair \((b,v)\), where \(b>1\) is an integer and \(v\in\mathbb Z_{\ge0}^m\). Maintain the invariant

\[
a_i=\prod_{(b,v)} b^{v_i}\qquad(1\le i\le m).
\]

Initialize one record \((a_i,\mathbf e_i)\) for every \(a_i>1\), where \(\mathbf e_i\) is the \(i\)-th unit vector. Omit \(a_i=1\). Coalesce records with equal bases by replacing \((b,v)\) and \((b,w)\) with \((b,v+w)\). Keep the records sorted by their bases.

While two records have a nontrivial gcd, choose the first such pair in the sorted order. Write the records as \((b,v)\) and \((c,w)\), and put

\[
d=\gcd(b,c)>1.
\]

Remove those two records and insert

\[
(d,v+w),
\]

together with \((b/d,v)\) if \(b/d>1\), and \((c/d,w)\) if \(c/d>1\). All divisions are exact. Coalesce equal bases and sort again.

This replacement preserves the invariant because, coordinate by coordinate,

\[
d^{v_i+w_i}(b/d)^{v_i}(c/d)^{w_i}=b^{v_i}c^{w_i}.
\]

When the loop stops, the bases are pairwise coprime.

### Termination

For the proof only, let \(\Omega(z)\) denote the number of prime factors of \(z\), counted with multiplicity. The algorithm does not compute \(\Omega\). Use the potential

\[
P=\sum_{(b,v)}\Omega(b).
\]

Before coalescing, one refinement replaces the contribution \(\Omega(b)+\Omega(c)\) by

\[
\Omega(d)+\Omega(b/d)+\Omega(c/d)
=\Omega(b)+\Omega(c)-\Omega(d).
\]

Thus every refinement decreases \(P\) by at least one. Coalescing equal bases decreases it further. Initially,

\[
P\le \sum_i\Omega(a_i)\le\sum_i\log_2 a_i.
\]

Therefore every choice rule terminates, and the specified first-pair rule makes the algorithm deterministic.

### Remove square block powers

A terminal GCD-free block can itself be a perfect square. Normalize every record independently as follows:

```text
while b is a perfect square:
    b = exact positive square root of b
    v = 2v
```

The invariant remains true. The new base divides the old base, so pairwise coprimality is preserved. Since \(b>1\) strictly decreases, this loop terminates. At the end, every block \(b_j\) is nonsquare. A block need not be prime or squarefree. For example, a lone block \(12\) can remain intact.

Let the final coordinate vector of \(b_j\) be the \(j\)-th row of an integer matrix \(E=(e_{ji})\).

## Step 2: the exact square kernel

Set

\[
M=E\bmod 2\in\mathbb F_2^{t\times m}.
\]

For \(c\in\mathbb F_2^m\), define the ordinary nonnegative integers

\[
s_j(c)=\sum_{i=1}^m e_{ji}c_i.
\]

The block representation gives

\[
A(c)=\prod_{j=1}^t b_j^{s_j(c)}.
\]

If \(Mc=0\), every \(s_j(c)\) is even, so \(A(c)\) is a square.

Conversely, suppose some \(s_j(c)\) is odd. Since \(b_j\) is nonsquare, some prime occurs to an odd exponent in \(b_j\). Pairwise coprimality means that prime occurs in no other block. Its exponent in \(A(c)\) is therefore odd. Hence \(A(c)\) is not a square. This proves

\[
\boxed{\ker M=\{c\in\mathbb F_2^m:A(c)\text{ is an integer square}\}.}
\]

The proof refers to prime valuations, but the algorithm does not compute them. Exact square tests on whole blocks are sufficient, including for composite nonsquare blocks.

Use binary Gaussian elimination to compute any basis

\[
v_1,\ldots,v_k
\]

of \(K=\ker M\).

## Step 3: exact roots

For any supplied \(c\in K\), compute all \(s_j(c)\) over the integers and return

\[
R(c)=\prod_{j=1}^t b_j^{s_j(c)/2}.
\]

Every exponent is an integer. Squaring the displayed expression gives \(A(c)\), so it is the unique positive integer square root. This avoids floating-point square roots and does not factor any block.

The factoring loop evaluates this formula for each basis vector \(v_\ell\). The same formula is a polynomial-time exact-root evaluator for every other kernel vector.

## Step 4: basis-only factor test

For each basis vector \(v_\ell\):

1. Compute the exact integer \(R=R(v_\ell)\).
2. Compute \(X=X(v_\ell)\) by modular multiplication.
3. Let \(r=R\bmod N\), and compute
   \[
   g_- = \gcd(N,X-r),\qquad g_+ = \gcd(N,X+r).
   \]
4. Return either gcd that lies strictly between \(1\) and \(N\).

If no basis vector yields a proper gcd, return “no nontrivial square congruence occurs among these subset relations.” This is not a primality statement.

For every \(c\in K\),

\[
X(c)^2\equiv \prod_i a_i^{c_i}=A(c)=R(c)^2\pmod N.
\]

The next two lemmas prove both the factor extraction and the completeness of testing only a basis.

## Factor lemma for odd, possibly nonsquarefree \(N\)

Let \(x,r\) be units modulo odd \(N\) with \(x^2\equiv r^2\pmod N\). If \(x\not\equiv r\pmod N\) and \(x\not\equiv-r\pmod N\), then

\[
1<\gcd(N,x-r)<N,
\qquad
1<\gcd(N,x+r)<N.
\]

To prove this, consider any prime power \(p^e\) dividing \(N\). This is only a proof device. Since \(p\) is odd and \(x,r\) are units, \(p\) cannot divide both \(x-r\) and \(x+r\): otherwise it would divide both \(2x\) and \(2r\). But

\[
p^e\mid(x-r)(x+r).
\]

Therefore the full power \(p^e\) divides exactly one of the two factors. The two gcds collect complementary full prime-power divisors of \(N\), so their product is \(N\). Neither gcd is \(N\), by the two assumed noncongruences. Hence neither can be one.

This argument does not require \(N\) to be squarefree. If \(N\) is a power of one odd prime, a nontrivial mismatch cannot occur: every square root of one among the units is \(\pm1\). For a general odd \(N\), a mismatch means that different prime-power components use different signs, and the two gcds separate those components without first finding them.

## The normalized-root homomorphism

For \(c\in K\), define

\[
\eta(c)=X(c)R(c)^{-1}\pmod N.
\]

The inverse exists because \(R(c)\) is a unit. Also \(\eta(c)^2=1\), so \(\eta\) takes values in the group

\[
T_N=\{u\in(\mathbb Z/N\mathbb Z)^\times:u^2=1\}.
\]

The important fact is that \(\eta\) is a homomorphism from the additive binary space \(K\) to \(T_N\).

Let \(c,d\in K\), let \(c\oplus d\) denote coordinatewise XOR, and put

\[
J(c,d)=\prod_{i:c_i=d_i=1}a_i.
\]

There are exact integer and modular identities

\[
A(c)A(d)=A(c\oplus d)J(c,d)^2
\]

and

\[
X(c)X(d)\equiv X(c\oplus d)J(c,d)\pmod N.
\]

The first identity, together with positivity of all roots, gives

\[
R(c)R(d)=R(c\oplus d)J(c,d).
\]

Dividing the modular identity by this exact root identity yields

\[
\eta(c)\eta(d)=\eta(c\oplus d).
\]

This is why the positive-root normalization matters. The unnormalized map \(c\mapsto R(c)\) is not itself multiplicative under XOR; the intersection factor \(J(c,d)\) is exactly what cancels in \(X(c)/R(c)\).

Since \(N\) is odd, \(S=\{1,-1\}\) is a subgroup of \(T_N\). Moreover,

\[
R(c)\equiv\pm X(c)\pmod N
\quad\Longleftrightarrow\quad
\eta(c)\in S.
\]

Suppose some \(c\in K\) has \(\eta(c)\notin S\). Write \(c\) in an arbitrary basis as

\[
c=\lambda_1v_1\oplus\cdots\oplus\lambda_kv_k.
\]

If every \(\eta(v_\ell)\) belonged to \(S\), the homomorphism law would put \(\eta(c)\) in \(S\), a contradiction. Therefore at least one vector in every basis has

\[
R(v_\ell)\not\equiv\pm X(v_\ell)\pmod N.
\]

The factor lemma then returns a proper divisor. Conversely, if every tested basis vector has normalized root \(\pm1\), every vector in the kernel does. Thus an arbitrary basis is complete; enumeration of all square subsets is unnecessary.

## Polynomial bounds

Put

\[
B=\sum_i\left\lceil\log_2(a_i+1)\right\rceil,
\]

so \(B\le L\) and \(m\le L\).

The refinement loop has at most \(B\) iterations by the potential argument. It starts with at most \(m\) records, and one refinement increases the record count by at most one. Hence

\[
t\le m+B\le 2L.
\]

Every block is a divisor of a previously present block, so its bit length is at most the largest input bit length. From the representation invariant and \(b_j\ge2\),

\[
\sum_j e_{ji}\le\log_2 a_i.
\]

Thus every coordinate has \(O(\log L)\) bits. Repeated square normalization preserves this bound because it preserves the represented integers.

A naive scan of all record pairs at each refinement already uses only polynomially many gcd operations on \(O(L)\)-bit integers. Exact square testing, exact division, sorting, and coordinate arithmetic are polynomial as well. The matrix has at most \(2L\) rows and \(m\le L\) columns, so binary elimination is polynomial.

For a subset \(c\),

\[
\log_2 A(c)\le\sum_i\log_2 a_i\le B,
\]

and \(R(c)\) has at most \(O(L)\) bits. Exact powering and multiplication therefore remain polynomial. There are at most \(m\) basis vectors. Their modular products and gcds use \(O(n)\)-bit residues. Although the supplied \(x_i\) occupy up to \(mn\) bits, \(mn\le(L+n)^2\). The full running time and output size are polynomial in \(L+n\).

## Multiset and degenerate cases

- **The zero kernel vector.** The vector \(0\) is always in \(K\), with \(A(0)=R(0)=X(0)=1\). It is never a basis vector and never yields a factor. If \(m=0\), the basis is empty and the algorithm returns no factor.

- **An integer zero.** The stated input has positive \(a_i\). An input \(a_i=0\), or even \(a_i\equiv0\pmod N\), cannot have a unit modular square root. It is outside the promise. No zero block is created by the refinement.

- **The value one.** A value \(a_i=1\) contributes no block, so column \(i\) of \(M\) is zero. It must still remain as a separate source coordinate because its supplied \(x_i\) can be any element of \(T_N\), not necessarily a global sign. The vector selecting that source has exact root one and can itself reveal a factor.

- **Duplicates.** Equal integer bases are coalesced only inside the block representation. Source indices are never coalesced. If \(a_i=a_h\), their matrix columns can coincide, but \(x_i\) and \(x_h\) can be different modular roots. The relation selecting both copies can contain the entire factoring signal.

- **Integer squares.** Repeated exact square normalization transfers powers of two from a square block into its coordinate row. Thus an integer-square source has a zero column in \(M\), as it must, while the exact-root formula still returns its actual positive square root.

- **Composite nonsquare blocks.** Such blocks do not need further splitting. A nonsquare block has at least one odd prime valuation. Pairwise coprimality isolates that valuation from all other blocks, which is exactly enough for the kernel proof.

- **Nonunit supplied roots.** They are not covered by the normalized-root theorem. A proper \(\gcd(x_i,N)\) is already a factor; \(\gcd(x_i,N)=N\) is only a promise failure. On promised inputs, products \(X(c)\) and roots \(R(c)\) stay units. The possibly nonunit quantities \(X(c)-R(c)\) and \(X(c)+R(c)\) are the intended gcd witnesses.

## What the decoder does not imply

Binary row reduction may delete dependent equations of \(M\) without changing its kernel. That is constraint compression. It does not justify deleting source columns merely because the corresponding integer square classes are dependent. The modular roots contain information that is absent from the integers \(a_i\).

A concrete pair of inputs shows both limitations. Let

\[
N=15,\qquad a_1=a_2=19.
\]

Since \(19\equiv4\pmod {15}\), both \(2\) and \(7\) are unit square roots of \(19\) modulo \(15\). The GCD-free matrix is

\[
M=\begin{bmatrix}1&1\end{bmatrix},
\]

and its sole nonzero relation is \(c=(1,1)\). Its exact root is \(R(c)=19\equiv4\pmod {15}\).

If \((x_1,x_2)=(2,2)\), then \(X(c)=4\), so the relation is trivial and no factor results. If \((x_1,x_2)=(2,7)\), then \(X(c)=14\), which is neither \(4\) nor \(-4\equiv11\). The two gcds are

\[
\gcd(15,14-4)=5,
\qquad
\gcd(15,14+4)=3.
\]

The integer data and matrix are identical in the two cases, but success differs. Keeping only one representative of the one-dimensional square-class span removes the kernel relation and loses the successful witness. An even sharper zero-square-class example is \(N=15\), \(a_1=4\), \(x_1=7\): the integer class is already a square, yet comparing \(7\) with the positive root \(2\) factors \(15\).

Therefore the construction proves no source-success theorem from square-class rank, kernel dimension, duplicates, or the existence of square relations alone. It is a conditional decoder: if some available square subset has a non-sign normalized root, it finds a factor by testing any kernel basis. It does not prove that such a subset is supplied by any external source process.

## Output-size qualification for part (iii)

If “computes the exact positive root for each kernel vector” is read as “explicitly list every vector-root pair,” the literal claim is false by output size. Take \(a_i=1\) and \(x_i=1\) for all \(i\). Then \(K=\mathbb F_2^m\) has \(2^m\) vectors. An explicit list identifying every vector is exponential in \(L\), even though every root equals one.

The block coordinates and displayed formula give the natural polynomial-size meaning: they are an exact decoder for every kernel vector, and the algorithm materializes only the roots of an arbitrary basis. Under that meaning, all four parts of the claim hold.
