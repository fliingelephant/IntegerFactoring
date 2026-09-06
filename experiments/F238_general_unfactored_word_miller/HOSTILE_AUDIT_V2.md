# F238 V2 focused hostile audit

## Verdict

**PASS.**  No counterexample, false probability law, implementation defect,
or remaining proof gap was found.  The V2 corrigendum repairs the invalid
last inference in V1 section 6.  The squarefree-semiprime theorem is
unchanged.

This is a conditional reduction.  It does not construct the required
quasipolynomial-size word `W`.  It is not an unconditional factoring
algorithm.

## Frozen-input integrity and evidence boundary

I authenticated exact bytes before reading the candidate artifacts.  The
five V1 expected hashes were supplied externally by the author before the
read.  The local `MANIFEST.md` does not contain a hash table.  This is a
workflow qualification, but it does not affect the authenticated
mathematics.

| Artifact | Expected and observed SHA-256 | Result |
|---|---|---|
| `STATEMENT.md` | `4be9c61c28826701960cdebdf326638d04ae00ec5ffa5db279ca3a7b5b19d2d9` | match |
| `PROOF.md` | `3dae9a2543dccd5ca52403dc3e6a732f75e34cb5dd16c6db3fe4507828946913` | match |
| `SELF_AUDIT.md` | `dfa47004c79d7b98d64da4dfda03aa90e6e4bf3ceaa5ffc17bc34971846834e0` | match |
| `PROVENANCE.md` | `31aa0f270ca5c567b4d9bde062abdf771aee66a50e5f067fc9ed0f42cdd954c6` | match |
| `MANIFEST.md` | `81e19b0a3d73e984ba6231f66f1401e339521c00c227a32fd2207567f6691a43` | match |
| `CORRIGENDUM_V2.md` | `459038e7d3ddfde462c5badbd41bd2ca7b076fb5c9952a97261103f33724414a` | match |

The disclosed unpreregistered random diagnostic is post hoc.  I treated it
as non-evidence.  No empirical output is used in this verdict.

I did not edit a frozen input or a durable ledger.  I wrote only this audit
in the packet directory.

## 1. Local semiprime return probabilities

Let `N=pq`, let `d=gcd(p-1,q-1)`, and write

\[
 p-1=ds_p,\qquad q-1=ds_q,\qquad N-1=dA.
\]

Reduction modulo `p-1` gives

\[
 \gcd(N-1,p-1)=\gcd(q-1,p-1)=d.
\]

After dividing both arguments by `d`, this also gives
`gcd(A,s_p)=1`.  Therefore, for `E=(N-1)W`,

\[
 \gcd(E,p-1)
 =d\gcd(AW,s_p)
 =d\gcd(W,s_p).
\]

The same identity holds at `q`.  A cyclic group of order `m` has exactly
`gcd(E,m)` elements killed by the `E`-power map.  Thus

\[
 \Pr(x^E=1\bmod p)=\frac{1}{r_p}=\alpha_p,
 \qquad
 \Pr(x^E=1\bmod q)=\frac{1}{r_q}=\alpha_q.
\]

CRT makes the events independent for a uniform unit modulo `N`.  Exactly
one return makes the initial gcd proper.  Its total probability is

\[
 \alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p).
\]

Both returns occur with probability `alpha_p alpha_q`, and for a
squarefree semiprime this event is exactly `g=N`.  These claims do not use
balance, zero defect, or a factorization of `W`.

## 2. Conditional unequal two-kernel law

Write `e_i=v_2(p_i-1)`, `v=v_2(E)`, and
`h_i=min(e_i,v)`.  On the event `x^E=1` at one prime, the local element is
uniform in the kernel of the power map.  The odd and two-primary
coordinates of this cyclic kernel are independent.  Its two-primary
coordinate is uniform in `C_(2^h_i)`.  Conditioning on both local returns
preserves CRT independence.

If `E=2^v u` with `u` odd, raising to `u` kills every local odd-order
coordinate.  It is an automorphism on the two-primary coordinate, so it
preserves its exact order.  For a uniform element of `C_(2^h)`, define
`J` by `ord=2^J`.  Direct counting gives

\[
 P_h(0)=2^{-h},\qquad
 P_h(j)=2^{j-1-h}\quad(1\le j\le h).
\]

The two conditional variables `J_p,J_q` are independent with these laws.
The square chain exposes a proper CRT square root of one exactly when
`J_p` and `J_q` differ.  If they agree, both coordinates reach `-1` and
then `1` at the same indices.  If they differ, one coordinate reaches `1`
first, and a tested signed gcd is proper.

For `a=min(h_p,h_q)` and `b=max(h_p,h_q)`, the failure probability is

\[
 \sum_{j=0}^{a}P_a(j)P_b(j)
 =2^{-a-b}\left(1+\sum_{j=1}^{a}4^{j-1}\right)
 =\frac{4^a+2}{3\,2^{a+b}}.
\]

Hence the conditional Miller probability is exactly

\[
 \mu_{a,b}=1-\frac{4^a+2}{3\,2^{a+b}}.
\]

Both `h` values are positive because `N-1` and both local orders are even.
For fixed `a`, failure is largest at `b=a`, where it equals

\[
 \frac{1+2\cdot4^{-a}}{3}\le\frac12.
\]

Thus `mu_(a,b)>=1/2`, including the edge case `a=b=1`, where equality
holds.

The valuation specializations also pass.  If `e_p<e_q`, expansion of the
two odd primes gives `v_2(N-1)=e_p`, so

\[
 h_p=e_p,\qquad h_q=\min(e_q,e_p+v_2(W)).
\]

If `e_p=e_q=e`, the two lowest terms add and
`v_2(N-1)>=e+1`.  Hence `h_p=h_q=e` and

\[
 \mu_{e,e}=\frac23(1-4^{-e}).
\]

## 3. Exact total law and residual lower bound

Adding the exclusive-return atoms and the Miller contribution on the
global-return atom gives the exact semiprime law

\[
 S=\alpha_p+\alpha_q-(2-\mu_{a,b})\alpha_p\alpha_q.
\]

Assume `A=alpha_p>=alpha_q=B`, and write `mu=mu_(a,b)`.  Then

\[
 S-\mu A=(1-\mu)A+B(1-(2-\mu)A).
\]

If the coefficient of `B` is nonnegative, the result is immediate.  If it
is negative, `B<=A` reverses the inequality and gives

\[
 S-\mu A
 \ge (2-\mu)A(1-A)\ge0.
\]

Therefore

\[
 S\ge\mu\max(\alpha_p,\alpha_q)
 \ge\frac{1}{2\min(r_p,r_q)}.
\]

Fresh independent trials are geometric.  If `min(r_p,r_q)<=R`, they
terminate almost surely and use at most `2R` trials in expectation.  This
also verifies the stated two-trial bound when either residual divides
`W`.

## 4. Miller implementation and cost

The finite chain is `z_i=x^(u 2^i) mod N` for `0<=i<=v`; `z_v=x^E`.
Testing both `gcd(z_i-1,N)` and `gcd(z_i+1,N)` covers the mismatch event
above.  The implementation returns only a gcd `g` with `1<g<N`, so every
output is verified.

The claimed one-exponentiation cost is attainable without factoring any
integer.  Compute `z_0=x^u mod N` once, square through `z_v`, and retain a
proper signed gcd candidate while continuing the chain.  At `z_v`, apply
the initial-gcd branch: return its proper gcd; accept the retained chain
candidate only when that final gcd is `N`; otherwise declare null.  This
has the exact stated trial law.  It uses one modular exponentiation, `v`
modular squarings, and `O(v)` gcds.  Storing the chain and scanning it only
after the final gcd is an equivalent implementation.

Uniform unit sampling also needs no factorization.  Rejection by
`gcd(x,N)` leaves the exact uniform distribution on the units.  A proper
gcd found during sampling can instead terminate with a verified factor;
this is extra success outside the abstract uniform-unit trial and cannot
weaken its bound.  For two distinct odd primes, pure rejection has constant
expected sampling cost.

Finally,

\[
 \operatorname{bitlen}(E)
 \le\lceil\log_2N\rceil+\lceil\log_2W\rceil,
 \qquad v\le\operatorname{bitlen}(E).
\]

The product, valuation, modular arithmetic, and gcd work are polynomial in
this bit length and in `log N`.  Multiplying by an expected `2R` trials
preserves numerical-quasipolynomial cost under the stated bounds on
`bitlen(W)` and `R`.

## 5. Extension to multiple prime supports

Let `N=prod_i p_i^(c_i)` have `k>=2` distinct odd prime supports.  With

\[
 d_i=\gcd(N-1,p_i-1),\qquad s_i=(p_i-1)/d_i,
\]

the same divided-gcd argument proves

\[
 \Pr(x^E=1\bmod p_i)
 =\frac{d_i\gcd(W,s_i)}{p_i-1}
 =\alpha_i.
\]

CRT makes these support-return events independent.  Every nonempty proper
return pattern makes the initial gcd proper.  Their total probability is

\[
 1-\prod_i(1-\alpha_i)-\prod_i\alpha_i.
\]

On the all-return pattern, either the initial gcd is already a proper
partial-power factor or it equals `N`.  Conditional on `g=N`, the local
prime-power unit groups remain independent.  For odd `p_i`, reduction
modulo `p_i` is an isomorphism on the two-primary subgroup, so its
conditional exponent law is still `P_(h_i)` with

\[
 h_i=\min(v_2(p_i-1),v_2(E)).
\]

The Miller chain fails exactly when every local order exponent agrees.
Thus

\[
 \mu_{\boldsymbol h}
 =1-\sum_{j\ge0}\prod_iP_{h_i}(j).
\]

The all-agree event is contained in the equality event for any two
supports.  The two-support calculation bounds that event by `1/2`, so
`mu_boldsymbol_h>=1/2`.

It follows that the complete success probability is at least

\[
 S_0=1-\prod_i(1-\alpha_i)
       -(1-\mu_{\boldsymbol h})\prod_i\alpha_i.
\]

The final V1 proof of the next inequality used product estimates with an
invalid sign.  The authenticated corrigendum supplies the correct proof.
Let `a=max_i alpha_i`, choose `m` attaining it, and put

\[
 B=\prod_{i\ne m}(1-\alpha_i),\qquad
 C=\prod_{i\ne m}\alpha_i,\qquad
 \mu=\mu_{\boldsymbol h}.
\]

Then the exact identity

\[
 S_0-\mu a
 =(1-a)(1-B)+(1-\mu)a(1-C)\ge0
\]

proves

\[
 \Pr(\text{factor})\ge S_0
 \ge\mu_{\boldsymbol h}\max_i\alpha_i
 \ge\frac12\max_i\alpha_i.
\]

If every `c_i=1`, all support returns are equivalent to `g=N`; therefore
the first inequality is equality.  With repeated prime powers, an all-
support return can expose a proper partial power before Miller, so only the
lower bound is claimed.  This distinction is correct.
