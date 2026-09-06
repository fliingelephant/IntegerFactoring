# F215 provenance

## Namespace

Before creation, a repository-wide search found no F215 entry or experiment
directory.

## Source question

The beta-two branch grants the complete factorization of

\[
K=\frac{N-1}{2}
\]

for a balanced semiprime $N=pq\equiv3\pmod4$. The question was whether
cubic, quartic, octic, or general higher reciprocity, cyclotomic residue
symbols, local Hilbert symbols, or explicit ray/genus characters supported
on $\operatorname{factor}(K)$ can orient the hidden inverse pair or force a
factor/common-order transition in numerical-QP time.

F215 arose from the elementary congruence

\[
pq\equiv1\pmod d
\qquad(d\mid K),
\]

which makes the two cyclotomic Frobenius elements exact inverses. The
investigation then separated three interfaces:

1. scalar abelian products, which collapse to public values;
2. a coherent non-diagonal element in the full rational cyclotomic CRT
   algebra, which deterministically factors by coefficient content; and
3. nonlinear character traces, which determine the inversion orbit but are
   exact divisor coefficients rather than reciprocity outputs.

## Closest prior routes and material difference

- P15/F09 proves that individually factor-swap-invariant scalar
  higher-residue characters have only diagonal rank. It also notes that a
  chosen cyclotomic orientation can retain more information. F215 is
  materially different because the factorization of $K$ gives the exact
  relation $\operatorname{Frob}_q=\operatorname{Frob}_p^{-1}$ for every
  $d\mid K$, includes decomposition groups, ray/genus characters and
  Hilbert products, gives a new $N=527$ fixed-order witness, and proves an
  exact full-component non-diagonal extraction lemma.
- P165/F187 classifies rational bases returning under a completely factored
  $N-1$ exponent and shows that uniform sampling fails on bounded-gap
  pairs. F215 supplies the exact rational common-order obstruction on
  $N=527$, then tests whether higher reciprocity escapes it. It does not
  extend P165's probability theorem.
- P179/F203 identifies a $\chi_4$-twisted weighted divisor coefficient as
  the exact first beta-two selector. F215's unweighted character trace is a
  different nonlinear Fourier interface. It separates inversion orbits
  conditionally but still lacks a numerical-QP exact coefficient
  evaluator.
- P183/F207 proves that the factorizations of $K$ and a second child leave
  a large inversion torsor, while quadratic/genus data do not orient it.
  F215 treats the nonquadratic abelian mechanisms left open there and
  narrows the surviving object to a non-diagonal lift or trace coefficient.
- P185/F210 shows that odd-local affine invariants of the dyadic sibling
  charts agree. F215 instead studies Artin and Hilbert character data
  attached directly to the fully factored $K$.

The material new point is not a generic ring-invariant test. It is the
exact conjunction of:

1. Frobenius inversion for every $K$-supported cyclotomic field;
2. closure of the declared scalar ray/genus/Hilbert transcript;
3. an explicit balanced $N\equiv3\pmod4$ input on which cubic, quartic,
   and octic labels vanish even when individual local values are granted;
4. an exact rational common-order cap on the same input;
5. a corrected full-component coefficient-content extraction theorem; and
6. a Fourier proof identifying the exact nonlinear divisor coefficient
   that would orient the torsor.

## Correction made before freeze

The initial extraction sketch said that if a cyclotomic element has
different root-of-unity reductions at the two hidden factors, subtracting
one root and taking coefficient content factors $N$. That statement was
ambiguous and too strong if each reduction is known only at one selected
prime ideal. Vanishing at one prime ideal above $p$ need not make every
rational power-basis coefficient divisible by $p$. Also, if a hidden
prime divides the root order, cyclotomic reduction can be inseparable and
orders can collapse.

The frozen theorem repairs both points. It assumes

\[
\gcd(m,N)=1
\]

and congruence in the full rational components

\[
\mathbb Z[\zeta_m]/p\mathbb Z[\zeta_m],
\qquad
\mathbb Z[\zeta_m]/q\mathbb Z[\zeta_m].
\]

Then each algebra is finite etale, $\zeta_m$ has exact order $m$ in
every field component, and distinct powers have unit difference. The
selected-prime-ideal version is retained only with an explicit norm
no-collision hypothesis.

## Primary literature checked

The named-method comparison used the following primary sources.

1. Eric Bach and Jeffrey Shallit, “Factoring with cyclotomic polynomials,”
   *Mathematics of Computation* 52 (1989), 201--219,
   DOI: [10.1090/S0025-5718-1989-0947467-1](https://doi.org/10.1090/S0025-5718-1989-0947467-1).
   Its cyclotomic transition starts from a multiple of a hidden value
   $\Phi_j(p)$; F215 does not infer such a multiple from $pq-1$.
2. Leonard M. Adleman, Carl Pomerance, and Robert S. Rumely, “On
   distinguishing prime numbers from composite numbers,” *Annals of
   Mathematics* 117 (1983), 173--206,
   [journal page](https://annals.math.princeton.edu/1983/117-1/p07).
3. Henri Cohen and Hendrik W. Lenstra Jr., “Primality testing and Jacobi
   sums,” *Mathematics of Computation* 42 (1984), 297--330,
   DOI: [10.1090/S0025-5718-1984-0726006-X](https://doi.org/10.1090/S0025-5718-1984-0726006-X).

These sources establish context and named algorithm hypotheses. The F215
theorems themselves use only elementary cyclotomic Artin theory, character
duality, Hensel's lemma, Hilbert-symbol bimultiplicativity, and explicit
integer arithmetic.

## Mathematical dependencies

1. The cyclotomic Artin formula
   $\operatorname{Frob}_r(\zeta_d)=\zeta_d^r$ for $r\nmid d$.
2. The equality between cyclotomic residue degree and
   $\operatorname{ord}_d(r)$.
3. One-dimensional character multiplicativity.
4. Bimultiplicativity and global reciprocity for Hilbert symbols.
5. Hensel's lemma for a simple root.
6. Separability of $\Phi_m$ modulo primes not dividing $m$.
7. Fourier inversion on a finite abelian group.
8. Cyclicity of the multiplicative group of a finite prime field.

No smoothness, prime distribution, random-character independence,
unproved reciprocity formula, class-number estimate, or hidden order oracle
is assumed.

## Computation and evidence

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, or numerical fit was performed. The $N=527$
certificate is checked by displayed exact integer arithmetic. Public web
lookup was used only to confirm the named primary literature and its
algorithmic scope. Hashing is used only to freeze the packet.

## Ledger policy

No durable registry, proved ledger, failed ledger, progress ledger,
statement ledger, inspiration file, or process-lessons file is edited by
this packet.
