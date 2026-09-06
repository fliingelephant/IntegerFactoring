# F138 blind reconstruction

## Verdict

**PASS.** I found no counterexample to an exact mathematical claim in
`RESULT.md`. The carry gate, both 400-bit private-row certificates, both
complete initial-seed bounds, and the selected `N = 161` rank certificate all
reconstruct independently.

The source-position statements also pass at the level that can be established
from `RESULT.md`: every stated index is in its stated range, and every stated
source occurrence produces the claimed exact value. I did not inspect the
F130/F132/F133 implementations, so this reconstruction does not independently
certify that an external implementation has the source ranges described in
`RESULT.md`. That is an evidence boundary, not a mathematical counterexample.

## Evidence boundary and file ledger

I computed the input hash before reading its contents. It was the required
hash.

| File explicitly read | SHA-256 | Purpose |
|---|---|---|
| `/Users/zhou/autoresearch/IntegerFactoring/experiments/F138_owner_pivot_carry_gate/RESULT.md` | `f6ac31e00bbf81b67f4cc64137f108fbe2224b3c5ba629e32bbabab58f0832be` | Sole project input |
| `/private/tmp/f138_blind_check.sage`, first executed version | `87a3c4f18f7c6a7295cb798276288fc9f8381fbf115825653bbe6ee4204eee49` | Independent exact checks; stopped after the large certificates because a Sage `Factorization` object was compared directly with a list |
| `/private/tmp/f138_blind_check.sage.py`, generated from the first version | `3b147acaa9e8bfb579a6d536ae7dbe26edf1b045d7fb9333647d67e36f7e73d5` | Sage-generated Python read by the interpreter |
| `/private/tmp/f138_blind_check.sage`, second executed version | `7b00b5b689805f06533ee8ef1b3ce03abcb0ee742a619e7d292bb7247af26097` | Corrected container comparison; all assertions passed |
| `/private/tmp/f138_blind_check.sage.py`, generated from the second version | `fbb4c25a151aa61be669c8fc78cd741f10ec1b8e95dc6b041c6a3b6ab73883eb` | Sage-generated Python read by the interpreter |
| `/private/tmp/f138_blind_check.sage`, final executed version | `668b28915f103c95eb44e1d1e427665419c81f26cebf5585d0760deec4c26217` | Added explicit checks of `L`, `E`, and the prime-anchor position; all assertions passed |
| `/private/tmp/f138_blind_check.sage.py`, generated from the final version | `a765a2a2d05d6084cccedadd7929c321652b665f3d737d110bf653d76682419e` | Sage-generated Python read by the interpreter |

No other project file was opened. SageMath necessarily loaded its installed
runtime and libraries; those system files were execution dependencies, not
project evidence. The Sage state directory was redirected to
`/private/tmp/f138_sage_state`.

The material commands were:

```text
shasum -a 256 /Users/zhou/autoresearch/IntegerFactoring/experiments/F138_owner_pivot_carry_gate/RESULT.md
cat /Users/zhou/autoresearch/IntegerFactoring/experiments/F138_owner_pivot_carry_gate/RESULT.md
command -v sage
shasum -a 256 /private/tmp/f138_blind_check.sage
env DOT_SAGE=/private/tmp/f138_sage_state sage /private/tmp/f138_blind_check.sage
shasum -a 256 /private/tmp/f138_blind_check.sage.py
env DOT_SAGE=/private/tmp/f138_sage_state sage --version
```

The script was created and revised with `apply_patch`. The first Sage run
proved both large-number certificates and then stopped at the non-mathematical
container comparison. The corrected and final runs ended with
`ALL ASSERTIONS PASSED`. The runtime was SageMath 10.9. It ran with
`proof.all(True)`, and every large primality test explicitly used
`is_prime(proof=True)`.

## 1. Exact carry and cross-star gate

Let `w = iota_N(c)`. The canonical representatives satisfy

\[
1\le c,w\le N-1,
\qquad cw\equiv1\pmod N.
\]

Hence `cw = 1 + kappa N` for an integer `kappa`. The endpoint bound gives

\[
1\le cw\le (N-1)^2=1+(N-2)N,
\]

so `0 <= kappa <= N-2`. Equality of two exact values is equivalent to
equality of their carries because

\[
1+\kappa N=1+\lambda N\iff\kappa=\lambda.
\]

After exact-value deduplication, one column remains for each retained carry.
Therefore the parity-row degree is exactly

\[
\deg(r)=\#\{\kappa\in\mathcal K:
v_r(1+\kappa N)\equiv1\pmod2\}.
\]

Suppose a prime `r` divides the values for two distinct retained carries
`kappa` and `lambda`. It cannot divide `N`, because it divides
`1 + kappa N`. Subtraction gives

\[
r\mid N(\kappa-\lambda),
\]

and invertibility of `N` modulo `r` gives
`kappa = lambda (mod r)`. Conversely, if `r` divides the first value and the
two carries are congruent modulo `r`, then it divides the second value. Odd
valuation in each value is exactly the remaining parity condition.

For a star with `bw_b = 1 + k_b N`, direct expansion gives

\[
b(w_b+NA)=1+(k_b+bA)N.
\]

Thus `kappa(b,A) = k_b + bA`, and two retained star columns can share row `r`
only through

\[
k_b+bA\equiv k_d+dB\pmod r,
\]

with odd valuation in both. “Two retained columns” is material here: equal
carries are one exact value and are removed by deduplication. This condition
is already implicit in the distinct-column premise in `RESULT.md`.

## 2. Certificate 2A

### Independent arithmetic and primality

Proof-mode Sage verified all of the following:

- the displayed `N` is exactly `p*q`;
- `p`, `q`, and `r` are prime;
- `p < q < 2p`;
- `N.nbits() = 400`;
- `400.nbits() = 9` and
  `2^(9^2) = 2^81 = 2417851639229258349412352`;
- for `c = 2E = 2^82`, `N mod c = 1`;
- the displayed `r` is exactly
  `(1 + (c-1)N)/c`;
- `c^2 + 1 < p < q`;
- both endpoint sign gcds are one; and
- the valuation of `r` in `cr` is one.

The displayed values of `N` and `r` were compared as exact integers, not as
decimal approximations.

### Complete initial seed bank

For every stated initial seed `2 <= s <= E+1`,

\[
s<E+E=c<p<q
\]

and, more sharply,

\[
0<s^2-1<s^2+1<c^2+1<p<q.
\]

Thus neither prime factor of `N` divides `s`, `s^2-1`, or `s^2+1`.
Consequently every trial gcd is one. Since `s` is a unit and
`sw_s = 1 (mod N)`, multiplication by `s` modulo `N` gives

\[
\gcd(s-w_s,N)=\gcd(s^2-1,N),\qquad
\gcd(s+w_s,N)=\gcd(s^2+1,N).
\]

Every endpoint sign screen in the complete stated seed interval is therefore
one. This is a universal bound, so no enumeration of the enormous interval is
needed.

### Max-digit source position and exact value

The stated integer-anchor range includes `a = E`, and its digit range includes
the maximum digit `A = a-1`. With `b = 2` and
`w_2 = (N+1)/2`,

\[
\begin{aligned}
H
 &=\frac{N+1}{2}+(E-1)N\\
 &=\frac{1+(2E-1)N}{2}\\
 &=E\,\frac{1+(2E-1)N}{2E}=ar.
\end{aligned}
\]

Thus the anchored endpoints are exactly `ab = 2E = c` and `H/a = r`, and

\[
P_N(c)=cr=1+(c-1)N.
\]

They lie in `[1,N-1]` and are mutual canonical inverses. The residue is beyond
the initial seed range because `c = 2E > E+1`. It is also the stated
support-one word because `2^82 = 2E`, and `82 < E`. Therefore, under the
source ranges stated in `RESULT.md`, the F130 occurrence and later F133
occurrence have the same exact value and global deduplication retains only one
copy. Also, `a = 2^81` is composite, so no prime-anchor width premise is being
used for this arm.

### Sign screens and complete-universe privacy

For either prime factor `t` of `N`, `cr = 1 (mod t)`. If `t` divided
`c-r` or `c+r`, multiplication by `c` would make `t` divide respectively
`c^2-1` or `c^2+1`. Both are positive and smaller than `p <= t`. Hence both
sign gcds are one.

The exact identity

\[
r=N-\frac{N-1}{c}>\frac{N-1}{2}
\]

shows that `r` is the only positive multiple of itself below `N`. If a
canonical exact value `xy`, with `1 <= x,y < N`, is divisible by the prime
`r`, one endpoint must therefore equal `r`. Its inverse is uniquely `c`, so
the exact value must be `cr`. Since `r` does not divide `c`, its valuation in
that value is one. Exact-value deduplication consequently gives
`deg(r) = 1` in the complete canonical-inverse universe.

This proves the claimed permanent private row. It does not prove that an
execution reaches the F133 scan, that no earlier word factors `N`, or that the
certificate is globally new at F133. `RESULT.md` expressly excludes those
stronger conclusions.

## 3. Certificate 2B

### Independent arithmetic and primality

Proof-mode Sage independently verified:

- the displayed `N` equals `p*q` exactly;
- `p`, `q`, and `r` are prime;
- `p < q < 2p` and `N.nbits() = 400`;
- `N mod 6 = 1`;
- the displayed `r` equals `(5N+1)/6` exactly, so `6r = 5N+1`;
- `(E+1)^2+1 < p < q` for the displayed `E = 2^81`;
- both endpoint sign gcds are one; and
- the valuation of `r` in `6r` is one.

### Complete initial seed bank

For every `2 <= s <= E+1`,

\[
0<s^2-1<s^2+1\le(E+1)^2+1<p<q.
\]

The same unit-multiplication identities proved in Certificate 2A show that
all initial trial gcds and all initial endpoint sign gcds are one. This proves
the complete stated initial seed-null claim. It says nothing about later F130
words, exactly as `RESULT.md` states.

### Prime-anchor position, screens, and privacy

Because `N = 1 (mod 6)`,

\[
w_2=\frac{N+1}{2}\equiv1\pmod3,
\qquad N\equiv1\pmod3.
\]

For the digit range `A in {0,1,2}`, divisibility of `w_2+AN` by `3` is
therefore equivalent to `1+A = 0 (mod 3)`. The unique eligible and maximum
digit is `A=2`. Directly,

\[
H=w_2+2N=\frac{5N+1}{2}=3r.
\]

The anchored endpoints are consequently `c = 3*2 = 6` and `H/3 = r`, and

\[
P_N(6)=6r=1+5N.
\]

The sign-screen proof from Certificate 2A applies with `c=6`; here
`c^2+1=37<p`. Finally,

\[
r=\frac{5N+1}{6}>\frac{N-1}{2}.
\]

The same below-`N` multiple argument forces every canonical exact value
containing row `r` to be the deduplicated value `6r`. Its valuation is one,
so `deg(r)=1` in the complete canonical-inverse universe. Because the
F130/F132/F133 values described in `RESULT.md` are all members of this
universe, none of them can supply a distinct column that cancels this row.

This proves universal owner-pivot cancellation false. It does not imply that
the rest of the selected matrix has zero kernel.

## 4. The `N = 161` certificate

Sage factored `161 = 7*23`. Exact multiplication gives

\[
10(145)=1450=1+9(161),
\]
\[
26(31)=806=1+5(161),
\]
\[
32(156)=4992=1+31(161),
\]
\[
87(124)=10788=1+67(161).
\]

All endpoints lie in `[1,160]`; hence each second endpoint is the unique
canonical inverse of the first. The absolute difference and sum pairs used
by the sign screens are

\[
(135,155),\ (5,57),\ (124,188),\ (37,211),
\]

and every gcd with `161` is one.

The four exact factorizations independently reconstruct as

\[
1450=2\cdot5^2\cdot29,
\quad806=2\cdot13\cdot31,
\]
\[
4992=2^7\cdot3\cdot13,
\quad10788=2^2\cdot3\cdot29\cdot31.
\]

Removing even exponents gives exactly the five-row matrix in `RESULT.md`.
Its row degrees are `(3,2,2,2,2)`, so no parity row has degree one.

Over `GF(2)`, the row equations for rows `13`, `3`, and `29` give

\[
x_2=x_3=x_4=x_1.
\]

The row for `2` then gives `x_1+x_2+x_3=x_1=0`, so all four coordinates
vanish. Sage independently returned rank `4` and right-nullity `0`.
Therefore complete row reuse does not imply a nonzero kernel.

This is only a selected four-column canonical certificate. It makes no claim
about every presentation or every source column at `N=161`.

## 5. Missing conditions and scope audit

For a parity matrix with one column per distinct retained exact carry, a
nonzero kernel exists exactly when

\[
\operatorname{rank}M_{\mathrm{final}}
<\#\{\text{distinct retained exact carries}\}.
\]

The `N=161` matrix proves that minimum row degree two, complete reuse of its
rows, and a nonempty incidence 2-core do not force this inequality. Thus the
two gates in `RESULT.md` are genuinely separate:

1. another distinct retained carry must hit each required owner residue class,
   with odd valuation; and
2. the resulting columns must have an actual rank defect.

Even a nonzero parity kernel only supplies a congruence of squares. A factor
still requires a non-global root; a root congruent to `+1` or `-1` modulo all
of `N` gives only a trivial gcd. Thus the stated need for a separate
non-global-root theorem is correct.

The two large certificates do **not** prove a complete-source obstruction.
They do not exclude a factor from an earlier or later screen, and they do not
exclude a useful kernel formed by other columns. Certificate 2A also does not
refute a claim restricted to globally new F133 values, because its stated
F133 value duplicates its F130 support-one value. The `N=161` example only
refutes the bare logical implication from row reuse to dependency. These are
exactly the limitations stated in `RESULT.md`.

The historical summaries of P111, P112, P120/X73, P122/X74, and F135, and
the claims about what a registered verifier previously did, were not used as
evidence. The task prohibited reading those artifacts. Every arithmetic fact
attributed to that verifier and needed by the two certificates was instead
checked independently in proof-mode Sage.
