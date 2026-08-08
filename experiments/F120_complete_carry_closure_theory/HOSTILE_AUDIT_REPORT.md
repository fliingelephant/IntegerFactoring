# F120 fresh hostile mathematical audit

## Verdict

**PASS.** The source-independent degree bound, its stable-private corollary,
the `N=2q-1` construction, the finite trial-hard semiprime falsifier, and the
private-row peeling statement are correct within the stated exact-value
projection.

The main collision risk does not break the proof. Different inverse orbits
can have one exact product. Exact-value deduplication turns all of them into
one column. For each distinct product, choose one witness orbit. Witness
orbits chosen for different products are disjoint, so the endpoint-counting
map is injective.

The result does not prove a factoring obstruction. It refutes `REUSE` only.
It leaves `CLOSE` and `ROOT` open. It also does not rule out feedback that
uses a different integer representation of an already known exact product.

## Audit method

I read these candidate files in full:

- `QUESTION.md`;
- `RESULT.md`;
- `FAILED_ROUTES.md`;
- `MANIFEST.md`;
- `FAILED_RUNS.md`;
- `REGISTRATION.json`;
- `find_semiprime_private_row.py`;
- `run_with_timeout.py`;
- `OUTPUT.json`;
- `RUN.log`;
- the preserved failed output and failed log.

I also read the existing independent audit registration, verifier, runner,
output, and run log in full. I inspected `RECONSTRUCT_STATEMENT.md` and the
fixed-source definitions cited from F116 and F118.

I did not run a new search, enumerate a new source, or use external evidence.
The existing registered independent verifier is treated as finite evidence
only after its method and output were checked.

## 1. Inverse orbits and exact-product collisions

For a unit `c` in `1..N-1`, its least positive inverse `w(c)` is unique. The
map `c -> w(c)` is an involution. Therefore the unordered set

```text
O(c) = {c,w(c)}
```

is one inverse orbit, and its exact product is constant on that orbit.

Different orbits can share a product. The existing independent verifier gives
the smallest reported example:

```text
N = 11,
P = 12,
orbits {2,6} and {3,4}.
```

This does not invalidate the degree proof. Let `P` range over distinct exact
products after projection. Choose one witness orbit `O_P` for each `P`. If
two chosen orbits for products `P` and `Q` share an endpoint `x`, then both
must contain the unique inverse of `x`. Hence the orbits are equal and
`P=Q`. Thus chosen orbits for distinct products are disjoint.

If a prime `r` occurs to odd valuation in `P`, then `r` divides `P=cw` for
the chosen witness orbit. Primality makes `r` divide at least one endpoint.
Assign one such endpoint to `P`. The disjoint-orbit fact makes these assigned
endpoints distinct across distinct products. This is the required injection.

The proof does not claim that raw residue occurrences are disjoint after a
product collision. It counts projected exact-value columns. This scope is
essential.

## 2. Degree bound and stable privacy

There are exactly

```text
floor((N-1)/r)
```

positive multiples of `r` below `N`. The injection above therefore proves

```text
degree(r) <= floor((N-1)/r).
```

No property of the source menu is used. The statement holds for every subset
of the complete canonical exact-value universe.

If `r>(N-1)/2`, the upper bound is one. A present odd row has degree at least
one, so its degree is exactly one. Adding more canonical residues cannot add
a second distinct exact-value column with that row. The stable-private
corollary is correct.

## 3. Carry formulas

From

```text
1 + kappa*N = c*w,
1 <= c,w < N,
```

we have `kappa>=0`. Since `w<N`,

```text
c*w < c*N,
```

and hence `kappa<c`. Interchanging `c` and `w` gives `kappa<w`. Therefore

```text
0 <= kappa < min(c,w).
```

Reducing the exact identity modulo `c` gives

```text
kappa*N = -1 mod c.
```

Since `gcd(c,N)=1`, this is the unique class

```text
kappa = -N^(-1) mod c.
```

The range `0<=kappa<c` selects its canonical representative. At `c=1`, the
only residue class modulo one is zero and `kappa=0`; alternatively, the
inverse notation can be stated for `c>1` and the `c=1` case handled directly.
The projected source removes its exact product `P=1`, so this convention has
no effect on F120.

## 4. The `N=2q-1` identities

Let `q>2` be prime and set `N=2q-1`. Then `N` is odd and

```text
2q = N+1 = 1 mod N,
```

so the least positive inverse of `2` is `q`. The exact product is `2q`, its
carry is one, and `v_q(2q)=1`. Also

```text
q = (N+1)/2 > (N-1)/2.
```

The stable-private theorem applies.

Because `N` is odd, multiplication by two does not change either sign gcd:

```text
gcd(2-q,N) = gcd(4-2q,N) = gcd(3,N),
gcd(2+q,N) = gcd(4+2q,N) = gcd(5,N).
```

If `q=1 mod 30`, then `N=1 mod 60`. Both gcds are one. Dirichlet's theorem
gives infinitely many prime `q` in this residue class. It gives no required
factorization of `2q-1`. The candidate states this limit correctly.

## 5. Finite semiprime evidence

The registered search reports

```text
p   = 1,000,289,
ell = 2,000,309,
N   = 2,000,887,089,301,
r   = 1,000,443,544,651,
n   = 41,
n^2 = 1,681.
```

The search used proof-enabled Sage primality checks and stopped at registered
ordinal 23. Its first attempt failed before candidate generation because of
a Sage cache permission error. The failed log and empty failed output are
preserved. The approved retry changed only the cache location.

The existing independent verifier did not import or execute the candidate
search code. It:

- rebuilt both consecutive-prime sequences;
- reproduced all 22 earlier rejections and ordinal 23;
- proved `p`, `ell`, and `r` prime by complete trial division through their
  integer square roots;
- reproduced the registered trace hash;
- checked the exact product, inverse, carry, valuation, sign gcds, bit length,
  and trial bound;
- exhaustively checked the degree theorem for all odd `N` from 3 through 301;
- explicitly tested the `N=11, P=12` different-orbit collision.

The output records all checks as true. The arithmetic consequences follow:

- `N=p*ell` is an odd distinct semiprime;
- distinct prime exponents make `N` a non-perfect power;
- both factors exceed `n^2`;
- seed `2` has exact value `N+1=2r` and a valuation-one `r` row;
- `r>(N-1)/2`, so this row is private in the complete projected universe;
- both endpoint sign screens are one.

This one input is enough to refute universal semiprime `REUSE`. It is not an
infinite family.

## 6. Private-row peeling

Let row `r` have its only one in column `j`. For every binary dependency
vector `x`, the row equation is

```text
x_j = 0.
```

Delete row `r` and column `j`. Restriction maps the original kernel to the
reduced kernel. Extension by `x_j=0` maps the reduced kernel back to the
original kernel. These maps are inverse. Thus peeling preserves kernel
nullity and all supports that survive the deletion.

The selected exact products are unchanged under this correspondence.
Therefore their positive exact square roots, and their residue classes modulo
`N`, are unchanged. The normalized-root image on the surviving kernel is also
unchanged.

## 7. Separation of the three gates

The candidate keeps the gates separate.

### `REUSE`

`REUSE` is false on the finite trial-hard semiprime. The seed-`2` row is
present and has degree one in the globally deduplicated exact-value matrix.

### `CLOSE`

One private row forces only its own column coefficient to zero. The peeled
matrix can have zero or positive nullity. F120 does not determine `CLOSE` for
the remaining complete source.

### `ROOT`

A nonzero binary kernel can map only to the global signs. F120 does not prove
that the normalized-root map is nonzero. Private-row peeling preserves the
existing image; it does not create a useful root.

No implication between these gates is smuggled into the result.

## 8. Exact scope after audit

The strongest valid statement is:

> After global exact-value deduplication, a prime row `r` has degree at most
> `floor((N-1)/r)`. Hence every present row above `(N-1)/2` is permanently
> private. One trial-hard distinct semiprime contains such a seed row, so a
> complete canonical source does not force exact-value `REUSE`.

The audit does not promote any of these stronger statements:

- raw residue occurrences obey the same degree bound;
- different endpoint orbits with one product contain no new representation
  information;
- one private row makes the complete matrix full rank;
- the finite instance belongs to an infinite semiprime family;
- failure of `REUSE` implies failure of `CLOSE` or `ROOT`;
- the complete source fails to factor the finite instance;
- feedback cannot gain new named integer blocks.

The result is a sound barrier to one proposed closure lemma. It is not a
factoring algorithm and not a complete-source impossibility theorem.
