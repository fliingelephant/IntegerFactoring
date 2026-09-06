# F138 preregistration 2 — literal max-digit anchored private row

## Purpose

Strengthen the first F138 certificate. The protected row must occur in a
literal nonzero F133 prime-anchor arm, not only in the seed-2 unary value.

## Fixed integers

```text
p = 1320008795989904748182462774062723291576584579927832140369037
q = 1483391727238122164760277073344336797129797980984686650045533
N = 1958090127852978830975606630525183532915462684425760907751271701246799901589218459681729024239617354885430788103473361721
r = 1631741773210815692479672192104319610762885570354800756459393084372333251324348716401440853533014462404525656752894468101
```

## Required exact checks

1. `p`, `q`, and `r` are prime in proof-enabled Sage arithmetic.
2. `N=p*q`, `p<q<2*p`, `N=1 mod 6`, and `r=(5*N+1)/6`.
3. The F130 parameters are `n=400`, `L=9`, and `E=2^81`.
4. Both factors exceed `(E+1)^2+1`. Thus the full initial F130 seed bank has
   no trial factor and no endpoint-sign factor.
5. For base block `q0=2`, its canonical inverse is
   `w0=(N+1)/2`. With prime anchor `ell=3`, the unique digit is the maximum
   possible digit `A=2`, and

   ```text
   H = w0 + 2*N = 3*r.
   ```

6. The literal anchored endpoints are `c=ell*q0=6` and `z=H/ell=r`.
   They are canonical, their exact value is `6*r=1+5*N`, and both endpoint
   sign screens are one.
7. `r>(N-1)/2` and has valuation one in the exact value. The exact
   complete-universe theorem therefore makes its row permanently private
   after global exact-value deduplication.

## Scope

The certificate refutes universal cancellation of max-digit owner pivots.
It does not claim that later source positions fail to factor `N`, or that the
rest of the final P66 matrix has zero kernel.

## Execution contract

- Verifier: `verify_nonzero_arm.sage`.
- Authoritative output: `OUTPUT_NONZERO_ARM.json`.
- Proof mode: Sage `is_prime(proof=True)`.
- Required result: every Boolean check is true.

