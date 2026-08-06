# Verdict: RECONSTRUCTED

The claim follows from a rigid classification of automorphisms of the nodal ring over a field, applied separately modulo (p) and modulo (q). The proof below is symbolic; it uses no computational experiment.

## 1. The node over a field

Let

\[
B_F=F[K,X]/(KX)
\]

for an arbitrary field (F), including (F=\mathbf F_2). Its two minimal prime ideals are

\[
P_K=(K),\qquad P_X=(X).
\]

Indeed, ((KX)=(K)\cap(X)) in (F[K,X]), and both quotients are polynomial rings over (F). Every (F)-algebra automorphism (phi) of (B_F) therefore permutes (P_K,P_X). Consequently it fixes their sum

\[
\mathfrak m=P_K+P_X=(K,X).
\]

There are only two possibilities.

If (phi) preserves both minimal primes, then

\[
(phi(K))=(K),\qquad (\phi(X))=(X).
\]

Every element of ((K)) has the form (Kf(K)). If ((Kf(K))=(K)), then (K=Kf(K)g(K)) for some (g(K)\in F[K]); cancellation in the domain (F[K]) gives (f(K)g(K)=1). Thus (f) is a nonzero scalar. The same argument applies to (X). Hence

\[
\phi(K)=aK,\qquad \phi(X)=dX,qquad a,d\in F^\times.
\]

If (phi) swaps the two minimal primes, the identical generator argument gives

\[
\phi(K)=bX,\qquad \phi(X)=cK,qquad b,c\in F^\times.
\]

This is an exact classification, not merely a first-order statement. In particular, terms such as (K^2) or (X^2) cannot occur in a field-node automorphism. Nothing in the argument uses odd characteristic.

## 2. CRT and the intrinsic first jet

Now let (N=pq) for distinct primes and (R=\mathbf Z/N\mathbf Z). CRT gives

\[
R\simeq \mathbf F_p\times\mathbf F_q,
\qquad
A_R\simeq B_{\mathbf F_p}\times B_{\mathbf F_q}.
\]

An (R)-algebra automorphism fixes every element of (R), hence fixes the two central CRT idempotents. It therefore cannot exchange the (p)- and (q)-components and restricts to automorphisms

\[
\Phi_p:B_{\mathbf F_p}\to B_{\mathbf F_p},
\qquad
\Phi_q:B_{\mathbf F_q}\to B_{\mathbf F_q}.
\]

By the field-node classification, each restriction either preserves or swaps the two axes. Also, each fixes its local ideal ((K,X)). Therefore the global ideal

\[
I=(K,X)\subset A_R
\]

is fixed by every (R)-algebra automorphism.

The quotient

\[
I/I^2=R\bar K\oplus R\bar X
\]

is intrinsically a free rank-two (R)-module with the basis supplied by the named coordinates. Since (Phi(I)=I), (Phi) induces an (R)-linear automorphism on (I/I^2). Define its first-jet matrix by

\[
\Phi(K)\equiv aK+bX,\qquad
\Phi(X)\equiv cK+dX\pmod {I^2},
\qquad
J(\Phi)=
\begin{pmatrix}
a&c\\
b&d
\end{pmatrix}.
\]

The columns here are the coefficient vectors of (Phi(K)) and (Phi(X)). This definition is independent of any polynomial representative in (A_R).

Suppose, for definiteness, that the (p)-orientation preserves the axes and the (q)-orientation swaps them. Under the CRT identification, the four entries have the form

\[
a=(a_p,0),\quad d=(d_p,0),\quad
b=(0,b_q),\quad c=(0,c_q),
\]

where all displayed field scalars are nonzero. Thus every entry is a nonzero zero divisor. If (widetilde a\in\mathbf Z) is any lift of (a), then

\[
\gcd(\widetilde a,N)=q,
\]

and the entries supported on the (q)-component yield (p). The opposite mismatch reverses the roles. Thus differing orientations reveal a proper factor by taking the gcd of a jet entry with (N).

Conversely, if no one of the four gcds is strictly between (1) and (N), the orientations cannot differ. If both local orientations preserve axes, then

\[
a,d\in R^\times,\qquad b=c=0,
\]

and the exact local classifications recombine to give

\[
\Phi(K)=aK,\qquad \Phi(X)=dX.
\]

If both swap axes, then

\[
b,c\in R^\times,\qquad a=d=0,
\]

and

\[
\Phi(K)=bX,\qquad \Phi(X)=cK.
\]

The coefficients are global units because both of their field components are nonzero. This proves the stated dichotomy and also rules out hidden nonlinear terms in the synchronized case.

Using a different integer representative of a jet entry cannot affect the extractor, since

\[
\gcd(r+tN,N)=\gcd(r,N).
\]

The CRT idempotents are used only in the proof; the extraction algorithm neither knows nor constructs them.

## 3. Point action and arbitrary adaptive compositions

An (R)-point of (A_R) is an evaluation map determined by a pair

\[
(k,x)\in\Omega_N=\{(k,x)\in R^2:kx=0\}.
\]

A coordinate-ring automorphism acts contravariantly on these points by precomposition. With one conventional direction, its coordinate formula is

\[
T_\Phi(k,x)=\bigl(\Phi(K)(k,x),\Phi(X)(k,x)\bigr).
\]

Choosing the inverse convention replaces (Phi) by (Phi^{-1}) and changes none of the conclusions: inverse local orientations are still preserve/swap in the same sense.

For a synchronized automorphism, (T_\Phi) is exactly one of

\[
(k,x)\longmapsto(uk,vx),
\qquad
(k,x)\longmapsto(ux,vk),
\qquad u,v\in R^\times.
\]

It consequently preserves

\[
\mathcal A_N=
(R^\times\times\{0\})\;\dot\cup\;
(\{0\}\times R^\times)\;\dot\cup\;
\{(0,0)\}.
\]

Consider any finite realized run, with random and adaptive choices allowed. Before applying each explicitly represented move, evaluate its jet and take the four gcds. At a mismatched move this produces (p) or (q). On a run where no move produces a proper factor, every move is synchronized, so induction keeps every state that started in (mathcal A_N) inside (mathcal A_N). Random mixtures, history dependence, random stopping times, and arbitrary composition order do not change this pathwise dichotomy.

## 4. Counting and total variation

Modulo a prime (ell), the equation (kx=0) describes two axes with their origins identified, so

\[
|\Omega_\ell|=2\ell-1.
\]

CRT acts componentwise on the equation, hence

\[
|\Omega_N|=(2p-1)(2q-1).
\]

Moreover

\[
|\mathcal A_N|=2|R^\times|+1
=2(p-1)(q-1)+1.
\]

It follows that

\[
|\Omega_N\setminus\mathcal A_N|
=(2p-1)(2q-1)-\bigl(2(p-1)(q-1)+1\bigr)
=2N-2.
\]

For the uniform law (U_N) on (Omega_N), write

\[
\rho_N=U_N(\Omega_N\setminus\mathcal A_N)
=\frac{2N-2}{(2p-1)(2q-1)}.
\]

The strict inequality is

\[
\rho_N-\frac12
=\frac{2p+2q-5}{2(2p-1)(2q-1)}>0.
\]

This includes the smallest characteristic-two case, ({p,q}=\{2,3\}). If a law (mu) is supported on (mathcal A_N), taking the event (E=\Omega_N\setminus\mathcal A_N) in the variational definition gives

\[
d_{\mathrm{TV}}(\mu,U_N)
\ge |\mu(E)-U_N(E)|
=\rho_N>\frac12.
\]

Thus the obstruction is stronger than a support mismatch: it gives the claimed strict TV gap.

## 5. Intrinsic circuit computation

Suppose (Phi(K)) and (Phi(X)) are supplied by division-free straight-line circuits over (R), using only (+,-,\times). Evaluate each circuit directly in

\[
A_R/I^2\simeq R\oplus R\bar K\oplus R\bar X.
\]

Represent an element by a triple ((r,a,b)), meaning (r+a\bar K+b\bar X). The gate operations are

\[
(r,a,b)+(s,c,d)=(r+s,a+c,b+d),
\]

\[
(r,a,b)(s,c,d)
=(rs,\;rc+as,\;rd+bs),
\]

with negation componentwise. Initialize an (R)-constant (r) as ((r,0,0)), (K) as ((0,1,0)), and (X) as ((0,0,1)). The square-zero relations discard all higher-degree terms automatically; no symbolic expansion or choice of a representative polynomial is involved.

Each circuit gate causes only a constant number of arithmetic operations modulo (N). For total encoded circuit length (s), including the bit strings for all (R)-constants, the bit complexity is polynomial in (s+\log N). Reading the two linear-coordinate pairs gives (a,b,c,d), and four Euclidean gcd computations remain polynomial in (log N). This establishes the promised intrinsic polynomial-time extraction.

For a purported polynomial-time uniform sampler or factoring reduction, each realized move must therefore have a division-free circuit of encoded size (operatorname{poly}(\log N)); every constant must be given by an ordinary (O(\log N))-bit residue representative (or, equivalently, the complete encoding size must charge its bits). A constant-size token that names a hidden or exponentially costly map is not such an encoding. A different succinct representation is usable only if it exposes the same truncated-quotient evaluation in polynomial time; otherwise it is a black-box extension of the model.

## 6. Consequence for an all-input automorphism-only sampler

Monitor an alleged sampler by computing every realized move's jet before applying it. Let (F) be the event that some jet gcd is a proper factor. For any run started in (mathcal A_N),

\[
\{\text{terminal output}\notin\mathcal A_N\}\subseteq F.
\]

If the terminal law were exactly uniform on (Omega_N), then

\[
\Pr(F)\ge\rho_N>\frac12.
\]

The monitor would therefore factor (N) with probability greater than (1/2) in polynomial time under the circuit-size premise. Repetition amplifies this probability. More generally, if the output is within (\varepsilon) TV of uniform, then (Pr(F)\ge\rho_N-\varepsilon).

This is an unconditional dichotomy, not an assumption that factoring is hard: an exact sampler may factor (N), but it cannot use explicit automorphisms to evade factoring. If it promises never to expose a factor, its output is supported on (mathcal A_N) and remains more than (1/2) from uniform. Any proposal claimed to work on all input moduli must in particular work on the distinct-semiprime subfamily, so this subfamily suffices to refute an all-input, nonfactoring, automorphism-only proposal in the stated exact model.

## 7. Exact scope and excluded extensions

The conclusion is deliberately limited to the following model. These changes are not covered:

- **Endomorphisms.** Invertibility is essential. For example (K\mapsto K^2, X\mapsto X) is an endomorphism with zero/degenerate first jet, not one of the classified automorphisms.
- **Finite-set-only permutations.** An arbitrary permutation of the finite set (Omega_N) need not arise contravariantly from an (R)-algebra automorphism of (A_R). Such permutations have no constrained algebraic jet.
- **Auxiliary or lifted kernels.** Automorphisms of a larger ring, extra-coordinate Markov kernels, and projections back to (Omega_N) are different mechanisms; the two-axis classification need not control them.
- **Branch-dependent or black-box maps.** A piecewise transformation need not be one global algebra automorphism. A hidden map, even if advertised as an automorphism, does not support the polynomial-time jet reduction unless its realized circuit or an equivalent jet-evaluation interface is exposed.
- **Division or rational circuits.** The stated evaluation proof is for total polynomial operations. Division by zero divisors is not a ring operation, and branch-dependent rational formulas can fail to define one global automorphism. Even certified-unit rational extensions require extra semantics and are outside this exact claim.
- **Nontrivial warm starts.** The pathwise invariance statement starts in (mathcal A_N). This is not a loophole that hides useful mass: if ((k,x)\in\Omega_N\setminus\mathcal A_N), at least one of (k,x) is a nonzero zero divisor, so (gcd(k,N)) or (gcd(x,N)) immediately reveals (p) or (q). A warm start outside (mathcal A_N) is allowed only by crediting this already readable factoring probability.
- **Prime powers or other nonsquarefree bases.** The proof uses the reduced decomposition into two fields. It does not claim the same global rigidity over (\mathbf Z/p^a\mathbf Z). Indeed, over (\mathbf Z/p^2\mathbf Z), (K\mapsto K+pK^2, X\mapsto X) has inverse (K\mapsto K-pK^2, X\mapsto X), showing directly that nilpotent coefficients permit nonlinear automorphisms with identity first jet.

## 8. Counterexample audit

- **Characteristic (2):** no counterexample. The minimal-prime and principal-generator proof is characteristic-free, and the TV numerator (2p+2q-5) remains positive when one prime is (2).
- **Quotient representatives:** no counterexample. The jet lives in the canonical module (I/I^2), and gcds are invariant under changing an integer lift by a multiple of (N).
- **CRT contravariance:** no counterexample. CRT decomposes the coefficient ring and its algebra covariantly; only the induced action on points is contravariant. Replacing a coordinate-ring map by its inverse preserves the local orientation type and the synchronized invariance of (mathcal A_N).
- **Nonlinear terms:** no counterexample for automorphisms over a distinct semiprime. Equality of the image principal ideals forces scalar generators on each field component. Nonlinear examples appear precisely after weakening to endomorphisms or nonsquarefree coefficient rings.
- **Adaptive mixtures:** no counterexample. The argument is per realized move and hence pathwise; no independence or fixed distribution over moves is assumed.
- **Count and TV inequality:** direct CRT counting gives complement size (2N-2), and the exact positive difference from (1/2) is ((2p+2q-5)/(2(2p-1)(2q-1))).

No counterexample remains within the exact stated model.
