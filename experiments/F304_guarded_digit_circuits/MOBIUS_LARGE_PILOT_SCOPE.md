# Scope correction for `MOBIUS_LARGE_PILOT`

The preserved `MOBIUS_LARGE_PILOT` source, JSON, and log use `s=k`, hence
`L=2^k`, together with `N=9*2^k+1`. Those results are valid non-enumerative
one-map evaluations. They are not the original first-quotient patches for an
original modulus `M=2^k`, because that coupling requires `L=M/2=2^(k-1)`.

No value in the preserved artifacts is invalidated. Only their coupling to the
original modulus was overstated. `MOBIUS_ORIGINAL_K65_PILOT` records the
corrected original-input case with

```text
k=65, M=2^65, L=2^64, s=64,
N=9M+1, A=B=1, C=2, n=(N-1)/2.
```

The corrected pilot checks that the largest power of two not exceeding `N/8`
is `M`, that `S_00=L`, and that all degree-three row and column marginal
moments have their universal power-sum values. It does not independently
verify the large mixed moments.
