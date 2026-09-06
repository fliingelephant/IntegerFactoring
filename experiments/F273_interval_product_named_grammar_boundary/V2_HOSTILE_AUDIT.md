# F273 V2 fresh hostile audit — PASS

## Frozen authentication

I authenticated the V2 boundary before judging its claims. The required and
observed SHA-256 of `V2_FROZEN.sha256` are both

```text
68cfb6e2d7c15563f9cb953b3233421746c62bfe9ee8ed6b04ee996530f62a94
```

Every V2 freeze entry matches:

| File | SHA-256 |
|---|---|
| `V2_STATEMENT.md` | `95cf55e02dd02322de2c78f95dfa6ddecae7c783fd152f7c00a64de511bf96b4` |
| `V2_PROOF.md` | `a91f2cdf97c26ac95010594383a299c3450527b98c8219638bef02d98ce28d99` |
| `V2_SELF_AUDIT.md` | `7bd76f3914495df1684564b69744a5b9a66a2ecfc332edd92398d3f9f7ac13b8` |
| `V2_PROVENANCE.md` | `13a4be4ef7772ba1230a4847cd6c938c1c711a2c8cad53a1f0b71712456613c5` |
| `V2_MANIFEST.md` | `873f240845cf44d8d79d2dc2ee9d1dcd2a812716fe85b2b991b51d4855abb017` |

The preserved V1 root also matches:

```text
bbfce77ead51db2d540d665ed620840894a317f1c96102c62a5ef8315e6df88c  FROZEN.sha256
```

Every V1 freeze entry and both post-freeze V1 audits match the V2 lineage:

| File | SHA-256 |
|---|---|
| `STATEMENT.md` | `cdc099e0a74b5d2510ac4d9b88cf965f0ef797e6bcc428ac855c3f74daec5079` |
| `PROOF.md` | `09978512f2e66768628df481380e059e3d6c90fc0010e5007db249322b723dc2` |
| `SELF_AUDIT.md` | `66218b417fa92037526d4d7b9b40a06638fd7ae7f578d5ec3176d886039a49dd` |
| `PROVENANCE.md` | `4595033097f3b66b3b1a12e4fce1dc339bf58fbc8f1e31bcbd40cf21c34a784c` |
| `MANIFEST.md` | `2b33fdd0d8921bccf613ef360e92dd7a604b06133de09bf8c91d944678e41786` |
| `HOSTILE_AUDIT.md` | `a8ff865f43d29e5af1c8956bd2c1bcb65fbf53f97339da024db4e8f2a35e0cb6` |
| `BLIND_RECONSTRUCTION.md` | `9bc7775fd05ec20c9f78923043857504a5795fef03966893d16535ae7a50cda9` |

I also resolved every external hash cited in the V2 statement or provenance
to its local artifact. All match:

| Lineage artifact | SHA-256 |
|---|---|
| P173/F196 statement | `07d2bccb9f508248a44f39faba3bd13a87cc0b2a1bc3dafa1464c348ae871c5c` |
| P173/F196 proof | `9f6e71c1c69661ad62780f0864b8fa460bd43df9f262b2774b7d231d20bba19b` |
| P174/F197 statement | `774ce7c5496c28942d6cb11814b95cc2487ae10477127d40d8609332090e49c3` |
| P174/F197 proof | `6b30bd83a52b380c6f04e32c4839b924324b5e55688e48077265abd06e83bc84` |
| P177/F200 V2 statement | `1edaedf1e0121e4603b8502cfb2473de250366cdc4b35acb216c3be314c8b7e5` |
| P177/F200 V2 proof | `b573b44d35d577e4c567448092997923c0a83cdeda8a1a1cb89ec9e1cf03e30b` |
| P178/F201 statement | `4915cbeea9e258524ece5dcf21e115f1a6c8ef0775dd0d1b926b94cdcbda8d41` |
| P178/F201 proof | `56dce149bdd39b545b35e695108aa8a1dd3fa0bb8cc891aaf437a95d03e82e17` |
| P215/F249 statement | `2b6594484dcb394b58126398d9944ab3e6aa18f8bc2d62e462dcc6e3c18db825` |
| P215/F249 proof | `8938898cf8118ddcee1b4831468c7f6a62a4928c35688abe61ace52ca8bd9865` |
| F263 V2 frozen root | `2a41fb0ca76955522843fdc0b15c69b1b2d811a3ac79021b0518bf6da9224271` |
| F263 V2 algebra | `fdf72364070e5b0ded549be171afcf005dc063afe4d7179968aa58ffdbb318d6` |
| F263 V2 source | `05c0b87a453eb3c2c40c01bf058b0559a6ff2e9b943d16ddcf68d147b1f4c827` |
| F263 V2 result audit | `320427df65f9d45f63cfaf4ad93194fe7e09cc499b4bd6d86b9a5ad7fb92b976` |
| P221/F272 V2 statement | `1b6c52624e5f957b2814f5e3e98572612e7cf9312b167ed117e01dddf0d4abb5` |
| P221/F272 V2 proof | `671c6810a753791fa7c08e3c8eec89b68a0b9fa64fc129d7263130a2b19b67d8` |

The complete F263 V2 freeze list also passes its own checksum verification.
I did not modify a frozen file, another audit, or a durable ledger.

## Verdict

**PASS under the exact named grammars, hypotheses, and exclusions in
`V2_STATEMENT.md`.** The V2 Smith correction is mathematically complete.
The V2 recursion counts distinguish the base frontier from every keyed
state in the memoized DAG. I found no false boxed formula, omitted recursion
level, invalid quotient, hidden modular inversion, or upgrade to a general
lower bound.

One wording boundary must stay explicit. The factorial and lcm are different
terminal formulas and different evaluation targets; they are not unequal for
every small input. For example, they coincide for `B=2` and `B=3`. The V2
proof says they are distinct integers *in general*, and every displayed
formula and gcd claim remains true in those small cases. No theorem uses
universal numerical inequality between them.

## 1. Child-zero ideal and formal dependency — pass

Write a polynomial as

```text
F = sum_i e_0^i F_i(o_0,z).
```

Restriction to `e_0=0` is zero exactly when `F_0=0`, so its kernel is
`(e_0)`. Joint expansion in `e_0,o_0` shows that vanishing on both axes
removes every term with either exponent zero. Every surviving monomial is
therefore divisible by `e_0 o_0`. This argument is valid over the stated
integral domain and needs no coprimality or Bezout step.

For `G/H`, a nonzero specialized denominator defines an element of the
generic-axis fraction field. A zero specialized quotient then forces the
specialized numerator to be zero. A denominator whose specialization is the
zero polynomial is outside the theorem, as stated.

For Corollary 1.1, let `U` be the union of the leaf sets used by the `K`
summaries. Then `|U| <= K q_0`. If a formal leaf is absent from `U`, every
allowed expression is independent of it, while the target product has degree
one in it. Hence all `M` leaves belong to `U` and `M <= K q_0`. This proves
only the independent-leaf claim. The affine specialization `y_j=x+j` remains
outside it.

## 2. Corrected Smith reconstruction — pass

For each `k<m`, rank `m-1` modulo `p` supplies a `k`-minor not divisible by
`p`. Full rank modulo `q` supplies a possibly different `k`-minor not
divisible by `q`. Therefore

```text
gcd(Delta_k,N)=1,  0 <= k < m.
```

At `k=m`, the determinant is the only minor. It is zero modulo `p` and
nonzero modulo `q`, so `gcd(Delta_m,N)=p`. Full rank modulo `q` also makes
the integer determinant nonzero. Thus the Smith ratios are defined, and

```text
d_m = Delta_m/Delta_(m-1),
gcd(d_m,N)=p.
```

No valuation-one assumption is needed.

For `A_B=diag(1,...,B)`, the balanced inequalities give

```text
p <= B < q,   B < 2p.
```

Thus exactly one diagonal entry is zero modulo `p`, and none is zero modulo
`q`. Independently computing the terminal determinantal divisors gives

```text
Delta_B = B!.
```

The nonzero minors of size `B-1` are exactly `B!/i` for `1<=i<=B`. For
each prime `ell`,

```text
v_ell(Delta_(B-1))
  = min_i v_ell(B!/i)
  = v_ell(B!) - max_i v_ell(i)
  = v_ell(B!) - v_ell(lcm(1,...,B)).
```

Consequently,

```text
Delta_(B-1) = B!/lcm(1,...,B),
d_B         = lcm(1,...,B).
```

Because `p<=B<q`, both `B!` and the lcm contain `p` and do not contain
`q`. Their gcd with `N=pq` is exactly `p`. This authenticates the corrected
determinantal-divisor/invariant-factor distinction. It supplies no reduction
between evaluation of the factorial and evaluation of the lcm.

## 3. Discriminant and superfactorial — pass

The roots of `P_m` are the distinct integers `-1,...,-m`. The absolute
derivative resultant is the squared product of pairwise root differences.
A difference `d` occurs `m-d` times, so

```text
D_m = product_(d=1)^(m-1) d^(2(m-d))
    = (product_(k=1)^(m-1) k!)^2.
```

Adding the next factorial proves `D_(m+1)/D_m=(m!)^2` as an integer
identity. Summing logarithms gives the upper size bound. Restricting to
`m/4 <= d <= m/2` gives the matching lower bound. Hence
`bitlen(D_m)=Theta(m^2 log(m+1))`.

On the unresolved balanced branch, preliminary `gcd(B,N)` excludes `B=p`.
Thus `p<=B-1<q`. The base `p` occurs with positive exponent in `D_B`, while
no base is divisible by `q`. Therefore `gcd(D_B,N)=p`. This is a
factor-bearing identity, not an evaluator.

## 4. Cross-resultant recursion and telescope — pass

Evaluating the second monic polynomial at the roots of the first gives

```text
R_c(m) = product_(0<=i,j<m) (cm+j-i).
```

Its smallest factor is `(c-1)m+1`, so it is positive. Splitting both
length-`2m` blocks into length-`m` children gives separations
`2c-1,2c,2c,2c+1`. Resultant multiplicativity therefore proves

```text
R_c(2m) = R_(2c-1)(m) R_(2c)(m)^2 R_(2c+1)(m).
```

For the telescope, the inner product over `j` is a quotient of two
factorials. Multiplying over `i` gives adjacent factorial ranges. With
`S(k)=1!2!...(k-1)!`, including `S(0)=S(1)=1`, this reconstructs

```text
R_c(m) = S((c+1)m) S((c-1)m) / S(cm)^2,
D_m    = S(m)^2,
S(m+1)/S(m) = m!.
```

The `c=1` endpoint is valid because `0!=1`. The quotient is an exact
integer identity derived before modular reduction. It does not authorize
inversion of `S(cm)` modulo a composite modulus. On the unresolved balanced
branch, `S(B)` contains `p!` and contains no factor divisible by `q`, so
`gcd(S(B),N)=p`.

## 5. Corrected recursion-state counts — pass

Let `C_0={1}` and replace every `c` by `{2c-1,2c,2c+1}` at the next length
level. Consecutive triples overlap at their endpoints. Induction gives

```text
C_s = {1,...,2^(s+1)-1}.
```

Starting from `R_1(2^t q_0)`, the exact base-frontier count is therefore

```text
|C_t| = 2^(t+1)-1.
```

Memoization uses `(length,offset)` keys. Equal offsets at different levels
remain different states. Thus the complete cross-resultant DAG contains

```text
sum_(s=0)^t (2^(s+1)-1) = 2^(t+2)-t-3
```

states. For `M=2^t q_0`, the standalone counts are exactly

| Standalone `R_1(M)` quantity | Exact count |
|---|---:|
| base frontier | `2M/q_0-1` |
| complete cross-resultant DAG | `4M/q_0-t-3` |

For the discriminant recursion, `D_(2m)=D_m^2 R_1(m)^2`. When `t>=1`,
the top cross term is `R_1(M/2)=R_1(2^(t-1)q_0)`. Applying the preceding
formulas with `t-1` gives

| `D_M` expansion quantity | Exact count |
|---|---:|
| base-frontier offsets | `M/q_0-1` |
| cross-resultant DAG | `2M/q_0-t-2` |

Every lower discriminant cross term is the offset-one node already present
at the corresponding length in the top cross-resultant DAG. The distinct
discriminant nodes `D_M,...,D_(q_0)` add `t+1` states. The full literal
discriminant/resultant DAG therefore has exactly

```text
2M/q_0-1
```

states. For `t=0`, it has the single state `D_(q_0)`, and the same formula
still gives one.

As a finite check of the derivation, the base/full cross-resultant counts
for `t=0,1,2,3,4,5` are respectively
`(1,1),(3,4),(7,11),(15,26),(31,57),(63,120)`, exactly as the two formulas
predict.

If `M=2^Theta(n)` and `q_0` is bounded by a fixed quasipolynomial, then
`log q_0=o(n)` and `M/q_0=2^Theta(n)`. One explicit `n`-bit residue per
keyed state uses `Theta((M/q_0)n)` bits. Literal enumeration performs
`Omega(M/q_0)` state operations. These costs do not apply to an implicit
representation or another identity.

## 6. Retained theorem and scope audit — pass

The unchanged child-zero, independent-leaf, rank-defect, discriminant,
superfactorial, resultant-recurrence, telescope, balanced-gcd, and literal
asymptotic claims all reconstruct under their stated hypotheses. The V2
diff changes the Smith classification and exact state accounting; it does
not silently strengthen the other theorems.

The imported P173, P174, and P177 results are context only. Their hashes are
authenticated, but no F273 V2 proof step uses their mathematical content.
The F201, F249, F263, and F272 references are also boundary comparisons,
not premises.

The proof never specializes algebraically independent leaves to an affine
jet variety, turns polynomial divisibility into a general circuit lower
bound, identifies the lcm evaluator with the factorial evaluator, converts
exact integer cancellation into modular inversion, or counts an implicit
algorithm as a literal keyed DAG. Therefore the stated exclusions remain
necessary and accurate. In particular, V2 proves no general arithmetic or
Boolean circuit lower bound, uniform interval-product evaluator lower bound,
succinct-matrix lower bound, numerical-quasipolynomial evaluator, factoring
algorithm, or empirical result.
