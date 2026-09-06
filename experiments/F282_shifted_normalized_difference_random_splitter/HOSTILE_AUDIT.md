# Hostile audit of F282

## Verdict

**PASS, with the exact scope stated in the packet.**

The frozen proof establishes a constant-success random splitter for balanced
products of two distinct odd primes, conditional on access to the normalized
modular evaluator stated in `STATEMENT.md`. It does not construct that
evaluator. It therefore does not establish an executable numerical-QP
factoring algorithm or an unconditional factoring theorem.

This verdict uses only the symbolic argument. No finite experiment,
numerical search, or empirical evidence is relevant to it.

## Frozen-byte authentication

The SHA-256 digest of `FROZEN.sha256` is

```text
5e173dbf13cea22681133082df0b5771c7e2397d8612b5becf2ef63c9f468fec
```

This is the required digest. Independent checking of every entry in that
file gave:

```text
831ac1a429968a20fdeffa2e0c0e7d1972fe43deec3a22e43ee4b71a2d01f0bf  STATEMENT.md
0a5e20cb27f671d5e797196b1a987e776547b2f67be5a2e95af21b663ce69d2c  PROOF.md
f6b27283bc901fcf1959ed9bb393696194f6b4bc740248354cb34a2add52ef3f  SELF_AUDIT.md
f2423dffeb2bad01d05f09acb2f6fd1010f599b3cbbb2cb8a7d776680b95d2ed  PROVENANCE.md
7b6e1860f9f160a3e229c6980ada5643c6b72a6ea0341e51ac12fcd763ad7b88  MANIFEST.md
```

`HOSTILE_AUDIT.md` is not an entry in the frozen set.

## Reconstruction of the proof

### Promise geometry

Let $N=pq$, where $p<q<2p$ are distinct odd primes, and let
$B=\lfloor\sqrt N\rfloor$. Distinctness makes $N$ nonsquare, so

\[
p<B+1\leq q,
\qquad p\leq B<q<2p.
\]

If the public screen $\gcd(B,N)$ is nontrivial, then $B$ is a multiple of
$p$ or $q$. It cannot be a multiple of $q$, and the only multiple of
$p$ in $[p,2p)$ is $p$. Thus this branch has $B=p$ and immediately
returns $p$.

On the unresolved branch, write

\[
B=p+s,\qquad q=B+h.
\]

Then $s\geq1$. Since $B^2<N$,

\[
s(p+s)<ph,
\]

so $h>s$. Also $q-p=s+h$ is even. The endpoint $h=s+1$ would make it
odd. Hence

\[
h\geq s+2.
\]

Finally, $q<2p$ gives $s+h<p$. Therefore

\[
2s+2\leq s+h<p,
\qquad p\geq2s+3.
\]

The later strict bounds also follow: $q<2p<2B$ gives $h<B$, and
$h\geq2$ gives $B<q-1$.

### Exact normalization identity

For $m+1$ distinct nodes,

\[
[x_0,\ldots,x_m]X^{m+d}=h_d(x_0,\ldots,x_m).
\]

With $m=d=B$ and $x_j=a+j$, the Lagrange denominator is

\[
\prod_{k\ne j}(j-k)=(-1)^{B-j}j!(B-j)!.
\]

Consequently,

\[
h_B(a,a+1,\ldots,a+B)
=\frac1{B!}\sum_{j=0}^{B}(-1)^{B-j}\binom Bj(a+j)^{2B}
=\frac{\Delta^B X^{2B}|_{X=a}}{B!}.
\]

The right-hand complete-homogeneous polynomial lies in $\mathbb Z[a]$.
Thus the division is exact in the integers for every integer $a$. The proof
does not use modular division by $B!$.

### The $q$-local zero law

The $B+1$ consecutive nodes are distinct modulo $q$. Let their residue
set be $E\subset\mathbb F_q$, and let $C=\mathbb F_q\setminus E$. Then

\[
|C|=q-(B+1)=h-1.
\]

Using

\[
\prod_{x\in\mathbb F_q}(1-xt)=1-t^{q-1},
\]

the complete-homogeneous generating series becomes

\[
\prod_{x\in E}(1-xt)^{-1}
=\frac{\prod_{c\in C}(1-ct)}{1-t^{q-1}}.
\]

The numerator has degree at most $h-1<B$, and $B<q-1$. Therefore its
$t^B$ coefficient is zero. This proves

\[
F_B(a)\equiv0\pmod q
\]

for every integer shift $a$.

### The shifted $p$-local law

Modulo $p$, the $B+1=p+s+1$ nodes are one full copy of
$\mathbb F_p$ plus the extra multiset

\[
E_a=(a,a+1,\ldots,a+s).
\]

Hence

\[
\prod_{j=0}^{B}(1-(a+j)t)^{-1}
=\frac{H_{E_a}(t)}{1-t^{p-1}}.
\]

The coefficient of $t^{p+s}$ is

\[
h_{p+s}(E_a)+h_{s+1}(E_a).
\]

There are no more terms because the next index is
$s-p+2<0$. The nodes in $E_a$ are pairwise distinct modulo $p$, since
$s<p$. The distinct-node formula gives

\[
h_r(E_a)=\sum_{j=0}^{s}
\frac{x_j^{r+s}}{\prod_{k\ne j}(x_j-x_k)},
\qquad x_j=a+j.
\]

For $r=p+s$ and $r=s+1$, the numerator exponents are $p+2s$ and
$2s+1$. Fermat's law makes these powers equal for every nonzero $x_j$.
If $x_j=0$, both positive powers are zero. Thus no division by a possibly
zero node occurs, and

\[
h_{p+s}(E_a)=h_{s+1}(E_a)\pmod p.
\]

It follows that

\[
F_B(a)\equiv2h_{s+1}(a,a+1,\ldots,a+s)\pmod p.
\]

### Degree, leading coefficient, and roots

Set

\[
P_s(a)=2h_{s+1}(a,a+1,\ldots,a+s).
\]

There are $\binom{2s+1}{s}$ weak compositions of $s+1$ into $s+1$
parts. Each corresponding monomial contributes one to the coefficient of
$a^{s+1}$. Therefore $P_s$ has degree $s+1$ and leading coefficient

\[
2\binom{2s+1}{s}.
\]

Since $2s+1<p$, all factorials in the binomial coefficient are units in
$\mathbb F_p$. The factor $2$ is also a unit because $p$ is odd. Thus
the reduction of $P_s$ has exact degree $s+1$, is nonzero, and has at
most $s+1$ roots in $\mathbb F_p$.

### Exact success law and Las Vegas conclusion

Let

\[
r=|\{u\in\mathbb F_p:P_s(u)=0\}|.
\]

A uniform residue modulo $N$ has exactly $q$ lifts above each residue
modulo $p$. Therefore the exact one-trial distribution on the unresolved
branch is

\[
\Pr[\gcd(F_B(a),N)=q]=1-\frac rp,
\qquad
\Pr[\gcd(F_B(a),N)=N]=\frac rp.
\]

No third outcome is possible: $q$ always divides $F_B(a)$, and $N=pq$
is squarefree. Since $r\leq s+1$ and $p\geq2s+3$,

\[
1-\frac rp
\geq1-\frac{s+1}{p}
\geq\frac{p+1}{2p}
>\frac12.
\]

Independent trials terminate almost surely. Their exact expected count is
$p/(p-r)$, and

\[
\frac p{p-r}\leq\frac{2p}{p+1}<2.
\]

Assuming the stated uniform numerical-QP evaluator, the other operations are
exact polynomial-bit-complexity operations. Only a checked proper divisor is
returned. This is a conditional uniform classical Las Vegas factorer on the
stated promise. The public-gcd branch terminates before sampling.

## Hostile boundary checks

- **Endpoints:** The strict inequality $B^2<N$ is justified because the
  promised semiprime is nonsquare. The direct endpoint $B=p$ is screened.
  On the unresolved branch, parity excludes $h=s+1$, which is essential to
  $B<q-1$. All later coefficient cutoffs are strict.
- **Zero nodes:** A zero residue can occur in either local node set. The
  product identities include it harmlessly as a factor $1$. In the
  $p$-local Lagrange comparison, denominators contain only distinct-node
  differences; both powers of a zero node vanish.
- **Characteristic ranges:** The extra $p$-nodes are distinct because
  $s<p$. The exponent comparison differs by $p-1$. The leading
  coefficient is nonzero because $p>2s+1$, and characteristic two is
  excluded by the odd-prime promise.
- **Integer divisibility:** On the unresolved branch $p<B<q<2p$. Thus
  $B!$ contains $p$ exactly once and no $q$, so
  $\gcd(B!,N)=p$. Since $q\mid F_B(a)$, the raw difference
  $B!F_B(a)$ is always zero modulo $N$. The proof correctly performs the
  quotient over $\mathbb Z$ before reduction and never treats $B!$ as a
  unit modulo $N$.
- **Literal representation costs:** The $B+1$-term forward sum and the
  direct length-$B$ complete-homogeneous recurrence are exponential-scale
  in the input bit length. At $a=0$, the bounds
  $B^B\leq h_B(0,1,\ldots,B)\leq\binom{2B}{B}B^B$ give
  $\Theta(B\log B)$ materialized bits. These facts reject only the named
  literal methods; the packet does not turn them into an evaluator lower
  bound.

## Exact qualifications

The proof assumes the balanced, distinct, odd semiprime promise. It neither
recognizes that promise nor reduces arbitrary composites to it. It proves
nothing here for unbalanced semiprimes, prime squares, or composites with
three or more prime factors.

Most importantly, the packet supplies no algorithm to evaluate

\[
F_{\lfloor\sqrt N\rfloor}(a)\bmod N
\]

in numerical-QP bit complexity. The normalization by $B!$ is exactly the
factor-bearing obstruction for the literal forward-difference route. A
different uniform succinct evaluator is left open. The splitter theorem is
therefore exact but conditional, and no broader factoring claim is validated
by this audit.
