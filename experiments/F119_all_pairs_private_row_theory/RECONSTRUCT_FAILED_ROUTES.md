# Failed proof routes and required corrections

## 1. Prescribing every carry independently modulo overlapping residues

The moduli `a^2*b` share base primes. Independent congruences for `N` modulo
these moduli need not be compatible. The reconstruction instead imposes the
single compatible condition `N = 1 mod L`. It then gets the explicit carry
`k = a^2*b - 1` for every pair.

## 2. Using arbitrary integer bases

Products `a^2*b` can collide when the bases are composite. Distinct prime
bases make the exponent-two and exponent-one roles recoverable by unique
factorization.

## 3. Forcing only divisibility by a protected prime

A congruence modulo `r` does not prove valuation one. The CRT condition must
be imposed modulo `r^2`. The residue

```text
N = (r-1)*k^(-1) mod r^2
```

gives `1+k*N = r mod r^2` and therefore exact valuation one.

## 4. Treating distinct protected primes as automatically private

Distinctness of the primes is insufficient. One protected prime could divide
several selected values. Choosing every `r` above the full selected carry
diameter and using the unique carry residue class modulo `r` prevents this.

## 5. Using only Dirichlet's theorem for the semiprime factors

Dirichlet gives existence but no upper bound for the chosen primes. Without
an upper bound, the required relation between `t` and the bit length is not
proved. Linnik's theorem supplies `p,q <= C*Q^lambda`.

## 6. Proving only an upper bound on the bit length

Linnik alone gives `log N = O(log Q)`. The lower bound comes from choosing
`p = 1 mod Q`, which forces `p > Q`. Together these bounds give
`log N = Theta(log Q)`.

## 7. Making only one semiprime factor large

The condition `p > Q` says nothing by itself about `q`. The shared condition
`q = 1 mod L` forces `q >= L+1`, which is larger than `n^2` for large `t`.

## 8. Omitting parity from the CRT modulus

Congruences modulo an odd modulus do not force both progression primes to be
odd. Including the modulus two and prescribing residue one makes both classes
odd.

## 9. Counting the two menu orientations incorrectly

There are `t choose 2` unordered base pairs but two exponent-two
orientations. They give exactly `t(t-1)` ordered products. Counting only the
unordered pairs loses a factor of two.

## 10. Inferring a dependency from many private rows

Private rows make columns independent. They obstruct dependencies in the
selected submatrix. They do not produce a square relation.

## 11. Extending submatrix privacy to the complete source

The carry-diameter argument covers only the selected carry set. Other seed,
frozen, or all-pairs values can lie in the same protected residue class and
reuse a row. Full-source privacy requires a new global avoidance statement.

## 12. Transferring sign screens through exact-value equality

The sign screens use `gcd(d^2-1,N)` and `gcd(d^2+1,N)` for the actual residue
`d`. Two different residues can have the same exact value but different
screens. Only a repeated occurrence of the same canonical residue has the
same endpoints and the same screens.

## 13. Claiming the source reaches every named attempt

The construction proves the two sign gcds for each named residue. It does not
exclude a direct factor at an earlier, different residue. Therefore it cannot
assert that a stopping implementation reaches all named attempts.

## 14. Treating dependency existence as a factor

An exact square dependency gives a root of one modulo `N`. It factors a
distinct semiprime only when the root is non-global. A `+1` or `-1` root gives
no proper sign gcd.
