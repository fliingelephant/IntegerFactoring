# F138 hostile audit — PASS AS NARROWLY CLAIMED

## Verdict

F138 passes as an auxiliary refutation result.

The result proves three narrow facts.

1. Reuse of a prime-parity row is controlled by an exact congruence between
   canonical carries.
2. A declared maximum-anchor presentation can contain a prime row that no
   other canonical exact value can reuse.
3. Reuse of every row in a selected matrix does not imply a binary
   dependency.

These facts refute the proposed shortcut from owner-pivot reuse to final
closure. They do not refute the complete F130/F132/F133 source. They do not
give a factoring algorithm.

I found no false mathematical claim within this scope.

## Artifacts checked

I read and checked:

- `RESULT.md`;
- all three preregistrations;
- all four pre-run pin files;
- the registered revision and both preserved failed-run records;
- all three Sage verifiers and all three JSON outputs;
- `RUN_QPOLY_MAX_DIGIT.log`; and
- `MANIFEST.md`.

I reran all three proof-enabled Sage verifiers. Each returned `PASS`. Each
JSON file was reproduced byte for byte. Every Boolean field in every output
is true. All 18 hashes recorded in the manifest match the current files.

The one-line maximum-digit run log contains `PASS` and has SHA-256

```text
c26de83abdc9496cd1301470918ec39ecca1cf389ef0ae1c6504da1800d1c431
```

The log is not pinned in the manifest. This is not an evidence gap because
the pinned JSON output is authoritative and was reproduced directly from
the pinned verifier.

Sage-generated `.sage.py` files are not pinned and are not evidence.

## F137 to F138 renumbering audit

The candidate originally used the label `F137`. It was mechanically
renumbered to `F138` after another experiment received that number. The
internal pre-run hashes therefore refer to the frozen `F137` text, while the
manifest records the current `F138` files.

I reversed exactly the text substitution `F138 -> F137` on the current
frozen sources. The reconstructed hashes are:

| Reconstructed frozen source | SHA-256 | Recorded pin |
|---|---|---|
| `PREREGISTRATION.md` | `f22bb90534eba71b4e0895808687cc0080886c74f253c43fb12ba9be88d2529a` | match |
| `verify.sage` | `9db2aa35ab3500252fb534198d6296e34b9fe7be9c97b2f039bc0854aa6d359a` | match |
| `PREREGISTRATION_NONZERO_ARM.md` | `570d0cc28641d1bb90ce29223d5d1e12e71f4f8f107786b3b430295acb6b50ef` | match |
| corrected `verify_nonzero_arm.sage` | `008da005fa560370cba9dc46ecd3b8deec3dec75669e0b0296bd6680ca36ee29` | match |
| `PREREGISTRATION_QPOLY_MAX_DIGIT.md` | `61891419ad5fc4e1b410b37a7e4d130536d74bf9481c7a0d8a1988c3afaeab70` | match |
| `verify_qpoly_max_digit.sage` | `f0a67ebe5d8f371da095a976f2cdaaf1da6eddce9f5a10024da43a37dc196658` | match |

I also reversed the one registered serialization correction in the
nonzero-arm verifier. Its reconstructed failed-source hash is

```text
b945dce61bda8434afd87b8b9c3e283de469c1cd127a9f75886ef21f4621fdfc
```

This matches the preserved failed-run record. The reconstructed revision
note and pre-retry failed-run record also match their pins. Thus the
renumbering changed only the experiment label and output path. It did not
change the preregistered arithmetic or the evidence.

## Theorem 1 audit — carry gate

For a canonical inverse pair,

\[
P_N(c)=c\iota_N(c)=1+\kappa N.
\]

The endpoint bound (1\le c,\iota_N(c)\le N-1) gives

\[
0\le\kappa\le N-2.
\]

For fixed (N), equality of exact values is therefore exactly equality of
carries. If a prime (r) divides two exact values, subtraction gives

\[
r\mid N(\kappa-\lambda).
\]

Since a prime divisor of (1+\kappa N) cannot divide (N), this is
equivalent to

\[
\kappa\equiv\lambda\pmod r.
\]

Odd valuation is still necessary in both columns. The result states this
condition. For anchored values, substitution of

\[
\kappa(b,A)=k_b+bA
\]

gives the stated cross-star congruence. I found no missing arithmetic
hypothesis.

## Theorem 2A audit — maximum integer anchor

The proof-enabled verifier establishes that the displayed (p,q,r) are
prime, (N=pq), (p<q<2p), and the input has

\[
n=400,\qquad L=9,\qquad E=2^{81}.
\]

Put (a=E), (c=2E), and (A=E-1). The verifier proves

\[
N\equiv1\pmod c,
\qquad
r=\frac{1+(c-1)N}{c},
\qquad
c^2+1<p<q.
\]

### Initial seed claim

Every initial seed satisfies (2\le s\le E+1<c). Hence

\[
0<s^2-1<s^2+1<c^2+1<p.
\]

Because (N=pq), the trial gcd and both sign gcds are one. The sign claim
uses the exact identities

\[
\gcd(s\mp\iota_N(s),N)=\gcd(s^2\mp1,N),
\]

valid after the trial gcd proves that (s) is a unit. Thus the claim covers
the complete initial seed interval without enumerating its
quasipolynomially many positions.

### Source membership and privacy

The prime block (2) must occur in the initial gcd-free block basis because
the literal endpoint (2) occurs. At the declared F133 integer anchor
(a=E), the derived carry digit is (A=E-1), and

\[
\iota_N(2)+AN=ar.
\]

Therefore the anchored endpoints are exactly (c=2E) and (r). Both are
below (N), and their value is

\[
cr=1+(c-1)N.
\]

The residue is outside the initial seed bank because (2E>E+1).

The privacy argument is complete. Since (r>(N-1)/2), the only positive
multiple of (r) below (N) is (r). Any canonical inverse value divisible
by (r) must therefore have endpoint (r). Its other endpoint is uniquely
(c). Exact-value deduplication leaves one column, and (r) has valuation
one in that column.

I also checked the stated duplicate boundary. The same residue is generated
in the first F130 frozen menu by the support-one word

\[
2^{82}=2E,
\]

whose exponent is allowed. Thus this certificate refutes universal
owner-row cancellation, but it does not prove that F133 introduces a
globally new exact value. `RESULT.md` states this limitation explicitly.

The certificate is conditional on execution reaching the named scan. It
proves only that the initial seed phase is null. It does not claim that all
earlier adaptive screens are null.

## Theorem 2B audit — prime anchor

The second proof-enabled verifier establishes primality, balance, the
400-bit parameter values, the complete initial-seed bound, and

\[
N\equiv1\pmod6,
\qquad
r=\frac{5N+1}{6},
\qquad
r>\frac{N-1}{2}.
\]

For block (2), anchor (3), and maximum digit (2), it verifies

\[
\iota_N(2)+2N=3r,
\qquad
P_N(6)=6r=1+5N.
\]

Both endpoint screens are one and (r) has valuation one. The same
complete-universe privacy proof applies.

Here (P_N(6)) is already the initial seed-(6) value. The anchored
presentation is literal, but it is not globally new. This does not
contradict the result: no global-newness claim is made, and the theorem is
used only against universal cancellation. It would not refute a theorem
restricted to globally new anchored values.

## Theorem 3 audit — reuse without a dependency

At (N=161), I reconstructed every inverse, exact value, factorization, and
sign screen in the four-column certificate. The complete odd-valuation row
sets are

\[
\{2,29\},\quad
\{2,13,31\},\quad
\{2,3,13\},\quad
\{3,29,31\}.
\]

The row degrees are (3,2,2,2,2), so every row is reused. The four columns
are nevertheless linearly independent over \(\mathbf F_2\). Their rank is
four and their right kernel has dimension zero.

This is exactly a selected-source counterexample. It does not describe all
canonical values at (N=161), and `RESULT.md` does not claim that it does.

## Accepted boundary

F138 does not establish any of the following:

- a complete-source terminal null;
- failure of every later F130 word screen;
- failure of every other kernel column;
- privacy of every owner row;
- an obstruction restricted to globally new F133 values; or
- a normalized-root obstruction after a kernel exists.

Its valid conclusion is narrower and useful: row multiplicity alone cannot
close the feedback route. A positive proof needs a carry collision pattern
that forces a final rank defect. It then still needs a non-global normalized
root.

