# F229 hostile audit

## Verdict

**PASS, with the exact scope readings below.**

I found no counterexample or proof gap in the fixed-gap exponent collapse,
the primary-block ceiling, the height threshold, the all-height interval
bound, or the ideal uniform-subgroup bound. The result is an obstruction for
three declared sample laws and one declared return/certificate channel. It is
not an obstruction for arbitrary small-prime words or for factoring this
fixed-gap family by other means.

Two readings must remain explicit.

1. The zero-return theorem is for nontrivial nonnegative bases
   `2 <= X <= H(n)`. The base `X=1` has a global order-one return but no
   useful event. Thus the shorter manifest phrase "every positive base" must
   not be read literally as including `1`.
2. Equation (C.2) is an **upper bound** inherited from (C.1). It is not a
   matching estimate. Some permitted choices of `H` have exactly zero useful
   probability.

These qualifications are already enforced by the formal theorem statements
and proof. They do not require a mathematical amendment.

## Authentication

I read `MANIFEST.md` first. Before reading any frozen candidate or frozen
local source, I recomputed every SHA-256 identity listed there. Every digest
matched.

| Frozen artifact | Expected and observed SHA-256 |
|---|---|
| `STATEMENT.md` | `715d27021f59e53f2d1198ae7440985d8cf7749123aa2f94463d9d870ce49dfb` |
| `PROOF.md` | `3554973f56f9c48b4ef727473fc016e1d2fe6939067a12b1a5999934e20e475d` |
| `SELF_AUDIT.md` | `01c93248deeae35e0998507e2a7afe2038ce36d63bc930d2904a26c024846feb` |
| `PROVENANCE.md` | `5db49e5fe139700be89c76ed1b5995a9e36fa154f3383a12e722af74b9cbe118` |
| `PROMPT.md` | `a4a85d0fc0cc540af7d2ab410dc8d7b6e6bf8a72dc2037509cb0999ddc9ee938` |
| P161 / F181 `STATEMENT.md` | `992f84a580a362d7908d9287e186dbae46963044956dae65b7b52540fa15df32` |
| P165 / F187 `STATEMENT.md` | `9434188bf8c35cbd54d0f6f553b7e0698f19470745515bb1fe503fbe8b67f14e` |
| P172 / F195 `V2_STATEMENT.md` | `49df39f6311c00c9fa1fc2f54b7da715783f17da10eec302373fe0fe479e2c3a` |
| P197 / F220 `V2_STATEMENT.md` | `935ef9a28dff6bfade891ca069eb5d544236977c4c8c20c6d4208ff582b5fe45` |
| F227 `V2_STATEMENT.md` | `dd905a434ed69fe0fcca5b034666e46444381cf2313176c48d42b38f76e3ad57` |

The observed SHA-256 of the unhashed manifest itself was
`df82b19fa75907a603b88316eee017b9c8f6efe7db59c13b0043968707a00785`.

## 1. Fixed gap and both exponent signs

The bounded-gap input is valid. Zhang proves a finite upper bound for
infinitely many consecutive prime gaps
([primary source](https://annals.math.princeton.edu/2014/179-3/p07)). After
discarding the unique gap involving `2`, those gaps are even. Infinite
pigeonhole over the finitely many even gaps below the bound gives one fixed
even `d >= 2` occurring infinitely often. This does not assert that any
prescribed gap occurs infinitely often.

For `q=p+d` and `A=pq-1`, the reductions are

\[
A\equiv q-1\equiv d\pmod{p-1},
\qquad
A\equiv p-1\equiv-d\pmod{q-1}.
\]

Thus the signs in the packet are correct. For a unit `X`, Fermat gives

\[
X^A\equiv X^d\pmod p,
\qquad
X^A\equiv X^{-d}\pmod q.
\]

At `q`, multiplication by the unit `-X^{-d}` shows
`X^{-d}-1=0` if and only if `X^d-1=0`.

The gcd identity is in fact valid for **every integer** `X`, stronger than
the stated unit version. For each `r` in `{p,q}`:

- if `r` does not divide `X`, the preceding exponent reduction applies;
- if `r` divides `X`, both `X^A-1` and `X^d-1` are `-1 modulo r`.

Hence the two integers have the same divisibility status at both squarefree
prime factors, and

\[
\gcd(X^{N-1}-1,N)=\gcd(X^d-1,N)
\]

for arbitrary `X`. If exactly one hidden prime divides `X`, the initial gcd
already factors `N`. If `N` divides `X`, the initial gcd is the trivial full
gcd and both displayed gcds equal `1`. The packet's unit-stage treatment of
nonunits is therefore safe.

## 2. Every certified common contribution divides `d`

On a unit global return, let `t_p` and `t_q` be the two local orders. The
gcd identity gives

\[
t_p\mid d,
\qquad
t_q\mid d.
\]

Now let `ell^e || A`. If the P197 primary test has

\[
\gcd(X^{A/\ell}-1,N)=1,
\]

then neither local order divides `A/ell`. Since both local orders divide
`A`, this forces

\[
v_\ell(t_p)=v_\ell(t_q)=e.
\]

Therefore `ell^e` divides `d`. Products of distinct certified primary
powers divide `d`, and the lcm of arbitrarily many such blocks still divides
`d`. If complete factor-first stripping ends without a factor, its exact
common order equals both local orders and also divides `d`.

This ceiling applies to the lcm contributed by these global returns. It does
not say that a larger state assembled from unrelated mechanisms must divide
`d`.

## 3. Height and word quantifiers

For one fixed numerical-QP value bound

\[
H(n)\le 2^{C(\log_2(n+1))^k},
\]

the constants are independent of the input, factors, stage, and history.
Thus `log H=o(n)`. Since `d` is fixed and
`log_2 p=n/2+O(1)`, eventually `H^d<p`. Every `2<=X<=H` then satisfies

\[
0<X^d-1<p<q,
\]

so it is a unit and has no local return. The cases `0` and `1` behave as
stated and create no useful event.

For an arbitrary nonempty positive unreduced word `X=prod_j b_j`, the exact condition

\[
\sum_j\log_2 b_j<\frac{\log_2p}{d}
\]

is `X^d<p`. Therefore a return requires total log-height at least
`n/(2d)+O(1)`. This is only a necessary condition.

The quantifiers do not close a numerical-QP-*length* word. A long word in
small generators can have total log-height well above the linear threshold.
Likewise, Theorem B bounds the **integer value** by a numerical-QP function;
it does not bound an integer merely because its bit length is numerical QP.
Those stronger readings would be false and are not used.

## 4. Uniform initial intervals at arbitrary height

If `H^d<p`, the useful probability is exactly zero. Otherwise
`H>=p^(1/d)`. In `I_H={2,...,H}`, the initial nonunit union has probability
at most

\[
\frac{H/p+H/q}{H-1}\le\frac4p.
\]

The polynomial `T^d-1` has at most `d` roots in either prime field. Each
residue class modulo `p` occurs at most `H/p+1` times, so

\[
\Pr(p\mid X^d-1)
\le \frac{d(H/p+1)}{H-1}
\le \frac{2d}{p}+\frac{2d}{H},
\]

and the same argument holds modulo `q`. Every declared useful event not
already caught by the initial gcd requires at least one local return. The
union bound therefore gives exactly the frozen upper bound

\[
\Pr(\mathrm{useful})
\le \frac{4+4d}{p}+\frac{4d}{H}
\le(4+8d)p^{-1/d}.
\]

This includes the crossing regime `H^d>=p` and remains valid for arbitrarily
large `H`. Conditional application at each reached history is valid provided
the history selects `H` before the fresh uniform draw. A numerical-QP union
bound costs only `2^{o(n)}` and needs no independence across stages.

This theorem does not cover a nonuniform law, a shifted interval, or joint
processing that extracts information from nonreturn samples by another
channel.

## 5. Exact-uniform subgroup endpoint

Projection from `G_N(B)` onto either image subgroup is a surjective finite
group homomorphism. Equal-size fibres make each projection exactly uniform.
No assertion about independence of the two projections is needed.

Each image is cyclic. If its size is `m`, it contains exactly `gcd(d,m)`
solutions of `x^d=1`. This proves the exact local probability

\[
\frac{\gcd(d,m)}m\le\frac dm.
\]

The subgroup-size lower bound also survives. Every positive `B`-smooth
integer `u<p` is a product of the generating rational primes, and distinct
integers in `[1,p-1]` give distinct residues modulo `p`. Since `B<p`, the
prime `p` itself is not `B`-smooth. Hence all `Psi(p,B)` integers counted up
to `p` inject into `G_p(B)`. The same holds at `q`.

Harvey--Hittmeir Lemma 2.4 states, for `x>=y>=2` and `x>=4`,

\[
\Psi(x,y)\ge
\frac{x}{(\log x)^{\log x/\log y}}
\]

([primary source](https://arxiv.org/html/2601.11131v2)). The candidate has
`p,q>B>=2` eventually, so it is in range. Its assumptions
`log n=o(log B)` and `log B=o(n)` give

\[
\frac{\log\log p}{\log B}=o(1),
\]

and therefore `Psi(p,B)=p^(1-o(1))`, with the analogous statement at `q`.
Combining the two marginal bounds by a union bound yields

\[
\Pr(\text{proper or global return})
\le \frac d{\Psi(p,B)}+\frac d{\Psi(q,B)}
=2^{-n/2+o(n)}.
\]

Projection correlation cannot increase this union-bound calculation.

## 6. Sample laws are not factoring algorithms

The three negative conclusions have different, narrow premises.

- Theorem B concerns adaptive laws supported on nonnegative integers whose
  **values** have one fixed numerical-QP envelope.
- Theorem C concerns a fresh conditionally uniform draw from an initial
  interval after its endpoint is fixed by the history.
- Theorem D grants an oracle-like exact uniform element of the entire
  generated subgroup. It proves no random-walk mixing result and constructs
  no exact sampler.

The complete factorization of `N-1` is also granted. An implementation of an
exact subgroup sampler could itself discover a factor, and a different
algorithm could process failed samples jointly. Neither possibility is
bounded by these distributional statements.

The hostile fixed-gap semiprimes are not factoring-hard instances. Once a
constant bound on `q-p` is known, one can test the finitely many gaps and
recover a matching factor pair directly. Their role is only to refute a
universal inverse-QP progress claim for the declared return/primary stage.

Most importantly, no inference is made about intermediate nonuniform word
laws. Such a law can cross the linear unreduced-height threshold while
remaining far from uniform on `G_N(B)`. The packet explicitly leaves that
regime open. It also makes no claim for arbitrary composites, another
annihilator, or an all-input factoring algorithm.

## Final assessment

All requested attacks survive. The proof establishes the advertised
fixed-gap obstruction in its exact restricted scope. **PASS.**
