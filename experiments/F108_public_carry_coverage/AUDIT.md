# F108 hostile audit

## Verdict: PASS

The gcd-saturation theorem is correct. The fixed F98 replay counts are
correct. The public exposed rows have the same rank and the same right kernel
as the full 166-column circuit. The factor-free claim, polynomial-time claim,
and F99 boundary also pass.

No mathematical or numerical correction is required. Three scope and proof
details should be added before promotion:

1. Call the 1,840 and 15,935 integers **raw full-batch exposures**. Their two
   adjacent relation values are retained in the complete 9,414-value F98
   batch, but they need not both be columns of the selected 166-column
   circuit.
2. In the F99 boundary, state the missing second-carry identity
   `2*w_(e+1)-w_e=N`. Thus every second carry is one; only the first endpoint
   `2^e` is exposed.
3. State polynomial time in the total bit length of the explicit endpoint
   batch and exposure list. If exposures are supplied by a generator, its
   enumeration cost must also be included.

These additions prevent stronger readings. They do not change the theorem or
the fixed raw-scope conclusion.

## Independent method

The audit read every frozen F108 artifact and the complete pinned F98 public
input. It did not import or execute `analyze_public_carry_coverage.py`.

The fresh Sage verifier reconstructed:

- the P66 refinement from its transition rule;
- every one of the 42,336 raw round-one transitions;
- the two carry coordinates and exact adjacent products;
- gcd saturation on the public terminal blocks;
- the complete and exposed matrices over `GF(2)`;
- the exact normalized root and gcds; and
- a fresh F99 private-row instance at `T=6`.

Sage factorization was used only after the public construction existed. It
provided hidden prime rows as an audit oracle. Sage's matrix implementation
computed all ranks and right kernels.

The verifier also tested 25,122 small `(q,E)` saturation pairs exhaustively
and 512 deterministic random pairwise-coprime terminal systems. It found no
counterexample.

## General theorem

For a prime `p`, define the parity-mask invariant of a refinement state by

\[
R_p=\bigoplus_{(x,m)}(v_p(x)\bmod2)m.
\]

One refinement replaces `(a,M),(b,N)` by

```text
(d,M xor N), (a/d,M), (b/d,N),   d=gcd(a,b).
```

Write `alpha=v_p(a)`, `beta=v_p(b)`, and
`delta=min(alpha,beta)`. The new contribution is

\[
\delta(M+N)+(\alpha-\delta)M+(\beta-\delta)N
=\alpha M+\beta N
\pmod2.
\]

Thus refinement preserves `R_p`. At termination, pairwise coprimality puts
`p` in at most one retained block `(q_j,m_j)`. Therefore

\[
r_p=(v_p(q_j)\bmod2)m_j,
\]

or `r_p=0` if its contribution was discarded with a zero mask.

Now write `v_p(q_j)=a` and `v_p(E)=b`. Each saturation iteration removes
`min(a_current,b)` copies of `p`. It removes the complete `p^a` exactly when
`b>0`, and none when `b=0`. Hence `S_E(q_j)` is nonsquare exactly when some
prime `p|E` in that block has odd valuation. Such a prime supplies the row
`m_j`. Conversely, every nonzero exposed prime row supplies that same mask.

The theorem is therefore stronger than the stated span equality: the two
sets of distinct nonzero masks are equal.

## Fixed replay

All candidate counts reproduced exactly.

| Scope | Prime rows | Distinct masks | Public rows | Rank | Same kernel |
|---|---:|---:|---:|---:|---|
| Complete circuit | 230 | 227 | 227 | 165 | reference |
| Eight represented raw trajectories | 194 | 191 | 191 | 165 | yes |
| All 54 raw trajectories | 203 | 200 | 200 | 165 | yes |

The public refinement produced 228 terminal blocks: 227 nonsquare blocks and
one square block. Its rank is 165 and its nullity is one.

The raw carry counts also match:

| Scope | Transitions | First-zero | Second-zero | Two-zero excluded | Neither | Exposures |
|---|---:|---:|---:|---:|---:|---:|
| Eight trajectories | 6,272 | 998 | 842 | 541 | 3,891 | 1,840 |
| All 54 trajectories | 42,336 | 8,379 | 7,556 | 6,008 | 20,393 | 15,935 |

The exact root is

\[
132013085\pmod{202537109},
\]

and its two gcds are `19727` and `10267`.

## Exposure-scope boundary

For a transition with multiplier `a`, write

```text
c_(e+1) = a*c_e - h*N
a*w_(e+1) = w_e + l*N.
```

If `h=0`, then `c_e` divides both adjacent relation values. If `l=0`, then
`w_(e+1)` does. If both vanish, the exact values are equal. If exactly one
vanishes, the exact values are distinct.

Every raw state belongs to the generated round-one value set. Exact-value
deduplication retains 9,414 nonunit values. The audit confirmed that every
counted raw exposure joins two distinct values in this complete set.

This is not the same as joining two columns inside the selected circuit. If
both adjacent values are required to occur among the 166 selected columns,
the result is:

| Scope | Selected adjacent pairs | Exposure integers | Distinct masks | Rank |
|---|---:|---:|---:|---:|
| Eight represented trajectories | 34 | 34 | 54 | 54 |
| All 54 trajectories | 82 | 82 | 54 | 54 |

Thus “raw exposure spans the circuit” is correct. “Carry edges internal to
the circuit span the circuit” would be false. F108's `RESULT.md` uses the
word “raw,” so the published numerical claim passes. The scope should still
be stated next to the counts.

## Equal rank gives the same kernel

Every exposed public row is a full nonsquare-block row: a nonsquare supported
part cannot come from a square full block. Hence the exposed row space is a
subspace of the full row space. Both have rank 165, so the row spaces are
equal. Equal row spaces have the same orthogonal complement, which is the
same right kernel.

This statement concerns the kernel subspace. Two elimination routines need
not return the same basis in higher nullity. Here nullity is one, so there is
one nonzero dependency and both matrices determine it.

## Factor-free and complexity audit

Static AST inspection found no call to factorization, primality testing, or
prime-factor helpers in the candidate. Its imports are standard arithmetic,
JSON, hashing, timing, and path modules. Modular inversion, gcd, exact
division, integer square root, multiplication, and binary elimination do not
factor relation values. The pinned JSON contains factor certificates, but
the candidate does not read those fields.

Let `L` be the sum of the bit lengths of the initial endpoint entries. A
nontrivial refinement of values `a,b` by `d>1` changes the logarithmic mass

\[
\log a+\log b
\quad\text{to}\quad
\log d+\log(a/d)+\log(b/d),
\]

which decreases it by `log d >= 1`. Therefore there are `O(L)` refinements.
The number of pending and stable entries and the number of pair scans are
polynomial in `L`.

If the exposure integers have total bit length `H`, their product has
`O(H)` bits. Each successful saturation division at least halves the
remaining block, so a block uses at most `floor(log2(q_j))` divisions, plus
one final gcd test. Exact square tests and `GF(2)` rank are polynomial. This
proves the claim for explicit inputs. The fixed F98 generator enumerates only
54 times 784 transitions, so its exposure-list construction is also
polynomial in the F98 input length.

## F99 boundary

For the private-row family,

\[
w_e=N-\frac{N-1}{2^e}.
\]

Consequently

\[
2c_e-c_{e+1}=0,
\qquad
2w_{e+1}-w_e=N.
\]

Every carry pair is `(0,1)`. The exposure product is a power of two, so its
row span has rank at most one. The private primes `q_e` give an identity
minor and full rank `T`.

The fresh `T=6` instance had a 256-bit semiprime, full rank six, and exposed
rank one. This boundary remains narrower than F98: it has length
`Theta(sqrt(bitlength(N)))`, not `n^2`, and it does not establish P98
stability or null direct screens.

## Failed audit attempts

Two failures are preserved in `AUDIT_FAILED_RUNS.md`.

- The first run could not initialize Sage because the sandbox blocked its
  cache. It did not load the verifier.
- The second run reached the randomized phase, then failed because Sage had
  preparsed the deterministic seed as a non-native integer. The final source
  changes only that cast.

Neither failed run contributes evidence to the verdict.
