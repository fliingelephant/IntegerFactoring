# F75 fresh hostile re-audit — CRT beam and canonical-residue closure

**Candidate audited:**
experiments/F75_crt_beam_residue_closure_kill/RESULT.md

**Pinned candidate SHA-256:**
9e3333f490c62c68c1aab66f920394e13e4ce51974bbde543be312a5cc30309a

**Verdict: PASS.**

This re-audit was proof-only. I ran no arithmetic script, CAS, search, or
research computation. I checked the symbolic identities and the displayed
finite certificates directly. The corrected candidate now states the exact
scope of its score counterexamples. It proves no beam-width lower bound and
no failed run of a screened factoring algorithm.

## 1. CRT identities and domains — PASS

Let \(1<g<N\) and \(\gcd(g,N)=1\). Multiplication by \(N\) is invertible modulo
\(g\), so there is a unique nonzero residue

\[
1\leq \rho_g\leq g-1,
\qquad
N\rho_g\equiv-1\pmod g.
\]

Consequently

\[
w_g=\frac{1+N\rho_g}{g}
\]

is a positive integer. The bound

\[
1+N\rho_g\leq1+N(g-1)<Ng
\]

gives \(w_g<N\), and \(gw_g\equiv1\pmod N\). Thus \(w_g\) is the canonical
inverse of \(g\), and

\[
gw_g=1+\rho_gN.
\]

If \(g\) is an authorized divisor of a retained P70 product
\(P=1+KN\), then \(KN\equiv-1\pmod g\). Hence \(K\bmod g\), in the least
nonzero range, is exactly \(\rho_g\). This proves the candidate's
\(\rho_g=k(g)\) identity. It does not apply to a bare CRT state without the
required integer-product provenance; the candidate says this.

Now let \(\gcd(b,gN)=1\), and set

\[
t=(\rho_b-\rho_g)g^{-1}\pmod b,
\qquad 0\leq t<b.
\]

The integer \(\rho_g+gt\) has the required residue modulo both \(g\) and
\(b\), and it lies in \([0,gb)\). Coprime CRT uniqueness therefore gives

\[
\rho_{gb}=\rho_g+gt.
\]

Substitution gives

\[
w_{gb}
=\frac{1+N(\rho_g+gt)}{gb}
=\frac{w_g+Nt}{b}.
\]

Both \(w_{gb}\) and \(w_gw_b\) represent \((gb)^{-1}\bmod N\), so their
canonical residues agree. These formulas require coprime extension. They do
not add a repeated copy of a block or an overlapping macroblock. A P70 use
also needs separate occurrence provenance and the required positive-product
bound. The candidate keeps these restrictions explicit.

Finally, because \(g\) is a unit modulo \(N\),

\[
\gcd(g-w_g,N)=\gcd(g(g-w_g),N)=\gcd(g^2-1,N).
\]

If \(g\) is a non-global square root of one, then \(w_g=g\). The difference
gcd is \(N\), but neither \(g-1\) nor \(g+1\) is zero modulo \(N\), and each
has a nontrivial gcd with \(N\). Thus the two sign screens remain mandatory.

## 2. Score reversals and their exact scope — PASS

The four displayed reversals at \(N=55\) are internally exact.

- Canonical inverse: \(w_8=7<w_7=8\), but after the common coprime extension
  by \(3\), \(w_{24}=39>w_{21}=21\).
- Quotient: \(\rho_{13}=4<\rho_{23}=5\), but after extension by \(2\),
  \(\rho_{26}=17>\rho_{46}=5\).
- Distance: \(|7-8|=1<|17-13|=4\), but after extension by \(2\), the
  distances are \(10>0\).
- Refinement gain: \(17\) does not overlap \(28\), while the extended inverse
  \(24\) splits \(28\) through gcd \(4\). In the reverse example, \(13\)
  splits \(26\), while the extended inverse \(41\) has gcd \(1\) with \(26\).

These are counterexamples to extension-monotone ordering by the current value
of each named scalar. That is all they prove. In particular, they do not
prove any of the following:

- a superpolynomial Pareto frontier;
- failure of every polynomial-width beam;
- failure of the proposed four-beam combination;
- failure of an enriched state or another score; or
- failure of a factorer that applies every direct gcd screen before pruning.

The examples supply arithmetic CRT states and pairwise-coprime extensions;
they do not supply retained-relation provenance for a complete P70 run. The
candidate does not claim such provenance or an operational failed run. Its
correct conclusion is therefore only that the displayed current scalar value
is not, by itself, an exact extension-dominance certificate. The corrected
scope paragraphs state this clearly.

## 3. Canonical-residue closure — PASS

For blocks whose residues generate \(H\), every selected modular word

\[
c=\left[\prod_jq_j^{e_j}\right]_N
\]

and its inverse \(w=[c^{-1}]_N\) remain in \(H\). Hence adding \(c,w\) does
not enlarge the residue subgroup. If the raw positive word is an authorized
P70 product below \(N\), the operation reduces to ordinary feedback. If the
word is reduced modulo \(N\), uses negative exponents, or exceeds occurrence
capacities, it is a genuinely different source operation and P70's integer
quotient identity does not follow.

The possible gain is representation-level. Factoring \(c\) and \(w\) into a
gcd-free block presentation can expose individual unit blocks outside \(H\),
although their products remain in \(H\). This is consistent with P78 and is
not residue-subgroup expansion by \(c,w\) themselves.

For one supplied exponent vector, modular exponentiation, canonical
inversion, gcd screens, and gcd-free refinement have polynomial bit cost.
Enumerating fixed support over polynomial-size block and exponent menus is
also polynomial in the represented state size. Dense exhaustive enumeration
is exponential. A capped beam or random dense sample therefore still needs a
separate success theorem.

## 4. The \(N=4033\) certificates — PASS

The fixed refined state uses

\[
4033=37\cdot109,
\qquad H_1=\langle2,5\rangle.
\]

For the P78 word,

\[
5\cdot2^{13}=40960=10\cdot4033+630,
\]

and

\[
630\cdot3220=2028600=1+503\cdot4033.
\]

Moreover,

\[
630-1=629=17\cdot37,
\qquad
630-3220=-2590=-70\cdot37.
\]

The cofactors \(17\) and \(70\) are coprime to \(109\), so both displayed
gcds with \(4033\) are exactly \(37\). Canonical reduction therefore makes
this known subgroup word a usable representative even though its raw
positive value exceeds \(N\).

The smaller literal-menu certificate is also exact. Since
\(2^{11}<4033<2^{12}\), the stated bit length is \(n=12\), and the exponents
\(2,8\) occur in the proposed menu. They give

\[
5^2 2^8=6400=4033+2367,
\]

\[
2367\cdot443=1048581=1+260\cdot4033.
\]

Also,

\[
2367+1=2368=64\cdot37,
\qquad
2367-443=1924=52\cdot37.
\]

Both cofactors are coprime to \(109\), so the two gcds are exactly \(37\).
The sign screen already succeeds; inversion is not needed for this fixed
candidate. The raw word \(6400>N\), so this is a real source-operation
difference from the old positive whole-block box.

## 5. Final verdict

The candidate proves four narrow results:

1. Coprime CRT composition computes canonical inverse states exactly.
2. The four proposed current-value rankings are not extension-monotone scalar
   dominance certificates.
3. Canonical-residue closure changes the integer source but not the residue
   subgroup.
4. On P78's already reached \(N=4033\) refined state, a fixed-support word
   from the stated exponent menu gives a factor.

It does not prove how to reach that refined state, how to select a useful
word on every input, a polynomial beam-width guarantee, an inverse-polynomial
success law, or a factoring algorithm. Canonical reduction removes the
finite positive-box obstruction only after a suitable word is selected. With
these disclaimers, no correction is required.
