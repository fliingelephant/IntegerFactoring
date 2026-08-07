# F96 final hostile re-audit

## Verdict: **PASS**

The final current F96 candidate passes strict whole-artifact re-audit.

The general theorem is correct. The fixed arithmetic, subgroup claims,
finite counts, enumeration order, target-free selector data flow, complexity
claims, scope limits, logs, JSON outputs, and all nine manifest hashes pass
independent checks. The normalization term is now accurate.

I found no remaining false or materially misleading claim in the pinned
candidate.

## 1. Clean-room protocol and pinned snapshot

I pinned these SHA-256 hashes before reading any current candidate content:

```text
4ffa68dc66bd48f62c15fc1ef16dc8e54c4157e64f5c1f49ee544e24e06783d9  RESULT.md
f907e94762ada59b70d11338eec7467f1d427f4945da79d178a8b8e4cf860d39  RUN_MANIFEST.md
b2a06e0ee52c2734595e22bebaaaa8dcabd5378d1d175f2e88473704d0c6c783  RECONSTRUCT_STATEMENT.md
ad58a175d58cc0f726969be58a0d3884c7869fdce027bb39f6763358322754ec  analyze_squareclass_boundary.py
da82081dd62ba1f13e8b7ddd7b30e0597df3f68381c777c4f9dbd9275648feaa  blind_selector.py
3fcd569f574cee030ca8406825a407df882003a9cc8bfb730b549379eedc40bb  run_with_timeout.py
2432998b7a02678017c05cfc69406a7a1d1adfe5b474c674ad2e760facf3e576  run_blind_selector_with_timeout.py
723f4ba60fca5e1d8b0cdd49cf0ddb4e620a0e8a2571620d2837c603801dcf71  RUN.log
617c4c27edb401713a24ca220e958276ee55ae8347aa827279138b4534b96469  BLIND_SELECTOR_RUN.log
0b0ada4d8cf40155a3758e160d30f272d42fa97d7372c3c40b589c551926f57e  OUTPUT.json
c20e4f9849a025a72e4058298b9dfb7f481ed6168531084b44f06758efb52f42  BLIND_SELECTOR_OUTPUT.json
```

I then read all 11 files completely. I did not inspect `failed_v1/`,
`RESULT_FAILED_V2.md`, `RUN_MANIFEST_FAILED_V2.md`, `HOSTILE_AUDIT.md`,
`FINAL_AUDIT.md`, or `RECONSTRUCT_RESULT.md` until after I had reached the
PASS verdict from the current candidate alone.

A final pre-report rehash reproduced the same 11 hashes.

## 2. General theorem: PASS

Let (v_p) be the prime valuation. Equality of the square classes of
(P_1) and (P_2) is equivalent to

\[
v_p(P_1)\equiv v_p(P_2)\pmod 2
\]

for every prime (p). This is equivalent to every valuation of (P_1P_2)
being even, hence to (P_1P_2) being an exact integer square.

Put (D=\gcd(P_1,P_2)). The two quotients (P_1/D) and (P_2/D) are
coprime. Their valuations are even under the condition above. Therefore

\[
P_1=DA^2,\qquad P_2=DB^2,\qquad \gcd(A,B)=1.
\]

Conversely, this form makes (P_1P_2=(DAB)^2). Since neither (P_i) is a
square, (D) cannot be a square. This proves all three stated conditions
equivalent.

Because (P_i\equiv1\pmod N), both (P_i) are units modulo (N). Every
divisor (D) of a unit is also a unit modulo (N). The equations above then
show that (A) and (B) are units and

\[
A^2\equiv B^2\pmod N.
\]

For (R=DAB=\sqrt{P_1P_2}), the exact congruences

\[
R-P_2=DB(A-B),\qquad R+P_2=DB(A+B)
\]

and the fact that (DB) is a unit give

\[
\gcd(R-1,N)=\gcd(A-B,N),
\]

\[
\gcd(R+1,N)=\gcd(A+B,N).
\]

Also (R^2\equiv1\pmod N). If (N) is odd, a root that is not globally
(1) or (-1) makes each displayed gcd proper and nontrivial. A global sign
makes one gcd (N) and the other (1). The stated factorization boundary
and its equivalent condition (A\not\equiv\pm B\pmod N) are exact.

The counterexample also checks:

\[
13872=3\cdot68^2=1+97\cdot143,
\]

\[
16875=3\cdot75^2=1+118\cdot143.
\]

Here (R=3\cdot68\cdot75=15300\equiv-1\pmod{143}). The gcds are (1)
and (143), so equal nonzero square class alone does not factor (N).

## 3. Normalization terminology: PASS

The operative term is now **factorization-free square normalization**. This
is accurate. The operation uses one gcd, two exact divisions, and two exact
integer square-root tests. It does not use prime factorization of (N),
(P_1), or (P_2), and it does not receive the factors of (N).

The current result explicitly says that one gcd is used. Thus
“factorization-free” does not falsely imply “gcd-free.” The only current
occurrence of “gcd-free” quotes the rejected historical wording and explains
why it was replaced. It is not an operational claim.

## 4. Fixed arithmetic and subgroup: PASS

Independent exact arithmetic gives

\[
2773=47\cdot59,
\qquad
P_1=3\cdot43^2=5547=1+2\cdot2773.
\]

It also gives

\[
\operatorname{ord}_{2773}(3)=667,
\quad
\operatorname{ord}_{2773}(43)=1334,
\quad
|\langle3,43\rangle|=1334.
\]

The short nonmembership certificate is valid:

\[
43^{667}\equiv-1,
\quad
842\cdot43^{-1}\equiv471,
\quad
471^2\equiv1\pmod{2773},
\]

with (471\not\equiv\pm1). Since the subgroup is cyclic, it has only one
element of order two. Thus (842\notin H). Its inverse (2526) is also not
in (H).

The alternative presentation checks exactly:

\[
3^{99}43\equiv1263\pmod{2773},
\qquad
1263^{-1}_{\rm can}=1684,
\]

\[
1263\cdot1684=2126892=842\cdot2526=3\cdot842^2.
\]

Therefore

\[
\sqrt{5547\cdot2126892}=108618,
\]

and the two root gcds are (47) and (59).

## 5. Counts and ordering: PASS

An independent standard-library enumerator did not import either candidate
source. It reproduced these exact results:

| Census | Pairs or residues | Same-class hits | Distinct useful hits |
|---|---:|---:|---:|
| Raw monomials (3^a43^b<N), excluding (1) | 12 | 4 | 0 |
| Menu (0\le a,b\le12) | 169 pairs, 37 unique residues | 4 | 0 |
| Menu (0\le a,b\le144) | 21,025 pairs, 433 unique residues | 5 | 1 |
| Complete subgroup (H) | 1,334 residues | 6 | 2 residues, one value |
| Complete canonical-relation census | 634 values, 631 nonsquares | 3 value pairs | 3 |

The four repeated old-relation residues are

\[
3,\ 43,\ 129,\ 1849.
\]

The two useful subgroup residues are (1263) and (1684). They are one
inverse pair and give one distinct relation value. Hence the exact subgroup
densities are

\[
6/1334=3/667
\]

for all same-class presentations and

\[
2/1334=1/667
\]

for useful new presentations.

Both sources implement increasing (a+b), then increasing (a). They count
every valid exponent pair before duplicate-residue suppression. They assign
the unique-residue ordinal only after a residue first appears. Under this
order, ((99,1)) is pair ordinal 5150 and unique-residue ordinal 299. It is
the first distinct and first useful collision.

The other declared orders also match the source: positive BFS uses (3)
before (43); signed BFS uses (3,3^{-1},43,43^{-1}); relation records are
sorted by ((P,g,w)); and same-class pairs use nested sorted order. The
independent (N\le199) scan reproduced (N=143) as the first global-sign
counterexample in the declared order.

## 6. Target-free data flow: PASS

The diagnostic source receives (842) for the separate membership query.
Its menu collision test does not depend on that target. Target comparison is
stored only in separate diagnostic fields.

The authoritative selector is stronger evidence. Its command receives only

- (N=2773);
- the public blocks (3,43);
- the public bound (144); and
- an output path.

The source has no target, target-relation, or factor argument. It derives
(P_1) from the public blocks. Candidate acceptance uses modular arithmetic,
canonical inversion, an exact square test, and the two final gcds. Neither
(842), (P_2), (47), nor (59) occurs in its input or acceptance path.

The runner invokes that source with the documented arguments and a hard
120-second timeout. The log records exit code zero and the exact five-hit
result. The diagnostic runner and log do the same for their documented
command.

## 7. Complexity and scope: PASS

For (n=\lceil\log_2N\rceil), the two-block (n^2) menu has

\[
(n^2+1)^2=O(n^4)
\]

exponent pairs. Modular exponentiation, inversion, exact square root, gcd,
and duplicate tracking all have polynomial bit complexity for these
canonical values. Thus the declared fixed two-block menu is polynomial in
the input bit length.

The complete subgroup BFS, complete relation census, and bounded semiprime
scan are correctly separated as certificate-only discovery work. The result
also states that the successful (n^2) bound was found after a complete
finite scan. It therefore discloses post-selection.

The candidate does not extrapolate this instance to an all-input theorem.
It expressly disclaims a general success law, inverse-polynomial density,
and a polynomial-time factoring algorithm. The evidence supports exactly
the fixed-instance selector and the general elementary collision theorem.

## 8. Logs, outputs, replay, and manifest: PASS

Both current logs name the commands encoded by their runners, record the
120-second timeout, and end with exit code zero. Each logged JSON SHA-256 is
the actual hash of its current output.

I parsed all nine SHA-256 entries in `RUN_MANIFEST.md` and recomputed each
file hash. All nine match. The command, timeout, ordering, public-data,
outcome, and evidence-limit sections also match the sources and outputs.

I copied both sources and both runners to an isolated temporary directory
and ran the copied runners. Both completed successfully. After removing only
the nondeterministic `elapsed_seconds` field, both replayed JSON objects were
identical to the pinned current outputs.

## 9. Failure-record preservation: PASS

I inspected the excluded records only after reaching the verdict above.

The `failed_v1/` directory contains the failed source, runner, log, output,
result, reconstruction statement, reconstruction result, and manifest. The
seven hashes pinned by `HOSTILE_AUDIT.md` match those preserved files. The
archived reconstruction retains its strict count-based FAIL verdict.

`RESULT_FAILED_V2.md` and `RUN_MANIFEST_FAILED_V2.md` preserve the second
candidate. Their hashes match the versions pinned by `FINAL_AUDIT.md`. All
nine hashes recorded in the archived V2 manifest match the corresponding
preserved or unchanged executable artifacts. `FINAL_AUDIT.md` retains the
strict terminology-based FAIL verdict.

The corrected `RECONSTRUCT_RESULT.md` is present and records PASS. It was not
used to reach this re-audit verdict.

The failure history is therefore both complete and consistent with the
current result’s status narrative.

## Final decision

**PASS.** The final F96 candidate is mathematically correct, operationally
faithful, accurately scoped, target-free where claimed, and internally
consistent at the pinned hashes above. No candidate artifact or durable
ledger requires correction from this re-audit.
