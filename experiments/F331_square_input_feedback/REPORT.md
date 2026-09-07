# F331 public square-input feedback

**Family:** route:F31

Status: completed bounded seeded experiment. The results are finite policy
comparisons, not a distribution theorem, asymptotic fit, or quasipolynomial
factoring bound.

## Implemented public boundary

The outer driver draws the hidden nonzero residue and forms \(a_0=r^2\bmod
N\). The controller has exactly the interface
\((N,a_0,\mathrm{policy},\mathrm{policy\ seed})\); it never receives \(r\)
or offline factors. It retains public \(a,C\) with
\[
 a=a_0C^2\pmod N.
\]
Every root of a current input is multiplied by \(C^{-1}\), checked as a
root of \(a_0\), and returned to the outer driver before the hidden-root gcd.

Each of at most 16 rounds first tests whether \(a\) is an ordinary integer
square, then makes eight calls on F326's rank-reflection path. The multiplier
pool contains distinct absolute values of computed current coordinates and
their computed \(F\)-images when these are nontrivial units. The path policy
samples up to four pool values without replacement; uniform samples four
independent nonzero residues and gcd-screens them; last uses only the final
nontrivial visited unit. Every proposal \(b=ac^2\bmod N\) is scored by its
distance from the nearest ordinary integer square, with the lower root on a
tie. Every score gcd is charged and verified.

## Exact controls

The pilot checked 2,720 root-pullback identities exhaustively on four small
moduli. Four independent eight-call probes agreed exactly with F328's frozen
arithmetic walk in status, endpoint, domain constants, and all pairing
operation counters. The serialized controller histories contain no hidden
root field.

The full aggregate rechecked all public invariants, factors, roots, batch
coverage, and shared initial roots. It contains exactly 768 attempts:
eight retained balanced semiprimes, 32 initial roots per modulus, and three
policies. Each policy receives the same initial root for a paired comparison
and a separate policy seed.

## Finite outcomes

| Target bits | Path | Uniform | Last |
|---:|---:|---:|---:|
| 20 | 15 / 64 | 20 / 64 | 13 / 64 |
| 28 | 1 / 64 | 3 / 64 | 2 / 64 |
| 36 | 0 / 64 | 0 / 64 | 0 / 64 |
| 44 | 0 / 64 | 0 / 64 | 0 / 64 |
| all | 16 / 256 | 23 / 256 | 15 / 256 |

The path outputs comprise ten direct path factors and six factors from
pulled-back ordinary-square roots. Seven further pulled roots gave trivial
outer gcds, and 233 attempts reached the round cap. Uniform produced six
direct path factors, seven multiplier-generation gcd factors, one proposal
screen factor, and nine pulled-root factors; five pulled roots failed and
228 attempts were censored. Last produced ten direct path factors and five
pulled-root factors, with 241 censors.

Eight of uniform's 23 successes therefore came from its additional public
multiplier-generation or proposal gcds. Those are valid charged outputs,
but they are not evidence that its selected square inputs were easier.
There were no initial hidden-residue gcd factors. Zero successes at 36 and
44 bits do not imply zero probability.

## Charged costs

| Policy | Factors | F calls/factor | Floor iterations/factor | Gcds/factor | Fair bits/factor | Seconds/factor |
|---|---:|---:|---:|---:|---:|---:|
| path | 16 | 1,959.00 | 840,918.75 | 2,708.00 | 6,007.69 | 0.223 |
| uniform | 23 | 1,344.74 | 592,058.30 | 2,529.65 | 31,927.83 | 0.158 |
| last | 15 | 2,113.53 | 936,131.13 | 2,130.93 | 747.20 | 0.249 |

Every failed attempt and every unselected proposal contributes to these
ratios. Integer-square tests, modular multiplications and inversions,
rank/select operations, proposal counts, and random-bit rejection counts
are retained in the aggregate. The fair bits were emulated with separate
seeded pseudorandom streams for reproducibility.

The pilot used 0.023 seconds and 28,344,320 peak RSS bytes. The eight full
batches used 0.334--2.850 seconds and at most 39,157,760 bytes each. The
sequential aggregate used 0.490 seconds and 179,453,952 bytes. Every process
stayed below its 28-second internal alarm, 30-second external timeout, and
512 MiB ceiling.

The finite ordering uniform, path, last is not a bias theorem. All observed
successes occur at 20 or 28 bits, and the policies perform different amounts
of gcd and random-bit work. Establishing an advantage requires a per-input
success law after all filters and proposal costs, not a pooled hit count.

Evidence:
DESIGN.md,
square_input_feedback.py,
aggregate_feedback.py,
pilot_output.json,
the eight named batch output/status/log triples,
aggregate_output.json,
aggregate_status.json,
aggregate_run.log, and
RESOURCE.md.
