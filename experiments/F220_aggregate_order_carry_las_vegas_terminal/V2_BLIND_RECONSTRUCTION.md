# F220 V2 statement-only blind reconstruction

## Verdict

**PASS.** I found no false theorem, missing case, or quantifier reversal in the
V2 statement. This verdict applies only to the conditional terminal and source
laws stated in V2. It does **not** promote F220 to a solution of the integer
factoring prompt: V2 explicitly does not construct a witness source satisfying
its progress premise, handle arbitrary composites in the terminal, or give the
full recursive factoring algorithm.

Before reading the statement I computed

```text
SHA-256(V2_STATEMENT.md)
= 935ef9a28dff6bfade891ca069eb5d544236977c4c8c20c6d4208ff582b5fe45
```

which exactly matches the required hash. I then used only `PROMPT.md` and
`V2_STATEMENT.md`. I did not read a proof, self-audit, provenance, manifest,
V1 packet, hostile audit, durable ledger, or another agent's work.

One complexity convention is essential below. I read “every stage has
numerical-QP bit cost” in the standard uniform sense: the fixed public
procedure has one numerical-QP worst-case stage bound \(W(n)\), valid for every
stage and every history. A merely pointwise family of unrelated bounds
\(W_k(n)\) would not imply the stated total-cost conclusion. Under the standard
uniform reading, the theorem is correct.

## A. Primary certificates and unrelated witnesses

Fix a rational prime \(r\mid N\), and write

\[
o_r=\operatorname{ord}_r(a).
\]

From \(a^A\equiv1\pmod N\), \(a\) is a unit modulo \(N\), and
\(o_r\mid A\). If \(g_\ell=1\), then
\(a^{A/\ell}\not\equiv1\pmod r\) for every \(r\mid N\). Hence
\(o_r\nmid A/\ell\). Since \(o_r\mid A\) and
\(\ell^{e_\ell}\parallel A\), this is possible exactly when

\[
v_\ell(o_r)=e_\ell.
\]

Fermat's theorem gives \(o_r\mid r-1\), so

\[
\ell^{e_\ell}\mid r-1
\]

for every rational prime \(r\mid N\). This proves (A3), including when \(N\)
contains arbitrary powers \(r^f\): the proof deliberately reduces modulo the
rational prime \(r\). Also, \(g_\ell=1\) excludes divisibility by every such
\(r\), while any value \(1<g_\ell<N\), including a partial power of a repeated
prime, is already a valid proper divisor.

The product in (A4) uses distinct primary components of \(A\), so each of its
components divides every \(r-1\); thus (A5) follows. For certificates from
unrelated witnesses, write \(c_i\mid r-1\) for each fixed \(r\mid N\). Taking
the maximum valuation prime by prime gives

\[
\operatorname{lcm}_i(c_i)\mid r-1.
\]

No equality, synchronization, or common origin of the hidden local orders is
used. This proves (A6) with the stated quantifiers.

## B. Generalized CRT and the exact GFHP threshold

Because \(M\mid p-1\) and \(M\mid q-1\), the two congruences in (B4) are
compatible: their common hidden solution is \(p\). The overlap must not be
counted twice. Put

\[
u=v_2(M),\qquad \beta_2=\min\{t,u\},\qquad d=2^{\beta_2}
   =\gcd(2^t,M).
\]

Compatibility is the concrete condition \(b\equiv1\pmod d\), and

\[
L=\frac{2^tM}{d}.
\]

Writing \(s=b+2^t k\), divide
\(2^t k\equiv1-b\pmod M\) by \(d\). The coefficient
\(2^t/d\) is invertible modulo \(M/d\), so one inversion computes \(k\)
modulo \(M/d\), hence the unique \(s\pmod L\). This is the generalized-CRT
“two-primary carry”; it also shows directly that all integers involved have
\(O(n)\) bits on a valid semiprime instance. Euclid, inversion, multiplication,
and reduction therefore take polynomial bit complexity.

The hidden solution gives \(p\equiv s\pmod L\). Moreover, \(2^t\) is coprime
to odd \(N\), while \(M\mid p-1,q-1\), so neither \(p\) nor \(q\) divides
\(M\). Thus

\[
\gcd(L,N)=1.
\]

The canonical \(s\) is odd because \(s\equiv p\pmod2\), hence \(s\ne0\).
If \(L>p\), the congruence and \(0\le s<L\) force \(s=p\), so
\(\gcd(s,N)=p\). Equality \(L=p\) contradicts \(\gcd(L,N)=1\). Consequently,
if the preliminary gcd does not split \(N\), then \(L<p<N\), exactly as
claimed.

For completeness, the arithmetic-progression terminal used here has the
following bit-complexity form for
\(\sqrt{N/2}<p<\sqrt N\): knowing

\[
p\equiv s\pmod L,\qquad \gcd(L,N)=1,
\]

permits deterministic factoring in

\[
\left(1+\frac{N^{1/4}}L\right)n^{O(1)}
\tag{1}
\]

bit operations. This is the relevant Gao--Feng--Hu--Pan progression bound,
not a bound with a square root of \(L\). One way to see the parameter exactly
is to write \(p=s+Lx\), where \(0\le x<\sqrt N/L\), and partition the possible
\(x\)'s into \(O(1+N^{1/4}/L)\) intervals of length a fixed constant times
\(N^{1/4}\). After shifting an interval and multiplying by \(L^{-1}\bmod N\),
each interval is one monic linear small-root problem modulo an unknown divisor
\(p>\sqrt{N/2}\). The GFHP linear progression routine solves each such block in
\(n^{O(1)}\) bit operations. Its lattice dimension and all intermediate bit
lengths are polynomial in \(n\); candidate divisors are verified by gcd. This
gives (1) in the bit model.

If \(L\ge N^{1/4}/S(n)\), (1) is at most
\((1+S(n))n^{O(1)}\), which is numerical QP. Since \(L\) is an integer,

\[
L\ge T_{\rm G}
\iff L\ge\lceil T_{\rm G}\rceil=J_{\rm G}.
\]

Thus the threshold in (B7) is exact. No replacement by the larger dyadic
envelope is valid or needed.

Finally, valuations give

\[
v_\ell(\operatorname{lcm}(L,c))-v_\ell(L)
=\max\{v_\ell(c)-v_\ell(L),0\},
\]

which proves (B8). In particular, the factor \(2^{\beta_2}\) in the CRT
overlap prevents a two-primary block already present in \(2^t\) from being
credited again.

## C. Exact-target Las Vegas drift

For integer \(L\ge1\), (C3) has the exact dichotomy

\[
\Phi(L)=0\iff L\ge J_{\rm G},
\qquad
\Phi(L)\ge1\iff L<J_{\rm G}.
\]

Also \(0\le\Phi(L)\le H\), with \(H=O(n)\). If a stage produces a block
\(c\nmid L\), then

\[
\frac{\operatorname{lcm}(L,c)}L
\]

is an integer at least (2). Therefore \(\Phi\) decreases by at least one.
A verified factor sends it to zero. If neither event occurs, \(L\) and
\(\Phi\) are unchanged. For the useful event \(U_k\), this gives

\[
\mathbf 1_{U_k}
\le \Phi_k-\Phi_{k+1}
\le H\mathbf 1_{U_k}.
\tag{2}
\]

The left inequality proves (C6) implies (C5) with the same \(Q\). The right
inequality proves the converse:

\[
\Pr(U_k\mid\mathcal F_k)
\ge \frac1{H Q(n)}.
\]

For a nonterminal history \(H\ge1\); replacing \(Q\) by \(HQ\) costs only an
\(O(n)\) factor. This proves the claimed equivalence at numerical-QP scale and
does not use independence.

Let \(\tau\) be the first terminal stage. Apply (C5) to the stopped process.
For every \(m\), conditional expectation and telescoping give

\[
\frac1{Q(n)}\,\mathbb E[\tau\wedge m]
\le \Phi_0-\mathbb E[\Phi_{\tau\wedge m}]
\le \Phi_0\le H.
\]

Monotone convergence yields

\[
\mathbb E\tau\le H Q(n)<\infty.
\]

Hence \(\tau<\infty\) almost surely. With the single uniform stage bound
\(W(n)\), the expected preterminal cost is at most
\(W(n)H Q(n)\), still numerical QP. The final verified factor or Theorem B
adds one more numerical-QP cost. This proves the precise Las Vegas claim for
the fixed scheduled procedure.

For iid draws, while a failure leaves \(L\) unchanged, the next draw sees the
same event with probability \(\pi_\mu(L)\). Independence then gives

\[
\Pr(T=j)=(1-\pi_\mu(L))^{j-1}\pi_\mu(L),
\qquad
\mathbb E T=1/\pi_\mu(L),
\]

with the usual infinite-mean convention if \(\pi_\mu(L)=0\). No iid claim is
used in the history-uniform drift theorem.

## D. Exact CRT-uniform primary law

For odd \(R_j=r_j^{f_j}\), the unit group is cyclic of order
\(h_j=\varphi(R_j)\). Since \(\gcd(A,N)=1\), no \(r_j\) divides \(A\), and

\[
d_j=\gcd(A,h_j)=\gcd(A,r_j-1).
\]

Reduction of a uniform unit modulo \(R_j\) is uniform modulo \(r_j\). There
are \(d_j\) roots of \(X^A=1\) in the \(r_j-1\) element group modulo \(r_j\).
Thus the probability that \(r_j\nmid a^A-1\) is
\(1-d_j/(r_j-1)\). CRT independence proves

\[
\Pr(G_0=1)=
\prod_j\left(1-\frac{d_j}{r_j-1}\right)=B.
\]

There are exactly \(d_j\) roots modulo \(R_j\), so

\[
\Pr(G_0=N)=\prod_j\frac{d_j}{h_j}=\Gamma.
\]

This explicitly handles the apparent repeated-prime-power hazard. It is
possible that \(G_0\) contains only \(r_j^v\) with \(0<v<f_j\); such an
outcome is neither in \(G_0=1\) nor \(G_0=N\), and is already a proper factor.

Condition on \(G_0=N\). The component \(a_j\) is then uniform in the cyclic
\(A\)-torsion subgroup of size \(d_j\). The reduction kernel from units modulo
\(r_j^{f_j}\) to units modulo \(r_j\) is an \(r_j\)-group. Since
\(r_j\nmid A\), it intersects the \(A\)-torsion trivially. Consequently, for
these conditional components, equality modulo \(r_j\) is equivalent to
equality modulo all of \(R_j\); the later gcds cannot expose only a partial
power of \(r_j\).

Fix \(\ell^{e_\ell}\parallel A\). If
\(v_\ell(d_j)<e_\ell\), then every element in the local torsion subgroup
satisfies \(a_j^{A/\ell}=1\). If
\(v_\ell(d_j)=e_\ell\), the same equality holds with probability exactly
\(1/\ell\). Call the latter coordinates active; there are \(c_\ell\) of
them. For one primary gcd to avoid a proper factor, all coordinates must have
the same equality status. This gives all four cases in (D8):

- If \(c_\ell=0\), all coordinates equal \(1\), so the no-progress
  probability is \(1\).
- If \(0<c_\ell<\nu\), inactive coordinates always equal \(1\), so every
  active coordinate must also equal \(1\), with probability
  \(\ell^{-c_\ell}\).
- If \(c_\ell=\nu\) and the block would grow \(L\), only the all-equal case
  avoids progress, with probability \(\ell^{-\nu}\).
- If \(c_\ell=\nu\) and the block is already in \(L\), both the all-equal
  case and the all-non-equal case avoid progress. Their probabilities are
  \(\ell^{-\nu}\) and \((1-\ell^{-1})^\nu\).

For a uniform element of a finite cyclic group, its Sylow components are
independent. The tests for distinct \(\ell\)'s depend on distinct Sylow
components, and CRT also makes the \(j\)-components independent. Hence the
conditional no-progress probability is exactly
\(\prod_{\ell\mid A}f_\ell(L)\), not merely a bound. The disjoint initial
events then give

\[
P_{\rm np}(L)=B+\Gamma\prod_{\ell\mid A}f_\ell(L),
\qquad
\pi_A(L)=1-P_{\rm np}(L).
\]

This reconstructs (D8)--(D10), including arbitrary rational-prime powers and
accumulation from witnesses with different local orders.

## E. Exact ceilings and source obstructions

Each certified aggregate satisfies \(M\mid r-1\) for every distinct rational
prime \(r\mid N\). Therefore

\[
M\mid D_N,
\qquad
L=\operatorname{lcm}(2^t,M)\mid
\operatorname{lcm}(2^t,D_N)=C_N(t).
\]

Thus \(C_N(t)<J_{\rm G}\) makes the actual threshold unreachable by aggregate
growth. In contrast, \(C_N(t)<R_*\) alone says only that the dyadic envelope
is unreachable. When \(J_{\rm G}\le C_N(t)<R_*\), the ceiling supplies no
obstruction to the actual target; it does not assert that a particular source
will attain the ceiling.

For \(N=pq\),

\[
D_N=\gcd(p-1,q-1)\mid(q-p).
\]

In the uniform \(A=N-1\) experiment,

\[
\gcd(A,p-1)=\gcd(A,q-1)=D_N=d.
\]

A useful stage must lie in the union of the events
\(a^A=1\pmod p\) and \(a^A=1\pmod q\): a partial initial gcd needs at least
one such event, and a later certified block needs both. Reduction modulo the
two primes and a union bound therefore give, at every current \(L\),

\[
\Pr(\text{factor or strict growth})
\le \frac d{p-1}+\frac d{q-1}.
\]

If \(q-p\le C\), then \(M\le d\le C\), and for the associated balanced
semiprimes the displayed probability is \(O(C/p)=2^{-\Omega(n)}\). The
bounded-prime-gap theorem supplies infinitely many fixed-\(C\) prime pairs,
and all sufficiently large pairs satisfy \(q<2p\). Splitting certificates into
primary blocks changes neither \(M\mid d\) nor this probability ceiling.

For the cyclic-direction model, the key repeated-power point is precisely
\(\gcd(c,N)=1\). The kernel of

\[
(\mathbb Z/r_j^{f_j}\mathbb Z)^\times
\longrightarrow(\mathbb Z/r_j\mathbb Z)^\times
\]

is an \(r_j\)-group. A cyclic subgroup of order \(c\), with \(r_j\nmid c\),
meets that kernel trivially. Thus each \(g_j\) still has order \(c\) after
reduction modulo \(r_j\). For synchronized exponent \(z\), every local order
is consequently

\[
m_z=\frac c{\gcd(c,z)}.
\]

For every stripping exponent, the equality test has the same truth value in
all components and, by injectivity, modulo \(r_j\) if and only if modulo the
whole \(R_j\). Every gcd is therefore \(1\) or \(N\), even with repeated
rational-prime powers. Exact orders and certified primary blocks all divide
\(c\).

Let \(\ell^e\parallel c\). The full \(\ell^e\) part occurs in \(m_z\) exactly
when \(\ell\nmid z\). It is absent from the lcm of \(k\) independent witnesses
exactly when all \(k\) exponents are divisible by \(\ell\). Uniformity modulo
\(c\) gives probability

\[
(1/\ell)^k=\ell^{-k}.
\]

Finally, every source aggregate divides \(c\), so its total modulus divides
\(C_c(t)=\operatorname{lcm}(2^t,c)\). The strict condition
\(C_c(t)<J_{\rm G}\) is therefore the exact actual-threshold obstruction;
\(C_c(t)<R_*\) alone is not.

## Refutation summary

I specifically tried the following failure modes and found that the statement
already excludes or accounts for each one:

1. partial gcds inside \(r^f\) in Theorem D;
2. double-counting the common two-primary part in the generalized CRT;
3. treating unrelated witness orders as equal instead of accumulating only
   certified primary divisibility;
4. replacing \(J_{\rm G}\) by the strictly larger dyadic envelope;
5. deriving expected total cost from nonuniform per-stage bounds;
6. using independence where the history-uniform drift proof does not have it;
7. assuming torsion injects through repeated prime powers without
   \(\gcd(c,N)=1\); and
8. mistaking a bounded aggregate ceiling or exponentially small source
   probability for a complete factoring impossibility result.

No counterexample survived these checks. The exact remaining scope paragraph
is accurate: the deterministic terminal is conditional, and the missing
uniform witness-source progress law remains a theorem-strength gap relative to
the top-level factoring prompt.
