# F157-D01 V2 hostile re-audit — PASS

## Verdict

**PASS.** V2 repairs exactly the V1 public-locator scope error. It changes no
registered source, input, arithmetic output, count, finite null, or public
certificate.

The exhaustive support-two scan declared by F156 is already public and
quasipolynomial. The disclosed factors are used only by the registered fast
index. They are not needed to construct or test a support-two candidate.

The exact surviving result is:

- one fixed 32-bit input has 65 proper support-two pairs;
- four fixed 58-bit inputs have no proper pair at support at most two;
- the positive fixed input has a public quasipolynomial locator by exhaustive
  F156 pair enumeration;
- there is no all-input success theorem, density law, polynomial-time
  factoring result, public selector asymptotically smaller than exhaustive
  enumeration, or claim that the public exhaustive scan finishes in 900
  seconds.

I found no remaining arithmetic, completeness, disclosure, or scope defect.

## Frozen inputs and history

I read all 16 top-level F157 files that existed before this report. I treated
the 1,341 Sage cache files and two Python cache files as unregistered runtime
state, not evidence.

The two supplied V2 hashes match:

| V2 file | SHA-256 |
|---|---|
| `V2_RESULT.md` | `a6278bc71959396e7dbb745c2dbce18f2a4c1df0fffc5c8b5cd09c9daf87b3d4` |
| `V2_MANIFEST.md` | `13d4f5517a27e027c1b145b5c57db8900ba4ebeec9b816828bbd10d6ffd6e75f` |

All six preregistered file hashes match `REGISTRATION.json`. All four
post-run hashes match the original manifest. All seven upstream pins in
`INPUT.json` match their current files, including the pinned F156 statement
and proof:

```text
F156_STATEMENT.md  d426df6c293fd835c85260b14fb6ddd57a99ff812a4c7b9a74b084318ed34527
F156_PROOF.md      4024a5d8732ffec5dea0711498bf77e0accfc079868fecc82ace56c91243169d
```

The preserved history is intact:

| History file | SHA-256 |
|---|---|
| `MANIFEST.md` | `e14072aa78d0922480bf097e91884f8f5c774e9d8f8375250bb4ca59c435ebc2` |
| `V1_MANIFEST.md` | `e14072aa78d0922480bf097e91884f8f5c774e9d8f8375250bb4ca59c435ebc2` |
| `HOSTILE_AUDIT.md` | `e897bc1ead3989703f1b9d9d1e46e5fec91194ffdfe751891cd41d8803683b5e` |
| `HOSTILE_AUDIT_FAILED.md` | `e897bc1ead3989703f1b9d9d1e46e5fec91194ffdfe751891cd41d8803683b5e` |

The two manifest files are byte-identical. The two hostile-audit files are
byte-identical. The failed audit says that the computation, certificate,
finite nulls, hashes, and factor-assisted index passed. It fails only the two
V1 sentences that deny an existing public quasipolynomial locator.

I did not rerun the full five-input experiment. After checking the preserved
audit hash and all frozen evidence hashes, I used its replay only for runtime
corroboration. The authoritative runner time was `167.38698695900166`
seconds. The preserved isolated replay time was `165.508371` seconds. Both
are below the registered 900-second limit.

## V2 changes only the failed claim boundary

The V1 and V2 arithmetic sections are unchanged. The verdict, five table
rows, first certificate, factor split, 65-pair count, and candidate hash are
the same. V2 adds version metadata and replaces only the locator and remaining
problem discussion.

The two failed V1 claims were:

> It does not give a public method to locate the successful pair.

> The remaining source-side problem is to replace the disclosed
> factor-assisted index with a public quasipolynomial selector.

V2 removes both claims. It now distinguishes three things precisely:

1. exhaustive public F156 enumeration already locates the fixed positive
   pair in quasipolynomial time;
2. the disclosed factors accelerate the registered finite classification;
3. the open questions are an all-input progress law and a substantially
   faster public selector.

This is the exact repair required by the failed hostile audit.

## The exhaustive support-two locator is public

The pinned F156 statement defines

\[
n=\lceil\log_2(N+1)\rceil,
\qquad
L=\lceil\log_2(n+1)\rceil,
\qquad
D=L^2.
\]

It then enumerates every nonempty subset of the public relation basis with
support at most `D`. For these five inputs, `n` is 32 or 58. In both cases,
`L=6` and `D=36`. Every support-two pair is therefore in the declared menu.

The basis candidates are public. Each base relation has an exact
factor-free presentation

\[
A_i=t_i^2Q(v_i)\equiv1\pmod N,
\]

so its retained actual lift is

\[
e_i=(v_i,t_i^{-1}).
\]

For two basis lifts, let `C` be the product of their common public blocks.
Their star-product is

\[
(v_i,z_i)\star(v_j,z_j)
=
(v_i\mathbin{\mathrm{xor}}v_j,\ z_i z_j C^{-1}\bmod N).
\]

The inverse endpoint and both screens use only modular inversion and gcd with
the public `N`. They use neither disclosed prime factor nor a hidden CRT sign.

F156 bounds the base rank by

\[
r\le 2^{O(L^4)}
\]

and the complete declared source by `2^{O(L^6)}`. Exhaustive support-two
enumeration has `r(r-1)/2` candidates. Squaring a quasipolynomial quantity is
still quasipolynomial. Thus the pair scan is a public quasipolynomial locator
on the fixed positive input.

This conclusion does not depend on the later F156 V2 wording repairs. The
two F156 files pinned by F157 already state the nonempty support-at-most-`D`
menu, the public decorated product, and the stated cost bound. The later
F156 repairs concern stage order and the inert identity element. Neither
removes or changes any support-two candidate on this fixed frozen base
ledger.

## The disclosed factors only accelerate the registered implementation

The registered source constructs the base ledger, factor-free blocks, parity
basis, actual lifts, and support-one screens before it uses `p` or `q`. The
factors enter `scan_feedback` only to build the support-two lookup index.

For a pair with common-block product `C`, its direct screen has sign
`epsilon` modulo a disclosed prime `r` exactly when

\[
Q_j=\epsilon C^2/Q_i\pmod r.
\]

The registered index uses this equality only to avoid replaying billions of
public pairs:

- a pair with a common light block is enumerated once under its least common
  light block;
- otherwise all common blocks are heavy, and the exact common set occurs as
  one enumerated subset of the left record's heavy blocks;
- an equality modulo exactly one of the two distinct prime factors is exactly
  a proper gcd screen for these fixed semiprimes;
- an equality modulo both factors gives only the improper gcd `N` and is
  discarded.

The two cases are disjoint and cover every unordered pair, including an empty
intersection. Every retained key is then reconstructed by the public star law
and tested by ordinary gcd. The index found 65 candidates on the first input
and none on the other four. It retained no key without a proper public gcd.

Therefore the factor-assisted index proves the complete fixed-corpus
classification efficiently. It is not the public locator itself. The public
locator is exhaustive F156 enumeration. V2 states this distinction exactly.

## Independent first-certificate reconstruction

I independently rebuilt the first F111 base ledger and its public
multiplicity-aware factor-free basis. Basis indices `(253,9723)` select source
columns `(253,9729)`. Their common block indices are `(0,1,23)`, with values
`(2,3,89)`. Hence

\[
C=2\cdot3\cdot89=534.
\]

The two exact public relations reconstruct as

```text
A_left  = 229474381530244008 = 2^2   * 57368595382561002
A_right = 734499429781561344 = 192^2 * 19924572205446
```

Their actual lifts are `1620816237` and `2549408872`. Direct application of
the public star law gives

```text
z = 1620816237 * 2549408872 * 534^(-1) mod N
  = 3183314832
w = z^(-1) mod N
  = 205056
z*w mod N = 1
z^2 mod N = 1509286823
gcd(z - w, N) = gcd(z^2 - 1, N) = 41011
gcd(z + w, N) = gcd(z^2 + 1, N) = 1
N / 41011 = 79043
```

This reconstruction uses the public blocks and actual lifts. The displayed
factor is an output of the gcd, not an input to the construction.

## Independent counts and certificate arithmetic

I recomputed every support-two count as `r*(r-1)/2` and every null count as
the full pair count minus the proper-hit count.

| `N` | `r` | Recomputed pairs | Hits | Recomputed nulls |
|---:|---:|---:|---:|---:|
| 3,241,632,473 | 11,874 | 70,490,001 | 65 | 70,489,936 |
| 204,800,061,759,986,701 | 106,937 | 5,717,707,516 | 0 | 5,717,707,516 |
| 204,800,066,879,973,329 | 80,446 | 3,235,739,235 | 0 | 3,235,739,235 |
| 204,800,093,759,919,353 | 65,005 | 2,112,792,510 | 0 | 2,112,792,510 |
| 204,800,123,199,900,673 | 91,979 | 4,230,022,231 | 0 | 4,230,022,231 |
| **Total** | **356,241** | **15,366,751,493** | **65** | **15,366,751,428** |

The public-block total is `446,394`. The support-one total is `356,241`, and
all support-one hit lists are empty.

I also rechecked every serialized support-two hit in `OUTPUT.json`:

- every basis pair is ordered, in range, and unique;
- `z*w = 1 mod N` and `z^2 = q_mod_N mod N`;
- both reported gcds and both dense-screen gcd identities match;
- every hit contains a proper factor;
- 63 hits expose `41011`, and two expose `79043`.

Re-encoding the 65 sorted pair keys with the registered length-prefixed
integer format gives

```text
ef54beec77babbcd82ea9e9833c24216bf4e6ac4603811c6a8abb160e15eca3d
```

The four empty candidate lists also reproduce their registered empty-list
hash.

## Exact claim boundary

V2 proves a public quasipolynomial path only for the fixed positive witness,
because the finite evidence proves that this witness has a successful pair.
Exhaustive enumeration is public and quasipolynomial on every input in the
declared source, but F157 does not prove that it finds a factor on any new
input.

The four nulls are exact only for the registered frozen ledgers and support at
most two. They do not constrain larger support, later feedback stages, or new
inputs.

The remaining theoretical problem is an all-input success or progress law.
The remaining practical problem is a public selector substantially faster
than exhaustive enumeration. V2 neither conflates those problems nor claims
that either is solved.

I did not edit a V1 or V2 input, a registered artifact, `REGISTRY.md`, or a
durable ledger.
