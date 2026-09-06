# F223 V2 fresh hostile re-audit

## Verdict

**PASS.** The five supplied V2 SHA-256 values match exactly. V2 repairs both
defects in the preserved V1 hostile FAIL. I found no remaining theorem-level
error, quantifier reversal, unsupported compatibility step, bit-complexity
gap, probability error, witness error, or scope inflation.

This is a conditional interface result. It is not a factoring algorithm. It
does not supply the compatible APR/CL certificate, a conditional drift law,
or a recursive all-input factorization procedure.

## Frozen-input integrity

I recomputed all five requested hashes before opening any V2 packet content.
Every expected and observed digest agrees byte for byte.

| Frozen input | Expected and observed SHA-256 | Result |
|---|---|---|
| `V2_STATEMENT.md` | `a5d38c57213a9c237723e2ea916ee2865f81cc8b086287728d493a07ebf2334c` | match |
| `V2_PROOF.md` | `290af2762069471b625442a851fd56b9e65d2db8964ee50ae3ab4a3832ea0e5a` | match |
| `V2_SELF_AUDIT.md` | `44e9d36889b7ac58c3cf2ff95ec560bd84b16b7daa1bc21df63536582a1dcdbb` | match |
| `V2_PROVENANCE.md` | `3b6dc93067e5f8a53ec641e686a210c9586fa0cba40367c310381ad28557a790` | match |
| `V2_MANIFEST.md` | `9fa00359d662b439c130a131be64d53df91933bab929d67da0a805e2b0a96f11` | match |

I then read the complete V2 statement, proof, self-audit, provenance, and
manifest, and the complete preserved V1 hostile audit. The observed digest of
the latter is

```text
ace81606d7d93a6f400431a9fb35094567cb730055f241541ab8bb40cdbc42cd  HOSTILE_AUDIT.md
```

It matches the preserved identity in V2. The five V1 packet identities listed
in `V2_PROVENANCE.md` also match their current files. I did not edit a frozen
input or a durable ledger.

## 1. Theorem A: local orbit and cross-q compatibility

**PASS.** For a prime `q` not dividing `N`, the character group of
`G_q=(Z/qZ)^*` separates points. Therefore one common integer `i` satisfying

\[
\chi(r)=\chi(N)^i
\]

for every character is equivalent to `r=N^i mod q`. The working exponents are
exactly one residue class modulo `h_q=ord_q(N)`.

For a finite bank, generalized CRT solves

\[
i\equiv i_q(r)\pmod {h_q}
\]

if and only if every pair agrees modulo the gcd of its two moduli. V2 keeps the
existential quantifier outside the character and auxiliary-prime loops. It
does not confuse independent local orbit membership with a single global
exponent. The case `q=2` correctly reduces to modulus one and adds no
condition.

## 2. Theorem B: exact Cohen--Lenstra hypotheses and conclusion

**PASS.** No matching primary paper was cached in the repository or local
search paths. I therefore checked the author-hosted primary paper directly:
[Cohen--Lenstra, *Primality Testing and Jacobi Sums*](https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1984a/art.pdf).

The exact source chain is as follows.

1. Theorem 6.3 assumes positive `t,s` satisfying (2.3), `n>1`, and
   `gcd(n,st)=1`. For every primary prime `p|t`, condition (6.4) says that for
   every prime divisor `r|n` there is one
   `ell_p(r) in Z_p` with

   \[
   r^{p-1}=(n^{p-1})^{\ell_p(r)}
   \quad\text{in }1+p\mathbf Z_p.
   \]

   The source remarks that this exponent is unique when it exists.
2. Theorem 7.8 applies to a character of order `p^k`. In addition to (6.4), it
   assumes the exact Gauss-sum congruence (7.9), a group-ring exponent
   satisfying (7.6), and an ideal satisfying (7.7). It concludes condition
   (6.5):

   \[
   \chi(r)=\chi(n)^{\ell_p(r)}
   \]

   for every divisor `r|n`. The exponent is the same value from (6.4); it does
   not depend on the character or on its auxiliary prime.
3. The selected primary characters `chi_{p,q}` generate the full character
   group at each auxiliary prime `q`. Theorem 6.3 combines the primary
   exponents and concludes, exactly,

   \[
   r\equiv n^i\pmod s
   \quad\text{for some }i\in\{0,1,\ldots,t-1\}.
   \]

Thus V2's opening instruction to use all hypotheses and notation of Theorems
6.3 and 7.8 is essential and sufficient. Its phrase “the relevant Gauss-sum
or Jacobi-sum tests pass” cannot be read as an arbitrary local pass; it means
the tests establishing the named hypotheses for every selected generator.
Under the statement's explicit scope, the attribution and conclusion are
exact.

The source's algorithm 11.1 also has the direction stated in V2: it checks all
selected character relations, separately establishes (6.4) for every `p|t`,
then invokes Theorems 7.8 and 6.3. There is no inference from unrelated local
exponents.

I also checked the cited primary APR paper directly:
[Adleman--Pomerance--Rumely, *On Distinguishing Prime Numbers from Composite Numbers*](https://math.dartmouth.edu/~carlp/PDF/paper37.pdf).
Equations (4.5)--(4.6) assemble the primary indices. Steps C.1--C.3 construct
the candidate divisor residue modulo the product of Euclidean primes. Step
C.4 tests the canonical candidate by integer division. Remark 4.1 says that a
composite passing all extraction tests is factored during consolidation, but
that composites are normally rejected before or during extraction. V2's
failure-semantics distinction is accurate: an earlier failed identity proves
compositeness but is not asserted to return a rational factor.

## 3. Theorem C: aggregate CRT and GFHP bit complexity

**PASS.** The V1 large-`tau` defect is fully repaired.

### The `tau>=n` branch

The canonical premise gives both `0<=b<2^tau` and
`0<p<N<2^n<=2^tau`. Since `p=b mod 2^tau`, uniqueness in the canonical
interval gives `b=p`. The algorithm compares the explicitly encoded `tau`
with `n` and computes `gcd(b,N)=p`. Here `b` has only `O(n)` value bits
because it equals `p`. It never constructs `2^tau`. Reading and comparing the
QP-bit encoding of `tau` remains numerical QP.

### The `tau<n` branch

Now `2^tau` and `b` have `O(n)` bits. Since `M|p-1`, also `M<N` and `M`
has `O(n)` bits. Hence

\[
L_0=\operatorname{lcm}(2^\tau,M)
\]

has `O(n)` bits. The true factor proves compatibility of the low-bit and
`1 mod M` congruences. For its guaranteed exponent `i_*`, it also proves
compatibility with `N^{i_*} mod S`, so the true residue modulo

\[
L=\operatorname{lcm}(L_0,S)
\]

is retained.

The coprimality proof is exact. If a rational prime `rho` divided both `M` and
`N`, condition (C3) applied to `rho|N` would give both `rho|M` and
`M|rho-1`, hence `rho|rho-1`, a contradiction. Thus `gcd(L_0,N)=1`, and
the separate premise `gcd(S,N)=1` gives `gcd(L,N)=1`.

The complete gcd-screen pass must precede GFHP calls. V2's statement orders
enumeration, gcd screening, and then application to the surviving residues,
and its proof uses exactly this ordering. On the true residue:

- if `L>p`, its canonical representative is `p`, so the screen returns the
  factor;
- `L=p` is impossible because `gcd(L,N)=1`;
- if no factor was returned, then `L<p<N`.

Because `tau>=1`, every retained representative is odd modulo `2^tau` and
is therefore positive. Consequently, after a factor-free complete screen,
every GFHP input has

\[
1\le s_i<L<N,
\qquad \gcd(L,N)=1.
\]

At the true exponent it also has `p=s_i mod L` and `p^1|N`.

I checked the current primary source directly:
[Gao--Feng--Hu--Pan, ePrint 2025/1004, revision 2025-11-11](https://eprint.iacr.org/2025/1004.pdf).
Theorem 3.1 takes natural `N,s`, a unit modulus `m in (Z/NZ)^*`, and
`s,m<N`. With `r=1`, it finds all prime divisors in the selected residue
class in

\[
O\!\left(
\left\lceil\frac{N^{1/4}}m\right\rceil
\log^{7+3\epsilon}N
\right)
\]

deterministic Turing-machine bit operations. Taking `m=L` matches every
premise above. If `L>=N^{1/4}/A(n)`, this cost is numerical QP.

The preprocessing bound also closes. `S` and every exponent have QP bit
length, `I` has QP size and is QP-enumerable, and `L` has at most the sum of
the bit lengths of `L_0` and `S`. Modular exponentiation, generalized CRT,
gcd screening, and at most QP GFHP calls therefore stay numerical QP. If a
candidate exponent is negative, `gcd(N,S)=1` permits the standard modular
inverse interpretation with the same bound.

No exact-order witness is used. Only the divisibility statement
`M|r-1` for every prime `r|N` enters the proof.

## 4. Theorem D: fixed bank, including `R=1`

**PASS.** For fixed `R>1`, `-1 mod R` is a reduced residue class. The prime
number theorem in that fixed arithmetic progression gives

\[
\pi(2X;R,-1)-\pi(X;R,-1)
\sim \frac{X}{\varphi(R)\log X},
\]

so every sufficiently large dyadic interval contains at least two such
primes. Choosing `u<v` gives `u<v<2u`. At each odd bank prime, `N=uv` is
`1`, while both factors are `-1`; the generated orbit is `{1}`, so neither
factor is accepted.

For `R=1`, the ordinary prime number theorem gives

\[
\pi(2X)-\pi(X)\sim X/\log X\to\infty,
\]

which supplies the same two-prime conclusion. This is the exact case omitted
from V1. At `q=2`, the unit group is trivial. V2 keeps the bank fixed before
choosing the factors and expressly excludes `N`-dependent, adaptive, and
refreshed banks.

## 5. Theorem E: accepted-product tails

**PASS.** For fixed `i` and `q`, `a_q^i` is one unit among `q-1`, so the
indicator parameter is exactly `1/(q-1)`. Independence is assumed only across
the sampled `U_q`. It gives the displayed moment product for `K_i`, and
Chernoff--Markov gives (E3) and (E5).

For

\[
W_i=\log P_i=\sum_q(\log q)I_{q,i},
\]

the moment factor is correctly

\[
1+\frac{q^\lambda-1}{q-1},
\]

not the unweighted `e^lambda` factor. Markov's inequality for every
`lambda>0`, followed by an infimum, proves (E7). A union bound over `T`
candidate exponents needs no independence between exponents. V2 labels this
as a probability model and never promotes it to an all-input distribution
theorem.

## 6. Theorem F: primary-prime-2 laws

**PASS.** In the cyclic group of order `u-1`, the `E`-power map has kernel
size `g_u=gcd(E,u-1)`. Thus the `+1` fibre has exactly `g_u` elements. The
`-1` fibre solves

\[
Ek\equiv (u-1)/2\pmod {u-1};
\]

it exists exactly when `g_u|(u-1)/2`, and then also has `g_u` elements. The
two fibres are disjoint. This proves (F4) and (F8), with the symmetric laws at
`v`.

CRT makes the two local components of a uniform unit independent. Therefore
(F5) is the exact union probability, while (F6) is the exact exclusive-or
probability and hence the exact proper-gcd probability.

The divisibility reduction is also exact:

\[
g_u\mid\gcd(N-1,u-1)=\gcd(v-1,u-1)=d,
\]

with the symmetric statement for `g_v`, and `d|v-u`. On a fixed bounded-gap
family this bounds each sign fibre by `O_H(1/u)` or `O_H(1/v)`. Since the
factors are balanced, the union is `2^{-n/2+O_H(1)}`. Equality
`g_u=g_v=d` is used only under the explicit extra hypothesis. No general
equality is claimed.

## 7. Exact witness

**PASS.** The two witness-artifact hashes match V2's manifest:

```text
d5eb0a272319d1d1dbd9314277464f39368f4e3d634d4de66b8ef82a17947c3f  verify_witness.py
8a352422599c9fb24d6344bcd0e28c77e8697fbb94197d5d8e368b30080de5fa  POSTHOC_OUTPUT.json
```

The frozen verifier completed successfully and reproduced
`POSTHOC_OUTPUT.json` byte for byte. It uses complete trial division through
the integer square root for both factors. It verifies

\[
32987\cdot32993=1088340091,
\quad Q=\{2,3,7,23,67\},
\quad \prod_{q\in Q}q=64722>\lfloor\sqrt N\rfloor=32989,
\]

and every displayed orbit. Both hidden residues lie in the orbit only at
`q=2`. This was the only mathematical computation in the re-audit. It was a
necessary exact witness check, not a search or a new experiment.

The provenance boundary is honest. The remote discovery scan is not frozen,
reproducible, or claimed as evidence. The local verifier is explicitly
post-hoc, and no asymptotic conclusion depends on it.

## 8. Quantifiers, source boundary, and recursion

**PASS.** The scopes remain separated:

- Theorem C assumes a certified compatible residue source; it does not build
  one.
- Theorem D applies only after a finite bank is fixed.
- Theorem E is an independent-uniform model, not an integer theorem.
- Theorem F analyzes the named uniform primary-2 anchor and does not exclude
  other anchors or correlated sampling.
- An APR/CL identity failure proves compositeness but need not expose a
  rational zero divisor.

There is no hidden recursive running-time claim. On the promised semiprime
input, a successful terminal returns one prime and exact division returns the
other. Extending the packet to arbitrary composites would require a separate
recursion and total-cost proof. The final “remaining core requirement” is
stated as missing work, not as a proved sufficiency theorem. In particular,
any future progress law must count strict growth in the aggregate terminal
information and remain inverse-QP after conditioning on the full prior
history.

## Exact defect list

None.

The V1 blocking large-`tau` encoding gap is closed by the canonical-residue
gcd branch. The V1 nonblocking `R=1` omission is closed by the ordinary prime
number theorem. All other attacked claims survive under their explicit
hypotheses.
