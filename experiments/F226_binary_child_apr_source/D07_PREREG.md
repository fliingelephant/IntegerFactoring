# F226-D07 preregistration — exact random-multiplier repair rate

Take exactly the 54 D06 rows whose deterministic lower-half prefix bank has
no locally accepted auxiliary prime.  For each row put `m=floor(n/2)` and
enumerate every odd `R` in `[1,2^m)`.  Because multiplication by odd `N`
permutes the odd residues modulo `2^m`, this is the exact distribution of

`R=u*N mod 2^m`

for a uniform odd multiplier `u`.

For each `R`, use all distinct prefixes `R mod 2^j`, `2<=j<=m`.  Gcd-screen
their prime factors against `N`.  Otherwise compute the ideal-oracle local
orbit records using the known factor `p`, and compute the largest exact
generalized-CRT-compatible product with exponent lcm at most `n^4`, as in
D06.  Count a success when a gcd is proper or that product reaches
`ceil(N^(1/4))`.

Record the exact numerator and denominator for every input.  This measures
the best-case source density after granting local orbit labels.  It does not
claim that APR/CL supplies those labels and does not prove an asymptotic
lower bound.

One local SageMath process.  Runtime cap: 300 seconds.  Expected runtime:
under 90 seconds.  Expected peak memory: under 600 MiB.  Output:
`D07_OUTPUT.json`; log: `logs/F226-D07.log`.

