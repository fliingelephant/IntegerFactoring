# F148 preregistration — residual-kernel cross-ratio closure

## Question

Can two directed P128 containment cycles whose residual products have the
same rational square class give a factor certificate in a metric range that
P131's combined-product window does not cover?

## Frozen finite search

- Enumerate distinct odd-prime semiprimes `N=p*q` with `5 <= p < q <= 500`.
- For each `N`, enumerate nonsquare integers `d` with `2 <= d < N` and
  `gcd(d,N)=1`.
- Enumerate distinct positive roots `a < b < N` of `x^2 = d (mod N)` with
  `a+b<N` and with both `a^2>d`, `b^2>d`.
- Enumerate unit centers `u,v >= 2` with `u*d<N`, `v*d<N`.
- Form the two one-edge containment cycles

  `u*a^2 = k*N + u*d` and `v*b^2 = l*N + v*d`.

- Require every canonical endpoint gcd, inverse endpoint sign gcd, and
  anchor gcd to be null before the final combined dependency.
- Stop at the lexicographically first certificate under the loop order
  `(p,q,d,a,b,u,v)`.

## Outputs

The search will print the first complete certificate and verify:

1. both canonical/lifted P128 values;
2. the exact square product of the four selected values;
3. the normalized root and both final factors;
4. the smaller cross-ratio gcds `gcd(a-b,N)` and `gcd(a+b,N)`;
5. all preregistered direct screens.

This finite search is evidence of capability only. It cannot prove an
all-input source law or a success frequency.
