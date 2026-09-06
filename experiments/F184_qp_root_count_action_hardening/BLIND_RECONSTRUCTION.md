# F184 statement-only blind reconstruction

## Source restriction, hash, and verdict

The SHA-256 digest of `STATEMENT.md` is

```text
8bb68536d92e58cbbbcc6059950d0a3478e4854b50186bdc413af6919068ef3b
```

This reconstruction uses only that statement within the F184 directory.

**Verdict: VERIFIED AFTER ONE TYPO REPAIR.** Equation (5) has the malformed
display

```text
{,2+t(D+1),...,1+(t+1)(D+1)}.
```

The unique reading consistent with the immediately preceding phrase
“the block of `D+1` consecutive positive integers,” with the displayed last
endpoint, and with the later distinctness conclusion is

\[
\boxed{
\mathcal I_t={2+t(D+1),\ldots,1+(t+1)(D+1)\}.}
\tag{R0}
\]

That is, the stray comma after the opening brace must be deleted. The
repaired interval has exactly `D+1` entries. No mathematical claim fails
under this reading.

## 1. The bad-base polynomial and its degree

Define

\[
P(X)=X\prod_{k=1}^{K}(X^k-1)\in\mathbf Z[X].
\]

Its degree is

\[
\deg P=1+\sum_{k=1}^{K}k
=1+\frac{K(K+1)}2=D.
\tag{R1}
\]

For a rational prime \(\ell\), the condition \(\ell\mid C_a=P(a)\) is
equivalent to

\[
a=0\pmod\ell
\quad\text{or}\quad
a^k=1\pmod\ell
\text{ for some }1\le k\le K.
\tag{R2}
\]

If \(\ell\nmid a\), the latter condition is equivalent to
\(\operatorname{ord}_\ell(a)\le K\), since an order at most `K` divides
one of the integers \(1,\ldots,K\), and conversely a relation
\(a^k=1\) makes the order divide `k`.

The polynomial `P` is nonzero modulo every prime \(\ell>T\). Its leading
coefficient is one, so no reduction can make it the zero polynomial. A
nonzero degree-`D` polynomial over \(\mathbb F_\ell\) has at most `D`
distinct roots. Thus, for each such prime, at most `D` residue classes of
integer bases are bad in the sense of (R2).

## 2. Exact local-order update

Let

\[
g_{t,j}=\operatorname{ord}_{R_j}(w_t).
\]

For any finite-order group element `x`,

\[
\operatorname{ord}(x^e)
=\frac{\operatorname{ord}(x)}{\gcd(\operatorname{ord}(x),e)}.
\]

Using \(e=C_a^n\) gives

\[
\operatorname{ord}_{R_j}(z_{t,a})
=\frac{g_{t,j}}{\gcd(g_{t,j},C_a^n)}.
\tag{R3}
\]

If \(\ell^e\parallel g_{t,j}\) and \(\ell\mid C_a\), then
\(v_\ell(C_a^n)\ge n\). Also

\[
\ell^e\le g_{t,j}le\varphi(R_j)<R_j\le N<2^n,
\]

so \(e<n\). Therefore \(C_a^n\) removes the complete
\(\ell\)-primary part of the local order. If \(\ell\nmid C_a\), that
part survives unchanged. Hence (R3) can be written exactly as

\[
\operatorname{ord}_{R_j}(z_{t,a})
=\prod_{\substack{\ell^e\parallel g_{t,j}\\\ell\nmid C_a}}
\ell^e.
\tag{R4}
\]

This is why the fixed exponent `n` is sufficient for arbitrary prime-power
orders.

The gcd \(H_{t,a}=\gcd(z_{t,a}-1,N)\) is factor-first. If `z` is one
modulo some complete hidden components but not all, the gcd contains those
components and omits another, so it is proper. Divisibility by only part of
a component also gives a proper divisor. Thus on a branch with no returned
factor:

- \(H_{t,a}=N\) exactly when every local order in (R4) is one;
- \(H_{t,a}=1\) implies every local order in (R4) is nontrivial.

No field structure of \(\mathbf Z/R_j\mathbf Z\) is used. The argument
uses only the order of a unit modulo an arbitrary prime power and the
factor-first gcd. It therefore applies to repeated prime factors exactly as
claimed.

## 3. Existence of a survivor at every stage

Fix a stage `t`. Suppose, for contradiction, that no tested base returns a
factor and every one has \(H_{t,a}=N\). Then for every base
\(a\in\mathcal I_t\), all prime divisors of every current local order
divide \(C_a\), by (R4).

Choose any hidden component `j` and any rational prime
\(\ell\mid g_{t,j}\). Such a prime exists because the inductive invariant
will give \(g_{t,j}>1\). Since the current order is a divisor of the
initial order, it remains `T`-rough, so

\[
\ell>T>1+M(D+1).
\tag{R5}
\]

Every base in every stage lies between `2` and

\[
1+M(D+1)<\ell.
\tag{R6}
\]

In particular, the `D+1` distinct integers in \(\mathcal I_t\) remain
distinct residues modulo \(\ell\). The preceding supposition says that all
of them are roots of \(P\bmod\ell\). This is impossible because `P` has
degree `D` and at most `D` roots. Therefore some base cannot have
\(H_{t,a}=N\). On the no-factor branch its gcd must be one. This proves the
existence assertion (7).

The proof uses one arbitrary order prime from one component, but the chosen
gcd-one base simultaneously leaves a nontrivial order in every component.
That simultaneous conclusion comes from the global gcd, not from the root
count alone.

## 4. Inductive preservation and all selected actions

Select the first base with \(H_{t,a_t}=1\) and put
\(w_{t+1}=z_{t,a_t}\). Equation (R4) shows that every new local order
divides the preceding local order. The gcd-one condition shows that it is
nontrivial. It follows inductively that

\[
g_{t+1,j}>1,
\qquad
g_{t+1,j}\mid g_{t,j}\mid g_{0,j}.
\tag{R7}
\]

Hence every `g_{t+1,j}` remains coprime to `N`, and every rational prime
dividing it remains greater than `T`. This establishes the complete order
invariant at every stage, including the final assertion (9).

Now fix \(\ell\mid g_{M,j}\). Divisibility in (R7) implies
\(\ell\mid g_{t+1,j}\) for every earlier selected stage `t`. By (R4), an
order prime survives the update at stage `t` only if

\[
\ell\nmid C_{a_t}.
\]

Using the factorization of \(C_{a_t}\), this is equivalent to

\[
\ell\nmid a_t,
\qquad
a_t^k\ne1\pmod\ell\quad(1\le k\le K).
\]

Since the first condition makes \(a_t\) a unit modulo \(\ell\), the second
is exactly

\[
\operatorname{ord}_\ell(a_t)>K.
\tag{R8}
\]

Thus every prime in every final local order supports all `M` selected
long-action conditions simultaneously.

The repaired intervals are consecutive, pairwise disjoint blocks:

\[
\max\mathcal I_t=1+(t+1)(D+1),
\]

\[
\min\mathcal I_{t+1}=2+(t+1)(D+1).
\]

Therefore the selected integer bases \(a_0,\ldots,a_{M-1}\) are distinct.
For each final order prime \(\ell\), multiplication by `a_t` is an
automorphism of the additive cyclic group \(\mathbf Z/\ell\mathbf Z\), and
that automorphism has exact order \(\operatorname{ord}_\ell(a_t)>K\).
This justifies the wording in (11).

## 5. Deterministic quasipolynomial cost

Let numerical-QP mean a bound of the form

\[
2^{(\log(n+1))^{O(1)}}.
\]

Both `K` and `M` have this size. Then

\[
D=1+\frac{K(K+1)}2
\]

and the total number of tested bases, at most

\[
M(D+1),
\]

are numerical QP as well.

Every tested base satisfies

\[
2\le a\le1+M(D+1),
\]

so \(\operatorname{bitlen}(a)=(\log n)^{O(1)}\). The integer

\[
C_a=a\prod_{k=1}^{K}(a^k-1)
\]

need not be factored. Its bit length obeys

\[
\begin{aligned}
\operatorname{bitlen}(C_a)
&=O\!\left(1+\log a+\sum_{k=1}^{K}k\log a\right)\\
&=O(D\log a),
\end{aligned}
\tag{R9}
\]

which is numerical QP. It can be built by iterative powering and integer
multiplication in time polynomial in this output length, hence QP.

The exponent \(E_a=C_a^n\) has

\[
\operatorname{bitlen}(E_a)
=O(n\operatorname{bitlen}(C_a)),
\tag{R10}
\]

again numerical QP. Binary modular exponentiation computes
\(w_t^{E_a}\bmod N\) with `O(bitlen(E_a))` modular multiplications. Each
modular multiplication and each gcd is polynomial in `n`. Multiplying this
cost by the QP number of bases remains QP.

All choices use public lexicographic order: stages are increasing, bases in
each block are increasing, and the first gcd-one base is selected. The
algorithm is therefore uniform and deterministic. It invokes neither
factorization of `C_a` nor a resultant or annihilator factorization.

## 6. Exact scope boundary

For a final prime \(\ell\), the selected bases lie in the cyclic group
\((\mathbf Z/\ell\mathbf Z)^\times\). Conditions (R8) say that every one
has individual order greater than `K`. They do not say that the subgroup
generated by the `M` bases has product-sized order, positive rank `M`, or
even increasing order with `M`. All selected elements may be powers of one
generator inside one large cyclic subgroup.

Therefore the construction supplies simultaneous long actions but neither
independent quotient directions nor the factorization of any hidden local
order. The surviving branch does not certify an exact common order and is
not an all-input factoring algorithm.

## Final verdict

**VERIFIED AFTER TYPO REPAIR — SHA-256
`8bb68536d92e58cbbbcc6059950d0a3478e4854b50186bdc413af6919068ef3b`.**

The only statement defect is the stray comma at the beginning of the set in
equation (5). Deleting it yields the uniquely intended `D+1`-element block.
After that syntactic repair, the arbitrary-prime-power correctness, exact
degree and root count, survivor existence at each stage, simultaneous
preservation of all selected action conditions, distinct-base conclusion,
and uniform deterministic QP cost all withstand independent reconstruction.
