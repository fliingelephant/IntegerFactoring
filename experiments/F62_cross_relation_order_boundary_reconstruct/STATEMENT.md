# Proof-blind reconstruction statement — exact order and HSP boundary

Reconstruct or refute every claim below. Work from this file only. Do not read
the candidate proof, its audits, `PROVED.md`, `FAILED.md`, or
`notes/Progress.md`.

## Setup

Let $N$ be odd. Let $q_1,\ldots,q_s$ be public units modulo $N$, and define

\[
\Phi_N:\mathbb Z^s\longrightarrow (\mathbb Z/N\mathbb Z)^\times,
\qquad
v\longmapsto \prod_{j=1}^s q_j^{v_j}.
\]

Let $\Lambda_N=\ker\Phi_N$. A finite source consists of indexed relation
occurrences with exponent rows $\lambda_i\in\Lambda_N$. Equal rows remain
separate occurrences. Selecting occurrences with coefficients
$c_i\in\{0,1\}$ gives total exponent $E=\sum_i c_i\lambda_i$. A legal
whole-block divisor has exponent vector $v$ with $0\le v\le E$ and integer
magnitude $1<q^v<N$. Its complementary endpoint is $q^{E-v}$.

## Claims to reconstruct

1. The selected endpoints are inverses modulo $N$. They are equal modulo $N$
   exactly when $2v\in\Lambda_N$. A non-global self-inverse unit gives proper
   factors through both $\gcd(q^v-1,N)$ and $\gcd(q^v+1,N)$. This is only a
   sufficient subtarget: the full direct screen can succeed even when
   $2v\notin\Lambda_N$.

2. Let $L_0=\langle\lambda_1,\ldots,\lambda_m\rangle_{\mathbb Z}$. The exact
   modular residue image of the old square-relation decoder is

   \[
   R_{\rm old}
   =\{\Phi_N(v):v\in\mathbb Z^s,\ 2v\in L_0\}.
   \]

   This is a residue-image statement. It does not supply a nonnegative
   representative in the finite legal box or an integer below $N$.

3. In the quotient $Q_0=\mathbb Z^s/L_0$ with
   $K=\Lambda_N/L_0$, a new abstract involution in the generated residue
   group is represented by a class $x$ with $x\notin K$ and $2x\in K$.
   Turning it into an F62 state still needs a finite legal representative and
   a non-global residue outside the old image.

4. For one generator $a$ of exact order $r$ modulo $N$, the least positive
   exponent $e$ with $a^{2e}=1$ and $a^e\ne1$ exists exactly when $r$ is even,
   and then equals $r/2$. A total least-answer oracle that returns `NONE` for
   odd order is Turing-equivalent to exact modular order finding by one extra
   query on $-a$. A weaker oracle that returns any factoring-useful power is
   not claimed equivalent. Full recovery of $\Lambda_N$ contains exact order
   finding because for one generator $\Lambda_N=r\mathbb Z$.

5. If a basis of $\Lambda_N$ is supplied, Smith normal form computes the
   finite generated group and an $\mathbb F_2$-basis of its 2-torsion in time
   polynomial in the complete input and output encodings. Screening at most
   $s$ resulting basis residues finds a non-global involution whenever the
   generated subgroup contains one. Signed exponent representatives are used
   only for modular products, not as positive legal divisors.

6. Output equality for $\Phi_N$ is exactly coset equality modulo
   $\Lambda_N$. This is the algebraic hidden-subgroup identity behind Shor's
   order finding. It is not by itself an efficient quantum algorithm on the
   infinite domain $\mathbb Z^s$; finite-domain truncation, precision,
   circuits, and success analysis remain separate requirements.

## Finite claims to verify

- At $N=65$, the relations $66=2\cdot3\cdot11$ and
  $651=3\cdot7\cdot31$ have independent parity rows, but the cross choice
  $g=2\cdot7=14$ is a non-global square root of one and factors $65$. The
  claim compares the selected blocks $2$ and $7$ only; other blocks can also
  have useful half-order residues.

- At $N=187$, the one relation $188=2^2\cdot47$ has legal proper products
  $2,4,47,94$, none of which passes either direct screen. Yet $2$ has order
  $40$ modulo $187$, and $2^{20}$ is a non-global involution. Thus an
  unbounded subgroup can contain useful order data absent from the finite
  one-copy source box.

- For every odd $t\ge3$, put $G=2^t$,
  $N=(G^2-1)/3$, and $B=(N+1)/2$. With fewer than $t$ indexed copies of the
  relation $2B=N+1$, no legal divisor below $N$ is self-inverse. With $t$
  copies, $G<N$, $G^2=1+3N$, and $G$ is a non-global involution. Every old
  parity-decoder relation remains global. Also $\operatorname{ord}_N(2)=2t$
  and $t=\Theta(\log N)$. This is a lower bound on total occurrence
  multiplicity for the self-inverse subtarget, not on support and not on the
  broader direct screen.

## Required conclusion and scope

Decide whether the exact structural claims hold. Explain why they do or give
a counterexample. Keep finite occurrence capacities, integer magnitude,
prime-power behavior, and the distinction between direct separators and
self-inverse states explicit. Do not claim an all-input classical selector or
factoring algorithm.
