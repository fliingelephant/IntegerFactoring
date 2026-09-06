# F138 preregistration 3 — full-budget max-digit private row

## Purpose

Put the universe-private row at the maximum integer anchor and maximum carry
digit of the declared F133 source. The selected residue must lie beyond the
initial F130 seed interval.

## Fixed integers

```text
p = 1440575060366591719164812115423434185454445360021359262957569
q = 1531570574064344929935978281536186047620048484429603222323201
N = 2206342372188439231071704119788681118383639175630092611385003672288203658512531224766164082517129137765776226834467258369
r = 2206342372188439231071703663527772386250305539544495574654345939408069421197500116321867676177152627713145274674754869377
```

## Required checks

1. `p`, `q`, and `r` are prime with proof-enabled Sage arithmetic.
2. `N=p*q`, `p<q<2*p`, and the F130 parameters are
   `n=400`, `L=9`, `E=2^81`.
3. Put `a=E`, `c=2*E`, and `A=E-1`. Check `N=1 mod c` and

   ```text
   r = (1+(c-1)*N)/c.
   ```

4. Both factors exceed `c^2+1`. This also proves that the full initial seed
   bank has null trial and sign screens.
5. For base block `2`, check

   ```text
   w = (N+1)/2,
   H = w + A*N = a*r,
   c = a*2,
   inverse_mod(c,N) = r.
   ```

6. The anchor and digit are the largest declared values: `a=E`, `A=a-1`.
   Also `c>E+1`, so this residue is not an initial seed.
7. The exact value is `c*r=1+(c-1)*N`, both sign screens are one, and
   `r>(N-1)/2` occurs to valuation one. It is therefore private in the
   complete canonical exact-value universe.

## Scope

This is a guaranteed F133 integer-anchor position if execution reaches that
scan. It does not assert that its exact value was absent from all earlier
F130 word positions. It does not assert complete-source failure.

## Execution contract

- Verifier: `verify_qpoly_max_digit.sage`.
- Authoritative output: `OUTPUT_QPOLY_MAX_DIGIT.json`.
- Proof mode: Sage `is_prime(proof=True)`.
- Required result: all Boolean checks are true.

