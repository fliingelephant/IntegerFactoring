# Resource plan

The pilot uses one Python process with a 28-second internal alarm and a
30-second external timeout. Estimated runtime is below five seconds and
estimated peak memory is below 256 MiB. Small checks enumerate only through
R = 4096. Larger calls use polynomial-size odd-product expansions and
degree-two Euclidean floor moments, with no point enumeration.

The preflight reported 71 percent system-wide memory free, no swap I/O,
and load averages 1.95, 2.11, 2.18. The process snapshot showed suggestd
using one core and no large research process. No remote machine is used.
