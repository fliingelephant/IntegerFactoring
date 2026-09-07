# Adaptive output-selected roots: finite public trials and conditional field populations

**Family:** route:F29

**Status:** exact bounded discovery data. The public trials use no factor
information. The field-population process is a separate conditional
diagnostic. No unbounded success probability, expected-cost theorem, or
factoring algorithm is claimed.

## Public composite experiment

For an odd composite \(N\), each independent trial starts with an empty root
list. At a probe, it draws \(x\) uniformly from \([0,N)\), puts \(y=x\), and
applies
\[
 y\leftarrow y(y-a)\pmod N
\]
once for each stored output \(a\). It computes \(\gcd(y,N)\). A proper gcd
is returned and verified. If the gcd is one, the public value \(a=y\) is
appended. If the gcd is \(N\), no root is appended. The finite trial ends
after
\[
 B=\min(512,\operatorname{bitlength}(N)^2)
\]
probes and remains explicitly censored if it has not succeeded.

The controls are uniform-residue gcd probes with the same gcd budget and a
basic randomized Pollard-rho trial with one polynomial \(z^2+c\), Floyd
iteration, and the same gcd-call budget. The accounting counts each modular
multiplication and gcd call actually executed. A rho iteration uses exactly
three modular multiplications.

Five balanced labels use \(p\) just above \(2^b\), \(b=8,10,12,14,16\), and
\(q\) just above \(1.6p\). Three unbalanced labels use exponent pairs
\((8,16),(10,18),(12,20)\). Factors construct and audit these inputs only.
Every tested method receives only \(N\), \(B\), and independent random bits.

| \(p,q\) | bits | \(B\) | method | successes | mean gcd calls | mean modular multiplications | median successful probe |
|---|---:|---:|---|---:|---:|---:|---:|
| 257, 419 | 17 | 289 | adaptive roots | 16/16 | 9.5625 | 44.875 | 9.5 |
|  |  |  | uniform gcd | 12/16 | 149.6875 | 0 | 94.5 |
|  |  |  | Pollard rho | 16/16 | 11.8125 | 35.4375 | 11.5 |
| 1031, 1657 | 21 | 441 | adaptive roots | 16/16 | 13.3125 | 97.125 | 13 |
|  |  |  | uniform gcd | 8/16 | 326.4375 | 0 | 239.5 |
|  |  |  | Pollard rho | 16/16 | 31.1875 | 93.5625 | 33.5 |
| 4099, 6563 | 25 | 512 | adaptive roots | 16/16 | 23.125 | 281.8125 | 24.5 |
|  |  |  | uniform gcd | 4/16 | 456.125 | 0 | 280 |
|  |  |  | Pollard rho | 16/16 | 42.5625 | 127.6875 | 39.5 |
| 16411, 26261 | 29 | 512 | adaptive roots | 16/16 | 29.3125 | 488.25 | 31.5 |
|  |  |  | uniform gcd | 1/16 | 488.3125 | 0 | 133 |
|  |  |  | Pollard rho | 16/16 | 94.875 | 284.625 | 96 |
| 65537, 104869 | 33 | 512 | adaptive roots | 16/16 | 54.75 | 1680.5625 | 55 |
|  |  |  | uniform gcd | 0/16 | 512 | 0 | -- |
|  |  |  | Pollard rho | 16/16 | 164 | 492 | 148 |
| 257, 65537 | 25 | 512 | adaptive roots | 16/16 | 9.375 | 50.0625 | 10 |
|  |  |  | uniform gcd | 13/16 | 244.4375 | 0 | 190 |
|  |  |  | Pollard rho | 16/16 | 13.8125 | 41.4375 | 14.5 |
| 1031, 262147 | 29 | 512 | adaptive roots | 16/16 | 15.0625 | 121.625 | 13.5 |
|  |  |  | uniform gcd | 5/16 | 429.3125 | 0 | 219 |
|  |  |  | Pollard rho | 16/16 | 35.25 | 105.75 | 37.5 |
| 4099, 1048583 | 33 | 512 | adaptive roots | 16/16 | 17.5 | 177.5625 | 16 |
|  |  |  | uniform gcd | 2/16 | 477.75 | 0 | 238 |
|  |  |  | Pollard rho | 16/16 | 55.875 | 167.625 | 47.5 |

Adaptive roots and rho each succeeded in all 128 finite trials. Uniform gcd
succeeded in 45. Every unsuccessful uniform trial and its budget censor is
retained. These fractions are exploratory finite observations. They supply
no lower bound on success for later inputs and no expected restart bound.

## Conditional finite-field population diagnostic

For each verified prime
\[
 p\in\{257,1031,4099,16411,65521\},
\]
the diagnostic initializes the complete image array \(H(x)=x\). At each
accepted update it chooses a seed uniformly from the indices with
\(H(x)\ne0\), sets \(a=H(x)\), and replaces every image value by
\[
 z\leftarrow z(z-a)\pmod p.
\]
If \(c(a)\) is the current image multiplicity and \(z_0=c(0)\), then the
chosen root has law \(c(a)/(p-z_0)\). The exact conditional expected increase
of the zero fraction is
\[
 \frac{\sum_{a\ne0}c(a)^2}{p(p-z_0)}. \tag{1}
\]
Every selected stage retains the numerator and denominator in (1), \(z_0\),
\(\sum_ac(a)^2\), nonzero support size, selected-root multiplicity, and
elapsed time. Every update asserts exactly
\[
 z_{0,\mathrm{next}}=z_0+c(a).
\]

| \(p\) | four completed-update counts | stop status | final \(z_0\) range | final nonzero-support range |
|---:|---|---|---:|---:|
| 257 | 31, 33, 32, 29 | all whole-field zero | 257 | 0 |
| 1031 | 64, 64, 65, 59 | all whole-field zero | 1031 | 0 |
| 4099 | 132, 135, 139, 130 | all whole-field zero | 4099 | 0 |
| 16411 | 256, 256, 256, 256 | update cap | 16105--16299 | 12--22 |
| 65521 | 256, 256, 256, 256 | update cap | 27711--29564 | 398--416 |

The field process conditions on a nonzero current image and samples according
to image multiplicity. It is not the distribution of public composite trials
conditioned on all earlier gcd failures unless a separate survival-weighting
identity is proved. The finite collapse pattern is not transferred to the
public algorithm.

## Resources and evidence

The public stage took 0.017654 seconds and 25,886,720 bytes peak RSS. The
field stage took 0.436121 seconds and 39,141,376 bytes peak RSS. Each ran as
one process under a separate internal 28-second alarm, external 30-second
timeout, and 512 MiB ceiling.

Evidence:
composite_pilot.py, composite_output.json, composite_status.json,
composite_run.log, field_population.py, field_output.json, field_status.json,
field_run.log, RESOURCE.md, and SHA256SUMS.txt.
