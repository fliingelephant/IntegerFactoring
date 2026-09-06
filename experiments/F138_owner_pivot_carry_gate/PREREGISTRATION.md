# F138 preregistration — universe-private owner pivot

## Purpose

Test one necessary part of the proposed full-source closure claim:

> Every prime-parity pivot created by the adaptive F130/F132/F133 source is
> eventually reused by an old column or a different anchored star.

The test uses a fixed, balanced, trial-hard semiprime. Its seed-2 exact value
has a prime row that is private in the complete canonical-inverse universe.
If the arithmetic checks pass, no canonical adaptive extension can reuse
that row.

This does not test whether other columns give a factor or a P66 dependency.
It is not a complete-source failure claim.

## Fixed integers

```text
p = 1045051789228925522286798994428155162483171043575427210769649
q = 1554444160139607735219235490867513970584901047572020145318529
N = 1624474650810351494674724672626447596101101292465081710399215356070170241230595297993492854704406556802940436598350526321
r = 812237325405175747337362336313223798050550646232540855199607678035085120615297648996746427352203278401470218299175263161
```

## Required exact checks

1. `p`, `q`, and `r` are prime with proof-enabled Sage arithmetic.
2. `N = p*q = 2*r-1`, and `p < q < 2*p`.
3. With the exact F130 parameters
   \(n=\lceil\log_2(N+1)\rceil\),
   \(L=\lceil\log_2(n+1)\rceil\), and \(E=2^{L^2}\), the verifier gets
   `n=400`, `L=9`, and `E=2^81`.
4. Both factors exceed `(E+1)^2+1`. Therefore every initial F130 seed
   `2 <= s <= E+1` has null trial and endpoint-sign gcds. This conclusion is
   certified by the inequality, not by enumerating the seed bank.
5. `r=(N+1)/2` is the canonical inverse of `2`, and
   `P_N(2)=N+1=2*r` has odd `r`-valuation.
6. Since `r>(N-1)/2`, `r` is the only positive multiple of itself below
   `N`. The verifier checks the numerical inequalities used by the exact
   complete-universe privacy proof.

## Secondary exact certificate

Verify the four canonical values at `N=161`:

```text
(c,w,k) = (10,145,9), (26,31,5), (32,156,31), (87,124,67).
```

The selected endpoint sign screens must all be null. Their complete prime
valuation-parity matrix must have no degree-one row and must have full column
rank four. This certificate tests the separate inference

```text
all displayed rows reused  =>  nonzero binary kernel.
```

It is selected-source only. It does not control other endpoint presentations
or the complete adaptive source at `N=161`.

## Execution contract

- Verifier: `verify.sage`.
- Authoritative output: `OUTPUT.json`.
- Proof mode: Sage `is_prime(proof=True)`.
- Required result: every Boolean check is true.
- No durable project ledger is part of this experiment.

