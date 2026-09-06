# F158 blind reconstruction

## Scope and verified input

Before reading the statement, I computed its SHA-256:

```text
82c67580584de96200be0644b809ddd10f67fa24e5c088bd484342f3b4fee864  experiments/F158_certified_quadratic_tower_winwin/STATEMENT.md
```

This reconstruction uses only that statement. It does not use another F158
file or a proof of a prior result.

## Verdict

**The algebraic factor-or-double theorem is correct as a conditional
theorem.** The explicit and compact tests have the claimed local and global
consequences. The common-order certificate is sound. The order of every
genuine compact lift is exactly `2M`, and the square-root capacity argument
is sound.

It is **not** an unconditional factoring algorithm. The universal certificate
`(-1,2)` does not imply that a square root of `-1` exists, much less that one
can be constructed. A total source must return either a factor or a suitable
lift. If the phrase in Section 4 that a source “supplies a ... lift at every
level” is read literally as a lift-only promise, it is impossible at the
cutoff and does not by itself describe an algorithm that returns a factor.
The factor-or-lift formulation in Section 6 is the precise conditional claim
that makes the factoring conclusion valid.

There are two complexity qualifications:

1. “Polylogarithmic number of doublings” must be measured in the input bit
   length for the explicit-list size to remain quasipolynomial.
2. A polynomial-time source gives a polynomial-time factoring algorithm. A
   quasipolynomial-time source gives a quasipolynomial-time factoring
   algorithm. The compact decoder and the number of levels are polynomial;
   they do not reduce the source's running time.

The arithmetic F154 example and the consequences conditional on (18) and
(20) are verified below. Historical claims about what P138, F154, P139, or
F156 proved cannot be independently reconstructed from the statement alone.

## 1. Explicit-subgroup test

Write `H_r` for the image of `H` in `F_r^*`, for `r=p,q`.

If `gcd(x-h,N)` is proper, it is `p` or `q`, so it factors `N`. If no proper
gcd occurs and one gcd is `N`, then `x=h (mod N)` and hence `x` is in `H`.

Suppose instead that every gcd is one. If `x mod p` were in `H_p`, some
`h in H` would satisfy `x=h (mod p)`. Then `p` would divide `gcd(x-h,N)`,
contrary to that gcd being one. Thus `x` is outside `H_p`. The same argument
works for `q`.

For either hidden prime, `x^2` is in `H_r` while `x` is not. Therefore

```text
<H_r,x> = H_r disjoint_union x H_r,
```

and its order is `2|H_r|`. Globally, `x^2 in H` and `x notin H` give the
same two-coset decomposition, so `|<H,x>|=2|H|`.

### Why the priority rule is necessary

The raw predicates “a proper gcd exists” and “an `N` gcd exists” need not be
disjoint. For example, take

```text
N=15,  H=U_15,  x=1.
```

Then `gcd(x-1,15)=15`, but `gcd(x-4,15)=3`. Thus `x` is old and the same
scan also exposes a factor. With the stated priority, the algorithm returns
the factor. Without that priority, the claimed trichotomy would be
ambiguous. On the third branch all gcds are one, so neither of the first two
conditions holds.

The full scan performs one gcd per listed element; an implementation can stop
early after finding a proper gcd. Hence the worst-case time is
`|H| poly(log N)`.

## 2. The finite `N=77` witness and explicit towers

Modulo 7, `9` has order 3. Modulo 11, `9` has order 5. Hence `9` has order
`lcm(3,5)=15` modulo 77. Also

```text
26^2 = 676 = 60 (mod 77),
9*60 = 1 (mod 77),
gcd(26-9^2,77) = gcd(-55,77) = 11.
```

Thus `26^2=9^{-1}` lies in `<9>`, and the explicit scan returns the factor
11. Finally, `3*26=1 (mod 77)`, so the claimed inverse description is also
correct.

This is only one supplied lift. It proves a finite decoder capability. It
does not construct lifts for other inputs or later levels.

For a sequence of explicit subgroups, apply the preceding two-coset proof at
each step. Every step on which the priority scan returns neither a factor nor
an old element doubles the global group and each local image. Induction gives

```text
|H_t|       = 2^t |H_0|,
|(H_t)_r|   = 2^t |(H_0)_r|,  r in {p,q}.
```

Let `n=ceil(log_2 N)` be the input length. If the initial list has size
`exp((log n)^O(1))`, then after `t` doublings its size is

```text
exp((log n)^O(1) + t).
```

This remains quasipolynomial when `t=(log n)^O(1)`. Reaching the generic
square-root scale can require `t=Theta(n)`, at which point the list can have
size `2^Theta(n)`. Thus explicit enumeration does not give a uniform
quasipolynomial route to the capacity cutoff. If “polylogarithmic” were
instead intended to mean polylogarithmic in the numerical value `N`, the
complexity sentence would be false under the standard bit-complexity
definition; the relevant parameter is `n=log N`.

## 3. Common-order certificate

Fix `r` in `{p,q}`, and let `d=ord_r(g)`. Condition (7) gives `d | M`.
Suppose `d<M`. Choose a rational prime `ell` dividing `M/d`. Then
`d | M/ell`, so

```text
g^(M/ell) = 1 (mod r).
```

Consequently `r` divides `g^(M/ell)-1`, contradicting the gcd-one condition
(8). Therefore `ord_p(g)=ord_q(g)=M`. The supplied factorization of `M`
lets a verifier enumerate all distinct primes `ell | M`.

For `g=-1` and `M=2`, condition (7) is immediate. The only prime screen is

```text
gcd((-1)^(2/2)-1,N) = gcd(-2,N) = 1,
```

because `N` is odd. Thus `(-1,2)` is indeed a universal initial
common-order certificate within the stated semiprime scope.

## 4. Compact quadratic-lift test

Because `gcd(a,M)=1`, the element `g^a` has exact order `M` in each hidden
field. Let `D_r=ord_r(x)`. From `x^2=g^a` we get

```text
D_r / gcd(D_r,2) = M.                         (A)
```

This already limits `D_r` to `M` or `2M`.

The congruence `2k=a (mod M)` has `gcd(2,M)` solutions when it is soluble,
and none otherwise. Hence it has at most two solutions in general. Under the
coprimality assumption here the sharper statement is:

- if `M` is even, then `a` is odd and there is no solution;
- if `M` is odd, there is exactly one solution modulo `M`.

### Even `M`

There is no solution to (11). Also (A) cannot have `D_r=M`, because that
would make `D_r` odd while `M` is even. Therefore `D_p=D_q=2M`. If `x`
were in `<g_r>`, say `x=g^k`, its square would give `2k=a (mod M)`, a
contradiction. Thus `x` is outside both local cyclic subgroups.

### Odd `M`

Let `k` be the unique solution. Then

```text
x^2=(g^k)^2
```

in each hidden field, so, because the characteristic is odd,
`x=+g^k` or `x=-g^k` independently at `p` and `q`. The four sign patterns
give an exhaustive proof of the test:

| sign at `p` | sign at `q` | gcd of `x-g^k` | outcome |
|---|---|---:|---|
| `+` | `+` | `N` | `x=g^k` globally; inert |
| `+` | `-` | `p` | factor |
| `-` | `+` | `q` | factor |
| `-` | `-` | `1` | outside both local subgroups |

In the last row, `gcd(k,M)=1`, and `-g^k` has order `2M` because `M` is
odd. Thus `x` has exact order `2M` in both fields. This proves (13).

It also proves that `(x,2M)` satisfies the public certificate conditions.
Its `2M`-th power is one. Exact local order `2M` implies that, for every
prime `ell | 2M`, `x^(2M/ell)` is nonidentity in both hidden fields, so the
corresponding gcd is one. The factorization of `2M` is obtained from the
supplied factorization of `M` by adding one factor of two.

The displayed sign analysis also shows that the compact outcomes really are
exclusive. Although a general linear congruence can have two solutions, the
coprimality hypothesis means this test evaluates at most one candidate.

Solving the congruence, doing the modular exponentiation and gcd, and
checking the updated certificate all take time polynomial in the explicit
bit lengths.

## 5. Tower cutoff

Induction on the compact step gives

```text
M_t=2^t M_0.
```

Since `g_t` has exact order `M_t` in each finite field, Lagrange's theorem
gives `M_t | p-1` and `M_t | q-1`. Because `p<q`,

```text
p^2 < pq=N,
```

so `M_t <= p-1 < p < sqrt(N)`. No no-factor expansion can therefore create
a state with `M_t >= sqrt(N)`.

Let `t_*` be the first integer with `2^t_* M_0 >= sqrt(N)`. The preceding
state satisfies `M_(t_*-1)<sqrt(N)`. A total source with the Section 6
factor-or-lift guarantee can be called there. If it returns a factor, the
algorithm is done. If it returns a non-inert lift, the compact test either
finds a factor or claims a no-factor state of order
`M_t_*>=sqrt(N)`, which the divisibility argument forbids. The inert outcome
is excluded by the source promise. Hence a factor must be returned or
decoded no later than that call.

There are `O(log N)` levels. Comparisons with the cutoff can be performed
publicly as `M_t^2 >= N`. Consequently the decoder overhead is polynomial in
the input length. The total complexity and determinism still inherit those
of the source: a deterministic polynomial source yields deterministic
polynomial factoring, while a quasipolynomial source yields the analogous
quasipolynomial result.

The looser Section 4 wording is not sufficient if interpreted literally.
A routine promised only to output a valid lift at every level cannot fulfill
that promise at the final below-capacity state. The contradiction shows that
such a lift cannot exist; it does not specify an output from a lift-only
routine. Section 6 correctly repairs this by requiring the source itself to
return a factor when it cannot return a suitable lift.

## 6. Universal start versus existence of the first lift

Starting with `M_0=2`, every exponent coprime to `M_i` is odd, and every
genuine expansion gives

```text
M_i=2^(i+1).
```

At the first level,

```text
x_1^2=(-1)^a=-1 (mod N).
```

Such an `x_1` exists if and only if `-1` is a square modulo both `p` and
`q`, equivalently \(p\equiv q\equiv1\pmod 4\). For example,
`N=15=3*5` has the universal certificate `(-1,2)`, but no square root of
`-1` modulo 3 and hence none modulo 15. Thus the universal certificate is
not a universal root-existence theorem.

Even when both hidden primes are `1 mod 4`, the statement gives no method to
construct a root modulo `N`. If a valid root is supplied, the even-`M` case
above certifies exact common order four; it does not explain where the root
came from.

There is a further useful specialization of the case proof. Along the tower
started at `(-1,2)`, every `M_i` is even and every coprime `a_i` is odd.
Therefore (11) has no solution at any level, so the compact test performs no
candidate gcds. Every valid supplied lift is automatically an exact doubling.
At the final below-capacity state no further valid lift can exist. Thus, for
this universal start, the eventual factor must come from the **factor** arm
of the Section 6 source; it cannot be extracted by (12) from a valid lift.

## 7. Conditional F154 specialization

Assume only the displayed property (18). Since `Q(v)^(-1)` lies in the unit
subgroup `H`, `s_v^2` is a unit, which also makes `s_v` a unit. Thus `s_v`
is a legal input to the explicit-subgroup test. Its priority outcome is
exactly

```text
factor, or (if no factor) old endpoint, or (if neither) double both local images.
```

This proves (19) from (18), provided the complete old subgroup can be listed
within the claimed resource bound.

For the compact specialization, (20) supplies precisely the extra data that
the compact proof needs: a cyclic certified state, an exponent presentation
of the square, and coprimality of that exponent. Merely knowing that the
square lies in a multigenerator subgroup does not provide these data. Thus
the compact conclusion follows conditionally from (18), (20), and the
common-order certificate.

The statement alone does not define the F154 construction, `Q(v)`, row
reuse, or the named prior results beyond these displayed assumptions.
Accordingly, this reconstruction verifies the implication from (18)/(20),
not the external provenance claim that every F154 completion has those
properties.

## 8. Exact source nonclaim

What has been proved is a decoder and a monotone progress invariant:

```text
valid source output -> factor or exact common-order doubling,
enough consecutive doublings -> contradiction with p-1 < sqrt(N).
```

What has **not** been proved is a uniform routine that, at every
below-capacity certified state, returns either a factor or a public
non-inert `x,a` satisfying

```text
x^2=g^a (mod N),  gcd(a,M)=1.
```

In particular, the theorem does not construct the first square root of
`-1`, does not derive the required exponent presentation from membership in
an arbitrary subgroup, and does not turn an unknown subgroup order into the
certified common order `M`. Relation quantity or reuse alone does not imply
any of these missing properties. The statement's finite `N=77` witness also
does not imply an all-input source.

Therefore the precise final status is: **proved conditional win-win decoder;
unproved factor-or-lift source; no unconditional factoring algorithm.** The
meta-claim that “no current result proves the source claim” is a literature
claim and cannot itself be certified in a statement-only blind
reconstruction.
