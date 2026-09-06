# F215 self-audit

## Verdict

Self-audit passes for the frozen proof-only candidate. The negative result
is an exact boundary for the scalar abelian transcript declared in the
statement. The positive results are conditional extraction interfaces, not
constructions of the missing data. No mathematical computation, finite
search, random sampling, or benchmark is used as proof.

## Assumption and quantifier audit

1. The main setup is restricted to balanced distinct odd semiprimes with
   $N\equiv3\pmod4$. It does not claim an all-input factoring result.
2. Complete factorization of $K=(N-1)/2$ is granted. No step silently
   treats the hidden factorization of $N$ as known.
3. The Frobenius theorem quantifies over $d\mid K$. The more general
   conductor statement is only the affine involution
   $z\mapsto\chi(N)z^{-1}$; it does not claim that $\chi(N)=1$.
4. Transcript closure applies only to one-dimensional scalar products and
   adaptivity based on those products. It excludes ordered CRT vectors,
   non-diagonal algebra elements, nonlinear traces, divisor coefficients,
   and Archimedean side information.
5. The $N=527$ witness closes fixed cubic, quartic, and octic labels, not
   every higher-order character. In fact, order-131 characters exist and
   can distinguish the inverse pair if one can evaluate the two local
   values separately.
6. The trace theorem proves separation by the full character family and a
   conditional transition for a numerical-QP separating bank. It does not
   assert that such a bank or coefficient evaluator exists.

## Frobenius and ray-character audit

1. From $d\mid K$ one gets $pq=N\equiv1\pmod d$.
2. Neither hidden prime divides $K$, since $2K\equiv-1$ modulo either
   prime. Thus inversion modulo $d$ is legal.
3. The cyclotomic Artin map sends a rational unramified prime $r$ to
   $\zeta_d\mapsto\zeta_d^r$. This gives
   $\operatorname{Frob}_q=\operatorname{Frob}_p^{-1}$ exactly.
4. Inverse elements generate the same decomposition subgroup and have the
   same order. The proof claims equality of unlabelled cyclotomic residue
   degrees, not equality of all possible nonsymmetric polynomial
   transcripts.
5. A one-dimensional character sends an inverse pair to
   $(z,z^{-1})$. A genus character has $z=z^{-1}$. The global
   character product is one because $N\equiv1\pmod d$.
6. For an additional conductor part, multiplicativity gives
   $\chi(q)=\chi(N)\chi(p)^{-1}$. This public affine involution remains
   unordered.
7. The statement about an arbitrary ideal/ray class pair is explicitly
   conditional on the pair being $C,C^{-1}$. It does not assert that
   every hidden construction automatically yields such a pair.

## Hilbert-symbol audit

1. Bimultiplicativity proves
   $(p,a)_{m,v}(q,a)_{m,v}=(N,a)_{m,v}$ whenever the symbols are
   defined.
2. Global reciprocity supplies a product over places. It does not select
   which rational factor contributed a local value.
3. If $r\mid K$ and $r\nmid m$, then
   $X^m-N$ has the simple root $1\bmod r$. Hensel's lemma therefore
   proves that $N$ is an $m$-th power in $\mathbb Q_r$.
4. No local triviality claim is made when $r\mid m$. Wild corrections can
   be nontrivial, but the product identity remains swap-invariant.
5. The proof does not confuse a Hilbert symbol in $\mathbb Q_r$ with one
   in a field lacking $\mu_m$. The m-th-power conclusion is made in
   $\mathbb Q_r$ itself and persists after any extension where the symbol
   is evaluated.

## Exact-witness audit

1. $17\cdot31=527$, $2\cdot263+1=527$, and
   $17<31<34$.
2. Trial division by $2,3,5,7,11,13$ proves that 263 is prime because
   $\sqrt{263}<17$.
3. The unit group modulo 263 has order $262=2\cdot131$. Thus it has no
   character of order three, and its characters with values in
   $\mu_4$ or $\mu_8$ have image of order at most two.
4. The exact congruences
   $65^2=16\cdot263+17$ and
   $174^2=115\cdot263+31$ put both factors in the quadratic-character
   kernel.
5. For $m=3,4,8$, 263 has order two modulo $m$, so the residue norm at
   every prime above 263 is $263^2$.
6. A rational residue lies in $\mathbb F_{263}$. Since
   $(263^2-1)/m=262(264/m)$, the power-residue Euler criterion gives one.
   The proof explicitly excludes nonrational primary numerators.

## Common-order audit

1. Reduction of $pq-1$ modulo $p-1$ and $q-1$ proves
   $\gcd(N-1,p-1)=\gcd(N-1,q-1)=\gcd(p-1,q-1)$.
2. The opposite mod-four factor classes give
   $v_2(\gcd(p-1,q-1))=1$.
3. With $h=(q-p)/2$, exact modular division gives
   $K\equiv h\pmod{p-1}$ and
   $K\equiv-h\pmod{q-1}$. Since $h$ is odd, each gcd with $K$ is
   half the common gcd.
4. On $17,31$, the common gcd is two. Hence every returning rational
   base has local order one or two. Mixed signs factor; equal signs give no
   strict common-order growth.
5. This is a rational multiplicative-group statement. It does not bound
   orders in arbitrary algebraic tori or nonabelian groups.

## Coefficient-content extraction audit

This was the highest-risk point, and the frozen version uses the exact
conditions needed for the claim.

1. It assumes $\gcd(m,N)=1$. Without this condition, $\Phi_m$ can become
   inseparable and the order of the reduced root can collapse.
2. It assumes congruence in the full rational components
   $A_m/pA_m$ and $A_m/qA_m$, not merely at one selected prime ideal.
   Full-component vanishing is exactly equivalent to divisibility of every
   power-basis coefficient by the rational prime.
3. For $r\nmid m$, $A_m/rA_m$ is a finite product of finite fields and
   the image of $\zeta_m$ has exact order $m$ in every component.
4. If $a\not\equiv b\pmod m$, then
   $\zeta_m^a-\zeta_m^b$ is nonzero in every component and hence a unit
   in the product algebra. This proves that it cannot vanish as a full
   rational component.
5. At $e=a$, every coefficient is divisible by $p$, while not all are
   divisible by $q$. Since $N=pq$, the coefficient-content gcd is
   exactly $p$. The symmetric argument gives $q$.
6. The standard power basis remains a basis modulo every rational prime
   because $\Phi_m$ is monic. No index-of-orders issue is hidden here:
   $A_m$ is defined as $\mathbb Z[\zeta_m]$ itself.
7. The selected-prime-ideal variant was weakened. A selected local zero
   gives norm divisibility, but a no-collision condition at all primes over
   the other rational factor is required. Merely having distinct selected
   values is not claimed sufficient.
8. Complexity includes all $m$ trials and all $\varphi(m)$
   coefficients. With numerical-QP $m,\varphi(m)$, even elementary
   cyclotomic-polynomial construction, reduction, and gcd arithmetic are
   numerical QP. The supplied element has coefficients reduced modulo
   $N$, so its serialized coefficients have $O(n)$ bits.

## Trace and divisor-coefficient audit

1. The symmetric measure
   $\delta_u+\delta_{u^{-1}}$ has Fourier transform
   $\chi(u)+\chi(u)^{-1}$.
2. Fourier inversion on a finite abelian group proves that the complete
   trace vector determines the inversion orbit, including the self-inverse
   case where the measure has multiplicity two.
3. Every divisor of $N$ is a unit modulo $K$. The exact four-divisor
   expansion gives
   $2+\chi(p)+\chi(p)^{-1}$.
4. Ordinary reciprocity supplies only the product
   $\chi(p)\chi(q)=1$. It does not evaluate the sum.
5. The conditional positive boundary charges character construction,
   exact root representation, coefficient evaluation, transcript size,
   decoding, and verification. It contains no hidden claim that the full
   character group is numerical QP.

## Literature and named-method audit

1. Bach--Shallit requires a known multiple of $\Phi_j(p)$ for its
   cyclotomic group-order transition. Factorization of $pq-1$ does not
   supply such a multiple in general.
2. APR and Cohen--Lenstra use cyclotomic/Jacobi-sum identities for
   primality and restrictions on prime divisors. On an already known
   composite, a failed identity is not automatically a proper gcd.
3. These comparisons are scope statements only. The proof does not derive
   a lower bound against all Jacobi-sum or cyclotomic-ring algorithms.

## Required fresh hostile checks

1. Reconstruct the full-component unit proof for
   $\zeta_m^a-\zeta_m^b$, including the $r\nmid m$ condition.
2. Try to find a selected-prime-ideal counterexample to any accidental
   stronger reading of the coefficient-content lemma.
3. Recheck the $K$-torsion gcd formula when the smaller factor is either
   $1$ or $3\bmod4$.
4. Verify the power-residue Euler criterion at every prime over 263 for
   $m=8$.
5. Check that transcript closure never absorbs a nonlinear trace or an
   ordered CRT vector.
6. Reject any interpretation as a general impossibility theorem for higher
   reciprocity or as an unconditional factoring algorithm.
