# F157 V2 blind reconstruction

## Verdict

**PASS.**

The displayed certificate is arithmetically valid. The declared F156 public
menu includes its support-two pair. Exhaustive public pair enumeration is
quasipolynomial. The 167.39-second registered run and the public exhaustive
locator are different algorithms with different performance claims. The
positive and null conclusions are finite, fixed-input conclusions only.

This verdict checks the claims that can be reconstructed from the two
permitted documents. It does not replay the registered enumeration. In
particular, the permitted evidence does not contain the basis records or the
65-pair list, so it cannot independently authenticate the pair provenance,
the value `C = 534`, the other 64 hits, or the four empirical null scans.

## Blind-input boundary and hash correction

I read only:

- `F157_sparse_section_feedback_capability/V2_RESULT.md`, SHA-256
  `a6278bc71959396e7dbb745c2dbce18f2a4c1df0fffc5c8b5cd09c9daf87b3d4`;
- `F156_sparse_section_feedback_source/V2_STATEMENT.md`, SHA-256
  `71b640469c0f57440d8e290b63af411eb33ee08b08c814413b5a04fff1c7d3dc`,
  and only for its declared public-source and cost interface.

The initially supplied expected hash for the second file was
`d426df6c293fd835c85260b14fb6ddd57a99ff812a4c7b9a74b084318ed34527`.
The file did not match it, so I stopped before reading. The coordinator then
confirmed that the promoted V2 statement has hash `71b640...` and that
`d426...` belongs to the preserved V1 statement. I proceeded only after that
explicit correction. I read no other F157 artifact, audit, output, proof,
manifest, ledger, or prior reconstruction.

## 1. Displayed factor certificate

For

```text
N = 3241632473
z = 3183314832
w = 205056
p = 41011
q = 79043
```

direct integer arithmetic gives

```text
p*q                  = 3241632473 = N
z*w                  = 652757806190592
(z*w - 1)/N          = 201367 exactly
z*w mod N            = 1
gcd(z - w, N)        = 41011
gcd(z + w, N)        = 1
N/41011              = 79043, with remainder 0
```

Trial division through each square root also confirms that `41011` and
`79043` are prime. Thus `w` is the displayed modular inverse of `z`, and the
minus screen exposes the proper factor `41011`. This certificate alone gives
an unconditional factorization of the displayed `N`.

The certificate does not, by itself, prove that `z` came from basis indices
`(253, 9723)`, source columns `(253, 9729)`, or common-block product `534`.
Those are provenance claims. They require the forbidden basis/output data to
replay. The indices are at least range-consistent with the reported rank
`11874` and public-block count `13284`.

## 2. Public support-two inclusion

The F156 interface defines

```text
n = ceil(log2(N + 1))
L = ceil(log2(n + 1))
D = L^2
```

and scans every nonempty subset of the retained relation basis with support
at most `D`. Direct calculation gives `n = 32`, `L = 6`, and `D = 36` for
the positive input. Each of the four other displayed inputs gives `n = 58`,
`L = 6`, and `D = 36`.

The indices `253` and `9723` are distinct and below the displayed positive
rank `11874`. Their two-element set therefore belongs to the declared F156
menu because `2 <= 36`. F156 constructs its decorated star product, computes
the canonical inverse, and applies both gcd screens. A deterministic
factor-free enumeration must consequently find a proper factor no later than
this pair, provided the displayed pair provenance is correct. It does not
need `p` or `q` to do so. The claim that this is the *first* proper pair is an
empirical ordering claim and is not replayable from the two permitted files.

The table is combinatorially consistent. For ranks

```text
11874, 106937, 80446, 65005, 91979
```

the exact unordered-pair counts `r(r-1)/2` are

```text
70490001, 5717707516, 3235739235, 2112792510, 4230022231.
```

They match every table row and sum to `15366751493`. The ranks sum to
`356241`, matching the reported support-one total. This verifies the count
arithmetic, not the reported hit/null classification of those candidates.

## 3. Quasipolynomial closure

F156 declares a total base-record bound

```text
r <= R0 = 2^{O(L^4)}.
```

Therefore

```text
binom(r, 2) <= r^2/2 = 2^{O(L^4)}.
```

The equality of asymptotic classes is exact: if `r <= 2^(c L^4)`, then
`r^2 <= 2^(2c L^4)`. Squaring changes only the hidden constant. Because
`L = Theta(log n)`, this is quasipolynomial in the input bit length `n`.

F156 separately bounds construction of the public source, endpoint work,
storage, and final decoding by `2^{O(L^6)}`. Rebuilding the basis and then
testing all pairs is thus bounded by `2^{O(L^6)}` overall. The stronger F156
menu already scans every support through `D = L^2`; support two is only a
subset of that declared quasipolynomial computation.

This establishes an asymptotic public locator. It does not establish that a
literal exhaustive pair scan meets the experiment's 900-second limit.

## 4. Registered acceleration versus public location

The distinction is coherent and must remain explicit:

1. The registered finite classifier used the disclosed factors to index
   pairs and reject cases that can yield only an improper gcd. Its reported
   167.39-second runtime and complete five-input classification belong to
   that factor-assisted run.
2. Each retained candidate was reportedly rebuilt from the public basis and
   checked by a direct gcd. This makes each displayed hit publicly
   checkable, but it does not turn the candidate-selection index into a
   factor-free procedure.
3. The public locator is the separate exhaustive algorithm declared by
   F156: rebuild the deterministic public basis, enumerate all unordered
   pairs, and run the two direct gcd screens. It needs no factors, but V2
   makes no 900-second claim for it.

Thus factor assistance accelerates the registered completeness experiment;
it is not needed for the theoretical public location of the displayed
support-two witness. Conversely, existence of the exhaustive public locator
does not retroactively make the timed registered run factor-free.

## 5. Exact finite scope

The positive evidence concerns only `N = 3241632473`. It proves that one
declared support-two operation can expose a factor on that fixed input. It
does not prove success on a new input, a positive success frequency, a useful
pair density, an all-input progress law, polynomial-time factoring, or a
public selector smaller than exhaustive enumeration.

The negative evidence concerns only the four displayed 58-bit inputs and
only the reported support-at-most-two classification. The empty support is
inert under the F156 interface, support one was reported null, and every
unordered support-two pair was reported null. This does not exclude success
at supports `3` through `36`, at another stage or input, or through another
F156 success channel. It is not a null theorem for the full F156 source and
not an asymptotic obstruction.

The claims therefore survive the requested attack only with this narrow
boundary and with the empirical provenance/completeness limitations stated
above.
