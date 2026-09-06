# F216 hostile audit

## Verdict

**PASS, with a provenance qualification.** All ten manifest hashes match. I
found no false image identity, cardinality formula, normalization step,
endpoint, interval-progression claim, or complexity conclusion within the
packet's stated scope.

The qualification concerns evidence, not mathematics. The complete F216
directory is untracked. Its preregistration claim is supported by consistent
local and remote timestamps, but not by an immutable commit or an external
timestamp. The frozen experiment also tests only the cardinality of
`W_t(1)`, not its exact valuation-stratum description. That is consistent
with the preregistered prediction, but it is weaker than a finite test of the
full theorem statement. The proof is independent of this computation.

I did not edit a frozen input or a durable ledger. I wrote only this audit.

## 1. Frozen-input integrity

I read `MANIFEST.md` first. I did not open the packet until all nine named
local files and the full remote output had been hashed.

| Artifact | Expected and observed SHA-256 | Result |
|---|---|---|
| `STATEMENT.md` | `fdc4a78e1189b4e733edf5a8d07549c459c3dbabf096ecf445a94acdc0f1df59` | match |
| `PROOF.md` | `aeefbbd1a6425383ffb9f924628e0c1bed15dbcf571596bb1052b91ad8de7592` | match |
| `SELF_AUDIT.md` | `8b1823e272191959e2f63a683938266435b76861bba472e7088237b6f84008bc` | match |
| `PROVENANCE.md` | `061fd9222017378acdcc97551d46b68033eeca2fe6b2f7b577a2932464479155` | match |
| `INTERVAL_COROLLARY.md` | `19386f7bf2febcaee16c7717cc31f99697f3a079ce2807ac7d4820ffb10cf390` | match |
| `PREREGISTRATION.md` | `3e47bea5bbbbeea3c9748455264f492a39f8cde24324372875d53c02aa79ec0a` | match |
| `scripts/F216_D01_dyadic_trace_saturation.py` | `19ed530c8b86ad1dc28245820b3566cd27ab8d44f4e243153dea6dfd4fad9a87` | match |
| `RESULT.md` | `5d6f65f57c1144812335d12515bda237a845c2ab077ba5269acc38256cfe8e50` | match |
| `output/F216-D01.summary.json` | `e2a638b8c6401b79d59cb48e014da7eff155adc1417fc5c9f431730c0ee145d7` | match |
| full remote output, `/tmp/F216_D01_output.json` | `ab021b50d02a92bdcaddcc091c8c95b981b0d7e2f09149ca03b61b1d30173ac0` | match |

The remote copy of the script also has SHA-256
`19ed530c8b86ad1dc28245820b3566cd27ab8d44f4e243153dea6dfd4fad9a87`.
The manifest does not declare a self-hash. Its observed SHA-256 is
`7634af31edf7f4c23eba3210435d0571cfba6f05f495addf105f1b50a0cb877a`.

## 2. Public square-class normalization

Let `d` be the member of `{1,3,5,7}` congruent to `N` modulo `8`, and set

\[
x=Nd^{-1}\pmod {2^t}.
\]

Since `d^2=1 mod 8`, one has `x=1 mod 8`. An odd unit modulo `2^t` is a
square exactly when it is `1 mod 8`. Thus an odd `a` with

\[
a^2=x\pmod {2^t}
\]

always exists.

The constructibility claim is also exact. Suppose `a^2=x mod 2^k` for
`k>=3`. Replacing `a` by `a+2^(k-1)` changes its square by `2^k mod
2^(k+1)`, because `a` is odd. This toggles the next square bit. Starting
from `a=1 mod 8` gives a root in `t-3` public steps. The routine in the
frozen source implements this lift correctly.

For `u=av`, direct substitution gives

\[
u+Nu^{-1}=a(v+dv^{-1})\pmod {2^t}.
\]

Both changes of variable are unit bijections. Therefore

\[
W_t(N)=aW_t(d)
\]

as sets, not only as cardinalities. No factor of `N` is used.

## 3. The classes `d=3`, `d=7`, and `d=5`

For every odd `u`, `u^{-1}=u mod 8`. Hence the necessary conditions are

\[
u+3u^{-1}=4\pmod8,
\qquad
u+7u^{-1}=0\pmod8.
\]

They are sufficient. For `s=4k` with `k` odd, the first equation is
equivalent to

\[
(u-2k)^2=4k^2-3\pmod {2^t}.
\]

The right side is `1 mod 8`. Its odd square root gives an odd `u`. For
`s=8k`, the second equation similarly becomes

\[
(u-4k)^2=16k^2-7\pmod {2^t},
\]

whose right side is also `1 mod 8`. Thus both complete progressions and
their counts are exact.

For `d=5`, direct evaluation modulo `32` gives only `6` and `26`. The
pairing `u -> u+16` preserves the trace modulo `32`, so eight odd inputs
modulo `16` suffice for the containment check. Conversely, write `s=2v`
with `v=3` or `-3 mod 16`. Then

\[
(u-v)^2=v^2-5=4R\pmod {2^t},
\qquad R=1\pmod8.
\]

An odd root `z^2=R mod 2^(t-2)` and `u=v+2z` realize `s`. Therefore

\[
W_t(5)=\{s:s=6\text{ or }26\pmod {32}\},
\qquad |W_t(5)|=2^{t-4}.
\]

This remains valid at the first claimed endpoint `t=5`, where the image is
exactly `{6,26}`.

## 4. The ramified class `d=1`

On the branch `u=1 mod 4`,

\[
u+u^{-1}-2=(u-1)^2u^{-1}.
\]

If this vanishes modulo `2^t`, it gives the single image value `2`.
Otherwise, put `b=v_2(u-1)`. Then `b>=2`, `2b<t`, and

\[
u+u^{-1}=2+2^{2b}w,
\]

where `w` is odd. Exact reduction modulo `8` gives `w=5 mod 8` for `b=2`
and `w=1 mod 8` for `b>=3`. When fewer than three bits remain, these are
exactly the reduced congruences in the statement.

The surjectivity argument survives the short-tail endpoints. Extend any
finite target `w` to a 2-adic odd integer that is `5 mod 8` for `b=2`, or
`1 mod 8` for `b>=3`. This is always compatible with the condition modulo
`2^min(3,t-2b)`. For `z=2^(2b)w`, the discriminant of

\[
u^2-(2+z)u+1=0
\]

is

\[
2^{2b+2}w(1+2^{2b-2}w).
\]

Its odd part is `1 mod 8`, so it is a 2-adic square. The resulting root has

\[
u-1=2^b(2^{b-1}w\mathbin{\pm}r)
\]

with `r` odd. Thus its valuation is exactly `b`, and `u=1 mod 4`. This
proves every displayed stratum occurs without merging adjacent strata.

Negation maps the other source branch to `-W_t^+(1)`. The positive and
negative images are `2` and `14 mod 16`, so they are disjoint. Within one
branch, distinct `b` have distinct valuations of the trace minus `2`.

For `k=t-2b`, one prescribed low class contains

\[
2^{\max(k-3,0)}
\]

odd residues. Therefore

\[
|W_t(1)|=2\left(1+
\sum_{b=2}^{\lfloor(t-1)/2\rfloor}
2^{\max(t-2b-3,0)}\right).
\]

The two geometric sums are

\[
|W_t(1)|=
\begin{cases}
(2^{t-4}+8)/3,&t\text{ even},\\
(2^{t-4}+10)/3,&t\text{ odd}.
\end{cases}
\]

At the low endpoints,

\[
W_5(1)=\{2,14,18,30\},
\]

and the formula gives `4`. It also gives `4` at `t=6` and `6` at `t=7`.
There is no missing tail case.

## 5. Interval progression and balanced trace range

For `t>=7`, the `b=2` stratum is the complete class

\[
2+16w=82\pmod {128},
\qquad w=5\pmod8,
\]

together with its negative. Multiplication by odd `a` maps all lifts of a
class modulo `128` bijectively to all lifts of the class multiplied by `a`.
This proves the two `d=1` classes in the corollary. The `d=5` classes are
`6a` and `-6a mod 32`. Odd scaling fixes the classes `4 mod 8` and `0 mod
8` for `d=3` and `d=7`.

Thus every `W_t(N)` contains at least one complete ordinary class modulo
`128`. Every interval of `L` consecutive integers contains at least
`floor(L/128)` members of any fixed class. The interval lower bound follows
with no dependence on `t`.

For a balanced factorization `N=pq` with `p<q<2p`, put `r=q/p`. Then

\[
\frac{p+q}{\sqrt N}=\sqrt r+\frac1{\sqrt r},
\qquad 1<r<2.
\]

This gives the strict bounds `2 sqrt(N) < p+q < 3 sqrt(N)/sqrt(2)`.
The integer interval has `Theta(sqrt(N))` points, and at least a fixed
`1/128`-scale subprogression survives. The packet correctly calls this a
pruning result. It does not claim that the surviving traces factor `N` or
that exact-square testing on them is hard.

The stated endpoint `t>=7` is safe because reduction modulo `128` is then
literal. It is not claimed to be sharp. At smaller `t`, a residue modulo
`2^t` can still contain one or more ordinary classes modulo `128` after
lifting.

## 6. Cardinality and complexity interpretation

The four representative densities are `1/8`, `1/16`, `1/8`, and
`1/48+O(2^-t)`. Normalization preserves cardinality. Hence

\[
|W_t(N)|\ge 2^t/48
\]

for every odd `N` and `t>=5`.

If `n` is the input bit length and

\[
t=n/4-\operatorname{polylog}(n),
\]

with the usual integer rounding, then

\[
\log_2|W_t(N)|\ge n/4-o(n).
\]

A literal list is therefore of size `2^Omega(n)`, not numerical-QP size.
This is an output-size statement for materialization. It is not a circuit
lower bound, a lower bound for an implicit interval finder, or a statement
about a decoder that retains `u`. The statement, proof, self-audit, and
interval corollary preserve these scope limits.

## 7. Frozen computation and provenance

The source computes the defining image exactly. It tests exact representative
sets for `d=3,5,7`, the exact `d=1` count, sampled square-class
normalizations, and factor-trace membership. Its root lift is valid. The
seeded inputs are deterministic. The 16 generated factors are below `2^16`,
where the Miller--Rabin bases in the source are more than sufficient; an
independent trial-division check also confirmed all 32 primes.

The full remote JSON is internally consistent:

- all 168 stored rows have `ok=true`;
- the actual kind counts are 56 representative, 96 normalization, and 16
  factor-trace rows;
- the representative split is 40 training and 16 holdout rows;
- all declared and actual row counts agree;
- the recomputed minimum density is `0.020843505859375`, attained by
  `|W_18(1)|=5464`;
- the 16 semiprime labels are valid, balanced products.

The factor-trace holdout is a sanity check, not strong evidence. Membership
is forced by the definition: choosing `u=p` gives
`p+Np^-1=p+q mod 2^t`. The source correctly keeps the factors out of image
construction, but this holdout cannot fail if modular inversion and the
label are computed correctly.

The exact `W_t(1)` stratum set is not compared by the frozen source. Only its
count is compared. Neither `PREREGISTRATION.md` nor `RESULT.md` falsely says
otherwise: the preregistered `d=1` prediction is a cardinality prediction.
The stronger theorem formula rests on the proof above.

The current remote state supports the environment report. `python3` is not
on the shell path. `/root/miniconda3/bin/python` reports Python 3.12.3.
The process affinity exposes 32 of 128 host CPUs. Current memory, disk, and
load figures are consistent with the rounded preregistration figures. These
current observations do not authenticate the historical command.

The timestamp order is also consistent:

- local preregistration and source: epoch `1786565987`;
- remote frozen script: `1786566009`;
- remote full output: `1786566048`;
- local result and summary: `1786566245`.

However, all F216 files are untracked, and filesystem timestamps are mutable.
The packet provides no committed preregistration, signed run log, or
immutable remote execution record. Therefore the statement “preregistered
before execution” is plausible and internally supported, but it is not
independently certified. The manifest also gives no path for the full remote
output; the file had to be located on the named host.

The cited Hittmeir paper,
[Integer Factorization as Subset-Sum Problem](https://arxiv.org/abs/2205.10074),
does contain the modular-hyperbola trace image, the hyperbolic-sieve
framework, CRT combination, and odd-prime-power cardinality formulas. It
does not supply the dyadic formulas proved here, and the packet does not
claim that it does. The promoted P26, P167, P179, P185, and P186 entries
exist in the local ledgers, but none is a premise of this self-contained
proof. The asserted order in which they were checked is a process claim and
cannot be reconstructed from the packet.

## 8. Independent exact attacks

I ran two named, read-only checks. They wrote no artifact.

`F216-AUDIT-CHECK-01` used an independent direct-image enumerator and an
explicit constructor for the `d=1` strata. It checked:

- all 56 representative images for `5<=t<=18`, including exact `d=1` set
  equality;
- 2,097,024 representative-universe memberships;
- all 65,532 square-root bit lifts `x=1 mod 8` for `5<=t<=18`;
- normalization for all 4,080 odd residues `N` for `5<=t<=12`;
- all 4,032 claimed scaled progressions for `7<=t<=12`;
- 4,210,688 start, length, and residue cases for the interval counting
  lemma.

Every check passed. The canonical result-record SHA-256 is
`a70ee647f4c2bd0a47cf2e5da2f1ae9ae6649e7d5cc06e6b4e7132ca5a61b688`.

`F216-AUDIT-CHECK-02` independently rechecked all 168 rows in the frozen
remote JSON. It used the full exact `d=1` set, recomputed every normalized
set hash, and verified every semiprime by trial division. Every check passed.
After deleting only the nondeterministic elapsed-time field, the canonical
semantic JSON has SHA-256
`5cf312aa391f9844265c2ecac5ab8179acc3ab3f3e60de4d37b55f4003fb751e`.

These finite checks are counterexample searches. They are not proof evidence
for the quantified theorem.
