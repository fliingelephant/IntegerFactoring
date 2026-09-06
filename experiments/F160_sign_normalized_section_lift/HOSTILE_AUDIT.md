# F160 hostile audit — PASS

## Frozen inputs

I read the complete frozen statement, proof, and manifest. Their SHA-256
hashes matched the expected values before this audit:

- `STATEMENT.md`:
  `fd232fabd54a66ed03090a3ce4a03905dc1d3e3667b6ba712acee80751751ecc`;
- `PROOF.md`:
  `cc18b16e96f8363c0eb71bdb85e840bef9d5d9c7c954d5ec1f0b15875d9b17c7`;
- `MANIFEST.md`:
  `2b740dff6f4b61eb4ed5b28dcd9661450089dacc8cb819493062b46586287273`.

I did not modify a frozen input or a durable ledger. I ran no research
computation. I checked the exact examples below directly from the displayed
integers.

## Verdict

**PASS.** The sign-normalized factor-or-double theorem is correct for both
parities of `M`. The propagated common-order certificate is exact. The P138
bridge and the F154 specialization are valid under their stated provenance
hypotheses. The Jacobi character formula, its two capacity cases, the two
displayed examples, and the paired-discriminant root equivalence are also
correct.

The main limitation is not hidden by the statement. A triple `(v,u,a)` in
the bridge already contains enough information to construct the missing
scalar root `x=u z_v`. For fixed `v` and `a`, finding such a `u` is equivalent
to finding that root after a public change of coordinates. F160 removes the
old *externality* condition, but it does not manufacture a lift or prove that
the sparse section source hits one. Thus this is a clean conditional decoder
and source target, not an all-input factorization algorithm.

## 1. The order calculation leaves no omitted branch

Fix a hidden prime `r` and put `d_r=ord_r(x)`. Since `gcd(a,M)=1`, the
element `g^a` has exact local order `M`. From `x^2=g^a` one gets

\[
\frac{d_r}{\gcd(d_r,2)}=M.
\]

If `M` is even, `d_r` cannot be odd. Hence `d_r=2M` at both hidden
primes. There is no inert root to detect in this case.

If `M` is odd, the congruence `2k=a modulo M` has one solution. Moreover,
`gcd(k,M)=1`: multiplication by two is an automorphism modulo odd `M`, and
`2k` is a unit because `a` is a unit. The two local roots are exactly
`+g^k` and `-g^k`. Therefore `gcd(x-g^k,N)` has only the reported outcomes:

- one mixed CRT sign gives `p` or `q`;
- two positive signs give `N`, after which replacing `x` by `-x` is valid;
- two negative signs give `1`, after which keeping `x` is valid.

In both no-factor cases the selected element is `-g^k` locally. Since
`g^k` has odd order `M`, its negative has exact order `2M`. This also covers
the edge case `M=1`: the global comparison of a square root of one either
factors `N` or selects `-1`, of order two.

The source-free odd-order doubling is therefore exact. One can take `a=1`,
compute `k=2^{-1} modulo M`, and use `-g^k`. It is external to the odd-order
cyclic subgroup at both hidden primes. This construction cannot repeat after
the order becomes even, as the statement says.

### Exact branch checks

An odd-order instance is

\[
N=341=11\cdot31,\qquad g=157,\qquad M=5.
\]

Here `g=3 modulo 11` and `g=2 modulo 31`, and both local elements have
order five. Take `a=2`, so `k=1`. For the internal root `x=g`, the gcd is
`N` and the procedure selects `-g=184`, which has local order ten. For the
mixed root `x=91`, one has

\[
91\equiv 3\pmod {11},\qquad 91\equiv-2\pmod {31},
\]

and

\[
91^2\equiv157^2\equiv97\pmod {341},\qquad
\gcd(91-157,341)=11.
\]

Thus the same public comparison handles the inert and mixed branches exactly.

An even-order instance is the statement's `N=221`. With

\[
g=-1=220,\qquad M=2,\qquad a=1,\qquad x=174,
\]

one has `x^2=-1 modulo 221`. The reduction of `x` has order four modulo both
13 and 17, as the theorem requires.

## 2. Certificate propagation is valid

Exact local order `2M` immediately gives

\[
y^{2M}=1\pmod N.
\]

For every rational prime `ell` dividing `2M`, an element of exact order
`2M` cannot satisfy `y^(2M/ell)=1` in either hidden field. Hence

\[
\gcd(y^{2M/\ell}-1,N)=1.
\]

These are precisely the P144 public certificate checks. The known
factorization of `M` gives the factorization of `2M` by increasing the
two-adic exponent. No discrete logarithm or hidden-prime information is
needed.

This argument also confirms that the no-factor result is common-order
doubling, not only global subgroup growth. It rules out a hidden branch in
which one local order stays at `M` while the other becomes `2M`.

## 3. The section bridge is algebraically exact but source-strong

For an actual P138 decorated lift,

\[
z_v^2=Q(v)\pmod N.
\]

The public congruence in (8) therefore gives

\[
(u z_v)^2=u^2Q(v)=g^a\pmod N.
\]

Thus `x=u z_v` satisfies the primitive-lift theorem. Membership `v in W`,
the modular equality, `gcd(a,M)=1`, and the unit condition on `u` are all
publicly testable. If testing `u` finds a proper gcd, it has already factored
`N`.

The provenance requirement is essential. A parity vector by itself does not
supply `z_v`; the algorithm needs the actual decorated section lift obtained
from the retained records. F160 states this requirement.

There is also an exact equivalence that limits the interpretation. Once
`z_v` is public, any root `x` of `g^a` yields

\[
u=xz_v^{-1},
\]

and any valid `u` yields `x=u z_v`. Hence the existence or discovery of `u`
for fixed `(v,a)` is the original scalar-root problem in new coordinates.
The value of the bridge is its compatibility with a concrete P138/F156
source grammar. The bridge alone is not a new root-generation operation.

For F154, `s_v^2=Q(v)^(-1)`. Therefore the public equality

\[
Q(v)^{-1}=g^a\pmod N
\]

is sufficient with `x=s_v`. The coprimality condition on `a` is still
necessary and is correctly retained. Mere membership of `Q(v)^(-1)` in a
larger multigenerator subgroup would not be enough; F160 does not claim
otherwise.

## 4. The even-order Jacobi formula is exact

For a primitive element `zeta_r`, every exact-order-`M` element has the form

\[
g=\zeta_r^{c_rt_r},\qquad c_r=(r-1)/M,\qquad\gcd(t_r,M)=1.
\]

When `M` is even, both `t_r` and every `a` coprime to `M` are odd. Euler's
criterion then gives

\[
\left(\frac{g^a}{r}\right)=(-1)^{c_rt_ra}=(-1)^{c_r}.
\]

Thus a local root exists exactly when `c_r` is even, or equivalently when
`2M` divides `r-1`. Jacobi value `-1` means that the two parities differ,
so exactly one local root exists and no scalar CRT root exists. For example,

\[
N=35=5\cdot7,\qquad (g,M)=(-1,2)
\]

has `c_5=2` and `c_7=3`. The Jacobi symbol of `g` is `-1`, and `-1` has a
root modulo 5 but not modulo 7.

Jacobi value `+1` means only that the *next-layer parity capacities* agree.
It does not assert equality of the full two-adic valuations of `p-1` and
`q-1`. Under that precise reading, the statement's word “capacities” is
correct. Its two examples check both branches:

- for `N=221=13*17`, `c_13=6` and `c_17=8`, and
  `174^2=30276=-1 modulo 221`;
- for `N=77=7*11`, `c_7=3` and `c_11=5`, so `-1` is a nonsquare in both
  fields.

The sentence that a total factor-or-root source must factor on the Jacobi
`-1` branch is a requirement on that source's output contract. The Jacobi
calculation itself does not factor `N`. The frozen scope makes no contrary
claim.

## 5. Paired discriminants are exactly root-equivalent

For a unit `D` of Jacobi symbol `-1` and `E=Dg^a`, multiplicativity gives
Jacobi symbol `-1` for `E` when `g` has Jacobi symbol `+1`. Also

\[
DE=D^2g^a\pmod N.
\]

Multiplication by the public unit `D` gives a bijection

\[
x^2=g^a
\quad\longleftrightarrow\quad
(Dx)^2=DE,
\]

with inverse multiplication by `D^(-1)`. No choice of a hidden CRT sign is
used.

The soluble example can be made fully explicit with `N=221`, `g=-1`, and
`D=2`. Both `D` and `E=-2=219` have Jacobi symbol `-1`. The root `x=174`
maps to `z=2x=127 modulo 221`, and

\[
z^2=217=DE\pmod {221}.
\]

For the nonsoluble branch, take `N=77`, `g=-1`, and `D=3`. Then
`E=-3=74`, both discriminants have Jacobi symbol `-1`, and `DE=68=-9`.
A root of `DE` would map through `D^(-1)` to a root of `-1`, which does not
exist modulo 7 or 11. Pairing has not changed solvability in either case.

## 6. Complexity and scope

For one supplied hit, the procedure uses modular exponentiation, one or a
constant number of gcds, and public certificate checks. Its bit cost is
polynomial in the explicit input and provenance length. A quasipolynomial
number of candidates, each with quasipolynomial explicit length, still gives
quasipolynomial total cost. No enumeration of the cyclic subgroup is needed.

The theorem proves none of the following:

- an all-input factor-or-hit source;
- inverse-quasipolynomial hit density;
- a way to find `u` in (8);
- recursive availability of a new square root after each even-order doubling;
- a factoring algorithm;
- publication-level novelty relative to the literature.

The exact remaining source problem in Section 4 is therefore stated
correctly. A fresh statement-only reconstruction is still required before
promotion under the project protocol.
