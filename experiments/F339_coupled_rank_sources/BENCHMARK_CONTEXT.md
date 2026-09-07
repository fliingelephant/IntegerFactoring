# The retained small inputs have an immediate Fermat control

The three retained F337/F339 diagnostic inputs all factor at the very first
Fermat square test, using only N:

| N | ceil(sqrt(N)) | x^2-N | Verified factors |
| ---: | ---: | ---: | --- |
| 209 | 15 | 16=4^2 | 11, 19 |
| 1333 | 37 | 36=6^2 | 31, 43 |
| 10807 | 104 | 9=3^2 | 101, 107 |

These are exact arithmetic certificates. They leave all retained rank
probabilities and formula checks valid, but the observed high-success
cells do not establish a performance improvement over this cheap control.
No source parameter or frozen trial has been changed after observing it.

A scale study should therefore retain these cases as identity controls and
also include existing wider-gap balanced inputs, such as F321's public
ratio-1.6 family or the F328 scale corpus. Compute the first Fermat test
from N and keep all its actual successes. Factor labels may describe the
input family and audit outputs, but must not select a public sample or a
jump. Larger-input studies should use the public floor-sum sampler when
the full sorted array is too expensive; a sorting budget is not a runtime
requirement of the proposed Las Vegas procedure.
