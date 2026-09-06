# F227 V2 hostile re-audit

## Authentication

I authenticated all five frozen V2 files before reading any packet content.

- `V2_STATEMENT.md`:
  `dd905a434ed69fe0fcca5b034666e46444381cf2313176c48d42b38f76e3ad57`
- `V2_PROOF.md`:
  `a660128940d0d2b02907ff5ef476432b06d45d3098b35426a3a19564870a3da5`
- `V2_SELF_AUDIT.md`:
  `78d6f17310b23306bce3392916ccf08519b4fe0d057e522a968fda343d516e4e`
- `V2_PROVENANCE.md`:
  `f492d02486ee670e3fb143d469610a5970c8b7f318ad2677d773b64b821d0548`
- `V2_MANIFEST.md`:
  `523c97d11d6d9161404f3a013f1564131b59e9b4c42e20a75eb0fbab590b072d`

All five hashes matched the preregistered values exactly. I then read the
entire V2 packet and the preserved V1 hostile FAIL. I also authenticated all
six preserved V1 artifacts against the identities in `V2_MANIFEST.md`; they
matched.

## Verdict

**FAIL, for a narrow recursive-cost defect in Theorem C.**

V2 repairs the V1 promotion blocker. It defines the input length, defines
numerical QP, and binds one fixed envelope over every conditional law,
history, and stage. Theorem A, the probability assertions in Theorem B, the
fixed-base probability assertion in Theorem C, and Corollary D survive this
re-audit.

Equation (C4), however, is not the recurrence of the complete conditional
routine described around it. A useful trial need not factor the current
integer. It can only enlarge `L`. The same integer then needs another
progress stage at the same bit length. The proof stops its cost accounting
after the first useful trial and omits these same-size continuations.

This is a cost-accounting defect, not a counterexample to the AP or order
claims. Adding the omitted stages still gives a numerical-QP bound, but it
does not give the frozen recurrence (C4).

## Promotion-blocking defect: (C4) counts one progress stage as a whole node

At one fixed nonterminal state `(N,L)`, Theorem C proves the following valid
claim. If a supplied base is nonstale and `u_p<=Q(n)`, then either the cell
is directly enumerable or independent uniform candidate trials need at most
`2Q(n)` expected recursively factored exponents before one useful event.

A useful event has two different outcomes:

1. it returns a proper factor; or
2. it certifies a block not dividing `L` and replaces `L` by a strict larger
   lcm.

Only the first outcome completes the current factoring node. In the second
outcome, `N` is unchanged. The procedure needs a new supplied base and a new
candidate loop at the same input size. Nothing in Theorem C says that the
first strict lcm growth reaches the terminal threshold.

Strict lcm growth at least doubles `L`. Therefore the number of such
same-size progress stages before the aggregate terminal is at most

\[
O\!\left(\log_2\frac{N^{1/4}}{L}\right)=O(n).
\]

This fact repairs the qualitative complexity conclusion, but the factor is
absent from (C4). If `F(n)` denotes the complete conditional factoring cost
and `P(n)` bounds the public work in one candidate trial, the direct
unrolling has the shape

\[
F(n)
\le
O\!\bigl(n\mathcal Q(n)\bigr)
F(n/2+O(1))
+O\!\bigl(n\mathcal Q(n)P(n)\bigr),
\]

not

\[
F(n)
\le
O(\mathcal Q(n))F(n/2+O(1))+\mathcal Q(n).
\]

There is a second instance of the same accounting issue. V2 says that
`Q(n)` dominates the *per-stage* public arithmetic cost. It then allows
`O(Q(n))` expected candidate stages but writes only `+Q(n)` in (C4). From
the stated bounds alone, the local term is at most `O(Q(n)^2)` per progress
state, and at most `O(n Q(n)^2)` after the same-size states are unrolled.
Using the actual polynomial modular-arithmetic cost gives a sharper term,
but it still must be multiplied by the expected number of trials.

The omitted factors are harmless to the numerical-QP classification:

\[
n\mathcal Q(n),\qquad
n\mathcal Q(n)^2,
\]

and the product of those envelopes over halved input sizes are all numerical
QP. Thus a revised packet can retain the intended conditional conclusion.
It must use a full-state recurrence, or it must define (C4) only as the cost
of one progress transition and use a separate function for complete child
factorization. As frozen, `T` is used for recursive complete factorization
while its recurrence accounts for only one progress transition.

## Checks that survived

### Factor cell and balanced interval counts

From `p<q<2p`,

\[
\sqrt{N/2}<p<\sqrt N<q<2p.
\]

Hence `p` belongs to `I_N`, and it is the only member of `I_N` with a
nontrivial gcd with `N`. Since `L` is even and every candidate is congruent
to the odd integer `p`, every `A_x=x-1` is even. Also
`0<A_x<q<2p`, so parity excludes the only possible positive multiple `p`.
Thus `gcd(A_x,N)=1` for every candidate.

If `W=|I_N|`, then `W=Theta(p)` with absolute constants. A residue class in
`W` consecutive integers occurs `floor(W/L)` or `ceil(W/L)` times. The
preterminal condition gives `L=O(sqrt(p))`, so `W/L` tends to infinity and

\[
H=\Theta(p/L)
\]

uniformly over all admissible `L` and `S`. The endpoint rounding changes
the count by at most one.

### Theorem A: divisor-average bound

For each `d|m`, the congruence `c+jL=0 mod d` is insoluble or is one class
modulo `d/gcd(d,L)`. Its count in `H` consecutive indices is at most

\[
\frac{H\gcd(d,L)}d+1\le\frac{HL}d+1.
\]

A law with largest atom `eta` assigns at most `eta` times this count. The
identity

\[
\gcd(A,m)=\sum_{d\mid\gcd(A,m)}\varphi(d)
\]

then gives

\[
\mathbb E_\mu\frac{\gcd(A,m)}m
\le
\eta\left[
\frac{HL}{m}\sum_{d\mid m}\frac{\varphi(d)}d+1
\right]
\le
\eta\left(\frac{HL\tau(m)}m+1\right).
\]

The insoluble cases, endpoints, and arbitrary nonuniform laws are all
covered. I found no missing divisor or normalization factor.

### Theorem B: local law and adaptive conditioning

For a fixed candidate, CRT makes the two reductions of a uniform unit
independent and uniform. Therefore

\[
\Pr(a^{A_x}=1\bmod r)
=\frac{\gcd(A_x,r-1)}{r-1}
\qquad(r=p,q).
\]

Apart from `x=p`, every declared factor or primary-certificate exit requires
a return in at least one field. The direct event has mass at most `eta`.
The two applications of Theorem A contribute one further `eta` each. This
reconstructs the exact constant `3` and proves (B1).

The rejection-sampling mass is also exact. Among the `N-1` nonzero residues,
exactly `q-1` are nonzero multiples of `p` and exactly `p-1` are nonzero
multiples of `q`. Thus the probability of a proper gcd before an accepted
unit is

\[
\frac{p+q-2}{N-1}.
\]

Retrying the zero residue does not change this ratio. The accepted residue
is a uniform unit, so the local-return calculation remains valid.

The fixed envelope closes the adaptive quantifiers. On every no-progress
history,

\[
\eta H\le\mathcal Q(n),
\qquad
L=O(p^{1/2}),
\qquad
H=\Theta(p/L).
\]

The uniform divisor bound and `Q(n)=p^{o(1)}` give

\[
\Pr(\text{useful}\mid\text{history})
\le p^{-1/2+o(1)}.
\]

Because `Q` has fixed constants, this `o(1)` is uniform. Since
`log_2 p=n/2+O(1)`, fixed `c_0,n_0` exist. A conditional union bound over
at most the same `Q(n)` trials proves (B6). Candidate adaptation does not
break the argument because each new base is sampled after the candidate and
its preprocessing are fixed.

### Theorem C: fixed-base progression and stale classification

The index of `p` is a solution of

\[
o_p\mid x_j-1.
\]

After division by `gcd(o_p,L)`, the step is invertible modulo
`u_p=o_p/gcd(o_p,L)`. The returning indices are exactly one residue class
modulo `u_p`. Any interval of `H` indices contains at least
`floor(H/u_p)` of them.

Every such `p`-return is useful for a nonstale base:

- a missing `q`-return gives the factor `p`;
- unequal local orders split during prime-by-prime stripping; and
- equal local orders leave their exact common order, whose primary block
  grows `L` unless that common order already divides `L`.

Thus the only no-progress local-order case is

\[
o_p=o_q\quad\text{and}\quad o_p\mid L.
\]

The lower bound (C3), the `H>=2Q(n)` consequence, and the small-cell direct
enumeration are correct. Repeated sampling is Las Vegas for one fixed
progress state: it advances almost surely and uses at most `2Q(n)` expected
child factorizations. The frozen proof does not carry that one-state result
through all later aggregate states, which is exactly the (C4) defect above.

### Corollary D and the promoted P161 interface

Every prime divisor of `u_p` is a prime divisor of `o_p`. If all those order
primes exceed `T(n)`, then either `u_p=1` or `u_p>T(n)`. Hence
`u_p<=Q(n)<T(n)` forces `u_p=1`, equivalently `o_p|L`.

The promoted P161 surviving branch supplies the premise for a squarefree
semiprime: its local orders are nontrivial, coprime to `N`, and have least
prime divisor above the chosen cap. Reduction from a hidden prime-power
component to its prime field is injective on that cyclic subgroup; in the
present squarefree scope this is immediate.

If `o_p|L`, then `x congruent to p mod L` and `o_p|p-1` imply
`o_p|x-1` for every candidate. Thus the two residual-order branches in
Corollary D are exhaustive. The corollary does not claim that P161 produces
the missing nonstale base.

## Scope and supplemental checks

The negative theorem is limited to the declared per-trial channel. It does
not cover heavy candidate atoms, candidate/base coupling, integer-biased
bases, or joint processing of nonreturns. Those exclusions are material and
are stated. Granting complete factorizations of `A_x` only strengthens the
negative upper bound.

The packet also does not claim an all-input factoring algorithm. Its base
source remains conditional. The present FAIL concerns only the frozen
recursive-cost equation, not an omitted construction of that source.

As a supplemental check, I exhaustively tested small balanced semiprimes,
admissible even moduli, all units, and all factor-cell candidates through a
small finite range. The tests found no counterexample to (B2), the return
progression, or the nonstale classification. This finite check is not used
as proof.

## Final assessment

V2 successfully closes the uniform adaptive envelope that caused the V1
FAIL. The AP mean, exponential obstruction, exact unit-rejection mass,
fixed-base success law, and roughness dichotomy are correct in their stated
scope. Promotion is still blocked because (C4) omits both repeated
same-input progress states and the multiplication of per-stage public work
by the number of trials. A revised recurrence with the omitted numerical-QP
factors would repair the defect without changing the main mathematical
boundary.
