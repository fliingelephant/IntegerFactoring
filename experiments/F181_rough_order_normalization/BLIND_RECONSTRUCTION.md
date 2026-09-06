# F181 blind reconstruction

Source used: `STATEMENT.md` only.

Pinned source SHA-256:

```text
992f84a580a362d7908d9287e186dbae46963044956dae65b7b52540fa15df32
```

## Verdict

**PASS.** All stated conclusions follow from the stated hypotheses. The proof
works for every odd composite (N), including a single prime power and
products containing repeated prime factors. No squarefreeness assumption is
used. The shift-three corollary removes the nonunit escape, but it does not
turn the remaining long-action outcome into a factor.

## 1. Two general lemmas

Write the prime-power decomposition as

\[
N=\prod_{j=1}^s R_j,
\qquad R_j=p_j^{e_j},
\]

where the (p_j) are distinct. For every local order (r_j) of a unit modulo
(R_j),

\[
r_j\mid \varphi(R_j),
\qquad r_j< R_j\le N<2^n.
\tag{15}
\]

The last inequality follows from
(n=\lceil\log_2(N+1)\rceil).

### Lemma 1: exact primary deletion

Let (x) be a unit modulo (N), let
(r_j=\operatorname{ord}_{R_j}(x)), and let (C\ge2). Then

\[
\operatorname{ord}_{R_j}(x^{C^n})
=\frac{r_j}{\gcd(r_j,C^n)}.
\tag{16}
\]

If (q^a\parallel r_j), then (15) gives

\[
2^a\le q^a\le r_j<2^n,
\]

so (a<n). Hence:

- if (q\mid C), then (v_q(C^n)\ge n>a), so the full factor
  (q^a) is deleted;
- if (q\nmid C), then (v_q(C^n)=0), so the full factor (q^a)
  remains.

Therefore

\[
\boxed{
\operatorname{ord}_{R_j}(x^{C^n})
=\prod_{\substack{q^a\parallel r_j\\q\nmid C}}q^a.
}
\tag{17}
\]

This is exact deletion of primary components. It is not only deletion of one
copy of each prime.

### Lemma 2: factor-first stripping

Let (E) be given with its complete factorization. Suppose
(r_j=\operatorname{ord}_{R_j}(x)) divides (E) for every (j). Start with
(M=E). For each prime (q\mid M), repeat the following step while
(q\mid M):

\[
z=x^{M/q}\bmod N,
\qquad d=\gcd(z-1,N).
\tag{18}
\]

- If (1<d<N), return the proper factor (d).
- If (d=N), replace (M) by (M/q).
- If (d=1), retain this copy of (q) and stop stripping (q).

The invariant (r_j\mid M) holds. Indeed, (d=N) says
(x^{M/q}=1\pmod {R_j}) for every (j), which is equivalent to
(r_j\mid M/q) for every (j).

Assume the procedure returns no factor. At the first retained copy of (q),
(d=1). Thus no full (R_j) divides (x^{M/q}-1), and therefore
(r_j\nmid M/q) for every (j). Since (r_j\mid M), this forces

\[
v_q(r_j)=v_q(M)
\qquad\text{for every }j.
\tag{19}
\]

Later stripping of other primes preserves this equality. A prime stripped
completely has valuation zero in every (r_j). Consequently the final value
satisfies

\[
\boxed{M=r_1=\cdots=r_s.}
\tag{20}
\]

The factorization of (M) is inherited from the factorization of (E).

This argument also covers repeated prime factors of (N). If
(x^{M/q}-1) is divisible by (p_j) but not by all of
(R_j=p_j^{e_j}), then (18) can be a partial power of (p_j). It is still a
proper factor and is returned. Thus the proof never assumes that a gcd is a
product of whole hidden components. This observation also covers the case
(s=1), where (N) itself is a composite prime power.

## 2. Exact rough-order normalization

The complete factorization of the least common multiple is

\[
\Lambda_T
=\prod_{\substack{\ell\le T\\ \ell\ {m prime}}}
 \ell^{\lfloor\log_\ell T\rfloor}.
\tag{21}
\]

Its prime support is exactly the set of primes at most (T). Apply Lemma 1
with (x=y) and (C=\Lambda_T). Since
(Q=\Lambda_T^n), it gives

\[
\operatorname{ord}_{R_j}(w)
=\prod_{\substack{\ell^a\parallel f_j\\\ell>T}}\ell^a
=g_j.
\tag{22}
\]

This proves the boxed identity in (7). Notice why the exponent (n) is
needed. A prime (ell\le T) can occur in (f_j) to a high power, including
a power larger than (T). The bound (a<n) makes (Q) delete that complete
primary factor.

Now let (H=\gcd(w-1,N)). Since (H\mid N), exactly one of the three cases
below occurs.

### Case (1<H<N)

The value (H) is a nontrivial proper divisor of (N). No claim that it is
a product of whole (R_j)'s is required.

### Case (H=N)

Here (w=1\pmod N). Hence (w=1\pmod {R_j}) and
(f_j\mid Q) for every (j). Equivalently, (22) has (g_j=1) for every
(j).

Use Lemma 2 with (x=y) and the fully factored annihilator (E=Q). It
returns either a proper factor or a fully factored integer (m) such that

\[
m=f_1=\cdots=f_s.
\tag{23}
\]

The hypothesis \(\sigma(f_j)>T\) implies (f_j>T). Therefore the no-factor
outcome is exactly the stated factored common-order state (m>T).

This case is essential. The condition \(\sigma(f_j)>T\) does not imply that
(f_j) has a prime divisor larger than (T). For example, its largest
primary factor can be a high power of a small prime. Such orders are deleted
completely by (Q), and factor-first stripping resolves whether their exact
local orders agree.

### Case (H=1)

For every (j), the congruence (w=1\pmod {R_j}) is impossible. Hence
(g_j=\operatorname{ord}_{R_j}(w)>1). Every prime divisor of (g_j) is
larger than (T), by (22). It follows that

\[
g_j>T,
\qquad P^-(g_j)>T.
\tag{24}
\]

Also (g_j\mid f_j), so the input hypothesis gives

\[
\gcd(g_j,N)=1.
\tag{25}
\]

Equations (24) and (25) prove all three assertions in (9). They also make
(P^-(g_j)) well-defined.

These three cases prove the exclusive output list and the replacement
trichotomy in (10). They do not claim an all-input factoring algorithm.

## 3. Uniform deterministic bit cost

A deterministic sieve or trial division through (T) constructs (21) and
its factorization. The crude bound

\[
\log_2\Lambda_T\le\log_2(T!)=O(T\log T)
\tag{26}
\]

gives

\[
\log_2 Q=O(nT\log T).
\tag{27}
\]

Since the fixed numerical bound (T(n)) is quasipolynomial, enumeration
through (T), integer construction, modular powering, and gcd computation
all have deterministic quasipolynomial bit cost.

In factor-first stripping, the number of attempted deletions is at most the
number of prime factors of (Q), counted with multiplicity. This is at most
(\log_2Q). Each attempt uses one modular power with an exponent of at most
(\log_2Q) bits and one gcd on (O(n))-bit residues. Thus the complete
factor-first stage also has uniform deterministic quasipolynomial bit cost.

## 4. The separate shift-three corollary

Assume now that (w) is the rough descendant. Put

\[
u_0=w^{A_0^n}\bmod N,
\qquad
u_3=w^{B_3^n}\bmod N.
\tag{28}
\]

Lemma 1 gives their local orders exactly:

\[
\operatorname{ord}_{R_j}(u_0)
=\prod_{\substack{q^a\parallel g_j\\q\nmid A_0}}q^a,
\qquad
\operatorname{ord}_{R_j}(u_3)
=\prod_{\substack{q^a\parallel g_j\\q\nmid B_3}}q^a.
\tag{29}
\]

For either (u_b), compute

\[
H_b=\gcd(u_b-1,N).
\tag{30}
\]

A proper value of (H_b) is a factor. A value (H_b=N) means that the
filter is the identity on every hidden component. A value (H_b=1) means
that every local order in (29) is nontrivial. Such a surviving order remains
(T)-rough and is larger than (T).

Consider the zero-shift filter. Every prime (q\mid g_j) is a unit modulo
(N), because \(\gcd(g_j,N)=1\). If (q) survives this filter, then
(q\nmid A_0). If \(\operatorname{ord}_q(N)\le K\), then for
(k=\operatorname{ord}_q(N)) the factor (N^k-1) occurs in (A_0). This
would give (q\mid A_0), a contradiction. Therefore every surviving order
prime satisfies

\[
q\nmid N,
\qquad \operatorname{ord}_q(N)>K.
\tag{31}
\]

Now consider the shift-three filter. If (q) survives it, then
(q\nmid B_3). The explicit factor (N+3) first gives

\[
q\nmid N+3.
\tag{32}
\]

Thus (N+3) is a unit modulo (q). If its multiplicative order were at
most (K), the corresponding factor ((N+3)^k-1) in (B_3) would be
divisible by (q). Hence

\[
\operatorname{ord}_q(N+3)>K.
\tag{33}
\]

Equations (32) and (33) delete the shift-three nonunit alternative. Without
the explicit factor (N+3), a prime divisor of (N+3) would survive all
factors ((N+3)^k-1).

It remains to analyze the case in which both filters are the identity
globally. Then (g_j\mid A_0^n) and (g_j\mid B_3^n) for every (j). Fix
a prime (q\mid g_j). There is some (k\le K) with

\[
q\mid N^k-1.
\tag{34}
\]

Also either (q\mid N+3), or there is some (l\le K) with

\[
q\mid (N+3)^l-1.
\tag{35}
\]

In the first case, (N\equiv-3\pmod q). Combining this with (34) gives

\[
q\mid (-3)^k-1
\quad\Longleftrightarrow\quad
q\mid 3^k-(-1)^k=S_k.
\tag{36}
\]

In the second case, the residue (N\pmod q) is a common root of

\[
X^k-1
\quad\text{and}\quad
(X+3)^l-1
\]

over \(\mathbb F_q\). Therefore their integer resultant is zero modulo
(q), and

\[
q\mid R_{k,l}.
\tag{37}
\]

All cage integers are nonzero. Clearly (S_k>0). If the two polynomials in
(37) had a common complex root \(\alpha\), then

\[
|\alpha|=1,
\qquad |\alpha+3|=1.
\]

But the triangle inequality would give

\[
3=|(\alpha+3)-\alpha|
\le |\alpha+3|+|\alpha|=2,
\]

a contradiction. Hence every (R_{k,l}) is a positive nonzero integer.

Define

\[
C=\prod_{k=1}^K S_k
  \prod_{k=1}^K\prod_{l=1}^K R_{k,l}.
\tag{38}
\]

Equations (36) and (37) show that every prime in every (g_j) divides
(C). If (q^a\parallel g_j), then (a<n) by (15). Thus (C^n) contains
at least (q^n), and therefore

\[
g_j\mid C^n
\qquad\text{for every }j.
\tag{39}
\]

Factor each integer in (38) by deterministic trial division and merge the
factorizations. Multiplying all exponents by (n) gives a complete
factorization of the annihilator (C^n). Apply Lemma 2 with (x=w) and
(E=C^n). It returns a proper factor, or it proves

\[
\operatorname{ord}_{R_1}(w)=\cdots=
\operatorname{ord}_{R_s}(w)=m.
\tag{40}
\]

The integer (m) is fully factored and (m>T), because every local order
of the rough descendant has that property.

Together, (30)--(40) give the two-shift trichotomy: a proper factor, a
factored exact common-order state above (T), or a nontrivial filtered
descendant whose surviving order primes are units for the relevant public
base and have multiplicative order above (K). The last outcome is not
claimed to force a factor.

## 5. Bit cost of the corollary

Since (K=O((\log n)^c)),

\[
\log_2 A_0=O(nK^2),
\qquad
\log_2 B_3=O(nK^2).
\tag{41}
\]

The exponents (A_0^n) and (B_3^n) therefore have
(O(n^2K^2)) bits. Their construction and the modular powers in (28) have
polynomial, hence quasipolynomial, bit cost.

For a (k)-th root of unity \(\alpha\),

\[
|((\alpha+3)^l-1)|\le4^l+1.
\]

The product formula for a monic resultant gives

\[
\log_2 R_{k,l}=O(kl)=O(K^2).
\tag{42}
\]

There are (K^2) resultants, and each (S_k) has (O(K)) bits. Thus
(C) has (O(K^4)) bits and (C^n) has (O(nK^4)) bits. Computing the
resultants by their Sylvester determinants is polynomial in these displayed
dimensions and bit lengths.

Trial division of an (O(K^2))-bit integer costs at most

\[
2^{O(K^2)}
=\exp((\log n)^{O(1)}),
\tag{43}
\]

which is quasipolynomial in (n). There are only (O(K^2)) cage integers.
The resulting factor-first stage has quasipolynomially many bit operations
by the same count as in Section 3. This proves the stated uniform
deterministic quasipolynomial cost.

The reconstruction is symbolic. It uses no numerical experiment.
