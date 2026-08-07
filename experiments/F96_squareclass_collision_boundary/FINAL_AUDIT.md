# F96 corrected-candidate final hostile audit

## Verdict: **FAIL as written**

The correction fixes both failures recorded for `failed_v1`. The general
theorem is correct. The finite counts, ordering, subgroup claims, target-free
selector, post-selection disclosure, complexity bounds, logs, outputs, and
manifest hashes all pass independent checks.

The corrected candidate still contains one false operational claim.
`RESULT.md` calls the normalization

> gcd-free square normalization of a supplied relation pair

but the same result correctly defines

\[
D=\gcd(P_1,P_2)
\]

and states that the normalization needs one gcd. The diagnostic source also
uses that gcd. The accurate term is **gcd-based** or **factor-free** square
normalization. A strict artifact-wide audit cannot pass an explicit claim
that contradicts the theorem and implementation, even though this wording
defect does not invalidate the theorem or finite witness.

## Pinned corrected artifacts

I pinned the following SHA-256 hashes before reading any corrected-candidate
artifact. I excluded `failed_v1/`, `HOSTILE_AUDIT.md`, `FINAL_AUDIT.md`, and
`RECONSTRUCT_RESULT.md` as instructed.

```text
c20e4f9849a025a72e4058298b9dfb7f481ed6168531084b44f06758efb52f42  BLIND_SELECTOR_OUTPUT.json
617c4c27edb401713a24ca220e958276ee55ae8347aa827279138b4534b96469  BLIND_SELECTOR_RUN.log
0b0ada4d8cf40155a3758e160d30f272d42fa97d7372c3c40b589c551926f57e  OUTPUT.json
b2a06e0ee52c2734595e22bebaaaa8dcabd5378d1d175f2e88473704d0c6c783  RECONSTRUCT_STATEMENT.md
3e217e662428055ca8fa7e85eab3bcab8aa3fe7bb201498ca6613abd7baaf858  RESULT.md
723f4ba60fca5e1d8b0cdd49cf0ddb4e620a0e8a2571620d2837c603801dcf71  RUN.log
c97c65c8ae279ecd1a7c00fdc2e37a760b2801e83f18ef61f5b48571d89b6b73  RUN_MANIFEST.md
ad58a175d58cc0f726969be58a0d3884c7869fdce027bb39f6763358322754ec  analyze_squareclass_boundary.py
da82081dd62ba1f13e8b7ddd7b30e0597df3f68381c777c4f9dbd9275648feaa  blind_selector.py
2432998b7a02678017c05cfc69406a7a1d1adfe5b474c674ad2e760facf3e576  run_blind_selector_with_timeout.py
3fcd569f574cee030ca8406825a407df882003a9cc8bfb730b549379eedc40bb  run_with_timeout.py
```

I read every pinned file. A final rehash before writing this report reproduced
the same list.

I then wrote an independent standard-library enumerator in a temporary
directory. It did not import either candidate source. I also copied the two
sources and runners to an isolated temporary directory and ran the copied
runners. Both returned exit code zero. Their deterministic JSON fields match
the pinned outputs exactly after removing only `elapsed_seconds`.

I reached the verdict above before I inspected `failed_v1/` or
`HOSTILE_AUDIT.md`.

## 1. General theorem: PASS

For each prime \(q\), let

\[
x_q=v_q(P_1),\qquad y_q=v_q(P_2).
\]

The two positive integers have the same rational square class exactly when
\(x_q-y_q\) is even for every \(q\). This is equivalent to \(x_q+y_q\)
being even for every \(q\), which is equivalent to \(P_1P_2\) being an
integer square.

Let \(D=\gcd(P_1,P_2)\). If \(P_1P_2\) is a square, then

\[
\frac{P_1}{D}\frac{P_2}{D}
\]

is a square and its two factors are coprime. Each factor is therefore a
square. Thus

\[
P_1=DA^2,\qquad P_2=DB^2,\qquad \gcd(A,B)=1.
\]

If \(D\) were a square, both \(P_i\) would be squares, contrary to the
hypothesis. The converse follows from

\[
P_1P_2=(DAB)^2.
\]

Since \(P_i\equiv1\pmod N\), both \(P_i\) are units. Every divisor of a
unit is coprime to \(N\), so \(D,A,B\) are units. Cancelling \(D\) gives

\[
A^2\equiv B^2\pmod N.
\]

The positive induced root is

\[
R=DAB=\sqrt{P_1P_2},\qquad R^2\equiv1\pmod N.
\]

The identities

\[
DB(A-B)=R-P_2,\qquad DB(A+B)=R+P_2
\]

and the fact that \(DB\) is a unit give

\[
\gcd(R-1,N)=\gcd(A-B,N),
\]

\[
\gcd(R+1,N)=\gcd(A+B,N).
\]

For odd composite \(N\), no prime factor of \(N\) divides both \(R-1\)
and \(R+1\). Since \(N\mid(R-1)(R+1)\), a proper gcd occurs exactly when
\(R\) is neither global sign modulo \(N\). The displayed identities make
this equivalent to \(A\not\equiv\pm B\pmod N\) globally.

The counterexample is exact:

```text
N = 143 = 11*13
102*136 = 13872 = 3*68^2 = 1 + 97*143
125*135 = 16875 = 3*75^2 = 1 + 118*143
R = 3*68*75 = 15300 = -1 (mod 143)
gcds = (1,143)
```

An independent scan of distinct odd semiprimes through 199, in the declared
relation order, confirms that \(N=143\) is the first global-sign example.

## 2. Fixed arithmetic and subgroup: PASS

The exact arithmetic gives

```text
2773 = 47*59
3*43^2 = 5547 = 1 + 2*2773
43^1334 mod 2773 = 1
43^667  mod 2773 = 2772
43^58   mod 2773 = 237
43^46   mod 2773 = 847
```

Since \(1334=2\cdot23\cdot29\), the last four power checks prove
\(\operatorname{ord}_{2773}(43)=1334\). Also
\(3=43^{-2}\pmod{2773}\), so

\[
\operatorname{ord}_{2773}(3)=667,
\qquad H=\langle3,43\rangle=\langle43\rangle,
\qquad |H|=1334.
\]

For the target endpoint,

```text
842*43^(-1) mod 2773 = 471
471^2 mod 2773 = 1
471 is neither 1 nor 2772
43^667 mod 2773 = 2772
```

A cyclic group has at most one nonidentity involution. Therefore 471 is not
in \(H\), so 842 is not in \(H\). Its inverse 2526 is not in \(H\) either.
An independent full traversal of all 1334 powers confirms both conclusions.

The alternative presentation also checks:

```text
3^99*43 mod 2773 = 1263
1263^(-1) mod 2773 = 1684
1263*1684 = 2126892 = 842*2526 = 3*842^2
sqrt(5547*2126892) = 108618
gcd(108618 - 1,2773) = 47
gcd(108618 + 1,2773) = 59
```

Using \(3^a43^b=43^{b-2a}\), the shortest nonnegative word for 1263 is
\((99,1)\), and the shortest one for 1684 is \((0,197)\). The signed BFS
order independently gives \((98,-1)\) and \((-98,1)\). These match the
recorded words.

## 3. Exact finite separation and order: PASS

The following counts include every same-class hit. “New presentations” means
residues whose exact relation value is not \(P_1=5547\).

| Search set | Pairs or residues | Unique residues | Same-class hits | Old \(P_1\) repeats | New presentations | Distinct new values | Useful roots |
|---|---:|---:|---:|---:|---:|---:|---:|
| Raw monomials below \(N\) | 12 | 12 | 4 | 4 | 0 | 0 | 0 |
| Menu \(0\le a,b\le12\) | 169 | 37 | 4 | 4 | 0 | 0 | 0 |
| Menu \(0\le a,b\le144\) | 21,025 | 433 | 5 | 4 | 1 | 1 | 1 |
| Complete subgroup \(H\) | 1,334 | 1,334 | 6 | 4 | 2 | 1 | 2 |

The four old-relation residues are

```text
3, 43, 129, 1849.
```

Each has relation value 5547, induced root 5547, root residue 1, and gcd
pair \((2773,1)\). The two new subgroup presentations are 1263 and 1684.
They are an inverse pair. Each has relation value 2126892, induced root
108618, root residue 471, and gcd pair \((47,59)\).

The bound-144 menu reaches only the first of those two new presentations.
Its complete same-class order is:

| Pair ordinal | Unique ordinal | \((a,b)\) | Residue | Relation value | Useful |
|---:|---:|---:|---:|---:|---|
| 2 | 2 | \((0,1)\) | 43 | 5547 | no |
| 3 | 3 | \((1,0)\) | 3 | 5547 | no |
| 4 | 4 | \((0,2)\) | 1849 | 5547 | no |
| 5 | 5 | \((1,1)\) | 129 | 5547 | no |
| 5150 | 299 | \((99,1)\) | 1263 | 2126892 | yes |

There are \(1+2+\cdots+100=5050\) pairs before total exponent 100.
Within total 100, \((99,1)\) is the 100th pair. This proves pair ordinal
5150. Independent residue tracking gives unique ordinal 299. No other
same-class hit occurs among the 433 unique residues. The bound-12 menu has
exactly the first four rows.

The exhaustive raw list is

```text
3, 9, 27, 43, 81, 129, 243, 387, 729, 1161, 1849, 2187.
```

Only 3, 43, 129, and 1849 are canonical-relation same-class hits. All four
repeat \(P_1\). No raw monomial reaches endpoint 842, relation value
2126892, a distinct same-class relation value, or a useful root.

The subgroup densities are therefore exact:

\[
\frac{6}{1334}=\frac3{667}
\quad\text{for all same-class presentations},
\]

\[
\frac{2}{1334}=\frac1{667}
\quad\text{for distinct useful presentations}.
\]

The complete canonical-relation census has 634 unique relation values. Of
these, 631 are nonsquares. Its three distinct-value same-class pairs are:

```text
(5547,    2126892) -> gcds (47,59)
(1294992, 1907825) -> gcds (59,47)
(2315456, 6461091) -> gcds (59,47)
```

All three are useful. There are no global-sign pairs in this census.

## 4. Diagnostic and target-free executables: PASS

The diagnostic runner receives 842. The diagnostic source uses it for the
membership certificate, endpoint-hit fields, target-relation fields, and the
named F95 pair. The menu acceptance path itself does not use it. It depends
only on \(N\), 3, 43, canonical inversion, the exact-square test, and the
induced-root gcds. As a runtime check, replacing the diagnostic target with
43 leaves every menu count and collision field unchanged after removing only
the diagnostic `target_hits` fields.

The authoritative target-free source accepts exactly these arguments:

```text
--n --block-a --block-b --bound --output
```

Its runner supplies only

```text
--n 2773 --block-a 3 --block-b 43 --bound 144 --output BLIND_SELECTOR_OUTPUT.json
```

The source and runner contain no literal 842, 2526, 2126892, 47, 59, `P2`,
or `--target`. The source reads no environment variable and no input file.
The words `factor_received` and `factors` occur only in a Boolean `False`
input-policy field and in output formatting. The run log contains 47 and 59
only after the selector derives them by gcd. Thus the executable literally
receives no target endpoint, target relation value, or factor.

The isolated runner replay returned:

```text
pairs=21025 residues=433 same_class=5 distinct=1 useful=1
first_useful=exponents=[99, 1] residue=1263 inverse=1684 factors=(47,59)
runner_exit_code=0
```

After deleting only elapsed time, its JSON is identical to the pinned
`BLIND_SELECTOR_OUTPUT.json`. The same comparison passes for the diagnostic
runner and `OUTPUT.json`.

## 5. Exhaustion, complexity, and scope: PASS

Both raw bases exceed one. The nested raw-product bounds therefore exhaust
all nonnegative monomials below \(N\) and stop exactly after the 12 listed
values.

For \(n=\lceil\log_2N\rceil=12\), the bound in each menu dimension is
\(n^2\). The menu has

\[
(n^2+1)^2=O(n^4)
\]

candidates. Modular powers, modular inversion, exact integer square roots,
and gcd use polynomial-bit arithmetic. The fixed two-block menu is therefore
polynomial in \(n\).

The discovery evidence is not polynomial in \(\log N\). It includes a full
1334-element subgroup scan, a complete canonical-relation census, and the
bounded semiprime counterexample scan. The \(n^2\) bound was chosen after the
full subgroup scan. The candidate explicitly calls the result post-selected
fixed-instance evidence. It does not claim an all-input success theorem, an
inverse-polynomial density law, or a new factoring mechanism. These scope
limits are accurate.

## 6. Logs, outputs, and manifest: PASS

Every hash listed in `RUN_MANIFEST.md` matches its current artifact. The
runner commands match the two logs. Both runners impose `timeout=120` and
record exit code zero. Each log's output hash matches the corresponding JSON
file. The isolated copies of the four executable files had the same hashes
as the pinned originals before replay.

The manifest correctly distinguishes the target-aware diagnostic run from
the target-free authoritative selector. It also correctly distinguishes
public polynomial menu work from certificate-only discovery work.

## 7. Earlier failure preservation and correction: PASS

Only after reaching the current verdict did I inspect `HOSTILE_AUDIT.md` and
all files under `failed_v1/`.

The seven hashes pinned by the earlier hostile audit exactly match the
preserved failed source, runner, log, output, result, reconstruction
statement, and manifest. The failed reconstruction is also present and gives
the same strict count-based failure. The old source contains the precise
cause:

```python
if candidate["P"] == first_product:
    return None
```

That condition silently removed the four old-relation repeats before the
old artifacts reported unqualified same-class counts. The corrected source
removes the condition, labels every hit with
`same_relation_value_as_first`, and reports the all-hit, old-value,
distinct-value, and useful subsets separately. The corrected prose and
reconstruction statement make the same separation.

The other earlier failure is also corrected. The old run received 842 while
its prose called the run blind. The corrected candidate retains that run as
a diagnostic and adds a separate source, runner, log, and output that accept
no target.

Thus the earlier failure is both preserved and actually corrected. The
remaining `gcd-free` wording defect already existed in the failed result and
was carried into the corrected result. It is independent of the earlier two
failures.

## Final decision

**FAIL as written.** The mathematical theorem and all substantive corrected
F96 evidence pass. Change “gcd-free square normalization” to “gcd-based
square normalization” or “factor-free square normalization.” No other
correction is required by this audit.
