# F108 proof-blind reconstruction

## Verdict

**Required statement: FAIL.**

The failure is limited and exact:

- The general set equality is **proved**.
- All five fixed public reconstruction claims **pass**.
- The required F99 boundary is **under-specified**. The authorized statement
  cites an inverse formula but does not include that formula or the F99
  parameters. The claimed inverse carry does not follow from
  `c_e = 2^e < N` alone.

The independent verifier completed 219,304 public checks with no verifier
failure. It read only `RECONSTRUCT_STATEMENT.md` and the pinned public F98
JSON. It did not factor an endpoint or relation value.

## General theorem: proved

Let the masks lie in (V=\mathbb F_2^n). For any current multiset of blocks
((x,s)), define the proof-only invariant

\[
I_p=\sum_{(x,s)} (v_p(x)\bmod 2)s.
\]

No algorithmic step needs to know (p) or compute this valuation.

For one refinement, put

\[
\alpha=v_p(x),\qquad \beta=v_p(y),\qquad
\delta=v_p(\gcd(x,y))=\min(\alpha,\beta).
\]

The new contribution is

\[
\delta(s+t)+(\alpha-\delta)s+(\beta-\delta)t
=\alpha s+\beta t
\]

in (V). Thus every (I_p) is invariant. Removing value one changes no
valuation. Removing a zero-mask block changes no invariant.

Initially, both endpoints in column (i) have mask (e_i). Therefore

\[
I_p=\sum_i(v_p(c_i)+v_p(w_i)\bmod2)e_i=r_p.
\]

At termination, the surviving (q_j) are pairwise coprime. A prime (p)
divides at most one surviving (q_j). If it divides none, (r_p=0). If it
divides (q_j), then

\[
r_p=(v_p(q_j)\bmod2)m_j.
\]

Hence an odd valuation gives (r_p=m_j\ne0), and an even valuation gives
(r_p=0).

Now (S_E(q_j)) is nonsquare exactly when some prime (p\mid E) has odd
valuation in (q_j). For that prime, (m_j=r_p\ne0). Conversely, every
nonzero (r_p) with (p\mid E) comes from the unique surviving (q_j) in
which (p) has odd valuation, so (S_E(q_j)) is nonsquare and (m_j=r_p).
Taking sets removes duplicate masks. Therefore

\[
\{m_j:S_E(q_j)\text{ is nonsquare}\}
=\{r_p:p\mid E,\ r_p\ne0\}.
\]

### Factor-free supported-part algorithm

For one coprime block (q), compute:

```text
S = gcd(q, E)
R = q / S
while gcd(R, S) > 1:
    g = gcd(R, S)
    S = S * g
    R = R / g
```

At termination, `S*R = q` and `gcd(S,R) = 1`. Every prime shared by `q` and
`E` enters `S` in the first step. While any further power of that prime
remains in `R`, the loop moves a nontrivial divisor into `S`. Thus `S` is
exactly (S_E(q)). An integer square-root test decides whether it is square.
This uses gcd, exact division, multiplication, and a square test. It does not
identify any prime.

### Bit complexity

Let (L) be the total explicit input bit length. Let (M(L)) be the cost of
an (L)-bit multiplication and (G(L)=O(M(L)\log L)) the cost of a gcd.

A successful refinement replaces the product (xy) by
(d(x/d)(y/d)=xy/d), before any zero-mask removal. Since (d>1), the base-2
logarithm of the live product falls by at least one. There are at most (L)
successful refinements and (O(L)) live blocks. A simple restart or work-list
implementation uses at most (O(L^3)) gcd tests.

Gcd saturation uses at most (L) successful divisions per block and there
are (O(L)) blocks. Product construction and square tests are lower-order.
A conservative bound is

\[
O(L^3G(L)+L^2M(L)\log L),
\]

which is polynomial in (L).

It is polynomial in (log N) when the total explicit batch and exposure-list
length is polynomial in (log N). This requires both the number of listed
relations or transitions and every listed integer's bit length to be
polynomial. It is not a polynomial-time-in-(log N) statement for an
exponentially large explicit batch. Reading such a batch already costs more
than polynomial time.

## Fixed public reconstruction: pass

The pinned public input hash is:

```text
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab
```

The verifier checked every public endpoint product, modular inverse,
trajectory provenance formula, carry numerator, carry range, and two-zero
duplicate identity.

It started with the 332 endpoint blocks from the 166 certificate columns. A
gcd-only work list produced 228 pairwise-coprime surviving values. Of their
nonzero masks, 227 distinct masks were nonsquare.

| Public check | Claimed | Reconstructed | Result |
|---|---:|---:|---|
| Complete nonsquare masks | 227 | 227 | PASS |
| Complete rank | 165 | 165 | PASS |
| Complete nullity | 1 | 1 | PASS |
| Represented raw insertions | 1,840 | 1,840 | PASS |
| Represented two-zero exclusions | 541 | 541 | PASS |
| Represented exposed masks | 191 | 191 | PASS |
| Represented exposed rank | 165 | 165 | PASS |
| All-round raw insertions | 15,935 | 15,935 | PASS |
| All-round two-zero exclusions | 6,008 | 6,008 | PASS |
| All-round exposed masks | 200 | 200 | PASS |
| All-round exposed rank | 165 | 165 | PASS |
| Represented circuit-local insertions | 34 | 34 | PASS |
| All-round circuit-local insertions | 82 | 82 | PASS |
| Circuit-local exposed rank | 54 | 54 | PASS |
| Root modulo (N) | 132,013,085 | 132,013,085 | PASS |
| \(\gcd(root-1,N)\) | 19,727 | 19,727 | PASS |
| \(\gcd(root+1,N)\) | 10,267 | 10,267 | PASS |

Both circuit-local scans produce the same 54 distinct masks and rank 54. The
local test uses exact selected relation values, not only their recorded
provenance. This is why scanning all 54 trajectories can find 82 insertions
although only eight trajectory keys occur in the certificate.

The raw exposure product has bit length 43,701 for the eight represented
trajectories and 386,008 for all 54 trajectories. The supported-part
calculation used these explicit products and gcd saturation only.

The all-column root also needs no factorization. The exact product of the 166
public relation values is a square. Its integer square root, reduced modulo
(N), is 132,013,085. Two gcd calls give the stated nontrivial divisors.

SageMath 10.9 independently checked the ranks from the reconstruction's own
factor-free mask sets:

```text
full=165
represented_raw=165
all_raw=165
represented_local=54
all_local=54
```

The canonical SHA-256 of those five mask sets is:

```text
ff909525563be0b47ed74682999e700418cf9b89717afe1ffbc31892f655291b
```

## F99 boundary: under-specified

The authorized statement gives (c_e=2^e<N), but it does not give the cited
formula for (w_e), the modulus family, or the private-row incidence data.

What follows from the supplied information is exact. If
(c_{e+1}=2c_e<N), then the first carry is zero. For least positive canonical
inverses,

\[
2w_{e+1}\equiv w_e\pmod N.
\]

The bounds (0<w_e,w_{e+1}<N) imply

\[
2w_{e+1}-w_e\in\{0,N\}.
\]

It equals (N) exactly when (w_e) is odd. It equals zero when (w_e) is
even. The condition (2^e<N) does not decide this parity. For example,

```text
N=15, e=2
c_e=4, c_{e+1}=8
w_e=4, w_{e+1}=2
2*w_{e+1}-w_e=0
```

Thus the claimed identity cannot be verified from the authorized statement.
The omitted F99 formula must prove that every relevant (w_e) is odd.

The requested boundary explanation is valid conditionally. If that formula
does prove (2w_{e+1}-w_e=N), then every first carry is zero and every inverse
carry is nonzero. The raw exposure list then contains only
(c_e=2^e), so its product has only the prime support of 2.

If each of (T) columns also has an odd valuation of a distinct private
prime, the corresponding masks are the (T) unit vectors. Those rows form an
identity matrix and keep the columns independent. Many zero carries can still
expose only one prime support. Carry frequency therefore does not imply a
dependency.

A non-global root needs more than a dependency. It needs the two square roots
to choose different signs modulo at least two coprime factors of (N).
Carry frequency controls neither the private rows nor these signs. It cannot
force a dependency or a non-global root.

To make the full statement pass, add the explicit F99 inverse formula and the
private-prime incidence assumptions to `RECONSTRUCT_STATEMENT.md`, or remove
the demand for an unconditional proof-blind verification of that boundary.

## Artifacts and failed attempts

`RECONSTRUCTION_OUTPUT.json` contains the complete pairwise-coprime basis,
all five mask sets, every supported-part result, and the public check results.
`reconstruction_run_with_timeout.py` enforces a 60-second hard timeout.

No reconstruction attempt failed. The runner preserves every future timeout,
invalid output, or verifier failure as a timestamped
`RECONSTRUCTION_FAILED_*` JSON and log pair. No pre-existing file was edited.
