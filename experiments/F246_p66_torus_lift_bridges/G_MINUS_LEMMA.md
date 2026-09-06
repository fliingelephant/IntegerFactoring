# F246 exact lemma — the missing negative-identity screen

Let `N=pq` for distinct odd primes.  Let

`Y=(x,y)`

be a norm-one point in

`(Z/NZ)[w]/(w^2-D)`.

Define

`G_minus(Y)=gcd(N,x+1,y)`.

Then:

1. `G_minus(Y)` is a proper divisor of `N` exactly when `Y` is `-1` in
   exactly one hidden local torus.
2. `G_minus(Y)=N` exactly when `Y=-1` globally.
3. `G_minus(Y)=1` exactly when neither hidden local point is `-1`.

## Proof

For a hidden prime `r` in `{p,q}`, the point `Y` is `-1` modulo `r` exactly
when

`x=-1 mod r` and `y=0 mod r`.

This is exactly the condition that `r` divides `gcd(N,x+1,y)`.  The three
claims follow because `N` has exactly the two distinct prime factors `p`
and `q`.

## Algorithmic consequence

After a P208 powered point gives `G_plus(Y)=1`, compute `G_minus(Y)` before
declaring the trial null.  A proper value gives a verified factor.  A value
`N` certifies a global negative return.  A value 1 certifies a genuine
failure of both signed-return tests.

This screen strictly dominates the stated P208 first screen on individual
transcripts.  It does not give a lower bound on how often a negative local
return occurs.  It therefore does not repair the missing all-input word
source by itself.

