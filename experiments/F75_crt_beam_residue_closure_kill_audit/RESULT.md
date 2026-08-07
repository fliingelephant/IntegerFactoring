# F75 hostile audit — CRT beam and canonical-residue closure

**Candidate audited:**
`experiments/F75_crt_beam_residue_closure_kill/RESULT.md`

**Verified candidate SHA-256:**
`b8133164023e6cf219eabbd8baedcf0b0d75cefcf0b80ab5ba2511329376ee65`

**Verdict: PASS, with a strict scope clarification.**

The CRT identities, their coprimality restrictions, all four (N=55)
examples, the subgroup/representation distinction, and both (N=4033)
certificates are correct.

The finite (N=55) examples prove only that the displayed scalar score
orders are not preserved by a common CRT extension. They do not prove that
all polynomial-width beams fail. They do not even exhibit a failed run of a
factorer that applies the mandatory gcd screens before extension: several of
the displayed prefixes or extensions already expose a factor. The
candidate's final all-input disclaimer is therefore essential. The phrase
"invalidate exact dynamic-programming pruning" is valid only for a dominance
rule based solely on the current value of the named score. It is not a beam
lower bound.

No research computation was used. I checked the symbolic identities directly.
I also used a transient exact-integer script to recompute the finite tables,
gcds, modular powers, and the 41 legal positive products in the stated P78
occurrence box. This was arithmetic verification of declared finite
certificates, not a search experiment.

## 1. CRT state and domain restrictions — PASS

Let (1<g<N) and (gcd(g,N)=1). The congruence

\[
N\rho_g\equiv-1\pmod g
\]

has one nonzero residue modulo (g). Its representative satisfies
(1\leq\rho_g\leq g-1). Hence

\[
w_g=\frac{1+N\rho_g}{g}
\]

is a positive integer. Moreover,

\[
1+N\rho_g\leq 1+N(g-1)<Ng,
\]

so (w_g<N). The congruence (gw_g\equiv1\pmod N) then proves that
(w_g) is the canonical inverse.

If (g\mid P=1+KN), then (KN\equiv-1\pmod g). Therefore (K\bmod g)
is the same nonzero least residue as rho_g. This verifies

\[
\rho_g=k(g).
\]

This equality applies only when (g) is an authorized divisor of the
retained integer product. A bare CRT state does not prove that authorization.
The candidate states this restriction.

Now assume (gcd(b,gN)=1), and put

\[
t=(\rho_b-\rho_g)g^{-1}\pmod b,
\qquad 0\leq t<b.
\]

Then rho_g + gt has the required residues modulo both g and b.
It lies in ([0,gb)), so uniqueness in the coprime CRT gives

\[
\rho_{gb}=\rho_g+gt.
\]

Substitution gives

\[
w_{gb}
=\frac{1+N(\rho_g+gt)}{gb}
=\frac{w_g+Nt}{b}.
\]

Both (w_{gb}) and (w_gw_b) are canonical representatives of
((gb)^{-1}\pmod N), so

\[
w_{gb}=[w_gw_b]_N.
\]

The condition (gcd(g,b)=1) is necessary for this update. It does not add a
second copy of a block already in (g), and it does not accept an overlapping
macroblock. Encoding a whole power as one new atom is different from applying
this CRT formula repeatedly to the same block. The candidate keeps these
cases separate.

Finally, multiplication by the unit (g) gives

\[
\gcd(g-w_g,N)=\gcd(g^2-1,N).
\]

If (g) is a non-global root of one, then (w_g=g). The difference gcd is
(N), while both sign gcds are proper. The candidate is therefore correct
that the sign screens cannot be removed.

## 2. Every (N=55) table — arithmetic PASS

All stated block sets are pairwise coprime. All prefixes are units, and every
extension is below (55).

### 2.1 Canonical-inverse score

The exact states are

\[
\begin{array}{c|cc|cc}
g&\rho_g&w_g&\rho_{3g}&w_{3g}\\ \hline
8&1&7&17&39\\
7&1&8&8&21.
\end{array}
\]

Thus (7<8) before extension, but (39>21) after extension. The score order
reverses.

The direct screens also give

\[
\gcd(24+1,55)=5,
\qquad
\gcd(21-1,55)=5,
\qquad
\gcd(21+1,55)=11.
\]

Thus both extensions terminate a correctly screened factorer. This table is
an order reversal, not a failed factoring beam.

### 2.2 Quotient score

The exact states are

\[
\begin{array}{c|cc|cc}
g&\rho_g&w_g&\rho_{2g}&w_{2g}\\ \hline
13&4&17&17&36\\
23&5&12&5&6.
\end{array}
\]

Thus (4<5), but (17>5). The quotient order reverses.

Here an earlier screen already succeeds:

\[
\gcd(23-1,55)=11.
\]

Both extensions also succeed:

\[
\gcd(26-1,55)=5,
\qquad
\gcd(46-1,55)=5.
\]

Therefore this table also cannot be used as an operational failure of a beam
that screens candidates first.

### 2.3 Distance score

The exact states are

\[
\begin{array}{c|cc|c}
g&w_g&|g-w_g|&|2g-w_{2g}|\\ \hline
7&8&1&10\\
17&13&4&0.
\end{array}
\]

The distance order reverses. The candidate correctly discloses that (14)
already factors (55). The other extension also factors:

\[
\gcd(14+1,55)=5,
\qquad
\gcd(34-1,55)=11,
\qquad
\gcd(34+1,55)=5.
\]

### 2.4 Refinement gain

For blocks ({13,3,28}), the inverses are

\[
13^{-1}=17,
\qquad
39^{-1}=24
\pmod {55}.
\]

Hence

\[
\gcd(17,28)=1,
\qquad
\gcd(24,28)=4.
\]

A proper overlap appears. But the same extension already gives

\[
\gcd(39+1,55)=5,
\qquad
\gcd(39-24,55)=5.
\]

For blocks ({17,3,26}), the inverses are

\[
17^{-1}=13,
\qquad
51^{-1}=41
\pmod {55}.
\]

Thus

\[
\gcd(13,26)=13,
\qquad
\gcd(41,26)=1.
\]

The proper overlap disappears. Again the extension already factors:

\[
\gcd(51-1,55)=5.
\]

The overlap statistic is therefore nonmonotone as claimed. These two paths
do not show that refinement-aware search loses a factor.

## 3. Exact conclusion supported by the reversals

For each displayed scalar score (s), the examples refute a dominance rule
of the form

\[
s(g_1)<s(g_2)
\quad\Longrightarrow\quad
s(g_1b)\leq s(g_2b)
\]

for every common legal coprime extension (b). The refinement examples also
show that zero current overlap is not a zero upper bound on later overlap.

Nothing finite here proves one of the following stronger statements:

- every polynomial-width beam fails;
- four simultaneous beams fail;
- the Pareto frontier is superpolynomial;
- no enriched state admits safe pruning; or
- a beam cannot have an inverse-polynomial success law for a different
  reason.

The candidate does not assert these stronger statements. It says that the
needed success theorem is absent. That is the correct boundary. Any promoted
statement should use "not extension-monotone" instead of an unqualified
claim that beam pruning is unsafe.

## 4. Canonical-residue closure — PASS

Let

\[
H=\langle q_1,\ldots,q_m\rangle
\subseteq(\mathbb Z/N\mathbb Z)^\times.
\]

For any public exponent vector, both

\[
c=\left[\prod_jq_j^{e_j}\right]_N
\quad\text{and}\quad
w=[c^{-1}]_N
\]

belong to (H). Thus

\[
\langle H,c,w\rangle=H.
\]

There is no residue-subgroup expansion. The operation change is the choice of
new canonical integer representatives. If a canonical integer factors as a
product of gcd-free blocks, the residues of the individual factors need not
belong to (H), although their product does. This is the same
representation-level effect used in P78.

For a selected exponent vector, modular exponentiation, inversion, gcd
screens, and gcd-free refinement have polynomial bit cost. A fixed support
over polynomially many exponent choices also has polynomial size. This says
nothing about the density of successful words. Dense exhaustive search is
still exponential.

Canonical reduction removes the positive-product and occurrence-box
restriction for a word that the algorithm selects. It does not solve the
word-selection problem. It also does not turn a CRT triple into valid P70
provenance.

## 5. Both (N=4033) certificates — PASS

The factorization is

\[
4033=37\cdot109.
\]

P78's refined state satisfies (H_1=\langle2,5\rangle). For the first word,

\[
5\cdot2^{13}=40960=10\cdot4033+630.
\]

Thus (c=630). Its canonical inverse is (w=3220), because

\[
630\cdot3220=2028600=1+503\cdot4033.
\]

The two claimed gcds are

\[
\gcd(630-1,4033)=37,
\qquad
\gcd(630-3220,4033)=37.
\]

The raw product (40960) is above (N). The old positive representative rule
therefore cannot emit this (630) through that word.

For the second word, (n=\lceil\log_2 4033\rceil=12). Both exponents (2)
and (8) occur literally in the proposed set ({1,\ldots,n}), and they
also occur in its power-of-two part. Direct arithmetic gives

\[
5^2 2^8=6400=4033+2367.
\]

Thus (c'=2367). Its canonical inverse is (w'=443), since

\[
2367\cdot443=1048581=1+260\cdot4033.
\]

The factor certificates are

\[
\gcd(2367+1,4033)=37,
\qquad
\gcd(2367-443,4033)=37.
\]

The first gcd shows that inversion is not needed for this candidate. The
canonical residue and its mandatory sign screen already factor (N). The
candidate says that it factors immediately, so this is not a contradiction.

The literal lcm part of the same exponent menu contains (2520), because

\[
2520=\operatorname{lcm}(1,\ldots,10).
\]

There is also a support-one hit:

\[
5^{2520}\bmod4033=3442,
\qquad
\gcd(3442-1,4033)=37.
\]

Therefore the support-two certificate is not minimal in support within the
full literal menu. This strengthens the fixed-state success and does not
weaken it. No minimality claim appears in the candidate.

As a check on earlier direct screens, the P78 feedback endpoints
(g=2048,w=3905) pass all of their stated immediate screens before the
refinement that exposes (5). I also enumerated the 41 integers (1<g<4033)
in P78's stated positive whole-block occurrence box after refinement. None
has a proper sign gcd or difference gcd. This finite check does not rule out
other decoders or later feedback. It confirms that the two displayed raw
words, (40960) and (6400), represent a real source-operation change rather
than an already legal positive representative.

## 6. Final scope

The audited result proves four narrow facts:

1. CRT bookkeeping exactly composes canonical inverse states under coprime
   extension.
2. The proposed scalar rankings are not extension-monotone, so their current
   values alone are not exact dominance certificates.
3. Canonical-residue closure changes the integer source without enlarging the
   residue subgroup.
4. On the fixed post-refinement (N=4033) state, a literal fixed-support word
   from the proposed menu gives a factor.

It does not prove a selector theorem, a beam-width lower bound, a rule for
reaching the P78 state, an inverse-polynomial success probability, or a
factoring algorithm.
