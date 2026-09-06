# F223 V2 statement-only blind reconstruction

## Verdict

**PASS**, with the exact scope stated in V2.

Theorems A, C, D, E, and F reconstruct. Theorem B reconstructs exactly as
an imported Cohen--Lenstra interface; the statement does not contain, and
this reconstruction does not invent, a proof of Cohen--Lenstra Theorems 6.3
and 7.8. The Gao--Feng--Hu--Pan known-residue algorithm is likewise used only
through the named terminal interface in Theorem C. The finite witness can be
checked from the displayed integers alone.

This pass does **not** turn F223 into an integer-factoring algorithm. The
certificates in Theorem C are hypotheses. No all-input inverse-QP source for
them is proved.

The statement was read only after its SHA-256 was checked to be

```text
a5d38c57213a9c237723e2ea916ee2865f81cc8b086287728d493a07ebf2334c
```

No witness program or output was used, and no numerical program was run.

## A. Local orbit, characters, and simultaneous exponents

Let

\[
G=(\mathbb Z/q\mathbb Z)^\times,
\qquad H=\langle N\bmod q\rangle,
\qquad h=\operatorname{ord}_q(N).
\]

Statements (A1) and (A2) are the same assertion by the definition of
\(H\). If \(r=N^i\) in \(G\), every multiplicative character satisfies
\(\chi(r)=\chi(N)^i\), so (A1) implies (A3).

Conversely, suppose (A3) holds for one integer \(i\). Then every character
is trivial on \(rN^{-i}\). Characters separate elements of the finite cyclic
group \(G\): if \(g\) generates \(G\) and \(x=g^a\ne1\), the character
defined by

\[
\chi(g)=\exp(2\pi i/(q-1))
\]

has \(\chi(x)\ne1\). Hence \(rN^{-i}=1\), so \(r=N^i\) in \(G\). This proves
the three-way equivalence, including \(q=2\), where \(G\) is trivial.

If \(N^i=N^j\pmod q\), then \(N^{i-j}=1\pmod q\), which is equivalent to
\(h\mid i-j\). Thus all working exponents form exactly one residue class
modulo \(h\).

It remains to justify the bank-wide compatibility criterion. A system

\[
x\equiv a_j\pmod {m_j}
\]

has a solution only if \(a_j\equiv a_k\pmod{\gcd(m_j,m_k)}\) for every pair.
For sufficiency, fix a prime \(\ell\). Among the moduli choose one having
maximal \(\ell\)-adic valuation \(e\), and impose its residue modulo
\(\ell^e\). Pairwise compatibility shows that this residue agrees with
every other imposed residue modulo the smaller relevant power of \(\ell\).
Do this for every prime dividing the moduli. Ordinary CRT combines the
resulting congruences because their prime-power moduli are coprime. The
combined integer solves every original congruence. Applying this generalized
CRT with \(a_j=i_q(r)\) and \(m_j=h_q\) gives exactly (A5). In particular,
separate local orbit membership does not supply a shared exponent unless
these congruences are compatible.

## B. Exact Cohen--Lenstra import boundary

The following is the precise interface imported by the statement.

- Under the hypotheses and notation of Cohen--Lenstra Theorems 6.3 and 7.8,
  condition (6.4) supplies, for each primary prime \(p\mid t\), one shared
  \(p\)-adic exponent \(\ell_p(r)\).
- Theorem 7.8 supplies
  \(\chi(r)=\chi(N)^{\ell_p(r)}\) for every tested character of \(p\)-power
  order. Exponentiation here depends only on the reduction of \(\ell_p(r)\)
  modulo the finite order of \(\chi(N)\).
- Because the same \(\ell_p(r)\) is used for all auxiliary primes with that
  primary support, the resulting finite exponent congruences agree within
  the \(p\)-primary part. The primary parts for distinct \(p\)'s have
  coprime moduli and combine by CRT.
- Cohen--Lenstra Theorem 6.3 is then invoked to conclude that the combined
  exponent can be chosen from the public finite exponent set and satisfies

  \[
  r\equiv N^i\pmod S.
  \]

The last implication is imported, not derived from the abbreviated
hypotheses in V2. Its important logical content is that the exponent is
shared. Allowing an unrelated exponent at each auxiliary prime would remove
the premise that lets the primary pieces combine and would not justify the
congruence modulo \(S\).

## C. Conditional residue accumulator and terminal

Assume all data in Theorem C are valid.

### The \(\tau\ge n\) branch

The input-length convention gives \(N<2^n\). Hence

\[
0<p<N<2^n\le2^\tau.
\]

Both \(p\) and the canonical residue \(b\) lie in \([0,2^\tau)\), and they
are congruent modulo \(2^\tau\). Uniqueness of the canonical representative
therefore gives \(b=p\). Computing \(\gcd(b,N)\) returns \(p\).

Crucially, the algorithm first compares the binary integer \(\tau\) with
\(n\). On this branch it never constructs \(2^\tau\). The valid certificate
itself forces \(b=p<N\), so \(b\) has only \(O(n)\) bits. The comparison and
gcd have polynomial bit complexity even when the numerical value of \(\tau\)
is enormous.

### The \(\tau<n\) branch

Now \(2^\tau\) has at most \(n+1\) bits and is constructed directly. Since
\(M\mid p-1\),

\[
p\equiv b\pmod {2^\tau},
\qquad p\equiv1\pmod M.
\]

The existence of \(p\) proves generalized-CRT compatibility, so these two
congruences determine one class \(s_0\pmod{L_0}\), where
\(L_0=\operatorname{lcm}(2^\tau,M)\). Also \(M\le p-1<N\), so \(M\),
\(2^\tau\), \(b\), and \(L_0\) all have \(O(n)\) bits.

For every \(i\in I\), compute \(a_i=N^i\bmod S\). Negative exponents, if
the public representation permits them, are also computable because
\(\gcd(N,S)=1\). The pair

\[
x\equiv s_0\pmod {L_0},
\qquad x\equiv a_i\pmod S
\]

is compatible exactly when

\[
s_0\equiv a_i\pmod {\gcd(L_0,S)}.
\]

For each compatible pair, generalized CRT gives its canonical residue
\(s_i\pmod L\), with \(L=\operatorname{lcm}(L_0,S)\). By (C5), at least one
index for the factor \(p\) is present. For that index both congruences hold
for \(p\), so it survives and satisfies \(s_i\equiv p\pmod L\).

There is no hidden coprimality problem. The integer \(N\) is odd,
\(M\mid p-1\) and \(M\mid q-1\), and \(S\) is coprime to \(N\). Therefore

\[
\gcd(L,N)=1.
\]

For each retained \(s_i\), compute \(d_i=\gcd(s_i,N)\). A proper value is
already a factor; a value \(N\) can be discarded. For the true residue,
the canonical representative is at most \(p\), so it either gives the
factor immediately or has gcd one and remains available to the terminal.

Use the following named Gao--Feng--Hu--Pan interface: for a balanced
semiprime, a certified residue of a factor modulo a modulus of size at least
\(N^{1/4}\) lets a deterministic known-residue routine recover a proper
factor in bit complexity polynomial in the encoded operands. Calls on false
residues terminate without creating an unverified factor.

The QP slack in (C10) can be removed explicitly. Let \(B\) be the least
power of two at least \(\max\{1,A(n)\}\). Then \(B\le2\max\{1,A(n)\}\),
\(B\) is numerical-QP, and \(BL\ge N^{1/4}\). Because \(N\) is odd,
\(BL\) remains coprime to \(N\). If the true factor has

\[
p=s_i+kL,

\]

then for exactly one \(j\in\{0,\ldots,B-1\}\), namely
\(j\equiv k\pmod B\),

\[
p\equiv s_i+jL\pmod {BL}.

\]

Enumerate these \(B\) refinements and apply the no-slack terminal. Thus one
call in the full enumeration has a certified true residue and returns a
proper factor. Division then returns the other prime.

### Bit complexity

On the nonterminal branch, \(L_0\) has \(O(n)\) bits. By hypothesis \(S\)
and every \(i\) have numerical-QP bit length, so \(L\), \(BL\), modular
powers, gcds, extended-gcd CRT calculations, and all intermediate residues
also have numerical-QP bit length. Binary modular exponentiation uses a
number of modular operations polynomial in the bit length of \(i\).
Integer multiplication, division, gcd, and CRT are polynomial in their
operand lengths.

There are at most \(|I|B=\operatorname{QP}(n)\) terminal refinements. Each
terminal call is polynomial in numerical-QP-sized operands. Finite sums and
products of fixed numerical-QP bounds remain numerical-QP. This proves the
claimed total bit complexity, including enumeration, screening, arithmetic,
and output verification.

Only the divisibility \(M\mid p-1,q-1\) was used. If several certified
common primary orders each divide both group orders, their lcm does also.
No element of exact order \(M\) is required.

## D. Obstruction to a fixed prime bank

Fix the bank before choosing the factors. If \(R>1\), then \(R\) is odd and
\(\gcd(-1,R)=1\). The prime number theorem in arithmetic progressions gives

\[
\pi(2X;R,-1)-\pi(X;R,-1)
\sim \frac{X}{\varphi(R)\log X}.

\]

The right side tends to infinity because \(R\) is fixed. Hence, for every
sufficiently large \(X\), the interval \((X,2X)\) contains at least two
distinct primes in the class \(-1\pmod R\).

If \(R=1\), the congruence is vacuous. The ordinary prime number theorem
instead gives

\[
\pi(2X)-\pi(X)\sim \frac{X}{\log X},

\]

which again tends to infinity. Increasing \(X_0\) if necessary makes the
chosen primes odd. This separately handles an empty odd bank, including a
bank consisting only of \(2\).

Choose two such primes \(u<v\). Since \(X<u<v<2X<2u\), they form a
balanced squarefree semiprime. For each odd \(q\in Q\), the definition of
\(R\) gives

\[
u\equiv v\equiv-1\pmod q,
\qquad N=uv\equiv1\pmod q.

\]

Thus \(\langle N\bmod q\rangle=\{1\}\), whereas \(-1\ne1\pmod q\), so
neither factor is in the orbit. At \(q=2\), the unit group is \(\{1\}\),
and the orbit test carries no information. Taking arbitrarily large \(X\)
gives infinitely many obstructing balanced inputs. The proof uses essentially
that \(Q\), hence \(R\), is fixed before the input is chosen.

## E. Generic independent-residue model

For fixed \(q\) and \(i\), the value \(a_q^i\) is one specified unit. A
uniform \(U_q\) hits it with probability \(1/(q-1)\). Since the variables
\(U_q\) are independent across \(q\), so are the indicators \(I_{q,i}\).

For \(\lambda>0\), Markov's inequality and the exact Bernoulli moment
generating function give

\[
\begin{aligned}
\Pr(K_i\ge k)
&\le e^{-\lambda k}\mathbb E[e^{\lambda K_i}]\\
&=e^{-\lambda k}
  \prod_{q\in Q}
  \left(1+\frac{e^\lambda-1}{q-1}\right),
\end{aligned}

\]

which is (E3). With \(\mu=\sum_q1/(q-1)\), the inequality
\(1+x\le e^x\) gives

\[
\Pr(K_i\ge k)
\le \exp\!\left(-\lambda k+\mu(e^\lambda-1)\right).

\]

For \(k>\mu\), set \(e^\lambda=k/\mu\). Dropping the extra factor
\(e^{-\mu}\le1\) yields \((e\mu/k)^k\). At \(k=\mu\), (E5) is the trivial
bound by a quantity at least one (or follows by a limit). This proves (E5).

Moreover,

\[
P_i^\lambda
=\prod_{q\in Q}q^{\lambda I_{q,i}},

\]

and independence gives

\[
\mathbb E[P_i^\lambda]
=\prod_{q\in Q}
\left(1+\frac{q^\lambda-1}{q-1}\right).

\]

Markov's inequality followed by an infimum over \(\lambda>0\) is exactly
(E7). For \(T\) proposed exponents, the union bound adds at most a factor
\(T\). It needs no independence between different exponents. These are
statements about the declared random model, not uniform claims about hidden
prime residues of all integers.

## F. The primary-prime-2 anchor law

CRT identifies a uniform unit modulo \(N=uv\) with independent uniform
units modulo \(u\) and \(v\). The group modulo \(u\) is cyclic of order
\(m_u=u-1\). The kernel of the power map \(x\mapsto x^E\) on a cyclic group
of order \(m_u\) has size \(\gcd(E,m_u)=g_u\). Therefore

\[
\Pr(a^E=1\bmod u)=\frac{g_u}{u-1},

\]

and similarly at \(v\). Independence gives (F5). The exclusive-or
probability is

\[
\alpha_u(1-\alpha_v)+\alpha_v(1-\alpha_u)
=\alpha_u+\alpha_v-2\alpha_u\alpha_v,

\]

which is (F6). In the exclusive-or event, \(\gcd(a^E-1,N)\) is exactly one
of \(u,v\).

For the sign gate, write a unit modulo \(u\) as \(g^z\), where \(g\)
generates the group. The equation \(x^E=-1\) becomes

\[
Ez\equiv (u-1)/2\pmod {u-1}.

\]

A linear congruence has solutions exactly when
\(g_u\mid(u-1)/2\), and then it has exactly \(g_u\) solutions. The equations
with right sides \(1\) and \(-1\) have disjoint solution sets. Hence the
sign-gate probability is

\[
\frac{g_u(1+\delta_u)}{u-1}\le\frac{2g_u}{u-1},

\]

and likewise at \(v\).

To prove (F9), let \(h=g_u\). Since \(h\mid E\) and \(h\mid u-1\),

\[
0\equiv 2E=uv-1\equiv v-1\pmod h.

\]

Thus \(h\mid\gcd(u-1,v-1)=d\). The same argument gives \(g_v\mid d\),
and subtracting \(u-1\) from \(v-1\) gives \(d\mid v-u\).

If \(v-u\le H\), then \(g_u,g_v\le H\). A union bound over the two local
sign gates gives

\[
\Pr(\text{either sign gate})
\le \frac{2H}{u-1}+\frac{2H}{v-1}.

\]

On a balanced bounded-gap family, \(u,v=2^{n/2+O_H(1)}\), so this is
\(2^{-n/2+O_H(1)}\). Finally, if an additional argument gives
\(g_u=g_v=d\), substitution into (F5) gives (F11). Nothing above implies
that additional equality.

## Finite witness reconstructed from the statement

First,

\[
32987\cdot32993=(32990-3)(32990+3)
=32990^2-9=1088340091.

\]

Also \(182^2=33124>32993\). The following table gives
\(32987\bmod\ell\,/\,32993\bmod\ell\) for every prime \(\ell\le181\):

```text
  2: 1/1      3: 2/2      5: 2/3      7: 3/2     11: 9/4
 13: 6/12    17: 7/13    19: 3/9     23: 5/11    29: 14/20
 31: 3/9     37: 20/26   41: 23/29   43: 6/12    47: 40/46
 53: 21/27   59: 6/12    61: 47/53   67: 23/29   71: 43/49
 73: 64/70   79: 44/50   83: 36/42   89: 57/63   97: 7/13
101: 61/67  103: 27/33  107: 31/37  109: 69/75  113: 104/110
127: 94/100 131: 106/112 137: 107/113 139: 44/50 149: 58/64
151: 69/75  157: 17/23  163: 61/67  167: 88/94  173: 117/123
179: 51/57  181: 45/51
```

Every remainder is nonzero. Trial division therefore certifies that both
displayed factors are prime.

The positive divisors of \(66\) are
\(1,2,3,6,11,22,33,66\). Adding one and retaining primes gives exactly

\[
Q=\{2,3,7,23,67\}.

\]

Their product is

\[
2\cdot3\cdot7\cdot23\cdot67=64722.

\]

It exceeds \(32993\), hence also \(\sqrt{32987\cdot32993}\).

All orbit checks are short enough to reconstruct directly:

\[
\begin{array}{c|c|c|c|l}
q&u\bmod q&v\bmod q&N\bmod q&\langle N\bmod q\rangle\\ \hline
2&1&1&1&\{1\}\\
3&2&2&1&\{1\}\\
7&3&2&6&\{1,6\}\\
23&5&11&9&\{1,9,12,16,6,8,3,4,13,2,18\}\\
67&23&29&64&\{1,64,9,40,14,25,59,24,62,15,22\}.
\end{array}

\]

For \(q=23\) and \(q=67\), the displayed sequences return to \(1\) after
eleven powers and list the whole orbit. Thus both factors are in the orbit
only at \(q=2\). This verifies the finite arithmetic, but it supplies no
unbounded progress theorem and does not repair the explicitly stated
provenance limitation.

## Remaining source boundary

The reconstruction proves only the conditional accumulator and the three
negative model results. A complete Las Vegas algorithm would still need,
for every nonterminal input and after every possible prior history, an
inverse-QP probability of a verified factor or certified enlargement of
\(M\), \(S\), or the known low-bit modulus. A compositeness identity failure
alone need not produce a rational zero divisor. No theorem reconstructed
above supplies this missing source law.
