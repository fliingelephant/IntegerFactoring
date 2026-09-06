# F261-D01 fresh hostile audit

## Verdict

**FAIL.** The substantive algebra is correct after one explicit `R=1`
convention. The frozen packet is not exact as written. The no-prefix
definition is incomplete, two preregistered predictor rules do not match the
source, and the runtime projection does not follow the worker count used by
the runner.

This was a static audit. I did not compile the source, run the self-test, run
the preflight, generate a cohort, or scan a cohort. I did not read the prior
hostile audit or blind reconstruction.

## Authenticated inputs

I computed each SHA-256 before reading the file. All five hashes match the
requested values.

| Artifact | SHA-256 | Result |
|---|---|---|
| `ALGEBRA.md` | `df27b6557ac2fe2ae29a495241c66741e864f8d667237f04855aa82f499aa67f` | PASS |
| `PREREGISTRATION.md` | `ae0e04eb7b1593795560eae3444c753ed07c4e4c0758c41386562fb72779c7f1` | PASS |
| `search.cpp` | `9af35178e041b3d02f4bf33134b451b9fe938cf8235ae450fb8df7f0027b1e6d` | PASS |
| `remote_run.sh` | `07fd9d53c1e2f08b647b24272908f1487ed1ba38657e7aef1a196d4f389137f3` | PASS |
| `PRELAUNCH_MANIFEST.md` | `110aee72fd78731f354643ccbc9517784e3ee28a8ea5c454069d9e959a6f70e8` | PASS |

## Decisive failures

### F1. The no-prefix case has no explicit inverse convention

`ALGEBRA.md:161-164` defines

\[
a=p\bmod R,\qquad b=Na^{-1}\bmod R
\]

for all schedules, while `ALGEBRA.md:219-221` later sets `R=1` for no
prefix. `PREREGISTRATION.md:139-140` repeats the same definition. Neither
file states what `a^{-1} mod 1` means. Many modular-inverse interfaces reject
this input. The source therefore has a separate rule at
`search.cpp:604-606`: it sets `a=0` and `b=0` when `R=1` and does not call
the inverse routine.

The intended repair is exact and harmless: declare `a=b=0` for `R=1`, and
use the unique residue class modulo one. Equations (7)-(10) and the
`O(U^3+C U^2)` bound then remain valid. The frozen theorem does not state
this convention, so its claimed exact no-prefix definition fails literally.

### F2. Predictor selection does not implement the frozen median score

`PREREGISTRATION.md:180-186` uses smaller median
`log2(1+min |c|)` as its third selection key. The source sorts the untransformed
carry minima and compares the sum of the two middle raw values
(`search.cpp:903-908`).

There are 798 train values per predictor: seven factor sizes times 114 rows.
Thus the even-sample convention matters. The arithmetic mean of two raw
middle values does not in general order predictors in the same way as the
arithmetic mean of their logarithms. Equivalently, the source compares a
sum where the stated score compares a product after adding one. This can
change the selected three predictors and therefore the only heldout results
allowed to count as leads.

The preregistration also does not define an even-sample median convention.
The source's convention cannot be inferred from the frozen text.

### F3. `product_surrogate` uses a different center

`PREREGISTRATION.md:169` specifies

\[
K_0=\operatorname{round}(u\sqrt N/B).
\]

The source first sets `sqrtN=floor(sqrt(N))` and then computes

\[
K_0=\operatorname{round}(u\lfloor\sqrt N\rfloor/B)
\]

at `search.cpp:598,635-638`. These functions are not equal. On the packet's
own exact algebra row `N=101*109=11009`, `B=128`, and `u=19`, the source
uses `floor(sqrt(N))=104` and returns `K0=15`, while the preregistered real
square-root expression returns `K0=16`.

The frozen text must either insert `floor` or the source must implement exact
rounding of the algebraic square root. This rule can change the chosen
multipliers.

### F4. The preflight projection is fixed at four workers

The runner accepts one through eight workers and can reduce the count to two
under load (`remote_run.sh:5-8,38-42`). It launches the full run with that
count (`remote_run.sh:51-57`). The preflight always divides the scan estimate
by four and labels it `projected_four_worker_seconds`
(`search.cpp:1099-1104`). The 12,000-second gate then tests this four-worker
quantity (`search.cpp:1128-1130`).

Consequently the gate can pass for a one-, two-, or three-worker launch even
when its own worker-scaled projection exceeds 12,000 seconds or the four-hour
timeout. This does not implement the conservative launch gate stated in
`PREREGISTRATION.md:270-277` and `PRELAUNCH_MANIFEST.md:34-41` for the actual
run configuration.

## Exact theorem reconstruction

Apart from F1, the requested mathematical checks pass.

### Centers, half ties, and carry identity: PASS

For positive `u`, round-half-up gives

\[
x=up-K_pB,\quad y=uq-K_qB,\qquad -B/2\le x,y<B/2.
\]

For odd `p` and `m>=2`, `up mod B=B/2` is equivalent to
`u=B/2 mod B`: multiplication by an odd inverse leaves the unique
order-two residue fixed. The floor formula sends that residue to `-B/2`.
`rounded_center` and the source's `>=B/2` centered conversion use the same
tie rule.

Since `N=1 mod B`, `xy=u^2 mod B`, so

\[
c=(xy-u^2)/B
\]

is integral. Expansion gives

\[
u^2H=K_pK_qB+K_py+K_qx+c
\]

and hence

\[
uT=u^2H+K_pK_qB-c,\qquad T=K_pq+K_qp.
\]

The source computes these quantities independently enough to check
integrality, trace divisibility, and the weighted-trace identity at every
scanned point (`search.cpp:198-222`).

### Balance bounds and center interval endpoints: PASS

The strict balance inequalities imply

\[
p^2>N/2,\quad p^2<N,\quad q^2>N,\quad q^2<2N.
\]

The integer endpoints in (5) follow exactly:

\[
p_-=\lfloor\sqrt{\lfloor N/2\rfloor}\rfloor+1,
\quad p_+=\lfloor\sqrt N\rfloor,
\]

\[
q_-=p_++1,
\quad q_+=\lfloor\sqrt{2N-1}\rfloor.
\]

`search.cpp:467-495` implements these endpoints with integer square roots.
Each rounded interval has `O(u)` entries uniformly because all four factor
bounds are `O(B)` for `B=2^floor(n/2)`.

The claim that the true centers are positive is also correct. If `n=2m`,
then `N>=B^2/2` and `p>sqrt(N/2)>=B/2`. If `n=2m+1`, then `N>=B^2` and
`p>B/sqrt(2)>B/2`. Thus both true centers are at least one.

### Direct-`T` enumeration and candidate bound: PASS after F1

Let `A=u^2H+Kp*Kq*B`. The identity `c=A-uT` converts `|c|<=C` into the
signed-safe interval

\[
\left\lceil\frac{A-C}{u}\right\rceil
\le T\le
\left\lfloor\frac{A+C}{u}\right\rfloor.
\]

The known residue gives

\[
T=K_pb+K_qa\pmod R.
\]

A fixed residue class has at most

\[
1+\left\lfloor\frac{2C}{uR}\right\rfloor
\]

members in that interval. There are `O(u^2)` public center pairs. Summing

\[
O\left(u^2+\frac{C}{R}u\right)
\]

over `1<=u<=U` gives exactly

\[
O\left(U^3+\frac{CU^2}{R}\right).
\]

At `R=1`, the repaired convention gives
`O(U^3+C U^2)`. If `uR>2C`, the interval is shorter than one residue step,
so it contains at most one admissible `T` for each center pair.

`bank_bound` evaluates the proved upper bound with exact public interval
cardinalities and multiprecision integers (`search.cpp:479-495`). It does
not enumerate the candidate tuples.

### Quadratic, linear, and verification decoder: PASS as mathematics

Substitution shows that `p` is a root of

\[
K_qX^2-TX+K_pN=0
\]

and that its discriminant is

\[
(K_pq-K_qp)^2.
\]

For `Kq>0`, exact square-root and divisibility tests on both signs recover
every integral root. For `Kq=0`, the equation is linear and the stated test
`X=Kp*N/T` is correct when `T` is nonzero and divides the numerator. If both
centers vanish, the tuple has no factor information. Testing every returned
root as a proper exact divisor makes every acceptance sound.

The full source has no candidate-bank decoder. Its self-test checks one
quadratic discriminant/divisibility case and one artificial linear case
(`search.cpp:1060-1075`). Therefore this audit validates the proof, not an
executed decoder or an executed factor-bank hit.

### One-dimensional inverse map: PASS

For `R>=2` and odd `u`, `x` is odd. It is a unit modulo `B`, and

\[
y=u^2x^{-1}\pmod B,\qquad x=ua+Rz.
\]

The centered interval contains exactly `B/R` members of this residue class
because it consists of `B` consecutive integers and `R` divides `B`. The
unique centered representative of `u^2x^{-1}` gives integral `c(z)`, and the
true point is present. The source's signed `z` endpoints, size assertion,
odd-step permutation, and centered inverse calculation implement this map
(`search.cpp:716-819`). Exhaustion still costs `B/R`, as stated.

## Scope and overclaim audit

- **PASS:** `ALGEBRA.md` limits the theorem to distinct odd balanced
  zero-defect semiprimes with a supplied residue `a`. It does not claim to
  produce the prefix, make the true carry small, prove a useful inverse-map
  distribution, or factor all inputs.
- **PASS:** The finite cohorts are described as conjecture and
  counterexample evidence. The heldout gates do not turn a finite pattern
  into an asymptotic theorem.
- **PASS:** `terminal_prefix` implements the stated integer test
  `R^4*n^8>=N`, which is `R^4*S^4>=N` for `S=n^2`.
- **REQUIRED INTERPRETATION:** All `hit_*` fields in the source come from
  the hidden true carry (`search.cpp:563-575`). The program reports bank
  upper bounds but never executes (9), the decoder, or candidate
  verification. No output may be called an executed or verified
  factor-bank hit. The manifest correctly makes no dynamic correctness
  claim before its gates run, but the term "executable thresholds" must not
  be used to imply execution.

## Secondary exactness defects

These do not affect the algebra, but they contradict literal preregistered
diagnostic language.

- `PREREGISTRATION.md:69-71` calls the edge candidate `p` uniform. The
  source maps one 64-bit SplitMix value with `h % count`
  (`search.cpp:234-245`). The edge interval size is not generally a divisor
  of `2^64`, so this map has modulo bias. The cohort is deterministic, but
  it is not an exact uniform sampler under the stated finite-word model.
- `PREREGISTRATION.md:198` asks for `max v2(c)` while also allowing zeros.
  The source assigns `v2(0)=128` (`search.cpp:582-583` through `v2_abs`).
  Mathematically `v2(0)` is infinite or undefined. The sentinel convention
  is not frozen in the preregistration.
- `PREREGISTRATION.md:208-211` says to report excess rank defects. The TSV
  stores raw ranks (`search.cpp:708-711,923-928`). A reader can derive the
  defects from the frozen ceilings, but the named quantity is not what the
  file directly reports.

## Required disposition

Do not launch this hash set as the exact preregistered experiment. A repair
must create a new declared hash set. At minimum it must:

1. define `a=b=0` for `R=1` in both mathematical documents;
2. make the median selection key exact and define its even-sample rule;
3. align the product-surrogate square-root rule;
4. scale the preflight projection by the actual launch worker count; and
5. preserve the boundary that the source measures oracle carry hits and
   bank bounds, not executed factor-bank hits.
