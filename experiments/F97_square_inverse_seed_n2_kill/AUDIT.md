# F97 hostile audit

## Verdict: **PASS**

The current F97 candidate passes strict whole-artifact audit. The family
selection, stable certificate, exhaustive target-free menu, complete-subgroup
claim, zero distinct same-class result, and positive control all reproduce
independently. The implementation keeps factor data out of the per-input
selector. The timeout, logs, output, manifest hashes, and stated scope are
consistent.

I found no false or materially misleading claim in the pinned candidate.

## 1. Pinned snapshot and protocol

I pinned these SHA-256 hashes before reading the files:

```text
5acc26288f11048a69c5d5f43cc72eaf2178e3f56d25ef3329583c07ab34a659  OUTPUT.json
5db670600ff70bda37daf439c90f3183793e28969cc5de2e1f3c32c40ea92ab9  RECONSTRUCT_STATEMENT.md
c598e7f28cd35e81aba3c92af9232da2605f1a1ed8434ef537339870da860d99  RESULT.md
00208af4720055de2ce17dcdbef450dff7f961f72b5b3fe6e6aea51ae6ffdf41  RUN.log
16790b33e7e2c0ecddd67cb2b77b47d29fd9dae13d763903df4eb32b8e75d42e  RUN_MANIFEST.md
41f13b22b37facef4a915ad41606f0917e1175bb0853f2946ce4302d49426358  run_with_timeout.py
859c4d956df08050fdc803249775bdb481b786ee1734633262c63bb3edec84aa  search_square_inverse_seed_family.py
```

I then read all seven files completely. I did not use a prior `AUDIT.md` or
`RECONSTRUCT_RESULT.md`; neither was in the pinned file set.

For the arithmetic replay, I wrote a separate Sage/Python enumerator. It
constructed the family, pair stream, canonical inverse relation, exact-square
test, and subgroup orbit independently. It did not import or call the
candidate source. A final rehash reproduced the same seven hashes.

## 2. Family selection and stable certificate: PASS

Independent factorization gives:

| \(x\) | \(N_x=(3x^2-1)/2\) | Factorization |
|---:|---:|---|
| 3 | 13 | prime |
| 5 | 37 | prime |
| 7 | 73 | prime |
| 9 | 121 | \(11^2\) |
| 11 | 181 | prime |
| 13 | 253 | \(11\cdot23\) |

Thus the first distinct odd semiprime in the declared increasing odd-\(x\)
order is \(x=13\). There is no earlier eligible input whose stability or menu
result was skipped.

For \(N=253\), independent arithmetic gives

\[
g=\gcd(10,22)=2,\qquad A=5,\qquad B=11,
\]

\[
\gcd(AB,N-1)=\gcd(55,252)=1.
\]

The product check \(11\cdot23=253\) also passes. The selection trace and all
reported counts follow: six family inputs examined, five rejected by the
distinct-odd-semiprime filter, zero rejected as unstable, and one stable input
tested before the stop.

## 3. Seed and exhaustive menu at 253: PASS

For odd \(x\), the identity

\[
3x^2=1+2N_x
\]

shows that \(x^2\) is the inverse of 3 modulo \(N_x\). Also
\(x^2<N_x\) for every odd \(x\ge3\), so this is the least positive inverse.
At \(x=13\), the exact values are

\[
3^{-1}_{\rm can}=169=13^2,
\qquad P_1=3\cdot169=507=1+2\cdot253.
\]

The independent menu used \(n=8\), bound \(n^2=64\), and every pair in
\([0,64]^2\). It reproduced:

| Check | Independent result |
|---|---:|
| exponent pairs | 4,225 |
| distinct exponent pairs | 4,225 |
| first-occurrence residues | 110 |
| distinct values \(P\ne P_1\) in the square class of \(P_1\) | 0 |
| global-sign collisions | 0 |
| useful closures | 0 |

The pair stream is exactly increasing \(a+b\), then increasing \(a\). It
starts at \((0,0)\), ends at \((64,64)\), and contains each bounded pair
once. The candidate exhausts the stream before returning `finite_null`.

The four residues whose canonical relation merely repeats the old value are

\[
c\in\{3,13,39,169\},\qquad c\,c^{-1}_{\rm can}=507.
\]

Every other visited residue fails the exact-square test for \(P_1P\). Thus
the reported zero is a zero of distinct relation values, not an accidental
failure to encounter another presentation of the seed relation.

## 4. Complete-subgroup certificate: PASS

The seed identity gives

\[
3=13^{-2}\pmod{253},
\]

so every menu word lies in \(H=\langle13\rangle\). Independently,

\[
\operatorname{ord}_{11}(13)=10,
\qquad
\operatorname{ord}_{23}(13)=11,
\]

and therefore

\[
\operatorname{ord}_{253}(13)=\operatorname{lcm}(10,11)=110.
\]

I compared sets, not only counts: the 110 first-occurrence menu residues are
exactly the 110 powers in \(\langle13\rangle\). A separate direct census of
all 110 subgroup elements again found the four presentations of \(P_1\) and
no distinct relation in its square class.

Because a canonical inverse relation is determined by its residue, increasing
the exponent bound cannot create a new one-step relation while the source and
presentation remain inside this same subgroup. The candidate's stronger
subgroup-wide conclusion is valid.

## 5. Positive control at 2773: PASS

Independent arithmetic gives

\[
2773=47\cdot59,
\qquad g=2,
\qquad A=23,
\qquad B=29,
\qquad \gcd(667,2772)=1.
\]

With \(n=12\) and bound 144, a fresh ordered enumeration found no earlier
distinct same-class relation. Its first useful hit is exactly

\[
(a,b)=(99,1),
\]

at exponent-pair ordinal 5,150 and unique-residue ordinal 299. The exact
relation is

\[
c=1263,
\qquad w=1684,
\qquad P=cw=2{,}126{,}892.
\]

Normalization gives

\[
D=3,
\qquad P_1/D=43^2,
\qquad P/D=842^2,
\]

so the induced root is

\[
R=3\cdot43\cdot842=108{,}618,
\qquad R\bmod2773=471.
\]

Finally,

\[
\gcd(R-1,2773)=47,
\qquad
\gcd(R+1,2773)=59.
\]

This reproduces every control field in `OUTPUT.json`. The full declared
control menu has \(145^2=21{,}025\) pairs; its early return at the first useful
hit is the documented rule.

## 6. Factor and target data flow: PASS

The source separates selection from the menu at a real function boundary:

- `factor_small` feeds the semiprime filter and stable certificate.
- `run_target_free_menu` receives only `modulus` and `block_x`.
- The menu derives the fixed block 3, seed inverse, seed product, bit-length
  bound, residues, inverses, square tests, and final gcds from those public
  inputs.
- No factor, endpoint, target relation, or target word is a parameter, global,
  closure value, or hard-coded constant in the selector.
- The known control input \(x=43\) is passed as a declared positive-control
  instance. Its successful word \((99,1)\), factors, relation, and endpoints
  are not passed to the menu.

The subgroup-order computation also uses only \(N\) and \(x\). It is used for
reporting coverage and does not choose a word or affect acceptance. The
factorization record is assembled by the caller only after the selector's
input boundary has been fixed.

## 7. Source, timeout, outputs, and manifest: PASS

The source implements the declared pair order and duplicate-residue rule.
For positive integers, testing whether \(P_1P\) is an exact square is exactly
the same as testing equality of square classes. For odd semiprime \(N\), a
root of unity is useful exactly when it is not a global sign; then both root
gcds are proper. The implementation's `factor_minus` acceptance test is
therefore sufficient in this scope.

The runner uses `subprocess.run(..., timeout=120)` and maps a timeout to exit
code 124. The pinned log records the exact command, the 120-second limit,
successful candidate output, and runner exit code zero. Its logged output hash
equals the current `OUTPUT.json` hash.

All five hashes listed in `RUN_MANIFEST.md` match their current files. The
JSON parses with no duplicate keys and agrees with the result and
reconstruction statement.

As a separate implementation replay, I copied only the source and runner to
an isolated temporary directory and ran the copied runner. It exited zero.
After removing only `elapsed_seconds`, its JSON object was identical to the
pinned output. No candidate artifact was changed by this replay.

## 8. Scope and limitations: PASS

One stable instance with an exhaustive null menu refutes the stated universal
one-step law. The candidate does not extend that result beyond its evidence.
It expressly leaves open:

- a changed or refined block presentation;
- multiple seeds or multiple retained square classes;
- a source outside the old subgroup;
- multiple feedback rounds; and
- another decoder or factoring screen.

It also discloses the decisive practical limitation:

\[
11<n^2=64.
\]

Thus this finite example does not obstruct a hybrid algorithm that first
removes polynomially bounded small factors. It supplies neither an
asymptotic failure rate nor a general lower bound. These limitations are
stated consistently in all three narrative artifacts.

## Final decision

**PASS.** F97 is an exact, reproducible, target-free counterexample to the
declared stable square-inverse-seed, two-block, one-step \(n^2\)-menu law. Its
complete-subgroup strengthening and positive control are correct. Its claims
remain within the evidence.
